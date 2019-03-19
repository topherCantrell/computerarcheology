![Bank 12](GBZelda.jpg)

# Bank 12

>>> cpu Z80GB

>>> memoryTable ram 
[RAM Usage](RAMUse.md)

>>> memoryTable hard 
[Hardware Info](../Hardware.md)

```
4000: 03         INC     BC              
4001: 00         NOP                     
4002: 3F         CCF                     
4003: 01 3F 13   LD      BC,$133F        
4006: 7F         LD      A,A             
4007: 1F         RRA                     
4008: FF         RST     0X38            
4009: 31 FF 60   LD      SP,$60FF        
400C: FF         RST     0X38            
400D: 24         INC     H               
400E: 7F         LD      A,A             
400F: 26 7F      LD      H,$7F           
4011: 26 FF      LD      H,$FF           
4013: 22         LD      (HLI),A         
4014: FF         RST     0X38            
4015: 70         LD      (HL),B          
4016: FF         RST     0X38            
4017: 38 7F      JR      C,$4098         
4019: 1F         RRA                     
401A: 3F         CCF                     
401B: 13         INC     DE              
401C: 3F         CCF                     
401D: 01 03 00   LD      BC,$0003        
4020: BD         CP      L               
4021: 00         NOP                     
4022: FF         RST     0X38            
4023: 18 FF      JR      $4024           
4025: FF         RST     0X38            
4026: FF         RST     0X38            
4027: F3         DI                      
4028: FF         RST     0X38            
4029: F3         DI                      
402A: FF         RST     0X38            
402B: F3         DI                      
402C: FF         RST     0X38            
402D: 63         LD      H,E             
402E: FF         RST     0X38            
402F: 61         LD      H,C             
4030: FF         RST     0X38            
4031: 64         LD      H,H             
4032: FF         RST     0X38            
4033: 44         LD      B,H             
4034: FF         RST     0X38            
4035: 4C         LD      C,H             
4036: FF         RST     0X38            
4037: CC FF FF   CALL    Z,$FFFF         
403A: FF         RST     0X38            
403B: FF         RST     0X38            
403C: FF         RST     0X38            
403D: 18 BD      JR      $3FFC           
403F: 00         NOP                     
4040: C0         RET     NZ              
4041: 00         NOP                     
4042: FC         ???                     
4043: 80         ADD     A,B             
4044: FE C8      CP      $C8             
4046: FE FC      CP      $FC             
4048: FF         RST     0X38            
4049: E4         ???                     
404A: FF         RST     0X38            
404B: E6 FF      AND     $FF             
404D: C4 FE CC   CALL    NZ,$CCFE        
4050: FE CC      CP      $CC             
4052: FF         RST     0X38            
4053: FC         ???                     
4054: FF         RST     0X38            
4055: 9E         SBC     (HL)            
4056: FF         RST     0X38            
4057: 9C         SBC     H               
4058: FE F8      CP      $F8             
405A: FC         ???                     
405B: C8         RET     Z               
405C: FC         ???                     
405D: 80         ADD     A,B             
405E: C0         RET     NZ              
405F: 00         NOP                     
4060: 00         NOP                     
4061: 00         NOP                     
4062: 00         NOP                     
4063: 00         NOP                     
4064: 00         NOP                     
4065: 00         NOP                     
4066: 01 00 03   LD      BC,$0300        
4069: 00         NOP                     
406A: 0C         INC     C               
406B: 03         INC     BC              
406C: 13         INC     DE              
406D: 0C         INC     C               
406E: 27         DAA                     
406F: 18 2F      JR      $40A0           
4071: 10 5F      STOP    $5F             
4073: 20 5F      JR      NZ,$40D4        
4075: 20 5F      JR      NZ,$40D6        
4077: 20 CB      JR      NZ,$4044        
4079: 34         INC     (HL)            
407A: FF         RST     0X38            
407B: 00         NOP                     
407C: AF         XOR     A               
407D: 58         LD      E,B             
407E: B7         OR      A               
407F: 4F         LD      C,A             
4080: 07         RLCA                    
4081: 00         NOP                     
4082: 18 07      JR      $408B           
4084: 67         LD      H,A             
4085: 18 9F      JR      $4026           
4087: 60         LD      H,B             
4088: FF         RST     0X38            
4089: 00         NOP                     
408A: 3F         CCF                     
408B: C0         RET     NZ              
408C: EF         RST     0X28            
408D: 10 D7      STOP    $D7             
408F: 38 BF      JR      C,$4050         
4091: 78         LD      A,B             
4092: 7B         LD      A,E             
4093: FC         ???                     
4094: FB         EI                      
4095: FC         ???                     
4096: FB         EI                      
4097: 7C         LD      A,H             
4098: FB         EI                      
4099: 7C         LD      A,H             
409A: FF         RST     0X38            
409B: 78         LD      A,B             
409C: F7         RST     0X30            
409D: F8 EF      LDHL    SP,$EF          
409F: F0 FC      LD      A,($FC)         
40A1: 03         INC     BC              
40A2: 3F         CCF                     
40A3: 00         NOP                     
40A4: 1F         RRA                     
40A5: 00         NOP                     
40A6: 2E 1F      LD      L,$1F           
40A8: 5F         LD      E,A             
40A9: 3F         CCF                     
40AA: 5F         LD      E,A             
40AB: 3F         CCF                     
40AC: 43         LD      B,E             
40AD: 3F         CCF                     
40AE: 3B         DEC     SP              
40AF: 07         RLCA                    
40B0: 11 0F 09   LD      DE,$090F        
40B3: 07         RLCA                    
40B4: 04         INC     B               
40B5: 03         INC     BC              
40B6: 02         LD      (BC),A          
40B7: 01 01 00   LD      BC,$0001        
40BA: 00         NOP                     
40BB: 00         NOP                     
40BC: 00         NOP                     
40BD: 00         NOP                     
40BE: 00         NOP                     
40BF: 00         NOP                     
40C0: 3F         CCF                     
40C1: CC F9 1E   CALL    Z,$1EF9         
40C4: 37         SCF                     
40C5: DE EF      SBC     $EF             
40C7: DE F9      SBC     $F9             
40C9: DE E7      SBC     $E7             
40CB: DE 7F      SBC     $7F             
40CD: ED         ???                     
40CE: 8F         ADC     A,A             
40CF: 73         LD      (HL),E          
40D0: F7         RST     0X30            
40D1: 8F         ADC     A,A             
40D2: FF         RST     0X38            
40D3: FF         RST     0X38            
40D4: 7F         LD      A,A             
40D5: FF         RST     0X38            
40D6: 1E FF      LD      E,$FF           
40D8: 80         ADD     A,B             
40D9: 7F         LD      A,A             
40DA: 70         LD      (HL),B          
40DB: 0F         RRCA                    
40DC: 0E 01      LD      C,$01           
40DE: 01 00 F2   LD      BC,$F200        
40E1: 0D         DEC     C               
40E2: FF         RST     0X38            
40E3: 00         NOP                     
40E4: D9         RETI                    
40E5: 26 F1      LD      H,$F1           
40E7: 0E FB      LD      C,$FB           
40E9: 04         INC     B               
40EA: CE 31      ADC     $31             
40EC: CC 33 EC   CALL    Z,$EC33         
40EF: 13         INC     DE              
40F0: FF         RST     0X38            
40F1: 00         NOP                     
40F2: F0 0F      LD      A,($0F)         
40F4: E8 1F      ADD     SP,$1F          
40F6: FC         ???                     
40F7: FF         RST     0X38            
40F8: F0 FF      LD      A,($FF)         
40FA: 92         SUB     D               
40FB: FF         RST     0X38            
40FC: 9E         SBC     (HL)            
40FD: FF         RST     0X38            
40FE: F8 FF      LDHL    SP,$FF          
4100: 00         NOP                     
4101: 00         NOP                     
4102: 00         NOP                     
4103: 00         NOP                     
4104: 00         NOP                     
4105: 00         NOP                     
4106: 01 00 03   LD      BC,$0300        
4109: 00         NOP                     
410A: 0C         INC     C               
410B: 03         INC     BC              
410C: 13         INC     DE              
410D: 0C         INC     C               
410E: 27         DAA                     
410F: 18 2F      JR      $4140           
4111: 10 5F      STOP    $5F             
4113: 20 4F      JR      NZ,$4164        
4115: 30 7B      JR      NC,$4192        
4117: 04         INC     B               
4118: CF         RST     0X08            
4119: 30 FF      JR      NC,$411A        
411B: 10 AF      STOP    $AF             
411D: 58         LD      E,B             
411E: B7         OR      A               
411F: 4F         LD      C,A             
4120: 07         RLCA                    
4121: 00         NOP                     
4122: 18 07      JR      $412B           
4124: 67         LD      H,A             
4125: 18 9F      JR      $40C6           
4127: 60         LD      H,B             
4128: FF         RST     0X38            
4129: 00         NOP                     
412A: 3F         CCF                     
412B: C0         RET     NZ              
412C: CF         RST     0X08            
412D: 30 F7      JR      NC,$4126        
412F: 08 FF 00   LD      ($00FF),SP      
4132: FF         RST     0X38            
4133: 00         NOP                     
4134: FF         RST     0X38            
4135: 00         NOP                     
4136: FF         RST     0X38            
4137: 00         NOP                     
4138: 9F         SBC     A               
4139: 60         LD      H,B             
413A: F7         RST     0X30            
413B: 78         LD      A,B             
413C: F7         RST     0X30            
413D: F8 EF      LDHL    SP,$EF          
413F: F0 FC      LD      A,($FC)         
4141: 03         INC     BC              
4142: 7F         LD      A,A             
4143: 00         NOP                     
4144: B7         OR      A               
4145: 78         LD      A,B             
4146: BF         CP      A               
4147: 7F         LD      A,A             
4148: 47         LD      B,A             
4149: 3F         CCF                     
414A: 37         SCF                     
414B: 0F         RRCA                    
414C: 23         INC     HL              
414D: 1F         RRA                     
414E: 13         INC     DE              
414F: 0F         RRCA                    
4150: 11 0F 09   LD      DE,$090F        
4153: 07         RLCA                    
4154: 04         INC     B               
4155: 03         INC     BC              
4156: 02         LD      (BC),A          
4157: 01 01 00   LD      BC,$0001        
415A: 00         NOP                     
415B: 00         NOP                     
415C: 00         NOP                     
415D: 00         NOP                     
415E: 00         NOP                     
415F: 00         NOP                     
4160: 3F         CCF                     
4161: C3 FE 07   JP      $07FE           
4164: FD         ???                     
4165: 0F         RRCA                    
4166: 73         LD      (HL),E          
4167: EF         RST     0X28            
4168: FE EF      CP      $EF             
416A: F1         POP     AF              
416B: EF         RST     0X28            
416C: 6F         LD      L,A             
416D: F6 8F      OR      $8F             
416F: 71         LD      (HL),C          
4170: F7         RST     0X30            
4171: 8F         ADC     A,A             
4172: FF         RST     0X38            
4173: FF         RST     0X38            
4174: 7F         LD      A,A             
4175: FF         RST     0X38            
4176: 1E FF      LD      E,$FF           
4178: 80         ADD     A,B             
4179: 7F         LD      A,A             
417A: 70         LD      (HL),B          
417B: 0F         RRCA                    
417C: 0E 01      LD      C,$01           
417E: 01 00 07   LD      BC,$0700        
4181: 00         NOP                     
4182: 0B         DEC     BC              
4183: 04         INC     B               
4184: 17         RLA                     
4185: 08 2F 10   LD      ($102F),SP      
4188: 2E 10      LD      L,$10           
418A: 5E         LD      E,(HL)          
418B: 20 5E      JR      NZ,$41EB        
418D: 20 BF      JR      NZ,$414E        
418F: 40         LD      B,B             
4190: 9F         SBC     A               
4191: 60         LD      H,B             
4192: FF         RST     0X38            
4193: 00         NOP                     
4194: FF         RST     0X38            
4195: 00         NOP                     
4196: FF         RST     0X38            
4197: 00         NOP                     
4198: FF         RST     0X38            
4199: 00         NOP                     
419A: FD         ???                     
419B: 02         LD      (BC),A          
419C: FF         RST     0X38            
419D: 00         NOP                     
419E: F6 09      OR      $09             
41A0: F2         ???                     
41A1: 0D         DEC     C               
41A2: FF         RST     0X38            
41A3: 00         NOP                     
41A4: D9         RETI                    
41A5: 26 F1      LD      H,$F1           
41A7: 0E FB      LD      C,$FB           
41A9: 04         INC     B               
41AA: CE 31      ADC     $31             
41AC: CC 33 EC   CALL    Z,$EC33         
41AF: 13         INC     DE              
41B0: FF         RST     0X38            
41B1: 80         ADD     A,B             
41B2: 30 CF      JR      NC,$4183        
41B4: E8 DF      ADD     SP,$DF          
41B6: 3C         INC     A               
41B7: DF         RST     0X18            
41B8: F0 DF      LD      A,($DF)         
41BA: D2 BF 9E   JP      NC,$9EBF        
41BD: 7F         LD      A,A             
41BE: F8 FF      LDHL    SP,$FF          
41C0: F8 FF      LDHL    SP,$FF          
41C2: C8         RET     Z               
41C3: FF         RST     0X38            
41C4: C0         RET     NZ              
41C5: FF         RST     0X38            
41C6: 00         NOP                     
41C7: FF         RST     0X38            
41C8: 0F         RRCA                    
41C9: F0 70      LD      A,($70)         
41CB: 8F         ADC     A,A             
41CC: 81         ADD     A,C             
41CD: 7F         LD      A,A             
41CE: 87         ADD     A,A             
41CF: 78         LD      A,B             
41D0: 62         LD      H,D             
41D1: 3C         INC     A               
41D2: 52         LD      D,D             
41D3: 3C         INC     A               
41D4: 31 1E 29   LD      SP,$291E        
41D7: 1E 19      LD      E,$19           
41D9: 0E 15      LD      C,$15           
41DB: 0E 09      LD      C,$09           
41DD: 06 06      LD      B,$06           
41DF: 00         NOP                     
41E0: C0         RET     NZ              
41E1: 00         NOP                     
41E2: B8         CP      B               
41E3: C0         RET     NZ              
41E4: 44         LD      B,H             
41E5: F8 BE      LDHL    SP,$BE          
41E7: 7C         LD      A,H             
41E8: B2         OR      D               
41E9: 7C         LD      A,H             
41EA: CD 3E 5F   CALL    $5F3E           
41ED: BE         CP      (HL)            
41EE: 5F         LD      E,A             
41EF: BE         CP      (HL)            
41F0: 5D         LD      E,L             
41F1: BE         CP      (HL)            
41F2: 42         LD      B,D             
41F3: BC         CP      H               
41F4: DD         ???                     
41F5: 3E DD      LD      A,$DD           
41F7: 3E DD      LD      A,$DD           
41F9: 3E 42      LD      A,$42           
41FB: BC         CP      H               
41FC: 5D         LD      E,L             
41FD: BE         CP      (HL)            
41FE: DD         ???                     
41FF: 3E 60      LD      A,$60           
4201: 00         NOP                     
4202: B0         OR      B               
4203: 40         LD      B,B             
4204: B0         OR      B               
4205: 40         LD      B,B             
4206: B0         OR      B               
4207: 40         LD      B,B             
4208: B8         CP      B               
4209: 40         LD      B,B             
420A: BC         CP      H               
420B: 40         LD      B,B             
420C: BC         CP      H               
420D: 40         LD      B,B             
420E: BE         CP      (HL)            
420F: 40         LD      B,B             
4210: 9F         SBC     A               
4211: 60         LD      H,B             
4212: FF         RST     0X38            
4213: 00         NOP                     
4214: FF         RST     0X38            
4215: 00         NOP                     
4216: FF         RST     0X38            
4217: 00         NOP                     
4218: FF         RST     0X38            
4219: 00         NOP                     
421A: FD         ???                     
421B: 02         LD      (BC),A          
421C: FF         RST     0X38            
421D: 00         NOP                     
421E: F6 09      OR      $09             
4220: F8 FF      LDHL    SP,$FF          
4222: C8         RET     Z               
4223: FF         RST     0X38            
4224: C0         RET     NZ              
4225: FF         RST     0X38            
4226: 00         NOP                     
4227: FF         RST     0X38            
4228: 0F         RRCA                    
4229: F0 70      LD      A,($70)         
422B: 8F         ADC     A,A             
422C: 81         ADD     A,C             
422D: 7F         LD      A,A             
422E: 87         ADD     A,A             
422F: 78         LD      A,B             
4230: C2 7C C2   JP      NZ,$C27C        
4233: 7C         LD      A,H             
4234: C4 78 C4   CALL    NZ,$C478        
4237: 78         LD      A,B             
4238: C8         RET     Z               
4239: 70         LD      (HL),B          
423A: 88         ADC     A,B             
423B: 70         LD      (HL),B          
423C: 90         SUB     B               
423D: 60         LD      H,B             
423E: 60         LD      H,B             
423F: 00         NOP                     
4240: 00         NOP                     
4241: 00         NOP                     
4242: 03         INC     BC              
4243: 00         NOP                     
4244: 0C         INC     C               
4245: 03         INC     BC              
4246: 17         RLA                     
4247: 0F         RRCA                    
4248: 2F         CPL                     
4249: 1F         RRA                     
424A: 3F         CCF                     
424B: 1F         RRA                     
424C: 5F         LD      E,A             
424D: 3F         CCF                     
424E: 5F         LD      E,A             
424F: 3F         CCF                     
4250: 5F         LD      E,A             
4251: 3F         CCF                     
4252: 5F         LD      E,A             
4253: 3F         CCF                     
4254: 3F         CCF                     
4255: 1F         RRA                     
4256: 2F         CPL                     
4257: 1F         RRA                     
4258: 17         RLA                     
4259: 0F         RRCA                    
425A: 0C         INC     C               
425B: 03         INC     BC              
425C: 03         INC     BC              
425D: 00         NOP                     
425E: 00         NOP                     
425F: 00         NOP                     
4260: 00         NOP                     
4261: 00         NOP                     
4262: C0         RET     NZ              
4263: 00         NOP                     
4264: 30 C0      JR      NC,$4226        
4266: E8 F0      ADD     SP,$F0          
4268: F4         ???                     
4269: F8 FC      LDHL    SP,$FC          
426B: F8 FA      LDHL    SP,$FA          
426D: FC         ???                     
426E: FA FC FA   LD      A,($FAFC)       
4271: 8C         ADC     A,H             
4272: FA 04 EC   LD      A,($EC04)       
4275: 10 FC      STOP    $FC             
4277: 00         NOP                     
4278: F8 80      LDHL    SP,$80          
427A: 30 C0      JR      NC,$423C        
427C: C0         RET     NZ              
427D: 00         NOP                     
427E: 00         NOP                     
427F: 00         NOP                     
4280: 0F         RRCA                    
4281: 00         NOP                     
4282: 3F         CCF                     
4283: 0E 5F      LD      C,$5F           
4285: 2A         LD      A,(HLI)         
4286: 7F         LD      A,A             
4287: 2E 8E      LD      L,$8E           
4289: 71         LD      (HL),C          
428A: 80         ADD     A,B             
428B: 7F         LD      A,A             
428C: 95         SUB     L               
428D: 6E         LD      L,(HL)          
428E: 6F         LD      L,A             
428F: 1D         DEC     E               
4290: 1F         RRA                     
4291: 03         INC     BC              
4292: 1F         RRA                     
4293: 0B         DEC     BC              
4294: 1F         RRA                     
4295: 0D         DEC     C               
4296: 0F         RRCA                    
4297: 06 07      LD      B,$07           
4299: 00         NOP                     
429A: 01 00 00   LD      BC,$0000        
429D: 00         NOP                     
429E: 00         NOP                     
429F: 00         NOP                     
42A0: CC 00 3E   CALL    Z,$3E00         
42A3: CC 2F F6   CALL    Z,$F62F         
42A6: 57         LD      D,A             
42A7: BA         CP      D               
42A8: 4F         LD      C,A             
42A9: BA         CP      D               
42AA: 4B         LD      C,E             
42AB: BC         CP      H               
42AC: 82         ADD     A,D             
42AD: 7C         LD      A,H             
42AE: 82         ADD     A,D             
42AF: FC         ???                     
42B0: C2 FC C2   JP      NZ,$C2FC        
42B3: BC         CP      H               
42B4: C2 BC C4   JP      NZ,$C4BC        
42B7: 38 E4      JR      C,$429D         
42B9: D8         RET     C               
42BA: B8         CP      B               
42BB: E0 F0      LDFF00  ($F0),A         
42BD: 60         LD      H,B             
42BE: 70         LD      (HL),B          
42BF: 00         NOP                     
42C0: 1F         RRA                     
42C1: 00         NOP                     
42C2: 3F         CCF                     
42C3: 17         RLA                     
42C4: 3F         CCF                     
42C5: 05         DEC     B               
42C6: 5F         LD      E,A             
42C7: 37         SCF                     
42C8: 67         LD      H,A             
42C9: 38 40      JR      C,$430B         
42CB: 3F         CCF                     
42CC: 4A         LD      C,D             
42CD: 37         SCF                     
42CE: 37         SCF                     
42CF: 0E 1F      LD      C,$1F           
42D1: 00         NOP                     
42D2: 05         DEC     B               
42D3: 02         LD      (BC),A          
42D4: 07         RLCA                    
42D5: 02         LD      (BC),A          
42D6: 03         INC     BC              
42D7: 00         NOP                     
42D8: 01 00 01   LD      BC,$0100        
42DB: 00         NOP                     
42DC: 00         NOP                     
42DD: 00         NOP                     
42DE: 00         NOP                     
42DF: 00         NOP                     
42E0: D8         RET     C               
42E1: 00         NOP                     
42E2: BC         CP      H               
42E3: 58         LD      E,B             
42E4: BE         CP      (HL)            
42E5: 6C         LD      L,H             
42E6: BE         CP      (HL)            
42E7: 54         LD      D,H             
42E8: 2E D4      LD      L,$D4           
42EA: 26 D8      LD      H,$D8           
42EC: C2 3C E2   JP      NZ,$E23C        
42EF: DC 82 FC   CALL    C,$FC82         
42F2: D2 EC F4   JP      NC,$F4EC        
42F5: 68         LD      L,B             
42F6: E4         ???                     
42F7: 18 E8      JR      $42E1           
42F9: D0         RET     NC              
42FA: B0         OR      B               
42FB: E0 F0      LDFF00  ($F0),A         
42FD: 60         LD      H,B             
42FE: 70         LD      (HL),B          
42FF: 00         NOP                     
4300: 06 00      LD      B,$00           
4302: 0F         RRCA                    
4303: 06 0F      LD      B,$0F           
4305: 05         DEC     B               
4306: 0F         RRCA                    
4307: 06 16      LD      B,$16           
4309: 09         ADD     HL,BC           
430A: 11 0F 10   LD      DE,$100F        
430D: 0F         RRCA                    
430E: 0B         DEC     BC              
430F: 04         INC     B               
4310: 0C         INC     C               
4311: 03         INC     BC              
4312: 0F         RRCA                    
4313: 04         INC     B               
4314: 0D         DEC     C               
4315: 06 0B      LD      B,$0B           
4317: 04         INC     B               
4318: 07         RLCA                    
4319: 01 03 01   LD      BC,$0103        
431C: 02         LD      (BC),A          
431D: 01 01 00   LD      BC,$0001        
4320: 01 00 37   LD      BC,$3700        
4323: 01 7F 37   LD      BC,$377F        
4326: CF         RST     0X08            
4327: 77         LD      (HL),A          
4328: CF         RST     0X08            
4329: 7E         LD      A,(HL)          
432A: FE 6F      CP      $6F             
432C: 7C         LD      A,H             
432D: 1F         RRA                     
432E: 3F         CCF                     
432F: 1D         DEC     E               
4330: 3F         CCF                     
4331: 1D         DEC     E               
4332: 3D         DEC     A               
4333: 1E 2C      LD      E,$2C           
4335: 1F         RRA                     
4336: 1E 0F      LD      E,$0F           
4338: 3F         CCF                     
4339: 17         RLA                     
433A: 3D         DEC     A               
433B: 1B         DEC     DE              
433C: 1F         RRA                     
433D: 0C         INC     C               
433E: 0C         INC     C               
433F: 00         NOP                     
4340: F0 00      LD      A,($00)         
4342: C8         RET     Z               
4343: B0         OR      B               
4344: C8         RET     Z               
4345: B0         OR      B               
4346: C8         RET     Z               
4347: F0 C8      LD      A,($C8)         
4349: 30 E8      JR      NC,$4333        
434B: D0         RET     NC              
434C: 70         LD      (HL),B          
434D: E0 70      LDFF00  ($70),A         
434F: E0 E0      LDFF00  ($E0),A         
4351: C0         RET     NZ              
4352: CC 00 5E   CALL    Z,$5E00         
4355: 8C         ADC     A,H             
4356: 7F         LD      A,A             
4357: 9E         SBC     (HL)            
4358: 3F         CCF                     
4359: DE FF      SBC     $FF             
435B: DE FE      SBC     $FE             
435D: 0C         INC     C               
435E: 0C         INC     C               
435F: 00         NOP                     
4360: 00         NOP                     
4361: 00         NOP                     
4362: 00         NOP                     
4363: 00         NOP                     
4364: 00         NOP                     
4365: 00         NOP                     
4366: 00         NOP                     
4367: 00         NOP                     
4368: 03         INC     BC              
4369: 00         NOP                     
436A: 0F         RRCA                    
436B: 03         INC     BC              
436C: 1F         RRA                     
436D: 0A         LD      A,(BC)          
436E: 1F         RRA                     
436F: 0B         DEC     BC              
4370: 33         INC     SP              
4371: 1C         INC     E               
4372: 20 1F      JR      NZ,$4393        
4374: 24         INC     H               
4375: 1B         DEC     DE              
4376: 19         ADD     HL,DE           
4377: 07         RLCA                    
4378: 07         RLCA                    
4379: 00         NOP                     
437A: 00         NOP                     
437B: 00         NOP                     
437C: 00         NOP                     
437D: 00         NOP                     
437E: 00         NOP                     
437F: 00         NOP                     
4380: 00         NOP                     
4381: 00         NOP                     
4382: 00         NOP                     
4383: 00         NOP                     
4384: 1E 00      LD      E,$00           
4386: 3F         CCF                     
4387: 1E FF      LD      E,$FF           
4389: 00         NOP                     
438A: C0         RET     NZ              
438B: BF         CP      A               
438C: CC B3 DE   CALL    Z,$DEB3         
438F: AD         XOR     L               
4390: 9E         SBC     (HL)            
4391: 6D         LD      L,L             
4392: 7F         LD      A,A             
4393: DB         ???                     
4394: FF         RST     0X38            
4395: D7         RST     0X10            
4396: FD         ???                     
4397: BE         CP      (HL)            
4398: FF         RST     0X38            
4399: 00         NOP                     
439A: 00         NOP                     
439B: 00         NOP                     
439C: 00         NOP                     
439D: 00         NOP                     
439E: 00         NOP                     
439F: 00         NOP                     
43A0: 00         NOP                     
43A1: 00         NOP                     
43A2: 00         NOP                     
43A3: 00         NOP                     
43A4: 00         NOP                     
43A5: 00         NOP                     
43A6: 00         NOP                     
43A7: 00         NOP                     
43A8: 0E 00      LD      C,$00           
43AA: DE 0C      SBC     $0C             
43AC: 3E DC      LD      A,$DC           
43AE: 3E DC      LD      A,$DC           
43B0: FE DC      CP      $DC             
43B2: BE         CP      (HL)            
43B3: CC 4E 80   CALL    Z,$804E         
43B6: E0 C0      LDFF00  ($C0),A         
43B8: E0 00      LDFF00  ($00),A         
43BA: 00         NOP                     
43BB: 00         NOP                     
43BC: 00         NOP                     
43BD: 00         NOP                     
43BE: 00         NOP                     
43BF: 00         NOP                     
43C0: 00         NOP                     
43C1: 00         NOP                     
43C2: 00         NOP                     
43C3: 00         NOP                     
43C4: 00         NOP                     
43C5: 00         NOP                     
43C6: 00         NOP                     
43C7: 00         NOP                     
43C8: 03         INC     BC              
43C9: 00         NOP                     
43CA: 0F         RRCA                    
43CB: 03         INC     BC              
43CC: 1F         RRA                     
43CD: 0A         LD      A,(BC)          
43CE: 37         SCF                     
43CF: 1B         DEC     DE              
43D0: 23         INC     HL              
43D1: 1C         INC     E               
43D2: 20 1F      JR      NZ,$43F3        
43D4: 3C         INC     A               
43D5: 03         INC     BC              
43D6: 05         DEC     B               
43D7: 03         INC     BC              
43D8: 05         DEC     B               
43D9: 02         LD      (BC),A          
43DA: 07         RLCA                    
43DB: 00         NOP                     
43DC: 00         NOP                     
43DD: 00         NOP                     
43DE: 00         NOP                     
43DF: 00         NOP                     
43E0: 00         NOP                     
43E1: 00         NOP                     
43E2: 00         NOP                     
43E3: 00         NOP                     
43E4: 00         NOP                     
43E5: 00         NOP                     
43E6: 00         NOP                     
43E7: 00         NOP                     
43E8: 0C         INC     C               
43E9: 00         NOP                     
43EA: DC 08 3C   CALL    C,$3C08         
43ED: D8         RET     C               
43EE: 3C         INC     A               
43EF: D8         RET     C               
43F0: FC         ???                     
43F1: D8         RET     C               
43F2: BC         CP      H               
43F3: C8         RET     Z               
43F4: 4C         LD      C,H             
43F5: 80         ADD     A,B             
43F6: E0 C0      LDFF00  ($C0),A         
43F8: E0 00      LDFF00  ($00),A         
43FA: 00         NOP                     
43FB: 00         NOP                     
43FC: 00         NOP                     
43FD: 00         NOP                     
43FE: 00         NOP                     
43FF: 00         NOP                     
4400: 1C         INC     E               
4401: 00         NOP                     
4402: 3E 1C      LD      A,$1C           
4404: 37         SCF                     
4405: 0E 0B      LD      C,$0B           
4407: 06 0B      LD      B,$0B           
4409: 04         INC     B               
440A: 0F         RRCA                    
440B: 07         RLCA                    
440C: 1F         RRA                     
440D: 0B         DEC     BC              
440E: 1F         RRA                     
440F: 0B         DEC     BC              
4410: 2F         CPL                     
4411: 19         ADD     HL,DE           
4412: 2F         CPL                     
4413: 1F         RRA                     
4414: 17         RLA                     
4415: 0F         RRCA                    
4416: 3F         CCF                     
4417: 10 3F      STOP    $3F             
4419: 17         RLA                     
441A: 1B         DEC     DE              
441B: 07         RLCA                    
441C: 1D         DEC     E               
441D: 0E 1F      LD      C,$1F           
441F: 00         NOP                     
4420: 60         LD      H,B             
4421: 00         NOP                     
4422: F0 60      LD      A,($60)         
4424: 90         SUB     B               
4425: E0 A0      LDFF00  ($A0),A         
4427: C0         RET     NZ              
4428: A0         AND     B               
4429: C0         RET     NZ              
442A: E0 C0      LDFF00  ($C0),A         
442C: F0 60      LD      A,($60)         
442E: F8 60      LDHL    SP,$60          
4430: E8 F0      ADD     SP,$F0          
4432: C8         RET     Z               
4433: F0 F0      LD      A,($F0)         
4435: 80         ADD     A,B             
4436: F0 60      LD      A,($60)         
4438: F0 60      LD      A,($60)         
443A: F0 80      LD      A,($80)         
443C: 78         LD      A,B             
443D: F0 F8      LD      A,($F8)         
443F: 00         NOP                     
4440: 06 00      LD      B,$00           
4442: 0F         RRCA                    
4443: 06 0F      LD      B,$0F           
4445: 07         RLCA                    
4446: 07         RLCA                    
4447: 03         INC     BC              
4448: 07         RLCA                    
4449: 03         INC     BC              
444A: 07         RLCA                    
444B: 03         INC     BC              
444C: 0F         RRCA                    
444D: 07         RLCA                    
444E: 1F         RRA                     
444F: 0F         RRCA                    
4450: 1F         RRA                     
4451: 0F         RRCA                    
4452: 17         RLA                     
4453: 0F         RRCA                    
4454: 0B         DEC     BC              
4455: 04         INC     B               
4456: 1F         RRA                     
4457: 0B         DEC     BC              
4458: 17         RLA                     
4459: 0B         DEC     BC              
445A: 0F         RRCA                    
445B: 04         INC     B               
445C: 1E 0F      LD      E,$0F           
445E: 1F         RRA                     
445F: 00         NOP                     
4460: 38 00      JR      C,$4462         
4462: 7C         LD      A,H             
4463: 38 FC      JR      C,$4461         
4465: 70         LD      (HL),B          
4466: F0 60      LD      A,($60)         
4468: F0 60      LD      A,($60)         
446A: F0 E0      LD      A,($E0)         
446C: F8 F0      LDHL    SP,$F0          
446E: F8 F0      LDHL    SP,$F0          
4470: F4         ???                     
4471: F8 F4      LDHL    SP,$F4          
4473: F8 E8      LDHL    SP,$E8          
4475: 70         LD      (HL),B          
4476: FC         ???                     
4477: B8         CP      B               
4478: F4         ???                     
4479: B8         CP      B               
447A: F8 60      LDHL    SP,$60          
447C: F8 70      LDHL    SP,$70          
447E: F8 00      LDHL    SP,$00          
4480: 77         LD      (HL),A          
4481: 00         NOP                     
4482: 7F         LD      A,A             
4483: 36 2D      LD      (HL),$2D        
4485: 1B         DEC     DE              
4486: 15         DEC     D               
4487: 0B         DEC     BC              
4488: 0D         DEC     C               
4489: 03         INC     BC              
448A: 1F         RRA                     
448B: 0F         RRCA                    
448C: 1F         RRA                     
448D: 0B         DEC     BC              
448E: 3F         CCF                     
448F: 1B         DEC     DE              
4490: 7F         LD      A,A             
4491: 0F         RRCA                    
4492: 7F         LD      A,A             
4493: 3F         CCF                     
4494: 5D         LD      E,L             
4495: 3E 3F      LD      A,$3F           
4497: 01 07 01   LD      BC,$0107        
449A: 07         RLCA                    
449B: 00         NOP                     
449C: 07         RLCA                    
449D: 03         INC     BC              
449E: 0F         RRCA                    
449F: 00         NOP                     
44A0: 00         NOP                     
44A1: 00         NOP                     
44A2: 80         ADD     A,B             
44A3: 00         NOP                     
44A4: 80         ADD     A,B             
44A5: 00         NOP                     
44A6: 80         ADD     A,B             
44A7: 00         NOP                     
44A8: 80         ADD     A,B             
44A9: 00         NOP                     
44AA: C0         RET     NZ              
44AB: 00         NOP                     
44AC: E0 C0      LDFF00  ($C0),A         
44AE: D0         RET     NC              
44AF: E0 D0      LDFF00  ($D0),A         
44B1: E0 A0      LDFF00  ($A0),A         
44B3: C0         RET     NZ              
44B4: 78         LD      A,B             
44B5: E0 DC      LDFF00  ($DC),A         
44B7: E8 BC      ADD     SP,$BC          
44B9: C8         RET     Z               
44BA: D8         RET     C               
44BB: 20 F0      JR      NZ,$44AD        
44BD: E0 F0      LDFF00  ($F0),A         
44BF: 00         NOP                     
44C0: 00         NOP                     
44C1: 00         NOP                     
44C2: 00         NOP                     
44C3: 00         NOP                     
44C4: 00         NOP                     
44C5: 00         NOP                     
44C6: 00         NOP                     
44C7: 00         NOP                     
44C8: 00         NOP                     
44C9: 00         NOP                     
44CA: 00         NOP                     
44CB: 00         NOP                     
44CC: 1C         INC     E               
44CD: 00         NOP                     
44CE: 3E 14      LD      A,$14           
44D0: 3E 00      LD      A,$00           
44D2: 24         INC     H               
44D3: 00         NOP                     
44D4: 00         NOP                     
44D5: 00         NOP                     
44D6: 00         NOP                     
44D7: 00         NOP                     
44D8: 00         NOP                     
44D9: 00         NOP                     
44DA: 00         NOP                     
44DB: 00         NOP                     
44DC: 00         NOP                     
44DD: 00         NOP                     
44DE: 00         NOP                     
44DF: 00         NOP                     
44E0: 00         NOP                     
44E1: 00         NOP                     
44E2: 00         NOP                     
44E3: 00         NOP                     
44E4: 00         NOP                     
44E5: 00         NOP                     
44E6: 00         NOP                     
44E7: 00         NOP                     
44E8: C3 00 E7   JP      $E700           
44EB: 42         LD      B,D             
44EC: FF         RST     0X38            
44ED: 66         LD      H,(HL)          
44EE: FF         RST     0X38            
44EF: 66         LD      H,(HL)          
44F0: 7E         LD      A,(HL)          
44F1: 24         INC     H               
44F2: 3C         INC     A               
44F3: 00         NOP                     
44F4: 00         NOP                     
44F5: 00         NOP                     
44F6: 00         NOP                     
44F7: 00         NOP                     
44F8: 00         NOP                     
44F9: 00         NOP                     
44FA: 00         NOP                     
44FB: 00         NOP                     
44FC: 00         NOP                     
44FD: 00         NOP                     
44FE: 00         NOP                     
44FF: 00         NOP                     
4500: 07         RLCA                    
4501: 00         NOP                     
4502: 18 07      JR      $450B           
4504: 26 19      LD      H,$19           
4506: 27         DAA                     
4507: 1A         LD      A,(DE)          
4508: 4F         LD      C,A             
4509: 33         INC     SP              
450A: 5F         LD      E,A             
450B: 2B         DEC     HL              
450C: 3F         CCF                     
450D: 0F         RRCA                    
450E: 1F         RRA                     
450F: 0D         DEC     C               
4510: 17         RLA                     
4511: 0D         DEC     C               
4512: 2B         DEC     HL              
4513: 17         RLA                     
4514: 2F         CPL                     
4515: 10 3F      STOP    $3F             
4517: 0D         DEC     C               
4518: 1F         RRA                     
4519: 0D         DEC     C               
451A: 1D         DEC     E               
451B: 02         LD      (BC),A          
451C: 17         RLA                     
451D: 0F         RRCA                    
451E: 1F         RRA                     
451F: 00         NOP                     
4520: C0         RET     NZ              
4521: 00         NOP                     
4522: 20 C0      JR      NZ,$44E4        
4524: 1C         INC     E               
4525: E0 82      LDFF00  ($82),A         
4527: 7C         LD      A,H             
4528: D2 2C FA   JP      NC,$FA2C        
452B: 54         LD      D,H             
452C: FC         ???                     
452D: D0         RET     NC              
452E: EA F4 B2   LD      ($B2F4),A       
4531: CC 61 9E   CALL    Z,$9E61         
4534: D1         POP     DE              
4535: 2E D1      LD      L,$D1           
4537: AE         XOR     (HL)            
4538: D2 AC 8C   JP      NC,$8CAC        
453B: 70         LD      (HL),B          
453C: 88         ADC     A,B             
453D: F0 F8      LD      A,($F8)         
453F: 00         NOP                     
4540: 07         RLCA                    
4541: 00         NOP                     
4542: 08 07 31   LD      ($3107),SP      
4545: 0E 43      LD      C,$43           
4547: 3D         DEC     A               
4548: 57         LD      D,A             
4549: 29         ADD     HL,HL           
454A: 7F         LD      A,A             
454B: 15         DEC     D               
454C: 3F         CCF                     
454D: 17         RLA                     
454E: 5F         LD      E,A             
454F: 2F         CPL                     
4550: 8B         ADC     A,E             
4551: 77         LD      (HL),A          
4552: 85         ADD     A,L             
4553: 7B         LD      A,E             
4554: 87         ADD     A,A             
4555: 78         LD      A,B             
4556: 4F         LD      C,A             
4557: 36 3F      LD      (HL),$3F        
4559: 06 16      LD      B,$16           
455B: 09         ADD     HL,BC           
455C: 13         INC     DE              
455D: 0F         RRCA                    
455E: 1F         RRA                     
455F: 00         NOP                     
4560: 00         NOP                     
4561: FF         RST     0X38            
4562: 00         NOP                     
4563: FF         RST     0X38            
4564: 22         LD      (HLI),A         
4565: FF         RST     0X38            
4566: 14         INC     D               
4567: FF         RST     0X38            
4568: 08 FF 14   LD      ($14FF),SP      
456B: FF         RST     0X38            
456C: 22         LD      (HLI),A         
456D: FF         RST     0X38            
456E: 00         NOP                     
456F: FF         RST     0X38            
4570: 00         NOP                     
4571: FF         RST     0X38            
4572: 00         NOP                     
4573: FF         RST     0X38            
4574: 22         LD      (HLI),A         
4575: FF         RST     0X38            
4576: 14         INC     D               
4577: FF         RST     0X38            
4578: 08 FF 14   LD      ($14FF),SP      
457B: FF         RST     0X38            
457C: 22         LD      (HLI),A         
457D: FF         RST     0X38            
457E: 00         NOP                     
457F: FF         RST     0X38            
4580: 77         LD      (HL),A          
4581: 00         NOP                     
4582: 7F         LD      A,A             
4583: 36 2D      LD      (HL),$2D        
4585: 1B         DEC     DE              
4586: 15         DEC     D               
4587: 0B         DEC     BC              
4588: 0D         DEC     C               
4589: 03         INC     BC              
458A: 1F         RRA                     
458B: 0F         RRCA                    
458C: 1F         RRA                     
458D: 0B         DEC     BC              
458E: 3F         CCF                     
458F: 1B         DEC     DE              
4590: 7F         LD      A,A             
4591: 0F         RRCA                    
4592: 7F         LD      A,A             
4593: 3F         CCF                     
4594: 5D         LD      E,L             
4595: 3E 3F      LD      A,$3F           
4597: 01 07 01   LD      BC,$0107        
459A: 07         RLCA                    
459B: 00         NOP                     
459C: 07         RLCA                    
459D: 03         INC     BC              
459E: 0F         RRCA                    
459F: 00         NOP                     
45A0: 00         NOP                     
45A1: 00         NOP                     
45A2: 80         ADD     A,B             
45A3: 00         NOP                     
45A4: 80         ADD     A,B             
45A5: 00         NOP                     
45A6: 80         ADD     A,B             
45A7: 00         NOP                     
45A8: 80         ADD     A,B             
45A9: 00         NOP                     
45AA: C0         RET     NZ              
45AB: 00         NOP                     
45AC: E0 C0      LDFF00  ($C0),A         
45AE: D0         RET     NC              
45AF: E0 D0      LDFF00  ($D0),A         
45B1: E0 A0      LDFF00  ($A0),A         
45B3: C0         RET     NZ              
45B4: 78         LD      A,B             
45B5: E0 DC      LDFF00  ($DC),A         
45B7: E8 BC      ADD     SP,$BC          
45B9: C8         RET     Z               
45BA: D8         RET     C               
45BB: 20 F0      JR      NZ,$45AD        
45BD: E0 F0      LDFF00  ($F0),A         
45BF: 00         NOP                     
45C0: 3C         INC     A               
45C1: 00         NOP                     
45C2: 3E 1C      LD      A,$1C           
45C4: 17         RLA                     
45C5: 0E 0B      LD      C,$0B           
45C7: 06 0F      LD      B,$0F           
45C9: 02         LD      (BC),A          
45CA: 1F         RRA                     
45CB: 0F         RRCA                    
45CC: 1F         RRA                     
45CD: 07         RLCA                    
45CE: 3F         CCF                     
45CF: 17         RLA                     
45D0: 7F         LD      A,A             
45D1: 1F         RRA                     
45D2: 7F         LD      A,A             
45D3: 3F         CCF                     
45D4: 5A         LD      E,D             
45D5: 3D         DEC     A               
45D6: 3F         CCF                     
45D7: 03         INC     BC              
45D8: 07         RLCA                    
45D9: 03         INC     BC              
45DA: 0F         RRCA                    
45DB: 00         NOP                     
45DC: 19         ADD     HL,DE           
45DD: 0E 1F      LD      C,$1F           
45DF: 00         NOP                     
45E0: 00         NOP                     
45E1: 00         NOP                     
45E2: 00         NOP                     
45E3: 00         NOP                     
45E4: 00         NOP                     
45E5: 00         NOP                     
45E6: 00         NOP                     
45E7: 00         NOP                     
45E8: 00         NOP                     
45E9: 00         NOP                     
45EA: 80         ADD     A,B             
45EB: 00         NOP                     
45EC: C0         RET     NZ              
45ED: 80         ADD     A,B             
45EE: A0         AND     B               
45EF: C0         RET     NZ              
45F0: A0         AND     B               
45F1: C0         RET     NZ              
45F2: C0         RET     NZ              
45F3: 80         ADD     A,B             
45F4: EC         ???                     
45F5: C0         RET     NZ              
45F6: 9E         SBC     (HL)            
45F7: EC         ???                     
45F8: 7E         LD      A,(HL)          
45F9: B4         OR      H               
45FA: AC         XOR     H               
45FB: 70         LD      (HL),B          
45FC: D8         RET     C               
45FD: E0 F0      LDFF00  ($F0),A         
45FF: 00         NOP                     
4600: 05         DEC     B               
4601: 00         NOP                     
4602: 07         RLCA                    
4603: 00         NOP                     
4604: 0D         DEC     C               
4605: 02         LD      (BC),A          
4606: 0B         DEC     BC              
4607: 04         INC     B               
4608: 0F         RRCA                    
4609: 00         NOP                     
460A: 1F         RRA                     
460B: 0C         INC     C               
460C: 3F         CCF                     
460D: 0D         DEC     C               
460E: 79         LD      A,C             
460F: 3E C7      LD      A,$C7           
4611: 78         LD      A,B             
4612: E9         JP      (HL)            
4613: 56         LD      D,(HL)          
4614: 8B         ADC     A,E             
4615: 75         LD      (HL),L          
4616: 5F         LD      E,A             
4617: 21 31 00   LD      HL,$0031        
461A: 03         INC     BC              
461B: 01 07 02   LD      BC,$0207        
461E: 07         RLCA                    
461F: 00         NOP                     
4620: F0 00      LD      A,($00)         
4622: F0 00      LD      A,($00)         
4624: E0 00      LDFF00  ($00),A         
4626: F0 00      LD      A,($00)         
4628: F0 80      LD      A,($80)         
462A: E8 90      ADD     SP,$90          
462C: 54         LD      D,H             
462D: B8         CP      B               
462E: CC 38 CA   CALL    Z,$CA38         
4631: 3C         INC     A               
4632: C6 BC      ADD     $BC             
4634: E7         RST     0X20            
4635: DC F3 CC   CALL    C,$CCF3         
4638: 5E         LD      E,(HL)          
4639: A0         AND     B               
463A: CC 70 A8   CALL    Z,$A870         
463D: D0         RET     NC              
463E: F8 00      LDHL    SP,$00          
4640: 30 00      JR      NC,$4642        
4642: 3D         DEC     A               
4643: 10 3F      STOP    $3F             
4645: 18 2D      JR      $4674           
4647: 1A         LD      A,(DE)          
4648: 1B         DEC     DE              
4649: 04         INC     B               
464A: 1F         RRA                     
464B: 00         NOP                     
464C: 1F         RRA                     
464D: 0C         INC     C               
464E: 3F         CCF                     
464F: 0D         DEC     C               
4650: 79         LD      A,C             
4651: 3E C7      LD      A,$C7           
4653: 78         LD      A,B             
4654: E9         JP      (HL)            
4655: 56         LD      D,(HL)          
4656: 8B         ADC     A,E             
4657: 75         LD      (HL),L          
4658: 5D         LD      E,L             
4659: 23         INC     HL              
465A: 33         INC     SP              
465B: 00         NOP                     
465C: 07         RLCA                    
465D: 02         LD      (BC),A          
465E: 07         RLCA                    
465F: 00         NOP                     
4660: 03         INC     BC              
4661: 00         NOP                     
4662: E5         PUSH    HL              
4663: 02         LD      (BC),A          
4664: E9         JP      (HL)            
4665: 06 D5      LD      B,$D5           
4667: 0E EF      LD      C,$EF           
4669: 1E FD      LD      E,$FD           
466B: 9E         SBC     (HL)            
466C: DA BC 5A   JP      C,$5ABC         
466F: BC         CP      H               
4670: E4         ???                     
4671: 18 F8      JR      $466B           
4673: 00         NOP                     
4674: FE 80      CP      $80             
4676: FF         RST     0X38            
4677: C0         RET     NZ              
4678: DE A0      SBC     $A0             
467A: CC 70 A8   CALL    Z,$A870         
467D: D0         RET     NC              
467E: F8 00      LDHL    SP,$00          
4680: 00         NOP                     
4681: FF         RST     0X38            
4682: 00         NOP                     
4683: FF         RST     0X38            
4684: 22         LD      (HLI),A         
4685: FF         RST     0X38            
4686: 14         INC     D               
4687: FF         RST     0X38            
4688: 08 FF 14   LD      ($14FF),SP      
468B: FF         RST     0X38            
468C: 22         LD      (HLI),A         
468D: FF         RST     0X38            
468E: 00         NOP                     
468F: FF         RST     0X38            
4690: 00         NOP                     
4691: FF         RST     0X38            
4692: 00         NOP                     
4693: FF         RST     0X38            
4694: 22         LD      (HLI),A         
4695: FF         RST     0X38            
4696: 14         INC     D               
4697: FF         RST     0X38            
4698: 08 FF 14   LD      ($14FF),SP      
469B: FF         RST     0X38            
469C: 22         LD      (HLI),A         
469D: FF         RST     0X38            
469E: 00         NOP                     
469F: FF         RST     0X38            
46A0: 00         NOP                     
46A1: FF         RST     0X38            
46A2: 00         NOP                     
46A3: FF         RST     0X38            
46A4: 22         LD      (HLI),A         
46A5: FF         RST     0X38            
46A6: 14         INC     D               
46A7: FF         RST     0X38            
46A8: 08 FF 14   LD      ($14FF),SP      
46AB: FF         RST     0X38            
46AC: 22         LD      (HLI),A         
46AD: FF         RST     0X38            
46AE: 00         NOP                     
46AF: FF         RST     0X38            
46B0: 00         NOP                     
46B1: FF         RST     0X38            
46B2: 00         NOP                     
46B3: FF         RST     0X38            
46B4: 22         LD      (HLI),A         
46B5: FF         RST     0X38            
46B6: 14         INC     D               
46B7: FF         RST     0X38            
46B8: 08 FF 14   LD      ($14FF),SP      
46BB: FF         RST     0X38            
46BC: 22         LD      (HLI),A         
46BD: FF         RST     0X38            
46BE: 00         NOP                     
46BF: FF         RST     0X38            
46C0: 00         NOP                     
46C1: FF         RST     0X38            
46C2: 00         NOP                     
46C3: FF         RST     0X38            
46C4: 22         LD      (HLI),A         
46C5: FF         RST     0X38            
46C6: 14         INC     D               
46C7: FF         RST     0X38            
46C8: 08 FF 14   LD      ($14FF),SP      
46CB: FF         RST     0X38            
46CC: 22         LD      (HLI),A         
46CD: FF         RST     0X38            
46CE: 00         NOP                     
46CF: FF         RST     0X38            
46D0: 00         NOP                     
46D1: FF         RST     0X38            
46D2: 00         NOP                     
46D3: FF         RST     0X38            
46D4: 22         LD      (HLI),A         
46D5: FF         RST     0X38            
46D6: 14         INC     D               
46D7: FF         RST     0X38            
46D8: 08 FF 14   LD      ($14FF),SP      
46DB: FF         RST     0X38            
46DC: 22         LD      (HLI),A         
46DD: FF         RST     0X38            
46DE: 00         NOP                     
46DF: FF         RST     0X38            
46E0: 00         NOP                     
46E1: FF         RST     0X38            
46E2: 00         NOP                     
46E3: FF         RST     0X38            
46E4: 22         LD      (HLI),A         
46E5: FF         RST     0X38            
46E6: 14         INC     D               
46E7: FF         RST     0X38            
46E8: 08 FF 14   LD      ($14FF),SP      
46EB: FF         RST     0X38            
46EC: 22         LD      (HLI),A         
46ED: FF         RST     0X38            
46EE: 00         NOP                     
46EF: FF         RST     0X38            
46F0: 00         NOP                     
46F1: FF         RST     0X38            
46F2: 00         NOP                     
46F3: FF         RST     0X38            
46F4: 22         LD      (HLI),A         
46F5: FF         RST     0X38            
46F6: 14         INC     D               
46F7: FF         RST     0X38            
46F8: 08 FF 14   LD      ($14FF),SP      
46FB: FF         RST     0X38            
46FC: 22         LD      (HLI),A         
46FD: FF         RST     0X38            
46FE: 00         NOP                     
46FF: FF         RST     0X38            
4700: 01 00 03   LD      BC,$0300        
4703: 01 F9 00   LD      BC,$00F9        
4706: B4         OR      H               
4707: 78         LD      A,B             
4708: 63         LD      H,E             
4709: 1C         INC     E               
470A: 38 07      JR      C,$4713         
470C: 36 19      LD      (HL),$19        
470E: 3A         LD      A,(HLD)         
470F: 1D         DEC     E               
4710: 3A         LD      A,(HLD)         
4711: 1D         DEC     E               
4712: 1C         INC     E               
4713: 0B         DEC     BC              
4714: 0C         INC     C               
4715: 03         INC     BC              
4716: 02         LD      (BC),A          
4717: 01 01 00   LD      BC,$0001        
471A: 03         INC     BC              
471B: 00         NOP                     
471C: 07         RLCA                    
471D: 03         INC     BC              
471E: 07         RLCA                    
471F: 00         NOP                     
4720: C3 00 A5   JP      $A500           
4723: C3 99 66   JP      $6699           
4726: 5A         LD      E,D             
4727: 24         INC     H               
4728: 81         ADD     A,C             
4729: 7E         LD      A,(HL)          
472A: C3 3C FF   JP      $FF3C           
472D: 42         LD      B,D             
472E: FF         RST     0X38            
472F: 66         LD      H,(HL)          
4730: 66         LD      H,(HL)          
4731: 99         SBC     C               
4732: 99         SBC     C               
4733: 7E         LD      A,(HL)          
4734: FF         RST     0X38            
4735: 00         NOP                     
4736: 7E         LD      A,(HL)          
4737: A5         AND     L               
4738: 3C         INC     A               
4739: C3 81 7E   JP      $7E81           
473C: BD         CP      L               
473D: 42         LD      B,D             
473E: C3 00 01   JP      $0100           
4741: 00         NOP                     
4742: 03         INC     BC              
4743: 01 01 00   LD      BC,$0001        
4746: 01 00 06   LD      BC,$0600        
4749: 01 0A 07   LD      BC,$070A        
474C: 0C         INC     C               
474D: 07         RLCA                    
474E: 12         LD      (DE),A          
474F: 0D         DEC     C               
4750: 12         LD      (DE),A          
4751: 0D         DEC     C               
4752: 12         LD      (DE),A          
4753: 0D         DEC     C               
4754: 13         INC     DE              
4755: 0C         INC     C               
4756: 13         INC     DE              
4757: 0C         INC     C               
4758: 0B         DEC     BC              
4759: 04         INC     B               
475A: 09         ADD     HL,BC           
475B: 06 07      LD      B,$07           
475D: 01 03 00   LD      BC,$0003        
4760: E7         RST     0X20            
4761: 00         NOP                     
4762: 99         SBC     C               
4763: E7         RST     0X20            
4764: DB         ???                     
4765: 24         INC     H               
4766: 81         ADD     A,C             
4767: 7E         LD      A,(HL)          
4768: C3 3C FF   JP      $FF3C           
476B: 42         LD      B,D             
476C: FF         RST     0X38            
476D: 66         LD      H,(HL)          
476E: 66         LD      H,(HL)          
476F: 99         SBC     C               
4770: 99         SBC     C               
4771: 7E         LD      A,(HL)          
4772: 7E         LD      A,(HL)          
4773: 81         ADD     A,C             
4774: 00         NOP                     
4775: FF         RST     0X38            
4776: 18 E7      JR      $475F           
4778: 81         ADD     A,C             
4779: 7E         LD      A,(HL)          
477A: 99         SBC     C               
477B: 66         LD      H,(HL)          
477C: E7         RST     0X20            
477D: 81         ADD     A,C             
477E: C3 00 E0   JP      $E000           
4781: 00         NOP                     
4782: F8 00      LDHL    SP,$00          
4784: FE 30      CP      $30             
4786: 7B         LD      A,E             
4787: 3C         INC     A               
4788: 7E         LD      A,(HL)          
4789: 1F         RRA                     
478A: 2F         CPL                     
478B: 1F         RRA                     
478C: 3F         CCF                     
478D: 0F         RRCA                    
478E: 16 0F      LD      D,$0F           
4790: 1E 07      LD      E,$07           
4792: 1F         RRA                     
4793: 07         RLCA                    
4794: 3F         CCF                     
4795: 07         RLCA                    
4796: 36 0F      LD      (HL),$0F        
4798: 6F         LD      L,A             
4799: 1E 7D      LD      E,$7D           
479B: 1E FB      LD      E,$FB           
479D: 1C         INC     E               
479E: FF         RST     0X38            
479F: 18 03      JR      $47A4           
47A1: 00         NOP                     
47A2: 0F         RRCA                    
47A3: 00         NOP                     
47A4: 3F         CCF                     
47A5: 00         NOP                     
47A6: F7         RST     0X30            
47A7: 0F         RRCA                    
47A8: EF         RST     0X28            
47A9: 1F         RRA                     
47AA: FD         ???                     
47AB: FE F7      CP      $F7             
47AD: F8 6F      LDHL    SP,$6F          
47AF: F0 FF      LD      A,($FF)         
47B1: 00         NOP                     
47B2: FE 00      CP      $00             
47B4: FC         ???                     
47B5: 00         NOP                     
47B6: E0 00      LDFF00  ($00),A         
47B8: E0 00      LDFF00  ($00),A         
47BA: E0 00      LDFF00  ($00),A         
47BC: C0         RET     NZ              
47BD: 00         NOP                     
47BE: 80         ADD     A,B             
47BF: 00         NOP                     
47C0: 07         RLCA                    
47C1: 00         NOP                     
47C2: 0F         RRCA                    
47C3: 03         INC     BC              
47C4: 0F         RRCA                    
47C5: 03         INC     BC              
47C6: 07         RLCA                    
47C7: 01 03 00   LD      BC,$0003        
47CA: 03         INC     BC              
47CB: 00         NOP                     
47CC: 03         INC     BC              
47CD: 00         NOP                     
47CE: 07         RLCA                    
47CF: 01 1F 03   LD      BC,$031F        
47D2: 3F         CCF                     
47D3: 0F         RRCA                    
47D4: 7F         LD      A,A             
47D5: 1F         RRA                     
47D6: 3F         CCF                     
47D7: 0F         RRCA                    
47D8: 1F         RRA                     
47D9: 03         INC     BC              
47DA: 07         RLCA                    
47DB: 01 03 00   LD      BC,$0003        
47DE: 01 00 00   LD      BC,$0000        
47E1: 00         NOP                     
47E2: 00         NOP                     
47E3: 00         NOP                     
47E4: 00         NOP                     
47E5: 00         NOP                     
47E6: 18 00      JR      $47E8           
47E8: 3C         INC     A               
47E9: 18 3E      JR      $4829           
47EB: 1C         INC     E               
47EC: 1F         RRA                     
47ED: 0C         INC     C               
47EE: 0E 05      LD      C,$05           
47F0: 05         DEC     B               
47F1: 03         INC     BC              
47F2: 02         LD      (BC),A          
47F3: 01 01 00   LD      BC,$0001        
47F6: 00         NOP                     
47F7: 00         NOP                     
47F8: 00         NOP                     
47F9: 00         NOP                     
47FA: 00         NOP                     
47FB: 00         NOP                     
47FC: 00         NOP                     
47FD: 00         NOP                     
47FE: 00         NOP                     
47FF: 00         NOP                     
4800: 1F         RRA                     
4801: 00         NOP                     
4802: 16 0B      LD      D,$0B           
4804: 20 1F      JR      NZ,$4825        
4806: 3C         INC     A               
4807: 03         INC     BC              
4808: FE 09      CP      $09             
480A: FE 61      CP      $61             
480C: F6 39      OR      $39             
480E: FC         ???                     
480F: 7F         LD      A,A             
4810: 5A         LD      E,D             
4811: 3D         DEC     A               
4812: 7C         LD      A,H             
4813: 33         INC     SP              
4814: F8 6F      LDHL    SP,$6F          
4816: F8 6F      LDHL    SP,$6F          
4818: 7F         LD      A,A             
4819: 30 3C      JR      NC,$4857        
481B: 03         INC     BC              
481C: 3E 17      LD      A,$17           
481E: 3F         CCF                     
481F: 00         NOP                     
4820: 00         NOP                     
4821: 00         NOP                     
4822: 80         ADD     A,B             
4823: 00         NOP                     
4824: 40         LD      B,B             
4825: 80         ADD     A,B             
4826: 20 C0      JR      NZ,$47E8        
4828: 20 C0      JR      NZ,$47EA        
482A: 10 E0      STOP    $E0             
482C: 10 E0      STOP    $E0             
482E: 10 E0      STOP    $E0             
4830: 08 F0 08   LD      ($08F0),SP      
4833: F0 08      LD      A,($08)         
4835: F0 8E      LD      A,($8E)         
4837: 70         LD      (HL),B          
4838: 15         DEC     D               
4839: EA 35 CA   LD      ($CA35),A       
483C: 3E C0      LD      A,$C0           
483E: E0 00      LDFF00  ($00),A         
4840: 06 00      LD      B,$00           
4842: 0D         DEC     C               
4843: 06 08      LD      B,$08           
4845: 07         RLCA                    
4846: 10 0F      STOP    $0F             
4848: 7C         LD      A,H             
4849: 03         INC     BC              
484A: FC         ???                     
484B: 63         LD      H,E             
484C: C8         RET     Z               
484D: 77         LD      (HL),A          
484E: 88         ADC     A,B             
484F: 77         LD      (HL),A          
4850: 40         LD      B,B             
4851: 3F         CCF                     
4852: 60         LD      H,B             
4853: 1F         RRA                     
4854: 70         LD      (HL),B          
4855: 2F         CPL                     
4856: 70         LD      (HL),B          
4857: 3F         CCF                     
4858: 30 1F      JR      NC,$4879        
485A: 38 07      JR      C,$4863         
485C: 70         LD      (HL),B          
485D: 3F         CCF                     
485E: 7F         LD      A,A             
485F: 00         NOP                     
4860: C0         RET     NZ              
4861: 00         NOP                     
4862: 20 C0      JR      NZ,$4824        
4864: 10 E0      STOP    $E0             
4866: 10 E0      STOP    $E0             
4868: 08 F0 08   LD      ($08F0),SP      
486B: F0 04      LD      A,($04)         
486D: F8 04      LDHL    SP,$04          
486F: F8 04      LDHL    SP,$04          
4871: F8 1E      LDHL    SP,$1E          
4873: E0 69      LDFF00  ($69),A         
4875: 96         SUB     (HL)            
4876: E9         JP      (HL)            
4877: 16 FF      LD      D,$FF           
4879: 00         NOP                     
487A: 7E         LD      A,(HL)          
487B: 80         ADD     A,B             
487C: C2 3C FE   JP      NZ,$FE3C        
487F: 00         NOP                     
4880: 0C         INC     C               
4881: 00         NOP                     
4882: 13         INC     DE              
4883: 0C         INC     C               
4884: 10 0F      STOP    $0F             
4886: 17         RLA                     
4887: 08 6F 14   LD      ($146F),SP      
488A: EF         RST     0X28            
488B: 50         LD      D,B             
488C: AF         XOR     A               
488D: 5F         LD      E,A             
488E: AF         XOR     A               
488F: 59         LD      E,C             
4890: 5F         LD      E,A             
4891: 2F         CPL                     
4892: 5C         LD      E,H             
4893: 33         INC     SP              
4894: 5F         LD      E,A             
4895: 3F         CCF                     
4896: 5F         LD      E,A             
4897: 3F         CCF                     
4898: 2F         CPL                     
4899: 1D         DEC     E               
489A: 37         SCF                     
489B: 0F         RRCA                    
489C: 71         LD      (HL),C          
489D: 3E 7F      LD      A,$7F           
489F: 00         NOP                     
48A0: 60         LD      H,B             
48A1: 00         NOP                     
48A2: 90         SUB     B               
48A3: 60         LD      H,B             
48A4: 30 E0      JR      NC,$4886        
48A6: C8         RET     Z               
48A7: 30 E4      JR      NC,$488D        
48A9: 98         SBC     B               
48AA: E4         ???                     
48AB: 18 64      JR      $4911           
48AD: 98         SBC     B               
48AE: C2 FC F2   JP      NZ,$F2FC        
48B1: EC         ???                     
48B2: E2         LDFF00  (C),A           
48B3: DC E2 BC   CALL    C,$BCE2         
48B6: E7         RST     0X20            
48B7: B8         CP      B               
48B8: FD         ???                     
48B9: C2 87 F8   JP      NZ,$F887        
48BC: 8E         ADC     A,(HL)          
48BD: 7C         LD      A,H             
48BE: FE 00      CP      $00             
48C0: 03         INC     BC              
48C1: 00         NOP                     
48C2: 04         INC     B               
48C3: 03         INC     BC              
48C4: 0F         RRCA                    
48C5: 00         NOP                     
48C6: 1F         RRA                     
48C7: 04         INC     B               
48C8: 1F         RRA                     
48C9: 00         NOP                     
48CA: 6F         LD      L,A             
48CB: 1F         RRA                     
48CC: FB         EI                      
48CD: 54         LD      D,H             
48CE: BF         CP      A               
48CF: 50         LD      D,B             
48D0: BF         CP      A               
48D1: 58         LD      E,B             
48D2: 5F         LD      E,A             
48D3: 2F         CPL                     
48D4: 59         LD      E,C             
48D5: 37         SCF                     
48D6: 5F         LD      E,A             
48D7: 3F         CCF                     
48D8: 5F         LD      E,A             
48D9: 3B         DEC     SP              
48DA: 2F         CPL                     
48DB: 1F         RRA                     
48DC: 71         LD      (HL),C          
48DD: 3E 7F      LD      A,$7F           
48DF: 00         NOP                     
48E0: 30 00      JR      NC,$48E2        
48E2: D8         RET     C               
48E3: 30 E8      JR      NC,$48CD        
48E5: 10 E4      STOP    $E4             
48E7: 98         SBC     B               
48E8: E4         ???                     
48E9: 18 E4      JR      $48CF           
48EB: F8 B2      LDHL    SP,$B2          
48ED: 5C         LD      E,H             
48EE: F2         ???                     
48EF: 1C         INC     E               
48F0: E9         JP      (HL)            
48F1: 36 F1      LD      (HL),$F1        
48F3: EE F1      XOR     $F1             
48F5: DE F3      SBC     $F3             
48F7: DC FD E2   CALL    C,$E2FD         
48FA: E7         RST     0X20            
48FB: F8 8E      LDHL    SP,$8E          
48FD: 7C         LD      A,H             
48FE: FE 00      CP      $00             
4900: CF         RST     0X08            
4901: 3F         CCF                     
4902: CF         RST     0X08            
4903: 3F         CCF                     
4904: CF         RST     0X08            
4905: 3F         CCF                     
4906: CF         RST     0X08            
4907: 3F         CCF                     
4908: CF         RST     0X08            
4909: 3F         CCF                     
490A: CF         RST     0X08            
490B: 3F         CCF                     
490C: CF         RST     0X08            
490D: 3F         CCF                     
490E: CF         RST     0X08            
490F: 3F         CCF                     
4910: CF         RST     0X08            
4911: 3F         CCF                     
4912: CF         RST     0X08            
4913: 3F         CCF                     
4914: CF         RST     0X08            
4915: 3F         CCF                     
4916: CF         RST     0X08            
4917: 3F         CCF                     
4918: CF         RST     0X08            
4919: 3F         CCF                     
491A: CF         RST     0X08            
491B: 3F         CCF                     
491C: CF         RST     0X08            
491D: 3F         CCF                     
491E: CF         RST     0X08            
491F: 3F         CCF                     
4920: 00         NOP                     
4921: 00         NOP                     
4922: 00         NOP                     
4923: 00         NOP                     
4924: 00         NOP                     
4925: 00         NOP                     
4926: 01 00 03   LD      BC,$0300        
4929: 01 03 00   LD      BC,$0003        
492C: 01 00 01   LD      BC,$0100        
492F: 00         NOP                     
4930: 07         RLCA                    
4931: 00         NOP                     
4932: 0D         DEC     C               
4933: 06 1A      LD      B,$1A           
4935: 0D         DEC     C               
4936: 1F         RRA                     
4937: 00         NOP                     
4938: 02         LD      (BC),A          
4939: 01 02 01   LD      BC,$0102        
493C: 03         INC     BC              
493D: 01 03 01   LD      BC,$0103        
4940: 03         INC     BC              
4941: 01 03 01   LD      BC,$0103        
4944: 03         INC     BC              
4945: 01 03 01   LD      BC,$0103        
4948: 03         INC     BC              
4949: 01 03 01   LD      BC,$0103        
494C: 03         INC     BC              
494D: 01 03 01   LD      BC,$0103        
4950: 02         LD      (BC),A          
4951: 01 01 00   LD      BC,$0001        
4954: 01 00 00   LD      BC,$0000        
4957: 00         NOP                     
4958: 00         NOP                     
4959: 00         NOP                     
495A: 00         NOP                     
495B: 00         NOP                     
495C: 00         NOP                     
495D: 00         NOP                     
495E: 00         NOP                     
495F: 00         NOP                     
4960: 00         NOP                     
4961: 00         NOP                     
4962: 00         NOP                     
4963: 00         NOP                     
4964: 00         NOP                     
4965: 00         NOP                     
4966: 00         NOP                     
4967: 00         NOP                     
4968: 00         NOP                     
4969: 00         NOP                     
496A: 00         NOP                     
496B: 00         NOP                     
496C: 00         NOP                     
496D: 00         NOP                     
496E: 01 01 03   LD      BC,$0301        
4971: 02         LD      (BC),A          
4972: 07         RLCA                    
4973: 04         INC     B               
4974: 07         RLCA                    
4975: 04         INC     B               
4976: 0F         RRCA                    
4977: 08 0F 08   LD      ($080F),SP      
497A: 1F         RRA                     
497B: 10 1F      STOP    $1F             
497D: 10 1F      STOP    $1F             
497F: 10 00      STOP    $00             
4981: 00         NOP                     
4982: 00         NOP                     
4983: 00         NOP                     
4984: 00         NOP                     
4985: 00         NOP                     
4986: 07         RLCA                    
4987: 07         RLCA                    
4988: 1F         RRA                     
4989: 18 7F      JR      $4A0A           
498B: 60         LD      H,B             
498C: FF         RST     0X38            
498D: 80         ADD     A,B             
498E: FF         RST     0X38            
498F: 00         NOP                     
4990: FF         RST     0X38            
4991: 00         NOP                     
4992: FF         RST     0X38            
4993: 00         NOP                     
4994: FF         RST     0X38            
4995: 00         NOP                     
4996: FF         RST     0X38            
4997: 00         NOP                     
4998: FF         RST     0X38            
4999: 00         NOP                     
499A: FF         RST     0X38            
499B: 00         NOP                     
499C: FF         RST     0X38            
499D: 00         NOP                     
499E: FF         RST     0X38            
499F: 00         NOP                     
49A0: 00         NOP                     
49A1: 00         NOP                     
49A2: 00         NOP                     
49A3: 00         NOP                     
49A4: 00         NOP                     
49A5: 00         NOP                     
49A6: 00         NOP                     
49A7: 00         NOP                     
49A8: 00         NOP                     
49A9: 00         NOP                     
49AA: 01 01 03   LD      BC,$0301        
49AD: 02         LD      (BC),A          
49AE: 07         RLCA                    
49AF: 04         INC     B               
49B0: 07         RLCA                    
49B1: 04         INC     B               
49B2: 0F         RRCA                    
49B3: 08 0F 08   LD      ($080F),SP      
49B6: 0F         RRCA                    
49B7: 08 0F 08   LD      ($080F),SP      
49BA: 0F         RRCA                    
49BB: 08 0F 08   LD      ($080F),SP      
49BE: 07         RLCA                    
49BF: 04         INC     B               
49C0: 00         NOP                     
49C1: 00         NOP                     
49C2: 00         NOP                     
49C3: 00         NOP                     
49C4: 0F         RRCA                    
49C5: 0F         RRCA                    
49C6: 3F         CCF                     
49C7: 30 FF      JR      NC,$49C8        
49C9: C0         RET     NZ              
49CA: FF         RST     0X38            
49CB: 00         NOP                     
49CC: FF         RST     0X38            
49CD: 00         NOP                     
49CE: FF         RST     0X38            
49CF: 00         NOP                     
49D0: FF         RST     0X38            
49D1: 00         NOP                     
49D2: FF         RST     0X38            
49D3: 00         NOP                     
49D4: FF         RST     0X38            
49D5: 00         NOP                     
49D6: FF         RST     0X38            
49D7: 00         NOP                     
49D8: FF         RST     0X38            
49D9: 00         NOP                     
49DA: FF         RST     0X38            
49DB: 00         NOP                     
49DC: FF         RST     0X38            
49DD: 00         NOP                     
49DE: FF         RST     0X38            
49DF: 00         NOP                     
49E0: 07         RLCA                    
49E1: 04         INC     B               
49E2: 03         INC     BC              
49E3: 02         LD      (BC),A          
49E4: 03         INC     BC              
49E5: 02         LD      (BC),A          
49E6: 01 01 01   LD      BC,$0101        
49E9: 01 00 00   LD      BC,$0000        
49EC: 00         NOP                     
49ED: 00         NOP                     
49EE: 00         NOP                     
49EF: 00         NOP                     
49F0: 00         NOP                     
49F1: 00         NOP                     
49F2: 00         NOP                     
49F3: 00         NOP                     
49F4: 00         NOP                     
49F5: 00         NOP                     
49F6: 00         NOP                     
49F7: 00         NOP                     
49F8: 00         NOP                     
49F9: 00         NOP                     
49FA: 00         NOP                     
49FB: 00         NOP                     
49FC: 00         NOP                     
49FD: 00         NOP                     
49FE: 00         NOP                     
49FF: 00         NOP                     
4A00: FF         RST     0X38            
4A01: 00         NOP                     
4A02: FF         RST     0X38            
4A03: 00         NOP                     
4A04: FF         RST     0X38            
4A05: 00         NOP                     
4A06: FF         RST     0X38            
4A07: 00         NOP                     
4A08: FF         RST     0X38            
4A09: 00         NOP                     
4A0A: FF         RST     0X38            
4A0B: 80         ADD     A,B             
4A0C: FF         RST     0X38            
4A0D: 80         ADD     A,B             
4A0E: 7F         LD      A,A             
4A0F: 40         LD      B,B             
4A10: 7F         LD      A,A             
4A11: 40         LD      B,B             
4A12: 3F         CCF                     
4A13: 20 3F      JR      NZ,$4A54        
4A15: 20 1F      JR      NZ,$4A36        
4A17: 10 0F      STOP    $0F             
4A19: 0C         INC     C               
4A1A: 03         INC     BC              
4A1B: 03         INC     BC              
4A1C: 00         NOP                     
4A1D: 00         NOP                     
4A1E: 00         NOP                     
4A1F: 00         NOP                     
4A20: 00         NOP                     
4A21: 00         NOP                     
4A22: 00         NOP                     
4A23: 00         NOP                     
4A24: 00         NOP                     
4A25: 00         NOP                     
4A26: 00         NOP                     
4A27: 00         NOP                     
4A28: 00         NOP                     
4A29: 00         NOP                     
4A2A: 00         NOP                     
4A2B: 00         NOP                     
4A2C: 01 01 03   LD      BC,$0301        
4A2F: 02         LD      (BC),A          
4A30: 07         RLCA                    
4A31: 04         INC     B               
4A32: 0F         RRCA                    
4A33: 08 0F 08   LD      ($080F),SP      
4A36: 0F         RRCA                    
4A37: 08 07 04   LD      ($0407),SP      
4A3A: 03         INC     BC              
4A3B: 03         INC     BC              
4A3C: 00         NOP                     
4A3D: 00         NOP                     
4A3E: 00         NOP                     
4A3F: 00         NOP                     
4A40: 00         NOP                     
4A41: 00         NOP                     
4A42: 07         RLCA                    
4A43: 07         RLCA                    
4A44: 0F         RRCA                    
4A45: 08 1F 10   LD      ($101F),SP      
4A48: 1F         RRA                     
4A49: 10 7F      STOP    $7F             
4A4B: 60         LD      H,B             
4A4C: FF         RST     0X38            
4A4D: 80         ADD     A,B             
4A4E: FF         RST     0X38            
4A4F: 00         NOP                     
4A50: FF         RST     0X38            
4A51: 00         NOP                     
4A52: FF         RST     0X38            
4A53: 00         NOP                     
4A54: FF         RST     0X38            
4A55: 00         NOP                     
4A56: FF         RST     0X38            
4A57: 00         NOP                     
4A58: FF         RST     0X38            
4A59: 00         NOP                     
4A5A: FF         RST     0X38            
4A5B: 00         NOP                     
4A5C: FF         RST     0X38            
4A5D: 80         ADD     A,B             
4A5E: 7F         LD      A,A             
4A5F: 40         LD      B,B             
4A60: 7F         LD      A,A             
4A61: 40         LD      B,B             
4A62: 3F         CCF                     
4A63: 20 3F      JR      NZ,$4AA4        
4A65: 20 3F      JR      NZ,$4AA6        
4A67: 20 3F      JR      NZ,$4AA8        
4A69: 20 3F      JR      NZ,$4AAA        
4A6B: 20 3F      JR      NZ,$4AAC        
4A6D: 20 1F      JR      NZ,$4A8E        
4A6F: 10 1F      STOP    $1F             
4A71: 10 1F      STOP    $1F             
4A73: 10 0F      STOP    $0F             
4A75: 08 0F 08   LD      ($080F),SP      
4A78: 07         RLCA                    
4A79: 04         INC     B               
4A7A: 03         INC     BC              
4A7B: 02         LD      (BC),A          
4A7C: 01 01 00   LD      BC,$0001        
4A7F: 00         NOP                     
4A80: 00         NOP                     
4A81: 00         NOP                     
4A82: 00         NOP                     
4A83: 00         NOP                     
4A84: 00         NOP                     
4A85: 00         NOP                     
4A86: 00         NOP                     
4A87: 00         NOP                     
4A88: 00         NOP                     
4A89: 00         NOP                     
4A8A: 00         NOP                     
4A8B: 00         NOP                     
4A8C: 01 01 03   LD      BC,$0301        
4A8F: 02         LD      (BC),A          
4A90: 07         RLCA                    
4A91: 04         INC     B               
4A92: 07         RLCA                    
4A93: 04         INC     B               
4A94: 07         RLCA                    
4A95: 04         INC     B               
4A96: 03         INC     BC              
4A97: 02         LD      (BC),A          
4A98: 01 01 00   LD      BC,$0001        
4A9B: 00         NOP                     
4A9C: 00         NOP                     
4A9D: 00         NOP                     
4A9E: 00         NOP                     
4A9F: 00         NOP                     
4AA0: 03         INC     BC              
4AA1: 03         INC     BC              
4AA2: 07         RLCA                    
4AA3: 04         INC     B               
4AA4: 0F         RRCA                    
4AA5: 08 0F 08   LD      ($080F),SP      
4AA8: 0F         RRCA                    
4AA9: 08 3F 38   LD      ($383F),SP      
4AAC: FF         RST     0X38            
4AAD: C0         RET     NZ              
4AAE: FF         RST     0X38            
4AAF: 00         NOP                     
4AB0: FF         RST     0X38            
4AB1: 00         NOP                     
4AB2: FF         RST     0X38            
4AB3: 00         NOP                     
4AB4: FF         RST     0X38            
4AB5: 00         NOP                     
4AB6: FF         RST     0X38            
4AB7: 00         NOP                     
4AB8: FF         RST     0X38            
4AB9: C0         RET     NZ              
4ABA: 3F         CCF                     
4ABB: 20 1F      JR      NZ,$4ADC        
4ABD: 10 1F      STOP    $1F             
4ABF: 10 1F      STOP    $1F             
4AC1: 10 1F      STOP    $1F             
4AC3: 10 1F      STOP    $1F             
4AC5: 10 1F      STOP    $1F             
4AC7: 10 1F      STOP    $1F             
4AC9: 10 1F      STOP    $1F             
4ACB: 10 1F      STOP    $1F             
4ACD: 10 1F      STOP    $1F             
4ACF: 10 1F      STOP    $1F             
4AD1: 10 1F      STOP    $1F             
4AD3: 10 0F      STOP    $0F             
4AD5: 08 0F 08   LD      ($080F),SP      
4AD8: 07         RLCA                    
4AD9: 04         INC     B               
4ADA: 07         RLCA                    
4ADB: 04         INC     B               
4ADC: 03         INC     BC              
4ADD: 02         LD      (BC),A          
4ADE: 01 01 01   LD      BC,$0101        
4AE1: 01 03 02   LD      BC,$0203        
4AE4: 07         RLCA                    
4AE5: 04         INC     B               
4AE6: 07         RLCA                    
4AE7: 04         INC     B               
4AE8: 07         RLCA                    
4AE9: 04         INC     B               
4AEA: 03         INC     BC              
4AEB: 02         LD      (BC),A          
4AEC: 1F         RRA                     
4AED: 1E 3F      LD      E,$3F           
4AEF: 22         LD      (HLI),A         
4AF0: 7F         LD      A,A             
4AF1: 40         LD      B,B             
4AF2: FF         RST     0X38            
4AF3: 80         ADD     A,B             
4AF4: FF         RST     0X38            
4AF5: 80         ADD     A,B             
4AF6: FF         RST     0X38            
4AF7: F0 0F      LD      A,($0F)         
4AF9: 08 0F 08   LD      ($080F),SP      
4AFC: 0F         RRCA                    
4AFD: 08 0F 08   LD      ($080F),SP      
4B00: 0F         RRCA                    
4B01: 08 0F 08   LD      ($080F),SP      
4B04: 0F         RRCA                    
4B05: 08 0F 08   LD      ($080F),SP      
4B08: 0F         RRCA                    
4B09: 08 0F 08   LD      ($080F),SP      
4B0C: 0F         RRCA                    
4B0D: 08 0F 08   LD      ($080F),SP      
4B10: 0F         RRCA                    
4B11: 08 0F 08   LD      ($080F),SP      
4B14: 07         RLCA                    
4B15: 04         INC     B               
4B16: 07         RLCA                    
4B17: 04         INC     B               
4B18: 07         RLCA                    
4B19: 04         INC     B               
4B1A: 03         INC     BC              
4B1B: 02         LD      (BC),A          
4B1C: 03         INC     BC              
4B1D: 02         LD      (BC),A          
4B1E: 01 01 18   LD      BC,$1801        
4B21: 00         NOP                     
4B22: 3C         INC     A               
4B23: 18 3C      JR      $4B61           
4B25: 18 3C      JR      $4B63           
4B27: 18 3C      JR      $4B65           
4B29: 18 3C      JR      $4B67           
4B2B: 18 3C      JR      $4B69           
4B2D: 18 3C      JR      $4B6B           
4B2F: 18 3C      JR      $4B6D           
4B31: 18 3C      JR      $4B6F           
4B33: 18 3C      JR      $4B71           
4B35: 18 3C      JR      $4B73           
4B37: 18 3C      JR      $4B75           
4B39: 18 3C      JR      $4B77           
4B3B: 18 3C      JR      $4B79           
4B3D: 18 18      JR      $4B57           
4B3F: 00         NOP                     
4B40: 00         NOP                     
4B41: 00         NOP                     
4B42: 03         INC     BC              
4B43: 00         NOP                     
4B44: 07         RLCA                    
4B45: 02         LD      (BC),A          
4B46: 0F         RRCA                    
4B47: 06 0F      LD      B,$0F           
4B49: 06 1E      LD      B,$1E           
4B4B: 0C         INC     C               
4B4C: 1E 0C      LD      E,$0C           
4B4E: 3C         INC     A               
4B4F: 18 3C      JR      $4B8D           
4B51: 18 78      JR      $4BCB           
4B53: 30 78      JR      NC,$4BCD        
4B55: 30 F0      JR      NC,$4B47        
4B57: 60         LD      H,B             
4B58: F0 60      LD      A,($60)         
4B5A: E0 40      LDFF00  ($40),A         
4B5C: C0         RET     NZ              
4B5D: 00         NOP                     
4B5E: 00         NOP                     
4B5F: 00         NOP                     
4B60: 00         NOP                     
4B61: 00         NOP                     
4B62: 00         NOP                     
4B63: 00         NOP                     
4B64: 18 00      JR      $4B66           
4B66: 3C         INC     A               
4B67: 18 7C      JR      $4BE5           
4B69: 38 F8      JR      C,$4B63         
4B6B: 70         LD      (HL),B          
4B6C: F0 E0      LD      A,($E0)         
4B6E: E0 C0      LDFF00  ($C0),A         
4B70: C0         RET     NZ              
4B71: 80         ADD     A,B             
4B72: 80         ADD     A,B             
4B73: 00         NOP                     
4B74: 00         NOP                     
4B75: 00         NOP                     
4B76: 00         NOP                     
4B77: 00         NOP                     
4B78: 00         NOP                     
4B79: 00         NOP                     
4B7A: 00         NOP                     
4B7B: 00         NOP                     
4B7C: 00         NOP                     
4B7D: 00         NOP                     
4B7E: 00         NOP                     
4B7F: 00         NOP                     
4B80: 00         NOP                     
4B81: 00         NOP                     
4B82: 00         NOP                     
4B83: 00         NOP                     
4B84: 00         NOP                     
4B85: 00         NOP                     
4B86: 00         NOP                     
4B87: 00         NOP                     
4B88: 1E 00      LD      E,$00           
4B8A: 7E         LD      A,(HL)          
4B8B: 1C         INC     E               
4B8C: FC         ???                     
4B8D: 78         LD      A,B             
4B8E: F8 E0      LDHL    SP,$E0          
4B90: E0 80      LDFF00  ($80),A         
4B92: 80         ADD     A,B             
4B93: 00         NOP                     
4B94: 00         NOP                     
4B95: 00         NOP                     
4B96: 00         NOP                     
4B97: 00         NOP                     
4B98: 00         NOP                     
4B99: 00         NOP                     
4B9A: 00         NOP                     
4B9B: 00         NOP                     
4B9C: 00         NOP                     
4B9D: 00         NOP                     
4B9E: 00         NOP                     
4B9F: 00         NOP                     
4BA0: 07         RLCA                    
4BA1: 07         RLCA                    
4BA2: 1F         RRA                     
4BA3: 18 3F      JR      $4BE4           
4BA5: 20 7F      JR      NZ,$4C26        
4BA7: 40         LD      B,B             
4BA8: 7F         LD      A,A             
4BA9: 40         LD      B,B             
4BAA: FF         RST     0X38            
4BAB: 80         ADD     A,B             
4BAC: FF         RST     0X38            
4BAD: 80         ADD     A,B             
4BAE: FF         RST     0X38            
4BAF: 80         ADD     A,B             
4BB0: FF         RST     0X38            
4BB1: 80         ADD     A,B             
4BB2: FF         RST     0X38            
4BB3: 80         ADD     A,B             
4BB4: FF         RST     0X38            
4BB5: 80         ADD     A,B             
4BB6: 7F         LD      A,A             
4BB7: 40         LD      B,B             
4BB8: 7F         LD      A,A             
4BB9: 40         LD      B,B             
4BBA: 3F         CCF                     
4BBB: 20 1F      JR      NZ,$4BDC        
4BBD: 18 07      JR      $4BC6           
4BBF: 07         RLCA                    
4BC0: C0         RET     NZ              
4BC1: 00         NOP                     
4BC2: 7C         LD      A,H             
4BC3: 00         NOP                     
4BC4: 3E 00      LD      A,$00           
4BC6: 06 00      LD      B,$00           
4BC8: 0C         INC     C               
4BC9: 00         NOP                     
4BCA: 18 00      JR      $4BCC           
4BCC: 18 00      JR      $4BCE           
4BCE: 19         ADD     HL,DE           
4BCF: 00         NOP                     
4BD0: 33         INC     SP              
4BD1: 00         NOP                     
4BD2: 3E 00      LD      A,$00           
4BD4: 1C         INC     E               
4BD5: 00         NOP                     
4BD6: 00         NOP                     
4BD7: 00         NOP                     
4BD8: 00         NOP                     
4BD9: 00         NOP                     
4BDA: 00         NOP                     
4BDB: 00         NOP                     
4BDC: 00         NOP                     
4BDD: 00         NOP                     
4BDE: 00         NOP                     
4BDF: 00         NOP                     
4BE0: 3C         INC     A               
4BE1: 00         NOP                     
4BE2: 7E         LD      A,(HL)          
4BE3: 00         NOP                     
4BE4: 6E         LD      L,(HL)          
4BE5: 30 77      JR      NC,$4C5E        
4BE7: 38 3E      JR      C,$4C27         
4BE9: 01 03 00   LD      BC,$0003        
4BEC: FF         RST     0X38            
4BED: 00         NOP                     
4BEE: 8F         ADC     A,A             
4BEF: 7E         LD      A,(HL)          
4BF0: 8F         ADC     A,A             
4BF1: 7E         LD      A,(HL)          
4BF2: FF         RST     0X38            
4BF3: 00         NOP                     
4BF4: 41         LD      B,C             
4BF5: 3E 4F      LD      A,$4F           
4BF7: 3E 4F      LD      A,$4F           
4BF9: 3E 4F      LD      A,$4F           
4BFB: 3E 4F      LD      A,$4F           
4BFD: 3E 7F      LD      A,$7F           
4BFF: 00         NOP                     
4C00: 0E 00      LD      C,$00           
4C02: 15         DEC     D               
4C03: 0A         LD      A,(BC)          
4C04: 10 0F      STOP    $0F             
4C06: 1E 01      LD      E,$01           
4C08: CF         RST     0X08            
4C09: 06 E5      LD      B,$E5           
4C0B: 03         INC     BC              
4C0C: FB         EI                      
4C0D: 00         NOP                     
4C0E: 79         LD      A,C             
4C0F: 30 3F      JR      NC,$4C50        
4C11: 00         NOP                     
4C12: 0E 05      LD      C,$05           
4C14: 0E 01      LD      C,$01           
4C16: 09         ADD     HL,BC           
4C17: 06 07      LD      B,$07           
4C19: 00         NOP                     
4C1A: 00         NOP                     
4C1B: 00         NOP                     
4C1C: 00         NOP                     
4C1D: 00         NOP                     
4C1E: 00         NOP                     
4C1F: 00         NOP                     
4C20: 00         NOP                     
4C21: 00         NOP                     
4C22: 01 00 3F   LD      BC,$3F00        
4C25: 00         NOP                     
4C26: 4D         LD      C,L             
4C27: 3E 7C      LD      A,$7C           
4C29: 03         INC     BC              
4C2A: 7E         LD      A,(HL)          
4C2B: 2D         DEC     L               
4C2C: FF         RST     0X38            
4C2D: 7E         LD      A,(HL)          
4C2E: FF         RST     0X38            
4C2F: 56         LD      D,(HL)          
4C30: EE 11      XOR     $11             
4C32: E0 7F      LDFF00  ($7F),A         
4C34: 04         INC     B               
4C35: FB         EI                      
4C36: 2E D5      LD      L,$D5           
4C38: FF         RST     0X38            
4C39: 20 FF      JR      NZ,$4C3A        
4C3B: DF         RST     0X18            
4C3C: 7F         LD      A,A             
4C3D: FF         RST     0X38            
4C3E: FF         RST     0X38            
4C3F: 00         NOP                     
4C40: 00         NOP                     
4C41: 00         NOP                     
4C42: 80         ADD     A,B             
4C43: 00         NOP                     
4C44: C0         RET     NZ              
4C45: 80         ADD     A,B             
4C46: C0         RET     NZ              
4C47: 00         NOP                     
4C48: 80         ADD     A,B             
4C49: 00         NOP                     
4C4A: 40         LD      B,B             
4C4B: 80         ADD     A,B             
4C4C: 40         LD      B,B             
4C4D: 80         ADD     A,B             
4C4E: 83         ADD     A,E             
4C4F: 00         NOP                     
4C50: 47         LD      B,A             
4C51: 82         ADD     A,D             
4C52: 29         ADD     HL,HL           
4C53: C6 91      ADD     $91             
4C55: 6E         LD      L,(HL)          
4C56: D2 6C 52   JP      NC,$526C        
4C59: EC         ???                     
4C5A: FA 84 BA   LD      A,($BA84)       
4C5D: 74         LD      (HL),H          
4C5E: 85         ADD     A,L             
4C5F: 7A         LD      A,D             
4C60: 7F         LD      A,A             
4C61: 8E         ADC     A,(HL)          
4C62: 3E DD      LD      A,$DD           
4C64: 7F         LD      A,A             
4C65: 94         SUB     H               
4C66: FF         RST     0X38            
4C67: 17         RLA                     
4C68: FF         RST     0X38            
4C69: 1D         DEC     E               
4C6A: 5F         LD      E,A             
4C6B: 2F         CPL                     
4C6C: EF         RST     0X28            
4C6D: 70         LD      (HL),B          
4C6E: FF         RST     0X38            
4C6F: 00         NOP                     
4C70: 00         NOP                     
4C71: 00         NOP                     
4C72: 00         NOP                     
4C73: 00         NOP                     
4C74: 00         NOP                     
4C75: 00         NOP                     
4C76: 00         NOP                     
4C77: 00         NOP                     
4C78: 00         NOP                     
4C79: 00         NOP                     
4C7A: 00         NOP                     
4C7B: 00         NOP                     
4C7C: 00         NOP                     
4C7D: 00         NOP                     
4C7E: 00         NOP                     
4C7F: 00         NOP                     
4C80: C7         RST     0X00            
4C81: 3A         LD      A,(HLD)         
4C82: 27         DAA                     
4C83: DA 8F 72   JP      C,$728F         
4C86: 9D         SBC     L               
4C87: 66         LD      H,(HL)          
4C88: FE 00      CP      $00             
4C8A: F2         ???                     
4C8B: 8C         ADC     A,H             
4C8C: C7         RST     0X00            
4C8D: 3E FF      LD      A,$FF           
4C8F: 00         NOP                     
4C90: 00         NOP                     
4C91: 00         NOP                     
4C92: 00         NOP                     
4C93: 00         NOP                     
4C94: 00         NOP                     
4C95: 00         NOP                     
4C96: 00         NOP                     
4C97: 00         NOP                     
4C98: 00         NOP                     
4C99: 00         NOP                     
4C9A: 00         NOP                     
4C9B: 00         NOP                     
4C9C: 00         NOP                     
4C9D: 00         NOP                     
4C9E: 00         NOP                     
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
4CAA: 00         NOP                     
4CAB: 00         NOP                     
4CAC: 07         RLCA                    
4CAD: 00         NOP                     
4CAE: 0D         DEC     C               
4CAF: 06 10      LD      B,$10           
4CB1: 0F         RRCA                    
4CB2: 10 0F      STOP    $0F             
4CB4: 1D         DEC     E               
4CB5: 02         LD      (BC),A          
4CB6: 0F         RRCA                    
4CB7: 04         INC     B               
4CB8: 0F         RRCA                    
4CB9: 02         LD      (BC),A          
4CBA: 03         INC     BC              
4CBB: 01 01 00   LD      BC,$0001        
4CBE: 00         NOP                     
4CBF: 00         NOP                     
4CC0: 00         NOP                     
4CC1: 00         NOP                     
4CC2: 00         NOP                     
4CC3: 00         NOP                     
4CC4: 1E 00      LD      E,$00           
4CC6: 2F         CPL                     
4CC7: 1C         INC     E               
4CC8: 23         INC     HL              
4CC9: 1D         DEC     E               
4CCA: 21 1E 60   LD      HL,$601E        
4CCD: 1F         RRA                     
4CCE: F0 2F      LD      A,($2F)         
4CD0: 78         LD      A,B             
4CD1: A7         AND     A               
4CD2: 07         RLCA                    
4CD3: F8 A0      LDHL    SP,$A0          
4CD5: 5F         LD      E,A             
4CD6: F0 BF      LD      A,($BF)         
4CD8: EF         RST     0X28            
4CD9: 70         LD      (HL),B          
4CDA: D7         RST     0X10            
4CDB: EE FF      XOR     $FF             
4CDD: 00         NOP                     
4CDE: 67         LD      H,A             
4CDF: 18 00      JR      $4CE1           
4CE1: 00         NOP                     
4CE2: 00         NOP                     
4CE3: 00         NOP                     
4CE4: 00         NOP                     
4CE5: 00         NOP                     
4CE6: 80         ADD     A,B             
4CE7: 00         NOP                     
4CE8: C0         RET     NZ              
4CE9: 00         NOP                     
4CEA: A0         AND     B               
4CEB: 40         LD      B,B             
4CEC: 20 C0      JR      NZ,$4CAE        
4CEE: 20 C0      JR      NZ,$4CB0        
4CF0: 27         DAA                     
4CF1: C0         RET     NZ              
4CF2: FB         EI                      
4CF3: 06 6D      LD      B,$6D           
4CF5: 9E         SBC     (HL)            
4CF6: DA 3C 84   JP      C,$843C         
4CF9: 78         LD      A,B             
4CFA: 38 C0      JR      C,$4CBC         
4CFC: 38 F0      JR      C,$4CEE         
4CFE: 38 F0      JR      C,$4CF0         
4D00: A2         AND     D               
4D01: 5D         LD      E,L             
4D02: 82         ADD     A,D             
4D03: 7D         LD      A,L             
4D04: 44         LD      B,H             
4D05: 3B         DEC     SP              
4D06: 38 07      JR      C,$4D0F         
4D08: 39         ADD     HL,SP           
4D09: 07         RLCA                    
4D0A: 65         LD      H,L             
4D0B: 1B         DEC     DE              
4D0C: C3 7C FF   JP      $FF7C           
4D0F: 00         NOP                     
4D10: 00         NOP                     
4D11: 00         NOP                     
4D12: 00         NOP                     
4D13: 00         NOP                     
4D14: 00         NOP                     
4D15: 00         NOP                     
4D16: 00         NOP                     
4D17: 00         NOP                     
4D18: 00         NOP                     
4D19: 00         NOP                     
4D1A: 00         NOP                     
4D1B: 00         NOP                     
4D1C: 00         NOP                     
4D1D: 00         NOP                     
4D1E: 00         NOP                     
4D1F: 00         NOP                     
4D20: 24         INC     H               
4D21: F8 7C      LDHL    SP,$7C          
4D23: F8 8C      LDHL    SP,$8C          
4D25: F8 F4      LDHL    SP,$F4          
4D27: F8 1C      LDHL    SP,$1C          
4D29: F0 FA      LD      A,($FA)         
4D2B: E4         ???                     
4D2C: F3         DI                      
4D2D: 0E FF      LD      C,$FF           
4D2F: 00         NOP                     
4D30: 00         NOP                     
4D31: 00         NOP                     
4D32: 00         NOP                     
4D33: 00         NOP                     
4D34: 00         NOP                     
4D35: 00         NOP                     
4D36: 00         NOP                     
4D37: 00         NOP                     
4D38: 00         NOP                     
4D39: 00         NOP                     
4D3A: 00         NOP                     
4D3B: 00         NOP                     
4D3C: 00         NOP                     
4D3D: 00         NOP                     
4D3E: 00         NOP                     
4D3F: 00         NOP                     
4D40: 00         NOP                     
4D41: 00         NOP                     
4D42: 00         NOP                     
4D43: 00         NOP                     
4D44: 03         INC     BC              
4D45: 00         NOP                     
4D46: 07         RLCA                    
4D47: 03         INC     BC              
4D48: 07         RLCA                    
4D49: 03         INC     BC              
4D4A: 07         RLCA                    
4D4B: 02         LD      (BC),A          
4D4C: 0F         RRCA                    
4D4D: 00         NOP                     
4D4E: 0A         LD      A,(BC)          
4D4F: 05         DEC     B               
4D50: 0F         RRCA                    
4D51: 00         NOP                     
4D52: 10 0F      STOP    $0F             
4D54: 2B         DEC     HL              
4D55: 14         INC     D               
4D56: 2A         LD      A,(HLI)         
4D57: 15         DEC     D               
4D58: 20 1F      JR      NZ,$4D79        
4D5A: 4C         LD      C,H             
4D5B: 3F         CCF                     
4D5C: 80         ADD     A,B             
4D5D: 7F         LD      A,A             
4D5E: A4         AND     H               
4D5F: 5B         LD      E,E             
4D60: 00         NOP                     
4D61: 00         NOP                     
4D62: 00         NOP                     
4D63: 00         NOP                     
4D64: 0E 00      LD      C,$00           
4D66: 9F         SBC     A               
4D67: 0E FF      LD      C,$FF           
4D69: 1E B7      LD      E,$B7           
4D6B: DE B6      SBC     $B6             
4D6D: 4C         LD      C,H             
4D6E: 7E         LD      A,(HL)          
4D6F: 9C         SBC     H               
4D70: 3E CC      LD      A,$CC           
4D72: 1E E4      LD      E,$E4           
4D74: 0C         INC     C               
4D75: F0 48      LD      A,($48)         
4D77: F0 C4      LD      A,($C4)         
4D79: 38 84      JR      C,$4CFF         
4D7B: 78         LD      A,B             
4D7C: 82         ADD     A,D             
4D7D: 7C         LD      A,H             
4D7E: 42         LD      B,D             
4D7F: BC         CP      H               
4D80: 80         ADD     A,B             
4D81: 7F         LD      A,A             
4D82: 80         ADD     A,B             
4D83: 7F         LD      A,A             
4D84: 40         LD      B,B             
4D85: 3F         CCF                     
4D86: 3F         CCF                     
4D87: 00         NOP                     
4D88: 40         LD      B,B             
4D89: 3F         CCF                     
4D8A: 40         LD      B,B             
4D8B: 3F         CCF                     
4D8C: 80         ADD     A,B             
4D8D: 7F         LD      A,A             
4D8E: 80         ADD     A,B             
4D8F: 7F         LD      A,A             
4D90: 80         ADD     A,B             
4D91: 7F         LD      A,A             
4D92: 80         ADD     A,B             
4D93: 7F         LD      A,A             
4D94: 80         ADD     A,B             
4D95: 7F         LD      A,A             
4D96: 40         LD      B,B             
4D97: 3F         CCF                     
4D98: 30 0F      JR      NC,$4DA9        
4D9A: 4F         LD      C,A             
4D9B: 30 82      JR      NC,$4D1F        
4D9D: 7D         LD      A,L             
4D9E: FF         RST     0X38            
4D9F: 00         NOP                     
4DA0: 42         LD      B,D             
4DA1: BC         CP      H               
4DA2: 41         LD      B,C             
4DA3: BE         CP      (HL)            
4DA4: 81         ADD     A,C             
4DA5: 7E         LD      A,(HL)          
4DA6: 21 DE 31   LD      HL,$31DE        
4DA9: CE 21      ADC     $21             
4DAB: DE 43      SBC     $43             
4DAD: BC         CP      H               
4DAE: 65         LD      H,L             
4DAF: BA         CP      D               
4DB0: 39         ADD     HL,SP           
4DB1: C6 01      ADD     $01             
4DB3: FE 02      CP      $02             
4DB5: FC         ???                     
4DB6: 04         INC     B               
4DB7: F8 C4      LDHL    SP,$C4          
4DB9: 38 02      JR      C,$4DBD         
4DBB: FC         ???                     
4DBC: 02         LD      (BC),A          
4DBD: FC         ???                     
4DBE: FE 00      CP      $00             
4DC0: 00         NOP                     
4DC1: 00         NOP                     
4DC2: 00         NOP                     
4DC3: 00         NOP                     
4DC4: 00         NOP                     
4DC5: 00         NOP                     
4DC6: 00         NOP                     
4DC7: 00         NOP                     
4DC8: 00         NOP                     
4DC9: 00         NOP                     
4DCA: 00         NOP                     
4DCB: 00         NOP                     
4DCC: 00         NOP                     
4DCD: 00         NOP                     
4DCE: 00         NOP                     
4DCF: 00         NOP                     
4DD0: 18 00      JR      $4DD2           
4DD2: 3C         INC     A               
4DD3: 18 3F      JR      $4E14           
4DD5: 18 3D      JR      $4E14           
4DD7: 16 7D      LD      D,$7D           
4DD9: 02         LD      (BC),A          
4DDA: 53         LD      D,E             
4DDB: 2C         INC     L               
4DDC: 79         LD      A,C             
4DDD: 06 80      LD      B,$80           
4DDF: 7F         LD      A,A             
4DE0: 00         NOP                     
4DE1: 00         NOP                     
4DE2: 00         NOP                     
4DE3: 00         NOP                     
4DE4: 00         NOP                     
4DE5: 00         NOP                     
4DE6: 00         NOP                     
4DE7: 00         NOP                     
4DE8: 00         NOP                     
4DE9: 00         NOP                     
4DEA: 00         NOP                     
4DEB: 00         NOP                     
4DEC: 00         NOP                     
4DED: 00         NOP                     
4DEE: 00         NOP                     
4DEF: 00         NOP                     
4DF0: 70         LD      (HL),B          
4DF1: 00         NOP                     
4DF2: F8 70      LDHL    SP,$70          
4DF4: F8 F0      LDHL    SP,$F0          
4DF6: B8         CP      B               
4DF7: F0 B0      LD      A,($B0)         
4DF9: 60         LD      H,B             
4DFA: F0 E0      LD      A,($E0)         
4DFC: F0 60      LD      A,($60)         
4DFE: E0 00      LDFF00  ($00),A         
4E00: 01 00 01   LD      BC,$0100        
4E03: 00         NOP                     
4E04: 01 00 02   LD      BC,$0200        
4E07: 01 04 03   LD      BC,$0304        
4E0A: 05         DEC     B               
4E0B: 02         LD      (BC),A          
4E0C: 04         INC     B               
4E0D: 03         INC     BC              
4E0E: 02         LD      (BC),A          
4E0F: 01 01 00   LD      BC,$0001        
4E12: 03         INC     BC              
4E13: 00         NOP                     
4E14: 07         RLCA                    
4E15: 03         INC     BC              
4E16: 06 03      LD      B,$03           
4E18: 04         INC     B               
4E19: 03         INC     BC              
4E1A: 04         INC     B               
4E1B: 03         INC     BC              
4E1C: 02         LD      (BC),A          
4E1D: 01 01 00   LD      BC,$0001        
4E20: 58         LD      E,B             
4E21: A7         AND     A               
4E22: 52         LD      D,D             
4E23: AF         XOR     A               
4E24: 06 F9      LD      B,$F9           
4E26: 64         LD      H,H             
4E27: FB         EI                      
4E28: 02         LD      (BC),A          
4E29: FD         ???                     
4E2A: 22         LD      (HLI),A         
4E2B: DD         ???                     
4E2C: 03         INC     BC              
4E2D: FC         ???                     
4E2E: 06 F9      LD      B,$F9           
4E30: F8 07      LDHL    SP,$07          
4E32: 06 F9      LD      B,$F9           
4E34: 8F         ADC     A,A             
4E35: 76         HALT                    
4E36: 53         LD      D,E             
4E37: AE         XOR     (HL)            
4E38: 51         LD      D,C             
4E39: AE         XOR     (HL)            
4E3A: 51         LD      D,C             
4E3B: AE         XOR     (HL)            
4E3C: 73         LD      (HL),E          
4E3D: 8C         ADC     A,H             
4E3E: FF         RST     0X38            
4E3F: 00         NOP                     
4E40: 20 C0      JR      NZ,$4E02        
4E42: 10 E0      STOP    $E0             
4E44: 08 F0 04   LD      ($04F0),SP      
4E47: F8 04      LDHL    SP,$04          
4E49: F8 02      LDHL    SP,$02          
4E4B: FC         ???                     
4E4C: 22         LD      (HLI),A         
4E4D: DC 21 DE   CALL    C,$DE21         
4E50: 31 CE 41   LD      SP,$41CE        
4E53: BE         CP      (HL)            
4E54: 62         LD      H,D             
4E55: BC         CP      H               
4E56: 6E         LD      L,(HL)          
4E57: B0         OR      B               
4E58: 72         LD      (HL),D          
4E59: 8C         ADC     A,H             
4E5A: 06 F8      LD      B,$F8           
4E5C: 1C         INC     E               
4E5D: E0 F0      LDFF00  ($F0),A         
4E5F: 00         NOP                     
4E60: 00         NOP                     
4E61: 00         NOP                     
4E62: 00         NOP                     
4E63: 00         NOP                     
4E64: 00         NOP                     
4E65: 00         NOP                     
4E66: 00         NOP                     
4E67: 00         NOP                     
4E68: 0E 00      LD      C,$00           
4E6A: 0A         LD      A,(BC)          
4E6B: 04         INC     B               
4E6C: 3F         CCF                     
4E6D: 00         NOP                     
4E6E: 7F         LD      A,A             
4E6F: 2D         DEC     L               
4E70: 60         LD      H,B             
4E71: 3F         CCF                     
4E72: 60         LD      H,B             
4E73: 3F         CCF                     
4E74: 60         LD      H,B             
4E75: 3F         CCF                     
4E76: 60         LD      H,B             
4E77: 3F         CCF                     
4E78: 60         LD      H,B             
4E79: 3F         CCF                     
4E7A: 60         LD      H,B             
4E7B: 3F         CCF                     
4E7C: 60         LD      H,B             
4E7D: 3F         CCF                     
4E7E: 60         LD      H,B             
4E7F: 3F         CCF                     
4E80: 60         LD      H,B             
4E81: 3F         CCF                     
4E82: 60         LD      H,B             
4E83: 3F         CCF                     
4E84: 60         LD      H,B             
4E85: 3F         CCF                     
4E86: 60         LD      H,B             
4E87: 3F         CCF                     
4E88: 60         LD      H,B             
4E89: 3F         CCF                     
4E8A: 60         LD      H,B             
4E8B: 3F         CCF                     
4E8C: 5F         LD      E,A             
4E8D: 3F         CCF                     
4E8E: FF         RST     0X38            
4E8F: 00         NOP                     
4E90: C0         RET     NZ              
4E91: 7F         LD      A,A             
4E92: FF         RST     0X38            
4E93: 00         NOP                     
4E94: 0D         DEC     C               
4E95: 00         NOP                     
4E96: 0D         DEC     C               
4E97: 00         NOP                     
4E98: 1D         DEC     E               
4E99: 00         NOP                     
4E9A: 2C         INC     L               
4E9B: 13         INC     DE              
4E9C: 38 07      JR      C,$4EA5         
4E9E: 00         NOP                     
4E9F: 00         NOP                     
4EA0: 01 00 01   LD      BC,$0100        
4EA3: 00         NOP                     
4EA4: 03         INC     BC              
4EA5: 00         NOP                     
4EA6: 04         INC     B               
4EA7: 03         INC     BC              
4EA8: 05         DEC     B               
4EA9: 02         LD      (BC),A          
4EAA: 04         INC     B               
4EAB: 03         INC     BC              
4EAC: 04         INC     B               
4EAD: 03         INC     BC              
4EAE: 02         LD      (BC),A          
4EAF: 01 01 00   LD      BC,$0001        
4EB2: 03         INC     BC              
4EB3: 00         NOP                     
4EB4: 07         RLCA                    
4EB5: 03         INC     BC              
4EB6: 06 03      LD      B,$03           
4EB8: 04         INC     B               
4EB9: 03         INC     BC              
4EBA: 04         INC     B               
4EBB: 03         INC     BC              
4EBC: 02         LD      (BC),A          
4EBD: 01 01 00   LD      BC,$0001        
4EC0: 58         LD      E,B             
4EC1: A7         AND     A               
4EC2: 52         LD      D,D             
4EC3: AF         XOR     A               
4EC4: 66         LD      H,(HL)          
4EC5: F9         LD      SP,HL           
4EC6: 04         INC     B               
4EC7: FB         EI                      
4EC8: 12         LD      (DE),A          
4EC9: ED         ???                     
4ECA: 02         LD      (BC),A          
4ECB: FD         ???                     
4ECC: 03         INC     BC              
4ECD: FC         ???                     
4ECE: 0C         INC     C               
4ECF: F3         DI                      
4ED0: F0 0F      LD      A,($0F)         
4ED2: 06 F9      LD      B,$F9           
4ED4: 8F         ADC     A,A             
4ED5: 76         HALT                    
4ED6: 53         LD      D,E             
4ED7: AE         XOR     (HL)            
4ED8: 51         LD      D,C             
4ED9: AE         XOR     (HL)            
4EDA: 51         LD      D,C             
4EDB: AE         XOR     (HL)            
4EDC: 73         LD      (HL),E          
4EDD: 8C         ADC     A,H             
4EDE: FF         RST     0X38            
4EDF: 00         NOP                     
4EE0: 00         NOP                     
4EE1: FF         RST     0X38            
4EE2: 00         NOP                     
4EE3: FF         RST     0X38            
4EE4: 22         LD      (HLI),A         
4EE5: FF         RST     0X38            
4EE6: 14         INC     D               
4EE7: FF         RST     0X38            
4EE8: 08 FF 14   LD      ($14FF),SP      
4EEB: FF         RST     0X38            
4EEC: 22         LD      (HLI),A         
4EED: FF         RST     0X38            
4EEE: 00         NOP                     
4EEF: FF         RST     0X38            
4EF0: 00         NOP                     
4EF1: FF         RST     0X38            
4EF2: 00         NOP                     
4EF3: FF         RST     0X38            
4EF4: 22         LD      (HLI),A         
4EF5: FF         RST     0X38            
4EF6: 14         INC     D               
4EF7: FF         RST     0X38            
4EF8: 08 FF 14   LD      ($14FF),SP      
4EFB: FF         RST     0X38            
4EFC: 22         LD      (HLI),A         
4EFD: FF         RST     0X38            
4EFE: 00         NOP                     
4EFF: FF         RST     0X38            
4F00: 00         NOP                     
4F01: 00         NOP                     
4F02: 00         NOP                     
4F03: 00         NOP                     
4F04: 00         NOP                     
4F05: 00         NOP                     
4F06: 1B         DEC     DE              
4F07: 00         NOP                     
4F08: 24         INC     H               
4F09: 1B         DEC     DE              
4F0A: 2E 13      LD      L,$13           
4F0C: 30 0F      JR      NC,$4F1D        
4F0E: 20 1F      JR      NZ,$4F2F        
4F10: 73         LD      (HL),E          
4F11: 0C         INC     C               
4F12: 78         LD      A,B             
4F13: 1F         RRA                     
4F14: 7B         LD      A,E             
4F15: 3C         INC     A               
4F16: 5F         LD      E,A             
4F17: 3B         DEC     SP              
4F18: 38 07      JR      C,$4F21         
4F1A: 29         ADD     HL,HL           
4F1B: 16 1C      LD      D,$1C           
4F1D: 03         INC     BC              
4F1E: 07         RLCA                    
4F1F: 00         NOP                     
4F20: 00         NOP                     
4F21: 00         NOP                     
4F22: 00         NOP                     
4F23: 00         NOP                     
4F24: 00         NOP                     
4F25: 00         NOP                     
4F26: 00         NOP                     
4F27: 00         NOP                     
4F28: 80         ADD     A,B             
4F29: 00         NOP                     
4F2A: B8         CP      B               
4F2B: 00         NOP                     
4F2C: 5C         LD      E,H             
4F2D: B8         CP      B               
4F2E: 2C         INC     L               
4F2F: D0         RET     NC              
4F30: 3E CC      LD      A,$CC           
4F32: 27         DAA                     
4F33: DE 07      SBC     $07             
4F35: F8 82      LDHL    SP,$82          
4F37: 7C         LD      A,H             
4F38: 82         ADD     A,D             
4F39: 7C         LD      A,H             
4F3A: 22         LD      (HLI),A         
4F3B: DC 44 B8   CALL    C,$B844         
4F3E: F8 00      LDHL    SP,$00          
4F40: 00         NOP                     
4F41: 00         NOP                     
4F42: 00         NOP                     
4F43: 00         NOP                     
4F44: 06 00      LD      B,$00           
4F46: 09         ADD     HL,BC           
4F47: 06 1D      LD      B,$1D           
4F49: 06 28      LD      B,$28           
4F4B: 17         RLA                     
4F4C: 20 1F      JR      NZ,$4F6D        
4F4E: 33         INC     SP              
4F4F: 0C         INC     C               
4F50: 78         LD      A,B             
4F51: 1F         RRA                     
4F52: 7B         LD      A,E             
4F53: 3C         INC     A               
4F54: 5F         LD      E,A             
4F55: 3B         DEC     SP              
4F56: 28 17      JR      Z,$4F6F         
4F58: 59         LD      E,C             
4F59: 26 48      LD      H,$48           
4F5B: 37         SCF                     
4F5C: 3C         INC     A               
4F5D: 03         INC     BC              
4F5E: 07         RLCA                    
4F5F: 00         NOP                     
4F60: 00         NOP                     
4F61: 00         NOP                     
4F62: 00         NOP                     
4F63: 00         NOP                     
4F64: 00         NOP                     
4F65: 00         NOP                     
4F66: 00         NOP                     
4F67: 00         NOP                     
4F68: 00         NOP                     
4F69: 00         NOP                     
4F6A: 9C         SBC     H               
4F6B: 00         NOP                     
4F6C: 6E         LD      L,(HL)          
4F6D: 9C         SBC     H               
4F6E: 3E C0      LD      A,$C0           
4F70: 2E DC      LD      L,$DC           
4F72: 24         INC     H               
4F73: D8         RET     C               
4F74: 84         ADD     A,H             
4F75: 78         LD      A,B             
4F76: 82         ADD     A,D             
4F77: 7C         LD      A,H             
4F78: 02         LD      (BC),A          
4F79: FC         ???                     
4F7A: 22         LD      (HLI),A         
4F7B: DC 44 B8   CALL    C,$B844         
4F7E: F8 00      LDHL    SP,$00          
4F80: 00         NOP                     
4F81: 00         NOP                     
4F82: 30 00      JR      NC,$4F84        
4F84: 7F         LD      A,A             
4F85: 30 A1      JR      NC,$4F28        
4F87: 5E         LD      E,(HL)          
4F88: 87         ADD     A,A             
4F89: 7F         LD      A,A             
4F8A: BF         CP      A               
4F8B: 40         LD      B,B             
4F8C: A0         AND     B               
4F8D: 5F         LD      E,A             
4F8E: DD         ???                     
4F8F: 02         LD      (BC),A          
4F90: 03         INC     BC              
4F91: 00         NOP                     
4F92: 07         RLCA                    
4F93: 00         NOP                     
4F94: 07         RLCA                    
4F95: 00         NOP                     
4F96: 07         RLCA                    
4F97: 00         NOP                     
4F98: 03         INC     BC              
4F99: 00         NOP                     
4F9A: 07         RLCA                    
4F9B: 02         LD      (BC),A          
4F9C: 07         RLCA                    
4F9D: 00         NOP                     
4F9E: 01 00 60   LD      BC,$6000        
4FA1: 00         NOP                     
4FA2: F0 40      LD      A,($40)         
4FA4: 3E C0      LD      A,$C0           
4FA6: 7C         LD      A,H             
4FA7: 80         ADD     A,B             
4FA8: AE         XOR     (HL)            
4FA9: 70         LD      (HL),B          
4FAA: FC         ???                     
4FAB: 50         LD      D,B             
4FAC: B8         CP      B               
4FAD: 60         LD      H,B             
4FAE: F0 00      LD      A,($00)         
4FB0: FC         ???                     
4FB1: 00         NOP                     
4FB2: D6 28      SUB     $28             
4FB4: D6 28      SUB     $28             
4FB6: A4         AND     H               
4FB7: 58         LD      E,B             
4FB8: FC         ???                     
4FB9: 00         NOP                     
4FBA: F0 00      LD      A,($00)         
4FBC: C8         RET     Z               
4FBD: F0 F8      LD      A,($F8)         
4FBF: 00         NOP                     
4FC0: 18 00      JR      $4FC2           
4FC2: 3E 18      LD      A,$18           
4FC4: 51         LD      D,C             
4FC5: 2E 9C      LD      L,$9C           
4FC7: 7F         LD      A,A             
4FC8: BB         CP      E               
4FC9: 47         LD      B,A             
4FCA: C7         RST     0X00            
4FCB: 00         NOP                     
4FCC: 0E 01      LD      C,$01           
4FCE: 04         INC     B               
4FCF: 03         INC     BC              
4FD0: 09         ADD     HL,BC           
4FD1: 06 0F      LD      B,$0F           
4FD3: 00         NOP                     
4FD4: 07         RLCA                    
4FD5: 00         NOP                     
4FD6: 07         RLCA                    
4FD7: 00         NOP                     
4FD8: 03         INC     BC              
4FD9: 00         NOP                     
4FDA: 07         RLCA                    
4FDB: 02         LD      (BC),A          
4FDC: 07         RLCA                    
4FDD: 00         NOP                     
4FDE: 01 00 30   LD      BC,$3000        
4FE1: 00         NOP                     
4FE2: 78         LD      A,B             
4FE3: 20 9C      JR      NZ,$4F81        
4FE5: 60         LD      H,B             
4FE6: BF         CP      A               
4FE7: 40         LD      B,B             
4FE8: FE 80      CP      $80             
4FEA: C7         RST     0X00            
4FEB: 38 7C      JR      C,$5069         
4FED: 80         ADD     A,B             
4FEE: 78         LD      A,B             
4FEF: 80         ADD     A,B             
4FF0: FC         ???                     
4FF1: 00         NOP                     
4FF2: D6 28      SUB     $28             
4FF4: D6 28      SUB     $28             
4FF6: A4         AND     H               
4FF7: 58         LD      E,B             
4FF8: FC         ???                     
4FF9: 00         NOP                     
4FFA: F0 00      LD      A,($00)         
4FFC: C8         RET     Z               
4FFD: F0 F8      LD      A,($F8)         
4FFF: 00         NOP                     
5000: 06 00      LD      B,$00           
5002: 0E 04      LD      C,$04           
5004: 1E 0C      LD      E,$0C           
5006: 3B         DEC     SP              
5007: 1C         INC     E               
5008: 74         LD      (HL),H          
5009: 3B         DEC     SP              
500A: E8 77      ADD     SP,$77          
500C: FA 05 1A   LD      A,($1A05)       
500F: 05         DEC     B               
5010: 18 07      JR      $5019           
5012: FC         ???                     
5013: 03         INC     BC              
5014: EF         RST     0X28            
5015: 70         LD      (HL),B          
5016: 77         LD      (HL),A          
5017: 38 3B      JR      C,$5054         
5019: 1C         INC     E               
501A: 1E 0C      LD      E,$0C           
501C: 0E 04      LD      C,$04           
501E: 06 00      LD      B,$00           
5020: 00         NOP                     
5021: 00         NOP                     
5022: 01 00 03   LD      BC,$0300        
5025: 01 E3 01   LD      BC,$01E3        
5028: F7         RST     0X30            
5029: 60         LD      H,B             
502A: FF         RST     0X38            
502B: 74         LD      (HL),H          
502C: 7D         LD      A,L             
502D: 2B         DEC     HL              
502E: 78         LD      A,B             
502F: 27         DAA                     
5030: F3         DI                      
5031: 6C         LD      L,H             
5032: F7         RST     0X30            
5033: 69         LD      L,C             
5034: 77         LD      (HL),A          
5035: 28 F7      JR      Z,$502E         
5037: 68         LD      L,B             
5038: F3         DI                      
5039: 8C         ADC     A,H             
503A: F8 E7      LDHL    SP,$E7          
503C: 77         LD      (HL),A          
503D: 78         LD      A,B             
503E: 0F         RRCA                    
503F: 0F         RRCA                    
5040: 00         NOP                     
5041: 00         NOP                     
5042: 07         RLCA                    
5043: 07         RLCA                    
5044: 1F         RRA                     
5045: 1C         INC     E               
5046: 3F         CCF                     
5047: 31 7F 67   LD      SP,$677F        
504A: 7F         LD      A,A             
504B: 6E         LD      L,(HL)          
504C: FF         RST     0X38            
504D: CC FF CD   CALL    Z,$CDFF         
5050: FF         RST     0X38            
5051: 67         LD      H,A             
5052: FF         RST     0X38            
5053: 73         LD      (HL),E          
5054: FF         RST     0X38            
5055: B8         CP      B               
5056: FF         RST     0X38            
5057: 9F         SBC     A               
5058: 7F         LD      A,A             
5059: 47         LD      B,A             
505A: 3F         CCF                     
505B: 30 0F      JR      NC,$506C        
505D: 0F         RRCA                    
505E: 00         NOP                     
505F: 00         NOP                     
5060: 01 00 03   LD      BC,$0300        
5063: 01 E3 01   LD      BC,$01E3        
5066: F7         RST     0X30            
5067: 60         LD      H,B             
5068: FF         RST     0X38            
5069: 70         LD      (HL),B          
506A: 7F         LD      A,A             
506B: 2C         INC     L               
506C: 7F         LD      A,A             
506D: 2E FF      LD      L,$FF           
506F: 6B         LD      L,E             
5070: FF         RST     0X38            
5071: 68         LD      L,B             
5072: 79         LD      A,C             
5073: 27         DAA                     
5074: F3         DI                      
5075: 6C         LD      L,H             
5076: F4         ???                     
5077: 4B         LD      C,E             
5078: F1         POP     AF              
5079: 8E         ADC     A,(HL)          
507A: FF         RST     0X38            
507B: F1         POP     AF              
507C: 3F         CCF                     
507D: 3F         CCF                     
507E: 07         RLCA                    
507F: 07         RLCA                    
5080: 00         NOP                     
5081: 00         NOP                     
5082: 03         INC     BC              
5083: 00         NOP                     
5084: 0C         INC     C               
5085: 03         INC     BC              
5086: 11 0F 13   LD      DE,$130F        
5089: 0F         RRCA                    
508A: 23         INC     HL              
508B: 1D         DEC     E               
508C: 27         DAA                     
508D: 18 27      JR      $50B6           
508F: 18 77      JR      $5108           
5091: 28 73      JR      Z,$5106         
5093: 2C         INC     L               
5094: 5C         LD      E,H             
5095: 33         INC     SP              
5096: 2F         CPL                     
5097: 1C         INC     E               
5098: 7B         LD      A,E             
5099: 07         RLCA                    
509A: 77         LD      (HL),A          
509B: 18 3F      JR      $50DC           
509D: 10 1F      STOP    $1F             
509F: 00         NOP                     
50A0: 03         INC     BC              
50A1: 00         NOP                     
50A2: 77         LD      (HL),A          
50A3: 70         LD      (HL),B          
50A4: 7F         LD      A,A             
50A5: 78         LD      A,B             
50A6: 7F         LD      A,A             
50A7: 78         LD      A,B             
50A8: 3F         CCF                     
50A9: 33         INC     SP              
50AA: 7F         LD      A,A             
50AB: 07         RLCA                    
50AC: FF         RST     0X38            
50AD: 09         ADD     HL,BC           
50AE: FF         RST     0X38            
50AF: 09         ADD     HL,BC           
50B0: FF         RST     0X38            
50B1: 0D         DEC     C               
50B2: FF         RST     0X38            
50B3: 0F         RRCA                    
50B4: 7F         LD      A,A             
50B5: 03         INC     BC              
50B6: 3F         CCF                     
50B7: 32         LD      (HLD),A         
50B8: 7F         LD      A,A             
50B9: 7A         LD      A,D             
50BA: 7F         LD      A,A             
50BB: 78         LD      A,B             
50BC: 77         LD      (HL),A          
50BD: 70         LD      (HL),B          
50BE: 03         INC     BC              
50BF: 00         NOP                     
50C0: 0F         RRCA                    
50C1: 09         ADD     HL,BC           
50C2: 3F         CCF                     
50C3: 18 7F      JR      $5144           
50C5: 03         INC     BC              
50C6: 7F         LD      A,A             
50C7: 4F         LD      C,A             
50C8: FF         RST     0X38            
50C9: D3         ???                     
50CA: FF         RST     0X38            
50CB: 19         ADD     HL,DE           
50CC: FF         RST     0X38            
50CD: 3D         DEC     A               
50CE: FF         RST     0X38            
50CF: AF         XOR     A               
50D0: FF         RST     0X38            
50D1: A7         AND     A               
50D2: FF         RST     0X38            
50D3: 39         ADD     HL,SP           
50D4: FF         RST     0X38            
50D5: 1C         INC     E               
50D6: FF         RST     0X38            
50D7: DE 7F      SBC     $7F             
50D9: 4F         LD      C,A             
50DA: 7F         LD      A,A             
50DB: 03         INC     BC              
50DC: 3F         CCF                     
50DD: 18 0F      JR      $50EE           
50DF: 09         ADD     HL,BC           
50E0: 1F         RRA                     
50E1: 00         NOP                     
50E2: 3F         CCF                     
50E3: 1F         RRA                     
50E4: 5F         LD      E,A             
50E5: 3F         CCF                     
50E6: 9F         SBC     A               
50E7: 60         LD      H,B             
50E8: A0         AND     B               
50E9: 5F         LD      E,A             
50EA: C0         RET     NZ              
50EB: 3F         CCF                     
50EC: 9B         SBC     E               
50ED: 64         LD      H,H             
50EE: 9F         SBC     A               
50EF: 78         LD      A,B             
50F0: 87         ADD     A,A             
50F1: 78         LD      A,B             
50F2: B7         OR      A               
50F3: 48         LD      C,B             
50F4: B7         OR      A               
50F5: 78         LD      A,B             
50F6: 87         ADD     A,A             
50F7: 7C         LD      A,H             
50F8: BB         CP      E               
50F9: 46         LD      B,(HL)          
50FA: B9         CP      C               
50FB: 7F         LD      A,A             
50FC: 80         ADD     A,B             
50FD: 7F         LD      A,A             
50FE: FF         RST     0X38            
50FF: 00         NOP                     
5100: 00         NOP                     
5101: 00         NOP                     
5102: 00         NOP                     
5103: 00         NOP                     
5104: 00         NOP                     
5105: 00         NOP                     
5106: 0F         RRCA                    
5107: 00         NOP                     
5108: 3F         CCF                     
5109: 00         NOP                     
510A: 3F         CCF                     
510B: 00         NOP                     
510C: 1F         RRA                     
510D: 01 07 03   LD      BC,$0307        
5110: 7F         LD      A,A             
5111: 02         LD      (BC),A          
5112: A7         AND     A               
5113: 58         LD      E,B             
5114: 81         ADD     A,C             
5115: 7E         LD      A,(HL)          
5116: F8 07      LDHL    SP,$07          
5118: 7D         LD      A,L             
5119: 3A         LD      A,(HLD)         
511A: 5F         LD      E,A             
511B: 3D         DEC     A               
511C: 37         SCF                     
511D: 0E 0B      LD      C,$0B           
511F: 07         RLCA                    
5120: 00         NOP                     
5121: 00         NOP                     
5122: 7C         LD      A,H             
5123: 00         NOP                     
5124: B2         OR      D               
5125: 7C         LD      A,H             
5126: F9         LD      SP,HL           
5127: 06 FF      LD      B,$FF           
5129: 00         NOP                     
512A: FF         RST     0X38            
512B: 00         NOP                     
512C: FF         RST     0X38            
512D: 60         LD      H,B             
512E: FF         RST     0X38            
512F: F0 FF      LD      A,($FF)         
5131: B0         OR      B               
5132: E3         ???                     
5133: 1C         INC     E               
5134: 00         NOP                     
5135: FF         RST     0X38            
5136: 04         INC     B               
5137: FB         EI                      
5138: 3F         CCF                     
5139: C3 FF 2F   JP      $2FFF           
513C: F6 D9      OR      $D9             
513E: E9         JP      (HL)            
513F: F6 00      OR      $00             
5141: 00         NOP                     
5142: 00         NOP                     
5143: 00         NOP                     
5144: 00         NOP                     
5145: 00         NOP                     
5146: 00         NOP                     
5147: 00         NOP                     
5148: 00         NOP                     
5149: 00         NOP                     
514A: C0         RET     NZ              
514B: 00         NOP                     
514C: E0 00      LDFF00  ($00),A         
514E: E0 00      LDFF00  ($00),A         
5150: CC 00 0E   CALL    Z,$0E00         
5153: 04         INC     B               
5154: 8E         ADC     A,(HL)          
5155: 04         INC     B               
5156: 5E         LD      E,(HL)          
5157: 8C         ADC     A,H             
5158: 5E         LD      E,(HL)          
5159: 8C         ADC     A,H             
515A: 7A         LD      A,D             
515B: 9C         SBC     H               
515C: F6 38      OR      $38             
515E: EA 74 0E   LD      ($0E74),A       
5161: 01 0B 04   LD      BC,$040B        
5164: 13         INC     DE              
5165: 0D         DEC     C               
5166: 12         LD      (DE),A          
5167: 0D         DEC     C               
5168: 0F         RRCA                    
5169: 00         NOP                     
516A: 1D         DEC     E               
516B: 06 3C      LD      B,$3C           
516D: 1F         RRA                     
516E: 3F         CCF                     
516F: 00         NOP                     
5170: 00         NOP                     
5171: 00         NOP                     
5172: 00         NOP                     
5173: 00         NOP                     
5174: 00         NOP                     
5175: 00         NOP                     
5176: 00         NOP                     
5177: 00         NOP                     
5178: 00         NOP                     
5179: 00         NOP                     
517A: 00         NOP                     
517B: 00         NOP                     
517C: 00         NOP                     
517D: 00         NOP                     
517E: 00         NOP                     
517F: 00         NOP                     
5180: 38 C7      JR      C,$5149         
5182: C4 3B 40   CALL    NZ,$403B        
5185: BF         CP      A               
5186: 61         LD      H,C             
5187: 9E         SBC     (HL)            
5188: FF         RST     0X38            
5189: 00         NOP                     
518A: F0 1F      LD      A,($1F)         
518C: F8 7F      LDHL    SP,$7F          
518E: FF         RST     0X38            
518F: 00         NOP                     
5190: 00         NOP                     
5191: 00         NOP                     
5192: 00         NOP                     
5193: 00         NOP                     
5194: 00         NOP                     
5195: 00         NOP                     
5196: 00         NOP                     
5197: 00         NOP                     
5198: 00         NOP                     
5199: 00         NOP                     
519A: 00         NOP                     
519B: 00         NOP                     
519C: 00         NOP                     
519D: 00         NOP                     
519E: 00         NOP                     
519F: 00         NOP                     
51A0: B2         OR      D               
51A1: 4C         LD      C,H             
51A2: C2 3C 84   JP      NZ,$843C        
51A5: 78         LD      A,B             
51A6: 84         ADD     A,H             
51A7: 78         LD      A,B             
51A8: 08 F0 B0   LD      ($B0F0),SP      
51AB: 40         LD      B,B             
51AC: 40         LD      B,B             
51AD: 80         ADD     A,B             
51AE: C0         RET     NZ              
51AF: 00         NOP                     
51B0: 00         NOP                     
51B1: 00         NOP                     
51B2: 00         NOP                     
51B3: 00         NOP                     
51B4: 00         NOP                     
51B5: 00         NOP                     
51B6: 00         NOP                     
51B7: 00         NOP                     
51B8: 00         NOP                     
51B9: 00         NOP                     
51BA: 00         NOP                     
51BB: 00         NOP                     
51BC: 00         NOP                     
51BD: 00         NOP                     
51BE: 00         NOP                     
51BF: 00         NOP                     
51C0: 00         NOP                     
51C1: 00         NOP                     
51C2: 00         NOP                     
51C3: 00         NOP                     
51C4: 00         NOP                     
51C5: 00         NOP                     
51C6: 00         NOP                     
51C7: 00         NOP                     
51C8: 00         NOP                     
51C9: 00         NOP                     
51CA: C0         RET     NZ              
51CB: 00         NOP                     
51CC: E0 00      LDFF00  ($00),A         
51CE: E0 00      LDFF00  ($00),A         
51D0: C0         RET     NZ              
51D1: 00         NOP                     
51D2: 00         NOP                     
51D3: 00         NOP                     
51D4: 80         ADD     A,B             
51D5: 00         NOP                     
51D6: 40         LD      B,B             
51D7: 80         ADD     A,B             
51D8: 40         LD      B,B             
51D9: 80         ADD     A,B             
51DA: 40         LD      B,B             
51DB: 80         ADD     A,B             
51DC: 80         ADD     A,B             
51DD: 00         NOP                     
51DE: 00         NOP                     
51DF: 00         NOP                     
51E0: C0         RET     NZ              
51E1: 00         NOP                     
51E2: E0 40      LDFF00  ($40),A         
51E4: B8         CP      B               
51E5: 60         LD      H,B             
51E6: DE 38      SBC     $38             
51E8: 37         SCF                     
51E9: CE 8F      ADC     $8F             
51EB: 70         LD      (HL),B          
51EC: 40         LD      B,B             
51ED: BF         CP      A               
51EE: FF         RST     0X38            
51EF: 00         NOP                     
51F0: 00         NOP                     
51F1: 00         NOP                     
51F2: 00         NOP                     
51F3: 00         NOP                     
51F4: 00         NOP                     
51F5: 00         NOP                     
51F6: 00         NOP                     
51F7: 00         NOP                     
51F8: 00         NOP                     
51F9: 00         NOP                     
51FA: 00         NOP                     
51FB: 00         NOP                     
51FC: 00         NOP                     
51FD: 00         NOP                     
51FE: 00         NOP                     
51FF: 00         NOP                     
5200: 00         NOP                     
5201: 00         NOP                     
5202: 00         NOP                     
5203: 00         NOP                     
5204: 00         NOP                     
5205: 00         NOP                     
5206: 00         NOP                     
5207: 00         NOP                     
5208: 80         ADD     A,B             
5209: 00         NOP                     
520A: E0 00      LDFF00  ($00),A         
520C: 10 E0      STOP    $E0             
520E: F0 00      LD      A,($00)         
5210: 00         NOP                     
5211: 00         NOP                     
5212: 00         NOP                     
5213: 00         NOP                     
5214: 00         NOP                     
5215: 00         NOP                     
5216: 00         NOP                     
5217: 00         NOP                     
5218: 00         NOP                     
5219: 00         NOP                     
521A: 00         NOP                     
521B: 00         NOP                     
521C: 00         NOP                     
521D: 00         NOP                     
521E: 00         NOP                     
521F: 00         NOP                     
5220: 00         NOP                     
5221: 00         NOP                     
5222: 07         RLCA                    
5223: 00         NOP                     
5224: 0F         RRCA                    
5225: 00         NOP                     
5226: 0F         RRCA                    
5227: 00         NOP                     
5228: 0F         RRCA                    
5229: 00         NOP                     
522A: 07         RLCA                    
522B: 00         NOP                     
522C: 3F         CCF                     
522D: 01 53 2C   LD      BC,$2C53        
5230: 40         LD      B,B             
5231: 3F         CCF                     
5232: 78         LD      A,B             
5233: 07         RLCA                    
5234: 7C         LD      A,H             
5235: 2B         DEC     HL              
5236: 2F         CPL                     
5237: 00         NOP                     
5238: 07         RLCA                    
5239: 00         NOP                     
523A: 03         INC     BC              
523B: 00         NOP                     
523C: 3F         CCF                     
523D: 01 3F 1E   LD      BC,$1E3F        
5240: 1E 00      LD      E,$00           
5242: ED         ???                     
5243: 1E F8      LD      E,$F8           
5245: 07         RLCA                    
5246: FE 01      CP      $01             
5248: FF         RST     0X38            
5249: 00         NOP                     
524A: FF         RST     0X38            
524B: B0         OR      B               
524C: FF         RST     0X38            
524D: F8 FF      LDHL    SP,$FF          
524F: 58         LD      E,B             
5250: F3         DI                      
5251: 0C         INC     C               
5252: 01 FE 25   LD      BC,$25FE        
5255: DA FE 23   JP      C,$23FE         
5258: FE 07      CP      $07             
525A: FE 0F      CP      $0F             
525C: F6 19      OR      $19             
525E: E9         JP      (HL)            
525F: F6 00      OR      $00             
5261: 00         NOP                     
5262: 00         NOP                     
5263: 00         NOP                     
5264: 80         ADD     A,B             
5265: 00         NOP                     
5266: 80         ADD     A,B             
5267: 00         NOP                     
5268: 80         ADD     A,B             
5269: 00         NOP                     
526A: 80         ADD     A,B             
526B: 00         NOP                     
526C: C0         RET     NZ              
526D: 00         NOP                     
526E: E0 00      LDFF00  ($00),A         
5270: E0 00      LDFF00  ($00),A         
5272: C0         RET     NZ              
5273: 00         NOP                     
5274: 80         ADD     A,B             
5275: 00         NOP                     
5276: 80         ADD     A,B             
5277: 00         NOP                     
5278: 80         ADD     A,B             
5279: 00         NOP                     
527A: 80         ADD     A,B             
527B: 00         NOP                     
527C: 80         ADD     A,B             
527D: 00         NOP                     
527E: 80         ADD     A,B             
527F: 00         NOP                     
5280: 2F         CPL                     
5281: 1F         RRA                     
5282: 1F         RRA                     
5283: 00         NOP                     
5284: 13         INC     DE              
5285: 0D         DEC     C               
5286: 12         LD      (DE),A          
5287: 0D         DEC     C               
5288: 0F         RRCA                    
5289: 00         NOP                     
528A: 1D         DEC     E               
528B: 06 3C      LD      B,$3C           
528D: 1F         RRA                     
528E: 3F         CCF                     
528F: 00         NOP                     
5290: 00         NOP                     
5291: 00         NOP                     
5292: 00         NOP                     
5293: 00         NOP                     
5294: 00         NOP                     
5295: 00         NOP                     
5296: 00         NOP                     
5297: 00         NOP                     
5298: 00         NOP                     
5299: 00         NOP                     
529A: 00         NOP                     
529B: 00         NOP                     
529C: 00         NOP                     
529D: 00         NOP                     
529E: 00         NOP                     
529F: 00         NOP                     
52A0: 00         NOP                     
52A1: 00         NOP                     
52A2: 00         NOP                     
52A3: 00         NOP                     
52A4: 00         NOP                     
52A5: 00         NOP                     
52A6: 00         NOP                     
52A7: 00         NOP                     
52A8: 00         NOP                     
52A9: 00         NOP                     
52AA: 00         NOP                     
52AB: 00         NOP                     
52AC: 00         NOP                     
52AD: 00         NOP                     
52AE: 00         NOP                     
52AF: 00         NOP                     
52B0: 00         NOP                     
52B1: 00         NOP                     
52B2: 00         NOP                     
52B3: 00         NOP                     
52B4: 07         RLCA                    
52B5: 00         NOP                     
52B6: 07         RLCA                    
52B7: 03         INC     BC              
52B8: 02         LD      (BC),A          
52B9: 01 03 00   LD      BC,$0003        
52BC: 3F         CCF                     
52BD: 02         LD      (BC),A          
52BE: 3F         CCF                     
52BF: 1C         INC     E               
52C0: 3F         CCF                     
52C1: 00         NOP                     
52C2: 7E         LD      A,(HL)          
52C3: 2D         DEC     L               
52C4: 2A         LD      A,(HLI)         
52C5: 15         DEC     D               
52C6: 3C         INC     A               
52C7: 03         INC     BC              
52C8: 7C         LD      A,H             
52C9: 2B         DEC     HL              
52CA: 3C         INC     A               
52CB: 03         INC     BC              
52CC: 7C         LD      A,H             
52CD: 2B         DEC     HL              
52CE: 39         ADD     HL,SP           
52CF: 06 79      LD      B,$79           
52D1: 06 FB      LD      B,$FB           
52D3: 54         LD      D,H             
52D4: F1         POP     AF              
52D5: 0E 71      LD      C,$71           
52D7: 8E         ADC     A,(HL)          
52D8: DE E7      SBC     $E7             
52DA: 3E CF      LD      A,$CF           
52DC: FE 39      CP      $39             
52DE: F9         LD      SP,HL           
52DF: F6 00      OR      $00             
52E1: 00         NOP                     
52E2: 80         ADD     A,B             
52E3: 00         NOP                     
52E4: 40         LD      B,B             
52E5: 80         ADD     A,B             
52E6: 40         LD      B,B             
52E7: 80         ADD     A,B             
52E8: F0 00      LD      A,($00)         
52EA: F8 00      LDHL    SP,$00          
52EC: F8 00      LDHL    SP,$00          
52EE: FC         ???                     
52EF: 00         NOP                     
52F0: 7C         LD      A,H             
52F1: 80         ADD     A,B             
52F2: FE 40      CP      $40             
52F4: FF         RST     0X38            
52F5: C2 7F 82   JP      NZ,$827F        
52F8: F9         LD      SP,HL           
52F9: 06 FA      LD      B,$FA           
52FB: 04         INC     B               
52FC: FC         ???                     
52FD: 00         NOP                     
52FE: E0 00      LDFF00  ($00),A         
5300: 03         INC     BC              
5301: 00         NOP                     
5302: 07         RLCA                    
5303: 00         NOP                     
5304: 0F         RRCA                    
5305: 00         NOP                     
5306: 0F         RRCA                    
5307: 07         RLCA                    
5308: 1F         RRA                     
5309: 0B         DEC     BC              
530A: 1F         RRA                     
530B: 0B         DEC     BC              
530C: 0F         RRCA                    
530D: 07         RLCA                    
530E: 1F         RRA                     
530F: 0F         RRCA                    
5310: 16 0F      LD      D,$0F           
5312: 2F         CPL                     
5313: 10 27      STOP    $27             
5315: 19         ADD     HL,DE           
5316: 2F         CPL                     
5317: 14         INC     D               
5318: 1F         RRA                     
5319: 06 0F      LD      B,$0F           
531B: 00         NOP                     
531C: 1C         INC     E               
531D: 0F         RRCA                    
531E: 1F         RRA                     
531F: 00         NOP                     
5320: E0 00      LDFF00  ($00),A         
5322: F0 00      LD      A,($00)         
5324: F8 80      LDHL    SP,$80          
5326: FC         ???                     
5327: D8         RET     C               
5328: FC         ???                     
5329: 58         LD      E,B             
532A: F4         ???                     
532B: 78         LD      A,B             
532C: E8 F0      ADD     SP,$F0          
532E: F8 20      LDHL    SP,$20          
5330: F4         ???                     
5331: 28 E4      JR      Z,$5317         
5333: 58         LD      E,B             
5334: E4         ???                     
5335: 98         SBC     B               
5336: F4         ???                     
5337: 68         LD      L,B             
5338: F8 60      LDHL    SP,$60          
533A: F8 00      LDHL    SP,$00          
533C: 9C         SBC     H               
533D: 78         LD      A,B             
533E: FC         ???                     
533F: 00         NOP                     
5340: 07         RLCA                    
5341: 00         NOP                     
5342: 0F         RRCA                    
5343: 00         NOP                     
5344: 0F         RRCA                    
5345: 07         RLCA                    
5346: 0D         DEC     C               
5347: 03         INC     BC              
5348: 3F         CCF                     
5349: 0F         RRCA                    
534A: FF         RST     0X38            
534B: 2F         CPL                     
534C: F5         PUSH    AF              
534D: 6E         LD      L,(HL)          
534E: FF         RST     0X38            
534F: 60         LD      H,B             
5350: 7F         LD      A,A             
5351: 00         NOP                     
5352: 4F         LD      C,A             
5353: 37         SCF                     
5354: 2F         CPL                     
5355: 13         INC     DE              
5356: 1F         RRA                     
5357: 00         NOP                     
5358: 0C         INC     C               
5359: 03         INC     BC              
535A: 0F         RRCA                    
535B: 00         NOP                     
535C: 1C         INC     E               
535D: 0F         RRCA                    
535E: 1F         RRA                     
535F: 00         NOP                     
5360: E0 00      LDFF00  ($00),A         
5362: F0 80      LD      A,($80)         
5364: F0 C0      LD      A,($C0)         
5366: F8 40      LDHL    SP,$40          
5368: FC         ???                     
5369: 58         LD      E,B             
536A: FC         ???                     
536B: F8 F4      LDHL    SP,$F4          
536D: 78         LD      A,B             
536E: F8 60      LDHL    SP,$60          
5370: F4         ???                     
5371: C8         RET     Z               
5372: E4         ???                     
5373: 98         SBC     B               
5374: E4         ???                     
5375: 18 F4      JR      $536B           
5377: 68         LD      L,B             
5378: F8 60      LDHL    SP,$60          
537A: F8 00      LDHL    SP,$00          
537C: 9C         SBC     H               
537D: 78         LD      A,B             
537E: FC         ???                     
537F: 00         NOP                     
5380: 37         SCF                     
5381: 00         NOP                     
5382: 7F         LD      A,A             
5383: 31 7F 37   LD      SP,$377F        
5386: 7D         LD      A,L             
5387: 23         INC     HL              
5388: 7F         LD      A,A             
5389: 0F         RRCA                    
538A: 5F         LD      E,A             
538B: 2F         CPL                     
538C: 5F         LD      E,A             
538D: 2E 2F      LD      L,$2F           
538F: 10 2F      STOP    $2F             
5391: 10 1F      STOP    $1F             
5393: 05         DEC     B               
5394: 6F         LD      L,A             
5395: 05         DEC     B               
5396: FE 63      CP      $63             
5398: FF         RST     0X38            
5399: 70         LD      (HL),B          
539A: 7F         LD      A,A             
539B: 30 3F      JR      NC,$53DC        
539D: 00         NOP                     
539E: 00         NOP                     
539F: 00         NOP                     
53A0: D8         RET     C               
53A1: 00         NOP                     
53A2: FC         ???                     
53A3: 18 FE      JR      $53A3           
53A5: 9C         SBC     H               
53A6: FE 44      CP      $44             
53A8: F6 48      OR      $48             
53AA: F2         ???                     
53AB: EC         ???                     
53AC: F2         ???                     
53AD: 6C         LD      L,H             
53AE: E4         ???                     
53AF: 58         LD      E,B             
53B0: E4         ???                     
53B1: D8         RET     C               
53B2: E8 90      ADD     SP,$90          
53B4: 78         LD      A,B             
53B5: 80         ADD     A,B             
53B6: F8 30      LDHL    SP,$30          
53B8: F8 70      LDHL    SP,$70          
53BA: F0 60      LD      A,($60)         
53BC: E0 00      LDFF00  ($00),A         
53BE: 00         NOP                     
53BF: 00         NOP                     
53C0: 37         SCF                     
53C1: 00         NOP                     
53C2: 7F         LD      A,A             
53C3: 31 7F 37   LD      SP,$377F        
53C6: 7D         LD      A,L             
53C7: 23         INC     HL              
53C8: 7F         LD      A,A             
53C9: 0F         RRCA                    
53CA: 5F         LD      E,A             
53CB: 2F         CPL                     
53CC: 5F         LD      E,A             
53CD: 2E 2F      LD      L,$2F           
53CF: 10 2F      STOP    $2F             
53D1: 10 1F      STOP    $1F             
53D3: 07         RLCA                    
53D4: 0F         RRCA                    
53D5: 03         INC     BC              
53D6: 0F         RRCA                    
53D7: 00         NOP                     
53D8: 06 01      LD      B,$01           
53DA: 07         RLCA                    
53DB: 00         NOP                     
53DC: 03         INC     BC              
53DD: 01 01 00   LD      BC,$0001        
53E0: D8         RET     C               
53E1: 00         NOP                     
53E2: FC         ???                     
53E3: 18 FE      JR      $53E3           
53E5: 9C         SBC     H               
53E6: FE 44      CP      $44             
53E8: F6 48      OR      $48             
53EA: F2         ???                     
53EB: EC         ???                     
53EC: F2         ???                     
53ED: 6C         LD      L,H             
53EE: E4         ???                     
53EF: 58         LD      E,B             
53F0: E4         ???                     
53F1: D8         RET     C               
53F2: E8 90      ADD     SP,$90          
53F4: F8 00      LDHL    SP,$00          
53F6: F8 00      LDHL    SP,$00          
53F8: 7C         LD      A,H             
53F9: 80         ADD     A,B             
53FA: FE 04      CP      $04             
53FC: FE DC      CP      $DC             
53FE: DC 00 00   CALL    C,$0000         
5401: 00         NOP                     
5402: 00         NOP                     
5403: 00         NOP                     
5404: 00         NOP                     
5405: 00         NOP                     
5406: 00         NOP                     
5407: 00         NOP                     
5408: 01 00 03   LD      BC,$0300        
540B: 04         INC     B               
540C: 1E 01      LD      E,$01           
540E: 3F         CCF                     
540F: 0D         DEC     C               
5410: 3F         CCF                     
5411: 1D         DEC     E               
5412: 3F         CCF                     
5413: 1D         DEC     E               
5414: 2E 1D      LD      L,$1D           
5416: 13         INC     DE              
5417: 0C         INC     C               
5418: 0F         RRCA                    
5419: 00         NOP                     
541A: 00         NOP                     
541B: 00         NOP                     
541C: 00         NOP                     
541D: 00         NOP                     
541E: 00         NOP                     
541F: 00         NOP                     
5420: 00         NOP                     
5421: 00         NOP                     
5422: 00         NOP                     
5423: 00         NOP                     
5424: 00         NOP                     
5425: 00         NOP                     
5426: 00         NOP                     
5427: 00         NOP                     
5428: C3 00 24   JP      $2400           
542B: DB         ???                     
542C: A5         AND     L               
542D: DB         ???                     
542E: E7         RST     0X20            
542F: DB         ???                     
5430: FF         RST     0X38            
5431: C3 DB E7   JP      $E7DB           
5434: DB         ???                     
5435: E7         RST     0X20            
5436: DB         ???                     
5437: E7         RST     0X20            
5438: 5A         LD      E,D             
5439: E7         RST     0X20            
543A: 99         SBC     C               
543B: 66         LD      H,(HL)          
543C: 7F         LD      A,A             
543D: 00         NOP                     
543E: 00         NOP                     
543F: 00         NOP                     
5440: 00         NOP                     
5441: 00         NOP                     
5442: 00         NOP                     
5443: 00         NOP                     
5444: 03         INC     BC              
5445: 00         NOP                     
5446: 0C         INC     C               
5447: 03         INC     BC              
5448: 11 0F 30   LD      DE,$300F        
544B: 0F         RRCA                    
544C: 40         LD      B,B             
544D: 3F         CCF                     
544E: 6E         LD      L,(HL)          
544F: 3F         CCF                     
5450: 6F         LD      L,A             
5451: 33         INC     SP              
5452: 3F         CCF                     
5453: 0B         DEC     BC              
5454: 57         LD      D,A             
5455: 2F         CPL                     
5456: 4B         LD      C,E             
5457: 36 77      LD      (HL),$77        
5459: 08 F7 6E   LD      ($6EF7),SP      
545C: FF         RST     0X38            
545D: 06 07      LD      B,$07           
545F: 00         NOP                     
5460: 0F         RRCA                    
5461: 00         NOP                     
5462: 13         INC     DE              
5463: 0F         RRCA                    
5464: 60         LD      H,B             
5465: 1F         RRA                     
5466: 80         ADD     A,B             
5467: 7F         LD      A,A             
5468: DD         ???                     
5469: 7F         LD      A,A             
546A: DF         RST     0X18            
546B: 67         LD      H,A             
546C: 7F         LD      A,A             
546D: 17         RLA                     
546E: AF         XOR     A               
546F: 5F         LD      E,A             
5470: B7         OR      A               
5471: 4D         LD      C,L             
5472: 9F         SBC     A               
5473: 60         LD      H,B             
5474: 9F         SBC     A               
5475: 7D         LD      A,L             
5476: 5F         LD      E,A             
5477: 3B         DEC     SP              
5478: 39         ADD     HL,SP           
5479: 07         RLCA                    
547A: 40         LD      B,B             
547B: 3F         CCF                     
547C: F3         DI                      
547D: 7C         LD      A,H             
547E: FC         ???                     
547F: 00         NOP                     
5480: D1         POP     DE              
5481: 0E 31      LD      C,$31           
5483: CE 19      ADC     $19             
5485: E6 05      AND     $05             
5487: FA DD FA   LD      A,($FADD)       
548A: DD         ???                     
548B: 3A         LD      A,(HLD)         
548C: DA 64 D2   JP      C,$D264         
548F: EC         ???                     
5490: A4         AND     H               
5491: D8         RET     C               
5492: E4         ???                     
5493: 38 F2      JR      C,$5487         
5495: FC         ???                     
5496: F2         ???                     
5497: FC         ???                     
5498: E6 F8      AND     $F8             
549A: 07         RLCA                    
549B: FE FF      CP      $FF             
549D: 00         NOP                     
549E: 00         NOP                     
549F: 00         NOP                     
54A0: 00         NOP                     
54A1: 00         NOP                     
54A2: 00         NOP                     
54A3: 00         NOP                     
54A4: 00         NOP                     
54A5: 00         NOP                     
54A6: 00         NOP                     
54A7: 00         NOP                     
54A8: 00         NOP                     
54A9: 00         NOP                     
54AA: 00         NOP                     
54AB: 00         NOP                     
54AC: 00         NOP                     
54AD: 00         NOP                     
54AE: 00         NOP                     
54AF: 00         NOP                     
54B0: 00         NOP                     
54B1: 00         NOP                     
54B2: 00         NOP                     
54B3: 00         NOP                     
54B4: 3C         INC     A               
54B5: 00         NOP                     
54B6: 7A         LD      A,D             
54B7: 3C         INC     A               
54B8: 7E         LD      A,(HL)          
54B9: 1C         INC     E               
54BA: 7D         LD      A,L             
54BB: 3E 31      LD      A,$31           
54BD: 0E 11      LD      C,$11           
54BF: 0E 00      LD      C,$00           
54C1: 00         NOP                     
54C2: 00         NOP                     
54C3: 00         NOP                     
54C4: 03         INC     BC              
54C5: 00         NOP                     
54C6: 0D         DEC     C               
54C7: 03         INC     BC              
54C8: 17         RLA                     
54C9: 0F         RRCA                    
54CA: 1C         INC     E               
54CB: 0F         RRCA                    
54CC: 28 1F      JR      Z,$54ED         
54CE: 38 1F      JR      C,$54EF         
54D0: 30 1F      JR      NC,$54F1        
54D2: 30 1F      JR      NC,$54F3        
54D4: 20 1F      JR      NZ,$54F5        
54D6: 27         DAA                     
54D7: 18 18      JR      $54F1           
54D9: 07         RLCA                    
54DA: 0F         RRCA                    
54DB: 00         NOP                     
54DC: 00         NOP                     
54DD: 00         NOP                     
54DE: 00         NOP                     
54DF: 00         NOP                     
54E0: 00         NOP                     
54E1: 00         NOP                     
54E2: 00         NOP                     
54E3: 00         NOP                     
54E4: F0 00      LD      A,($00)         
54E6: C8         RET     Z               
54E7: F0 08      LD      A,($08)         
54E9: F0 14      LD      A,($14)         
54EB: E8 14      ADD     SP,$14          
54ED: E8 14      ADD     SP,$14          
54EF: E8 14      ADD     SP,$14          
54F1: E8 24      ADD     SP,$24          
54F3: D8         RET     C               
54F4: 48         LD      C,B             
54F5: B0         OR      B               
54F6: 88         ADC     A,B             
54F7: 70         LD      (HL),B          
54F8: 30 C0      JR      NC,$54BA        
54FA: C0         RET     NZ              
54FB: 00         NOP                     
54FC: 00         NOP                     
54FD: 00         NOP                     
54FE: 00         NOP                     
54FF: 00         NOP                     
5500: FF         RST     0X38            
5501: 7E         LD      A,(HL)          
5502: FF         RST     0X38            
5503: 7E         LD      A,(HL)          
5504: 81         ADD     A,C             
5505: 7E         LD      A,(HL)          
5506: FF         RST     0X38            
5507: 00         NOP                     
5508: FC         ???                     
5509: 7B         LD      A,E             
550A: 85         ADD     A,L             
550B: 7A         LD      A,D             
550C: 86         ADD     A,(HL)          
550D: 79         LD      A,C             
550E: FC         ???                     
550F: 03         INC     BC              
5510: 7C         LD      A,H             
5511: 3B         DEC     SP              
5512: 45         LD      B,L             
5513: 3A         LD      A,(HLD)         
5514: 7D         LD      A,L             
5515: 02         LD      (BC),A          
5516: 7C         LD      A,H             
5517: 3B         DEC     SP              
5518: 44         LD      B,H             
5519: 3B         DEC     SP              
551A: 7F         LD      A,A             
551B: 00         NOP                     
551C: 7F         LD      A,A             
551D: 3E 7F      LD      A,$7F           
551F: 00         NOP                     
5520: FF         RST     0X38            
5521: FB         EI                      
5522: FF         RST     0X38            
5523: FB         EI                      
5524: 04         INC     B               
5525: FB         EI                      
5526: FF         RST     0X38            
5527: 00         NOP                     
5528: 00         NOP                     
5529: FF         RST     0X38            
552A: E0 1F      LDFF00  ($1F),A         
552C: D3         ???                     
552D: 2C         INC     L               
552E: 06 F9      LD      B,$F9           
5530: FF         RST     0X38            
5531: 00         NOP                     
5532: 52         LD      D,D             
5533: AD         XOR     L               
5534: B3         OR      E               
5535: 4C         LD      C,H             
5536: FF         RST     0X38            
5537: 00         NOP                     
5538: 06 F9      LD      B,$F9           
553A: FF         RST     0X38            
553B: 00         NOP                     
553C: FF         RST     0X38            
553D: F7         RST     0X30            
553E: FF         RST     0X38            
553F: 00         NOP                     
5540: FF         RST     0X38            
5541: DF         RST     0X18            
5542: FF         RST     0X38            
5543: DF         RST     0X18            
5544: 20 DF      JR      NZ,$5525        
5546: FF         RST     0X38            
5547: 00         NOP                     
5548: 55         LD      D,L             
5549: AA         XOR     D               
554A: 00         NOP                     
554B: FF         RST     0X38            
554C: 55         LD      D,L             
554D: AA         XOR     D               
554E: 00         NOP                     
554F: FF         RST     0X38            
5550: F9         LD      SP,HL           
5551: 06 DF      LD      B,$DF           
5553: 20 2F      JR      NZ,$5584        
5555: D0         RET     NC              
5556: F9         LD      SP,HL           
5557: 06 00      LD      B,$00           
5559: FF         RST     0X38            
555A: FF         RST     0X38            
555B: 00         NOP                     
555C: FF         RST     0X38            
555D: EF         RST     0X28            
555E: FF         RST     0X38            
555F: 00         NOP                     
5560: FF         RST     0X38            
5561: 7E         LD      A,(HL)          
5562: FF         RST     0X38            
5563: 7E         LD      A,(HL)          
5564: 81         ADD     A,C             
5565: 7E         LD      A,(HL)          
5566: FF         RST     0X38            
5567: 00         NOP                     
5568: 3F         CCF                     
5569: DE 21      SBC     $21             
556B: DE 21      SBC     $21             
556D: DE BF      SBC     $BF             
556F: 40         LD      B,B             
5570: BE         CP      (HL)            
5571: 5C         LD      E,H             
5572: 22         LD      (HLI),A         
5573: DC 3E C0   CALL    C,$C03E         
5576: BE         CP      (HL)            
5577: 5C         LD      E,H             
5578: A2         AND     D               
5579: 5C         LD      E,H             
557A: FE 00      CP      $00             
557C: FE 7C      CP      $7C             
557E: FE 00      CP      $00             
5580: FF         RST     0X38            
5581: 00         NOP                     
5582: A1         AND     C               
5583: 5E         LD      E,(HL)          
5584: A1         AND     C               
5585: 5E         LD      E,(HL)          
5586: BF         CP      A               
5587: 40         LD      B,B             
5588: BF         CP      A               
5589: 40         LD      B,B             
558A: BF         CP      A               
558B: 40         LD      B,B             
558C: BF         CP      A               
558D: 40         LD      B,B             
558E: FF         RST     0X38            
558F: 00         NOP                     
5590: DF         RST     0X18            
5591: 7E         LD      A,(HL)          
5592: DF         RST     0X18            
5593: 7E         LD      A,(HL)          
5594: FF         RST     0X38            
5595: 00         NOP                     
5596: 00         NOP                     
5597: 00         NOP                     
5598: 00         NOP                     
5599: 00         NOP                     
559A: 00         NOP                     
559B: 00         NOP                     
559C: 00         NOP                     
559D: 00         NOP                     
559E: 00         NOP                     
559F: 00         NOP                     
55A0: 7C         LD      A,H             
55A1: 00         NOP                     
55A2: BE         CP      (HL)            
55A3: 7C         LD      A,H             
55A4: BF         CP      A               
55A5: 7E         LD      A,(HL)          
55A6: BE         CP      (HL)            
55A7: 7F         LD      A,A             
55A8: BE         CP      (HL)            
55A9: 7F         LD      A,A             
55AA: BE         CP      (HL)            
55AB: 7F         LD      A,A             
55AC: 86         ADD     A,(HL)          
55AD: 7F         LD      A,A             
55AE: 81         ADD     A,C             
55AF: 7E         LD      A,(HL)          
55B0: FF         RST     0X38            
55B1: 01 03 00   LD      BC,$0003        
55B4: 00         NOP                     
55B5: 00         NOP                     
55B6: 00         NOP                     
55B7: 00         NOP                     
55B8: 00         NOP                     
55B9: 00         NOP                     
55BA: 00         NOP                     
55BB: 00         NOP                     
55BC: 00         NOP                     
55BD: 00         NOP                     
55BE: 00         NOP                     
55BF: 00         NOP                     
55C0: 00         NOP                     
55C1: FF         RST     0X38            
55C2: 00         NOP                     
55C3: FF         RST     0X38            
55C4: 22         LD      (HLI),A         
55C5: FF         RST     0X38            
55C6: 14         INC     D               
55C7: FF         RST     0X38            
55C8: 08 FF 14   LD      ($14FF),SP      
55CB: FF         RST     0X38            
55CC: 22         LD      (HLI),A         
55CD: FF         RST     0X38            
55CE: 00         NOP                     
55CF: FF         RST     0X38            
55D0: 00         NOP                     
55D1: FF         RST     0X38            
55D2: 00         NOP                     
55D3: FF         RST     0X38            
55D4: 22         LD      (HLI),A         
55D5: FF         RST     0X38            
55D6: 14         INC     D               
55D7: FF         RST     0X38            
55D8: 08 FF 14   LD      ($14FF),SP      
55DB: FF         RST     0X38            
55DC: 22         LD      (HLI),A         
55DD: FF         RST     0X38            
55DE: 00         NOP                     
55DF: FF         RST     0X38            
55E0: 00         NOP                     
55E1: FF         RST     0X38            
55E2: 00         NOP                     
55E3: FF         RST     0X38            
55E4: 22         LD      (HLI),A         
55E5: FF         RST     0X38            
55E6: 14         INC     D               
55E7: FF         RST     0X38            
55E8: 08 FF 14   LD      ($14FF),SP      
55EB: FF         RST     0X38            
55EC: 22         LD      (HLI),A         
55ED: FF         RST     0X38            
55EE: 00         NOP                     
55EF: FF         RST     0X38            
55F0: 00         NOP                     
55F1: FF         RST     0X38            
55F2: 00         NOP                     
55F3: FF         RST     0X38            
55F4: 22         LD      (HLI),A         
55F5: FF         RST     0X38            
55F6: 14         INC     D               
55F7: FF         RST     0X38            
55F8: 08 FF 14   LD      ($14FF),SP      
55FB: FF         RST     0X38            
55FC: 22         LD      (HLI),A         
55FD: FF         RST     0X38            
55FE: 00         NOP                     
55FF: FF         RST     0X38            
5600: C0         RET     NZ              
5601: B8         CP      B               
5602: 88         ADC     A,B             
5603: F8 98      LDHL    SP,$98          
5605: F8 98      LDHL    SP,$98          
5607: F8 98      LDHL    SP,$98          
5609: F8 98      LDHL    SP,$98          
560B: F8 F8      LDHL    SP,$F8          
560D: F8 98      LDHL    SP,$98          
560F: F8 98      LDHL    SP,$98          
5611: F8 9C      LDHL    SP,$9C          
5613: FC         ???                     
5614: 98         SBC     B               
5615: F8 98      LDHL    SP,$98          
5617: F8 98      LDHL    SP,$98          
5619: F8 98      LDHL    SP,$98          
561B: F8 B8      LDHL    SP,$B8          
561D: F8 D8      LDHL    SP,$D8          
561F: E0 FC      LDFF00  ($FC),A         
5621: 00         NOP                     
5622: E4         ???                     
5623: 18 EC      JR      $5611           
5625: 18 FC      JR      $5623           
5627: 00         NOP                     
5628: FC         ???                     
5629: 00         NOP                     
562A: E4         ???                     
562B: 18 EC      JR      $5619           
562D: 18 FC      JR      $562B           
562F: 00         NOP                     
5630: FC         ???                     
5631: 00         NOP                     
5632: E4         ???                     
5633: 18 EC      JR      $5621           
5635: 18 FC      JR      $5633           
5637: 00         NOP                     
5638: FC         ???                     
5639: 00         NOP                     
563A: E4         ???                     
563B: 18 EC      JR      $5629           
563D: 18 1C      JR      $565B           
563F: 00         NOP                     
5640: C5         PUSH    BC              
5641: 3E 8E      LD      A,$8E           
5643: 7F         LD      A,A             
5644: 1F         RRA                     
5645: FF         RST     0X38            
5646: 1F         RRA                     
5647: FF         RST     0X38            
5648: 1F         RRA                     
5649: FF         RST     0X38            
564A: 1F         RRA                     
564B: FF         RST     0X38            
564C: 3F         CCF                     
564D: FF         RST     0X38            
564E: DF         RST     0X18            
564F: FF         RST     0X38            
5650: 9F         SBC     A               
5651: 7F         LD      A,A             
5652: 9F         SBC     A               
5653: 7F         LD      A,A             
5654: 1F         RRA                     
5655: FF         RST     0X38            
5656: 1F         RRA                     
5657: FF         RST     0X38            
5658: 1F         RRA                     
5659: FF         RST     0X38            
565A: 19         ADD     HL,DE           
565B: FF         RST     0X38            
565C: 2F         CPL                     
565D: F1         POP     AF              
565E: 7F         LD      A,A             
565F: C1         POP     BC              
5660: FF         RST     0X38            
5661: 00         NOP                     
5662: E1         POP     HL              
5663: 1E EF      LD      E,$EF           
5665: 1E FF      LD      E,$FF           
5667: 00         NOP                     
5668: FF         RST     0X38            
5669: 00         NOP                     
566A: E1         POP     HL              
566B: 1E EF      LD      E,$EF           
566D: 1E FF      LD      E,$FF           
566F: 00         NOP                     
5670: FF         RST     0X38            
5671: 00         NOP                     
5672: E1         POP     HL              
5673: 1E EF      LD      E,$EF           
5675: 1E FF      LD      E,$FF           
5677: 00         NOP                     
5678: FF         RST     0X38            
5679: 00         NOP                     
567A: E1         POP     HL              
567B: 1E 6F      LD      E,$6F           
567D: 1E 3F      LD      E,$3F           
567F: 00         NOP                     
5680: F3         DI                      
5681: 0F         RRCA                    
5682: CF         RST     0X08            
5683: 3F         CCF                     
5684: 9F         SBC     A               
5685: 7F         LD      A,A             
5686: 3F         CCF                     
5687: FF         RST     0X38            
5688: 3F         CCF                     
5689: FF         RST     0X38            
568A: 3F         CCF                     
568B: FF         RST     0X38            
568C: 3F         CCF                     
568D: FF         RST     0X38            
568E: 7F         LD      A,A             
568F: FF         RST     0X38            
5690: BF         CP      A               
5691: FF         RST     0X38            
5692: BF         CP      A               
5693: 7F         LD      A,A             
5694: BF         CP      A               
5695: 7F         LD      A,A             
5696: 1F         RRA                     
5697: FF         RST     0X38            
5698: 1F         RRA                     
5699: FF         RST     0X38            
569A: 20 FF      JR      NZ,$569B        
569C: 5F         LD      E,A             
569D: E0 BF      LDFF00  ($BF),A         
569F: C0         RET     NZ              
56A0: FF         RST     0X38            
56A1: 00         NOP                     
56A2: C0         RET     NZ              
56A3: 3F         CCF                     
56A4: DF         RST     0X18            
56A5: 3F         CCF                     
56A6: FF         RST     0X38            
56A7: 00         NOP                     
56A8: FF         RST     0X38            
56A9: 00         NOP                     
56AA: C0         RET     NZ              
56AB: 3F         CCF                     
56AC: DF         RST     0X18            
56AD: 3F         CCF                     
56AE: FF         RST     0X38            
56AF: 00         NOP                     
56B0: FF         RST     0X38            
56B1: 00         NOP                     
56B2: C0         RET     NZ              
56B3: 3F         CCF                     
56B4: DF         RST     0X18            
56B5: 3F         CCF                     
56B6: FF         RST     0X38            
56B7: 00         NOP                     
56B8: FF         RST     0X38            
56B9: 00         NOP                     
56BA: C0         RET     NZ              
56BB: 3F         CCF                     
56BC: DF         RST     0X18            
56BD: 3F         CCF                     
56BE: FF         RST     0X38            
56BF: 00         NOP                     
56C0: 00         NOP                     
56C1: FF         RST     0X38            
56C2: 00         NOP                     
56C3: FF         RST     0X38            
56C4: 22         LD      (HLI),A         
56C5: FF         RST     0X38            
56C6: 14         INC     D               
56C7: FF         RST     0X38            
56C8: 08 FF 14   LD      ($14FF),SP      
56CB: FF         RST     0X38            
56CC: 22         LD      (HLI),A         
56CD: FF         RST     0X38            
56CE: 00         NOP                     
56CF: FF         RST     0X38            
56D0: 00         NOP                     
56D1: FF         RST     0X38            
56D2: 00         NOP                     
56D3: FF         RST     0X38            
56D4: 22         LD      (HLI),A         
56D5: FF         RST     0X38            
56D6: 14         INC     D               
56D7: FF         RST     0X38            
56D8: 08 FF 14   LD      ($14FF),SP      
56DB: FF         RST     0X38            
56DC: 22         LD      (HLI),A         
56DD: FF         RST     0X38            
56DE: 00         NOP                     
56DF: FF         RST     0X38            
56E0: 00         NOP                     
56E1: FF         RST     0X38            
56E2: 00         NOP                     
56E3: FF         RST     0X38            
56E4: 22         LD      (HLI),A         
56E5: FF         RST     0X38            
56E6: 14         INC     D               
56E7: FF         RST     0X38            
56E8: 08 FF 14   LD      ($14FF),SP      
56EB: FF         RST     0X38            
56EC: 22         LD      (HLI),A         
56ED: FF         RST     0X38            
56EE: 00         NOP                     
56EF: FF         RST     0X38            
56F0: 00         NOP                     
56F1: FF         RST     0X38            
56F2: 00         NOP                     
56F3: FF         RST     0X38            
56F4: 22         LD      (HLI),A         
56F5: FF         RST     0X38            
56F6: 14         INC     D               
56F7: FF         RST     0X38            
56F8: 08 FF 14   LD      ($14FF),SP      
56FB: FF         RST     0X38            
56FC: 22         LD      (HLI),A         
56FD: FF         RST     0X38            
56FE: 00         NOP                     
56FF: FF         RST     0X38            
5700: 1F         RRA                     
5701: 00         NOP                     
5702: 3F         CCF                     
5703: 16 7F      LD      D,$7F           
5705: 36 EB      LD      (HL),$EB        
5707: 76         HALT                    
5708: DB         ???                     
5709: 66         LD      H,(HL)          
570A: FB         EI                      
570B: 56         LD      D,(HL)          
570C: BB         CP      E               
570D: 46         LD      B,(HL)          
570E: 7B         LD      A,E             
570F: 06 FB      LD      B,$FB           
5711: 66         LD      H,(HL)          
5712: FB         EI                      
5713: 76         HALT                    
5714: FB         EI                      
5715: 76         HALT                    
5716: FB         EI                      
5717: 56         LD      D,(HL)          
5718: EB         ???                     
5719: 76         HALT                    
571A: FB         EI                      
571B: 66         LD      H,(HL)          
571C: DF         RST     0X18            
571D: 62         LD      H,D             
571E: 73         LD      (HL),E          
571F: 00         NOP                     
5720: 3D         DEC     A               
5721: 00         NOP                     
5722: 7F         LD      A,A             
5723: 2D         DEC     L               
5724: 7E         LD      A,(HL)          
5725: 3F         CCF                     
5726: 7B         LD      A,E             
5727: 3C         INC     A               
5728: F7         RST     0X30            
5729: 7B         LD      A,E             
572A: FF         RST     0X38            
572B: 77         LD      (HL),A          
572C: 9F         SBC     A               
572D: 71         LD      (HL),C          
572E: 6F         LD      L,A             
572F: 11 FC 63   LD      DE,$63FC        
5732: FB         EI                      
5733: 7C         LD      A,H             
5734: FB         EI                      
5735: 7C         LD      A,H             
5736: F6 59      OR      $59             
5738: FC         ???                     
5739: 73         LD      (HL),E          
573A: FF         RST     0X38            
573B: 70         LD      (HL),B          
573C: B8         CP      B               
573D: 60         LD      H,B             
573E: 70         LD      (HL),B          
573F: 00         NOP                     
5740: BC         CP      H               
5741: 00         NOP                     
5742: FE BC      CP      $BC             
5744: E7         RST     0X20            
5745: 7E         LD      A,(HL)          
5746: 93         SUB     E               
5747: 6E         LD      L,(HL)          
5748: DB         ???                     
5749: 26 7B      LD      H,$7B           
574B: 86         ADD     A,(HL)          
574C: 4B         LD      C,E             
574D: B6         OR      (HL)            
574E: 4B         LD      C,E             
574F: B6         OR      (HL)            
5750: 8B         ADC     A,E             
5751: 76         HALT                    
5752: 9B         SBC     E               
5753: 66         LD      H,(HL)          
5754: 1B         DEC     DE              
5755: E6 9B      AND     $9B             
5757: 66         LD      H,(HL)          
5758: FB         EI                      
5759: 06 9B      LD      B,$9B           
575B: 06 0F      LD      B,$0F           
575D: 00         NOP                     
575E: 06 00      LD      B,$00           
5760: 1B         DEC     DE              
5761: 00         NOP                     
5762: 3F         CCF                     
5763: 1A         LD      A,(DE)          
5764: 67         LD      H,A             
5765: 3B         DEC     SP              
5766: 6D         LD      L,L             
5767: 33         INC     SP              
5768: FF         RST     0X38            
5769: 65         LD      H,L             
576A: DF         RST     0X18            
576B: 65         LD      H,L             
576C: EE 51      XOR     $51             
576E: EF         RST     0X28            
576F: 50         LD      D,B             
5770: EB         ???                     
5771: 55         LD      D,L             
5772: E7         RST     0X20            
5773: 5B         LD      E,E             
5774: E7         RST     0X20            
5775: 5B         LD      E,E             
5776: E7         RST     0X20            
5777: 59         LD      E,C             
5778: EF         RST     0X28            
5779: 53         LD      D,E             
577A: F5         PUSH    AF              
577B: 03         INC     BC              
577C: 62         LD      H,D             
577D: 01 01 00   LD      BC,$0001        
5780: CE 00      ADC     $00             
5782: FF         RST     0X38            
5783: CC F3 FD   CALL    Z,$FDF3         
5786: EE F1      XOR     $F1             
5788: DF         RST     0X18            
5789: EC         ???                     
578A: FD         ???                     
578B: DE 7D      SBC     $7D             
578D: C6 BD      ADD     $BD             
578F: 46         LD      B,(HL)          
5790: FB         EI                      
5791: 8C         ADC     A,H             
5792: DE E1      SBC     $E1             
5794: FC         ???                     
5795: F3         DI                      
5796: F9         LD      SP,HL           
5797: 66         LD      H,(HL)          
5798: F9         LD      SP,HL           
5799: C6 BF      ADD     $BF             
579B: C0         RET     NZ              
579C: 70         LD      (HL),B          
579D: 80         ADD     A,B             
579E: E0 00      LDFF00  ($00),A         
57A0: F8 00      LDHL    SP,$00          
57A2: FC         ???                     
57A3: F8 8E      LDHL    SP,$8E          
57A5: FC         ???                     
57A6: 36 CC      LD      (HL),$CC        
57A8: 76         HALT                    
57A9: 8C         ADC     A,H             
57AA: FF         RST     0X38            
57AB: 06 1B      LD      B,$1B           
57AD: E6 0B      AND     $0B             
57AF: F6 0B      OR      $0B             
57B1: F6 2B      OR      $2B             
57B3: D6 2B      SUB     $2B             
57B5: D6 2B      SUB     $2B             
57B7: D6 EB      SUB     $EB             
57B9: 16 3B      LD      D,$3B           
57BB: 06 1F      LD      B,$1F           
57BD: 00         NOP                     
57BE: 0E 00      LD      C,$00           
57C0: 0F         RRCA                    
57C1: 00         NOP                     
57C2: 1F         RRA                     
57C3: 0F         RRCA                    
57C4: 31 1F 36   LD      SP,$361F        
57C7: 19         ADD     HL,DE           
57C8: 6F         LD      L,A             
57C9: 30 6F      JR      NC,$583A        
57CB: 30 78      JR      NC,$5845        
57CD: 27         DAA                     
57CE: D0         RET     NC              
57CF: 6F         LD      L,A             
57D0: D0         RET     NC              
57D1: 6F         LD      L,A             
57D2: D2 6D D2   JP      NC,$D26D        
57D5: 6D         LD      L,L             
57D6: D2 6D D7   JP      NC,$D76D        
57D9: 68         LD      L,B             
57DA: DC 60 78   CALL    C,$7860         
57DD: 00         NOP                     
57DE: 30 00      JR      NC,$57E0        
57E0: 39         ADD     HL,SP           
57E1: 00         NOP                     
57E2: BF         CP      A               
57E3: 19         ADD     HL,DE           
57E4: E7         RST     0X20            
57E5: 9F         SBC     A               
57E6: BB         CP      E               
57E7: C7         RST     0X00            
57E8: 57         LD      D,A             
57E9: BB         CP      E               
57EA: FF         RST     0X38            
57EB: 3B         DEC     SP              
57EC: FE 23      CP      $23             
57EE: 7D         LD      A,L             
57EF: A2         AND     D               
57F0: 7F         LD      A,A             
57F1: 99         SBC     C               
57F2: 3D         DEC     A               
57F3: C3 1F E7   JP      $E71F           
57F6: 4F         LD      C,A             
57F7: B5         OR      L               
57F8: CF         RST     0X08            
57F9: 37         SCF                     
57FA: 7D         LD      A,L             
57FB: 03         INC     BC              
57FC: 0E 01      LD      C,$01           
57FE: 07         RLCA                    
57FF: 00         NOP                     
5800: 37         SCF                     
5801: 00         NOP                     
5802: 6F         LD      L,A             
5803: 37         SCF                     
5804: 5F         LD      E,A             
5805: 2F         CPL                     
5806: 3F         CCF                     
5807: 1A         LD      A,(DE)          
5808: 3F         CCF                     
5809: 12         LD      (DE),A          
580A: 7F         LD      A,A             
580B: 17         RLA                     
580C: FF         RST     0X38            
580D: 7F         LD      A,A             
580E: BF         CP      A               
580F: 78         LD      A,B             
5810: 5F         LD      E,A             
5811: 30 3F      JR      NC,$5852        
5813: 13         INC     DE              
5814: 3F         CCF                     
5815: 1F         RRA                     
5816: 2C         INC     L               
5817: 1F         RRA                     
5818: 17         RLA                     
5819: 0F         RRCA                    
581A: 10 0F      STOP    $0F             
581C: 0C         INC     C               
581D: 03         INC     BC              
581E: 03         INC     BC              
581F: 00         NOP                     
5820: D8         RET     C               
5821: 00         NOP                     
5822: EC         ???                     
5823: D8         RET     C               
5824: E4         ???                     
5825: D8         RET     C               
5826: F8 60      LDHL    SP,$60          
5828: FC         ???                     
5829: 38 FE      JR      C,$5829         
582B: 30 FF      JR      NC,$582C        
582D: FE FD      CP      $FD             
582F: 7E         LD      A,(HL)          
5830: E2         LDFF00  (C),A           
5831: 3C         INC     A               
5832: EC         ???                     
5833: 30 E6      JR      NC,$581B        
5835: F8 C5      LDHL    SP,$C5          
5837: FA 89 F6   LD      A,($F689)       
583A: 02         LD      (BC),A          
583B: FC         ???                     
583C: 0C         INC     C               
583D: F0 F0      LD      A,($F0)         
583F: 00         NOP                     
5840: 37         SCF                     
5841: 00         NOP                     
5842: 6F         LD      L,A             
5843: 37         SCF                     
5844: 5F         LD      E,A             
5845: 2F         CPL                     
5846: 3F         CCF                     
5847: 1A         LD      A,(DE)          
5848: 3F         CCF                     
5849: 12         LD      (DE),A          
584A: 3F         CCF                     
584B: 17         RLA                     
584C: 3F         CCF                     
584D: 1F         RRA                     
584E: 3F         CCF                     
584F: 18 7F      JR      $58D0           
5851: 30 FF      JR      NC,$5852        
5853: 73         LD      (HL),E          
5854: 9F         SBC     A               
5855: 7F         LD      A,A             
5856: 6C         LD      L,H             
5857: 1F         RRA                     
5858: 17         RLA                     
5859: 0F         RRCA                    
585A: 10 0F      STOP    $0F             
585C: 0C         INC     C               
585D: 03         INC     BC              
585E: 03         INC     BC              
585F: 00         NOP                     
5860: D8         RET     C               
5861: 00         NOP                     
5862: EC         ???                     
5863: D8         RET     C               
5864: E4         ???                     
5865: D8         RET     C               
5866: F8 60      LDHL    SP,$60          
5868: FC         ???                     
5869: 38 FC      JR      C,$5867         
586B: 38 FC      JR      C,$5869         
586D: F8 FE      LDHL    SP,$FE          
586F: 7C         LD      A,H             
5870: FF         RST     0X38            
5871: 3E F7      LD      A,$F7           
5873: 3E E9      LD      A,$E9           
5875: F6 CE      OR      $CE             
5877: F0 98      LD      A,($98)         
5879: E0 04      LDFF00  ($04),A         
587B: F8 02      LDHL    SP,$02          
587D: FC         ???                     
587E: FC         ???                     
587F: 00         NOP                     
5880: 1B         DEC     DE              
5881: 00         NOP                     
5882: 37         SCF                     
5883: 1B         DEC     DE              
5884: 27         DAA                     
5885: 1B         DEC     DE              
5886: 1F         RRA                     
5887: 07         RLCA                    
5888: 1F         RRA                     
5889: 0F         RRCA                    
588A: 7F         LD      A,A             
588B: 0F         RRCA                    
588C: FF         RST     0X38            
588D: 7F         LD      A,A             
588E: BF         CP      A               
588F: 7F         LD      A,A             
5890: 5F         LD      E,A             
5891: 3F         CCF                     
5892: 3D         DEC     A               
5893: 1E 2F      LD      E,$2F           
5895: 1F         RRA                     
5896: 27         DAA                     
5897: 1F         RRA                     
5898: 10 0F      STOP    $0F             
589A: 10 0F      STOP    $0F             
589C: 0C         INC     C               
589D: 03         INC     BC              
589E: 03         INC     BC              
589F: 00         NOP                     
58A0: D8         RET     C               
58A1: 00         NOP                     
58A2: EC         ???                     
58A3: D8         RET     C               
58A4: F4         ???                     
58A5: E8 F8      ADD     SP,$F8          
58A7: F0 F8      LD      A,($F8)         
58A9: F0 FE      LD      A,($FE)         
58AB: F0 FF      LD      A,($FF)         
58AD: FE FD      CP      $FD             
58AF: 9E         SBC     (HL)            
58B0: FA 6C FC   LD      A,($FC6C)       
58B3: F0 9C      LD      A,($9C)         
58B5: F8 04      LDHL    SP,$04          
58B7: F8 04      LDHL    SP,$04          
58B9: F8 08      LDHL    SP,$08          
58BB: F0 10      LD      A,($10)         
58BD: E0 E0      LDFF00  ($E0),A         
58BF: 00         NOP                     
58C0: 1B         DEC     DE              
58C1: 00         NOP                     
58C2: 37         SCF                     
58C3: 1B         DEC     DE              
58C4: 27         DAA                     
58C5: 1B         DEC     DE              
58C6: 1F         RRA                     
58C7: 07         RLCA                    
58C8: 1F         RRA                     
58C9: 0F         RRCA                    
58CA: 2F         CPL                     
58CB: 1F         RRA                     
58CC: 2F         CPL                     
58CD: 1F         RRA                     
58CE: 7F         LD      A,A             
58CF: 3F         CCF                     
58D0: FF         RST     0X38            
58D1: 7F         LD      A,A             
58D2: 8F         ADC     A,A             
58D3: 7F         LD      A,A             
58D4: 7F         LD      A,A             
58D5: 0F         RRCA                    
58D6: 27         DAA                     
58D7: 1F         RRA                     
58D8: 13         INC     DE              
58D9: 0F         RRCA                    
58DA: 10 0F      STOP    $0F             
58DC: 0C         INC     C               
58DD: 03         INC     BC              
58DE: 03         INC     BC              
58DF: 00         NOP                     
58E0: D8         RET     C               
58E1: 00         NOP                     
58E2: EC         ???                     
58E3: D8         RET     C               
58E4: F4         ???                     
58E5: E8 F8      ADD     SP,$F8          
58E7: F0 F8      LD      A,($F8)         
58E9: F0 F8      LD      A,($F8)         
58EB: F0 FC      LD      A,($FC)         
58ED: F8 FE      LDHL    SP,$FE          
58EF: FC         ???                     
58F0: FF         RST     0X38            
58F1: FE F9      CP      $F9             
58F3: FE FE      CP      $FE             
58F5: 88         ADC     A,B             
58F6: FC         ???                     
58F7: 70         LD      (HL),B          
58F8: CC F8 04   CALL    Z,$04F8         
58FB: F8 08      LDHL    SP,$08          
58FD: F0 F0      LD      A,($F0)         
58FF: 00         NOP                     
5900: 07         RLCA                    
5901: 00         NOP                     
5902: 3C         INC     A               
5903: 03         INC     BC              
5904: 48         LD      C,B             
5905: 37         SCF                     
5906: 59         LD      E,C             
5907: 27         DAA                     
5908: 77         LD      (HL),A          
5909: 0F         RRCA                    
590A: CC 3F 99   CALL    Z,$993F         
590D: 7E         LD      A,(HL)          
590E: 92         SUB     D               
590F: 7D         LD      A,L             
5910: 95         SUB     L               
5911: 7B         LD      A,E             
5912: CA 37 B5   JP      Z,$B537         
5915: 4E         LD      C,(HL)          
5916: F5         PUSH    AF              
5917: 4E         LD      C,(HL)          
5918: B0         OR      B               
5919: 4F         LD      C,A             
591A: C8         RET     Z               
591B: 37         SCF                     
591C: 94         SUB     H               
591D: 7B         LD      A,E             
591E: 88         ADC     A,B             
591F: 7F         LD      A,A             
5920: FF         RST     0X38            
5921: 00         NOP                     
5922: 7C         LD      A,H             
5923: BB         CP      E               
5924: BB         CP      E               
5925: C7         RST     0X00            
5926: C6 FF      ADD     $FF             
5928: 3C         INC     A               
5929: FF         RST     0X38            
592A: 00         NOP                     
592B: FF         RST     0X38            
592C: F0 0F      LD      A,($0F)         
592E: E8 F7      ADD     SP,$F7          
5930: F4         ???                     
5931: FB         EI                      
5932: 0A         LD      A,(BC)          
5933: FD         ???                     
5934: E5         PUSH    HL              
5935: 1E F3      LD      E,$F3           
5937: 2F         CPL                     
5938: FE 31      CP      $31             
593A: 7C         LD      A,H             
593B: 83         ADD     A,E             
593C: 00         NOP                     
593D: FF         RST     0X38            
593E: 00         NOP                     
593F: FF         RST     0X38            
5940: 88         ADC     A,B             
5941: 7F         LD      A,A             
5942: 88         ADC     A,B             
5943: 7F         LD      A,A             
5944: C8         RET     Z               
5945: 3F         CCF                     
5946: A8         XOR     B               
5947: 5F         LD      E,A             
5948: E8 5F      ADD     SP,$5F          
594A: AA         XOR     D               
594B: 5D         LD      E,L             
594C: CB 3D      SET     1,E             
594E: 92         SUB     D               
594F: 7D         LD      A,L             
5950: 93         SUB     E               
5951: 7C         LD      A,H             
5952: C9         RET                     
5953: 3E 64      LD      A,$64           
5955: 1F         RRA                     
5956: 52         LD      D,D             
5957: 2F         CPL                     
5958: 48         LD      C,B             
5959: 37         SCF                     
595A: 24         INC     H               
595B: 1B         DEC     DE              
595C: 1F         RRA                     
595D: 00         NOP                     
595E: 00         NOP                     
595F: 00         NOP                     
5960: 00         NOP                     
5961: FF         RST     0X38            
5962: 7C         LD      A,H             
5963: 83         ADD     A,E             
5964: BB         CP      E               
5965: 7C         LD      A,H             
5966: FF         RST     0X38            
5967: 3F         CCF                     
5968: BF         CP      A               
5969: 47         LD      B,A             
596A: BF         CP      A               
596B: 78         LD      A,B             
596C: 78         LD      A,B             
596D: 87         ADD     A,A             
596E: C3 FF 00   JP      $00FF           
5971: FF         RST     0X38            
5972: 8C         ADC     A,H             
5973: 73         LD      (HL),E          
5974: F0 0F      LD      A,($0F)         
5976: 00         NOP                     
5977: FF         RST     0X38            
5978: 70         LD      (HL),B          
5979: 8F         ADC     A,A             
597A: A8         XOR     B               
597B: 77         LD      (HL),A          
597C: FF         RST     0X38            
597D: 00         NOP                     
597E: 00         NOP                     
597F: 00         NOP                     
5980: 07         RLCA                    
5981: 00         NOP                     
5982: 3C         INC     A               
5983: 03         INC     BC              
5984: 48         LD      C,B             
5985: 37         SCF                     
5986: 58         LD      E,B             
5987: 27         DAA                     
5988: 7D         LD      A,L             
5989: 03         INC     BC              
598A: CF         RST     0X08            
598B: 39         ADD     HL,SP           
598C: 8F         ADC     A,A             
598D: 7C         LD      A,H             
598E: 93         SUB     E               
598F: 7C         LD      A,H             
5990: 97         SUB     A               
5991: 7B         LD      A,E             
5992: CC 37 BD   CALL    Z,$BD37         
5995: 46         LD      B,(HL)          
5996: FD         ???                     
5997: 46         LD      B,(HL)          
5998: B9         CP      C               
5999: 46         LD      B,(HL)          
599A: C9         RET                     
599B: 36 99      LD      (HL),$99        
599D: 66         LD      H,(HL)          
599E: F8 07      LDHL    SP,$07          
59A0: FF         RST     0X38            
59A1: 00         NOP                     
59A2: 7C         LD      A,H             
59A3: BB         CP      E               
59A4: BB         CP      E               
59A5: C7         RST     0X00            
59A6: 76         HALT                    
59A7: CF         RST     0X08            
59A8: FC         ???                     
59A9: CF         RST     0X08            
59AA: 30 CF      JR      NC,$597B        
59AC: FC         ???                     
59AD: 03         INC     BC              
59AE: FB         EI                      
59AF: FC         ???                     
59B0: 80         ADD     A,B             
59B1: 7F         LD      A,A             
59B2: F8 07      LDHL    SP,$07          
59B4: FC         ???                     
59B5: 03         INC     BC              
59B6: FF         RST     0X38            
59B7: 30 FF      JR      NC,$59B8        
59B9: 48         LD      C,B             
59BA: FF         RST     0X38            
59BB: 49         LD      C,C             
59BC: FE 33      CP      $33             
59BE: FE 03      CP      $03             
59C0: DC 3B E7   CALL    C,$E73B         
59C3: 7C         LD      A,H             
59C4: C3 3E A1   JP      $A13E           
59C7: 5E         LD      E,(HL)          
59C8: EB         ???                     
59C9: 5D         LD      E,L             
59CA: AF         XOR     A               
59CB: 59         LD      E,C             
59CC: FE 03      CP      $03             
59CE: 9C         SBC     H               
59CF: 73         LD      (HL),E          
59D0: 8E         ADC     A,(HL)          
59D1: 79         LD      A,C             
59D2: C7         RST     0X00            
59D3: 3C         INC     A               
59D4: 67         LD      H,A             
59D5: 1C         INC     E               
59D6: 57         LD      D,A             
59D7: 29         ADD     HL,HL           
59D8: 4C         LD      C,H             
59D9: 33         INC     SP              
59DA: 24         INC     H               
59DB: 1B         DEC     DE              
59DC: 1F         RRA                     
59DD: 00         NOP                     
59DE: 00         NOP                     
59DF: 00         NOP                     
59E0: 7C         LD      A,H             
59E1: 8F         ADC     A,A             
59E2: F1         POP     AF              
59E3: 0E FB      LD      C,$FB           
59E5: 65         LD      H,L             
59E6: 9B         SBC     E               
59E7: F5         PUSH    AF              
59E8: 0B         DEC     BC              
59E9: FC         ???                     
59EA: 03         INC     BC              
59EB: FC         ???                     
59EC: 03         INC     BC              
59ED: FC         ???                     
59EE: 13         INC     DE              
59EF: EC         ???                     
59F0: 10 EF      STOP    $EF             
59F2: FB         EI                      
59F3: 07         RLCA                    
59F4: FC         ???                     
59F5: F3         DI                      
59F6: 07         RLCA                    
59F7: F8 71      LDHL    SP,$71          
59F9: 8E         ADC     A,(HL)          
59FA: A9         XOR     C               
59FB: 76         HALT                    
59FC: FF         RST     0X38            
59FD: 00         NOP                     
59FE: 00         NOP                     
59FF: 00         NOP                     
5A00: 00         NOP                     
5A01: 00         NOP                     
5A02: 00         NOP                     
5A03: 00         NOP                     
5A04: 00         NOP                     
5A05: 00         NOP                     
5A06: 00         NOP                     
5A07: 01 00 03   LD      BC,$0300        
5A0A: 00         NOP                     
5A0B: 07         RLCA                    
5A0C: 01 0F 03   LD      BC,$030F        
5A0F: 1F         RRA                     
5A10: 07         RLCA                    
5A11: 1F         RRA                     
5A12: 07         RLCA                    
5A13: 3F         CCF                     
5A14: 0F         RRCA                    
5A15: 3F         CCF                     
5A16: 0F         RRCA                    
5A17: 3F         CCF                     
5A18: 1F         RRA                     
5A19: 7F         LD      A,A             
5A1A: 1F         RRA                     
5A1B: 7F         LD      A,A             
5A1C: 1F         RRA                     
5A1D: 7F         LD      A,A             
5A1E: 1F         RRA                     
5A1F: 7F         LD      A,A             
5A20: 00         NOP                     
5A21: 00         NOP                     
5A22: 00         NOP                     
5A23: 0F         RRCA                    
5A24: 00         NOP                     
5A25: 7F         LD      A,A             
5A26: 0F         RRCA                    
5A27: FF         RST     0X38            
5A28: 3F         CCF                     
5A29: FF         RST     0X38            
5A2A: FF         RST     0X38            
5A2B: FF         RST     0X38            
5A2C: FF         RST     0X38            
5A2D: FF         RST     0X38            
5A2E: FF         RST     0X38            
5A2F: FF         RST     0X38            
5A30: FF         RST     0X38            
5A31: FF         RST     0X38            
5A32: FF         RST     0X38            
5A33: FF         RST     0X38            
5A34: FF         RST     0X38            
5A35: FF         RST     0X38            
5A36: FF         RST     0X38            
5A37: FF         RST     0X38            
5A38: FF         RST     0X38            
5A39: C7         RST     0X00            
5A3A: FF         RST     0X38            
5A3B: 83         ADD     A,E             
5A3C: FF         RST     0X38            
5A3D: 83         ADD     A,E             
5A3E: FF         RST     0X38            
5A3F: 83         ADD     A,E             
5A40: 00         NOP                     
5A41: 00         NOP                     
5A42: 00         NOP                     
5A43: 00         NOP                     
5A44: 00         NOP                     
5A45: 00         NOP                     
5A46: 00         NOP                     
5A47: 00         NOP                     
5A48: 00         NOP                     
5A49: 00         NOP                     
5A4A: 00         NOP                     
5A4B: 03         INC     BC              
5A4C: 00         NOP                     
5A4D: 07         RLCA                    
5A4E: 01 0F 03   LD      BC,$030F        
5A51: 1F         RRA                     
5A52: 07         RLCA                    
5A53: 3F         CCF                     
5A54: 0F         RRCA                    
5A55: 3F         CCF                     
5A56: 0F         RRCA                    
5A57: 7F         LD      A,A             
5A58: 1F         RRA                     
5A59: 7F         LD      A,A             
5A5A: 1F         RRA                     
5A5B: 7F         LD      A,A             
5A5C: 3F         CCF                     
5A5D: FF         RST     0X38            
5A5E: 3F         CCF                     
5A5F: FF         RST     0X38            
5A60: 00         NOP                     
5A61: 00         NOP                     
5A62: 00         NOP                     
5A63: 00         NOP                     
5A64: 00         NOP                     
5A65: 00         NOP                     
5A66: 00         NOP                     
5A67: 1F         RRA                     
5A68: 00         NOP                     
5A69: FF         RST     0X38            
5A6A: 1F         RRA                     
5A6B: FF         RST     0X38            
5A6C: 7F         LD      A,A             
5A6D: FF         RST     0X38            
5A6E: FF         RST     0X38            
5A6F: FF         RST     0X38            
5A70: FF         RST     0X38            
5A71: FF         RST     0X38            
5A72: FF         RST     0X38            
5A73: FF         RST     0X38            
5A74: FF         RST     0X38            
5A75: FF         RST     0X38            
5A76: FF         RST     0X38            
5A77: FF         RST     0X38            
5A78: FF         RST     0X38            
5A79: FF         RST     0X38            
5A7A: FF         RST     0X38            
5A7B: 87         ADD     A,A             
5A7C: FF         RST     0X38            
5A7D: 03         INC     BC              
5A7E: FF         RST     0X38            
5A7F: 03         INC     BC              
5A80: 00         NOP                     
5A81: 00         NOP                     
5A82: 00         NOP                     
5A83: 00         NOP                     
5A84: 00         NOP                     
5A85: 00         NOP                     
5A86: 00         NOP                     
5A87: 00         NOP                     
5A88: 00         NOP                     
5A89: 01 00 03   LD      BC,$0300        
5A8C: 00         NOP                     
5A8D: 07         RLCA                    
5A8E: 01 07 01   LD      BC,$0107        
5A91: 0F         RRCA                    
5A92: 03         INC     BC              
5A93: 0F         RRCA                    
5A94: 03         INC     BC              
5A95: 0F         RRCA                    
5A96: 07         RLCA                    
5A97: 1F         RRA                     
5A98: 07         RLCA                    
5A99: 1F         RRA                     
5A9A: 07         RLCA                    
5A9B: 1F         RRA                     
5A9C: 07         RLCA                    
5A9D: 1F         RRA                     
5A9E: 07         RLCA                    
5A9F: 1F         RRA                     
5AA0: 00         NOP                     
5AA1: 03         INC     BC              
5AA2: 00         NOP                     
5AA3: 1F         RRA                     
5AA4: 03         INC     BC              
5AA5: 7F         LD      A,A             
5AA6: 0F         RRCA                    
5AA7: FF         RST     0X38            
5AA8: 3F         CCF                     
5AA9: FF         RST     0X38            
5AAA: 7F         LD      A,A             
5AAB: FF         RST     0X38            
5AAC: FF         RST     0X38            
5AAD: FF         RST     0X38            
5AAE: FF         RST     0X38            
5AAF: FF         RST     0X38            
5AB0: FF         RST     0X38            
5AB1: FF         RST     0X38            
5AB2: FF         RST     0X38            
5AB3: FF         RST     0X38            
5AB4: FF         RST     0X38            
5AB5: FF         RST     0X38            
5AB6: FF         RST     0X38            
5AB7: F3         DI                      
5AB8: FF         RST     0X38            
5AB9: E1         POP     HL              
5ABA: FF         RST     0X38            
5ABB: E1         POP     HL              
5ABC: FF         RST     0X38            
5ABD: E1         POP     HL              
5ABE: FF         RST     0X38            
5ABF: E1         POP     HL              
5AC0: CF         RST     0X08            
5AC1: F0 B7      LD      A,($B7)         
5AC3: CF         RST     0X08            
5AC4: 5F         LD      E,A             
5AC5: BF         CP      A               
5AC6: 7F         LD      A,A             
5AC7: BF         CP      A               
5AC8: FF         RST     0X38            
5AC9: 7F         LD      A,A             
5ACA: FF         RST     0X38            
5ACB: 7F         LD      A,A             
5ACC: FF         RST     0X38            
5ACD: 43         LD      B,E             
5ACE: E7         RST     0X20            
5ACF: 19         ADD     HL,DE           
5AD0: 7F         LD      A,A             
5AD1: 81         ADD     A,C             
5AD2: 7F         LD      A,A             
5AD3: 81         ADD     A,C             
5AD4: 3F         CCF                     
5AD5: C3 0F F0   JP      $F00F           
5AD8: 00         NOP                     
5AD9: FF         RST     0X38            
5ADA: 07         RLCA                    
5ADB: F8 0F      LDHL    SP,$0F          
5ADD: F0 4E      LD      A,($4E)         
5ADF: B1         OR      C               
5AE0: CF         RST     0X08            
5AE1: F0 BF      LD      A,($BF)         
5AE3: C3 67 99   JP      $9967           
5AE6: 7F         LD      A,A             
5AE7: 81         ADD     A,C             
5AE8: FF         RST     0X38            
5AE9: 01 FF 43   LD      BC,$43FF        
5AEC: FF         RST     0X38            
5AED: 7F         LD      A,A             
5AEE: FF         RST     0X38            
5AEF: 7F         LD      A,A             
5AF0: 7F         LD      A,A             
5AF1: BF         CP      A               
5AF2: 5F         LD      E,A             
5AF3: BF         CP      A               
5AF4: 37         SCF                     
5AF5: CF         RST     0X08            
5AF6: 0F         RRCA                    
5AF7: F0 00      LD      A,($00)         
5AF9: FF         RST     0X38            
5AFA: 07         RLCA                    
5AFB: F8 0F      LDHL    SP,$0F          
5AFD: F0 4E      LD      A,($4E)         
5AFF: B1         OR      C               
5B00: FF         RST     0X38            
5B01: 00         NOP                     
5B02: 87         ADD     A,A             
5B03: 7F         LD      A,A             
5B04: 80         ADD     A,B             
5B05: 7F         LD      A,A             
5B06: 80         ADD     A,B             
5B07: 7F         LD      A,A             
5B08: FF         RST     0X38            
5B09: 00         NOP                     
5B0A: 7F         LD      A,A             
5B0B: 00         NOP                     
5B0C: 40         LD      B,B             
5B0D: 3F         CCF                     
5B0E: 41         LD      B,C             
5B0F: 3E 62      LD      A,$62           
5B11: 1D         DEC     E               
5B12: F3         DI                      
5B13: 6D         LD      L,L             
5B14: F5         PUSH    AF              
5B15: 6B         LD      L,E             
5B16: 96         SUB     (HL)            
5B17: 6B         LD      L,E             
5B18: 96         SUB     (HL)            
5B19: 6B         LD      L,E             
5B1A: 66         LD      H,(HL)          
5B1B: 1B         DEC     DE              
5B1C: 46         LD      B,(HL)          
5B1D: 3B         DEC     SP              
5B1E: 44         LD      B,H             
5B1F: 3B         DEC     SP              
5B20: FF         RST     0X38            
5B21: 00         NOP                     
5B22: FF         RST     0X38            
5B23: FF         RST     0X38            
5B24: FF         RST     0X38            
5B25: FF         RST     0X38            
5B26: FF         RST     0X38            
5B27: FF         RST     0X38            
5B28: FF         RST     0X38            
5B29: 00         NOP                     
5B2A: FF         RST     0X38            
5B2B: 00         NOP                     
5B2C: DF         RST     0X18            
5B2D: 3F         CCF                     
5B2E: 70         LD      (HL),B          
5B2F: FF         RST     0X38            
5B30: C0         RET     NZ              
5B31: FF         RST     0X38            
5B32: 80         ADD     A,B             
5B33: FF         RST     0X38            
5B34: 00         NOP                     
5B35: FF         RST     0X38            
5B36: 70         LD      (HL),B          
5B37: 8F         ADC     A,A             
5B38: BF         CP      A               
5B39: 70         LD      (HL),B          
5B3A: FF         RST     0X38            
5B3B: 7F         LD      A,A             
5B3C: FF         RST     0X38            
5B3D: 7F         LD      A,A             
5B3E: BF         CP      A               
5B3F: 7F         LD      A,A             
5B40: 64         LD      H,H             
5B41: 1B         DEC     DE              
5B42: F2         ???                     
5B43: 6D         LD      L,L             
5B44: F2         ???                     
5B45: 6D         LD      L,L             
5B46: 91         SUB     C               
5B47: 6E         LD      L,(HL)          
5B48: 90         SUB     B               
5B49: 6F         LD      L,A             
5B4A: 60         LD      H,B             
5B4B: 1F         RRA                     
5B4C: 40         LD      B,B             
5B4D: 3F         CCF                     
5B4E: 40         LD      B,B             
5B4F: 3F         CCF                     
5B50: 40         LD      B,B             
5B51: 3F         CCF                     
5B52: 60         LD      H,B             
5B53: 1F         RRA                     
5B54: 70         LD      (HL),B          
5B55: 0F         RRCA                    
5B56: 58         LD      E,B             
5B57: 27         DAA                     
5B58: 4F         LD      C,A             
5B59: 30 5A      JR      NC,$5BB5        
5B5B: 3C         INC     A               
5B5C: 24         INC     H               
5B5D: 18 18      JR      $5B77           
5B5F: 00         NOP                     
5B60: 7F         LD      A,A             
5B61: BC         CP      H               
5B62: 5E         LD      E,(HL)          
5B63: B9         CP      C               
5B64: 37         SCF                     
5B65: C8         RET     Z               
5B66: 0F         RRCA                    
5B67: F0 00      LD      A,($00)         
5B69: FF         RST     0X38            
5B6A: 98         SBC     B               
5B6B: 67         LD      H,A             
5B6C: 9F         SBC     A               
5B6D: 60         LD      H,B             
5B6E: 8F         ADC     A,A             
5B6F: 70         LD      (HL),B          
5B70: 40         LD      B,B             
5B71: BF         CP      A               
5B72: 20 DF      JR      NZ,$5B53        
5B74: 00         NOP                     
5B75: FF         RST     0X38            
5B76: 00         NOP                     
5B77: FF         RST     0X38            
5B78: FF         RST     0X38            
5B79: 00         NOP                     
5B7A: 5A         LD      E,D             
5B7B: 3C         INC     A               
5B7C: 24         INC     H               
5B7D: 18 18      JR      $5B97           
5B7F: 00         NOP                     
5B80: CF         RST     0X08            
5B81: F0 B7      LD      A,($B7)         
5B83: CF         RST     0X08            
5B84: 5F         LD      E,A             
5B85: BF         CP      A               
5B86: 7F         LD      A,A             
5B87: BF         CP      A               
5B88: BF         CP      A               
5B89: 7F         LD      A,A             
5B8A: FF         RST     0X38            
5B8B: 7F         LD      A,A             
5B8C: FF         RST     0X38            
5B8D: 7C         LD      A,H             
5B8E: BF         CP      A               
5B8F: 78         LD      A,B             
5B90: 7E         LD      A,(HL)          
5B91: B9         CP      C               
5B92: 5F         LD      E,A             
5B93: B8         CP      B               
5B94: 37         SCF                     
5B95: CC 0F F0   CALL    Z,$F00F         
5B98: 00         NOP                     
5B99: FF         RST     0X38            
5B9A: 07         RLCA                    
5B9B: F8 0F      LDHL    SP,$0F          
5B9D: F0 4E      LD      A,($4E)         
5B9F: B1         OR      C               
5BA0: CF         RST     0X08            
5BA1: F0 B7      LD      A,($B7)         
5BA3: CC 5E B9   CALL    Z,$B95E         
5BA6: 7F         LD      A,A             
5BA7: B8         CP      B               
5BA8: BF         CP      A               
5BA9: 78         LD      A,B             
5BAA: FF         RST     0X38            
5BAB: 7C         LD      A,H             
5BAC: FF         RST     0X38            
5BAD: 7F         LD      A,A             
5BAE: BF         CP      A               
5BAF: 7F         LD      A,A             
5BB0: 7F         LD      A,A             
5BB1: BF         CP      A               
5BB2: 5F         LD      E,A             
5BB3: BF         CP      A               
5BB4: 37         SCF                     
5BB5: CF         RST     0X08            
5BB6: 0F         RRCA                    
5BB7: F0 00      LD      A,($00)         
5BB9: FF         RST     0X38            
5BBA: 07         RLCA                    
5BBB: F8 0F      LDHL    SP,$0F          
5BBD: F0 4E      LD      A,($4E)         
5BBF: B1         OR      C               
5BC0: CF         RST     0X08            
5BC1: F0 B7      LD      A,($B7)         
5BC3: CF         RST     0X08            
5BC4: 5F         LD      E,A             
5BC5: BF         CP      A               
5BC6: 7F         LD      A,A             
5BC7: 87         ADD     A,A             
5BC8: CF         RST     0X08            
5BC9: 33         INC     SP              
5BCA: FF         RST     0X38            
5BCB: 03         INC     BC              
5BCC: FF         RST     0X38            
5BCD: 03         INC     BC              
5BCE: FF         RST     0X38            
5BCF: 07         RLCA                    
5BD0: 7F         LD      A,A             
5BD1: BF         CP      A               
5BD2: 5F         LD      E,A             
5BD3: BF         CP      A               
5BD4: 37         SCF                     
5BD5: CF         RST     0X08            
5BD6: 0F         RRCA                    
5BD7: F0 00      LD      A,($00)         
5BD9: FF         RST     0X38            
5BDA: 07         RLCA                    
5BDB: F8 0F      LDHL    SP,$0F          
5BDD: F0 4E      LD      A,($4E)         
5BDF: B1         OR      C               
5BE0: F3         DI                      
5BE1: 0F         RRCA                    
5BE2: ED         ???                     
5BE3: F3         DI                      
5BE4: FA FD FE   LD      A,($FEFD)       
5BE7: FD         ???                     
5BE8: FD         ???                     
5BE9: FE FF      CP      $FF             
5BEB: FE FF      CP      $FF             
5BED: FE FD      CP      $FD             
5BEF: FE FE      CP      $FE             
5BF1: FD         ???                     
5BF2: FA FD EC   LD      A,($ECFD)       
5BF5: F3         DI                      
5BF6: F0 0F      LD      A,($0F)         
5BF8: 00         NOP                     
5BF9: FF         RST     0X38            
5BFA: E0 1F      LDFF00  ($1F),A         
5BFC: F0 0F      LD      A,($0F)         
5BFE: 72         LD      (HL),D          
5BFF: 8D         ADC     A,L             
5C00: 00         NOP                     
5C01: 00         NOP                     
5C02: 00         NOP                     
5C03: 00         NOP                     
5C04: 07         RLCA                    
5C05: 00         NOP                     
5C06: 0F         RRCA                    
5C07: 00         NOP                     
5C08: 3F         CCF                     
5C09: 00         NOP                     
5C0A: 7F         LD      A,A             
5C0B: 30 7F      JR      NC,$5C8C        
5C0D: 37         SCF                     
5C0E: 7F         LD      A,A             
5C0F: 3E 3F      LD      A,$3F           
5C11: 0E 0B      LD      C,$0B           
5C13: 07         RLCA                    
5C14: 1F         RRA                     
5C15: 00         NOP                     
5C16: 3F         CCF                     
5C17: 18 3C      JR      $5C55           
5C19: 1B         DEC     DE              
5C1A: 1F         RRA                     
5C1B: 00         NOP                     
5C1C: 0F         RRCA                    
5C1D: 07         RLCA                    
5C1E: 0F         RRCA                    
5C1F: 00         NOP                     
5C20: 00         NOP                     
5C21: 00         NOP                     
5C22: 00         NOP                     
5C23: 00         NOP                     
5C24: E0 00      LDFF00  ($00),A         
5C26: F0 00      LD      A,($00)         
5C28: F8 C0      LDHL    SP,$C0          
5C2A: FC         ???                     
5C2B: C8         RET     Z               
5C2C: FC         ???                     
5C2D: E8 FC      ADD     SP,$FC          
5C2F: D8         RET     C               
5C30: F8 D0      LDHL    SP,$D0          
5C32: F8 E0      LDHL    SP,$E0          
5C34: FC         ???                     
5C35: 18 FC      JR      $5C33           
5C37: 18 38      JR      $5C71           
5C39: C0         RET     NZ              
5C3A: 10 E0      STOP    $E0             
5C3C: F8 00      LDHL    SP,$00          
5C3E: F0 00      LD      A,($00)         
5C40: 00         NOP                     
5C41: 00         NOP                     
5C42: 00         NOP                     
5C43: 00         NOP                     
5C44: 07         RLCA                    
5C45: 00         NOP                     
5C46: 0F         RRCA                    
5C47: 00         NOP                     
5C48: 3F         CCF                     
5C49: 00         NOP                     
5C4A: 7F         LD      A,A             
5C4B: 30 7F      JR      NC,$5CCC        
5C4D: 30 7F      JR      NC,$5CCE        
5C4F: 30 3F      JR      NC,$5C90        
5C51: 0C         INC     C               
5C52: 1F         RRA                     
5C53: 07         RLCA                    
5C54: 37         SCF                     
5C55: 18 3F      JR      $5C96           
5C57: 10 18      STOP    $18             
5C59: 07         RLCA                    
5C5A: 08 07 1F   LD      ($1F07),SP      
5C5D: 00         NOP                     
5C5E: 0F         RRCA                    
5C5F: 00         NOP                     
5C60: 00         NOP                     
5C61: 00         NOP                     
5C62: 00         NOP                     
5C63: 00         NOP                     
5C64: E0 00      LDFF00  ($00),A         
5C66: F0 00      LD      A,($00)         
5C68: FC         ???                     
5C69: 00         NOP                     
5C6A: FE 0C      CP      $0C             
5C6C: FE 0C      CP      $0C             
5C6E: FE 0C      CP      $0C             
5C70: FC         ???                     
5C71: 30 F0      JR      NC,$5C63        
5C73: E0 F8      LDFF00  ($F8),A         
5C75: 00         NOP                     
5C76: FC         ???                     
5C77: 08 3C C8   LD      ($C83C),SP      
5C7A: F8 00      LDHL    SP,$00          
5C7C: F8 E0      LDHL    SP,$E0          
5C7E: F0 00      LD      A,($00)         
5C80: 18 00      JR      $5C82           
5C82: 38 10      JR      C,$5C94         
5C84: 3E 10      LD      A,$10           
5C86: 69         LD      L,C             
5C87: 36 DF      LD      (HL),$DF        
5C89: 60         LD      H,B             
5C8A: FF         RST     0X38            
5C8B: 4E         LD      C,(HL)          
5C8C: FF         RST     0X38            
5C8D: 0A         LD      A,(BC)          
5C8E: FF         RST     0X38            
5C8F: 4E         LD      C,(HL)          
5C90: FF         RST     0X38            
5C91: 60         LD      H,B             
5C92: FE 61      CP      $61             
5C94: DF         RST     0X18            
5C95: 60         LD      H,B             
5C96: FF         RST     0X38            
5C97: 4C         LD      C,H             
5C98: AF         XOR     A               
5C99: 46         LD      B,(HL)          
5C9A: C7         RST     0X00            
5C9B: 03         INC     BC              
5C9C: 07         RLCA                    
5C9D: 01 07 02   LD      BC,$0207        
5CA0: 00         NOP                     
5CA1: 00         NOP                     
5CA2: 03         INC     BC              
5CA3: 00         NOP                     
5CA4: 07         RLCA                    
5CA5: 02         LD      (BC),A          
5CA6: 77         LD      (HL),A          
5CA7: 02         LD      (BC),A          
5CA8: 95         SUB     L               
5CA9: 62         LD      H,D             
5CAA: F5         PUSH    AF              
5CAB: 02         LD      (BC),A          
5CAC: F7         RST     0X30            
5CAD: 00         NOP                     
5CAE: FF         RST     0X38            
5CAF: 02         LD      (BC),A          
5CB0: 1F         RRA                     
5CB1: EA DD 22   LD      ($22DD),A       
5CB4: D7         RST     0X10            
5CB5: 20 F5      JR      NZ,$5CAC        
5CB7: 02         LD      (BC),A          
5CB8: F5         PUSH    AF              
5CB9: 62         LD      H,D             
5CBA: E5         PUSH    HL              
5CBB: C2 C5 02   JP      NZ,$02C5        
5CBE: C3 80 07   JP      $0780           
5CC1: 03         INC     BC              
5CC2: 03         INC     BC              
5CC3: 00         NOP                     
5CC4: 1F         RRA                     
5CC5: 01 3B 0D   LD      BC,$0D3B        
5CC8: 5B         LD      E,E             
5CC9: 2D         DEC     L               
5CCA: DB         ???                     
5CCB: 2C         INC     L               
5CCC: D8         RET     C               
5CCD: 2F         CPL                     
5CCE: DF         RST     0X18            
5CCF: 2F         CPL                     
5CD0: DF         RST     0X18            
5CD1: 20 DF      JR      NZ,$5CB2        
5CD3: 20 C0      JR      NZ,$5C95        
5CD5: 3F         CCF                     
5CD6: DF         RST     0X18            
5CD7: 20 BF      JR      NZ,$5C98        
5CD9: 4F         LD      C,A             
5CDA: BF         CP      A               
5CDB: 4A         LD      C,D             
5CDC: BF         CP      A               
5CDD: 4F         LD      C,A             
5CDE: FF         RST     0X38            
5CDF: 00         NOP                     
5CE0: C0         RET     NZ              
5CE1: 80         ADD     A,B             
5CE2: 80         ADD     A,B             
5CE3: 00         NOP                     
5CE4: F0 00      LD      A,($00)         
5CE6: B8         CP      B               
5CE7: 60         LD      H,B             
5CE8: B4         OR      H               
5CE9: 68         LD      L,B             
5CEA: B6         OR      (HL)            
5CEB: 68         LD      L,B             
5CEC: 36 E8      LD      (HL),$E8        
5CEE: F6 E8      OR      $E8             
5CF0: F6 08      OR      $08             
5CF2: F6 08      OR      $08             
5CF4: 06 F8      LD      B,$F8           
5CF6: F6 08      OR      $08             
5CF8: FA E4 FA   LD      A,($FAE4)       
5CFB: A4         AND     H               
5CFC: FA E4 FE   LD      A,($FEE4)       
5CFF: 00         NOP                     
5D00: 37         SCF                     
5D01: 00         NOP                     
5D02: 5F         LD      E,A             
5D03: 20 7E      JR      NZ,$5D83        
5D05: 00         NOP                     
5D06: 7F         LD      A,A             
5D07: 00         NOP                     
5D08: 55         LD      D,L             
5D09: 2E 7F      LD      L,$7F           
5D0B: 0A         LD      A,(BC)          
5D0C: 95         SUB     L               
5D0D: 6E         LD      L,(HL)          
5D0E: DE 61      SBC     $61             
5D10: BC         CP      H               
5D11: 43         LD      B,E             
5D12: FE 11      CP      $11             
5D14: 3F         CCF                     
5D15: 19         ADD     HL,DE           
5D16: 2F         CPL                     
5D17: 1F         RRA                     
5D18: 17         RLA                     
5D19: 0F         RRCA                    
5D1A: 0F         RRCA                    
5D1B: 00         NOP                     
5D1C: 1B         DEC     DE              
5D1D: 0D         DEC     C               
5D1E: 1F         RRA                     
5D1F: 00         NOP                     
5D20: 00         NOP                     
5D21: 00         NOP                     
5D22: 38 00      JR      C,$5D24         
5D24: 3C         INC     A               
5D25: 18 CE      JR      $5CF5           
5D27: 3C         INC     A               
5D28: 06 FC      LD      B,$FC           
5D2A: 06 FC      LD      B,$FC           
5D2C: 1C         INC     E               
5D2D: E0 04      LDFF00  ($04),A         
5D2F: F8 02      LDHL    SP,$02          
5D31: FC         ???                     
5D32: 01 FE 05   LD      BC,$05FE        
5D35: FA 83 FC   LD      A,($FC83)       
5D38: C2 BC FE   JP      NZ,$FEBC        
5D3B: 00         NOP                     
5D3C: D8         RET     C               
5D3D: E0 F0      LDFF00  ($F0),A         
5D3F: 00         NOP                     
5D40: 00         NOP                     
5D41: 00         NOP                     
5D42: 37         SCF                     
5D43: 00         NOP                     
5D44: 5F         LD      E,A             
5D45: 20 7E      JR      NZ,$5DC5        
5D47: 00         NOP                     
5D48: 7F         LD      A,A             
5D49: 00         NOP                     
5D4A: 55         LD      D,L             
5D4B: 2E 7F      LD      L,$7F           
5D4D: 0A         LD      A,(BC)          
5D4E: 95         SUB     L               
5D4F: 6E         LD      L,(HL)          
5D50: DE 61      SBC     $61             
5D52: BC         CP      H               
5D53: 43         LD      B,E             
5D54: FE 11      CP      $11             
5D56: 3F         CCF                     
5D57: 19         ADD     HL,DE           
5D58: 3F         CCF                     
5D59: 1F         RRA                     
5D5A: 19         ADD     HL,DE           
5D5B: 06 1F      LD      B,$1F           
5D5D: 09         ADD     HL,BC           
5D5E: 1F         RRA                     
5D5F: 00         NOP                     
5D60: 00         NOP                     
5D61: 00         NOP                     
5D62: 00         NOP                     
5D63: 00         NOP                     
5D64: 1C         INC     E               
5D65: 00         NOP                     
5D66: 2E 1C      LD      L,$1C           
5D68: CE 30      ADC     $30             
5D6A: 11 EE 23   LD      DE,$23EE        
5D6D: DC 05 FA   CALL    C,$FA05         
5D70: 01 FE 01   LD      BC,$01FE        
5D73: FE 01      CP      $01             
5D75: FE 82      CP      $82             
5D77: FC         ???                     
5D78: A4         AND     H               
5D79: D8         RET     C               
5D7A: D8         RET     C               
5D7B: 20 D0      JR      NZ,$5D4D        
5D7D: E0 F0      LDFF00  ($F0),A         
5D7F: 00         NOP                     
5D80: 03         INC     BC              
5D81: 00         NOP                     
5D82: 0F         RRCA                    
5D83: 02         LD      (BC),A          
5D84: 1B         DEC     DE              
5D85: 0C         INC     C               
5D86: 17         RLA                     
5D87: 08 0F 04   LD      ($040F),SP      
5D8A: 1E 09      LD      E,$09           
5D8C: 3F         CCF                     
5D8D: 0C         INC     C               
5D8E: 4E         LD      C,(HL)          
5D8F: 31 87 79   LD      SP,$7987        
5D92: 96         SUB     (HL)            
5D93: 69         LD      L,C             
5D94: 77         LD      (HL),A          
5D95: 0E 17      LD      C,$17           
5D97: 0F         RRCA                    
5D98: 0B         DEC     BC              
5D99: 07         RLCA                    
5D9A: 0E 01      LD      C,$01           
5D9C: 11 0E 1F   LD      DE,$1F0E        
5D9F: 00         NOP                     
5DA0: 00         NOP                     
5DA1: 00         NOP                     
5DA2: 01 00 01   LD      BC,$0100        
5DA5: 00         NOP                     
5DA6: 73         LD      (HL),E          
5DA7: 00         NOP                     
5DA8: AF         XOR     A               
5DA9: 50         LD      D,B             
5DAA: 8F         ADC     A,A             
5DAB: 74         LD      (HL),H          
5DAC: 5E         LD      E,(HL)          
5DAD: 29         ADD     HL,HL           
5DAE: 57         LD      D,A             
5DAF: 2C         INC     L               
5DB0: 2E 11      LD      L,$11           
5DB2: 27         DAA                     
5DB3: 19         ADD     HL,DE           
5DB4: 26 19      LD      H,$19           
5DB6: 17         RLA                     
5DB7: 0E 17      LD      C,$17           
5DB9: 0F         RRCA                    
5DBA: 0B         DEC     BC              
5DBB: 07         RLCA                    
5DBC: 14         INC     D               
5DBD: 0B         DEC     BC              
5DBE: 1F         RRA                     
5DBF: 00         NOP                     
5DC0: 01 00 03   LD      BC,$0300        
5DC3: 00         NOP                     
5DC4: 05         DEC     B               
5DC5: 02         LD      (BC),A          
5DC6: 09         ADD     HL,BC           
5DC7: 06 08      LD      B,$08           
5DC9: 07         RLCA                    
5DCA: 10 0F      STOP    $0F             
5DCC: 31 0E 47   LD      SP,$470E        
5DCF: 39         ADD     HL,SP           
5DD0: 8F         ADC     A,A             
5DD1: 77         LD      (HL),A          
5DD2: AF         XOR     A               
5DD3: 57         LD      D,A             
5DD4: 77         LD      (HL),A          
5DD5: 0B         DEC     BC              
5DD6: 17         RLA                     
5DD7: 0F         RRCA                    
5DD8: 0B         DEC     BC              
5DD9: 07         RLCA                    
5DDA: 0E 01      LD      C,$01           
5DDC: 11 0E 1F   LD      DE,$1F0E        
5DDF: 00         NOP                     
5DE0: 00         NOP                     
5DE1: 00         NOP                     
5DE2: 00         NOP                     
5DE3: 00         NOP                     
5DE4: 01 00 63   LD      BC,$6300        
5DE7: 00         NOP                     
5DE8: 95         SUB     L               
5DE9: 62         LD      H,D             
5DEA: 89         ADC     A,C             
5DEB: 76         HALT                    
5DEC: C8         RET     Z               
5DED: 37         SCF                     
5DEE: 41         LD      B,C             
5DEF: 3E 27      LD      A,$27           
5DF1: 19         ADD     HL,DE           
5DF2: 2F         CPL                     
5DF3: 17         RLA                     
5DF4: 2F         CPL                     
5DF5: 17         RLA                     
5DF6: 17         RLA                     
5DF7: 0B         DEC     BC              
5DF8: 17         RLA                     
5DF9: 0F         RRCA                    
5DFA: 0B         DEC     BC              
5DFB: 07         RLCA                    
5DFC: 14         INC     D               
5DFD: 0B         DEC     BC              
5DFE: 1F         RRA                     
5DFF: 00         NOP                     
5E00: 38 00      JR      C,$5E02         
5E02: 78         LD      A,B             
5E03: 30 F0      JR      NC,$5DF5        
5E05: 40         LD      B,B             
5E06: E7         RST     0X20            
5E07: 00         NOP                     
5E08: BF         CP      A               
5E09: 67         LD      H,A             
5E0A: EF         RST     0X28            
5E0B: 1F         RRA                     
5E0C: 57         LD      D,A             
5E0D: 3E 5F      LD      A,$5F           
5E0F: 2C         INC     L               
5E10: 7F         LD      A,A             
5E11: 0C         INC     C               
5E12: 7F         LD      A,A             
5E13: 34         INC     (HL)            
5E14: FB         EI                      
5E15: 77         LD      (HL),A          
5E16: F4         ???                     
5E17: 5B         LD      E,E             
5E18: FF         RST     0X38            
5E19: 60         LD      H,B             
5E1A: E2         LDFF00  (C),A           
5E1B: 5D         LD      E,L             
5E1C: C1         POP     BC              
5E1D: 22         LD      (HLI),A         
5E1E: 00         NOP                     
5E1F: 01 03 00   LD      BC,$0003        
5E22: 67         LD      H,A             
5E23: 02         LD      (BC),A          
5E24: FA 64 DC   LD      A,($DC64)       
5E27: 20 FE      JR      NZ,$5E27        
5E29: 8C         ADC     A,H             
5E2A: FB         EI                      
5E2B: D6 DD      SUB     $DD             
5E2D: 6A         LD      L,D             
5E2E: FE 69      CP      $69             
5E30: D4 6A 5C   CALL    NC,$5C6A        
5E33: E2         LDFF00  (C),A           
5E34: BC         CP      H               
5E35: C2 63 9C   JP      NZ,$9C63        
5E38: C7         RST     0X00            
5E39: 3A         LD      A,(HLD)         
5E3A: FD         ???                     
5E3B: C6 3A      ADD     $3A             
5E3D: DC FC 00   CALL    C,$00FC         
5E40: 00         NOP                     
5E41: 00         NOP                     
5E42: 00         NOP                     
5E43: 00         NOP                     
5E44: 00         NOP                     
5E45: 00         NOP                     
5E46: 00         NOP                     
5E47: 00         NOP                     
5E48: 00         NOP                     
5E49: 00         NOP                     
5E4A: 00         NOP                     
5E4B: 00         NOP                     
5E4C: 00         NOP                     
5E4D: 00         NOP                     
5E4E: 00         NOP                     
5E4F: 00         NOP                     
5E50: 00         NOP                     
5E51: 00         NOP                     
5E52: 00         NOP                     
5E53: 00         NOP                     
5E54: 00         NOP                     
5E55: 00         NOP                     
5E56: 0C         INC     C               
5E57: 00         NOP                     
5E58: 12         LD      (DE),A          
5E59: 0C         INC     C               
5E5A: 22         LD      (HLI),A         
5E5B: 1C         INC     E               
5E5C: 22         LD      (HLI),A         
5E5D: 1C         INC     E               
5E5E: 5A         LD      E,D             
5E5F: 2C         INC     L               
5E60: 5B         LD      E,E             
5E61: 2C         INC     L               
5E62: 5C         LD      E,H             
5E63: 3B         DEC     SP              
5E64: BE         CP      (HL)            
5E65: 59         LD      E,C             
5E66: BB         CP      E               
5E67: 74         LD      (HL),H          
5E68: BD         CP      L               
5E69: 76         HALT                    
5E6A: 77         LD      (HL),A          
5E6B: 2C         INC     L               
5E6C: 5F         LD      E,A             
5E6D: 2C         INC     L               
5E6E: 3F         CCF                     
5E6F: 0F         RRCA                    
5E70: 1F         RRA                     
5E71: 0F         RRCA                    
5E72: 17         RLA                     
5E73: 0F         RRCA                    
5E74: 0B         DEC     BC              
5E75: 07         RLCA                    
5E76: 07         RLCA                    
5E77: 03         INC     BC              
5E78: 02         LD      (BC),A          
5E79: 01 07 00   LD      BC,$0007        
5E7C: 0E 07      LD      C,$07           
5E7E: 0F         RRCA                    
5E7F: 00         NOP                     
5E80: 9C         SBC     H               
5E81: 00         NOP                     
5E82: F4         ???                     
5E83: 88         ADC     A,B             
5E84: 7E         LD      A,(HL)          
5E85: 80         ADD     A,B             
5E86: AF         XOR     A               
5E87: 70         LD      (HL),B          
5E88: FF         RST     0X38            
5E89: 50         LD      D,B             
5E8A: AC         XOR     H               
5E8B: 70         LD      (HL),B          
5E8C: 7E         LD      A,(HL)          
5E8D: 80         ADD     A,B             
5E8E: 11 EE 83   LD      DE,$83EE        
5E91: FC         ???                     
5E92: 85         ADD     A,L             
5E93: 7A         LD      A,D             
5E94: 81         ADD     A,C             
5E95: 7E         LD      A,(HL)          
5E96: 82         ADD     A,D             
5E97: 7C         LD      A,H             
5E98: C6 B8      ADD     $B8             
5E9A: F9         LD      SP,HL           
5E9B: 06 FB      LD      B,$FB           
5E9D: 1C         INC     E               
5E9E: FE 00      CP      $00             
5EA0: 3C         INC     A               
5EA1: 00         NOP                     
5EA2: 7E         LD      A,(HL)          
5EA3: 00         NOP                     
5EA4: FF         RST     0X38            
5EA5: 00         NOP                     
5EA6: FF         RST     0X38            
5EA7: 00         NOP                     
5EA8: FF         RST     0X38            
5EA9: 00         NOP                     
5EAA: FF         RST     0X38            
5EAB: 00         NOP                     
5EAC: 7E         LD      A,(HL)          
5EAD: 00         NOP                     
5EAE: 3C         INC     A               
5EAF: 00         NOP                     
5EB0: 00         NOP                     
5EB1: 00         NOP                     
5EB2: 00         NOP                     
5EB3: 00         NOP                     
5EB4: 00         NOP                     
5EB5: 00         NOP                     
5EB6: 00         NOP                     
5EB7: 00         NOP                     
5EB8: 00         NOP                     
5EB9: 00         NOP                     
5EBA: 00         NOP                     
5EBB: 00         NOP                     
5EBC: 00         NOP                     
5EBD: 00         NOP                     
5EBE: 00         NOP                     
5EBF: 00         NOP                     
5EC0: 00         NOP                     
5EC1: 00         NOP                     
5EC2: 3C         INC     A               
5EC3: 00         NOP                     
5EC4: 7E         LD      A,(HL)          
5EC5: 00         NOP                     
5EC6: 7E         LD      A,(HL)          
5EC7: 00         NOP                     
5EC8: 7E         LD      A,(HL)          
5EC9: 00         NOP                     
5ECA: 7E         LD      A,(HL)          
5ECB: 00         NOP                     
5ECC: 3C         INC     A               
5ECD: 00         NOP                     
5ECE: 00         NOP                     
5ECF: 00         NOP                     
5ED0: 00         NOP                     
5ED1: 00         NOP                     
5ED2: 00         NOP                     
5ED3: 00         NOP                     
5ED4: 00         NOP                     
5ED5: 00         NOP                     
5ED6: 00         NOP                     
5ED7: 00         NOP                     
5ED8: 00         NOP                     
5ED9: 00         NOP                     
5EDA: 00         NOP                     
5EDB: 00         NOP                     
5EDC: 00         NOP                     
5EDD: 00         NOP                     
5EDE: 00         NOP                     
5EDF: 00         NOP                     
5EE0: 00         NOP                     
5EE1: 00         NOP                     
5EE2: 00         NOP                     
5EE3: 00         NOP                     
5EE4: 18 00      JR      $5EE6           
5EE6: 3C         INC     A               
5EE7: 00         NOP                     
5EE8: 3C         INC     A               
5EE9: 00         NOP                     
5EEA: 18 00      JR      $5EEC           
5EEC: 00         NOP                     
5EED: 00         NOP                     
5EEE: 00         NOP                     
5EEF: 00         NOP                     
5EF0: 00         NOP                     
5EF1: 00         NOP                     
5EF2: 00         NOP                     
5EF3: 00         NOP                     
5EF4: 00         NOP                     
5EF5: 00         NOP                     
5EF6: 00         NOP                     
5EF7: 00         NOP                     
5EF8: 00         NOP                     
5EF9: 00         NOP                     
5EFA: 00         NOP                     
5EFB: 00         NOP                     
5EFC: 00         NOP                     
5EFD: 00         NOP                     
5EFE: 00         NOP                     
5EFF: 00         NOP                     
5F00: 00         NOP                     
5F01: 00         NOP                     
5F02: 00         NOP                     
5F03: 00         NOP                     
5F04: 00         NOP                     
5F05: 00         NOP                     
5F06: 00         NOP                     
5F07: 00         NOP                     
5F08: 00         NOP                     
5F09: 00         NOP                     
5F0A: 00         NOP                     
5F0B: 00         NOP                     
5F0C: 33         INC     SP              
5F0D: 00         NOP                     
5F0E: 2D         DEC     L               
5F0F: 13         INC     DE              
5F10: 33         INC     SP              
5F11: 1E 44      LD      E,$44           
5F13: 3B         DEC     SP              
5F14: E4         ???                     
5F15: 1B         DEC     DE              
5F16: 86         ADD     A,(HL)          
5F17: 7F         LD      A,A             
5F18: F1         POP     AF              
5F19: 6E         LD      L,(HL)          
5F1A: 7E         LD      A,(HL)          
5F1B: 01 3F 17   LD      BC,$173F        
5F1E: 3F         CCF                     
5F1F: 00         NOP                     
5F20: 04         INC     B               
5F21: 00         NOP                     
5F22: 08 00 08   LD      ($0800),SP      
5F25: 00         NOP                     
5F26: 0C         INC     C               
5F27: 00         NOP                     
5F28: 06 00      LD      B,$00           
5F2A: 02         LD      (BC),A          
5F2B: 00         NOP                     
5F2C: E3         ???                     
5F2D: 00         NOP                     
5F2E: 91         SUB     C               
5F2F: 60         LD      H,B             
5F30: 8B         ADC     A,E             
5F31: 70         LD      (HL),B          
5F32: 25         DEC     H               
5F33: DA 42 BC   JP      C,$BC42         
5F36: 42         LD      B,D             
5F37: BC         CP      H               
5F38: 46         LD      B,(HL)          
5F39: B8         CP      B               
5F3A: 74         LD      (HL),H          
5F3B: 88         ADC     A,B             
5F3C: E4         ???                     
5F3D: 78         LD      A,B             
5F3E: F8 00      LDHL    SP,$00          
5F40: 00         NOP                     
5F41: 00         NOP                     
5F42: 00         NOP                     
5F43: 00         NOP                     
5F44: 19         ADD     HL,DE           
5F45: 00         NOP                     
5F46: 16 09      LD      D,$09           
5F48: 19         ADD     HL,DE           
5F49: 0F         RRCA                    
5F4A: 22         LD      (HLI),A         
5F4B: 1D         DEC     E               
5F4C: 72         LD      (HL),D          
5F4D: 0D         DEC     C               
5F4E: 43         LD      B,E             
5F4F: 3F         CCF                     
5F50: 78         LD      A,B             
5F51: 37         SCF                     
5F52: 3F         CCF                     
5F53: 00         NOP                     
5F54: 1E 0F      LD      E,$0F           
5F56: 37         SCF                     
5F57: 1E 3F      LD      E,$3F           
5F59: 15         DEC     D               
5F5A: 3B         DEC     SP              
5F5B: 04         INC     B               
5F5C: 75         LD      (HL),L          
5F5D: 3A         LD      A,(HLD)         
5F5E: 7F         LD      A,A             
5F5F: 00         NOP                     
5F60: 00         NOP                     
5F61: 00         NOP                     
5F62: 00         NOP                     
5F63: 00         NOP                     
5F64: C0         RET     NZ              
5F65: 00         NOP                     
5F66: C3 80 C6   JP      $C680           
5F69: 00         NOP                     
5F6A: 44         LD      B,H             
5F6B: 80         ADD     A,B             
5F6C: 24         INC     H               
5F6D: C0         RET     NZ              
5F6E: 16 E0      LD      D,$E0           
5F70: 93         SUB     E               
5F71: 60         LD      H,B             
5F72: 09         ADD     HL,BC           
5F73: F0 09      LD      A,($09)         
5F75: F0 CB      LD      A,($CB)         
5F77: B0         OR      B               
5F78: CF         RST     0X08            
5F79: B0         OR      B               
5F7A: FA 04 6C   LD      A,($6C04)       
5F7D: F0 F8      LD      A,($F8)         
5F7F: 00         NOP                     
5F80: 00         NOP                     
5F81: FF         RST     0X38            
5F82: 00         NOP                     
5F83: FF         RST     0X38            
5F84: 22         LD      (HLI),A         
5F85: FF         RST     0X38            
5F86: 14         INC     D               
5F87: FF         RST     0X38            
5F88: 08 FF 14   LD      ($14FF),SP      
5F8B: FF         RST     0X38            
5F8C: 22         LD      (HLI),A         
5F8D: FF         RST     0X38            
5F8E: 00         NOP                     
5F8F: FF         RST     0X38            
5F90: 00         NOP                     
5F91: FF         RST     0X38            
5F92: 00         NOP                     
5F93: FF         RST     0X38            
5F94: 22         LD      (HLI),A         
5F95: FF         RST     0X38            
5F96: 14         INC     D               
5F97: FF         RST     0X38            
5F98: 08 FF 14   LD      ($14FF),SP      
5F9B: FF         RST     0X38            
5F9C: 22         LD      (HLI),A         
5F9D: FF         RST     0X38            
5F9E: 00         NOP                     
5F9F: FF         RST     0X38            
5FA0: 00         NOP                     
5FA1: FF         RST     0X38            
5FA2: 00         NOP                     
5FA3: FF         RST     0X38            
5FA4: 22         LD      (HLI),A         
5FA5: FF         RST     0X38            
5FA6: 14         INC     D               
5FA7: FF         RST     0X38            
5FA8: 08 FF 14   LD      ($14FF),SP      
5FAB: FF         RST     0X38            
5FAC: 22         LD      (HLI),A         
5FAD: FF         RST     0X38            
5FAE: 00         NOP                     
5FAF: FF         RST     0X38            
5FB0: 00         NOP                     
5FB1: FF         RST     0X38            
5FB2: 00         NOP                     
5FB3: FF         RST     0X38            
5FB4: 22         LD      (HLI),A         
5FB5: FF         RST     0X38            
5FB6: 14         INC     D               
5FB7: FF         RST     0X38            
5FB8: 08 FF 14   LD      ($14FF),SP      
5FBB: FF         RST     0X38            
5FBC: 22         LD      (HLI),A         
5FBD: FF         RST     0X38            
5FBE: 00         NOP                     
5FBF: FF         RST     0X38            
5FC0: 00         NOP                     
5FC1: FF         RST     0X38            
5FC2: 00         NOP                     
5FC3: FF         RST     0X38            
5FC4: 22         LD      (HLI),A         
5FC5: FF         RST     0X38            
5FC6: 14         INC     D               
5FC7: FF         RST     0X38            
5FC8: 08 FF 14   LD      ($14FF),SP      
5FCB: FF         RST     0X38            
5FCC: 22         LD      (HLI),A         
5FCD: FF         RST     0X38            
5FCE: 00         NOP                     
5FCF: FF         RST     0X38            
5FD0: 00         NOP                     
5FD1: FF         RST     0X38            
5FD2: 00         NOP                     
5FD3: FF         RST     0X38            
5FD4: 22         LD      (HLI),A         
5FD5: FF         RST     0X38            
5FD6: 14         INC     D               
5FD7: FF         RST     0X38            
5FD8: 08 FF 14   LD      ($14FF),SP      
5FDB: FF         RST     0X38            
5FDC: 22         LD      (HLI),A         
5FDD: FF         RST     0X38            
5FDE: 00         NOP                     
5FDF: FF         RST     0X38            
5FE0: 00         NOP                     
5FE1: FF         RST     0X38            
5FE2: 00         NOP                     
5FE3: FF         RST     0X38            
5FE4: 22         LD      (HLI),A         
5FE5: FF         RST     0X38            
5FE6: 14         INC     D               
5FE7: FF         RST     0X38            
5FE8: 08 FF 14   LD      ($14FF),SP      
5FEB: FF         RST     0X38            
5FEC: 22         LD      (HLI),A         
5FED: FF         RST     0X38            
5FEE: 00         NOP                     
5FEF: FF         RST     0X38            
5FF0: 00         NOP                     
5FF1: FF         RST     0X38            
5FF2: 00         NOP                     
5FF3: FF         RST     0X38            
5FF4: 22         LD      (HLI),A         
5FF5: FF         RST     0X38            
5FF6: 14         INC     D               
5FF7: FF         RST     0X38            
5FF8: 08 FF 14   LD      ($14FF),SP      
5FFB: FF         RST     0X38            
5FFC: 22         LD      (HLI),A         
5FFD: FF         RST     0X38            
5FFE: 00         NOP                     
5FFF: FF         RST     0X38            
6000: 00         NOP                     
6001: 00         NOP                     
6002: 00         NOP                     
6003: 00         NOP                     
6004: 00         NOP                     
6005: 00         NOP                     
6006: 00         NOP                     
6007: 00         NOP                     
6008: 00         NOP                     
6009: 00         NOP                     
600A: 03         INC     BC              
600B: 04         INC     B               
600C: 0F         RRCA                    
600D: 00         NOP                     
600E: 0F         RRCA                    
600F: 10 1F      STOP    $1F             
6011: 00         NOP                     
6012: 1F         RRA                     
6013: 00         NOP                     
6014: 1F         RRA                     
6015: 08 1B 0E   LD      ($0E1B),SP      
6018: 1E 03      LD      E,$03           
601A: 0F         RRCA                    
601B: 00         NOP                     
601C: 03         INC     BC              
601D: 04         INC     B               
601E: 00         NOP                     
601F: 00         NOP                     
6020: 00         NOP                     
6021: 00         NOP                     
6022: 00         NOP                     
6023: 00         NOP                     
6024: 00         NOP                     
6025: 00         NOP                     
6026: 00         NOP                     
6027: 00         NOP                     
6028: 00         NOP                     
6029: 00         NOP                     
602A: C0         RET     NZ              
602B: 20 70      JR      NZ,$609D        
602D: 80         ADD     A,B             
602E: F0 08      LD      A,($08)         
6030: 58         LD      E,B             
6031: E0 F8      LDFF00  ($F8),A         
6033: A0         AND     B               
6034: 58         LD      E,B             
6035: E0 F8      LDFF00  ($F8),A         
6037: 00         NOP                     
6038: F0 08      LD      A,($08)         
603A: F0 00      LD      A,($00)         
603C: C0         RET     NZ              
603D: 20 00      JR      NZ,$603F        
603F: 00         NOP                     
6040: 00         NOP                     
6041: 00         NOP                     
6042: 00         NOP                     
6043: 00         NOP                     
6044: 00         NOP                     
6045: 00         NOP                     
6046: 00         NOP                     
6047: 00         NOP                     
6048: 00         NOP                     
6049: 00         NOP                     
604A: 03         INC     BC              
604B: 04         INC     B               
604C: 0F         RRCA                    
604D: 00         NOP                     
604E: 0F         RRCA                    
604F: 10 1F      STOP    $1F             
6051: 0C         INC     C               
6052: 1F         RRA                     
6053: 0B         DEC     BC              
6054: 0F         RRCA                    
6055: 02         LD      (BC),A          
6056: 17         RLA                     
6057: 08 10 0F   LD      ($0F10),SP      
605A: 0F         RRCA                    
605B: 00         NOP                     
605C: 03         INC     BC              
605D: 04         INC     B               
605E: 00         NOP                     
605F: 00         NOP                     
6060: 00         NOP                     
6061: 00         NOP                     
6062: 00         NOP                     
6063: 00         NOP                     
6064: 00         NOP                     
6065: 00         NOP                     
6066: 00         NOP                     
6067: 00         NOP                     
6068: 00         NOP                     
6069: 00         NOP                     
606A: C0         RET     NZ              
606B: 20 70      JR      NZ,$60DD        
606D: 80         ADD     A,B             
606E: F0 08      LD      A,($08)         
6070: A8         XOR     B               
6071: 70         LD      (HL),B          
6072: F8 50      LDHL    SP,$50          
6074: A8         XOR     B               
6075: F0 78      LD      A,($78)         
6077: 80         ADD     A,B             
6078: F0 08      LD      A,($08)         
607A: F0 00      LD      A,($00)         
607C: C0         RET     NZ              
607D: 20 00      JR      NZ,$607F        
607F: 00         NOP                     
6080: 00         NOP                     
6081: 00         NOP                     
6082: 00         NOP                     
6083: 00         NOP                     
6084: 00         NOP                     
6085: 00         NOP                     
6086: 07         RLCA                    
6087: 00         NOP                     
6088: 18 07      JR      $6091           
608A: 26 19      LD      H,$19           
608C: 27         DAA                     
608D: 1A         LD      A,(DE)          
608E: 4F         LD      C,A             
608F: 33         INC     SP              
6090: 5F         LD      E,A             
6091: 2B         DEC     HL              
6092: 3F         CCF                     
6093: 0F         RRCA                    
6094: 1F         RRA                     
6095: 07         RLCA                    
6096: 1F         RRA                     
6097: 0A         LD      A,(BC)          
6098: 1F         RRA                     
6099: 0D         DEC     C               
609A: 1F         RRA                     
609B: 00         NOP                     
609C: 3F         CCF                     
609D: 1B         DEC     DE              
609E: 3F         CCF                     
609F: 00         NOP                     
60A0: 00         NOP                     
60A1: 00         NOP                     
60A2: 00         NOP                     
60A3: 00         NOP                     
60A4: 00         NOP                     
60A5: 00         NOP                     
60A6: C0         RET     NZ              
60A7: 00         NOP                     
60A8: 20 C0      JR      NZ,$606A        
60AA: 1C         INC     E               
60AB: E0 82      LDFF00  ($82),A         
60AD: 7C         LD      A,H             
60AE: D2 2C FA   JP      NC,$FA2C        
60B1: 54         LD      D,H             
60B2: FC         ???                     
60B3: F0 EA      LD      A,($EA)         
60B5: 14         INC     D               
60B6: F9         LD      SP,HL           
60B7: C6 CD      ADD     $CD             
60B9: B2         OR      D               
60BA: D5         PUSH    DE              
60BB: 2A         LD      A,(HLI)         
60BC: 66         LD      H,(HL)          
60BD: 98         SBC     B               
60BE: FC         ???                     
60BF: 00         NOP                     
60C0: 00         NOP                     
60C1: FF         RST     0X38            
60C2: 00         NOP                     
60C3: FF         RST     0X38            
60C4: 22         LD      (HLI),A         
60C5: FF         RST     0X38            
60C6: 14         INC     D               
60C7: FF         RST     0X38            
60C8: 08 FF 14   LD      ($14FF),SP      
60CB: FF         RST     0X38            
60CC: 22         LD      (HLI),A         
60CD: FF         RST     0X38            
60CE: 00         NOP                     
60CF: FF         RST     0X38            
60D0: 00         NOP                     
60D1: FF         RST     0X38            
60D2: 00         NOP                     
60D3: FF         RST     0X38            
60D4: 22         LD      (HLI),A         
60D5: FF         RST     0X38            
60D6: 14         INC     D               
60D7: FF         RST     0X38            
60D8: 08 FF 14   LD      ($14FF),SP      
60DB: FF         RST     0X38            
60DC: 22         LD      (HLI),A         
60DD: FF         RST     0X38            
60DE: 00         NOP                     
60DF: FF         RST     0X38            
60E0: 00         NOP                     
60E1: 00         NOP                     
60E2: 00         NOP                     
60E3: 00         NOP                     
60E4: 00         NOP                     
60E5: 02         LD      (BC),A          
60E6: 02         LD      (BC),A          
60E7: 05         DEC     B               
60E8: 02         LD      (BC),A          
60E9: 05         DEC     B               
60EA: 02         LD      (BC),A          
60EB: 05         DEC     B               
60EC: 02         LD      (BC),A          
60ED: 05         DEC     B               
60EE: 02         LD      (BC),A          
60EF: 05         DEC     B               
60F0: 02         LD      (BC),A          
60F1: 1D         DEC     E               
60F2: 1E 21      LD      E,$21           
60F4: 2E 51      LD      L,$51           
60F6: 3E 41      LD      A,$41           
60F8: 3C         INC     A               
60F9: 42         LD      B,D             
60FA: 00         NOP                     
60FB: 3C         INC     A               
60FC: 00         NOP                     
60FD: 00         NOP                     
60FE: 00         NOP                     
60FF: 00         NOP                     
6100: 00         NOP                     
6101: 00         NOP                     
6102: 01 00 01   LD      BC,$0100        
6105: 00         NOP                     
6106: 03         INC     BC              
6107: 01 03 01   LD      BC,$0103        
610A: 0F         RRCA                    
610B: 00         NOP                     
610C: 1E 01      LD      E,$01           
610E: 1F         RRA                     
610F: 20 3E      JR      NZ,$614F        
6111: 01 3F 01   LD      BC,$013F        
6114: 3E 11      LD      A,$11           
6116: 37         SCF                     
6117: 1C         INC     E               
6118: 3D         DEC     A               
6119: 06 1F      LD      B,$1F           
611B: 00         NOP                     
611C: 07         RLCA                    
611D: 08 00 00   LD      ($0000),SP      
6120: C0         RET     NZ              
6121: 00         NOP                     
6122: E6 C0      AND     $C0             
6124: EF         RST     0X28            
6125: C6 FF      ADD     $FF             
6127: 8E         ADC     A,(HL)          
6128: DF         RST     0X18            
6129: 6E         LD      L,(HL)          
612A: 9F         SBC     A               
612B: 66         LD      H,(HL)          
612C: FF         RST     0X38            
612D: 0E FF      LD      C,$FF           
612F: 0E BF      LD      C,$BF           
6131: C6 F6      ADD     $F6             
6133: 40         LD      B,B             
6134: B0         OR      B               
6135: C0         RET     NZ              
6136: F0 00      LD      A,($00)         
6138: E0 10      LDFF00  ($10),A         
613A: E0 00      LDFF00  ($00),A         
613C: 80         ADD     A,B             
613D: 40         LD      B,B             
613E: 00         NOP                     
613F: 00         NOP                     
6140: 00         NOP                     
6141: 00         NOP                     
6142: 00         NOP                     
6143: 00         NOP                     
6144: 01 00 01   LD      BC,$0100        
6147: 00         NOP                     
6148: 03         INC     BC              
6149: 01 0F 00   LD      BC,$000F        
614C: 1E 01      LD      E,$01           
614E: 1F         RRA                     
614F: 20 3F      JR      NZ,$6190        
6151: 18 3F      JR      $6192           
6153: 16 1F      LD      D,$1F           
6155: 05         DEC     B               
6156: 2E 11      LD      L,$11           
6158: 21 1E 1F   LD      HL,$1F1E        
615B: 00         NOP                     
615C: 07         RLCA                    
615D: 08 00 00   LD      ($0000),SP      
6160: 00         NOP                     
6161: 00         NOP                     
6162: C0         RET     NZ              
6163: 00         NOP                     
6164: E6 C0      AND     $C0             
6166: EF         RST     0X28            
6167: C6 FF      ADD     $FF             
6169: 8E         ADC     A,(HL)          
616A: DF         RST     0X18            
616B: 6E         LD      L,(HL)          
616C: DF         RST     0X18            
616D: 26 FF      LD      H,$FF           
616F: 0E 5F      LD      C,$5F           
6171: EE FF      XOR     $FF             
6173: A6         AND     (HL)            
6174: 56         LD      D,(HL)          
6175: E0 F0      LDFF00  ($F0),A         
6177: 00         NOP                     
6178: E0 10      LDFF00  ($10),A         
617A: E0 00      LDFF00  ($00),A         
617C: 80         ADD     A,B             
617D: 40         LD      B,B             
617E: 00         NOP                     
617F: 00         NOP                     
6180: 00         NOP                     
6181: 00         NOP                     
6182: 10 10      STOP    $10             
6184: 00         NOP                     
6185: 00         NOP                     
6186: 00         NOP                     
6187: 82         ADD     A,D             
6188: 00         NOP                     
6189: 38 38      JR      C,$61C3         
618B: 7C         LD      A,H             
618C: 5C         LD      E,H             
618D: FE 3E      CP      $3E             
618F: 7F         LD      A,A             
6190: 7E         LD      A,(HL)          
6191: FF         RST     0X38            
6192: 07         RLCA                    
6193: FF         RST     0X38            
6194: 03         INC     BC              
6195: 07         RLCA                    
6196: 01 03 41   LD      BC,$4103        
6199: 43         LD      B,E             
619A: 01 13 00   LD      BC,$0013        
619D: 01 00 01   LD      BC,$0100        
61A0: 00         NOP                     
61A1: C0         RET     NZ              
61A2: 00         NOP                     
61A3: 60         LD      H,B             
61A4: 00         NOP                     
61A5: 71         LD      (HL),C          
61A6: 00         NOP                     
61A7: 33         INC     SP              
61A8: 00         NOP                     
61A9: 37         SCF                     
61AA: 00         NOP                     
61AB: 36 00      LD      (HL),$00        
61AD: 16 00      LD      D,$00           
61AF: 14         INC     D               
61B0: 00         NOP                     
61B1: 00         NOP                     
61B2: 00         NOP                     
61B3: 00         NOP                     
61B4: 00         NOP                     
61B5: 00         NOP                     
61B6: 00         NOP                     
61B7: 00         NOP                     
61B8: 00         NOP                     
61B9: 00         NOP                     
61BA: 00         NOP                     
61BB: 00         NOP                     
61BC: 00         NOP                     
61BD: 00         NOP                     
61BE: 00         NOP                     
61BF: 00         NOP                     
61C0: 00         NOP                     
61C1: 00         NOP                     
61C2: 00         NOP                     
61C3: 00         NOP                     
61C4: 00         NOP                     
61C5: 00         NOP                     
61C6: 30 10      JR      NC,$61D8        
61C8: 30 10      JR      NC,$61DA        
61CA: 1C         INC     E               
61CB: 0C         INC     C               
61CC: 0F         RRCA                    
61CD: 03         INC     BC              
61CE: 03         INC     BC              
61CF: 00         NOP                     
61D0: 00         NOP                     
61D1: 00         NOP                     
61D2: 00         NOP                     
61D3: 00         NOP                     
61D4: 00         NOP                     
61D5: 00         NOP                     
61D6: 00         NOP                     
61D7: 00         NOP                     
61D8: 00         NOP                     
61D9: 00         NOP                     
61DA: 00         NOP                     
61DB: 00         NOP                     
61DC: 00         NOP                     
61DD: 00         NOP                     
61DE: 00         NOP                     
61DF: 00         NOP                     
61E0: 00         NOP                     
61E1: 00         NOP                     
61E2: 00         NOP                     
61E3: 00         NOP                     
61E4: 00         NOP                     
61E5: 00         NOP                     
61E6: 00         NOP                     
61E7: 00         NOP                     
61E8: 07         RLCA                    
61E9: 00         NOP                     
61EA: 08 07 11   LD      ($1107),SP      
61ED: 0F         RRCA                    
61EE: 13         INC     DE              
61EF: 0F         RRCA                    
61F0: 0B         DEC     BC              
61F1: 07         RLCA                    
61F2: 09         ADD     HL,BC           
61F3: 07         RLCA                    
61F4: 08 07 04   LD      ($0407),SP      
61F7: 03         INC     BC              
61F8: 03         INC     BC              
61F9: 00         NOP                     
61FA: 00         NOP                     
61FB: 00         NOP                     
61FC: 00         NOP                     
61FD: 00         NOP                     
61FE: 00         NOP                     
61FF: 00         NOP                     
6200: 15         DEC     D               
6201: 00         NOP                     
6202: 1F         RRA                     
6203: 00         NOP                     
6204: 1F         RRA                     
6205: 00         NOP                     
6206: 3F         CCF                     
6207: 07         RLCA                    
6208: 7F         LD      A,A             
6209: 2D         DEC     L               
620A: 7F         LD      A,A             
620B: 28 5B      JR      Z,$6268         
620D: 37         SCF                     
620E: 38 17      JR      C,$6227         
6210: 3F         CCF                     
6211: 10 3F      STOP    $3F             
6213: 08 7F 27   LD      ($277F),SP      
6216: 77         LD      (HL),A          
6217: 28 33      JR      Z,$624C         
6219: 0F         RRCA                    
621A: 1E 01      LD      E,$01           
621C: 3D         DEC     A               
621D: 1E 1F      LD      E,$1F           
621F: 00         NOP                     
6220: E0 00      LDFF00  ($00),A         
6222: F8 00      LDHL    SP,$00          
6224: FC         ???                     
6225: 00         NOP                     
6226: FC         ???                     
6227: E0 FE      LDFF00  ($FE),A         
6229: B4         OR      H               
622A: FE B4      CP      $B4             
622C: 3A         LD      A,(HLD)         
622D: FC         ???                     
622E: 3C         INC     A               
622F: C8         RET     Z               
6230: FC         ???                     
6231: 18 FA      JR      $622D           
6233: 34         INC     (HL)            
6234: F2         ???                     
6235: CC FA 34   CALL    Z,$34FA         
6238: FC         ???                     
6239: B0         OR      B               
623A: 38 C0      JR      C,$61FC         
623C: FC         ???                     
623D: 00         NOP                     
623E: F0 00      LD      A,($00)         
6240: 73         LD      (HL),E          
6241: 00         NOP                     
6242: FF         RST     0X38            
6243: 70         LD      (HL),B          
6244: FF         RST     0X38            
6245: 75         LD      (HL),L          
6246: FF         RST     0X38            
6247: 60         LD      H,B             
6248: FB         EI                      
6249: 07         RLCA                    
624A: 98         SBC     B               
624B: 67         LD      H,A             
624C: 9F         SBC     A               
624D: 60         LD      H,B             
624E: 4F         LD      C,A             
624F: 30 4F      JR      NC,$62A0        
6251: 36 2B      LD      (HL),$2B        
6253: 16 15      LD      D,$15           
6255: 0B         DEC     BC              
6256: 1B         DEC     DE              
6257: 0C         INC     C               
6258: 27         DAA                     
6259: 1F         RRA                     
625A: 78         LD      A,B             
625B: 07         RLCA                    
625C: F7         RST     0X30            
625D: 78         LD      A,B             
625E: FF         RST     0X38            
625F: 00         NOP                     
6260: 00         NOP                     
6261: 00         NOP                     
6262: 00         NOP                     
6263: 00         NOP                     
6264: 7E         LD      A,(HL)          
6265: 00         NOP                     
6266: FF         RST     0X38            
6267: 00         NOP                     
6268: FF         RST     0X38            
6269: 00         NOP                     
626A: 7E         LD      A,(HL)          
626B: 00         NOP                     
626C: 00         NOP                     
626D: 00         NOP                     
626E: 00         NOP                     
626F: 00         NOP                     
6270: 00         NOP                     
6271: 00         NOP                     
6272: 00         NOP                     
6273: 00         NOP                     
6274: 00         NOP                     
6275: 00         NOP                     
6276: 00         NOP                     
6277: 00         NOP                     
6278: 00         NOP                     
6279: 00         NOP                     
627A: 00         NOP                     
627B: 00         NOP                     
627C: 00         NOP                     
627D: 00         NOP                     
627E: 00         NOP                     
627F: 00         NOP                     
6280: E0 00      LDFF00  ($00),A         
6282: F8 00      LDHL    SP,$00          
6284: FC         ???                     
6285: A0         AND     B               
6286: FC         ???                     
6287: A0         AND     B               
6288: 7E         LD      A,(HL)          
6289: F0 7E      LD      A,($7E)         
628B: 94         SUB     H               
628C: FE 1C      CP      $1C             
628E: FA 3C FC   LD      A,($FC3C)       
6291: 78         LD      A,B             
6292: FA 74 B9   LD      A,($B974)       
6295: C6 FD      ADD     $FD             
6297: 1A         LD      A,(DE)          
6298: BE         CP      (HL)            
6299: D8         RET     C               
629A: 1E E0      LD      E,$E0           
629C: EF         RST     0X28            
629D: 1E FF      LD      E,$FF           
629F: 00         NOP                     
62A0: 00         NOP                     
62A1: 00         NOP                     
62A2: 00         NOP                     
62A3: 00         NOP                     
62A4: 00         NOP                     
62A5: 00         NOP                     
62A6: 00         NOP                     
62A7: 00         NOP                     
62A8: 03         INC     BC              
62A9: 00         NOP                     
62AA: 05         DEC     B               
62AB: 03         INC     BC              
62AC: 09         ADD     HL,BC           
62AD: 07         RLCA                    
62AE: 10 0F      STOP    $0F             
62B0: 10 0F      STOP    $0F             
62B2: 10 0F      STOP    $0F             
62B4: 0C         INC     C               
62B5: 03         INC     BC              
62B6: 03         INC     BC              
62B7: 00         NOP                     
62B8: 03         INC     BC              
62B9: 01 03 01   LD      BC,$0103        
62BC: 01 00 00   LD      BC,$0000        
62BF: 00         NOP                     
62C0: 00         NOP                     
62C1: 00         NOP                     
62C2: 61         LD      H,C             
62C3: 00         NOP                     
62C4: 71         LD      (HL),C          
62C5: 20 3F      JR      NZ,$6306        
62C7: 10 1F      STOP    $1F             
62C9: 00         NOP                     
62CA: 14         INC     D               
62CB: 0F         RRCA                    
62CC: 6F         LD      L,A             
62CD: 1B         DEC     DE              
62CE: EF         RST     0X28            
62CF: 5B         LD      E,E             
62D0: 6F         LD      L,A             
62D1: 1B         DEC     DE              
62D2: 14         INC     D               
62D3: 0F         RRCA                    
62D4: 1F         RRA                     
62D5: 00         NOP                     
62D6: 3F         CCF                     
62D7: 10 6F      STOP    $6F             
62D9: 30 F3      JR      NC,$62CE        
62DB: 41         LD      B,C             
62DC: C3 01 01   JP      $0101           
62DF: 00         NOP                     
62E0: 80         ADD     A,B             
62E1: 00         NOP                     
62E2: C3 80 CF   JP      $CF80           
62E5: 82         ADD     A,D             
62E6: FE 0C      CP      $0C             
62E8: F4         ???                     
62E9: 18 B8      JR      $62A3           
62EB: C0         RET     NZ              
62EC: D8         RET     C               
62ED: 60         LD      H,B             
62EE: DE 60      SBC     $60             
62F0: DF         RST     0X18            
62F1: 6E         LD      L,(HL)          
62F2: BE         CP      (HL)            
62F3: C0         RET     NZ              
62F4: F8 00      LDHL    SP,$00          
62F6: F8 10      LDHL    SP,$10          
62F8: EC         ???                     
62F9: 18 9E      JR      $6299           
62FB: 04         INC     B               
62FC: 86         ADD     A,(HL)          
62FD: 00         NOP                     
62FE: 00         NOP                     
62FF: 00         NOP                     
6300: 07         RLCA                    
6301: 00         NOP                     
6302: E8 07      ADD     SP,$07          
6304: 91         SUB     C               
6305: 6F         LD      L,A             
6306: 53         LD      D,E             
6307: 2F         CPL                     
6308: 21 1F 2C   LD      HL,$2C1F        
630B: 1F         RRA                     
630C: 2F         CPL                     
630D: 1B         DEC     DE              
630E: 2F         CPL                     
630F: 19         ADD     HL,DE           
6310: 37         SCF                     
6311: 0D         DEC     C               
6312: 57         LD      D,A             
6313: 2F         CPL                     
6314: 9C         SBC     H               
6315: 63         LD      H,E             
6316: A5         AND     L               
6317: 43         LD      B,E             
6318: CF         RST     0X08            
6319: 00         NOP                     
631A: 13         INC     DE              
631B: 0F         RRCA                    
631C: 1F         RRA                     
631D: 00         NOP                     
631E: 00         NOP                     
631F: 00         NOP                     
6320: 00         NOP                     
6321: 00         NOP                     
6322: 07         RLCA                    
6323: 00         NOP                     
6324: 08 07 71   LD      ($7107),SP      
6327: 0F         RRCA                    
6328: 93         SUB     E               
6329: 6F         LD      L,A             
632A: E1         POP     HL              
632B: 1F         RRA                     
632C: 2C         INC     L               
632D: 1F         RRA                     
632E: 6F         LD      L,A             
632F: 1B         DEC     DE              
6330: AF         XOR     A               
6331: 59         LD      E,C             
6332: B7         OR      A               
6333: 4D         LD      C,L             
6334: F7         RST     0X30            
6335: 0F         RRCA                    
6336: 0C         INC     C               
6337: 03         INC     BC              
6338: 05         DEC     B               
6339: 03         INC     BC              
633A: 0F         RRCA                    
633B: 00         NOP                     
633C: 13         INC     DE              
633D: 0F         RRCA                    
633E: 1F         RRA                     
633F: 00         NOP                     
6340: 1C         INC     E               
6341: 00         NOP                     
6342: 13         INC     DE              
6343: 0C         INC     C               
6344: 6D         LD      L,L             
6345: 03         INC     BC              
6346: 57         LD      D,A             
6347: 22         LD      (HLI),A         
6348: 7B         LD      A,E             
6349: 27         DAA                     
634A: 7B         LD      A,E             
634B: 2F         CPL                     
634C: 7B         LD      A,E             
634D: 2E 7B      LD      L,$7B           
634F: 2F         CPL                     
6350: 71         LD      (HL),C          
6351: 2F         CPL                     
6352: 5C         LD      E,H             
6353: 23         INC     HL              
6354: 5F         LD      E,A             
6355: 20 6F      JR      NZ,$63C6        
6357: 03         INC     BC              
6358: 09         ADD     HL,BC           
6359: 06 13      LD      B,$13           
635B: 0C         INC     C               
635C: 1C         INC     E               
635D: 00         NOP                     
635E: 00         NOP                     
635F: 00         NOP                     
6360: F0 00      LD      A,($00)         
6362: EC         ???                     
6363: F0 EA      LD      A,($EA)         
6365: 3C         INC     A               
6366: DD         ???                     
6367: 7E         LD      A,(HL)          
6368: DD         ???                     
6369: FE C9      CP      $C9             
636B: FE E1      CP      $E1             
636D: 7E         LD      A,(HL)          
636E: E1         POP     HL              
636F: 3E E1      LD      A,$E1           
6371: BE         CP      (HL)            
6372: E2         LDFF00  (C),A           
6373: FC         ???                     
6374: 3E C0      LD      A,$C0           
6376: FE 18      CP      $18             
6378: F2         ???                     
6379: 0C         INC     C               
637A: F9         LD      SP,HL           
637B: 06 07      LD      B,$07           
637D: 00         NOP                     
637E: 00         NOP                     
637F: 00         NOP                     
6380: 03         INC     BC              
6381: 00         NOP                     
6382: 07         RLCA                    
6383: 01 CB 06   LD      BC,$06CB        
6386: AF         XOR     A               
6387: 44         LD      B,H             
6388: F7         RST     0X30            
6389: 4F         LD      C,A             
638A: F7         RST     0X30            
638B: 5F         LD      E,A             
638C: F7         RST     0X30            
638D: 5C         LD      E,H             
638E: F7         RST     0X30            
638F: 5E         LD      E,(HL)          
6390: E3         ???                     
6391: 5F         LD      E,A             
6392: B9         CP      C               
6393: 47         LD      B,A             
6394: BE         CP      (HL)            
6395: 41         LD      B,C             
6396: DF         RST     0X18            
6397: 06 09      LD      B,$09           
6399: 06 09      LD      B,$09           
639B: 06 05      LD      B,$05           
639D: 02         LD      (BC),A          
639E: 03         INC     BC              
639F: 00         NOP                     
63A0: E0 00      LDFF00  ($00),A         
63A2: D8         RET     C               
63A3: E0 D4      LDFF00  ($D4),A         
63A5: 78         LD      A,B             
63A6: BA         CP      D               
63A7: FC         ???                     
63A8: BA         CP      D               
63A9: FC         ???                     
63AA: 92         SUB     D               
63AB: FC         ???                     
63AC: C2 FC C2   JP      NZ,$C2FC        
63AF: 7C         LD      A,H             
63B0: C2 7C C4   JP      NZ,$C47C        
63B3: F8 3C      LDHL    SP,$3C          
63B5: C0         RET     NZ              
63B6: 7C         LD      A,H             
63B7: B0         OR      B               
63B8: CC 30 C8   CALL    Z,$C830         
63BB: 30 50      JR      NC,$640D        
63BD: 20 60      JR      NZ,$641F        
63BF: 00         NOP                     
63C0: 00         NOP                     
63C1: 00         NOP                     
63C2: 00         NOP                     
63C3: 00         NOP                     
63C4: 00         NOP                     
63C5: 00         NOP                     
63C6: 07         RLCA                    
63C7: 00         NOP                     
63C8: 09         ADD     HL,BC           
63C9: 06 13      LD      B,$13           
63CB: 0D         DEC     C               
63CC: 17         RLA                     
63CD: 0B         DEC     BC              
63CE: 17         RLA                     
63CF: 0B         DEC     BC              
63D0: 17         RLA                     
63D1: 09         ADD     HL,BC           
63D2: 19         ADD     HL,DE           
63D3: 06 11      LD      B,$11           
63D5: 0E 08      LD      C,$08           
63D7: 07         RLCA                    
63D8: 07         RLCA                    
63D9: 00         NOP                     
63DA: 00         NOP                     
63DB: 00         NOP                     
63DC: 00         NOP                     
63DD: 00         NOP                     
63DE: 00         NOP                     
63DF: 00         NOP                     
63E0: 00         NOP                     
63E1: 00         NOP                     
63E2: 3C         INC     A               
63E3: 00         NOP                     
63E4: 5A         LD      E,D             
63E5: 3C         INC     A               
63E6: 7E         LD      A,(HL)          
63E7: 3C         INC     A               
63E8: 7E         LD      A,(HL)          
63E9: 3C         INC     A               
63EA: 5A         LD      E,D             
63EB: 3C         INC     A               
63EC: 3C         INC     A               
63ED: 00         NOP                     
63EE: 00         NOP                     
63EF: 00         NOP                     
63F0: 00         NOP                     
63F1: 00         NOP                     
63F2: 00         NOP                     
63F3: 00         NOP                     
63F4: 00         NOP                     
63F5: 00         NOP                     
63F6: 00         NOP                     
63F7: 00         NOP                     
63F8: 00         NOP                     
63F9: 00         NOP                     
63FA: 00         NOP                     
63FB: 00         NOP                     
63FC: 00         NOP                     
63FD: 00         NOP                     
63FE: 00         NOP                     
63FF: 00         NOP                     
6400: 07         RLCA                    
6401: 00         NOP                     
6402: 1E 01      LD      E,$01           
6404: 3F         CCF                     
6405: 00         NOP                     
6406: 7F         LD      A,A             
6407: 00         NOP                     
6408: 7F         LD      A,A             
6409: 20 FF      JR      NZ,$640A        
640B: 50         LD      D,B             
640C: FF         RST     0X38            
640D: 50         LD      D,B             
640E: FF         RST     0X38            
640F: 20 FF      JR      NZ,$6410        
6411: 00         NOP                     
6412: BF         CP      A               
6413: 40         LD      B,B             
6414: FF         RST     0X38            
6415: 30 77      JR      NC,$648E        
6417: 3E 7E      LD      A,$7E           
6419: 17         RLA                     
641A: 3F         CCF                     
641B: 02         LD      (BC),A          
641C: 1F         RRA                     
641D: 00         NOP                     
641E: 07         RLCA                    
641F: 00         NOP                     
6420: 07         RLCA                    
6421: 00         NOP                     
6422: 1E 01      LD      E,$01           
6424: 3F         CCF                     
6425: 00         NOP                     
6426: 7F         LD      A,A             
6427: 20 7F      JR      NZ,$64A8        
6429: 10 FF      STOP    $FF             
642B: 50         LD      D,B             
642C: FF         RST     0X38            
642D: 20 FE      JR      NZ,$642D        
642F: 07         RLCA                    
6430: F7         RST     0X30            
6431: 1E FF      LD      E,$FF           
6433: 32         LD      (HLD),A         
6434: BF         CP      A               
6435: 50         LD      D,B             
6436: 5F         LD      E,A             
6437: 20 5F      JR      NZ,$6498        
6439: 20 27      JR      NZ,$6462        
643B: 18 19      JR      $6456           
643D: 07         RLCA                    
643E: 07         RLCA                    
643F: 00         NOP                     
6440: 07         RLCA                    
6441: 00         NOP                     
6442: 1E 01      LD      E,$01           
6444: 3F         CCF                     
6445: 00         NOP                     
6446: 7F         LD      A,A             
6447: 00         NOP                     
6448: 7F         LD      A,A             
6449: 00         NOP                     
644A: FF         RST     0X38            
644B: 01 FF 01   LD      BC,$01FF        
644E: FF         RST     0X38            
644F: 40         LD      B,B             
6450: FF         RST     0X38            
6451: 60         LD      H,B             
6452: FF         RST     0X38            
6453: 58         LD      E,B             
6454: FF         RST     0X38            
6455: 13         INC     DE              
6456: 7F         LD      A,A             
6457: 02         LD      (BC),A          
6458: 7F         LD      A,A             
6459: 00         NOP                     
645A: 3F         CCF                     
645B: 00         NOP                     
645C: 1F         RRA                     
645D: 00         NOP                     
645E: 07         RLCA                    
645F: 00         NOP                     
6460: E0 00      LDFF00  ($00),A         
6462: 78         LD      A,B             
6463: 80         ADD     A,B             
6464: FC         ???                     
6465: 00         NOP                     
6466: FE 00      CP      $00             
6468: FE C0      CP      $C0             
646A: FF         RST     0X38            
646B: 20 FF      JR      NZ,$646C        
646D: 20 FF      JR      NZ,$646E        
646F: C0         RET     NZ              
6470: FF         RST     0X38            
6471: 00         NOP                     
6472: FF         RST     0X38            
6473: 00         NOP                     
6474: BF         CP      A               
6475: 40         LD      B,B             
6476: FE 00      CP      $00             
6478: FE 00      CP      $00             
647A: FC         ???                     
647B: 00         NOP                     
647C: F8 00      LDHL    SP,$00          
647E: E0 00      LDFF00  ($00),A         
6480: 07         RLCA                    
6481: 00         NOP                     
6482: 1E 01      LD      E,$01           
6484: 3F         CCF                     
6485: 00         NOP                     
6486: 7F         LD      A,A             
6487: 00         NOP                     
6488: FF         RST     0X38            
6489: 60         LD      H,B             
648A: FF         RST     0X38            
648B: 50         LD      D,B             
648C: FF         RST     0X38            
648D: 58         LD      E,B             
648E: 7F         LD      A,A             
648F: 1C         INC     E               
6490: 3F         CCF                     
6491: 02         LD      (BC),A          
6492: 5F         LD      E,A             
6493: 23         INC     HL              
6494: FF         RST     0X38            
6495: 40         LD      B,B             
6496: FC         ???                     
6497: 43         LD      B,E             
6498: 7B         LD      A,E             
6499: 3C         INC     A               
649A: 3F         CCF                     
649B: 00         NOP                     
649C: 1F         RRA                     
649D: 00         NOP                     
649E: 07         RLCA                    
649F: 00         NOP                     
64A0: E0 00      LDFF00  ($00),A         
64A2: 78         LD      A,B             
64A3: 80         ADD     A,B             
64A4: FC         ???                     
64A5: 00         NOP                     
64A6: FE 60      CP      $60             
64A8: FE 90      CP      $90             
64AA: FF         RST     0X38            
64AB: 90         SUB     B               
64AC: FF         RST     0X38            
64AD: 60         LD      H,B             
64AE: FF         RST     0X38            
64AF: 00         NOP                     
64B0: FF         RST     0X38            
64B1: 00         NOP                     
64B2: FF         RST     0X38            
64B3: 00         NOP                     
64B4: 3F         CCF                     
64B5: C0         RET     NZ              
64B6: FE 00      CP      $00             
64B8: FE 00      CP      $00             
64BA: FC         ???                     
64BB: 00         NOP                     
64BC: F8 00      LDHL    SP,$00          
64BE: E0 00      LDFF00  ($00),A         
64C0: 07         RLCA                    
64C1: 00         NOP                     
64C2: 1E 01      LD      E,$01           
64C4: 3F         CCF                     
64C5: 00         NOP                     
64C6: 7F         LD      A,A             
64C7: 00         NOP                     
64C8: 7F         LD      A,A             
64C9: 00         NOP                     
64CA: FF         RST     0X38            
64CB: 00         NOP                     
64CC: FF         RST     0X38            
64CD: 00         NOP                     
64CE: FF         RST     0X38            
64CF: 00         NOP                     
64D0: FF         RST     0X38            
64D1: 00         NOP                     
64D2: FF         RST     0X38            
64D3: 00         NOP                     
64D4: FF         RST     0X38            
64D5: 00         NOP                     
64D6: 7F         LD      A,A             
64D7: 00         NOP                     
64D8: 7F         LD      A,A             
64D9: 00         NOP                     
64DA: 3F         CCF                     
64DB: 00         NOP                     
64DC: 1F         RRA                     
64DD: 00         NOP                     
64DE: 07         RLCA                    
64DF: 00         NOP                     
64E0: 00         NOP                     
64E1: 00         NOP                     
64E2: 00         NOP                     
64E3: 00         NOP                     
64E4: 00         NOP                     
64E5: 00         NOP                     
64E6: 00         NOP                     
64E7: 00         NOP                     
64E8: 00         NOP                     
64E9: 00         NOP                     
64EA: 3C         INC     A               
64EB: 00         NOP                     
64EC: 5A         LD      E,D             
64ED: 3C         INC     A               
64EE: 7E         LD      A,(HL)          
64EF: 24         INC     H               
64F0: 7E         LD      A,(HL)          
64F1: 24         INC     H               
64F2: 5A         LD      E,D             
64F3: 3C         INC     A               
64F4: 3C         INC     A               
64F5: 00         NOP                     
64F6: 00         NOP                     
64F7: 00         NOP                     
64F8: 00         NOP                     
64F9: 00         NOP                     
64FA: 00         NOP                     
64FB: 00         NOP                     
64FC: 00         NOP                     
64FD: 00         NOP                     
64FE: 00         NOP                     
64FF: 00         NOP                     
6500: 00         NOP                     
6501: 00         NOP                     
6502: 00         NOP                     
6503: 00         NOP                     
6504: 36 00      LD      (HL),$00        
6506: 5E         LD      E,(HL)          
6507: 20 7E      JR      NZ,$6587        
6509: 00         NOP                     
650A: 7F         LD      A,A             
650B: 0E 7F      LD      C,$7F           
650D: 3F         CCF                     
650E: 7F         LD      A,A             
650F: 1B         DEC     DE              
6510: DF         RST     0X18            
6511: 6B         LD      L,E             
6512: 9F         SBC     A               
6513: 6F         LD      L,A             
6514: BF         CP      A               
6515: 47         LD      B,A             
6516: F8 07      LDHL    SP,$07          
6518: 20 1F      JR      NZ,$6539        
651A: 18 07      JR      $6523           
651C: 37         SCF                     
651D: 18 3F      JR      $655E           
651F: 00         NOP                     
6520: 00         NOP                     
6521: 00         NOP                     
6522: 00         NOP                     
6523: 00         NOP                     
6524: 00         NOP                     
6525: 00         NOP                     
6526: 38 00      JR      C,$6528         
6528: 7C         LD      A,H             
6529: 38 FC      JR      C,$6527         
652B: 60         LD      H,B             
652C: FE DC      CP      $DC             
652E: FE B8      CP      $B8             
6530: BE         CP      (HL)            
6531: F4         ???                     
6532: FE FC      CP      $FC             
6534: 3A         LD      A,(HLD)         
6535: FC         ???                     
6536: 04         INC     B               
6537: F8 48      LDHL    SP,$48          
6539: B0         OR      B               
653A: B0         OR      B               
653B: 40         LD      B,B             
653C: A0         AND     B               
653D: C0         RET     NZ              
653E: E0 00      LDFF00  ($00),A         
6540: 00         NOP                     
6541: 00         NOP                     
6542: 36 00      LD      (HL),$00        
6544: 5E         LD      E,(HL)          
6545: 20 7E      JR      NZ,$65C5        
6547: 00         NOP                     
6548: 7F         LD      A,A             
6549: 0E 7F      LD      C,$7F           
654B: 3F         CCF                     
654C: 7F         LD      A,A             
654D: 1B         DEC     DE              
654E: DF         RST     0X18            
654F: 6B         LD      L,E             
6550: 9F         SBC     A               
6551: 6F         LD      L,A             
6552: BE         CP      (HL)            
6553: 47         LD      B,A             
6554: FF         RST     0X38            
6555: 06 21      LD      B,$21           
6557: 1E 11      LD      E,$11           
6559: 0E 0F      LD      C,$0F           
655B: 00         NOP                     
655C: 07         RLCA                    
655D: 03         INC     BC              
655E: 07         RLCA                    
655F: 00         NOP                     
6560: 00         NOP                     
6561: 00         NOP                     
6562: 00         NOP                     
6563: 00         NOP                     
6564: 70         LD      (HL),B          
6565: 00         NOP                     
6566: 78         LD      A,B             
6567: 30 FC      JR      NC,$6565        
6569: 78         LD      A,B             
656A: F4         ???                     
656B: F8 FC      LDHL    SP,$FC          
656D: F8 D8      LDHL    SP,$D8          
656F: E0 FC      LDFF00  ($FC),A         
6571: F8 FE      LDHL    SP,$FE          
6573: FC         ???                     
6574: EE F4      XOR     $F4             
6576: 76         HALT                    
6577: F8 84      LDHL    SP,$84          
6579: 78         LD      A,B             
657A: 7C         LD      A,H             
657B: 80         ADD     A,B             
657C: F0 80      LD      A,($80)         
657E: E0 00      LDFF00  ($00),A         
6580: 00         NOP                     
6581: 00         NOP                     
6582: 30 00      JR      NC,$6584        
6584: 28 10      JR      Z,$6596         
6586: 29         ADD     HL,HL           
6587: 10 26      STOP    $26             
6589: 19         ADD     HL,DE           
658A: 20 1F      JR      NZ,$65AB        
658C: 2A         LD      A,(HLI)         
658D: 15         DEC     D               
658E: 4A         LD      C,D             
658F: 35         DEC     (HL)            
6590: C0         RET     NZ              
6591: 7F         LD      A,A             
6592: D8         RET     C               
6593: 67         LD      H,A             
6594: 41         LD      B,C             
6595: 3E 43      LD      A,$43           
6597: 3C         INC     A               
6598: 3E 01      LD      A,$01           
659A: 10 0F      STOP    $0F             
659C: 1B         DEC     DE              
659D: 0D         DEC     C               
659E: 1F         RRA                     
659F: 00         NOP                     
65A0: 00         NOP                     
65A1: 00         NOP                     
65A2: 60         LD      H,B             
65A3: 00         NOP                     
65A4: A0         AND     B               
65A5: 40         LD      B,B             
65A6: 66         LD      H,(HL)          
65A7: C0         RET     NZ              
65A8: EF         RST     0X28            
65A9: C0         RET     NZ              
65AA: CF         RST     0X08            
65AB: 80         ADD     A,B             
65AC: 2B         DEC     HL              
65AD: C4 31 EE   CALL    NZ,$EE31        
65B0: 71         LD      (HL),C          
65B1: CE 72      ADC     $72             
65B3: EC         ???                     
65B4: F2         ???                     
65B5: 0C         INC     C               
65B6: 14         INC     D               
65B7: E8 08      ADD     SP,$08          
65B9: F0 44      LD      A,($44)         
65BB: B8         CP      B               
65BC: FC         ???                     
65BD: 98         SBC     B               
65BE: FC         ???                     
65BF: 00         NOP                     
65C0: 00         NOP                     
65C1: 00         NOP                     
65C2: 60         LD      H,B             
65C3: 00         NOP                     
65C4: A0         AND     B               
65C5: 40         LD      B,B             
65C6: 78         LD      A,B             
65C7: C0         RET     NZ              
65C8: FC         ???                     
65C9: C0         RET     NZ              
65CA: FC         ???                     
65CB: 80         ADD     A,B             
65CC: 26 D8      LD      H,$D8           
65CE: 32         LD      (HLD),A         
65CF: EC         ???                     
65D0: 72         LD      (HL),D          
65D1: CC 72 EC   CALL    Z,$EC72         
65D4: F4         ???                     
65D5: 08 14 E8   LD      ($E814),SP      
65D8: 08 F0 44   LD      ($44F0),SP      
65DB: B8         CP      B               
65DC: FC         ???                     
65DD: 98         SBC     B               
65DE: FC         ???                     
65DF: 00         NOP                     
65E0: 00         NOP                     
65E1: 00         NOP                     
65E2: 00         NOP                     
65E3: 00         NOP                     
65E4: 00         NOP                     
65E5: 00         NOP                     
65E6: 00         NOP                     
65E7: 00         NOP                     
65E8: C3 00 E7   JP      $E700           
65EB: 42         LD      B,D             
65EC: FF         RST     0X38            
65ED: 66         LD      H,(HL)          
65EE: FF         RST     0X38            
65EF: 66         LD      H,(HL)          
65F0: 7E         LD      A,(HL)          
65F1: 24         INC     H               
65F2: 3C         INC     A               
65F3: 00         NOP                     
65F4: 00         NOP                     
65F5: 00         NOP                     
65F6: 00         NOP                     
65F7: 00         NOP                     
65F8: 00         NOP                     
65F9: 00         NOP                     
65FA: 00         NOP                     
65FB: 00         NOP                     
65FC: 00         NOP                     
65FD: 00         NOP                     
65FE: 00         NOP                     
65FF: 00         NOP                     
6600: 07         RLCA                    
6601: 00         NOP                     
6602: 18 07      JR      $660B           
6604: 26 19      LD      H,$19           
6606: 27         DAA                     
6607: 1A         LD      A,(DE)          
6608: 4F         LD      C,A             
6609: 33         INC     SP              
660A: 5F         LD      E,A             
660B: 2B         DEC     HL              
660C: 3F         CCF                     
660D: 0F         RRCA                    
660E: 1F         RRA                     
660F: 0D         DEC     C               
6610: 17         RLA                     
6611: 0D         DEC     C               
6612: 2B         DEC     HL              
6613: 17         RLA                     
6614: 2F         CPL                     
6615: 10 3F      STOP    $3F             
6617: 0D         DEC     C               
6618: 1F         RRA                     
6619: 0D         DEC     C               
661A: 1D         DEC     E               
661B: 02         LD      (BC),A          
661C: 17         RLA                     
661D: 0F         RRCA                    
661E: 1F         RRA                     
661F: 00         NOP                     
6620: C0         RET     NZ              
6621: 00         NOP                     
6622: 20 C0      JR      NZ,$65E4        
6624: 1C         INC     E               
6625: E0 82      LDFF00  ($82),A         
6627: 7C         LD      A,H             
6628: D2 2C FA   JP      NC,$FA2C        
662B: 54         LD      D,H             
662C: FC         ???                     
662D: D0         RET     NC              
662E: EA F4 B2   LD      ($B2F4),A       
6631: CC 61 9E   CALL    Z,$9E61         
6634: D1         POP     DE              
6635: 2E D1      LD      L,$D1           
6637: AE         XOR     (HL)            
6638: D2 AC 8C   JP      NC,$8CAC        
663B: 70         LD      (HL),B          
663C: 88         ADC     A,B             
663D: F0 F8      LD      A,($F8)         
663F: 00         NOP                     
6640: 07         RLCA                    
6641: 00         NOP                     
6642: 08 07 31   LD      ($3107),SP      
6645: 0E 43      LD      C,$43           
6647: 3D         DEC     A               
6648: 57         LD      D,A             
6649: 29         ADD     HL,HL           
664A: 7F         LD      A,A             
664B: 15         DEC     D               
664C: 3F         CCF                     
664D: 17         RLA                     
664E: 5F         LD      E,A             
664F: 2F         CPL                     
6650: 8B         ADC     A,E             
6651: 77         LD      (HL),A          
6652: 85         ADD     A,L             
6653: 7B         LD      A,E             
6654: 87         ADD     A,A             
6655: 78         LD      A,B             
6656: 4F         LD      C,A             
6657: 36 3F      LD      (HL),$3F        
6659: 06 16      LD      B,$16           
665B: 09         ADD     HL,BC           
665C: 13         INC     DE              
665D: 0F         RRCA                    
665E: 1F         RRA                     
665F: 00         NOP                     
6660: 03         INC     BC              
6661: 00         NOP                     
6662: 04         INC     B               
6663: 03         INC     BC              
6664: 39         ADD     HL,SP           
6665: 07         RLCA                    
6666: 40         LD      B,B             
6667: 3F         CCF                     
6668: 40         LD      B,B             
6669: 3F         CCF                     
666A: 20 1F      JR      NZ,$668B        
666C: 30 0F      JR      NC,$667D        
666E: 20 1F      JR      NZ,$668F        
6670: 10 0F      STOP    $0F             
6672: 20 1F      JR      NZ,$6693        
6674: 20 1F      JR      NZ,$6695        
6676: 30 0F      JR      NC,$6687        
6678: 1C         INC     E               
6679: 03         INC     BC              
667A: 23         INC     HL              
667B: 1C         INC     E               
667C: 20 1F      JR      NZ,$669D        
667E: 3F         CCF                     
667F: 00         NOP                     
6680: 07         RLCA                    
6681: 00         NOP                     
6682: 38 07      JR      C,$668B         
6684: 50         LD      D,B             
6685: 2F         CPL                     
6686: 41         LD      B,C             
6687: 3E 51      LD      A,$51           
6689: 2E 3F      LD      L,$3F           
668B: 10 3F      STOP    $3F             
668D: 15         DEC     D               
668E: 5F         LD      E,A             
668F: 2D         DEC     L               
6690: 9F         SBC     A               
6691: 67         LD      H,A             
6692: 9F         SBC     A               
6693: 63         LD      H,E             
6694: B7         OR      A               
6695: 48         LD      C,B             
6696: 7C         LD      A,H             
6697: 17         RLA                     
6698: 3B         DEC     SP              
6699: 17         RLA                     
669A: 30 0F      JR      NC,$66AB        
669C: 1F         RRA                     
669D: 0F         RRCA                    
669E: 1F         RRA                     
669F: 00         NOP                     
66A0: E0 00      LDFF00  ($00),A         
66A2: 1C         INC     E               
66A3: E0 8A      LDFF00  ($8A),A         
66A5: 74         LD      (HL),H          
66A6: C2 BC CA   JP      NZ,$CABC        
66A9: B4         OR      H               
66AA: FC         ???                     
66AB: 88         ADC     A,B             
66AC: FE A8      CP      $A8             
66AE: F9         LD      SP,HL           
66AF: B6         OR      (HL)            
66B0: F9         LD      SP,HL           
66B1: E6 F9      AND     $F9             
66B3: C6 EE      ADD     $EE             
66B5: 10 7C      STOP    $7C             
66B7: D8         RET     C               
66B8: BC         CP      H               
66B9: D8         RET     C               
66BA: 1C         INC     E               
66BB: E0 08      LDFF00  ($08),A         
66BD: F0 F8      LD      A,($F8)         
66BF: 00         NOP                     
66C0: 0F         RRCA                    
66C1: 00         NOP                     
66C2: 36 0F      LD      (HL),$0F        
66C4: 60         LD      H,B             
66C5: 3F         CCF                     
66C6: 58         LD      E,B             
66C7: 27         DAA                     
66C8: 7C         LD      A,H             
66C9: 0B         DEC     BC              
66CA: 1F         RRA                     
66CB: 08 1F 0A   LD      ($0A1F),SP      
66CE: 3F         CCF                     
66CF: 1A         LD      A,(DE)          
66D0: 3F         CCF                     
66D1: 1F         RRA                     
66D2: 1E 0F      LD      E,$0F           
66D4: 0F         RRCA                    
66D5: 00         NOP                     
66D6: 07         RLCA                    
66D7: 03         INC     BC              
66D8: 07         RLCA                    
66D9: 03         INC     BC              
66DA: 07         RLCA                    
66DB: 00         NOP                     
66DC: 08 07 0F   LD      ($0F07),SP      
66DF: 00         NOP                     
66E0: 80         ADD     A,B             
66E1: 00         NOP                     
66E2: 60         LD      H,B             
66E3: 80         ADD     A,B             
66E4: 10 E0      STOP    $E0             
66E6: 1C         INC     E               
66E7: E0 04      LDFF00  ($04),A         
66E9: F8 74      LDHL    SP,$74          
66EB: 88         ADC     A,B             
66EC: 78         LD      A,B             
66ED: A0         AND     B               
66EE: D8         RET     C               
66EF: 60         LD      H,B             
66F0: A4         AND     H               
66F1: D8         RET     C               
66F2: 44         LD      B,H             
66F3: B8         CP      B               
66F4: C2 3C E2   JP      NZ,$E23C        
66F7: 1C         INC     E               
66F8: BC         CP      H               
66F9: 40         LD      B,B             
66FA: 10 E0      STOP    $E0             
66FC: 08 F0 F8   LD      ($F8F0),SP      
66FF: 00         NOP                     
6700: 00         NOP                     
6701: 00         NOP                     
6702: 00         NOP                     
6703: 00         NOP                     
6704: 07         RLCA                    
6705: 00         NOP                     
6706: 0F         RRCA                    
6707: 00         NOP                     
6708: 3F         CCF                     
6709: 00         NOP                     
670A: 7F         LD      A,A             
670B: 30 7F      JR      NC,$678C        
670D: 37         SCF                     
670E: 7F         LD      A,A             
670F: 3E 3F      LD      A,$3F           
6711: 0E 0B      LD      C,$0B           
6713: 07         RLCA                    
6714: 1F         RRA                     
6715: 00         NOP                     
6716: 3F         CCF                     
6717: 18 3C      JR      $6755           
6719: 1B         DEC     DE              
671A: 1F         RRA                     
671B: 00         NOP                     
671C: 0F         RRCA                    
671D: 07         RLCA                    
671E: 0F         RRCA                    
671F: 00         NOP                     
6720: 00         NOP                     
6721: 00         NOP                     
6722: 00         NOP                     
6723: 00         NOP                     
6724: E0 00      LDFF00  ($00),A         
6726: F0 00      LD      A,($00)         
6728: F8 C0      LDHL    SP,$C0          
672A: FC         ???                     
672B: C8         RET     Z               
672C: FC         ???                     
672D: E8 FC      ADD     SP,$FC          
672F: D8         RET     C               
6730: F8 D0      LDHL    SP,$D0          
6732: F8 E0      LDHL    SP,$E0          
6734: FC         ???                     
6735: 18 FC      JR      $6733           
6737: 18 38      JR      $6771           
6739: C0         RET     NZ              
673A: 10 E0      STOP    $E0             
673C: F8 00      LDHL    SP,$00          
673E: F0 00      LD      A,($00)         
6740: 00         NOP                     
6741: 00         NOP                     
6742: 00         NOP                     
6743: 00         NOP                     
6744: 07         RLCA                    
6745: 00         NOP                     
6746: 0F         RRCA                    
6747: 00         NOP                     
6748: 3F         CCF                     
6749: 00         NOP                     
674A: 7F         LD      A,A             
674B: 30 7F      JR      NC,$67CC        
674D: 30 7F      JR      NC,$67CE        
674F: 30 3F      JR      NC,$6790        
6751: 0C         INC     C               
6752: 1F         RRA                     
6753: 07         RLCA                    
6754: 37         SCF                     
6755: 18 3F      JR      $6796           
6757: 10 18      STOP    $18             
6759: 07         RLCA                    
675A: 08 07 1F   LD      ($1F07),SP      
675D: 00         NOP                     
675E: 0F         RRCA                    
675F: 00         NOP                     
6760: 00         NOP                     
6761: 00         NOP                     
6762: 00         NOP                     
6763: 00         NOP                     
6764: E0 00      LDFF00  ($00),A         
6766: F0 00      LD      A,($00)         
6768: FC         ???                     
6769: 00         NOP                     
676A: FE 0C      CP      $0C             
676C: FE 0C      CP      $0C             
676E: FE 0C      CP      $0C             
6770: FC         ???                     
6771: 30 F0      JR      NC,$6763        
6773: E0 F8      LDFF00  ($F8),A         
6775: 00         NOP                     
6776: FC         ???                     
6777: 08 3C C8   LD      ($C83C),SP      
677A: F8 00      LDHL    SP,$00          
677C: F8 E0      LDHL    SP,$E0          
677E: F0 00      LD      A,($00)         
6780: 00         NOP                     
6781: 00         NOP                     
6782: 00         NOP                     
6783: 00         NOP                     
6784: 0F         RRCA                    
6785: 00         NOP                     
6786: 1F         RRA                     
6787: 00         NOP                     
6788: 1F         RRA                     
6789: 04         INC     B               
678A: 1F         RRA                     
678B: 04         INC     B               
678C: 0F         RRCA                    
678D: 07         RLCA                    
678E: 1F         RRA                     
678F: 05         DEC     B               
6790: 1F         RRA                     
6791: 0D         DEC     C               
6792: 3F         CCF                     
6793: 07         RLCA                    
6794: 3F         CCF                     
6795: 18 3F      JR      $67D6           
6797: 16 1F      LD      D,$1F           
6799: 06 07      LD      B,$07           
679B: 00         NOP                     
679C: 03         INC     BC              
679D: 01 07 00   LD      BC,$0007        
67A0: 00         NOP                     
67A1: 00         NOP                     
67A2: 00         NOP                     
67A3: 00         NOP                     
67A4: C0         RET     NZ              
67A5: 00         NOP                     
67A6: E0 00      LDFF00  ($00),A         
67A8: F0 00      LD      A,($00)         
67AA: F8 30      LDHL    SP,$30          
67AC: F8 30      LDHL    SP,$30          
67AE: F8 F0      LDHL    SP,$F0          
67B0: D0         RET     NC              
67B1: E0 A0      LDFF00  ($A0),A         
67B3: C0         RET     NZ              
67B4: E0 00      LDFF00  ($00),A         
67B6: F0 00      LD      A,($00)         
67B8: 10 E0      STOP    $E0             
67BA: F0 00      LD      A,($00)         
67BC: E0 C0      LDFF00  ($C0),A         
67BE: F0 00      LD      A,($00)         
67C0: 00         NOP                     
67C1: 00         NOP                     
67C2: 00         NOP                     
67C3: 00         NOP                     
67C4: 00         NOP                     
67C5: 00         NOP                     
67C6: 1F         RRA                     
67C7: 00         NOP                     
67C8: 3F         CCF                     
67C9: 00         NOP                     
67CA: 3F         CCF                     
67CB: 08 3F 08   LD      ($083F),SP      
67CE: 1F         RRA                     
67CF: 0E 3F      LD      C,$3F           
67D1: 0B         DEC     BC              
67D2: 3F         CCF                     
67D3: 1B         DEC     DE              
67D4: 7F         LD      A,A             
67D5: 00         NOP                     
67D6: 7F         LD      A,A             
67D7: 38 3E      JR      C,$6817         
67D9: 19         ADD     HL,DE           
67DA: 3C         INC     A               
67DB: 03         INC     BC              
67DC: 47         LD      B,A             
67DD: 38 7F      JR      C,$685E         
67DF: 00         NOP                     
67E0: 00         NOP                     
67E1: 00         NOP                     
67E2: 00         NOP                     
67E3: 00         NOP                     
67E4: 00         NOP                     
67E5: 00         NOP                     
67E6: 80         ADD     A,B             
67E7: 00         NOP                     
67E8: C0         RET     NZ              
67E9: 00         NOP                     
67EA: E0 00      LDFF00  ($00),A         
67EC: F0 60      LD      A,($60)         
67EE: F0 60      LD      A,($60)         
67F0: F0 E0      LD      A,($E0)         
67F2: E0 80      LDFF00  ($80),A         
67F4: C0         RET     NZ              
67F5: 00         NOP                     
67F6: F0 00      LD      A,($00)         
67F8: 38 D0      JR      C,$67CA         
67FA: 78         LD      A,B             
67FB: B0         OR      B               
67FC: F0 60      LD      A,($60)         
67FE: F8 00      LDHL    SP,$00          
6800: 00         NOP                     
6801: 00         NOP                     
6802: 03         INC     BC              
6803: 00         NOP                     
6804: 0F         RRCA                    
6805: 00         NOP                     
6806: 1F         RRA                     
6807: 00         NOP                     
6808: 3F         CCF                     
6809: 00         NOP                     
680A: 7F         LD      A,A             
680B: 00         NOP                     
680C: 7F         LD      A,A             
680D: 00         NOP                     
680E: FF         RST     0X38            
680F: 00         NOP                     
6810: FF         RST     0X38            
6811: 00         NOP                     
6812: FF         RST     0X38            
6813: 00         NOP                     
6814: FF         RST     0X38            
6815: 00         NOP                     
6816: FF         RST     0X38            
6817: 00         NOP                     
6818: 7F         LD      A,A             
6819: 00         NOP                     
681A: 7F         LD      A,A             
681B: 00         NOP                     
681C: 3F         CCF                     
681D: 00         NOP                     
681E: 0F         RRCA                    
681F: 00         NOP                     
6820: 7E         LD      A,(HL)          
6821: 00         NOP                     
6822: FF         RST     0X38            
6823: 00         NOP                     
6824: FF         RST     0X38            
6825: 00         NOP                     
6826: FF         RST     0X38            
6827: 00         NOP                     
6828: FF         RST     0X38            
6829: 00         NOP                     
682A: FF         RST     0X38            
682B: 00         NOP                     
682C: FF         RST     0X38            
682D: 00         NOP                     
682E: FF         RST     0X38            
682F: 00         NOP                     
6830: FF         RST     0X38            
6831: 00         NOP                     
6832: FF         RST     0X38            
6833: 00         NOP                     
6834: FF         RST     0X38            
6835: 00         NOP                     
6836: FF         RST     0X38            
6837: 00         NOP                     
6838: FF         RST     0X38            
6839: 00         NOP                     
683A: FF         RST     0X38            
683B: 00         NOP                     
683C: FF         RST     0X38            
683D: 00         NOP                     
683E: FF         RST     0X38            
683F: 00         NOP                     
6840: 07         RLCA                    
6841: 00         NOP                     
6842: 0F         RRCA                    
6843: 00         NOP                     
6844: 1F         RRA                     
6845: 00         NOP                     
6846: 1F         RRA                     
6847: 00         NOP                     
6848: 3F         CCF                     
6849: 00         NOP                     
684A: 3F         CCF                     
684B: 00         NOP                     
684C: 3F         CCF                     
684D: 00         NOP                     
684E: 3F         CCF                     
684F: 00         NOP                     
6850: 3F         CCF                     
6851: 00         NOP                     
6852: 3F         CCF                     
6853: 00         NOP                     
6854: 3F         CCF                     
6855: 00         NOP                     
6856: 3F         CCF                     
6857: 00         NOP                     
6858: 3F         CCF                     
6859: 00         NOP                     
685A: 3F         CCF                     
685B: 00         NOP                     
685C: 3F         CCF                     
685D: 00         NOP                     
685E: 3F         CCF                     
685F: 00         NOP                     
6860: FF         RST     0X38            
6861: 00         NOP                     
6862: DB         ???                     
6863: 67         LD      H,A             
6864: F8 07      LDHL    SP,$07          
6866: DF         RST     0X18            
6867: 60         LD      H,B             
6868: DF         RST     0X18            
6869: 60         LD      H,B             
686A: DB         ???                     
686B: 67         LD      H,A             
686C: 98         SBC     B               
686D: 67         LD      H,A             
686E: FF         RST     0X38            
686F: 00         NOP                     
6870: FF         RST     0X38            
6871: 00         NOP                     
6872: DB         ???                     
6873: 67         LD      H,A             
6874: F8 07      LDHL    SP,$07          
6876: DF         RST     0X18            
6877: 60         LD      H,B             
6878: DF         RST     0X18            
6879: 60         LD      H,B             
687A: DB         ???                     
687B: 67         LD      H,A             
687C: 98         SBC     B               
687D: 67         LD      H,A             
687E: FF         RST     0X38            
687F: 00         NOP                     
6880: 07         RLCA                    
6881: 00         NOP                     
6882: 1F         RRA                     
6883: 00         NOP                     
6884: 3F         CCF                     
6885: 00         NOP                     
6886: 7F         LD      A,A             
6887: 00         NOP                     
6888: 4F         LD      C,A             
6889: 30 F7      JR      NC,$6882        
688B: 38 FB      JR      C,$6888         
688D: 3C         INC     A               
688E: FF         RST     0X38            
688F: 3C         INC     A               
6890: DD         ???                     
6891: 3E FF      LD      A,$FF           
6893: 1E EF      LD      E,$EF           
6895: 1E 77      LD      E,$77           
6897: 0E 7D      LD      C,$7D           
6899: 02         LD      (BC),A          
689A: 3F         CCF                     
689B: 00         NOP                     
689C: 1F         RRA                     
689D: 00         NOP                     
689E: 07         RLCA                    
689F: 00         NOP                     
68A0: 00         NOP                     
68A1: 00         NOP                     
68A2: 00         NOP                     
68A3: 00         NOP                     
68A4: 00         NOP                     
68A5: 00         NOP                     
68A6: 00         NOP                     
68A7: 00         NOP                     
68A8: 03         INC     BC              
68A9: 00         NOP                     
68AA: 07         RLCA                    
68AB: 00         NOP                     
68AC: 0F         RRCA                    
68AD: 00         NOP                     
68AE: 0F         RRCA                    
68AF: 00         NOP                     
68B0: 0F         RRCA                    
68B1: 00         NOP                     
68B2: 0F         RRCA                    
68B3: 00         NOP                     
68B4: 07         RLCA                    
68B5: 00         NOP                     
68B6: 03         INC     BC              
68B7: 00         NOP                     
68B8: 00         NOP                     
68B9: 00         NOP                     
68BA: 00         NOP                     
68BB: 00         NOP                     
68BC: 00         NOP                     
68BD: 00         NOP                     
68BE: 00         NOP                     
68BF: 00         NOP                     
68C0: 00         NOP                     
68C1: 00         NOP                     
68C2: 00         NOP                     
68C3: 00         NOP                     
68C4: 03         INC     BC              
68C5: 00         NOP                     
68C6: 0F         RRCA                    
68C7: 00         NOP                     
68C8: 1F         RRA                     
68C9: 00         NOP                     
68CA: 1F         RRA                     
68CB: 00         NOP                     
68CC: 3F         CCF                     
68CD: 00         NOP                     
68CE: 3F         CCF                     
68CF: 00         NOP                     
68D0: 3F         CCF                     
68D1: 00         NOP                     
68D2: 3F         CCF                     
68D3: 00         NOP                     
68D4: 1F         RRA                     
68D5: 00         NOP                     
68D6: 1F         RRA                     
68D7: 00         NOP                     
68D8: 0F         RRCA                    
68D9: 00         NOP                     
68DA: 03         INC     BC              
68DB: 00         NOP                     
68DC: 00         NOP                     
68DD: 00         NOP                     
68DE: 00         NOP                     
68DF: 00         NOP                     
68E0: 07         RLCA                    
68E1: 00         NOP                     
68E2: 1F         RRA                     
68E3: 00         NOP                     
68E4: 3F         CCF                     
68E5: 00         NOP                     
68E6: 7F         LD      A,A             
68E7: 00         NOP                     
68E8: 7F         LD      A,A             
68E9: 00         NOP                     
68EA: FF         RST     0X38            
68EB: 00         NOP                     
68EC: FF         RST     0X38            
68ED: 00         NOP                     
68EE: FF         RST     0X38            
68EF: 00         NOP                     
68F0: FF         RST     0X38            
68F1: 00         NOP                     
68F2: FF         RST     0X38            
68F3: 00         NOP                     
68F4: FF         RST     0X38            
68F5: 00         NOP                     
68F6: 7F         LD      A,A             
68F7: 00         NOP                     
68F8: 7F         LD      A,A             
68F9: 00         NOP                     
68FA: 3F         CCF                     
68FB: 00         NOP                     
68FC: 1F         RRA                     
68FD: 00         NOP                     
68FE: 07         RLCA                    
68FF: 00         NOP                     
6900: 00         NOP                     
6901: 00         NOP                     
6902: 1C         INC     E               
6903: 00         NOP                     
6904: 3E 00      LD      A,$00           
6906: 7F         LD      A,A             
6907: 00         NOP                     
6908: FF         RST     0X38            
6909: 00         NOP                     
690A: CF         RST     0X08            
690B: 00         NOP                     
690C: 0F         RRCA                    
690D: 00         NOP                     
690E: 0F         RRCA                    
690F: 00         NOP                     
6910: 7F         LD      A,A             
6911: 00         NOP                     
6912: FF         RST     0X38            
6913: 00         NOP                     
6914: FF         RST     0X38            
6915: 00         NOP                     
6916: FF         RST     0X38            
6917: 00         NOP                     
6918: FF         RST     0X38            
6919: 00         NOP                     
691A: FF         RST     0X38            
691B: 00         NOP                     
691C: FF         RST     0X38            
691D: 00         NOP                     
691E: 7F         LD      A,A             
691F: 00         NOP                     
6920: 00         NOP                     
6921: 00         NOP                     
6922: 3E 00      LD      A,$00           
6924: FF         RST     0X38            
6925: 00         NOP                     
6926: FF         RST     0X38            
6927: 00         NOP                     
6928: FF         RST     0X38            
6929: 00         NOP                     
692A: FF         RST     0X38            
692B: 00         NOP                     
692C: FF         RST     0X38            
692D: 00         NOP                     
692E: FF         RST     0X38            
692F: 00         NOP                     
6930: FF         RST     0X38            
6931: E0 FF      LDFF00  ($FF),A         
6933: F1         POP     AF              
6934: FF         RST     0X38            
6935: 79         LD      A,C             
6936: FF         RST     0X38            
6937: 19         ADD     HL,DE           
6938: FF         RST     0X38            
6939: 00         NOP                     
693A: FF         RST     0X38            
693B: 00         NOP                     
693C: FF         RST     0X38            
693D: 00         NOP                     
693E: FF         RST     0X38            
693F: 00         NOP                     
6940: 00         NOP                     
6941: 00         NOP                     
6942: 00         NOP                     
6943: 00         NOP                     
6944: 18 00      JR      $6946           
6946: 2A         LD      A,(HLI)         
6947: 10 5D      STOP    $5D             
6949: 32         LD      (HLD),A         
694A: 77         LD      (HL),A          
694B: 3A         LD      A,(HLD)         
694C: BF         CP      A               
694D: 7B         LD      A,E             
694E: BF         CP      A               
694F: 7E         LD      A,(HL)          
6950: B7         OR      A               
6951: 7E         LD      A,(HL)          
6952: A7         AND     A               
6953: 7F         LD      A,A             
6954: 9B         SBC     E               
6955: 67         LD      H,A             
6956: A6         AND     (HL)            
6957: 41         LD      B,C             
6958: A1         AND     C               
6959: 40         LD      B,B             
695A: C0         RET     NZ              
695B: 00         NOP                     
695C: 00         NOP                     
695D: 00         NOP                     
695E: 00         NOP                     
695F: 00         NOP                     
6960: 00         NOP                     
6961: 00         NOP                     
6962: 00         NOP                     
6963: 00         NOP                     
6964: 02         LD      (BC),A          
6965: 00         NOP                     
6966: 05         DEC     B               
6967: 02         LD      (BC),A          
6968: 07         RLCA                    
6969: 02         LD      (BC),A          
696A: 0B         DEC     BC              
696B: 07         RLCA                    
696C: 0B         DEC     BC              
696D: 06 0F      LD      B,$0F           
696F: 06 17      LD      B,$17           
6971: 0F         RRCA                    
6972: 15         DEC     D               
6973: 0F         RRCA                    
6974: 14         INC     D               
6975: 0F         RRCA                    
6976: 13         INC     DE              
6977: 0C         INC     C               
6978: 14         INC     D               
6979: 08 14 08   LD      ($0814),SP      
697C: 14         INC     D               
697D: 08 18 00   LD      ($0018),SP      
6980: 03         INC     BC              
6981: 00         NOP                     
6982: 04         INC     B               
6983: 03         INC     BC              
6984: 05         DEC     B               
6985: 03         INC     BC              
6986: 05         DEC     B               
6987: 03         INC     BC              
6988: 02         LD      (BC),A          
6989: 01 72 01   LD      BC,$0172        
698C: 8C         ADC     A,H             
698D: 73         LD      (HL),E          
698E: B1         OR      C               
698F: 7F         LD      A,A             
6990: B1         OR      C               
6991: 7F         LD      A,A             
6992: 8C         ADC     A,H             
6993: 73         LD      (HL),E          
6994: 72         LD      (HL),D          
6995: 01 02 01   LD      BC,$0102        
6998: 05         DEC     B               
6999: 03         INC     BC              
699A: 05         DEC     B               
699B: 03         INC     BC              
699C: 04         INC     B               
699D: 03         INC     BC              
699E: 03         INC     BC              
699F: 00         NOP                     
69A0: 00         NOP                     
69A1: 00         NOP                     
69A2: 38 00      JR      C,$69A4         
69A4: 44         LD      B,H             
69A5: 38 5A      JR      C,$6A01         
69A7: 3C         INC     A               
69A8: 5A         LD      E,D             
69A9: 3C         INC     A               
69AA: 21 1E 18   LD      HL,$181E        
69AD: 07         RLCA                    
69AE: 05         DEC     B               
69AF: 03         INC     BC              
69B0: 05         DEC     B               
69B1: 03         INC     BC              
69B2: 18 07      JR      $69BB           
69B4: 21 1E 5A   LD      HL,$5A1E        
69B7: 3C         INC     A               
69B8: 5A         LD      E,D             
69B9: 3C         INC     A               
69BA: 44         LD      B,H             
69BB: 38 38      JR      C,$69F5         
69BD: 00         NOP                     
69BE: 00         NOP                     
69BF: 00         NOP                     
69C0: 00         NOP                     
69C1: 00         NOP                     
69C2: 00         NOP                     
69C3: 00         NOP                     
69C4: 00         NOP                     
69C5: 00         NOP                     
69C6: 00         NOP                     
69C7: 00         NOP                     
69C8: 00         NOP                     
69C9: 00         NOP                     
69CA: 00         NOP                     
69CB: 00         NOP                     
69CC: 00         NOP                     
69CD: 00         NOP                     
69CE: 00         NOP                     
69CF: 00         NOP                     
69D0: 00         NOP                     
69D1: 00         NOP                     
69D2: 00         NOP                     
69D3: 00         NOP                     
69D4: 07         RLCA                    
69D5: 00         NOP                     
69D6: 1F         RRA                     
69D7: 00         NOP                     
69D8: 3F         CCF                     
69D9: 00         NOP                     
69DA: 7F         LD      A,A             
69DB: 00         NOP                     
69DC: 7F         LD      A,A             
69DD: 00         NOP                     
69DE: FF         RST     0X38            
69DF: 00         NOP                     
69E0: FF         RST     0X38            
69E1: 00         NOP                     
69E2: FF         RST     0X38            
69E3: 00         NOP                     
69E4: FF         RST     0X38            
69E5: 00         NOP                     
69E6: FF         RST     0X38            
69E7: 00         NOP                     
69E8: FF         RST     0X38            
69E9: 00         NOP                     
69EA: FF         RST     0X38            
69EB: 00         NOP                     
69EC: FF         RST     0X38            
69ED: 00         NOP                     
69EE: FF         RST     0X38            
69EF: 00         NOP                     
69F0: FF         RST     0X38            
69F1: 00         NOP                     
69F2: FF         RST     0X38            
69F3: 00         NOP                     
69F4: FF         RST     0X38            
69F5: 00         NOP                     
69F6: FF         RST     0X38            
69F7: 00         NOP                     
69F8: FF         RST     0X38            
69F9: 00         NOP                     
69FA: 7F         LD      A,A             
69FB: 00         NOP                     
69FC: 7F         LD      A,A             
69FD: 00         NOP                     
69FE: 1F         RRA                     
69FF: 00         NOP                     
6A00: 00         NOP                     
6A01: 00         NOP                     
6A02: 00         NOP                     
6A03: 00         NOP                     
6A04: 03         INC     BC              
6A05: 00         NOP                     
6A06: 0F         RRCA                    
6A07: 00         NOP                     
6A08: 1F         RRA                     
6A09: 00         NOP                     
6A0A: 1F         RRA                     
6A0B: 00         NOP                     
6A0C: 3F         CCF                     
6A0D: 00         NOP                     
6A0E: 3F         CCF                     
6A0F: 00         NOP                     
6A10: 3F         CCF                     
6A11: 00         NOP                     
6A12: 3F         CCF                     
6A13: 00         NOP                     
6A14: 3F         CCF                     
6A15: 00         NOP                     
6A16: 3F         CCF                     
6A17: 00         NOP                     
6A18: 1F         RRA                     
6A19: 00         NOP                     
6A1A: 1F         RRA                     
6A1B: 00         NOP                     
6A1C: 0F         RRCA                    
6A1D: 00         NOP                     
6A1E: 0F         RRCA                    
6A1F: 00         NOP                     
6A20: 00         NOP                     
6A21: 00         NOP                     
6A22: 00         NOP                     
6A23: 00         NOP                     
6A24: F0 00      LD      A,($00)         
6A26: FC         ???                     
6A27: 00         NOP                     
6A28: FF         RST     0X38            
6A29: 00         NOP                     
6A2A: FF         RST     0X38            
6A2B: 00         NOP                     
6A2C: FF         RST     0X38            
6A2D: 00         NOP                     
6A2E: FF         RST     0X38            
6A2F: 00         NOP                     
6A30: FF         RST     0X38            
6A31: 00         NOP                     
6A32: FF         RST     0X38            
6A33: 00         NOP                     
6A34: FF         RST     0X38            
6A35: 00         NOP                     
6A36: FF         RST     0X38            
6A37: 00         NOP                     
6A38: CF         RST     0X08            
6A39: 30 F7      JR      NC,$6A32        
6A3B: 38 FB      JR      C,$6A38         
6A3D: 3C         INC     A               
6A3E: FF         RST     0X38            
6A3F: 3C         INC     A               
6A40: DD         ???                     
6A41: 3E FF      LD      A,$FF           
6A43: 1E EF      LD      E,$EF           
6A45: 1E F7      LD      E,$F7           
6A47: 0E FD      LD      C,$FD           
6A49: 02         LD      (BC),A          
6A4A: FF         RST     0X38            
6A4B: 00         NOP                     
6A4C: FF         RST     0X38            
6A4D: 00         NOP                     
6A4E: FF         RST     0X38            
6A4F: 00         NOP                     
6A50: FF         RST     0X38            
6A51: 00         NOP                     
6A52: FF         RST     0X38            
6A53: 00         NOP                     
6A54: FF         RST     0X38            
6A55: 00         NOP                     
6A56: FF         RST     0X38            
6A57: 00         NOP                     
6A58: FC         ???                     
6A59: 00         NOP                     
6A5A: F0 00      LD      A,($00)         
6A5C: 00         NOP                     
6A5D: 00         NOP                     
6A5E: 00         NOP                     
6A5F: 00         NOP                     
6A60: 00         NOP                     
6A61: 00         NOP                     
6A62: 00         NOP                     
6A63: 00         NOP                     
6A64: 00         NOP                     
6A65: 00         NOP                     
6A66: 03         INC     BC              
6A67: 00         NOP                     
6A68: 07         RLCA                    
6A69: 00         NOP                     
6A6A: 0F         RRCA                    
6A6B: 00         NOP                     
6A6C: 1F         RRA                     
6A6D: 00         NOP                     
6A6E: 1F         RRA                     
6A6F: 00         NOP                     
6A70: 3F         CCF                     
6A71: 00         NOP                     
6A72: 3F         CCF                     
6A73: 00         NOP                     
6A74: 3F         CCF                     
6A75: 00         NOP                     
6A76: 7F         LD      A,A             
6A77: 00         NOP                     
6A78: 7F         LD      A,A             
6A79: 00         NOP                     
6A7A: 7F         LD      A,A             
6A7B: 00         NOP                     
6A7C: 7F         LD      A,A             
6A7D: 00         NOP                     
6A7E: 7F         LD      A,A             
6A7F: 00         NOP                     
6A80: 00         NOP                     
6A81: 00         NOP                     
6A82: 1F         RRA                     
6A83: 00         NOP                     
6A84: FF         RST     0X38            
6A85: 00         NOP                     
6A86: FF         RST     0X38            
6A87: 00         NOP                     
6A88: FF         RST     0X38            
6A89: 00         NOP                     
6A8A: FF         RST     0X38            
6A8B: 00         NOP                     
6A8C: FF         RST     0X38            
6A8D: 00         NOP                     
6A8E: FF         RST     0X38            
6A8F: 00         NOP                     
6A90: FF         RST     0X38            
6A91: 00         NOP                     
6A92: FF         RST     0X38            
6A93: 00         NOP                     
6A94: FF         RST     0X38            
6A95: 00         NOP                     
6A96: FF         RST     0X38            
6A97: 00         NOP                     
6A98: CF         RST     0X08            
6A99: 30 F7      JR      NC,$6A92        
6A9B: 38 FB      JR      C,$6A98         
6A9D: 3C         INC     A               
6A9E: FF         RST     0X38            
6A9F: 3C         INC     A               
6AA0: DD         ???                     
6AA1: 3E FF      LD      A,$FF           
6AA3: 1E EF      LD      E,$EF           
6AA5: 1E F7      LD      E,$F7           
6AA7: 0E FD      LD      C,$FD           
6AA9: 02         LD      (BC),A          
6AAA: FF         RST     0X38            
6AAB: 00         NOP                     
6AAC: FF         RST     0X38            
6AAD: 00         NOP                     
6AAE: FF         RST     0X38            
6AAF: 00         NOP                     
6AB0: FF         RST     0X38            
6AB1: 00         NOP                     
6AB2: FF         RST     0X38            
6AB3: 00         NOP                     
6AB4: FF         RST     0X38            
6AB5: 00         NOP                     
6AB6: FF         RST     0X38            
6AB7: 00         NOP                     
6AB8: FF         RST     0X38            
6AB9: 00         NOP                     
6ABA: FF         RST     0X38            
6ABB: 00         NOP                     
6ABC: 1F         RRA                     
6ABD: 00         NOP                     
6ABE: 00         NOP                     
6ABF: 00         NOP                     
6AC0: 00         NOP                     
6AC1: 00         NOP                     
6AC2: 00         NOP                     
6AC3: 00         NOP                     
6AC4: 00         NOP                     
6AC5: 00         NOP                     
6AC6: 01 00 01   LD      BC,$0100        
6AC9: 00         NOP                     
6ACA: 03         INC     BC              
6ACB: 00         NOP                     
6ACC: 07         RLCA                    
6ACD: 00         NOP                     
6ACE: 1F         RRA                     
6ACF: 00         NOP                     
6AD0: 3F         CCF                     
6AD1: 00         NOP                     
6AD2: 3F         CCF                     
6AD3: 00         NOP                     
6AD4: 7F         LD      A,A             
6AD5: 00         NOP                     
6AD6: 7F         LD      A,A             
6AD7: 00         NOP                     
6AD8: FF         RST     0X38            
6AD9: 00         NOP                     
6ADA: FF         RST     0X38            
6ADB: 00         NOP                     
6ADC: FF         RST     0X38            
6ADD: 00         NOP                     
6ADE: FF         RST     0X38            
6ADF: 00         NOP                     
6AE0: 0F         RRCA                    
6AE1: 00         NOP                     
6AE2: 3F         CCF                     
6AE3: 00         NOP                     
6AE4: FF         RST     0X38            
6AE5: 00         NOP                     
6AE6: FF         RST     0X38            
6AE7: 00         NOP                     
6AE8: FF         RST     0X38            
6AE9: 00         NOP                     
6AEA: FF         RST     0X38            
6AEB: 00         NOP                     
6AEC: FF         RST     0X38            
6AED: 00         NOP                     
6AEE: FF         RST     0X38            
6AEF: 00         NOP                     
6AF0: FF         RST     0X38            
6AF1: 00         NOP                     
6AF2: FF         RST     0X38            
6AF3: 00         NOP                     
6AF4: FF         RST     0X38            
6AF5: 00         NOP                     
6AF6: FF         RST     0X38            
6AF7: 00         NOP                     
6AF8: CF         RST     0X08            
6AF9: 30 F7      JR      NC,$6AF2        
6AFB: 38 FB      JR      C,$6AF8         
6AFD: 3C         INC     A               
6AFE: FF         RST     0X38            
6AFF: 3C         INC     A               
6B00: DD         ???                     
6B01: 3E FF      LD      A,$FF           
6B03: 1E EF      LD      E,$EF           
6B05: 1E F7      LD      E,$F7           
6B07: 0E FD      LD      C,$FD           
6B09: 02         LD      (BC),A          
6B0A: FF         RST     0X38            
6B0B: 00         NOP                     
6B0C: FF         RST     0X38            
6B0D: 00         NOP                     
6B0E: FF         RST     0X38            
6B0F: 00         NOP                     
6B10: FF         RST     0X38            
6B11: 00         NOP                     
6B12: FF         RST     0X38            
6B13: 00         NOP                     
6B14: FF         RST     0X38            
6B15: 00         NOP                     
6B16: FF         RST     0X38            
6B17: 00         NOP                     
6B18: FF         RST     0X38            
6B19: 00         NOP                     
6B1A: FF         RST     0X38            
6B1B: 00         NOP                     
6B1C: 3F         CCF                     
6B1D: 00         NOP                     
6B1E: 07         RLCA                    
6B1F: 00         NOP                     
6B20: 00         NOP                     
6B21: 00         NOP                     
6B22: 00         NOP                     
6B23: 00         NOP                     
6B24: 00         NOP                     
6B25: 00         NOP                     
6B26: 00         NOP                     
6B27: 00         NOP                     
6B28: 01 00 03   LD      BC,$0300        
6B2B: 00         NOP                     
6B2C: 07         RLCA                    
6B2D: 00         NOP                     
6B2E: 0F         RRCA                    
6B2F: 00         NOP                     
6B30: 0F         RRCA                    
6B31: 00         NOP                     
6B32: 1F         RRA                     
6B33: 00         NOP                     
6B34: 1F         RRA                     
6B35: 00         NOP                     
6B36: 1F         RRA                     
6B37: 00         NOP                     
6B38: 3F         CCF                     
6B39: 00         NOP                     
6B3A: 3F         CCF                     
6B3B: 00         NOP                     
6B3C: 3F         CCF                     
6B3D: 00         NOP                     
6B3E: 3F         CCF                     
6B3F: 00         NOP                     
6B40: 00         NOP                     
6B41: 00         NOP                     
6B42: 00         NOP                     
6B43: 00         NOP                     
6B44: 0F         RRCA                    
6B45: 00         NOP                     
6B46: 7F         LD      A,A             
6B47: 00         NOP                     
6B48: FF         RST     0X38            
6B49: 00         NOP                     
6B4A: FF         RST     0X38            
6B4B: 00         NOP                     
6B4C: FF         RST     0X38            
6B4D: 00         NOP                     
6B4E: FF         RST     0X38            
6B4F: 00         NOP                     
6B50: FF         RST     0X38            
6B51: 00         NOP                     
6B52: FF         RST     0X38            
6B53: 00         NOP                     
6B54: FF         RST     0X38            
6B55: 00         NOP                     
6B56: FF         RST     0X38            
6B57: 00         NOP                     
6B58: FF         RST     0X38            
6B59: 00         NOP                     
6B5A: FF         RST     0X38            
6B5B: 00         NOP                     
6B5C: FF         RST     0X38            
6B5D: 00         NOP                     
6B5E: FF         RST     0X38            
6B5F: 00         NOP                     
6B60: 00         NOP                     
6B61: 00         NOP                     
6B62: 00         NOP                     
6B63: 00         NOP                     
6B64: 00         NOP                     
6B65: 00         NOP                     
6B66: 00         NOP                     
6B67: 00         NOP                     
6B68: 00         NOP                     
6B69: 00         NOP                     
6B6A: 00         NOP                     
6B6B: 00         NOP                     
6B6C: 00         NOP                     
6B6D: 00         NOP                     
6B6E: 00         NOP                     
6B6F: 00         NOP                     
6B70: 01 00 03   LD      BC,$0300        
6B73: 00         NOP                     
6B74: 03         INC     BC              
6B75: 00         NOP                     
6B76: 07         RLCA                    
6B77: 00         NOP                     
6B78: 07         RLCA                    
6B79: 00         NOP                     
6B7A: 07         RLCA                    
6B7B: 00         NOP                     
6B7C: 0F         RRCA                    
6B7D: 00         NOP                     
6B7E: 0F         RRCA                    
6B7F: 00         NOP                     
6B80: 00         NOP                     
6B81: 00         NOP                     
6B82: 00         NOP                     
6B83: 00         NOP                     
6B84: 00         NOP                     
6B85: 00         NOP                     
6B86: 00         NOP                     
6B87: 00         NOP                     
6B88: 03         INC     BC              
6B89: 00         NOP                     
6B8A: 1F         RRA                     
6B8B: 00         NOP                     
6B8C: 7F         LD      A,A             
6B8D: 00         NOP                     
6B8E: FF         RST     0X38            
6B8F: 00         NOP                     
6B90: FF         RST     0X38            
6B91: 00         NOP                     
6B92: FF         RST     0X38            
6B93: 00         NOP                     
6B94: FF         RST     0X38            
6B95: 00         NOP                     
6B96: FF         RST     0X38            
6B97: 00         NOP                     
6B98: FF         RST     0X38            
6B99: 00         NOP                     
6B9A: FF         RST     0X38            
6B9B: 00         NOP                     
6B9C: FF         RST     0X38            
6B9D: 00         NOP                     
6B9E: FF         RST     0X38            
6B9F: 00         NOP                     
6BA0: 00         NOP                     
6BA1: 00         NOP                     
6BA2: 00         NOP                     
6BA3: 00         NOP                     
6BA4: 00         NOP                     
6BA5: 00         NOP                     
6BA6: 00         NOP                     
6BA7: 00         NOP                     
6BA8: 00         NOP                     
6BA9: 00         NOP                     
6BAA: 00         NOP                     
6BAB: 00         NOP                     
6BAC: 00         NOP                     
6BAD: 00         NOP                     
6BAE: 00         NOP                     
6BAF: 00         NOP                     
6BB0: 00         NOP                     
6BB1: 00         NOP                     
6BB2: 00         NOP                     
6BB3: 00         NOP                     
6BB4: 00         NOP                     
6BB5: 00         NOP                     
6BB6: 01 00 01   LD      BC,$0100        
6BB9: 00         NOP                     
6BBA: 03         INC     BC              
6BBB: 00         NOP                     
6BBC: 03         INC     BC              
6BBD: 00         NOP                     
6BBE: 03         INC     BC              
6BBF: 00         NOP                     
6BC0: 00         NOP                     
6BC1: 00         NOP                     
6BC2: 00         NOP                     
6BC3: 00         NOP                     
6BC4: 00         NOP                     
6BC5: 00         NOP                     
6BC6: 00         NOP                     
6BC7: 00         NOP                     
6BC8: 00         NOP                     
6BC9: 00         NOP                     
6BCA: 00         NOP                     
6BCB: 00         NOP                     
6BCC: 07         RLCA                    
6BCD: 00         NOP                     
6BCE: 1F         RRA                     
6BCF: 00         NOP                     
6BD0: 7F         LD      A,A             
6BD1: 00         NOP                     
6BD2: FF         RST     0X38            
6BD3: 00         NOP                     
6BD4: FF         RST     0X38            
6BD5: 00         NOP                     
6BD6: FF         RST     0X38            
6BD7: 00         NOP                     
6BD8: FF         RST     0X38            
6BD9: 00         NOP                     
6BDA: FF         RST     0X38            
6BDB: 00         NOP                     
6BDC: FF         RST     0X38            
6BDD: 00         NOP                     
6BDE: FF         RST     0X38            
6BDF: 00         NOP                     
6BE0: 00         NOP                     
6BE1: FF         RST     0X38            
6BE2: 00         NOP                     
6BE3: FF         RST     0X38            
6BE4: 22         LD      (HLI),A         
6BE5: FF         RST     0X38            
6BE6: 14         INC     D               
6BE7: FF         RST     0X38            
6BE8: 08 FF 14   LD      ($14FF),SP      
6BEB: FF         RST     0X38            
6BEC: 22         LD      (HLI),A         
6BED: FF         RST     0X38            
6BEE: 00         NOP                     
6BEF: FF         RST     0X38            
6BF0: 00         NOP                     
6BF1: FF         RST     0X38            
6BF2: 00         NOP                     
6BF3: FF         RST     0X38            
6BF4: 22         LD      (HLI),A         
6BF5: FF         RST     0X38            
6BF6: 14         INC     D               
6BF7: FF         RST     0X38            
6BF8: 08 FF 14   LD      ($14FF),SP      
6BFB: FF         RST     0X38            
6BFC: 22         LD      (HLI),A         
6BFD: FF         RST     0X38            
6BFE: 00         NOP                     
6BFF: FF         RST     0X38            
6C00: 00         NOP                     
6C01: 00         NOP                     
6C02: 00         NOP                     
6C03: 00         NOP                     
6C04: 00         NOP                     
6C05: 00         NOP                     
6C06: 00         NOP                     
6C07: 00         NOP                     
6C08: 00         NOP                     
6C09: 00         NOP                     
6C0A: 00         NOP                     
6C0B: 00         NOP                     
6C0C: 00         NOP                     
6C0D: 00         NOP                     
6C0E: 01 00 03   LD      BC,$0300        
6C11: 00         NOP                     
6C12: 03         INC     BC              
6C13: 00         NOP                     
6C14: 07         RLCA                    
6C15: 00         NOP                     
6C16: 07         RLCA                    
6C17: 00         NOP                     
6C18: 07         RLCA                    
6C19: 00         NOP                     
6C1A: 07         RLCA                    
6C1B: 00         NOP                     
6C1C: 07         RLCA                    
6C1D: 00         NOP                     
6C1E: 07         RLCA                    
6C1F: 00         NOP                     
6C20: 00         NOP                     
6C21: 00         NOP                     
6C22: 00         NOP                     
6C23: 00         NOP                     
6C24: 00         NOP                     
6C25: 00         NOP                     
6C26: 00         NOP                     
6C27: 00         NOP                     
6C28: 19         ADD     HL,DE           
6C29: 00         NOP                     
6C2A: 1F         RRA                     
6C2B: 00         NOP                     
6C2C: 3F         CCF                     
6C2D: 00         NOP                     
6C2E: BF         CP      A               
6C2F: 00         NOP                     
6C30: FF         RST     0X38            
6C31: 00         NOP                     
6C32: FB         EI                      
6C33: 1C         INC     E               
6C34: FD         ???                     
6C35: 1E EF      LD      E,$EF           
6C37: 1E F7      LD      E,$F7           
6C39: 0E FF      LD      C,$FF           
6C3B: 00         NOP                     
6C3C: FF         RST     0X38            
6C3D: 00         NOP                     
6C3E: FF         RST     0X38            
6C3F: 00         NOP                     
6C40: FF         RST     0X38            
6C41: 00         NOP                     
6C42: FF         RST     0X38            
6C43: 00         NOP                     
6C44: FF         RST     0X38            
6C45: 00         NOP                     
6C46: FF         RST     0X38            
6C47: 00         NOP                     
6C48: FF         RST     0X38            
6C49: 00         NOP                     
6C4A: FF         RST     0X38            
6C4B: 00         NOP                     
6C4C: FF         RST     0X38            
6C4D: 00         NOP                     
6C4E: FF         RST     0X38            
6C4F: 00         NOP                     
6C50: FF         RST     0X38            
6C51: 00         NOP                     
6C52: FF         RST     0X38            
6C53: 00         NOP                     
6C54: FF         RST     0X38            
6C55: 00         NOP                     
6C56: 1F         RRA                     
6C57: 00         NOP                     
6C58: 0C         INC     C               
6C59: 00         NOP                     
6C5A: DE 00      SBC     $00             
6C5C: FE 00      CP      $00             
6C5E: 78         LD      A,B             
6C5F: 00         NOP                     
6C60: 00         NOP                     
6C61: 00         NOP                     
6C62: 00         NOP                     
6C63: 00         NOP                     
6C64: 00         NOP                     
6C65: 00         NOP                     
6C66: 00         NOP                     
6C67: 00         NOP                     
6C68: 19         ADD     HL,DE           
6C69: 00         NOP                     
6C6A: 1F         RRA                     
6C6B: 00         NOP                     
6C6C: 3F         CCF                     
6C6D: 00         NOP                     
6C6E: BF         CP      A               
6C6F: 00         NOP                     
6C70: FF         RST     0X38            
6C71: 00         NOP                     
6C72: FF         RST     0X38            
6C73: 00         NOP                     
6C74: FF         RST     0X38            
6C75: 00         NOP                     
6C76: FF         RST     0X38            
6C77: 00         NOP                     
6C78: FF         RST     0X38            
6C79: 00         NOP                     
6C7A: FF         RST     0X38            
6C7B: 00         NOP                     
6C7C: FF         RST     0X38            
6C7D: 00         NOP                     
6C7E: FF         RST     0X38            
6C7F: 00         NOP                     
6C80: FF         RST     0X38            
6C81: 00         NOP                     
6C82: FF         RST     0X38            
6C83: 00         NOP                     
6C84: FF         RST     0X38            
6C85: 00         NOP                     
6C86: FF         RST     0X38            
6C87: 00         NOP                     
6C88: FF         RST     0X38            
6C89: 00         NOP                     
6C8A: FF         RST     0X38            
6C8B: 00         NOP                     
6C8C: FF         RST     0X38            
6C8D: 00         NOP                     
6C8E: FF         RST     0X38            
6C8F: 00         NOP                     
6C90: FF         RST     0X38            
6C91: 00         NOP                     
6C92: FF         RST     0X38            
6C93: 00         NOP                     
6C94: FF         RST     0X38            
6C95: 00         NOP                     
6C96: FF         RST     0X38            
6C97: 00         NOP                     
6C98: FF         RST     0X38            
6C99: 00         NOP                     
6C9A: FF         RST     0X38            
6C9B: 00         NOP                     
6C9C: 7C         LD      A,H             
6C9D: 00         NOP                     
6C9E: 1C         INC     E               
6C9F: 00         NOP                     
6CA0: 00         NOP                     
6CA1: 00         NOP                     
6CA2: 0C         INC     C               
6CA3: 00         NOP                     
6CA4: 0C         INC     C               
6CA5: 00         NOP                     
6CA6: C6 00      ADD     $00             
6CA8: F2         ???                     
6CA9: 00         NOP                     
6CAA: 1A         LD      A,(DE)          
6CAB: 00         NOP                     
6CAC: 0F         RRCA                    
6CAD: 00         NOP                     
6CAE: FF         RST     0X38            
6CAF: 00         NOP                     
6CB0: CF         RST     0X08            
6CB1: 00         NOP                     
6CB2: 1F         RRA                     
6CB3: 00         NOP                     
6CB4: 33         INC     SP              
6CB5: 00         NOP                     
6CB6: 33         INC     SP              
6CB7: 00         NOP                     
6CB8: 03         INC     BC              
6CB9: 00         NOP                     
6CBA: 03         INC     BC              
6CBB: 00         NOP                     
6CBC: 01 00 00   LD      BC,$0000        
6CBF: 00         NOP                     
6CC0: 00         NOP                     
6CC1: 00         NOP                     
6CC2: 00         NOP                     
6CC3: 00         NOP                     
6CC4: 00         NOP                     
6CC5: 00         NOP                     
6CC6: C0         RET     NZ              
6CC7: 00         NOP                     
6CC8: C0         RET     NZ              
6CC9: 00         NOP                     
6CCA: 40         LD      B,B             
6CCB: 00         NOP                     
6CCC: C0         RET     NZ              
6CCD: 00         NOP                     
6CCE: 80         ADD     A,B             
6CCF: 00         NOP                     
6CD0: 00         NOP                     
6CD1: 00         NOP                     
6CD2: 00         NOP                     
6CD3: 00         NOP                     
6CD4: 07         RLCA                    
6CD5: 00         NOP                     
6CD6: FF         RST     0X38            
6CD7: 00         NOP                     
6CD8: FF         RST     0X38            
6CD9: 00         NOP                     
6CDA: FF         RST     0X38            
6CDB: 00         NOP                     
6CDC: 1F         RRA                     
6CDD: 00         NOP                     
6CDE: 0F         RRCA                    
6CDF: 00         NOP                     
6CE0: 0F         RRCA                    
6CE1: 00         NOP                     
6CE2: 0F         RRCA                    
6CE3: 00         NOP                     
6CE4: 0F         RRCA                    
6CE5: 00         NOP                     
6CE6: 0F         RRCA                    
6CE7: 00         NOP                     
6CE8: 1F         RRA                     
6CE9: 00         NOP                     
6CEA: 1F         RRA                     
6CEB: 00         NOP                     
6CEC: 1F         RRA                     
6CED: 00         NOP                     
6CEE: 1F         RRA                     
6CEF: 00         NOP                     
6CF0: 3F         CCF                     
6CF1: 00         NOP                     
6CF2: 3F         CCF                     
6CF3: 00         NOP                     
6CF4: 3F         CCF                     
6CF5: 00         NOP                     
6CF6: 3F         CCF                     
6CF7: 00         NOP                     
6CF8: 3F         CCF                     
6CF9: 00         NOP                     
6CFA: 1E 00      LD      E,$00           
6CFC: 0C         INC     C               
6CFD: 00         NOP                     
6CFE: 00         NOP                     
6CFF: 00         NOP                     
6D00: E0 40      LDFF00  ($40),A         
6D02: E0 40      LDFF00  ($40),A         
6D04: FC         ???                     
6D05: 60         LD      H,B             
6D06: 7E         LD      A,(HL)          
6D07: 3C         INC     A               
6D08: 3F         CCF                     
6D09: 0E 0F      LD      C,$0F           
6D0B: 06 07      LD      B,$07           
6D0D: 02         LD      (BC),A          
6D0E: 07         RLCA                    
6D0F: 02         LD      (BC),A          
6D10: 3F         CCF                     
6D11: 06 7F      LD      B,$7F           
6D13: 3E FE      LD      A,$FE           
6D15: 70         LD      (HL),B          
6D16: F0 60      LD      A,($60)         
6D18: E0 40      LDFF00  ($40),A         
6D1A: E0 40      LDFF00  ($40),A         
6D1C: E0 40      LDFF00  ($40),A         
6D1E: E0 40      LDFF00  ($40),A         
6D20: 00         NOP                     
6D21: 00         NOP                     
6D22: 00         NOP                     
6D23: 00         NOP                     
6D24: 00         NOP                     
6D25: 00         NOP                     
6D26: 00         NOP                     
6D27: 00         NOP                     
6D28: 33         INC     SP              
6D29: 00         NOP                     
6D2A: 7F         LD      A,A             
6D2B: 00         NOP                     
6D2C: 7F         LD      A,A             
6D2D: 00         NOP                     
6D2E: FF         RST     0X38            
6D2F: 00         NOP                     
6D30: FF         RST     0X38            
6D31: 00         NOP                     
6D32: F7         RST     0X30            
6D33: 0C         INC     C               
6D34: EB         ???                     
6D35: 1C         INC     E               
6D36: 6F         LD      L,A             
6D37: 18 6F      JR      $6DA8           
6D39: 18 FF      JR      $6D3A           
6D3B: 00         NOP                     
6D3C: FF         RST     0X38            
6D3D: 00         NOP                     
6D3E: FF         RST     0X38            
6D3F: 00         NOP                     
6D40: 00         NOP                     
6D41: 00         NOP                     
6D42: 00         NOP                     
6D43: 00         NOP                     
6D44: 00         NOP                     
6D45: 00         NOP                     
6D46: 00         NOP                     
6D47: 00         NOP                     
6D48: 00         NOP                     
6D49: 00         NOP                     
6D4A: 80         ADD     A,B             
6D4B: 00         NOP                     
6D4C: C0         RET     NZ              
6D4D: 00         NOP                     
6D4E: C0         RET     NZ              
6D4F: 00         NOP                     
6D50: F0 00      LD      A,($00)         
6D52: F8 00      LDHL    SP,$00          
6D54: F8 00      LDHL    SP,$00          
6D56: F8 00      LDHL    SP,$00          
6D58: FE 00      CP      $00             
6D5A: FF         RST     0X38            
6D5B: 00         NOP                     
6D5C: FF         RST     0X38            
6D5D: 00         NOP                     
6D5E: FF         RST     0X38            
6D5F: 00         NOP                     
6D60: FF         RST     0X38            
6D61: 00         NOP                     
6D62: FF         RST     0X38            
6D63: 00         NOP                     
6D64: FF         RST     0X38            
6D65: 00         NOP                     
6D66: FF         RST     0X38            
6D67: 00         NOP                     
6D68: FF         RST     0X38            
6D69: 00         NOP                     
6D6A: FF         RST     0X38            
6D6B: 00         NOP                     
6D6C: FF         RST     0X38            
6D6D: 00         NOP                     
6D6E: FF         RST     0X38            
6D6F: 00         NOP                     
6D70: FF         RST     0X38            
6D71: 00         NOP                     
6D72: FF         RST     0X38            
6D73: 00         NOP                     
6D74: FF         RST     0X38            
6D75: 00         NOP                     
6D76: 7F         LD      A,A             
6D77: 00         NOP                     
6D78: 1F         RRA                     
6D79: 00         NOP                     
6D7A: 1F         RRA                     
6D7B: 00         NOP                     
6D7C: 7F         LD      A,A             
6D7D: 00         NOP                     
6D7E: 78         LD      A,B             
6D7F: 00         NOP                     
6D80: F8 00      LDHL    SP,$00          
6D82: F8 00      LDHL    SP,$00          
6D84: FC         ???                     
6D85: 00         NOP                     
6D86: FC         ???                     
6D87: 00         NOP                     
6D88: FC         ???                     
6D89: 00         NOP                     
6D8A: FE 00      CP      $00             
6D8C: FE 00      CP      $00             
6D8E: FE 00      CP      $00             
6D90: FF         RST     0X38            
6D91: 00         NOP                     
6D92: FF         RST     0X38            
6D93: 00         NOP                     
6D94: FF         RST     0X38            
6D95: 00         NOP                     
6D96: FF         RST     0X38            
6D97: 00         NOP                     
6D98: FE 00      CP      $00             
6D9A: FC         ???                     
6D9B: 00         NOP                     
6D9C: 00         NOP                     
6D9D: 00         NOP                     
6D9E: 00         NOP                     
6D9F: 00         NOP                     
6DA0: 00         NOP                     
6DA1: 00         NOP                     
6DA2: 1F         RRA                     
6DA3: 00         NOP                     
6DA4: 3F         CCF                     
6DA5: 00         NOP                     
6DA6: FF         RST     0X38            
6DA7: 00         NOP                     
6DA8: FF         RST     0X38            
6DA9: 00         NOP                     
6DAA: FF         RST     0X38            
6DAB: 00         NOP                     
6DAC: 3F         CCF                     
6DAD: 00         NOP                     
6DAE: 3F         CCF                     
6DAF: 00         NOP                     
6DB0: 3F         CCF                     
6DB1: 00         NOP                     
6DB2: 3F         CCF                     
6DB3: 00         NOP                     
6DB4: 3F         CCF                     
6DB5: 00         NOP                     
6DB6: 3F         CCF                     
6DB7: 00         NOP                     
6DB8: 3F         CCF                     
6DB9: 00         NOP                     
6DBA: 3F         CCF                     
6DBB: 00         NOP                     
6DBC: 1E 00      LD      E,$00           
6DBE: 00         NOP                     
6DBF: 00         NOP                     
6DC0: 00         NOP                     
6DC1: 00         NOP                     
6DC2: 00         NOP                     
6DC3: 00         NOP                     
6DC4: 03         INC     BC              
6DC5: 00         NOP                     
6DC6: 0C         INC     C               
6DC7: 03         INC     BC              
6DC8: 10 0F      STOP    $0F             
6DCA: 11 0F 23   LD      DE,$230F        
6DCD: 1F         RRA                     
6DCE: 27         DAA                     
6DCF: 1F         RRA                     
6DD0: 27         DAA                     
6DD1: 1F         RRA                     
6DD2: 23         INC     HL              
6DD3: 1F         RRA                     
6DD4: 11 0F 10   LD      DE,$100F        
6DD7: 0F         RRCA                    
6DD8: 0C         INC     C               
6DD9: 03         INC     BC              
6DDA: 03         INC     BC              
6DDB: 00         NOP                     
6DDC: 00         NOP                     
6DDD: 00         NOP                     
6DDE: 00         NOP                     
6DDF: 00         NOP                     
6DE0: 07         RLCA                    
6DE1: 00         NOP                     
6DE2: 18 07      JR      $6DEB           
6DE4: 20 1F      JR      NZ,$6E05        
6DE6: 40         LD      B,B             
6DE7: 3F         CCF                     
6DE8: 43         LD      B,E             
6DE9: 3F         CCF                     
6DEA: 87         ADD     A,A             
6DEB: 7F         LD      A,A             
6DEC: 8F         ADC     A,A             
6DED: 7F         LD      A,A             
6DEE: 8F         ADC     A,A             
6DEF: 7F         LD      A,A             
6DF0: 8F         ADC     A,A             
6DF1: 7F         LD      A,A             
6DF2: 8F         ADC     A,A             
6DF3: 7F         LD      A,A             
6DF4: 87         ADD     A,A             
6DF5: 7F         LD      A,A             
6DF6: 43         LD      B,E             
6DF7: 3F         CCF                     
6DF8: 40         LD      B,B             
6DF9: 3F         CCF                     
6DFA: 20 1F      JR      NZ,$6E1B        
6DFC: 18 07      JR      $6E05           
6DFE: 07         RLCA                    
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
6E0A: 00         NOP                     
6E0B: 00         NOP                     
6E0C: 00         NOP                     
6E0D: 00         NOP                     
6E0E: 00         NOP                     
6E0F: 00         NOP                     
6E10: 01 00 01   LD      BC,$0100        
6E13: 00         NOP                     
6E14: 00         NOP                     
6E15: 00         NOP                     
6E16: 00         NOP                     
6E17: 00         NOP                     
6E18: 01 00 01   LD      BC,$0100        
6E1B: 00         NOP                     
6E1C: 07         RLCA                    
6E1D: 00         NOP                     
6E1E: 0F         RRCA                    
6E1F: 00         NOP                     
6E20: 00         NOP                     
6E21: 00         NOP                     
6E22: 00         NOP                     
6E23: 00         NOP                     
6E24: 00         NOP                     
6E25: 00         NOP                     
6E26: 00         NOP                     
6E27: 00         NOP                     
6E28: 01 00 03   LD      BC,$0300        
6E2B: 00         NOP                     
6E2C: 03         INC     BC              
6E2D: 00         NOP                     
6E2E: CF         RST     0X08            
6E2F: 00         NOP                     
6E30: FF         RST     0X38            
6E31: 00         NOP                     
6E32: FF         RST     0X38            
6E33: 00         NOP                     
6E34: FF         RST     0X38            
6E35: 00         NOP                     
6E36: FF         RST     0X38            
6E37: 00         NOP                     
6E38: FF         RST     0X38            
6E39: 00         NOP                     
6E3A: FF         RST     0X38            
6E3B: 00         NOP                     
6E3C: FF         RST     0X38            
6E3D: 00         NOP                     
6E3E: FF         RST     0X38            
6E3F: 00         NOP                     
6E40: 0F         RRCA                    
6E41: 00         NOP                     
6E42: 07         RLCA                    
6E43: 00         NOP                     
6E44: 01 00 01   LD      BC,$0100        
6E47: 00         NOP                     
6E48: 03         INC     BC              
6E49: 00         NOP                     
6E4A: 03         INC     BC              
6E4B: 00         NOP                     
6E4C: 01 00 00   LD      BC,$0000        
6E4F: 00         NOP                     
6E50: 00         NOP                     
6E51: 00         NOP                     
6E52: 00         NOP                     
6E53: 00         NOP                     
6E54: 00         NOP                     
6E55: 00         NOP                     
6E56: 00         NOP                     
6E57: 00         NOP                     
6E58: 00         NOP                     
6E59: 00         NOP                     
6E5A: 00         NOP                     
6E5B: 00         NOP                     
6E5C: 00         NOP                     
6E5D: 00         NOP                     
6E5E: 00         NOP                     
6E5F: 00         NOP                     
6E60: FF         RST     0X38            
6E61: 00         NOP                     
6E62: FF         RST     0X38            
6E63: 00         NOP                     
6E64: FF         RST     0X38            
6E65: 00         NOP                     
6E66: FF         RST     0X38            
6E67: 00         NOP                     
6E68: DD         ???                     
6E69: 3E BE      LD      A,$BE           
6E6B: 7F         LD      A,A             
6E6C: FF         RST     0X38            
6E6D: 7F         LD      A,A             
6E6E: FF         RST     0X38            
6E6F: 7F         LD      A,A             
6E70: BE         CP      (HL)            
6E71: 7F         LD      A,A             
6E72: 5D         LD      E,L             
6E73: 3E 3E      LD      A,$3E           
6E75: 00         NOP                     
6E76: 78         LD      A,B             
6E77: 00         NOP                     
6E78: F0 00      LD      A,($00)         
6E7A: F0 00      LD      A,($00)         
6E7C: F0 00      LD      A,($00)         
6E7E: 60         LD      H,B             
6E7F: 00         NOP                     
6E80: 00         NOP                     
6E81: 00         NOP                     
6E82: 00         NOP                     
6E83: 00         NOP                     
6E84: 00         NOP                     
6E85: 00         NOP                     
6E86: 00         NOP                     
6E87: 00         NOP                     
6E88: 00         NOP                     
6E89: 00         NOP                     
6E8A: 00         NOP                     
6E8B: 00         NOP                     
6E8C: 00         NOP                     
6E8D: 00         NOP                     
6E8E: 00         NOP                     
6E8F: 00         NOP                     
6E90: 71         LD      (HL),C          
6E91: 00         NOP                     
6E92: FA 01 FD   LD      A,($FD01)       
6E95: 03         INC     BC              
6E96: 7F         LD      A,A             
6E97: 03         INC     BC              
6E98: 0F         RRCA                    
6E99: 03         INC     BC              
6E9A: 07         RLCA                    
6E9B: 03         INC     BC              
6E9C: 05         DEC     B               
6E9D: 03         INC     BC              
6E9E: 02         LD      (BC),A          
6E9F: 01 00 00   LD      BC,$0000        
6EA2: 00         NOP                     
6EA3: 00         NOP                     
6EA4: 00         NOP                     
6EA5: 00         NOP                     
6EA6: 00         NOP                     
6EA7: 00         NOP                     
6EA8: 01 00 03   LD      BC,$0300        
6EAB: 00         NOP                     
6EAC: 33         INC     SP              
6EAD: 00         NOP                     
6EAE: 7F         LD      A,A             
6EAF: 00         NOP                     
6EB0: FF         RST     0X38            
6EB1: 00         NOP                     
6EB2: DF         RST     0X18            
6EB3: E0 EF      LDFF00  ($EF),A         
6EB5: F0 FF      LD      A,($FF)         
6EB7: F0 FF      LD      A,($FF)         
6EB9: F0 FF      LD      A,($FF)         
6EBB: F0 EF      LD      A,($EF)         
6EBD: F0 DF      LD      A,($DF)         
6EBF: E0 0E      LDFF00  ($0E),A         
6EC1: 01 05 03   LD      BC,$0305        
6EC4: 3F         CCF                     
6EC5: 03         INC     BC              
6EC6: 7F         LD      A,A             
6EC7: 03         INC     BC              
6EC8: FF         RST     0X38            
6EC9: 03         INC     BC              
6ECA: F5         PUSH    AF              
6ECB: 03         INC     BC              
6ECC: 63         LD      H,E             
6ECD: 00         NOP                     
6ECE: 00         NOP                     
6ECF: 00         NOP                     
6ED0: 00         NOP                     
6ED1: 00         NOP                     
6ED2: 00         NOP                     
6ED3: 00         NOP                     
6ED4: 00         NOP                     
6ED5: 00         NOP                     
6ED6: 00         NOP                     
6ED7: 00         NOP                     
6ED8: 00         NOP                     
6ED9: 00         NOP                     
6EDA: 00         NOP                     
6EDB: 00         NOP                     
6EDC: 00         NOP                     
6EDD: 00         NOP                     
6EDE: 00         NOP                     
6EDF: 00         NOP                     
6EE0: DF         RST     0X18            
6EE1: E0 EF      LDFF00  ($EF),A         
6EE3: F0 FF      LD      A,($FF)         
6EE5: F0 FF      LD      A,($FF)         
6EE7: F0 ED      LD      A,($ED)         
6EE9: FE FE      CP      $FE             
6EEB: FF         RST     0X38            
6EEC: 3F         CCF                     
6EED: FF         RST     0X38            
6EEE: BF         CP      A               
6EEF: 7F         LD      A,A             
6EF0: 7E         LD      A,(HL)          
6EF1: 3F         CCF                     
6EF2: 5D         LD      E,L             
6EF3: 3E 3F      LD      A,$3F           
6EF5: 00         NOP                     
6EF6: 1D         DEC     E               
6EF7: 00         NOP                     
6EF8: 3C         INC     A               
6EF9: 00         NOP                     
6EFA: 7C         LD      A,H             
6EFB: 00         NOP                     
6EFC: 78         LD      A,B             
6EFD: 00         NOP                     
6EFE: 30 00      JR      NC,$6F00        
6F00: E7         RST     0X20            
6F01: 00         NOP                     
6F02: FF         RST     0X38            
6F03: 00         NOP                     
6F04: FF         RST     0X38            
6F05: 00         NOP                     
6F06: 7F         LD      A,A             
6F07: 00         NOP                     
6F08: 7F         LD      A,A             
6F09: 00         NOP                     
6F0A: FF         RST     0X38            
6F0B: 00         NOP                     
6F0C: FF         RST     0X38            
6F0D: 00         NOP                     
6F0E: FF         RST     0X38            
6F0F: 00         NOP                     
6F10: FF         RST     0X38            
6F11: 00         NOP                     
6F12: FF         RST     0X38            
6F13: 00         NOP                     
6F14: FF         RST     0X38            
6F15: 00         NOP                     
6F16: 7F         LD      A,A             
6F17: 00         NOP                     
6F18: 7F         LD      A,A             
6F19: 00         NOP                     
6F1A: FF         RST     0X38            
6F1B: 00         NOP                     
6F1C: FF         RST     0X38            
6F1D: 00         NOP                     
6F1E: E7         RST     0X20            
6F1F: 00         NOP                     
6F20: 00         NOP                     
6F21: 00         NOP                     
6F22: 73         LD      (HL),E          
6F23: 00         NOP                     
6F24: 7F         LD      A,A             
6F25: 00         NOP                     
6F26: 7F         LD      A,A             
6F27: 00         NOP                     
6F28: 3F         CCF                     
6F29: 00         NOP                     
6F2A: 3F         CCF                     
6F2B: 00         NOP                     
6F2C: 7F         LD      A,A             
6F2D: 00         NOP                     
6F2E: 7F         LD      A,A             
6F2F: 00         NOP                     
6F30: 7F         LD      A,A             
6F31: 00         NOP                     
6F32: 7F         LD      A,A             
6F33: 00         NOP                     
6F34: 3F         CCF                     
6F35: 00         NOP                     
6F36: 3F         CCF                     
6F37: 00         NOP                     
6F38: 7F         LD      A,A             
6F39: 00         NOP                     
6F3A: 7F         LD      A,A             
6F3B: 00         NOP                     
6F3C: 73         LD      (HL),E          
6F3D: 00         NOP                     
6F3E: 00         NOP                     
6F3F: 00         NOP                     
6F40: 03         INC     BC              
6F41: 00         NOP                     
6F42: 07         RLCA                    
6F43: 00         NOP                     
6F44: 07         RLCA                    
6F45: 00         NOP                     
6F46: 0F         RRCA                    
6F47: 00         NOP                     
6F48: 1F         RRA                     
6F49: 00         NOP                     
6F4A: 7F         LD      A,A             
6F4B: 00         NOP                     
6F4C: FF         RST     0X38            
6F4D: 08 FF 0C   LD      ($0CFF),SP      
6F50: FF         RST     0X38            
6F51: 0E FF      LD      C,$FF           
6F53: 06 7F      LD      B,$7F           
6F55: 02         LD      (BC),A          
6F56: 1F         RRA                     
6F57: 00         NOP                     
6F58: 0F         RRCA                    
6F59: 00         NOP                     
6F5A: 07         RLCA                    
6F5B: 00         NOP                     
6F5C: 07         RLCA                    
6F5D: 00         NOP                     
6F5E: 03         INC     BC              
6F5F: 00         NOP                     
6F60: 00         NOP                     
6F61: 00         NOP                     
6F62: 38 00      JR      C,$6F64         
6F64: 7F         LD      A,A             
6F65: 00         NOP                     
6F66: 7F         LD      A,A             
6F67: 00         NOP                     
6F68: 7F         LD      A,A             
6F69: 00         NOP                     
6F6A: 3F         CCF                     
6F6B: 00         NOP                     
6F6C: 3F         CCF                     
6F6D: 08 3F 0C   LD      ($0C3F),SP      
6F70: 3F         CCF                     
6F71: 0E 3F      LD      C,$3F           
6F73: 06 3F      LD      B,$3F           
6F75: 02         LD      (BC),A          
6F76: 7F         LD      A,A             
6F77: 00         NOP                     
6F78: 7F         LD      A,A             
6F79: 00         NOP                     
6F7A: 7F         LD      A,A             
6F7B: 00         NOP                     
6F7C: 38 00      JR      C,$6F7E         
6F7E: 00         NOP                     
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
6F8A: 00         NOP                     
6F8B: 00         NOP                     
6F8C: 01 00 03   LD      BC,$0300        
6F8F: 00         NOP                     
6F90: 03         INC     BC              
6F91: 00         NOP                     
6F92: 01 00 00   LD      BC,$0000        
6F95: 00         NOP                     
6F96: 00         NOP                     
6F97: 00         NOP                     
6F98: 01 00 01   LD      BC,$0100        
6F9B: 00         NOP                     
6F9C: 00         NOP                     
6F9D: 00         NOP                     
6F9E: 00         NOP                     
6F9F: 00         NOP                     
6FA0: 00         NOP                     
6FA1: 00         NOP                     
6FA2: 00         NOP                     
6FA3: 00         NOP                     
6FA4: 00         NOP                     
6FA5: 00         NOP                     
6FA6: 00         NOP                     
6FA7: 00         NOP                     
6FA8: 00         NOP                     
6FA9: 00         NOP                     
6FAA: 00         NOP                     
6FAB: 00         NOP                     
6FAC: 01 00 01   LD      BC,$0100        
6FAF: 00         NOP                     
6FB0: 67         LD      H,A             
6FB1: 00         NOP                     
6FB2: FF         RST     0X38            
6FB3: 00         NOP                     
6FB4: FF         RST     0X38            
6FB5: 00         NOP                     
6FB6: 7F         LD      A,A             
6FB7: 00         NOP                     
6FB8: FF         RST     0X38            
6FB9: 00         NOP                     
6FBA: FF         RST     0X38            
6FBB: 00         NOP                     
6FBC: FF         RST     0X38            
6FBD: 00         NOP                     
6FBE: FF         RST     0X38            
6FBF: 00         NOP                     
6FC0: FF         RST     0X38            
6FC1: 00         NOP                     
6FC2: FF         RST     0X38            
6FC3: 00         NOP                     
6FC4: FF         RST     0X38            
6FC5: 00         NOP                     
6FC6: F1         POP     AF              
6FC7: 0E E0      LD      C,$E0           
6FC9: 1F         RRA                     
6FCA: E0 1F      LDFF00  ($1F),A         
6FCC: 20 1F      JR      NZ,$6FED        
6FCE: 11 0E 1F   LD      DE,$1F0E        
6FD1: 00         NOP                     
6FD2: 3C         INC     A               
6FD3: 00         NOP                     
6FD4: 38 00      JR      C,$6FD6         
6FD6: 38 00      JR      C,$6FD8         
6FD8: 00         NOP                     
6FD9: 00         NOP                     
6FDA: 00         NOP                     
6FDB: 00         NOP                     
6FDC: 00         NOP                     
6FDD: 00         NOP                     
6FDE: 00         NOP                     
6FDF: 00         NOP                     
6FE0: 00         NOP                     
6FE1: FF         RST     0X38            
6FE2: 00         NOP                     
6FE3: FF         RST     0X38            
6FE4: 22         LD      (HLI),A         
6FE5: FF         RST     0X38            
6FE6: 14         INC     D               
6FE7: FF         RST     0X38            
6FE8: 08 FF 14   LD      ($14FF),SP      
6FEB: FF         RST     0X38            
6FEC: 22         LD      (HLI),A         
6FED: FF         RST     0X38            
6FEE: 00         NOP                     
6FEF: FF         RST     0X38            
6FF0: 00         NOP                     
6FF1: FF         RST     0X38            
6FF2: 00         NOP                     
6FF3: FF         RST     0X38            
6FF4: 22         LD      (HLI),A         
6FF5: FF         RST     0X38            
6FF6: 14         INC     D               
6FF7: FF         RST     0X38            
6FF8: 08 FF 14   LD      ($14FF),SP      
6FFB: FF         RST     0X38            
6FFC: 22         LD      (HLI),A         
6FFD: FF         RST     0X38            
6FFE: 00         NOP                     
6FFF: FF         RST     0X38            
7000: C3 00 F3   JP      $F300           
7003: 00         NOP                     
7004: FB         EI                      
7005: 00         NOP                     
7006: FB         EI                      
7007: 00         NOP                     
7008: FF         RST     0X38            
7009: 00         NOP                     
700A: FF         RST     0X38            
700B: 00         NOP                     
700C: FF         RST     0X38            
700D: 00         NOP                     
700E: FF         RST     0X38            
700F: 00         NOP                     
7010: FF         RST     0X38            
7011: 00         NOP                     
7012: FF         RST     0X38            
7013: 00         NOP                     
7014: 7F         LD      A,A             
7015: 00         NOP                     
7016: 3F         CCF                     
7017: 00         NOP                     
7018: 03         INC     BC              
7019: 00         NOP                     
701A: 00         NOP                     
701B: 00         NOP                     
701C: 00         NOP                     
701D: 00         NOP                     
701E: 00         NOP                     
701F: 00         NOP                     
7020: 00         NOP                     
7021: 00         NOP                     
7022: 18 00      JR      $7024           
7024: 38 00      JR      C,$7026         
7026: 30 00      JR      NC,$7028        
7028: 70         LD      (HL),B          
7029: 00         NOP                     
702A: E3         ???                     
702B: 00         NOP                     
702C: FF         RST     0X38            
702D: 00         NOP                     
702E: FE 00      CP      $00             
7030: F8 00      LDHL    SP,$00          
7032: FC         ???                     
7033: 00         NOP                     
7034: FF         RST     0X38            
7035: 00         NOP                     
7036: E7         RST     0X20            
7037: 00         NOP                     
7038: C0         RET     NZ              
7039: 00         NOP                     
703A: 00         NOP                     
703B: 00         NOP                     
703C: 00         NOP                     
703D: 00         NOP                     
703E: 00         NOP                     
703F: 00         NOP                     
7040: 1E 00      LD      E,$00           
7042: 3F         CCF                     
7043: 00         NOP                     
7044: 7F         LD      A,A             
7045: 00         NOP                     
7046: 7F         LD      A,A             
7047: 00         NOP                     
7048: 7E         LD      A,(HL)          
7049: 00         NOP                     
704A: FC         ???                     
704B: 00         NOP                     
704C: FC         ???                     
704D: 00         NOP                     
704E: FE 00      CP      $00             
7050: FE 00      CP      $00             
7052: FF         RST     0X38            
7053: 00         NOP                     
7054: 7F         LD      A,A             
7055: 00         NOP                     
7056: 7F         LD      A,A             
7057: 00         NOP                     
7058: 3F         CCF                     
7059: 00         NOP                     
705A: 3F         CCF                     
705B: 00         NOP                     
705C: 1F         RRA                     
705D: 00         NOP                     
705E: 0F         RRCA                    
705F: 00         NOP                     
7060: 01 00 07   LD      BC,$0700        
7063: 00         NOP                     
7064: 1F         RRA                     
7065: 00         NOP                     
7066: 3F         CCF                     
7067: 00         NOP                     
7068: 7F         LD      A,A             
7069: 00         NOP                     
706A: 7F         LD      A,A             
706B: 00         NOP                     
706C: FF         RST     0X38            
706D: 00         NOP                     
706E: FF         RST     0X38            
706F: 00         NOP                     
7070: FF         RST     0X38            
7071: 00         NOP                     
7072: FF         RST     0X38            
7073: 00         NOP                     
7074: FF         RST     0X38            
7075: 00         NOP                     
7076: 7F         LD      A,A             
7077: 00         NOP                     
7078: 1F         RRA                     
7079: 00         NOP                     
707A: 07         RLCA                    
707B: 00         NOP                     
707C: 00         NOP                     
707D: 00         NOP                     
707E: 00         NOP                     
707F: 00         NOP                     
7080: 07         RLCA                    
7081: 00         NOP                     
7082: 07         RLCA                    
7083: 00         NOP                     
7084: 1F         RRA                     
7085: 00         NOP                     
7086: 3F         CCF                     
7087: 00         NOP                     
7088: 7F         LD      A,A             
7089: 00         NOP                     
708A: 7F         LD      A,A             
708B: 00         NOP                     
708C: 7F         LD      A,A             
708D: 00         NOP                     
708E: 7F         LD      A,A             
708F: 00         NOP                     
7090: 3F         CCF                     
7091: 00         NOP                     
7092: 1F         RRA                     
7093: 00         NOP                     
7094: 1F         RRA                     
7095: 00         NOP                     
7096: 3F         CCF                     
7097: 00         NOP                     
7098: 7F         LD      A,A             
7099: 00         NOP                     
709A: 7F         LD      A,A             
709B: 00         NOP                     
709C: 1F         RRA                     
709D: 00         NOP                     
709E: 1D         DEC     E               
709F: 00         NOP                     
70A0: 07         RLCA                    
70A1: 00         NOP                     
70A2: 07         RLCA                    
70A3: 00         NOP                     
70A4: 07         RLCA                    
70A5: 00         NOP                     
70A6: 1F         RRA                     
70A7: 00         NOP                     
70A8: 3F         CCF                     
70A9: 00         NOP                     
70AA: 7F         LD      A,A             
70AB: 00         NOP                     
70AC: 7F         LD      A,A             
70AD: 00         NOP                     
70AE: FF         RST     0X38            
70AF: 00         NOP                     
70B0: FF         RST     0X38            
70B1: 00         NOP                     
70B2: 7F         LD      A,A             
70B3: 00         NOP                     
70B4: 1F         RRA                     
70B5: 00         NOP                     
70B6: 3F         CCF                     
70B7: 00         NOP                     
70B8: 7F         LD      A,A             
70B9: 00         NOP                     
70BA: 7F         LD      A,A             
70BB: 00         NOP                     
70BC: 1F         RRA                     
70BD: 00         NOP                     
70BE: 1D         DEC     E               
70BF: 00         NOP                     
70C0: FF         RST     0X38            
70C1: 00         NOP                     
70C2: FF         RST     0X38            
70C3: 00         NOP                     
70C4: FF         RST     0X38            
70C5: 00         NOP                     
70C6: FF         RST     0X38            
70C7: 00         NOP                     
70C8: FF         RST     0X38            
70C9: 00         NOP                     
70CA: FF         RST     0X38            
70CB: 00         NOP                     
70CC: FF         RST     0X38            
70CD: 00         NOP                     
70CE: FF         RST     0X38            
70CF: 00         NOP                     
70D0: FF         RST     0X38            
70D1: 00         NOP                     
70D2: FF         RST     0X38            
70D3: 00         NOP                     
70D4: FF         RST     0X38            
70D5: 00         NOP                     
70D6: FF         RST     0X38            
70D7: 00         NOP                     
70D8: FF         RST     0X38            
70D9: 00         NOP                     
70DA: FC         ???                     
70DB: 00         NOP                     
70DC: E0 00      LDFF00  ($00),A         
70DE: C0         RET     NZ              
70DF: 00         NOP                     
70E0: 3C         INC     A               
70E1: 00         NOP                     
70E2: 7E         LD      A,(HL)          
70E3: 00         NOP                     
70E4: FF         RST     0X38            
70E5: 00         NOP                     
70E6: E7         RST     0X20            
70E7: 00         NOP                     
70E8: F0 00      LD      A,($00)         
70EA: F0 00      LD      A,($00)         
70EC: F8 00      LDHL    SP,$00          
70EE: F8 00      LDHL    SP,$00          
70F0: FE C0      CP      $C0             
70F2: FF         RST     0X38            
70F3: C0         RET     NZ              
70F4: FF         RST     0X38            
70F5: 80         ADD     A,B             
70F6: FF         RST     0X38            
70F7: 00         NOP                     
70F8: FF         RST     0X38            
70F9: 00         NOP                     
70FA: FF         RST     0X38            
70FB: 00         NOP                     
70FC: FF         RST     0X38            
70FD: 00         NOP                     
70FE: FE 00      CP      $00             
7100: 01 00 09   LD      BC,$0900        
7103: 00         NOP                     
7104: 1B         DEC     DE              
7105: 00         NOP                     
7106: 1F         RRA                     
7107: 00         NOP                     
7108: 3F         CCF                     
7109: 00         NOP                     
710A: 3F         CCF                     
710B: 00         NOP                     
710C: 3B         DEC     SP              
710D: 00         NOP                     
710E: 33         INC     SP              
710F: 00         NOP                     
7110: 31 00 11   LD      SP,$1100        
7113: 00         NOP                     
7114: 01 00 03   LD      BC,$0300        
7117: 00         NOP                     
7118: 03         INC     BC              
7119: 00         NOP                     
711A: 01 00 01   LD      BC,$0100        
711D: 00         NOP                     
711E: 01 00 00   LD      BC,$0000        
7121: 00         NOP                     
7122: 00         NOP                     
7123: 00         NOP                     
7124: 0F         RRCA                    
7125: 00         NOP                     
7126: 3F         CCF                     
7127: 00         NOP                     
7128: 7E         LD      A,(HL)          
7129: 00         NOP                     
712A: 1C         INC     E               
712B: 00         NOP                     
712C: 3F         CCF                     
712D: 00         NOP                     
712E: FF         RST     0X38            
712F: 00         NOP                     
7130: FF         RST     0X38            
7131: 00         NOP                     
7132: 3F         CCF                     
7133: 00         NOP                     
7134: 1C         INC     E               
7135: 00         NOP                     
7136: 7E         LD      A,(HL)          
7137: 00         NOP                     
7138: 3F         CCF                     
7139: 00         NOP                     
713A: 0F         RRCA                    
713B: 00         NOP                     
713C: 00         NOP                     
713D: 00         NOP                     
713E: 00         NOP                     
713F: 00         NOP                     
7140: 00         NOP                     
7141: 00         NOP                     
7142: 00         NOP                     
7143: 00         NOP                     
7144: 80         ADD     A,B             
7145: 00         NOP                     
7146: C0         RET     NZ              
7147: 00         NOP                     
7148: 00         NOP                     
7149: 00         NOP                     
714A: 00         NOP                     
714B: 00         NOP                     
714C: 18 00      JR      $714E           
714E: FF         RST     0X38            
714F: 00         NOP                     
7150: FF         RST     0X38            
7151: 00         NOP                     
7152: 18 00      JR      $7154           
7154: 00         NOP                     
7155: 00         NOP                     
7156: 00         NOP                     
7157: 00         NOP                     
7158: C0         RET     NZ              
7159: 00         NOP                     
715A: 80         ADD     A,B             
715B: 00         NOP                     
715C: 00         NOP                     
715D: 00         NOP                     
715E: 00         NOP                     
715F: 00         NOP                     
7160: 07         RLCA                    
7161: 00         NOP                     
7162: 03         INC     BC              
7163: 00         NOP                     
7164: 33         INC     SP              
7165: 00         NOP                     
7166: 3F         CCF                     
7167: 00         NOP                     
7168: 1F         RRA                     
7169: 00         NOP                     
716A: 9F         SBC     A               
716B: 00         NOP                     
716C: DF         RST     0X18            
716D: 00         NOP                     
716E: FF         RST     0X38            
716F: 00         NOP                     
7170: F7         RST     0X30            
7171: 00         NOP                     
7172: 70         LD      (HL),B          
7173: 00         NOP                     
7174: 78         LD      A,B             
7175: 00         NOP                     
7176: 3C         INC     A               
7177: 00         NOP                     
7178: 00         NOP                     
7179: 00         NOP                     
717A: 00         NOP                     
717B: 00         NOP                     
717C: 00         NOP                     
717D: 00         NOP                     
717E: 00         NOP                     
717F: 00         NOP                     
7180: 80         ADD     A,B             
7181: 00         NOP                     
7182: E0 00      LDFF00  ($00),A         
7184: F0 00      LD      A,($00)         
7186: F0 00      LD      A,($00)         
7188: 30 00      JR      NC,$718A        
718A: 90         SUB     B               
718B: 00         NOP                     
718C: 80         ADD     A,B             
718D: 00         NOP                     
718E: 80         ADD     A,B             
718F: 00         NOP                     
7190: C0         RET     NZ              
7191: 00         NOP                     
7192: F0 00      LD      A,($00)         
7194: 70         LD      (HL),B          
7195: 00         NOP                     
7196: 78         LD      A,B             
7197: 00         NOP                     
7198: 1C         INC     E               
7199: 00         NOP                     
719A: 0E 00      LD      C,$00           
719C: 07         RLCA                    
719D: 00         NOP                     
719E: 03         INC     BC              
719F: 00         NOP                     
71A0: 00         NOP                     
71A1: 00         NOP                     
71A2: 00         NOP                     
71A3: 00         NOP                     
71A4: 00         NOP                     
71A5: 00         NOP                     
71A6: 00         NOP                     
71A7: 00         NOP                     
71A8: 00         NOP                     
71A9: 00         NOP                     
71AA: 00         NOP                     
71AB: 00         NOP                     
71AC: 00         NOP                     
71AD: 00         NOP                     
71AE: FF         RST     0X38            
71AF: 00         NOP                     
71B0: FF         RST     0X38            
71B1: 00         NOP                     
71B2: 00         NOP                     
71B3: 00         NOP                     
71B4: 00         NOP                     
71B5: 00         NOP                     
71B6: 00         NOP                     
71B7: 00         NOP                     
71B8: 00         NOP                     
71B9: 00         NOP                     
71BA: 00         NOP                     
71BB: 00         NOP                     
71BC: 00         NOP                     
71BD: 00         NOP                     
71BE: 00         NOP                     
71BF: 00         NOP                     
71C0: 01 00 01   LD      BC,$0100        
71C3: 00         NOP                     
71C4: 01 00 01   LD      BC,$0100        
71C7: 00         NOP                     
71C8: 01 00 01   LD      BC,$0100        
71CB: 00         NOP                     
71CC: 01 00 01   LD      BC,$0100        
71CF: 00         NOP                     
71D0: 01 00 01   LD      BC,$0100        
71D3: 00         NOP                     
71D4: 01 00 01   LD      BC,$0100        
71D7: 00         NOP                     
71D8: 01 00 00   LD      BC,$0000        
71DB: 00         NOP                     
71DC: 00         NOP                     
71DD: 00         NOP                     
71DE: 00         NOP                     
71DF: 00         NOP                     
71E0: C0         RET     NZ              
71E1: 00         NOP                     
71E2: E0 00      LDFF00  ($00),A         
71E4: 70         LD      (HL),B          
71E5: 00         NOP                     
71E6: 38 00      JR      C,$71E8         
71E8: 1C         INC     E               
71E9: 00         NOP                     
71EA: 0C         INC     C               
71EB: 00         NOP                     
71EC: 00         NOP                     
71ED: 00         NOP                     
71EE: 00         NOP                     
71EF: 00         NOP                     
71F0: 00         NOP                     
71F1: 00         NOP                     
71F2: 00         NOP                     
71F3: 00         NOP                     
71F4: 00         NOP                     
71F5: 00         NOP                     
71F6: 00         NOP                     
71F7: 00         NOP                     
71F8: 00         NOP                     
71F9: 00         NOP                     
71FA: 00         NOP                     
71FB: 00         NOP                     
71FC: 00         NOP                     
71FD: 00         NOP                     
71FE: 00         NOP                     
71FF: 00         NOP                     
7200: 00         NOP                     
7201: 00         NOP                     
7202: 00         NOP                     
7203: 00         NOP                     
7204: 00         NOP                     
7205: 00         NOP                     
7206: 00         NOP                     
7207: 00         NOP                     
7208: 00         NOP                     
7209: 00         NOP                     
720A: 00         NOP                     
720B: 00         NOP                     
720C: 00         NOP                     
720D: 00         NOP                     
720E: 39         ADD     HL,SP           
720F: 00         NOP                     
7210: 7F         LD      A,A             
7211: 00         NOP                     
7212: 7F         LD      A,A             
7213: 00         NOP                     
7214: FF         RST     0X38            
7215: 00         NOP                     
7216: FF         RST     0X38            
7217: 00         NOP                     
7218: FF         RST     0X38            
7219: 00         NOP                     
721A: FF         RST     0X38            
721B: 00         NOP                     
721C: FF         RST     0X38            
721D: 00         NOP                     
721E: FF         RST     0X38            
721F: 00         NOP                     
7220: 00         NOP                     
7221: 00         NOP                     
7222: 00         NOP                     
7223: 00         NOP                     
7224: 3C         INC     A               
7225: 00         NOP                     
7226: 7E         LD      A,(HL)          
7227: 00         NOP                     
7228: 7E         LD      A,(HL)          
7229: 00         NOP                     
722A: FF         RST     0X38            
722B: 00         NOP                     
722C: FF         RST     0X38            
722D: 00         NOP                     
722E: FF         RST     0X38            
722F: 00         NOP                     
7230: FF         RST     0X38            
7231: 00         NOP                     
7232: FF         RST     0X38            
7233: 00         NOP                     
7234: FF         RST     0X38            
7235: 00         NOP                     
7236: FF         RST     0X38            
7237: 00         NOP                     
7238: FF         RST     0X38            
7239: 00         NOP                     
723A: FF         RST     0X38            
723B: 00         NOP                     
723C: FF         RST     0X38            
723D: 00         NOP                     
723E: FF         RST     0X38            
723F: 00         NOP                     
7240: 00         NOP                     
7241: 00         NOP                     
7242: 00         NOP                     
7243: 00         NOP                     
7244: 00         NOP                     
7245: 00         NOP                     
7246: 00         NOP                     
7247: 00         NOP                     
7248: 00         NOP                     
7249: 00         NOP                     
724A: 00         NOP                     
724B: 00         NOP                     
724C: 38 00      JR      C,$724E         
724E: 7C         LD      A,H             
724F: 00         NOP                     
7250: 7F         LD      A,A             
7251: 00         NOP                     
7252: FF         RST     0X38            
7253: 00         NOP                     
7254: FF         RST     0X38            
7255: 00         NOP                     
7256: FF         RST     0X38            
7257: 00         NOP                     
7258: FF         RST     0X38            
7259: 00         NOP                     
725A: FF         RST     0X38            
725B: 00         NOP                     
725C: FF         RST     0X38            
725D: 00         NOP                     
725E: FF         RST     0X38            
725F: 00         NOP                     
7260: 00         NOP                     
7261: 00         NOP                     
7262: 00         NOP                     
7263: 00         NOP                     
7264: 00         NOP                     
7265: 00         NOP                     
7266: 00         NOP                     
7267: 00         NOP                     
7268: 3C         INC     A               
7269: 00         NOP                     
726A: 7E         LD      A,(HL)          
726B: 00         NOP                     
726C: 7E         LD      A,(HL)          
726D: 00         NOP                     
726E: FF         RST     0X38            
726F: 00         NOP                     
7270: FF         RST     0X38            
7271: 00         NOP                     
7272: FF         RST     0X38            
7273: 00         NOP                     
7274: FF         RST     0X38            
7275: 00         NOP                     
7276: FF         RST     0X38            
7277: 00         NOP                     
7278: FF         RST     0X38            
7279: 00         NOP                     
727A: FF         RST     0X38            
727B: 00         NOP                     
727C: FF         RST     0X38            
727D: 00         NOP                     
727E: FF         RST     0X38            
727F: 00         NOP                     
7280: 00         NOP                     
7281: 00         NOP                     
7282: 00         NOP                     
7283: 00         NOP                     
7284: 00         NOP                     
7285: 00         NOP                     
7286: 00         NOP                     
7287: 00         NOP                     
7288: 38 00      JR      C,$728A         
728A: 7E         LD      A,(HL)          
728B: 00         NOP                     
728C: 7F         LD      A,A             
728D: 00         NOP                     
728E: FF         RST     0X38            
728F: 00         NOP                     
7290: FF         RST     0X38            
7291: 00         NOP                     
7292: FF         RST     0X38            
7293: 00         NOP                     
7294: FF         RST     0X38            
7295: 00         NOP                     
7296: FF         RST     0X38            
7297: 00         NOP                     
7298: FF         RST     0X38            
7299: 00         NOP                     
729A: FF         RST     0X38            
729B: 00         NOP                     
729C: FF         RST     0X38            
729D: 00         NOP                     
729E: FF         RST     0X38            
729F: 00         NOP                     
72A0: 00         NOP                     
72A1: 00         NOP                     
72A2: 00         NOP                     
72A3: 00         NOP                     
72A4: 00         NOP                     
72A5: 00         NOP                     
72A6: 00         NOP                     
72A7: 00         NOP                     
72A8: 00         NOP                     
72A9: 00         NOP                     
72AA: 3C         INC     A               
72AB: 00         NOP                     
72AC: 7E         LD      A,(HL)          
72AD: 00         NOP                     
72AE: FF         RST     0X38            
72AF: 00         NOP                     
72B0: FF         RST     0X38            
72B1: 00         NOP                     
72B2: FF         RST     0X38            
72B3: 00         NOP                     
72B4: FF         RST     0X38            
72B5: 00         NOP                     
72B6: FF         RST     0X38            
72B7: 00         NOP                     
72B8: FF         RST     0X38            
72B9: 00         NOP                     
72BA: FF         RST     0X38            
72BB: 00         NOP                     
72BC: FF         RST     0X38            
72BD: 00         NOP                     
72BE: FF         RST     0X38            
72BF: 00         NOP                     
72C0: FF         RST     0X38            
72C1: 00         NOP                     
72C2: FF         RST     0X38            
72C3: 00         NOP                     
72C4: FF         RST     0X38            
72C5: 00         NOP                     
72C6: FF         RST     0X38            
72C7: 00         NOP                     
72C8: FF         RST     0X38            
72C9: 00         NOP                     
72CA: FF         RST     0X38            
72CB: 00         NOP                     
72CC: 7F         LD      A,A             
72CD: 00         NOP                     
72CE: 7F         LD      A,A             
72CF: 00         NOP                     
72D0: 7F         LD      A,A             
72D1: 00         NOP                     
72D2: 3F         CCF                     
72D3: 00         NOP                     
72D4: 3F         CCF                     
72D5: 00         NOP                     
72D6: 1F         RRA                     
72D7: 00         NOP                     
72D8: 0F         RRCA                    
72D9: 00         NOP                     
72DA: 03         INC     BC              
72DB: 00         NOP                     
72DC: 00         NOP                     
72DD: 00         NOP                     
72DE: 00         NOP                     
72DF: 00         NOP                     
72E0: FF         RST     0X38            
72E1: 00         NOP                     
72E2: FF         RST     0X38            
72E3: 00         NOP                     
72E4: FF         RST     0X38            
72E5: 00         NOP                     
72E6: FF         RST     0X38            
72E7: 00         NOP                     
72E8: FF         RST     0X38            
72E9: 00         NOP                     
72EA: FF         RST     0X38            
72EB: 00         NOP                     
72EC: FF         RST     0X38            
72ED: 00         NOP                     
72EE: FF         RST     0X38            
72EF: 00         NOP                     
72F0: FF         RST     0X38            
72F1: 00         NOP                     
72F2: FF         RST     0X38            
72F3: 00         NOP                     
72F4: FF         RST     0X38            
72F5: 00         NOP                     
72F6: FF         RST     0X38            
72F7: 00         NOP                     
72F8: FF         RST     0X38            
72F9: 00         NOP                     
72FA: FF         RST     0X38            
72FB: 00         NOP                     
72FC: 00         NOP                     
72FD: 00         NOP                     
72FE: 00         NOP                     
72FF: 00         NOP                     
7300: FF         RST     0X38            
7301: 00         NOP                     
7302: FF         RST     0X38            
7303: 00         NOP                     
7304: FF         RST     0X38            
7305: 00         NOP                     
7306: FF         RST     0X38            
7307: 00         NOP                     
7308: FF         RST     0X38            
7309: 00         NOP                     
730A: FF         RST     0X38            
730B: 00         NOP                     
730C: 7F         LD      A,A             
730D: 00         NOP                     
730E: 78         LD      A,B             
730F: 07         RLCA                    
7310: 7C         LD      A,H             
7311: 03         INC     BC              
7312: 3F         CCF                     
7313: 00         NOP                     
7314: 3F         CCF                     
7315: 00         NOP                     
7316: 1F         RRA                     
7317: 00         NOP                     
7318: 07         RLCA                    
7319: 00         NOP                     
731A: 01 00 00   LD      BC,$0000        
731D: 00         NOP                     
731E: 00         NOP                     
731F: 00         NOP                     
7320: FF         RST     0X38            
7321: 00         NOP                     
7322: FF         RST     0X38            
7323: 00         NOP                     
7324: FF         RST     0X38            
7325: 00         NOP                     
7326: FF         RST     0X38            
7327: 00         NOP                     
7328: FF         RST     0X38            
7329: 00         NOP                     
732A: FF         RST     0X38            
732B: 00         NOP                     
732C: FF         RST     0X38            
732D: 00         NOP                     
732E: 66         LD      H,(HL)          
732F: 99         SBC     C               
7330: FF         RST     0X38            
7331: 81         ADD     A,C             
7332: 7E         LD      A,(HL)          
7333: 81         ADD     A,C             
7334: FF         RST     0X38            
7335: 00         NOP                     
7336: FF         RST     0X38            
7337: 00         NOP                     
7338: FF         RST     0X38            
7339: 00         NOP                     
733A: FF         RST     0X38            
733B: 00         NOP                     
733C: 00         NOP                     
733D: 00         NOP                     
733E: 00         NOP                     
733F: 00         NOP                     
7340: FF         RST     0X38            
7341: 00         NOP                     
7342: FF         RST     0X38            
7343: 00         NOP                     
7344: FF         RST     0X38            
7345: 00         NOP                     
7346: FF         RST     0X38            
7347: 00         NOP                     
7348: FF         RST     0X38            
7349: 00         NOP                     
734A: FE 01      CP      $01             
734C: 7D         LD      A,L             
734D: 03         INC     BC              
734E: 7B         LD      A,E             
734F: 07         RLCA                    
7350: 79         LD      A,C             
7351: 07         RLCA                    
7352: 3C         INC     A               
7353: 03         INC     BC              
7354: 3E 01      LD      A,$01           
7356: 1F         RRA                     
7357: 00         NOP                     
7358: 07         RLCA                    
7359: 00         NOP                     
735A: 01 00 00   LD      BC,$0000        
735D: 00         NOP                     
735E: 00         NOP                     
735F: 00         NOP                     
7360: FF         RST     0X38            
7361: 00         NOP                     
7362: FF         RST     0X38            
7363: 00         NOP                     
7364: FF         RST     0X38            
7365: 00         NOP                     
7366: FF         RST     0X38            
7367: 00         NOP                     
7368: BD         CP      L               
7369: 7E         LD      A,(HL)          
736A: FF         RST     0X38            
736B: FF         RST     0X38            
736C: BD         CP      L               
736D: C3 E7 99   JP      $99E7           
7370: FF         RST     0X38            
7371: 81         ADD     A,C             
7372: 7E         LD      A,(HL)          
7373: 81         ADD     A,C             
7374: 7E         LD      A,(HL)          
7375: 81         ADD     A,C             
7376: BD         CP      L               
7377: 42         LD      B,D             
7378: FF         RST     0X38            
7379: 00         NOP                     
737A: FF         RST     0X38            
737B: 00         NOP                     
737C: 00         NOP                     
737D: 00         NOP                     
737E: 00         NOP                     
737F: 00         NOP                     
7380: FF         RST     0X38            
7381: 00         NOP                     
7382: FF         RST     0X38            
7383: 00         NOP                     
7384: FE 01      CP      $01             
7386: FD         ???                     
7387: 03         INC     BC              
7388: FF         RST     0X38            
7389: 03         INC     BC              
738A: FB         EI                      
738B: 07         RLCA                    
738C: 7B         LD      A,E             
738D: 07         RLCA                    
738E: 7B         LD      A,E             
738F: 07         RLCA                    
7390: 79         LD      A,C             
7391: 07         RLCA                    
7392: 3C         INC     A               
7393: 03         INC     BC              
7394: 3C         INC     A               
7395: 03         INC     BC              
7396: 1E 01      LD      E,$01           
7398: 0F         RRCA                    
7399: 00         NOP                     
739A: 03         INC     BC              
739B: 00         NOP                     
739C: 00         NOP                     
739D: 00         NOP                     
739E: 00         NOP                     
739F: 00         NOP                     
73A0: FF         RST     0X38            
73A1: 00         NOP                     
73A2: 81         ADD     A,C             
73A3: 7E         LD      A,(HL)          
73A4: FF         RST     0X38            
73A5: FF         RST     0X38            
73A6: FF         RST     0X38            
73A7: FF         RST     0X38            
73A8: FF         RST     0X38            
73A9: FF         RST     0X38            
73AA: FF         RST     0X38            
73AB: FF         RST     0X38            
73AC: BD         CP      L               
73AD: C3 E7 99   JP      $99E7           
73B0: FF         RST     0X38            
73B1: 81         ADD     A,C             
73B2: FF         RST     0X38            
73B3: 81         ADD     A,C             
73B4: 7E         LD      A,(HL)          
73B5: 81         ADD     A,C             
73B6: 3C         INC     A               
73B7: C3 80 7F   JP      $7F80           
73BA: FF         RST     0X38            
73BB: 00         NOP                     
73BC: 00         NOP                     
73BD: 00         NOP                     
73BE: 00         NOP                     
73BF: 00         NOP                     
73C0: C1         POP     BC              
73C1: 00         NOP                     
73C2: E3         ???                     
73C3: 00         NOP                     
73C4: 7F         LD      A,A             
73C5: 00         NOP                     
73C6: 3F         CCF                     
73C7: 00         NOP                     
73C8: 3C         INC     A               
73C9: 03         INC     BC              
73CA: 38 07      JR      C,$73D3         
73CC: 71         LD      (HL),C          
73CD: 0F         RRCA                    
73CE: F3         DI                      
73CF: 0F         RRCA                    
73D0: F3         DI                      
73D1: 0F         RRCA                    
73D2: 71         LD      (HL),C          
73D3: 0F         RRCA                    
73D4: 38 07      JR      C,$73DD         
73D6: 3C         INC     A               
73D7: 03         INC     BC              
73D8: 3F         CCF                     
73D9: 00         NOP                     
73DA: 7F         LD      A,A             
73DB: 00         NOP                     
73DC: E3         ???                     
73DD: 00         NOP                     
73DE: C1         POP     BC              
73DF: 00         NOP                     
73E0: FF         RST     0X38            
73E1: 00         NOP                     
73E2: FD         ???                     
73E3: F6 0F      OR      $0F             
73E5: F0 FD      LD      A,($FD)         
73E7: 06 FD      LD      B,$FD           
73E9: 06 FD      LD      B,$FD           
73EB: F6 09      OR      $09             
73ED: F6 FF      OR      $FF             
73EF: 00         NOP                     
73F0: FF         RST     0X38            
73F1: 00         NOP                     
73F2: FD         ???                     
73F3: F6 0F      OR      $0F             
73F5: F0 FD      LD      A,($FD)         
73F7: 06 FD      LD      B,$FD           
73F9: 06 FD      LD      B,$FD           
73FB: F6 09      OR      $09             
73FD: F6 FF      OR      $FF             
73FF: 00         NOP                     
7400: 3F         CCF                     
7401: 00         NOP                     
7402: 7F         LD      A,A             
7403: 3B         DEC     SP              
7404: BF         CP      A               
7405: 7B         LD      A,E             
7406: AF         XOR     A               
7407: 70         LD      (HL),B          
7408: BE         CP      (HL)            
7409: 61         LD      H,C             
740A: BE         CP      (HL)            
740B: 61         LD      H,C             
740C: BF         CP      A               
740D: 60         LD      H,B             
740E: BB         CP      E               
740F: 67         LD      H,A             
7410: F7         RST     0X30            
7411: 2F         CPL                     
7412: BB         CP      E               
7413: 4C         LD      C,H             
7414: BF         CP      A               
7415: 68         LD      L,B             
7416: BF         CP      A               
7417: 68         LD      L,B             
7418: BF         CP      A               
7419: 68         LD      L,B             
741A: 57         LD      D,A             
741B: 2C         INC     L               
741C: 2B         DEC     HL              
741D: 17         RLA                     
741E: 1F         RRA                     
741F: 00         NOP                     
7420: 3F         CCF                     
7421: 00         NOP                     
7422: 7F         LD      A,A             
7423: 3B         DEC     SP              
7424: BF         CP      A               
7425: 7B         LD      A,E             
7426: AF         XOR     A               
7427: 70         LD      (HL),B          
7428: BF         CP      A               
7429: 60         LD      H,B             
742A: BB         CP      E               
742B: 67         LD      H,A             
742C: B7         OR      A               
742D: 6F         LD      L,A             
742E: BB         CP      E               
742F: 6C         LD      L,H             
7430: FF         RST     0X38            
7431: 28 BF      JR      Z,$73F2         
7433: 48         LD      C,B             
7434: BF         CP      A               
7435: 68         LD      L,B             
7436: B7         OR      A               
7437: 6C         LD      L,H             
7438: BB         CP      E               
7439: 67         LD      H,A             
743A: 5F         LD      E,A             
743B: 20 20      JR      NZ,$745D        
743D: 1F         RRA                     
743E: 1F         RRA                     
743F: 00         NOP                     
7440: 19         ADD     HL,DE           
7441: 00         NOP                     
7442: 16 09      LD      D,$09           
7444: 13         INC     DE              
7445: 0D         DEC     C               
7446: 15         DEC     D               
7447: 0F         RRCA                    
7448: 6F         LD      L,A             
7449: 1F         RRA                     
744A: AC         XOR     H               
744B: 5F         LD      E,A             
744C: C9         RET                     
744D: 7E         LD      A,(HL)          
744E: DD         ???                     
744F: 7A         LD      A,D             
7450: D7         RST     0X10            
7451: 78         LD      A,B             
7452: B7         OR      A               
7453: 78         LD      A,B             
7454: B7         OR      A               
7455: 78         LD      A,B             
7456: 5B         LD      E,E             
7457: 3C         INC     A               
7458: 4C         LD      C,H             
7459: 3F         CCF                     
745A: 27         DAA                     
745B: 1F         RRA                     
745C: 18 07      JR      $7465           
745E: 07         RLCA                    
745F: 00         NOP                     
7460: 00         NOP                     
7461: 00         NOP                     
7462: 01 00 02   LD      BC,$0200        
7465: 01 03 01   LD      BC,$0103        
7468: 05         DEC     B               
7469: 03         INC     BC              
746A: 15         DEC     D               
746B: 03         INC     BC              
746C: 2B         DEC     HL              
746D: 17         RLA                     
746E: 27         DAA                     
746F: 1F         RRA                     
7470: 36 1F      LD      (HL),$1F        
7472: 3E 1D      LD      A,$1D           
7474: 2F         CPL                     
7475: 1C         INC     E               
7476: 1D         DEC     E               
7477: 0E 16      LD      C,$16           
7479: 0F         RRCA                    
747A: 09         ADD     HL,BC           
747B: 07         RLCA                    
747C: 06 01      LD      B,$01           
747E: 01 00 00   LD      BC,$0000        
7481: 00         NOP                     
7482: 00         NOP                     
7483: 00         NOP                     
7484: 00         NOP                     
7485: 00         NOP                     
7486: 00         NOP                     
7487: 00         NOP                     
7488: 01 00 03   LD      BC,$0300        
748B: 01 05 03   LD      BC,$0305        
748E: 07         RLCA                    
748F: 03         INC     BC              
7490: 0A         LD      A,(BC)          
7491: 07         RLCA                    
7492: 0B         DEC     BC              
7493: 06 0A      LD      B,$0A           
7495: 07         RLCA                    
7496: 05         DEC     B               
7497: 03         INC     BC              
7498: 03         INC     BC              
7499: 00         NOP                     
749A: 00         NOP                     
749B: 00         NOP                     
749C: 00         NOP                     
749D: 00         NOP                     
749E: 00         NOP                     
749F: 00         NOP                     
74A0: 00         NOP                     
74A1: 00         NOP                     
74A2: 06 00      LD      B,$00           
74A4: 09         ADD     HL,BC           
74A5: 06 16      LD      B,$16           
74A7: 0D         DEC     C               
74A8: 2D         DEC     L               
74A9: 1F         RRA                     
74AA: 2E 1F      LD      L,$1F           
74AC: 59         LD      E,C             
74AD: 3E 5B      LD      A,$5B           
74AF: 3C         INC     A               
74B0: AC         XOR     H               
74B1: 73         LD      (HL),E          
74B2: AF         XOR     A               
74B3: 70         LD      (HL),B          
74B4: AF         XOR     A               
74B5: 70         LD      (HL),B          
74B6: B7         OR      A               
74B7: 78         LD      A,B             
74B8: 5C         LD      E,H             
74B9: 3F         CCF                     
74BA: 47         LD      B,A             
74BB: 3F         CCF                     
74BC: 30 0F      JR      NC,$74CD        
74BE: 0F         RRCA                    
74BF: 00         NOP                     
74C0: 37         SCF                     
74C1: 00         NOP                     
74C2: CB 36      SET     1,E             
74C4: 3D         DEC     A               
74C5: EE DE      XOR     $DE             
74C7: FC         ???                     
74C8: FF         RST     0X38            
74C9: FC         ???                     
74CA: 19         ADD     HL,DE           
74CB: FE 8D      CP      $8D             
74CD: 7E         LD      A,(HL)          
74CE: 2A         LD      A,(HLI)         
74CF: DC D6 38   CALL    C,$38D6         
74D2: BA         CP      D               
74D3: 74         LD      (HL),H          
74D4: BA         CP      D               
74D5: 7C         LD      A,H             
74D6: 74         LD      (HL),H          
74D7: F8 F4      LDHL    SP,$F4          
74D9: F8 C8      LDHL    SP,$C8          
74DB: F0 30      LD      A,($30)         
74DD: C0         RET     NZ              
74DE: C0         RET     NZ              
74DF: 00         NOP                     
74E0: 00         NOP                     
74E1: FF         RST     0X38            
74E2: 00         NOP                     
74E3: FF         RST     0X38            
74E4: 22         LD      (HLI),A         
74E5: FF         RST     0X38            
74E6: 14         INC     D               
74E7: FF         RST     0X38            
74E8: 08 FF 14   LD      ($14FF),SP      
74EB: FF         RST     0X38            
74EC: 22         LD      (HLI),A         
74ED: FF         RST     0X38            
74EE: 00         NOP                     
74EF: FF         RST     0X38            
74F0: 00         NOP                     
74F1: FF         RST     0X38            
74F2: 00         NOP                     
74F3: FF         RST     0X38            
74F4: 22         LD      (HLI),A         
74F5: FF         RST     0X38            
74F6: 14         INC     D               
74F7: FF         RST     0X38            
74F8: 08 FF 14   LD      ($14FF),SP      
74FB: FF         RST     0X38            
74FC: 22         LD      (HLI),A         
74FD: FF         RST     0X38            
74FE: 00         NOP                     
74FF: FF         RST     0X38            
7500: 03         INC     BC              
7501: 00         NOP                     
7502: 07         RLCA                    
7503: 00         NOP                     
7504: 07         RLCA                    
7505: 03         INC     BC              
7506: 1F         RRA                     
7507: 04         INC     B               
7508: 3D         DEC     A               
7509: 13         INC     DE              
750A: 39         ADD     HL,SP           
750B: 17         RLA                     
750C: 3A         LD      A,(HLD)         
750D: 15         DEC     D               
750E: 2C         INC     L               
750F: 13         INC     DE              
7510: 1C         INC     E               
7511: 03         INC     BC              
7512: 14         INC     D               
7513: 0B         DEC     BC              
7514: 34         INC     (HL)            
7515: 1B         DEC     DE              
7516: 3B         DEC     SP              
7517: 14         INC     D               
7518: 17         RLA                     
7519: 0F         RRCA                    
751A: 18 07      JR      $7523           
751C: 1F         RRA                     
751D: 00         NOP                     
751E: 0F         RRCA                    
751F: 00         NOP                     
7520: 80         ADD     A,B             
7521: 00         NOP                     
7522: C0         RET     NZ              
7523: 00         NOP                     
7524: E0 C0      LDFF00  ($C0),A         
7526: F8 20      LDHL    SP,$20          
7528: BC         CP      H               
7529: C8         RET     Z               
752A: 9C         SBC     H               
752B: E8 9C      ADD     SP,$9C          
752D: E8 94      ADD     SP,$94          
752F: E8 38      ADD     SP,$38          
7531: C0         RET     NZ              
7532: 54         LD      D,H             
7533: A8         XOR     B               
7534: 94         SUB     H               
7535: 68         LD      L,B             
7536: 2C         INC     L               
7537: F0 C8      LD      A,($C8)         
7539: F0 38      LD      A,($38)         
753B: C0         RET     NZ              
753C: FC         ???                     
753D: 30 F8      JR      NC,$7537        
753F: 00         NOP                     
7540: 07         RLCA                    
7541: 00         NOP                     
7542: 0B         DEC     BC              
7543: 04         INC     B               
7544: 1F         RRA                     
7545: 00         NOP                     
7546: 3F         CCF                     
7547: 11 3F 15   LD      DE,$153F        
754A: 6F         LD      L,A             
754B: 1F         RRA                     
754C: FF         RST     0X38            
754D: 6E         LD      L,(HL)          
754E: FF         RST     0X38            
754F: 66         LD      H,(HL)          
7550: 6B         LD      L,E             
7551: 16 25      LD      D,$25           
7553: 1B         DEC     DE              
7554: 1B         DEC     DE              
7555: 04         INC     B               
7556: 38 07      JR      C,$755F         
7558: 3F         CCF                     
7559: 18 3F      JR      $759A           
755B: 1C         INC     E               
755C: 1F         RRA                     
755D: 0C         INC     C               
755E: 0C         INC     C               
755F: 00         NOP                     
7560: 00         NOP                     
7561: 00         NOP                     
7562: 01 00 1F   LD      BC,$1F00        
7565: 00         NOP                     
7566: 3D         DEC     A               
7567: 1A         LD      A,(DE)          
7568: 3B         DEC     SP              
7569: 17         RLA                     
756A: 3F         CCF                     
756B: 06 2F      LD      B,$2F           
756D: 14         INC     D               
756E: 2F         CPL                     
756F: 14         INC     D               
7570: 3B         DEC     SP              
7571: 07         RLCA                    
7572: 65         LD      H,L             
7573: 1B         DEC     DE              
7574: E3         ???                     
7575: 5C         LD      E,H             
7576: F1         POP     AF              
7577: 6E         LD      L,(HL)          
7578: FB         EI                      
7579: 65         LD      H,L             
757A: 7F         LD      A,A             
757B: 23         INC     HL              
757C: 37         SCF                     
757D: 03         INC     BC              
757E: 03         INC     BC              
757F: 00         NOP                     
7580: F0 00      LD      A,($00)         
7582: F8 00      LDHL    SP,$00          
7584: FC         ???                     
7585: 08 FE 8C   LD      ($8CFE),SP      
7588: FE C4      CP      $C4             
758A: FF         RST     0X38            
758B: 80         ADD     A,B             
758C: FD         ???                     
758D: EE FA      XOR     $FA             
758F: FC         ???                     
7590: FE E0      CP      $E0             
7592: DF         RST     0X18            
7593: E6 EF      AND     $EF             
7595: 16 8E      LD      D,$8E           
7597: 70         LD      (HL),B          
7598: F0 80      LD      A,($80)         
759A: E0 80      LDFF00  ($80),A         
759C: C0         RET     NZ              
759D: 00         NOP                     
759E: 80         ADD     A,B             
759F: 00         NOP                     
75A0: 00         NOP                     
75A1: 00         NOP                     
75A2: 3B         DEC     SP              
75A3: 00         NOP                     
75A4: 7D         LD      A,L             
75A5: 32         LD      (HLD),A         
75A6: FB         EI                      
75A7: 75         LD      (HL),L          
75A8: FF         RST     0X38            
75A9: 62         LD      H,D             
75AA: EF         RST     0X28            
75AB: 14         INC     D               
75AC: 6F         LD      L,A             
75AD: 14         INC     D               
75AE: 6B         LD      L,E             
75AF: 17         RLA                     
75B0: 65         LD      H,L             
75B1: 1B         DEC     DE              
75B2: 66         LD      H,(HL)          
75B3: 19         ADD     HL,DE           
75B4: F9         LD      SP,HL           
75B5: 66         LD      H,(HL)          
75B6: FD         ???                     
75B7: 7A         LD      A,D             
75B8: 7F         LD      A,A             
75B9: 38 38      JR      C,$75F3         
75BB: 00         NOP                     
75BC: 00         NOP                     
75BD: 00         NOP                     
75BE: 00         NOP                     
75BF: 00         NOP                     
75C0: C0         RET     NZ              
75C1: 00         NOP                     
75C2: EC         ???                     
75C3: C0         RET     NZ              
75C4: FE 00      CP      $00             
75C6: FE E0      CP      $E0             
75C8: FF         RST     0X38            
75C9: 40         LD      B,B             
75CA: FF         RST     0X38            
75CB: 70         LD      (HL),B          
75CC: FF         RST     0X38            
75CD: F2         ???                     
75CE: FF         RST     0X38            
75CF: C6 FF      ADD     $FF             
75D1: EC         ???                     
75D2: FD         ???                     
75D3: CA F9 36   JP      Z,$36F9         
75D6: FE D8      CP      $D8             
75D8: FC         ???                     
75D9: C0         RET     NZ              
75DA: C8         RET     Z               
75DB: 30 30      JR      NC,$760D        
75DD: 00         NOP                     
75DE: 00         NOP                     
75DF: 00         NOP                     
75E0: 03         INC     BC              
75E1: 00         NOP                     
75E2: 07         RLCA                    
75E3: 03         INC     BC              
75E4: 0F         RRCA                    
75E5: 00         NOP                     
75E6: 7A         LD      A,D             
75E7: 07         RLCA                    
75E8: F4         ???                     
75E9: 6F         LD      L,A             
75EA: F9         LD      SP,HL           
75EB: 76         HALT                    
75EC: 7B         LD      A,E             
75ED: 35         DEC     (HL)            
75EE: 3F         CCF                     
75EF: 03         INC     BC              
75F0: 17         RLA                     
75F1: 0B         DEC     BC              
75F2: 17         RLA                     
75F3: 0A         LD      A,(BC)          
75F4: 1F         RRA                     
75F5: 02         LD      (BC),A          
75F6: 3D         DEC     A               
75F7: 1B         DEC     DE              
75F8: 3F         CCF                     
75F9: 19         ADD     HL,DE           
75FA: 1F         RRA                     
75FB: 00         NOP                     
75FC: 02         LD      (BC),A          
75FD: 01 01 00   LD      BC,$0001        
7600: C0         RET     NZ              
7601: 00         NOP                     
7602: E0 C0      LDFF00  ($C0),A         
7604: E0 00      LDFF00  ($00),A         
7606: BC         CP      H               
7607: 40         LD      B,B             
7608: FE 0C      CP      $0C             
760A: FE CC      CP      $CC             
760C: FC         ???                     
760D: 80         ADD     A,B             
760E: FE 08      CP      $08             
7610: FD         ???                     
7611: 1A         LD      A,(DE)          
7612: F1         POP     AF              
7613: 3E B5      LD      A,$B5           
7615: 6E         LD      L,(HL)          
7616: A5         AND     L               
7617: 5E         LD      E,(HL)          
7618: CA 3C 82   JP      Z,$823C         
761B: 7C         LD      A,H             
761C: 0C         INC     C               
761D: F0 F0      LD      A,($F0)         
761F: 00         NOP                     
7620: 0C         INC     C               
7621: 00         NOP                     
7622: 1F         RRA                     
7623: 0C         INC     C               
7624: 3F         CCF                     
7625: 1C         INC     E               
7626: 3C         INC     A               
7627: 1B         DEC     DE              
7628: 19         ADD     HL,DE           
7629: 07         RLCA                    
762A: 2F         CPL                     
762B: 10 4B      STOP    $4B             
762D: 37         SCF                     
762E: 77         LD      (HL),A          
762F: 0C         INC     C               
7630: FF         RST     0X38            
7631: 68         LD      L,B             
7632: FB         EI                      
7633: 57         LD      D,A             
7634: 7E         LD      A,(HL)          
7635: 11 30 0F   LD      DE,$0F30        
7638: 11 0F 08   LD      DE,$080F        
763B: 07         RLCA                    
763C: 04         INC     B               
763D: 03         INC     BC              
763E: 03         INC     BC              
763F: 00         NOP                     
7640: 03         INC     BC              
7641: 00         NOP                     
7642: 07         RLCA                    
7643: 00         NOP                     
7644: 07         RLCA                    
7645: 03         INC     BC              
7646: 1F         RRA                     
7647: 04         INC     B               
7648: 3D         DEC     A               
7649: 13         INC     DE              
764A: 39         ADD     HL,SP           
764B: 17         RLA                     
764C: 3A         LD      A,(HLD)         
764D: 15         DEC     D               
764E: 2C         INC     L               
764F: 13         INC     DE              
7650: 1C         INC     E               
7651: 03         INC     BC              
7652: 2C         INC     L               
7653: 13         INC     DE              
7654: 6C         LD      L,H             
7655: 33         INC     SP              
7656: 73         LD      (HL),E          
7657: 2C         INC     L               
7658: 37         SCF                     
7659: 0F         RRCA                    
765A: 18 07      JR      $7663           
765C: 3F         CCF                     
765D: 18 3F      JR      $769E           
765F: 00         NOP                     
7660: 80         ADD     A,B             
7661: 00         NOP                     
7662: C0         RET     NZ              
7663: 00         NOP                     
7664: E0 C0      LDFF00  ($C0),A         
7666: F8 20      LDHL    SP,$20          
7668: BC         CP      H               
7669: C8         RET     Z               
766A: 9C         SBC     H               
766B: E8 9C      ADD     SP,$9C          
766D: E8 94      ADD     SP,$94          
766F: E8 38      ADD     SP,$38          
7671: C0         RET     NZ              
7672: 54         LD      D,H             
7673: A8         XOR     B               
7674: 96         SUB     (HL)            
7675: 6C         LD      L,H             
7676: 0E F4      LD      C,$F4           
7678: EC         ???                     
7679: F0 18      LD      A,($18)         
767B: E0 FC      LDFF00  ($FC),A         
767D: 18 FC      JR      $767B           
767F: 00         NOP                     
7680: 07         RLCA                    
7681: 00         NOP                     
7682: 0B         DEC     BC              
7683: 07         RLCA                    
7684: 1B         DEC     DE              
7685: 04         INC     B               
7686: 3F         CCF                     
7687: 13         INC     DE              
7688: 3F         CCF                     
7689: 14         INC     D               
768A: 3F         CCF                     
768B: 10 27      STOP    $27             
768D: 18 1F      JR      $76AE           
768F: 0D         DEC     C               
7690: 17         RLA                     
7691: 0D         DEC     C               
7692: 2B         DEC     HL              
7693: 17         RLA                     
7694: 6F         LD      L,A             
7695: 30 78      JR      NC,$770F        
7697: 27         DAA                     
7698: 37         SCF                     
7699: 0F         RRCA                    
769A: 1C         INC     E               
769B: 03         INC     BC              
769C: 3B         DEC     SP              
769D: 1C         INC     E               
769E: 3F         CCF                     
769F: 00         NOP                     
76A0: C0         RET     NZ              
76A1: 00         NOP                     
76A2: 20 C0      JR      NZ,$7664        
76A4: 18 E0      JR      $7686           
76A6: DC E8 FC   CALL    C,$FCE8         
76A9: 28 FC      JR      Z,$76A7         
76AB: 08 E4 18   LD      ($18E4),SP      
76AE: F8 B0      LDHL    SP,$B0          
76B0: E8 B0      ADD     SP,$B0          
76B2: D4 E8 F6   CALL    NC,$F6E8        
76B5: 0C         INC     C               
76B6: 1E E4      LD      E,$E4           
76B8: EC         ???                     
76B9: F0 38      LD      A,($38)         
76BB: C0         RET     NZ              
76BC: DC 38 FC   CALL    C,$FC38         
76BF: 00         NOP                     
76C0: 1B         DEC     DE              
76C1: 00         NOP                     
76C2: 3D         DEC     A               
76C3: 1B         DEC     DE              
76C4: 3F         CCF                     
76C5: 18 3F      JR      $7706           
76C7: 00         NOP                     
76C8: 2F         CPL                     
76C9: 11 2F 15   LD      DE,$152F        
76CC: 2F         CPL                     
76CD: 17         RLA                     
76CE: 2B         DEC     HL              
76CF: 16 2B      LD      D,$2B           
76D1: 16 15      LD      D,$15           
76D3: 0B         DEC     BC              
76D4: 1B         DEC     DE              
76D5: 04         INC     B               
76D6: 18 0F      JR      $76E7           
76D8: 27         DAA                     
76D9: 1F         RRA                     
76DA: 78         LD      A,B             
76DB: 27         DAA                     
76DC: F7         RST     0X30            
76DD: 78         LD      A,B             
76DE: 7F         LD      A,A             
76DF: 00         NOP                     
76E0: 00         NOP                     
76E1: FF         RST     0X38            
76E2: 00         NOP                     
76E3: FF         RST     0X38            
76E4: 22         LD      (HLI),A         
76E5: FF         RST     0X38            
76E6: 14         INC     D               
76E7: FF         RST     0X38            
76E8: 08 FF 14   LD      ($14FF),SP      
76EB: FF         RST     0X38            
76EC: 22         LD      (HLI),A         
76ED: FF         RST     0X38            
76EE: 00         NOP                     
76EF: FF         RST     0X38            
76F0: 00         NOP                     
76F1: FF         RST     0X38            
76F2: 00         NOP                     
76F3: FF         RST     0X38            
76F4: 22         LD      (HLI),A         
76F5: FF         RST     0X38            
76F6: 14         INC     D               
76F7: FF         RST     0X38            
76F8: 08 FF 14   LD      ($14FF),SP      
76FB: FF         RST     0X38            
76FC: 22         LD      (HLI),A         
76FD: FF         RST     0X38            
76FE: 00         NOP                     
76FF: FF         RST     0X38            
7700: 03         INC     BC              
7701: 03         INC     BC              
7702: 07         RLCA                    
7703: 04         INC     B               
7704: 0E 09      LD      C,$09           
7706: 1D         DEC     E               
7707: 1B         DEC     DE              
7708: 2D         DEC     L               
7709: 3B         DEC     SP              
770A: 2F         CPL                     
770B: 39         ADD     HL,SP           
770C: 4A         LD      C,D             
770D: 7C         LD      A,H             
770E: 45         LD      B,L             
770F: 7E         LD      A,(HL)          
7710: 63         LD      H,E             
7711: 7F         LD      A,A             
7712: 63         LD      H,E             
7713: 7C         LD      A,H             
7714: 51         LD      D,C             
7715: 7E         LD      A,(HL)          
7716: 5C         LD      E,H             
7717: 6F         LD      L,A             
7718: 3F         CCF                     
7719: 23         INC     HL              
771A: 2F         CPL                     
771B: 30 1B      JR      NC,$7738        
771D: 1C         INC     E               
771E: 07         RLCA                    
771F: 07         RLCA                    
7720: E0 E0      LDFF00  ($E0),A         
7722: F0 10      LD      A,($10)         
7724: 38 C8      JR      C,$76EE         
7726: DC EC DA   CALL    C,$DAEC         
7729: EE FA      XOR     $FA             
772B: CE 29      ADC     $29             
772D: 1F         RRA                     
772E: D1         POP     DE              
772F: 3F         CCF                     
7730: E1         POP     HL              
7731: FF         RST     0X38            
7732: 63         LD      H,E             
7733: 1F         RRA                     
7734: C5         PUSH    BC              
7735: 3F         CCF                     
7736: 1D         DEC     E               
7737: FB         EI                      
7738: FE E2      CP      $E2             
773A: FA 06 EC   LD      A,($EC06)       
773D: 1C         INC     E               
773E: F0 F0      LD      A,($F0)         
7740: 30 30      JR      NC,$7772        
7742: 2B         DEC     HL              
7743: 2B         DEC     HL              
7744: 26 24      LD      H,$24           
7746: 34         INC     (HL)            
7747: 24         INC     H               
7748: 3C         INC     A               
7749: 20 3E      JR      NZ,$7789        
774B: 38 67      JR      C,$77B4         
774D: 66         LD      H,(HL)          
774E: F3         DI                      
774F: A2         AND     D               
7750: FB         EI                      
7751: B2         OR      D               
7752: FF         RST     0X38            
7753: AE         XOR     (HL)            
7754: FE A3      CP      $A3             
7756: FF         RST     0X38            
7757: 93         SUB     E               
7758: F7         RST     0X30            
7759: 98         SBC     B               
775A: FF         RST     0X38            
775B: 8F         ADC     A,A             
775C: 80         ADD     A,B             
775D: 80         ADD     A,B             
775E: FF         RST     0X38            
775F: FF         RST     0X38            
7760: 0C         INC     C               
7761: 0C         INC     C               
7762: D4 D4 64   CALL    NC,$64D4        
7765: 24         INC     H               
7766: 2C         INC     L               
7767: 24         INC     H               
7768: 3C         INC     A               
7769: 04         INC     B               
776A: 7C         LD      A,H             
776B: 1C         INC     E               
776C: E6 66      AND     $66             
776E: CF         RST     0X08            
776F: 45         LD      B,L             
7770: DF         RST     0X18            
7771: 4D         LD      C,L             
7772: FF         RST     0X38            
7773: 75         LD      (HL),L          
7774: 7F         LD      A,A             
7775: C5         PUSH    BC              
7776: FF         RST     0X38            
7777: C9         RET                     
7778: EF         RST     0X28            
7779: 19         ADD     HL,DE           
777A: FF         RST     0X38            
777B: F1         POP     AF              
777C: 01 01 FF   LD      BC,$FF01        
777F: FF         RST     0X38            
7780: FF         RST     0X38            
7781: FF         RST     0X38            
7782: F6 81      OR      $81             
7784: DF         RST     0X18            
7785: A7         AND     A               
7786: DF         RST     0X18            
7787: A4         AND     H               
7788: 97         SUB     A               
7789: EC         ???                     
778A: CF         RST     0X08            
778B: B4         OR      H               
778C: DF         RST     0X18            
778D: A4         AND     H               
778E: DC A7 D6   CALL    C,$D6A7         
7791: A1         AND     C               
7792: D9         RETI                    
7793: A7         AND     A               
7794: 91         SUB     C               
7795: EF         RST     0X28            
7796: D1         POP     DE              
7797: AF         XOR     A               
7798: FF         RST     0X38            
7799: BF         CP      A               
779A: FF         RST     0X38            
779B: 88         ADC     A,B             
779C: 88         ADC     A,B             
779D: FF         RST     0X38            
779E: FF         RST     0X38            
779F: FF         RST     0X38            
77A0: FF         RST     0X38            
77A1: FF         RST     0X38            
77A2: E1         POP     HL              
77A3: 0F         RRCA                    
77A4: F5         PUSH    AF              
77A5: EF         RST     0X28            
77A6: D5         PUSH    DE              
77A7: 2F         CPL                     
77A8: C7         RST     0X00            
77A9: 3F         CCF                     
77AA: DD         ???                     
77AB: 2F         CPL                     
77AC: D5         PUSH    DE              
77AD: 2F         CPL                     
77AE: 15         DEC     D               
77AF: EF         RST     0X28            
77B0: E5         PUSH    HL              
77B1: 0F         RRCA                    
77B2: 15         DEC     D               
77B3: EF         RST     0X28            
77B4: 0F         RRCA                    
77B5: F7         RST     0X30            
77B6: 0D         DEC     C               
77B7: F7         RST     0X30            
77B8: FD         ???                     
77B9: FF         RST     0X38            
77BA: FF         RST     0X38            
77BB: 21 21 FF   LD      HL,$FF21        
77BE: FF         RST     0X38            
77BF: FF         RST     0X38            
77C0: FF         RST     0X38            
77C1: 7C         LD      A,H             
77C2: F3         DI                      
77C3: 83         ADD     A,E             
77C4: D7         RST     0X10            
77C5: A7         AND     A               
77C6: D6 A7      SUB     $A7             
77C8: DD         ???                     
77C9: 6E         LD      L,(HL)          
77CA: F5         PUSH    AF              
77CB: 36 D5      LD      (HL),$D5        
77CD: 67         LD      H,A             
77CE: D7         RST     0X10            
77CF: A7         AND     A               
77D0: D7         RST     0X10            
77D1: A2         AND     D               
77D2: C2 AF C5   JP      NZ,$C5AF        
77D5: 6F         LD      L,A             
77D6: C9         RET                     
77D7: 7F         LD      A,A             
77D8: FB         EI                      
77D9: BF         CP      A               
77DA: AF         XOR     A               
77DB: 9E         SBC     (HL)            
77DC: 8F         ADC     A,A             
77DD: F9         LD      SP,HL           
77DE: FF         RST     0X38            
77DF: 70         LD      (HL),B          
77E0: FF         RST     0X38            
77E1: FE 01      CP      $01             
77E3: 0F         RRCA                    
77E4: E5         PUSH    HL              
77E5: EF         RST     0X28            
77E6: 67         LD      H,A             
77E7: EE FF      XOR     $FF             
77E9: 7E         LD      A,(HL)          
77EA: EF         RST     0X28            
77EB: AF         XOR     A               
77EC: E5         PUSH    HL              
77ED: 2F         CPL                     
77EE: E7         RST     0X20            
77EF: EE 07      XOR     $07             
77F1: 0C         INC     C               
77F2: 1F         RRA                     
77F3: EC         ???                     
77F4: 1F         RRA                     
77F5: FE 1D      CP      $1D             
77F7: F7         RST     0X30            
77F8: FD         ???                     
77F9: FF         RST     0X38            
77FA: FF         RST     0X38            
77FB: 22         LD      (HLI),A         
77FC: 23         INC     HL              
77FD: FE FF      CP      $FF             
77FF: FC         ???                     
7800: 03         INC     BC              
7801: 03         INC     BC              
7802: 07         RLCA                    
7803: 04         INC     B               
7804: 0E 09      LD      C,$09           
7806: 1D         DEC     E               
7807: 1B         DEC     DE              
7808: 2D         DEC     L               
7809: 3B         DEC     SP              
780A: 2F         CPL                     
780B: 39         ADD     HL,SP           
780C: 4A         LD      C,D             
780D: 7C         LD      A,H             
780E: 45         LD      B,L             
780F: 7E         LD      A,(HL)          
7810: 63         LD      H,E             
7811: 7F         LD      A,A             
7812: 63         LD      H,E             
7813: 7C         LD      A,H             
7814: 51         LD      D,C             
7815: 7E         LD      A,(HL)          
7816: 5C         LD      E,H             
7817: 6F         LD      L,A             
7818: 3F         CCF                     
7819: 23         INC     HL              
781A: 2F         CPL                     
781B: 30 1B      JR      NC,$7838        
781D: 1C         INC     E               
781E: 07         RLCA                    
781F: 07         RLCA                    
7820: E0 E0      LDFF00  ($E0),A         
7822: F0 10      LD      A,($10)         
7824: 38 C8      JR      C,$77EE         
7826: DC EC DA   CALL    C,$DAEC         
7829: EE FA      XOR     $FA             
782B: CE 29      ADC     $29             
782D: 1F         RRA                     
782E: D1         POP     DE              
782F: 3F         CCF                     
7830: E1         POP     HL              
7831: FF         RST     0X38            
7832: 63         LD      H,E             
7833: 1F         RRA                     
7834: C5         PUSH    BC              
7835: 3F         CCF                     
7836: 1D         DEC     E               
7837: FB         EI                      
7838: FE E2      CP      $E2             
783A: FA 06 EC   LD      A,($EC06)       
783D: 1C         INC     E               
783E: F0 F0      LD      A,($F0)         
7840: F1         POP     AF              
7841: F1         POP     AF              
7842: BA         CP      D               
7843: CB 5D      SET     1,E             
7845: 66         LD      H,(HL)          
7846: 2D         DEC     L               
7847: 32         LD      (HLD),A         
7848: 31 3E 48   LD      SP,$483E        
784B: 4F         LD      C,A             
784C: 4D         LD      C,L             
784D: 4F         LD      C,A             
784E: 4F         LD      C,A             
784F: 4E         LD      C,(HL)          
7850: A6         AND     (HL)            
7851: E4         ???                     
7852: FE B8      CP      $B8             
7854: AE         XOR     (HL)            
7855: B8         CP      B               
7856: A6         AND     (HL)            
7857: BC         CP      H               
7858: 92         SUB     D               
7859: 9E         SBC     (HL)            
785A: CF         RST     0X08            
785B: 8E         ADC     A,(HL)          
785C: 63         LD      H,E             
785D: 41         LD      B,C             
785E: 3F         CCF                     
785F: 3F         CCF                     
7860: 8F         ADC     A,A             
7861: 8F         ADC     A,A             
7862: 5D         LD      E,L             
7863: D3         ???                     
7864: BA         CP      D               
7865: 66         LD      H,(HL)          
7866: B4         OR      H               
7867: 4C         LD      C,H             
7868: AC         XOR     H               
7869: 5C         LD      E,H             
786A: 12         LD      (DE),A          
786B: F2         ???                     
786C: B2         OR      D               
786D: F2         ???                     
786E: F2         ???                     
786F: 72         LD      (HL),D          
7870: 65         LD      H,L             
7871: 27         DAA                     
7872: 7F         LD      A,A             
7873: 1D         DEC     E               
7874: 75         LD      (HL),L          
7875: 3D         DEC     A               
7876: 65         LD      H,L             
7877: 3D         DEC     A               
7878: 49         LD      C,C             
7879: 79         LD      A,C             
787A: F3         DI                      
787B: 71         LD      (HL),C          
787C: C6 82      ADD     $82             
787E: FC         ???                     
787F: FC         ???                     
7880: FF         RST     0X38            
7881: FF         RST     0X38            
7882: E0 9F      LDFF00  ($9F),A         
7884: 90         SUB     B               
7885: EF         RST     0X28            
7886: 8F         ADC     A,A             
7887: F0 88      LD      A,($88)         
7889: F7         RST     0X30            
788A: 8B         ADC     A,E             
788B: F4         ???                     
788C: 8B         ADC     A,E             
788D: F4         ???                     
788E: 8B         ADC     A,E             
788F: F4         ???                     
7890: 8B         ADC     A,E             
7891: F4         ???                     
7892: 88         ADC     A,B             
7893: F7         RST     0X30            
7894: 8F         ADC     A,A             
7895: F0 8F      LD      A,($8F)         
7897: FF         RST     0X38            
7898: 9F         SBC     A               
7899: FF         RST     0X38            
789A: BF         CP      A               
789B: FF         RST     0X38            
789C: FF         RST     0X38            
789D: FF         RST     0X38            
789E: FF         RST     0X38            
789F: FF         RST     0X38            
78A0: FF         RST     0X38            
78A1: FF         RST     0X38            
78A2: 01 FF 07   LD      BC,$07FF        
78A5: FF         RST     0X38            
78A6: FF         RST     0X38            
78A7: 0F         RRCA                    
78A8: 1F         RRA                     
78A9: EF         RST     0X28            
78AA: DF         RST     0X18            
78AB: 2F         CPL                     
78AC: DF         RST     0X18            
78AD: 2F         CPL                     
78AE: DF         RST     0X18            
78AF: 2F         CPL                     
78B0: DF         RST     0X18            
78B1: 2F         CPL                     
78B2: 1F         RRA                     
78B3: EF         RST     0X28            
78B4: FF         RST     0X38            
78B5: 0F         RRCA                    
78B6: FF         RST     0X38            
78B7: F7         RST     0X30            
78B8: FF         RST     0X38            
78B9: FB         EI                      
78BA: FF         RST     0X38            
78BB: FD         ???                     
78BC: FF         RST     0X38            
78BD: FD         ???                     
78BE: FF         RST     0X38            
78BF: FF         RST     0X38            
78C0: 7F         LD      A,A             
78C1: FF         RST     0X38            
78C2: E1         POP     HL              
78C3: 9F         SBC     A               
78C4: 90         SUB     B               
78C5: EF         RST     0X28            
78C6: 8F         ADC     A,A             
78C7: F0 88      LD      A,($88)         
78C9: F7         RST     0X30            
78CA: 97         SUB     A               
78CB: FC         ???                     
78CC: F7         RST     0X30            
78CD: E3         ???                     
78CE: EA D6 CB   LD      ($CBD6),A       
78D1: B6         OR      (HL)            
78D2: 89         ADC     A,C             
78D3: F7         RST     0X30            
78D4: 8E         ADC     A,(HL)          
78D5: F2         ???                     
78D6: 8E         ADC     A,(HL)          
78D7: FF         RST     0X38            
78D8: 9E         SBC     (HL)            
78D9: FF         RST     0X38            
78DA: BE         CP      (HL)            
78DB: FF         RST     0X38            
78DC: FF         RST     0X38            
78DD: FF         RST     0X38            
78DE: 7F         LD      A,A             
78DF: FF         RST     0X38            
78E0: FE FF      CP      $FF             
78E2: C1         POP     BC              
78E3: BF         CP      A               
78E4: C7         RST     0X00            
78E5: BF         CP      A               
78E6: 3F         CCF                     
78E7: 8F         ADC     A,A             
78E8: 9F         SBC     A               
78E9: EF         RST     0X28            
78EA: 9F         SBC     A               
78EB: AF         XOR     A               
78EC: 9F         SBC     A               
78ED: BF         CP      A               
78EE: E3         ???                     
78EF: FF         RST     0X38            
78F0: 0C         INC     C               
78F1: 2F         CPL                     
78F2: 1F         RRA                     
78F3: EF         RST     0X28            
78F4: FF         RST     0X38            
78F5: 0F         RRCA                    
78F6: FF         RST     0X38            
78F7: F7         RST     0X30            
78F8: FF         RST     0X38            
78F9: FB         EI                      
78FA: FF         RST     0X38            
78FB: FD         ???                     
78FC: 7F         LD      A,A             
78FD: FD         ???                     
78FE: 7E         LD      A,(HL)          
78FF: FF         RST     0X38            
7900: 03         INC     BC              
7901: 03         INC     BC              
7902: 07         RLCA                    
7903: 04         INC     B               
7904: 0E 09      LD      C,$09           
7906: 1D         DEC     E               
7907: 1B         DEC     DE              
7908: 2D         DEC     L               
7909: 3B         DEC     SP              
790A: 2F         CPL                     
790B: 39         ADD     HL,SP           
790C: 4A         LD      C,D             
790D: 7C         LD      A,H             
790E: 45         LD      B,L             
790F: 7E         LD      A,(HL)          
7910: 63         LD      H,E             
7911: 7F         LD      A,A             
7912: 63         LD      H,E             
7913: 7C         LD      A,H             
7914: 51         LD      D,C             
7915: 7E         LD      A,(HL)          
7916: 5C         LD      E,H             
7917: 6F         LD      L,A             
7918: 3F         CCF                     
7919: 23         INC     HL              
791A: 2F         CPL                     
791B: 30 1B      JR      NC,$7938        
791D: 1C         INC     E               
791E: 07         RLCA                    
791F: 07         RLCA                    
7920: E0 E0      LDFF00  ($E0),A         
7922: F0 10      LD      A,($10)         
7924: 38 C8      JR      C,$78EE         
7926: DC EC DA   CALL    C,$DAEC         
7929: EE FA      XOR     $FA             
792B: CE 29      ADC     $29             
792D: 1F         RRA                     
792E: D1         POP     DE              
792F: 3F         CCF                     
7930: E1         POP     HL              
7931: FF         RST     0X38            
7932: 63         LD      H,E             
7933: 1F         RRA                     
7934: C5         PUSH    BC              
7935: 3F         CCF                     
7936: 1D         DEC     E               
7937: FB         EI                      
7938: FE E2      CP      $E2             
793A: FA 06 EC   LD      A,($EC06)       
793D: 1C         INC     E               
793E: F0 F0      LD      A,($F0)         
7940: 07         RLCA                    
7941: 07         RLCA                    
7942: 3A         LD      A,(HLD)         
7943: 3C         INC     A               
7944: 4E         LD      C,(HL)          
7945: 48         LD      C,B             
7946: 77         LD      (HL),A          
7947: 58         LD      E,B             
7948: 5F         LD      E,A             
7949: 73         LD      (HL),E          
794A: 2C         INC     L               
794B: 34         INC     (HL)            
794C: 69         LD      L,C             
794D: 79         LD      A,C             
794E: AD         XOR     L               
794F: B9         CP      C               
7950: FA BC EF   LD      A,($EFBC)       
7953: F7         RST     0X30            
7954: AF         XOR     A               
7955: B0         OR      B               
7956: 96         SUB     (HL)            
7957: 98         SBC     B               
7958: 7B         LD      A,E             
7959: 7C         LD      A,H             
795A: 2C         INC     L               
795B: 27         DAA                     
795C: 5B         LD      E,E             
795D: 47         LD      B,A             
795E: 7F         LD      A,A             
795F: 7F         LD      A,A             
7960: E0 E0      LDFF00  ($E0),A         
7962: 5C         LD      E,H             
7963: 3C         INC     A               
7964: 72         LD      (HL),D          
7965: 12         LD      (DE),A          
7966: FE 12      CP      $12             
7968: FA CE 34   LD      A,($34CE)       
796B: 2C         INC     L               
796C: 96         SUB     (HL)            
796D: 9E         SBC     (HL)            
796E: B5         OR      L               
796F: 9D         SBC     L               
7970: 5F         LD      E,A             
7971: 3D         DEC     A               
7972: F7         RST     0X30            
7973: EF         RST     0X28            
7974: F5         PUSH    AF              
7975: 0D         DEC     C               
7976: 69         LD      L,C             
7977: 19         ADD     HL,DE           
7978: DF         RST     0X18            
7979: 3F         CCF                     
797A: 36 E6      LD      (HL),$E6        
797C: DA E2 FE   JP      C,$FEE2         
797F: FE FF      CP      $FF             
7981: FF         RST     0X38            
7982: E0 9F      LDFF00  ($9F),A         
7984: 90         SUB     B               
7985: EF         RST     0X28            
7986: 8F         ADC     A,A             
7987: F0 88      LD      A,($88)         
7989: F7         RST     0X30            
798A: 8B         ADC     A,E             
798B: F4         ???                     
798C: 8B         ADC     A,E             
798D: F4         ???                     
798E: 8B         ADC     A,E             
798F: F4         ???                     
7990: 8B         ADC     A,E             
7991: F4         ???                     
7992: 88         ADC     A,B             
7993: F7         RST     0X30            
7994: 8F         ADC     A,A             
7995: F0 8F      LD      A,($8F)         
7997: FF         RST     0X38            
7998: 9F         SBC     A               
7999: FF         RST     0X38            
799A: BF         CP      A               
799B: FF         RST     0X38            
799C: FF         RST     0X38            
799D: FF         RST     0X38            
799E: FF         RST     0X38            
799F: FF         RST     0X38            
79A0: FF         RST     0X38            
79A1: FF         RST     0X38            
79A2: 01 FF 07   LD      BC,$07FF        
79A5: FF         RST     0X38            
79A6: FF         RST     0X38            
79A7: 0F         RRCA                    
79A8: 1F         RRA                     
79A9: EF         RST     0X28            
79AA: DF         RST     0X18            
79AB: 2F         CPL                     
79AC: DF         RST     0X18            
79AD: 2F         CPL                     
79AE: DF         RST     0X18            
79AF: 2F         CPL                     
79B0: DF         RST     0X18            
79B1: 2F         CPL                     
79B2: 1F         RRA                     
79B3: EF         RST     0X28            
79B4: FF         RST     0X38            
79B5: 0F         RRCA                    
79B6: FF         RST     0X38            
79B7: F7         RST     0X30            
79B8: FF         RST     0X38            
79B9: FB         EI                      
79BA: FF         RST     0X38            
79BB: FD         ???                     
79BC: FF         RST     0X38            
79BD: FD         ???                     
79BE: FF         RST     0X38            
79BF: FF         RST     0X38            
79C0: 7F         LD      A,A             
79C1: FF         RST     0X38            
79C2: E1         POP     HL              
79C3: 9F         SBC     A               
79C4: 90         SUB     B               
79C5: EF         RST     0X28            
79C6: 8F         ADC     A,A             
79C7: F0 88      LD      A,($88)         
79C9: F7         RST     0X30            
79CA: 97         SUB     A               
79CB: FC         ???                     
79CC: F7         RST     0X30            
79CD: E3         ???                     
79CE: EA D6 CB   LD      ($CBD6),A       
79D1: B6         OR      (HL)            
79D2: 89         ADC     A,C             
79D3: F7         RST     0X30            
79D4: 8E         ADC     A,(HL)          
79D5: F2         ???                     
79D6: 8E         ADC     A,(HL)          
79D7: FF         RST     0X38            
79D8: 9E         SBC     (HL)            
79D9: FF         RST     0X38            
79DA: BE         CP      (HL)            
79DB: FF         RST     0X38            
79DC: FF         RST     0X38            
79DD: FF         RST     0X38            
79DE: 7F         LD      A,A             
79DF: FF         RST     0X38            
79E0: FE FF      CP      $FF             
79E2: C1         POP     BC              
79E3: BF         CP      A               
79E4: C7         RST     0X00            
79E5: BF         CP      A               
79E6: 3F         CCF                     
79E7: 8F         ADC     A,A             
79E8: 9F         SBC     A               
79E9: EF         RST     0X28            
79EA: 9F         SBC     A               
79EB: AF         XOR     A               
79EC: 9F         SBC     A               
79ED: BF         CP      A               
79EE: E3         ???                     
79EF: FF         RST     0X38            
79F0: 0C         INC     C               
79F1: 2F         CPL                     
79F2: 1F         RRA                     
79F3: EF         RST     0X28            
79F4: FF         RST     0X38            
79F5: 0F         RRCA                    
79F6: FF         RST     0X38            
79F7: F7         RST     0X30            
79F8: FF         RST     0X38            
79F9: FB         EI                      
79FA: FF         RST     0X38            
79FB: FD         ???                     
79FC: 7F         LD      A,A             
79FD: FD         ???                     
79FE: 7E         LD      A,(HL)          
79FF: FF         RST     0X38            
7A00: 00         NOP                     
7A01: 00         NOP                     
7A02: 03         INC     BC              
7A03: 03         INC     BC              
7A04: 0F         RRCA                    
7A05: 0C         INC     C               
7A06: 1F         RRA                     
7A07: 10 3F      STOP    $3F             
7A09: 26 3F      LD      H,$3F           
7A0B: 2E 7F      LD      L,$7F           
7A0D: 4C         LD      C,H             
7A0E: 7F         LD      A,A             
7A0F: 40         LD      B,B             
7A10: 5F         LD      E,A             
7A11: 65         LD      H,L             
7A12: 3F         CCF                     
7A13: 29         ADD     HL,HL           
7A14: 3F         CCF                     
7A15: 20 3F      JR      NZ,$7A56        
7A17: 30 7F      JR      NC,$7A98        
7A19: 4D         LD      C,L             
7A1A: 6F         LD      L,A             
7A1B: 5A         LD      E,D             
7A1C: 3F         CCF                     
7A1D: 3E 03      LD      A,$03           
7A1F: 03         INC     BC              
7A20: 00         NOP                     
7A21: 00         NOP                     
7A22: C0         RET     NZ              
7A23: C0         RET     NZ              
7A24: F0 30      LD      A,($30)         
7A26: E8 18      ADD     SP,$18          
7A28: F4         ???                     
7A29: CC FC E4   CALL    Z,$E4FC         
7A2C: FA E6 FA   LD      A,($FAE6)       
7A2F: 66         LD      H,(HL)          
7A30: FA 06 C6   LD      A,($C606)       
7A33: 3E 8C      LD      A,$8C           
7A35: 7C         LD      A,H             
7A36: B8         CP      B               
7A37: 78         LD      A,B             
7A38: A0         AND     B               
7A39: E0 C0      LDFF00  ($C0),A         
7A3B: 40         LD      B,B             
7A3C: 40         LD      B,B             
7A3D: C0         RET     NZ              
7A3E: 80         ADD     A,B             
7A3F: 80         ADD     A,B             
7A40: 07         RLCA                    
7A41: 07         RLCA                    
7A42: 3A         LD      A,(HLD)         
7A43: 3C         INC     A               
7A44: 4E         LD      C,(HL)          
7A45: 48         LD      C,B             
7A46: 77         LD      (HL),A          
7A47: 58         LD      E,B             
7A48: 5F         LD      E,A             
7A49: 73         LD      (HL),E          
7A4A: 2C         INC     L               
7A4B: 34         INC     (HL)            
7A4C: 69         LD      L,C             
7A4D: 79         LD      A,C             
7A4E: AD         XOR     L               
7A4F: B9         CP      C               
7A50: FA BC EF   LD      A,($EFBC)       
7A53: F7         RST     0X30            
7A54: AF         XOR     A               
7A55: B0         OR      B               
7A56: 96         SUB     (HL)            
7A57: 98         SBC     B               
7A58: 7B         LD      A,E             
7A59: 7C         LD      A,H             
7A5A: 2C         INC     L               
7A5B: 27         DAA                     
7A5C: 5B         LD      E,E             
7A5D: 47         LD      B,A             
7A5E: 7F         LD      A,A             
7A5F: 7F         LD      A,A             
7A60: E0 E0      LDFF00  ($E0),A         
7A62: 5C         LD      E,H             
7A63: 3C         INC     A               
7A64: 72         LD      (HL),D          
7A65: 12         LD      (DE),A          
7A66: FE 12      CP      $12             
7A68: FA CE 34   LD      A,($34CE)       
7A6B: 2C         INC     L               
7A6C: 96         SUB     (HL)            
7A6D: 9E         SBC     (HL)            
7A6E: B5         OR      L               
7A6F: 9D         SBC     L               
7A70: 5F         LD      E,A             
7A71: 3D         DEC     A               
7A72: F7         RST     0X30            
7A73: EF         RST     0X28            
7A74: F5         PUSH    AF              
7A75: 0D         DEC     C               
7A76: 69         LD      L,C             
7A77: 19         ADD     HL,DE           
7A78: DF         RST     0X18            
7A79: 3F         CCF                     
7A7A: 36 E6      LD      (HL),$E6        
7A7C: DA E2 FE   JP      C,$FEE2         
7A7F: FE 1F      CP      $1F             
7A81: 1F         RRA                     
7A82: 25         DEC     H               
7A83: 3E 4F      LD      A,$4F           
7A85: 77         LD      (HL),A          
7A86: FB         EI                      
7A87: EC         ???                     
7A88: 97         SUB     A               
7A89: F8 B7      LDHL    SP,$B7          
7A8B: D8         RET     C               
7A8C: B7         OR      A               
7A8D: D8         RET     C               
7A8E: B3         OR      E               
7A8F: DC B1 FE   CALL    C,$FEB1         
7A92: D8         RET     C               
7A93: EF         RST     0X28            
7A94: 9F         SBC     A               
7A95: E7         RST     0X20            
7A96: 8F         ADC     A,A             
7A97: F1         POP     AF              
7A98: 81         ADD     A,C             
7A99: FF         RST     0X38            
7A9A: 41         LD      B,C             
7A9B: 7F         LD      A,A             
7A9C: 21 3F 1F   LD      HL,$1F3F        
7A9F: 1F         RRA                     
7AA0: F8 F8      LDHL    SP,$F8          
7AA2: C4 3C F2   CALL    NZ,$F23C        
7AA5: EE D9      XOR     $D9             
7AA7: 37         SCF                     
7AA8: EF         RST     0X28            
7AA9: 1F         RRA                     
7AAA: ED         ???                     
7AAB: 1B         DEC     DE              
7AAC: ED         ???                     
7AAD: 1B         DEC     DE              
7AAE: CD 3B 8D   CALL    $8D3B           
7AB1: 7B         LD      A,E             
7AB2: 19         ADD     HL,DE           
7AB3: FF         RST     0X38            
7AB4: FD         ???                     
7AB5: E7         RST     0X20            
7AB6: F3         DI                      
7AB7: 0F         RRCA                    
7AB8: 01 FF 02   LD      BC,$02FF        
7ABB: FE 84      CP      $84             
7ABD: FC         ???                     
7ABE: F8 F8      LDHL    SP,$F8          
7AC0: 19         ADD     HL,DE           
7AC1: 19         ADD     HL,DE           
7AC2: 26 3F      LD      H,$3F           
7AC4: 4F         LD      C,A             
7AC5: 77         LD      (HL),A          
7AC6: FB         EI                      
7AC7: ED         ???                     
7AC8: 97         SUB     A               
7AC9: FA B7 DC   LD      A,($DCB7)       
7ACC: BF         CP      A               
7ACD: DA F7 D9   JP      C,$D9F7         
7AD0: F3         DI                      
7AD1: 3C         INC     A               
7AD2: D8         RET     C               
7AD3: 6F         LD      L,A             
7AD4: 9F         SBC     A               
7AD5: E7         RST     0X20            
7AD6: 8F         ADC     A,A             
7AD7: F1         POP     AF              
7AD8: 81         ADD     A,C             
7AD9: FF         RST     0X38            
7ADA: 41         LD      B,C             
7ADB: 7F         LD      A,A             
7ADC: 23         INC     HL              
7ADD: 3E 1E      LD      A,$1E           
7ADF: 1C         INC     E               
7AE0: F8 F8      LDHL    SP,$F8          
7AE2: C4 3C F2   CALL    NZ,$F23C        
7AE5: EE D9      XOR     $D9             
7AE7: 37         SCF                     
7AE8: EF         RST     0X28            
7AE9: 9F         SBC     A               
7AEA: ED         ???                     
7AEB: 5B         LD      E,E             
7AEC: FF         RST     0X38            
7AED: 7B         LD      A,E             
7AEE: EE 9C      XOR     $9C             
7AF0: EF         RST     0X28            
7AF1: 9A         SBC     D               
7AF2: 99         SBC     C               
7AF3: FF         RST     0X38            
7AF4: FD         ???                     
7AF5: E7         RST     0X20            
7AF6: F3         DI                      
7AF7: 0F         RRCA                    
7AF8: 01 FF 02   LD      BC,$02FF        
7AFB: FE 84      CP      $84             
7AFD: FC         ???                     
7AFE: F8 78      LDHL    SP,$78          
7B00: 03         INC     BC              
7B01: 03         INC     BC              
7B02: 0F         RRCA                    
7B03: 0C         INC     C               
7B04: 1F         RRA                     
7B05: 10 1C      STOP    $1C             
7B07: 13         INC     DE              
7B08: 3B         DEC     SP              
7B09: 27         DAA                     
7B0A: 7F         LD      A,A             
7B0B: 67         LD      H,A             
7B0C: 7F         LD      A,A             
7B0D: 67         LD      H,A             
7B0E: 7F         LD      A,A             
7B0F: 53         LD      D,E             
7B10: 77         LD      (HL),A          
7B11: 58         LD      E,B             
7B12: 5E         LD      E,(HL)          
7B13: 6C         LD      L,H             
7B14: 5F         LD      E,A             
7B15: 63         LD      H,E             
7B16: 57         LD      D,A             
7B17: 68         LD      L,B             
7B18: 22         LD      (HLI),A         
7B19: 3C         INC     A               
7B1A: 23         INC     HL              
7B1B: 3C         INC     A               
7B1C: 19         ADD     HL,DE           
7B1D: 1E 07      LD      E,$07           
7B1F: 07         RLCA                    
7B20: C0         RET     NZ              
7B21: C0         RET     NZ              
7B22: F0 30      LD      A,($30)         
7B24: F8 08      LDHL    SP,$08          
7B26: 38 C8      JR      C,$7AF0         
7B28: DC E4 FE   CALL    C,$FEE4         
7B2B: E6 FE      AND     $FE             
7B2D: E6 FE      AND     $FE             
7B2F: CA EE 1A   JP      Z,$1AEE         
7B32: 7A         LD      A,D             
7B33: 36 FA      LD      (HL),$FA        
7B35: C6 EA      ADD     $EA             
7B37: 16 44      LD      D,$44           
7B39: 3C         INC     A               
7B3A: C4 3C 98   CALL    NZ,$983C        
7B3D: 78         LD      A,B             
7B3E: E0 E0      LDFF00  ($E0),A         
7B40: 00         NOP                     
7B41: 00         NOP                     
7B42: 1E 1E      LD      E,$1E           
7B44: 3F         CCF                     
7B45: 21 79 46   LD      HL,$4679        
7B48: 74         LD      (HL),H          
7B49: 4B         LD      C,E             
7B4A: 37         SCF                     
7B4B: 68         LD      L,B             
7B4C: 35         DEC     (HL)            
7B4D: 6B         LD      L,E             
7B4E: 77         LD      (HL),A          
7B4F: 48         LD      C,B             
7B50: 6C         LD      L,H             
7B51: 53         LD      D,E             
7B52: 61         LD      H,C             
7B53: 5E         LD      E,(HL)          
7B54: 7F         LD      A,A             
7B55: 61         LD      H,C             
7B56: 5E         LD      E,(HL)          
7B57: 7F         LD      A,A             
7B58: 40         LD      B,B             
7B59: 7F         LD      A,A             
7B5A: 61         LD      H,C             
7B5B: 3F         CCF                     
7B5C: 3F         CCF                     
7B5D: 1E 00      LD      E,$00           
7B5F: 00         NOP                     
7B60: 00         NOP                     
7B61: 00         NOP                     
7B62: 78         LD      A,B             
7B63: 78         LD      A,B             
7B64: FC         ???                     
7B65: 84         ADD     A,H             
7B66: CE 32      ADC     $32             
7B68: 36 CA      LD      (HL),$CA        
7B6A: F6 0A      OR      $0A             
7B6C: AE         XOR     (HL)            
7B6D: D6 EC      SUB     $EC             
7B6F: 16 36      LD      D,$36           
7B71: CA CE 32   JP      Z,$32CE         
7B74: FE C6      CP      $C6             
7B76: 3A         LD      A,(HLD)         
7B77: FE 02      CP      $02             
7B79: FE C6      CP      $C6             
7B7B: FC         ???                     
7B7C: 7C         LD      A,H             
7B7D: 38 00      JR      C,$7B7F         
7B7F: 00         NOP                     
7B80: 7F         LD      A,A             
7B81: 7F         LD      A,A             
7B82: FF         RST     0X38            
7B83: 80         ADD     A,B             
7B84: BF         CP      A               
7B85: D0         RET     NC              
7B86: FF         RST     0X38            
7B87: 80         ADD     A,B             
7B88: 80         ADD     A,B             
7B89: FF         RST     0X38            
7B8A: FF         RST     0X38            
7B8B: 80         ADD     A,B             
7B8C: BF         CP      A               
7B8D: D0         RET     NC              
7B8E: FF         RST     0X38            
7B8F: 80         ADD     A,B             
7B90: 80         ADD     A,B             
7B91: FF         RST     0X38            
7B92: FF         RST     0X38            
7B93: 80         ADD     A,B             
7B94: BF         CP      A               
7B95: D0         RET     NC              
7B96: FF         RST     0X38            
7B97: 80         ADD     A,B             
7B98: FF         RST     0X38            
7B99: FF         RST     0X38            
7B9A: 92         SUB     D               
7B9B: FF         RST     0X38            
7B9C: 92         SUB     D               
7B9D: FF         RST     0X38            
7B9E: 7F         LD      A,A             
7B9F: 7F         LD      A,A             
7BA0: FE FE      CP      $FE             
7BA2: FF         RST     0X38            
7BA3: 01 FD 0B   LD      BC,$0BFD        
7BA6: FF         RST     0X38            
7BA7: 01 01 FF   LD      BC,$FF01        
7BAA: FF         RST     0X38            
7BAB: 01 FD 0B   LD      BC,$0BFD        
7BAE: FF         RST     0X38            
7BAF: 01 01 FF   LD      BC,$FF01        
7BB2: FF         RST     0X38            
7BB3: 01 FD 0B   LD      BC,$0BFD        
7BB6: FF         RST     0X38            
7BB7: 01 FF FF   LD      BC,$FFFF        
7BBA: 49         LD      C,C             
7BBB: FF         RST     0X38            
7BBC: 49         LD      C,C             
7BBD: FF         RST     0X38            
7BBE: FE FE      CP      $FE             
7BC0: FF         RST     0X38            
7BC1: FF         RST     0X38            
7BC2: 80         ADD     A,B             
7BC3: 80         ADD     A,B             
7BC4: 80         ADD     A,B             
7BC5: 80         ADD     A,B             
7BC6: 80         ADD     A,B             
7BC7: 80         ADD     A,B             
7BC8: 80         ADD     A,B             
7BC9: 80         ADD     A,B             
7BCA: FF         RST     0X38            
7BCB: FF         RST     0X38            
7BCC: 80         ADD     A,B             
7BCD: 80         ADD     A,B             
7BCE: FF         RST     0X38            
7BCF: BF         CP      A               
7BD0: FF         RST     0X38            
7BD1: FF         RST     0X38            
7BD2: 01 01 01   LD      BC,$0101        
7BD5: 01 01 01   LD      BC,$0101        
7BD8: 01 01 FF   LD      BC,$FF01        
7BDB: FF         RST     0X38            
7BDC: 01 01 FF   LD      BC,$FF01        
7BDF: FD         ???                     
7BE0: FF         RST     0X38            
7BE1: A0         AND     B               
7BE2: FF         RST     0X38            
7BE3: A1         AND     C               
7BE4: FE A0      CP      $A0             
7BE6: FF         RST     0X38            
7BE7: BF         CP      A               
7BE8: FF         RST     0X38            
7BE9: A0         AND     B               
7BEA: FF         RST     0X38            
7BEB: A1         AND     C               
7BEC: FE A0      CP      $A0             
7BEE: FF         RST     0X38            
7BEF: BF         CP      A               
7BF0: FF         RST     0X38            
7BF1: 05         DEC     B               
7BF2: FF         RST     0X38            
7BF3: 85         ADD     A,L             
7BF4: 7F         LD      A,A             
7BF5: 05         DEC     B               
7BF6: FF         RST     0X38            
7BF7: FD         ???                     
7BF8: FF         RST     0X38            
7BF9: 05         DEC     B               
7BFA: FF         RST     0X38            
7BFB: 85         ADD     A,L             
7BFC: 7F         LD      A,A             
7BFD: 05         DEC     B               
7BFE: FF         RST     0X38            
7BFF: FD         ???                     
7C00: 03         INC     BC              
7C01: 03         INC     BC              
7C02: 07         RLCA                    
7C03: 04         INC     B               
7C04: 0E 09      LD      C,$09           
7C06: 1D         DEC     E               
7C07: 1B         DEC     DE              
7C08: 2D         DEC     L               
7C09: 3B         DEC     SP              
7C0A: 2F         CPL                     
7C0B: 39         ADD     HL,SP           
7C0C: 4A         LD      C,D             
7C0D: 7C         LD      A,H             
7C0E: 45         LD      B,L             
7C0F: 7E         LD      A,(HL)          
7C10: 63         LD      H,E             
7C11: 7F         LD      A,A             
7C12: 63         LD      H,E             
7C13: 7C         LD      A,H             
7C14: 51         LD      D,C             
7C15: 7E         LD      A,(HL)          
7C16: 5C         LD      E,H             
7C17: 6F         LD      L,A             
7C18: 3F         CCF                     
7C19: 23         INC     HL              
7C1A: 2F         CPL                     
7C1B: 30 1B      JR      NC,$7C38        
7C1D: 1C         INC     E               
7C1E: 07         RLCA                    
7C1F: 07         RLCA                    
7C20: E0 E0      LDFF00  ($E0),A         
7C22: F0 10      LD      A,($10)         
7C24: 38 C8      JR      C,$7BEE         
7C26: DC EC DA   CALL    C,$DAEC         
7C29: EE FA      XOR     $FA             
7C2B: CE 29      ADC     $29             
7C2D: 1F         RRA                     
7C2E: D1         POP     DE              
7C2F: 3F         CCF                     
7C30: E1         POP     HL              
7C31: FF         RST     0X38            
7C32: 63         LD      H,E             
7C33: 1F         RRA                     
7C34: C5         PUSH    BC              
7C35: 3F         CCF                     
7C36: 1D         DEC     E               
7C37: FB         EI                      
7C38: FE E2      CP      $E2             
7C3A: FA 06 EC   LD      A,($EC06)       
7C3D: 1C         INC     E               
7C3E: F0 F0      LD      A,($F0)         
7C40: 38 38      JR      C,$7C7A         
7C42: 27         DAA                     
7C43: 27         DAA                     
7C44: 1E 14      LD      E,$14           
7C46: 0F         RRCA                    
7C47: 0B         DEC     BC              
7C48: 3F         CCF                     
7C49: 3B         DEC     SP              
7C4A: 5E         LD      E,(HL)          
7C4B: 4A         LD      C,D             
7C4C: 7B         LD      A,E             
7C4D: 4D         LD      C,L             
7C4E: FF         RST     0X38            
7C4F: FE 83      CP      $83             
7C51: 82         ADD     A,D             
7C52: FF         RST     0X38            
7C53: BB         CP      E               
7C54: FE BA      CP      $BA             
7C56: FE BB      CP      $BB             
7C58: FF         RST     0X38            
7C59: 93         SUB     E               
7C5A: FF         RST     0X38            
7C5B: C7         RST     0X00            
7C5C: FF         RST     0X38            
7C5D: B8         CP      B               
7C5E: FF         RST     0X38            
7C5F: FF         RST     0X38            
7C60: 0E 0E      LD      C,$0E           
7C62: F2         ???                     
7C63: F2         ???                     
7C64: 5C         LD      E,H             
7C65: 34         INC     (HL)            
7C66: F8 68      LDHL    SP,$68          
7C68: FE EE      CP      $EE             
7C6A: BB         CP      E               
7C6B: A9         XOR     C               
7C6C: EF         RST     0X28            
7C6D: D9         RETI                    
7C6E: C9         RET                     
7C6F: BF         CP      A               
7C70: DF         RST     0X18            
7C71: BF         CP      A               
7C72: FB         EI                      
7C73: F9         LD      SP,HL           
7C74: 5F         LD      E,A             
7C75: 39         ADD     HL,SP           
7C76: 3F         CCF                     
7C77: FF         RST     0X38            
7C78: E5         PUSH    HL              
7C79: C7         RST     0X00            
7C7A: FD         ???                     
7C7B: FF         RST     0X38            
7C7C: FD         ???                     
7C7D: 01 FF FF   LD      BC,$FFFF        
7C80: 7F         LD      A,A             
7C81: 7F         LD      A,A             
7C82: FF         RST     0X38            
7C83: 80         ADD     A,B             
7C84: BF         CP      A               
7C85: D0         RET     NC              
7C86: FF         RST     0X38            
7C87: 80         ADD     A,B             
7C88: 80         ADD     A,B             
7C89: FF         RST     0X38            
7C8A: FF         RST     0X38            
7C8B: 80         ADD     A,B             
7C8C: BF         CP      A               
7C8D: D0         RET     NC              
7C8E: FF         RST     0X38            
7C8F: 80         ADD     A,B             
7C90: 80         ADD     A,B             
7C91: FF         RST     0X38            
7C92: FF         RST     0X38            
7C93: 80         ADD     A,B             
7C94: BF         CP      A               
7C95: D0         RET     NC              
7C96: FF         RST     0X38            
7C97: 80         ADD     A,B             
7C98: FF         RST     0X38            
7C99: FF         RST     0X38            
7C9A: 92         SUB     D               
7C9B: FF         RST     0X38            
7C9C: 92         SUB     D               
7C9D: FF         RST     0X38            
7C9E: 7F         LD      A,A             
7C9F: 7F         LD      A,A             
7CA0: FE FE      CP      $FE             
7CA2: FF         RST     0X38            
7CA3: 01 FD 0B   LD      BC,$0BFD        
7CA6: FF         RST     0X38            
7CA7: 01 01 FF   LD      BC,$FF01        
7CAA: FF         RST     0X38            
7CAB: 01 FD 0B   LD      BC,$0BFD        
7CAE: FF         RST     0X38            
7CAF: 01 01 FF   LD      BC,$FF01        
7CB2: FF         RST     0X38            
7CB3: 01 FD 0B   LD      BC,$0BFD        
7CB6: FF         RST     0X38            
7CB7: 01 FF FF   LD      BC,$FFFF        
7CBA: 49         LD      C,C             
7CBB: FF         RST     0X38            
7CBC: 49         LD      C,C             
7CBD: FF         RST     0X38            
7CBE: FE FE      CP      $FE             
7CC0: FF         RST     0X38            
7CC1: FF         RST     0X38            
7CC2: 80         ADD     A,B             
7CC3: 80         ADD     A,B             
7CC4: 80         ADD     A,B             
7CC5: 80         ADD     A,B             
7CC6: 80         ADD     A,B             
7CC7: 80         ADD     A,B             
7CC8: 80         ADD     A,B             
7CC9: 80         ADD     A,B             
7CCA: FF         RST     0X38            
7CCB: FF         RST     0X38            
7CCC: 80         ADD     A,B             
7CCD: 80         ADD     A,B             
7CCE: FF         RST     0X38            
7CCF: BF         CP      A               
7CD0: FF         RST     0X38            
7CD1: FF         RST     0X38            
7CD2: 01 01 01   LD      BC,$0101        
7CD5: 01 01 01   LD      BC,$0101        
7CD8: 01 01 FF   LD      BC,$FF01        
7CDB: FF         RST     0X38            
7CDC: 01 01 FF   LD      BC,$FF01        
7CDF: FD         ???                     
7CE0: FF         RST     0X38            
7CE1: BF         CP      A               
7CE2: FF         RST     0X38            
7CE3: A7         AND     A               
7CE4: FD         ???                     
7CE5: A5         AND     L               
7CE6: FD         ???                     
7CE7: A5         AND     L               
7CE8: FD         ???                     
7CE9: A5         AND     L               
7CEA: FF         RST     0X38            
7CEB: BF         CP      A               
7CEC: FF         RST     0X38            
7CED: 80         ADD     A,B             
7CEE: FF         RST     0X38            
7CEF: BF         CP      A               
7CF0: FF         RST     0X38            
7CF1: E5         PUSH    HL              
7CF2: FF         RST     0X38            
7CF3: E5         PUSH    HL              
7CF4: 3F         CCF                     
7CF5: E5         PUSH    HL              
7CF6: 3F         CCF                     
7CF7: E5         PUSH    HL              
7CF8: 3F         CCF                     
7CF9: E5         PUSH    HL              
7CFA: FF         RST     0X38            
7CFB: FD         ???                     
7CFC: FF         RST     0X38            
7CFD: 01 FF FD   LD      BC,$FDFF        
7D00: 00         NOP                     
7D01: 00         NOP                     
7D02: 67         LD      H,A             
7D03: 67         LD      H,A             
7D04: FF         RST     0X38            
7D05: 99         SBC     C               
7D06: FF         RST     0X38            
7D07: 81         ADD     A,C             
7D08: FF         RST     0X38            
7D09: 81         ADD     A,C             
7D0A: FF         RST     0X38            
7D0B: A5         AND     L               
7D0C: FF         RST     0X38            
7D0D: 81         ADD     A,C             
7D0E: FF         RST     0X38            
7D0F: A9         XOR     C               
7D10: FF         RST     0X38            
7D11: 81         ADD     A,C             
7D12: FB         EI                      
7D13: 95         SUB     L               
7D14: FF         RST     0X38            
7D15: 81         ADD     A,C             
7D16: FF         RST     0X38            
7D17: A5         AND     L               
7D18: FF         RST     0X38            
7D19: 81         ADD     A,C             
7D1A: FF         RST     0X38            
7D1B: 99         SBC     C               
7D1C: E7         RST     0X20            
7D1D: E7         RST     0X20            
7D1E: 00         NOP                     
7D1F: 00         NOP                     
7D20: 00         NOP                     
7D21: 00         NOP                     
7D22: 18 18      JR      $7D3C           
7D24: 24         INC     H               
7D25: 24         INC     H               
7D26: 24         INC     H               
7D27: 24         INC     H               
7D28: 3C         INC     A               
7D29: 3C         INC     A               
7D2A: 7E         LD      A,(HL)          
7D2B: 42         LD      B,D             
7D2C: FF         RST     0X38            
7D2D: A1         AND     C               
7D2E: FF         RST     0X38            
7D2F: B1         OR      C               
7D30: F7         RST     0X30            
7D31: 99         SBC     C               
7D32: F3         DI                      
7D33: 8D         ADC     A,L             
7D34: E7         RST     0X20            
7D35: C3 BD FF   JP      $FFBD           
7D38: 91         SUB     C               
7D39: EF         RST     0X28            
7D3A: 52         LD      D,D             
7D3B: 6E         LD      L,(HL)          
7D3C: 3C         INC     A               
7D3D: 3C         INC     A               
7D3E: 00         NOP                     
7D3F: 00         NOP                     
7D40: 00         NOP                     
7D41: 00         NOP                     
7D42: 3E 3E      LD      A,$3E           
7D44: 41         LD      B,C             
7D45: 41         LD      B,C             
7D46: FF         RST     0X38            
7D47: BF         CP      A               
7D48: FF         RST     0X38            
7D49: C1         POP     BC              
7D4A: FF         RST     0X38            
7D4B: 81         ADD     A,C             
7D4C: FF         RST     0X38            
7D4D: BD         CP      L               
7D4E: C3 81 FF   JP      $FF81           
7D51: 81         ADD     A,C             
7D52: FF         RST     0X38            
7D53: E7         RST     0X20            
7D54: 99         SBC     C               
7D55: 81         ADD     A,C             
7D56: FE 82      CP      $82             
7D58: 7C         LD      A,H             
7D59: 44         LD      B,H             
7D5A: 38 38      JR      C,$7D94         
7D5C: 00         NOP                     
7D5D: 00         NOP                     
7D5E: 00         NOP                     
7D5F: 00         NOP                     
7D60: 00         NOP                     
7D61: 00         NOP                     
7D62: C3 C3 E7   JP      $E7C3           
7D65: A5         AND     L               
7D66: FF         RST     0X38            
7D67: BD         CP      L               
7D68: E7         RST     0X20            
7D69: A5         AND     L               
7D6A: DF         RST     0X18            
7D6B: C3 7E 42   JP      $427E           
7D6E: 7E         LD      A,(HL)          
7D6F: 7E         LD      A,(HL)          
7D70: 1C         INC     E               
7D71: 14         INC     D               
7D72: 1C         INC     E               
7D73: 14         INC     D               
7D74: 3F         CCF                     
7D75: 2F         CPL                     
7D76: 3F         CCF                     
7D77: 29         ADD     HL,HL           
7D78: 3F         CCF                     
7D79: 2B         DEC     HL              
7D7A: 3F         CCF                     
7D7B: 29         ADD     HL,HL           
7D7C: 3F         CCF                     
7D7D: 3F         CCF                     
7D7E: 00         NOP                     
7D7F: 00         NOP                     
7D80: FF         RST     0X38            
7D81: FF         RST     0X38            
7D82: FF         RST     0X38            
7D83: FF         RST     0X38            
7D84: FF         RST     0X38            
7D85: FF         RST     0X38            
7D86: FF         RST     0X38            
7D87: FF         RST     0X38            
7D88: F8 F8      LDHL    SP,$F8          
7D8A: FA FA F8   LD      A,($F8FA)       
7D8D: F8 FF      LDHL    SP,$FF          
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
7D9A: FA FA FA   LD      A,($FAFA)       
7D9D: FA FF FF   LD      A,($FFFF)       
7DA0: 00         NOP                     
7DA1: 00         NOP                     
7DA2: 00         NOP                     
7DA3: 00         NOP                     
7DA4: 7C         LD      A,H             
7DA5: 7C         LD      A,H             
7DA6: FE 82      CP      $82             
7DA8: FE BA      CP      $BA             
7DAA: FE BA      CP      $BA             
7DAC: FE 82      CP      $82             
7DAE: 7C         LD      A,H             
7DAF: 7C         LD      A,H             
7DB0: 38 28      JR      C,$7DDA         
7DB2: 38 28      JR      C,$7DDC         
7DB4: 3E 2E      LD      A,$2E           
7DB6: 3E 2A      LD      A,$2A           
7DB8: 3E 2E      LD      A,$2E           
7DBA: 3E 2A      LD      A,$2A           
7DBC: 3E 3E      LD      A,$3E           
7DBE: 00         NOP                     
7DBF: 00         NOP                     
7DC0: 00         NOP                     
7DC1: 00         NOP                     
7DC2: 00         NOP                     
7DC3: 00         NOP                     
7DC4: FE FE      CP      $FE             
7DC6: FE 82      CP      $82             
7DC8: FE FE      CP      $FE             
7DCA: 00         NOP                     
7DCB: 00         NOP                     
7DCC: 00         NOP                     
7DCD: 00         NOP                     
7DCE: 00         NOP                     
7DCF: 00         NOP                     
7DD0: 00         NOP                     
7DD1: 00         NOP                     
7DD2: 6C         LD      L,H             
7DD3: 00         NOP                     
7DD4: 92         SUB     D               
7DD5: 00         NOP                     
7DD6: 82         ADD     A,D             
7DD7: 00         NOP                     
7DD8: 82         ADD     A,D             
7DD9: 00         NOP                     
7DDA: 44         LD      B,H             
7DDB: 00         NOP                     
7DDC: 28 00      JR      Z,$7DDE         
7DDE: 10 00      STOP    $00             
7DE0: 00         NOP                     
7DE1: 00         NOP                     
7DE2: 6C         LD      L,H             
7DE3: 60         LD      H,B             
7DE4: F2         ???                     
7DE5: 90         SUB     B               
7DE6: C2 B0 82   JP      NZ,$82B0        
7DE9: F0 44      LD      A,($44)         
7DEB: 70         LD      (HL),B          
7DEC: 28 30      JR      Z,$7E1E         
7DEE: 10 10      STOP    $10             
7DF0: 00         NOP                     
7DF1: 00         NOP                     
7DF2: 0F         RRCA                    
7DF3: 0F         RRCA                    
7DF4: 11 11 25   LD      DE,$2511        
7DF7: 21 41 4F   LD      HL,$4F41        
7DFA: 42         LD      B,D             
7DFB: 7E         LD      A,(HL)          
7DFC: 44         LD      B,H             
7DFD: 7C         LD      A,H             
7DFE: 78         LD      A,B             
7DFF: 78         LD      A,B             
7E00: 00         NOP                     
7E01: FF         RST     0X38            
7E02: 00         NOP                     
7E03: 81         ADD     A,C             
7E04: 00         NOP                     
7E05: 81         ADD     A,C             
7E06: 00         NOP                     
7E07: 81         ADD     A,C             
7E08: 00         NOP                     
7E09: 81         ADD     A,C             
7E0A: 00         NOP                     
7E0B: 81         ADD     A,C             
7E0C: 00         NOP                     
7E0D: 81         ADD     A,C             
7E0E: 00         NOP                     
7E0F: FF         RST     0X38            
7E10: 00         NOP                     
7E11: E7         RST     0X20            
7E12: 00         NOP                     
7E13: 81         ADD     A,C             
7E14: 00         NOP                     
7E15: 81         ADD     A,C             
7E16: 00         NOP                     
7E17: 00         NOP                     
7E18: 00         NOP                     
7E19: 00         NOP                     
7E1A: 00         NOP                     
7E1B: 81         ADD     A,C             
7E1C: 00         NOP                     
7E1D: 81         ADD     A,C             
7E1E: 00         NOP                     
7E1F: E7         RST     0X20            
7E20: 00         NOP                     
7E21: FF         RST     0X38            
7E22: 00         NOP                     
7E23: 81         ADD     A,C             
7E24: 00         NOP                     
7E25: 81         ADD     A,C             
7E26: 00         NOP                     
7E27: 80         ADD     A,B             
7E28: 00         NOP                     
7E29: 80         ADD     A,B             
7E2A: 00         NOP                     
7E2B: 81         ADD     A,C             
7E2C: 00         NOP                     
7E2D: 81         ADD     A,C             
7E2E: 00         NOP                     
7E2F: FF         RST     0X38            
7E30: 00         NOP                     
7E31: FF         RST     0X38            
7E32: 00         NOP                     
7E33: 81         ADD     A,C             
7E34: 00         NOP                     
7E35: 81         ADD     A,C             
7E36: 00         NOP                     
7E37: 01 00 01   LD      BC,$0100        
7E3A: 00         NOP                     
7E3B: 81         ADD     A,C             
7E3C: 00         NOP                     
7E3D: 81         ADD     A,C             
7E3E: 00         NOP                     
7E3F: FF         RST     0X38            
7E40: 00         NOP                     
7E41: FF         RST     0X38            
7E42: 00         NOP                     
7E43: 81         ADD     A,C             
7E44: 00         NOP                     
7E45: 81         ADD     A,C             
7E46: 00         NOP                     
7E47: 81         ADD     A,C             
7E48: 00         NOP                     
7E49: 81         ADD     A,C             
7E4A: 00         NOP                     
7E4B: 81         ADD     A,C             
7E4C: 00         NOP                     
7E4D: 81         ADD     A,C             
7E4E: 00         NOP                     
7E4F: E7         RST     0X20            
7E50: 00         NOP                     
7E51: E7         RST     0X20            
7E52: 00         NOP                     
7E53: 81         ADD     A,C             
7E54: 00         NOP                     
7E55: 81         ADD     A,C             
7E56: 00         NOP                     
7E57: 81         ADD     A,C             
7E58: 00         NOP                     
7E59: 81         ADD     A,C             
7E5A: 00         NOP                     
7E5B: 81         ADD     A,C             
7E5C: 00         NOP                     
7E5D: 81         ADD     A,C             
7E5E: 00         NOP                     
7E5F: FF         RST     0X38            
7E60: 00         NOP                     
7E61: E7         RST     0X20            
7E62: 00         NOP                     
7E63: 81         ADD     A,C             
7E64: 00         NOP                     
7E65: 81         ADD     A,C             
7E66: 00         NOP                     
7E67: 81         ADD     A,C             
7E68: 00         NOP                     
7E69: 81         ADD     A,C             
7E6A: 00         NOP                     
7E6B: 81         ADD     A,C             
7E6C: 00         NOP                     
7E6D: 81         ADD     A,C             
7E6E: 00         NOP                     
7E6F: E7         RST     0X20            
7E70: 00         NOP                     
7E71: FF         RST     0X38            
7E72: 00         NOP                     
7E73: 81         ADD     A,C             
7E74: 00         NOP                     
7E75: 81         ADD     A,C             
7E76: 00         NOP                     
7E77: 00         NOP                     
7E78: 00         NOP                     
7E79: 00         NOP                     
7E7A: 00         NOP                     
7E7B: 81         ADD     A,C             
7E7C: 00         NOP                     
7E7D: 81         ADD     A,C             
7E7E: 00         NOP                     
7E7F: FF         RST     0X38            
7E80: 00         NOP                     
7E81: FF         RST     0X38            
7E82: 00         NOP                     
7E83: 81         ADD     A,C             
7E84: 00         NOP                     
7E85: 81         ADD     A,C             
7E86: 00         NOP                     
7E87: 80         ADD     A,B             
7E88: 00         NOP                     
7E89: 80         ADD     A,B             
7E8A: 00         NOP                     
7E8B: 81         ADD     A,C             
7E8C: 00         NOP                     
7E8D: 81         ADD     A,C             
7E8E: 00         NOP                     
7E8F: E7         RST     0X20            
7E90: 00         NOP                     
7E91: FF         RST     0X38            
7E92: 00         NOP                     
7E93: 81         ADD     A,C             
7E94: 00         NOP                     
7E95: 81         ADD     A,C             
7E96: 00         NOP                     
7E97: 01 00 01   LD      BC,$0100        
7E9A: 00         NOP                     
7E9B: 81         ADD     A,C             
7E9C: 00         NOP                     
7E9D: 81         ADD     A,C             
7E9E: 00         NOP                     
7E9F: E7         RST     0X20            
7EA0: 00         NOP                     
7EA1: E7         RST     0X20            
7EA2: 00         NOP                     
7EA3: 81         ADD     A,C             
7EA4: 00         NOP                     
7EA5: 81         ADD     A,C             
7EA6: 00         NOP                     
7EA7: 80         ADD     A,B             
7EA8: 00         NOP                     
7EA9: 80         ADD     A,B             
7EAA: 00         NOP                     
7EAB: 81         ADD     A,C             
7EAC: 00         NOP                     
7EAD: 81         ADD     A,C             
7EAE: 00         NOP                     
7EAF: FF         RST     0X38            
7EB0: 00         NOP                     
7EB1: E7         RST     0X20            
7EB2: 00         NOP                     
7EB3: 81         ADD     A,C             
7EB4: 00         NOP                     
7EB5: 81         ADD     A,C             
7EB6: 00         NOP                     
7EB7: 01 00 01   LD      BC,$0100        
7EBA: 00         NOP                     
7EBB: 81         ADD     A,C             
7EBC: 00         NOP                     
7EBD: 81         ADD     A,C             
7EBE: 00         NOP                     
7EBF: FF         RST     0X38            
7EC0: 00         NOP                     
7EC1: E7         RST     0X20            
7EC2: 00         NOP                     
7EC3: 81         ADD     A,C             
7EC4: 00         NOP                     
7EC5: 81         ADD     A,C             
7EC6: 00         NOP                     
7EC7: 80         ADD     A,B             
7EC8: 00         NOP                     
7EC9: 80         ADD     A,B             
7ECA: 00         NOP                     
7ECB: 81         ADD     A,C             
7ECC: 00         NOP                     
7ECD: 81         ADD     A,C             
7ECE: 00         NOP                     
7ECF: E7         RST     0X20            
7ED0: 00         NOP                     
7ED1: E7         RST     0X20            
7ED2: 00         NOP                     
7ED3: 81         ADD     A,C             
7ED4: 00         NOP                     
7ED5: 81         ADD     A,C             
7ED6: 00         NOP                     
7ED7: 01 00 01   LD      BC,$0100        
7EDA: 00         NOP                     
7EDB: 81         ADD     A,C             
7EDC: 00         NOP                     
7EDD: 81         ADD     A,C             
7EDE: 00         NOP                     
7EDF: E7         RST     0X20            
7EE0: 00         NOP                     
7EE1: FF         RST     0X38            
7EE2: 00         NOP                     
7EE3: 81         ADD     A,C             
7EE4: 00         NOP                     
7EE5: 81         ADD     A,C             
7EE6: 00         NOP                     
7EE7: 00         NOP                     
7EE8: 00         NOP                     
7EE9: 00         NOP                     
7EEA: 00         NOP                     
7EEB: 81         ADD     A,C             
7EEC: 00         NOP                     
7EED: 81         ADD     A,C             
7EEE: 00         NOP                     
7EEF: E7         RST     0X20            
7EF0: 00         NOP                     
7EF1: E7         RST     0X20            
7EF2: 00         NOP                     
7EF3: 81         ADD     A,C             
7EF4: 00         NOP                     
7EF5: 81         ADD     A,C             
7EF6: 00         NOP                     
7EF7: 00         NOP                     
7EF8: 00         NOP                     
7EF9: 00         NOP                     
7EFA: 00         NOP                     
7EFB: 81         ADD     A,C             
7EFC: 00         NOP                     
7EFD: 81         ADD     A,C             
7EFE: 00         NOP                     
7EFF: FF         RST     0X38            
7F00: 00         NOP                     
7F01: 00         NOP                     
7F02: 00         NOP                     
7F03: 00         NOP                     
7F04: 00         NOP                     
7F05: 00         NOP                     
7F06: 00         NOP                     
7F07: 07         RLCA                    
7F08: 04         INC     B               
7F09: 08 0B 10   LD      ($100B),SP      
7F0C: 07         RLCA                    
7F0D: 10 07      STOP    $07             
7F0F: 10 00      STOP    $00             
7F11: 00         NOP                     
7F12: 00         NOP                     
7F13: 00         NOP                     
7F14: 00         NOP                     
7F15: 00         NOP                     
7F16: 00         NOP                     
7F17: E0 20      LDFF00  ($20),A         
7F19: 10 D0      STOP    $D0             
7F1B: 08 E0 08   LD      ($08E0),SP      
7F1E: E0 08      LDFF00  ($08),A         
7F20: 07         RLCA                    
7F21: 10 07      STOP    $07             
7F23: 10 0B      STOP    $0B             
7F25: 10 04      STOP    $04             
7F27: 08 00 07   LD      ($0700),SP      
7F2A: 00         NOP                     
7F2B: 00         NOP                     
7F2C: 00         NOP                     
7F2D: 00         NOP                     
7F2E: 00         NOP                     
7F2F: 00         NOP                     
7F30: E0 08      LDFF00  ($08),A         
7F32: E0 08      LDFF00  ($08),A         
7F34: D0         RET     NC              
7F35: 08 20 10   LD      ($1020),SP      
7F38: 00         NOP                     
7F39: E0 00      LDFF00  ($00),A         
7F3B: 00         NOP                     
7F3C: 00         NOP                     
7F3D: 00         NOP                     
7F3E: 00         NOP                     
7F3F: 00         NOP                     
7F40: 00         NOP                     
7F41: 00         NOP                     
7F42: 00         NOP                     
7F43: 00         NOP                     
7F44: 00         NOP                     
7F45: 00         NOP                     
7F46: FF         RST     0X38            
7F47: 00         NOP                     
7F48: FF         RST     0X38            
7F49: 00         NOP                     
7F4A: 00         NOP                     
7F4B: 00         NOP                     
7F4C: 00         NOP                     
7F4D: 00         NOP                     
7F4E: 00         NOP                     
7F4F: 00         NOP                     
7F50: 00         NOP                     
7F51: 00         NOP                     
7F52: 00         NOP                     
7F53: 00         NOP                     
7F54: 00         NOP                     
7F55: 00         NOP                     
7F56: FF         RST     0X38            
7F57: 00         NOP                     
7F58: FF         RST     0X38            
7F59: 00         NOP                     
7F5A: 00         NOP                     
7F5B: 00         NOP                     
7F5C: 00         NOP                     
7F5D: 00         NOP                     
7F5E: 00         NOP                     
7F5F: 00         NOP                     
7F60: 00         NOP                     
7F61: 00         NOP                     
7F62: 00         NOP                     
7F63: 00         NOP                     
7F64: 00         NOP                     
7F65: 00         NOP                     
7F66: FF         RST     0X38            
7F67: 00         NOP                     
7F68: FF         RST     0X38            
7F69: 00         NOP                     
7F6A: 00         NOP                     
7F6B: 00         NOP                     
7F6C: 00         NOP                     
7F6D: 00         NOP                     
7F6E: 00         NOP                     
7F6F: 00         NOP                     
7F70: FF         RST     0X38            
7F71: FF         RST     0X38            
7F72: 81         ADD     A,C             
7F73: 81         ADD     A,C             
7F74: BD         CP      L               
7F75: BD         CP      L               
7F76: BD         CP      L               
7F77: BD         CP      L               
7F78: 81         ADD     A,C             
7F79: 81         ADD     A,C             
7F7A: FF         RST     0X38            
7F7B: 99         SBC     C               
7F7C: FF         RST     0X38            
7F7D: 81         ADD     A,C             
7F7E: FF         RST     0X38            
7F7F: FF         RST     0X38            
7F80: 00         NOP                     
7F81: 00         NOP                     
7F82: 00         NOP                     
7F83: 00         NOP                     
7F84: 4E         LD      C,(HL)          
7F85: 4E         LD      C,(HL)          
7F86: 48         LD      C,B             
7F87: 48         LD      C,B             
7F88: 4E         LD      C,(HL)          
7F89: 4E         LD      C,(HL)          
7F8A: 48         LD      C,B             
7F8B: 48         LD      C,B             
7F8C: 48         LD      C,B             
7F8D: 48         LD      C,B             
7F8E: 00         NOP                     
7F8F: 00         NOP                     
7F90: 00         NOP                     
7F91: 00         NOP                     
7F92: 00         NOP                     
7F93: 00         NOP                     
7F94: EE EE      XOR     $EE             
7F96: 28 28      JR      Z,$7FC0         
7F98: EE EE      XOR     $EE             
7F9A: 88         ADC     A,B             
7F9B: 88         ADC     A,B             
7F9C: E8 E8      ADD     SP,$E8          
7F9E: 00         NOP                     
7F9F: 00         NOP                     
7FA0: 00         NOP                     
7FA1: 00         NOP                     
7FA2: 00         NOP                     
7FA3: 00         NOP                     
7FA4: EE EE      XOR     $EE             
7FA6: 28 28      JR      Z,$7FD0         
7FA8: EE EE      XOR     $EE             
7FAA: 28 28      JR      Z,$7FD4         
7FAC: E8 E8      ADD     SP,$E8          
7FAE: 00         NOP                     
7FAF: 00         NOP                     
7FB0: 00         NOP                     
7FB1: 00         NOP                     
7FB2: 00         NOP                     
7FB3: 00         NOP                     
7FB4: AE         XOR     (HL)            
7FB5: AE         XOR     (HL)            
7FB6: A8         XOR     B               
7FB7: A8         XOR     B               
7FB8: AE         XOR     (HL)            
7FB9: AE         XOR     (HL)            
7FBA: E8 E8      ADD     SP,$E8          
7FBC: 28 28      JR      Z,$7FE6         
7FBE: 00         NOP                     
7FBF: 00         NOP                     
7FC0: 00         NOP                     
7FC1: 00         NOP                     
7FC2: 00         NOP                     
7FC3: 00         NOP                     
7FC4: 70         LD      (HL),B          
7FC5: 70         LD      (HL),B          
7FC6: 50         LD      D,B             
7FC7: 50         LD      D,B             
7FC8: 7A         LD      A,D             
7FC9: 7A         LD      A,D             
7FCA: 48         LD      C,B             
7FCB: 48         LD      C,B             
7FCC: 78         LD      A,B             
7FCD: 78         LD      A,B             
7FCE: 00         NOP                     
7FCF: 00         NOP                     
7FD0: FF         RST     0X38            
7FD1: FF         RST     0X38            
7FD2: 81         ADD     A,C             
7FD3: 81         ADD     A,C             
7FD4: 81         ADD     A,C             
7FD5: 81         ADD     A,C             
7FD6: FF         RST     0X38            
7FD7: 81         ADD     A,C             
7FD8: 99         SBC     C               
7FD9: E7         RST     0X20            
7FDA: C3 BD FF   JP      $FFBD           
7FDD: 81         ADD     A,C             
7FDE: FF         RST     0X38            
7FDF: FF         RST     0X38            
7FE0: E7         RST     0X20            
7FE1: FF         RST     0X38            
7FE2: BD         CP      L               
7FE3: BD         CP      L               
7FE4: 81         ADD     A,C             
7FE5: 81         ADD     A,C             
7FE6: A5         AND     L               
7FE7: A5         AND     L               
7FE8: A5         AND     L               
7FE9: A5         AND     L               
7FEA: C3 C3 DB   JP      $DBC3           
7FED: DB         ???                     
7FEE: 7E         LD      A,(HL)          
7FEF: FF         RST     0X38            
7FF0: 00         NOP                     
7FF1: FF         RST     0X38            
7FF2: 00         NOP                     
7FF3: FF         RST     0X38            
7FF4: 3C         INC     A               
7FF5: C3 3C C3   JP      $C33C           
7FF8: 3C         INC     A               
7FF9: C3 3C C3   JP      $C33C           
7FFC: 00         NOP                     
7FFD: FF         RST     0X38            
7FFE: 00         NOP                     
7FFF: FF         RST     0X38            
```
