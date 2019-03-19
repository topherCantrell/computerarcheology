![Bank 0D](GBZelda.jpg)

# Bank 0D

>>> cpu Z80GB

>>> memoryTable ram 
[RAM Usage](RAMUse.md)

>>> memoryTable hard 
[Hardware Info](../Hardware.md)

```
4000: 00         NOP                     
4001: 00         NOP                     
4002: 7F         LD      A,A             
4003: 00         NOP                     
4004: 70         LD      (HL),B          
4005: 3F         CCF                     
4006: 78         LD      A,B             
4007: 3F         CCF                     
4008: 5C         LD      E,H             
4009: 3F         CCF                     
400A: 4E         LD      C,(HL)          
400B: 3F         CCF                     
400C: 47         LD      B,A             
400D: 3F         CCF                     
400E: 43         LD      B,E             
400F: 3F         CCF                     
4010: 00         NOP                     
4011: 00         NOP                     
4012: FE 00      CP      $00             
4014: 0E FC      LD      C,$FC           
4016: 1E FC      LD      E,$FC           
4018: 3A         LD      A,(HLD)         
4019: FC         ???                     
401A: 72         LD      (HL),D          
401B: FC         ???                     
401C: E2         LDFF00  (C),A           
401D: FC         ???                     
401E: C2 FC 43   JP      NZ,$43FC        
4021: 3F         CCF                     
4022: 47         LD      B,A             
4023: 3F         CCF                     
4024: 4E         LD      C,(HL)          
4025: 3F         CCF                     
4026: 5C         LD      E,H             
4027: 3F         CCF                     
4028: 78         LD      A,B             
4029: 3F         CCF                     
402A: 70         LD      (HL),B          
402B: 3F         CCF                     
402C: 7F         LD      A,A             
402D: 00         NOP                     
402E: 00         NOP                     
402F: 00         NOP                     
4030: C2 FC E2   JP      NZ,$E2FC        
4033: FC         ???                     
4034: 72         LD      (HL),D          
4035: FC         ???                     
4036: 3A         LD      A,(HLD)         
4037: FC         ???                     
4038: 1E FC      LD      E,$FC           
403A: 0E FC      LD      C,$FC           
403C: FE 00      CP      $00             
403E: 00         NOP                     
403F: 00         NOP                     
4040: 00         NOP                     
4041: 3F         CCF                     
4042: 20 1F      JR      NZ,$4063        
4044: 50         LD      D,B             
4045: 8F         ADC     A,A             
4046: 28 C7      JR      Z,$400F         
4048: 14         INC     D               
4049: E3         ???                     
404A: 0A         LD      A,(BC)          
404B: F1         POP     AF              
404C: 05         DEC     B               
404D: F8 02      LDHL    SP,$02          
404F: FC         ???                     
4050: 00         NOP                     
4051: FC         ???                     
4052: 04         INC     B               
4053: F8 0A      LDHL    SP,$0A          
4055: F1         POP     AF              
4056: 14         INC     D               
4057: E3         ???                     
4058: 28 C7      JR      Z,$4021         
405A: 50         LD      D,B             
405B: 8F         ADC     A,A             
405C: A0         AND     B               
405D: 1F         RRA                     
405E: 40         LD      B,B             
405F: 3F         CCF                     
4060: 02         LD      (BC),A          
4061: FC         ???                     
4062: 05         DEC     B               
4063: F8 0A      LDHL    SP,$0A          
4065: F1         POP     AF              
4066: 14         INC     D               
4067: E3         ???                     
4068: 28 C7      JR      Z,$4031         
406A: 50         LD      D,B             
406B: 8F         ADC     A,A             
406C: 20 1F      JR      NZ,$408D        
406E: 00         NOP                     
406F: 3F         CCF                     
4070: 40         LD      B,B             
4071: 3F         CCF                     
4072: A0         AND     B               
4073: 1F         RRA                     
4074: 50         LD      D,B             
4075: 8F         ADC     A,A             
4076: 28 C7      JR      Z,$403F         
4078: 14         INC     D               
4079: E3         ???                     
407A: 0A         LD      A,(BC)          
407B: F1         POP     AF              
407C: 04         INC     B               
407D: F8 00      LDHL    SP,$00          
407F: FC         ???                     
4080: 00         NOP                     
4081: 00         NOP                     
4082: FF         RST     0X38            
4083: 00         NOP                     
4084: 60         LD      H,B             
4085: 9F         SBC     A               
4086: 00         NOP                     
4087: FF         RST     0X38            
4088: 00         NOP                     
4089: FF         RST     0X38            
408A: 06 FF      LD      B,$FF           
408C: 06 F9      LD      B,$F9           
408E: 00         NOP                     
408F: FF         RST     0X38            
4090: FF         RST     0X38            
4091: FF         RST     0X38            
4092: FF         RST     0X38            
4093: FF         RST     0X38            
4094: 00         NOP                     
4095: FF         RST     0X38            
4096: C0         RET     NZ              
4097: FF         RST     0X38            
4098: 06 F9      LD      B,$F9           
409A: F9         LD      SP,HL           
409B: 06 FF      LD      B,$FF           
409D: FF         RST     0X38            
409E: 18 FF      JR      $409F           
40A0: 40         LD      B,B             
40A1: 3F         CCF                     
40A2: 46         LD      B,(HL)          
40A3: 3D         DEC     A               
40A4: 46         LD      B,(HL)          
40A5: 3D         DEC     A               
40A6: 40         LD      B,B             
40A7: 3F         CCF                     
40A8: 40         LD      B,B             
40A9: 3F         CCF                     
40AA: 60         LD      H,B             
40AB: 1F         RRA                     
40AC: 60         LD      H,B             
40AD: 1F         RRA                     
40AE: 40         LD      B,B             
40AF: 3F         CCF                     
40B0: 63         LD      H,E             
40B1: DF         RST     0X18            
40B2: 53         LD      D,E             
40B3: EF         RST     0X28            
40B4: 53         LD      D,E             
40B5: EF         RST     0X28            
40B6: E3         ???                     
40B7: DF         RST     0X18            
40B8: E3         ???                     
40B9: DF         RST     0X18            
40BA: 63         LD      H,E             
40BB: DF         RST     0X18            
40BC: 6B         LD      L,E             
40BD: DF         RST     0X18            
40BE: 6B         LD      L,E             
40BF: DF         RST     0X18            
40C0: 81         ADD     A,C             
40C1: 00         NOP                     
40C2: 7E         LD      A,(HL)          
40C3: 81         ADD     A,C             
40C4: 85         ADD     A,L             
40C5: FB         EI                      
40C6: 81         ADD     A,C             
40C7: FF         RST     0X38            
40C8: 81         ADD     A,C             
40C9: FF         RST     0X38            
40CA: E3         ???                     
40CB: FF         RST     0X38            
40CC: F7         RST     0X30            
40CD: 3E 3E      LD      A,$3E           
40CF: DD         ???                     
40D0: FF         RST     0X38            
40D1: FF         RST     0X38            
40D2: FF         RST     0X38            
40D3: FF         RST     0X38            
40D4: C1         POP     BC              
40D5: BF         CP      A               
40D6: E1         POP     HL              
40D7: DF         RST     0X18            
40D8: 76         HALT                    
40D9: EB         ???                     
40DA: FD         ???                     
40DB: 36 FF      LD      (HL),$FF        
40DD: FF         RST     0X38            
40DE: 3C         INC     A               
40DF: DB         ???                     
40E0: BE         CP      (HL)            
40E1: 7D         LD      A,L             
40E2: 47         LD      B,A             
40E3: 3E 63      LD      A,$63           
40E5: 1F         RRA                     
40E6: 41         LD      B,C             
40E7: 3F         CCF                     
40E8: 43         LD      B,E             
40E9: 3F         CCF                     
40EA: 47         LD      B,A             
40EB: 3E 46      LD      A,$46           
40ED: 3D         DEC     A               
40EE: BE         CP      (HL)            
40EF: 7D         LD      A,L             
40F0: 6F         LD      L,A             
40F1: DF         RST     0X18            
40F2: 53         LD      D,E             
40F3: FF         RST     0X38            
40F4: F3         DI                      
40F5: 6F         LD      L,A             
40F6: E3         ???                     
40F7: DF         RST     0X18            
40F8: F3         DI                      
40F9: EF         RST     0X28            
40FA: FB         EI                      
40FB: 77         LD      (HL),A          
40FC: 7F         LD      A,A             
40FD: DB         ???                     
40FE: 6F         LD      L,A             
40FF: DF         RST     0X18            
4100: C0         RET     NZ              
4101: FF         RST     0X38            
4102: FF         RST     0X38            
4103: FF         RST     0X38            
4104: 7F         LD      A,A             
4105: F0 70      LD      A,($70)         
4107: FF         RST     0X38            
4108: 78         LD      A,B             
4109: DF         RST     0X18            
410A: 6C         LD      L,H             
410B: DF         RST     0X18            
410C: 67         LD      H,A             
410D: DF         RST     0X18            
410E: 63         LD      H,E             
410F: DF         RST     0X18            
4110: 03         INC     BC              
4111: FF         RST     0X38            
4112: FF         RST     0X38            
4113: FF         RST     0X38            
4114: FE 0F      CP      $0F             
4116: 0E FF      LD      C,$FF           
4118: 1E FB      LD      E,$FB           
411A: 36 FB      LD      (HL),$FB        
411C: E6 FB      AND     $FB             
411E: C6 FB      ADD     $FB             
4120: 63         LD      H,E             
4121: DF         RST     0X18            
4122: 63         LD      H,E             
4123: DF         RST     0X18            
4124: 66         LD      H,(HL)          
4125: DF         RST     0X18            
4126: 6C         LD      L,H             
4127: DF         RST     0X18            
4128: 78         LD      A,B             
4129: DF         RST     0X18            
412A: 7F         LD      A,A             
412B: F0 FF      LD      A,($FF)         
412D: FF         RST     0X38            
412E: C0         RET     NZ              
412F: FF         RST     0X38            
4130: C6 FB      ADD     $FB             
4132: C6 FB      ADD     $FB             
4134: 66         LD      H,(HL)          
4135: FB         EI                      
4136: 36 FB      LD      (HL),$FB        
4138: 1E FB      LD      E,$FB           
413A: FE 0F      CP      $0F             
413C: FF         RST     0X38            
413D: FF         RST     0X38            
413E: 03         INC     BC              
413F: FF         RST     0X38            
4140: 63         LD      H,E             
4141: 5F         LD      E,A             
4142: A3         AND     E               
4143: DF         RST     0X18            
4144: C3 1F 13   JP      $131F           
4147: EF         RST     0X28            
4148: 0B         DEC     BC              
4149: F7         RST     0X30            
414A: 07         RLCA                    
414B: FB         EI                      
414C: FF         RST     0X38            
414D: FF         RST     0X38            
414E: FF         RST     0X38            
414F: FF         RST     0X38            
4150: C6 FA      ADD     $FA             
4152: C5         PUSH    BC              
4153: FB         EI                      
4154: C3 F8 C8   JP      $C8F8           
4157: F7         RST     0X30            
4158: D0         RET     NC              
4159: EF         RST     0X28            
415A: E0 DF      LDFF00  ($DF),A         
415C: FF         RST     0X38            
415D: FF         RST     0X38            
415E: FF         RST     0X38            
415F: FF         RST     0X38            
4160: FF         RST     0X38            
4161: FF         RST     0X38            
4162: FF         RST     0X38            
4163: FF         RST     0X38            
4164: 07         RLCA                    
4165: FB         EI                      
4166: 0B         DEC     BC              
4167: F7         RST     0X30            
4168: 13         INC     DE              
4169: EF         RST     0X28            
416A: C3 1F A3   JP      $A31F           
416D: DF         RST     0X18            
416E: 63         LD      H,E             
416F: 5F         LD      E,A             
4170: FF         RST     0X38            
4171: FF         RST     0X38            
4172: FF         RST     0X38            
4173: FF         RST     0X38            
4174: E0 DF      LDFF00  ($DF),A         
4176: D0         RET     NC              
4177: EF         RST     0X28            
4178: C8         RET     Z               
4179: F7         RST     0X30            
417A: C3 F8 C5   JP      $C5F8           
417D: FB         EI                      
417E: C6 FA      ADD     $FA             
4180: 18 FF      JR      $4181           
4182: FF         RST     0X38            
4183: FF         RST     0X38            
4184: F9         LD      SP,HL           
4185: 06 06      LD      B,$06           
4187: F9         LD      SP,HL           
4188: C0         RET     NZ              
4189: FF         RST     0X38            
418A: 00         NOP                     
418B: FF         RST     0X38            
418C: FF         RST     0X38            
418D: FF         RST     0X38            
418E: FF         RST     0X38            
418F: FF         RST     0X38            
4190: 00         NOP                     
4191: FF         RST     0X38            
4192: 06 F9      LD      B,$F9           
4194: 06 FF      LD      B,$FF           
4196: 00         NOP                     
4197: FF         RST     0X38            
4198: 00         NOP                     
4199: FF         RST     0X38            
419A: 60         LD      H,B             
419B: 9F         SBC     A               
419C: FF         RST     0X38            
419D: 00         NOP                     
419E: 00         NOP                     
419F: 00         NOP                     
41A0: C6 FB      ADD     $FB             
41A2: CA F7 CA   JP      Z,$CAF7         
41A5: F7         RST     0X30            
41A6: C7         RST     0X00            
41A7: FB         EI                      
41A8: C7         RST     0X00            
41A9: FB         EI                      
41AA: C6 FB      ADD     $FB             
41AC: D6 FB      SUB     $FB             
41AE: D6 FB      SUB     $FB             
41B0: 02         LD      (BC),A          
41B1: FC         ???                     
41B2: 62         LD      H,D             
41B3: BC         CP      H               
41B4: 62         LD      H,D             
41B5: BC         CP      H               
41B6: 02         LD      (BC),A          
41B7: FC         ???                     
41B8: 02         LD      (BC),A          
41B9: FC         ???                     
41BA: 06 F8      LD      B,$F8           
41BC: 06 F8      LD      B,$F8           
41BE: 02         LD      (BC),A          
41BF: FC         ???                     
41C0: 3C         INC     A               
41C1: DB         ???                     
41C2: FF         RST     0X38            
41C3: FF         RST     0X38            
41C4: FD         ???                     
41C5: 36 76      LD      (HL),$76        
41C7: EB         ???                     
41C8: E1         POP     HL              
41C9: DF         RST     0X18            
41CA: C1         POP     BC              
41CB: BF         CP      A               
41CC: FF         RST     0X38            
41CD: FF         RST     0X38            
41CE: FF         RST     0X38            
41CF: FF         RST     0X38            
41D0: 3E DD      LD      A,$DD           
41D2: F7         RST     0X30            
41D3: 3E E3      LD      A,$E3           
41D5: FF         RST     0X38            
41D6: 81         ADD     A,C             
41D7: FF         RST     0X38            
41D8: 81         ADD     A,C             
41D9: FF         RST     0X38            
41DA: 85         ADD     A,L             
41DB: FB         EI                      
41DC: 7E         LD      A,(HL)          
41DD: 81         ADD     A,C             
41DE: 81         ADD     A,C             
41DF: 00         NOP                     
41E0: F6 FB      OR      $FB             
41E2: CA FF CF   JP      Z,$CFFF         
41E5: F6 C7      OR      $C7             
41E7: FB         EI                      
41E8: CF         RST     0X08            
41E9: F7         RST     0X30            
41EA: DF         RST     0X18            
41EB: EE FE      XOR     $FE             
41ED: DB         ???                     
41EE: F6 FB      OR      $FB             
41F0: 7D         LD      A,L             
41F1: BE         CP      (HL)            
41F2: E2         LDFF00  (C),A           
41F3: 7C         LD      A,H             
41F4: C6 F8      ADD     $F8             
41F6: 82         ADD     A,D             
41F7: FC         ???                     
41F8: C2 FC E2   JP      NZ,$E2FC        
41FB: 7C         LD      A,H             
41FC: 62         LD      H,D             
41FD: BC         CP      H               
41FE: 7D         LD      A,L             
41FF: BE         CP      (HL)            
4200: 80         ADD     A,B             
4201: 80         ADD     A,B             
4202: 80         ADD     A,B             
4203: 80         ADD     A,B             
4204: 80         ADD     A,B             
4205: 80         ADD     A,B             
4206: FF         RST     0X38            
4207: 80         ADD     A,B             
4208: C0         RET     NZ              
4209: BF         CP      A               
420A: C0         RET     NZ              
420B: BF         CP      A               
420C: C0         RET     NZ              
420D: BF         CP      A               
420E: C0         RET     NZ              
420F: BF         CP      A               
4210: 01 01 01   LD      BC,$0101        
4213: 01 01 01   LD      BC,$0101        
4216: FF         RST     0X38            
4217: 01 03 FD   LD      BC,$FD03        
421A: 03         INC     BC              
421B: FD         ???                     
421C: 03         INC     BC              
421D: FD         ???                     
421E: 03         INC     BC              
421F: FD         ???                     
4220: FF         RST     0X38            
4221: FF         RST     0X38            
4222: C0         RET     NZ              
4223: BC         CP      H               
4224: C1         POP     BC              
4225: BD         CP      L               
4226: C1         POP     BC              
4227: BD         CP      L               
4228: C1         POP     BC              
4229: B9         CP      C               
422A: C3 BB C3   JP      $C3BB           
422D: BB         CP      E               
422E: C0         RET     NZ              
422F: BC         CP      H               
4230: FF         RST     0X38            
4231: FF         RST     0X38            
4232: 03         INC     BC              
4233: 3D         DEC     A               
4234: 83         ADD     A,E             
4235: BD         CP      L               
4236: 83         ADD     A,E             
4237: BD         CP      L               
4238: 83         ADD     A,E             
4239: 9D         SBC     L               
423A: C3 DD C3   JP      $C3DD           
423D: DD         ???                     
423E: 03         INC     BC              
423F: 3D         DEC     A               
4240: FF         RST     0X38            
4241: FF         RST     0X38            
4242: 1F         RRA                     
4243: 00         NOP                     
4244: 10 0F      STOP    $0F             
4246: 10 0F      STOP    $0F             
4248: 10 0F      STOP    $0F             
424A: 10 0F      STOP    $0F             
424C: 10 0F      STOP    $0F             
424E: 10 0F      STOP    $0F             
4250: FF         RST     0X38            
4251: FF         RST     0X38            
4252: FF         RST     0X38            
4253: 01 01 FF   LD      BC,$FF01        
4256: 01 FF 01   LD      BC,$01FF        
4259: FF         RST     0X38            
425A: 01 8F 61   LD      BC,$618F        
425D: 61         LD      H,C             
425E: 7D         LD      A,L             
425F: 7D         LD      A,L             
4260: FF         RST     0X38            
4261: FF         RST     0X38            
4262: FF         RST     0X38            
4263: 80         ADD     A,B             
4264: 80         ADD     A,B             
4265: FF         RST     0X38            
4266: 80         ADD     A,B             
4267: FF         RST     0X38            
4268: 80         ADD     A,B             
4269: FF         RST     0X38            
426A: 80         ADD     A,B             
426B: F1         POP     AF              
426C: 86         ADD     A,(HL)          
426D: 86         ADD     A,(HL)          
426E: BE         CP      (HL)            
426F: BE         CP      (HL)            
4270: FF         RST     0X38            
4271: FF         RST     0X38            
4272: F8 00      LDHL    SP,$00          
4274: 08 F0 08   LD      ($08F0),SP      
4277: F0 08      LD      A,($08)         
4279: F0 08      LD      A,($08)         
427B: F0 08      LD      A,($08)         
427D: F0 08      LD      A,($08)         
427F: F0 BF      LD      A,($BF)         
4281: FF         RST     0X38            
4282: BC         CP      H               
4283: FF         RST     0X38            
4284: FD         ???                     
4285: FF         RST     0X38            
4286: F9         LD      SP,HL           
4287: FF         RST     0X38            
4288: 1F         RRA                     
4289: FF         RST     0X38            
428A: FF         RST     0X38            
428B: FF         RST     0X38            
428C: F1         POP     AF              
428D: FF         RST     0X38            
428E: F7         RST     0X30            
428F: FF         RST     0X38            
4290: BF         CP      A               
4291: FF         RST     0X38            
4292: BC         CP      H               
4293: FF         RST     0X38            
4294: FD         ???                     
4295: FF         RST     0X38            
4296: F9         LD      SP,HL           
4297: FF         RST     0X38            
4298: 9F         SBC     A               
4299: FF         RST     0X38            
429A: FF         RST     0X38            
429B: FF         RST     0X38            
429C: FF         RST     0X38            
429D: 3C         INC     A               
429E: FF         RST     0X38            
429F: 18 FF      JR      $42A0           
42A1: FF         RST     0X38            
42A2: FF         RST     0X38            
42A3: 9E         SBC     (HL)            
42A4: FF         RST     0X38            
42A5: 8C         ADC     A,H             
42A6: DE 80      SBC     $80             
42A8: ED         ???                     
42A9: A1         AND     C               
42AA: D2 B3 CC   JP      NC,$CCB3        
42AD: BF         CP      A               
42AE: C0         RET     NZ              
42AF: BF         CP      A               
42B0: FF         RST     0X38            
42B1: FF         RST     0X38            
42B2: FF         RST     0X38            
42B3: 79         LD      A,C             
42B4: FF         RST     0X38            
42B5: 31 7B 01   LD      SP,$017B        
42B8: B7         OR      A               
42B9: 85         ADD     A,L             
42BA: 4B         LD      C,E             
42BB: CD 33 FD   CALL    $FD33           
42BE: 03         INC     BC              
42BF: FD         ???                     
42C0: 81         ADD     A,C             
42C1: 81         ADD     A,C             
42C2: FF         RST     0X38            
42C3: 81         ADD     A,C             
42C4: FF         RST     0X38            
42C5: FF         RST     0X38            
42C6: 66         LD      H,(HL)          
42C7: C3 66 C3   JP      $C366           
42CA: 7E         LD      A,(HL)          
42CB: E7         RST     0X20            
42CC: FF         RST     0X38            
42CD: FF         RST     0X38            
42CE: FF         RST     0X38            
42CF: FF         RST     0X38            
42D0: FF         RST     0X38            
42D1: FF         RST     0X38            
42D2: FF         RST     0X38            
42D3: 01 17 F1   LD      BC,$F117        
42D6: 2F         CPL                     
42D7: E3         ???                     
42D8: 5F         LD      E,A             
42D9: C7         RST     0X00            
42DA: 5F         LD      E,A             
42DB: C7         RST     0X00            
42DC: 2F         CPL                     
42DD: E3         ???                     
42DE: 17         RLA                     
42DF: F1         POP     AF              
42E0: FF         RST     0X38            
42E1: FF         RST     0X38            
42E2: FF         RST     0X38            
42E3: 80         ADD     A,B             
42E4: E8 8F      ADD     SP,$8F          
42E6: F4         ???                     
42E7: C7         RST     0X00            
42E8: FA E3 FA   LD      A,($FAE3)       
42EB: E3         ???                     
42EC: F4         ???                     
42ED: C7         RST     0X00            
42EE: E8 8F      ADD     SP,$8F          
42F0: FF         RST     0X38            
42F1: FF         RST     0X38            
42F2: FF         RST     0X38            
42F3: FF         RST     0X38            
42F4: 7E         LD      A,(HL)          
42F5: E7         RST     0X20            
42F6: 66         LD      H,(HL)          
42F7: C3 66 C3   JP      $C366           
42FA: FF         RST     0X38            
42FB: FF         RST     0X38            
42FC: FF         RST     0X38            
42FD: 81         ADD     A,C             
42FE: 81         ADD     A,C             
42FF: 81         ADD     A,C             
4300: C0         RET     NZ              
4301: BC         CP      H               
4302: C3 BB C3   JP      $C3BB           
4305: BB         CP      E               
4306: C1         POP     BC              
4307: B9         CP      C               
4308: C1         POP     BC              
4309: BD         CP      L               
430A: C1         POP     BC              
430B: BD         CP      L               
430C: C0         RET     NZ              
430D: BC         CP      H               
430E: FF         RST     0X38            
430F: FF         RST     0X38            
4310: 03         INC     BC              
4311: 3D         DEC     A               
4312: C3 DD C3   JP      $C3DD           
4315: DD         ???                     
4316: 83         ADD     A,E             
4317: 9D         SBC     L               
4318: 83         ADD     A,E             
4319: BD         CP      L               
431A: 83         ADD     A,E             
431B: BD         CP      L               
431C: 03         INC     BC              
431D: 3D         DEC     A               
431E: FF         RST     0X38            
431F: FF         RST     0X38            
4320: C0         RET     NZ              
4321: BF         CP      A               
4322: C0         RET     NZ              
4323: BF         CP      A               
4324: C0         RET     NZ              
4325: BF         CP      A               
4326: C0         RET     NZ              
4327: BF         CP      A               
4328: FF         RST     0X38            
4329: 80         ADD     A,B             
432A: 80         ADD     A,B             
432B: 80         ADD     A,B             
432C: 80         ADD     A,B             
432D: 80         ADD     A,B             
432E: 80         ADD     A,B             
432F: 80         ADD     A,B             
4330: 03         INC     BC              
4331: FD         ???                     
4332: 03         INC     BC              
4333: FD         ???                     
4334: 03         INC     BC              
4335: FD         ???                     
4336: 03         INC     BC              
4337: FD         ???                     
4338: FF         RST     0X38            
4339: 01 01 01   LD      BC,$0101        
433C: 01 01 01   LD      BC,$0101        
433F: 01 10 0F   LD      BC,$0F10        
4342: 10 0F      STOP    $0F             
4344: 10 0F      STOP    $0F             
4346: 10 0F      STOP    $0F             
4348: 10 0F      STOP    $0F             
434A: 10 0F      STOP    $0F             
434C: 1F         RRA                     
434D: 00         NOP                     
434E: FF         RST     0X38            
434F: FF         RST     0X38            
4350: 7D         LD      A,L             
4351: 7D         LD      A,L             
4352: 61         LD      H,C             
4353: 61         LD      H,C             
4354: 01 8F 01   LD      BC,$018F        
4357: FF         RST     0X38            
4358: 01 FF 01   LD      BC,$01FF        
435B: FF         RST     0X38            
435C: FF         RST     0X38            
435D: 01 FF FF   LD      BC,$FFFF        
4360: BE         CP      (HL)            
4361: BE         CP      (HL)            
4362: 86         ADD     A,(HL)          
4363: 86         ADD     A,(HL)          
4364: 80         ADD     A,B             
4365: F1         POP     AF              
4366: 80         ADD     A,B             
4367: FF         RST     0X38            
4368: 80         ADD     A,B             
4369: FF         RST     0X38            
436A: 80         ADD     A,B             
436B: FF         RST     0X38            
436C: FF         RST     0X38            
436D: 80         ADD     A,B             
436E: FF         RST     0X38            
436F: FF         RST     0X38            
4370: 08 F0 08   LD      ($08F0),SP      
4373: F0 08      LD      A,($08)         
4375: F0 08      LD      A,($08)         
4377: F0 08      LD      A,($08)         
4379: F0 08      LD      A,($08)         
437B: F0 F8      LD      A,($F8)         
437D: 00         NOP                     
437E: FF         RST     0X38            
437F: FF         RST     0X38            
4380: C0         RET     NZ              
4381: BF         CP      A               
4382: CC BF D2   CALL    Z,$D2BF         
4385: B3         OR      E               
4386: ED         ???                     
4387: A1         AND     C               
4388: DE 80      SBC     $80             
438A: FF         RST     0X38            
438B: 8C         ADC     A,H             
438C: FF         RST     0X38            
438D: 9E         SBC     (HL)            
438E: FF         RST     0X38            
438F: FF         RST     0X38            
4390: 03         INC     BC              
4391: FD         ???                     
4392: 33         INC     SP              
4393: FD         ???                     
4394: 4B         LD      C,E             
4395: CD B7 85   CALL    $85B7           
4398: 7B         LD      A,E             
4399: 01 FF 31   LD      BC,$31FF        
439C: FF         RST     0X38            
439D: 79         LD      A,C             
439E: FF         RST     0X38            
439F: FF         RST     0X38            
43A0: 02         LD      (BC),A          
43A1: 00         NOP                     
43A2: 20 00      JR      NZ,$43A4        
43A4: 01 00 08   LD      BC,$0800        
43A7: 00         NOP                     
43A8: 80         ADD     A,B             
43A9: 00         NOP                     
43AA: 00         NOP                     
43AB: 00         NOP                     
43AC: 22         LD      (HLI),A         
43AD: 00         NOP                     
43AE: 08 00 00   LD      ($0000),SP      
43B1: 00         NOP                     
43B2: 7E         LD      A,(HL)          
43B3: 00         NOP                     
43B4: 7A         LD      A,D             
43B5: 00         NOP                     
43B6: 5E         LD      E,(HL)          
43B7: 00         NOP                     
43B8: 7E         LD      A,(HL)          
43B9: 00         NOP                     
43BA: 76         HALT                    
43BB: 00         NOP                     
43BC: 7E         LD      A,(HL)          
43BD: 00         NOP                     
43BE: 00         NOP                     
43BF: 00         NOP                     
43C0: E3         ???                     
43C1: FF         RST     0X38            
43C2: 7F         LD      A,A             
43C3: 3F         CCF                     
43C4: 7F         LD      A,A             
43C5: 27         DAA                     
43C6: 67         LD      H,A             
43C7: 23         INC     HL              
43C8: 67         LD      H,A             
43C9: 23         INC     HL              
43CA: 7F         LD      A,A             
43CB: 27         DAA                     
43CC: 7F         LD      A,A             
43CD: 3F         CCF                     
43CE: E3         ???                     
43CF: FF         RST     0X38            
43D0: 17         RLA                     
43D1: F1         POP     AF              
43D2: 2F         CPL                     
43D3: E3         ???                     
43D4: 5F         LD      E,A             
43D5: C7         RST     0X00            
43D6: 5F         LD      E,A             
43D7: C7         RST     0X00            
43D8: 2F         CPL                     
43D9: E3         ???                     
43DA: 17         RLA                     
43DB: F1         POP     AF              
43DC: FF         RST     0X38            
43DD: 01 FF FF   LD      BC,$FFFF        
43E0: E8 8F      ADD     SP,$8F          
43E2: F4         ???                     
43E3: C7         RST     0X00            
43E4: FA E3 FA   LD      A,($FAE3)       
43E7: E3         ???                     
43E8: F4         ???                     
43E9: C7         RST     0X00            
43EA: E8 8F      ADD     SP,$8F          
43EC: FF         RST     0X38            
43ED: 80         ADD     A,B             
43EE: FF         RST     0X38            
43EF: FF         RST     0X38            
43F0: C7         RST     0X00            
43F1: FF         RST     0X38            
43F2: FE FC      CP      $FC             
43F4: FE E4      CP      $E4             
43F6: E6 C4      AND     $C4             
43F8: E6 C4      AND     $C4             
43FA: FE E4      CP      $E4             
43FC: FE FC      CP      $FC             
43FE: C7         RST     0X00            
43FF: FF         RST     0X38            
4400: FF         RST     0X38            
4401: FF         RST     0X38            
4402: 80         ADD     A,B             
4403: 80         ADD     A,B             
4404: 9E         SBC     (HL)            
4405: 9E         SBC     (HL)            
4406: 9E         SBC     (HL)            
4407: 92         SUB     D               
4408: 9E         SBC     (HL)            
4409: 92         SUB     D               
440A: 9E         SBC     (HL)            
440B: 92         SUB     D               
440C: 9E         SBC     (HL)            
440D: 9E         SBC     (HL)            
440E: 80         ADD     A,B             
440F: 80         ADD     A,B             
4410: FF         RST     0X38            
4411: FF         RST     0X38            
4412: 01 01 79   LD      BC,$7901        
4415: 79         LD      A,C             
4416: 79         LD      A,C             
4417: 49         LD      C,C             
4418: 79         LD      A,C             
4419: 49         LD      C,C             
441A: 79         LD      A,C             
441B: 49         LD      C,C             
441C: 79         LD      A,C             
441D: 79         LD      A,C             
441E: 01 01 FF   LD      BC,$FF01        
4421: FF         RST     0X38            
4422: 80         ADD     A,B             
4423: 80         ADD     A,B             
4424: A0         AND     B               
4425: BF         CP      A               
4426: A0         AND     B               
4427: BF         CP      A               
4428: A0         AND     B               
4429: BF         CP      A               
442A: A0         AND     B               
442B: BF         CP      A               
442C: BF         CP      A               
442D: BF         CP      A               
442E: BF         CP      A               
442F: BF         CP      A               
4430: FF         RST     0X38            
4431: FF         RST     0X38            
4432: 01 01 05   LD      BC,$0501        
4435: FD         ???                     
4436: 05         DEC     B               
4437: FD         ???                     
4438: 05         DEC     B               
4439: FD         ???                     
443A: 05         DEC     B               
443B: FD         ???                     
443C: FD         ???                     
443D: FD         ???                     
443E: FD         ???                     
443F: FD         ???                     
4440: 3F         CCF                     
4441: 3F         CCF                     
4442: 40         LD      B,B             
4443: 40         LD      B,B             
4444: 8F         ADC     A,A             
4445: 8F         ADC     A,A             
4446: 9F         SBC     A               
4447: 9F         SBC     A               
4448: 9F         SBC     A               
4449: 9F         SBC     A               
444A: 9F         SBC     A               
444B: 9F         SBC     A               
444C: 9F         SBC     A               
444D: 9F         SBC     A               
444E: 8F         ADC     A,A             
444F: 8F         ADC     A,A             
4450: FC         ???                     
4451: FC         ???                     
4452: 02         LD      (BC),A          
4453: 02         LD      (BC),A          
4454: F1         POP     AF              
4455: F1         POP     AF              
4456: F9         LD      SP,HL           
4457: F9         LD      SP,HL           
4458: F9         LD      SP,HL           
4459: F9         LD      SP,HL           
445A: F9         LD      SP,HL           
445B: F9         LD      SP,HL           
445C: F9         LD      SP,HL           
445D: F9         LD      SP,HL           
445E: F1         POP     AF              
445F: F1         POP     AF              
4460: FF         RST     0X38            
4461: FF         RST     0X38            
4462: C0         RET     NZ              
4463: BF         CP      A               
4464: C1         POP     BC              
4465: BE         CP      (HL)            
4466: C3 BC C7   JP      $C7BC           
4469: B8         CP      B               
446A: CE B1      ADC     $B1             
446C: CC B3 C8   CALL    Z,$C8B3         
446F: B7         OR      A               
4470: FF         RST     0X38            
4471: FF         RST     0X38            
4472: 03         INC     BC              
4473: FD         ???                     
4474: 83         ADD     A,E             
4475: 7D         LD      A,L             
4476: C3 3D E3   JP      $E33D           
4479: 1D         DEC     E               
447A: 73         LD      (HL),E          
447B: 8D         ADC     A,L             
447C: 33         INC     SP              
447D: CD 13 ED   CALL    $ED13           
4480: FF         RST     0X38            
4481: FF         RST     0X38            
4482: 9F         SBC     A               
4483: C1         POP     BC              
4484: 9F         SBC     A               
4485: C1         POP     BC              
4486: 9F         SBC     A               
4487: C1         POP     BC              
4488: 9F         SBC     A               
4489: C1         POP     BC              
448A: 81         ADD     A,C             
448B: C1         POP     BC              
448C: 81         ADD     A,C             
448D: FF         RST     0X38            
448E: FF         RST     0X38            
448F: FF         RST     0X38            
4490: C3 FF 66   JP      $66FF           
4493: 7E         LD      A,(HL)          
4494: 3C         INC     A               
4495: 3C         INC     A               
4496: 18 18      JR      $44B0           
4498: 40         LD      B,B             
4499: 00         NOP                     
449A: 01 00 3C   LD      BC,$3C00        
449D: 00         NOP                     
449E: 42         LD      B,D             
449F: 00         NOP                     
44A0: 00         NOP                     
44A1: FF         RST     0X38            
44A2: 00         NOP                     
44A3: 80         ADD     A,B             
44A4: 20 BF      JR      NZ,$4465        
44A6: 20 BF      JR      NZ,$4467        
44A8: 3F         CCF                     
44A9: BF         CP      A               
44AA: 3F         CCF                     
44AB: BF         CP      A               
44AC: 3F         CCF                     
44AD: BC         CP      H               
44AE: 3F         CCF                     
44AF: BC         CP      H               
44B0: 00         NOP                     
44B1: FF         RST     0X38            
44B2: 00         NOP                     
44B3: 01 7C FD   LD      BC,$FD7C        
44B6: 44         LD      B,H             
44B7: C5         PUSH    BC              
44B8: C4 C5 C4   CALL    NZ,$C4C5        
44BB: C5         PUSH    BC              
44BC: C4 45 C4   CALL    NZ,$C445        
44BF: 45         LD      B,L             
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
44CC: 00         NOP                     
44CD: 00         NOP                     
44CE: 00         NOP                     
44CF: 00         NOP                     
44D0: 00         NOP                     
44D1: 00         NOP                     
44D2: 00         NOP                     
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
44E8: 00         NOP                     
44E9: 00         NOP                     
44EA: 00         NOP                     
44EB: 00         NOP                     
44EC: 00         NOP                     
44ED: 00         NOP                     
44EE: 00         NOP                     
44EF: 00         NOP                     
44F0: 00         NOP                     
44F1: 00         NOP                     
44F2: 00         NOP                     
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
4500: 80         ADD     A,B             
4501: 80         ADD     A,B             
4502: FF         RST     0X38            
4503: FF         RST     0X38            
4504: D5         PUSH    DE              
4505: 9D         SBC     L               
4506: D5         PUSH    DE              
4507: 9D         SBC     L               
4508: D4 9C DF   CALL    NC,$DF9C        
450B: 9F         SBC     A               
450C: C0         RET     NZ              
450D: 80         ADD     A,B             
450E: FF         RST     0X38            
450F: FF         RST     0X38            
4510: 01 01 FF   LD      BC,$FF01        
4513: FF         RST     0X38            
4514: AB         XOR     E               
4515: B9         CP      C               
4516: AB         XOR     E               
4517: B9         CP      C               
4518: 2B         DEC     HL              
4519: 39         ADD     HL,SP           
451A: FB         EI                      
451B: F9         LD      SP,HL           
451C: 03         INC     BC              
451D: 01 FF FF   LD      BC,$FFFF        
4520: 80         ADD     A,B             
4521: 80         ADD     A,B             
4522: C7         RST     0X00            
4523: C0         RET     NZ              
4524: 64         LD      H,H             
4525: E0 34      LDFF00  ($34),A         
4527: F0 36      LD      A,($36)         
4529: F0 63      LD      A,($63)         
452B: E0 C0      LDFF00  ($C0),A         
452D: C0         RET     NZ              
452E: 88         ADC     A,B             
452F: 80         ADD     A,B             
4530: 01 01 8B   LD      BC,$8B01        
4533: 03         INC     BC              
4534: 46         LD      B,(HL)          
4535: 07         RLCA                    
4536: 2C         INC     L               
4537: 0F         RRCA                    
4538: 6C         LD      L,H             
4539: 0F         RRCA                    
453A: C6 07      ADD     $07             
453C: 13         INC     DE              
453D: 03         INC     BC              
453E: 01 01 80   LD      BC,$8001        
4541: 80         ADD     A,B             
4542: 80         ADD     A,B             
4543: C0         RET     NZ              
4544: 80         ADD     A,B             
4545: BF         CP      A               
4546: 80         ADD     A,B             
4547: 80         ADD     A,B             
4548: C4 84 E2   CALL    NZ,$E284        
454B: 42         LD      B,D             
454C: BF         CP      A               
454D: A0         AND     B               
454E: DF         RST     0X18            
454F: FF         RST     0X38            
4550: 01 01 01   LD      BC,$0101        
4553: 03         INC     BC              
4554: 01 FD 01   LD      BC,$01FD        
4557: 01 23 21   LD      BC,$2123        
455A: 47         LD      B,A             
455B: 42         LD      B,D             
455C: FD         ???                     
455D: 05         DEC     B               
455E: FB         EI                      
455F: FF         RST     0X38            
4560: D7         RST     0X10            
4561: 38 93      JR      C,$44F6         
4563: 7C         LD      A,H             
4564: 10 FF      STOP    $FF             
4566: 38 FF      JR      C,$4567         
4568: 7C         LD      A,H             
4569: FF         RST     0X38            
456A: FF         RST     0X38            
456B: FF         RST     0X38            
456C: FF         RST     0X38            
456D: FF         RST     0X38            
456E: FF         RST     0X38            
456F: FF         RST     0X38            
4570: FF         RST     0X38            
4571: FF         RST     0X38            
4572: FF         RST     0X38            
4573: FF         RST     0X38            
4574: FF         RST     0X38            
4575: FF         RST     0X38            
4576: FF         RST     0X38            
4577: FF         RST     0X38            
4578: FF         RST     0X38            
4579: FF         RST     0X38            
457A: FF         RST     0X38            
457B: FF         RST     0X38            
457C: FF         RST     0X38            
457D: 3C         INC     A               
457E: FF         RST     0X38            
457F: 18 00      JR      $4581           
4581: 00         NOP                     
4582: FF         RST     0X38            
4583: FF         RST     0X38            
4584: FF         RST     0X38            
4585: FF         RST     0X38            
4586: 00         NOP                     
4587: 00         NOP                     
4588: 00         NOP                     
4589: 00         NOP                     
458A: FF         RST     0X38            
458B: FF         RST     0X38            
458C: FF         RST     0X38            
458D: FF         RST     0X38            
458E: 00         NOP                     
458F: 00         NOP                     
4590: 62         LD      H,D             
4591: 00         NOP                     
4592: 3C         INC     A               
4593: 00         NOP                     
4594: 18 00      JR      $4596           
4596: 40         LD      B,B             
4597: 00         NOP                     
4598: 1A         LD      A,(DE)          
4599: 18 3C      JR      $45D7           
459B: 3C         INC     A               
459C: 66         LD      H,(HL)          
459D: 7E         LD      A,(HL)          
459E: C3 FF 3F   JP      $3FFF           
45A1: BC         CP      H               
45A2: 27         DAA                     
45A3: BC         CP      H               
45A4: 27         DAA                     
45A5: BC         CP      H               
45A6: 27         DAA                     
45A7: BC         CP      H               
45A8: 27         DAA                     
45A9: BC         CP      H               
45AA: 3F         CCF                     
45AB: BF         CP      A               
45AC: 00         NOP                     
45AD: 80         ADD     A,B             
45AE: 00         NOP                     
45AF: FF         RST     0X38            
45B0: C4 45 C4   CALL    NZ,$C445        
45B3: 45         LD      B,L             
45B4: C4 45 C4   CALL    NZ,$C445        
45B7: 45         LD      B,L             
45B8: C4 45 FC   CALL    NZ,$FC45        
45BB: FD         ???                     
45BC: 00         NOP                     
45BD: 01 00 FF   LD      BC,$FF00        
45C0: FF         RST     0X38            
45C1: 00         NOP                     
45C2: FF         RST     0X38            
45C3: 00         NOP                     
45C4: FF         RST     0X38            
45C5: 00         NOP                     
45C6: FF         RST     0X38            
45C7: 00         NOP                     
45C8: FF         RST     0X38            
45C9: 00         NOP                     
45CA: FF         RST     0X38            
45CB: 00         NOP                     
45CC: FF         RST     0X38            
45CD: 00         NOP                     
45CE: FF         RST     0X38            
45CF: 00         NOP                     
45D0: 00         NOP                     
45D1: FF         RST     0X38            
45D2: 00         NOP                     
45D3: FF         RST     0X38            
45D4: 00         NOP                     
45D5: FF         RST     0X38            
45D6: 00         NOP                     
45D7: FF         RST     0X38            
45D8: 00         NOP                     
45D9: FF         RST     0X38            
45DA: 00         NOP                     
45DB: FF         RST     0X38            
45DC: 00         NOP                     
45DD: FF         RST     0X38            
45DE: 00         NOP                     
45DF: FF         RST     0X38            
45E0: FF         RST     0X38            
45E1: FF         RST     0X38            
45E2: FF         RST     0X38            
45E3: FF         RST     0X38            
45E4: FF         RST     0X38            
45E5: FF         RST     0X38            
45E6: FF         RST     0X38            
45E7: FF         RST     0X38            
45E8: FF         RST     0X38            
45E9: FF         RST     0X38            
45EA: FF         RST     0X38            
45EB: FF         RST     0X38            
45EC: FF         RST     0X38            
45ED: FF         RST     0X38            
45EE: FF         RST     0X38            
45EF: FF         RST     0X38            
45F0: 00         NOP                     
45F1: 00         NOP                     
45F2: 00         NOP                     
45F3: 00         NOP                     
45F4: 00         NOP                     
45F5: 00         NOP                     
45F6: 00         NOP                     
45F7: 00         NOP                     
45F8: 00         NOP                     
45F9: 00         NOP                     
45FA: 00         NOP                     
45FB: 00         NOP                     
45FC: 00         NOP                     
45FD: 00         NOP                     
45FE: 00         NOP                     
45FF: 00         NOP                     
4600: 00         NOP                     
4601: 00         NOP                     
4602: 07         RLCA                    
4603: 00         NOP                     
4604: 04         INC     B               
4605: 03         INC     BC              
4606: 04         INC     B               
4607: 03         INC     BC              
4608: 0C         INC     C               
4609: 03         INC     BC              
460A: 7C         LD      A,H             
460B: 03         INC     BC              
460C: 60         LD      H,B             
460D: 1F         RRA                     
460E: 4F         LD      C,A             
460F: 3F         CCF                     
4610: 00         NOP                     
4611: 00         NOP                     
4612: E0 00      LDFF00  ($00),A         
4614: 60         LD      H,B             
4615: 80         ADD     A,B             
4616: 20 C0      JR      NZ,$45D8        
4618: B0         OR      B               
4619: C0         RET     NZ              
461A: BE         CP      (HL)            
461B: C0         RET     NZ              
461C: 82         ADD     A,D             
461D: FC         ???                     
461E: 82         ADD     A,D             
461F: FC         ???                     
4620: 41         LD      B,C             
4621: 3F         CCF                     
4622: 41         LD      B,C             
4623: 3F         CCF                     
4624: 7D         LD      A,L             
4625: 03         INC     BC              
4626: 0D         DEC     C               
4627: 03         INC     BC              
4628: 04         INC     B               
4629: 03         INC     BC              
462A: 06 01      LD      B,$01           
462C: 07         RLCA                    
462D: 00         NOP                     
462E: 00         NOP                     
462F: 00         NOP                     
4630: F2         ???                     
4631: FC         ???                     
4632: 06 F8      LD      B,$F8           
4634: 3E C0      LD      A,$C0           
4636: 30 C0      JR      NC,$45F8        
4638: 20 C0      JR      NZ,$45FA        
463A: 20 C0      JR      NZ,$45FC        
463C: E0 00      LDFF00  ($00),A         
463E: 00         NOP                     
463F: 00         NOP                     
4640: 01 0F 0C   LD      BC,$0C0F        
4643: 03         INC     BC              
4644: 0E 01      LD      C,$01           
4646: 8E         ADC     A,(HL)          
4647: 01 76 81   LD      BC,$8176        
464A: 7A         LD      A,D             
464B: 81         ADD     A,C             
464C: BC         CP      H               
464D: C3 80 FF   JP      $FF80           
4650: 80         ADD     A,B             
4651: F0 30      LD      A,($30)         
4653: C0         RET     NZ              
4654: 70         LD      (HL),B          
4655: 80         ADD     A,B             
4656: 71         LD      (HL),C          
4657: 80         ADD     A,B             
4658: 6E         LD      L,(HL)          
4659: 81         ADD     A,C             
465A: 5E         LD      E,(HL)          
465B: 81         ADD     A,C             
465C: 3D         DEC     A               
465D: C3 01 FF   JP      $FF01           
4660: 80         ADD     A,B             
4661: FF         RST     0X38            
4662: BC         CP      H               
4663: C3 7A 81   JP      $817A           
4666: 76         HALT                    
4667: 81         ADD     A,C             
4668: 8E         ADC     A,(HL)          
4669: 01 0E 01   LD      BC,$010E        
466C: 0C         INC     C               
466D: 03         INC     BC              
466E: 01 0F 01   LD      BC,$010F        
4671: FF         RST     0X38            
4672: 3D         DEC     A               
4673: C3 5E 81   JP      $815E           
4676: 6E         LD      L,(HL)          
4677: 81         ADD     A,C             
4678: 71         LD      (HL),C          
4679: 80         ADD     A,B             
467A: 70         LD      (HL),B          
467B: 80         ADD     A,B             
467C: 30 C0      JR      NC,$463E        
467E: 80         ADD     A,B             
467F: F0 00      LD      A,($00)         
4681: 00         NOP                     
4682: 01 00 C2   LD      BC,$C200        
4685: 01 66 81   LD      BC,$8166        
4688: 3C         INC     A               
4689: C3 B8 C7   JP      $C7B8           
468C: B0         OR      B               
468D: CF         RST     0X08            
468E: 90         SUB     B               
468F: EF         RST     0X28            
4690: DB         ???                     
4691: E7         RST     0X20            
4692: 66         LD      H,(HL)          
4693: FF         RST     0X38            
4694: 3C         INC     A               
4695: FF         RST     0X38            
4696: 98         SBC     B               
4697: 7F         LD      A,A             
4698: DB         ???                     
4699: 3C         INC     A               
469A: EF         RST     0X28            
469B: 3C         INC     A               
469C: C3 7E 81   JP      $817E           
469F: FF         RST     0X38            
46A0: 40         LD      B,B             
46A1: 3F         CCF                     
46A2: 30 0F      JR      NC,$46B3        
46A4: 18 07      JR      $46AD           
46A6: 0C         INC     C               
46A7: 03         INC     BC              
46A8: 0F         RRCA                    
46A9: 00         NOP                     
46AA: 1E 01      LD      E,$01           
46AC: 30 0F      JR      NC,$46BD        
46AE: 27         DAA                     
46AF: 1F         RRA                     
46B0: F1         POP     AF              
46B1: 8F         ADC     A,A             
46B2: 73         LD      (HL),E          
46B3: CF         RST     0X08            
46B4: 26 FF      LD      H,$FF           
46B6: 3D         DEC     A               
46B7: FE 1D      CP      $1D             
46B9: FE 26      CP      $26             
46BB: FF         RST     0X38            
46BC: 73         LD      (HL),E          
46BD: CF         RST     0X08            
46BE: F9         LD      SP,HL           
46BF: 87         ADD     A,A             
46C0: FF         RST     0X38            
46C1: 00         NOP                     
46C2: BD         CP      L               
46C3: 7E         LD      A,(HL)          
46C4: 7E         LD      A,(HL)          
46C5: FF         RST     0X38            
46C6: DF         RST     0X18            
46C7: E3         ???                     
46C8: BD         CP      L               
46C9: C3 B9 C7   JP      $C7B9           
46CC: 99         SBC     C               
46CD: E7         RST     0X20            
46CE: 89         ADC     A,C             
46CF: F7         RST     0X30            
46D0: DB         ???                     
46D1: E7         RST     0X20            
46D2: 66         LD      H,(HL)          
46D3: FF         RST     0X38            
46D4: 3C         INC     A               
46D5: FF         RST     0X38            
46D6: 98         SBC     B               
46D7: 7F         LD      A,A             
46D8: DB         ???                     
46D9: 3C         INC     A               
46DA: BD         CP      L               
46DB: 7E         LD      A,(HL)          
46DC: 66         LD      H,(HL)          
46DD: FF         RST     0X38            
46DE: C3 FF DF   JP      $DFFF           
46E1: 3F         CCF                     
46E2: B0         OR      B               
46E3: 7F         LD      A,A             
46E4: EC         ???                     
46E5: 73         LD      (HL),E          
46E6: FE 61      CP      $61             
46E8: FF         RST     0X38            
46E9: 60         LD      H,B             
46EA: F8 67      LDHL    SP,$67          
46EC: B0         OR      B               
46ED: 7F         LD      A,A             
46EE: DF         RST     0X18            
46EF: 3F         CCF                     
46F0: B9         CP      C               
46F1: C7         RST     0X00            
46F2: D3         ???                     
46F3: EF         RST     0X28            
46F4: 66         LD      H,(HL)          
46F5: FF         RST     0X38            
46F6: 3D         DEC     A               
46F7: FE 3D      CP      $3D             
46F9: FE 66      CP      $66             
46FB: FF         RST     0X38            
46FC: D3         ???                     
46FD: EF         RST     0X28            
46FE: B1         OR      C               
46FF: CF         RST     0X08            
4700: 83         ADD     A,E             
4701: FE CF      CP      $CF             
4703: FC         ???                     
4704: 77         LD      (HL),A          
4705: F8 33      LDHL    SP,$33          
4707: FC         ???                     
4708: 58         LD      E,B             
4709: FF         RST     0X38            
470A: 8C         ADC     A,H             
470B: FF         RST     0X38            
470C: C6 BF      ADD     $BF             
470E: E3         ???                     
470F: 1F         RRA                     
4710: E3         ???                     
4711: 7F         LD      A,A             
4712: D6 3F      SUB     $3F             
4714: 8C         ADC     A,H             
4715: 7F         LD      A,A             
4716: 1C         INC     E               
4717: FF         RST     0X38            
4718: 32         LD      (HLD),A         
4719: FF         RST     0X38            
471A: 66         LD      H,(HL)          
471B: FB         EI                      
471C: CF         RST     0X08            
471D: F1         POP     AF              
471E: 8F         ADC     A,A             
471F: F0 F1      LD      A,($F1)         
4721: 0F         RRCA                    
4722: F3         DI                      
4723: 8F         ADC     A,A             
4724: 66         LD      H,(HL)          
4725: DF         RST     0X18            
4726: 4C         LD      C,H             
4727: FF         RST     0X38            
4728: 38 FF      JR      C,$4729         
472A: 31 FE 6B   LD      SP,$6BFE        
472D: FC         ???                     
472E: C7         RST     0X00            
472F: FE C7      CP      $C7             
4731: F8 63      LDHL    SP,$63          
4733: FD         ???                     
4734: 31 FF 1A   LD      SP,$1AFF        
4737: FF         RST     0X38            
4738: CC 3F EE   CALL    Z,$EE3F         
473B: 1F         RRA                     
473C: F3         DI                      
473D: 3F         CCF                     
473E: C1         POP     BC              
473F: 7F         LD      A,A             
4740: 81         ADD     A,C             
4741: FF         RST     0X38            
4742: 7F         LD      A,A             
4743: FE 76      CP      $76             
4745: CE 7A      ADC     $7A             
4747: C6 5A      ADD     $5A             
4749: E6 66      AND     $66             
474B: FC         ???                     
474C: 7C         LD      A,H             
474D: F8 E0      LDHL    SP,$E0          
474F: C0         RET     NZ              
4750: 81         ADD     A,C             
4751: FF         RST     0X38            
4752: FE 7F      CP      $7F             
4754: 6E         LD      L,(HL)          
4755: 73         LD      (HL),E          
4756: 5E         LD      E,(HL)          
4757: 63         LD      H,E             
4758: 5A         LD      E,D             
4759: 67         LD      H,A             
475A: 66         LD      H,(HL)          
475B: 3F         CCF                     
475C: 3E 1F      LD      A,$1F           
475E: 07         RLCA                    
475F: 03         INC     BC              
4760: E0 C0      LDFF00  ($C0),A         
4762: 7C         LD      A,H             
4763: F8 66      LDHL    SP,$66          
4765: FC         ???                     
4766: 5A         LD      E,D             
4767: E6 7A      AND     $7A             
4769: C6 76      ADD     $76             
476B: CE 7F      ADC     $7F             
476D: FE 81      CP      $81             
476F: FF         RST     0X38            
4770: 07         RLCA                    
4771: 03         INC     BC              
4772: 3E 1F      LD      A,$1F           
4774: 66         LD      H,(HL)          
4775: 3F         CCF                     
4776: 5A         LD      E,D             
4777: 67         LD      H,A             
4778: 5E         LD      E,(HL)          
4779: 63         LD      H,E             
477A: 6E         LD      L,(HL)          
477B: 73         LD      (HL),E          
477C: FE 7F      CP      $7F             
477E: 81         ADD     A,C             
477F: FF         RST     0X38            
4780: 81         ADD     A,C             
4781: FF         RST     0X38            
4782: C3 7E EF   JP      $EF7E           
4785: 3C         INC     A               
4786: DB         ???                     
4787: 3C         INC     A               
4788: 98         SBC     B               
4789: 7F         LD      A,A             
478A: 3C         INC     A               
478B: FF         RST     0X38            
478C: 66         LD      H,(HL)          
478D: FF         RST     0X38            
478E: DB         ???                     
478F: E7         RST     0X20            
4790: 90         SUB     B               
4791: EF         RST     0X28            
4792: B0         OR      B               
4793: CF         RST     0X08            
4794: B8         CP      B               
4795: C7         RST     0X00            
4796: 3C         INC     A               
4797: C3 66 81   JP      $8166           
479A: C2 01 01   JP      NZ,$0101        
479D: 00         NOP                     
479E: 00         NOP                     
479F: 00         NOP                     
47A0: 9F         SBC     A               
47A1: E1         POP     HL              
47A2: CE F3      ADC     $F3             
47A4: 64         LD      H,H             
47A5: FF         RST     0X38            
47A6: B8         CP      B               
47A7: 7F         LD      A,A             
47A8: BC         CP      H               
47A9: 7F         LD      A,A             
47AA: 64         LD      H,H             
47AB: FF         RST     0X38            
47AC: CE F3      ADC     $F3             
47AE: 8F         ADC     A,A             
47AF: F1         POP     AF              
47B0: E4         ???                     
47B1: F8 0C      LDHL    SP,$0C          
47B3: F0 78      LD      A,($78)         
47B5: 80         ADD     A,B             
47B6: F0 00      LD      A,($00)         
47B8: 30 C0      JR      NC,$477A        
47BA: 18 E0      JR      $479C           
47BC: 0C         INC     C               
47BD: F0 02      LD      A,($02)         
47BF: FC         ???                     
47C0: C3 FF 66   JP      $66FF           
47C3: FF         RST     0X38            
47C4: BD         CP      L               
47C5: 7E         LD      A,(HL)          
47C6: DB         ???                     
47C7: 3C         INC     A               
47C8: 98         SBC     B               
47C9: 7F         LD      A,A             
47CA: 3C         INC     A               
47CB: FF         RST     0X38            
47CC: 66         LD      H,(HL)          
47CD: FF         RST     0X38            
47CE: DB         ???                     
47CF: E7         RST     0X20            
47D0: 89         ADC     A,C             
47D1: F7         RST     0X30            
47D2: 99         SBC     C               
47D3: E7         RST     0X20            
47D4: B9         CP      C               
47D5: C7         RST     0X00            
47D6: BD         CP      L               
47D7: C3 DF E3   JP      $E3DF           
47DA: 7E         LD      A,(HL)          
47DB: FF         RST     0X38            
47DC: BD         CP      L               
47DD: 7E         LD      A,(HL)          
47DE: FF         RST     0X38            
47DF: 00         NOP                     
47E0: 9D         SBC     L               
47E1: E3         ???                     
47E2: CB F7      SET     1,E             
47E4: 66         LD      H,(HL)          
47E5: FF         RST     0X38            
47E6: BC         CP      H               
47E7: 7F         LD      A,A             
47E8: BC         CP      H               
47E9: 7F         LD      A,A             
47EA: 66         LD      H,(HL)          
47EB: FF         RST     0X38            
47EC: CB F7      SET     1,E             
47EE: 8D         ADC     A,L             
47EF: F3         DI                      
47F0: FB         EI                      
47F1: FC         ???                     
47F2: 0D         DEC     C               
47F3: FE 37      CP      $37             
47F5: CE 7F      ADC     $7F             
47F7: 86         ADD     A,(HL)          
47F8: FF         RST     0X38            
47F9: 06 1F      LD      B,$1F           
47FB: E6 0D      AND     $0D             
47FD: FE FB      CP      $FB             
47FF: FC         ???                     
4800: FF         RST     0X38            
4801: 00         NOP                     
4802: 80         ADD     A,B             
4803: 00         NOP                     
4804: 80         ADD     A,B             
4805: 3F         CCF                     
4806: 9F         SBC     A               
4807: 3F         CCF                     
4808: 9F         SBC     A               
4809: 38 9F      JR      C,$47AA         
480B: 34         INC     (HL)            
480C: 9F         SBC     A               
480D: 32         LD      (HLD),A         
480E: 9F         SBC     A               
480F: 31 FF 00   LD      SP,$00FF        
4812: 01 00 01   LD      BC,$0100        
4815: FC         ???                     
4816: F9         LD      SP,HL           
4817: FC         ???                     
4818: F9         LD      SP,HL           
4819: 1C         INC     E               
481A: F9         LD      SP,HL           
481B: 2C         INC     L               
481C: F9         LD      SP,HL           
481D: 4C         LD      C,H             
481E: F9         LD      SP,HL           
481F: 8C         ADC     A,H             
4820: 9F         SBC     A               
4821: 31 9F 32   LD      SP,$329F        
4824: 9F         SBC     A               
4825: 34         INC     (HL)            
4826: 9F         SBC     A               
4827: 38 9F      JR      C,$47C8         
4829: 3F         CCF                     
482A: 80         ADD     A,B             
482B: 3F         CCF                     
482C: 80         ADD     A,B             
482D: 00         NOP                     
482E: FF         RST     0X38            
482F: 00         NOP                     
4830: F9         LD      SP,HL           
4831: 8C         ADC     A,H             
4832: F9         LD      SP,HL           
4833: 4C         LD      C,H             
4834: F9         LD      SP,HL           
4835: 2C         INC     L               
4836: F9         LD      SP,HL           
4837: 1C         INC     E               
4838: F9         LD      SP,HL           
4839: FC         ???                     
483A: 01 FC 01   LD      BC,$01FC        
483D: 00         NOP                     
483E: FF         RST     0X38            
483F: 00         NOP                     
4840: 9F         SBC     A               
4841: 30 1F      JR      NC,$4862        
4843: 30 1F      JR      NC,$4864        
4845: F0 FF      LD      A,($FF)         
4847: F0 F7      LD      A,($F7)         
4849: 00         NOP                     
484A: FB         EI                      
484B: 00         NOP                     
484C: FD         ???                     
484D: 00         NOP                     
484E: FE 00      CP      $00             
4850: F9         LD      SP,HL           
4851: 0C         INC     C               
4852: F8 0C      LDHL    SP,$0C          
4854: F8 0F      LDHL    SP,$0F          
4856: FF         RST     0X38            
4857: 0F         RRCA                    
4858: EF         RST     0X28            
4859: 00         NOP                     
485A: DF         RST     0X18            
485B: 00         NOP                     
485C: BF         CP      A               
485D: 00         NOP                     
485E: 7F         LD      A,A             
485F: 00         NOP                     
4860: FE 00      CP      $00             
4862: FD         ???                     
4863: 00         NOP                     
4864: FB         EI                      
4865: 00         NOP                     
4866: F7         RST     0X30            
4867: 00         NOP                     
4868: FF         RST     0X38            
4869: F0 1F      LD      A,($1F)         
486B: F0 1F      LD      A,($1F)         
486D: 30 9F      JR      NC,$480E        
486F: 30 7F      JR      NC,$48F0        
4871: 00         NOP                     
4872: BF         CP      A               
4873: 00         NOP                     
4874: DF         RST     0X18            
4875: 00         NOP                     
4876: EF         RST     0X28            
4877: 00         NOP                     
4878: FF         RST     0X38            
4879: 0F         RRCA                    
487A: F8 0F      LDHL    SP,$0F          
487C: F8 0C      LDHL    SP,$0C          
487E: F9         LD      SP,HL           
487F: 0C         INC     C               
4880: FF         RST     0X38            
4881: 00         NOP                     
4882: 00         NOP                     
4883: 00         NOP                     
4884: 00         NOP                     
4885: FF         RST     0X38            
4886: FF         RST     0X38            
4887: FF         RST     0X38            
4888: FF         RST     0X38            
4889: 00         NOP                     
488A: FF         RST     0X38            
488B: 00         NOP                     
488C: FF         RST     0X38            
488D: 00         NOP                     
488E: FF         RST     0X38            
488F: 00         NOP                     
4890: FF         RST     0X38            
4891: FF         RST     0X38            
4892: FF         RST     0X38            
4893: FF         RST     0X38            
4894: 40         LD      B,B             
4895: FF         RST     0X38            
4896: FF         RST     0X38            
4897: FF         RST     0X38            
4898: 04         INC     B               
4899: FF         RST     0X38            
489A: 04         INC     B               
489B: FF         RST     0X38            
489C: FF         RST     0X38            
489D: 04         INC     B               
489E: FF         RST     0X38            
489F: FF         RST     0X38            
48A0: 9F         SBC     A               
48A1: 30 9F      JR      NC,$4842        
48A3: 30 9F      JR      NC,$4844        
48A5: 30 9F      JR      NC,$4846        
48A7: 30 9F      JR      NC,$4848        
48A9: 30 9F      JR      NC,$484A        
48AB: 30 9F      JR      NC,$484C        
48AD: 30 9F      JR      NC,$484E        
48AF: 30 CB      JR      NC,$487C        
48B1: BF         CP      A               
48B2: CB BF      SET     1,E             
48B4: CB BF      SET     1,E             
48B6: FB         EI                      
48B7: FF         RST     0X38            
48B8: CB BF      SET     1,E             
48BA: CB BF      SET     1,E             
48BC: CF         RST     0X08            
48BD: BF         CP      A               
48BE: CB BF      SET     1,E             
48C0: 81         ADD     A,C             
48C1: 00         NOP                     
48C2: 7E         LD      A,(HL)          
48C3: 81         ADD     A,C             
48C4: 85         ADD     A,L             
48C5: FB         EI                      
48C6: 81         ADD     A,C             
48C7: FF         RST     0X38            
48C8: 81         ADD     A,C             
48C9: FF         RST     0X38            
48CA: E3         ???                     
48CB: FF         RST     0X38            
48CC: F7         RST     0X30            
48CD: 3E 3E      LD      A,$3E           
48CF: DD         ???                     
48D0: FF         RST     0X38            
48D1: FF         RST     0X38            
48D2: 83         ADD     A,E             
48D3: FF         RST     0X38            
48D4: C1         POP     BC              
48D5: BF         CP      A               
48D6: E1         POP     HL              
48D7: DF         RST     0X18            
48D8: 76         HALT                    
48D9: EB         ???                     
48DA: FD         ???                     
48DB: 36 FF      LD      (HL),$FF        
48DD: FF         RST     0X38            
48DE: 3C         INC     A               
48DF: DB         ???                     
48E0: BE         CP      (HL)            
48E1: 7D         LD      A,L             
48E2: 47         LD      B,A             
48E3: 3E 63      LD      A,$63           
48E5: 1F         RRA                     
48E6: 41         LD      B,C             
48E7: 3F         CCF                     
48E8: 43         LD      B,E             
48E9: 3F         CCF                     
48EA: 47         LD      B,A             
48EB: 3E 46      LD      A,$46           
48ED: 3D         DEC     A               
48EE: BE         CP      (HL)            
48EF: 7D         LD      A,L             
48F0: 6F         LD      L,A             
48F1: DF         RST     0X18            
48F2: 53         LD      D,E             
48F3: FF         RST     0X38            
48F4: F1         POP     AF              
48F5: 6F         LD      L,A             
48F6: E1         POP     HL              
48F7: DF         RST     0X18            
48F8: F1         POP     AF              
48F9: EF         RST     0X28            
48FA: F9         LD      SP,HL           
48FB: 77         LD      (HL),A          
48FC: 7D         LD      A,L             
48FD: DB         ???                     
48FE: 6F         LD      L,A             
48FF: DF         RST     0X18            
4900: FF         RST     0X38            
4901: FF         RST     0X38            
4902: FF         RST     0X38            
4903: C0         RET     NZ              
4904: E0 BF      LDFF00  ($BF),A         
4906: D0         RET     NC              
4907: BF         CP      A               
4908: CF         RST     0X08            
4909: BF         CP      A               
490A: CC BF CB   CALL    Z,$CBBF         
490D: BF         CP      A               
490E: CB BF      SET     1,E             
4910: FF         RST     0X38            
4911: FF         RST     0X38            
4912: FF         RST     0X38            
4913: 03         INC     BC              
4914: 07         RLCA                    
4915: FD         ???                     
4916: 0B         DEC     BC              
4917: FD         ???                     
4918: F3         DI                      
4919: FD         ???                     
491A: 33         INC     SP              
491B: FD         ???                     
491C: D3         ???                     
491D: FD         ???                     
491E: D3         ???                     
491F: FD         ???                     
4920: CB BF      SET     1,E             
4922: CB BF      SET     1,E             
4924: CC BF CF   CALL    Z,$CFBF         
4927: BF         CP      A               
4928: D0         RET     NC              
4929: BF         CP      A               
492A: E0 BF      LDFF00  ($BF),A         
492C: FF         RST     0X38            
492D: C0         RET     NZ              
492E: FF         RST     0X38            
492F: FF         RST     0X38            
4930: D3         ???                     
4931: FD         ???                     
4932: D3         ???                     
4933: FD         ???                     
4934: 33         INC     SP              
4935: FD         ???                     
4936: F3         DI                      
4937: FD         ???                     
4938: 0B         DEC     BC              
4939: FD         ???                     
493A: 07         RLCA                    
493B: FD         ???                     
493C: FF         RST     0X38            
493D: 03         INC     BC              
493E: FF         RST     0X38            
493F: FF         RST     0X38            
4940: CB BF      SET     1,E             
4942: CB 3F      SET     1,E             
4944: 2B         DEC     HL              
4945: DF         RST     0X18            
4946: 1B         DEC     DE              
4947: EF         RST     0X28            
4948: FB         EI                      
4949: FF         RST     0X38            
494A: 07         RLCA                    
494B: FB         EI                      
494C: FF         RST     0X38            
494D: FF         RST     0X38            
494E: FF         RST     0X38            
494F: FF         RST     0X38            
4950: D3         ???                     
4951: FD         ???                     
4952: D3         ???                     
4953: FC         ???                     
4954: D4 FB D8   CALL    NC,$D8FB        
4957: F7         RST     0X30            
4958: DF         RST     0X18            
4959: FF         RST     0X38            
495A: E0 DF      LDFF00  ($DF),A         
495C: FF         RST     0X38            
495D: FF         RST     0X38            
495E: FF         RST     0X38            
495F: FF         RST     0X38            
4960: FF         RST     0X38            
4961: FF         RST     0X38            
4962: FF         RST     0X38            
4963: FF         RST     0X38            
4964: 07         RLCA                    
4965: FB         EI                      
4966: FB         EI                      
4967: FF         RST     0X38            
4968: 1B         DEC     DE              
4969: EF         RST     0X28            
496A: 2B         DEC     HL              
496B: DF         RST     0X18            
496C: CB 3F      SET     1,E             
496E: CB BF      SET     1,E             
4970: FF         RST     0X38            
4971: FF         RST     0X38            
4972: FF         RST     0X38            
4973: FF         RST     0X38            
4974: E0 DF      LDFF00  ($DF),A         
4976: DF         RST     0X18            
4977: FF         RST     0X38            
4978: D8         RET     C               
4979: F7         RST     0X30            
497A: D4 FB D3   CALL    NC,$D3FB        
497D: FC         ???                     
497E: D3         ???                     
497F: FD         ???                     
4980: FF         RST     0X38            
4981: FF         RST     0X38            
4982: FF         RST     0X38            
4983: 04         INC     B               
4984: 04         INC     B               
4985: FF         RST     0X38            
4986: 04         INC     B               
4987: FF         RST     0X38            
4988: FF         RST     0X38            
4989: FF         RST     0X38            
498A: 40         LD      B,B             
498B: FF         RST     0X38            
498C: FF         RST     0X38            
498D: FF         RST     0X38            
498E: FF         RST     0X38            
498F: FF         RST     0X38            
4990: FF         RST     0X38            
4991: 00         NOP                     
4992: FF         RST     0X38            
4993: 00         NOP                     
4994: FF         RST     0X38            
4995: 00         NOP                     
4996: FF         RST     0X38            
4997: 00         NOP                     
4998: FF         RST     0X38            
4999: FF         RST     0X38            
499A: 00         NOP                     
499B: FF         RST     0X38            
499C: 00         NOP                     
499D: 00         NOP                     
499E: FF         RST     0X38            
499F: 00         NOP                     
49A0: D3         ???                     
49A1: FD         ???                     
49A2: D3         ???                     
49A3: FD         ???                     
49A4: D3         ???                     
49A5: FD         ???                     
49A6: DF         RST     0X18            
49A7: FF         RST     0X38            
49A8: D3         ???                     
49A9: FD         ???                     
49AA: D3         ???                     
49AB: FD         ???                     
49AC: F3         DI                      
49AD: FD         ???                     
49AE: D3         ???                     
49AF: FD         ???                     
49B0: F9         LD      SP,HL           
49B1: 0C         INC     C               
49B2: F9         LD      SP,HL           
49B3: 0C         INC     C               
49B4: F9         LD      SP,HL           
49B5: 0C         INC     C               
49B6: F9         LD      SP,HL           
49B7: 0C         INC     C               
49B8: F9         LD      SP,HL           
49B9: 0C         INC     C               
49BA: F9         LD      SP,HL           
49BB: 0C         INC     C               
49BC: F9         LD      SP,HL           
49BD: 0C         INC     C               
49BE: F9         LD      SP,HL           
49BF: 0C         INC     C               
49C0: 3C         INC     A               
49C1: DB         ???                     
49C2: FF         RST     0X38            
49C3: FF         RST     0X38            
49C4: FD         ???                     
49C5: 36 76      LD      (HL),$76        
49C7: EB         ???                     
49C8: E1         POP     HL              
49C9: DF         RST     0X18            
49CA: C1         POP     BC              
49CB: BF         CP      A               
49CC: 83         ADD     A,E             
49CD: FF         RST     0X38            
49CE: FF         RST     0X38            
49CF: FF         RST     0X38            
49D0: 3E DD      LD      A,$DD           
49D2: F7         RST     0X30            
49D3: 3E E3      LD      A,$E3           
49D5: FF         RST     0X38            
49D6: 81         ADD     A,C             
49D7: FF         RST     0X38            
49D8: 81         ADD     A,C             
49D9: FF         RST     0X38            
49DA: 85         ADD     A,L             
49DB: FB         EI                      
49DC: 7E         LD      A,(HL)          
49DD: 81         ADD     A,C             
49DE: 81         ADD     A,C             
49DF: 00         NOP                     
49E0: F6 FB      OR      $FB             
49E2: CA FF 8F   JP      Z,$8FFF         
49E5: F6 87      OR      $87             
49E7: FB         EI                      
49E8: 8F         ADC     A,A             
49E9: F7         RST     0X30            
49EA: 9F         SBC     A               
49EB: EE BE      XOR     $BE             
49ED: DB         ???                     
49EE: F6 FB      OR      $FB             
49F0: 7D         LD      A,L             
49F1: BE         CP      (HL)            
49F2: E2         LDFF00  (C),A           
49F3: 7C         LD      A,H             
49F4: C6 F8      ADD     $F8             
49F6: 82         ADD     A,D             
49F7: FC         ???                     
49F8: C2 FC E2   JP      NZ,$E2FC        
49FB: 7C         LD      A,H             
49FC: 62         LD      H,D             
49FD: BC         CP      H               
49FE: 7D         LD      A,L             
49FF: BE         CP      (HL)            
4A00: 00         NOP                     
4A01: 00         NOP                     
4A02: 6F         LD      L,A             
4A03: 70         LD      (HL),B          
4A04: 75         LD      (HL),L          
4A05: 7A         LD      A,D             
4A06: 3A         LD      A,(HLD)         
4A07: 7D         LD      A,L             
4A08: 5C         LD      E,H             
4A09: 3F         CCF                     
4A0A: 6E         LD      L,(HL)          
4A0B: 1F         RRA                     
4A0C: 57         LD      D,A             
4A0D: 2F         CPL                     
4A0E: 63         LD      H,E             
4A0F: 1F         RRA                     
4A10: 00         NOP                     
4A11: 00         NOP                     
4A12: F6 0E      OR      $0E             
4A14: AE         XOR     (HL)            
4A15: 5E         LD      E,(HL)          
4A16: 5C         LD      E,H             
4A17: BE         CP      (HL)            
4A18: 3A         LD      A,(HLD)         
4A19: FC         ???                     
4A1A: 76         HALT                    
4A1B: F8 EA      LDHL    SP,$EA          
4A1D: F4         ???                     
4A1E: C6 F8      ADD     $F8             
4A20: 63         LD      H,E             
4A21: 1F         RRA                     
4A22: 57         LD      D,A             
4A23: 2F         CPL                     
4A24: 6E         LD      L,(HL)          
4A25: 1F         RRA                     
4A26: 5C         LD      E,H             
4A27: 3F         CCF                     
4A28: 3A         LD      A,(HLD)         
4A29: 7D         LD      A,L             
4A2A: 75         LD      (HL),L          
4A2B: 7A         LD      A,D             
4A2C: 6F         LD      L,A             
4A2D: 70         LD      (HL),B          
4A2E: 00         NOP                     
4A2F: 00         NOP                     
4A30: C6 F8      ADD     $F8             
4A32: EA F4 76   LD      ($76F4),A       
4A35: F8 3A      LDHL    SP,$3A          
4A37: FC         ???                     
4A38: 5C         LD      E,H             
4A39: BE         CP      (HL)            
4A3A: AE         XOR     (HL)            
4A3B: 5E         LD      E,(HL)          
4A3C: F6 0E      OR      $0E             
4A3E: 00         NOP                     
4A3F: 00         NOP                     
4A40: 18 07      JR      $4A49           
4A42: 10 0F      STOP    $0F             
4A44: 08 07 C0   LD      ($C007),SP      
4A47: 07         RLCA                    
4A48: A0         AND     B               
4A49: 43         LD      B,E             
4A4A: 40         LD      B,B             
4A4B: B1         OR      C               
4A4C: 00         NOP                     
4A4D: F8 00      LDHL    SP,$00          
4A4F: FC         ???                     
4A50: 18 E0      JR      $4A32           
4A52: 08 F0 10   LD      ($10F0),SP      
4A55: E0 03      LDFF00  ($03),A         
4A57: E0 05      LDFF00  ($05),A         
4A59: C2 02 8D   JP      NZ,$8D02        
4A5C: 00         NOP                     
4A5D: 1F         RRA                     
4A5E: 00         NOP                     
4A5F: 3F         CCF                     
4A60: 00         NOP                     
4A61: FC         ???                     
4A62: 00         NOP                     
4A63: F8 40      LDHL    SP,$40          
4A65: B1         OR      C               
4A66: A0         AND     B               
4A67: 43         LD      B,E             
4A68: C0         RET     NZ              
4A69: 07         RLCA                    
4A6A: 08 07 10   LD      ($1007),SP      
4A6D: 0F         RRCA                    
4A6E: 18 07      JR      $4A77           
4A70: 00         NOP                     
4A71: 3F         CCF                     
4A72: 00         NOP                     
4A73: 1F         RRA                     
4A74: 02         LD      (BC),A          
4A75: 8D         ADC     A,L             
4A76: 05         DEC     B               
4A77: C2 03 E0   JP      NZ,$E003        
4A7A: 10 E0      STOP    $E0             
4A7C: 08 F0 18   LD      ($18F0),SP      
4A7F: E0 00      LDFF00  ($00),A         
4A81: 00         NOP                     
4A82: 99         SBC     C               
4A83: 00         NOP                     
4A84: FE 01      CP      $01             
4A86: 5B         LD      E,E             
4A87: A4         AND     H               
4A88: 84         ADD     A,H             
4A89: 7B         LD      A,E             
4A8A: 00         NOP                     
4A8B: FF         RST     0X38            
4A8C: 10 FF      STOP    $FF             
4A8E: 02         LD      (BC),A          
4A8F: FF         RST     0X38            
4A90: FF         RST     0X38            
4A91: FF         RST     0X38            
4A92: FF         RST     0X38            
4A93: FF         RST     0X38            
4A94: EE FF      XOR     $FF             
4A96: 7D         LD      A,L             
4A97: FF         RST     0X38            
4A98: D7         RST     0X10            
4A99: FF         RST     0X38            
4A9A: 44         LD      B,H             
4A9B: FF         RST     0X38            
4A9C: 11 FF 40   LD      DE,$40FF        
4A9F: FF         RST     0X38            
4AA0: 50         LD      D,B             
4AA1: 2F         CPL                     
4AA2: 31 0F 28   LD      SP,$280F        
4AA5: 17         RLA                     
4AA6: 70         LD      (HL),B          
4AA7: 0F         RRCA                    
4AA8: 72         LD      (HL),D          
4AA9: 0F         RRCA                    
4AAA: 20 1F      JR      NZ,$4ACB        
4AAC: 30 0F      JR      NC,$4ABD        
4AAE: 68         LD      L,B             
4AAF: 17         RLA                     
4AB0: 17         RLA                     
4AB1: FF         RST     0X38            
4AB2: BF         CP      A               
4AB3: FF         RST     0X38            
4AB4: 0F         RRCA                    
4AB5: FF         RST     0X38            
4AB6: 5B         LD      E,E             
4AB7: FF         RST     0X38            
4AB8: 0F         RRCA                    
4AB9: FF         RST     0X38            
4ABA: 3F         CCF                     
4ABB: FF         RST     0X38            
4ABC: 17         RLA                     
4ABD: FF         RST     0X38            
4ABE: 5B         LD      E,E             
4ABF: FF         RST     0X38            
4AC0: 81         ADD     A,C             
4AC1: 00         NOP                     
4AC2: 76         HALT                    
4AC3: 89         ADC     A,C             
4AC4: 89         ADC     A,C             
4AC5: F7         RST     0X30            
4AC6: A3         AND     E               
4AC7: DD         ???                     
4AC8: 89         ADC     A,C             
4AC9: FF         RST     0X38            
4ACA: E3         ???                     
4ACB: FF         RST     0X38            
4ACC: F7         RST     0X30            
4ACD: 3E 3E      LD      A,$3E           
4ACF: DD         ???                     
4AD0: FF         RST     0X38            
4AD1: FF         RST     0X38            
4AD2: FF         RST     0X38            
4AD3: FF         RST     0X38            
4AD4: F7         RST     0X30            
4AD5: BF         CP      A               
4AD6: FD         ???                     
4AD7: DF         RST     0X18            
4AD8: 76         HALT                    
4AD9: EB         ???                     
4ADA: 3C         INC     A               
4ADB: F7         RST     0X30            
4ADC: 3D         DEC     A               
4ADD: FF         RST     0X38            
4ADE: 3C         INC     A               
4ADF: DB         ???                     
4AE0: BE         CP      (HL)            
4AE1: 7D         LD      A,L             
4AE2: 57         LD      D,A             
4AE3: 2E 43      LD      L,$43           
4AE5: 3F         CCF                     
4AE6: 29         ADD     HL,HL           
4AE7: 5F         LD      E,A             
4AE8: 43         LD      B,E             
4AE9: 3F         CCF                     
4AEA: 57         LD      D,A             
4AEB: 2E 46      LD      L,$46           
4AED: 3D         DEC     A               
4AEE: BE         CP      (HL)            
4AEF: 7D         LD      A,L             
4AF0: 4F         LD      C,A             
4AF1: FF         RST     0X38            
4AF2: 17         RLA                     
4AF3: FF         RST     0X38            
4AF4: FF         RST     0X38            
4AF5: 6F         LD      L,A             
4AF6: EB         ???                     
4AF7: DF         RST     0X18            
4AF8: FF         RST     0X38            
4AF9: EF         RST     0X28            
4AFA: FF         RST     0X38            
4AFB: 77         LD      (HL),A          
4AFC: 1F         RRA                     
4AFD: FB         EI                      
4AFE: 0F         RRCA                    
4AFF: FF         RST     0X38            
4B00: C0         RET     NZ              
4B01: FF         RST     0X38            
4B02: E4         ???                     
4B03: FF         RST     0X38            
4B04: 70         LD      (HL),B          
4B05: FF         RST     0X38            
4B06: 3A         LD      A,(HLD)         
4B07: FF         RST     0X38            
4B08: 1D         DEC     E               
4B09: FF         RST     0X38            
4B0A: 9F         SBC     A               
4B0B: FF         RST     0X38            
4B0C: 07         RLCA                    
4B0D: FF         RST     0X38            
4B0E: 2F         CPL                     
4B0F: FF         RST     0X38            
4B10: 03         INC     BC              
4B11: FF         RST     0X38            
4B12: 27         DAA                     
4B13: FF         RST     0X38            
4B14: 0E FF      LD      C,$FF           
4B16: 5C         LD      E,H             
4B17: FF         RST     0X38            
4B18: B8         CP      B               
4B19: FF         RST     0X38            
4B1A: F9         LD      SP,HL           
4B1B: FF         RST     0X38            
4B1C: E0 FF      LDFF00  ($FF),A         
4B1E: F4         ???                     
4B1F: FF         RST     0X38            
4B20: 2F         CPL                     
4B21: FF         RST     0X38            
4B22: 07         RLCA                    
4B23: FF         RST     0X38            
4B24: 9F         SBC     A               
4B25: FF         RST     0X38            
4B26: 1D         DEC     E               
4B27: FF         RST     0X38            
4B28: 3A         LD      A,(HLD)         
4B29: FF         RST     0X38            
4B2A: 70         LD      (HL),B          
4B2B: FF         RST     0X38            
4B2C: E4         ???                     
4B2D: FF         RST     0X38            
4B2E: C0         RET     NZ              
4B2F: FF         RST     0X38            
4B30: F4         ???                     
4B31: FF         RST     0X38            
4B32: E0 FF      LDFF00  ($FF),A         
4B34: F9         LD      SP,HL           
4B35: FF         RST     0X38            
4B36: B8         CP      B               
4B37: FF         RST     0X38            
4B38: 5C         LD      E,H             
4B39: FF         RST     0X38            
4B3A: 0E FF      LD      C,$FF           
4B3C: 27         DAA                     
4B3D: FF         RST     0X38            
4B3E: 03         INC     BC              
4B3F: FF         RST     0X38            
4B40: 57         LD      D,A             
4B41: 3F         CCF                     
4B42: AF         XOR     A               
4B43: 1F         RRA                     
4B44: 43         LD      B,E             
4B45: 9F         SBC     A               
4B46: 87         ADD     A,A             
4B47: EF         RST     0X28            
4B48: 23         INC     HL              
4B49: F7         RST     0X30            
4B4A: B3         OR      E               
4B4B: FF         RST     0X38            
4B4C: FD         ???                     
4B4D: FF         RST     0X38            
4B4E: FF         RST     0X38            
4B4F: FF         RST     0X38            
4B50: EA FC F5   LD      ($F5FC),A       
4B53: F8 C2      LDHL    SP,$C2          
4B55: F9         LD      SP,HL           
4B56: E1         POP     HL              
4B57: F7         RST     0X30            
4B58: C4 EF CD   CALL    NZ,$CDEF        
4B5B: FF         RST     0X38            
4B5C: BF         CP      A               
4B5D: FF         RST     0X38            
4B5E: FF         RST     0X38            
4B5F: FF         RST     0X38            
4B60: FF         RST     0X38            
4B61: FF         RST     0X38            
4B62: FD         ???                     
4B63: FF         RST     0X38            
4B64: B3         OR      E               
4B65: FF         RST     0X38            
4B66: 23         INC     HL              
4B67: F7         RST     0X30            
4B68: 87         ADD     A,A             
4B69: EF         RST     0X28            
4B6A: 43         LD      B,E             
4B6B: 9F         SBC     A               
4B6C: AF         XOR     A               
4B6D: 1F         RRA                     
4B6E: 57         LD      D,A             
4B6F: 3F         CCF                     
4B70: FF         RST     0X38            
4B71: FF         RST     0X38            
4B72: BF         CP      A               
4B73: FF         RST     0X38            
4B74: CD FF C4   CALL    $C4FF           
4B77: EF         RST     0X28            
4B78: E1         POP     HL              
4B79: F7         RST     0X30            
4B7A: C2 F9 F5   JP      NZ,$F5F9        
4B7D: F8 EA      LDHL    SP,$EA          
4B7F: FC         ???                     
4B80: 40         LD      B,B             
4B81: FF         RST     0X38            
4B82: 11 FF 44   LD      DE,$44FF        
4B85: FF         RST     0X38            
4B86: D7         RST     0X10            
4B87: FF         RST     0X38            
4B88: 7D         LD      A,L             
4B89: FF         RST     0X38            
4B8A: EE FF      XOR     $FF             
4B8C: FF         RST     0X38            
4B8D: FF         RST     0X38            
4B8E: FF         RST     0X38            
4B8F: FF         RST     0X38            
4B90: 02         LD      (BC),A          
4B91: FF         RST     0X38            
4B92: 10 FF      STOP    $FF             
4B94: 00         NOP                     
4B95: FF         RST     0X38            
4B96: 84         ADD     A,H             
4B97: 7B         LD      A,E             
4B98: 5B         LD      E,E             
4B99: A4         AND     H               
4B9A: FE 01      CP      $01             
4B9C: 99         SBC     C               
4B9D: 00         NOP                     
4B9E: 00         NOP                     
4B9F: 00         NOP                     
4BA0: E8 FF      ADD     SP,$FF          
4BA2: FD         ???                     
4BA3: FF         RST     0X38            
4BA4: F0 FF      LD      A,($FF)         
4BA6: DA FF F0   JP      C,$F0FF         
4BA9: FF         RST     0X38            
4BAA: FC         ???                     
4BAB: FF         RST     0X38            
4BAC: E8 FF      ADD     SP,$FF          
4BAE: DA FF 0A   JP      C,$0AFF         
4BB1: F4         ???                     
4BB2: 8C         ADC     A,H             
4BB3: F0 14      LD      A,($14)         
4BB5: E8 0E      ADD     SP,$0E          
4BB7: F0 4E      LD      A,($4E)         
4BB9: F0 04      LD      A,($04)         
4BBB: F8 0C      LDHL    SP,$0C          
4BBD: F0 16      LD      A,($16)         
4BBF: E8 3C      ADD     SP,$3C          
4BC1: DB         ???                     
4BC2: 3D         DEC     A               
4BC3: FF         RST     0X38            
4BC4: 3C         INC     A               
4BC5: F7         RST     0X30            
4BC6: 76         HALT                    
4BC7: EB         ???                     
4BC8: FD         ???                     
4BC9: DF         RST     0X18            
4BCA: F7         RST     0X30            
4BCB: BF         CP      A               
4BCC: FF         RST     0X38            
4BCD: FF         RST     0X38            
4BCE: FF         RST     0X38            
4BCF: FF         RST     0X38            
4BD0: 3E DD      LD      A,$DD           
4BD2: F7         RST     0X30            
4BD3: 3E E3      LD      A,$E3           
4BD5: FF         RST     0X38            
4BD6: 89         ADC     A,C             
4BD7: FF         RST     0X38            
4BD8: A3         AND     E               
4BD9: DD         ???                     
4BDA: 89         ADC     A,C             
4BDB: F7         RST     0X30            
4BDC: 76         HALT                    
4BDD: 89         ADC     A,C             
4BDE: 81         ADD     A,C             
4BDF: 00         NOP                     
4BE0: F2         ???                     
4BE1: FF         RST     0X38            
4BE2: E8 FF      ADD     SP,$FF          
4BE4: FF         RST     0X38            
4BE5: F6 D7      OR      $D7             
4BE7: FB         EI                      
4BE8: FF         RST     0X38            
4BE9: F7         RST     0X30            
4BEA: FF         RST     0X38            
4BEB: EE F8      XOR     $F8             
4BED: DF         RST     0X18            
4BEE: F0 FF      LD      A,($FF)         
4BF0: 7D         LD      A,L             
4BF1: BE         CP      (HL)            
4BF2: EA 74 C2   LD      ($C274),A       
4BF5: FC         ???                     
4BF6: 94         SUB     H               
4BF7: FA C2 FC   LD      A,($FCC2)       
4BFA: EA 74 62   LD      ($6274),A       
4BFD: BC         CP      H               
4BFE: 7D         LD      A,L             
4BFF: BE         CP      (HL)            
4C00: 41         LD      B,C             
4C01: 00         NOP                     
4C02: 41         LD      B,C             
4C03: 00         NOP                     
4C04: 45         LD      B,L             
4C05: 00         NOP                     
4C06: C1         POP     BC              
4C07: 00         NOP                     
4C08: E3         ???                     
4C09: 00         NOP                     
4C0A: FC         ???                     
4C0B: 00         NOP                     
4C0C: 38 00      JR      C,$4C0E         
4C0E: 12         LD      (DE),A          
4C0F: 00         NOP                     
4C10: F8 00      LDHL    SP,$00          
4C12: 18 00      JR      $4C14           
4C14: 0C         INC     C               
4C15: 00         NOP                     
4C16: 04         INC     B               
4C17: 00         NOP                     
4C18: 87         ADD     A,A             
4C19: 00         NOP                     
4C1A: C7         RST     0X00            
4C1B: 00         NOP                     
4C1C: 44         LD      B,H             
4C1D: 00         NOP                     
4C1E: 6C         LD      L,H             
4C1F: 00         NOP                     
4C20: 50         LD      D,B             
4C21: 00         NOP                     
4C22: 10 00      STOP    $00             
4C24: 91         SUB     C               
4C25: 00         NOP                     
4C26: 18 00      JR      $4C28           
4C28: 3C         INC     A               
4C29: 00         NOP                     
4C2A: E3         ???                     
4C2B: 00         NOP                     
4C2C: C1         POP     BC              
4C2D: 00         NOP                     
4C2E: C9         RET                     
4C2F: 00         NOP                     
4C30: 38 00      JR      C,$4C32         
4C32: 3A         LD      A,(HLD)         
4C33: 00         NOP                     
4C34: 38 00      JR      C,$4C36         
4C36: 64         LD      H,H             
4C37: 00         NOP                     
4C38: C6 00      ADD     $00             
4C3A: 93         SUB     E               
4C3B: 00         NOP                     
4C3C: 83         ADD     A,E             
4C3D: 00         NOP                     
4C3E: FF         RST     0X38            
4C3F: 00         NOP                     
4C40: 00         NOP                     
4C41: 00         NOP                     
4C42: 00         NOP                     
4C43: 00         NOP                     
4C44: 00         NOP                     
4C45: 00         NOP                     
4C46: 07         RLCA                    
4C47: 07         RLCA                    
4C48: 0C         INC     C               
4C49: 08 1B 10   LD      ($101B),SP      
4C4C: 17         RLA                     
4C4D: 10 17      STOP    $17             
4C4F: 10 00      STOP    $00             
4C51: 00         NOP                     
4C52: 00         NOP                     
4C53: 00         NOP                     
4C54: 00         NOP                     
4C55: 00         NOP                     
4C56: E0 E0      LDFF00  ($E0),A         
4C58: 30 10      JR      NC,$4C6A        
4C5A: D8         RET     C               
4C5B: 08 E8 08   LD      ($08E8),SP      
4C5E: E8 08      ADD     SP,$08          
4C60: 17         RLA                     
4C61: 10 1B      STOP    $1B             
4C63: 10 14      STOP    $14             
4C65: 18 08      JR      $4C6F           
4C67: 0F         RRCA                    
4C68: 07         RLCA                    
4C69: 07         RLCA                    
4C6A: 00         NOP                     
4C6B: 00         NOP                     
4C6C: 00         NOP                     
4C6D: 00         NOP                     
4C6E: 00         NOP                     
4C6F: 00         NOP                     
4C70: E8 08      ADD     SP,$08          
4C72: D8         RET     C               
4C73: 08 28 18   LD      ($1828),SP      
4C76: 10 F0      STOP    $F0             
4C78: E0 E0      LDFF00  ($E0),A         
4C7A: 00         NOP                     
4C7B: 00         NOP                     
4C7C: 00         NOP                     
4C7D: 00         NOP                     
4C7E: 00         NOP                     
4C7F: 00         NOP                     
4C80: 00         NOP                     
4C81: 00         NOP                     
4C82: 3F         CCF                     
4C83: 00         NOP                     
4C84: 41         LD      B,C             
4C85: 00         NOP                     
4C86: 41         LD      B,C             
4C87: 00         NOP                     
4C88: 41         LD      B,C             
4C89: 00         NOP                     
4C8A: 42         LD      B,D             
4C8B: 00         NOP                     
4C8C: 45         LD      B,L             
4C8D: 00         NOP                     
4C8E: 7B         LD      A,E             
4C8F: 00         NOP                     
4C90: 00         NOP                     
4C91: 00         NOP                     
4C92: 7C         LD      A,H             
4C93: 00         NOP                     
4C94: 7E         LD      A,(HL)          
4C95: 00         NOP                     
4C96: 7E         LD      A,(HL)          
4C97: 00         NOP                     
4C98: 7E         LD      A,(HL)          
4C99: 00         NOP                     
4C9A: 0E 00      LD      C,$00           
4C9C: F6 00      OR      $00             
4C9E: F8 00      LDHL    SP,$00          
4CA0: 07         RLCA                    
4CA1: 00         NOP                     
4CA2: 7B         LD      A,E             
4CA3: 00         NOP                     
4CA4: 7D         LD      A,L             
4CA5: 00         NOP                     
4CA6: 7E         LD      A,(HL)          
4CA7: 00         NOP                     
4CA8: 7E         LD      A,(HL)          
4CA9: 00         NOP                     
4CAA: 7E         LD      A,(HL)          
4CAB: 00         NOP                     
4CAC: 3E 00      LD      A,$00           
4CAE: 00         NOP                     
4CAF: 00         NOP                     
4CB0: F6 00      OR      $00             
4CB2: EA 00 D2   LD      ($D200),A       
4CB5: 00         NOP                     
4CB6: 22         LD      (HLI),A         
4CB7: 00         NOP                     
4CB8: C2 00 82   JP      NZ,$8200        
4CBB: 00         NOP                     
4CBC: FC         ???                     
4CBD: 00         NOP                     
4CBE: 00         NOP                     
4CBF: 00         NOP                     
4CC0: 00         NOP                     
4CC1: 81         ADD     A,C             
4CC2: 00         NOP                     
4CC3: 81         ADD     A,C             
4CC4: 42         LD      B,D             
4CC5: 81         ADD     A,C             
4CC6: 64         LD      H,H             
4CC7: 83         ADD     A,E             
4CC8: 98         SBC     B               
4CC9: 67         LD      H,A             
4CCA: C0         RET     NZ              
4CCB: 3F         CCF                     
4CCC: 43         LD      B,E             
4CCD: 3C         INC     A               
4CCE: 27         DAA                     
4CCF: 18 F8      JR      $4CC9           
4CD1: 00         NOP                     
4CD2: 18 00      JR      $4CD4           
4CD4: 2C         INC     L               
4CD5: 10 D0      STOP    $D0             
4CD7: 24         INC     H               
4CD8: 20 C7      JR      NZ,$4CA1        
4CDA: 29         ADD     HL,HL           
4CDB: C6 3A      ADD     $3A             
4CDD: C4 00 FC   CALL    NZ,$FC00        
4CE0: 6D         LD      L,L             
4CE1: 12         LD      (DE),A          
4CE2: 2F         CPL                     
4CE3: 10 AE      STOP    $AE             
4CE5: 11 2F 10   LD      DE,$102F        
4CE8: 47         LD      B,A             
4CE9: 38 98      JR      C,$4C83         
4CEB: 67         LD      H,A             
4CEC: 22         LD      (HLI),A         
4CED: C1         POP     BC              
4CEE: C9         RET                     
4CEF: 00         NOP                     
4CF0: 84         ADD     A,H             
4CF1: 78         LD      A,B             
4CF2: C2 38 C0   JP      NZ,$C038        
4CF5: 38 D4      JR      C,$4CCB         
4CF7: 28 AA      JR      Z,$4CA3         
4CF9: 44         LD      B,H             
4CFA: 55         LD      D,L             
4CFB: 82         ADD     A,D             
4CFC: 45         LD      B,L             
4CFD: 82         ADD     A,D             
4CFE: 3F         CCF                     
4CFF: C0         RET     NZ              
4D00: 06 00      LD      B,$00           
4D02: 28 01      JR      Z,$4D05         
4D04: 0C         INC     C               
4D05: 03         INC     BC              
4D06: 00         NOP                     
4D07: 00         NOP                     
4D08: 20 00      JR      NZ,$4D0A        
4D0A: 02         LD      (BC),A          
4D0B: 00         NOP                     
4D0C: 60         LD      H,B             
4D0D: 00         NOP                     
4D0E: B1         OR      C               
4D0F: 00         NOP                     
4D10: 20 00      JR      NZ,$4D12        
4D12: 00         NOP                     
4D13: 00         NOP                     
4D14: 00         NOP                     
4D15: 00         NOP                     
4D16: 10 00      STOP    $00             
4D18: 20 08      JR      NZ,$4D22        
4D1A: 28 10      JR      Z,$4D2C         
4D1C: 00         NOP                     
4D1D: 00         NOP                     
4D1E: 80         ADD     A,B             
4D1F: 00         NOP                     
4D20: E1         POP     HL              
4D21: 10 11      STOP    $11             
4D23: 60         LD      H,B             
4D24: 00         NOP                     
4D25: 00         NOP                     
4D26: 0C         INC     C               
4D27: 00         NOP                     
4D28: 56         LD      D,(HL)          
4D29: 00         NOP                     
4D2A: 0C         INC     C               
4D2B: 12         LD      (DE),A          
4D2C: 12         LD      (DE),A          
4D2D: 0C         INC     C               
4D2E: 00         NOP                     
4D2F: 00         NOP                     
4D30: 42         LD      B,D             
4D31: 00         NOP                     
4D32: C0         RET     NZ              
4D33: 00         NOP                     
4D34: 00         NOP                     
4D35: 00         NOP                     
4D36: 00         NOP                     
4D37: 00         NOP                     
4D38: 18 00      JR      $4D3A           
4D3A: 2C         INC     L               
4D3B: 00         NOP                     
4D3C: 38 04      JR      C,$4D42         
4D3E: 04         INC     B               
4D3F: 18 00      JR      $4D41           
4D41: 00         NOP                     
4D42: 00         NOP                     
4D43: 00         NOP                     
4D44: 00         NOP                     
4D45: 00         NOP                     
4D46: 07         RLCA                    
4D47: 07         RLCA                    
4D48: 0C         INC     C               
4D49: 08 1B 10   LD      ($101B),SP      
4D4C: 17         RLA                     
4D4D: 10 17      STOP    $17             
4D4F: 10 00      STOP    $00             
4D51: 00         NOP                     
4D52: 00         NOP                     
4D53: 00         NOP                     
4D54: 00         NOP                     
4D55: 00         NOP                     
4D56: E0 E0      LDFF00  ($E0),A         
4D58: 30 10      JR      NC,$4D6A        
4D5A: D8         RET     C               
4D5B: 08 E8 08   LD      ($08E8),SP      
4D5E: E8 08      ADD     SP,$08          
4D60: 17         RLA                     
4D61: 10 1B      STOP    $1B             
4D63: 10 14      STOP    $14             
4D65: 18 08      JR      $4D6F           
4D67: 0F         RRCA                    
4D68: 07         RLCA                    
4D69: 07         RLCA                    
4D6A: 00         NOP                     
4D6B: 00         NOP                     
4D6C: 00         NOP                     
4D6D: 00         NOP                     
4D6E: 00         NOP                     
4D6F: 00         NOP                     
4D70: E8 08      ADD     SP,$08          
4D72: D8         RET     C               
4D73: 08 28 18   LD      ($1828),SP      
4D76: 10 F0      STOP    $F0             
4D78: E0 E0      LDFF00  ($E0),A         
4D7A: 00         NOP                     
4D7B: 00         NOP                     
4D7C: 00         NOP                     
4D7D: 00         NOP                     
4D7E: 00         NOP                     
4D7F: 00         NOP                     
4D80: 00         NOP                     
4D81: 00         NOP                     
4D82: 00         NOP                     
4D83: 18 00      JR      $4D85           
4D85: 25         DEC     H               
4D86: 10 49      STOP    $49             
4D88: 20 50      JR      NZ,$4DDA        
4D8A: 00         NOP                     
4D8B: 6F         LD      L,A             
4D8C: 00         NOP                     
4D8D: 10 00      STOP    $00             
4D8F: 2C         INC     L               
4D90: 00         NOP                     
4D91: 7C         LD      A,H             
4D92: 00         NOP                     
4D93: 82         ADD     A,D             
4D94: 82         ADD     A,D             
4D95: 3D         DEC     A               
4D96: 00         NOP                     
4D97: C3 00 00   JP      $0000           
4D9A: 00         NOP                     
4D9B: 06 00      LD      B,$00           
4D9D: C9         RET                     
4D9E: 00         NOP                     
4D9F: 2B         DEC     HL              
4DA0: 00         NOP                     
4DA1: 29         ADD     HL,HL           
4DA2: 00         NOP                     
4DA3: 21 01 28   LD      HL,$2801        
4DA6: 02         LD      (BC),A          
4DA7: 41         LD      B,C             
4DA8: 04         INC     B               
4DA9: 53         LD      D,E             
4DAA: 00         NOP                     
4DAB: 76         HALT                    
4DAC: 00         NOP                     
4DAD: 1D         DEC     E               
4DAE: 00         NOP                     
4DAF: 01 00 AA   LD      BC,$AA00        
4DB2: 44         LD      B,H             
4DB3: AA         XOR     D               
4DB4: C4 2A 00   CALL    NZ,$002A        
4DB7: CA 00 12   JP      Z,$1200         
4DBA: 00         NOP                     
4DBB: DA 40 2E   JP      C,$2E40         
4DBE: 00         NOP                     
4DBF: C0         RET     NZ              
4DC0: 22         LD      (HLI),A         
4DC1: 00         NOP                     
4DC2: 3E 00      LD      A,$00           
4DC4: E2         LDFF00  (C),A           
4DC5: 00         NOP                     
4DC6: 40         LD      B,B             
4DC7: 01 40 01   LD      BC,$0140        
4DCA: 20 02      JR      NZ,$4DCE        
4DCC: 00         NOP                     
4DCD: 1C         INC     E               
4DCE: 00         NOP                     
4DCF: 04         INC     B               
4DD0: 10 00      STOP    $00             
4DD2: 09         ADD     HL,BC           
4DD3: 00         NOP                     
4DD4: 02         LD      (BC),A          
4DD5: 0C         INC     C               
4DD6: 00         NOP                     
4DD7: 08 00 F8   LD      ($F800),SP      
4DDA: 00         NOP                     
4DDB: 24         INC     H               
4DDC: 00         NOP                     
4DDD: 22         LD      (HLI),A         
4DDE: 00         NOP                     
4DDF: 41         LD      B,C             
4DE0: 02         LD      (BC),A          
4DE1: 04         INC     B               
4DE2: 03         INC     BC              
4DE3: 07         RLCA                    
4DE4: C1         POP     BC              
4DE5: 09         ADD     HL,BC           
4DE6: 20 10      JR      NZ,$4DF8        
4DE8: 10 00      STOP    $00             
4DEA: 18 00      JR      $4DEC           
4DEC: 67         LD      H,A             
4DED: 00         NOP                     
4DEE: 01 00 40   LD      BC,$4000        
4DF1: 41         LD      B,C             
4DF2: E0 F9      LDFF00  ($F9),A         
4DF4: C0         RET     NZ              
4DF5: 86         ADD     A,(HL)          
4DF6: 80         ADD     A,B             
4DF7: 84         ADD     A,H             
4DF8: 00         NOP                     
4DF9: 84         ADD     A,H             
4DFA: 3E C0      LD      A,$C0           
4DFC: 01 00 00   LD      BC,$0000        
4DFF: 00         NOP                     
4E00: 00         NOP                     
4E01: 00         NOP                     
4E02: 00         NOP                     
4E03: 00         NOP                     
4E04: 60         LD      H,B             
4E05: 00         NOP                     
4E06: 00         NOP                     
4E07: 00         NOP                     
4E08: 00         NOP                     
4E09: 00         NOP                     
4E0A: 00         NOP                     
4E0B: 00         NOP                     
4E0C: 00         NOP                     
4E0D: 00         NOP                     
4E0E: FF         RST     0X38            
4E0F: 00         NOP                     
4E10: 00         NOP                     
4E11: 00         NOP                     
4E12: 00         NOP                     
4E13: 00         NOP                     
4E14: 00         NOP                     
4E15: 00         NOP                     
4E16: 00         NOP                     
4E17: 00         NOP                     
4E18: E0 00      LDFF00  ($00),A         
4E1A: 00         NOP                     
4E1B: 00         NOP                     
4E1C: 00         NOP                     
4E1D: 00         NOP                     
4E1E: FF         RST     0X38            
4E1F: 00         NOP                     
4E20: 38 00      JR      C,$4E22         
4E22: 00         NOP                     
4E23: 00         NOP                     
4E24: 00         NOP                     
4E25: 00         NOP                     
4E26: 00         NOP                     
4E27: 00         NOP                     
4E28: 00         NOP                     
4E29: 00         NOP                     
4E2A: 00         NOP                     
4E2B: 00         NOP                     
4E2C: 01 00 FF   LD      BC,$FF00        
4E2F: 00         NOP                     
4E30: 00         NOP                     
4E31: 00         NOP                     
4E32: 00         NOP                     
4E33: 00         NOP                     
4E34: 00         NOP                     
4E35: 00         NOP                     
4E36: 0C         INC     C               
4E37: 00         NOP                     
4E38: 00         NOP                     
4E39: 00         NOP                     
4E3A: 00         NOP                     
4E3B: 00         NOP                     
4E3C: C0         RET     NZ              
4E3D: 00         NOP                     
4E3E: FF         RST     0X38            
4E3F: 00         NOP                     
4E40: 00         NOP                     
4E41: 00         NOP                     
4E42: 00         NOP                     
4E43: 00         NOP                     
4E44: 00         NOP                     
4E45: 00         NOP                     
4E46: 07         RLCA                    
4E47: 07         RLCA                    
4E48: 0C         INC     C               
4E49: 08 1B 10   LD      ($101B),SP      
4E4C: 17         RLA                     
4E4D: 10 17      STOP    $17             
4E4F: 10 00      STOP    $00             
4E51: 00         NOP                     
4E52: 00         NOP                     
4E53: 00         NOP                     
4E54: 00         NOP                     
4E55: 00         NOP                     
4E56: E0 E0      LDFF00  ($E0),A         
4E58: 30 10      JR      NC,$4E6A        
4E5A: D8         RET     C               
4E5B: 08 E8 08   LD      ($08E8),SP      
4E5E: E8 08      ADD     SP,$08          
4E60: 17         RLA                     
4E61: 10 1B      STOP    $1B             
4E63: 10 14      STOP    $14             
4E65: 18 08      JR      $4E6F           
4E67: 0F         RRCA                    
4E68: 07         RLCA                    
4E69: 07         RLCA                    
4E6A: 00         NOP                     
4E6B: 00         NOP                     
4E6C: 00         NOP                     
4E6D: 00         NOP                     
4E6E: 00         NOP                     
4E6F: 00         NOP                     
4E70: E8 08      ADD     SP,$08          
4E72: D8         RET     C               
4E73: 08 28 18   LD      ($1828),SP      
4E76: 10 F0      STOP    $F0             
4E78: E0 E0      LDFF00  ($E0),A         
4E7A: 00         NOP                     
4E7B: 00         NOP                     
4E7C: 00         NOP                     
4E7D: 00         NOP                     
4E7E: 00         NOP                     
4E7F: 00         NOP                     
4E80: DD         ???                     
4E81: 00         NOP                     
4E82: C1         POP     BC              
4E83: 00         NOP                     
4E84: 5D         LD      E,L             
4E85: 00         NOP                     
4E86: BE         CP      (HL)            
4E87: 00         NOP                     
4E88: BE         CP      (HL)            
4E89: 00         NOP                     
4E8A: 9D         SBC     L               
4E8B: 00         NOP                     
4E8C: 63         LD      H,E             
4E8D: 00         NOP                     
4E8E: FB         EI                      
4E8F: 00         NOP                     
4E90: EF         RST     0X28            
4E91: 00         NOP                     
4E92: F7         RST     0X30            
4E93: 00         NOP                     
4E94: F0 00      LD      A,($00)         
4E96: F7         RST     0X30            
4E97: 00         NOP                     
4E98: 07         RLCA                    
4E99: 00         NOP                     
4E9A: DB         ???                     
4E9B: 00         NOP                     
4E9C: DC 00 DE   CALL    C,$DE00         
4E9F: 00         NOP                     
4EA0: FD         ???                     
4EA1: 00         NOP                     
4EA2: 7A         LD      A,D             
4EA3: 00         NOP                     
4EA4: B7         OR      A               
4EA5: 00         NOP                     
4EA6: CF         RST     0X08            
4EA7: 00         NOP                     
4EA8: EF         RST     0X28            
4EA9: 00         NOP                     
4EAA: C6 00      ADD     $00             
4EAC: 39         ADD     HL,SP           
4EAD: 00         NOP                     
4EAE: BD         CP      L               
4EAF: 00         NOP                     
4EB0: DE 00      SBC     $00             
4EB2: 0E 00      LD      C,$00           
4EB4: 71         LD      (HL),C          
4EB5: 00         NOP                     
4EB6: 7B         LD      A,E             
4EB7: 00         NOP                     
4EB8: 7B         LD      A,E             
4EB9: 00         NOP                     
4EBA: 39         ADD     HL,SP           
4EBB: 00         NOP                     
4EBC: C6 00      ADD     $00             
4EBE: EF         RST     0X28            
4EBF: 00         NOP                     
4EC0: 22         LD      (HLI),A         
4EC1: 00         NOP                     
4EC2: 3E 00      LD      A,$00           
4EC4: E2         LDFF00  (C),A           
4EC5: 00         NOP                     
4EC6: 40         LD      B,B             
4EC7: 01 40 01   LD      BC,$0140        
4ECA: 20 02      JR      NZ,$4ECE        
4ECC: 00         NOP                     
4ECD: 1C         INC     E               
4ECE: 00         NOP                     
4ECF: 04         INC     B               
4ED0: 10 00      STOP    $00             
4ED2: 09         ADD     HL,BC           
4ED3: 00         NOP                     
4ED4: 02         LD      (BC),A          
4ED5: 0C         INC     C               
4ED6: 00         NOP                     
4ED7: 08 00 F8   LD      ($F800),SP      
4EDA: 00         NOP                     
4EDB: 24         INC     H               
4EDC: 00         NOP                     
4EDD: 22         LD      (HLI),A         
4EDE: 00         NOP                     
4EDF: 41         LD      B,C             
4EE0: 02         LD      (BC),A          
4EE1: 04         INC     B               
4EE2: 03         INC     BC              
4EE3: 07         RLCA                    
4EE4: C1         POP     BC              
4EE5: 09         ADD     HL,BC           
4EE6: 20 10      JR      NZ,$4EF8        
4EE8: 10 00      STOP    $00             
4EEA: 18 00      JR      $4EEC           
4EEC: 67         LD      H,A             
4EED: 00         NOP                     
4EEE: 01 00 40   LD      BC,$4000        
4EF1: 41         LD      B,C             
4EF2: E0 F9      LDFF00  ($F9),A         
4EF4: C0         RET     NZ              
4EF5: 86         ADD     A,(HL)          
4EF6: 80         ADD     A,B             
4EF7: 84         ADD     A,H             
4EF8: 00         NOP                     
4EF9: 84         ADD     A,H             
4EFA: 3E C0      LD      A,$C0           
4EFC: 01 00 00   LD      BC,$0000        
4EFF: 00         NOP                     
4F00: F0 00      LD      A,($00)         
4F02: 12         LD      (DE),A          
4F03: 00         NOP                     
4F04: 10 00      STOP    $00             
4F06: 18 00      JR      $4F08           
4F08: 0F         RRCA                    
4F09: 00         NOP                     
4F0A: 01 00 21   LD      BC,$2100        
4F0D: 00         NOP                     
4F0E: 01 00 01   LD      BC,$0100        
4F11: 00         NOP                     
4F12: 01 00 41   LD      BC,$4100        
4F15: 00         NOP                     
4F16: 0F         RRCA                    
4F17: 00         NOP                     
4F18: 18 00      JR      $4F1A           
4F1A: 10 00      STOP    $00             
4F1C: 12         LD      (DE),A          
4F1D: 00         NOP                     
4F1E: F0 00      LD      A,($00)         
4F20: 8F         ADC     A,A             
4F21: 00         NOP                     
4F22: 08 00 08   LD      ($0800),SP      
4F25: 00         NOP                     
4F26: 18 00      JR      $4F28           
4F28: F0 00      LD      A,($00)         
4F2A: 84         ADD     A,H             
4F2B: 00         NOP                     
4F2C: 80         ADD     A,B             
4F2D: 00         NOP                     
4F2E: 80         ADD     A,B             
4F2F: 00         NOP                     
4F30: 80         ADD     A,B             
4F31: 00         NOP                     
4F32: 80         ADD     A,B             
4F33: 00         NOP                     
4F34: 82         ADD     A,D             
4F35: 00         NOP                     
4F36: F0 00      LD      A,($00)         
4F38: 18 00      JR      $4F3A           
4F3A: 08 00 88   LD      ($8800),SP      
4F3D: 00         NOP                     
4F3E: 0F         RRCA                    
4F3F: 00         NOP                     
4F40: 00         NOP                     
4F41: 00         NOP                     
4F42: 00         NOP                     
4F43: 00         NOP                     
4F44: 00         NOP                     
4F45: 00         NOP                     
4F46: 07         RLCA                    
4F47: 07         RLCA                    
4F48: 0C         INC     C               
4F49: 08 1B 10   LD      ($101B),SP      
4F4C: 17         RLA                     
4F4D: 10 17      STOP    $17             
4F4F: 10 00      STOP    $00             
4F51: 00         NOP                     
4F52: 00         NOP                     
4F53: 00         NOP                     
4F54: 00         NOP                     
4F55: 00         NOP                     
4F56: E0 E0      LDFF00  ($E0),A         
4F58: 30 10      JR      NC,$4F6A        
4F5A: D8         RET     C               
4F5B: 08 E8 08   LD      ($08E8),SP      
4F5E: E8 08      ADD     SP,$08          
4F60: 17         RLA                     
4F61: 10 1B      STOP    $1B             
4F63: 10 14      STOP    $14             
4F65: 18 08      JR      $4F6F           
4F67: 0F         RRCA                    
4F68: 07         RLCA                    
4F69: 07         RLCA                    
4F6A: 00         NOP                     
4F6B: 00         NOP                     
4F6C: 00         NOP                     
4F6D: 00         NOP                     
4F6E: 00         NOP                     
4F6F: 00         NOP                     
4F70: E8 08      ADD     SP,$08          
4F72: D8         RET     C               
4F73: 08 28 18   LD      ($1828),SP      
4F76: 10 F0      STOP    $F0             
4F78: E0 E0      LDFF00  ($E0),A         
4F7A: 00         NOP                     
4F7B: 00         NOP                     
4F7C: 00         NOP                     
4F7D: 00         NOP                     
4F7E: 00         NOP                     
4F7F: 00         NOP                     
4F80: E0 00      LDFF00  ($00),A         
4F82: CF         RST     0X08            
4F83: 00         NOP                     
4F84: 90         SUB     B               
4F85: 00         NOP                     
4F86: 27         DAA                     
4F87: 00         NOP                     
4F88: 4F         LD      C,A             
4F89: 00         NOP                     
4F8A: 5F         LD      E,A             
4F8B: 00         NOP                     
4F8C: 5F         LD      E,A             
4F8D: 00         NOP                     
4F8E: 7F         LD      A,A             
4F8F: 00         NOP                     
4F90: 07         RLCA                    
4F91: 00         NOP                     
4F92: F3         DI                      
4F93: 00         NOP                     
4F94: F9         LD      SP,HL           
4F95: 00         NOP                     
4F96: FC         ???                     
4F97: 00         NOP                     
4F98: FE 00      CP      $00             
4F9A: FE 00      CP      $00             
4F9C: FE 00      CP      $00             
4F9E: FE 00      CP      $00             
4FA0: 5F         LD      E,A             
4FA1: 00         NOP                     
4FA2: 7F         LD      A,A             
4FA3: 00         NOP                     
4FA4: 7F         LD      A,A             
4FA5: 00         NOP                     
4FA6: 7F         LD      A,A             
4FA7: 00         NOP                     
4FA8: 3F         CCF                     
4FA9: 00         NOP                     
4FAA: 9C         SBC     H               
4FAB: 03         INC     BC              
4FAC: CF         RST     0X08            
4FAD: 00         NOP                     
4FAE: E0 00      LDFF00  ($00),A         
4FB0: FE 00      CP      $00             
4FB2: FA 04 FA   LD      A,($FA04)       
4FB5: 04         INC     B               
4FB6: F2         ???                     
4FB7: 0C         INC     C               
4FB8: E4         ???                     
4FB9: 18 09      JR      $4FC4           
4FBB: F0 F2      LD      A,($F2)         
4FBD: 00         NOP                     
4FBE: 05         DEC     B               
4FBF: 00         NOP                     
4FC0: F0 00      LD      A,($00)         
4FC2: 32         LD      (HLD),A         
4FC3: 00         NOP                     
4FC4: 08 10 04   LD      ($0410),SP      
4FC7: 18 20      JR      $4FE9           
4FC9: 1F         RRA                     
4FCA: 80         ADD     A,B             
4FCB: 7F         LD      A,A             
4FCC: 40         LD      B,B             
4FCD: 31 1E 21   LD      SP,$211E        
4FD0: 00         NOP                     
4FD1: 21 20 41   LD      HL,$4120        
4FD4: 3E 41      LD      A,$41           
4FD6: 80         ADD     A,B             
4FD7: 7F         LD      A,A             
4FD8: 04         INC     B               
4FD9: F8 A8      LDHL    SP,$A8          
4FDB: 10 EA      STOP    $EA             
4FDD: 10 00      STOP    $00             
4FDF: FC         ???                     
4FE0: 00         NOP                     
4FE1: 3F         CCF                     
4FE2: 30 0F      JR      NC,$4FF3        
4FE4: 15         DEC     D               
4FE5: 08 65 18   LD      ($1865),SP      
4FE8: 00         NOP                     
4FE9: FF         RST     0X38            
4FEA: 84         ADD     A,H             
4FEB: 01 81 00   LD      BC,$0081        
4FEE: 80         ADD     A,B             
4FEF: 00         NOP                     
4FF0: 44         LD      B,H             
4FF1: 82         ADD     A,D             
4FF2: 10 82      STOP    $82             
4FF4: 44         LD      B,H             
4FF5: 82         ADD     A,D             
4FF6: 00         NOP                     
4FF7: FF         RST     0X38            
4FF8: 67         LD      H,A             
4FF9: 98         SBC     B               
4FFA: 90         SUB     B               
4FFB: 08 00 08   LD      ($0800),SP      
4FFE: 0F         RRCA                    
4FFF: 00         NOP                     
5000: 80         ADD     A,B             
5001: 80         ADD     A,B             
5002: C0         RET     NZ              
5003: C0         RET     NZ              
5004: A0         AND     B               
5005: A0         AND     B               
5006: 9F         SBC     A               
5007: 97         SUB     A               
5008: C8         RET     Z               
5009: 88         ADC     A,B             
500A: E8 C0      ADD     SP,$C0          
500C: F3         DI                      
500D: A1         AND     C               
500E: D3         ???                     
500F: B3         OR      E               
5010: 01 01 03   LD      BC,$0301        
5013: 03         INC     BC              
5014: 05         DEC     B               
5015: 05         DEC     B               
5016: F9         LD      SP,HL           
5017: E9         JP      (HL)            
5018: 13         INC     DE              
5019: 11 17 03   LD      DE,$0317        
501C: CF         RST     0X08            
501D: 85         ADD     A,L             
501E: CB CD      SET     1,E             
5020: D3         ???                     
5021: B3         OR      E               
5022: D3         ???                     
5023: B3         OR      E               
5024: D9         RETI                    
5025: B1         OR      C               
5026: E5         PUSH    HL              
5027: A1         AND     C               
5028: ED         ???                     
5029: AD         XOR     L               
502A: F6 BC      OR      $BC             
502C: C3 BE FF   JP      $FFBE           
502F: FF         RST     0X38            
5030: CB CD      SET     1,E             
5032: CB CD      SET     1,E             
5034: 9B         SBC     E               
5035: 8D         ADC     A,L             
5036: A7         AND     A               
5037: 85         ADD     A,L             
5038: B7         OR      A               
5039: B5         OR      L               
503A: 6F         LD      L,A             
503B: 3D         DEC     A               
503C: C3 7D FF   JP      $FF7D           
503F: FF         RST     0X38            
5040: 04         INC     B               
5041: 09         ADD     HL,BC           
5042: 7F         LD      A,A             
5043: 0D         DEC     C               
5044: 3B         DEC     SP              
5045: 6F         LD      L,A             
5046: 70         LD      (HL),B          
5047: 3F         CCF                     
5048: E7         RST     0X20            
5049: 38 E9      JR      C,$5034         
504B: B0         OR      B               
504C: 58         LD      E,B             
504D: E0 19      LDFF00  ($19),A         
504F: 60         LD      H,B             
5050: 30 10      JR      NC,$5062        
5052: F6 30      OR      $30             
5054: DC F6 0C   CALL    C,$0CF6         
5057: FC         ???                     
5058: E5         PUSH    HL              
5059: 1C         INC     E               
505A: 17         RLA                     
505B: 0D         DEC     C               
505C: 9A         SBC     D               
505D: 07         RLCA                    
505E: 48         LD      C,B             
505F: 06 26      LD      B,$26           
5061: 40         LD      B,B             
5062: 22         LD      (HLI),A         
5063: C0         RET     NZ              
5064: 2F         CPL                     
5065: 40         LD      B,B             
5066: 31 40 18   LD      SP,$1840        
5069: E0 0F      LDFF00  ($0F),A         
506B: 30 03      JR      NC,$5070        
506D: 1C         INC     E               
506E: 00         NOP                     
506F: 33         INC     SP              
5070: 3C         INC     A               
5071: 02         LD      (BC),A          
5072: 2C         INC     L               
5073: 03         INC     BC              
5074: C4 02 24   CALL    NZ,$2402        
5077: 02         LD      (BC),A          
5078: 9C         SBC     H               
5079: 03         INC     BC              
507A: F8 06      LDHL    SP,$06          
507C: 00         NOP                     
507D: FC         ???                     
507E: 00         NOP                     
507F: 26 00      LD      H,$00           
5081: FF         RST     0X38            
5082: 00         NOP                     
5083: 80         ADD     A,B             
5084: 3F         CCF                     
5085: 83         ADD     A,E             
5086: 3F         CCF                     
5087: 82         ADD     A,D             
5088: 3F         CCF                     
5089: BE         CP      (HL)            
508A: 3F         CCF                     
508B: A2         AND     D               
508C: 3F         CCF                     
508D: A2         AND     D               
508E: 3F         CCF                     
508F: A2         AND     D               
5090: 3F         CCF                     
5091: FF         RST     0X38            
5092: 3F         CCF                     
5093: 21 FF E1   LD      HL,$E1FF        
5096: FF         RST     0X38            
5097: 21 FF 21   LD      HL,$21FF        
509A: FF         RST     0X38            
509B: 21 E1 21   LD      HL,$21E1        
509E: FF         RST     0X38            
509F: 3F         CCF                     
50A0: 3E A2      LD      A,$A2           
50A2: 3F         CCF                     
50A3: A3         AND     E               
50A4: 23         INC     HL              
50A5: A3         AND     E               
50A6: 3F         CCF                     
50A7: BF         CP      A               
50A8: 3F         CCF                     
50A9: BF         CP      A               
50AA: 3F         CCF                     
50AB: 80         ADD     A,B             
50AC: 00         NOP                     
50AD: 80         ADD     A,B             
50AE: 00         NOP                     
50AF: FF         RST     0X38            
50B0: 3F         CCF                     
50B1: 3F         CCF                     
50B2: FF         RST     0X38            
50B3: FF         RST     0X38            
50B4: FF         RST     0X38            
50B5: FF         RST     0X38            
50B6: FF         RST     0X38            
50B7: FF         RST     0X38            
50B8: FF         RST     0X38            
50B9: FF         RST     0X38            
50BA: FE 01      CP      $01             
50BC: 00         NOP                     
50BD: 01 00 FF   LD      BC,$FF00        
50C0: 00         NOP                     
50C1: 00         NOP                     
50C2: FF         RST     0X38            
50C3: 00         NOP                     
50C4: DF         RST     0X18            
50C5: 3F         CCF                     
50C6: BF         CP      A               
50C7: 7F         LD      A,A             
50C8: FF         RST     0X38            
50C9: 7F         LD      A,A             
50CA: FF         RST     0X38            
50CB: 7F         LD      A,A             
50CC: FF         RST     0X38            
50CD: 7F         LD      A,A             
50CE: DF         RST     0X18            
50CF: 7F         LD      A,A             
50D0: 00         NOP                     
50D1: 00         NOP                     
50D2: FF         RST     0X38            
50D3: 00         NOP                     
50D4: FB         EI                      
50D5: FC         ???                     
50D6: FD         ???                     
50D7: FE FF      CP      $FF             
50D9: FE FF      CP      $FF             
50DB: FE FF      CP      $FF             
50DD: FE FF      CP      $FF             
50DF: FE CD      CP      $CD             
50E1: 7E         LD      A,(HL)          
50E2: DB         ???                     
50E3: 7C         LD      A,H             
50E4: F7         RST     0X30            
50E5: 78         LD      A,B             
50E6: EF         RST     0X28            
50E7: 70         LD      (HL),B          
50E8: DD         ???                     
50E9: 63         LD      H,E             
50EA: F6 4F      OR      $4F             
50EC: D8         RET     C               
50ED: 7C         LD      A,H             
50EE: FF         RST     0X38            
50EF: FF         RST     0X38            
50F0: FF         RST     0X38            
50F1: 7E         LD      A,(HL)          
50F2: FF         RST     0X38            
50F3: 3E FF      LD      A,$FF           
50F5: 3E 63      LD      A,$63           
50F7: F2         ???                     
50F8: 83         ADD     A,E             
50F9: C2 03 02   JP      NZ,$0203        
50FC: 03         INC     BC              
50FD: 02         LD      (BC),A          
50FE: FF         RST     0X38            
50FF: FF         RST     0X38            
5100: BF         CP      A               
5101: 7F         LD      A,A             
5102: FF         RST     0X38            
5103: 7F         LD      A,A             
5104: D0         RET     NC              
5105: EF         RST     0X28            
5106: 90         SUB     B               
5107: EF         RST     0X28            
5108: 90         SUB     B               
5109: EF         RST     0X28            
510A: 9F         SBC     A               
510B: E0 BF      LDFF00  ($BF),A         
510D: DF         RST     0X18            
510E: E0 BF      LDFF00  ($BF),A         
5110: FD         ???                     
5111: FE FF      CP      $FF             
5113: FE 0B      CP      $0B             
5115: F7         RST     0X30            
5116: 09         ADD     HL,BC           
5117: F7         RST     0X30            
5118: 09         ADD     HL,BC           
5119: F7         RST     0X30            
511A: F9         LD      SP,HL           
511B: 07         RLCA                    
511C: FD         ???                     
511D: FB         EI                      
511E: 07         RLCA                    
511F: FD         ???                     
5120: D0         RET     NC              
5121: EF         RST     0X28            
5122: 90         SUB     B               
5123: EF         RST     0X28            
5124: 90         SUB     B               
5125: EF         RST     0X28            
5126: 90         SUB     B               
5127: EF         RST     0X28            
5128: 9F         SBC     A               
5129: E0 BF      LDFF00  ($BF),A         
512B: FF         RST     0X38            
512C: E0 FF      LDFF00  ($FF),A         
512E: DF         RST     0X18            
512F: E0 0B      LDFF00  ($0B),A         
5131: F7         RST     0X30            
5132: 09         ADD     HL,BC           
5133: F7         RST     0X30            
5134: 09         ADD     HL,BC           
5135: F7         RST     0X30            
5136: 09         ADD     HL,BC           
5137: F7         RST     0X30            
5138: F9         LD      SP,HL           
5139: 07         RLCA                    
513A: FD         ???                     
513B: FF         RST     0X38            
513C: 07         RLCA                    
513D: FF         RST     0X38            
513E: FB         EI                      
513F: 07         RLCA                    
5140: BF         CP      A               
5141: C0         RET     NZ              
5142: F0 80      LD      A,($80)         
5144: E0 80      LDFF00  ($80),A         
5146: C0         RET     NZ              
5147: 80         ADD     A,B             
5148: C0         RET     NZ              
5149: 80         ADD     A,B             
514A: C0         RET     NZ              
514B: 80         ADD     A,B             
514C: 00         NOP                     
514D: 00         NOP                     
514E: 00         NOP                     
514F: 00         NOP                     
5150: FD         ???                     
5151: 03         INC     BC              
5152: 0F         RRCA                    
5153: 01 07 01   LD      BC,$0107        
5156: 03         INC     BC              
5157: 01 03 01   LD      BC,$0103        
515A: 03         INC     BC              
515B: 01 00 00   LD      BC,$0000        
515E: 00         NOP                     
515F: 00         NOP                     
5160: 81         ADD     A,C             
5161: 7E         LD      A,(HL)          
5162: 42         LD      B,D             
5163: BD         CP      L               
5164: 24         INC     H               
5165: DB         ???                     
5166: 18 E7      JR      $514F           
5168: 10 EF      STOP    $EF             
516A: 20 DF      JR      NZ,$514B        
516C: 40         LD      B,B             
516D: BF         CP      A               
516E: 80         ADD     A,B             
516F: 7F         LD      A,A             
5170: 86         ADD     A,(HL)          
5171: 78         LD      A,B             
5172: 5D         LD      E,L             
5173: A0         AND     B               
5174: 1B         DEC     DE              
5175: C0         RET     NZ              
5176: 67         LD      H,A             
5177: 80         ADD     A,B             
5178: EF         RST     0X28            
5179: 00         NOP                     
517A: DF         RST     0X18            
517B: 00         NOP                     
517C: BF         CP      A               
517D: 00         NOP                     
517E: 7F         LD      A,A             
517F: 00         NOP                     
5180: 61         LD      H,C             
5181: 1E BA      LD      E,$BA           
5183: 05         DEC     B               
5184: D8         RET     C               
5185: 03         INC     BC              
5186: E6 01      AND     $01             
5188: EF         RST     0X28            
5189: 00         NOP                     
518A: DF         RST     0X18            
518B: 00         NOP                     
518C: BF         CP      A               
518D: 00         NOP                     
518E: 7F         LD      A,A             
518F: 00         NOP                     
5190: 7E         LD      A,(HL)          
5191: 00         NOP                     
5192: BD         CP      L               
5193: 00         NOP                     
5194: DB         ???                     
5195: 00         NOP                     
5196: E7         RST     0X20            
5197: 00         NOP                     
5198: EF         RST     0X28            
5199: 00         NOP                     
519A: DF         RST     0X18            
519B: 00         NOP                     
519C: BF         CP      A               
519D: 00         NOP                     
519E: 7F         LD      A,A             
519F: 00         NOP                     
51A0: 3E 00      LD      A,$00           
51A2: 94         SUB     H               
51A3: 00         NOP                     
51A4: 89         ADC     A,C             
51A5: 00         NOP                     
51A6: 42         LD      B,D             
51A7: 00         NOP                     
51A8: A5         AND     L               
51A9: 00         NOP                     
51AA: 4A         LD      C,D             
51AB: 00         NOP                     
51AC: 00         NOP                     
51AD: 00         NOP                     
51AE: 00         NOP                     
51AF: 00         NOP                     
51B0: 00         NOP                     
51B1: FF         RST     0X38            
51B2: 7E         LD      A,(HL)          
51B3: 81         ADD     A,C             
51B4: 7E         LD      A,(HL)          
51B5: 81         ADD     A,C             
51B6: 7E         LD      A,(HL)          
51B7: 81         ADD     A,C             
51B8: 7E         LD      A,(HL)          
51B9: 81         ADD     A,C             
51BA: 7E         LD      A,(HL)          
51BB: 81         ADD     A,C             
51BC: 7E         LD      A,(HL)          
51BD: 81         ADD     A,C             
51BE: 00         NOP                     
51BF: FF         RST     0X38            
51C0: 01 01 02   LD      BC,$0201        
51C3: 02         LD      (BC),A          
51C4: 05         DEC     B               
51C5: 04         INC     B               
51C6: 09         ADD     HL,BC           
51C7: 08 EC E8   LD      ($E8EC),SP      
51CA: 9E         SBC     (HL)            
51CB: 98         SBC     B               
51CC: CA 88 A8   JP      Z,$A888         
51CF: C8         RET     Z               
51D0: 00         NOP                     
51D1: 00         NOP                     
51D2: 80         ADD     A,B             
51D3: 80         ADD     A,B             
51D4: 4E         LD      C,(HL)          
51D5: 4E         LD      C,(HL)          
51D6: 32         LD      (HLD),A         
51D7: 32         LD      (HLD),A         
51D8: 66         LD      H,(HL)          
51D9: 22         LD      (HLI),A         
51DA: AE         XOR     (HL)            
51DB: 62         LD      H,D             
51DC: 2C         INC     L               
51DD: E4         ???                     
51DE: 37         SCF                     
51DF: EF         RST     0X28            
51E0: 5C         LD      E,H             
51E1: 68         LD      L,B             
51E2: 2E 38      LD      L,$38           
51E4: 7B         LD      A,E             
51E5: 79         LD      A,C             
51E6: 9A         SBC     D               
51E7: 9A         SBC     D               
51E8: CE 8A      ADC     $8A             
51EA: 6E         LD      L,(HL)          
51EB: 4A         LD      C,D             
51EC: 36 3E      LD      (HL),$3E        
51EE: 05         DEC     B               
51EF: 03         INC     BC              
51F0: 2B         DEC     HL              
51F1: F9         LD      SP,HL           
51F2: B1         OR      C               
51F3: F3         DI                      
51F4: 66         LD      H,(HL)          
51F5: 62         LD      H,D             
51F6: 6A         LD      L,D             
51F7: 26 EC      LD      H,$EC           
51F9: 24         INC     H               
51FA: F4         ???                     
51FB: 2C         INC     L               
51FC: B8         CP      B               
51FD: 78         LD      A,B             
51FE: D0         RET     NC              
51FF: E0 80      LDFF00  ($80),A         
5201: 80         ADD     A,B             
5202: 80         ADD     A,B             
5203: 80         ADD     A,B             
5204: 80         ADD     A,B             
5205: 80         ADD     A,B             
5206: FF         RST     0X38            
5207: 83         ADD     A,E             
5208: FF         RST     0X38            
5209: 84         ADD     A,H             
520A: FF         RST     0X38            
520B: 88         ADC     A,B             
520C: FF         RST     0X38            
520D: 88         ADC     A,B             
520E: FF         RST     0X38            
520F: 88         ADC     A,B             
5210: 01 01 01   LD      BC,$0101        
5213: 01 01 01   LD      BC,$0101        
5216: FF         RST     0X38            
5217: C1         POP     BC              
5218: FF         RST     0X38            
5219: 21 FF 11   LD      HL,$11FF        
521C: FF         RST     0X38            
521D: 11 FF 11   LD      DE,$11FF        
5220: FF         RST     0X38            
5221: 9C         SBC     H               
5222: F7         RST     0X30            
5223: A0         AND     B               
5224: EF         RST     0X28            
5225: C8         RET     Z               
5226: FF         RST     0X38            
5227: F8 FE      LDHL    SP,$FE          
5229: 88         ADC     A,B             
522A: FF         RST     0X38            
522B: 89         ADC     A,C             
522C: F9         LD      SP,HL           
522D: 89         ADC     A,C             
522E: FF         RST     0X38            
522F: FF         RST     0X38            
5230: FF         RST     0X38            
5231: 39         ADD     HL,SP           
5232: EF         RST     0X28            
5233: 05         DEC     B               
5234: F7         RST     0X30            
5235: 13         INC     DE              
5236: FF         RST     0X38            
5237: 1F         RRA                     
5238: 7F         LD      A,A             
5239: 11 FF 91   LD      DE,$91FF        
523C: 9F         SBC     A               
523D: 91         SUB     C               
523E: FF         RST     0X38            
523F: FF         RST     0X38            
5240: 04         INC     B               
5241: 09         ADD     HL,BC           
5242: 7F         LD      A,A             
5243: 0D         DEC     C               
5244: 3B         DEC     SP              
5245: 6F         LD      L,A             
5246: 70         LD      (HL),B          
5247: 3F         CCF                     
5248: E7         RST     0X20            
5249: 38 E9      JR      C,$5234         
524B: B0         OR      B               
524C: 58         LD      E,B             
524D: E0 19      LDFF00  ($19),A         
524F: 60         LD      H,B             
5250: 30 10      JR      NC,$5262        
5252: F6 30      OR      $30             
5254: DC F6 0C   CALL    C,$0CF6         
5257: FC         ???                     
5258: E5         PUSH    HL              
5259: 1C         INC     E               
525A: 17         RLA                     
525B: 0D         DEC     C               
525C: 9A         SBC     D               
525D: 07         RLCA                    
525E: 48         LD      C,B             
525F: 06 26      LD      B,$26           
5261: 40         LD      B,B             
5262: 22         LD      (HLI),A         
5263: C0         RET     NZ              
5264: 2F         CPL                     
5265: 40         LD      B,B             
5266: 31 40 18   LD      SP,$1840        
5269: E0 0F      LDFF00  ($0F),A         
526B: 30 03      JR      NC,$5270        
526D: 1C         INC     E               
526E: 00         NOP                     
526F: 33         INC     SP              
5270: 3C         INC     A               
5271: 02         LD      (BC),A          
5272: 2C         INC     L               
5273: 03         INC     BC              
5274: C4 02 24   CALL    NZ,$2402        
5277: 02         LD      (BC),A          
5278: 9C         SBC     H               
5279: 03         INC     BC              
527A: F8 06      LDHL    SP,$06          
527C: 00         NOP                     
527D: FC         ???                     
527E: 00         NOP                     
527F: 26 00      LD      H,$00           
5281: FF         RST     0X38            
5282: 00         NOP                     
5283: 80         ADD     A,B             
5284: 3F         CCF                     
5285: 83         ADD     A,E             
5286: 3F         CCF                     
5287: 82         ADD     A,D             
5288: 3F         CCF                     
5289: BE         CP      (HL)            
528A: 3F         CCF                     
528B: A2         AND     D               
528C: 3F         CCF                     
528D: A2         AND     D               
528E: 3F         CCF                     
528F: A2         AND     D               
5290: 3F         CCF                     
5291: FF         RST     0X38            
5292: 3F         CCF                     
5293: 21 FF E1   LD      HL,$E1FF        
5296: FF         RST     0X38            
5297: 21 FF 21   LD      HL,$21FF        
529A: FF         RST     0X38            
529B: 21 E1 21   LD      HL,$21E1        
529E: FF         RST     0X38            
529F: 3F         CCF                     
52A0: 3E A2      LD      A,$A2           
52A2: 3F         CCF                     
52A3: A3         AND     E               
52A4: 23         INC     HL              
52A5: A3         AND     E               
52A6: 3F         CCF                     
52A7: BF         CP      A               
52A8: 3F         CCF                     
52A9: BF         CP      A               
52AA: 3F         CCF                     
52AB: 80         ADD     A,B             
52AC: 00         NOP                     
52AD: 80         ADD     A,B             
52AE: 00         NOP                     
52AF: FF         RST     0X38            
52B0: 3F         CCF                     
52B1: 3F         CCF                     
52B2: FF         RST     0X38            
52B3: FF         RST     0X38            
52B4: FF         RST     0X38            
52B5: FF         RST     0X38            
52B6: FF         RST     0X38            
52B7: FF         RST     0X38            
52B8: FF         RST     0X38            
52B9: FF         RST     0X38            
52BA: FE 01      CP      $01             
52BC: 00         NOP                     
52BD: 01 00 FF   LD      BC,$FF00        
52C0: FF         RST     0X38            
52C1: FF         RST     0X38            
52C2: 9F         SBC     A               
52C3: 81         ADD     A,C             
52C4: E7         RST     0X20            
52C5: 80         ADD     A,B             
52C6: F8 80      LDHL    SP,$80          
52C8: FB         EI                      
52C9: 83         ADD     A,E             
52CA: FB         EI                      
52CB: 93         SUB     E               
52CC: F9         LD      SP,HL           
52CD: B1         OR      C               
52CE: B9         CP      C               
52CF: A1         AND     C               
52D0: FF         RST     0X38            
52D1: FF         RST     0X38            
52D2: F9         LD      SP,HL           
52D3: 81         ADD     A,C             
52D4: E1         POP     HL              
52D5: 07         RLCA                    
52D6: 01 1F C1   LD      BC,$C11F        
52D9: DF         RST     0X18            
52DA: C9         RET                     
52DB: DF         RST     0X18            
52DC: 8D         ADC     A,L             
52DD: 9F         SBC     A               
52DE: 87         ADD     A,A             
52DF: 9D         SBC     L               
52E0: B8         CP      B               
52E1: 80         ADD     A,B             
52E2: F0 87      LD      A,($87)         
52E4: E1         POP     HL              
52E5: 8F         ADC     A,A             
52E6: C1         POP     BC              
52E7: 9F         SBC     A               
52E8: 81         ADD     A,C             
52E9: BF         CP      A               
52EA: 81         ADD     A,C             
52EB: BE         CP      (HL)            
52EC: 80         ADD     A,B             
52ED: FF         RST     0X38            
52EE: FF         RST     0X38            
52EF: FF         RST     0X38            
52F0: 03         INC     BC              
52F1: 1D         DEC     E               
52F2: 11 EF 89   LD      DE,$89EF        
52F5: F7         RST     0X30            
52F6: 85         ADD     A,L             
52F7: FB         EI                      
52F8: 83         ADD     A,E             
52F9: FD         ???                     
52FA: 83         ADD     A,E             
52FB: 7D         LD      A,L             
52FC: 01 FF FF   LD      BC,$FFFF        
52FF: FF         RST     0X38            
5300: 00         NOP                     
5301: 00         NOP                     
5302: FF         RST     0X38            
5303: 00         NOP                     
5304: DF         RST     0X18            
5305: 3F         CCF                     
5306: BF         CP      A               
5307: 7F         LD      A,A             
5308: FF         RST     0X38            
5309: 7F         LD      A,A             
530A: FF         RST     0X38            
530B: 7F         LD      A,A             
530C: FF         RST     0X38            
530D: 7C         LD      A,H             
530E: FF         RST     0X38            
530F: 78         LD      A,B             
5310: 00         NOP                     
5311: 00         NOP                     
5312: FF         RST     0X38            
5313: 00         NOP                     
5314: FB         EI                      
5315: FC         ???                     
5316: FD         ???                     
5317: 86         ADD     A,(HL)          
5318: DF         RST     0X18            
5319: 82         ADD     A,D             
531A: AF         XOR     A               
531B: C2 97 E2   JP      NZ,$E297        
531E: CB 72      SET     1,E             
5320: FB         EI                      
5321: 70         LD      (HL),B          
5322: F4         ???                     
5323: 78         LD      A,B             
5324: F1         POP     AF              
5325: 7E         LD      A,(HL)          
5326: FC         ???                     
5327: 7F         LD      A,A             
5328: EB         ???                     
5329: 47         LD      B,A             
532A: C1         POP     BC              
532B: 40         LD      B,B             
532C: C0         RET     NZ              
532D: 40         LD      B,B             
532E: FF         RST     0X38            
532F: FF         RST     0X38            
5330: E7         RST     0X20            
5331: 3A         LD      A,(HLD)         
5332: F3         DI                      
5333: 1E 3B      LD      E,$3B           
5335: 0E 4F      LD      C,$4F           
5337: 86         ADD     A,(HL)          
5338: 97         SUB     A               
5339: E2         LDFF00  (C),A           
533A: 73         LD      (HL),E          
533B: FE 2F      CP      $2F             
533D: 1E FF      LD      E,$FF           
533F: FE 00      CP      $00             
5341: 00         NOP                     
5342: F7         RST     0X30            
5343: F8 98      LDHL    SP,$98          
5345: EF         RST     0X28            
5346: 8F         ADC     A,A             
5347: F7         RST     0X30            
5348: 4F         LD      C,A             
5349: F8 30      LDHL    SP,$30          
534B: FF         RST     0X38            
534C: 2F         CPL                     
534D: FF         RST     0X38            
534E: 2D         DEC     L               
534F: FD         ???                     
5350: 00         NOP                     
5351: 00         NOP                     
5352: EF         RST     0X28            
5353: 1F         RRA                     
5354: 1D         DEC     E               
5355: F3         DI                      
5356: F1         POP     AF              
5357: EF         RST     0X28            
5358: F2         ???                     
5359: 1F         RRA                     
535A: 0C         INC     C               
535B: FF         RST     0X38            
535C: F4         ???                     
535D: FF         RST     0X38            
535E: B4         OR      H               
535F: BF         CP      A               
5360: 27         DAA                     
5361: FF         RST     0X38            
5362: E1         POP     HL              
5363: FF         RST     0X38            
5364: 21 FF 79   LD      HL,$79FF        
5367: FF         RST     0X38            
5368: E7         RST     0X20            
5369: DF         RST     0X18            
536A: C0         RET     NZ              
536B: BF         CP      A               
536C: 81         ADD     A,C             
536D: FF         RST     0X38            
536E: FF         RST     0X38            
536F: FF         RST     0X38            
5370: E4         ???                     
5371: FF         RST     0X38            
5372: 87         ADD     A,A             
5373: FF         RST     0X38            
5374: 84         ADD     A,H             
5375: FF         RST     0X38            
5376: 9E         SBC     (HL)            
5377: FF         RST     0X38            
5378: E7         RST     0X20            
5379: FB         EI                      
537A: 03         INC     BC              
537B: FD         ???                     
537C: 81         ADD     A,C             
537D: FF         RST     0X38            
537E: FF         RST     0X38            
537F: FF         RST     0X38            
5380: FF         RST     0X38            
5381: 06 DF      LD      B,$DF           
5383: E7         RST     0X20            
5384: EF         RST     0X28            
5385: F7         RST     0X30            
5386: FD         ???                     
5387: FF         RST     0X38            
5388: 4C         LD      C,H             
5389: 7F         LD      A,A             
538A: A0         AND     B               
538B: 3F         CCF                     
538C: 71         LD      (HL),C          
538D: 9F         SBC     A               
538E: 30 DF      JR      NC,$536F        
5390: FF         RST     0X38            
5391: 30 FD      JR      NC,$5390        
5393: F3         DI                      
5394: FB         EI                      
5395: F7         RST     0X30            
5396: 9F         SBC     A               
5397: FF         RST     0X38            
5398: 1A         LD      A,(DE)          
5399: FE 05      CP      $05             
539B: FC         ???                     
539C: 0E F9      LD      C,$F9           
539E: 0C         INC     C               
539F: FB         EI                      
53A0: 38 DF      JR      C,$5381         
53A2: F2         ???                     
53A3: FF         RST     0X38            
53A4: 30 3F      JR      NC,$53E5        
53A6: 3A         LD      A,(HLD)         
53A7: DF         RST     0X18            
53A8: 38 DF      JR      C,$5389         
53AA: 1F         RRA                     
53AB: FF         RST     0X38            
53AC: EF         RST     0X28            
53AD: F0 DF      LD      A,($DF)         
53AF: E0 1C      LDFF00  ($1C),A         
53B1: FB         EI                      
53B2: 4F         LD      C,A             
53B3: FF         RST     0X38            
53B4: 0C         INC     C               
53B5: FC         ???                     
53B6: 5F         LD      E,A             
53B7: F8 1C      LDHL    SP,$1C          
53B9: FB         EI                      
53BA: F8 FF      LDHL    SP,$FF          
53BC: F7         RST     0X30            
53BD: 0F         RRCA                    
53BE: FB         EI                      
53BF: 07         RLCA                    
53C0: 00         NOP                     
53C1: 00         NOP                     
53C2: FF         RST     0X38            
53C3: 00         NOP                     
53C4: DF         RST     0X18            
53C5: 3F         CCF                     
53C6: BF         CP      A               
53C7: 7F         LD      A,A             
53C8: FF         RST     0X38            
53C9: 7F         LD      A,A             
53CA: FF         RST     0X38            
53CB: 7F         LD      A,A             
53CC: FF         RST     0X38            
53CD: 7F         LD      A,A             
53CE: DF         RST     0X18            
53CF: 7F         LD      A,A             
53D0: 00         NOP                     
53D1: 00         NOP                     
53D2: FF         RST     0X38            
53D3: 00         NOP                     
53D4: FB         EI                      
53D5: FC         ???                     
53D6: FD         ???                     
53D7: FE FF      CP      $FF             
53D9: FE FF      CP      $FF             
53DB: FE FF      CP      $FF             
53DD: FE FF      CP      $FF             
53DF: FE CD      CP      $CD             
53E1: 7E         LD      A,(HL)          
53E2: DB         ???                     
53E3: 7C         LD      A,H             
53E4: F7         RST     0X30            
53E5: 78         LD      A,B             
53E6: EF         RST     0X28            
53E7: 70         LD      (HL),B          
53E8: DD         ???                     
53E9: 63         LD      H,E             
53EA: F6 4F      OR      $4F             
53EC: D8         RET     C               
53ED: 7C         LD      A,H             
53EE: FF         RST     0X38            
53EF: FF         RST     0X38            
53F0: FF         RST     0X38            
53F1: 7E         LD      A,(HL)          
53F2: FF         RST     0X38            
53F3: 3E FF      LD      A,$FF           
53F5: 3E 63      LD      A,$63           
53F7: F2         ???                     
53F8: 83         ADD     A,E             
53F9: C2 03 02   JP      NZ,$0203        
53FC: 03         INC     BC              
53FD: 02         LD      (BC),A          
53FE: FF         RST     0X38            
53FF: FF         RST     0X38            
5400: FF         RST     0X38            
5401: FE 9D      CP      $9D             
5403: E1         POP     HL              
5404: 9D         SBC     L               
5405: E1         POP     HL              
5406: A9         XOR     C               
5407: D1         POP     DE              
5408: A9         XOR     C               
5409: D1         POP     DE              
540A: 99         SBC     C               
540B: E1         POP     HL              
540C: 9D         SBC     L               
540D: E1         POP     HL              
540E: 9D         SBC     L               
540F: E1         POP     HL              
5410: 89         ADC     A,C             
5411: F1         POP     AF              
5412: A9         XOR     C               
5413: D1         POP     DE              
5414: A9         XOR     C               
5415: D1         POP     DE              
5416: BD         CP      L               
5417: FD         ???                     
5418: C3 C3 81   JP      $81C3           
541B: 99         SBC     C               
541C: 81         ADD     A,C             
541D: A5         AND     L               
541E: 81         ADD     A,C             
541F: A5         AND     L               
5420: FF         RST     0X38            
5421: 7F         LD      A,A             
5422: B9         CP      C               
5423: 87         ADD     A,A             
5424: B9         CP      C               
5425: 87         ADD     A,A             
5426: 95         SUB     L               
5427: 8B         ADC     A,E             
5428: 95         SUB     L               
5429: 8B         ADC     A,E             
542A: 99         SBC     C               
542B: 87         ADD     A,A             
542C: B9         CP      C               
542D: 87         ADD     A,A             
542E: B9         CP      C               
542F: 87         ADD     A,A             
5430: 91         SUB     C               
5431: 8F         ADC     A,A             
5432: 95         SUB     L               
5433: 8B         ADC     A,E             
5434: 95         SUB     L               
5435: 8B         ADC     A,E             
5436: BD         CP      L               
5437: BF         CP      A               
5438: C3 C3 81   JP      $81C3           
543B: 99         SBC     C               
543C: 81         ADD     A,C             
543D: A5         AND     L               
543E: 81         ADD     A,C             
543F: A5         AND     L               
5440: FF         RST     0X38            
5441: FF         RST     0X38            
5442: 18 FF      JR      $5443           
5444: 00         NOP                     
5445: FF         RST     0X38            
5446: FF         RST     0X38            
5447: FF         RST     0X38            
5448: FF         RST     0X38            
5449: 00         NOP                     
544A: 00         NOP                     
544B: 38 FF      JR      C,$544C         
544D: EF         RST     0X28            
544E: 38 28      JR      C,$5478         
5450: 38 28      JR      C,$547A         
5452: 38 28      JR      C,$547C         
5454: 38 28      JR      C,$547E         
5456: FF         RST     0X38            
5457: FF         RST     0X38            
5458: 00         NOP                     
5459: FF         RST     0X38            
545A: FF         RST     0X38            
545B: 00         NOP                     
545C: 00         NOP                     
545D: 00         NOP                     
545E: 00         NOP                     
545F: 00         NOP                     
5460: 00         NOP                     
5461: 00         NOP                     
5462: 00         NOP                     
5463: 00         NOP                     
5464: FF         RST     0X38            
5465: 00         NOP                     
5466: 00         NOP                     
5467: FF         RST     0X38            
5468: FF         RST     0X38            
5469: FF         RST     0X38            
546A: 38 28      JR      C,$5494         
546C: 38 28      JR      C,$5496         
546E: 38 28      JR      C,$5498         
5470: 38 28      JR      C,$549A         
5472: FF         RST     0X38            
5473: EF         RST     0X28            
5474: 00         NOP                     
5475: 38 FF      JR      C,$5476         
5477: 00         NOP                     
5478: FF         RST     0X38            
5479: FF         RST     0X38            
547A: 00         NOP                     
547B: FF         RST     0X38            
547C: 18 FF      JR      $547D           
547E: FF         RST     0X38            
547F: FF         RST     0X38            
5480: 3C         INC     A               
5481: 3C         INC     A               
5482: 5A         LD      E,D             
5483: 66         LD      H,(HL)          
5484: 66         LD      H,(HL)          
5485: 42         LD      B,D             
5486: 66         LD      H,(HL)          
5487: 42         LD      B,D             
5488: 5A         LD      E,D             
5489: 66         LD      H,(HL)          
548A: 66         LD      H,(HL)          
548B: 7E         LD      A,(HL)          
548C: 3C         INC     A               
548D: 3C         INC     A               
548E: 00         NOP                     
548F: 00         NOP                     
5490: 00         NOP                     
5491: 00         NOP                     
5492: CE CE      ADC     $CE             
5494: DB         ???                     
5495: DB         ???                     
5496: DB         ???                     
5497: DB         ???                     
5498: DB         ???                     
5499: DB         ???                     
549A: DB         ???                     
549B: DB         ???                     
549C: CE CE      ADC     $CE             
549E: 00         NOP                     
549F: 00         NOP                     
54A0: 00         NOP                     
54A1: 00         NOP                     
54A2: 22         LD      (HLI),A         
54A3: 22         LD      (HLI),A         
54A4: 14         INC     D               
54A5: 14         INC     D               
54A6: 08 08 08   LD      ($0808),SP      
54A9: 08 14 14   LD      ($1414),SP      
54AC: 22         LD      (HLI),A         
54AD: 22         LD      (HLI),A         
54AE: 00         NOP                     
54AF: 00         NOP                     
54B0: 00         NOP                     
54B1: 00         NOP                     
54B2: FF         RST     0X38            
54B3: 00         NOP                     
54B4: 00         NOP                     
54B5: FF         RST     0X38            
54B6: FF         RST     0X38            
54B7: FF         RST     0X38            
54B8: A1         AND     C               
54B9: FF         RST     0X38            
54BA: A5         AND     L               
54BB: FF         RST     0X38            
54BC: 85         ADD     A,L             
54BD: FF         RST     0X38            
54BE: FF         RST     0X38            
54BF: FF         RST     0X38            
54C0: 3C         INC     A               
54C1: 3C         INC     A               
54C2: 26 26      LD      H,$26           
54C4: 25         DEC     H               
54C5: 25         DEC     H               
54C6: 24         INC     H               
54C7: 24         INC     H               
54C8: E4         ???                     
54C9: E4         ???                     
54CA: A4         AND     H               
54CB: A4         AND     H               
54CC: BC         CP      H               
54CD: BC         CP      H               
54CE: BE         CP      (HL)            
54CF: A2         AND     D               
54D0: 00         NOP                     
54D1: 00         NOP                     
54D2: 00         NOP                     
54D3: 00         NOP                     
54D4: 00         NOP                     
54D5: 00         NOP                     
54D6: 80         ADD     A,B             
54D7: 80         ADD     A,B             
54D8: FE FE      CP      $FE             
54DA: 82         ADD     A,D             
54DB: 82         ADD     A,D             
54DC: 82         ADD     A,D             
54DD: 82         ADD     A,D             
54DE: 82         ADD     A,D             
54DF: 82         ADD     A,D             
54E0: BF         CP      A               
54E1: A1         AND     C               
54E2: BF         CP      A               
54E3: A0         AND     B               
54E4: BF         CP      A               
54E5: BF         CP      A               
54E6: 80         ADD     A,B             
54E7: 80         ADD     A,B             
54E8: FF         RST     0X38            
54E9: 80         ADD     A,B             
54EA: FF         RST     0X38            
54EB: FF         RST     0X38            
54EC: 92         SUB     D               
54ED: FF         RST     0X38            
54EE: FF         RST     0X38            
54EF: FF         RST     0X38            
54F0: 82         ADD     A,D             
54F1: 82         ADD     A,D             
54F2: 82         ADD     A,D             
54F3: 82         ADD     A,D             
54F4: 82         ADD     A,D             
54F5: 82         ADD     A,D             
54F6: 02         LD      (BC),A          
54F7: 02         LD      (BC),A          
54F8: FE 02      CP      $02             
54FA: FE FE      CP      $FE             
54FC: 4A         LD      C,D             
54FD: FE FE      CP      $FE             
54FF: FE FA      CP      $FA             
5501: DC 2D F2   CALL    C,$F22D         
5504: 1C         INC     E               
5505: E1         POP     HL              
5506: D8         RET     C               
5507: 21 D0 21   LD      HL,$21D0        
550A: C0         RET     NZ              
550B: 31 E8 72   LD      SP,$72E8        
550E: 90         SUB     B               
550F: EC         ???                     
5510: 90         SUB     B               
5511: E4         ???                     
5512: 90         SUB     B               
5513: E4         ???                     
5514: B0         OR      B               
5515: C4 78 82   CALL    NZ,$8278        
5518: C4 01 82   CALL    NZ,$8201        
551B: 01 00 01   LD      BC,$0100        
551E: 01 00 5F   LD      BC,$5F00        
5521: 3F         CCF                     
5522: B0         OR      B               
5523: 4F         LD      C,A             
5524: 38 87      JR      C,$54AD         
5526: 1D         DEC     E               
5527: 82         ADD     A,D             
5528: 1B         DEC     DE              
5529: 84         ADD     A,H             
552A: 0B         DEC     BC              
552B: 84         ADD     A,H             
552C: 07         RLCA                    
552D: 4E         LD      C,(HL)          
552E: 09         ADD     HL,BC           
552F: 37         SCF                     
5530: 09         ADD     HL,BC           
5531: 27         DAA                     
5532: 09         ADD     HL,BC           
5533: 27         DAA                     
5534: 0D         DEC     C               
5535: 23         INC     HL              
5536: 1E 41      LD      E,$41           
5538: 23         INC     HL              
5539: 80         ADD     A,B             
553A: 41         LD      B,C             
553B: 80         ADD     A,B             
553C: 00         NOP                     
553D: 80         ADD     A,B             
553E: 80         ADD     A,B             
553F: 00         NOP                     
5540: 04         INC     B               
5541: 09         ADD     HL,BC           
5542: 7F         LD      A,A             
5543: 0D         DEC     C               
5544: 3B         DEC     SP              
5545: 6F         LD      L,A             
5546: 70         LD      (HL),B          
5547: 3F         CCF                     
5548: E7         RST     0X20            
5549: 38 E9      JR      C,$5534         
554B: B0         OR      B               
554C: 58         LD      E,B             
554D: E0 19      LDFF00  ($19),A         
554F: 60         LD      H,B             
5550: 30 10      JR      NC,$5562        
5552: F6 30      OR      $30             
5554: DC F6 0C   CALL    C,$0CF6         
5557: FC         ???                     
5558: E5         PUSH    HL              
5559: 1C         INC     E               
555A: 17         RLA                     
555B: 0D         DEC     C               
555C: 9A         SBC     D               
555D: 07         RLCA                    
555E: 48         LD      C,B             
555F: 06 26      LD      B,$26           
5561: 40         LD      B,B             
5562: 22         LD      (HLI),A         
5563: C0         RET     NZ              
5564: 2F         CPL                     
5565: 40         LD      B,B             
5566: 31 40 18   LD      SP,$1840        
5569: E0 0F      LDFF00  ($0F),A         
556B: 30 03      JR      NC,$5570        
556D: 1C         INC     E               
556E: 00         NOP                     
556F: 33         INC     SP              
5570: 3C         INC     A               
5571: 02         LD      (BC),A          
5572: 2C         INC     L               
5573: 03         INC     BC              
5574: C4 02 24   CALL    NZ,$2402        
5577: 02         LD      (BC),A          
5578: 9C         SBC     H               
5579: 03         INC     BC              
557A: F8 06      LDHL    SP,$06          
557C: 00         NOP                     
557D: FC         ???                     
557E: 00         NOP                     
557F: 26 00      LD      H,$00           
5581: FF         RST     0X38            
5582: 00         NOP                     
5583: 80         ADD     A,B             
5584: 3F         CCF                     
5585: 83         ADD     A,E             
5586: 3F         CCF                     
5587: 82         ADD     A,D             
5588: 3F         CCF                     
5589: BE         CP      (HL)            
558A: 3F         CCF                     
558B: A2         AND     D               
558C: 3F         CCF                     
558D: A2         AND     D               
558E: 3F         CCF                     
558F: A2         AND     D               
5590: 3F         CCF                     
5591: FF         RST     0X38            
5592: 3F         CCF                     
5593: 21 FF E1   LD      HL,$E1FF        
5596: FF         RST     0X38            
5597: 21 FF 21   LD      HL,$21FF        
559A: FF         RST     0X38            
559B: 21 E1 21   LD      HL,$21E1        
559E: FF         RST     0X38            
559F: 3F         CCF                     
55A0: 3E A2      LD      A,$A2           
55A2: 3F         CCF                     
55A3: A3         AND     E               
55A4: 23         INC     HL              
55A5: A3         AND     E               
55A6: 3F         CCF                     
55A7: BF         CP      A               
55A8: 3F         CCF                     
55A9: BF         CP      A               
55AA: 3F         CCF                     
55AB: 80         ADD     A,B             
55AC: 00         NOP                     
55AD: 80         ADD     A,B             
55AE: 00         NOP                     
55AF: FF         RST     0X38            
55B0: 3F         CCF                     
55B1: 3F         CCF                     
55B2: FF         RST     0X38            
55B3: FF         RST     0X38            
55B4: FF         RST     0X38            
55B5: FF         RST     0X38            
55B6: FF         RST     0X38            
55B7: FF         RST     0X38            
55B8: FF         RST     0X38            
55B9: FF         RST     0X38            
55BA: FE 01      CP      $01             
55BC: 00         NOP                     
55BD: 01 00 FF   LD      BC,$FF00        
55C0: 01 01 02   LD      BC,$0201        
55C3: 02         LD      (BC),A          
55C4: 05         DEC     B               
55C5: 04         INC     B               
55C6: 09         ADD     HL,BC           
55C7: 08 EC E8   LD      ($E8EC),SP      
55CA: 9E         SBC     (HL)            
55CB: 98         SBC     B               
55CC: CA 88 A8   JP      Z,$A888         
55CF: C8         RET     Z               
55D0: 00         NOP                     
55D1: 00         NOP                     
55D2: 80         ADD     A,B             
55D3: 80         ADD     A,B             
55D4: 4E         LD      C,(HL)          
55D5: 4E         LD      C,(HL)          
55D6: 32         LD      (HLD),A         
55D7: 32         LD      (HLD),A         
55D8: 66         LD      H,(HL)          
55D9: 22         LD      (HLI),A         
55DA: AE         XOR     (HL)            
55DB: 62         LD      H,D             
55DC: 2C         INC     L               
55DD: E4         ???                     
55DE: 37         SCF                     
55DF: EF         RST     0X28            
55E0: 5C         LD      E,H             
55E1: 68         LD      L,B             
55E2: 2E 38      LD      L,$38           
55E4: 7B         LD      A,E             
55E5: 79         LD      A,C             
55E6: 9A         SBC     D               
55E7: 9A         SBC     D               
55E8: CE 8A      ADC     $8A             
55EA: 6E         LD      L,(HL)          
55EB: 4A         LD      C,D             
55EC: 36 3E      LD      (HL),$3E        
55EE: 05         DEC     B               
55EF: 03         INC     BC              
55F0: 2B         DEC     HL              
55F1: F9         LD      SP,HL           
55F2: B1         OR      C               
55F3: F3         DI                      
55F4: 66         LD      H,(HL)          
55F5: 62         LD      H,D             
55F6: 6A         LD      L,D             
55F7: 26 EC      LD      H,$EC           
55F9: 24         INC     H               
55FA: F4         ???                     
55FB: 2C         INC     L               
55FC: B8         CP      B               
55FD: 78         LD      A,B             
55FE: D0         RET     NC              
55FF: E0 80      LDFF00  ($80),A         
5601: 80         ADD     A,B             
5602: C0         RET     NZ              
5603: C0         RET     NZ              
5604: A0         AND     B               
5605: A0         AND     B               
5606: 9F         SBC     A               
5607: 97         SUB     A               
5608: C8         RET     Z               
5609: 88         ADC     A,B             
560A: E8 C0      ADD     SP,$C0          
560C: F3         DI                      
560D: A1         AND     C               
560E: D3         ???                     
560F: B3         OR      E               
5610: 01 01 03   LD      BC,$0301        
5613: 03         INC     BC              
5614: 05         DEC     B               
5615: 05         DEC     B               
5616: F9         LD      SP,HL           
5617: E9         JP      (HL)            
5618: 13         INC     DE              
5619: 11 17 03   LD      DE,$0317        
561C: CF         RST     0X08            
561D: 85         ADD     A,L             
561E: CB CD      SET     1,E             
5620: D3         ???                     
5621: B3         OR      E               
5622: D3         ???                     
5623: B3         OR      E               
5624: D9         RETI                    
5625: B1         OR      C               
5626: E5         PUSH    HL              
5627: A1         AND     C               
5628: ED         ???                     
5629: AD         XOR     L               
562A: F6 BC      OR      $BC             
562C: C3 BE FF   JP      $FFBE           
562F: FF         RST     0X38            
5630: CB CD      SET     1,E             
5632: CB CD      SET     1,E             
5634: 9B         SBC     E               
5635: 8D         ADC     A,L             
5636: A7         AND     A               
5637: 85         ADD     A,L             
5638: B7         OR      A               
5639: B5         OR      L               
563A: 6F         LD      L,A             
563B: 3D         DEC     A               
563C: C3 7D FF   JP      $FF7D           
563F: FF         RST     0X38            
5640: 7E         LD      A,(HL)          
5641: FF         RST     0X38            
5642: FC         ???                     
5643: 3F         CCF                     
5644: D8         RET     C               
5645: FF         RST     0X38            
5646: 00         NOP                     
5647: FF         RST     0X38            
5648: 00         NOP                     
5649: FF         RST     0X38            
564A: 0D         DEC     C               
564B: F2         ???                     
564C: FF         RST     0X38            
564D: 00         NOP                     
564E: 00         NOP                     
564F: 00         NOP                     
5650: E7         RST     0X20            
5651: F8 30      LDHL    SP,$30          
5653: FF         RST     0X38            
5654: 1F         RRA                     
5655: FF         RST     0X38            
5656: 1F         RRA                     
5657: EF         RST     0X28            
5658: 3F         CCF                     
5659: CF         RST     0X08            
565A: FF         RST     0X38            
565B: 1F         RRA                     
565C: FF         RST     0X38            
565D: 3F         CCF                     
565E: FF         RST     0X38            
565F: FF         RST     0X38            
5660: E7         RST     0X20            
5661: 1F         RRA                     
5662: 0C         INC     C               
5663: FF         RST     0X38            
5664: F8 FF      LDHL    SP,$FF          
5666: F8 F7      LDHL    SP,$F7          
5668: FC         ???                     
5669: F3         DI                      
566A: FF         RST     0X38            
566B: F8 FF      LDHL    SP,$FF          
566D: FC         ???                     
566E: FF         RST     0X38            
566F: FF         RST     0X38            
5670: FF         RST     0X38            
5671: 00         NOP                     
5672: 00         NOP                     
5673: FF         RST     0X38            
5674: FF         RST     0X38            
5675: FF         RST     0X38            
5676: FF         RST     0X38            
5677: FF         RST     0X38            
5678: FF         RST     0X38            
5679: FF         RST     0X38            
567A: FF         RST     0X38            
567B: FF         RST     0X38            
567C: FF         RST     0X38            
567D: FF         RST     0X38            
567E: FF         RST     0X38            
567F: FF         RST     0X38            
5680: 00         NOP                     
5681: 00         NOP                     
5682: FF         RST     0X38            
5683: 00         NOP                     
5684: 0D         DEC     C               
5685: F2         ???                     
5686: 00         NOP                     
5687: FF         RST     0X38            
5688: 00         NOP                     
5689: FF         RST     0X38            
568A: D8         RET     C               
568B: FF         RST     0X38            
568C: FC         ???                     
568D: 3F         CCF                     
568E: 7E         LD      A,(HL)          
568F: FF         RST     0X38            
5690: FF         RST     0X38            
5691: FF         RST     0X38            
5692: FF         RST     0X38            
5693: 3F         CCF                     
5694: FF         RST     0X38            
5695: 1F         RRA                     
5696: 3F         CCF                     
5697: CF         RST     0X08            
5698: 1F         RRA                     
5699: EF         RST     0X28            
569A: 1F         RRA                     
569B: FF         RST     0X38            
569C: 30 FF      JR      NC,$569D        
569E: E7         RST     0X20            
569F: F8 FF      LDHL    SP,$FF          
56A1: FF         RST     0X38            
56A2: FF         RST     0X38            
56A3: FC         ???                     
56A4: FF         RST     0X38            
56A5: F8 FC      LDHL    SP,$FC          
56A7: F3         DI                      
56A8: F8 F7      LDHL    SP,$F7          
56AA: F8 FF      LDHL    SP,$FF          
56AC: 0C         INC     C               
56AD: FF         RST     0X38            
56AE: E7         RST     0X20            
56AF: 1F         RRA                     
56B0: FF         RST     0X38            
56B1: FF         RST     0X38            
56B2: FF         RST     0X38            
56B3: FF         RST     0X38            
56B4: FF         RST     0X38            
56B5: FF         RST     0X38            
56B6: FF         RST     0X38            
56B7: FF         RST     0X38            
56B8: FF         RST     0X38            
56B9: FF         RST     0X38            
56BA: FF         RST     0X38            
56BB: FF         RST     0X38            
56BC: 00         NOP                     
56BD: FF         RST     0X38            
56BE: FF         RST     0X38            
56BF: 00         NOP                     
56C0: FF         RST     0X38            
56C1: FF         RST     0X38            
56C2: 9F         SBC     A               
56C3: 81         ADD     A,C             
56C4: E7         RST     0X20            
56C5: 80         ADD     A,B             
56C6: F8 80      LDHL    SP,$80          
56C8: FB         EI                      
56C9: 83         ADD     A,E             
56CA: FB         EI                      
56CB: 93         SUB     E               
56CC: F9         LD      SP,HL           
56CD: B1         OR      C               
56CE: B9         CP      C               
56CF: A1         AND     C               
56D0: FF         RST     0X38            
56D1: FF         RST     0X38            
56D2: F9         LD      SP,HL           
56D3: 81         ADD     A,C             
56D4: E1         POP     HL              
56D5: 07         RLCA                    
56D6: 01 1F C1   LD      BC,$C11F        
56D9: DF         RST     0X18            
56DA: C9         RET                     
56DB: DF         RST     0X18            
56DC: 8D         ADC     A,L             
56DD: 9F         SBC     A               
56DE: 87         ADD     A,A             
56DF: 9D         SBC     L               
56E0: B8         CP      B               
56E1: 80         ADD     A,B             
56E2: F0 87      LD      A,($87)         
56E4: E1         POP     HL              
56E5: 8F         ADC     A,A             
56E6: C1         POP     BC              
56E7: 9F         SBC     A               
56E8: 81         ADD     A,C             
56E9: BF         CP      A               
56EA: 81         ADD     A,C             
56EB: BE         CP      (HL)            
56EC: 80         ADD     A,B             
56ED: FF         RST     0X38            
56EE: FF         RST     0X38            
56EF: FF         RST     0X38            
56F0: 03         INC     BC              
56F1: 1D         DEC     E               
56F2: 11 EF 89   LD      DE,$89EF        
56F5: F7         RST     0X30            
56F6: 85         ADD     A,L             
56F7: FB         EI                      
56F8: 83         ADD     A,E             
56F9: FD         ???                     
56FA: 83         ADD     A,E             
56FB: 7D         LD      A,L             
56FC: 01 FF FF   LD      BC,$FFFF        
56FF: FF         RST     0X38            
5700: 00         NOP                     
5701: 00         NOP                     
5702: FF         RST     0X38            
5703: 00         NOP                     
5704: DF         RST     0X18            
5705: 3F         CCF                     
5706: BF         CP      A               
5707: 7F         LD      A,A             
5708: FF         RST     0X38            
5709: 7F         LD      A,A             
570A: FF         RST     0X38            
570B: 7F         LD      A,A             
570C: FF         RST     0X38            
570D: 7C         LD      A,H             
570E: FF         RST     0X38            
570F: 78         LD      A,B             
5710: 00         NOP                     
5711: 00         NOP                     
5712: FF         RST     0X38            
5713: 00         NOP                     
5714: FB         EI                      
5715: FC         ???                     
5716: FD         ???                     
5717: 86         ADD     A,(HL)          
5718: DF         RST     0X18            
5719: 82         ADD     A,D             
571A: AF         XOR     A               
571B: C2 97 E2   JP      NZ,$E297        
571E: CB 72      SET     1,E             
5720: FB         EI                      
5721: 70         LD      (HL),B          
5722: F4         ???                     
5723: 78         LD      A,B             
5724: F1         POP     AF              
5725: 7E         LD      A,(HL)          
5726: FC         ???                     
5727: 7F         LD      A,A             
5728: EB         ???                     
5729: 47         LD      B,A             
572A: C1         POP     BC              
572B: 40         LD      B,B             
572C: C0         RET     NZ              
572D: 40         LD      B,B             
572E: FF         RST     0X38            
572F: FF         RST     0X38            
5730: E7         RST     0X20            
5731: 3A         LD      A,(HLD)         
5732: F3         DI                      
5733: 1E 3B      LD      E,$3B           
5735: 0E 4F      LD      C,$4F           
5737: 86         ADD     A,(HL)          
5738: 97         SUB     A               
5739: E2         LDFF00  (C),A           
573A: 73         LD      (HL),E          
573B: FE 2F      CP      $2F             
573D: 1E FF      LD      E,$FF           
573F: FE FF      CP      $FF             
5741: EF         RST     0X28            
5742: FF         RST     0X38            
5743: EF         RST     0X28            
5744: FF         RST     0X38            
5745: FF         RST     0X38            
5746: 83         ADD     A,E             
5747: 80         ADD     A,B             
5748: B0         OR      B               
5749: 80         ADD     A,B             
574A: FF         RST     0X38            
574B: FF         RST     0X38            
574C: FF         RST     0X38            
574D: EF         RST     0X28            
574E: FF         RST     0X38            
574F: EF         RST     0X28            
5750: FF         RST     0X38            
5751: F7         RST     0X30            
5752: FF         RST     0X38            
5753: F7         RST     0X30            
5754: FF         RST     0X38            
5755: FF         RST     0X38            
5756: 01 01 19   LD      BC,$1901        
5759: 01 FF FF   LD      BC,$FFFF        
575C: FF         RST     0X38            
575D: F7         RST     0X30            
575E: FF         RST     0X38            
575F: F7         RST     0X30            
5760: FF         RST     0X38            
5761: FF         RST     0X38            
5762: C2 C0 FF   JP      NZ,$FFC0        
5765: FF         RST     0X38            
5766: 90         SUB     B               
5767: 80         ADD     A,B             
5768: FF         RST     0X38            
5769: FF         RST     0X38            
576A: 80         ADD     A,B             
576B: 80         ADD     A,B             
576C: FF         RST     0X38            
576D: FF         RST     0X38            
576E: C2 C0 FF   JP      NZ,$FFC0        
5771: FF         RST     0X38            
5772: 13         INC     DE              
5773: 03         INC     BC              
5774: FF         RST     0X38            
5775: FF         RST     0X38            
5776: 21 01 FF   LD      HL,$FF01        
5779: FF         RST     0X38            
577A: 03         INC     BC              
577B: 03         INC     BC              
577C: FF         RST     0X38            
577D: FF         RST     0X38            
577E: 09         ADD     HL,BC           
577F: 01 FF FF   LD      BC,$FFFF        
5782: 80         ADD     A,B             
5783: 80         ADD     A,B             
5784: 9B         SBC     E               
5785: 83         ADD     A,E             
5786: FE FE      CP      $FE             
5788: F8 F8      LDHL    SP,$F8          
578A: FB         EI                      
578B: FB         EI                      
578C: FD         ???                     
578D: F9         LD      SP,HL           
578E: FE FC      CP      $FC             
5790: FF         RST     0X38            
5791: FF         RST     0X38            
5792: 33         INC     SP              
5793: 03         INC     BC              
5794: C3 C3 7F   JP      $7FC3           
5797: 7F         LD      A,A             
5798: FF         RST     0X38            
5799: FF         RST     0X38            
579A: DF         RST     0X18            
579B: DF         RST     0X18            
579C: BF         CP      A               
579D: 9F         SBC     A               
579E: 7F         LD      A,A             
579F: 3F         CCF                     
57A0: FC         ???                     
57A1: FC         ???                     
57A2: FB         EI                      
57A3: F9         LD      SP,HL           
57A4: FB         EI                      
57A5: FB         EI                      
57A6: FF         RST     0X38            
57A7: FF         RST     0X38            
57A8: FE FE      CP      $FE             
57AA: FE FE      CP      $FE             
57AC: FF         RST     0X38            
57AD: FF         RST     0X38            
57AE: CC C0 3F   CALL    Z,$3FC0         
57B1: 3F         CCF                     
57B2: DF         RST     0X18            
57B3: 9F         SBC     A               
57B4: DF         RST     0X18            
57B5: DF         RST     0X18            
57B6: 3F         CCF                     
57B7: 1F         RRA                     
57B8: 7F         LD      A,A             
57B9: 7F         LD      A,A             
57BA: 7F         LD      A,A             
57BB: 7F         LD      A,A             
57BC: FF         RST     0X38            
57BD: FF         RST     0X38            
57BE: 19         ADD     HL,DE           
57BF: 01 FF FF   LD      BC,$FFFF        
57C2: 9F         SBC     A               
57C3: 81         ADD     A,C             
57C4: E7         RST     0X20            
57C5: 80         ADD     A,B             
57C6: F8 80      LDHL    SP,$80          
57C8: FB         EI                      
57C9: 83         ADD     A,E             
57CA: FB         EI                      
57CB: 93         SUB     E               
57CC: F9         LD      SP,HL           
57CD: B1         OR      C               
57CE: B9         CP      C               
57CF: A1         AND     C               
57D0: FF         RST     0X38            
57D1: FF         RST     0X38            
57D2: F9         LD      SP,HL           
57D3: 81         ADD     A,C             
57D4: E1         POP     HL              
57D5: 07         RLCA                    
57D6: 01 1F C1   LD      BC,$C11F        
57D9: DF         RST     0X18            
57DA: C9         RET                     
57DB: DF         RST     0X18            
57DC: 8D         ADC     A,L             
57DD: 9F         SBC     A               
57DE: 87         ADD     A,A             
57DF: 9D         SBC     L               
57E0: B8         CP      B               
57E1: 80         ADD     A,B             
57E2: F0 87      LD      A,($87)         
57E4: E1         POP     HL              
57E5: 8F         ADC     A,A             
57E6: C1         POP     BC              
57E7: 9F         SBC     A               
57E8: 81         ADD     A,C             
57E9: BF         CP      A               
57EA: 81         ADD     A,C             
57EB: BE         CP      (HL)            
57EC: 80         ADD     A,B             
57ED: FF         RST     0X38            
57EE: FF         RST     0X38            
57EF: FF         RST     0X38            
57F0: 03         INC     BC              
57F1: 1D         DEC     E               
57F2: 11 EF 89   LD      DE,$89EF        
57F5: F7         RST     0X30            
57F6: 85         ADD     A,L             
57F7: FB         EI                      
57F8: 83         ADD     A,E             
57F9: FD         ???                     
57FA: 83         ADD     A,E             
57FB: 7D         LD      A,L             
57FC: 01 FF FF   LD      BC,$FFFF        
57FF: FF         RST     0X38            
5800: FF         RST     0X38            
5801: FE 9D      CP      $9D             
5803: E1         POP     HL              
5804: 9D         SBC     L               
5805: E1         POP     HL              
5806: A9         XOR     C               
5807: D1         POP     DE              
5808: A9         XOR     C               
5809: D1         POP     DE              
580A: 99         SBC     C               
580B: E1         POP     HL              
580C: 9D         SBC     L               
580D: E1         POP     HL              
580E: 9D         SBC     L               
580F: E1         POP     HL              
5810: 89         ADC     A,C             
5811: F1         POP     AF              
5812: A9         XOR     C               
5813: D1         POP     DE              
5814: A9         XOR     C               
5815: D1         POP     DE              
5816: BD         CP      L               
5817: FD         ???                     
5818: C3 C3 81   JP      $81C3           
581B: 99         SBC     C               
581C: 81         ADD     A,C             
581D: A5         AND     L               
581E: 81         ADD     A,C             
581F: A5         AND     L               
5820: FF         RST     0X38            
5821: 7F         LD      A,A             
5822: B9         CP      C               
5823: 87         ADD     A,A             
5824: B9         CP      C               
5825: 87         ADD     A,A             
5826: 95         SUB     L               
5827: 8B         ADC     A,E             
5828: 95         SUB     L               
5829: 8B         ADC     A,E             
582A: 99         SBC     C               
582B: 87         ADD     A,A             
582C: B9         CP      C               
582D: 87         ADD     A,A             
582E: B9         CP      C               
582F: 87         ADD     A,A             
5830: 91         SUB     C               
5831: 8F         ADC     A,A             
5832: 95         SUB     L               
5833: 8B         ADC     A,E             
5834: 95         SUB     L               
5835: 8B         ADC     A,E             
5836: BD         CP      L               
5837: BF         CP      A               
5838: C3 C3 81   JP      $81C3           
583B: 99         SBC     C               
583C: 81         ADD     A,C             
583D: A5         AND     L               
583E: 81         ADD     A,C             
583F: A5         AND     L               
5840: FF         RST     0X38            
5841: FF         RST     0X38            
5842: FF         RST     0X38            
5843: 00         NOP                     
5844: FF         RST     0X38            
5845: 00         NOP                     
5846: FF         RST     0X38            
5847: 00         NOP                     
5848: FF         RST     0X38            
5849: 00         NOP                     
584A: FF         RST     0X38            
584B: 00         NOP                     
584C: FF         RST     0X38            
584D: 00         NOP                     
584E: FF         RST     0X38            
584F: 00         NOP                     
5850: FF         RST     0X38            
5851: 00         NOP                     
5852: FF         RST     0X38            
5853: 00         NOP                     
5854: FF         RST     0X38            
5855: 00         NOP                     
5856: 00         NOP                     
5857: 00         NOP                     
5858: 00         NOP                     
5859: FF         RST     0X38            
585A: FF         RST     0X38            
585B: FF         RST     0X38            
585C: 00         NOP                     
585D: FF         RST     0X38            
585E: FF         RST     0X38            
585F: 00         NOP                     
5860: E0 80      LDFF00  ($80),A         
5862: FF         RST     0X38            
5863: 80         ADD     A,B             
5864: BF         CP      A               
5865: C0         RET     NZ              
5866: FF         RST     0X38            
5867: FF         RST     0X38            
5868: C0         RET     NZ              
5869: 7F         LD      A,A             
586A: BF         CP      A               
586B: 7F         LD      A,A             
586C: 00         NOP                     
586D: 00         NOP                     
586E: FF         RST     0X38            
586F: 00         NOP                     
5870: 07         RLCA                    
5871: 01 FF 01   LD      BC,$01FF        
5874: FD         ???                     
5875: 03         INC     BC              
5876: FF         RST     0X38            
5877: FF         RST     0X38            
5878: 03         INC     BC              
5879: FE FC      CP      $FC             
587B: FE 00      CP      $00             
587D: 00         NOP                     
587E: FF         RST     0X38            
587F: 00         NOP                     
5880: 00         NOP                     
5881: 00         NOP                     
5882: 7F         LD      A,A             
5883: 3F         CCF                     
5884: 70         LD      (HL),B          
5885: 6F         LD      L,A             
5886: 60         LD      H,B             
5887: 5F         LD      E,A             
5888: 67         LD      H,A             
5889: 5F         LD      E,A             
588A: 78         LD      A,B             
588B: 78         LD      A,B             
588C: 4B         LD      C,E             
588D: 48         LD      C,B             
588E: 7F         LD      A,A             
588F: 7F         LD      A,A             
5890: 00         NOP                     
5891: 00         NOP                     
5892: FE FC      CP      $FC             
5894: 06 FE      LD      B,$FE           
5896: 02         LD      (BC),A          
5897: FE E2      CP      $E2             
5899: FE 1E      CP      $1E             
589B: 1E D2      LD      E,$D2           
589D: 12         LD      (DE),A          
589E: FE FE      CP      $FE             
58A0: C0         RET     NZ              
58A1: 80         ADD     A,B             
58A2: C0         RET     NZ              
58A3: 80         ADD     A,B             
58A4: FE 80      CP      $80             
58A6: E0 80      LDFF00  ($80),A         
58A8: C0         RET     NZ              
58A9: 80         ADD     A,B             
58AA: C0         RET     NZ              
58AB: 80         ADD     A,B             
58AC: C0         RET     NZ              
58AD: 80         ADD     A,B             
58AE: C0         RET     NZ              
58AF: 80         ADD     A,B             
58B0: 03         INC     BC              
58B1: 01 03 01   LD      BC,$0103        
58B4: 07         RLCA                    
58B5: 01 03 01   LD      BC,$0103        
58B8: 03         INC     BC              
58B9: 01 03 01   LD      BC,$0103        
58BC: 03         INC     BC              
58BD: 01 03 01   LD      BC,$0103        
58C0: 1F         RRA                     
58C1: 1F         RRA                     
58C2: 3F         CCF                     
58C3: 20 7F      JR      NZ,$5944        
58C5: 40         LD      B,B             
58C6: 7F         LD      A,A             
58C7: 40         LD      B,B             
58C8: 7F         LD      A,A             
58C9: 40         LD      B,B             
58CA: 7F         LD      A,A             
58CB: 40         LD      B,B             
58CC: 7F         LD      A,A             
58CD: 40         LD      B,B             
58CE: 7F         LD      A,A             
58CF: 40         LD      B,B             
58D0: F8 F8      LDHL    SP,$F8          
58D2: FC         ???                     
58D3: 04         INC     B               
58D4: FE 02      CP      $02             
58D6: FE 02      CP      $02             
58D8: FE 02      CP      $02             
58DA: FE 02      CP      $02             
58DC: FE 02      CP      $02             
58DE: FE 02      CP      $02             
58E0: 7F         LD      A,A             
58E1: 40         LD      B,B             
58E2: 5F         LD      E,A             
58E3: 40         LD      B,B             
58E4: 6F         LD      L,A             
58E5: 40         LD      B,B             
58E6: 50         LD      D,B             
58E7: 60         LD      H,B             
58E8: 20 3F      JR      NZ,$5929        
58EA: 3F         CCF                     
58EB: 3F         CCF                     
58EC: 2D         DEC     L               
58ED: 33         INC     SP              
58EE: 3F         CCF                     
58EF: 1E FE      LD      E,$FE           
58F1: 02         LD      (BC),A          
58F2: FA 02 F6   LD      A,($F602)       
58F5: 02         LD      (BC),A          
58F6: 0A         LD      A,(BC)          
58F7: 06 04      LD      B,$04           
58F9: FC         ???                     
58FA: FC         ???                     
58FB: FC         ???                     
58FC: B4         OR      H               
58FD: CC FC 78   CALL    Z,$78FC         
5900: 03         INC     BC              
5901: 03         INC     BC              
5902: 04         INC     B               
5903: 04         INC     B               
5904: 0A         LD      A,(BC)          
5905: 08 15 10   LD      ($1015),SP      
5908: 2C         INC     L               
5909: 21 58 45   LD      HL,$4558        
590C: 52         LD      D,D             
590D: 49         LD      C,C             
590E: 52         LD      D,D             
590F: 49         LD      C,C             
5910: C0         RET     NZ              
5911: C0         RET     NZ              
5912: 20 20      JR      NZ,$5934        
5914: 50         LD      D,B             
5915: 10 A8      STOP    $A8             
5917: 08 14 A4   LD      ($A414),SP      
591A: 0A         LD      A,(BC)          
591B: B2         OR      D               
591C: 26 9A      LD      H,$9A           
591E: 42         LD      B,D             
591F: 9A         SBC     D               
5920: 4A         LD      C,D             
5921: 41         LD      B,C             
5922: 73         LD      (HL),E          
5923: 40         LD      B,B             
5924: E8 50      ADD     SP,$50          
5926: E2         LDFF00  (C),A           
5927: 59         LD      E,C             
5928: C1         POP     BC              
5929: 7B         LD      A,E             
592A: E5         PUSH    HL              
592B: 3B         DEC     SP              
592C: 74         LD      (HL),H          
592D: 1B         DEC     DE              
592E: 3F         CCF                     
592F: 0F         RRCA                    
5930: 46         LD      B,(HL)          
5931: 92         SUB     D               
5932: CA 06 1B   JP      Z,$1B06         
5935: 0E 2B      LD      C,$2B           
5937: DE BF      SBC     $BF             
5939: DE BF      SBC     $BF             
593B: DC 3E D8   CALL    C,$D83E         
593E: FC         ???                     
593F: F0 04      LD      A,($04)         
5941: 09         ADD     HL,BC           
5942: 7F         LD      A,A             
5943: 0D         DEC     C               
5944: 3B         DEC     SP              
5945: 6F         LD      L,A             
5946: 70         LD      (HL),B          
5947: 3F         CCF                     
5948: E7         RST     0X20            
5949: 38 E9      JR      C,$5934         
594B: B0         OR      B               
594C: 58         LD      E,B             
594D: E0 19      LDFF00  ($19),A         
594F: 60         LD      H,B             
5950: 30 10      JR      NC,$5962        
5952: F6 30      OR      $30             
5954: DC F6 0C   CALL    C,$0CF6         
5957: FC         ???                     
5958: E5         PUSH    HL              
5959: 1C         INC     E               
595A: 17         RLA                     
595B: 0D         DEC     C               
595C: 9A         SBC     D               
595D: 07         RLCA                    
595E: 48         LD      C,B             
595F: 06 26      LD      B,$26           
5961: 40         LD      B,B             
5962: 22         LD      (HLI),A         
5963: C0         RET     NZ              
5964: 2F         CPL                     
5965: 40         LD      B,B             
5966: 31 40 18   LD      SP,$1840        
5969: E0 0F      LDFF00  ($0F),A         
596B: 30 03      JR      NC,$5970        
596D: 1C         INC     E               
596E: 00         NOP                     
596F: 33         INC     SP              
5970: 3C         INC     A               
5971: 02         LD      (BC),A          
5972: 2C         INC     L               
5973: 03         INC     BC              
5974: C4 02 24   CALL    NZ,$2402        
5977: 02         LD      (BC),A          
5978: 9C         SBC     H               
5979: 03         INC     BC              
597A: F8 06      LDHL    SP,$06          
597C: 00         NOP                     
597D: FC         ???                     
597E: 00         NOP                     
597F: 26 00      LD      H,$00           
5981: 00         NOP                     
5982: 00         NOP                     
5983: 1F         RRA                     
5984: 1F         RRA                     
5985: 20 3F      JR      NZ,$59C6        
5987: 40         LD      B,B             
5988: 3F         CCF                     
5989: 40         LD      B,B             
598A: 3C         INC     A               
598B: 43         LD      B,E             
598C: 38 47      JR      C,$59D5         
598E: 38 47      JR      C,$59D7         
5990: 00         NOP                     
5991: 00         NOP                     
5992: 00         NOP                     
5993: F8 F8      LDHL    SP,$F8          
5995: 04         INC     B               
5996: FC         ???                     
5997: 02         LD      (BC),A          
5998: FC         ???                     
5999: 02         LD      (BC),A          
599A: 3C         INC     A               
599B: C2 1C E2   JP      NZ,$E21C        
599E: 1C         INC     E               
599F: E2         LDFF00  (C),A           
59A0: 38 47      JR      C,$59E9         
59A2: 38 47      JR      C,$59EB         
59A4: 3C         INC     A               
59A5: 43         LD      B,E             
59A6: 3F         CCF                     
59A7: 40         LD      B,B             
59A8: 3F         CCF                     
59A9: 40         LD      B,B             
59AA: 1F         RRA                     
59AB: 20 00      JR      NZ,$59AD        
59AD: 1F         RRA                     
59AE: 00         NOP                     
59AF: 00         NOP                     
59B0: 1C         INC     E               
59B1: E2         LDFF00  (C),A           
59B2: 1C         INC     E               
59B3: E2         LDFF00  (C),A           
59B4: 3C         INC     A               
59B5: C2 FC 02   JP      NZ,$02FC        
59B8: FC         ???                     
59B9: 02         LD      (BC),A          
59BA: F8 04      LDHL    SP,$04          
59BC: 00         NOP                     
59BD: F8 00      LDHL    SP,$00          
59BF: 00         NOP                     
59C0: FF         RST     0X38            
59C1: FF         RST     0X38            
59C2: 9F         SBC     A               
59C3: 81         ADD     A,C             
59C4: E7         RST     0X20            
59C5: 80         ADD     A,B             
59C6: F8 80      LDHL    SP,$80          
59C8: FB         EI                      
59C9: 83         ADD     A,E             
59CA: FB         EI                      
59CB: 93         SUB     E               
59CC: F9         LD      SP,HL           
59CD: B1         OR      C               
59CE: B9         CP      C               
59CF: A1         AND     C               
59D0: FF         RST     0X38            
59D1: FF         RST     0X38            
59D2: F9         LD      SP,HL           
59D3: 81         ADD     A,C             
59D4: E1         POP     HL              
59D5: 07         RLCA                    
59D6: 01 1F C1   LD      BC,$C11F        
59D9: DF         RST     0X18            
59DA: C9         RET                     
59DB: DF         RST     0X18            
59DC: 8D         ADC     A,L             
59DD: 9F         SBC     A               
59DE: 87         ADD     A,A             
59DF: 9D         SBC     L               
59E0: B8         CP      B               
59E1: 80         ADD     A,B             
59E2: F0 87      LD      A,($87)         
59E4: E1         POP     HL              
59E5: 8F         ADC     A,A             
59E6: C1         POP     BC              
59E7: 9F         SBC     A               
59E8: 81         ADD     A,C             
59E9: BF         CP      A               
59EA: 81         ADD     A,C             
59EB: BE         CP      (HL)            
59EC: 80         ADD     A,B             
59ED: FF         RST     0X38            
59EE: FF         RST     0X38            
59EF: FF         RST     0X38            
59F0: 03         INC     BC              
59F1: 1D         DEC     E               
59F2: 11 EF 89   LD      DE,$89EF        
59F5: F7         RST     0X30            
59F6: 85         ADD     A,L             
59F7: FB         EI                      
59F8: 83         ADD     A,E             
59F9: FD         ???                     
59FA: 83         ADD     A,E             
59FB: 7D         LD      A,L             
59FC: 01 FF FF   LD      BC,$FFFF        
59FF: FF         RST     0X38            
5A00: 80         ADD     A,B             
5A01: 80         ADD     A,B             
5A02: C0         RET     NZ              
5A03: C0         RET     NZ              
5A04: A0         AND     B               
5A05: A0         AND     B               
5A06: 9F         SBC     A               
5A07: 97         SUB     A               
5A08: C8         RET     Z               
5A09: 88         ADC     A,B             
5A0A: E8 C0      ADD     SP,$C0          
5A0C: F3         DI                      
5A0D: A1         AND     C               
5A0E: D3         ???                     
5A0F: B3         OR      E               
5A10: 01 01 03   LD      BC,$0301        
5A13: 03         INC     BC              
5A14: 05         DEC     B               
5A15: 05         DEC     B               
5A16: F9         LD      SP,HL           
5A17: E9         JP      (HL)            
5A18: 13         INC     DE              
5A19: 11 17 03   LD      DE,$0317        
5A1C: CF         RST     0X08            
5A1D: 85         ADD     A,L             
5A1E: CB CD      SET     1,E             
5A20: D3         ???                     
5A21: B3         OR      E               
5A22: D3         ???                     
5A23: B3         OR      E               
5A24: D9         RETI                    
5A25: B1         OR      C               
5A26: E5         PUSH    HL              
5A27: A1         AND     C               
5A28: ED         ???                     
5A29: AD         XOR     L               
5A2A: F6 BC      OR      $BC             
5A2C: C3 BE FF   JP      $FFBE           
5A2F: FF         RST     0X38            
5A30: CB CD      SET     1,E             
5A32: CB CD      SET     1,E             
5A34: 9B         SBC     E               
5A35: 8D         ADC     A,L             
5A36: A7         AND     A               
5A37: 85         ADD     A,L             
5A38: B7         OR      A               
5A39: B5         OR      L               
5A3A: 6F         LD      L,A             
5A3B: 3D         DEC     A               
5A3C: C3 7D FF   JP      $FF7D           
5A3F: FF         RST     0X38            
5A40: 03         INC     BC              
5A41: 03         INC     BC              
5A42: 04         INC     B               
5A43: 04         INC     B               
5A44: 0A         LD      A,(BC)          
5A45: 08 15 10   LD      ($1015),SP      
5A48: 2C         INC     L               
5A49: 21 58 45   LD      HL,$4558        
5A4C: 52         LD      D,D             
5A4D: 49         LD      C,C             
5A4E: 52         LD      D,D             
5A4F: 49         LD      C,C             
5A50: C0         RET     NZ              
5A51: C0         RET     NZ              
5A52: 20 20      JR      NZ,$5A74        
5A54: 50         LD      D,B             
5A55: 10 A8      STOP    $A8             
5A57: 08 14 A4   LD      ($A414),SP      
5A5A: 0A         LD      A,(BC)          
5A5B: B2         OR      D               
5A5C: 26 9A      LD      H,$9A           
5A5E: 42         LD      B,D             
5A5F: 9A         SBC     D               
5A60: 4A         LD      C,D             
5A61: 41         LD      B,C             
5A62: 73         LD      (HL),E          
5A63: 40         LD      B,B             
5A64: E8 50      ADD     SP,$50          
5A66: E2         LDFF00  (C),A           
5A67: 59         LD      E,C             
5A68: C1         POP     BC              
5A69: 7B         LD      A,E             
5A6A: E5         PUSH    HL              
5A6B: 3B         DEC     SP              
5A6C: 74         LD      (HL),H          
5A6D: 1B         DEC     DE              
5A6E: 3F         CCF                     
5A6F: 0F         RRCA                    
5A70: 46         LD      B,(HL)          
5A71: 92         SUB     D               
5A72: CA 06 1B   JP      Z,$1B06         
5A75: 0E 2B      LD      C,$2B           
5A77: DE BF      SBC     $BF             
5A79: DE BF      SBC     $BF             
5A7B: DC 3E D8   CALL    C,$D83E         
5A7E: FC         ???                     
5A7F: F0 00      LD      A,($00)         
5A81: FF         RST     0X38            
5A82: 00         NOP                     
5A83: 80         ADD     A,B             
5A84: 3F         CCF                     
5A85: 83         ADD     A,E             
5A86: 3F         CCF                     
5A87: 82         ADD     A,D             
5A88: 3F         CCF                     
5A89: BE         CP      (HL)            
5A8A: 3F         CCF                     
5A8B: A2         AND     D               
5A8C: 3F         CCF                     
5A8D: A2         AND     D               
5A8E: 3F         CCF                     
5A8F: A2         AND     D               
5A90: 3F         CCF                     
5A91: FF         RST     0X38            
5A92: 3F         CCF                     
5A93: 21 FF E1   LD      HL,$E1FF        
5A96: FF         RST     0X38            
5A97: 21 FF 21   LD      HL,$21FF        
5A9A: FF         RST     0X38            
5A9B: 21 E1 21   LD      HL,$21E1        
5A9E: FF         RST     0X38            
5A9F: 3F         CCF                     
5AA0: 3E A2      LD      A,$A2           
5AA2: 3F         CCF                     
5AA3: A3         AND     E               
5AA4: 23         INC     HL              
5AA5: A3         AND     E               
5AA6: 3F         CCF                     
5AA7: BF         CP      A               
5AA8: 3F         CCF                     
5AA9: BF         CP      A               
5AAA: 3F         CCF                     
5AAB: 80         ADD     A,B             
5AAC: 00         NOP                     
5AAD: 80         ADD     A,B             
5AAE: 00         NOP                     
5AAF: FF         RST     0X38            
5AB0: 3F         CCF                     
5AB1: 3F         CCF                     
5AB2: FF         RST     0X38            
5AB3: FF         RST     0X38            
5AB4: FF         RST     0X38            
5AB5: FF         RST     0X38            
5AB6: FF         RST     0X38            
5AB7: FF         RST     0X38            
5AB8: FF         RST     0X38            
5AB9: FF         RST     0X38            
5ABA: FE 01      CP      $01             
5ABC: 00         NOP                     
5ABD: 01 00 FF   LD      BC,$FF00        
5AC0: FF         RST     0X38            
5AC1: FF         RST     0X38            
5AC2: 9F         SBC     A               
5AC3: 81         ADD     A,C             
5AC4: E7         RST     0X20            
5AC5: 80         ADD     A,B             
5AC6: F8 80      LDHL    SP,$80          
5AC8: FB         EI                      
5AC9: 83         ADD     A,E             
5ACA: FB         EI                      
5ACB: 93         SUB     E               
5ACC: F9         LD      SP,HL           
5ACD: B1         OR      C               
5ACE: B9         CP      C               
5ACF: A1         AND     C               
5AD0: FF         RST     0X38            
5AD1: FF         RST     0X38            
5AD2: F9         LD      SP,HL           
5AD3: 81         ADD     A,C             
5AD4: E1         POP     HL              
5AD5: 07         RLCA                    
5AD6: 01 1F C1   LD      BC,$C11F        
5AD9: DF         RST     0X18            
5ADA: C9         RET                     
5ADB: DF         RST     0X18            
5ADC: 8D         ADC     A,L             
5ADD: 9F         SBC     A               
5ADE: 87         ADD     A,A             
5ADF: 9D         SBC     L               
5AE0: B8         CP      B               
5AE1: 80         ADD     A,B             
5AE2: F0 87      LD      A,($87)         
5AE4: E1         POP     HL              
5AE5: 8F         ADC     A,A             
5AE6: C1         POP     BC              
5AE7: 9F         SBC     A               
5AE8: 81         ADD     A,C             
5AE9: BF         CP      A               
5AEA: 81         ADD     A,C             
5AEB: BE         CP      (HL)            
5AEC: 80         ADD     A,B             
5AED: FF         RST     0X38            
5AEE: FF         RST     0X38            
5AEF: FF         RST     0X38            
5AF0: 03         INC     BC              
5AF1: 1D         DEC     E               
5AF2: 11 EF 89   LD      DE,$89EF        
5AF5: F7         RST     0X30            
5AF6: 85         ADD     A,L             
5AF7: FB         EI                      
5AF8: 83         ADD     A,E             
5AF9: FD         ???                     
5AFA: 83         ADD     A,E             
5AFB: 7D         LD      A,L             
5AFC: 01 FF FF   LD      BC,$FFFF        
5AFF: FF         RST     0X38            
5B00: 80         ADD     A,B             
5B01: 80         ADD     A,B             
5B02: 80         ADD     A,B             
5B03: 80         ADD     A,B             
5B04: 80         ADD     A,B             
5B05: 80         ADD     A,B             
5B06: FF         RST     0X38            
5B07: 83         ADD     A,E             
5B08: FF         RST     0X38            
5B09: 84         ADD     A,H             
5B0A: FF         RST     0X38            
5B0B: 88         ADC     A,B             
5B0C: FF         RST     0X38            
5B0D: 88         ADC     A,B             
5B0E: FF         RST     0X38            
5B0F: 88         ADC     A,B             
5B10: 01 01 01   LD      BC,$0101        
5B13: 01 01 01   LD      BC,$0101        
5B16: FF         RST     0X38            
5B17: C1         POP     BC              
5B18: FF         RST     0X38            
5B19: 21 FF 11   LD      HL,$11FF        
5B1C: FF         RST     0X38            
5B1D: 11 FF 11   LD      DE,$11FF        
5B20: FF         RST     0X38            
5B21: 9C         SBC     H               
5B22: F7         RST     0X30            
5B23: A0         AND     B               
5B24: EF         RST     0X28            
5B25: C8         RET     Z               
5B26: FF         RST     0X38            
5B27: F8 FE      LDHL    SP,$FE          
5B29: 88         ADC     A,B             
5B2A: FF         RST     0X38            
5B2B: 89         ADC     A,C             
5B2C: F9         LD      SP,HL           
5B2D: 89         ADC     A,C             
5B2E: FF         RST     0X38            
5B2F: FF         RST     0X38            
5B30: FF         RST     0X38            
5B31: 39         ADD     HL,SP           
5B32: EF         RST     0X28            
5B33: 05         DEC     B               
5B34: F7         RST     0X30            
5B35: 13         INC     DE              
5B36: FF         RST     0X38            
5B37: 1F         RRA                     
5B38: 7F         LD      A,A             
5B39: 11 FF 91   LD      DE,$91FF        
5B3C: 9F         SBC     A               
5B3D: 91         SUB     C               
5B3E: FF         RST     0X38            
5B3F: FF         RST     0X38            
5B40: 00         NOP                     
5B41: 00         NOP                     
5B42: 00         NOP                     
5B43: 00         NOP                     
5B44: 00         NOP                     
5B45: 00         NOP                     
5B46: 00         NOP                     
5B47: 00         NOP                     
5B48: 00         NOP                     
5B49: 00         NOP                     
5B4A: 00         NOP                     
5B4B: 00         NOP                     
5B4C: 00         NOP                     
5B4D: 00         NOP                     
5B4E: 00         NOP                     
5B4F: 00         NOP                     
5B50: 00         NOP                     
5B51: 00         NOP                     
5B52: 00         NOP                     
5B53: 00         NOP                     
5B54: 00         NOP                     
5B55: 00         NOP                     
5B56: 00         NOP                     
5B57: 00         NOP                     
5B58: 00         NOP                     
5B59: 00         NOP                     
5B5A: 00         NOP                     
5B5B: 00         NOP                     
5B5C: 00         NOP                     
5B5D: 00         NOP                     
5B5E: 00         NOP                     
5B5F: 00         NOP                     
5B60: 00         NOP                     
5B61: 00         NOP                     
5B62: 00         NOP                     
5B63: 00         NOP                     
5B64: 00         NOP                     
5B65: 00         NOP                     
5B66: 00         NOP                     
5B67: 00         NOP                     
5B68: 00         NOP                     
5B69: 00         NOP                     
5B6A: 00         NOP                     
5B6B: 00         NOP                     
5B6C: 00         NOP                     
5B6D: 00         NOP                     
5B6E: 00         NOP                     
5B6F: 00         NOP                     
5B70: 00         NOP                     
5B71: 00         NOP                     
5B72: 00         NOP                     
5B73: 00         NOP                     
5B74: 00         NOP                     
5B75: 00         NOP                     
5B76: 00         NOP                     
5B77: 00         NOP                     
5B78: 00         NOP                     
5B79: 00         NOP                     
5B7A: 00         NOP                     
5B7B: 00         NOP                     
5B7C: 00         NOP                     
5B7D: 00         NOP                     
5B7E: 00         NOP                     
5B7F: 00         NOP                     
5B80: 00         NOP                     
5B81: FF         RST     0X38            
5B82: 00         NOP                     
5B83: 80         ADD     A,B             
5B84: 3F         CCF                     
5B85: 83         ADD     A,E             
5B86: 3F         CCF                     
5B87: 82         ADD     A,D             
5B88: 3F         CCF                     
5B89: BE         CP      (HL)            
5B8A: 3F         CCF                     
5B8B: A2         AND     D               
5B8C: 3F         CCF                     
5B8D: A2         AND     D               
5B8E: 3F         CCF                     
5B8F: A2         AND     D               
5B90: 3F         CCF                     
5B91: FF         RST     0X38            
5B92: 3F         CCF                     
5B93: 21 FF E1   LD      HL,$E1FF        
5B96: FF         RST     0X38            
5B97: 21 FF 21   LD      HL,$21FF        
5B9A: FF         RST     0X38            
5B9B: 21 E1 21   LD      HL,$21E1        
5B9E: FF         RST     0X38            
5B9F: 3F         CCF                     
5BA0: 3E A2      LD      A,$A2           
5BA2: 3F         CCF                     
5BA3: A3         AND     E               
5BA4: 23         INC     HL              
5BA5: A3         AND     E               
5BA6: 3F         CCF                     
5BA7: BF         CP      A               
5BA8: 3F         CCF                     
5BA9: BF         CP      A               
5BAA: 3F         CCF                     
5BAB: 80         ADD     A,B             
5BAC: 00         NOP                     
5BAD: 80         ADD     A,B             
5BAE: 00         NOP                     
5BAF: FF         RST     0X38            
5BB0: 3F         CCF                     
5BB1: 3F         CCF                     
5BB2: FF         RST     0X38            
5BB3: FF         RST     0X38            
5BB4: FF         RST     0X38            
5BB5: FF         RST     0X38            
5BB6: FF         RST     0X38            
5BB7: FF         RST     0X38            
5BB8: FF         RST     0X38            
5BB9: FF         RST     0X38            
5BBA: FE 01      CP      $01             
5BBC: 00         NOP                     
5BBD: 01 00 FF   LD      BC,$FF00        
5BC0: 00         NOP                     
5BC1: 00         NOP                     
5BC2: FF         RST     0X38            
5BC3: 00         NOP                     
5BC4: DF         RST     0X18            
5BC5: 3F         CCF                     
5BC6: BF         CP      A               
5BC7: 7F         LD      A,A             
5BC8: FF         RST     0X38            
5BC9: 7F         LD      A,A             
5BCA: FF         RST     0X38            
5BCB: 7F         LD      A,A             
5BCC: FF         RST     0X38            
5BCD: 7F         LD      A,A             
5BCE: DF         RST     0X18            
5BCF: 7F         LD      A,A             
5BD0: 00         NOP                     
5BD1: 00         NOP                     
5BD2: FF         RST     0X38            
5BD3: 00         NOP                     
5BD4: FB         EI                      
5BD5: FC         ???                     
5BD6: FD         ???                     
5BD7: FE FF      CP      $FF             
5BD9: FE FF      CP      $FF             
5BDB: FE FF      CP      $FF             
5BDD: FE FF      CP      $FF             
5BDF: FE CD      CP      $CD             
5BE1: 7E         LD      A,(HL)          
5BE2: DB         ???                     
5BE3: 7C         LD      A,H             
5BE4: F7         RST     0X30            
5BE5: 78         LD      A,B             
5BE6: EF         RST     0X28            
5BE7: 70         LD      (HL),B          
5BE8: DD         ???                     
5BE9: 63         LD      H,E             
5BEA: F6 4F      OR      $4F             
5BEC: D8         RET     C               
5BED: 7C         LD      A,H             
5BEE: FF         RST     0X38            
5BEF: FF         RST     0X38            
5BF0: FF         RST     0X38            
5BF1: 7E         LD      A,(HL)          
5BF2: FF         RST     0X38            
5BF3: 3E FF      LD      A,$FF           
5BF5: 3E 63      LD      A,$63           
5BF7: F2         ???                     
5BF8: 83         ADD     A,E             
5BF9: C2 03 02   JP      NZ,$0203        
5BFC: 03         INC     BC              
5BFD: 02         LD      (BC),A          
5BFE: FF         RST     0X38            
5BFF: FF         RST     0X38            
5C00: FA DC 2D   LD      A,($2DDC)       
5C03: F2         ???                     
5C04: 1C         INC     E               
5C05: E1         POP     HL              
5C06: D8         RET     C               
5C07: 21 D0 21   LD      HL,$21D0        
5C0A: C0         RET     NZ              
5C0B: 31 E8 72   LD      SP,$72E8        
5C0E: 90         SUB     B               
5C0F: EC         ???                     
5C10: 90         SUB     B               
5C11: E4         ???                     
5C12: 90         SUB     B               
5C13: E4         ???                     
5C14: B0         OR      B               
5C15: C4 78 82   CALL    NZ,$8278        
5C18: C4 01 82   CALL    NZ,$8201        
5C1B: 01 00 01   LD      BC,$0100        
5C1E: 01 00 5F   LD      BC,$5F00        
5C21: 3F         CCF                     
5C22: B0         OR      B               
5C23: 4F         LD      C,A             
5C24: 38 87      JR      C,$5BAD         
5C26: 1D         DEC     E               
5C27: 82         ADD     A,D             
5C28: 1B         DEC     DE              
5C29: 84         ADD     A,H             
5C2A: 0B         DEC     BC              
5C2B: 84         ADD     A,H             
5C2C: 07         RLCA                    
5C2D: 4E         LD      C,(HL)          
5C2E: 09         ADD     HL,BC           
5C2F: 37         SCF                     
5C30: 09         ADD     HL,BC           
5C31: 27         DAA                     
5C32: 09         ADD     HL,BC           
5C33: 27         DAA                     
5C34: 0D         DEC     C               
5C35: 23         INC     HL              
5C36: 1E 41      LD      E,$41           
5C38: 23         INC     HL              
5C39: 80         ADD     A,B             
5C3A: 41         LD      B,C             
5C3B: 80         ADD     A,B             
5C3C: 00         NOP                     
5C3D: 80         ADD     A,B             
5C3E: 80         ADD     A,B             
5C3F: 00         NOP                     
5C40: 04         INC     B               
5C41: 09         ADD     HL,BC           
5C42: 7F         LD      A,A             
5C43: 0D         DEC     C               
5C44: 3B         DEC     SP              
5C45: 6F         LD      L,A             
5C46: 70         LD      (HL),B          
5C47: 3F         CCF                     
5C48: E7         RST     0X20            
5C49: 38 E9      JR      C,$5C34         
5C4B: B0         OR      B               
5C4C: 58         LD      E,B             
5C4D: E0 19      LDFF00  ($19),A         
5C4F: 60         LD      H,B             
5C50: 30 10      JR      NC,$5C62        
5C52: F6 30      OR      $30             
5C54: DC F6 0C   CALL    C,$0CF6         
5C57: FC         ???                     
5C58: E5         PUSH    HL              
5C59: 1C         INC     E               
5C5A: 17         RLA                     
5C5B: 0D         DEC     C               
5C5C: 9A         SBC     D               
5C5D: 07         RLCA                    
5C5E: 48         LD      C,B             
5C5F: 06 26      LD      B,$26           
5C61: 40         LD      B,B             
5C62: 22         LD      (HLI),A         
5C63: C0         RET     NZ              
5C64: 2F         CPL                     
5C65: 40         LD      B,B             
5C66: 31 40 18   LD      SP,$1840        
5C69: E0 0F      LDFF00  ($0F),A         
5C6B: 30 03      JR      NC,$5C70        
5C6D: 1C         INC     E               
5C6E: 00         NOP                     
5C6F: 33         INC     SP              
5C70: 3C         INC     A               
5C71: 02         LD      (BC),A          
5C72: 2C         INC     L               
5C73: 03         INC     BC              
5C74: C4 02 24   CALL    NZ,$2402        
5C77: 02         LD      (BC),A          
5C78: 9C         SBC     H               
5C79: 03         INC     BC              
5C7A: F8 06      LDHL    SP,$06          
5C7C: 00         NOP                     
5C7D: FC         ???                     
5C7E: 00         NOP                     
5C7F: 26 00      LD      H,$00           
5C81: FF         RST     0X38            
5C82: 00         NOP                     
5C83: 80         ADD     A,B             
5C84: 3F         CCF                     
5C85: 83         ADD     A,E             
5C86: 3F         CCF                     
5C87: 82         ADD     A,D             
5C88: 3F         CCF                     
5C89: BE         CP      (HL)            
5C8A: 3F         CCF                     
5C8B: A2         AND     D               
5C8C: 3F         CCF                     
5C8D: A2         AND     D               
5C8E: 3F         CCF                     
5C8F: A2         AND     D               
5C90: 3F         CCF                     
5C91: FF         RST     0X38            
5C92: 3F         CCF                     
5C93: 21 FF E1   LD      HL,$E1FF        
5C96: FF         RST     0X38            
5C97: 21 FF 21   LD      HL,$21FF        
5C9A: FF         RST     0X38            
5C9B: 21 E1 21   LD      HL,$21E1        
5C9E: FF         RST     0X38            
5C9F: 3F         CCF                     
5CA0: 3E A2      LD      A,$A2           
5CA2: 3F         CCF                     
5CA3: A3         AND     E               
5CA4: 23         INC     HL              
5CA5: A3         AND     E               
5CA6: 3F         CCF                     
5CA7: BF         CP      A               
5CA8: 3F         CCF                     
5CA9: BF         CP      A               
5CAA: 3F         CCF                     
5CAB: 80         ADD     A,B             
5CAC: 00         NOP                     
5CAD: 80         ADD     A,B             
5CAE: 00         NOP                     
5CAF: FF         RST     0X38            
5CB0: 3F         CCF                     
5CB1: 3F         CCF                     
5CB2: FF         RST     0X38            
5CB3: FF         RST     0X38            
5CB4: FF         RST     0X38            
5CB5: FF         RST     0X38            
5CB6: FF         RST     0X38            
5CB7: FF         RST     0X38            
5CB8: FF         RST     0X38            
5CB9: FF         RST     0X38            
5CBA: FE 01      CP      $01             
5CBC: 00         NOP                     
5CBD: 01 00 FF   LD      BC,$FF00        
5CC0: 03         INC     BC              
5CC1: 03         INC     BC              
5CC2: 04         INC     B               
5CC3: 04         INC     B               
5CC4: 0A         LD      A,(BC)          
5CC5: 08 15 10   LD      ($1015),SP      
5CC8: 2C         INC     L               
5CC9: 21 58 45   LD      HL,$4558        
5CCC: 52         LD      D,D             
5CCD: 49         LD      C,C             
5CCE: 52         LD      D,D             
5CCF: 49         LD      C,C             
5CD0: C0         RET     NZ              
5CD1: C0         RET     NZ              
5CD2: 20 20      JR      NZ,$5CF4        
5CD4: 50         LD      D,B             
5CD5: 10 A8      STOP    $A8             
5CD7: 08 14 A4   LD      ($A414),SP      
5CDA: 0A         LD      A,(BC)          
5CDB: B2         OR      D               
5CDC: 26 9A      LD      H,$9A           
5CDE: 42         LD      B,D             
5CDF: 9A         SBC     D               
5CE0: 4A         LD      C,D             
5CE1: 41         LD      B,C             
5CE2: 73         LD      (HL),E          
5CE3: 40         LD      B,B             
5CE4: E8 50      ADD     SP,$50          
5CE6: E2         LDFF00  (C),A           
5CE7: 59         LD      E,C             
5CE8: C1         POP     BC              
5CE9: 7B         LD      A,E             
5CEA: E5         PUSH    HL              
5CEB: 3B         DEC     SP              
5CEC: 74         LD      (HL),H          
5CED: 1B         DEC     DE              
5CEE: 3F         CCF                     
5CEF: 0F         RRCA                    
5CF0: 46         LD      B,(HL)          
5CF1: 92         SUB     D               
5CF2: CA 06 1B   JP      Z,$1B06         
5CF5: 0E 2B      LD      C,$2B           
5CF7: DE BF      SBC     $BF             
5CF9: DE BF      SBC     $BF             
5CFB: DC 3E D8   CALL    C,$D83E         
5CFE: FC         ???                     
5CFF: F0 00      LD      A,($00)         
5D01: 00         NOP                     
5D02: 00         NOP                     
5D03: 00         NOP                     
5D04: 00         NOP                     
5D05: 00         NOP                     
5D06: 00         NOP                     
5D07: 00         NOP                     
5D08: 00         NOP                     
5D09: 00         NOP                     
5D0A: 00         NOP                     
5D0B: 00         NOP                     
5D0C: 00         NOP                     
5D0D: 00         NOP                     
5D0E: 00         NOP                     
5D0F: 00         NOP                     
5D10: 00         NOP                     
5D11: 00         NOP                     
5D12: 00         NOP                     
5D13: 00         NOP                     
5D14: 00         NOP                     
5D15: 00         NOP                     
5D16: 00         NOP                     
5D17: 00         NOP                     
5D18: 00         NOP                     
5D19: 00         NOP                     
5D1A: 00         NOP                     
5D1B: 00         NOP                     
5D1C: 00         NOP                     
5D1D: 00         NOP                     
5D1E: 00         NOP                     
5D1F: 00         NOP                     
5D20: 00         NOP                     
5D21: 00         NOP                     
5D22: 00         NOP                     
5D23: 00         NOP                     
5D24: 00         NOP                     
5D25: 00         NOP                     
5D26: 00         NOP                     
5D27: 00         NOP                     
5D28: 00         NOP                     
5D29: 00         NOP                     
5D2A: 00         NOP                     
5D2B: 00         NOP                     
5D2C: 00         NOP                     
5D2D: 00         NOP                     
5D2E: 00         NOP                     
5D2F: 00         NOP                     
5D30: 00         NOP                     
5D31: 00         NOP                     
5D32: 00         NOP                     
5D33: 00         NOP                     
5D34: 00         NOP                     
5D35: 00         NOP                     
5D36: 00         NOP                     
5D37: 00         NOP                     
5D38: 00         NOP                     
5D39: 00         NOP                     
5D3A: 00         NOP                     
5D3B: 00         NOP                     
5D3C: 00         NOP                     
5D3D: 00         NOP                     
5D3E: 00         NOP                     
5D3F: 00         NOP                     
5D40: FF         RST     0X38            
5D41: EF         RST     0X28            
5D42: FF         RST     0X38            
5D43: EF         RST     0X28            
5D44: FF         RST     0X38            
5D45: FF         RST     0X38            
5D46: 83         ADD     A,E             
5D47: 80         ADD     A,B             
5D48: B0         OR      B               
5D49: 80         ADD     A,B             
5D4A: FF         RST     0X38            
5D4B: FF         RST     0X38            
5D4C: FF         RST     0X38            
5D4D: EF         RST     0X28            
5D4E: FF         RST     0X38            
5D4F: EF         RST     0X28            
5D50: FF         RST     0X38            
5D51: F7         RST     0X30            
5D52: FF         RST     0X38            
5D53: F7         RST     0X30            
5D54: FF         RST     0X38            
5D55: FF         RST     0X38            
5D56: 01 01 19   LD      BC,$1901        
5D59: 01 FF FF   LD      BC,$FFFF        
5D5C: FF         RST     0X38            
5D5D: F7         RST     0X30            
5D5E: FF         RST     0X38            
5D5F: F7         RST     0X30            
5D60: FF         RST     0X38            
5D61: FF         RST     0X38            
5D62: C2 C0 FF   JP      NZ,$FFC0        
5D65: FF         RST     0X38            
5D66: 90         SUB     B               
5D67: 80         ADD     A,B             
5D68: FF         RST     0X38            
5D69: FF         RST     0X38            
5D6A: 80         ADD     A,B             
5D6B: 80         ADD     A,B             
5D6C: FF         RST     0X38            
5D6D: FF         RST     0X38            
5D6E: C2 C0 FF   JP      NZ,$FFC0        
5D71: FF         RST     0X38            
5D72: 13         INC     DE              
5D73: 03         INC     BC              
5D74: FF         RST     0X38            
5D75: FF         RST     0X38            
5D76: 21 01 FF   LD      HL,$FF01        
5D79: FF         RST     0X38            
5D7A: 03         INC     BC              
5D7B: 03         INC     BC              
5D7C: FF         RST     0X38            
5D7D: FF         RST     0X38            
5D7E: 09         ADD     HL,BC           
5D7F: 01 FF FF   LD      BC,$FFFF        
5D82: 80         ADD     A,B             
5D83: 80         ADD     A,B             
5D84: 9B         SBC     E               
5D85: 83         ADD     A,E             
5D86: FE FE      CP      $FE             
5D88: F8 F8      LDHL    SP,$F8          
5D8A: FB         EI                      
5D8B: FB         EI                      
5D8C: FD         ???                     
5D8D: F9         LD      SP,HL           
5D8E: FE FC      CP      $FC             
5D90: FF         RST     0X38            
5D91: FF         RST     0X38            
5D92: 33         INC     SP              
5D93: 03         INC     BC              
5D94: C3 C3 7F   JP      $7FC3           
5D97: 7F         LD      A,A             
5D98: FF         RST     0X38            
5D99: FF         RST     0X38            
5D9A: DF         RST     0X18            
5D9B: DF         RST     0X18            
5D9C: BF         CP      A               
5D9D: 9F         SBC     A               
5D9E: 7F         LD      A,A             
5D9F: 3F         CCF                     
5DA0: FC         ???                     
5DA1: FC         ???                     
5DA2: FB         EI                      
5DA3: F9         LD      SP,HL           
5DA4: FB         EI                      
5DA5: FB         EI                      
5DA6: FF         RST     0X38            
5DA7: FF         RST     0X38            
5DA8: FE FE      CP      $FE             
5DAA: FE FE      CP      $FE             
5DAC: FF         RST     0X38            
5DAD: FF         RST     0X38            
5DAE: CC C0 3F   CALL    Z,$3FC0         
5DB1: 3F         CCF                     
5DB2: DF         RST     0X18            
5DB3: 9F         SBC     A               
5DB4: DF         RST     0X18            
5DB5: DF         RST     0X18            
5DB6: 3F         CCF                     
5DB7: 1F         RRA                     
5DB8: 7F         LD      A,A             
5DB9: 7F         LD      A,A             
5DBA: 7F         LD      A,A             
5DBB: 7F         LD      A,A             
5DBC: FF         RST     0X38            
5DBD: FF         RST     0X38            
5DBE: 19         ADD     HL,DE           
5DBF: 01 03 03   LD      BC,$0303        
5DC2: 04         INC     B               
5DC3: 04         INC     B               
5DC4: 0A         LD      A,(BC)          
5DC5: 08 15 10   LD      ($1015),SP      
5DC8: 2C         INC     L               
5DC9: 21 58 45   LD      HL,$4558        
5DCC: 52         LD      D,D             
5DCD: 49         LD      C,C             
5DCE: 52         LD      D,D             
5DCF: 49         LD      C,C             
5DD0: C0         RET     NZ              
5DD1: C0         RET     NZ              
5DD2: 20 20      JR      NZ,$5DF4        
5DD4: 50         LD      D,B             
5DD5: 10 A8      STOP    $A8             
5DD7: 08 14 A4   LD      ($A414),SP      
5DDA: 0A         LD      A,(BC)          
5DDB: B2         OR      D               
5DDC: 26 9A      LD      H,$9A           
5DDE: 42         LD      B,D             
5DDF: 9A         SBC     D               
5DE0: 4A         LD      C,D             
5DE1: 41         LD      B,C             
5DE2: 73         LD      (HL),E          
5DE3: 40         LD      B,B             
5DE4: E8 50      ADD     SP,$50          
5DE6: E2         LDFF00  (C),A           
5DE7: 59         LD      E,C             
5DE8: C1         POP     BC              
5DE9: 7B         LD      A,E             
5DEA: E5         PUSH    HL              
5DEB: 3B         DEC     SP              
5DEC: 74         LD      (HL),H          
5DED: 1B         DEC     DE              
5DEE: 3F         CCF                     
5DEF: 0F         RRCA                    
5DF0: 46         LD      B,(HL)          
5DF1: 92         SUB     D               
5DF2: CA 06 1B   JP      Z,$1B06         
5DF5: 0E 2B      LD      C,$2B           
5DF7: DE BF      SBC     $BF             
5DF9: DE BF      SBC     $BF             
5DFB: DC 3E D8   CALL    C,$D83E         
5DFE: FC         ???                     
5DFF: F0 80      LD      A,($80)         
5E01: 80         ADD     A,B             
5E02: C0         RET     NZ              
5E03: C0         RET     NZ              
5E04: A0         AND     B               
5E05: A0         AND     B               
5E06: 9F         SBC     A               
5E07: 97         SUB     A               
5E08: C8         RET     Z               
5E09: 88         ADC     A,B             
5E0A: E8 C0      ADD     SP,$C0          
5E0C: F3         DI                      
5E0D: A1         AND     C               
5E0E: D3         ???                     
5E0F: B3         OR      E               
5E10: 01 01 03   LD      BC,$0301        
5E13: 03         INC     BC              
5E14: 05         DEC     B               
5E15: 05         DEC     B               
5E16: F9         LD      SP,HL           
5E17: E9         JP      (HL)            
5E18: 13         INC     DE              
5E19: 11 17 03   LD      DE,$0317        
5E1C: CF         RST     0X08            
5E1D: 85         ADD     A,L             
5E1E: CB CD      SET     1,E             
5E20: D3         ???                     
5E21: B3         OR      E               
5E22: D3         ???                     
5E23: B3         OR      E               
5E24: D9         RETI                    
5E25: B1         OR      C               
5E26: E5         PUSH    HL              
5E27: A1         AND     C               
5E28: ED         ???                     
5E29: AD         XOR     L               
5E2A: F6 BC      OR      $BC             
5E2C: C3 BE FF   JP      $FFBE           
5E2F: FF         RST     0X38            
5E30: CB CD      SET     1,E             
5E32: CB CD      SET     1,E             
5E34: 9B         SBC     E               
5E35: 8D         ADC     A,L             
5E36: A7         AND     A               
5E37: 85         ADD     A,L             
5E38: B7         OR      A               
5E39: B5         OR      L               
5E3A: 6F         LD      L,A             
5E3B: 3D         DEC     A               
5E3C: C3 7D FF   JP      $FF7D           
5E3F: FF         RST     0X38            
5E40: 00         NOP                     
5E41: 00         NOP                     
5E42: 00         NOP                     
5E43: 00         NOP                     
5E44: 00         NOP                     
5E45: 00         NOP                     
5E46: 00         NOP                     
5E47: 00         NOP                     
5E48: 00         NOP                     
5E49: 1F         RRA                     
5E4A: 0F         RRCA                    
5E4B: 10 0F      STOP    $0F             
5E4D: 10 0F      STOP    $0F             
5E4F: 10 00      STOP    $00             
5E51: 00         NOP                     
5E52: 00         NOP                     
5E53: 00         NOP                     
5E54: 00         NOP                     
5E55: 00         NOP                     
5E56: 00         NOP                     
5E57: 00         NOP                     
5E58: 00         NOP                     
5E59: FC         ???                     
5E5A: F8 04      LDHL    SP,$04          
5E5C: F8 04      LDHL    SP,$04          
5E5E: F8 04      LDHL    SP,$04          
5E60: 0F         RRCA                    
5E61: 10 0F      STOP    $0F             
5E63: 10 0F      STOP    $0F             
5E65: 10 0F      STOP    $0F             
5E67: 10 0F      STOP    $0F             
5E69: 10 00      STOP    $00             
5E6B: 1F         RRA                     
5E6C: 00         NOP                     
5E6D: 00         NOP                     
5E6E: 00         NOP                     
5E6F: 00         NOP                     
5E70: F8 04      LDHL    SP,$04          
5E72: F8 04      LDHL    SP,$04          
5E74: F8 04      LDHL    SP,$04          
5E76: F8 04      LDHL    SP,$04          
5E78: F8 04      LDHL    SP,$04          
5E7A: 00         NOP                     
5E7B: FC         ???                     
5E7C: 00         NOP                     
5E7D: 00         NOP                     
5E7E: 00         NOP                     
5E7F: 00         NOP                     
5E80: 1F         RRA                     
5E81: 0F         RRCA                    
5E82: 1F         RRA                     
5E83: 10 1F      STOP    $1F             
5E85: 10 1F      STOP    $1F             
5E87: 10 1F      STOP    $1F             
5E89: 10 1F      STOP    $1F             
5E8B: 10 1F      STOP    $1F             
5E8D: 10 1F      STOP    $1F             
5E8F: 10 FC      STOP    $FC             
5E91: F8 FC      LDHL    SP,$FC          
5E93: 04         INC     B               
5E94: FC         ???                     
5E95: 04         INC     B               
5E96: FC         ???                     
5E97: 04         INC     B               
5E98: FC         ???                     
5E99: 04         INC     B               
5E9A: FC         ???                     
5E9B: 04         INC     B               
5E9C: FC         ???                     
5E9D: 04         INC     B               
5E9E: FC         ???                     
5E9F: 04         INC     B               
5EA0: 10 10      STOP    $10             
5EA2: 10 1F      STOP    $1F             
5EA4: 10 1F      STOP    $1F             
5EA6: 10 1F      STOP    $1F             
5EA8: 10 1F      STOP    $1F             
5EAA: 1F         RRA                     
5EAB: 1F         RRA                     
5EAC: 00         NOP                     
5EAD: 00         NOP                     
5EAE: 00         NOP                     
5EAF: 00         NOP                     
5EB0: 04         INC     B               
5EB1: 04         INC     B               
5EB2: 04         INC     B               
5EB3: FC         ???                     
5EB4: 04         INC     B               
5EB5: FC         ???                     
5EB6: 04         INC     B               
5EB7: FC         ???                     
5EB8: 04         INC     B               
5EB9: FC         ???                     
5EBA: FC         ???                     
5EBB: FC         ???                     
5EBC: 00         NOP                     
5EBD: 00         NOP                     
5EBE: 00         NOP                     
5EBF: 00         NOP                     
5EC0: 00         NOP                     
5EC1: 00         NOP                     
5EC2: FF         RST     0X38            
5EC3: 00         NOP                     
5EC4: DF         RST     0X18            
5EC5: 3F         CCF                     
5EC6: BF         CP      A               
5EC7: 7F         LD      A,A             
5EC8: FF         RST     0X38            
5EC9: 7F         LD      A,A             
5ECA: FF         RST     0X38            
5ECB: 7F         LD      A,A             
5ECC: FF         RST     0X38            
5ECD: 7C         LD      A,H             
5ECE: FF         RST     0X38            
5ECF: 78         LD      A,B             
5ED0: 00         NOP                     
5ED1: 00         NOP                     
5ED2: FF         RST     0X38            
5ED3: 00         NOP                     
5ED4: FB         EI                      
5ED5: FC         ???                     
5ED6: FD         ???                     
5ED7: 86         ADD     A,(HL)          
5ED8: DF         RST     0X18            
5ED9: 82         ADD     A,D             
5EDA: AF         XOR     A               
5EDB: C2 97 E2   JP      NZ,$E297        
5EDE: CB 72      SET     1,E             
5EE0: FB         EI                      
5EE1: 70         LD      (HL),B          
5EE2: F4         ???                     
5EE3: 78         LD      A,B             
5EE4: F1         POP     AF              
5EE5: 7E         LD      A,(HL)          
5EE6: FC         ???                     
5EE7: 7F         LD      A,A             
5EE8: EB         ???                     
5EE9: 47         LD      B,A             
5EEA: C1         POP     BC              
5EEB: 40         LD      B,B             
5EEC: C0         RET     NZ              
5EED: 40         LD      B,B             
5EEE: FF         RST     0X38            
5EEF: FF         RST     0X38            
5EF0: E7         RST     0X20            
5EF1: 3A         LD      A,(HLD)         
5EF2: F3         DI                      
5EF3: 1E 3B      LD      E,$3B           
5EF5: 0E 4F      LD      C,$4F           
5EF7: 86         ADD     A,(HL)          
5EF8: 97         SUB     A               
5EF9: E2         LDFF00  (C),A           
5EFA: 73         LD      (HL),E          
5EFB: FE 2F      CP      $2F             
5EFD: 1E FF      LD      E,$FF           
5EFF: FE 0F      CP      $0F             
5F01: 0F         RRCA                    
5F02: 12         LD      (DE),A          
5F03: 10 22      STOP    $22             
5F05: 20 43      JR      NZ,$5F4A        
5F07: 47         LD      B,A             
5F08: 77         LD      (HL),A          
5F09: 4F         LD      C,A             
5F0A: 4F         LD      C,A             
5F0B: 4F         LD      C,A             
5F0C: 4F         LD      C,A             
5F0D: 4F         LD      C,A             
5F0E: 7F         LD      A,A             
5F0F: 4F         LD      C,A             
5F10: F0 F0      LD      A,($F0)         
5F12: 48         LD      C,B             
5F13: 08 44 04   LD      ($0444),SP      
5F16: C2 E2 EE   JP      NZ,$EEE2        
5F19: F2         ???                     
5F1A: F2         ???                     
5F1B: F2         ???                     
5F1C: F2         ???                     
5F1D: F2         ???                     
5F1E: FE F2      CP      $F2             
5F20: 47         LD      B,A             
5F21: 47         LD      B,A             
5F22: 62         LD      H,D             
5F23: 40         LD      B,B             
5F24: 72         LD      (HL),D          
5F25: 60         LD      H,B             
5F26: 7F         LD      A,A             
5F27: 52         LD      D,D             
5F28: 5F         LD      E,A             
5F29: 6F         LD      L,A             
5F2A: 40         LD      B,B             
5F2B: 70         LD      (HL),B          
5F2C: 2F         CPL                     
5F2D: 30 1F      JR      NC,$5F4E        
5F2F: 1F         RRA                     
5F30: E2         LDFF00  (C),A           
5F31: E2         LDFF00  (C),A           
5F32: 46         LD      B,(HL)          
5F33: 02         LD      (BC),A          
5F34: 4E         LD      C,(HL)          
5F35: 06 FE      LD      B,$FE           
5F37: 4A         LD      C,D             
5F38: FA F6 02   LD      A,($02F6)       
5F3B: 0E F4      LD      C,$F4           
5F3D: 0C         INC     C               
5F3E: F8 F8      LDHL    SP,$F8          
5F40: 06 06      LD      B,$06           
5F42: 0A         LD      A,(BC)          
5F43: 0A         LD      A,(BC)          
5F44: 1A         LD      A,(DE)          
5F45: 12         LD      (DE),A          
5F46: 1B         DEC     DE              
5F47: 13         INC     DE              
5F48: 3C         INC     A               
5F49: 3C         INC     A               
5F4A: 60         LD      H,B             
5F4B: 40         LD      B,B             
5F4C: 5C         LD      E,H             
5F4D: 5C         LD      E,H             
5F4E: DE 9E      SBC     $9E             
5F50: 60         LD      H,B             
5F51: 60         LD      H,B             
5F52: 50         LD      D,B             
5F53: 50         LD      D,B             
5F54: 58         LD      E,B             
5F55: 48         LD      C,B             
5F56: D8         RET     C               
5F57: C8         RET     Z               
5F58: 3C         INC     A               
5F59: 3C         INC     A               
5F5A: 06 02      LD      B,$02           
5F5C: 3A         LD      A,(HLD)         
5F5D: 3A         LD      A,(HLD)         
5F5E: 7B         LD      A,E             
5F5F: 79         LD      A,C             
5F60: 9E         SBC     (HL)            
5F61: 9E         SBC     (HL)            
5F62: 8E         ADC     A,(HL)          
5F63: 8E         ADC     A,(HL)          
5F64: C0         RET     NZ              
5F65: 80         ADD     A,B             
5F66: FA 92 72   LD      A,($7292)       
5F69: 62         LD      H,D             
5F6A: 30 20      JR      NC,$5F8C        
5F6C: 3C         INC     A               
5F6D: 2C         INC     L               
5F6E: 3F         CCF                     
5F6F: 3F         CCF                     
5F70: 79         LD      A,C             
5F71: 79         LD      A,C             
5F72: 71         LD      (HL),C          
5F73: 71         LD      (HL),C          
5F74: 03         INC     BC              
5F75: 01 5F 49   LD      BC,$495F        
5F78: 4E         LD      C,(HL)          
5F79: 46         LD      B,(HL)          
5F7A: 0C         INC     C               
5F7B: 04         INC     B               
5F7C: 3C         INC     A               
5F7D: 34         INC     (HL)            
5F7E: FC         ???                     
5F7F: FC         ???                     
5F80: 00         NOP                     
5F81: FF         RST     0X38            
5F82: 00         NOP                     
5F83: 80         ADD     A,B             
5F84: 3F         CCF                     
5F85: 83         ADD     A,E             
5F86: 3F         CCF                     
5F87: 82         ADD     A,D             
5F88: 3F         CCF                     
5F89: BE         CP      (HL)            
5F8A: 3F         CCF                     
5F8B: A2         AND     D               
5F8C: 3F         CCF                     
5F8D: A2         AND     D               
5F8E: 3F         CCF                     
5F8F: A2         AND     D               
5F90: 3F         CCF                     
5F91: FF         RST     0X38            
5F92: 3F         CCF                     
5F93: 21 FF E1   LD      HL,$E1FF        
5F96: FF         RST     0X38            
5F97: 21 FF 21   LD      HL,$21FF        
5F9A: FF         RST     0X38            
5F9B: 21 E1 21   LD      HL,$21E1        
5F9E: FF         RST     0X38            
5F9F: 3F         CCF                     
5FA0: 3E A2      LD      A,$A2           
5FA2: 3F         CCF                     
5FA3: A3         AND     E               
5FA4: 23         INC     HL              
5FA5: A3         AND     E               
5FA6: 3F         CCF                     
5FA7: BF         CP      A               
5FA8: 3F         CCF                     
5FA9: BF         CP      A               
5FAA: 3F         CCF                     
5FAB: 80         ADD     A,B             
5FAC: 00         NOP                     
5FAD: 80         ADD     A,B             
5FAE: 00         NOP                     
5FAF: FF         RST     0X38            
5FB0: 3F         CCF                     
5FB1: 3F         CCF                     
5FB2: FF         RST     0X38            
5FB3: FF         RST     0X38            
5FB4: FF         RST     0X38            
5FB5: FF         RST     0X38            
5FB6: FF         RST     0X38            
5FB7: FF         RST     0X38            
5FB8: FF         RST     0X38            
5FB9: FF         RST     0X38            
5FBA: FE 01      CP      $01             
5FBC: 00         NOP                     
5FBD: 01 00 FF   LD      BC,$FF00        
5FC0: 57         LD      D,A             
5FC1: 57         LD      D,A             
5FC2: B2         OR      D               
5FC3: 92         SUB     D               
5FC4: F8 B0      LDHL    SP,$B0          
5FC6: CE CC      ADC     $CC             
5FC8: 9F         SBC     A               
5FC9: 8F         ADC     A,A             
5FCA: AD         XOR     L               
5FCB: 9D         SBC     L               
5FCC: F9         LD      SP,HL           
5FCD: 99         SBC     C               
5FCE: D9         RETI                    
5FCF: B9         CP      C               
5FD0: EA EA 4D   LD      ($4DEA),A       
5FD3: 49         LD      C,C             
5FD4: 1F         RRA                     
5FD5: 0D         DEC     C               
5FD6: 73         LD      (HL),E          
5FD7: 33         INC     SP              
5FD8: F9         LD      SP,HL           
5FD9: F1         POP     AF              
5FDA: B5         OR      L               
5FDB: B9         CP      C               
5FDC: 9F         SBC     A               
5FDD: 99         SBC     C               
5FDE: 9B         SBC     E               
5FDF: 9D         SBC     L               
5FE0: F9         LD      SP,HL           
5FE1: F9         LD      SP,HL           
5FE2: 9F         SBC     A               
5FE3: F9         LD      SP,HL           
5FE4: A9         XOR     C               
5FE5: DF         RST     0X18            
5FE6: B7         OR      A               
5FE7: CF         RST     0X08            
5FE8: DF         RST     0X18            
5FE9: 60         LD      H,B             
5FEA: 4F         LD      C,A             
5FEB: 70         LD      (HL),B          
5FEC: 30 3F      JR      NC,$602D        
5FEE: 1F         RRA                     
5FEF: 0F         RRCA                    
5FF0: 9F         SBC     A               
5FF1: 9F         SBC     A               
5FF2: F9         LD      SP,HL           
5FF3: 9F         SBC     A               
5FF4: 95         SUB     L               
5FF5: FB         EI                      
5FF6: ED         ???                     
5FF7: F3         DI                      
5FF8: FB         EI                      
5FF9: 06 F2      LD      B,$F2           
5FFB: 0E 0C      LD      C,$0C           
5FFD: FC         ???                     
5FFE: F8 F0      LDHL    SP,$F0          
6000: 7C         LD      A,H             
6001: 00         NOP                     
6002: 86         ADD     A,(HL)          
6003: 00         NOP                     
6004: 82         ADD     A,D             
6005: 00         NOP                     
6006: 82         ADD     A,D             
6007: 00         NOP                     
6008: 86         ADD     A,(HL)          
6009: 00         NOP                     
600A: CC 00 79   CALL    Z,$7900         
600D: 00         NOP                     
600E: 03         INC     BC              
600F: 00         NOP                     
6010: 03         INC     BC              
6011: 00         NOP                     
6012: 79         LD      A,C             
6013: 00         NOP                     
6014: CC 00 86   CALL    Z,$8600         
6017: 00         NOP                     
6018: 82         ADD     A,D             
6019: 00         NOP                     
601A: 82         ADD     A,D             
601B: 00         NOP                     
601C: 86         ADD     A,(HL)          
601D: 00         NOP                     
601E: 7C         LD      A,H             
601F: 00         NOP                     
6020: 3E 00      LD      A,$00           
6022: 61         LD      H,C             
6023: 00         NOP                     
6024: 41         LD      B,C             
6025: 00         NOP                     
6026: 41         LD      B,C             
6027: 00         NOP                     
6028: 61         LD      H,C             
6029: 00         NOP                     
602A: 33         INC     SP              
602B: 00         NOP                     
602C: 9E         SBC     (HL)            
602D: 00         NOP                     
602E: C0         RET     NZ              
602F: 00         NOP                     
6030: C0         RET     NZ              
6031: 00         NOP                     
6032: 9E         SBC     (HL)            
6033: 00         NOP                     
6034: 33         INC     SP              
6035: 00         NOP                     
6036: 61         LD      H,C             
6037: 00         NOP                     
6038: 41         LD      B,C             
6039: 00         NOP                     
603A: 41         LD      B,C             
603B: 00         NOP                     
603C: 61         LD      H,C             
603D: 00         NOP                     
603E: 3E 00      LD      A,$00           
6040: 00         NOP                     
6041: 00         NOP                     
6042: 00         NOP                     
6043: 00         NOP                     
6044: 00         NOP                     
6045: 00         NOP                     
6046: 07         RLCA                    
6047: 07         RLCA                    
6048: 0C         INC     C               
6049: 08 1B 10   LD      ($101B),SP      
604C: 17         RLA                     
604D: 10 17      STOP    $17             
604F: 10 00      STOP    $00             
6051: 00         NOP                     
6052: 00         NOP                     
6053: 00         NOP                     
6054: 00         NOP                     
6055: 00         NOP                     
6056: E0 E0      LDFF00  ($E0),A         
6058: 30 10      JR      NC,$606A        
605A: D8         RET     C               
605B: 08 E8 08   LD      ($08E8),SP      
605E: E8 08      ADD     SP,$08          
6060: 17         RLA                     
6061: 10 1B      STOP    $1B             
6063: 10 14      STOP    $14             
6065: 18 08      JR      $606F           
6067: 0F         RRCA                    
6068: 07         RLCA                    
6069: 07         RLCA                    
606A: 00         NOP                     
606B: 00         NOP                     
606C: 00         NOP                     
606D: 00         NOP                     
606E: 00         NOP                     
606F: 00         NOP                     
6070: E8 08      ADD     SP,$08          
6072: D8         RET     C               
6073: 08 28 18   LD      ($1828),SP      
6076: 10 F0      STOP    $F0             
6078: E0 E0      LDFF00  ($E0),A         
607A: 00         NOP                     
607B: 00         NOP                     
607C: 00         NOP                     
607D: 00         NOP                     
607E: 00         NOP                     
607F: 00         NOP                     
6080: F0 0F      LD      A,($0F)         
6082: 96         SUB     (HL)            
6083: 6F         LD      L,A             
6084: 96         SUB     (HL)            
6085: 6F         LD      L,A             
6086: E0 1F      LDFF00  ($1F),A         
6088: 0E F1      LD      C,$F1           
608A: 6E         LD      L,(HL)          
608B: F1         POP     AF              
608C: 6E         LD      L,(HL)          
608D: F1         POP     AF              
608E: 00         NOP                     
608F: FF         RST     0X38            
6090: F0 0F      LD      A,($0F)         
6092: F6 0F      OR      $0F             
6094: F6 0F      OR      $0F             
6096: 10 EF      STOP    $EF             
6098: 1F         RRA                     
6099: E0 67      LDFF00  ($67),A         
609B: 98         SBC     B               
609C: 67         LD      H,A             
609D: 98         SBC     B               
609E: 07         RLCA                    
609F: F8 E0      LDHL    SP,$E0          
60A1: 1F         RRA                     
60A2: E6 19      AND     $19             
60A4: E6 19      AND     $19             
60A6: F8 07      LDHL    SP,$07          
60A8: 08 F7 6F   LD      ($6FF7),SP      
60AB: F0 6F      LD      A,($6F)         
60AD: F0 0F      LD      A,($0F)         
60AF: F0 00      LD      A,($00)         
60B1: FF         RST     0X38            
60B2: 76         HALT                    
60B3: 8F         ADC     A,A             
60B4: 76         HALT                    
60B5: 8F         ADC     A,A             
60B6: 70         LD      (HL),B          
60B7: 8F         ADC     A,A             
60B8: 07         RLCA                    
60B9: F8 69      LDHL    SP,$69          
60BB: F6 69      OR      $69             
60BD: F6 0F      OR      $0F             
60BF: F0 60      LD      A,($60)         
60C1: 1C         INC     E               
60C2: C8         RET     Z               
60C3: 07         RLCA                    
60C4: 85         ADD     A,L             
60C5: 02         LD      (BC),A          
60C6: 85         ADD     A,L             
60C7: 02         LD      (BC),A          
60C8: C9         RET                     
60C9: 06 30      LD      B,$30           
60CB: CF         RST     0X08            
60CC: 00         NOP                     
60CD: 7F         LD      A,A             
60CE: 18 26      JR      $60F6           
60D0: 03         INC     BC              
60D1: 10 09      STOP    $09             
60D3: F0 84      LD      A,($84)         
60D5: 40         LD      B,B             
60D6: 02         LD      (BC),A          
60D7: 80         ADD     A,B             
60D8: 00         NOP                     
60D9: 82         ADD     A,D             
60DA: 44         LD      B,H             
60DB: 82         ADD     A,D             
60DC: 3C         INC     A               
60DD: C2 80 7C   JP      NZ,$7C80        
60E0: 01 3E 1C   LD      BC,$1C3E        
60E3: 63         LD      H,E             
60E4: 22         LD      (HLI),A         
60E5: 41         LD      B,C             
60E6: 40         LD      B,B             
60E7: 01 42 01   LD      BC,$0142        
60EA: 3C         INC     A               
60EB: 03         INC     BC              
60EC: 80         ADD     A,B             
60ED: 1E C0      LD      E,$C0           
60EF: 00         NOP                     
60F0: 00         NOP                     
60F1: F8 60      LDHL    SP,$60          
60F3: 9E         SBC     (HL)            
60F4: D2 21 A1   JP      NC,$A121        
60F7: 40         LD      B,B             
60F8: 81         ADD     A,C             
60F9: 40         LD      B,B             
60FA: 21 C0 53   LD      HL,$53C0        
60FD: 20 26      JR      NZ,$6125        
60FF: 18 05      JR      $6106           
6101: 00         NOP                     
6102: 45         LD      B,L             
6103: 00         NOP                     
6104: 09         ADD     HL,BC           
6105: 00         NOP                     
6106: 13         INC     DE              
6107: 00         NOP                     
6108: 26 00      LD      H,$00           
610A: CD 00 1B   CALL    $1B00           
610D: 00         NOP                     
610E: F7         RST     0X30            
610F: 00         NOP                     
6110: A0         AND     B               
6111: 00         NOP                     
6112: A0         AND     B               
6113: 00         NOP                     
6114: A4         AND     H               
6115: 00         NOP                     
6116: D0         RET     NC              
6117: 00         NOP                     
6118: 68         LD      L,B             
6119: 00         NOP                     
611A: B7         OR      A               
611B: 00         NOP                     
611C: D8         RET     C               
611D: 00         NOP                     
611E: EF         RST     0X28            
611F: 00         NOP                     
6120: F7         RST     0X30            
6121: 00         NOP                     
6122: 1B         DEC     DE              
6123: 00         NOP                     
6124: ED         ???                     
6125: 00         NOP                     
6126: 16 00      LD      D,$00           
6128: 0B         DEC     BC              
6129: 00         NOP                     
612A: 05         DEC     B               
612B: 00         NOP                     
612C: 45         LD      B,L             
612D: 00         NOP                     
612E: 05         DEC     B               
612F: 00         NOP                     
6130: EF         RST     0X28            
6131: 00         NOP                     
6132: D8         RET     C               
6133: 00         NOP                     
6134: B7         OR      A               
6135: 00         NOP                     
6136: 68         LD      L,B             
6137: 00         NOP                     
6138: D0         RET     NC              
6139: 00         NOP                     
613A: A4         AND     H               
613B: 00         NOP                     
613C: A0         AND     B               
613D: 00         NOP                     
613E: A0         AND     B               
613F: 00         NOP                     
6140: 00         NOP                     
6141: 00         NOP                     
6142: 00         NOP                     
6143: 00         NOP                     
6144: 00         NOP                     
6145: 00         NOP                     
6146: 07         RLCA                    
6147: 07         RLCA                    
6148: 0C         INC     C               
6149: 08 1B 10   LD      ($101B),SP      
614C: 17         RLA                     
614D: 10 17      STOP    $17             
614F: 10 00      STOP    $00             
6151: 00         NOP                     
6152: 00         NOP                     
6153: 00         NOP                     
6154: 00         NOP                     
6155: 00         NOP                     
6156: E0 E0      LDFF00  ($E0),A         
6158: 30 10      JR      NC,$616A        
615A: D8         RET     C               
615B: 08 E8 08   LD      ($08E8),SP      
615E: E8 08      ADD     SP,$08          
6160: 17         RLA                     
6161: 10 1B      STOP    $1B             
6163: 10 14      STOP    $14             
6165: 18 08      JR      $616F           
6167: 0F         RRCA                    
6168: 07         RLCA                    
6169: 07         RLCA                    
616A: 00         NOP                     
616B: 00         NOP                     
616C: 00         NOP                     
616D: 00         NOP                     
616E: 00         NOP                     
616F: 00         NOP                     
6170: E8 08      ADD     SP,$08          
6172: D8         RET     C               
6173: 08 28 18   LD      ($1828),SP      
6176: 10 F0      STOP    $F0             
6178: E0 E0      LDFF00  ($E0),A         
617A: 00         NOP                     
617B: 00         NOP                     
617C: 00         NOP                     
617D: 00         NOP                     
617E: 00         NOP                     
617F: 00         NOP                     
6180: 00         NOP                     
6181: 00         NOP                     
6182: 00         NOP                     
6183: 3F         CCF                     
6184: 1F         RRA                     
6185: 60         LD      H,B             
6186: 3E 41      LD      A,$41           
6188: 36 49      LD      (HL),$49        
618A: 23         INC     HL              
618B: 5C         LD      E,H             
618C: 29         ADD     HL,HL           
618D: 56         LD      D,(HL)          
618E: 3C         INC     A               
618F: 43         LD      B,E             
6190: 00         NOP                     
6191: 00         NOP                     
6192: 00         NOP                     
6193: FC         ???                     
6194: F8 06      LDHL    SP,$06          
6196: 7C         LD      A,H             
6197: 82         ADD     A,D             
6198: 6C         LD      L,H             
6199: 92         SUB     D               
619A: C4 3A 94   CALL    NZ,$943A        
619D: 6A         LD      L,D             
619E: 3C         INC     A               
619F: C2 3E 41   JP      NZ,$413E        
61A2: 2E 51      LD      L,$51           
61A4: 26 59      LD      H,$59           
61A6: 37         SCF                     
61A7: 48         LD      C,B             
61A8: 3E 41      LD      A,$41           
61AA: 1F         RRA                     
61AB: 60         LD      H,B             
61AC: 00         NOP                     
61AD: 3F         CCF                     
61AE: 00         NOP                     
61AF: 00         NOP                     
61B0: 7C         LD      A,H             
61B1: 82         ADD     A,D             
61B2: 74         LD      (HL),H          
61B3: 8A         ADC     A,D             
61B4: 64         LD      H,H             
61B5: 9A         SBC     D               
61B6: EC         ???                     
61B7: 12         LD      (DE),A          
61B8: 7C         LD      A,H             
61B9: 82         ADD     A,D             
61BA: F8 06      LDHL    SP,$06          
61BC: 00         NOP                     
61BD: FC         ???                     
61BE: 00         NOP                     
61BF: 00         NOP                     
61C0: 05         DEC     B               
61C1: 02         LD      (BC),A          
61C2: 44         LD      B,H             
61C3: 01 08 01   LD      BC,$0108        
61C6: 12         LD      (DE),A          
61C7: 81         ADD     A,C             
61C8: 26 81      LD      H,$81           
61CA: 8D         ADC     A,L             
61CB: 42         LD      B,D             
61CC: 03         INC     BC              
61CD: 3C         INC     A               
61CE: D3         ???                     
61CF: 24         INC     H               
61D0: A0         AND     B               
61D1: 00         NOP                     
61D2: A2         AND     D               
61D3: 00         NOP                     
61D4: A0         AND     B               
61D5: 0E D0      LD      C,$D0           
61D7: 08 00 F8   LD      ($F800),SP      
61DA: 93         SUB     E               
61DB: 24         INC     H               
61DC: D8         RET     C               
61DD: 22         LD      (HLI),A         
61DE: AE         XOR     (HL)            
61DF: 41         LD      B,C             
61E0: D3         ???                     
61E1: 24         INC     H               
61E2: 1B         DEC     DE              
61E3: 27         DAA                     
61E4: C5         PUSH    BC              
61E5: 39         ADD     HL,SP           
61E6: 06 10      LD      B,$10           
61E8: 0B         DEC     BC              
61E9: 30 00      JR      NC,$61EB        
61EB: 2F         CPL                     
61EC: 45         LD      B,L             
61ED: 20 05      JR      NZ,$61F4        
61EF: 40         LD      B,B             
61F0: EE 41      XOR     $41             
61F2: E0 F9      LDFF00  ($F9),A         
61F4: B1         OR      C               
61F5: 86         ADD     A,(HL)          
61F6: E8 84      ADD     SP,$84          
61F8: 50         LD      D,B             
61F9: 84         ADD     A,H             
61FA: 00         NOP                     
61FB: FC         ???                     
61FC: A0         AND     B               
61FD: 42         LD      B,D             
61FE: A1         AND     C               
61FF: 40         LD      B,B             
6200: 84         ADD     A,H             
6201: 00         NOP                     
6202: 27         DAA                     
6203: 00         NOP                     
6204: 68         LD      L,B             
6205: 00         NOP                     
6206: 09         ADD     HL,BC           
6207: 00         NOP                     
6208: 9A         SBC     D               
6209: 00         NOP                     
620A: F2         ???                     
620B: 00         NOP                     
620C: 20 00      JR      NZ,$620E        
620E: 29         ADD     HL,HL           
620F: 00         NOP                     
6210: 14         INC     D               
6211: 00         NOP                     
6212: F6 00      OR      $00             
6214: 12         LD      (DE),A          
6215: 00         NOP                     
6216: D8         RET     C               
6217: 00         NOP                     
6218: 0F         RRCA                    
6219: 00         NOP                     
621A: 66         LD      H,(HL)          
621B: 00         NOP                     
621C: 04         INC     B               
621D: 00         NOP                     
621E: 95         SUB     L               
621F: 00         NOP                     
6220: 2C         INC     L               
6221: 00         NOP                     
6222: 2C         INC     L               
6223: 00         NOP                     
6224: 60         LD      H,B             
6225: 00         NOP                     
6226: F9         LD      SP,HL           
6227: 00         NOP                     
6228: 0C         INC     C               
6229: 00         NOP                     
622A: 67         LD      H,A             
622B: 00         NOP                     
622C: 24         INC     H               
622D: 00         NOP                     
622E: 94         SUB     H               
622F: 00         NOP                     
6230: B4         OR      H               
6231: 00         NOP                     
6232: 24         INC     H               
6233: 00         NOP                     
6234: 0F         RRCA                    
6235: 00         NOP                     
6236: 99         SBC     C               
6237: 00         NOP                     
6238: 30 00      JR      NC,$623A        
623A: E6 00      AND     $00             
623C: 24         INC     H               
623D: 00         NOP                     
623E: 31 00 00   LD      SP,$0000        
6241: 00         NOP                     
6242: 00         NOP                     
6243: 00         NOP                     
6244: 00         NOP                     
6245: 00         NOP                     
6246: 07         RLCA                    
6247: 07         RLCA                    
6248: 0C         INC     C               
6249: 08 1B 10   LD      ($101B),SP      
624C: 17         RLA                     
624D: 10 17      STOP    $17             
624F: 10 00      STOP    $00             
6251: 00         NOP                     
6252: 00         NOP                     
6253: 00         NOP                     
6254: 00         NOP                     
6255: 00         NOP                     
6256: E0 E0      LDFF00  ($E0),A         
6258: 30 10      JR      NC,$626A        
625A: D8         RET     C               
625B: 08 E8 08   LD      ($08E8),SP      
625E: E8 08      ADD     SP,$08          
6260: 17         RLA                     
6261: 10 1B      STOP    $1B             
6263: 10 14      STOP    $14             
6265: 18 08      JR      $626F           
6267: 0F         RRCA                    
6268: 07         RLCA                    
6269: 07         RLCA                    
626A: 00         NOP                     
626B: 00         NOP                     
626C: 00         NOP                     
626D: 00         NOP                     
626E: 00         NOP                     
626F: 00         NOP                     
6270: E8 08      ADD     SP,$08          
6272: D8         RET     C               
6273: 08 28 18   LD      ($1828),SP      
6276: 10 F0      STOP    $F0             
6278: E0 E0      LDFF00  ($E0),A         
627A: 00         NOP                     
627B: 00         NOP                     
627C: 00         NOP                     
627D: 00         NOP                     
627E: 00         NOP                     
627F: 00         NOP                     
6280: 09         ADD     HL,BC           
6281: 00         NOP                     
6282: 13         INC     DE              
6283: 00         NOP                     
6284: 26 00      LD      H,$00           
6286: 4D         LD      C,L             
6287: 00         NOP                     
6288: 9B         SBC     E               
6289: 00         NOP                     
628A: 36 00      LD      (HL),$00        
628C: 6F         LD      L,A             
628D: 00         NOP                     
628E: DF         RST     0X18            
628F: 00         NOP                     
6290: 90         SUB     B               
6291: 00         NOP                     
6292: C8         RET     Z               
6293: 00         NOP                     
6294: 64         LD      H,H             
6295: 00         NOP                     
6296: B2         OR      D               
6297: 00         NOP                     
6298: D9         RETI                    
6299: 00         NOP                     
629A: EC         ???                     
629B: 00         NOP                     
629C: F6 00      OR      $00             
629E: FB         EI                      
629F: 00         NOP                     
62A0: DB         ???                     
62A1: 00         NOP                     
62A2: 6F         LD      L,A             
62A3: 00         NOP                     
62A4: 37         SCF                     
62A5: 00         NOP                     
62A6: 9B         SBC     E               
62A7: 00         NOP                     
62A8: 4D         LD      C,L             
62A9: 00         NOP                     
62AA: 26 00      LD      H,$00           
62AC: 13         INC     DE              
62AD: 00         NOP                     
62AE: 09         ADD     HL,BC           
62AF: 00         NOP                     
62B0: FB         EI                      
62B1: 00         NOP                     
62B2: B6         OR      (HL)            
62B3: 00         NOP                     
62B4: EC         ???                     
62B5: 00         NOP                     
62B6: D9         RETI                    
62B7: 00         NOP                     
62B8: B2         OR      D               
62B9: 00         NOP                     
62BA: 64         LD      H,H             
62BB: 00         NOP                     
62BC: C8         RET     Z               
62BD: 00         NOP                     
62BE: 90         SUB     B               
62BF: 00         NOP                     
62C0: 82         ADD     A,D             
62C1: 04         INC     B               
62C2: 28 07      JR      Z,$62CB         
62C4: 60         LD      H,B             
62C5: 0F         RRCA                    
62C6: 12         LD      (DE),A          
62C7: 0C         INC     C               
62C8: 64         LD      H,H             
62C9: 98         SBC     B               
62CA: 80         ADD     A,B             
62CB: 78         LD      A,B             
62CC: 40         LD      B,B             
62CD: 3F         CCF                     
62CE: 00         NOP                     
62CF: 32         LD      (HLD),A         
62D0: 24         INC     H               
62D1: 10 06      STOP    $06             
62D3: F0 0A      LD      A,($0A)         
62D5: F0 44      LD      A,($44)         
62D7: 38 40      JR      C,$6319         
62D9: 3F         CCF                     
62DA: 92         SUB     D               
62DB: 6C         LD      L,H             
62DC: 28 C4      JR      Z,$62A2         
62DE: 99         SBC     C               
62DF: 44         LD      B,H             
62E0: 15         DEC     D               
62E1: 22         LD      (HLI),A         
62E2: 10 27      STOP    $27             
62E4: 5A         LD      E,D             
62E5: 24         INC     H               
62E6: 00         NOP                     
62E7: FC         ???                     
62E8: 13         INC     DE              
62E9: 0C         INC     C               
62EA: 68         LD      L,B             
62EB: 07         RLCA                    
62EC: 20 04      JR      NZ,$62F2        
62EE: 90         SUB     B               
62EF: 04         INC     B               
62F0: 80         ADD     A,B             
62F1: 44         LD      B,H             
62F2: 28 C4      JR      Z,$62B8         
62F4: 51         LD      D,C             
62F5: 2E 47      LD      L,$47           
62F7: 38 C8      JR      C,$62C1         
62F9: 30 16      JR      NC,$6311        
62FB: E0 04      LDFF00  ($04),A         
62FD: 20 11      JR      NZ,$6310        
62FF: 20 89      JR      NZ,$628A        
6301: 00         NOP                     
6302: 41         LD      B,C             
6303: 00         NOP                     
6304: 22         LD      (HLI),A         
6305: 00         NOP                     
6306: 3C         INC     A               
6307: 00         NOP                     
6308: 30 00      JR      NC,$630A        
630A: 24         INC     H               
630B: 00         NOP                     
630C: 48         LD      C,B             
630D: 00         NOP                     
630E: D0         RET     NC              
630F: 00         NOP                     
6310: 88         ADC     A,B             
6311: 00         NOP                     
6312: C0         RET     NZ              
6313: 00         NOP                     
6314: 24         INC     H               
6315: 00         NOP                     
6316: 12         LD      (DE),A          
6317: 00         NOP                     
6318: 98         SBC     B               
6319: 00         NOP                     
631A: 38 00      JR      C,$631C         
631C: 44         LD      B,H             
631D: 00         NOP                     
631E: 83         ADD     A,E             
631F: 00         NOP                     
6320: C1         POP     BC              
6321: 00         NOP                     
6322: 22         LD      (HLI),A         
6323: 00         NOP                     
6324: 1C         INC     E               
6325: 00         NOP                     
6326: 09         ADD     HL,BC           
6327: 00         NOP                     
6328: 48         LD      C,B             
6329: 00         NOP                     
632A: 24         INC     H               
632B: 00         NOP                     
632C: 13         INC     DE              
632D: 00         NOP                     
632E: 01 00 01   LD      BC,$0100        
6331: 00         NOP                     
6332: 12         LD      (DE),A          
6333: 00         NOP                     
6334: 24         INC     H               
6335: 00         NOP                     
6336: 4C         LD      C,H             
6337: 00         NOP                     
6338: 1C         INC     E               
6339: 00         NOP                     
633A: 24         INC     H               
633B: 00         NOP                     
633C: C2 00 81   JP      NZ,$8100        
633F: 00         NOP                     
6340: 00         NOP                     
6341: 00         NOP                     
6342: 00         NOP                     
6343: 00         NOP                     
6344: 00         NOP                     
6345: 00         NOP                     
6346: 07         RLCA                    
6347: 07         RLCA                    
6348: 0C         INC     C               
6349: 08 1B 10   LD      ($101B),SP      
634C: 17         RLA                     
634D: 10 17      STOP    $17             
634F: 10 00      STOP    $00             
6351: 00         NOP                     
6352: 00         NOP                     
6353: 00         NOP                     
6354: 00         NOP                     
6355: 00         NOP                     
6356: E0 E0      LDFF00  ($E0),A         
6358: 30 10      JR      NC,$636A        
635A: D8         RET     C               
635B: 08 E8 08   LD      ($08E8),SP      
635E: E8 08      ADD     SP,$08          
6360: 17         RLA                     
6361: 10 1B      STOP    $1B             
6363: 10 14      STOP    $14             
6365: 18 08      JR      $636F           
6367: 0F         RRCA                    
6368: 07         RLCA                    
6369: 07         RLCA                    
636A: 00         NOP                     
636B: 00         NOP                     
636C: 00         NOP                     
636D: 00         NOP                     
636E: 00         NOP                     
636F: 00         NOP                     
6370: E8 08      ADD     SP,$08          
6372: D8         RET     C               
6373: 08 28 18   LD      ($1828),SP      
6376: 10 F0      STOP    $F0             
6378: E0 E0      LDFF00  ($E0),A         
637A: 00         NOP                     
637B: 00         NOP                     
637C: 00         NOP                     
637D: 00         NOP                     
637E: 00         NOP                     
637F: 00         NOP                     
6380: 00         NOP                     
6381: 00         NOP                     
6382: 3F         CCF                     
6383: 00         NOP                     
6384: 67         LD      H,A             
6385: 00         NOP                     
6386: 5F         LD      E,A             
6387: 00         NOP                     
6388: 7E         LD      A,(HL)          
6389: 00         NOP                     
638A: 7C         LD      A,H             
638B: 00         NOP                     
638C: 79         LD      A,C             
638D: 00         NOP                     
638E: 32         LD      (HLD),A         
638F: 00         NOP                     
6390: 00         NOP                     
6391: 00         NOP                     
6392: 7C         LD      A,H             
6393: 00         NOP                     
6394: 4E         LD      C,(HL)          
6395: 00         NOP                     
6396: 7E         LD      A,(HL)          
6397: 00         NOP                     
6398: 1E 00      LD      E,$00           
639A: CE 00      ADC     $00             
639C: E0 00      LDFF00  ($00),A         
639E: 60         LD      H,B             
639F: 00         NOP                     
63A0: 02         LD      (BC),A          
63A1: 00         NOP                     
63A2: 3B         DEC     SP              
63A3: 00         NOP                     
63A4: 49         LD      C,C             
63A5: 00         NOP                     
63A6: 5C         LD      E,H             
63A7: 00         NOP                     
63A8: 7E         LD      A,(HL)          
63A9: 00         NOP                     
63AA: 7E         LD      A,(HL)          
63AB: 00         NOP                     
63AC: 3C         INC     A               
63AD: 00         NOP                     
63AE: 00         NOP                     
63AF: 00         NOP                     
63B0: E6 00      AND     $00             
63B2: CA 00 96   JP      Z,$9600         
63B5: 00         NOP                     
63B6: 2E 00      LD      L,$00           
63B8: 7E         LD      A,(HL)          
63B9: 00         NOP                     
63BA: 7E         LD      A,(HL)          
63BB: 00         NOP                     
63BC: 3C         INC     A               
63BD: 00         NOP                     
63BE: 00         NOP                     
63BF: 00         NOP                     
63C0: 81         ADD     A,C             
63C1: 00         NOP                     
63C2: 21 40 12   LD      HL,$1240        
63C5: 21 2C 12   LD      HL,$122C        
63C8: 20 1E      JR      NZ,$63E8        
63CA: 14         INC     D               
63CB: 22         LD      (HLI),A         
63CC: 41         LD      B,C             
63CD: 22         LD      (HLI),A         
63CE: 80         ADD     A,B             
63CF: 63         LD      H,E             
63D0: 80         ADD     A,B             
63D1: 00         NOP                     
63D2: C2 00 2C   JP      NZ,$2C00        
63D5: C0         RET     NZ              
63D6: 08 30 C8   LD      ($C830),SP      
63D9: 30 D0      JR      NC,$63AB        
63DB: 28 88      JR      Z,$6365         
63DD: 44         LD      B,H             
63DE: 44         LD      B,H             
63DF: 83         ADD     A,E             
63E0: 18 E7      JR      $63C9           
63E2: 02         LD      (BC),A          
63E3: 3C         INC     A               
63E4: 04         INC     B               
63E5: 18 14      JR      $63FB           
63E7: 08 14 08   LD      ($0814),SP      
63EA: 13         INC     DE              
63EB: 0C         INC     C               
63EC: 60         LD      H,B             
63ED: 13         INC     DE              
63EE: 00         NOP                     
63EF: 01 45 82   LD      BC,$8245        
63F2: BC         CP      H               
63F3: 42         LD      B,D             
63F4: 58         LD      E,B             
63F5: 24         INC     H               
63F6: 44         LD      B,H             
63F7: 38 4C      JR      C,$6445         
63F9: 30 A4      JR      NC,$639F        
63FB: 40         LD      B,B             
63FC: 42         LD      B,D             
63FD: 80         ADD     A,B             
63FE: 81         ADD     A,C             
63FF: 00         NOP                     
6400: 80         ADD     A,B             
6401: 00         NOP                     
6402: 8C         ADC     A,H             
6403: 00         NOP                     
6404: 8E         ADC     A,(HL)          
6405: 00         NOP                     
6406: C6 00      ADD     $00             
6408: 60         LD      H,B             
6409: 00         NOP                     
640A: 30 00      JR      NC,$640C        
640C: 58         LD      E,B             
640D: 00         NOP                     
640E: 0F         RRCA                    
640F: 00         NOP                     
6410: 0F         RRCA                    
6411: 00         NOP                     
6412: 18 00      JR      $6414           
6414: 30 00      JR      NC,$6416        
6416: 62         LD      H,D             
6417: 00         NOP                     
6418: C0         RET     NZ              
6419: 00         NOP                     
641A: 8C         ADC     A,H             
641B: 00         NOP                     
641C: 8C         ADC     A,H             
641D: 00         NOP                     
641E: 80         ADD     A,B             
641F: 00         NOP                     
6420: 01 00 31   LD      BC,$3100        
6423: 00         NOP                     
6424: 71         LD      (HL),C          
6425: 00         NOP                     
6426: 63         LD      H,E             
6427: 00         NOP                     
6428: 06 00      LD      B,$00           
642A: 0C         INC     C               
642B: 00         NOP                     
642C: 18 00      JR      $642E           
642E: F0 00      LD      A,($00)         
6430: F0 00      LD      A,($00)         
6432: 18 00      JR      $6434           
6434: 0C         INC     C               
6435: 00         NOP                     
6436: 06 00      LD      B,$00           
6438: 33         INC     SP              
6439: 00         NOP                     
643A: 31 00 81   LD      SP,$8100        
643D: 00         NOP                     
643E: 01 00 00   LD      BC,$0000        
6441: 00         NOP                     
6442: 00         NOP                     
6443: 00         NOP                     
6444: 00         NOP                     
6445: 00         NOP                     
6446: 07         RLCA                    
6447: 07         RLCA                    
6448: 0C         INC     C               
6449: 08 1B 10   LD      ($101B),SP      
644C: 17         RLA                     
644D: 10 17      STOP    $17             
644F: 10 00      STOP    $00             
6451: 00         NOP                     
6452: 00         NOP                     
6453: 00         NOP                     
6454: 00         NOP                     
6455: 00         NOP                     
6456: E0 E0      LDFF00  ($E0),A         
6458: 30 10      JR      NC,$646A        
645A: D8         RET     C               
645B: 08 E8 08   LD      ($08E8),SP      
645E: E8 08      ADD     SP,$08          
6460: 17         RLA                     
6461: 10 1B      STOP    $1B             
6463: 10 14      STOP    $14             
6465: 18 08      JR      $646F           
6467: 0F         RRCA                    
6468: 07         RLCA                    
6469: 07         RLCA                    
646A: 00         NOP                     
646B: 00         NOP                     
646C: 00         NOP                     
646D: 00         NOP                     
646E: 00         NOP                     
646F: 00         NOP                     
6470: E8 08      ADD     SP,$08          
6472: D8         RET     C               
6473: 08 28 18   LD      ($1828),SP      
6476: 10 F0      STOP    $F0             
6478: E0 E0      LDFF00  ($E0),A         
647A: 00         NOP                     
647B: 00         NOP                     
647C: 00         NOP                     
647D: 00         NOP                     
647E: 00         NOP                     
647F: 00         NOP                     
6480: F8 00      LDHL    SP,$00          
6482: B8         CP      B               
6483: 44         LD      B,H             
6484: F9         LD      SP,HL           
6485: 04         INC     B               
6486: E9         JP      (HL)            
6487: 14         INC     D               
6488: 79         LD      A,C             
6489: 84         ADD     A,H             
648A: 01 78 03   LD      BC,$0378        
648D: 00         NOP                     
648E: 3F         CCF                     
648F: 00         NOP                     
6490: 01 02 F8   LD      BC,$F802        
6493: 01 BC 40   LD      BC,$40BC        
6496: FC         ???                     
6497: 02         LD      (BC),A          
6498: EC         ???                     
6499: 12         LD      (DE),A          
649A: FC         ???                     
649B: 02         LD      (BC),A          
649C: FC         ???                     
649D: 02         LD      (BC),A          
649E: C0         RET     NZ              
649F: 3C         INC     A               
64A0: 7F         LD      A,A             
64A1: 00         NOP                     
64A2: 6F         LD      L,A             
64A3: 10 7E      STOP    $7E             
64A5: 01 7A 05   LD      BC,$057A        
64A8: 3E 41      LD      A,$41           
64AA: 1E 21      LD      E,$21           
64AC: 80         ADD     A,B             
64AD: 1E C0      LD      E,$C0           
64AF: 00         NOP                     
64B0: 80         ADD     A,B             
64B1: 40         LD      B,B             
64B2: 1E 80      LD      E,$80           
64B4: 3F         CCF                     
64B5: 00         NOP                     
64B6: 7B         LD      A,E             
64B7: 04         INC     B               
64B8: 6F         LD      L,A             
64B9: 10 7F      STOP    $7F             
64BB: 00         NOP                     
64BC: 7F         LD      A,A             
64BD: 00         NOP                     
64BE: 01 3E 80   LD      BC,$803E        
64C1: 00         NOP                     
64C2: 40         LD      B,B             
64C3: 8F         ADC     A,A             
64C4: 69         LD      L,C             
64C5: 90         SUB     B               
64C6: 10 E0      STOP    $E0             
64C8: 10 60      STOP    $60             
64CA: 09         ADD     HL,BC           
64CB: 30 46      JR      NC,$6513        
64CD: 39         ADD     HL,SP           
64CE: 18 27      JR      $64F7           
64D0: 13         INC     DE              
64D1: 0C         INC     C               
64D2: 24         INC     H               
64D3: 18 48      JR      $651D           
64D5: B0         OR      B               
64D6: 02         LD      (BC),A          
64D7: F0 08      LD      A,($08)         
64D9: F0 51      LD      A,($51)         
64DB: 8E         ADC     A,(HL)          
64DC: 44         LD      B,H             
64DD: 88         ADC     A,B             
64DE: 30 C8      JR      NC,$64A8        
64E0: 14         INC     D               
64E1: 23         INC     HL              
64E2: 42         LD      B,D             
64E3: 21 D2 21   LD      HL,$21D2        
64E6: 0D         DEC     C               
64E7: F2         ???                     
64E8: 11 0E 10   LD      DE,$100E        
64EB: 0F         RRCA                    
64EC: 20 18      JR      NZ,$6506        
64EE: 80         ADD     A,B             
64EF: 70         LD      (HL),B          
64F0: 00         NOP                     
64F1: F8 64      LDHL    SP,$64          
64F3: 98         SBC     B               
64F4: 92         SUB     D               
64F5: 0C         INC     C               
64F6: 11 0E E0   LD      DE,$E00E        
64F9: 13         INC     DE              
64FA: 00         NOP                     
64FB: E1         POP     HL              
64FC: 80         ADD     A,B             
64FD: 01 01 00   LD      BC,$0001        
6500: 13         INC     DE              
6501: 00         NOP                     
6502: 26 00      LD      H,$00           
6504: 4C         LD      C,H             
6505: 00         NOP                     
6506: 98         SBC     B               
6507: 00         NOP                     
6508: 30 00      JR      NC,$650A        
650A: 64         LD      H,H             
650B: 00         NOP                     
650C: C8         RET     Z               
650D: 00         NOP                     
650E: 90         SUB     B               
650F: 00         NOP                     
6510: C0         RET     NZ              
6511: 00         NOP                     
6512: 60         LD      H,B             
6513: 00         NOP                     
6514: 32         LD      (HLD),A         
6515: 00         NOP                     
6516: 99         SBC     C               
6517: 00         NOP                     
6518: 4C         LD      C,H             
6519: 00         NOP                     
651A: 26 00      LD      H,$00           
651C: 13         INC     DE              
651D: 00         NOP                     
651E: 09         ADD     HL,BC           
651F: 00         NOP                     
6520: 90         SUB     B               
6521: 00         NOP                     
6522: C8         RET     Z               
6523: 00         NOP                     
6524: 64         LD      H,H             
6525: 00         NOP                     
6526: 32         LD      (HLD),A         
6527: 00         NOP                     
6528: 99         SBC     C               
6529: 00         NOP                     
652A: 4C         LD      C,H             
652B: 00         NOP                     
652C: 06 00      LD      B,$00           
652E: 03         INC     BC              
652F: 00         NOP                     
6530: 09         ADD     HL,BC           
6531: 00         NOP                     
6532: 13         INC     DE              
6533: 00         NOP                     
6534: 26 00      LD      H,$00           
6536: 0C         INC     C               
6537: 00         NOP                     
6538: 19         ADD     HL,DE           
6539: 00         NOP                     
653A: 32         LD      (HLD),A         
653B: 00         NOP                     
653C: 64         LD      H,H             
653D: 00         NOP                     
653E: C8         RET     Z               
653F: 00         NOP                     
6540: 00         NOP                     
6541: 00         NOP                     
6542: 00         NOP                     
6543: 00         NOP                     
6544: 00         NOP                     
6545: 00         NOP                     
6546: 07         RLCA                    
6547: 07         RLCA                    
6548: 0C         INC     C               
6549: 08 1B 10   LD      ($101B),SP      
654C: 17         RLA                     
654D: 10 17      STOP    $17             
654F: 10 00      STOP    $00             
6551: 00         NOP                     
6552: 00         NOP                     
6553: 00         NOP                     
6554: 00         NOP                     
6555: 00         NOP                     
6556: E0 E0      LDFF00  ($E0),A         
6558: 30 10      JR      NC,$656A        
655A: D8         RET     C               
655B: 08 E8 08   LD      ($08E8),SP      
655E: E8 08      ADD     SP,$08          
6560: 17         RLA                     
6561: 10 1B      STOP    $1B             
6563: 10 14      STOP    $14             
6565: 18 08      JR      $656F           
6567: 0F         RRCA                    
6568: 07         RLCA                    
6569: 07         RLCA                    
656A: 00         NOP                     
656B: 00         NOP                     
656C: 00         NOP                     
656D: 00         NOP                     
656E: 00         NOP                     
656F: 00         NOP                     
6570: E8 08      ADD     SP,$08          
6572: D8         RET     C               
6573: 08 28 18   LD      ($1828),SP      
6576: 10 F0      STOP    $F0             
6578: E0 E0      LDFF00  ($E0),A         
657A: 00         NOP                     
657B: 00         NOP                     
657C: 00         NOP                     
657D: 00         NOP                     
657E: 00         NOP                     
657F: 00         NOP                     
6580: 00         NOP                     
6581: 00         NOP                     
6582: 3F         CCF                     
6583: 00         NOP                     
6584: 7E         LD      A,(HL)          
6585: 01 6C 02   LD      BC,$026C        
6588: 79         LD      A,C             
6589: 04         INC     B               
658A: 73         LD      (HL),E          
658B: 08 66 10   LD      ($1066),SP      
658E: 6F         LD      L,A             
658F: 00         NOP                     
6590: 00         NOP                     
6591: 00         NOP                     
6592: FC         ???                     
6593: 00         NOP                     
6594: 7E         LD      A,(HL)          
6595: 80         ADD     A,B             
6596: 36 40      LD      (HL),$40        
6598: 9E         SBC     (HL)            
6599: 20 CE      JR      NZ,$6569        
659B: 10 E6      STOP    $E6             
659D: 08 F6 00   LD      ($00F6),SP      
65A0: 67         LD      H,A             
65A1: 08 73 04   LD      ($0473),SP      
65A4: 79         LD      A,C             
65A5: 02         LD      (BC),A          
65A6: 5C         LD      E,H             
65A7: 01 7E 00   LD      BC,$007E        
65AA: 3F         CCF                     
65AB: 40         LD      B,B             
65AC: 00         NOP                     
65AD: 3F         CCF                     
65AE: 00         NOP                     
65AF: 00         NOP                     
65B0: E6 10      AND     $10             
65B2: CE 20      ADC     $20             
65B4: 9E         SBC     (HL)            
65B5: 40         LD      B,B             
65B6: 36 80      LD      (HL),$80        
65B8: 7E         LD      A,(HL)          
65B9: 00         NOP                     
65BA: FC         ???                     
65BB: 02         LD      (BC),A          
65BC: 00         NOP                     
65BD: FC         ???                     
65BE: 00         NOP                     
65BF: 00         NOP                     
65C0: 12         LD      (DE),A          
65C1: 01 E5 02   LD      BC,$02E5        
65C4: 0A         LD      A,(BC)          
65C5: 24         INC     H               
65C6: 84         ADD     A,H             
65C7: 18 24      JR      $65ED           
65C9: 18 5B      JR      $6626           
65CB: 24         INC     H               
65CC: A4         AND     H               
65CD: 43         LD      B,E             
65CE: 44         LD      B,H             
65CF: 83         ADD     A,E             
65D0: 41         LD      B,C             
65D1: 80         ADD     A,B             
65D2: A1         AND     C               
65D3: 40         LD      B,B             
65D4: 52         LD      D,D             
65D5: 24         INC     H               
65D6: 20 18      JR      NZ,$65F0        
65D8: 44         LD      B,H             
65D9: 28 8A      JR      Z,$6565         
65DB: 44         LD      B,H             
65DC: 09         ADD     HL,BC           
65DD: C6 32      ADD     $32             
65DF: C9         RET                     
65E0: 45         LD      B,L             
65E1: 82         ADD     A,D             
65E2: B8         CP      B               
65E3: 47         LD      B,A             
65E4: 56         LD      D,(HL)          
65E5: 29         ADD     HL,HL           
65E6: 25         DEC     H               
65E7: 18 94      JR      $657D           
65E9: 08 42 0C   LD      ($0C42),SP      
65EC: 05         DEC     B               
65ED: 3A         LD      A,(HLD)         
65EE: E2         LDFF00  (C),A           
65EF: 01 8A 71   LD      BC,$718A        
65F2: 95         SUB     L               
65F3: 42         LD      B,D             
65F4: 6A         LD      L,D             
65F5: 84         ADD     A,H             
65F6: 14         INC     D               
65F7: E8 C9      ADD     SP,$C9          
65F9: 30 42      JR      NC,$663D        
65FB: 3C         INC     A               
65FC: A4         AND     H               
65FD: 42         LD      B,D             
65FE: 49         LD      C,C             
65FF: 80         ADD     A,B             
6600: 3E 00      LD      A,$00           
6602: 3E 00      LD      A,$00           
6604: A2         AND     D               
6605: 00         NOP                     
6606: 41         LD      B,C             
6607: 00         NOP                     
6608: 41         LD      B,C             
6609: 00         NOP                     
660A: 63         LD      H,E             
660B: 00         NOP                     
660C: 9F         SBC     A               
660D: 00         NOP                     
660E: 07         RLCA                    
660F: 00         NOP                     
6610: 10 00      STOP    $00             
6612: 08 00 2F   LD      ($2F00),SP      
6615: 00         NOP                     
6616: 08 00 F8   LD      ($F800),SP      
6619: 00         NOP                     
661A: E4         ???                     
661B: 00         NOP                     
661C: E3         ???                     
661D: 00         NOP                     
661E: E1         POP     HL              
661F: 00         NOP                     
6620: 27         DAA                     
6621: 00         NOP                     
6622: 87         ADD     A,A             
6623: 00         NOP                     
6624: C8         RET     Z               
6625: 00         NOP                     
6626: 70         LD      (HL),B          
6627: 00         NOP                     
6628: 70         LD      (HL),B          
6629: 00         NOP                     
662A: 79         LD      A,C             
662B: 00         NOP                     
662C: C7         RST     0X00            
662D: 00         NOP                     
662E: 43         LD      B,E             
662F: 00         NOP                     
6630: E1         POP     HL              
6631: 00         NOP                     
6632: F1         POP     AF              
6633: 00         NOP                     
6634: 8E         ADC     A,(HL)          
6635: 00         NOP                     
6636: 84         ADD     A,H             
6637: 00         NOP                     
6638: 94         SUB     H               
6639: 00         NOP                     
663A: C4 00 F9   CALL    NZ,$F900        
663D: 00         NOP                     
663E: F0 00      LD      A,($00)         
6640: 00         NOP                     
6641: 00         NOP                     
6642: 00         NOP                     
6643: 00         NOP                     
6644: 00         NOP                     
6645: 00         NOP                     
6646: 07         RLCA                    
6647: 07         RLCA                    
6648: 0C         INC     C               
6649: 08 1B 10   LD      ($101B),SP      
664C: 17         RLA                     
664D: 10 17      STOP    $17             
664F: 10 00      STOP    $00             
6651: 00         NOP                     
6652: 00         NOP                     
6653: 00         NOP                     
6654: 00         NOP                     
6655: 00         NOP                     
6656: E0 E0      LDFF00  ($E0),A         
6658: 30 10      JR      NC,$666A        
665A: D8         RET     C               
665B: 08 E8 08   LD      ($08E8),SP      
665E: E8 08      ADD     SP,$08          
6660: 17         RLA                     
6661: 10 1B      STOP    $1B             
6663: 10 14      STOP    $14             
6665: 18 08      JR      $666F           
6667: 0F         RRCA                    
6668: 07         RLCA                    
6669: 07         RLCA                    
666A: 00         NOP                     
666B: 00         NOP                     
666C: 00         NOP                     
666D: 00         NOP                     
666E: 00         NOP                     
666F: 00         NOP                     
6670: E8 08      ADD     SP,$08          
6672: D8         RET     C               
6673: 08 28 18   LD      ($1828),SP      
6676: 10 F0      STOP    $F0             
6678: E0 E0      LDFF00  ($E0),A         
667A: 00         NOP                     
667B: 00         NOP                     
667C: 00         NOP                     
667D: 00         NOP                     
667E: 00         NOP                     
667F: 00         NOP                     
6680: 00         NOP                     
6681: 00         NOP                     
6682: 3F         CCF                     
6683: 00         NOP                     
6684: 73         LD      (HL),E          
6685: 00         NOP                     
6686: 66         LD      H,(HL)          
6687: 00         NOP                     
6688: 4C         LD      C,H             
6689: 00         NOP                     
668A: 59         LD      E,C             
668B: 00         NOP                     
668C: 73         LD      (HL),E          
668D: 00         NOP                     
668E: 67         LD      H,A             
668F: 00         NOP                     
6690: 00         NOP                     
6691: 00         NOP                     
6692: FC         ???                     
6693: 00         NOP                     
6694: 1E 00      LD      E,$00           
6696: 7E         LD      A,(HL)          
6697: 00         NOP                     
6698: FE 00      CP      $00             
669A: FE 00      CP      $00             
669C: FE 00      CP      $00             
669E: FE 00      CP      $00             
66A0: 4F         LD      C,A             
66A1: 00         NOP                     
66A2: 5F         LD      E,A             
66A3: 00         NOP                     
66A4: 5F         LD      E,A             
66A5: 00         NOP                     
66A6: 7F         LD      A,A             
66A7: 00         NOP                     
66A8: 7F         LD      A,A             
66A9: 00         NOP                     
66AA: 3F         CCF                     
66AB: 40         LD      B,B             
66AC: 00         NOP                     
66AD: 3F         CCF                     
66AE: 00         NOP                     
66AF: 00         NOP                     
66B0: FE 00      CP      $00             
66B2: FE 00      CP      $00             
66B4: FE 00      CP      $00             
66B6: FE 00      CP      $00             
66B8: FE 00      CP      $00             
66BA: FC         ???                     
66BB: 02         LD      (BC),A          
66BC: 00         NOP                     
66BD: FC         ???                     
66BE: 00         NOP                     
66BF: 00         NOP                     
66C0: 3C         INC     A               
66C1: 02         LD      (BC),A          
66C2: 3C         INC     A               
66C3: 02         LD      (BC),A          
66C4: 25         DEC     H               
66C5: 82         ADD     A,D             
66C6: 06 43      LD      B,$43           
66C8: 2E 43      LD      L,$43           
66CA: 5B         LD      E,E             
66CB: 27         DAA                     
66CC: E3         ???                     
66CD: 1F         RRA                     
66CE: 1B         DEC     DE              
66CF: 07         RLCA                    
66D0: 10 00      STOP    $00             
66D2: 00         NOP                     
66D3: 08 20 0F   LD      ($0F20),SP      
66D6: 90         SUB     B               
66D7: 08 00 F8   LD      ($F800),SP      
66DA: 14         INC     D               
66DB: E0 D3      LDFF00  ($D3),A         
66DD: E0 D1      LDFF00  ($D1),A         
66DF: E0 0B      LDFF00  ($0B),A         
66E1: 07         RLCA                    
66E2: 89         ADC     A,C             
66E3: 07         RLCA                    
66E4: C4 09 68   CALL    NZ,$6809        
66E7: 10 48      STOP    $48             
66E9: 30 34      JR      NC,$671F        
66EB: 48         LD      C,B             
66EC: C3 04 43   JP      $4304           
66EF: 00         NOP                     
66F0: D1         POP     DE              
66F1: E0 89      LDFF00  ($89),A         
66F3: F0 F2      LD      A,($F2)         
66F5: 8C         ADC     A,H             
66F6: 48         LD      C,B             
66F7: 84         ADD     A,H             
66F8: 50         LD      D,B             
66F9: 84         ADD     A,H             
66FA: 84         ADD     A,H             
66FB: 40         LD      B,B             
66FC: B9         CP      C               
66FD: 40         LD      B,B             
66FE: B0         OR      B               
66FF: 40         LD      B,B             
6700: 80         ADD     A,B             
6701: 80         ADD     A,B             
6702: C0         RET     NZ              
6703: C0         RET     NZ              
6704: A0         AND     B               
6705: A0         AND     B               
6706: 9F         SBC     A               
6707: 97         SUB     A               
6708: C8         RET     Z               
6709: 88         ADC     A,B             
670A: E8 C0      ADD     SP,$C0          
670C: F3         DI                      
670D: A1         AND     C               
670E: D3         ???                     
670F: B3         OR      E               
6710: 01 01 03   LD      BC,$0301        
6713: 03         INC     BC              
6714: 05         DEC     B               
6715: 05         DEC     B               
6716: F9         LD      SP,HL           
6717: E9         JP      (HL)            
6718: 13         INC     DE              
6719: 11 17 03   LD      DE,$0317        
671C: CF         RST     0X08            
671D: 85         ADD     A,L             
671E: CB CD      SET     1,E             
6720: D3         ???                     
6721: B3         OR      E               
6722: D3         ???                     
6723: B3         OR      E               
6724: D9         RETI                    
6725: B1         OR      C               
6726: E5         PUSH    HL              
6727: A1         AND     C               
6728: ED         ???                     
6729: AD         XOR     L               
672A: F6 BC      OR      $BC             
672C: C3 BE FF   JP      $FFBE           
672F: FF         RST     0X38            
6730: CB CD      SET     1,E             
6732: CB CD      SET     1,E             
6734: 9B         SBC     E               
6735: 8D         ADC     A,L             
6736: A7         AND     A               
6737: 85         ADD     A,L             
6738: B7         OR      A               
6739: B5         OR      L               
673A: 6F         LD      L,A             
673B: 3D         DEC     A               
673C: C3 7D FF   JP      $FF7D           
673F: FF         RST     0X38            
6740: 00         NOP                     
6741: 00         NOP                     
6742: 00         NOP                     
6743: 00         NOP                     
6744: 00         NOP                     
6745: 00         NOP                     
6746: 00         NOP                     
6747: 00         NOP                     
6748: 00         NOP                     
6749: 00         NOP                     
674A: 00         NOP                     
674B: 00         NOP                     
674C: 00         NOP                     
674D: 00         NOP                     
674E: 00         NOP                     
674F: 00         NOP                     
6750: 00         NOP                     
6751: 00         NOP                     
6752: 00         NOP                     
6753: 00         NOP                     
6754: 00         NOP                     
6755: 00         NOP                     
6756: 00         NOP                     
6757: 00         NOP                     
6758: 00         NOP                     
6759: 00         NOP                     
675A: 00         NOP                     
675B: 00         NOP                     
675C: 00         NOP                     
675D: 00         NOP                     
675E: 00         NOP                     
675F: 00         NOP                     
6760: 00         NOP                     
6761: 00         NOP                     
6762: 00         NOP                     
6763: 00         NOP                     
6764: 00         NOP                     
6765: 00         NOP                     
6766: 00         NOP                     
6767: 00         NOP                     
6768: 00         NOP                     
6769: 00         NOP                     
676A: 00         NOP                     
676B: 00         NOP                     
676C: 00         NOP                     
676D: 00         NOP                     
676E: 00         NOP                     
676F: 00         NOP                     
6770: 00         NOP                     
6771: 00         NOP                     
6772: 00         NOP                     
6773: 00         NOP                     
6774: 00         NOP                     
6775: 00         NOP                     
6776: 00         NOP                     
6777: 00         NOP                     
6778: 00         NOP                     
6779: 00         NOP                     
677A: 00         NOP                     
677B: 00         NOP                     
677C: 00         NOP                     
677D: 00         NOP                     
677E: 00         NOP                     
677F: 00         NOP                     
6780: 00         NOP                     
6781: FF         RST     0X38            
6782: 00         NOP                     
6783: 80         ADD     A,B             
6784: 3F         CCF                     
6785: 83         ADD     A,E             
6786: 3F         CCF                     
6787: 82         ADD     A,D             
6788: 3F         CCF                     
6789: BE         CP      (HL)            
678A: 3F         CCF                     
678B: A2         AND     D               
678C: 3F         CCF                     
678D: A2         AND     D               
678E: 3F         CCF                     
678F: A2         AND     D               
6790: 3F         CCF                     
6791: FF         RST     0X38            
6792: 3F         CCF                     
6793: 21 FF E1   LD      HL,$E1FF        
6796: FF         RST     0X38            
6797: 21 FF 21   LD      HL,$21FF        
679A: FF         RST     0X38            
679B: 21 E1 21   LD      HL,$21E1        
679E: FF         RST     0X38            
679F: 3F         CCF                     
67A0: 3E A2      LD      A,$A2           
67A2: 3F         CCF                     
67A3: A3         AND     E               
67A4: 23         INC     HL              
67A5: A3         AND     E               
67A6: 3F         CCF                     
67A7: BF         CP      A               
67A8: 3F         CCF                     
67A9: BF         CP      A               
67AA: 3F         CCF                     
67AB: 80         ADD     A,B             
67AC: 00         NOP                     
67AD: 80         ADD     A,B             
67AE: 00         NOP                     
67AF: FF         RST     0X38            
67B0: 3F         CCF                     
67B1: 3F         CCF                     
67B2: FF         RST     0X38            
67B3: FF         RST     0X38            
67B4: FF         RST     0X38            
67B5: FF         RST     0X38            
67B6: FF         RST     0X38            
67B7: FF         RST     0X38            
67B8: FF         RST     0X38            
67B9: FF         RST     0X38            
67BA: FE 01      CP      $01             
67BC: 00         NOP                     
67BD: 01 00 FF   LD      BC,$FF00        
67C0: 00         NOP                     
67C1: 00         NOP                     
67C2: FF         RST     0X38            
67C3: 00         NOP                     
67C4: DF         RST     0X18            
67C5: 3F         CCF                     
67C6: BF         CP      A               
67C7: 7F         LD      A,A             
67C8: FF         RST     0X38            
67C9: 7F         LD      A,A             
67CA: FF         RST     0X38            
67CB: 7F         LD      A,A             
67CC: FF         RST     0X38            
67CD: 7C         LD      A,H             
67CE: FF         RST     0X38            
67CF: 78         LD      A,B             
67D0: 00         NOP                     
67D1: 00         NOP                     
67D2: FF         RST     0X38            
67D3: 00         NOP                     
67D4: FB         EI                      
67D5: FC         ???                     
67D6: FD         ???                     
67D7: 86         ADD     A,(HL)          
67D8: DF         RST     0X18            
67D9: 82         ADD     A,D             
67DA: AF         XOR     A               
67DB: C2 97 E2   JP      NZ,$E297        
67DE: CB 72      SET     1,E             
67E0: FB         EI                      
67E1: 70         LD      (HL),B          
67E2: F4         ???                     
67E3: 78         LD      A,B             
67E4: F1         POP     AF              
67E5: 7E         LD      A,(HL)          
67E6: FC         ???                     
67E7: 7F         LD      A,A             
67E8: EB         ???                     
67E9: 47         LD      B,A             
67EA: C1         POP     BC              
67EB: 40         LD      B,B             
67EC: C0         RET     NZ              
67ED: 40         LD      B,B             
67EE: FF         RST     0X38            
67EF: FF         RST     0X38            
67F0: E7         RST     0X20            
67F1: 3A         LD      A,(HLD)         
67F2: F3         DI                      
67F3: 1E 3B      LD      E,$3B           
67F5: 0E 4F      LD      C,$4F           
67F7: 86         ADD     A,(HL)          
67F8: 97         SUB     A               
67F9: E2         LDFF00  (C),A           
67FA: 73         LD      (HL),E          
67FB: FE 2F      CP      $2F             
67FD: 1E FF      LD      E,$FF           
67FF: FE FF      CP      $FF             
6801: FF         RST     0X38            
6802: FF         RST     0X38            
6803: FF         RST     0X38            
6804: FF         RST     0X38            
6805: FF         RST     0X38            
6806: FE FE      CP      $FE             
6808: FC         ???                     
6809: FC         ???                     
680A: F8 F8      LDHL    SP,$F8          
680C: F0 F0      LD      A,($F0)         
680E: E0 E0      LDFF00  ($E0),A         
6810: FF         RST     0X38            
6811: FF         RST     0X38            
6812: F0 F0      LD      A,($F0)         
6814: 80         ADD     A,B             
6815: 80         ADD     A,B             
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
6820: FF         RST     0X38            
6821: FF         RST     0X38            
6822: 0F         RRCA                    
6823: 0F         RRCA                    
6824: 01 01 00   LD      BC,$0001        
6827: 00         NOP                     
6828: 00         NOP                     
6829: 00         NOP                     
682A: 00         NOP                     
682B: 00         NOP                     
682C: 00         NOP                     
682D: 00         NOP                     
682E: 00         NOP                     
682F: 00         NOP                     
6830: FF         RST     0X38            
6831: FF         RST     0X38            
6832: FF         RST     0X38            
6833: FF         RST     0X38            
6834: FF         RST     0X38            
6835: FF         RST     0X38            
6836: 7F         LD      A,A             
6837: 7F         LD      A,A             
6838: 3F         CCF                     
6839: 3F         CCF                     
683A: 1F         RRA                     
683B: 1F         RRA                     
683C: 0F         RRCA                    
683D: 0F         RRCA                    
683E: 07         RLCA                    
683F: 07         RLCA                    
6840: E0 E0      LDFF00  ($E0),A         
6842: C0         RET     NZ              
6843: C0         RET     NZ              
6844: C0         RET     NZ              
6845: C0         RET     NZ              
6846: C0         RET     NZ              
6847: C0         RET     NZ              
6848: 80         ADD     A,B             
6849: 80         ADD     A,B             
684A: 80         ADD     A,B             
684B: 80         ADD     A,B             
684C: 80         ADD     A,B             
684D: 80         ADD     A,B             
684E: 80         ADD     A,B             
684F: 80         ADD     A,B             
6850: 07         RLCA                    
6851: 07         RLCA                    
6852: 03         INC     BC              
6853: 03         INC     BC              
6854: 03         INC     BC              
6855: 03         INC     BC              
6856: 03         INC     BC              
6857: 03         INC     BC              
6858: 01 01 01   LD      BC,$0101        
685B: 01 01 01   LD      BC,$0101        
685E: 01 01 80   LD      BC,$8001        
6861: 80         ADD     A,B             
6862: 80         ADD     A,B             
6863: 80         ADD     A,B             
6864: 80         ADD     A,B             
6865: 80         ADD     A,B             
6866: 80         ADD     A,B             
6867: 80         ADD     A,B             
6868: C0         RET     NZ              
6869: C0         RET     NZ              
686A: C0         RET     NZ              
686B: C0         RET     NZ              
686C: C0         RET     NZ              
686D: C0         RET     NZ              
686E: E0 E0      LDFF00  ($E0),A         
6870: 01 01 01   LD      BC,$0101        
6873: 01 01 01   LD      BC,$0101        
6876: 01 01 03   LD      BC,$0301        
6879: 03         INC     BC              
687A: 03         INC     BC              
687B: 03         INC     BC              
687C: 03         INC     BC              
687D: 03         INC     BC              
687E: 07         RLCA                    
687F: 07         RLCA                    
6880: 00         NOP                     
6881: FF         RST     0X38            
6882: 00         NOP                     
6883: 80         ADD     A,B             
6884: 3F         CCF                     
6885: 83         ADD     A,E             
6886: 3F         CCF                     
6887: 82         ADD     A,D             
6888: 3F         CCF                     
6889: BE         CP      (HL)            
688A: 3F         CCF                     
688B: A2         AND     D               
688C: 3F         CCF                     
688D: A2         AND     D               
688E: 3F         CCF                     
688F: A2         AND     D               
6890: 3F         CCF                     
6891: FF         RST     0X38            
6892: 3F         CCF                     
6893: 21 FF E1   LD      HL,$E1FF        
6896: FF         RST     0X38            
6897: 21 FF 21   LD      HL,$21FF        
689A: FF         RST     0X38            
689B: 21 E1 21   LD      HL,$21E1        
689E: FF         RST     0X38            
689F: 3F         CCF                     
68A0: 3E A2      LD      A,$A2           
68A2: 3F         CCF                     
68A3: A3         AND     E               
68A4: 23         INC     HL              
68A5: A3         AND     E               
68A6: 3F         CCF                     
68A7: BF         CP      A               
68A8: 3F         CCF                     
68A9: BF         CP      A               
68AA: 3F         CCF                     
68AB: 80         ADD     A,B             
68AC: 00         NOP                     
68AD: 80         ADD     A,B             
68AE: 00         NOP                     
68AF: FF         RST     0X38            
68B0: 3F         CCF                     
68B1: 3F         CCF                     
68B2: FF         RST     0X38            
68B3: FF         RST     0X38            
68B4: FF         RST     0X38            
68B5: FF         RST     0X38            
68B6: FF         RST     0X38            
68B7: FF         RST     0X38            
68B8: FF         RST     0X38            
68B9: FF         RST     0X38            
68BA: FE 01      CP      $01             
68BC: 00         NOP                     
68BD: 01 00 FF   LD      BC,$FF00        
68C0: E0 E0      LDFF00  ($E0),A         
68C2: F0 F0      LD      A,($F0)         
68C4: F8 F8      LDHL    SP,$F8          
68C6: FC         ???                     
68C7: FC         ???                     
68C8: FE FE      CP      $FE             
68CA: FF         RST     0X38            
68CB: FF         RST     0X38            
68CC: FF         RST     0X38            
68CD: FF         RST     0X38            
68CE: FF         RST     0X38            
68CF: FF         RST     0X38            
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
68DA: 80         ADD     A,B             
68DB: 80         ADD     A,B             
68DC: F0 F0      LD      A,($F0)         
68DE: FF         RST     0X38            
68DF: FF         RST     0X38            
68E0: 00         NOP                     
68E1: 00         NOP                     
68E2: 00         NOP                     
68E3: 00         NOP                     
68E4: 00         NOP                     
68E5: 00         NOP                     
68E6: 00         NOP                     
68E7: 00         NOP                     
68E8: 00         NOP                     
68E9: 00         NOP                     
68EA: 01 01 0F   LD      BC,$0F01        
68ED: 0F         RRCA                    
68EE: FF         RST     0X38            
68EF: FF         RST     0X38            
68F0: 07         RLCA                    
68F1: 07         RLCA                    
68F2: 0F         RRCA                    
68F3: 0F         RRCA                    
68F4: 1F         RRA                     
68F5: 1F         RRA                     
68F6: 3F         CCF                     
68F7: 3F         CCF                     
68F8: 7F         LD      A,A             
68F9: 7F         LD      A,A             
68FA: FF         RST     0X38            
68FB: FF         RST     0X38            
68FC: FF         RST     0X38            
68FD: FF         RST     0X38            
68FE: FF         RST     0X38            
68FF: FF         RST     0X38            
6900: FA DC 2D   LD      A,($2DDC)       
6903: F2         ???                     
6904: 1C         INC     E               
6905: E1         POP     HL              
6906: D8         RET     C               
6907: 21 D0 21   LD      HL,$21D0        
690A: C0         RET     NZ              
690B: 31 E8 72   LD      SP,$72E8        
690E: 90         SUB     B               
690F: EC         ???                     
6910: 90         SUB     B               
6911: E4         ???                     
6912: 90         SUB     B               
6913: E4         ???                     
6914: B0         OR      B               
6915: C4 78 82   CALL    NZ,$8278        
6918: C4 01 82   CALL    NZ,$8201        
691B: 01 00 01   LD      BC,$0100        
691E: 01 00 5F   LD      BC,$5F00        
6921: 3F         CCF                     
6922: B0         OR      B               
6923: 4F         LD      C,A             
6924: 38 87      JR      C,$68AD         
6926: 1D         DEC     E               
6927: 82         ADD     A,D             
6928: 1B         DEC     DE              
6929: 84         ADD     A,H             
692A: 0B         DEC     BC              
692B: 84         ADD     A,H             
692C: 07         RLCA                    
692D: 4E         LD      C,(HL)          
692E: 09         ADD     HL,BC           
692F: 37         SCF                     
6930: 09         ADD     HL,BC           
6931: 27         DAA                     
6932: 09         ADD     HL,BC           
6933: 27         DAA                     
6934: 0D         DEC     C               
6935: 23         INC     HL              
6936: 1E 41      LD      E,$41           
6938: 23         INC     HL              
6939: 80         ADD     A,B             
693A: 41         LD      B,C             
693B: 80         ADD     A,B             
693C: 00         NOP                     
693D: 80         ADD     A,B             
693E: 80         ADD     A,B             
693F: 00         NOP                     
6940: C0         RET     NZ              
6941: C0         RET     NZ              
6942: A0         AND     B               
6943: A0         AND     B               
6944: 93         SUB     E               
6945: 93         SUB     E               
6946: CD 8E 69   CALL    $698E           
6949: 4E         LD      C,(HL)          
694A: 70         LD      (HL),B          
694B: 5F         LD      E,A             
694C: 31 3F 13   LD      SP,$133F        
694F: 1E 03      LD      E,$03           
6951: 03         INC     BC              
6952: 05         DEC     B               
6953: 05         DEC     B               
6954: C9         RET                     
6955: C9         RET                     
6956: B3         OR      E               
6957: 71         LD      (HL),C          
6958: 96         SUB     (HL)            
6959: 72         LD      (HL),D          
695A: 0E FA      LD      C,$FA           
695C: 8C         ADC     A,H             
695D: FC         ???                     
695E: C8         RET     Z               
695F: 78         LD      A,B             
6960: 63         LD      H,E             
6961: 7E         LD      A,(HL)          
6962: 8F         ADC     A,A             
6963: FE 8F      CP      $8F             
6965: FA 4F 78   LD      A,($784F)       
6968: 3F         CCF                     
6969: 3C         INC     A               
696A: 1F         RRA                     
696B: 17         RLA                     
696C: 29         ADD     HL,HL           
696D: 27         DAA                     
696E: 58         LD      E,B             
696F: 4F         LD      C,A             
6970: C6 7E      ADD     $7E             
6972: F1         POP     AF              
6973: 7F         LD      A,A             
6974: F1         POP     AF              
6975: 5F         LD      E,A             
6976: F2         ???                     
6977: 1E FC      LD      E,$FC           
6979: 3C         INC     A               
697A: F8 E8      LDHL    SP,$E8          
697C: 94         SUB     H               
697D: E4         ???                     
697E: 1A         LD      A,(DE)          
697F: F2         ???                     
6980: 00         NOP                     
6981: FF         RST     0X38            
6982: 00         NOP                     
6983: 80         ADD     A,B             
6984: 3F         CCF                     
6985: 83         ADD     A,E             
6986: 3F         CCF                     
6987: 82         ADD     A,D             
6988: 3F         CCF                     
6989: BE         CP      (HL)            
698A: 3F         CCF                     
698B: A2         AND     D               
698C: 3F         CCF                     
698D: A2         AND     D               
698E: 3F         CCF                     
698F: A2         AND     D               
6990: 3F         CCF                     
6991: FF         RST     0X38            
6992: 3F         CCF                     
6993: 21 FF E1   LD      HL,$E1FF        
6996: FF         RST     0X38            
6997: 21 FF 21   LD      HL,$21FF        
699A: FF         RST     0X38            
699B: 21 E1 21   LD      HL,$21E1        
699E: FF         RST     0X38            
699F: 3F         CCF                     
69A0: 3E A2      LD      A,$A2           
69A2: 3F         CCF                     
69A3: A3         AND     E               
69A4: 23         INC     HL              
69A5: A3         AND     E               
69A6: 3F         CCF                     
69A7: BF         CP      A               
69A8: 3F         CCF                     
69A9: BF         CP      A               
69AA: 3F         CCF                     
69AB: 80         ADD     A,B             
69AC: 00         NOP                     
69AD: 80         ADD     A,B             
69AE: 00         NOP                     
69AF: FF         RST     0X38            
69B0: 3F         CCF                     
69B1: 3F         CCF                     
69B2: FF         RST     0X38            
69B3: FF         RST     0X38            
69B4: FF         RST     0X38            
69B5: FF         RST     0X38            
69B6: FF         RST     0X38            
69B7: FF         RST     0X38            
69B8: FF         RST     0X38            
69B9: FF         RST     0X38            
69BA: FE 01      CP      $01             
69BC: 00         NOP                     
69BD: 01 00 FF   LD      BC,$FF00        
69C0: B5         OR      L               
69C1: 96         SUB     (HL)            
69C2: EC         ???                     
69C3: EF         RST     0X28            
69C4: 0C         INC     C               
69C5: 0B         DEC     BC              
69C6: 0E 09      LD      C,$09           
69C8: 3B         DEC     SP              
69C9: 3C         INC     A               
69CA: 47         LD      B,A             
69CB: 44         LD      B,H             
69CC: BD         CP      L               
69CD: 9E         SBC     (HL)            
69CE: A3         AND     E               
69CF: BE         CP      (HL)            
69D0: AD         XOR     L               
69D1: 69         LD      L,C             
69D2: 37         SCF                     
69D3: F7         RST     0X30            
69D4: 30 D0      JR      NC,$69A6        
69D6: 70         LD      (HL),B          
69D7: 90         SUB     B               
69D8: DC 3C E2   CALL    C,$E23C         
69DB: 22         LD      (HLI),A         
69DC: BD         CP      L               
69DD: 79         LD      A,C             
69DE: CD 7D A7   CALL    $A77D           
69E1: BA         CP      D               
69E2: A5         AND     L               
69E3: BB         CP      E               
69E4: A3         AND     E               
69E5: BC         CP      H               
69E6: DF         RST     0X18            
69E7: 9F         SBC     A               
69E8: A0         AND     B               
69E9: C0         RET     NZ              
69EA: 80         ADD     A,B             
69EB: FF         RST     0X38            
69EC: 40         LD      B,B             
69ED: 7F         LD      A,A             
69EE: 3F         CCF                     
69EF: 3F         CCF                     
69F0: E5         PUSH    HL              
69F1: 5D         LD      E,L             
69F2: A5         AND     L               
69F3: DD         ???                     
69F4: C5         PUSH    BC              
69F5: 3D         DEC     A               
69F6: FB         EI                      
69F7: F9         LD      SP,HL           
69F8: 05         DEC     B               
69F9: 03         INC     BC              
69FA: 01 FF 02   LD      BC,$02FF        
69FD: FE FC      CP      $FC             
69FF: FC         ???                     
6A00: 3C         INC     A               
6A01: 00         NOP                     
6A02: 46         LD      B,(HL)          
6A03: 00         NOP                     
6A04: E2         LDFF00  (C),A           
6A05: 00         NOP                     
6A06: F2         ???                     
6A07: 00         NOP                     
6A08: FA 00 F8   LD      A,($F800)       
6A0B: 00         NOP                     
6A0C: FD         ???                     
6A0D: 00         NOP                     
6A0E: 7D         LD      A,L             
6A0F: 00         NOP                     
6A10: 00         NOP                     
6A11: 00         NOP                     
6A12: 73         LD      (HL),E          
6A13: 00         NOP                     
6A14: CF         RST     0X08            
6A15: 00         NOP                     
6A16: BF         CP      A               
6A17: 00         NOP                     
6A18: 7F         LD      A,A             
6A19: 00         NOP                     
6A1A: FF         RST     0X38            
6A1B: 00         NOP                     
6A1C: FF         RST     0X38            
6A1D: 00         NOP                     
6A1E: FF         RST     0X38            
6A1F: 00         NOP                     
6A20: 7B         LD      A,E             
6A21: 00         NOP                     
6A22: 77         LD      (HL),A          
6A23: 00         NOP                     
6A24: 37         SCF                     
6A25: 00         NOP                     
6A26: 2F         CPL                     
6A27: 00         NOP                     
6A28: 2F         CPL                     
6A29: 00         NOP                     
6A2A: 1F         RRA                     
6A2B: 00         NOP                     
6A2C: 9F         SBC     A               
6A2D: 00         NOP                     
6A2E: 9F         SBC     A               
6A2F: 00         NOP                     
6A30: FF         RST     0X38            
6A31: 00         NOP                     
6A32: FF         RST     0X38            
6A33: 00         NOP                     
6A34: FF         RST     0X38            
6A35: 00         NOP                     
6A36: FF         RST     0X38            
6A37: 00         NOP                     
6A38: FF         RST     0X38            
6A39: 00         NOP                     
6A3A: FE 00      CP      $00             
6A3C: FE 00      CP      $00             
6A3E: FE 00      CP      $00             
6A40: 7F         LD      A,A             
6A41: 00         NOP                     
6A42: FF         RST     0X38            
6A43: 00         NOP                     
6A44: FF         RST     0X38            
6A45: 00         NOP                     
6A46: FF         RST     0X38            
6A47: 00         NOP                     
6A48: FC         ???                     
6A49: 00         NOP                     
6A4A: F3         DI                      
6A4B: 00         NOP                     
6A4C: EF         RST     0X28            
6A4D: 00         NOP                     
6A4E: DF         RST     0X18            
6A4F: 00         NOP                     
6A50: C3 00 F9   JP      $F900           
6A53: 00         NOP                     
6A54: FC         ???                     
6A55: 00         NOP                     
6A56: FE 00      CP      $00             
6A58: 3E 00      LD      A,$00           
6A5A: BE         CP      (HL)            
6A5B: 00         NOP                     
6A5C: BF         CP      A               
6A5D: 00         NOP                     
6A5E: BF         CP      A               
6A5F: 00         NOP                     
6A60: BF         CP      A               
6A61: 00         NOP                     
6A62: BF         CP      A               
6A63: 00         NOP                     
6A64: 7F         LD      A,A             
6A65: 00         NOP                     
6A66: 7F         LD      A,A             
6A67: 00         NOP                     
6A68: 7E         LD      A,(HL)          
6A69: 00         NOP                     
6A6A: FE 00      CP      $00             
6A6C: FE 00      CP      $00             
6A6E: FC         ???                     
6A6F: 00         NOP                     
6A70: 7F         LD      A,A             
6A71: 00         NOP                     
6A72: 7F         LD      A,A             
6A73: 00         NOP                     
6A74: 7F         LD      A,A             
6A75: 00         NOP                     
6A76: 7F         LD      A,A             
6A77: 00         NOP                     
6A78: FF         RST     0X38            
6A79: 00         NOP                     
6A7A: 7F         LD      A,A             
6A7B: 00         NOP                     
6A7C: 3E 00      LD      A,$00           
6A7E: 3E 00      LD      A,$00           
6A80: 3F         CCF                     
6A81: 00         NOP                     
6A82: BF         CP      A               
6A83: 00         NOP                     
6A84: BF         CP      A               
6A85: 00         NOP                     
6A86: 7F         LD      A,A             
6A87: 00         NOP                     
6A88: 7F         LD      A,A             
6A89: 00         NOP                     
6A8A: 7F         LD      A,A             
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
6A98: F8 00      LDHL    SP,$00          
6A9A: F0 00      LD      A,($00)         
6A9C: F0 00      LD      A,($00)         
6A9E: F1         POP     AF              
6A9F: 00         NOP                     
6AA0: FF         RST     0X38            
6AA1: 00         NOP                     
6AA2: FF         RST     0X38            
6AA3: 00         NOP                     
6AA4: FF         RST     0X38            
6AA5: 00         NOP                     
6AA6: FF         RST     0X38            
6AA7: 00         NOP                     
6AA8: FF         RST     0X38            
6AA9: 00         NOP                     
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
6AB6: FE 00      CP      $00             
6AB8: FC         ???                     
6AB9: 00         NOP                     
6ABA: F9         LD      SP,HL           
6ABB: 00         NOP                     
6ABC: E1         POP     HL              
6ABD: 00         NOP                     
6ABE: 9E         SBC     (HL)            
6ABF: 00         NOP                     
6AC0: FA 00 F2   LD      A,($F200)       
6AC3: 00         NOP                     
6AC4: EA 00 F9   LD      ($F900),A       
6AC7: 00         NOP                     
6AC8: F3         DI                      
6AC9: 00         NOP                     
6ACA: E7         RST     0X20            
6ACB: 00         NOP                     
6ACC: EF         RST     0X28            
6ACD: 00         NOP                     
6ACE: CF         RST     0X08            
6ACF: 00         NOP                     
6AD0: 3C         INC     A               
6AD1: 00         NOP                     
6AD2: 3C         INC     A               
6AD3: 00         NOP                     
6AD4: 78         LD      A,B             
6AD5: 00         NOP                     
6AD6: F8 00      LDHL    SP,$00          
6AD8: FC         ???                     
6AD9: 00         NOP                     
6ADA: FC         ???                     
6ADB: 00         NOP                     
6ADC: FE 00      CP      $00             
6ADE: FE 00      CP      $00             
6AE0: DF         RST     0X18            
6AE1: 00         NOP                     
6AE2: 9F         SBC     A               
6AE3: 00         NOP                     
6AE4: 5E         LD      E,(HL)          
6AE5: 00         NOP                     
6AE6: 59         LD      E,C             
6AE7: 00         NOP                     
6AE8: 41         LD      B,C             
6AE9: 00         NOP                     
6AEA: 33         INC     SP              
6AEB: 00         NOP                     
6AEC: 9E         SBC     (HL)            
6AED: 00         NOP                     
6AEE: C0         RET     NZ              
6AEF: 00         NOP                     
6AF0: FE 00      CP      $00             
6AF2: BE         CP      (HL)            
6AF3: 00         NOP                     
6AF4: 3F         CCF                     
6AF5: 00         NOP                     
6AF6: 5F         LD      E,A             
6AF7: 00         NOP                     
6AF8: 4F         LD      C,A             
6AF9: 00         NOP                     
6AFA: 4E         LD      C,(HL)          
6AFB: 00         NOP                     
6AFC: 62         LD      H,D             
6AFD: 00         NOP                     
6AFE: 3C         INC     A               
6AFF: 00         NOP                     
6B00: 83         ADD     A,E             
6B01: 00         NOP                     
6B02: 23         INC     HL              
6B03: 00         NOP                     
6B04: 00         NOP                     
6B05: 00         NOP                     
6B06: 00         NOP                     
6B07: 00         NOP                     
6B08: 30 00      JR      NC,$6B0A        
6B0A: 30 00      JR      NC,$6B0C        
6B0C: 01 00 01   LD      BC,$0100        
6B0F: 00         NOP                     
6B10: 07         RLCA                    
6B11: 00         NOP                     
6B12: 0E 00      LD      C,$00           
6B14: 1C         INC     E               
6B15: 00         NOP                     
6B16: 58         LD      E,B             
6B17: 00         NOP                     
6B18: 18 00      JR      $6B1A           
6B1A: 18 00      JR      $6B1C           
6B1C: 98         SBC     B               
6B1D: 00         NOP                     
6B1E: 99         SBC     C               
6B1F: 00         NOP                     
6B20: 40         LD      B,B             
6B21: 00         NOP                     
6B22: 00         NOP                     
6B23: 00         NOP                     
6B24: 00         NOP                     
6B25: 00         NOP                     
6B26: 3F         CCF                     
6B27: 00         NOP                     
6B28: 7F         LD      A,A             
6B29: 00         NOP                     
6B2A: E0 00      LDFF00  ($00),A         
6B2C: C2 00 80   JP      NZ,$8000        
6B2F: 00         NOP                     
6B30: 38 00      JR      C,$6B32         
6B32: 70         LD      (HL),B          
6B33: 00         NOP                     
6B34: E0 00      LDFF00  ($00),A         
6B36: C0         RET     NZ              
6B37: 00         NOP                     
6B38: 8C         ADC     A,H             
6B39: 00         NOP                     
6B3A: 0C         INC     C               
6B3B: 00         NOP                     
6B3C: 01 00 03   LD      BC,$0300        
6B3F: 00         NOP                     
6B40: 00         NOP                     
6B41: 00         NOP                     
6B42: 00         NOP                     
6B43: 00         NOP                     
6B44: 00         NOP                     
6B45: 00         NOP                     
6B46: 07         RLCA                    
6B47: 07         RLCA                    
6B48: 0C         INC     C               
6B49: 08 1B 10   LD      ($101B),SP      
6B4C: 17         RLA                     
6B4D: 10 17      STOP    $17             
6B4F: 10 00      STOP    $00             
6B51: 00         NOP                     
6B52: 00         NOP                     
6B53: 00         NOP                     
6B54: 00         NOP                     
6B55: 00         NOP                     
6B56: E0 E0      LDFF00  ($E0),A         
6B58: 30 10      JR      NC,$6B6A        
6B5A: D8         RET     C               
6B5B: 08 E8 08   LD      ($08E8),SP      
6B5E: E8 08      ADD     SP,$08          
6B60: 17         RLA                     
6B61: 10 1B      STOP    $1B             
6B63: 10 14      STOP    $14             
6B65: 18 08      JR      $6B6F           
6B67: 0F         RRCA                    
6B68: 07         RLCA                    
6B69: 07         RLCA                    
6B6A: 00         NOP                     
6B6B: 00         NOP                     
6B6C: 00         NOP                     
6B6D: 00         NOP                     
6B6E: 00         NOP                     
6B6F: 00         NOP                     
6B70: E8 08      ADD     SP,$08          
6B72: D8         RET     C               
6B73: 08 28 18   LD      ($1828),SP      
6B76: 10 F0      STOP    $F0             
6B78: E0 E0      LDFF00  ($E0),A         
6B7A: 00         NOP                     
6B7B: 00         NOP                     
6B7C: 00         NOP                     
6B7D: 00         NOP                     
6B7E: 00         NOP                     
6B7F: 00         NOP                     
6B80: 00         NOP                     
6B81: 00         NOP                     
6B82: 3F         CCF                     
6B83: 00         NOP                     
6B84: 7F         LD      A,A             
6B85: 00         NOP                     
6B86: 7F         LD      A,A             
6B87: 00         NOP                     
6B88: 7E         LD      A,(HL)          
6B89: 01 7C 02   LD      BC,$027C        
6B8C: 79         LD      A,C             
6B8D: 04         INC     B               
6B8E: 03         INC     BC              
6B8F: 78         LD      A,B             
6B90: 00         NOP                     
6B91: 00         NOP                     
6B92: 7C         LD      A,H             
6B93: 00         NOP                     
6B94: 7E         LD      A,(HL)          
6B95: 00         NOP                     
6B96: 7E         LD      A,(HL)          
6B97: 00         NOP                     
6B98: 1E 60      LD      E,$60           
6B9A: 0E 10      LD      C,$10           
6B9C: E0 0E      LDFF00  ($0E),A         
6B9E: F0 00      LD      A,($00)         
6BA0: 03         INC     BC              
6BA1: 00         NOP                     
6BA2: 79         LD      A,C             
6BA3: 02         LD      (BC),A          
6BA4: 7C         LD      A,H             
6BA5: 01 7E 00   LD      BC,$007E        
6BA8: 7E         LD      A,(HL)          
6BA9: 00         NOP                     
6BAA: 3E 40      LD      A,$40           
6BAC: 00         NOP                     
6BAD: 3E 00      LD      A,$00           
6BAF: 00         NOP                     
6BB0: E6 10      AND     $10             
6BB2: CE 20      ADC     $20             
6BB4: 1E C0      LD      E,$C0           
6BB6: 3E 00      LD      A,$00           
6BB8: FE 00      CP      $00             
6BBA: FC         ???                     
6BBB: 02         LD      (BC),A          
6BBC: 00         NOP                     
6BBD: FC         ???                     
6BBE: 00         NOP                     
6BBF: 00         NOP                     
6BC0: 00         NOP                     
6BC1: 01 02 01   LD      BC,$0102        
6BC4: 8C         ADC     A,H             
6BC5: 03         INC     BC              
6BC6: 52         LD      D,D             
6BC7: 8D         ADC     A,L             
6BC8: 69         LD      L,C             
6BC9: 90         SUB     B               
6BCA: 89         ADC     A,C             
6BCB: 70         LD      (HL),B          
6BCC: 36 49      LD      (HL),$49        
6BCE: 28 47      JR      Z,$6C17         
6BD0: 07         RLCA                    
6BD1: 00         NOP                     
6BD2: 88         ADC     A,B             
6BD3: 07         RLCA                    
6BD4: 90         SUB     B               
6BD5: 0C         INC     C               
6BD6: D0         RET     NC              
6BD7: 08 70 88   LD      ($8870),SP      
6BDA: 00         NOP                     
6BDB: F8 68      LDHL    SP,$68          
6BDD: 90         SUB     B               
6BDE: A9         XOR     C               
6BDF: 10 45      STOP    $45             
6BE1: 22         LD      (HLI),A         
6BE2: 45         LD      B,L             
6BE3: 22         LD      (HLI),A         
6BE4: 5D         LD      E,L             
6BE5: 22         LD      (HLI),A         
6BE6: 40         LD      B,B             
6BE7: 3F         CCF                     
6BE8: 1F         RRA                     
6BE9: 60         LD      H,B             
6BEA: A1         AND     C               
6BEB: 40         LD      B,B             
6BEC: 81         ADD     A,C             
6BED: 40         LD      B,B             
6BEE: 02         LD      (BC),A          
6BEF: 81         ADD     A,C             
6BF0: AC         XOR     H               
6BF1: 10 46      STOP    $46             
6BF3: 38 99      JR      C,$6B8E         
6BF5: 66         LD      H,(HL)          
6BF6: 20 C0      JR      NZ,$6BB8        
6BF8: 40         LD      B,B             
6BF9: 80         ADD     A,B             
6BFA: 46         LD      B,(HL)          
6BFB: 80         ADD     A,B             
6BFC: 46         LD      B,(HL)          
6BFD: 80         ADD     A,B             
6BFE: 80         ADD     A,B             
6BFF: 00         NOP                     
6C00: 00         NOP                     
6C01: 00         NOP                     
6C02: 7F         LD      A,A             
6C03: 00         NOP                     
6C04: 78         LD      A,B             
6C05: 3F         CCF                     
6C06: 7C         LD      A,H             
6C07: 3F         CCF                     
6C08: 5E         LD      E,(HL)          
6C09: 3F         CCF                     
6C0A: 4F         LD      C,A             
6C0B: 3F         CCF                     
6C0C: 47         LD      B,A             
6C0D: 3F         CCF                     
6C0E: 47         LD      B,A             
6C0F: 3F         CCF                     
6C10: 00         NOP                     
6C11: 00         NOP                     
6C12: FE 00      CP      $00             
6C14: 1E FC      LD      E,$FC           
6C16: 3E FC      LD      A,$FC           
6C18: 7A         LD      A,D             
6C19: FC         ???                     
6C1A: F2         ???                     
6C1B: FC         ???                     
6C1C: E2         LDFF00  (C),A           
6C1D: FC         ???                     
6C1E: E2         LDFF00  (C),A           
6C1F: FC         ???                     
6C20: 47         LD      B,A             
6C21: 3F         CCF                     
6C22: 47         LD      B,A             
6C23: 3F         CCF                     
6C24: 4F         LD      C,A             
6C25: 3F         CCF                     
6C26: 5E         LD      E,(HL)          
6C27: 3F         CCF                     
6C28: 7C         LD      A,H             
6C29: 3F         CCF                     
6C2A: 78         LD      A,B             
6C2B: 3F         CCF                     
6C2C: 7F         LD      A,A             
6C2D: 00         NOP                     
6C2E: 00         NOP                     
6C2F: 00         NOP                     
6C30: E2         LDFF00  (C),A           
6C31: FC         ???                     
6C32: E2         LDFF00  (C),A           
6C33: FC         ???                     
6C34: F2         ???                     
6C35: FC         ???                     
6C36: 7A         LD      A,D             
6C37: FC         ???                     
6C38: 3E FC      LD      A,$FC           
6C3A: 1E FC      LD      E,$FC           
6C3C: FE 00      CP      $00             
6C3E: 00         NOP                     
6C3F: 00         NOP                     
6C40: 26 1D      LD      H,$1D           
6C42: 34         INC     (HL)            
6C43: 0F         RRCA                    
6C44: D7         RST     0X10            
6C45: 0F         RRCA                    
6C46: 6E         LD      L,(HL)          
6C47: 85         ADD     A,L             
6C48: 16 E5      LD      D,$E5           
6C4A: FE F9      CP      $F9             
6C4C: 05         DEC     B               
6C4D: F8 02      LDHL    SP,$02          
6C4F: FC         ???                     
6C50: 64         LD      H,H             
6C51: B8         CP      B               
6C52: 6C         LD      L,H             
6C53: B0         OR      B               
6C54: EB         ???                     
6C55: F0 76      LD      A,($76)         
6C57: A1         AND     C               
6C58: 68         LD      L,B             
6C59: A7         AND     A               
6C5A: 7F         LD      A,A             
6C5B: 9F         SBC     A               
6C5C: BE         CP      (HL)            
6C5D: 05         DEC     B               
6C5E: 44         LD      B,H             
6C5F: 3F         CCF                     
6C60: 02         LD      (BC),A          
6C61: FC         ???                     
6C62: F5         PUSH    AF              
6C63: 08 FE F9   LD      ($F9FE),SP      
6C66: 16 E5      LD      D,$E5           
6C68: 6E         LD      L,(HL)          
6C69: 85         ADD     A,L             
6C6A: D6 0D      SUB     $0D             
6C6C: 36 0D      LD      (HL),$0D        
6C6E: 24         INC     H               
6C6F: 1F         RRA                     
6C70: 44         LD      B,H             
6C71: 3F         CCF                     
6C72: BF         CP      A               
6C73: 04         INC     B               
6C74: 7F         LD      A,A             
6C75: 9F         SBC     A               
6C76: 68         LD      L,B             
6C77: A7         AND     A               
6C78: 76         HALT                    
6C79: A1         AND     C               
6C7A: 6B         LD      L,E             
6C7B: B0         OR      B               
6C7C: 6C         LD      L,H             
6C7D: B0         OR      B               
6C7E: 24         INC     H               
6C7F: F8 00      LDHL    SP,$00          
6C81: 00         NOP                     
6C82: BF         CP      A               
6C83: 60         LD      H,B             
6C84: 32         LD      (HLD),A         
6C85: ED         ???                     
6C86: 20 FF      JR      NZ,$6C87        
6C88: 20 FF      JR      NZ,$6C89        
6C8A: FF         RST     0X38            
6C8B: FF         RST     0X38            
6C8C: F7         RST     0X30            
6C8D: 0C         INC     C               
6C8E: 04         INC     B               
6C8F: FF         RST     0X38            
6C90: FF         RST     0X38            
6C91: FF         RST     0X38            
6C92: FF         RST     0X38            
6C93: FF         RST     0X38            
6C94: 04         INC     B               
6C95: FF         RST     0X38            
6C96: FF         RST     0X38            
6C97: FF         RST     0X38            
6C98: 20 FF      JR      NZ,$6C99        
6C9A: BF         CP      A               
6C9B: 60         LD      H,B             
6C9C: FF         RST     0X38            
6C9D: FF         RST     0X38            
6C9E: 04         INC     B               
6C9F: FF         RST     0X38            
6CA0: 46         LD      B,(HL)          
6CA1: 3D         DEC     A               
6CA2: 66         LD      H,(HL)          
6CA3: 1D         DEC     E               
6CA4: 47         LD      B,A             
6CA5: 3F         CCF                     
6CA6: 44         LD      B,H             
6CA7: 3F         CCF                     
6CA8: 66         LD      H,(HL)          
6CA9: 1D         DEC     E               
6CAA: 7E         LD      A,(HL)          
6CAB: 7D         LD      A,L             
6CAC: 06 7D      LD      B,$7D           
6CAE: 46         LD      B,(HL)          
6CAF: 3D         DEC     A               
6CB0: 6B         LD      L,E             
6CB1: DF         RST     0X18            
6CB2: 6B         LD      L,E             
6CB3: DF         RST     0X18            
6CB4: EF         RST     0X28            
6CB5: DF         RST     0X18            
6CB6: 6B         LD      L,E             
6CB7: DF         RST     0X18            
6CB8: 6B         LD      L,E             
6CB9: DF         RST     0X18            
6CBA: 7B         LD      A,E             
6CBB: FF         RST     0X38            
6CBC: 4B         LD      C,E             
6CBD: FF         RST     0X38            
6CBE: 6B         LD      L,E             
6CBF: DF         RST     0X18            
6CC0: 81         ADD     A,C             
6CC1: 00         NOP                     
6CC2: FE 81      CP      $81             
6CC4: 92         SUB     D               
6CC5: ED         ???                     
6CC6: 80         ADD     A,B             
6CC7: FF         RST     0X38            
6CC8: E3         ???                     
6CC9: FF         RST     0X38            
6CCA: FF         RST     0X38            
6CCB: FF         RST     0X38            
6CCC: FF         RST     0X38            
6CCD: 3C         INC     A               
6CCE: 3C         INC     A               
6CCF: DF         RST     0X18            
6CD0: FF         RST     0X38            
6CD1: FF         RST     0X38            
6CD2: FF         RST     0X38            
6CD3: FF         RST     0X38            
6CD4: C7         RST     0X00            
6CD5: FF         RST     0X38            
6CD6: FF         RST     0X38            
6CD7: FF         RST     0X38            
6CD8: E6 DF      AND     $DF             
6CDA: FF         RST     0X38            
6CDB: 64         LD      H,H             
6CDC: FF         RST     0X38            
6CDD: FF         RST     0X38            
6CDE: 3C         INC     A               
6CDF: FF         RST     0X38            
6CE0: FE 7D      CP      $7D             
6CE2: 4E         LD      C,(HL)          
6CE3: 3D         DEC     A               
6CE4: 4F         LD      C,A             
6CE5: 3E 67      LD      A,$67           
6CE7: 1F         RRA                     
6CE8: 47         LD      B,A             
6CE9: 3F         CCF                     
6CEA: 47         LD      B,A             
6CEB: 3F         CCF                     
6CEC: 6E         LD      L,(HL)          
6CED: 1D         DEC     E               
6CEE: 8E         ADC     A,(HL)          
6CEF: 7D         LD      A,L             
6CF0: 6F         LD      L,A             
6CF1: DF         RST     0X18            
6CF2: 7F         LD      A,A             
6CF3: DF         RST     0X18            
6CF4: FF         RST     0X38            
6CF5: FF         RST     0X38            
6CF6: EB         ???                     
6CF7: DF         RST     0X18            
6CF8: EB         ???                     
6CF9: DF         RST     0X18            
6CFA: FB         EI                      
6CFB: EF         RST     0X28            
6CFC: 7F         LD      A,A             
6CFD: FF         RST     0X38            
6CFE: 7F         LD      A,A             
6CFF: DF         RST     0X18            
6D00: C4 FF FF   CALL    NZ,$FFFF        
6D03: FF         RST     0X38            
6D04: FF         RST     0X38            
6D05: F0 70      LD      A,($70)         
6D07: FF         RST     0X38            
6D08: 7F         LD      A,A             
6D09: DF         RST     0X18            
6D0A: 6C         LD      L,H             
6D0B: DF         RST     0X18            
6D0C: 6F         LD      L,A             
6D0D: DF         RST     0X18            
6D0E: 6B         LD      L,E             
6D0F: DF         RST     0X18            
6D10: 07         RLCA                    
6D11: FF         RST     0X38            
6D12: FF         RST     0X38            
6D13: FF         RST     0X38            
6D14: FF         RST     0X38            
6D15: 0F         RRCA                    
6D16: 0E FF      LD      C,$FF           
6D18: FE FB      CP      $FB             
6D1A: 36 FB      LD      (HL),$FB        
6D1C: F6 FB      OR      $FB             
6D1E: D6 FB      SUB     $FB             
6D20: 6B         LD      L,E             
6D21: DF         RST     0X18            
6D22: 6B         LD      L,E             
6D23: DF         RST     0X18            
6D24: 6E         LD      L,(HL)          
6D25: DF         RST     0X18            
6D26: 6F         LD      L,A             
6D27: DF         RST     0X18            
6D28: 78         LD      A,B             
6D29: DF         RST     0X18            
6D2A: 7F         LD      A,A             
6D2B: F0 FF      LD      A,($FF)         
6D2D: FF         RST     0X38            
6D2E: C4 FF D6   CALL    NZ,$D6FF        
6D31: FB         EI                      
6D32: D6 FB      SUB     $FB             
6D34: 76         HALT                    
6D35: FB         EI                      
6D36: F6 FB      OR      $FB             
6D38: 1E FB      LD      E,$FB           
6D3A: FE 0F      CP      $0F             
6D3C: FF         RST     0X38            
6D3D: FF         RST     0X38            
6D3E: 07         RLCA                    
6D3F: FF         RST     0X38            
6D40: 6B         LD      L,E             
6D41: 5F         LD      E,A             
6D42: AB         XOR     E               
6D43: DF         RST     0X18            
6D44: CB 1F      SET     1,E             
6D46: 1B         DEC     DE              
6D47: EF         RST     0X28            
6D48: FB         EI                      
6D49: F7         RST     0X30            
6D4A: 07         RLCA                    
6D4B: FB         EI                      
6D4C: FF         RST     0X38            
6D4D: FF         RST     0X38            
6D4E: FF         RST     0X38            
6D4F: FF         RST     0X38            
6D50: D6 FA      SUB     $FA             
6D52: D5         PUSH    DE              
6D53: FB         EI                      
6D54: D3         ???                     
6D55: F8 D8      LDHL    SP,$D8          
6D57: F7         RST     0X30            
6D58: DF         RST     0X18            
6D59: EF         RST     0X28            
6D5A: E0 DF      LDFF00  ($DF),A         
6D5C: FF         RST     0X38            
6D5D: FF         RST     0X38            
6D5E: FF         RST     0X38            
6D5F: FF         RST     0X38            
6D60: FF         RST     0X38            
6D61: FF         RST     0X38            
6D62: FF         RST     0X38            
6D63: FF         RST     0X38            
6D64: 07         RLCA                    
6D65: FB         EI                      
6D66: FB         EI                      
6D67: F7         RST     0X30            
6D68: 1B         DEC     DE              
6D69: EF         RST     0X28            
6D6A: CB 1F      SET     1,E             
6D6C: AB         XOR     E               
6D6D: DF         RST     0X18            
6D6E: 6B         LD      L,E             
6D6F: 5F         LD      E,A             
6D70: FF         RST     0X38            
6D71: FF         RST     0X38            
6D72: FF         RST     0X38            
6D73: FF         RST     0X38            
6D74: E0 DF      LDFF00  ($DF),A         
6D76: DF         RST     0X18            
6D77: EF         RST     0X28            
6D78: D8         RET     C               
6D79: F7         RST     0X30            
6D7A: D3         ???                     
6D7B: F8 D5      LDHL    SP,$D5          
6D7D: FB         EI                      
6D7E: D6 FA      SUB     $FA             
6D80: 04         INC     B               
6D81: FF         RST     0X38            
6D82: FF         RST     0X38            
6D83: FF         RST     0X38            
6D84: BF         CP      A               
6D85: 60         LD      H,B             
6D86: 20 FF      JR      NZ,$6D87        
6D88: FF         RST     0X38            
6D89: FF         RST     0X38            
6D8A: 04         INC     B               
6D8B: FF         RST     0X38            
6D8C: FF         RST     0X38            
6D8D: FF         RST     0X38            
6D8E: FF         RST     0X38            
6D8F: FF         RST     0X38            
6D90: 04         INC     B               
6D91: FF         RST     0X38            
6D92: F7         RST     0X30            
6D93: 0C         INC     C               
6D94: FF         RST     0X38            
6D95: FF         RST     0X38            
6D96: 20 FF      JR      NZ,$6D97        
6D98: 20 FF      JR      NZ,$6D99        
6D9A: 32         LD      (HLD),A         
6D9B: ED         ???                     
6D9C: BF         CP      A               
6D9D: 60         LD      H,B             
6D9E: 00         NOP                     
6D9F: 00         NOP                     
6DA0: D6 FB      SUB     $FB             
6DA2: D6 FB      SUB     $FB             
6DA4: F7         RST     0X30            
6DA5: FB         EI                      
6DA6: D6 FB      SUB     $FB             
6DA8: D6 FB      SUB     $FB             
6DAA: DE FF      SBC     $FF             
6DAC: D2 FF D6   JP      NC,$D6FF        
6DAF: FB         EI                      
6DB0: 62         LD      H,D             
6DB1: BC         CP      H               
6DB2: 66         LD      H,(HL)          
6DB3: B8         CP      B               
6DB4: E2         LDFF00  (C),A           
6DB5: FC         ???                     
6DB6: 22         LD      (HLI),A         
6DB7: FC         ???                     
6DB8: 66         LD      H,(HL)          
6DB9: B8         CP      B               
6DBA: 7E         LD      A,(HL)          
6DBB: BE         CP      (HL)            
6DBC: 60         LD      H,B             
6DBD: BE         CP      (HL)            
6DBE: 62         LD      H,D             
6DBF: BC         CP      H               
6DC0: 3C         INC     A               
6DC1: FF         RST     0X38            
6DC2: FF         RST     0X38            
6DC3: FF         RST     0X38            
6DC4: FF         RST     0X38            
6DC5: 64         LD      H,H             
6DC6: E6 DF      AND     $DF             
6DC8: FF         RST     0X38            
6DC9: FF         RST     0X38            
6DCA: C7         RST     0X00            
6DCB: FF         RST     0X38            
6DCC: FF         RST     0X38            
6DCD: FF         RST     0X38            
6DCE: FF         RST     0X38            
6DCF: FF         RST     0X38            
6DD0: 3C         INC     A               
6DD1: DF         RST     0X18            
6DD2: FF         RST     0X38            
6DD3: 3C         INC     A               
6DD4: FF         RST     0X38            
6DD5: FF         RST     0X38            
6DD6: E3         ???                     
6DD7: FF         RST     0X38            
6DD8: 80         ADD     A,B             
6DD9: FF         RST     0X38            
6DDA: 92         SUB     D               
6DDB: ED         ???                     
6DDC: FE 81      CP      $81             
6DDE: 81         ADD     A,C             
6DDF: 00         NOP                     
6DE0: F6 FB      OR      $FB             
6DE2: FE FB      CP      $FB             
6DE4: FF         RST     0X38            
6DE5: FF         RST     0X38            
6DE6: D7         RST     0X10            
6DE7: FB         EI                      
6DE8: D7         RST     0X10            
6DE9: FB         EI                      
6DEA: DF         RST     0X18            
6DEB: F7         RST     0X30            
6DEC: FE FF      CP      $FF             
6DEE: FE FB      CP      $FB             
6DF0: 71         LD      (HL),C          
6DF1: BE         CP      (HL)            
6DF2: 76         HALT                    
6DF3: B8         CP      B               
6DF4: E2         LDFF00  (C),A           
6DF5: FC         ???                     
6DF6: E2         LDFF00  (C),A           
6DF7: FC         ???                     
6DF8: E6 F8      AND     $F8             
6DFA: F2         ???                     
6DFB: 7C         LD      A,H             
6DFC: 72         LD      (HL),D          
6DFD: BC         CP      H               
6DFE: 7F         LD      A,A             
6DFF: BE         CP      (HL)            
6E00: 00         NOP                     
6E01: 00         NOP                     
6E02: 1F         RRA                     
6E03: 00         NOP                     
6E04: 2C         INC     L               
6E05: 1F         RRA                     
6E06: 5F         LD      E,A             
6E07: 3F         CCF                     
6E08: 7C         LD      A,H             
6E09: 3F         CCF                     
6E0A: 5E         LD      E,(HL)          
6E0B: 3F         CCF                     
6E0C: 57         LD      D,A             
6E0D: 3F         CCF                     
6E0E: 53         LD      D,E             
6E0F: 3F         CCF                     
6E10: 00         NOP                     
6E11: 00         NOP                     
6E12: F8 00      LDHL    SP,$00          
6E14: 34         INC     (HL)            
6E15: F8 FA      LDHL    SP,$FA          
6E17: FC         ???                     
6E18: 3E FC      LD      A,$FC           
6E1A: 7A         LD      A,D             
6E1B: FC         ???                     
6E1C: EA FC CA   LD      ($CAFC),A       
6E1F: FC         ???                     
6E20: 53         LD      D,E             
6E21: 3F         CCF                     
6E22: 57         LD      D,A             
6E23: 3F         CCF                     
6E24: 5E         LD      E,(HL)          
6E25: 3F         CCF                     
6E26: 7C         LD      A,H             
6E27: 3F         CCF                     
6E28: 5F         LD      E,A             
6E29: 3F         CCF                     
6E2A: 2C         INC     L               
6E2B: 1F         RRA                     
6E2C: 1F         RRA                     
6E2D: 00         NOP                     
6E2E: 00         NOP                     
6E2F: 00         NOP                     
6E30: CA FC EA   JP      Z,$EAFC         
6E33: FC         ???                     
6E34: 7A         LD      A,D             
6E35: FC         ???                     
6E36: 3E FC      LD      A,$FC           
6E38: FA FC 34   LD      A,($34FC)       
6E3B: F8 F8      LDHL    SP,$F8          
6E3D: 00         NOP                     
6E3E: 00         NOP                     
6E3F: 00         NOP                     
6E40: 39         ADD     HL,SP           
6E41: 17         RLA                     
6E42: 09         ADD     HL,BC           
6E43: 17         RLA                     
6E44: 83         ADD     A,E             
6E45: 0E 8B      LD      C,$8B           
6E47: C6 D7      ADD     $D7             
6E49: 22         LD      (HLI),A         
6E4A: 0B         DEC     BC              
6E4B: F1         POP     AF              
6E4C: 3D         DEC     A               
6E4D: F9         LD      SP,HL           
6E4E: FF         RST     0X38            
6E4F: C6 9C      ADD     $9C             
6E51: E8 90      ADD     SP,$90          
6E53: E8 C1      ADD     SP,$C1          
6E55: 70         LD      (HL),B          
6E56: D1         POP     DE              
6E57: 63         LD      H,E             
6E58: EB         ???                     
6E59: 44         LD      B,H             
6E5A: D0         RET     NC              
6E5B: 8F         ADC     A,A             
6E5C: BC         CP      H               
6E5D: 9F         SBC     A               
6E5E: FF         RST     0X38            
6E5F: 63         LD      H,E             
6E60: FF         RST     0X38            
6E61: C6 3D      ADD     $3D             
6E63: F9         LD      SP,HL           
6E64: 0B         DEC     BC              
6E65: F1         POP     AF              
6E66: D7         RST     0X10            
6E67: 22         LD      (HLI),A         
6E68: 8B         ADC     A,E             
6E69: C6 83      ADD     $83             
6E6B: 0E 09      LD      C,$09           
6E6D: 17         RLA                     
6E6E: 39         ADD     HL,SP           
6E6F: 17         RLA                     
6E70: FF         RST     0X38            
6E71: 63         LD      H,E             
6E72: BC         CP      H               
6E73: 9F         SBC     A               
6E74: D0         RET     NC              
6E75: 8F         ADC     A,A             
6E76: EB         ???                     
6E77: 44         LD      B,H             
6E78: D1         POP     DE              
6E79: 63         LD      H,E             
6E7A: C1         POP     BC              
6E7B: 70         LD      (HL),B          
6E7C: 90         SUB     B               
6E7D: E8 9C      ADD     SP,$9C          
6E7F: E8 00      ADD     SP,$00          
6E81: 00         NOP                     
6E82: BD         CP      L               
6E83: 7E         LD      A,(HL)          
6E84: 66         LD      H,(HL)          
6E85: C3 C3 81   JP      $81C3           
6E88: C3 3C 00   JP      $003C           
6E8B: FF         RST     0X38            
6E8C: 3C         INC     A               
6E8D: FF         RST     0X38            
6E8E: 66         LD      H,(HL)          
6E8F: FF         RST     0X38            
6E90: FF         RST     0X38            
6E91: FF         RST     0X38            
6E92: 3C         INC     A               
6E93: FF         RST     0X38            
6E94: 81         ADD     A,C             
6E95: FF         RST     0X38            
6E96: DB         ???                     
6E97: E7         RST     0X20            
6E98: 3C         INC     A               
6E99: FF         RST     0X38            
6E9A: 81         ADD     A,C             
6E9B: 7E         LD      A,(HL)          
6E9C: 66         LD      H,(HL)          
6E9D: 99         SBC     C               
6E9E: A5         AND     L               
6E9F: C3 58 37   JP      $3758           
6EA2: 39         ADD     HL,SP           
6EA3: 67         LD      H,A             
6EA4: 63         LD      H,E             
6EA5: 4F         LD      C,A             
6EA6: 42         LD      B,D             
6EA7: 4F         LD      C,A             
6EA8: 42         LD      B,D             
6EA9: 4F         LD      C,A             
6EAA: 63         LD      H,E             
6EAB: 4F         LD      C,A             
6EAC: 39         ADD     HL,SP           
6EAD: 67         LD      H,A             
6EAE: 58         LD      E,B             
6EAF: 37         SCF                     
6EB0: AD         XOR     L               
6EB1: DF         RST     0X18            
6EB2: 49         LD      C,C             
6EB3: BF         CP      A               
6EB4: D3         ???                     
6EB5: 3F         CCF                     
6EB6: 1B         DEC     DE              
6EB7: 77         LD      (HL),A          
6EB8: 1B         DEC     DE              
6EB9: 77         LD      (HL),A          
6EBA: D3         ???                     
6EBB: 3F         CCF                     
6EBC: 49         LD      C,C             
6EBD: BF         CP      A               
6EBE: AD         XOR     L               
6EBF: DF         RST     0X18            
6EC0: 00         NOP                     
6EC1: 00         NOP                     
6EC2: BD         CP      L               
6EC3: 7E         LD      A,(HL)          
6EC4: 66         LD      H,(HL)          
6EC5: C3 83 C3   JP      $C383           
6EC8: C3 FF C7   JP      $C7FF           
6ECB: 7E         LD      A,(HL)          
6ECC: 6E         LD      L,(HL)          
6ECD: FD         ???                     
6ECE: 7F         LD      A,A             
6ECF: FF         RST     0X38            
6ED0: FF         RST     0X38            
6ED1: FF         RST     0X38            
6ED2: BB         CP      E               
6ED3: FF         RST     0X38            
6ED4: 83         ADD     A,E             
6ED5: FF         RST     0X38            
6ED6: FF         RST     0X38            
6ED7: C7         RST     0X00            
6ED8: FC         ???                     
6ED9: FF         RST     0X38            
6EDA: 30 FF      JR      NC,$6EDB        
6EDC: F9         LD      SP,HL           
6EDD: 36 FF      LD      (HL),$FF        
6EDF: F9         LD      SP,HL           
6EE0: 5C         LD      E,H             
6EE1: 3B         DEC     SP              
6EE2: 2F         CPL                     
6EE3: 7F         LD      A,A             
6EE4: 63         LD      H,E             
6EE5: 4F         LD      C,A             
6EE6: 41         LD      B,C             
6EE7: 4F         LD      C,A             
6EE8: 43         LD      B,E             
6EE9: 4F         LD      C,A             
6EEA: 67         LD      H,A             
6EEB: 4F         LD      C,A             
6EEC: 3F         CCF                     
6EED: 7D         LD      A,L             
6EEE: 5D         LD      E,L             
6EEF: 3B         DEC     SP              
6EF0: DF         RST     0X18            
6EF1: BF         CP      A               
6EF2: D9         RETI                    
6EF3: BF         CP      A               
6EF4: FB         EI                      
6EF5: F7         RST     0X30            
6EF6: FB         EI                      
6EF7: F7         RST     0X30            
6EF8: DB         ???                     
6EF9: B7         OR      A               
6EFA: 99         SBC     C               
6EFB: 7F         LD      A,A             
6EFC: 8F         ADC     A,A             
6EFD: 7F         LD      A,A             
6EFE: CF         RST     0X08            
6EFF: BF         CP      A               
6F00: C7         RST     0X00            
6F01: E1         POP     HL              
6F02: E1         POP     HL              
6F03: FE 70      CP      $70             
6F05: FF         RST     0X38            
6F06: 38 7F      JR      C,$6F87         
6F08: 1C         INC     E               
6F09: 7F         LD      A,A             
6F0A: 8F         ADC     A,A             
6F0B: 7F         LD      A,A             
6F0C: 87         ADD     A,A             
6F0D: 7F         LD      A,A             
6F0E: C7         RST     0X00            
6F0F: BF         CP      A               
6F10: E3         ???                     
6F11: 87         ADD     A,A             
6F12: 87         ADD     A,A             
6F13: 7F         LD      A,A             
6F14: 0E FF      LD      C,$FF           
6F16: 1C         INC     E               
6F17: FE 38      CP      $38             
6F19: FE F1      CP      $F1             
6F1B: FE E1      CP      $E1             
6F1D: FE E3      CP      $E3             
6F1F: FD         ???                     
6F20: C7         RST     0X00            
6F21: BF         CP      A               
6F22: 87         ADD     A,A             
6F23: 7F         LD      A,A             
6F24: 8F         ADC     A,A             
6F25: 7F         LD      A,A             
6F26: 1C         INC     E               
6F27: 7F         LD      A,A             
6F28: 38 7F      JR      C,$6FA9         
6F2A: 70         LD      (HL),B          
6F2B: FF         RST     0X38            
6F2C: E1         POP     HL              
6F2D: FE C7      CP      $C7             
6F2F: E1         POP     HL              
6F30: E3         ???                     
6F31: FD         ???                     
6F32: E1         POP     HL              
6F33: FE F1      CP      $F1             
6F35: FE 38      CP      $38             
6F37: FE 1C      CP      $1C             
6F39: FE 0E      CP      $0E             
6F3B: FF         RST     0X38            
6F3C: 87         ADD     A,A             
6F3D: 7F         LD      A,A             
6F3E: E3         ???                     
6F3F: 87         ADD     A,A             
6F40: 4D         LD      C,L             
6F41: BF         CP      A               
6F42: 89         ADC     A,C             
6F43: 3F         CCF                     
6F44: 2B         DEC     HL              
6F45: DF         RST     0X18            
6F46: 1B         DEC     DE              
6F47: EF         RST     0X28            
6F48: FB         EI                      
6F49: F7         RST     0X30            
6F4A: 87         ADD     A,A             
6F4B: FB         EI                      
6F4C: 3F         CCF                     
6F4D: FF         RST     0X38            
6F4E: FF         RST     0X38            
6F4F: FF         RST     0X38            
6F50: B2         OR      D               
6F51: FD         ???                     
6F52: 91         SUB     C               
6F53: FC         ???                     
6F54: D4 FB D8   CALL    NC,$D8FB        
6F57: F7         RST     0X30            
6F58: DF         RST     0X18            
6F59: EF         RST     0X28            
6F5A: E1         POP     HL              
6F5B: DF         RST     0X18            
6F5C: FC         ???                     
6F5D: FF         RST     0X38            
6F5E: FF         RST     0X38            
6F5F: FF         RST     0X38            
6F60: FF         RST     0X38            
6F61: FF         RST     0X38            
6F62: 3F         CCF                     
6F63: FF         RST     0X38            
6F64: 87         ADD     A,A             
6F65: FB         EI                      
6F66: FB         EI                      
6F67: F7         RST     0X30            
6F68: 1B         DEC     DE              
6F69: EF         RST     0X28            
6F6A: 2B         DEC     HL              
6F6B: DF         RST     0X18            
6F6C: 89         ADC     A,C             
6F6D: 3F         CCF                     
6F6E: 4D         LD      C,L             
6F6F: BF         CP      A               
6F70: FF         RST     0X38            
6F71: FF         RST     0X38            
6F72: FC         ???                     
6F73: FF         RST     0X38            
6F74: E1         POP     HL              
6F75: DF         RST     0X18            
6F76: DF         RST     0X18            
6F77: EF         RST     0X28            
6F78: D8         RET     C               
6F79: F7         RST     0X30            
6F7A: D4 FB 91   CALL    NC,$91FB        
6F7D: FC         ???                     
6F7E: B2         OR      D               
6F7F: FD         ???                     
6F80: A5         AND     L               
6F81: C3 66 99   JP      $9966           
6F84: 81         ADD     A,C             
6F85: 7E         LD      A,(HL)          
6F86: 3C         INC     A               
6F87: FF         RST     0X38            
6F88: DB         ???                     
6F89: E7         RST     0X20            
6F8A: 81         ADD     A,C             
6F8B: FF         RST     0X38            
6F8C: 3C         INC     A               
6F8D: FF         RST     0X38            
6F8E: FF         RST     0X38            
6F8F: FF         RST     0X38            
6F90: 66         LD      H,(HL)          
6F91: FF         RST     0X38            
6F92: 3C         INC     A               
6F93: FF         RST     0X38            
6F94: 00         NOP                     
6F95: FF         RST     0X38            
6F96: C3 3C C3   JP      $C33C           
6F99: 81         ADD     A,C             
6F9A: 66         LD      H,(HL)          
6F9B: C3 BD 7E   JP      $7EBD           
6F9E: 00         NOP                     
6F9F: 00         NOP                     
6FA0: B5         OR      L               
6FA1: FB         EI                      
6FA2: 92         SUB     D               
6FA3: FD         ???                     
6FA4: CB FC      SET     1,E             
6FA6: D8         RET     C               
6FA7: EE D8      XOR     $D8             
6FA9: EE CB      XOR     $CB             
6FAB: FC         ???                     
6FAC: 92         SUB     D               
6FAD: FD         ???                     
6FAE: B5         OR      L               
6FAF: FB         EI                      
6FB0: 1A         LD      A,(DE)          
6FB1: EC         ???                     
6FB2: 9C         SBC     H               
6FB3: E6 C6      AND     $C6             
6FB5: F2         ???                     
6FB6: 42         LD      B,D             
6FB7: F2         ???                     
6FB8: 42         LD      B,D             
6FB9: F2         ???                     
6FBA: C6 F2      ADD     $F2             
6FBC: 9C         SBC     H               
6FBD: E6 1A      AND     $1A             
6FBF: EC         ???                     
6FC0: FF         RST     0X38            
6FC1: F9         LD      SP,HL           
6FC2: F9         LD      SP,HL           
6FC3: 36 30      LD      (HL),$30        
6FC5: FF         RST     0X38            
6FC6: FC         ???                     
6FC7: FF         RST     0X38            
6FC8: FF         RST     0X38            
6FC9: C7         RST     0X00            
6FCA: 83         ADD     A,E             
6FCB: FF         RST     0X38            
6FCC: BB         CP      E               
6FCD: FF         RST     0X38            
6FCE: FF         RST     0X38            
6FCF: FF         RST     0X38            
6FD0: 7F         LD      A,A             
6FD1: FF         RST     0X38            
6FD2: 6E         LD      L,(HL)          
6FD3: FD         ???                     
6FD4: C7         RST     0X00            
6FD5: 7E         LD      A,(HL)          
6FD6: C3 FF 83   JP      $83FF           
6FD9: C3 66 C3   JP      $C366           
6FDC: BD         CP      L               
6FDD: 7E         LD      A,(HL)          
6FDE: 00         NOP                     
6FDF: 00         NOP                     
6FE0: FB         EI                      
6FE1: FD         ???                     
6FE2: 9B         SBC     E               
6FE3: FD         ???                     
6FE4: DF         RST     0X18            
6FE5: EF         RST     0X28            
6FE6: DF         RST     0X18            
6FE7: EF         RST     0X28            
6FE8: DB         ???                     
6FE9: ED         ???                     
6FEA: 99         SBC     C               
6FEB: FE F1      CP      $F1             
6FED: FE F3      CP      $F3             
6FEF: FD         ???                     
6FF0: 3A         LD      A,(HLD)         
6FF1: DC F4 FE   CALL    C,$FEF4         
6FF4: C6 F2      ADD     $F2             
6FF6: 82         ADD     A,D             
6FF7: F2         ???                     
6FF8: C2 F2 E6   JP      NZ,$E6F2        
6FFB: F2         ???                     
6FFC: FC         ???                     
6FFD: BE         CP      (HL)            
6FFE: BA         CP      D               
6FFF: DC FF 00   CALL    C,$00FF         
7002: 07         RLCA                    
7003: F8 00      LDHL    SP,$00          
7005: FF         RST     0X38            
7006: 7C         LD      A,H             
7007: FF         RST     0X38            
7008: C7         RST     0X00            
7009: FF         RST     0X38            
700A: 39         ADD     HL,SP           
700B: C7         RST     0X00            
700C: FE 01      CP      $01             
700E: DF         RST     0X18            
700F: 20 FF      JR      NZ,$7010        
7011: 00         NOP                     
7012: FC         ???                     
7013: 03         INC     BC              
7014: 60         LD      H,B             
7015: 9F         SBC     A               
7016: 00         NOP                     
7017: FF         RST     0X38            
7018: 07         RLCA                    
7019: FF         RST     0X38            
701A: DC FF 73   CALL    C,$73FF         
701D: FC         ???                     
701E: 0F         RRCA                    
701F: F0 9F      LD      A,($9F)         
7021: E0 99      LDFF00  ($99),A         
7023: E6 CC      AND     $CC             
7025: F3         DI                      
7026: C4 F3 D0   CALL    NZ,$D0F3        
7029: E7         RST     0X20            
702A: AE         XOR     (HL)            
702B: C1         POP     BC              
702C: AB         XOR     E               
702D: C4 BF C0   CALL    NZ,$C0BF        
7030: FD         ???                     
7031: 03         INC     BC              
7032: F7         RST     0X30            
7033: 0F         RRCA                    
7034: 2F         CPL                     
7035: D9         RETI                    
7036: 77         LD      (HL),A          
7037: 99         SBC     C               
7038: 51         LD      D,C             
7039: 9F         SBC     A               
703A: 49         LD      C,C             
703B: 9F         SBC     A               
703C: D7         RST     0X10            
703D: 0F         RRCA                    
703E: E9         JP      (HL)            
703F: 07         RLCA                    
7040: 0F         RRCA                    
7041: FF         RST     0X38            
7042: 33         INC     SP              
7043: FC         ???                     
7044: 50         LD      D,B             
7045: E0 A0      LDFF00  ($A0),A         
7047: C0         RET     NZ              
7048: A3         AND     E               
7049: C0         RET     NZ              
704A: D3         ???                     
704B: E0 CF      LDFF00  ($CF),A         
704D: F0 8F      LD      A,($8F)         
704F: F0 F8      LD      A,($F8)         
7051: FF         RST     0X38            
7052: 14         INC     D               
7053: 0F         RRCA                    
7054: 0A         LD      A,(BC)          
7055: 07         RLCA                    
7056: 05         DEC     B               
7057: 03         INC     BC              
7058: 05         DEC     B               
7059: 03         INC     BC              
705A: FB         EI                      
705B: 07         RLCA                    
705C: E3         ???                     
705D: 1F         RRA                     
705E: F1         POP     AF              
705F: 0F         RRCA                    
7060: FF         RST     0X38            
7061: FF         RST     0X38            
7062: F3         DI                      
7063: FC         ???                     
7064: D8         RET     C               
7065: E0 B0      LDFF00  ($B0),A         
7067: C0         RET     NZ              
7068: BF         CP      A               
7069: C0         RET     NZ              
706A: DF         RST     0X18            
706B: E0 C3      LDFF00  ($C3),A         
706D: FC         ???                     
706E: 8F         ADC     A,A             
706F: F0 FF      LD      A,($FF)         
7071: FF         RST     0X38            
7072: 17         RLA                     
7073: 0F         RRCA                    
7074: 0B         DEC     BC              
7075: 07         RLCA                    
7076: 05         DEC     B               
7077: 03         INC     BC              
7078: 1D         DEC     E               
7079: 03         INC     BC              
707A: FB         EI                      
707B: 07         RLCA                    
707C: E3         ???                     
707D: 1F         RRA                     
707E: F1         POP     AF              
707F: 0F         RRCA                    
7080: FF         RST     0X38            
7081: FF         RST     0X38            
7082: C1         POP     BC              
7083: FF         RST     0X38            
7084: 80         ADD     A,B             
7085: FF         RST     0X38            
7086: 84         ADD     A,H             
7087: FF         RST     0X38            
7088: 80         ADD     A,B             
7089: FF         RST     0X38            
708A: 90         SUB     B               
708B: FF         RST     0X38            
708C: C6 FF      ADD     $FF             
708E: FF         RST     0X38            
708F: FF         RST     0X38            
7090: FF         RST     0X38            
7091: FF         RST     0X38            
7092: 83         ADD     A,E             
7093: FF         RST     0X38            
7094: 01 FF 09   LD      BC,$09FF        
7097: FF         RST     0X38            
7098: 01 FF 01   LD      BC,$01FF        
709B: FF         RST     0X38            
709C: 13         INC     DE              
709D: FF         RST     0X38            
709E: FF         RST     0X38            
709F: FF         RST     0X38            
70A0: FF         RST     0X38            
70A1: FF         RST     0X38            
70A2: C1         POP     BC              
70A3: 80         ADD     A,B             
70A4: BF         CP      A               
70A5: 9C         SBC     H               
70A6: B7         OR      A               
70A7: 97         SUB     A               
70A8: B0         OR      B               
70A9: 90         SUB     B               
70AA: BF         CP      A               
70AB: 9F         SBC     A               
70AC: BD         CP      L               
70AD: C3 FF FF   JP      $FFFF           
70B0: FF         RST     0X38            
70B1: FF         RST     0X38            
70B2: E1         POP     HL              
70B3: 03         INC     BC              
70B4: BF         CP      A               
70B5: 39         ADD     HL,SP           
70B6: EF         RST     0X28            
70B7: E9         JP      (HL)            
70B8: 0F         RRCA                    
70B9: 09         ADD     HL,BC           
70BA: FF         RST     0X38            
70BB: F9         LD      SP,HL           
70BC: FD         ???                     
70BD: 83         ADD     A,E             
70BE: FF         RST     0X38            
70BF: FF         RST     0X38            
70C0: F3         DI                      
70C1: F3         DI                      
70C2: F0 F0      LD      A,($F0)         
70C4: FF         RST     0X38            
70C5: F0 F7      LD      A,($F7)         
70C7: F8 FC      LDHL    SP,$FC          
70C9: FF         RST     0X38            
70CA: FF         RST     0X38            
70CB: FC         ???                     
70CC: FD         ???                     
70CD: FE FF      CP      $FF             
70CF: FF         RST     0X38            
70D0: CF         RST     0X08            
70D1: CF         RST     0X08            
70D2: 0F         RRCA                    
70D3: 0F         RRCA                    
70D4: FF         RST     0X38            
70D5: 0F         RRCA                    
70D6: EF         RST     0X28            
70D7: 1F         RRA                     
70D8: 3F         CCF                     
70D9: FF         RST     0X38            
70DA: FF         RST     0X38            
70DB: 3F         CCF                     
70DC: BF         CP      A               
70DD: 7F         LD      A,A             
70DE: FF         RST     0X38            
70DF: FF         RST     0X38            
70E0: FF         RST     0X38            
70E1: FF         RST     0X38            
70E2: C0         RET     NZ              
70E3: 80         ADD     A,B             
70E4: BF         CP      A               
70E5: 80         ADD     A,B             
70E6: AF         XOR     A               
70E7: 80         ADD     A,B             
70E8: BF         CP      A               
70E9: 80         ADD     A,B             
70EA: BF         CP      A               
70EB: 80         ADD     A,B             
70EC: BC         CP      H               
70ED: C3 FF FF   JP      $FFFF           
70F0: FF         RST     0X38            
70F1: FF         RST     0X38            
70F2: E1         POP     HL              
70F3: 03         INC     BC              
70F4: 1F         RRA                     
70F5: 01 FF 01   LD      BC,$01FF        
70F8: FF         RST     0X38            
70F9: 01 F7 09   LD      BC,$09F7        
70FC: 7D         LD      A,L             
70FD: 83         ADD     A,E             
70FE: FF         RST     0X38            
70FF: FF         RST     0X38            
7100: FF         RST     0X38            
7101: 00         NOP                     
7102: E3         ???                     
7103: 1C         INC     E               
7104: 81         ADD     A,C             
7105: 7E         LD      A,(HL)          
7106: 00         NOP                     
7107: FF         RST     0X38            
7108: 3C         INC     A               
7109: FF         RST     0X38            
710A: E3         ???                     
710B: FF         RST     0X38            
710C: 98         SBC     B               
710D: E7         RST     0X20            
710E: 7F         LD      A,A             
710F: 80         ADD     A,B             
7110: FF         RST     0X38            
7111: 00         NOP                     
7112: E3         ???                     
7113: 1C         INC     E               
7114: C1         POP     BC              
7115: 3E 00      LD      A,$00           
7117: FF         RST     0X38            
7118: 3C         INC     A               
7119: FF         RST     0X38            
711A: C3 FF 18   JP      $18FF           
711D: E7         RST     0X20            
711E: FE 01      CP      $01             
7120: 9F         SBC     A               
7121: E0 EF      LDFF00  ($EF),A         
7123: F0 B4      LD      A,($B4)         
7125: 9B         SBC     E               
7126: EE 99      XOR     $99             
7128: 8E         ADC     A,(HL)          
7129: F9         LD      SP,HL           
712A: 92         SUB     D               
712B: F9         LD      SP,HL           
712C: EB         ???                     
712D: F0 97      LD      A,($97)         
712F: E0 F9      LDFF00  ($F9),A         
7131: 07         RLCA                    
7132: 39         ADD     HL,SP           
7133: C7         RST     0X00            
7134: 33         INC     SP              
7135: CF         RST     0X08            
7136: 13         INC     DE              
7137: CF         RST     0X08            
7138: 0B         DEC     BC              
7139: E7         RST     0X20            
713A: 75         LD      (HL),L          
713B: 83         ADD     A,E             
713C: DD         ???                     
713D: 23         INC     HL              
713E: FD         ???                     
713F: 03         INC     BC              
7140: 8B         ADC     A,E             
7141: FC         ???                     
7142: B4         OR      H               
7143: CF         RST     0X08            
7144: BB         CP      E               
7145: C7         RST     0X00            
7146: 59         LD      E,C             
7147: E7         RST     0X20            
7148: 22         LD      (HLI),A         
7149: FF         RST     0X38            
714A: 1C         INC     E               
714B: FF         RST     0X38            
714C: 00         NOP                     
714D: FF         RST     0X38            
714E: 00         NOP                     
714F: FF         RST     0X38            
7150: DF         RST     0X18            
7151: 3F         CCF                     
7152: 31 FF CD   LD      SP,$CDFF        
7155: F3         DI                      
7156: 9D         SBC     L               
7157: E3         ???                     
7158: 5D         LD      E,L             
7159: E3         ???                     
715A: 2D         DEC     L               
715B: F3         DI                      
715C: 12         LD      (DE),A          
715D: FF         RST     0X38            
715E: 0C         INC     C               
715F: FF         RST     0X38            
7160: 8B         ADC     A,E             
7161: FC         ???                     
7162: B4         OR      H               
7163: CF         RST     0X08            
7164: BB         CP      E               
7165: C7         RST     0X00            
7166: D9         RETI                    
7167: E7         RST     0X20            
7168: E3         ???                     
7169: FF         RST     0X38            
716A: FF         RST     0X38            
716B: FF         RST     0X38            
716C: FF         RST     0X38            
716D: FF         RST     0X38            
716E: FF         RST     0X38            
716F: FF         RST     0X38            
7170: DF         RST     0X18            
7171: 3F         CCF                     
7172: 31 FF CD   LD      SP,$CDFF        
7175: F3         DI                      
7176: 9D         SBC     L               
7177: E3         ???                     
7178: DD         ???                     
7179: E3         ???                     
717A: ED         ???                     
717B: F3         DI                      
717C: F3         DI                      
717D: FF         RST     0X38            
717E: FF         RST     0X38            
717F: FF         RST     0X38            
7180: FF         RST     0X38            
7181: FF         RST     0X38            
7182: C3 FF 01   JP      $01FF           
7185: FF         RST     0X38            
7186: 11 FF 01   LD      DE,$01FF        
7189: FF         RST     0X38            
718A: 01 FF 63   LD      BC,$63FF        
718D: FF         RST     0X38            
718E: FF         RST     0X38            
718F: FF         RST     0X38            
7190: FF         RST     0X38            
7191: FF         RST     0X38            
7192: C0         RET     NZ              
7193: FF         RST     0X38            
7194: 82         ADD     A,D             
7195: FF         RST     0X38            
7196: 80         ADD     A,B             
7197: FF         RST     0X38            
7198: 81         ADD     A,C             
7199: FF         RST     0X38            
719A: 90         SUB     B               
719B: FF         RST     0X38            
719C: C0         RET     NZ              
719D: FF         RST     0X38            
719E: FF         RST     0X38            
719F: FF         RST     0X38            
71A0: FF         RST     0X38            
71A1: FF         RST     0X38            
71A2: FF         RST     0X38            
71A3: FF         RST     0X38            
71A4: FF         RST     0X38            
71A5: FF         RST     0X38            
71A6: F7         RST     0X30            
71A7: EF         RST     0X28            
71A8: FF         RST     0X38            
71A9: E0 E0      LDFF00  ($E0),A         
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
71B6: EF         RST     0X28            
71B7: F7         RST     0X30            
71B8: FF         RST     0X38            
71B9: 07         RLCA                    
71BA: 07         RLCA                    
71BB: FF         RST     0X38            
71BC: FF         RST     0X38            
71BD: FF         RST     0X38            
71BE: FF         RST     0X38            
71BF: FF         RST     0X38            
71C0: 18 FF      JR      $71C1           
71C2: 18 FF      JR      $71C3           
71C4: 3F         CCF                     
71C5: C0         RET     NZ              
71C6: 17         RLA                     
71C7: E8 3F      ADD     SP,$3F          
71C9: C0         RET     NZ              
71CA: 3F         CCF                     
71CB: FF         RST     0X38            
71CC: 18 FF      JR      $71CD           
71CE: 18 FF      JR      $71CF           
71D0: 18 FF      JR      $71D1           
71D2: 18 FF      JR      $71D3           
71D4: FC         ???                     
71D5: 03         INC     BC              
71D6: E8 17      ADD     SP,$17          
71D8: FC         ???                     
71D9: 03         INC     BC              
71DA: FC         ???                     
71DB: FF         RST     0X38            
71DC: 18 FF      JR      $71DD           
71DE: 18 FF      JR      $71DF           
71E0: FF         RST     0X38            
71E1: FF         RST     0X38            
71E2: E1         POP     HL              
71E3: 03         INC     BC              
71E4: 1F         RRA                     
71E5: 01 FF 01   LD      BC,$01FF        
71E8: FF         RST     0X38            
71E9: 01 F7 09   LD      BC,$09F7        
71EC: 7D         LD      A,L             
71ED: 83         ADD     A,E             
71EE: FF         RST     0X38            
71EF: FF         RST     0X38            
71F0: FF         RST     0X38            
71F1: FF         RST     0X38            
71F2: C0         RET     NZ              
71F3: 80         ADD     A,B             
71F4: BF         CP      A               
71F5: 80         ADD     A,B             
71F6: AF         XOR     A               
71F7: 80         ADD     A,B             
71F8: BF         CP      A               
71F9: 80         ADD     A,B             
71FA: BF         CP      A               
71FB: 80         ADD     A,B             
71FC: BC         CP      H               
71FD: C3 FF FF   JP      $FFFF           
7200: FF         RST     0X38            
7201: FF         RST     0X38            
7202: 90         SUB     B               
7203: A3         AND     E               
7204: 85         ADD     A,L             
7205: A2         AND     D               
7206: 85         ADD     A,L             
7207: A2         AND     D               
7208: 85         ADD     A,L             
7209: A2         AND     D               
720A: 85         ADD     A,L             
720B: A2         AND     D               
720C: DC A3 FF   CALL    C,$FFA3         
720F: FF         RST     0X38            
7210: FF         RST     0X38            
7211: FF         RST     0X38            
7212: 03         INC     BC              
7213: 01 03 01   LD      BC,$0103        
7216: 37         SCF                     
7217: 01 0B 01   LD      BC,$010B        
721A: 17         RLA                     
721B: 01 FD 03   LD      BC,$03FD        
721E: FF         RST     0X38            
721F: FF         RST     0X38            
7220: FF         RST     0X38            
7221: FF         RST     0X38            
7222: FE 81      CP      $81             
7224: C0         RET     NZ              
7225: BF         CP      A               
7226: C8         RET     Z               
7227: BF         CP      A               
7228: E0 BF      LDFF00  ($BF),A         
722A: C8         RET     Z               
722B: BF         CP      A               
722C: 80         ADD     A,B             
722D: FF         RST     0X38            
722E: FF         RST     0X38            
722F: FF         RST     0X38            
7230: FF         RST     0X38            
7231: FF         RST     0X38            
7232: DD         ???                     
7233: E5         PUSH    HL              
7234: 67         LD      H,A             
7235: DD         ???                     
7236: 67         LD      H,A             
7237: DD         ???                     
7238: 67         LD      H,A             
7239: DD         ???                     
723A: 67         LD      H,A             
723B: DD         ???                     
723C: C7         RST     0X00            
723D: FD         ???                     
723E: FF         RST     0X38            
723F: FF         RST     0X38            
7240: 30 3F      JR      NC,$7281        
7242: 50         LD      D,B             
7243: 7F         LD      A,A             
7244: 98         SBC     B               
7245: FF         RST     0X38            
7246: 89         ADC     A,C             
7247: FF         RST     0X38            
7248: 8F         ADC     A,A             
7249: FF         RST     0X38            
724A: 89         ADC     A,C             
724B: FF         RST     0X38            
724C: 90         SUB     B               
724D: FF         RST     0X38            
724E: 50         LD      D,B             
724F: 7F         LD      A,A             
7250: FF         RST     0X38            
7251: FF         RST     0X38            
7252: C1         POP     BC              
7253: FF         RST     0X38            
7254: 80         ADD     A,B             
7255: FF         RST     0X38            
7256: 00         NOP                     
7257: FF         RST     0X38            
7258: 00         NOP                     
7259: FF         RST     0X38            
725A: 00         NOP                     
725B: FF         RST     0X38            
725C: 81         ADD     A,C             
725D: FF         RST     0X38            
725E: C1         POP     BC              
725F: FF         RST     0X38            
7260: FF         RST     0X38            
7261: FF         RST     0X38            
7262: 83         ADD     A,E             
7263: FF         RST     0X38            
7264: 01 FF 00   LD      BC,$00FF        
7267: FF         RST     0X38            
7268: 00         NOP                     
7269: FF         RST     0X38            
726A: 00         NOP                     
726B: FF         RST     0X38            
726C: 81         ADD     A,C             
726D: FF         RST     0X38            
726E: 83         ADD     A,E             
726F: FF         RST     0X38            
7270: 0C         INC     C               
7271: FC         ???                     
7272: 0A         LD      A,(BC)          
7273: FE 19      CP      $19             
7275: FF         RST     0X38            
7276: 91         SUB     C               
7277: FF         RST     0X38            
7278: F1         POP     AF              
7279: FF         RST     0X38            
727A: 91         SUB     C               
727B: FF         RST     0X38            
727C: 09         ADD     HL,BC           
727D: FF         RST     0X38            
727E: 0A         LD      A,(BC)          
727F: FE 00      CP      $00             
7281: FF         RST     0X38            
7282: 01 FE 31   LD      BC,$31FE        
7285: CE 20      ADC     $20             
7287: CF         RST     0X08            
7288: 28 C7      JR      Z,$7251         
728A: 15         DEC     D               
728B: E2         LDFF00  (C),A           
728C: 08 F1 07   LD      ($07F1),SP      
728F: F8 00      LDHL    SP,$00          
7291: FF         RST     0X38            
7292: 80         ADD     A,B             
7293: 7F         LD      A,A             
7294: 0C         INC     C               
7295: 73         LD      (HL),E          
7296: 94         SUB     H               
7297: 63         LD      H,E             
7298: 28 C7      JR      Z,$7261         
729A: 10 0F      STOP    $0F             
729C: 66         LD      H,(HL)          
729D: 99         SBC     C               
729E: 8A         ADC     A,D             
729F: 71         LD      (HL),C          
72A0: FF         RST     0X38            
72A1: 00         NOP                     
72A2: FF         RST     0X38            
72A3: 00         NOP                     
72A4: FF         RST     0X38            
72A5: 00         NOP                     
72A6: FE 00      CP      $00             
72A8: FC         ???                     
72A9: 00         NOP                     
72AA: FC         ???                     
72AB: 00         NOP                     
72AC: F8 00      LDHL    SP,$00          
72AE: F8 00      LDHL    SP,$00          
72B0: FC         ???                     
72B1: 00         NOP                     
72B2: E0 00      LDFF00  ($00),A         
72B4: 00         NOP                     
72B5: 00         NOP                     
72B6: 00         NOP                     
72B7: 00         NOP                     
72B8: 00         NOP                     
72B9: 00         NOP                     
72BA: 00         NOP                     
72BB: 00         NOP                     
72BC: 00         NOP                     
72BD: 00         NOP                     
72BE: 00         NOP                     
72BF: 00         NOP                     
72C0: 3F         CCF                     
72C1: 00         NOP                     
72C2: 0F         RRCA                    
72C3: 00         NOP                     
72C4: 07         RLCA                    
72C5: 00         NOP                     
72C6: 07         RLCA                    
72C7: 00         NOP                     
72C8: 03         INC     BC              
72C9: 00         NOP                     
72CA: 03         INC     BC              
72CB: 00         NOP                     
72CC: 00         NOP                     
72CD: 00         NOP                     
72CE: 00         NOP                     
72CF: 00         NOP                     
72D0: FF         RST     0X38            
72D1: 00         NOP                     
72D2: FF         RST     0X38            
72D3: 00         NOP                     
72D4: FF         RST     0X38            
72D5: 00         NOP                     
72D6: FF         RST     0X38            
72D7: 00         NOP                     
72D8: FF         RST     0X38            
72D9: 00         NOP                     
72DA: FF         RST     0X38            
72DB: 00         NOP                     
72DC: 1F         RRA                     
72DD: 00         NOP                     
72DE: 07         RLCA                    
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
72FC: FF         RST     0X38            
72FD: 00         NOP                     
72FE: FF         RST     0X38            
72FF: 00         NOP                     
7300: FF         RST     0X38            
7301: FF         RST     0X38            
7302: 98         SBC     B               
7303: 80         ADD     A,B             
7304: 80         ADD     A,B             
7305: 90         SUB     B               
7306: 80         ADD     A,B             
7307: 90         SUB     B               
7308: 80         ADD     A,B             
7309: 90         SUB     B               
730A: 80         ADD     A,B             
730B: 90         SUB     B               
730C: A8         XOR     B               
730D: 90         SUB     B               
730E: FF         RST     0X38            
730F: FF         RST     0X38            
7310: FF         RST     0X38            
7311: FF         RST     0X38            
7312: A7         AND     A               
7313: 40         LD      B,B             
7314: 00         NOP                     
7315: 40         LD      B,B             
7316: 87         ADD     A,A             
7317: 40         LD      B,B             
7318: 8F         ADC     A,A             
7319: 40         LD      B,B             
731A: 87         ADD     A,A             
731B: 40         LD      B,B             
731C: BF         CP      A               
731D: 40         LD      B,B             
731E: FF         RST     0X38            
731F: FF         RST     0X38            
7320: FF         RST     0X38            
7321: FF         RST     0X38            
7322: FA 07 A6   LD      A,($A607)       
7325: 5B         LD      E,E             
7326: C3 3E A3   JP      $A33E           
7329: 5E         LD      E,(HL)          
732A: E3         ???                     
732B: 1E 83      LD      E,$83           
732D: 7E         LD      A,(HL)          
732E: FF         RST     0X38            
732F: FF         RST     0X38            
7330: FF         RST     0X38            
7331: FF         RST     0X38            
7332: CD 3B 0D   CALL    $0D3B           
7335: FB         EI                      
7336: 19         ADD     HL,DE           
7337: FF         RST     0X38            
7338: 09         ADD     HL,BC           
7339: FF         RST     0X38            
733A: 49         LD      C,C             
733B: FF         RST     0X38            
733C: 09         ADD     HL,BC           
733D: FF         RST     0X38            
733E: FF         RST     0X38            
733F: FF         RST     0X38            
7340: 30 3F      JR      NC,$7381        
7342: 50         LD      D,B             
7343: 7F         LD      A,A             
7344: 98         SBC     B               
7345: FF         RST     0X38            
7346: 89         ADC     A,C             
7347: FF         RST     0X38            
7348: 8F         ADC     A,A             
7349: FF         RST     0X38            
734A: 89         ADC     A,C             
734B: FF         RST     0X38            
734C: 90         SUB     B               
734D: FF         RST     0X38            
734E: D0         RET     NC              
734F: FF         RST     0X38            
7350: FF         RST     0X38            
7351: FF         RST     0X38            
7352: C1         POP     BC              
7353: FF         RST     0X38            
7354: 80         ADD     A,B             
7355: FF         RST     0X38            
7356: 00         NOP                     
7357: FF         RST     0X38            
7358: 00         NOP                     
7359: FF         RST     0X38            
735A: 00         NOP                     
735B: FF         RST     0X38            
735C: 81         ADD     A,C             
735D: FF         RST     0X38            
735E: C1         POP     BC              
735F: FF         RST     0X38            
7360: FF         RST     0X38            
7361: FF         RST     0X38            
7362: 83         ADD     A,E             
7363: FF         RST     0X38            
7364: 01 FF 00   LD      BC,$00FF        
7367: FF         RST     0X38            
7368: 00         NOP                     
7369: FF         RST     0X38            
736A: 00         NOP                     
736B: FF         RST     0X38            
736C: 81         ADD     A,C             
736D: FF         RST     0X38            
736E: 83         ADD     A,E             
736F: FF         RST     0X38            
7370: 0C         INC     C               
7371: FC         ???                     
7372: 0A         LD      A,(BC)          
7373: FE 19      CP      $19             
7375: FF         RST     0X38            
7376: 91         SUB     C               
7377: FF         RST     0X38            
7378: F1         POP     AF              
7379: FF         RST     0X38            
737A: 91         SUB     C               
737B: FF         RST     0X38            
737C: 09         ADD     HL,BC           
737D: FF         RST     0X38            
737E: 0A         LD      A,(BC)          
737F: FE 00      CP      $00             
7381: FF         RST     0X38            
7382: 40         LD      B,B             
7383: 9E         SBC     (HL)            
7384: 61         LD      H,C             
7385: 8E         ADC     A,(HL)          
7386: 32         LD      (HLD),A         
7387: C1         POP     BC              
7388: 1E E1      LD      E,$E1           
738A: 00         NOP                     
738B: FF         RST     0X38            
738C: 02         LD      (BC),A          
738D: FD         ???                     
738E: 04         INC     B               
738F: F8 14      LDHL    SP,$14          
7391: E3         ???                     
7392: B8         CP      B               
7393: 47         LD      B,A             
7394: F0 0F      LD      A,($0F)         
7396: C2 39 12   JP      NZ,$1239        
7399: E1         POP     HL              
739A: FC         ???                     
739B: 03         INC     BC              
739C: 00         NOP                     
739D: FF         RST     0X38            
739E: C0         RET     NZ              
739F: 3F         CCF                     
73A0: F8 00      LDHL    SP,$00          
73A2: C0         RET     NZ              
73A3: 00         NOP                     
73A4: 80         ADD     A,B             
73A5: 00         NOP                     
73A6: 80         ADD     A,B             
73A7: 00         NOP                     
73A8: 80         ADD     A,B             
73A9: 00         NOP                     
73AA: 00         NOP                     
73AB: 00         NOP                     
73AC: 00         NOP                     
73AD: 00         NOP                     
73AE: 00         NOP                     
73AF: 00         NOP                     
73B0: 00         NOP                     
73B1: 00         NOP                     
73B2: 00         NOP                     
73B3: 00         NOP                     
73B4: 00         NOP                     
73B5: 00         NOP                     
73B6: 00         NOP                     
73B7: 00         NOP                     
73B8: 00         NOP                     
73B9: 00         NOP                     
73BA: 00         NOP                     
73BB: 00         NOP                     
73BC: 00         NOP                     
73BD: 00         NOP                     
73BE: 00         NOP                     
73BF: 00         NOP                     
73C0: 00         NOP                     
73C1: 00         NOP                     
73C2: 00         NOP                     
73C3: 00         NOP                     
73C4: 00         NOP                     
73C5: 00         NOP                     
73C6: 00         NOP                     
73C7: 00         NOP                     
73C8: 00         NOP                     
73C9: 00         NOP                     
73CA: 00         NOP                     
73CB: 00         NOP                     
73CC: 00         NOP                     
73CD: 00         NOP                     
73CE: 00         NOP                     
73CF: 00         NOP                     
73D0: 03         INC     BC              
73D1: 00         NOP                     
73D2: 01 00 01   LD      BC,$0100        
73D5: 00         NOP                     
73D6: 01 00 00   LD      BC,$0000        
73D9: 00         NOP                     
73DA: 00         NOP                     
73DB: 00         NOP                     
73DC: 00         NOP                     
73DD: 00         NOP                     
73DE: 00         NOP                     
73DF: 00         NOP                     
73E0: FE 00      CP      $00             
73E2: FC         ???                     
73E3: 00         NOP                     
73E4: FC         ???                     
73E5: 00         NOP                     
73E6: F8 00      LDHL    SP,$00          
73E8: F8 00      LDHL    SP,$00          
73EA: C0         RET     NZ              
73EB: 00         NOP                     
73EC: 80         ADD     A,B             
73ED: 00         NOP                     
73EE: 00         NOP                     
73EF: 00         NOP                     
73F0: 1F         RRA                     
73F1: 00         NOP                     
73F2: 0F         RRCA                    
73F3: 00         NOP                     
73F4: 0F         RRCA                    
73F5: 00         NOP                     
73F6: 07         RLCA                    
73F7: 00         NOP                     
73F8: 03         INC     BC              
73F9: 00         NOP                     
73FA: 03         INC     BC              
73FB: 00         NOP                     
73FC: 01 00 00   LD      BC,$0000        
73FF: 00         NOP                     
7400: 00         NOP                     
7401: 00         NOP                     
7402: 00         NOP                     
7403: 00         NOP                     
7404: 00         NOP                     
7405: 00         NOP                     
7406: 00         NOP                     
7407: 00         NOP                     
7408: 00         NOP                     
7409: 00         NOP                     
740A: 00         NOP                     
740B: 00         NOP                     
740C: 00         NOP                     
740D: 00         NOP                     
740E: 00         NOP                     
740F: 00         NOP                     
7410: 00         NOP                     
7411: 00         NOP                     
7412: 00         NOP                     
7413: 00         NOP                     
7414: 00         NOP                     
7415: 00         NOP                     
7416: 00         NOP                     
7417: 00         NOP                     
7418: 00         NOP                     
7419: 00         NOP                     
741A: 00         NOP                     
741B: 00         NOP                     
741C: 38 00      JR      C,$741E         
741E: 7E         LD      A,(HL)          
741F: 00         NOP                     
7420: 00         NOP                     
7421: 00         NOP                     
7422: 00         NOP                     
7423: 00         NOP                     
7424: 00         NOP                     
7425: 00         NOP                     
7426: 00         NOP                     
7427: 00         NOP                     
7428: 00         NOP                     
7429: 00         NOP                     
742A: 00         NOP                     
742B: 00         NOP                     
742C: 00         NOP                     
742D: 00         NOP                     
742E: 00         NOP                     
742F: 00         NOP                     
7430: 00         NOP                     
7431: 00         NOP                     
7432: 00         NOP                     
7433: 00         NOP                     
7434: 00         NOP                     
7435: 00         NOP                     
7436: 00         NOP                     
7437: 00         NOP                     
7438: 00         NOP                     
7439: 00         NOP                     
743A: 00         NOP                     
743B: 00         NOP                     
743C: 00         NOP                     
743D: 00         NOP                     
743E: 00         NOP                     
743F: 00         NOP                     
7440: CE 31      ADC     $31             
7442: CE 31      ADC     $31             
7444: CF         RST     0X08            
7445: 30 CE      JR      NC,$7415        
7447: 31 8E 71   LD      SP,$718E        
744A: 8E         ADC     A,(HL)          
744B: 71         LD      (HL),C          
744C: 8F         ADC     A,A             
744D: 70         LD      (HL),B          
744E: CF         RST     0X08            
744F: 30 CD      JR      NC,$741E        
7451: 3F         CCF                     
7452: C9         RET                     
7453: 3F         CCF                     
7454: C8         RET     Z               
7455: 3F         CCF                     
7456: 4C         LD      C,H             
7457: BF         CP      A               
7458: 04         INC     B               
7459: FF         RST     0X38            
745A: 04         INC     B               
745B: FF         RST     0X38            
745C: C4 3F CC   CALL    NZ,$CC3F        
745F: 3F         CCF                     
7460: FF         RST     0X38            
7461: FF         RST     0X38            
7462: 00         NOP                     
7463: 00         NOP                     
7464: FF         RST     0X38            
7465: 00         NOP                     
7466: FF         RST     0X38            
7467: FF         RST     0X38            
7468: 13         INC     DE              
7469: 1E 12      LD      E,$12           
746B: 1F         RRA                     
746C: 09         ADD     HL,BC           
746D: 0F         RRCA                    
746E: 05         DEC     B               
746F: 06 FF      LD      B,$FF           
7471: FF         RST     0X38            
7472: 01 01 FF   LD      BC,$FF01        
7475: 01 FF FF   LD      BC,$FFFF        
7478: C8         RET     Z               
7479: 78         LD      A,B             
747A: 48         LD      C,B             
747B: F8 90      LDHL    SP,$90          
747D: F0 A0      LD      A,($A0)         
747F: 60         LD      H,B             
7480: FF         RST     0X38            
7481: 00         NOP                     
7482: FF         RST     0X38            
7483: 00         NOP                     
7484: FF         RST     0X38            
7485: 00         NOP                     
7486: FF         RST     0X38            
7487: 00         NOP                     
7488: FF         RST     0X38            
7489: 00         NOP                     
748A: FF         RST     0X38            
748B: 00         NOP                     
748C: FF         RST     0X38            
748D: 00         NOP                     
748E: FF         RST     0X38            
748F: 00         NOP                     
7490: FF         RST     0X38            
7491: 00         NOP                     
7492: FF         RST     0X38            
7493: 00         NOP                     
7494: FF         RST     0X38            
7495: 00         NOP                     
7496: FF         RST     0X38            
7497: 00         NOP                     
7498: FF         RST     0X38            
7499: 00         NOP                     
749A: FF         RST     0X38            
749B: 00         NOP                     
749C: FF         RST     0X38            
749D: 00         NOP                     
749E: FF         RST     0X38            
749F: 00         NOP                     
74A0: DF         RST     0X18            
74A1: BF         CP      A               
74A2: DF         RST     0X18            
74A3: BF         CP      A               
74A4: AF         XOR     A               
74A5: DF         RST     0X18            
74A6: EF         RST     0X28            
74A7: DF         RST     0X18            
74A8: 47         LD      B,A             
74A9: FF         RST     0X38            
74AA: 47         LD      B,A             
74AB: FF         RST     0X38            
74AC: 63         LD      H,E             
74AD: FF         RST     0X38            
74AE: 33         INC     SP              
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
74C0: 31 FF 37   LD      SP,$37FF        
74C3: FF         RST     0X38            
74C4: 37         SCF                     
74C5: FF         RST     0X38            
74C6: 37         SCF                     
74C7: FF         RST     0X38            
74C8: A3         AND     E               
74C9: FF         RST     0X38            
74CA: A3         AND     E               
74CB: FF         RST     0X38            
74CC: 33         INC     SP              
74CD: FF         RST     0X38            
74CE: 33         INC     SP              
74CF: FF         RST     0X38            
74D0: FF         RST     0X38            
74D1: 00         NOP                     
74D2: FF         RST     0X38            
74D3: 00         NOP                     
74D4: FF         RST     0X38            
74D5: 00         NOP                     
74D6: FF         RST     0X38            
74D7: 00         NOP                     
74D8: FF         RST     0X38            
74D9: 00         NOP                     
74DA: FF         RST     0X38            
74DB: 00         NOP                     
74DC: FF         RST     0X38            
74DD: 80         ADD     A,B             
74DE: FF         RST     0X38            
74DF: C0         RET     NZ              
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
74F0: FB         EI                      
74F1: FD         ???                     
74F2: FB         EI                      
74F3: FD         ???                     
74F4: F5         PUSH    AF              
74F5: FB         EI                      
74F6: F7         RST     0X30            
74F7: FB         EI                      
74F8: E2         LDFF00  (C),A           
74F9: FF         RST     0X38            
74FA: E2         LDFF00  (C),A           
74FB: FF         RST     0X38            
74FC: C6 FF      ADD     $FF             
74FE: CC FF 00   CALL    Z,$00FF         
7501: 00         NOP                     
7502: 01 00 07   LD      BC,$0700        
7505: 00         NOP                     
7506: 3F         CCF                     
7507: 00         NOP                     
7508: 7F         LD      A,A             
7509: 00         NOP                     
750A: FF         RST     0X38            
750B: 00         NOP                     
750C: FF         RST     0X38            
750D: 00         NOP                     
750E: FF         RST     0X38            
750F: 00         NOP                     
7510: FF         RST     0X38            
7511: 00         NOP                     
7512: FF         RST     0X38            
7513: 00         NOP                     
7514: FF         RST     0X38            
7515: 00         NOP                     
7516: FF         RST     0X38            
7517: 00         NOP                     
7518: FF         RST     0X38            
7519: 00         NOP                     
751A: FF         RST     0X38            
751B: 00         NOP                     
751C: FF         RST     0X38            
751D: 00         NOP                     
751E: FF         RST     0X38            
751F: 00         NOP                     
7520: 00         NOP                     
7521: 00         NOP                     
7522: F0 00      LD      A,($00)         
7524: F9         LD      SP,HL           
7525: 00         NOP                     
7526: FF         RST     0X38            
7527: 00         NOP                     
7528: FF         RST     0X38            
7529: 00         NOP                     
752A: FF         RST     0X38            
752B: 00         NOP                     
752C: FF         RST     0X38            
752D: 00         NOP                     
752E: FF         RST     0X38            
752F: 00         NOP                     
7530: 00         NOP                     
7531: 00         NOP                     
7532: 70         LD      (HL),B          
7533: 00         NOP                     
7534: F8 00      LDHL    SP,$00          
7536: FE 00      CP      $00             
7538: FF         RST     0X38            
7539: 00         NOP                     
753A: FF         RST     0X38            
753B: 00         NOP                     
753C: FF         RST     0X38            
753D: 00         NOP                     
753E: FF         RST     0X38            
753F: 00         NOP                     
7540: C7         RST     0X00            
7541: 38 8F      JR      C,$74D2         
7543: 70         LD      (HL),B          
7544: 1C         INC     E               
7545: E0 58      LDFF00  ($58),A         
7547: E0 58      LDFF00  ($58),A         
7549: E0 D8      LDFF00  ($D8),A         
754B: E0 CC      LDFF00  ($CC),A         
754D: F0 E7      LD      A,($E7)         
754F: F8 8E      LDHL    SP,$8E          
7551: 7F         LD      A,A             
7552: CE 3F      ADC     $3F             
7554: C7         RST     0X00            
7555: 3F         CCF                     
7556: 63         LD      H,E             
7557: 1F         RRA                     
7558: 63         LD      H,E             
7559: 1F         RRA                     
755A: 63         LD      H,E             
755B: 1F         RRA                     
755C: C7         RST     0X00            
755D: 3F         CCF                     
755E: 87         ADD     A,A             
755F: 7F         LD      A,A             
7560: 05         DEC     B               
7561: 06 05      LD      B,$05           
7563: 06 05      LD      B,$05           
7565: 06 FF      LD      B,$FF           
7567: FF         RST     0X38            
7568: 80         ADD     A,B             
7569: 80         ADD     A,B             
756A: BF         CP      A               
756B: 80         ADD     A,B             
756C: 9C         SBC     H               
756D: E3         ???                     
756E: FF         RST     0X38            
756F: FF         RST     0X38            
7570: A0         AND     B               
7571: 60         LD      H,B             
7572: A0         AND     B               
7573: 60         LD      H,B             
7574: A0         AND     B               
7575: 60         LD      H,B             
7576: FF         RST     0X38            
7577: FF         RST     0X38            
7578: 01 01 F7   LD      BC,$F701        
757B: 09         ADD     HL,BC           
757C: 7D         LD      A,L             
757D: 83         ADD     A,E             
757E: FF         RST     0X38            
757F: FF         RST     0X38            
7580: F7         RST     0X30            
7581: 08 E7 18   LD      ($18E7),SP      
7584: CD 32 C9   CALL    $C932           
7587: 36 89      LD      (HL),$89        
7589: 76         HALT                    
758A: 81         ADD     A,C             
758B: 7E         LD      A,(HL)          
758C: 80         ADD     A,B             
758D: 7F         LD      A,A             
758E: 00         NOP                     
758F: FF         RST     0X38            
7590: 7F         LD      A,A             
7591: 80         ADD     A,B             
7592: 3F         CCF                     
7593: C0         RET     NZ              
7594: 3B         DEC     SP              
7595: C4 1B E4   CALL    NZ,$E41B        
7598: 19         ADD     HL,DE           
7599: E6 09      AND     $09             
759B: F6 01      OR      $01             
759D: FE 00      CP      $00             
759F: FF         RST     0X38            
75A0: 3F         CCF                     
75A1: FF         RST     0X38            
75A2: 6B         LD      L,E             
75A3: F7         RST     0X30            
75A4: 59         LD      E,C             
75A5: E7         RST     0X20            
75A6: B9         CP      C               
75A7: C7         RST     0X00            
75A8: BB         CP      E               
75A9: C7         RST     0X00            
75AA: B2         OR      D               
75AB: CF         RST     0X08            
75AC: A6         AND     (HL)            
75AD: DF         RST     0X18            
75AE: A7         AND     A               
75AF: DF         RST     0X18            
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
75C0: 1C         INC     E               
75C1: FF         RST     0X38            
75C2: 76         HALT                    
75C3: 8F         ADC     A,A             
75C4: 7B         LD      A,E             
75C5: 87         ADD     A,A             
75C6: 3D         DEC     A               
75C7: C3 8E F1   JP      $F18E           
75CA: 8E         ADC     A,(HL)          
75CB: F1         POP     AF              
75CC: C6 F9      ADD     $F9             
75CE: F0 FF      LD      A,($FF)         
75D0: 7F         LD      A,A             
75D1: E0 9F      LDFF00  ($9F),A         
75D3: 70         LD      (HL),B          
75D4: 4F         LD      C,A             
75D5: B8         CP      B               
75D6: A7         AND     A               
75D7: DC B7 CC   CALL    C,$CCB7         
75DA: D5         PUSH    DE              
75DB: EE C7      XOR     $C7             
75DD: FE C7      CP      $C7             
75DF: FE FF      CP      $FF             
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
75F0: FC         ???                     
75F1: FF         RST     0X38            
75F2: D6 EF      SUB     $EF             
75F4: 9A         SBC     D               
75F5: E7         RST     0X20            
75F6: 9D         SBC     L               
75F7: E3         ???                     
75F8: DD         ???                     
75F9: E3         ???                     
75FA: 4D         LD      C,L             
75FB: F3         DI                      
75FC: 65         LD      H,L             
75FD: FB         EI                      
75FE: E5         PUSH    HL              
75FF: FB         EI                      
7600: FF         RST     0X38            
7601: 00         NOP                     
7602: FF         RST     0X38            
7603: 00         NOP                     
7604: FF         RST     0X38            
7605: 00         NOP                     
7606: FF         RST     0X38            
7607: 00         NOP                     
7608: FF         RST     0X38            
7609: 00         NOP                     
760A: FF         RST     0X38            
760B: 00         NOP                     
760C: FF         RST     0X38            
760D: 01 FF 03   LD      BC,$03FF        
7610: 8D         ADC     A,L             
7611: FE CD      CP      $CD             
7613: FE CD      CP      $CD             
7615: FE CD      CP      $CD             
7617: FE 85      CP      $85             
7619: FE 85      CP      $85             
761B: FE 8D      CP      $8D             
761D: FE 8D      CP      $8D             
761F: FE FF      CP      $FF             
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
7640: F6 3F      OR      $3F             
7642: FF         RST     0X38            
7643: 49         LD      C,C             
7644: C9         RET                     
7645: 80         ADD     A,B             
7646: 80         ADD     A,B             
7647: 80         ADD     A,B             
7648: B6         OR      (HL)            
7649: 80         ADD     A,B             
764A: FF         RST     0X38            
764B: A0         AND     B               
764C: FF         RST     0X38            
764D: F6 FF      OR      $FF             
764F: FF         RST     0X38            
7650: 76         HALT                    
7651: FF         RST     0X38            
7652: FF         RST     0X38            
7653: 89         ADC     A,C             
7654: 88         ADC     A,B             
7655: 00         NOP                     
7656: 30 00      JR      NC,$7658        
7658: 7C         LD      A,H             
7659: 00         NOP                     
765A: FF         RST     0X38            
765B: 10 FF      STOP    $FF             
765D: 3C         INC     A               
765E: C3 FF 76   JP      $76FF           
7661: FF         RST     0X38            
7662: FF         RST     0X38            
7663: 89         ADC     A,C             
7664: 88         ADC     A,B             
7665: 00         NOP                     
7666: 30 00      JR      NC,$7668        
7668: 7C         LD      A,H             
7669: 00         NOP                     
766A: FF         RST     0X38            
766B: 10 FF      STOP    $FF             
766D: 3C         INC     A               
766E: C3 FF 76   JP      $76FF           
7671: FF         RST     0X38            
7672: FF         RST     0X38            
7673: 89         ADC     A,C             
7674: 88         ADC     A,B             
7675: 00         NOP                     
7676: 30 00      JR      NC,$7678        
7678: 7C         LD      A,H             
7679: 00         NOP                     
767A: FF         RST     0X38            
767B: 10 FF      STOP    $FF             
767D: 3C         INC     A               
767E: C3 FF 76   JP      $76FF           
7681: FF         RST     0X38            
7682: FF         RST     0X38            
7683: 89         ADC     A,C             
7684: 88         ADC     A,B             
7685: 00         NOP                     
7686: 30 00      JR      NC,$7688        
7688: 7C         LD      A,H             
7689: 00         NOP                     
768A: FF         RST     0X38            
768B: 10 FF      STOP    $FF             
768D: 3C         INC     A               
768E: C3 FF 6F   JP      $6FFF           
7691: FC         ???                     
7692: FF         RST     0X38            
7693: 92         SUB     D               
7694: 93         SUB     E               
7695: 01 01 01   LD      BC,$0101        
7698: 6D         LD      L,L             
7699: 01 FF 05   LD      BC,$05FF        
769C: FF         RST     0X38            
769D: 6F         LD      L,A             
769E: FF         RST     0X38            
769F: FF         RST     0X38            
76A0: 60         LD      H,B             
76A1: 7F         LD      A,A             
76A2: 60         LD      H,B             
76A3: 7F         LD      A,A             
76A4: 20 7F      JR      NZ,$7725        
76A6: 30 3F      JR      NC,$76E7        
76A8: 18 3F      JR      $76E9           
76AA: 0E 1F      LD      C,$1F           
76AC: 07         RLCA                    
76AD: 0F         RRCA                    
76AE: 01 03 03   LD      BC,$0303        
76B1: FF         RST     0X38            
76B2: 03         INC     BC              
76B3: FF         RST     0X38            
76B4: 02         LD      (BC),A          
76B5: FF         RST     0X38            
76B6: 06 FE      LD      B,$FE           
76B8: 0C         INC     C               
76B9: FE F8      CP      $F8             
76BB: FC         ???                     
76BC: F0 F8      LD      A,($F8)         
76BE: 80         ADD     A,B             
76BF: C0         RET     NZ              
76C0: 00         NOP                     
76C1: FF         RST     0X38            
76C2: 00         NOP                     
76C3: FF         RST     0X38            
76C4: 00         NOP                     
76C5: FF         RST     0X38            
76C6: 00         NOP                     
76C7: FF         RST     0X38            
76C8: 00         NOP                     
76C9: FF         RST     0X38            
76CA: 00         NOP                     
76CB: FF         RST     0X38            
76CC: 00         NOP                     
76CD: FF         RST     0X38            
76CE: 00         NOP                     
76CF: FF         RST     0X38            
76D0: 00         NOP                     
76D1: FF         RST     0X38            
76D2: 00         NOP                     
76D3: FF         RST     0X38            
76D4: 00         NOP                     
76D5: FF         RST     0X38            
76D6: 00         NOP                     
76D7: FF         RST     0X38            
76D8: 00         NOP                     
76D9: FF         RST     0X38            
76DA: 00         NOP                     
76DB: FF         RST     0X38            
76DC: 00         NOP                     
76DD: FF         RST     0X38            
76DE: 00         NOP                     
76DF: FF         RST     0X38            
76E0: 00         NOP                     
76E1: FF         RST     0X38            
76E2: 00         NOP                     
76E3: FF         RST     0X38            
76E4: 00         NOP                     
76E5: FF         RST     0X38            
76E6: 00         NOP                     
76E7: FF         RST     0X38            
76E8: 00         NOP                     
76E9: FF         RST     0X38            
76EA: 00         NOP                     
76EB: FF         RST     0X38            
76EC: 00         NOP                     
76ED: FF         RST     0X38            
76EE: 00         NOP                     
76EF: FF         RST     0X38            
76F0: 00         NOP                     
76F1: FF         RST     0X38            
76F2: 00         NOP                     
76F3: FF         RST     0X38            
76F4: 00         NOP                     
76F5: FF         RST     0X38            
76F6: 00         NOP                     
76F7: FF         RST     0X38            
76F8: 00         NOP                     
76F9: FF         RST     0X38            
76FA: 00         NOP                     
76FB: FF         RST     0X38            
76FC: 00         NOP                     
76FD: FF         RST     0X38            
76FE: 00         NOP                     
76FF: FF         RST     0X38            
7700: FC         ???                     
7701: 0F         RRCA                    
7702: F0 1F      LD      A,($1F)         
7704: E2         LDFF00  (C),A           
7705: 3D         DEC     A               
7706: E5         PUSH    HL              
7707: 3B         DEC     SP              
7708: CD 73 CA   CALL    $CA73           
770B: 77         LD      (HL),A          
770C: 9A         SBC     D               
770D: E7         RST     0X20            
770E: 82         ADD     A,D             
770F: FF         RST     0X38            
7710: 1F         RRA                     
7711: F8 2B      LDHL    SP,$2B          
7713: F0 C3      LD      A,($C3)         
7715: E0 A7      LDFF00  ($A7),A         
7717: C0         RET     NZ              
7718: 6E         LD      L,(HL)          
7719: 81         ADD     A,C             
771A: 7C         LD      A,H             
771B: 83         ADD     A,E             
771C: 7C         LD      A,H             
771D: 83         ADD     A,E             
771E: 70         LD      (HL),B          
771F: 8F         ADC     A,A             
7720: FF         RST     0X38            
7721: FF         RST     0X38            
7722: DD         ???                     
7723: FF         RST     0X38            
7724: FF         RST     0X38            
7725: DD         ???                     
7726: DD         ???                     
7727: DD         ???                     
7728: 99         SBC     C               
7729: DD         ???                     
772A: DD         ???                     
772B: 99         SBC     C               
772C: DD         ???                     
772D: 99         SBC     C               
772E: FF         RST     0X38            
772F: FF         RST     0X38            
7730: FF         RST     0X38            
7731: FF         RST     0X38            
7732: DD         ???                     
7733: FF         RST     0X38            
7734: FF         RST     0X38            
7735: DD         ???                     
7736: DD         ???                     
7737: DD         ???                     
7738: 99         SBC     C               
7739: DD         ???                     
773A: DD         ???                     
773B: 99         SBC     C               
773C: DD         ???                     
773D: 99         SBC     C               
773E: FF         RST     0X38            
773F: FF         RST     0X38            
7740: 9F         SBC     A               
7741: E0 99      LDFF00  ($99),A         
7743: E6 CC      AND     $CC             
7745: F3         DI                      
7746: C4 F3 D0   CALL    NZ,$D0F3        
7749: E7         RST     0X20            
774A: AE         XOR     (HL)            
774B: C1         POP     BC              
774C: AB         XOR     E               
774D: C4 BF C0   CALL    NZ,$C0BF        
7750: FF         RST     0X38            
7751: 00         NOP                     
7752: FC         ???                     
7753: 03         INC     BC              
7754: 60         LD      H,B             
7755: 9F         SBC     A               
7756: 00         NOP                     
7757: FF         RST     0X38            
7758: 07         RLCA                    
7759: FF         RST     0X38            
775A: DC FF 73   CALL    C,$73FF         
775D: FC         ???                     
775E: 0F         RRCA                    
775F: F0 FF      LD      A,($FF)         
7761: 00         NOP                     
7762: 07         RLCA                    
7763: F8 00      LDHL    SP,$00          
7765: FF         RST     0X38            
7766: 7C         LD      A,H             
7767: FF         RST     0X38            
7768: C7         RST     0X00            
7769: FF         RST     0X38            
776A: 39         ADD     HL,SP           
776B: C7         RST     0X00            
776C: FE 01      CP      $01             
776E: DF         RST     0X18            
776F: 20 FF      JR      NZ,$7770        
7771: 00         NOP                     
7772: FC         ???                     
7773: 03         INC     BC              
7774: 60         LD      H,B             
7775: 9F         SBC     A               
7776: 00         NOP                     
7777: FF         RST     0X38            
7778: 07         RLCA                    
7779: FF         RST     0X38            
777A: DC FF 73   CALL    C,$73FF         
777D: FC         ???                     
777E: 0F         RRCA                    
777F: F0 FF      LD      A,($FF)         
7781: 00         NOP                     
7782: 07         RLCA                    
7783: F8 00      LDHL    SP,$00          
7785: FF         RST     0X38            
7786: 7C         LD      A,H             
7787: FF         RST     0X38            
7788: C7         RST     0X00            
7789: FF         RST     0X38            
778A: 39         ADD     HL,SP           
778B: C7         RST     0X00            
778C: FE 01      CP      $01             
778E: DF         RST     0X18            
778F: 20 FD      JR      NZ,$778E        
7791: 03         INC     BC              
7792: F7         RST     0X30            
7793: 0F         RRCA                    
7794: 2F         CPL                     
7795: D9         RETI                    
7796: 77         LD      (HL),A          
7797: 99         SBC     C               
7798: 51         LD      D,C             
7799: 9F         SBC     A               
779A: 49         LD      C,C             
779B: 9F         SBC     A               
779C: D7         RST     0X10            
779D: 0F         RRCA                    
779E: E9         JP      (HL)            
779F: 07         RLCA                    
77A0: 00         NOP                     
77A1: FF         RST     0X38            
77A2: 00         NOP                     
77A3: FF         RST     0X38            
77A4: 00         NOP                     
77A5: FF         RST     0X38            
77A6: 00         NOP                     
77A7: FF         RST     0X38            
77A8: 18 FF      JR      $77A9           
77AA: 3C         INC     A               
77AB: FF         RST     0X38            
77AC: FF         RST     0X38            
77AD: FF         RST     0X38            
77AE: FF         RST     0X38            
77AF: FF         RST     0X38            
77B0: 00         NOP                     
77B1: FF         RST     0X38            
77B2: 00         NOP                     
77B3: FF         RST     0X38            
77B4: 00         NOP                     
77B5: FF         RST     0X38            
77B6: 00         NOP                     
77B7: FF         RST     0X38            
77B8: 18 FF      JR      $77B9           
77BA: 3C         INC     A               
77BB: FF         RST     0X38            
77BC: FF         RST     0X38            
77BD: FF         RST     0X38            
77BE: FF         RST     0X38            
77BF: FF         RST     0X38            
77C0: FF         RST     0X38            
77C1: 00         NOP                     
77C2: FF         RST     0X38            
77C3: 00         NOP                     
77C4: FF         RST     0X38            
77C5: 00         NOP                     
77C6: FF         RST     0X38            
77C7: 00         NOP                     
77C8: FF         RST     0X38            
77C9: 00         NOP                     
77CA: FF         RST     0X38            
77CB: 00         NOP                     
77CC: FF         RST     0X38            
77CD: 00         NOP                     
77CE: FF         RST     0X38            
77CF: 00         NOP                     
77D0: 00         NOP                     
77D1: FF         RST     0X38            
77D2: 00         NOP                     
77D3: FF         RST     0X38            
77D4: 00         NOP                     
77D5: FF         RST     0X38            
77D6: 00         NOP                     
77D7: FF         RST     0X38            
77D8: 00         NOP                     
77D9: FF         RST     0X38            
77DA: 00         NOP                     
77DB: FF         RST     0X38            
77DC: 00         NOP                     
77DD: FF         RST     0X38            
77DE: 00         NOP                     
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
77F0: 00         NOP                     
77F1: 00         NOP                     
77F2: 00         NOP                     
77F3: 00         NOP                     
77F4: 00         NOP                     
77F5: 00         NOP                     
77F6: 00         NOP                     
77F7: 00         NOP                     
77F8: 00         NOP                     
77F9: 00         NOP                     
77FA: 00         NOP                     
77FB: 00         NOP                     
77FC: 00         NOP                     
77FD: 00         NOP                     
77FE: 00         NOP                     
77FF: 00         NOP                     
7800: 46         LD      B,(HL)          
7801: FF         RST     0X38            
7802: 45         LD      B,L             
7803: FE C9      CP      $C9             
7805: FE F9      CP      $F9             
7807: FE C4      CP      $C4             
7809: FF         RST     0X38            
780A: 9A         SBC     D               
780B: E7         RST     0X20            
780C: BD         CP      L               
780D: C3 BE C1   JP      $C1BE           
7810: 20 FF      JR      NZ,$7811        
7812: 90         SUB     B               
7813: 7F         LD      A,A             
7814: C8         RET     Z               
7815: 3F         CCF                     
7816: A7         AND     A               
7817: 5F         LD      E,A             
7818: F3         DI                      
7819: 0F         RRCA                    
781A: 79         LD      A,C             
781B: 87         ADD     A,A             
781C: 01 FF FF   LD      BC,$FFFF        
781F: FF         RST     0X38            
7820: E6 9F      AND     $9F             
7822: 85         ADD     A,L             
7823: FE C9      CP      $C9             
7825: FE F9      CP      $F9             
7827: FE C4      CP      $C4             
7829: FF         RST     0X38            
782A: AA         XOR     D               
782B: C7         RST     0X00            
782C: 8D         ADC     A,L             
782D: C3 BE C1   JP      $C1BE           
7830: 35         DEC     (HL)            
7831: FB         EI                      
7832: 89         ADC     A,C             
7833: 7F         LD      A,A             
7834: D7         RST     0X10            
7835: 0F         RRCA                    
7836: CB 07      SET     1,E             
7838: E5         PUSH    HL              
7839: 03         INC     BC              
783A: 79         LD      A,C             
783B: 87         ADD     A,A             
783C: 03         INC     BC              
783D: FF         RST     0X38            
783E: FF         RST     0X38            
783F: FF         RST     0X38            
7840: 0F         RRCA                    
7841: FF         RST     0X38            
7842: 30 FF      JR      NC,$7843        
7844: 6F         LD      L,A             
7845: F0 D0      LD      A,($D0)         
7847: E0 A3      LDFF00  ($A3),A         
7849: C0         RET     NZ              
784A: B3         OR      E               
784B: C0         RET     NZ              
784C: BE         CP      (HL)            
784D: C1         POP     BC              
784E: 98         SBC     B               
784F: E7         RST     0X20            
7850: F0 FF      LD      A,($FF)         
7852: 1C         INC     E               
7853: FF         RST     0X38            
7854: E6 1F      AND     $1F             
7856: 13         INC     DE              
7857: 0F         RRCA                    
7858: 0B         DEC     BC              
7859: 07         RLCA                    
785A: E9         JP      (HL)            
785B: 07         RLCA                    
785C: 79         LD      A,C             
785D: 87         ADD     A,A             
785E: 31 CF FF   LD      SP,$FFCF        
7861: FF         RST     0X38            
7862: F0 FF      LD      A,($FF)         
7864: EF         RST     0X28            
7865: F0 D0      LD      A,($D0)         
7867: E0 A3      LDFF00  ($A3),A         
7869: C0         RET     NZ              
786A: B3         OR      E               
786B: C0         RET     NZ              
786C: BE         CP      (HL)            
786D: C1         POP     BC              
786E: 98         SBC     B               
786F: E7         RST     0X20            
7870: FF         RST     0X38            
7871: FF         RST     0X38            
7872: 1F         RRA                     
7873: FF         RST     0X38            
7874: E7         RST     0X20            
7875: 1F         RRA                     
7876: 13         INC     DE              
7877: 0F         RRCA                    
7878: 0B         DEC     BC              
7879: 07         RLCA                    
787A: E9         JP      (HL)            
787B: 07         RLCA                    
787C: 79         LD      A,C             
787D: 87         ADD     A,A             
787E: 31 CF FF   LD      SP,$FFCF        
7881: FF         RST     0X38            
7882: 86         ADD     A,(HL)          
7883: FF         RST     0X38            
7884: BF         CP      A               
7885: FF         RST     0X38            
7886: BF         CP      A               
7887: FF         RST     0X38            
7888: BF         CP      A               
7889: FF         RST     0X38            
788A: FF         RST     0X38            
788B: FF         RST     0X38            
788C: BF         CP      A               
788D: FF         RST     0X38            
788E: FF         RST     0X38            
788F: FF         RST     0X38            
7890: FF         RST     0X38            
7891: FF         RST     0X38            
7892: 17         RLA                     
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
78A0: E7         RST     0X20            
78A1: FF         RST     0X38            
78A2: FF         RST     0X38            
78A3: FF         RST     0X38            
78A4: C0         RET     NZ              
78A5: C0         RET     NZ              
78A6: E8 E8      ADD     SP,$E8          
78A8: C0         RET     NZ              
78A9: C0         RET     NZ              
78AA: FF         RST     0X38            
78AB: FF         RST     0X38            
78AC: E7         RST     0X20            
78AD: FF         RST     0X38            
78AE: E7         RST     0X20            
78AF: FF         RST     0X38            
78B0: E7         RST     0X20            
78B1: FF         RST     0X38            
78B2: FF         RST     0X38            
78B3: FF         RST     0X38            
78B4: 03         INC     BC              
78B5: 03         INC     BC              
78B6: 17         RLA                     
78B7: 17         RLA                     
78B8: C3 03 FF   JP      $FF03           
78BB: FF         RST     0X38            
78BC: E7         RST     0X20            
78BD: FF         RST     0X38            
78BE: E7         RST     0X20            
78BF: FF         RST     0X38            
78C0: F3         DI                      
78C1: F3         DI                      
78C2: F0 F0      LD      A,($F0)         
78C4: FF         RST     0X38            
78C5: F0 F7      LD      A,($F7)         
78C7: F8 FC      LDHL    SP,$FC          
78C9: FF         RST     0X38            
78CA: FF         RST     0X38            
78CB: FC         ???                     
78CC: FD         ???                     
78CD: FE FF      CP      $FF             
78CF: FF         RST     0X38            
78D0: CF         RST     0X08            
78D1: CF         RST     0X08            
78D2: 0F         RRCA                    
78D3: 0F         RRCA                    
78D4: FF         RST     0X38            
78D5: 0F         RRCA                    
78D6: EF         RST     0X28            
78D7: 1F         RRA                     
78D8: 3F         CCF                     
78D9: FF         RST     0X38            
78DA: FF         RST     0X38            
78DB: 3F         CCF                     
78DC: BF         CP      A               
78DD: 7F         LD      A,A             
78DE: FF         RST     0X38            
78DF: FF         RST     0X38            
78E0: FF         RST     0X38            
78E1: FF         RST     0X38            
78E2: C0         RET     NZ              
78E3: 80         ADD     A,B             
78E4: BF         CP      A               
78E5: 80         ADD     A,B             
78E6: AF         XOR     A               
78E7: 90         SUB     B               
78E8: AD         XOR     L               
78E9: 82         ADD     A,D             
78EA: FF         RST     0X38            
78EB: 80         ADD     A,B             
78EC: 9C         SBC     H               
78ED: E3         ???                     
78EE: C0         RET     NZ              
78EF: FF         RST     0X38            
78F0: FF         RST     0X38            
78F1: FF         RST     0X38            
78F2: E1         POP     HL              
78F3: 03         INC     BC              
78F4: 1F         RRA                     
78F5: 01 FF 01   LD      BC,$01FF        
78F8: F7         RST     0X30            
78F9: 09         ADD     HL,BC           
78FA: F7         RST     0X30            
78FB: 01 79 87   LD      BC,$8779        
78FE: 03         INC     BC              
78FF: FF         RST     0X38            
7900: 83         ADD     A,E             
7901: FC         ???                     
7902: E7         RST     0X20            
7903: F8 22      LDHL    SP,$22          
7905: FD         ???                     
7906: D0         RET     NC              
7907: 3F         CCF                     
7908: D1         POP     DE              
7909: 3F         CCF                     
790A: BE         CP      (HL)            
790B: 7F         LD      A,A             
790C: 2A         LD      A,(HLI)         
790D: F7         RST     0X30            
790E: 33         INC     SP              
790F: EF         RST     0X28            
7910: 83         ADD     A,E             
7911: 7F         LD      A,A             
7912: 07         RLCA                    
7913: FF         RST     0X38            
7914: 0C         INC     C               
7915: FF         RST     0X38            
7916: FB         EI                      
7917: FC         ???                     
7918: 5F         LD      E,A             
7919: B8         CP      B               
791A: 95         SUB     L               
791B: 7A         LD      A,D             
791C: 26 F9      LD      H,$F9           
791E: E4         ???                     
791F: FB         EI                      
7920: C3 FC E7   JP      $E7FC           
7923: F8 D2      LDHL    SP,$D2          
7925: FD         ???                     
7926: A8         XOR     B               
7927: DF         RST     0X18            
7928: B7         OR      A               
7929: 8F         ADC     A,A             
792A: 96         SUB     (HL)            
792B: 8F         ADC     A,A             
792C: DA 87 B3   JP      C,$B387         
792F: CF         RST     0X08            
7930: B9         CP      C               
7931: 47         LD      B,A             
7932: 33         INC     SP              
7933: CF         RST     0X08            
7934: 0F         RRCA                    
7935: FF         RST     0X38            
7936: F1         POP     AF              
7937: FF         RST     0X38            
7938: 4F         LD      C,A             
7939: B1         OR      C               
793A: 9B         SBC     E               
793B: 61         LD      H,C             
793C: 1B         DEC     DE              
793D: E1         POP     HL              
793E: CF         RST     0X08            
793F: F1         POP     AF              
7940: BE         CP      (HL)            
7941: C1         POP     BC              
7942: BE         CP      (HL)            
7943: C1         POP     BC              
7944: FD         ???                     
7945: C3 59 E7   JP      $E759           
7948: 63         LD      H,E             
7949: FF         RST     0X38            
794A: 3E FF      LD      A,$FF           
794C: 1C         INC     E               
794D: FF         RST     0X38            
794E: 00         NOP                     
794F: FF         RST     0X38            
7950: 83         ADD     A,E             
7951: FF         RST     0X38            
7952: 9F         SBC     A               
7953: E1         POP     HL              
7954: BF         CP      A               
7955: C1         POP     BC              
7956: BD         CP      L               
7957: C3 99 E7   JP      $E799           
795A: C3 FF 66   JP      $66FF           
795D: FF         RST     0X38            
795E: 3C         INC     A               
795F: FF         RST     0X38            
7960: BE         CP      (HL)            
7961: C1         POP     BC              
7962: BE         CP      (HL)            
7963: C1         POP     BC              
7964: FD         ???                     
7965: C3 D9 E7   JP      $E7D9           
7968: E3         ???                     
7969: FF         RST     0X38            
796A: FF         RST     0X38            
796B: FF         RST     0X38            
796C: FF         RST     0X38            
796D: FF         RST     0X38            
796E: FF         RST     0X38            
796F: FF         RST     0X38            
7970: 83         ADD     A,E             
7971: FF         RST     0X38            
7972: 9F         SBC     A               
7973: E1         POP     HL              
7974: BF         CP      A               
7975: C1         POP     BC              
7976: BD         CP      L               
7977: C3 99 E7   JP      $E799           
797A: C3 FF E7   JP      $E7FF           
797D: FF         RST     0X38            
797E: FF         RST     0X38            
797F: FF         RST     0X38            
7980: FF         RST     0X38            
7981: FF         RST     0X38            
7982: 17         RLA                     
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
7992: 86         ADD     A,(HL)          
7993: FF         RST     0X38            
7994: BF         CP      A               
7995: FF         RST     0X38            
7996: BF         CP      A               
7997: FF         RST     0X38            
7998: BF         CP      A               
7999: FF         RST     0X38            
799A: FF         RST     0X38            
799B: FF         RST     0X38            
799C: BF         CP      A               
799D: FF         RST     0X38            
799E: FF         RST     0X38            
799F: FF         RST     0X38            
79A0: FF         RST     0X38            
79A1: FF         RST     0X38            
79A2: FF         RST     0X38            
79A3: FF         RST     0X38            
79A4: FF         RST     0X38            
79A5: FF         RST     0X38            
79A6: F7         RST     0X30            
79A7: EF         RST     0X28            
79A8: FF         RST     0X38            
79A9: E0 E0      LDFF00  ($E0),A         
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
79B6: EF         RST     0X28            
79B7: F7         RST     0X30            
79B8: FF         RST     0X38            
79B9: 07         RLCA                    
79BA: 07         RLCA                    
79BB: FF         RST     0X38            
79BC: FF         RST     0X38            
79BD: FF         RST     0X38            
79BE: FF         RST     0X38            
79BF: FF         RST     0X38            
79C0: 18 FF      JR      $79C1           
79C2: 18 FF      JR      $79C3           
79C4: 3F         CCF                     
79C5: C0         RET     NZ              
79C6: 17         RLA                     
79C7: E8 3F      ADD     SP,$3F          
79C9: C0         RET     NZ              
79CA: 3F         CCF                     
79CB: FF         RST     0X38            
79CC: 18 FF      JR      $79CD           
79CE: 18 FF      JR      $79CF           
79D0: 18 FF      JR      $79D1           
79D2: 18 FF      JR      $79D3           
79D4: FC         ???                     
79D5: 03         INC     BC              
79D6: E8 17      ADD     SP,$17          
79D8: FC         ???                     
79D9: 03         INC     BC              
79DA: FC         ???                     
79DB: FF         RST     0X38            
79DC: 18 FF      JR      $79DD           
79DE: 18 FF      JR      $79DF           
79E0: FF         RST     0X38            
79E1: FF         RST     0X38            
79E2: E1         POP     HL              
79E3: 03         INC     BC              
79E4: 1F         RRA                     
79E5: 01 FF 01   LD      BC,$01FF        
79E8: F7         RST     0X30            
79E9: 09         ADD     HL,BC           
79EA: F7         RST     0X30            
79EB: 01 7D 83   LD      BC,$837D        
79EE: 83         ADD     A,E             
79EF: FF         RST     0X38            
79F0: FF         RST     0X38            
79F1: FF         RST     0X38            
79F2: C0         RET     NZ              
79F3: 80         ADD     A,B             
79F4: BF         CP      A               
79F5: 80         ADD     A,B             
79F6: AF         XOR     A               
79F7: 90         SUB     B               
79F8: AF         XOR     A               
79F9: 80         ADD     A,B             
79FA: BF         CP      A               
79FB: 80         ADD     A,B             
79FC: BC         CP      H               
79FD: C3 C1 FF   JP      $FFC1           
7A00: 8C         ADC     A,H             
7A01: F0 9C      LD      A,($9C)         
7A03: E0 E1      LDFF00  ($E1),A         
7A05: FE F0      CP      $F0             
7A07: C0         RET     NZ              
7A08: CE F0      ADC     $F0             
7A0A: CC F0 C4   CALL    Z,$C4F0         
7A0D: F8 C6      LDHL    SP,$C6          
7A0F: F8 79      LDHL    SP,$79          
7A11: 07         RLCA                    
7A12: 31 0F 87   LD      SP,$870F        
7A15: 7F         LD      A,A             
7A16: 0F         RRCA                    
7A17: 01 71 0F   LD      BC,$0F71        
7A1A: 21 1F 21   LD      HL,$211F        
7A1D: 1F         RRA                     
7A1E: 71         LD      (HL),C          
7A1F: 0F         RRCA                    
7A20: FF         RST     0X38            
7A21: FF         RST     0X38            
7A22: 40         LD      B,B             
7A23: 80         ADD     A,B             
7A24: 80         ADD     A,B             
7A25: 00         NOP                     
7A26: CC 00 7F   CALL    Z,$7F00         
7A29: 80         ADD     A,B             
7A2A: 00         NOP                     
7A2B: FF         RST     0X38            
7A2C: FF         RST     0X38            
7A2D: FF         RST     0X38            
7A2E: FF         RST     0X38            
7A2F: FF         RST     0X38            
7A30: FF         RST     0X38            
7A31: FF         RST     0X38            
7A32: 04         INC     B               
7A33: 03         INC     BC              
7A34: 02         LD      (BC),A          
7A35: 01 16 01   LD      BC,$0116        
7A38: FC         ???                     
7A39: 03         INC     BC              
7A3A: 01 FF FF   LD      BC,$FFFF        
7A3D: FF         RST     0X38            
7A3E: FF         RST     0X38            
7A3F: FF         RST     0X38            
7A40: 53         LD      D,E             
7A41: EF         RST     0X28            
7A42: CB F7      SET     1,E             
7A44: E7         RST     0X20            
7A45: FF         RST     0X38            
7A46: BC         CP      H               
7A47: FF         RST     0X38            
7A48: A7         AND     A               
7A49: FF         RST     0X38            
7A4A: 80         ADD     A,B             
7A4B: FF         RST     0X38            
7A4C: 91         SUB     C               
7A4D: FF         RST     0X38            
7A4E: C0         RET     NZ              
7A4F: FF         RST     0X38            
7A50: 9E         SBC     (HL)            
7A51: FF         RST     0X38            
7A52: 4F         LD      C,A             
7A53: BF         CP      A               
7A54: 6F         LD      L,A             
7A55: 9F         SBC     A               
7A56: 91         SUB     C               
7A57: FF         RST     0X38            
7A58: 61         LD      H,C             
7A59: FF         RST     0X38            
7A5A: 09         ADD     HL,BC           
7A5B: FF         RST     0X38            
7A5C: 83         ADD     A,E             
7A5D: FF         RST     0X38            
7A5E: 0F         RRCA                    
7A5F: FF         RST     0X38            
7A60: C0         RET     NZ              
7A61: FF         RST     0X38            
7A62: E5         PUSH    HL              
7A63: FF         RST     0X38            
7A64: F0 FF      LD      A,($FF)         
7A66: F8 FF      LDHL    SP,$FF          
7A68: E6 FF      AND     $FF             
7A6A: E0 FF      LDFF00  ($FF),A         
7A6C: F0 FF      LD      A,($FF)         
7A6E: FC         ???                     
7A6F: FF         RST     0X38            
7A70: 7F         LD      A,A             
7A71: FF         RST     0X38            
7A72: DF         RST     0X18            
7A73: FF         RST     0X38            
7A74: 1F         RRA                     
7A75: FF         RST     0X38            
7A76: 1F         RRA                     
7A77: FF         RST     0X38            
7A78: BF         CP      A               
7A79: FF         RST     0X38            
7A7A: 3F         CCF                     
7A7B: FF         RST     0X38            
7A7C: 7F         LD      A,A             
7A7D: FF         RST     0X38            
7A7E: BF         CP      A               
7A7F: FF         RST     0X38            
7A80: FD         ???                     
7A81: FE FA      CP      $FA             
7A83: FD         ???                     
7A84: F4         ???                     
7A85: FB         EI                      
7A86: C0         RET     NZ              
7A87: FF         RST     0X38            
7A88: D2 EF 80   JP      NC,$80EF        
7A8B: FF         RST     0X38            
7A8C: 39         ADD     HL,SP           
7A8D: FF         RST     0X38            
7A8E: F7         RST     0X30            
7A8F: FF         RST     0X38            
7A90: BF         CP      A               
7A91: 7F         LD      A,A             
7A92: DF         RST     0X18            
7A93: 3F         CCF                     
7A94: 6F         LD      L,A             
7A95: 9F         SBC     A               
7A96: 37         SCF                     
7A97: CF         RST     0X08            
7A98: 1B         DEC     DE              
7A99: E7         RST     0X20            
7A9A: 2B         DEC     HL              
7A9B: DF         RST     0X18            
7A9C: 5D         LD      E,L             
7A9D: BF         CP      A               
7A9E: 3F         CCF                     
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
7AAC: EB         ???                     
7AAD: F7         RST     0X30            
7AAE: E1         POP     HL              
7AAF: FF         RST     0X38            
7AB0: FF         RST     0X38            
7AB1: FF         RST     0X38            
7AB2: FF         RST     0X38            
7AB3: EF         RST     0X28            
7AB4: FF         RST     0X38            
7AB5: 7D         LD      A,L             
7AB6: E3         ???                     
7AB7: FF         RST     0X38            
7AB8: D5         PUSH    DE              
7AB9: E3         ???                     
7ABA: DD         ???                     
7ABB: E3         ???                     
7ABC: C3 FF EF   JP      $EFFF           
7ABF: FF         RST     0X38            
7AC0: 0D         DEC     C               
7AC1: 0E 0D      LD      C,$0D           
7AC3: 0E 0E      LD      C,$0E           
7AC5: 0F         RRCA                    
7AC6: 0A         LD      A,(BC)          
7AC7: 0F         RRCA                    
7AC8: 08 0F 09   LD      ($090F),SP      
7ACB: 0E 09      LD      C,$09           
7ACD: 0E 09      LD      C,$09           
7ACF: 0E D8      LD      C,$D8           
7AD1: 38 C8      JR      C,$7A9B         
7AD3: 38 C8      JR      C,$7A9D         
7AD5: 38 48      JR      C,$7B1F         
7AD7: B8         CP      B               
7AD8: 08 F8 28   LD      ($28F8),SP      
7ADB: F8 B8      LDHL    SP,$B8          
7ADD: 78         LD      A,B             
7ADE: F8 38      LDHL    SP,$38          
7AE0: 00         NOP                     
7AE1: 00         NOP                     
7AE2: 03         INC     BC              
7AE3: 03         INC     BC              
7AE4: 05         DEC     B               
7AE5: 06 09      LD      B,$09           
7AE7: 0E 08      LD      C,$08           
7AE9: 0F         RRCA                    
7AEA: 09         ADD     HL,BC           
7AEB: 0E 09      LD      C,$09           
7AED: 0E 09      LD      C,$09           
7AEF: 0E 00      LD      C,$00           
7AF1: 00         NOP                     
7AF2: E0 E0      LDFF00  ($E0),A         
7AF4: D0         RET     NC              
7AF5: 30 C8      JR      NC,$7ABF        
7AF7: 38 08      JR      C,$7B01         
7AF9: F8 28      LDHL    SP,$28          
7AFB: F8 B8      LDHL    SP,$B8          
7AFD: 78         LD      A,B             
7AFE: F8 38      LDHL    SP,$38          
7B00: CE F0      ADC     $F0             
7B02: CC F0 CC   CALL    Z,$CCF0         
7B05: F0 C6      LD      A,($C6)         
7B07: F8 F1      LDHL    SP,$F1          
7B09: FE E0      CP      $E0             
7B0B: 80         ADD     A,B             
7B0C: 9C         SBC     H               
7B0D: E0 8E      LDFF00  ($8E),A         
7B0F: F0 31      LD      A,($31)         
7B11: 0F         RRCA                    
7B12: 21 1F 61   LD      HL,$611F        
7B15: 1F         RRA                     
7B16: 71         LD      (HL),C          
7B17: 0F         RRCA                    
7B18: 8F         ADC     A,A             
7B19: 7F         LD      A,A             
7B1A: 0F         RRCA                    
7B1B: 01 31 0F   LD      BC,$0F31        
7B1E: 79         LD      A,C             
7B1F: 07         RLCA                    
7B20: EB         ???                     
7B21: 1C         INC     E               
7B22: 1C         INC     E               
7B23: EB         ???                     
7B24: 08 FF FF   LD      ($FFFF),SP      
7B27: FF         RST     0X38            
7B28: B0         OR      B               
7B29: CF         RST     0X08            
7B2A: C1         POP     BC              
7B2B: BE         CP      (HL)            
7B2C: 80         ADD     A,B             
7B2D: FF         RST     0X38            
7B2E: FF         RST     0X38            
7B2F: FF         RST     0X38            
7B30: EB         ???                     
7B31: 1C         INC     E               
7B32: 0C         INC     C               
7B33: FB         EI                      
7B34: 08 FF FF   LD      ($FFFF),SP      
7B37: FF         RST     0X38            
7B38: BE         CP      (HL)            
7B39: C1         POP     BC              
7B3A: C0         RET     NZ              
7B3B: BF         CP      A               
7B3C: 80         ADD     A,B             
7B3D: FF         RST     0X38            
7B3E: FF         RST     0X38            
7B3F: FF         RST     0X38            
7B40: E4         ???                     
7B41: FF         RST     0X38            
7B42: FF         RST     0X38            
7B43: FF         RST     0X38            
7B44: C8         RET     Z               
7B45: FF         RST     0X38            
7B46: C0         RET     NZ              
7B47: FF         RST     0X38            
7B48: C4 FF E0   CALL    NZ,$E0FF        
7B4B: FF         RST     0X38            
7B4C: DE FF      SBC     $FF             
7B4E: C0         RET     NZ              
7B4F: FF         RST     0X38            
7B50: 1F         RRA                     
7B51: FF         RST     0X38            
7B52: 47         LD      B,A             
7B53: FF         RST     0X38            
7B54: 07         RLCA                    
7B55: FF         RST     0X38            
7B56: 0F         RRCA                    
7B57: FF         RST     0X38            
7B58: 3F         CCF                     
7B59: FF         RST     0X38            
7B5A: 0F         RRCA                    
7B5B: FF         RST     0X38            
7B5C: 8F         ADC     A,A             
7B5D: FF         RST     0X38            
7B5E: 1F         RRA                     
7B5F: FF         RST     0X38            
7B60: F3         DI                      
7B61: FF         RST     0X38            
7B62: F0 FF      LD      A,($FF)         
7B64: F9         LD      SP,HL           
7B65: FF         RST     0X38            
7B66: FC         ???                     
7B67: FF         RST     0X38            
7B68: FB         EI                      
7B69: FF         RST     0X38            
7B6A: F8 FF      LDHL    SP,$FF          
7B6C: FC         ???                     
7B6D: FF         RST     0X38            
7B6E: FF         RST     0X38            
7B6F: FF         RST     0X38            
7B70: 3F         CCF                     
7B71: FF         RST     0X38            
7B72: 7F         LD      A,A             
7B73: FF         RST     0X38            
7B74: BF         CP      A               
7B75: FF         RST     0X38            
7B76: 7F         LD      A,A             
7B77: FF         RST     0X38            
7B78: FF         RST     0X38            
7B79: FF         RST     0X38            
7B7A: 7F         LD      A,A             
7B7B: FF         RST     0X38            
7B7C: FF         RST     0X38            
7B7D: FF         RST     0X38            
7B7E: FF         RST     0X38            
7B7F: FF         RST     0X38            
7B80: FF         RST     0X38            
7B81: 3F         CCF                     
7B82: 3F         CCF                     
7B83: DF         RST     0X18            
7B84: 0F         RRCA                    
7B85: FF         RST     0X38            
7B86: A7         AND     A               
7B87: FF         RST     0X38            
7B88: 17         RLA                     
7B89: FF         RST     0X38            
7B8A: AF         XOR     A               
7B8B: 7F         LD      A,A             
7B8C: 3F         CCF                     
7B8D: FF         RST     0X38            
7B8E: FF         RST     0X38            
7B8F: FF         RST     0X38            
7B90: FF         RST     0X38            
7B91: F0 F8      LD      A,($F8)         
7B93: E7         RST     0X20            
7B94: E4         ???                     
7B95: DB         ???                     
7B96: C2 BD 38   JP      NZ,$38BD        
7B99: FF         RST     0X38            
7B9A: FE FF      CP      $FF             
7B9C: FF         RST     0X38            
7B9D: FF         RST     0X38            
7B9E: FF         RST     0X38            
7B9F: FF         RST     0X38            
7BA0: FD         ???                     
7BA1: FF         RST     0X38            
7BA2: FB         EI                      
7BA3: FF         RST     0X38            
7BA4: FB         EI                      
7BA5: FF         RST     0X38            
7BA6: EF         RST     0X28            
7BA7: FF         RST     0X38            
7BA8: CD FF EB   CALL    $EBFF           
7BAB: DD         ???                     
7BAC: CC BB 00   CALL    Z,$00BB         
7BAF: FF         RST     0X38            
7BB0: F7         RST     0X30            
7BB1: FF         RST     0X38            
7BB2: F7         RST     0X30            
7BB3: FF         RST     0X38            
7BB4: 6F         LD      L,A             
7BB5: FF         RST     0X38            
7BB6: 2F         CPL                     
7BB7: FF         RST     0X38            
7BB8: 6F         LD      L,A             
7BB9: BF         CP      A               
7BBA: 49         LD      C,C             
7BBB: BF         CP      A               
7BBC: 41         LD      B,C             
7BBD: BF         CP      A               
7BBE: 00         NOP                     
7BBF: FF         RST     0X38            
7BC0: 0D         DEC     C               
7BC1: 0E 0D      LD      C,$0D           
7BC3: 0E 0E      LD      C,$0E           
7BC5: 0F         RRCA                    
7BC6: 0A         LD      A,(BC)          
7BC7: 0F         RRCA                    
7BC8: 08 0F 09   LD      ($090F),SP      
7BCB: 0E 09      LD      C,$09           
7BCD: 0E 09      LD      C,$09           
7BCF: 0E D8      LD      C,$D8           
7BD1: 38 C8      JR      C,$7B9B         
7BD3: 38 C8      JR      C,$7B9D         
7BD5: 38 48      JR      C,$7C1F         
7BD7: B8         CP      B               
7BD8: 08 F8 28   LD      ($28F8),SP      
7BDB: F8 B8      LDHL    SP,$B8          
7BDD: 78         LD      A,B             
7BDE: F8 38      LDHL    SP,$38          
7BE0: 0D         DEC     C               
7BE1: 0E 0D      LD      C,$0D           
7BE3: 0E 0E      LD      C,$0E           
7BE5: 0F         RRCA                    
7BE6: 0A         LD      A,(BC)          
7BE7: 0F         RRCA                    
7BE8: 08 0F 09   LD      ($090F),SP      
7BEB: 0E 09      LD      C,$09           
7BED: 0E 09      LD      C,$09           
7BEF: 0E D8      LD      C,$D8           
7BF1: 38 C8      JR      C,$7BBB         
7BF3: 38 C8      JR      C,$7BBD         
7BF5: 38 48      JR      C,$7C3F         
7BF7: B8         CP      B               
7BF8: 08 F8 28   LD      ($28F8),SP      
7BFB: F8 B8      LDHL    SP,$B8          
7BFD: 78         LD      A,B             
7BFE: F8 38      LDHL    SP,$38          
7C00: FF         RST     0X38            
7C01: FF         RST     0X38            
7C02: FF         RST     0X38            
7C03: F0 F3      LD      A,($F3)         
7C05: E0 E7      LDFF00  ($E7),A         
7C07: C0         RET     NZ              
7C08: FF         RST     0X38            
7C09: C6 FF      ADD     $FF             
7C0B: D6 FF      SUB     $FF             
7C0D: D2 FF C8   JP      NC,$C8FF        
7C10: FF         RST     0X38            
7C11: FF         RST     0X38            
7C12: BF         CP      A               
7C13: 7F         LD      A,A             
7C14: DF         RST     0X18            
7C15: 3F         CCF                     
7C16: 7F         LD      A,A             
7C17: 9F         SBC     A               
7C18: FF         RST     0X38            
7C19: 1F         RRA                     
7C1A: FF         RST     0X38            
7C1B: 7F         LD      A,A             
7C1C: FF         RST     0X38            
7C1D: FF         RST     0X38            
7C1E: FF         RST     0X38            
7C1F: BF         CP      A               
7C20: EF         RST     0X28            
7C21: F0 ED      LD      A,($ED)         
7C23: F2         ???                     
7C24: F7         RST     0X30            
7C25: DB         ???                     
7C26: F7         RST     0X30            
7C27: DA DB FE   JP      C,$FEDB         
7C2A: DE F5      SBC     $F5             
7C2C: FF         RST     0X38            
7C2D: D1         POP     DE              
7C2E: FE D1      CP      $D1             
7C30: 7B         LD      A,E             
7C31: DF         RST     0X18            
7C32: BF         CP      A               
7C33: DB         ???                     
7C34: 6F         LD      L,A             
7C35: 9B         SBC     E               
7C36: EF         RST     0X28            
7C37: 1B         DEC     DE              
7C38: 6B         LD      L,E             
7C39: 9F         SBC     A               
7C3A: 5F         LD      E,A             
7C3B: BB         CP      E               
7C3C: DF         RST     0X18            
7C3D: B9         CP      C               
7C3E: EF         RST     0X28            
7C3F: FB         EI                      
7C40: FF         RST     0X38            
7C41: FE FC      CP      $FC             
7C43: FD         ???                     
7C44: F8 F9      LDHL    SP,$F9          
7C46: FB         EI                      
7C47: F9         LD      SP,HL           
7C48: FF         RST     0X38            
7C49: F9         LD      SP,HL           
7C4A: FB         EI                      
7C4B: FC         ???                     
7C4C: FC         ???                     
7C4D: FE FE      CP      $FE             
7C4F: FE 7F      CP      $7F             
7C51: FF         RST     0X38            
7C52: 3F         CCF                     
7C53: FF         RST     0X38            
7C54: 5F         LD      E,A             
7C55: BF         CP      A               
7C56: FF         RST     0X38            
7C57: 9F         SBC     A               
7C58: FF         RST     0X38            
7C59: 9F         SBC     A               
7C5A: 5F         LD      E,A             
7C5B: BF         CP      A               
7C5C: 3F         CCF                     
7C5D: FF         RST     0X38            
7C5E: 7F         LD      A,A             
7C5F: FF         RST     0X38            
7C60: FF         RST     0X38            
7C61: FF         RST     0X38            
7C62: C0         RET     NZ              
7C63: C0         RET     NZ              
7C64: B8         CP      B               
7C65: C7         RST     0X00            
7C66: B3         OR      E               
7C67: CC A7 D8   CALL    Z,$D8A7         
7C6A: C0         RET     NZ              
7C6B: FF         RST     0X38            
7C6C: FF         RST     0X38            
7C6D: FF         RST     0X38            
7C6E: FF         RST     0X38            
7C6F: FF         RST     0X38            
7C70: FF         RST     0X38            
7C71: FF         RST     0X38            
7C72: 07         RLCA                    
7C73: 03         INC     BC              
7C74: CD 33 9D   CALL    $9D33           
7C77: 63         LD      H,E             
7C78: BD         CP      L               
7C79: 43         LD      B,E             
7C7A: 03         INC     BC              
7C7B: FF         RST     0X38            
7C7C: FF         RST     0X38            
7C7D: FF         RST     0X38            
7C7E: FF         RST     0X38            
7C7F: FF         RST     0X38            
7C80: 00         NOP                     
7C81: 00         NOP                     
7C82: 00         NOP                     
7C83: 00         NOP                     
7C84: 00         NOP                     
7C85: 01 00 07   LD      BC,$0700        
7C88: 03         INC     BC              
7C89: 0C         INC     C               
7C8A: 00         NOP                     
7C8B: 3F         CCF                     
7C8C: 18 60      JR      $7CEE           
7C8E: 30 C0      JR      NC,$7C50        
7C90: 00         NOP                     
7C91: 3C         INC     A               
7C92: 20 C6      JR      NZ,$7C5A        
7C94: 48         LD      C,B             
7C95: 86         ADD     A,(HL)          
7C96: 08 F6 30   LD      ($30F6),SP      
7C99: 0E 3C      LD      C,$3C           
7C9B: C3 4C 33   JP      $334C           
7C9E: F4         ???                     
7C9F: 0B         DEC     BC              
7CA0: 00         NOP                     
7CA1: FF         RST     0X38            
7CA2: 01 FE 31   LD      BC,$31FE        
7CA5: CE 20      ADC     $20             
7CA7: CF         RST     0X08            
7CA8: 28 C7      JR      Z,$7C71         
7CAA: 15         DEC     D               
7CAB: E2         LDFF00  (C),A           
7CAC: 08 F1 07   LD      ($07F1),SP      
7CAF: F8 00      LDHL    SP,$00          
7CB1: FF         RST     0X38            
7CB2: 80         ADD     A,B             
7CB3: 7F         LD      A,A             
7CB4: 0C         INC     C               
7CB5: 73         LD      (HL),E          
7CB6: 94         SUB     H               
7CB7: 63         LD      H,E             
7CB8: 28 C7      JR      Z,$7C81         
7CBA: 10 0F      STOP    $0F             
7CBC: 66         LD      H,(HL)          
7CBD: 99         SBC     C               
7CBE: 8A         ADC     A,D             
7CBF: 71         LD      (HL),C          
7CC0: FF         RST     0X38            
7CC1: FF         RST     0X38            
7CC2: FF         RST     0X38            
7CC3: FF         RST     0X38            
7CC4: FE FE      CP      $FE             
7CC6: FF         RST     0X38            
7CC7: FE FB      CP      $FB             
7CC9: F9         LD      SP,HL           
7CCA: 9C         SBC     H               
7CCB: 8B         ADC     A,E             
7CCC: 38 24      JR      C,$7CF2         
7CCE: 63         LD      H,E             
7CCF: 40         LD      B,B             
7CD0: F9         LD      SP,HL           
7CD1: F1         POP     AF              
7CD2: 37         SCF                     
7CD3: 23         INC     HL              
7CD4: BA         CP      D               
7CD5: 97         SUB     A               
7CD6: 36 1F      LD      (HL),$1F        
7CD8: FC         ???                     
7CD9: 3F         CCF                     
7CDA: EC         ???                     
7CDB: C7         RST     0X00            
7CDC: 06 03      LD      B,$03           
7CDE: CB 31      SET     1,E             
7CE0: FF         RST     0X38            
7CE1: F0 FF      LD      A,($FF)         
7CE3: C0         RET     NZ              
7CE4: BF         CP      A               
7CE5: D9         RETI                    
7CE6: BF         CP      A               
7CE7: D9         RETI                    
7CE8: BF         CP      A               
7CE9: C9         RET                     
7CEA: BF         CP      A               
7CEB: C0         RET     NZ              
7CEC: 9F         SBC     A               
7CED: EE FF      XOR     $FF             
7CEF: E4         ???                     
7CF0: DF         RST     0X18            
7CF1: 3F         CCF                     
7CF2: EF         RST     0X28            
7CF3: 1F         RRA                     
7CF4: F7         RST     0X30            
7CF5: CF         RST     0X08            
7CF6: F7         RST     0X30            
7CF7: CF         RST     0X08            
7CF8: F7         RST     0X30            
7CF9: 8F         ADC     A,A             
7CFA: E7         RST     0X20            
7CFB: 1F         RRA                     
7CFC: 8F         ADC     A,A             
7CFD: 7F         LD      A,A             
7CFE: 7F         LD      A,A             
7CFF: FF         RST     0X38            
7D00: FF         RST     0X38            
7D01: E1         POP     HL              
7D02: FF         RST     0X38            
7D03: F5         PUSH    AF              
7D04: EF         RST     0X28            
7D05: FE CF      CP      $CF             
7D07: F8 DF      LDHL    SP,$DF          
7D09: EF         RST     0X28            
7D0A: DF         RST     0X18            
7D0B: EA D6 E9   LD      ($E9D6),A       
7D0E: C9         RET                     
7D0F: F6 FF      OR      $FF             
7D11: BF         CP      A               
7D12: FF         RST     0X38            
7D13: BF         CP      A               
7D14: AF         XOR     A               
7D15: 7F         LD      A,A             
7D16: 4F         LD      C,A             
7D17: FB         EI                      
7D18: BF         CP      A               
7D19: D3         ???                     
7D1A: 5F         LD      E,A             
7D1B: BB         CP      E               
7D1C: EF         RST     0X28            
7D1D: 3B         DEC     SP              
7D1E: DF         RST     0X18            
7D1F: 7B         LD      A,E             
7D20: DE F7      SBC     $F7             
7D22: FE F5      CP      $F5             
7D24: F5         PUSH    AF              
7D25: FE F6      CP      $F6             
7D27: FF         RST     0X38            
7D28: FF         RST     0X38            
7D29: FE FD      CP      $FD             
7D2B: FE FE      CP      $FE             
7D2D: FD         ???                     
7D2E: FF         RST     0X38            
7D2F: FD         ???                     
7D30: EB         ???                     
7D31: DD         ???                     
7D32: FD         ???                     
7D33: DF         RST     0X18            
7D34: ED         ???                     
7D35: DF         RST     0X18            
7D36: DF         RST     0X18            
7D37: 6D         LD      L,L             
7D38: DF         RST     0X18            
7D39: 6D         LD      L,L             
7D3A: 7D         LD      A,L             
7D3B: CF         RST     0X08            
7D3C: EF         RST     0X28            
7D3D: DF         RST     0X18            
7D3E: DF         RST     0X18            
7D3F: FF         RST     0X38            
7D40: FF         RST     0X38            
7D41: FE FC      CP      $FC             
7D43: FD         ???                     
7D44: F8 F9      LDHL    SP,$F9          
7D46: FB         EI                      
7D47: F9         LD      SP,HL           
7D48: FF         RST     0X38            
7D49: F9         LD      SP,HL           
7D4A: FB         EI                      
7D4B: FC         ???                     
7D4C: FC         ???                     
7D4D: FE FE      CP      $FE             
7D4F: FE 7F      CP      $7F             
7D51: FF         RST     0X38            
7D52: 3F         CCF                     
7D53: FF         RST     0X38            
7D54: 5F         LD      E,A             
7D55: BF         CP      A               
7D56: FF         RST     0X38            
7D57: 9F         SBC     A               
7D58: FF         RST     0X38            
7D59: 9F         SBC     A               
7D5A: 5F         LD      E,A             
7D5B: BF         CP      A               
7D5C: 3F         CCF                     
7D5D: FF         RST     0X38            
7D5E: 7F         LD      A,A             
7D5F: FF         RST     0X38            
7D60: 11 FF 22   LD      DE,$22FF        
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
7D70: 11 FF 22   LD      DE,$22FF        
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
7D80: 3F         CCF                     
7D81: C0         RET     NZ              
7D82: 3C         INC     A               
7D83: C3 38 C7   JP      $C738           
7D86: 38 C7      JR      C,$7D4F         
7D88: 33         INC     SP              
7D89: CC 30 CF   CALL    Z,$CF30         
7D8C: 30 CC      JR      NC,$7D5A        
7D8E: 00         NOP                     
7D8F: F8 F8      LDHL    SP,$F8          
7D91: 07         RLCA                    
7D92: 3C         INC     A               
7D93: C3 0C F3   JP      $F30C           
7D96: 0C         INC     C               
7D97: F3         DI                      
7D98: F8 06      LDHL    SP,$06          
7D9A: 00         NOP                     
7D9B: FC         ???                     
7D9C: 00         NOP                     
7D9D: 00         NOP                     
7D9E: 00         NOP                     
7D9F: 00         NOP                     
7DA0: 00         NOP                     
7DA1: FF         RST     0X38            
7DA2: 40         LD      B,B             
7DA3: 9E         SBC     (HL)            
7DA4: 61         LD      H,C             
7DA5: 8E         ADC     A,(HL)          
7DA6: 32         LD      (HLD),A         
7DA7: C1         POP     BC              
7DA8: 1E E1      LD      E,$E1           
7DAA: 00         NOP                     
7DAB: FF         RST     0X38            
7DAC: 02         LD      (BC),A          
7DAD: FD         ???                     
7DAE: 04         INC     B               
7DAF: F8 14      LDHL    SP,$14          
7DB1: E3         ???                     
7DB2: B8         CP      B               
7DB3: 47         LD      B,A             
7DB4: F0 0F      LD      A,($0F)         
7DB6: C2 39 12   JP      NZ,$1239        
7DB9: E1         POP     HL              
7DBA: FC         ???                     
7DBB: 03         INC     BC              
7DBC: 00         NOP                     
7DBD: FF         RST     0X38            
7DBE: C0         RET     NZ              
7DBF: 3F         CCF                     
7DC0: DD         ???                     
7DC1: 03         INC     BC              
7DC2: 77         LD      (HL),A          
7DC3: 8F         ADC     A,A             
7DC4: 9E         SBC     (HL)            
7DC5: FF         RST     0X38            
7DC6: FD         ???                     
7DC7: F6 FF      OR      $FF             
7DC9: F4         ???                     
7DCA: FF         RST     0X38            
7DCB: FF         RST     0X38            
7DCC: D0         RET     NC              
7DCD: E0 E0      LDFF00  ($E0),A         
7DCF: FF         RST     0X38            
7DD0: F3         DI                      
7DD1: F9         LD      SP,HL           
7DD2: D5         PUSH    DE              
7DD3: FB         EI                      
7DD4: B5         OR      L               
7DD5: DB         ???                     
7DD6: FB         EI                      
7DD7: 97         SUB     A               
7DD8: FB         EI                      
7DD9: E7         RST     0X20            
7DDA: F4         ???                     
7DDB: CF         RST     0X08            
7DDC: E8 1F      ADD     SP,$1F          
7DDE: 1F         RRA                     
7DDF: FF         RST     0X38            
7DE0: FF         RST     0X38            
7DE1: 20 3F      JR      NZ,$7E22        
7DE3: D4 0F FF   CALL    NC,$FF0F        
7DE6: A7         AND     A               
7DE7: FF         RST     0X38            
7DE8: 17         RLA                     
7DE9: FF         RST     0X38            
7DEA: AF         XOR     A               
7DEB: 7F         LD      A,A             
7DEC: 3F         CCF                     
7DED: FF         RST     0X38            
7DEE: FF         RST     0X38            
7DEF: FF         RST     0X38            
7DF0: FF         RST     0X38            
7DF1: F0 F8      LD      A,($F8)         
7DF3: E7         RST     0X20            
7DF4: E4         ???                     
7DF5: DB         ???                     
7DF6: C2 BD 38   JP      NZ,$38BD        
7DF9: FF         RST     0X38            
7DFA: FE FF      CP      $FF             
7DFC: FF         RST     0X38            
7DFD: FF         RST     0X38            
7DFE: FF         RST     0X38            
7DFF: FF         RST     0X38            
7E00: FF         RST     0X38            
7E01: FF         RST     0X38            
7E02: C0         RET     NZ              
7E03: 7F         LD      A,A             
7E04: E0 7F      LDFF00  ($7F),A         
7E06: B8         CP      B               
7E07: FF         RST     0X38            
7E08: 8F         ADC     A,A             
7E09: FF         RST     0X38            
7E0A: C0         RET     NZ              
7E0B: FF         RST     0X38            
7E0C: 60         LD      H,B             
7E0D: FF         RST     0X38            
7E0E: 38 FF      JR      C,$7E0F         
7E10: FF         RST     0X38            
7E11: FF         RST     0X38            
7E12: 06 FC      LD      B,$FC           
7E14: 0F         RRCA                    
7E15: FC         ???                     
7E16: 3B         DEC     SP              
7E17: FF         RST     0X38            
7E18: E3         ???                     
7E19: FF         RST     0X38            
7E1A: 07         RLCA                    
7E1B: FF         RST     0X38            
7E1C: 0D         DEC     C               
7E1D: FF         RST     0X38            
7E1E: 39         ADD     HL,SP           
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
7E42: 7F         LD      A,A             
7E43: 80         ADD     A,B             
7E44: 1F         RRA                     
7E45: 87         ADD     A,A             
7E46: 78         LD      A,B             
7E47: 88         ADC     A,B             
7E48: 14         INC     D               
7E49: F3         DI                      
7E4A: 73         LD      (HL),E          
7E4B: 97         SUB     A               
7E4C: 77         LD      (HL),A          
7E4D: 97         SUB     A               
7E4E: 17         RLA                     
7E4F: F7         RST     0X30            
7E50: FF         RST     0X38            
7E51: FF         RST     0X38            
7E52: FE 01      CP      $01             
7E54: F8 E1      LDHL    SP,$E1          
7E56: 1E 11      LD      E,$11           
7E58: 2C         INC     L               
7E59: CB CE      SET     1,E             
7E5B: E9         JP      (HL)            
7E5C: EE E9      XOR     $E9             
7E5E: E8 EF      ADD     SP,$EF          
7E60: FF         RST     0X38            
7E61: FF         RST     0X38            
7E62: FF         RST     0X38            
7E63: 1C         INC     E               
7E64: 0C         INC     C               
7E65: FB         EI                      
7E66: 0C         INC     C               
7E67: FB         EI                      
7E68: 0C         INC     C               
7E69: FF         RST     0X38            
7E6A: FF         RST     0X38            
7E6B: FF         RST     0X38            
7E6C: BD         CP      L               
7E6D: C3 C1 BF   JP      $BFC1           
7E70: FF         RST     0X38            
7E71: FF         RST     0X38            
7E72: F7         RST     0X30            
7E73: 38 58      JR      C,$7ECD         
7E75: F7         RST     0X30            
7E76: 18 F7      JR      $7E6F           
7E78: 10 FF      STOP    $FF             
7E7A: FF         RST     0X38            
7E7B: FF         RST     0X38            
7E7C: 7F         LD      A,A             
7E7D: 81         ADD     A,C             
7E7E: 81         ADD     A,C             
7E7F: 7F         LD      A,A             
7E80: FF         RST     0X38            
7E81: FF         RST     0X38            
7E82: 7F         LD      A,A             
7E83: 80         ADD     A,B             
7E84: 90         SUB     B               
7E85: 00         NOP                     
7E86: FF         RST     0X38            
7E87: 00         NOP                     
7E88: 07         RLCA                    
7E89: FB         EI                      
7E8A: FE 02      CP      $02             
7E8C: 63         LD      H,E             
7E8D: 9F         SBC     A               
7E8E: 1F         RRA                     
7E8F: E0 FF      LDFF00  ($FF),A         
7E91: FF         RST     0X38            
7E92: FE 01      CP      $01             
7E94: C1         POP     BC              
7E95: 00         NOP                     
7E96: FF         RST     0X38            
7E97: 00         NOP                     
7E98: B4         OR      H               
7E99: CB FF      SET     1,E             
7E9B: 80         ADD     A,B             
7E9C: 8E         ADC     A,(HL)          
7E9D: F1         POP     AF              
7E9E: F0 0F      LD      A,($0F)         
7EA0: 9F         SBC     A               
7EA1: 8F         ADC     A,A             
7EA2: EC         ???                     
7EA3: C4 5D E9   CALL    NZ,$E95D        
7EA6: 6C         LD      L,H             
7EA7: F8 3F      LDHL    SP,$3F          
7EA9: FC         ???                     
7EAA: 37         SCF                     
7EAB: E3         ???                     
7EAC: 60         LD      H,B             
7EAD: C0         RET     NZ              
7EAE: D3         ???                     
7EAF: 8C         ADC     A,H             
7EB0: FF         RST     0X38            
7EB1: FF         RST     0X38            
7EB2: FF         RST     0X38            
7EB3: FF         RST     0X38            
7EB4: 7F         LD      A,A             
7EB5: 7F         LD      A,A             
7EB6: FF         RST     0X38            
7EB7: 7F         LD      A,A             
7EB8: DF         RST     0X18            
7EB9: 9F         SBC     A               
7EBA: 39         ADD     HL,SP           
7EBB: D1         POP     DE              
7EBC: 1C         INC     E               
7EBD: 24         INC     H               
7EBE: C6 02      ADD     $02             
7EC0: 00         NOP                     
7EC1: FF         RST     0X38            
7EC2: 00         NOP                     
7EC3: FF         RST     0X38            
7EC4: 00         NOP                     
7EC5: FF         RST     0X38            
7EC6: 00         NOP                     
7EC7: FF         RST     0X38            
7EC8: 00         NOP                     
7EC9: FF         RST     0X38            
7ECA: 00         NOP                     
7ECB: FF         RST     0X38            
7ECC: 00         NOP                     
7ECD: FF         RST     0X38            
7ECE: 00         NOP                     
7ECF: FF         RST     0X38            
7ED0: 00         NOP                     
7ED1: FF         RST     0X38            
7ED2: 00         NOP                     
7ED3: FF         RST     0X38            
7ED4: 00         NOP                     
7ED5: FF         RST     0X38            
7ED6: 00         NOP                     
7ED7: FF         RST     0X38            
7ED8: 00         NOP                     
7ED9: FF         RST     0X38            
7EDA: 00         NOP                     
7EDB: FF         RST     0X38            
7EDC: 00         NOP                     
7EDD: FF         RST     0X38            
7EDE: 00         NOP                     
7EDF: FF         RST     0X38            
7EE0: 00         NOP                     
7EE1: FF         RST     0X38            
7EE2: 00         NOP                     
7EE3: FF         RST     0X38            
7EE4: 00         NOP                     
7EE5: FF         RST     0X38            
7EE6: 00         NOP                     
7EE7: FF         RST     0X38            
7EE8: 00         NOP                     
7EE9: FF         RST     0X38            
7EEA: 00         NOP                     
7EEB: FF         RST     0X38            
7EEC: 00         NOP                     
7EED: FF         RST     0X38            
7EEE: 00         NOP                     
7EEF: FF         RST     0X38            
7EF0: 00         NOP                     
7EF1: FF         RST     0X38            
7EF2: 00         NOP                     
7EF3: FF         RST     0X38            
7EF4: 00         NOP                     
7EF5: FF         RST     0X38            
7EF6: 00         NOP                     
7EF7: FF         RST     0X38            
7EF8: 00         NOP                     
7EF9: FF         RST     0X38            
7EFA: 00         NOP                     
7EFB: FF         RST     0X38            
7EFC: 00         NOP                     
7EFD: FF         RST     0X38            
7EFE: 00         NOP                     
7EFF: FF         RST     0X38            
7F00: 0F         RRCA                    
7F01: FF         RST     0X38            
7F02: 80         ADD     A,B             
7F03: FF         RST     0X38            
7F04: E0 FF      LDFF00  ($FF),A         
7F06: 7F         LD      A,A             
7F07: FF         RST     0X38            
7F08: DF         RST     0X18            
7F09: 3F         CCF                     
7F0A: FF         RST     0X38            
7F0B: 00         NOP                     
7F0C: E1         POP     HL              
7F0D: 00         NOP                     
7F0E: 80         ADD     A,B             
7F0F: 00         NOP                     
7F10: E1         POP     HL              
7F11: FF         RST     0X38            
7F12: 03         INC     BC              
7F13: FF         RST     0X38            
7F14: 0F         RRCA                    
7F15: FF         RST     0X38            
7F16: FD         ???                     
7F17: FE F7      CP      $F7             
7F19: F8 FF      LDHL    SP,$FF          
7F1B: 00         NOP                     
7F1C: FF         RST     0X38            
7F1D: 00         NOP                     
7F1E: 7F         LD      A,A             
7F1F: 00         NOP                     
7F20: FF         RST     0X38            
7F21: FF         RST     0X38            
7F22: DD         ???                     
7F23: FF         RST     0X38            
7F24: FF         RST     0X38            
7F25: DD         ???                     
7F26: DD         ???                     
7F27: DD         ???                     
7F28: 99         SBC     C               
7F29: DD         ???                     
7F2A: DD         ???                     
7F2B: 99         SBC     C               
7F2C: DD         ???                     
7F2D: 99         SBC     C               
7F2E: FF         RST     0X38            
7F2F: FF         RST     0X38            
7F30: FF         RST     0X38            
7F31: FF         RST     0X38            
7F32: DD         ???                     
7F33: FF         RST     0X38            
7F34: FF         RST     0X38            
7F35: DD         ???                     
7F36: DD         ???                     
7F37: DD         ???                     
7F38: 99         SBC     C               
7F39: DD         ???                     
7F3A: DD         ???                     
7F3B: 99         SBC     C               
7F3C: DD         ???                     
7F3D: 99         SBC     C               
7F3E: FF         RST     0X38            
7F3F: FF         RST     0X38            
7F40: 77         LD      (HL),A          
7F41: 97         SUB     A               
7F42: 57         LD      D,A             
7F43: B7         OR      A               
7F44: 7B         LD      A,E             
7F45: 93         SUB     E               
7F46: 0C         INC     C               
7F47: F8 3F      LDHL    SP,$3F          
7F49: FF         RST     0X38            
7F4A: 80         ADD     A,B             
7F4B: FF         RST     0X38            
7F4C: FF         RST     0X38            
7F4D: FF         RST     0X38            
7F4E: FF         RST     0X38            
7F4F: FF         RST     0X38            
7F50: EE E9      XOR     $E9             
7F52: EE E9      XOR     $E9             
7F54: D8         RET     C               
7F55: CF         RST     0X08            
7F56: 30 1F      JR      NC,$7F77        
7F58: FC         ???                     
7F59: FF         RST     0X38            
7F5A: 03         INC     BC              
7F5B: FF         RST     0X38            
7F5C: FF         RST     0X38            
7F5D: FF         RST     0X38            
7F5E: FF         RST     0X38            
7F5F: FF         RST     0X38            
7F60: C1         POP     BC              
7F61: BF         CP      A               
7F62: 81         ADD     A,C             
7F63: FF         RST     0X38            
7F64: FF         RST     0X38            
7F65: FF         RST     0X38            
7F66: EB         ???                     
7F67: 1C         INC     E               
7F68: 1C         INC     E               
7F69: EB         ???                     
7F6A: 0C         INC     C               
7F6B: FB         EI                      
7F6C: 0C         INC     C               
7F6D: FF         RST     0X38            
7F6E: FF         RST     0X38            
7F6F: FF         RST     0X38            
7F70: 81         ADD     A,C             
7F71: 7F         LD      A,A             
7F72: 01 FF FF   LD      BC,$FFFF        
7F75: FF         RST     0X38            
7F76: EB         ???                     
7F77: 1C         INC     E               
7F78: 0C         INC     C               
7F79: FB         EI                      
7F7A: 0C         INC     C               
7F7B: FB         EI                      
7F7C: 18 FF      JR      $7F7D           
7F7E: FF         RST     0X38            
7F7F: FF         RST     0X38            
7F80: FF         RST     0X38            
7F81: 00         NOP                     
7F82: C3 3F 7E   JP      $7E3F           
7F85: 82         ADD     A,D             
7F86: 03         INC     BC              
7F87: FF         RST     0X38            
7F88: 3C         INC     A               
7F89: FF         RST     0X38            
7F8A: 80         ADD     A,B             
7F8B: FF         RST     0X38            
7F8C: FF         RST     0X38            
7F8D: FF         RST     0X38            
7F8E: FF         RST     0X38            
7F8F: FF         RST     0X38            
7F90: FF         RST     0X38            
7F91: 00         NOP                     
7F92: 8E         ADC     A,(HL)          
7F93: F1         POP     AF              
7F94: F0 8F      LD      A,($8F)         
7F96: 80         ADD     A,B             
7F97: FF         RST     0X38            
7F98: 7C         LD      A,H             
7F99: FF         RST     0X38            
7F9A: 03         INC     BC              
7F9B: FF         RST     0X38            
7F9C: FF         RST     0X38            
7F9D: FF         RST     0X38            
7F9E: FF         RST     0X38            
7F9F: FF         RST     0X38            
7FA0: CF         RST     0X08            
7FA1: 9F         SBC     A               
7FA2: AB         XOR     E               
7FA3: DF         RST     0X18            
7FA4: AD         XOR     L               
7FA5: DB         ???                     
7FA6: DF         RST     0X18            
7FA7: E9         JP      (HL)            
7FA8: DF         RST     0X18            
7FA9: E7         RST     0X20            
7FAA: 2F         CPL                     
7FAB: F3         DI                      
7FAC: 17         RLA                     
7FAD: F8 F8      LDHL    SP,$F8          
7FAF: FF         RST     0X38            
7FB0: BB         CP      E               
7FB1: C0         RET     NZ              
7FB2: EE F1      XOR     $F1             
7FB4: 79         LD      A,C             
7FB5: FF         RST     0X38            
7FB6: BF         CP      A               
7FB7: 6F         LD      L,A             
7FB8: FF         RST     0X38            
7FB9: 2F         CPL                     
7FBA: FF         RST     0X38            
7FBB: FF         RST     0X38            
7FBC: 0B         DEC     BC              
7FBD: 07         RLCA                    
7FBE: 07         RLCA                    
7FBF: FF         RST     0X38            
7FC0: FF         RST     0X38            
7FC1: 00         NOP                     
7FC2: FF         RST     0X38            
7FC3: 00         NOP                     
7FC4: FF         RST     0X38            
7FC5: 00         NOP                     
7FC6: FF         RST     0X38            
7FC7: 00         NOP                     
7FC8: FF         RST     0X38            
7FC9: 00         NOP                     
7FCA: FF         RST     0X38            
7FCB: 00         NOP                     
7FCC: FF         RST     0X38            
7FCD: 00         NOP                     
7FCE: FF         RST     0X38            
7FCF: 00         NOP                     
7FD0: 00         NOP                     
7FD1: FF         RST     0X38            
7FD2: 00         NOP                     
7FD3: FF         RST     0X38            
7FD4: 00         NOP                     
7FD5: FF         RST     0X38            
7FD6: 00         NOP                     
7FD7: FF         RST     0X38            
7FD8: 00         NOP                     
7FD9: FF         RST     0X38            
7FDA: 00         NOP                     
7FDB: FF         RST     0X38            
7FDC: 00         NOP                     
7FDD: FF         RST     0X38            
7FDE: 00         NOP                     
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
7FF0: 00         NOP                     
7FF1: 00         NOP                     
7FF2: 00         NOP                     
7FF3: 00         NOP                     
7FF4: 00         NOP                     
7FF5: 00         NOP                     
7FF6: 00         NOP                     
7FF7: 00         NOP                     
7FF8: 00         NOP                     
7FF9: 00         NOP                     
7FFA: 00         NOP                     
7FFB: 00         NOP                     
7FFC: 00         NOP                     
7FFD: 00         NOP                     
7FFE: 00         NOP                     
7FFF: 00         NOP                     
```
