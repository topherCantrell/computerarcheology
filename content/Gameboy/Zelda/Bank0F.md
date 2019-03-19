![Bank 0F](GBZelda.jpg)

# Bank 0F

>>> cpu Z80GB

>>> memoryTable ram 
[RAM Usage](RAMUse.md)

>>> memoryTable hard 
[Hardware Info](../Hardware.md)

```
4000: 87         ADD     A,A             
4001: 87         ADD     A,A             
4002: 01 01 C0   LD      BC,$C001        
4005: C0         RET     NZ              
4006: 9C         SBC     H               
4007: 9C         SBC     H               
4008: 9C         SBC     H               
4009: 9C         SBC     H               
400A: 18 18      JR      $4024           
400C: 81         ADD     A,C             
400D: 81         ADD     A,C             
400E: 83         ADD     A,E             
400F: 83         ADD     A,E             
4010: E7         RST     0X20            
4011: E7         RST     0X20            
4012: CF         RST     0X08            
4013: CF         RST     0X08            
4014: C9         RET                     
4015: CF         RST     0X08            
4016: 89         ADC     A,C             
4017: 8F         ADC     A,A             
4018: 99         SBC     C               
4019: 9F         SBC     A               
401A: 93         SUB     E               
401B: 9F         SBC     A               
401C: 12         LD      (DE),A          
401D: 1E 1F      LD      E,$1F           
401F: 1F         RRA                     
4020: C7         RST     0X00            
4021: C7         RST     0X00            
4022: C3 C3 83   JP      $83C3           
4025: 83         ADD     A,E             
4026: 93         SUB     E               
4027: 93         SUB     E               
4028: B3         OR      E               
4029: B3         OR      E               
402A: 31 31 01   LD      SP,$0131        
402D: 01 03 03   LD      BC,$0303        
4030: B9         CP      C               
4031: B9         CP      C               
4032: 39         ADD     HL,SP           
4033: 39         ADD     HL,SP           
4034: 31 31 31   LD      SP,$3131        
4037: 31 02 02   LD      SP,$0202        
403A: 02         LD      (BC),A          
403B: 02         LD      (BC),A          
403C: 86         ADD     A,(HL)          
403D: 86         ADD     A,(HL)          
403E: E6 E6      AND     $E6             
4040: 83         ADD     A,E             
4041: 83         ADD     A,E             
4042: 02         LD      (BC),A          
4043: 02         LD      (BC),A          
4044: 1F         RRA                     
4045: 1F         RRA                     
4046: 31 3F 1F   LD      SP,$1F3F        
4049: 1F         RRA                     
404A: 03         INC     BC              
404B: 03         INC     BC              
404C: 07         RLCA                    
404D: 07         RLCA                    
404E: 3F         CCF                     
404F: 3F         CCF                     
4050: FF         RST     0X38            
4051: FF         RST     0X38            
4052: D4 DC 9C   CALL    NC,$9CDC        
4055: 9C         SBC     H               
4056: 98         SBC     B               
4057: 98         SBC     B               
4058: 98         SBC     B               
4059: 98         SBC     B               
405A: 81         ADD     A,C             
405B: 81         ADD     A,C             
405C: 81         ADD     A,C             
405D: 81         ADD     A,C             
405E: C3 C3 FF   JP      $FFC3           
4061: FF         RST     0X38            
4062: F3         DI                      
4063: F3         DI                      
4064: C3 C3 C3   JP      $C3C3           
4067: C3 81 81   JP      $8181           
406A: 9D         SBC     L               
406B: 9D         SBC     L               
406C: 1D         DEC     E               
406D: 1D         DEC     E               
406E: 39         ADD     HL,SP           
406F: 39         ADD     HL,SP           
4070: FF         RST     0X38            
4071: FF         RST     0X38            
4072: AA         XOR     D               
4073: BA         CP      D               
4074: 32         LD      (HLD),A         
4075: 32         LD      (HLD),A         
4076: 32         LD      (HLD),A         
4077: 32         LD      (HLD),A         
4078: 32         LD      (HLD),A         
4079: 32         LD      (HLD),A         
407A: 32         LD      (HLD),A         
407B: 32         LD      (HLD),A         
407C: 32         LD      (HLD),A         
407D: 32         LD      (HLD),A         
407E: 32         LD      (HLD),A         
407F: 32         LD      (HLD),A         
4080: FF         RST     0X38            
4081: FF         RST     0X38            
4082: 1B         DEC     DE              
4083: 1F         RRA                     
4084: 0D         DEC     C               
4085: 0F         RRCA                    
4086: 45         LD      B,L             
4087: 47         LD      B,A             
4088: 65         LD      H,L             
4089: 67         LD      H,A             
408A: 65         LD      H,L             
408B: 67         LD      H,A             
408C: 0D         DEC     C               
408D: 0F         RRCA                    
408E: 3F         CCF                     
408F: 3F         CCF                     
4090: 0F         RRCA                    
4091: 0F         RRCA                    
4092: 03         INC     BC              
4093: 03         INC     BC              
4094: 31 31 39   LD      SP,$3931        
4097: 39         ADD     HL,SP           
4098: 31 31 03   LD      SP,$0331        
409B: 03         INC     BC              
409C: 1F         RRA                     
409D: 1F         RRA                     
409E: 0F         RRCA                    
409F: 0F         RRCA                    
40A0: 1F         RRA                     
40A1: 1F         RRA                     
40A2: 0F         RRCA                    
40A3: 0F         RRCA                    
40A4: 83         ADD     A,E             
40A5: 83         ADD     A,E             
40A6: E1         POP     HL              
40A7: E1         POP     HL              
40A8: F1         POP     AF              
40A9: F1         POP     AF              
40AA: 03         INC     BC              
40AB: 03         INC     BC              
40AC: 87         ADD     A,A             
40AD: 87         ADD     A,A             
40AE: FF         RST     0X38            
40AF: FF         RST     0X38            
40B0: 0F         RRCA                    
40B1: 0F         RRCA                    
40B2: 01 01 03   LD      BC,$0301        
40B5: 03         INC     BC              
40B6: 1F         RRA                     
40B7: 1F         RRA                     
40B8: 1F         RRA                     
40B9: 1F         RRA                     
40BA: 01 01 43   LD      BC,$4301        
40BD: 43         LD      B,E             
40BE: FF         RST     0X38            
40BF: FF         RST     0X38            
40C0: 9F         SBC     A               
40C1: 9F         SBC     A               
40C2: 99         SBC     C               
40C3: 9F         SBC     A               
40C4: 19         ADD     HL,DE           
40C5: 1F         RRA                     
40C6: 1F         RRA                     
40C7: 1F         RRA                     
40C8: 19         ADD     HL,DE           
40C9: 19         ADD     HL,DE           
40CA: 01 01 87   LD      BC,$8701        
40CD: 87         ADD     A,A             
40CE: FF         RST     0X38            
40CF: FF         RST     0X38            
40D0: 0F         RRCA                    
40D1: 0F         RRCA                    
40D2: 01 01 03   LD      BC,$0301        
40D5: 03         INC     BC              
40D6: 1F         RRA                     
40D7: 1F         RRA                     
40D8: 1F         RRA                     
40D9: 1F         RRA                     
40DA: 01 01 43   LD      BC,$4301        
40DD: 43         LD      B,E             
40DE: FF         RST     0X38            
40DF: FF         RST     0X38            
40E0: 1F         RRA                     
40E1: 1F         RRA                     
40E2: 30 3F      JR      NC,$4123        
40E4: 37         SCF                     
40E5: 3F         CCF                     
40E6: 1D         DEC     E               
40E7: 1D         DEC     E               
40E8: 01 01 81   LD      BC,$8101        
40EB: 81         ADD     A,C             
40EC: C3 C3 FF   JP      $FFC3           
40EF: FF         RST     0X38            
40F0: FF         RST     0X38            
40F1: FF         RST     0X38            
40F2: FF         RST     0X38            
40F3: C0         RET     NZ              
40F4: FC         ???                     
40F5: 83         ADD     A,E             
40F6: F8 87      LDHL    SP,$87          
40F8: E0 9F      LDFF00  ($9F),A         
40FA: E0 9F      LDFF00  ($9F),A         
40FC: F0 CF      LD      A,($CF)         
40FE: FF         RST     0X38            
40FF: FF         RST     0X38            
4100: 9F         SBC     A               
4101: 9F         SBC     A               
4102: 93         SUB     E               
4103: 9F         SBC     A               
4104: B1         OR      C               
4105: BF         CP      A               
4106: FF         RST     0X38            
4107: FF         RST     0X38            
4108: E3         ???                     
4109: E3         ???                     
410A: 81         ADD     A,C             
410B: 81         ADD     A,C             
410C: 01 01 0D   LD      BC,$0D01        
410F: 0D         DEC     C               
4110: 19         ADD     HL,DE           
4111: 19         ADD     HL,DE           
4112: 01 01 87   LD      BC,$8701        
4115: 87         ADD     A,A             
4116: FF         RST     0X38            
4117: FF         RST     0X38            
4118: C1         POP     BC              
4119: C1         POP     BC              
411A: 81         ADD     A,C             
411B: 81         ADD     A,C             
411C: 8F         ADC     A,A             
411D: 8F         ADC     A,A             
411E: 9F         SBC     A               
411F: 9F         SBC     A               
4120: 33         INC     SP              
4121: 33         INC     SP              
4122: 73         LD      (HL),E          
4123: 73         LD      (HL),E          
4124: 57         LD      D,A             
4125: 77         LD      (HL),A          
4126: FD         ???                     
4127: FF         RST     0X38            
4128: 65         LD      H,L             
4129: E7         RST     0X20            
412A: 4D         LD      C,L             
412B: CF         RST     0X08            
412C: CD CF 8F   CALL    $8FCF           
412F: 8F         ADC     A,A             
4130: CE CE      ADC     $CE             
4132: 8A         ADC     A,D             
4133: 8E         ADC     A,(HL)          
4134: 9A         SBC     D               
4135: 9E         SBC     (HL)            
4136: FF         RST     0X38            
4137: FF         RST     0X38            
4138: C1         POP     BC              
4139: C1         POP     BC              
413A: 81         ADD     A,C             
413B: 81         ADD     A,C             
413C: 8F         ADC     A,A             
413D: 8F         ADC     A,A             
413E: 9F         SBC     A               
413F: 9F         SBC     A               
4140: 3F         CCF                     
4141: 3F         CCF                     
4142: 03         INC     BC              
4143: 03         INC     BC              
4144: 87         ADD     A,A             
4145: 87         ADD     A,A             
4146: FF         RST     0X38            
4147: FF         RST     0X38            
4148: 71         LD      (HL),C          
4149: F1         POP     AF              
414A: C1         POP     BC              
414B: C1         POP     BC              
414C: 81         ADD     A,C             
414D: 81         ADD     A,C             
414E: 8F         ADC     A,A             
414F: 8F         ADC     A,A             
4150: F3         DI                      
4151: F3         DI                      
4152: 67         LD      H,A             
4153: E7         RST     0X20            
4154: 45         LD      B,L             
4155: C7         RST     0X00            
4156: 4D         LD      C,L             
4157: CF         RST     0X08            
4158: 7B         LD      A,E             
4159: FF         RST     0X38            
415A: D2 DE 92   JP      NC,$92DE        
415D: 9E         SBC     (HL)            
415E: 9E         SBC     (HL)            
415F: 9E         SBC     (HL)            
4160: 39         ADD     HL,SP           
4161: 39         ADD     HL,SP           
4162: 33         INC     SP              
4163: 33         INC     SP              
4164: 83         ADD     A,E             
4165: 83         ADD     A,E             
4166: C7         RST     0X00            
4167: C7         RST     0X00            
4168: FE FF      CP      $FF             
416A: E3         ???                     
416B: E3         ???                     
416C: E1         POP     HL              
416D: E1         POP     HL              
416E: C1         POP     BC              
416F: C1         POP     BC              
4170: 22         LD      (HLI),A         
4171: 22         LD      (HLI),A         
4172: 02         LD      (BC),A          
4173: 02         LD      (BC),A          
4174: 06 06      LD      B,$06           
4176: C7         RST     0X00            
4177: C7         RST     0X00            
4178: 7F         LD      A,A             
4179: FF         RST     0X38            
417A: CC CC 8C   CALL    Z,$8CCC         
417D: 8C         ADC     A,H             
417E: 8C         ADC     A,H             
417F: 8C         ADC     A,H             
4180: 1F         RRA                     
4181: 1F         RRA                     
4182: 0E 0F      LD      C,$0F           
4184: 46         LD      B,(HL)          
4185: 47         LD      B,A             
4186: 66         LD      H,(HL)          
4187: 67         LD      H,A             
4188: FF         RST     0X38            
4189: FF         RST     0X38            
418A: F0 F0      LD      A,($F0)         
418C: 60         LD      H,B             
418D: 60         LD      H,B             
418E: 63         LD      H,E             
418F: 63         LD      H,E             
4190: FF         RST     0X38            
4191: FF         RST     0X38            
4192: FB         EI                      
4193: 07         RLCA                    
4194: 01 FF 7F   LD      BC,$7FFF        
4197: FF         RST     0X38            
4198: C1         POP     BC              
4199: C1         POP     BC              
419A: 80         ADD     A,B             
419B: 80         ADD     A,B             
419C: 80         ADD     A,B             
419D: 80         ADD     A,B             
419E: 98         SBC     B               
419F: 98         SBC     B               
41A0: 8C         ADC     A,H             
41A1: 8C         ADC     A,H             
41A2: 8C         ADC     A,H             
41A3: 8C         ADC     A,H             
41A4: 05         DEC     B               
41A5: 05         DEC     B               
41A6: 11 11 11   LD      DE,$1111        
41A9: 11 39 39   LD      DE,$3939        
41AC: 29         ADD     HL,HL           
41AD: 39         ADD     HL,SP           
41AE: BB         CP      E               
41AF: BB         CP      E               
41B0: C9         RET                     
41B1: C9         RET                     
41B2: D9         RETI                    
41B3: D9         RETI                    
41B4: 98         SBC     B               
41B5: 98         SBC     B               
41B6: 00         NOP                     
41B7: 00         NOP                     
41B8: 81         ADD     A,C             
41B9: 81         ADD     A,C             
41BA: 99         SBC     C               
41BB: 99         SBC     C               
41BC: B9         CP      C               
41BD: B9         CP      C               
41BE: BB         CP      E               
41BF: BB         CP      E               
41C0: 88         ADC     A,B             
41C1: 88         ADC     A,B             
41C2: 80         ADD     A,B             
41C3: 80         ADD     A,B             
41C4: A2         AND     D               
41C5: A2         AND     D               
41C6: A2         AND     D               
41C7: A2         AND     D               
41C8: B6         OR      (HL)            
41C9: B6         OR      (HL)            
41CA: BE         CP      (HL)            
41CB: BE         CP      (HL)            
41CC: A2         AND     D               
41CD: BE         CP      (HL)            
41CE: BE         CP      (HL)            
41CF: BE         CP      (HL)            
41D0: 67         LD      H,A             
41D1: 67         LD      H,A             
41D2: 40         LD      B,B             
41D3: 40         LD      B,B             
41D4: 40         LD      B,B             
41D5: 40         LD      B,B             
41D6: 43         LD      B,E             
41D7: 43         LD      B,E             
41D8: 47         LD      B,A             
41D9: 47         LD      B,A             
41DA: 4E         LD      C,(HL)          
41DB: 4E         LD      C,(HL)          
41DC: 40         LD      B,B             
41DD: 40         LD      B,B             
41DE: E1         POP     HL              
41DF: E1         POP     HL              
41E0: F9         LD      SP,HL           
41E1: F9         LD      SP,HL           
41E2: F3         DI                      
41E3: F3         DI                      
41E4: A6         AND     (HL)            
41E5: E7         RST     0X20            
41E6: AC         XOR     H               
41E7: EF         RST     0X28            
41E8: A4         AND     H               
41E9: E7         RST     0X20            
41EA: BC         CP      H               
41EB: FF         RST     0X38            
41EC: E4         ???                     
41ED: E7         RST     0X20            
41EE: E7         RST     0X20            
41EF: E7         RST     0X20            
41F0: FF         RST     0X38            
41F1: FF         RST     0X38            
41F2: E3         ???                     
41F3: 1F         RRA                     
41F4: 01 FF 01   LD      BC,$01FF        
41F7: FF         RST     0X38            
41F8: 03         INC     BC              
41F9: FD         ???                     
41FA: 03         INC     BC              
41FB: FD         ???                     
41FC: 7D         LD      A,L             
41FD: 83         ADD     A,E             
41FE: FF         RST     0X38            
41FF: FF         RST     0X38            
4200: 00         NOP                     
4201: 00         NOP                     
4202: E0 00      LDFF00  ($00),A         
4204: F0 00      LD      A,($00)         
4206: F8 00      LDHL    SP,$00          
4208: FE 00      CP      $00             
420A: FF         RST     0X38            
420B: 00         NOP                     
420C: FF         RST     0X38            
420D: 00         NOP                     
420E: FF         RST     0X38            
420F: 00         NOP                     
4210: 00         NOP                     
4211: 00         NOP                     
4212: 00         NOP                     
4213: 00         NOP                     
4214: 03         INC     BC              
4215: 00         NOP                     
4216: 07         RLCA                    
4217: 00         NOP                     
4218: 1F         RRA                     
4219: 00         NOP                     
421A: 7F         LD      A,A             
421B: 00         NOP                     
421C: FF         RST     0X38            
421D: 00         NOP                     
421E: FF         RST     0X38            
421F: 00         NOP                     
4220: FF         RST     0X38            
4221: 00         NOP                     
4222: FF         RST     0X38            
4223: 00         NOP                     
4224: F9         LD      SP,HL           
4225: 06 C8      LD      B,$C8           
4227: 35         DEC     (HL)            
4228: 40         LD      B,B             
4229: AC         XOR     H               
422A: 00         NOP                     
422B: 4B         LD      C,E             
422C: 00         NOP                     
422D: A7         AND     A               
422E: 00         NOP                     
422F: FF         RST     0X38            
4230: F8 F8      LDHL    SP,$F8          
4232: C7         RST     0X00            
4233: 87         ADD     A,A             
4234: 7E         LD      A,(HL)          
4235: 64         LD      H,H             
4236: 1F         RRA                     
4237: 18 1F      JR      $4258           
4239: 11 2F 33   LD      DE,$332F        
423C: 2F         CPL                     
423D: 33         INC     SP              
423E: FF         RST     0X38            
423F: FC         ???                     
4240: 0E 0E      LD      C,$0E           
4242: F2         ???                     
4243: F2         ???                     
4244: 1C         INC     E               
4245: 1C         INC     E               
4246: F8 C8      LDHL    SP,$C8          
4248: FC         ???                     
4249: E4         ???                     
424A: FC         ???                     
424B: F4         ???                     
424C: FC         ???                     
424D: F4         ???                     
424E: FC         ???                     
424F: C4 87 84   CALL    NZ,$8487        
4252: 87         ADD     A,A             
4253: F4         ???                     
4254: E7         RST     0X20            
4255: 96         SUB     (HL)            
4256: E7         RST     0X20            
4257: 95         SUB     L               
4258: E7         RST     0X20            
4259: 94         SUB     H               
425A: E5         PUSH    HL              
425B: 97         SUB     A               
425C: E6 97      AND     $97             
425E: E5         PUSH    HL              
425F: 96         SUB     (HL)            
4260: FE C6      CP      $C6             
4262: FD         ???                     
4263: C5         PUSH    BC              
4264: FF         RST     0X38            
4265: 1D         DEC     E               
4266: EF         RST     0X28            
4267: E5         PUSH    HL              
4268: 1F         RRA                     
4269: 06 FF      LD      B,$FF           
426B: E6 9D      AND     $9D             
426D: 1D         DEC     E               
426E: FF         RST     0X38            
426F: 09         ADD     HL,BC           
4270: 87         ADD     A,A             
4271: F7         RST     0X30            
4272: 85         ADD     A,L             
4273: 86         ADD     A,(HL)          
4274: FF         RST     0X38            
4275: FF         RST     0X38            
4276: FF         RST     0X38            
4277: 38 E7      JR      C,$4260         
4279: E7         RST     0X20            
427A: 02         LD      (BC),A          
427B: 1A         LD      A,(DE)          
427C: 00         NOP                     
427D: FD         ???                     
427E: 00         NOP                     
427F: FF         RST     0X38            
4280: FF         RST     0X38            
4281: FF         RST     0X38            
4282: DF         RST     0X18            
4283: E4         ???                     
4284: FF         RST     0X38            
4285: FC         ???                     
4286: D3         ???                     
4287: E3         ???                     
4288: 22         LD      (HLI),A         
4289: 3E 1C      LD      A,$1C           
428B: DD         ???                     
428C: 00         NOP                     
428D: E3         ???                     
428E: 00         NOP                     
428F: FF         RST     0X38            
4290: FF         RST     0X38            
4291: FF         RST     0X38            
4292: EC         ???                     
4293: 13         INC     DE              
4294: 80         ADD     A,B             
4295: 7F         LD      A,A             
4296: 21 FF FF   LD      HL,$FFFF        
4299: FF         RST     0X38            
429A: FF         RST     0X38            
429B: FF         RST     0X38            
429C: FF         RST     0X38            
429D: FF         RST     0X38            
429E: FF         RST     0X38            
429F: FF         RST     0X38            
42A0: 07         RLCA                    
42A1: 07         RLCA                    
42A2: 21 21 B3   LD      HL,$B321        
42A5: B3         OR      E               
42A6: FE FF      CP      $FF             
42A8: 03         INC     BC              
42A9: 03         INC     BC              
42AA: 01 01 01   LD      BC,$0101        
42AD: 01 C7 C7   LD      BC,$C7C7        
42B0: 03         INC     BC              
42B1: 03         INC     BC              
42B2: 73         LD      (HL),E          
42B3: 73         LD      (HL),E          
42B4: 33         INC     SP              
42B5: 33         INC     SP              
42B6: 33         INC     SP              
42B7: 33         INC     SP              
42B8: 33         INC     SP              
42B9: 33         INC     SP              
42BA: 33         INC     SP              
42BB: 33         INC     SP              
42BC: 33         INC     SP              
42BD: 33         INC     SP              
42BE: 03         INC     BC              
42BF: 03         INC     BC              
42C0: 03         INC     BC              
42C1: 03         INC     BC              
42C2: 7B         LD      A,E             
42C3: 7B         LD      A,E             
42C4: 1B         DEC     DE              
42C5: 1B         DEC     DE              
42C6: 7B         LD      A,E             
42C7: 7B         LD      A,E             
42C8: 63         LD      H,E             
42C9: 63         LD      H,E             
42CA: 63         LD      H,E             
42CB: 63         LD      H,E             
42CC: 7B         LD      A,E             
42CD: 7B         LD      A,E             
42CE: 03         INC     BC              
42CF: 03         INC     BC              
42D0: 03         INC     BC              
42D1: 03         INC     BC              
42D2: 7B         LD      A,E             
42D3: 7B         LD      A,E             
42D4: 1B         DEC     DE              
42D5: 1B         DEC     DE              
42D6: 7B         LD      A,E             
42D7: 7B         LD      A,E             
42D8: 1B         DEC     DE              
42D9: 1B         DEC     DE              
42DA: 1B         DEC     DE              
42DB: 1B         DEC     DE              
42DC: 7B         LD      A,E             
42DD: 7B         LD      A,E             
42DE: 03         INC     BC              
42DF: 03         INC     BC              
42E0: FF         RST     0X38            
42E1: FF         RST     0X38            
42E2: 93         SUB     E               
42E3: 93         SUB     E               
42E4: 6D         LD      L,L             
42E5: 01 7D 01   LD      BC,$017D        
42E8: BB         CP      E               
42E9: 83         ADD     A,E             
42EA: D7         RST     0X10            
42EB: C7         RST     0X00            
42EC: EF         RST     0X28            
42ED: EF         RST     0X28            
42EE: FF         RST     0X38            
42EF: FF         RST     0X38            
42F0: C7         RST     0X00            
42F1: C7         RST     0X00            
42F2: 47         LD      B,A             
42F3: C7         RST     0X00            
42F4: 45         LD      B,L             
42F5: C7         RST     0X00            
42F6: 4D         LD      C,L             
42F7: CF         RST     0X08            
42F8: 49         LD      C,C             
42F9: CF         RST     0X08            
42FA: 49         LD      C,C             
42FB: CF         RST     0X08            
42FC: 59         LD      E,C             
42FD: DF         RST     0X18            
42FE: FF         RST     0X38            
42FF: FF         RST     0X38            
4300: FF         RST     0X38            
4301: FF         RST     0X38            
4302: E3         ???                     
4303: E3         ???                     
4304: DB         ???                     
4305: DB         ???                     
4306: DB         ???                     
4307: DB         ???                     
4308: B7         OR      A               
4309: B7         OR      A               
430A: B7         OR      A               
430B: B7         OR      A               
430C: CF         RST     0X08            
430D: CF         RST     0X08            
430E: FF         RST     0X38            
430F: FF         RST     0X38            
4310: FF         RST     0X38            
4311: FF         RST     0X38            
4312: FB         EI                      
4313: FB         EI                      
4314: FB         EI                      
4315: FB         EI                      
4316: F7         RST     0X30            
4317: F7         RST     0X30            
4318: F7         RST     0X30            
4319: F7         RST     0X30            
431A: EF         RST     0X28            
431B: EF         RST     0X28            
431C: EF         RST     0X28            
431D: EF         RST     0X28            
431E: FF         RST     0X38            
431F: FF         RST     0X38            
4320: FF         RST     0X38            
4321: FF         RST     0X38            
4322: E3         ???                     
4323: E3         ???                     
4324: D9         RETI                    
4325: D9         RETI                    
4326: FB         EI                      
4327: FB         EI                      
4328: F7         RST     0X30            
4329: F7         RST     0X30            
432A: EF         RST     0X28            
432B: EF         RST     0X28            
432C: 83         ADD     A,E             
432D: 83         ADD     A,E             
432E: FF         RST     0X38            
432F: FF         RST     0X38            
4330: FF         RST     0X38            
4331: FF         RST     0X38            
4332: E3         ???                     
4333: E3         ???                     
4334: D9         RETI                    
4335: D9         RETI                    
4336: F3         DI                      
4337: F3         DI                      
4338: FB         EI                      
4339: FB         EI                      
433A: BB         CP      E               
433B: BB         CP      E               
433C: C7         RST     0X00            
433D: C7         RST     0X00            
433E: FF         RST     0X38            
433F: FF         RST     0X38            
4340: FF         RST     0X38            
4341: FF         RST     0X38            
4342: FB         EI                      
4343: FB         EI                      
4344: F7         RST     0X30            
4345: F7         RST     0X30            
4346: EF         RST     0X28            
4347: EF         RST     0X28            
4348: DB         ???                     
4349: DB         ???                     
434A: 81         ADD     A,C             
434B: 81         ADD     A,C             
434C: F7         RST     0X30            
434D: F7         RST     0X30            
434E: FF         RST     0X38            
434F: FF         RST     0X38            
4350: FF         RST     0X38            
4351: FF         RST     0X38            
4352: E1         POP     HL              
4353: E1         POP     HL              
4354: EF         RST     0X28            
4355: EF         RST     0X28            
4356: C7         RST     0X00            
4357: C7         RST     0X00            
4358: FB         EI                      
4359: FB         EI                      
435A: FB         EI                      
435B: FB         EI                      
435C: 87         ADD     A,A             
435D: 87         ADD     A,A             
435E: FF         RST     0X38            
435F: FF         RST     0X38            
4360: FF         RST     0X38            
4361: FF         RST     0X38            
4362: FB         EI                      
4363: FB         EI                      
4364: F7         RST     0X30            
4365: F7         RST     0X30            
4366: E7         RST     0X20            
4367: E7         RST     0X20            
4368: DB         ???                     
4369: DB         ???                     
436A: 9B         SBC     E               
436B: 9B         SBC     E               
436C: C7         RST     0X00            
436D: C7         RST     0X00            
436E: FF         RST     0X38            
436F: FF         RST     0X38            
4370: FF         RST     0X38            
4371: FF         RST     0X38            
4372: C1         POP     BC              
4373: C1         POP     BC              
4374: FB         EI                      
4375: FB         EI                      
4376: F7         RST     0X30            
4377: F7         RST     0X30            
4378: F7         RST     0X30            
4379: F7         RST     0X30            
437A: EF         RST     0X28            
437B: EF         RST     0X28            
437C: EF         RST     0X28            
437D: EF         RST     0X28            
437E: FF         RST     0X38            
437F: FF         RST     0X38            
4380: FF         RST     0X38            
4381: FF         RST     0X38            
4382: E1         POP     HL              
4383: E1         POP     HL              
4384: DB         ???                     
4385: DB         ???                     
4386: E7         RST     0X20            
4387: E7         RST     0X20            
4388: DB         ???                     
4389: DB         ???                     
438A: BB         CP      E               
438B: BB         CP      E               
438C: C7         RST     0X00            
438D: C7         RST     0X00            
438E: FF         RST     0X38            
438F: FF         RST     0X38            
4390: FF         RST     0X38            
4391: FF         RST     0X38            
4392: E3         ???                     
4393: E3         ???                     
4394: D9         RETI                    
4395: D9         RETI                    
4396: DB         ???                     
4397: DB         ???                     
4398: E7         RST     0X20            
4399: E7         RST     0X20            
439A: EF         RST     0X28            
439B: EF         RST     0X28            
439C: DF         RST     0X18            
439D: DF         RST     0X18            
439E: FF         RST     0X38            
439F: FF         RST     0X38            
43A0: FF         RST     0X38            
43A1: FF         RST     0X38            
43A2: 87         ADD     A,A             
43A3: 87         ADD     A,A             
43A4: 33         INC     SP              
43A5: 33         INC     SP              
43A6: 33         INC     SP              
43A7: 33         INC     SP              
43A8: 33         INC     SP              
43A9: 33         INC     SP              
43AA: 33         INC     SP              
43AB: 33         INC     SP              
43AC: 87         ADD     A,A             
43AD: 87         ADD     A,A             
43AE: FF         RST     0X38            
43AF: FF         RST     0X38            
43B0: FF         RST     0X38            
43B1: FF         RST     0X38            
43B2: 9C         SBC     H               
43B3: 9C         SBC     H               
43B4: 99         SBC     C               
43B5: 99         SBC     C               
43B6: 93         SUB     E               
43B7: 93         SUB     E               
43B8: 83         ADD     A,E             
43B9: 83         ADD     A,E             
43BA: 89         ADC     A,C             
43BB: 89         ADC     A,C             
43BC: 9C         SBC     H               
43BD: 9C         SBC     H               
43BE: FF         RST     0X38            
43BF: FF         RST     0X38            
43C0: 00         NOP                     
43C1: 00         NOP                     
43C2: FF         RST     0X38            
43C3: FF         RST     0X38            
43C4: FF         RST     0X38            
43C5: FF         RST     0X38            
43C6: 00         NOP                     
43C7: 00         NOP                     
43C8: 00         NOP                     
43C9: 00         NOP                     
43CA: 00         NOP                     
43CB: 00         NOP                     
43CC: 00         NOP                     
43CD: 00         NOP                     
43CE: 00         NOP                     
43CF: 00         NOP                     
43D0: 00         NOP                     
43D1: 00         NOP                     
43D2: 00         NOP                     
43D3: 00         NOP                     
43D4: 00         NOP                     
43D5: 00         NOP                     
43D6: 00         NOP                     
43D7: 00         NOP                     
43D8: 00         NOP                     
43D9: 00         NOP                     
43DA: 00         NOP                     
43DB: 00         NOP                     
43DC: 00         NOP                     
43DD: 00         NOP                     
43DE: 00         NOP                     
43DF: 00         NOP                     
43E0: 08 08 0C   LD      ($0C08),SP      
43E3: 0C         INC     C               
43E4: FE FE      CP      $FE             
43E6: FF         RST     0X38            
43E7: FF         RST     0X38            
43E8: FE FE      CP      $FE             
43EA: 0C         INC     C               
43EB: 0C         INC     C               
43EC: 08 08 00   LD      ($0008),SP      
43EF: 00         NOP                     
43F0: 00         NOP                     
43F1: 00         NOP                     
43F2: 00         NOP                     
43F3: 00         NOP                     
43F4: 00         NOP                     
43F5: 00         NOP                     
43F6: 00         NOP                     
43F7: 00         NOP                     
43F8: 00         NOP                     
43F9: 00         NOP                     
43FA: 00         NOP                     
43FB: 00         NOP                     
43FC: 00         NOP                     
43FD: 00         NOP                     
43FE: 00         NOP                     
43FF: 00         NOP                     
4400: FF         RST     0X38            
4401: 07         RLCA                    
4402: FF         RST     0X38            
4403: 1F         RRA                     
4404: FF         RST     0X38            
4405: 30 FF      JR      NC,$4406        
4407: 60         LD      H,B             
4408: FF         RST     0X38            
4409: 40         LD      B,B             
440A: FF         RST     0X38            
440B: C0         RET     NZ              
440C: FF         RST     0X38            
440D: C0         RET     NZ              
440E: FF         RST     0X38            
440F: C0         RET     NZ              
4410: FF         RST     0X38            
4411: 80         ADD     A,B             
4412: FF         RST     0X38            
4413: E0 FF      LDFF00  ($FF),A         
4415: F0 FF      LD      A,($FF)         
4417: 78         LD      A,B             
4418: FF         RST     0X38            
4419: 78         LD      A,B             
441A: FF         RST     0X38            
441B: 31 FF 02   LD      SP,$02FF        
441E: FF         RST     0X38            
441F: 02         LD      (BC),A          
4420: FF         RST     0X38            
4421: 00         NOP                     
4422: FF         RST     0X38            
4423: 00         NOP                     
4424: FF         RST     0X38            
4425: 30 FF      JR      NC,$4426        
4427: 10 FF      STOP    $FF             
4429: 18 FF      JR      $442A           
442B: 98         SBC     B               
442C: FF         RST     0X38            
442D: 8D         ADC     A,L             
442E: FF         RST     0X38            
442F: 8F         ADC     A,A             
4430: FF         RST     0X38            
4431: 00         NOP                     
4432: FF         RST     0X38            
4433: 00         NOP                     
4434: FF         RST     0X38            
4435: 70         LD      (HL),B          
4436: FF         RST     0X38            
4437: 70         LD      (HL),B          
4438: FF         RST     0X38            
4439: E0 FF      LDFF00  ($FF),A         
443B: E3         ???                     
443C: FF         RST     0X38            
443D: 6E         LD      L,(HL)          
443E: FF         RST     0X38            
443F: 66         LD      H,(HL)          
4440: FF         RST     0X38            
4441: 01 FF 06   LD      BC,$06FF        
4444: FF         RST     0X38            
4445: 0C         INC     C               
4446: FF         RST     0X38            
4447: 0C         INC     C               
4448: FF         RST     0X38            
4449: 18 FF      JR      $444A           
444B: 98         SBC     B               
444C: FF         RST     0X38            
444D: 18 FF      JR      $444E           
444F: 18 FF      JR      $4450           
4451: C0         RET     NZ              
4452: FF         RST     0X38            
4453: 30 FF      JR      NC,$4454        
4455: 18 FF      JR      $4456           
4457: 18 FF      JR      $4458           
4459: 0C         INC     C               
445A: FF         RST     0X38            
445B: 0D         DEC     C               
445C: FF         RST     0X38            
445D: 0D         DEC     C               
445E: FF         RST     0X38            
445F: 0D         DEC     C               
4460: FF         RST     0X38            
4461: 00         NOP                     
4462: FF         RST     0X38            
4463: 01 FF 0F   LD      BC,$0FFF        
4466: FF         RST     0X38            
4467: 0C         INC     C               
4468: FF         RST     0X38            
4469: 0C         INC     C               
446A: FF         RST     0X38            
446B: 2C         INC     L               
446C: FF         RST     0X38            
446D: 6C         LD      L,H             
446E: FF         RST     0X38            
446F: 4E         LD      C,(HL)          
4470: FF         RST     0X38            
4471: 00         NOP                     
4472: FF         RST     0X38            
4473: 00         NOP                     
4474: FF         RST     0X38            
4475: 00         NOP                     
4476: FF         RST     0X38            
4477: 00         NOP                     
4478: FF         RST     0X38            
4479: 00         NOP                     
447A: FF         RST     0X38            
447B: FC         ???                     
447C: FF         RST     0X38            
447D: 26 FF      LD      H,$FF           
447F: 26 FF      LD      H,$FF           
4481: C0         RET     NZ              
4482: FF         RST     0X38            
4483: C3 FF E3   JP      $E3FF           
4486: FF         RST     0X38            
4487: 60         LD      H,B             
4488: FF         RST     0X38            
4489: 70         LD      (HL),B          
448A: FF         RST     0X38            
448B: 38 FF      JR      C,$448C         
448D: 1F         RRA                     
448E: FF         RST     0X38            
448F: 07         RLCA                    
4490: FF         RST     0X38            
4491: E4         ???                     
4492: FF         RST     0X38            
4493: E4         ???                     
4494: FF         RST     0X38            
4495: 24         INC     H               
4496: FF         RST     0X38            
4497: 2F         CPL                     
4498: FF         RST     0X38            
4499: 2C         INC     L               
449A: FF         RST     0X38            
449B: 6C         LD      L,H             
449C: FF         RST     0X38            
449D: CC FF 80   CALL    Z,$80FF         
44A0: FF         RST     0X38            
44A1: 8A         ADC     A,D             
44A2: FF         RST     0X38            
44A3: 8A         ADC     A,D             
44A4: FF         RST     0X38            
44A5: C8         RET     Z               
44A6: FF         RST     0X38            
44A7: C8         RET     Z               
44A8: FF         RST     0X38            
44A9: C8         RET     Z               
44AA: FF         RST     0X38            
44AB: 18 FF      JR      $44AC           
44AD: 78         LD      A,B             
44AE: FF         RST     0X38            
44AF: 60         LD      H,B             
44B0: FF         RST     0X38            
44B1: 66         LD      H,(HL)          
44B2: FF         RST     0X38            
44B3: 66         LD      H,(HL)          
44B4: FF         RST     0X38            
44B5: 67         LD      H,A             
44B6: FF         RST     0X38            
44B7: 66         LD      H,(HL)          
44B8: FF         RST     0X38            
44B9: 76         HALT                    
44BA: FF         RST     0X38            
44BB: 76         HALT                    
44BC: FF         RST     0X38            
44BD: 0F         RRCA                    
44BE: FF         RST     0X38            
44BF: 00         NOP                     
44C0: FF         RST     0X38            
44C1: 18 FF      JR      $44C2           
44C3: 18 FF      JR      $44C4           
44C5: 88         ADC     A,B             
44C6: FF         RST     0X38            
44C7: 0C         INC     C               
44C8: FF         RST     0X38            
44C9: 04         INC     B               
44CA: FF         RST     0X38            
44CB: 03         INC     BC              
44CC: FF         RST     0X38            
44CD: C0         RET     NZ              
44CE: FF         RST     0X38            
44CF: 00         NOP                     
44D0: FF         RST     0X38            
44D1: 0D         DEC     C               
44D2: FF         RST     0X38            
44D3: 0D         DEC     C               
44D4: FF         RST     0X38            
44D5: 19         ADD     HL,DE           
44D6: FF         RST     0X38            
44D7: 19         ADD     HL,DE           
44D8: FF         RST     0X38            
44D9: 71         LD      (HL),C          
44DA: FF         RST     0X38            
44DB: C1         POP     BC              
44DC: FF         RST     0X38            
44DD: 00         NOP                     
44DE: FF         RST     0X38            
44DF: 00         NOP                     
44E0: FF         RST     0X38            
44E1: 4C         LD      C,H             
44E2: FF         RST     0X38            
44E3: 4C         LD      C,H             
44E4: FF         RST     0X38            
44E5: 8C         ADC     A,H             
44E6: FF         RST     0X38            
44E7: 8C         ADC     A,H             
44E8: FF         RST     0X38            
44E9: 9F         SBC     A               
44EA: FF         RST     0X38            
44EB: 00         NOP                     
44EC: FF         RST     0X38            
44ED: 00         NOP                     
44EE: FF         RST     0X38            
44EF: 00         NOP                     
44F0: FF         RST     0X38            
44F1: 26 FF      LD      H,$FF           
44F3: 2C         INC     L               
44F4: FF         RST     0X38            
44F5: 30 FF      JR      NC,$44F6        
44F7: 28 FF      JR      Z,$44F8         
44F9: 2C         INC     L               
44FA: FF         RST     0X38            
44FB: 67         LD      H,A             
44FC: FF         RST     0X38            
44FD: E3         ???                     
44FE: FF         RST     0X38            
44FF: C0         RET     NZ              
4500: 80         ADD     A,B             
4501: FF         RST     0X38            
4502: 0F         RRCA                    
4503: FF         RST     0X38            
4504: 7F         LD      A,A             
4505: FF         RST     0X38            
4506: 7F         LD      A,A             
4507: FF         RST     0X38            
4508: 7F         LD      A,A             
4509: FF         RST     0X38            
450A: 73         LD      (HL),E          
450B: FF         RST     0X38            
450C: 3E FF      LD      A,$FF           
450E: 0C         INC     C               
450F: FC         ???                     
4510: 00         NOP                     
4511: FF         RST     0X38            
4512: FE FF      CP      $FF             
4514: FF         RST     0X38            
4515: FF         RST     0X38            
4516: FF         RST     0X38            
4517: FF         RST     0X38            
4518: FF         RST     0X38            
4519: FF         RST     0X38            
451A: 9F         SBC     A               
451B: E0 04      LDFF00  ($04),A         
451D: 00         NOP                     
451E: 53         LD      D,E             
451F: E0 00      LDFF00  ($00),A         
4521: FF         RST     0X38            
4522: 1F         RRA                     
4523: FF         RST     0X38            
4524: 7F         LD      A,A             
4525: FF         RST     0X38            
4526: EF         RST     0X28            
4527: F0 C0      LD      A,($C0)         
4529: 00         NOP                     
452A: 03         INC     BC              
452B: 00         NOP                     
452C: 0F         RRCA                    
452D: 01 FF 01   LD      BC,$01FF        
4530: 00         NOP                     
4531: FF         RST     0X38            
4532: FF         RST     0X38            
4533: FF         RST     0X38            
4534: F4         ???                     
4535: F8 83      LDHL    SP,$83          
4537: 00         NOP                     
4538: 38 07      JR      C,$4541         
453A: E7         RST     0X20            
453B: 1F         RRA                     
453C: 1B         DEC     DE              
453D: FC         ???                     
453E: E8 F0      ADD     SP,$F0          
4540: FF         RST     0X38            
4541: FF         RST     0X38            
4542: 83         ADD     A,E             
4543: C1         POP     BC              
4544: 1F         RRA                     
4545: 0F         RRCA                    
4546: B0         OR      B               
4547: 7F         LD      A,A             
4548: DF         RST     0X18            
4549: E0 7B      LDFF00  ($7B),A         
454B: 80         ADD     A,B             
454C: 01 00 01   LD      BC,$0100        
454F: 00         NOP                     
4550: F8 F9      LDHL    SP,$F9          
4552: F3         DI                      
4553: F0 F1      LD      A,($F1)         
4555: F8 F8      LDHL    SP,$F8          
4557: FC         ???                     
4558: F1         POP     AF              
4559: E0 E7      LDFF00  ($E7),A         
455B: E0 EF      LDFF00  ($EF),A         
455D: E0 E7      LDFF00  ($E7),A         
455F: E0 F8      LDFF00  ($F8),A         
4561: F0 7E      LD      A,($7E)         
4563: FE B9      CP      $B9             
4565: 78         LD      A,B             
4566: DB         ???                     
4567: 38 DA      JR      C,$4543         
4569: 39         ADD     HL,SP           
456A: F5         PUSH    AF              
456B: 33         INC     SP              
456C: AA         XOR     D               
456D: 67         LD      H,A             
456E: DD         ???                     
456F: 3E E2      LD      A,$E2           
4571: 1F         RRA                     
4572: 8E         ADC     A,(HL)          
4573: 7C         LD      A,H             
4574: 14         INC     D               
4575: F8 E8      LDHL    SP,$E8          
4577: F0 A0      LD      A,($A0)         
4579: C0         RET     NZ              
457A: 40         LD      B,B             
457B: 80         ADD     A,B             
457C: 80         ADD     A,B             
457D: 00         NOP                     
457E: 00         NOP                     
457F: 00         NOP                     
4580: 97         SUB     A               
4581: 8F         ADC     A,A             
4582: 05         DEC     B               
4583: 83         ADD     A,E             
4584: 30 00      JR      NC,$4586        
4586: FE 00      CP      $00             
4588: FF         RST     0X38            
4589: 00         NOP                     
458A: 9F         SBC     A               
458B: 00         NOP                     
458C: 8F         ADC     A,A             
458D: 00         NOP                     
458E: 01 00 F4   LD      BC,$F400        
4591: F8 D0      LDHL    SP,$D0          
4593: E0 47      LDFF00  ($47),A         
4595: C0         RET     NZ              
4596: 5F         LD      E,A             
4597: 40         LD      B,B             
4598: 1D         DEC     E               
4599: 40         LD      B,B             
459A: A9         XOR     C               
459B: 00         NOP                     
459C: E0 00      LDFF00  ($00),A         
459E: 80         ADD     A,B             
459F: 00         NOP                     
45A0: 01 00 8F   LD      BC,$8F00        
45A3: 00         NOP                     
45A4: 9E         SBC     (HL)            
45A5: 00         NOP                     
45A6: FC         ???                     
45A7: 01 FD 01   LD      BC,$01FD        
45AA: 31 01 05   LD      SP,$0501        
45AD: 83         ADD     A,E             
45AE: 97         SUB     A               
45AF: 8F         ADC     A,A             
45B0: 80         ADD     A,B             
45B1: 00         NOP                     
45B2: E0 00      LDFF00  ($00),A         
45B4: E9         JP      (HL)            
45B5: 00         NOP                     
45B6: 7D         LD      A,L             
45B7: 00         NOP                     
45B8: 7F         LD      A,A             
45B9: 00         NOP                     
45BA: 87         ADD     A,A             
45BB: 00         NOP                     
45BC: D0         RET     NC              
45BD: E0 F4      LDFF00  ($F4),A         
45BF: F8 8E      LDHL    SP,$8E          
45C1: 80         ADD     A,B             
45C2: 9C         SBC     H               
45C3: 80         ADD     A,B             
45C4: DC 80 8C   CALL    C,$8C80         
45C7: C0         RET     NZ              
45C8: EE C0      XOR     $C0             
45CA: CE E0      ADC     $E0             
45CC: EE E0      XOR     $E0             
45CE: E7         RST     0X20            
45CF: E0 71      LDFF00  ($71),A         
45D1: 01 39 01   LD      BC,$0139        
45D4: 3B         DEC     SP              
45D5: 01 31 03   LD      BC,$0331        
45D8: 77         LD      (HL),A          
45D9: 03         INC     BC              
45DA: 73         LD      (HL),E          
45DB: 07         RLCA                    
45DC: 77         LD      (HL),A          
45DD: 07         RLCA                    
45DE: E7         RST     0X20            
45DF: 07         RLCA                    
45E0: C3 F0 E7   JP      $E7F0           
45E3: C0         RET     NZ              
45E4: F7         RST     0X30            
45E5: E0 8F      LDFF00  ($8F),A         
45E7: C0         RET     NZ              
45E8: DC 80 98   CALL    C,$9880         
45EB: 80         ADD     A,B             
45EC: DC 80 CF   CALL    C,$CF80         
45EF: E0 C3      LDFF00  ($C3),A         
45F1: 0F         RRCA                    
45F2: E7         RST     0X20            
45F3: 03         INC     BC              
45F4: EF         RST     0X28            
45F5: 07         RLCA                    
45F6: F1         POP     AF              
45F7: 03         INC     BC              
45F8: 3B         DEC     SP              
45F9: 01 19 01   LD      BC,$0119        
45FC: 3B         DEC     SP              
45FD: 01 F3 07   LD      BC,$07F3        
4600: 0F         RRCA                    
4601: 00         NOP                     
4602: 0F         RRCA                    
4603: 00         NOP                     
4604: 3F         CCF                     
4605: 00         NOP                     
4606: 7F         LD      A,A             
4607: 00         NOP                     
4608: 7F         LD      A,A             
4609: 00         NOP                     
460A: 7F         LD      A,A             
460B: 00         NOP                     
460C: 1F         RRA                     
460D: 00         NOP                     
460E: 0F         RRCA                    
460F: 00         NOP                     
4610: F0 00      LD      A,($00)         
4612: F0 00      LD      A,($00)         
4614: FC         ???                     
4615: 00         NOP                     
4616: FE 00      CP      $00             
4618: FE 00      CP      $00             
461A: FE 00      CP      $00             
461C: F8 00      LDHL    SP,$00          
461E: F0 00      LD      A,($00)         
4620: 00         NOP                     
4621: 00         NOP                     
4622: 00         NOP                     
4623: 00         NOP                     
4624: 00         NOP                     
4625: 00         NOP                     
4626: 00         NOP                     
4627: 00         NOP                     
4628: 1C         INC     E               
4629: 00         NOP                     
462A: 3E 00      LD      A,$00           
462C: FF         RST     0X38            
462D: 00         NOP                     
462E: FF         RST     0X38            
462F: 00         NOP                     
4630: FF         RST     0X38            
4631: 00         NOP                     
4632: FF         RST     0X38            
4633: 00         NOP                     
4634: 3E 00      LD      A,$00           
4636: 1C         INC     E               
4637: 00         NOP                     
4638: 00         NOP                     
4639: 00         NOP                     
463A: 00         NOP                     
463B: 00         NOP                     
463C: 00         NOP                     
463D: 00         NOP                     
463E: 00         NOP                     
463F: 00         NOP                     
4640: FF         RST     0X38            
4641: FF         RST     0X38            
4642: 57         LD      D,A             
4643: 8F         ADC     A,A             
4644: 0F         RRCA                    
4645: 07         RLCA                    
4646: E7         RST     0X20            
4647: 07         RLCA                    
4648: F3         DI                      
4649: 07         RLCA                    
464A: F7         RST     0X30            
464B: 03         INC     BC              
464C: F3         DI                      
464D: 03         INC     BC              
464E: E3         ???                     
464F: 03         INC     BC              
4650: E9         JP      (HL)            
4651: F0 E3      LD      A,($E3)         
4653: C0         RET     NZ              
4654: EF         RST     0X28            
4655: C0         RET     NZ              
4656: E7         RST     0X20            
4657: C0         RET     NZ              
4658: D0         RET     NC              
4659: E0 FA      LDFF00  ($FA),A         
465B: FC         ???                     
465C: FF         RST     0X38            
465D: FF         RST     0X38            
465E: FE FF      CP      $FF             
4660: 7D         LD      A,L             
4661: 01 79 01   LD      BC,$0179        
4664: FB         EI                      
4665: 01 F9 03   LD      BC,$03F9        
4668: F1         POP     AF              
4669: 03         INC     BC              
466A: 67         LD      H,A             
466B: 03         INC     BC              
466C: 0B         DEC     BC              
466D: 87         ADD     A,A             
466E: 17         RLA                     
466F: 8F         ADC     A,A             
4670: FF         RST     0X38            
4671: FF         RST     0X38            
4672: FF         RST     0X38            
4673: FF         RST     0X38            
4674: FF         RST     0X38            
4675: FF         RST     0X38            
4676: FF         RST     0X38            
4677: FF         RST     0X38            
4678: DF         RST     0X18            
4679: FF         RST     0X38            
467A: FB         EI                      
467B: FF         RST     0X38            
467C: FE FF      CP      $FF             
467E: DE FF      SBC     $FF             
4680: FF         RST     0X38            
4681: FF         RST     0X38            
4682: FF         RST     0X38            
4683: FF         RST     0X38            
4684: FF         RST     0X38            
4685: FF         RST     0X38            
4686: 7B         LD      A,E             
4687: FF         RST     0X38            
4688: 7F         LD      A,A             
4689: FF         RST     0X38            
468A: 7F         LD      A,A             
468B: FF         RST     0X38            
468C: 7F         LD      A,A             
468D: FF         RST     0X38            
468E: 3F         CCF                     
468F: FF         RST     0X38            
4690: 00         NOP                     
4691: 00         NOP                     
4692: 71         LD      (HL),C          
4693: 71         LD      (HL),C          
4694: 8A         ADC     A,D             
4695: 8A         ADC     A,D             
4696: 82         ADD     A,D             
4697: 82         ADD     A,D             
4698: 73         LD      (HL),E          
4699: 73         LD      (HL),E          
469A: 0A         LD      A,(BC)          
469B: 0A         LD      A,(BC)          
469C: 8A         ADC     A,D             
469D: 8A         ADC     A,D             
469E: 72         LD      (HL),D          
469F: 72         LD      (HL),D          
46A0: 00         NOP                     
46A1: 00         NOP                     
46A2: C8         RET     Z               
46A3: C8         RET     Z               
46A4: 28 28      JR      Z,$46CE         
46A6: 28 28      JR      Z,$46D0         
46A8: E8 E8      ADD     SP,$E8          
46AA: 25         DEC     H               
46AB: 25         DEC     H               
46AC: 25         DEC     H               
46AD: 25         DEC     H               
46AE: 22         LD      (HLI),A         
46AF: 22         LD      (HLI),A         
46B0: 00         NOP                     
46B1: 00         NOP                     
46B2: BE         CP      (HL)            
46B3: BE         CP      (HL)            
46B4: A0         AND     B               
46B5: A0         AND     B               
46B6: A0         AND     B               
46B7: A0         AND     B               
46B8: BC         CP      H               
46B9: BC         CP      H               
46BA: 20 20      JR      NZ,$46DC        
46BC: 20 20      JR      NZ,$46DE        
46BE: 3E 3E      LD      A,$3E           
46C0: 03         INC     BC              
46C1: 03         INC     BC              
46C2: 04         INC     B               
46C3: 04         INC     B               
46C4: 04         INC     B               
46C5: 04         INC     B               
46C6: 03         INC     BC              
46C7: 03         INC     BC              
46C8: 06 06      LD      B,$06           
46CA: 09         ADD     HL,BC           
46CB: 09         ADD     HL,BC           
46CC: 08 08 07   LD      ($0708),SP      
46CF: 07         RLCA                    
46D0: 00         NOP                     
46D1: 00         NOP                     
46D2: 80         ADD     A,B             
46D3: 80         ADD     A,B             
46D4: 80         ADD     A,B             
46D5: 80         ADD     A,B             
46D6: 00         NOP                     
46D7: 00         NOP                     
46D8: 60         LD      H,B             
46D9: 60         LD      H,B             
46DA: 80         ADD     A,B             
46DB: 80         ADD     A,B             
46DC: C0         RET     NZ              
46DD: C0         RET     NZ              
46DE: 20 20      JR      NZ,$4700        
46E0: 00         NOP                     
46E1: FF         RST     0X38            
46E2: 3B         DEC     SP              
46E3: FF         RST     0X38            
46E4: 7F         LD      A,A             
46E5: FF         RST     0X38            
46E6: 7F         LD      A,A             
46E7: FF         RST     0X38            
46E8: 6F         LD      L,A             
46E9: FF         RST     0X38            
46EA: 7F         LD      A,A             
46EB: FF         RST     0X38            
46EC: 7D         LD      A,L             
46ED: FF         RST     0X38            
46EE: 3F         CCF                     
46EF: FF         RST     0X38            
46F0: 00         NOP                     
46F1: FF         RST     0X38            
46F2: FE FF      CP      $FF             
46F4: EF         RST     0X28            
46F5: FF         RST     0X38            
46F6: FF         RST     0X38            
46F7: FF         RST     0X38            
46F8: FF         RST     0X38            
46F9: FF         RST     0X38            
46FA: FF         RST     0X38            
46FB: FF         RST     0X38            
46FC: F6 FF      OR      $FF             
46FE: FC         ???                     
46FF: FF         RST     0X38            
4700: 00         NOP                     
4701: 00         NOP                     
4702: 71         LD      (HL),C          
4703: 71         LD      (HL),C          
4704: 8A         ADC     A,D             
4705: 8A         ADC     A,D             
4706: 8A         ADC     A,D             
4707: 8A         ADC     A,D             
4708: 82         ADD     A,D             
4709: 82         ADD     A,D             
470A: 8A         ADC     A,D             
470B: 8A         ADC     A,D             
470C: 8A         ADC     A,D             
470D: 8A         ADC     A,D             
470E: 71         LD      (HL),C          
470F: 71         LD      (HL),C          
4710: 00         NOP                     
4711: 00         NOP                     
4712: C8         RET     Z               
4713: C8         RET     Z               
4714: 28 28      JR      Z,$473E         
4716: 2C         INC     L               
4717: 2C         INC     L               
4718: 2A         LD      A,(HLI)         
4719: 2A         LD      A,(HLI)         
471A: 29         ADD     HL,HL           
471B: 29         ADD     HL,HL           
471C: 28 28      JR      Z,$4746         
471E: C8         RET     Z               
471F: C8         RET     Z               
4720: 00         NOP                     
4721: 00         NOP                     
4722: BE         CP      (HL)            
4723: BE         CP      (HL)            
4724: 88         ADC     A,B             
4725: 88         ADC     A,B             
4726: 88         ADC     A,B             
4727: 88         ADC     A,B             
4728: 88         ADC     A,B             
4729: 88         ADC     A,B             
472A: 88         ADC     A,B             
472B: 88         ADC     A,B             
472C: 88         ADC     A,B             
472D: 88         ADC     A,B             
472E: 88         ADC     A,B             
472F: 88         ADC     A,B             
4730: 00         NOP                     
4731: 00         NOP                     
4732: E8 E8      ADD     SP,$E8          
4734: 48         LD      C,B             
4735: 48         LD      C,B             
4736: 4C         LD      C,H             
4737: 4C         LD      C,H             
4738: 4A         LD      C,D             
4739: 4A         LD      C,D             
473A: 49         LD      C,C             
473B: 49         LD      C,C             
473C: 48         LD      C,B             
473D: 48         LD      C,B             
473E: E8 E8      ADD     SP,$E8          
4740: 00         NOP                     
4741: 00         NOP                     
4742: A2         AND     D               
4743: A2         AND     D               
4744: A2         AND     D               
4745: A2         AND     D               
4746: A2         AND     D               
4747: A2         AND     D               
4748: A2         AND     D               
4749: A2         AND     D               
474A: A2         AND     D               
474B: A2         AND     D               
474C: A2         AND     D               
474D: A2         AND     D               
474E: 9C         SBC     H               
474F: 9C         SBC     H               
4750: 00         NOP                     
4751: 00         NOP                     
4752: F8 F8      LDHL    SP,$F8          
4754: 80         ADD     A,B             
4755: 80         ADD     A,B             
4756: 80         ADD     A,B             
4757: 80         ADD     A,B             
4758: F0 F0      LD      A,($F0)         
475A: 80         ADD     A,B             
475B: 80         ADD     A,B             
475C: 80         ADD     A,B             
475D: 80         ADD     A,B             
475E: F8 F8      LDHL    SP,$F8          
4760: 00         NOP                     
4761: 00         NOP                     
4762: 72         LD      (HL),D          
4763: 72         LD      (HL),D          
4764: 8A         ADC     A,D             
4765: 8A         ADC     A,D             
4766: 8A         ADC     A,D             
4767: 8A         ADC     A,D             
4768: 8A         ADC     A,D             
4769: 8A         ADC     A,D             
476A: AA         XOR     D               
476B: AA         XOR     D               
476C: 92         SUB     D               
476D: 92         SUB     D               
476E: 69         LD      L,C             
476F: 69         LD      L,C             
4770: 00         NOP                     
4771: 00         NOP                     
4772: 2E 2E      LD      L,$2E           
4774: 24         INC     H               
4775: 24         INC     H               
4776: 24         INC     H               
4777: 24         INC     H               
4778: 24         INC     H               
4779: 24         INC     H               
477A: 24         INC     H               
477B: 24         INC     H               
477C: 24         INC     H               
477D: 24         INC     H               
477E: CE CE      ADC     $CE             
4780: 00         NOP                     
4781: 00         NOP                     
4782: F8 F8      LDHL    SP,$F8          
4784: 20 20      JR      NZ,$47A6        
4786: 20 20      JR      NZ,$47A8        
4788: 20 20      JR      NZ,$47AA        
478A: 20 20      JR      NZ,$47AC        
478C: 20 20      JR      NZ,$47AE        
478E: 20 20      JR      NZ,$47B0        
4790: 00         NOP                     
4791: 00         NOP                     
4792: F3         DI                      
4793: F3         DI                      
4794: 8A         ADC     A,D             
4795: 8A         ADC     A,D             
4796: 8A         ADC     A,D             
4797: 8A         ADC     A,D             
4798: F3         DI                      
4799: F3         DI                      
479A: 8A         ADC     A,D             
479B: 8A         ADC     A,D             
479C: 8A         ADC     A,D             
479D: 8A         ADC     A,D             
479E: 8B         ADC     A,E             
479F: 8B         ADC     A,E             
47A0: 00         NOP                     
47A1: 00         NOP                     
47A2: EF         RST     0X28            
47A3: EF         RST     0X28            
47A4: 02         LD      (BC),A          
47A5: 02         LD      (BC),A          
47A6: 02         LD      (BC),A          
47A7: 02         LD      (BC),A          
47A8: C2 C2 02   JP      NZ,$02C2        
47AB: 02         LD      (BC),A          
47AC: 02         LD      (BC),A          
47AD: 02         LD      (BC),A          
47AE: E2         LDFF00  (C),A           
47AF: E2         LDFF00  (C),A           
47B0: 00         NOP                     
47B1: 00         NOP                     
47B2: A2         AND     D               
47B3: A2         AND     D               
47B4: 22         LD      (HLI),A         
47B5: 22         LD      (HLI),A         
47B6: 22         LD      (HLI),A         
47B7: 22         LD      (HLI),A         
47B8: 22         LD      (HLI),A         
47B9: 22         LD      (HLI),A         
47BA: 22         LD      (HLI),A         
47BB: 22         LD      (HLI),A         
47BC: 22         LD      (HLI),A         
47BD: 22         LD      (HLI),A         
47BE: 1C         INC     E               
47BF: 1C         INC     E               
47C0: 00         NOP                     
47C1: 00         NOP                     
47C2: F2         ???                     
47C3: F2         ???                     
47C4: 8A         ADC     A,D             
47C5: 8A         ADC     A,D             
47C6: 8B         ADC     A,E             
47C7: 8B         ADC     A,E             
47C8: F2         ???                     
47C9: F2         ???                     
47CA: 8A         ADC     A,D             
47CB: 8A         ADC     A,D             
47CC: 8A         ADC     A,D             
47CD: 8A         ADC     A,D             
47CE: 8A         ADC     A,D             
47CF: 8A         ADC     A,D             
47D0: 00         NOP                     
47D1: 00         NOP                     
47D2: 20 20      JR      NZ,$47F4        
47D4: 20 20      JR      NZ,$47F6        
47D6: 20 20      JR      NZ,$47F8        
47D8: A0         AND     B               
47D9: A0         AND     B               
47DA: 60         LD      H,B             
47DB: 60         LD      H,B             
47DC: 20 20      JR      NZ,$47FE        
47DE: 20 20      JR      NZ,$4800        
47E0: 00         NOP                     
47E1: 00         NOP                     
47E2: 08 00 0C   LD      ($0C00),SP      
47E5: 00         NOP                     
47E6: FE 00      CP      $00             
47E8: FF         RST     0X38            
47E9: 00         NOP                     
47EA: FE 00      CP      $00             
47EC: 0C         INC     C               
47ED: 00         NOP                     
47EE: 08 00 00   LD      ($0000),SP      
47F1: 00         NOP                     
47F2: 00         NOP                     
47F3: 00         NOP                     
47F4: 00         NOP                     
47F5: 00         NOP                     
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
4800: 00         NOP                     
4801: 00         NOP                     
4802: F9         LD      SP,HL           
4803: F9         LD      SP,HL           
4804: 22         LD      (HLI),A         
4805: 22         LD      (HLI),A         
4806: 22         LD      (HLI),A         
4807: 22         LD      (HLI),A         
4808: 22         LD      (HLI),A         
4809: 22         LD      (HLI),A         
480A: 22         LD      (HLI),A         
480B: 22         LD      (HLI),A         
480C: 22         LD      (HLI),A         
480D: 22         LD      (HLI),A         
480E: 21 21 00   LD      HL,$0021        
4811: 00         NOP                     
4812: C0         RET     NZ              
4813: C0         RET     NZ              
4814: 20 20      JR      NZ,$4836        
4816: 20 20      JR      NZ,$4838        
4818: 20 20      JR      NZ,$483A        
481A: 20 20      JR      NZ,$483C        
481C: 20 20      JR      NZ,$483E        
481E: C0         RET     NZ              
481F: C0         RET     NZ              
4820: 00         NOP                     
4821: 00         NOP                     
4822: 38 38      JR      C,$485C         
4824: 45         LD      B,L             
4825: 45         LD      B,L             
4826: 41         LD      B,C             
4827: 41         LD      B,C             
4828: 5D         LD      E,L             
4829: 5D         LD      E,L             
482A: 45         LD      B,L             
482B: 45         LD      B,L             
482C: 45         LD      B,L             
482D: 45         LD      B,L             
482E: 39         ADD     HL,SP           
482F: 39         ADD     HL,SP           
4830: 00         NOP                     
4831: 00         NOP                     
4832: E4         ???                     
4833: E4         ???                     
4834: 16 16      LD      D,$16           
4836: 15         DEC     D               
4837: 15         DEC     D               
4838: F4         ???                     
4839: F4         ???                     
483A: 14         INC     D               
483B: 14         INC     D               
483C: 14         INC     D               
483D: 14         INC     D               
483E: 14         INC     D               
483F: 14         INC     D               
4840: 00         NOP                     
4841: 00         NOP                     
4842: 5F         LD      E,A             
4843: 5F         LD      E,A             
4844: D0         RET     NC              
4845: D0         RET     NC              
4846: 50         LD      D,B             
4847: 50         LD      D,B             
4848: 5E         LD      E,(HL)          
4849: 5E         LD      E,(HL)          
484A: 50         LD      D,B             
484B: 50         LD      D,B             
484C: 50         LD      D,B             
484D: 50         LD      D,B             
484E: 5F         LD      E,A             
484F: 5F         LD      E,A             
4850: 00         NOP                     
4851: 00         NOP                     
4852: 34         INC     (HL)            
4853: 34         INC     (HL)            
4854: 44         LD      B,H             
4855: 44         LD      B,H             
4856: 84         ADD     A,H             
4857: 84         ADD     A,H             
4858: 84         ADD     A,H             
4859: 84         ADD     A,H             
485A: 85         ADD     A,L             
485B: 85         ADD     A,L             
485C: 46         LD      B,(HL)          
485D: 46         LD      B,(HL)          
485E: 34         INC     (HL)            
485F: 34         INC     (HL)            
4860: 00         NOP                     
4861: 00         NOP                     
4862: 5D         LD      E,L             
4863: 5D         LD      E,L             
4864: 48         LD      C,B             
4865: 48         LD      C,B             
4866: 48         LD      C,B             
4867: 48         LD      C,B             
4868: 48         LD      C,B             
4869: 48         LD      C,B             
486A: 48         LD      C,B             
486B: 48         LD      C,B             
486C: C8         RET     Z               
486D: C8         RET     Z               
486E: 5C         LD      E,H             
486F: 5C         LD      E,H             
4870: 00         NOP                     
4871: 00         NOP                     
4872: F4         ???                     
4873: F4         ???                     
4874: 44         LD      B,H             
4875: 44         LD      B,H             
4876: 44         LD      B,H             
4877: 44         LD      B,H             
4878: 47         LD      B,A             
4879: 47         LD      B,A             
487A: 44         LD      B,H             
487B: 44         LD      B,H             
487C: 44         LD      B,H             
487D: 44         LD      B,H             
487E: 44         LD      B,H             
487F: 44         LD      B,H             
4880: 00         NOP                     
4881: 00         NOP                     
4882: 4E         LD      C,(HL)          
4883: 4E         LD      C,(HL)          
4884: 51         LD      D,C             
4885: 51         LD      D,C             
4886: 51         LD      D,C             
4887: 51         LD      D,C             
4888: D1         POP     DE              
4889: D1         POP     DE              
488A: 51         LD      D,C             
488B: 51         LD      D,C             
488C: 51         LD      D,C             
488D: 51         LD      D,C             
488E: 4E         LD      C,(HL)          
488F: 4E         LD      C,(HL)          
4890: 00         NOP                     
4891: 00         NOP                     
4892: 45         LD      B,L             
4893: 45         LD      B,L             
4894: 44         LD      B,H             
4895: 44         LD      B,H             
4896: 44         LD      B,H             
4897: 44         LD      B,H             
4898: 44         LD      B,H             
4899: 44         LD      B,H             
489A: 44         LD      B,H             
489B: 44         LD      B,H             
489C: 44         LD      B,H             
489D: 44         LD      B,H             
489E: 38 38      JR      C,$48D8         
48A0: 00         NOP                     
48A1: 00         NOP                     
48A2: F0 F0      LD      A,($F0)         
48A4: 40         LD      B,B             
48A5: 40         LD      B,B             
48A6: 40         LD      B,B             
48A7: 40         LD      B,B             
48A8: 40         LD      B,B             
48A9: 40         LD      B,B             
48AA: 40         LD      B,B             
48AB: 40         LD      B,B             
48AC: 40         LD      B,B             
48AD: 40         LD      B,B             
48AE: 40         LD      B,B             
48AF: 40         LD      B,B             
48B0: 00         NOP                     
48B1: 00         NOP                     
48B2: BA         CP      D               
48B3: BA         CP      D               
48B4: 92         SUB     D               
48B5: 92         SUB     D               
48B6: 93         SUB     E               
48B7: 93         SUB     E               
48B8: 92         SUB     D               
48B9: 92         SUB     D               
48BA: 12         LD      (DE),A          
48BB: 12         LD      (DE),A          
48BC: 12         LD      (DE),A          
48BD: 12         LD      (DE),A          
48BE: 3A         LD      A,(HLD)         
48BF: 3A         LD      A,(HLD)         
48C0: 00         NOP                     
48C1: 00         NOP                     
48C2: 27         DAA                     
48C3: 27         DAA                     
48C4: 28 28      JR      Z,$48EE         
48C6: 28 28      JR      Z,$48F0         
48C8: AB         XOR     E               
48C9: AB         XOR     E               
48CA: 68         LD      L,B             
48CB: 68         LD      L,B             
48CC: 28 28      JR      Z,$48F6         
48CE: 27         DAA                     
48CF: 27         DAA                     
48D0: 00         NOP                     
48D1: 00         NOP                     
48D2: 30 30      JR      NC,$4904        
48D4: 88         ADC     A,B             
48D5: 88         ADC     A,B             
48D6: 04         INC     B               
48D7: 04         INC     B               
48D8: 84         ADD     A,H             
48D9: 84         ADD     A,H             
48DA: 84         ADD     A,H             
48DB: 84         ADD     A,H             
48DC: 88         ADC     A,B             
48DD: 88         ADC     A,B             
48DE: 30 30      JR      NC,$4910        
48E0: 00         NOP                     
48E1: 00         NOP                     
48E2: 00         NOP                     
48E3: 00         NOP                     
48E4: 44         LD      B,H             
48E5: 00         NOP                     
48E6: 28 00      JR      Z,$48E8         
48E8: 10 00      STOP    $00             
48EA: 28 00      JR      Z,$48EC         
48EC: 44         LD      B,H             
48ED: 00         NOP                     
48EE: 00         NOP                     
48EF: 00         NOP                     
48F0: 00         NOP                     
48F1: 00         NOP                     
48F2: 00         NOP                     
48F3: 00         NOP                     
48F4: 44         LD      B,H             
48F5: 00         NOP                     
48F6: 28 00      JR      Z,$48F8         
48F8: 10 00      STOP    $00             
48FA: 28 00      JR      Z,$48FC         
48FC: 44         LD      B,H             
48FD: 00         NOP                     
48FE: 00         NOP                     
48FF: 00         NOP                     
4900: 00         NOP                     
4901: 01 00 01   LD      BC,$0100        
4904: 00         NOP                     
4905: 01 00 02   LD      BC,$0200        
4908: 00         NOP                     
4909: 02         LD      (BC),A          
490A: 00         NOP                     
490B: 02         LD      (BC),A          
490C: 01 05 01   LD      BC,$0105        
490F: 05         DEC     B               
4910: 00         NOP                     
4911: FF         RST     0X38            
4912: 00         NOP                     
4913: 00         NOP                     
4914: 7F         LD      A,A             
4915: 7F         LD      A,A             
4916: FF         RST     0X38            
4917: FF         RST     0X38            
4918: FF         RST     0X38            
4919: FF         RST     0X38            
491A: FF         RST     0X38            
491B: FF         RST     0X38            
491C: FF         RST     0X38            
491D: FC         ???                     
491E: FF         RST     0X38            
491F: F8 00      LDHL    SP,$00          
4921: FF         RST     0X38            
4922: 00         NOP                     
4923: 00         NOP                     
4924: FF         RST     0X38            
4925: FF         RST     0X38            
4926: FF         RST     0X38            
4927: FF         RST     0X38            
4928: FF         RST     0X38            
4929: FF         RST     0X38            
492A: FF         RST     0X38            
492B: FF         RST     0X38            
492C: FF         RST     0X38            
492D: 00         NOP                     
492E: FF         RST     0X38            
492F: 00         NOP                     
4930: 00         NOP                     
4931: FF         RST     0X38            
4932: 00         NOP                     
4933: 00         NOP                     
4934: FF         RST     0X38            
4935: FF         RST     0X38            
4936: FF         RST     0X38            
4937: FF         RST     0X38            
4938: FF         RST     0X38            
4939: FF         RST     0X38            
493A: FF         RST     0X38            
493B: FF         RST     0X38            
493C: FF         RST     0X38            
493D: 3D         DEC     A               
493E: 3D         DEC     A               
493F: 39         ADD     HL,SP           
4940: 00         NOP                     
4941: FF         RST     0X38            
4942: 01 00 FF   LD      BC,$FF00        
4945: FC         ???                     
4946: FF         RST     0X38            
4947: F8 FE      LDHL    SP,$FE          
4949: F8 FE      LDHL    SP,$FE          
494B: F0 FC      LD      A,($FC)         
494D: F0 FC      LD      A,($FC)         
494F: E0 80      LDFF00  ($80),A         
4951: 00         NOP                     
4952: 80         ADD     A,B             
4953: 7E         LD      A,(HL)          
4954: 3E 7F      LD      A,$7F           
4956: 2A         LD      A,(HLI)         
4957: 7F         LD      A,A             
4958: 08 7F 08   LD      ($087F),SP      
495B: 1C         INC     E               
495C: 08 1C 08   LD      ($081C),SP      
495F: 1C         INC     E               
4960: 00         NOP                     
4961: 00         NOP                     
4962: 00         NOP                     
4963: CD CD FF   CALL    $FFCD           
4966: 48         LD      C,B             
4967: FF         RST     0X38            
4968: 48         LD      C,B             
4969: FF         RST     0X38            
496A: 78         LD      A,B             
496B: FF         RST     0X38            
496C: 48         LD      C,B             
496D: FF         RST     0X38            
496E: 48         LD      C,B             
496F: FF         RST     0X38            
4970: 00         NOP                     
4971: 00         NOP                     
4972: 00         NOP                     
4973: F3         DI                      
4974: F1         POP     AF              
4975: FB         EI                      
4976: 90         SUB     B               
4977: F9         LD      SP,HL           
4978: 80         ADD     A,B             
4979: F1         POP     AF              
497A: E0 F1      LDFF00  ($F1),A         
497C: 80         ADD     A,B             
497D: F1         POP     AF              
497E: 90         SUB     B               
497F: F9         LD      SP,HL           
4980: 00         NOP                     
4981: 00         NOP                     
4982: 00         NOP                     
4983: EF         RST     0X28            
4984: C7         RST     0X00            
4985: EF         RST     0X28            
4986: 82         ADD     A,D             
4987: E7         RST     0X20            
4988: 82         ADD     A,D             
4989: C7         RST     0X00            
498A: 83         ADD     A,E             
498B: C7         RST     0X00            
498C: 82         ADD     A,D             
498D: F7         RST     0X30            
498E: 92         SUB     D               
498F: FF         RST     0X38            
4990: 00         NOP                     
4991: 00         NOP                     
4992: 00         NOP                     
4993: CE CE      ADC     $CE             
4995: FF         RST     0X38            
4996: 53         LD      D,E             
4997: FF         RST     0X38            
4998: 10 FF      STOP    $FF             
499A: 93         SUB     E               
499B: FF         RST     0X38            
499C: 11 FF 51   LD      DE,$51FF        
499F: FF         RST     0X38            
49A0: 00         NOP                     
49A1: 00         NOP                     
49A2: 00         NOP                     
49A3: 7D         LD      A,L             
49A4: 7D         LD      A,L             
49A5: FF         RST     0X38            
49A6: 24         INC     H               
49A7: FF         RST     0X38            
49A8: 20 FD      JR      NZ,$49A7        
49AA: 38 FD      JR      C,$49A9         
49AC: 20 FD      JR      NZ,$49AB        
49AE: 24         INC     H               
49AF: FF         RST     0X38            
49B0: 00         NOP                     
49B1: 00         NOP                     
49B2: 00         NOP                     
49B3: 9B         SBC     E               
49B4: 9B         SBC     E               
49B5: FF         RST     0X38            
49B6: 91         SUB     C               
49B7: FB         EI                      
49B8: D1         POP     DE              
49B9: FB         EI                      
49BA: D1         POP     DE              
49BB: FB         EI                      
49BC: B1         OR      C               
49BD: FB         EI                      
49BE: 91         SUB     C               
49BF: FB         EI                      
49C0: 00         NOP                     
49C1: 00         NOP                     
49C2: 00         NOP                     
49C3: C1         POP     BC              
49C4: C1         POP     BC              
49C5: E3         ???                     
49C6: 22         LD      (HLI),A         
49C7: F7         RST     0X30            
49C8: 22         LD      (HLI),A         
49C9: F7         RST     0X30            
49CA: 22         LD      (HLI),A         
49CB: F7         RST     0X30            
49CC: 22         LD      (HLI),A         
49CD: F7         RST     0X30            
49CE: 22         LD      (HLI),A         
49CF: F7         RST     0X30            
49D0: 00         NOP                     
49D1: 00         NOP                     
49D2: 00         NOP                     
49D3: CF         RST     0X08            
49D4: CF         RST     0X08            
49D5: FF         RST     0X38            
49D6: 24         INC     H               
49D7: FF         RST     0X38            
49D8: 24         INC     H               
49D9: 7F         LD      A,A             
49DA: 27         DAA                     
49DB: 7F         LD      A,A             
49DC: 24         INC     H               
49DD: 7F         LD      A,A             
49DE: 24         INC     H               
49DF: FE 00      CP      $00             
49E1: 00         NOP                     
49E2: 00         NOP                     
49E3: 80         ADD     A,B             
49E4: 80         ADD     A,B             
49E5: C0         RET     NZ              
49E6: 80         ADD     A,B             
49E7: C0         RET     NZ              
49E8: 00         NOP                     
49E9: 80         ADD     A,B             
49EA: 00         NOP                     
49EB: 80         ADD     A,B             
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
4A00: 01 05 03   LD      BC,$0305        
4A03: 0B         DEC     BC              
4A04: 03         INC     BC              
4A05: 0B         DEC     BC              
4A06: 03         INC     BC              
4A07: 0B         DEC     BC              
4A08: 07         RLCA                    
4A09: 17         RLA                     
4A0A: 07         RLCA                    
4A0B: 16 07      LD      D,$07           
4A0D: 14         INC     D               
4A0E: 0F         RRCA                    
4A0F: 38 FE      JR      C,$4A0F         
4A11: F0 FC      LD      A,($FC)         
4A13: E0 F8      LDFF00  ($F8),A         
4A15: C0         RET     NZ              
4A16: F0 80      LD      A,($80)         
4A18: E0 00      LDFF00  ($00),A         
4A1A: C0         RET     NZ              
4A1B: 00         NOP                     
4A1C: 80         ADD     A,B             
4A1D: 00         NOP                     
4A1E: 00         NOP                     
4A1F: 00         NOP                     
4A20: 00         NOP                     
4A21: 01 00 03   LD      BC,$0300        
4A24: 00         NOP                     
4A25: 02         LD      (BC),A          
4A26: 00         NOP                     
4A27: 06 01      LD      B,$01           
4A29: 05         DEC     B               
4A2A: 01 0D 03   LD      BC,$030D        
4A2D: 0B         DEC     BC              
4A2E: 03         INC     BC              
4A2F: 1B         DEC     DE              
4A30: 7F         LD      A,A             
4A31: 79         LD      A,C             
4A32: 7B         LD      A,E             
4A33: 73         LD      (HL),E          
4A34: FB         EI                      
4A35: E3         ???                     
4A36: F7         RST     0X30            
4A37: E7         RST     0X20            
4A38: F7         RST     0X30            
4A39: C7         RST     0X00            
4A3A: E7         RST     0X20            
4A3B: C7         RST     0X00            
4A3C: EF         RST     0X28            
4A3D: 8F         ADC     A,A             
4A3E: CF         RST     0X08            
4A3F: 8E         ADC     A,(HL)          
4A40: F8 E0      LDHL    SP,$E0          
4A42: E0 CF      LDFF00  ($CF),A         
4A44: C0         RET     NZ              
4A45: C0         RET     NZ              
4A46: FF         RST     0X38            
4A47: 9F         SBC     A               
4A48: FF         RST     0X38            
4A49: 8F         ADC     A,A             
4A4A: FF         RST     0X38            
4A4B: 07         RLCA                    
4A4C: DF         RST     0X18            
4A4D: 03         INC     BC              
4A4E: CD 01 1C   CALL    $1C01           
4A51: 3F         CCF                     
4A52: 00         NOP                     
4A53: FF         RST     0X38            
4A54: 00         NOP                     
4A55: 00         NOP                     
4A56: FF         RST     0X38            
4A57: FF         RST     0X38            
4A58: FF         RST     0X38            
4A59: FF         RST     0X38            
4A5A: FF         RST     0X38            
4A5B: FF         RST     0X38            
4A5C: FF         RST     0X38            
4A5D: F0 FF      LD      A,($FF)         
4A5F: F0 CD      LD      A,($CD)         
4A61: FF         RST     0X38            
4A62: 00         NOP                     
4A63: FF         RST     0X38            
4A64: 00         NOP                     
4A65: 00         NOP                     
4A66: FF         RST     0X38            
4A67: FC         ???                     
4A68: FF         RST     0X38            
4A69: FC         ???                     
4A6A: FF         RST     0X38            
4A6B: FC         ???                     
4A6C: FF         RST     0X38            
4A6D: 3C         INC     A               
4A6E: FF         RST     0X38            
4A6F: 3C         INC     A               
4A70: F1         POP     AF              
4A71: FB         EI                      
4A72: 00         NOP                     
4A73: FF         RST     0X38            
4A74: 00         NOP                     
4A75: 00         NOP                     
4A76: FF         RST     0X38            
4A77: FF         RST     0X38            
4A78: FF         RST     0X38            
4A79: 7F         LD      A,A             
4A7A: FF         RST     0X38            
4A7B: 3F         CCF                     
4A7C: DF         RST     0X18            
4A7D: 1F         RRA                     
4A7E: 5F         LD      E,A             
4A7F: 1F         RRA                     
4A80: F7         RST     0X30            
4A81: FF         RST     0X38            
4A82: 00         NOP                     
4A83: FF         RST     0X38            
4A84: 00         NOP                     
4A85: 04         INC     B               
4A86: FC         ???                     
4A87: E0 F8      LDFF00  ($F8),A         
4A89: C0         RET     NZ              
4A8A: F0 80      LD      A,($80)         
4A8C: E0 00      LDFF00  ($00),A         
4A8E: C0         RET     NZ              
4A8F: 00         NOP                     
4A90: CE FF      ADC     $FF             
4A92: 00         NOP                     
4A93: FF         RST     0X38            
4A94: C0         RET     NZ              
4A95: 00         NOP                     
4A96: FF         RST     0X38            
4A97: 1F         RRA                     
4A98: 7F         LD      A,A             
4A99: 0F         RRCA                    
4A9A: 3F         CCF                     
4A9B: 07         RLCA                    
4A9C: 1B         DEC     DE              
4A9D: 03         INC     BC              
4A9E: 0B         DEC     BC              
4A9F: 03         INC     BC              
4AA0: 7D         LD      A,L             
4AA1: FF         RST     0X38            
4AA2: 00         NOP                     
4AA3: FF         RST     0X38            
4AA4: 07         RLCA                    
4AA5: 00         NOP                     
4AA6: FF         RST     0X38            
4AA7: F8 FF      LDHL    SP,$FF          
4AA9: FE FF      CP      $FF             
4AAB: FF         RST     0X38            
4AAC: FF         RST     0X38            
4AAD: FF         RST     0X38            
4AAE: FF         RST     0X38            
4AAF: E3         ???                     
4AB0: 9B         SBC     E               
4AB1: FF         RST     0X38            
4AB2: 00         NOP                     
4AB3: 9B         SBC     E               
4AB4: 00         NOP                     
4AB5: 00         NOP                     
4AB6: C0         RET     NZ              
4AB7: 00         NOP                     
4AB8: E0 00      LDFF00  ($00),A         
4ABA: F0 80      LD      A,($80)         
4ABC: F8 C0      LDHL    SP,$C0          
4ABE: F8 E0      LDHL    SP,$E0          
4AC0: C1         POP     BC              
4AC1: E3         ???                     
4AC2: 00         NOP                     
4AC3: FF         RST     0X38            
4AC4: C0         RET     NZ              
4AC5: 00         NOP                     
4AC6: FF         RST     0X38            
4AC7: 1F         RRA                     
4AC8: 7F         LD      A,A             
4AC9: 0F         RRCA                    
4ACA: 37         SCF                     
4ACB: 07         RLCA                    
4ACC: 17         RLA                     
4ACD: 07         RLCA                    
4ACE: 07         RLCA                    
4ACF: 17         RLA                     
4AD0: CE FF      ADC     $FF             
4AD2: 00         NOP                     
4AD3: FF         RST     0X38            
4AD4: 70         LD      (HL),B          
4AD5: 00         NOP                     
4AD6: F0 C0      LD      A,($C0)         
4AD8: F0 C0      LD      A,($C0)         
4ADA: F8 C0      LDHL    SP,$C0          
4ADC: F8 E0      LDHL    SP,$E0          
4ADE: F8 E0      LDHL    SP,$E0          
4AE0: 00         NOP                     
4AE1: 00         NOP                     
4AE2: 00         NOP                     
4AE3: 00         NOP                     
4AE4: 00         NOP                     
4AE5: 00         NOP                     
4AE6: FA FA 23   LD      A,($23FA)       
4AE9: 23         INC     HL              
4AEA: 22         LD      (HLI),A         
4AEB: 22         LD      (HLI),A         
4AEC: 22         LD      (HLI),A         
4AED: 22         LD      (HLI),A         
4AEE: 22         LD      (HLI),A         
4AEF: 22         LD      (HLI),A         
4AF0: 00         NOP                     
4AF1: 00         NOP                     
4AF2: 00         NOP                     
4AF3: 00         NOP                     
4AF4: 00         NOP                     
4AF5: 00         NOP                     
4AF6: 08 08 18   LD      ($1808),SP      
4AF9: 18 A8      JR      $4AA3           
4AFB: A8         XOR     B               
4AFC: 48         LD      C,B             
4AFD: 48         LD      C,B             
4AFE: 08 08 0E   LD      ($0E08),SP      
4B01: 20 0C      JR      NZ,$4B0F        
4B03: 20 38      JR      NZ,$4B3D        
4B05: 00         NOP                     
4B06: 00         NOP                     
4B07: 00         NOP                     
4B08: 00         NOP                     
4B09: 00         NOP                     
4B0A: 00         NOP                     
4B0B: 00         NOP                     
4B0C: 00         NOP                     
4B0D: 00         NOP                     
4B0E: 00         NOP                     
4B0F: 00         NOP                     
4B10: 00         NOP                     
4B11: 00         NOP                     
4B12: 00         NOP                     
4B13: 00         NOP                     
4B14: 00         NOP                     
4B15: 00         NOP                     
4B16: 00         NOP                     
4B17: 00         NOP                     
4B18: 00         NOP                     
4B19: 00         NOP                     
4B1A: 00         NOP                     
4B1B: 00         NOP                     
4B1C: 00         NOP                     
4B1D: 00         NOP                     
4B1E: 00         NOP                     
4B1F: 01 07 17   LD      BC,$1707        
4B22: 07         RLCA                    
4B23: 37         SCF                     
4B24: 0F         RRCA                    
4B25: 2E 0F      LD      L,$0F           
4B27: 6E         LD      L,(HL)          
4B28: 1F         RRA                     
4B29: 5E         LD      E,(HL)          
4B2A: 1F         RRA                     
4B2B: DE 3F      SBC     $3F             
4B2D: BF         CP      A               
4B2E: 3F         CCF                     
4B2F: BD         CP      L               
4B30: CF         RST     0X08            
4B31: 0E 9F      LD      C,$9F           
4B33: 1C         INC     E               
4B34: 9F         SBC     A               
4B35: 1C         INC     E               
4B36: 3F         CCF                     
4B37: 38 7E      JR      C,$4BB7         
4B39: 78         LD      A,B             
4B3A: FE F0      CP      $F0             
4B3C: FC         ???                     
4B3D: F0 FC      LD      A,($FC)         
4B3F: E0 81      LDFF00  ($81),A         
4B41: 05         DEC     B               
4B42: 81         ADD     A,C             
4B43: 05         DEC     B               
4B44: 01 05 01   LD      BC,$0105        
4B47: 05         DEC     B               
4B48: 01 05 01   LD      BC,$0105        
4B4B: 05         DEC     B               
4B4C: 01 05 01   LD      BC,$0105        
4B4F: 05         DEC     B               
4B50: FC         ???                     
4B51: F0 FC      LD      A,($FC)         
4B53: F0 FC      LD      A,($FC)         
4B55: F0 FC      LD      A,($FC)         
4B57: F1         POP     AF              
4B58: FC         ???                     
4B59: F1         POP     AF              
4B5A: FC         ???                     
4B5B: F2         ???                     
4B5C: FD         ???                     
4B5D: F3         DI                      
4B5E: F1         POP     AF              
4B5F: FD         ???                     
4B60: FF         RST     0X38            
4B61: 1C         INC     E               
4B62: 7F         LD      A,A             
4B63: 1C         INC     E               
4B64: 7F         LD      A,A             
4B65: 0C         INC     C               
4B66: 7F         LD      A,A             
4B67: 8C         ADC     A,H             
4B68: 7F         LD      A,A             
4B69: 04         INC     B               
4B6A: FF         RST     0X38            
4B6B: 84         ADD     A,H             
4B6C: FF         RST     0X38            
4B6D: 80         ADD     A,B             
4B6E: EF         RST     0X28            
4B6F: 80         ADD     A,B             
4B70: 1F         RRA                     
4B71: 5F         LD      E,A             
4B72: 1F         RRA                     
4B73: 5F         LD      E,A             
4B74: 1F         RRA                     
4B75: 5F         LD      E,A             
4B76: 1F         RRA                     
4B77: 5F         LD      E,A             
4B78: 1F         RRA                     
4B79: 5F         LD      E,A             
4B7A: 1F         RRA                     
4B7B: 5F         LD      E,A             
4B7C: 1F         RRA                     
4B7D: 5F         LD      E,A             
4B7E: 1F         RRA                     
4B7F: 5F         LD      E,A             
4B80: C0         RET     NZ              
4B81: 00         NOP                     
4B82: C0         RET     NZ              
4B83: 00         NOP                     
4B84: C0         RET     NZ              
4B85: 00         NOP                     
4B86: C0         RET     NZ              
4B87: 00         NOP                     
4B88: C0         RET     NZ              
4B89: 00         NOP                     
4B8A: C0         RET     NZ              
4B8B: 00         NOP                     
4B8C: C0         RET     NZ              
4B8D: 00         NOP                     
4B8E: C0         RET     NZ              
4B8F: 00         NOP                     
4B90: 03         INC     BC              
4B91: 0B         DEC     BC              
4B92: 03         INC     BC              
4B93: 0B         DEC     BC              
4B94: 03         INC     BC              
4B95: 0B         DEC     BC              
4B96: 03         INC     BC              
4B97: 0B         DEC     BC              
4B98: 03         INC     BC              
4B99: 0B         DEC     BC              
4B9A: 03         INC     BC              
4B9B: 0B         DEC     BC              
4B9C: 03         INC     BC              
4B9D: 0B         DEC     BC              
4B9E: 03         INC     BC              
4B9F: 0B         DEC     BC              
4BA0: FF         RST     0X38            
4BA1: E1         POP     HL              
4BA2: FF         RST     0X38            
4BA3: E0 FB      LDFF00  ($FB),A         
4BA5: E0 F9      LDFF00  ($F9),A         
4BA7: E0 F8      LDFF00  ($F8),A         
4BA9: E0 F8      LDFF00  ($F8),A         
4BAB: E1         POP     HL              
4BAC: F8 E1      LDHL    SP,$E1          
4BAE: F8 E1      LDHL    SP,$E1          
4BB0: FC         ???                     
4BB1: F0 FC      LD      A,($FC)         
4BB3: F0 FE      LD      A,($FE)         
4BB5: F8 FE      LDHL    SP,$FE          
4BB7: 78         LD      A,B             
4BB8: FE 78      CP      $78             
4BBA: FF         RST     0X38            
4BBB: 7C         LD      A,H             
4BBC: 7F         LD      A,A             
4BBD: 7C         LD      A,H             
4BBE: 7F         LD      A,A             
4BBF: 7C         LD      A,H             
4BC0: 07         RLCA                    
4BC1: 17         RLA                     
4BC2: 07         RLCA                    
4BC3: 17         RLA                     
4BC4: 07         RLCA                    
4BC5: 17         RLA                     
4BC6: 0F         RRCA                    
4BC7: 2F         CPL                     
4BC8: 0F         RRCA                    
4BC9: 2F         CPL                     
4BCA: 0E 2C      LD      C,$2C           
4BCC: 0E 2C      LD      C,$2C           
4BCE: 1E 5C      LD      E,$5C           
4BD0: F8 E0      LDHL    SP,$E0          
4BD2: FC         ???                     
4BD3: E0 FC      LDFF00  ($FC),A         
4BD5: F0 FC      LD      A,($FC)         
4BD7: F0 FC      LD      A,($FC)         
4BD9: F0 FE      LD      A,($FE)         
4BDB: F0 FE      LD      A,($FE)         
4BDD: F8 FE      LDHL    SP,$FE          
4BDF: F8 22      LDHL    SP,$22          
4BE1: 22         LD      (HLI),A         
4BE2: 00         NOP                     
4BE3: 00         NOP                     
4BE4: 00         NOP                     
4BE5: 00         NOP                     
4BE6: 00         NOP                     
4BE7: 00         NOP                     
4BE8: 00         NOP                     
4BE9: 00         NOP                     
4BEA: 00         NOP                     
4BEB: 00         NOP                     
4BEC: 00         NOP                     
4BED: 00         NOP                     
4BEE: 00         NOP                     
4BEF: 00         NOP                     
4BF0: 08 08 00   LD      ($0008),SP      
4BF3: 00         NOP                     
4BF4: 00         NOP                     
4BF5: 00         NOP                     
4BF6: 00         NOP                     
4BF7: 00         NOP                     
4BF8: 00         NOP                     
4BF9: 00         NOP                     
4BFA: 00         NOP                     
4BFB: 00         NOP                     
4BFC: 00         NOP                     
4BFD: 00         NOP                     
4BFE: 00         NOP                     
4BFF: 00         NOP                     
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
4C0A: 00         NOP                     
4C0B: 00         NOP                     
4C0C: 00         NOP                     
4C0D: 00         NOP                     
4C0E: 00         NOP                     
4C0F: 00         NOP                     
4C10: 00         NOP                     
4C11: 01 00 03   LD      BC,$0300        
4C14: 00         NOP                     
4C15: 02         LD      (BC),A          
4C16: 00         NOP                     
4C17: 06 01      LD      B,$01           
4C19: 05         DEC     B               
4C1A: 01 0D 03   LD      BC,$030D        
4C1D: 0B         DEC     BC              
4C1E: 03         INC     BC              
4C1F: 1B         DEC     DE              
4C20: 7D         LD      A,L             
4C21: 79         LD      A,C             
4C22: 7D         LD      A,L             
4C23: 71         LD      (HL),C          
4C24: F9         LD      SP,HL           
4C25: E1         POP     HL              
4C26: F9         LD      SP,HL           
4C27: C7         RST     0X00            
4C28: C3 CF C7   JP      $C7CF           
4C2B: CF         RST     0X08            
4C2C: CF         RST     0X08            
4C2D: DF         RST     0X18            
4C2E: DF         RST     0X18            
4C2F: DE F8      SBC     $F8             
4C31: E0 F8      LDFF00  ($F8),A         
4C33: C0         RET     NZ              
4C34: F0 C0      LD      A,($C0)         
4C36: F0 80      LD      A,($80)         
4C38: E0 80      LDFF00  ($80),A         
4C3A: E0 00      LDFF00  ($00),A         
4C3C: C0         RET     NZ              
4C3D: 00         NOP                     
4C3E: C0         RET     NZ              
4C3F: 00         NOP                     
4C40: 01 05 01   LD      BC,$0105        
4C43: 05         DEC     B               
4C44: 01 05 01   LD      BC,$0105        
4C47: 05         DEC     B               
4C48: 01 05 01   LD      BC,$0105        
4C4B: 05         DEC     B               
4C4C: 01 05 01   LD      BC,$0105        
4C4F: 05         DEC     B               
4C50: F3         DI                      
4C51: F3         DI                      
4C52: FF         RST     0X38            
4C53: FF         RST     0X38            
4C54: FF         RST     0X38            
4C55: FF         RST     0X38            
4C56: FF         RST     0X38            
4C57: FF         RST     0X38            
4C58: FF         RST     0X38            
4C59: F3         DI                      
4C5A: FF         RST     0X38            
4C5B: F1         POP     AF              
4C5C: FF         RST     0X38            
4C5D: F1         POP     AF              
4C5E: FF         RST     0X38            
4C5F: F0 E0      LD      A,($E0)         
4C61: 80         ADD     A,B             
4C62: E0 80      LDFF00  ($80),A         
4C64: E0 80      LDFF00  ($80),A         
4C66: E0 80      LDFF00  ($80),A         
4C68: E1         POP     HL              
4C69: 8E         ADC     A,(HL)          
4C6A: E7         RST     0X20            
4C6B: 88         ADC     A,B             
4C6C: E7         RST     0X20            
4C6D: 94         SUB     H               
4C6E: E7         RST     0X20            
4C6F: 94         SUB     H               
4C70: 1F         RRA                     
4C71: 5F         LD      E,A             
4C72: 1F         RRA                     
4C73: 5F         LD      E,A             
4C74: 1F         RRA                     
4C75: 5F         LD      E,A             
4C76: 1F         RRA                     
4C77: 5F         LD      E,A             
4C78: 1F         RRA                     
4C79: 5F         LD      E,A             
4C7A: 1F         RRA                     
4C7B: 5F         LD      E,A             
4C7C: 1F         RRA                     
4C7D: 5F         LD      E,A             
4C7E: 1F         RRA                     
4C7F: 5F         LD      E,A             
4C80: C0         RET     NZ              
4C81: 00         NOP                     
4C82: C0         RET     NZ              
4C83: 00         NOP                     
4C84: C0         RET     NZ              
4C85: 00         NOP                     
4C86: C0         RET     NZ              
4C87: 00         NOP                     
4C88: C0         RET     NZ              
4C89: 01 C0 01   LD      BC,$01C0        
4C8C: C0         RET     NZ              
4C8D: 02         LD      (BC),A          
4C8E: C0         RET     NZ              
4C8F: 02         LD      (BC),A          
4C90: 03         INC     BC              
4C91: 0B         DEC     BC              
4C92: 03         INC     BC              
4C93: 0B         DEC     BC              
4C94: 03         INC     BC              
4C95: 0B         DEC     BC              
4C96: 03         INC     BC              
4C97: 0B         DEC     BC              
4C98: 23         INC     HL              
4C99: CB E3      SET     1,E             
4C9B: 0B         DEC     BC              
4C9C: E3         ???                     
4C9D: 8B         ADC     A,E             
4C9E: E3         ???                     
4C9F: 8B         ADC     A,E             
4CA0: F8 E1      LDHL    SP,$E1          
4CA2: F8 E1      LDHL    SP,$E1          
4CA4: F8 E1      LDHL    SP,$E1          
4CA6: F8 E1      LDHL    SP,$E1          
4CA8: F8 E1      LDHL    SP,$E1          
4CAA: F8 E1      LDHL    SP,$E1          
4CAC: F8 E1      LDHL    SP,$E1          
4CAE: F8 E1      LDHL    SP,$E1          
4CB0: 7F         LD      A,A             
4CB1: 7C         LD      A,H             
4CB2: 7F         LD      A,A             
4CB3: 7C         LD      A,H             
4CB4: 7F         LD      A,A             
4CB5: 7C         LD      A,H             
4CB6: 7F         LD      A,A             
4CB7: 7C         LD      A,H             
4CB8: 7F         LD      A,A             
4CB9: 7C         LD      A,H             
4CBA: 7F         LD      A,A             
4CBB: 7C         LD      A,H             
4CBC: 7F         LD      A,A             
4CBD: 7C         LD      A,H             
4CBE: 7F         LD      A,A             
4CBF: 7C         LD      A,H             
4CC0: 1E 5C      LD      E,$5C           
4CC2: 1E 58      LD      E,$58           
4CC4: 9F         SBC     A               
4CC5: 58         LD      E,B             
4CC6: 3F         CCF                     
4CC7: B8         CP      B               
4CC8: 3F         CCF                     
4CC9: B8         CP      B               
4CCA: 3C         INC     A               
4CCB: B3         OR      E               
4CCC: 30 B0      JR      NC,$4C7E        
4CCE: 7F         LD      A,A             
4CCF: 7F         LD      A,A             
4CD0: FE F8      CP      $F8             
4CD2: FF         RST     0X38            
4CD3: F8 7F      LDHL    SP,$7F          
4CD5: 7C         LD      A,H             
4CD6: 7F         LD      A,A             
4CD7: 7C         LD      A,H             
4CD8: 7F         LD      A,A             
4CD9: 7C         LD      A,H             
4CDA: 7F         LD      A,A             
4CDB: 7C         LD      A,H             
4CDC: 3F         CCF                     
4CDD: 3E FF      LD      A,$FF           
4CDF: FE 00      CP      $00             
4CE1: 00         NOP                     
4CE2: 00         NOP                     
4CE3: 00         NOP                     
4CE4: 00         NOP                     
4CE5: 00         NOP                     
4CE6: 00         NOP                     
4CE7: 00         NOP                     
4CE8: 00         NOP                     
4CE9: 00         NOP                     
4CEA: 80         ADD     A,B             
4CEB: 00         NOP                     
4CEC: 80         ADD     A,B             
4CED: 00         NOP                     
4CEE: 80         ADD     A,B             
4CEF: 00         NOP                     
4CF0: 00         NOP                     
4CF1: 00         NOP                     
4CF2: 00         NOP                     
4CF3: 00         NOP                     
4CF4: 00         NOP                     
4CF5: 00         NOP                     
4CF6: 00         NOP                     
4CF7: 00         NOP                     
4CF8: 00         NOP                     
4CF9: 00         NOP                     
4CFA: 00         NOP                     
4CFB: 00         NOP                     
4CFC: 00         NOP                     
4CFD: 00         NOP                     
4CFE: 00         NOP                     
4CFF: 00         NOP                     
4D00: 00         NOP                     
4D01: 00         NOP                     
4D02: 00         NOP                     
4D03: 00         NOP                     
4D04: 00         NOP                     
4D05: 00         NOP                     
4D06: 00         NOP                     
4D07: 00         NOP                     
4D08: 00         NOP                     
4D09: 00         NOP                     
4D0A: 00         NOP                     
4D0B: 00         NOP                     
4D0C: 00         NOP                     
4D0D: 00         NOP                     
4D0E: 00         NOP                     
4D0F: 01 07 17   LD      BC,$1707        
4D12: 07         RLCA                    
4D13: 37         SCF                     
4D14: 0F         RRCA                    
4D15: 2F         CPL                     
4D16: 0F         RRCA                    
4D17: 6E         LD      L,(HL)          
4D18: 1F         RRA                     
4D19: 5C         LD      E,H             
4D1A: 1E D8      LD      E,$D8           
4D1C: 3E B8      LD      A,$B8           
4D1E: 3C         INC     A               
4D1F: B8         CP      B               
4D20: FF         RST     0X38            
4D21: FE FF      CP      $FF             
4D23: FC         ???                     
4D24: 7F         LD      A,A             
4D25: 7C         LD      A,H             
4D26: 7F         LD      A,A             
4D27: 78         LD      A,B             
4D28: 7E         LD      A,(HL)          
4D29: 78         LD      A,B             
4D2A: 7E         LD      A,(HL)          
4D2B: 70         LD      (HL),B          
4D2C: 7C         LD      A,H             
4D2D: 70         LD      (HL),B          
4D2E: FC         ???                     
4D2F: E0 80      LDFF00  ($80),A         
4D31: 00         NOP                     
4D32: 80         ADD     A,B             
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
4D40: 01 05 01   LD      BC,$0105        
4D43: 05         DEC     B               
4D44: 01 05 01   LD      BC,$0105        
4D47: 05         DEC     B               
4D48: 01 05 01   LD      BC,$0105        
4D4B: 05         DEC     B               
4D4C: 01 05 01   LD      BC,$0105        
4D4F: 05         DEC     B               
4D50: FD         ???                     
4D51: F0 FD      LD      A,($FD)         
4D53: F0 FC      LD      A,($FC)         
4D55: F0 FC      LD      A,($FC)         
4D57: F0 FC      LD      A,($FC)         
4D59: F0 FC      LD      A,($FC)         
4D5B: F0 FC      LD      A,($FC)         
4D5D: F0 FC      LD      A,($FC)         
4D5F: F0 EF      LD      A,($EF)         
4D61: 14         INC     D               
4D62: CF         RST     0X08            
4D63: 2C         INC     L               
4D64: 0F         RRCA                    
4D65: 2C         INC     L               
4D66: 1F         RRA                     
4D67: 2C         INC     L               
4D68: 1F         RRA                     
4D69: 5C         LD      E,H             
4D6A: 1F         RRA                     
4D6B: 5C         LD      E,H             
4D6C: 3F         CCF                     
4D6D: 5C         LD      E,H             
4D6E: 3F         CCF                     
4D6F: BC         CP      H               
4D70: 1F         RRA                     
4D71: 5F         LD      E,A             
4D72: 1F         RRA                     
4D73: 5F         LD      E,A             
4D74: 1F         RRA                     
4D75: 5F         LD      E,A             
4D76: 1F         RRA                     
4D77: 5F         LD      E,A             
4D78: 1F         RRA                     
4D79: 5F         LD      E,A             
4D7A: 1F         RRA                     
4D7B: 5F         LD      E,A             
4D7C: 1F         RRA                     
4D7D: 5F         LD      E,A             
4D7E: 1F         RRA                     
4D7F: 5F         LD      E,A             
4D80: C1         POP     BC              
4D81: 02         LD      (BC),A          
4D82: C1         POP     BC              
4D83: 05         DEC     B               
4D84: C1         POP     BC              
4D85: 05         DEC     B               
4D86: C3 05 C3   JP      $C305           
4D89: 0B         DEC     BC              
4D8A: C3 0B C7   JP      $C70B           
4D8D: 0B         DEC     BC              
4D8E: C7         RST     0X00            
4D8F: 17         RLA                     
4D90: E3         ???                     
4D91: 8B         ADC     A,E             
4D92: E3         ???                     
4D93: 8B         ADC     A,E             
4D94: E3         ???                     
4D95: 8B         ADC     A,E             
4D96: E3         ???                     
4D97: 8B         ADC     A,E             
4D98: E3         ???                     
4D99: 8B         ADC     A,E             
4D9A: E3         ???                     
4D9B: 8B         ADC     A,E             
4D9C: E3         ???                     
4D9D: 8B         ADC     A,E             
4D9E: E3         ???                     
4D9F: 8B         ADC     A,E             
4DA0: F8 E1      LDHL    SP,$E1          
4DA2: F8 E1      LDHL    SP,$E1          
4DA4: F8 E1      LDHL    SP,$E1          
4DA6: F8 E1      LDHL    SP,$E1          
4DA8: F8 E1      LDHL    SP,$E1          
4DAA: F8 E2      LDHL    SP,$E2          
4DAC: F9         LD      SP,HL           
4DAD: E3         ???                     
4DAE: FB         EI                      
4DAF: E5         PUSH    HL              
4DB0: 7E         LD      A,(HL)          
4DB1: 7D         LD      A,L             
4DB2: 7E         LD      A,(HL)          
4DB3: 7D         LD      A,L             
4DB4: 7E         LD      A,(HL)          
4DB5: 7C         LD      A,H             
4DB6: FE 78      CP      $78             
4DB8: FE 78      CP      $78             
4DBA: FC         ???                     
4DBB: FA FC F0   LD      A,($F0FC)       
4DBE: FD         ???                     
4DBF: F1         POP     AF              
4DC0: 7F         LD      A,A             
4DC1: 7F         LD      A,A             
4DC2: 7F         LD      A,A             
4DC3: 7F         LD      A,A             
4DC4: 7F         LD      A,A             
4DC5: 60         LD      H,B             
4DC6: FF         RST     0X38            
4DC7: E0 F8      LDFF00  ($F8),A         
4DC9: E0 F8      LDFF00  ($F8),A         
4DCB: C0         RET     NZ              
4DCC: F0 C0      LD      A,($C0)         
4DCE: F0 C0      LD      A,($C0)         
4DD0: FF         RST     0X38            
4DD1: FE FF      CP      $FF             
4DD3: FE DF      CP      $DF             
4DD5: 1F         RRA                     
4DD6: DF         RST     0X18            
4DD7: 1F         RRA                     
4DD8: 5F         LD      E,A             
4DD9: 1F         RRA                     
4DDA: 5F         LD      E,A             
4DDB: 1F         RRA                     
4DDC: 6F         LD      L,A             
4DDD: 0F         RRCA                    
4DDE: 2F         CPL                     
4DDF: 0F         RRCA                    
4DE0: 80         ADD     A,B             
4DE1: 00         NOP                     
4DE2: C0         RET     NZ              
4DE3: 00         NOP                     
4DE4: C0         RET     NZ              
4DE5: 00         NOP                     
4DE6: C0         RET     NZ              
4DE7: 00         NOP                     
4DE8: C0         RET     NZ              
4DE9: 00         NOP                     
4DEA: E0 00      LDFF00  ($00),A         
4DEC: E0 80      LDFF00  ($80),A         
4DEE: E0 80      LDFF00  ($80),A         
4DF0: 00         NOP                     
4DF1: 00         NOP                     
4DF2: 00         NOP                     
4DF3: 00         NOP                     
4DF4: 00         NOP                     
4DF5: 00         NOP                     
4DF6: 00         NOP                     
4DF7: 00         NOP                     
4DF8: 00         NOP                     
4DF9: 00         NOP                     
4DFA: 00         NOP                     
4DFB: 00         NOP                     
4DFC: 00         NOP                     
4DFD: 00         NOP                     
4DFE: 00         NOP                     
4DFF: 00         NOP                     
4E00: 00         NOP                     
4E01: 01 00 03   LD      BC,$0300        
4E04: 00         NOP                     
4E05: 02         LD      (BC),A          
4E06: 00         NOP                     
4E07: 06 01      LD      B,$01           
4E09: 05         DEC     B               
4E0A: 01 0D 03   LD      BC,$030D        
4E0D: 0B         DEC     BC              
4E0E: 03         INC     BC              
4E0F: 1B         DEC     DE              
4E10: 7C         LD      A,H             
4E11: 70         LD      (HL),B          
4E12: 79         LD      A,C             
4E13: 71         LD      (HL),C          
4E14: FB         EI                      
4E15: E3         ???                     
4E16: F3         DI                      
4E17: E3         ???                     
4E18: F7         RST     0X30            
4E19: E7         RST     0X20            
4E1A: E7         RST     0X20            
4E1B: C7         RST     0X00            
4E1C: EF         RST     0X28            
4E1D: CF         RST     0X08            
4E1E: DF         RST     0X18            
4E1F: DE F8      SBC     $F8             
4E21: E0 F8      LDFF00  ($F8),A         
4E23: C0         RET     NZ              
4E24: F0 C0      LD      A,($C0)         
4E26: F0 80      LD      A,($80)         
4E28: E0 80      LDFF00  ($80),A         
4E2A: E0 00      LDFF00  ($00),A         
4E2C: C0         RET     NZ              
4E2D: 00         NOP                     
4E2E: C0         RET     NZ              
4E2F: 00         NOP                     
4E30: 00         NOP                     
4E31: 00         NOP                     
4E32: 00         NOP                     
4E33: 00         NOP                     
4E34: 00         NOP                     
4E35: 00         NOP                     
4E36: 00         NOP                     
4E37: 00         NOP                     
4E38: 00         NOP                     
4E39: 00         NOP                     
4E3A: 00         NOP                     
4E3B: 01 00 03   LD      BC,$0300        
4E3E: 00         NOP                     
4E3F: 06 01      LD      B,$01           
4E41: 0D         DEC     C               
4E42: 03         INC     BC              
4E43: 1B         DEC     DE              
4E44: 07         RLCA                    
4E45: 37         SCF                     
4E46: 0F         RRCA                    
4E47: 6F         LD      L,A             
4E48: 1F         RRA                     
4E49: DF         RST     0X18            
4E4A: 3F         CCF                     
4E4B: B8         CP      B               
4E4C: 7F         LD      A,A             
4E4D: 78         LD      A,B             
4E4E: FE F1      CP      $F1             
4E50: F8 F7      LDHL    SP,$F7          
4E52: F0 F0      LD      A,($F0)         
4E54: FF         RST     0X38            
4E55: FF         RST     0X38            
4E56: FF         RST     0X38            
4E57: FF         RST     0X38            
4E58: FF         RST     0X38            
4E59: FF         RST     0X38            
4E5A: FF         RST     0X38            
4E5B: 00         NOP                     
4E5C: FF         RST     0X38            
4E5D: 00         NOP                     
4E5E: 00         NOP                     
4E5F: 09         ADD     HL,BC           
4E60: 3F         CCF                     
4E61: BC         CP      H               
4E62: 7F         LD      A,A             
4E63: 3C         INC     A               
4E64: FE FD      CP      $FD             
4E66: FC         ???                     
4E67: FD         ???                     
4E68: FC         ???                     
4E69: FC         ???                     
4E6A: FF         RST     0X38            
4E6B: 00         NOP                     
4E6C: FF         RST     0X38            
4E6D: 00         NOP                     
4E6E: 00         NOP                     
4E6F: 12         LD      (DE),A          
4E70: 1F         RRA                     
4E71: 5F         LD      E,A             
4E72: 1F         RRA                     
4E73: DF         RST     0X18            
4E74: 3F         CCF                     
4E75: BF         CP      A               
4E76: 7F         LD      A,A             
4E77: 7F         LD      A,A             
4E78: FF         RST     0X38            
4E79: FF         RST     0X38            
4E7A: FF         RST     0X38            
4E7B: 00         NOP                     
4E7C: FF         RST     0X38            
4E7D: 00         NOP                     
4E7E: 00         NOP                     
4E7F: 2C         INC     L               
4E80: 87         ADD     A,A             
4E81: 77         LD      (HL),A          
4E82: 0F         RRCA                    
4E83: 07         RLCA                    
4E84: FF         RST     0X38            
4E85: FF         RST     0X38            
4E86: FF         RST     0X38            
4E87: FF         RST     0X38            
4E88: FF         RST     0X38            
4E89: FF         RST     0X38            
4E8A: FF         RST     0X38            
4E8B: 00         NOP                     
4E8C: FF         RST     0X38            
4E8D: 00         NOP                     
4E8E: 00         NOP                     
4E8F: E0 E3      LDFF00  ($E3),A         
4E91: 8B         ADC     A,E             
4E92: F3         DI                      
4E93: 8B         ADC     A,E             
4E94: E7         RST     0X20            
4E95: 97         SUB     A               
4E96: CF         RST     0X08            
4E97: AF         XOR     A               
4E98: DF         RST     0X18            
4E99: 9F         SBC     A               
4E9A: FF         RST     0X38            
4E9B: 00         NOP                     
4E9C: FF         RST     0X38            
4E9D: 00         NOP                     
4E9E: 00         NOP                     
4E9F: 11 E7 EB   LD      DE,$EBE7        
4EA2: FF         RST     0X38            
4EA3: FF         RST     0X38            
4EA4: FF         RST     0X38            
4EA5: FF         RST     0X38            
4EA6: FF         RST     0X38            
4EA7: FE FF      CP      $FF             
4EA9: F8 FF      LDHL    SP,$FF          
4EAB: 00         NOP                     
4EAC: FC         ???                     
4EAD: 00         NOP                     
4EAE: 00         NOP                     
4EAF: 24         INC     H               
4EB0: FD         ???                     
4EB1: E1         POP     HL              
4EB2: F9         LD      SP,HL           
4EB3: C5         PUSH    BC              
4EB4: F3         DI                      
4EB5: 8B         ADC     A,E             
4EB6: E7         RST     0X20            
4EB7: 07         RLCA                    
4EB8: EF         RST     0X28            
4EB9: 0F         RRCA                    
4EBA: BF         CP      A               
4EBB: 00         NOP                     
4EBC: 3F         CCF                     
4EBD: 00         NOP                     
4EBE: 00         NOP                     
4EBF: 44         LD      B,H             
4EC0: F0 C0      LD      A,($C0)         
4EC2: F8 C0      LDHL    SP,$C0          
4EC4: FC         ???                     
4EC5: E0 FF      LDFF00  ($FF),A         
4EC7: F0 FF      LD      A,($FF)         
4EC9: F8 FF      LDHL    SP,$FF          
4ECB: 00         NOP                     
4ECC: FF         RST     0X38            
4ECD: 00         NOP                     
4ECE: 00         NOP                     
4ECF: 5F         LD      E,A             
4ED0: 2F         CPL                     
4ED1: 0F         RRCA                    
4ED2: 0F         RRCA                    
4ED3: 6F         LD      L,A             
4ED4: 1F         RRA                     
4ED5: DF         RST     0X18            
4ED6: 3F         CCF                     
4ED7: BF         CP      A               
4ED8: 7F         LD      A,A             
4ED9: 7F         LD      A,A             
4EDA: FF         RST     0X38            
4EDB: 00         NOP                     
4EDC: FF         RST     0X38            
4EDD: 00         NOP                     
4EDE: 00         NOP                     
4EDF: 44         LD      B,H             
4EE0: E0 80      LDFF00  ($80),A         
4EE2: F0 80      LD      A,($80)         
4EE4: F8 C0      LDHL    SP,$C0          
4EE6: FC         ???                     
4EE7: E0 FE      LDFF00  ($FE),A         
4EE9: F0 FE      LD      A,($FE)         
4EEB: 00         NOP                     
4EEC: FE 00      CP      $00             
4EEE: 00         NOP                     
4EEF: 91         SUB     C               
4EF0: 00         NOP                     
4EF1: 00         NOP                     
4EF2: 00         NOP                     
4EF3: 00         NOP                     
4EF4: 00         NOP                     
4EF5: 00         NOP                     
4EF6: 00         NOP                     
4EF7: 00         NOP                     
4EF8: 00         NOP                     
4EF9: 00         NOP                     
4EFA: 00         NOP                     
4EFB: 00         NOP                     
4EFC: 00         NOP                     
4EFD: 00         NOP                     
4EFE: 00         NOP                     
4EFF: 38 07      JR      C,$4F08         
4F01: 17         RLA                     
4F02: 07         RLCA                    
4F03: 37         SCF                     
4F04: 0F         RRCA                    
4F05: 2F         CPL                     
4F06: 0F         RRCA                    
4F07: 6F         LD      L,A             
4F08: 1F         RRA                     
4F09: 5F         LD      E,A             
4F0A: 1F         RRA                     
4F0B: DF         RST     0X18            
4F0C: 3F         CCF                     
4F0D: 80         ADD     A,B             
4F0E: FF         RST     0X38            
4F0F: 00         NOP                     
4F10: DF         RST     0X18            
4F11: 9E         SBC     (HL)            
4F12: BE         CP      (HL)            
4F13: BE         CP      (HL)            
4F14: FF         RST     0X38            
4F15: FF         RST     0X38            
4F16: FF         RST     0X38            
4F17: FF         RST     0X38            
4F18: FF         RST     0X38            
4F19: FF         RST     0X38            
4F1A: FF         RST     0X38            
4F1B: FF         RST     0X38            
4F1C: FF         RST     0X38            
4F1D: 00         NOP                     
4F1E: FF         RST     0X38            
4F1F: 00         NOP                     
4F20: 00         NOP                     
4F21: 7F         LD      A,A             
4F22: 00         NOP                     
4F23: 00         NOP                     
4F24: FF         RST     0X38            
4F25: FF         RST     0X38            
4F26: FF         RST     0X38            
4F27: FF         RST     0X38            
4F28: FF         RST     0X38            
4F29: FF         RST     0X38            
4F2A: FF         RST     0X38            
4F2B: FF         RST     0X38            
4F2C: FF         RST     0X38            
4F2D: 00         NOP                     
4F2E: FF         RST     0X38            
4F2F: 00         NOP                     
4F30: 01 FD 03   LD      BC,$03FD        
4F33: 03         INC     BC              
4F34: FF         RST     0X38            
4F35: FF         RST     0X38            
4F36: FF         RST     0X38            
4F37: FF         RST     0X38            
4F38: FF         RST     0X38            
4F39: FF         RST     0X38            
4F3A: FF         RST     0X38            
4F3B: FF         RST     0X38            
4F3C: FF         RST     0X38            
4F3D: 00         NOP                     
4F3E: FF         RST     0X38            
4F3F: 00         NOP                     
4F40: FD         ???                     
4F41: F3         DI                      
4F42: FD         ???                     
4F43: F3         DI                      
4F44: FD         ???                     
4F45: E3         ???                     
4F46: F9         LD      SP,HL           
4F47: E3         ???                     
4F48: F9         LD      SP,HL           
4F49: E3         ???                     
4F4A: F9         LD      SP,HL           
4F4B: C3 F1 03   JP      $03F1           
4F4E: F0 03      LD      A,($03)         
4F50: 09         ADD     HL,BC           
4F51: 9F         SBC     A               
4F52: 09         ADD     HL,BC           
4F53: 9F         SBC     A               
4F54: 09         ADD     HL,BC           
4F55: 9F         SBC     A               
4F56: 09         ADD     HL,BC           
4F57: 9F         SBC     A               
4F58: 09         ADD     HL,BC           
4F59: 9F         SBC     A               
4F5A: 09         ADD     HL,BC           
4F5B: FF         RST     0X38            
4F5C: E9         JP      (HL)            
4F5D: FF         RST     0X38            
4F5E: 00         NOP                     
4F5F: E9         JP      (HL)            
4F60: 12         LD      (DE),A          
4F61: BF         CP      A               
4F62: 12         LD      (DE),A          
4F63: BF         CP      A               
4F64: 92         SUB     D               
4F65: FF         RST     0X38            
4F66: 53         LD      D,E             
4F67: FF         RST     0X38            
4F68: 32         LD      (HLD),A         
4F69: FF         RST     0X38            
4F6A: 12         LD      (DE),A          
4F6B: BF         CP      A               
4F6C: 12         LD      (DE),A          
4F6D: BF         CP      A               
4F6E: 00         NOP                     
4F6F: 12         LD      (DE),A          
4F70: 2C         INC     L               
4F71: 7F         LD      A,A             
4F72: 49         LD      C,C             
4F73: FF         RST     0X38            
4F74: 81         ADD     A,C             
4F75: CB 00      SET     1,E             
4F77: 81         ADD     A,C             
4F78: 80         ADD     A,B             
4F79: C1         POP     BC              
4F7A: 41         LD      B,C             
4F7B: E3         ???                     
4F7C: 20 71      JR      NZ,$4FEF        
4F7E: 00         NOP                     
4F7F: 30 E0      JR      NC,$4F61        
4F81: F0 10      LD      A,($10)         
4F83: F8 00      LDHL    SP,$00          
4F85: F0 E0      LD      A,($E0)         
4F87: F0 10      LD      A,($10)         
4F89: F8 10      LDHL    SP,$10          
4F8B: F8 E0      LDHL    SP,$E0          
4F8D: F0 00      LD      A,($00)         
4F8F: E0 11      LDFF00  ($11),A         
4F91: 3B         DEC     SP              
4F92: 29         ADD     HL,HL           
4F93: 7F         LD      A,A             
4F94: 29         ADD     HL,HL           
4F95: 7F         LD      A,A             
4F96: 45         LD      B,L             
4F97: FF         RST     0X38            
4F98: 7D         LD      A,L             
4F99: FF         RST     0X38            
4F9A: 45         LD      B,L             
4F9B: FF         RST     0X38            
4F9C: 44         LD      B,H             
4F9D: EF         RST     0X28            
4F9E: 00         NOP                     
4F9F: 6C         LD      L,H             
4FA0: 24         INC     H               
4FA1: FE 24      CP      $24             
4FA3: FF         RST     0X38            
4FA4: 24         INC     H               
4FA5: FF         RST     0X38            
4FA6: 25         DEC     H               
4FA7: FF         RST     0X38            
4FA8: 25         DEC     H               
4FA9: FF         RST     0X38            
4FAA: 25         DEC     H               
4FAB: FF         RST     0X38            
4FAC: D9         RETI                    
4FAD: FF         RST     0X38            
4FAE: 00         NOP                     
4FAF: D9         RETI                    
4FB0: 44         LD      B,H             
4FB1: EE A4      XOR     $A4             
4FB3: FF         RST     0X38            
4FB4: A5         AND     L               
4FB5: FF         RST     0X38            
4FB6: 16 FF      LD      D,$FF           
4FB8: F5         PUSH    AF              
4FB9: FF         RST     0X38            
4FBA: 14         INC     D               
4FBB: FF         RST     0X38            
4FBC: 14         INC     D               
4FBD: BE         CP      (HL)            
4FBE: 00         NOP                     
4FBF: 14         INC     D               
4FC0: 5F         LD      E,A             
4FC1: FF         RST     0X38            
4FC2: 90         SUB     B               
4FC3: FF         RST     0X38            
4FC4: 10 BF      STOP    $BF             
4FC6: 1E 3F      LD      E,$3F           
4FC8: 10 BF      STOP    $BF             
4FCA: 90         SUB     B               
4FCB: FF         RST     0X38            
4FCC: 5F         LD      E,A             
4FCD: FF         RST     0X38            
4FCE: 00         NOP                     
4FCF: 5F         LD      E,A             
4FD0: 44         LD      B,H             
4FD1: EF         RST     0X28            
4FD2: 44         LD      B,H             
4FD3: EF         RST     0X28            
4FD4: 64         LD      H,H             
4FD5: FF         RST     0X38            
4FD6: 54         LD      D,H             
4FD7: FF         RST     0X38            
4FD8: 4C         LD      C,H             
4FD9: FF         RST     0X38            
4FDA: 44         LD      B,H             
4FDB: EF         RST     0X28            
4FDC: 44         LD      B,H             
4FDD: EF         RST     0X28            
4FDE: 00         NOP                     
4FDF: 44         LD      B,H             
4FE0: 91         SUB     C               
4FE1: FB         EI                      
4FE2: 91         SUB     C               
4FE3: FB         EI                      
4FE4: 99         SBC     C               
4FE5: FF         RST     0X38            
4FE6: 95         SUB     L               
4FE7: FF         RST     0X38            
4FE8: 93         SUB     E               
4FE9: FF         RST     0X38            
4FEA: 91         SUB     C               
4FEB: FB         EI                      
4FEC: 91         SUB     C               
4FED: FB         EI                      
4FEE: 00         NOP                     
4FEF: 91         SUB     C               
4FF0: 38 FC      JR      C,$4FEE         
4FF2: 44         LD      B,H             
4FF3: FE 40      CP      $40             
4FF5: FC         ???                     
4FF6: 5C         LD      E,H             
4FF7: FE 44      CP      $44             
4FF9: FE 44      CP      $44             
4FFB: FE 38      CP      $38             
4FFD: FC         ???                     
4FFE: 00         NOP                     
4FFF: 38 FD      JR      C,$4FFE         
5001: FD         ???                     
5002: F9         LD      SP,HL           
5003: F9         LD      SP,HL           
5004: F5         PUSH    AF              
5005: F5         PUSH    AF              
5006: ED         ???                     
5007: ED         ???                     
5008: C1         POP     BC              
5009: C1         POP     BC              
500A: BD         CP      L               
500B: BD         CP      L               
500C: 7D         LD      A,L             
500D: 7D         LD      A,L             
500E: FF         RST     0X38            
500F: FF         RST     0X38            
5010: C3 C3 DD   JP      $DDC3           
5013: DD         ???                     
5014: DD         ???                     
5015: DD         ???                     
5016: 83         ADD     A,E             
5017: 83         ADD     A,E             
5018: BB         CP      E               
5019: BB         CP      E               
501A: 7B         LD      A,E             
501B: 7B         LD      A,E             
501C: 07         RLCA                    
501D: 07         RLCA                    
501E: FF         RST     0X38            
501F: FF         RST     0X38            
5020: E3         ???                     
5021: E3         ???                     
5022: DD         ???                     
5023: DD         ???                     
5024: BF         CP      A               
5025: BF         CP      A               
5026: BF         CP      A               
5027: BF         CP      A               
5028: 7F         LD      A,A             
5029: 7F         LD      A,A             
502A: 7B         LD      A,E             
502B: 7B         LD      A,E             
502C: 87         ADD     A,A             
502D: 87         ADD     A,A             
502E: FF         RST     0X38            
502F: FF         RST     0X38            
5030: C3 C3 DD   JP      $DDC3           
5033: DD         ???                     
5034: DD         ???                     
5035: DD         ???                     
5036: BD         CP      L               
5037: BD         CP      L               
5038: BD         CP      L               
5039: BD         CP      L               
503A: 7B         LD      A,E             
503B: 7B         LD      A,E             
503C: 07         RLCA                    
503D: 07         RLCA                    
503E: FF         RST     0X38            
503F: FF         RST     0X38            
5040: C1         POP     BC              
5041: C1         POP     BC              
5042: DF         RST     0X18            
5043: DF         RST     0X18            
5044: DF         RST     0X18            
5045: DF         RST     0X18            
5046: 83         ADD     A,E             
5047: 83         ADD     A,E             
5048: BF         CP      A               
5049: BF         CP      A               
504A: 7F         LD      A,A             
504B: 7F         LD      A,A             
504C: 03         INC     BC              
504D: 03         INC     BC              
504E: FF         RST     0X38            
504F: FF         RST     0X38            
5050: C1         POP     BC              
5051: C1         POP     BC              
5052: DF         RST     0X18            
5053: DF         RST     0X18            
5054: DF         RST     0X18            
5055: DF         RST     0X18            
5056: 83         ADD     A,E             
5057: 83         ADD     A,E             
5058: BF         CP      A               
5059: BF         CP      A               
505A: 7F         LD      A,A             
505B: 7F         LD      A,A             
505C: 7F         LD      A,A             
505D: 7F         LD      A,A             
505E: FF         RST     0X38            
505F: FF         RST     0X38            
5060: E3         ???                     
5061: E3         ???                     
5062: DD         ???                     
5063: DD         ???                     
5064: BF         CP      A               
5065: BF         CP      A               
5066: BF         CP      A               
5067: BF         CP      A               
5068: 71         LD      (HL),C          
5069: 71         LD      (HL),C          
506A: 7B         LD      A,E             
506B: 7B         LD      A,E             
506C: 87         ADD     A,A             
506D: 87         ADD     A,A             
506E: FF         RST     0X38            
506F: FF         RST     0X38            
5070: DD         ???                     
5071: DD         ???                     
5072: DD         ???                     
5073: DD         ???                     
5074: BB         CP      E               
5075: BB         CP      E               
5076: 83         ADD     A,E             
5077: 83         ADD     A,E             
5078: BB         CP      E               
5079: BB         CP      E               
507A: 77         LD      (HL),A          
507B: 77         LD      (HL),A          
507C: 77         LD      (HL),A          
507D: 77         LD      (HL),A          
507E: FF         RST     0X38            
507F: FF         RST     0X38            
5080: E3         ???                     
5081: E3         ???                     
5082: F7         RST     0X30            
5083: F7         RST     0X30            
5084: EF         RST     0X28            
5085: EF         RST     0X28            
5086: EF         RST     0X28            
5087: EF         RST     0X28            
5088: DF         RST     0X18            
5089: DF         RST     0X18            
508A: DF         RST     0X18            
508B: DF         RST     0X18            
508C: 8F         ADC     A,A             
508D: 8F         ADC     A,A             
508E: FF         RST     0X38            
508F: FF         RST     0X38            
5090: FD         ???                     
5091: FD         ???                     
5092: FD         ???                     
5093: FD         ???                     
5094: FB         EI                      
5095: FB         EI                      
5096: FB         EI                      
5097: FB         EI                      
5098: 77         LD      (HL),A          
5099: 77         LD      (HL),A          
509A: 77         LD      (HL),A          
509B: 77         LD      (HL),A          
509C: 8F         ADC     A,A             
509D: 8F         ADC     A,A             
509E: FF         RST     0X38            
509F: FF         RST     0X38            
50A0: DB         ???                     
50A1: DB         ???                     
50A2: D7         RST     0X10            
50A3: D7         RST     0X10            
50A4: CF         RST     0X08            
50A5: CF         RST     0X08            
50A6: 9F         SBC     A               
50A7: 9F         SBC     A               
50A8: 9F         SBC     A               
50A9: 9F         SBC     A               
50AA: 6F         LD      L,A             
50AB: 6F         LD      L,A             
50AC: 77         LD      (HL),A          
50AD: 77         LD      (HL),A          
50AE: FF         RST     0X38            
50AF: FF         RST     0X38            
50B0: DF         RST     0X18            
50B1: DF         RST     0X18            
50B2: DF         RST     0X18            
50B3: DF         RST     0X18            
50B4: BF         CP      A               
50B5: BF         CP      A               
50B6: BF         CP      A               
50B7: BF         CP      A               
50B8: BF         CP      A               
50B9: BF         CP      A               
50BA: 7F         LD      A,A             
50BB: 7F         LD      A,A             
50BC: 07         RLCA                    
50BD: 07         RLCA                    
50BE: FF         RST     0X38            
50BF: FF         RST     0X38            
50C0: ED         ???                     
50C1: ED         ???                     
50C2: C9         RET                     
50C3: C9         RET                     
50C4: C5         PUSH    BC              
50C5: C5         PUSH    BC              
50C6: AD         XOR     L               
50C7: AD         XOR     L               
50C8: BB         CP      E               
50C9: BB         CP      E               
50CA: 7B         LD      A,E             
50CB: 7B         LD      A,E             
50CC: 7B         LD      A,E             
50CD: 7B         LD      A,E             
50CE: FF         RST     0X38            
50CF: FF         RST     0X38            
50D0: DD         ???                     
50D1: DD         ???                     
50D2: DD         ???                     
50D3: DD         ???                     
50D4: 8D         ADC     A,L             
50D5: 8D         ADC     A,L             
50D6: AB         XOR     E               
50D7: AB         XOR     E               
50D8: B3         OR      E               
50D9: B3         OR      E               
50DA: 7B         LD      A,E             
50DB: 7B         LD      A,E             
50DC: 7B         LD      A,E             
50DD: 7B         LD      A,E             
50DE: FF         RST     0X38            
50DF: FF         RST     0X38            
50E0: C3 C3 BD   JP      $BDC3           
50E3: BD         CP      L               
50E4: BD         CP      L               
50E5: BD         CP      L               
50E6: 7D         LD      A,L             
50E7: 7D         LD      A,L             
50E8: 7B         LD      A,E             
50E9: 7B         LD      A,E             
50EA: 7B         LD      A,E             
50EB: 7B         LD      A,E             
50EC: 87         ADD     A,A             
50ED: 87         ADD     A,A             
50EE: FF         RST     0X38            
50EF: FF         RST     0X38            
50F0: C3 C3 DD   JP      $DDC3           
50F3: DD         ???                     
50F4: BD         CP      L               
50F5: BD         CP      L               
50F6: 83         ADD     A,E             
50F7: 83         ADD     A,E             
50F8: BF         CP      A               
50F9: BF         CP      A               
50FA: 7F         LD      A,A             
50FB: 7F         LD      A,A             
50FC: 7F         LD      A,A             
50FD: 7F         LD      A,A             
50FE: FF         RST     0X38            
50FF: FF         RST     0X38            
5100: C3 C3 BD   JP      $BDC3           
5103: BD         CP      L               
5104: BD         CP      L               
5105: BD         CP      L               
5106: 7D         LD      A,L             
5107: 7D         LD      A,L             
5108: 63         LD      H,E             
5109: 63         LD      H,E             
510A: 7B         LD      A,E             
510B: 7B         LD      A,E             
510C: 85         ADD     A,L             
510D: 85         ADD     A,L             
510E: FF         RST     0X38            
510F: FF         RST     0X38            
5110: C3 C3 DD   JP      $DDC3           
5113: DD         ???                     
5114: BD         CP      L               
5115: BD         CP      L               
5116: 83         ADD     A,E             
5117: 83         ADD     A,E             
5118: B7         OR      A               
5119: B7         OR      A               
511A: 77         LD      (HL),A          
511B: 77         LD      (HL),A          
511C: 77         LD      (HL),A          
511D: 77         LD      (HL),A          
511E: FF         RST     0X38            
511F: FF         RST     0X38            
5120: C3 C3 BD   JP      $BDC3           
5123: BD         CP      L               
5124: BF         CP      A               
5125: BF         CP      A               
5126: C7         RST     0X00            
5127: C7         RST     0X00            
5128: FB         EI                      
5129: FB         EI                      
512A: 7B         LD      A,E             
512B: 7B         LD      A,E             
512C: 87         ADD     A,A             
512D: 87         ADD     A,A             
512E: FF         RST     0X38            
512F: FF         RST     0X38            
5130: 81         ADD     A,C             
5131: 81         ADD     A,C             
5132: EF         RST     0X28            
5133: EF         RST     0X28            
5134: EF         RST     0X28            
5135: EF         RST     0X28            
5136: DF         RST     0X18            
5137: DF         RST     0X18            
5138: DF         RST     0X18            
5139: DF         RST     0X18            
513A: BF         CP      A               
513B: BF         CP      A               
513C: BF         CP      A               
513D: BF         CP      A               
513E: FF         RST     0X38            
513F: FF         RST     0X38            
5140: DD         ???                     
5141: DD         ???                     
5142: DD         ???                     
5143: DD         ???                     
5144: BB         CP      E               
5145: BB         CP      E               
5146: BB         CP      E               
5147: BB         CP      E               
5148: 77         LD      (HL),A          
5149: 77         LD      (HL),A          
514A: 77         LD      (HL),A          
514B: 77         LD      (HL),A          
514C: 8F         ADC     A,A             
514D: 8F         ADC     A,A             
514E: FF         RST     0X38            
514F: FF         RST     0X38            
5150: 7D         LD      A,L             
5151: 7D         LD      A,L             
5152: 7B         LD      A,E             
5153: 7B         LD      A,E             
5154: 77         LD      (HL),A          
5155: 77         LD      (HL),A          
5156: 6F         LD      L,A             
5157: 6F         LD      L,A             
5158: 5F         LD      E,A             
5159: 5F         LD      E,A             
515A: 3F         CCF                     
515B: 3F         CCF                     
515C: 7F         LD      A,A             
515D: 7F         LD      A,A             
515E: FF         RST     0X38            
515F: FF         RST     0X38            
5160: BD         CP      L               
5161: BD         CP      L               
5162: BD         CP      L               
5163: BD         CP      L               
5164: BB         CP      E               
5165: BB         CP      E               
5166: 6B         LD      L,E             
5167: 6B         LD      L,E             
5168: 4B         LD      C,E             
5169: 4B         LD      C,E             
516A: 27         DAA                     
516B: 27         DAA                     
516C: 77         LD      (HL),A          
516D: 77         LD      (HL),A          
516E: FF         RST     0X38            
516F: FF         RST     0X38            
5170: DD         ???                     
5171: DD         ???                     
5172: DB         ???                     
5173: DB         ???                     
5174: E7         RST     0X20            
5175: E7         RST     0X20            
5176: EF         RST     0X28            
5177: EF         RST     0X28            
5178: CF         RST     0X08            
5179: CF         RST     0X08            
517A: B7         OR      A               
517B: B7         OR      A               
517C: 77         LD      (HL),A          
517D: 77         LD      (HL),A          
517E: FF         RST     0X38            
517F: FF         RST     0X38            
5180: BD         CP      L               
5181: BD         CP      L               
5182: B3         OR      E               
5183: B3         OR      E               
5184: CF         RST     0X08            
5185: CF         RST     0X08            
5186: DF         RST     0X18            
5187: DF         RST     0X18            
5188: DF         RST     0X18            
5189: DF         RST     0X18            
518A: BF         CP      A               
518B: BF         CP      A               
518C: BF         CP      A               
518D: BF         CP      A               
518E: FF         RST     0X38            
518F: FF         RST     0X38            
5190: 81         ADD     A,C             
5191: 81         ADD     A,C             
5192: FB         EI                      
5193: FB         EI                      
5194: F7         RST     0X30            
5195: F7         RST     0X30            
5196: EF         RST     0X28            
5197: EF         RST     0X28            
5198: DF         RST     0X18            
5199: DF         RST     0X18            
519A: BF         CP      A               
519B: BF         CP      A               
519C: 03         INC     BC              
519D: 03         INC     BC              
519E: FF         RST     0X38            
519F: FF         RST     0X38            
51A0: FF         RST     0X38            
51A1: FF         RST     0X38            
51A2: FF         RST     0X38            
51A3: FF         RST     0X38            
51A4: E7         RST     0X20            
51A5: E7         RST     0X20            
51A6: DB         ???                     
51A7: DB         ???                     
51A8: BB         CP      E               
51A9: BB         CP      E               
51AA: B7         OR      A               
51AB: B7         OR      A               
51AC: CB CB      SET     1,E             
51AE: FF         RST     0X38            
51AF: FF         RST     0X38            
51B0: EF         RST     0X28            
51B1: EF         RST     0X28            
51B2: EF         RST     0X28            
51B3: EF         RST     0X28            
51B4: DF         RST     0X18            
51B5: DF         RST     0X18            
51B6: C7         RST     0X00            
51B7: C7         RST     0X00            
51B8: DB         ???                     
51B9: DB         ???                     
51BA: BB         CP      E               
51BB: BB         CP      E               
51BC: 87         ADD     A,A             
51BD: 87         ADD     A,A             
51BE: FF         RST     0X38            
51BF: FF         RST     0X38            
51C0: FF         RST     0X38            
51C1: FF         RST     0X38            
51C2: FF         RST     0X38            
51C3: FF         RST     0X38            
51C4: E7         RST     0X20            
51C5: E7         RST     0X20            
51C6: DF         RST     0X18            
51C7: DF         RST     0X18            
51C8: BF         CP      A               
51C9: BF         CP      A               
51CA: BF         CP      A               
51CB: BF         CP      A               
51CC: C7         RST     0X00            
51CD: C7         RST     0X00            
51CE: FF         RST     0X38            
51CF: FF         RST     0X38            
51D0: FD         ???                     
51D1: FD         ???                     
51D2: FD         ???                     
51D3: FD         ???                     
51D4: FB         EI                      
51D5: FB         EI                      
51D6: C3 C3 B7   JP      $B7C3           
51D9: B7         OR      A               
51DA: B7         OR      A               
51DB: B7         OR      A               
51DC: C7         RST     0X00            
51DD: C7         RST     0X00            
51DE: FF         RST     0X38            
51DF: FF         RST     0X38            
51E0: FF         RST     0X38            
51E1: FF         RST     0X38            
51E2: FF         RST     0X38            
51E3: FF         RST     0X38            
51E4: E7         RST     0X20            
51E5: E7         RST     0X20            
51E6: DB         ???                     
51E7: DB         ???                     
51E8: 83         ADD     A,E             
51E9: 83         ADD     A,E             
51EA: BF         CP      A               
51EB: BF         CP      A               
51EC: C7         RST     0X00            
51ED: C7         RST     0X00            
51EE: FF         RST     0X38            
51EF: FF         RST     0X38            
51F0: F9         LD      SP,HL           
51F1: F9         LD      SP,HL           
51F2: F7         RST     0X30            
51F3: F7         RST     0X30            
51F4: 81         ADD     A,C             
51F5: 81         ADD     A,C             
51F6: EF         RST     0X28            
51F7: EF         RST     0X28            
51F8: EF         RST     0X28            
51F9: EF         RST     0X28            
51FA: DF         RST     0X18            
51FB: DF         RST     0X18            
51FC: DF         RST     0X18            
51FD: DF         RST     0X18            
51FE: FF         RST     0X38            
51FF: FF         RST     0X38            
5200: FF         RST     0X38            
5201: FF         RST     0X38            
5202: FF         RST     0X38            
5203: FF         RST     0X38            
5204: E7         RST     0X20            
5205: E7         RST     0X20            
5206: DB         ???                     
5207: DB         ???                     
5208: DB         ???                     
5209: DB         ???                     
520A: E3         ???                     
520B: E3         ???                     
520C: B7         OR      A               
520D: B7         OR      A               
520E: 8F         ADC     A,A             
520F: 8F         ADC     A,A             
5210: EF         RST     0X28            
5211: EF         RST     0X28            
5212: EF         RST     0X28            
5213: EF         RST     0X28            
5214: DF         RST     0X18            
5215: DF         RST     0X18            
5216: DF         RST     0X18            
5217: DF         RST     0X18            
5218: C7         RST     0X00            
5219: C7         RST     0X00            
521A: B7         OR      A               
521B: B7         OR      A               
521C: B7         OR      A               
521D: B7         OR      A               
521E: FF         RST     0X38            
521F: FF         RST     0X38            
5220: F3         DI                      
5221: F3         DI                      
5222: FF         RST     0X38            
5223: FF         RST     0X38            
5224: FF         RST     0X38            
5225: FF         RST     0X38            
5226: EF         RST     0X28            
5227: EF         RST     0X28            
5228: EF         RST     0X28            
5229: EF         RST     0X28            
522A: DF         RST     0X18            
522B: DF         RST     0X18            
522C: DF         RST     0X18            
522D: DF         RST     0X18            
522E: FF         RST     0X38            
522F: FF         RST     0X38            
5230: F3         DI                      
5231: F3         DI                      
5232: FF         RST     0X38            
5233: FF         RST     0X38            
5234: FF         RST     0X38            
5235: FF         RST     0X38            
5236: F7         RST     0X30            
5237: F7         RST     0X30            
5238: F7         RST     0X30            
5239: F7         RST     0X30            
523A: EF         RST     0X28            
523B: EF         RST     0X28            
523C: 6F         LD      L,A             
523D: 6F         LD      L,A             
523E: 9F         SBC     A               
523F: 9F         SBC     A               
5240: EF         RST     0X28            
5241: EF         RST     0X28            
5242: EF         RST     0X28            
5243: EF         RST     0X28            
5244: DB         ???                     
5245: DB         ???                     
5246: D7         RST     0X10            
5247: D7         RST     0X10            
5248: CF         RST     0X08            
5249: CF         RST     0X08            
524A: B7         OR      A               
524B: B7         OR      A               
524C: BB         CP      E               
524D: BB         CP      E               
524E: FF         RST     0X38            
524F: FF         RST     0X38            
5250: F7         RST     0X30            
5251: F7         RST     0X30            
5252: F7         RST     0X30            
5253: F7         RST     0X30            
5254: EF         RST     0X28            
5255: EF         RST     0X28            
5256: EF         RST     0X28            
5257: EF         RST     0X28            
5258: EF         RST     0X28            
5259: EF         RST     0X28            
525A: DF         RST     0X18            
525B: DF         RST     0X18            
525C: DF         RST     0X18            
525D: DF         RST     0X18            
525E: FF         RST     0X38            
525F: FF         RST     0X38            
5260: FF         RST     0X38            
5261: FF         RST     0X38            
5262: FF         RST     0X38            
5263: FF         RST     0X38            
5264: CB CB      SET     1,E             
5266: D5         PUSH    DE              
5267: D5         PUSH    DE              
5268: D5         PUSH    DE              
5269: D5         PUSH    DE              
526A: AB         XOR     E               
526B: AB         XOR     E               
526C: AB         XOR     E               
526D: AB         XOR     E               
526E: FF         RST     0X38            
526F: FF         RST     0X38            
5270: FF         RST     0X38            
5271: FF         RST     0X38            
5272: FF         RST     0X38            
5273: FF         RST     0X38            
5274: D7         RST     0X10            
5275: D7         RST     0X10            
5276: CB CB      SET     1,E             
5278: DB         ???                     
5279: DB         ???                     
527A: B7         OR      A               
527B: B7         OR      A               
527C: B7         OR      A               
527D: B7         OR      A               
527E: FF         RST     0X38            
527F: FF         RST     0X38            
5280: FF         RST     0X38            
5281: FF         RST     0X38            
5282: FF         RST     0X38            
5283: FF         RST     0X38            
5284: E7         RST     0X20            
5285: E7         RST     0X20            
5286: DB         ???                     
5287: DB         ???                     
5288: BB         CP      E               
5289: BB         CP      E               
528A: B7         OR      A               
528B: B7         OR      A               
528C: CF         RST     0X08            
528D: CF         RST     0X08            
528E: FF         RST     0X38            
528F: FF         RST     0X38            
5290: FF         RST     0X38            
5291: FF         RST     0X38            
5292: FF         RST     0X38            
5293: FF         RST     0X38            
5294: E7         RST     0X20            
5295: E7         RST     0X20            
5296: DB         ???                     
5297: DB         ???                     
5298: DB         ???                     
5299: DB         ???                     
529A: C7         RST     0X00            
529B: C7         RST     0X00            
529C: BF         CP      A               
529D: BF         CP      A               
529E: BF         CP      A               
529F: BF         CP      A               
52A0: FF         RST     0X38            
52A1: FF         RST     0X38            
52A2: FF         RST     0X38            
52A3: FF         RST     0X38            
52A4: E7         RST     0X20            
52A5: E7         RST     0X20            
52A6: DB         ???                     
52A7: DB         ???                     
52A8: BB         CP      E               
52A9: BB         CP      E               
52AA: C7         RST     0X00            
52AB: C7         RST     0X00            
52AC: F7         RST     0X30            
52AD: F7         RST     0X30            
52AE: EF         RST     0X28            
52AF: EF         RST     0X28            
52B0: FF         RST     0X38            
52B1: FF         RST     0X38            
52B2: FF         RST     0X38            
52B3: FF         RST     0X38            
52B4: EB         ???                     
52B5: EB         ???                     
52B6: E7         RST     0X20            
52B7: E7         RST     0X20            
52B8: EF         RST     0X28            
52B9: EF         RST     0X28            
52BA: DF         RST     0X18            
52BB: DF         RST     0X18            
52BC: DF         RST     0X18            
52BD: DF         RST     0X18            
52BE: FF         RST     0X38            
52BF: FF         RST     0X38            
52C0: FF         RST     0X38            
52C1: FF         RST     0X38            
52C2: FF         RST     0X38            
52C3: FF         RST     0X38            
52C4: E7         RST     0X20            
52C5: E7         RST     0X20            
52C6: DB         ???                     
52C7: DB         ???                     
52C8: EF         RST     0X28            
52C9: EF         RST     0X28            
52CA: B7         OR      A               
52CB: B7         OR      A               
52CC: CF         RST     0X08            
52CD: CF         RST     0X08            
52CE: FF         RST     0X38            
52CF: FF         RST     0X38            
52D0: FF         RST     0X38            
52D1: FF         RST     0X38            
52D2: F7         RST     0X30            
52D3: F7         RST     0X30            
52D4: C3 C3 EF   JP      $EFC3           
52D7: EF         RST     0X28            
52D8: EF         RST     0X28            
52D9: EF         RST     0X28            
52DA: DF         RST     0X18            
52DB: DF         RST     0X18            
52DC: DF         RST     0X18            
52DD: DF         RST     0X18            
52DE: FF         RST     0X38            
52DF: FF         RST     0X38            
52E0: FF         RST     0X38            
52E1: FF         RST     0X38            
52E2: FF         RST     0X38            
52E3: FF         RST     0X38            
52E4: DB         ???                     
52E5: DB         ???                     
52E6: DB         ???                     
52E7: DB         ???                     
52E8: B7         OR      A               
52E9: B7         OR      A               
52EA: B7         OR      A               
52EB: B7         OR      A               
52EC: CB CB      SET     1,E             
52EE: FF         RST     0X38            
52EF: FF         RST     0X38            
52F0: FF         RST     0X38            
52F1: FF         RST     0X38            
52F2: FF         RST     0X38            
52F3: FF         RST     0X38            
52F4: BB         CP      E               
52F5: BB         CP      E               
52F6: B7         OR      A               
52F7: B7         OR      A               
52F8: AF         XOR     A               
52F9: AF         XOR     A               
52FA: 9F         SBC     A               
52FB: 9F         SBC     A               
52FC: BF         CP      A               
52FD: BF         CP      A               
52FE: FF         RST     0X38            
52FF: FF         RST     0X38            
5300: FF         RST     0X38            
5301: FF         RST     0X38            
5302: FF         RST     0X38            
5303: FF         RST     0X38            
5304: D5         PUSH    DE              
5305: D5         PUSH    DE              
5306: D5         PUSH    DE              
5307: D5         PUSH    DE              
5308: AB         XOR     E               
5309: AB         XOR     E               
530A: AB         XOR     E               
530B: AB         XOR     E               
530C: D7         RST     0X10            
530D: D7         RST     0X10            
530E: FF         RST     0X38            
530F: FF         RST     0X38            
5310: FF         RST     0X38            
5311: FF         RST     0X38            
5312: FF         RST     0X38            
5313: FF         RST     0X38            
5314: DB         ???                     
5315: DB         ???                     
5316: E7         RST     0X20            
5317: E7         RST     0X20            
5318: EF         RST     0X28            
5319: EF         RST     0X28            
531A: D7         RST     0X10            
531B: D7         RST     0X10            
531C: B7         OR      A               
531D: B7         OR      A               
531E: FF         RST     0X38            
531F: FF         RST     0X38            
5320: FF         RST     0X38            
5321: FF         RST     0X38            
5322: FF         RST     0X38            
5323: FF         RST     0X38            
5324: DD         ???                     
5325: DD         ???                     
5326: EB         ???                     
5327: EB         ???                     
5328: E7         RST     0X20            
5329: E7         RST     0X20            
532A: EF         RST     0X28            
532B: EF         RST     0X28            
532C: DF         RST     0X18            
532D: DF         RST     0X18            
532E: BF         CP      A               
532F: BF         CP      A               
5330: 87         ADD     A,A             
5331: 87         ADD     A,A             
5332: CF         RST     0X08            
5333: CF         RST     0X08            
5334: CF         RST     0X08            
5335: CF         RST     0X08            
5336: CE CE      ADC     $CE             
5338: CF         RST     0X08            
5339: CF         RST     0X08            
533A: CD CD 81   CALL    $81CD           
533D: 81         ADD     A,C             
533E: FF         RST     0X38            
533F: FF         RST     0X38            
5340: EF         RST     0X28            
5341: EF         RST     0X28            
5342: C7         RST     0X00            
5343: C7         RST     0X00            
5344: 83         ADD     A,E             
5345: 83         ADD     A,E             
5346: 01 01 C7   LD      BC,$C701        
5349: C7         RST     0X00            
534A: C7         RST     0X00            
534B: C7         RST     0X00            
534C: C7         RST     0X00            
534D: C7         RST     0X00            
534E: FF         RST     0X38            
534F: FF         RST     0X38            
5350: C7         RST     0X00            
5351: C7         RST     0X00            
5352: C7         RST     0X00            
5353: C7         RST     0X00            
5354: C7         RST     0X00            
5355: C7         RST     0X00            
5356: 01 01 83   LD      BC,$8301        
5359: 83         ADD     A,E             
535A: C7         RST     0X00            
535B: C7         RST     0X00            
535C: EF         RST     0X28            
535D: EF         RST     0X28            
535E: FF         RST     0X38            
535F: FF         RST     0X38            
5360: F7         RST     0X30            
5361: F7         RST     0X30            
5362: E7         RST     0X20            
5363: E7         RST     0X20            
5364: C0         RET     NZ              
5365: C0         RET     NZ              
5366: 80         ADD     A,B             
5367: 80         ADD     A,B             
5368: C0         RET     NZ              
5369: C0         RET     NZ              
536A: E7         RST     0X20            
536B: E7         RST     0X20            
536C: F7         RST     0X30            
536D: F7         RST     0X30            
536E: FF         RST     0X38            
536F: FF         RST     0X38            
5370: F7         RST     0X30            
5371: F7         RST     0X30            
5372: F3         DI                      
5373: F3         DI                      
5374: 81         ADD     A,C             
5375: 81         ADD     A,C             
5376: 80         ADD     A,B             
5377: 80         ADD     A,B             
5378: 81         ADD     A,C             
5379: 81         ADD     A,C             
537A: F3         DI                      
537B: F3         DI                      
537C: F7         RST     0X30            
537D: F7         RST     0X30            
537E: FF         RST     0X38            
537F: FF         RST     0X38            
5380: 00         NOP                     
5381: 00         NOP                     
5382: 00         NOP                     
5383: 00         NOP                     
5384: 44         LD      B,H             
5385: 00         NOP                     
5386: 28 00      JR      Z,$5388         
5388: 10 00      STOP    $00             
538A: 28 00      JR      Z,$538C         
538C: 44         LD      B,H             
538D: 00         NOP                     
538E: 00         NOP                     
538F: 00         NOP                     
5390: FF         RST     0X38            
5391: FF         RST     0X38            
5392: FF         RST     0X38            
5393: FF         RST     0X38            
5394: FF         RST     0X38            
5395: FF         RST     0X38            
5396: FF         RST     0X38            
5397: FF         RST     0X38            
5398: FF         RST     0X38            
5399: FF         RST     0X38            
539A: CF         RST     0X08            
539B: CF         RST     0X08            
539C: CF         RST     0X08            
539D: CF         RST     0X08            
539E: FF         RST     0X38            
539F: FF         RST     0X38            
53A0: FF         RST     0X38            
53A1: FF         RST     0X38            
53A2: FF         RST     0X38            
53A3: FF         RST     0X38            
53A4: FF         RST     0X38            
53A5: FF         RST     0X38            
53A6: FF         RST     0X38            
53A7: FF         RST     0X38            
53A8: FF         RST     0X38            
53A9: FF         RST     0X38            
53AA: 9F         SBC     A               
53AB: 9F         SBC     A               
53AC: DF         RST     0X18            
53AD: DF         RST     0X18            
53AE: BF         CP      A               
53AF: BF         CP      A               
53B0: FF         RST     0X38            
53B1: FF         RST     0X38            
53B2: FF         RST     0X38            
53B3: FF         RST     0X38            
53B4: FF         RST     0X38            
53B5: FF         RST     0X38            
53B6: FF         RST     0X38            
53B7: FF         RST     0X38            
53B8: FF         RST     0X38            
53B9: FF         RST     0X38            
53BA: 3F         CCF                     
53BB: 3F         CCF                     
53BC: 3F         CCF                     
53BD: 3F         CCF                     
53BE: FF         RST     0X38            
53BF: FF         RST     0X38            
53C0: C3 C3 99   JP      $99C3           
53C3: 99         SBC     C               
53C4: F9         LD      SP,HL           
53C5: F9         LD      SP,HL           
53C6: E3         ???                     
53C7: E3         ???                     
53C8: CF         RST     0X08            
53C9: CF         RST     0X08            
53CA: FF         RST     0X38            
53CB: FF         RST     0X38            
53CC: 9F         SBC     A               
53CD: 9F         SBC     A               
53CE: FF         RST     0X38            
53CF: FF         RST     0X38            
53D0: E7         RST     0X20            
53D1: E7         RST     0X20            
53D2: E7         RST     0X20            
53D3: E7         RST     0X20            
53D4: E7         RST     0X20            
53D5: E7         RST     0X20            
53D6: EF         RST     0X28            
53D7: EF         RST     0X28            
53D8: EF         RST     0X28            
53D9: EF         RST     0X28            
53DA: FF         RST     0X38            
53DB: FF         RST     0X38            
53DC: CF         RST     0X08            
53DD: CF         RST     0X08            
53DE: FF         RST     0X38            
53DF: FF         RST     0X38            
53E0: FF         RST     0X38            
53E1: FF         RST     0X38            
53E2: FF         RST     0X38            
53E3: FF         RST     0X38            
53E4: C3 C3 F7   JP      $F7C3           
53E7: F7         RST     0X30            
53E8: EF         RST     0X28            
53E9: EF         RST     0X28            
53EA: DF         RST     0X18            
53EB: DF         RST     0X18            
53EC: 87         ADD     A,A             
53ED: 87         ADD     A,A             
53EE: FF         RST     0X38            
53EF: FF         RST     0X38            
53F0: FF         RST     0X38            
53F1: FF         RST     0X38            
53F2: FF         RST     0X38            
53F3: FF         RST     0X38            
53F4: FF         RST     0X38            
53F5: FF         RST     0X38            
53F6: FF         RST     0X38            
53F7: FF         RST     0X38            
53F8: 07         RLCA                    
53F9: 07         RLCA                    
53FA: FF         RST     0X38            
53FB: FF         RST     0X38            
53FC: FF         RST     0X38            
53FD: FF         RST     0X38            
53FE: FF         RST     0X38            
53FF: FF         RST     0X38            
5400: 9F         SBC     A               
5401: 9F         SBC     A               
5402: DF         RST     0X18            
5403: DF         RST     0X18            
5404: BF         CP      A               
5405: BF         CP      A               
5406: FF         RST     0X38            
5407: FF         RST     0X38            
5408: FF         RST     0X38            
5409: FF         RST     0X38            
540A: FF         RST     0X38            
540B: FF         RST     0X38            
540C: FF         RST     0X38            
540D: FF         RST     0X38            
540E: FF         RST     0X38            
540F: FF         RST     0X38            
5410: 93         SUB     E               
5411: 93         SUB     E               
5412: DB         ???                     
5413: DB         ???                     
5414: B7         OR      A               
5415: B7         OR      A               
5416: FF         RST     0X38            
5417: FF         RST     0X38            
5418: FF         RST     0X38            
5419: FF         RST     0X38            
541A: FF         RST     0X38            
541B: FF         RST     0X38            
541C: FF         RST     0X38            
541D: FF         RST     0X38            
541E: FF         RST     0X38            
541F: FF         RST     0X38            
5420: FF         RST     0X38            
5421: FF         RST     0X38            
5422: CF         RST     0X08            
5423: CF         RST     0X08            
5424: CF         RST     0X08            
5425: CF         RST     0X08            
5426: FF         RST     0X38            
5427: FF         RST     0X38            
5428: FF         RST     0X38            
5429: FF         RST     0X38            
542A: 9F         SBC     A               
542B: 9F         SBC     A               
542C: 9F         SBC     A               
542D: 9F         SBC     A               
542E: FF         RST     0X38            
542F: FF         RST     0X38            
5430: FF         RST     0X38            
5431: FF         RST     0X38            
5432: CF         RST     0X08            
5433: CF         RST     0X08            
5434: CF         RST     0X08            
5435: CF         RST     0X08            
5436: FF         RST     0X38            
5437: FF         RST     0X38            
5438: FF         RST     0X38            
5439: FF         RST     0X38            
543A: 9F         SBC     A               
543B: 9F         SBC     A               
543C: DF         RST     0X18            
543D: DF         RST     0X18            
543E: BF         CP      A               
543F: BF         CP      A               
5440: EF         RST     0X28            
5441: EF         RST     0X28            
5442: D7         RST     0X10            
5443: D7         RST     0X10            
5444: D7         RST     0X10            
5445: D7         RST     0X10            
5446: CF         RST     0X08            
5447: CF         RST     0X08            
5448: 99         SBC     C               
5449: 99         SBC     C               
544A: 67         LD      H,A             
544B: 67         LD      H,A             
544C: 73         LD      (HL),E          
544D: 73         LD      (HL),E          
544E: 8D         ADC     A,L             
544F: 8D         ADC     A,L             
5450: F3         DI                      
5451: F3         DI                      
5452: EF         RST     0X28            
5453: EF         RST     0X28            
5454: DF         RST     0X18            
5455: DF         RST     0X18            
5456: DF         RST     0X18            
5457: DF         RST     0X18            
5458: DF         RST     0X18            
5459: DF         RST     0X18            
545A: DF         RST     0X18            
545B: DF         RST     0X18            
545C: EF         RST     0X28            
545D: EF         RST     0X28            
545E: F3         DI                      
545F: F3         DI                      
5460: 9F         SBC     A               
5461: 9F         SBC     A               
5462: EF         RST     0X28            
5463: EF         RST     0X28            
5464: F7         RST     0X30            
5465: F7         RST     0X30            
5466: F7         RST     0X30            
5467: F7         RST     0X30            
5468: F7         RST     0X30            
5469: F7         RST     0X30            
546A: F7         RST     0X30            
546B: F7         RST     0X30            
546C: EF         RST     0X28            
546D: EF         RST     0X28            
546E: 9F         SBC     A               
546F: 9F         SBC     A               
5470: EF         RST     0X28            
5471: EF         RST     0X28            
5472: F7         RST     0X30            
5473: F7         RST     0X30            
5474: FF         RST     0X38            
5475: FF         RST     0X38            
5476: E7         RST     0X20            
5477: E7         RST     0X20            
5478: DB         ???                     
5479: DB         ???                     
547A: BB         CP      E               
547B: BB         CP      E               
547C: B7         OR      A               
547D: B7         OR      A               
547E: CB CB      SET     1,E             
5480: E7         RST     0X20            
5481: E7         RST     0X20            
5482: DB         ???                     
5483: DB         ???                     
5484: FF         RST     0X38            
5485: FF         RST     0X38            
5486: E7         RST     0X20            
5487: E7         RST     0X20            
5488: DB         ???                     
5489: DB         ???                     
548A: BB         CP      E               
548B: BB         CP      E               
548C: B7         OR      A               
548D: B7         OR      A               
548E: CB CB      SET     1,E             
5490: DB         ???                     
5491: DB         ???                     
5492: FF         RST     0X38            
5493: FF         RST     0X38            
5494: FF         RST     0X38            
5495: FF         RST     0X38            
5496: E7         RST     0X20            
5497: E7         RST     0X20            
5498: DB         ???                     
5499: DB         ???                     
549A: BB         CP      E               
549B: BB         CP      E               
549C: B7         OR      A               
549D: B7         OR      A               
549E: CB CB      SET     1,E             
54A0: EF         RST     0X28            
54A1: EF         RST     0X28            
54A2: F7         RST     0X30            
54A3: F7         RST     0X30            
54A4: FF         RST     0X38            
54A5: FF         RST     0X38            
54A6: E7         RST     0X20            
54A7: E7         RST     0X20            
54A8: DB         ???                     
54A9: DB         ???                     
54AA: 83         ADD     A,E             
54AB: 83         ADD     A,E             
54AC: BF         CP      A               
54AD: BF         CP      A               
54AE: C7         RST     0X00            
54AF: C7         RST     0X00            
54B0: FB         EI                      
54B1: FB         EI                      
54B2: F7         RST     0X30            
54B3: F7         RST     0X30            
54B4: FF         RST     0X38            
54B5: FF         RST     0X38            
54B6: E7         RST     0X20            
54B7: E7         RST     0X20            
54B8: DB         ???                     
54B9: DB         ???                     
54BA: 83         ADD     A,E             
54BB: 83         ADD     A,E             
54BC: BF         CP      A               
54BD: BF         CP      A               
54BE: C7         RST     0X00            
54BF: C7         RST     0X00            
54C0: E7         RST     0X20            
54C1: E7         RST     0X20            
54C2: DB         ???                     
54C3: DB         ???                     
54C4: FF         RST     0X38            
54C5: FF         RST     0X38            
54C6: E7         RST     0X20            
54C7: E7         RST     0X20            
54C8: DB         ???                     
54C9: DB         ???                     
54CA: 83         ADD     A,E             
54CB: 83         ADD     A,E             
54CC: BF         CP      A               
54CD: BF         CP      A               
54CE: C7         RST     0X00            
54CF: C7         RST     0X00            
54D0: EF         RST     0X28            
54D1: EF         RST     0X28            
54D2: F7         RST     0X30            
54D3: F7         RST     0X30            
54D4: FF         RST     0X38            
54D5: FF         RST     0X38            
54D6: DB         ???                     
54D7: DB         ???                     
54D8: DB         ???                     
54D9: DB         ???                     
54DA: B7         OR      A               
54DB: B7         OR      A               
54DC: B7         OR      A               
54DD: B7         OR      A               
54DE: CB CB      SET     1,E             
54E0: E7         RST     0X20            
54E1: E7         RST     0X20            
54E2: DB         ???                     
54E3: DB         ???                     
54E4: FF         RST     0X38            
54E5: FF         RST     0X38            
54E6: DB         ???                     
54E7: DB         ???                     
54E8: DB         ???                     
54E9: DB         ???                     
54EA: B7         OR      A               
54EB: B7         OR      A               
54EC: B7         OR      A               
54ED: B7         OR      A               
54EE: CB CB      SET     1,E             
54F0: DB         ???                     
54F1: DB         ???                     
54F2: FF         RST     0X38            
54F3: FF         RST     0X38            
54F4: FF         RST     0X38            
54F5: FF         RST     0X38            
54F6: DB         ???                     
54F7: DB         ???                     
54F8: DB         ???                     
54F9: DB         ???                     
54FA: B7         OR      A               
54FB: B7         OR      A               
54FC: B7         OR      A               
54FD: B7         OR      A               
54FE: CB CB      SET     1,E             
5500: E7         RST     0X20            
5501: E7         RST     0X20            
5502: DB         ???                     
5503: DB         ???                     
5504: FF         RST     0X38            
5505: FF         RST     0X38            
5506: E7         RST     0X20            
5507: E7         RST     0X20            
5508: DB         ???                     
5509: DB         ???                     
550A: BB         CP      E               
550B: BB         CP      E               
550C: B7         OR      A               
550D: B7         OR      A               
550E: CF         RST     0X08            
550F: CF         RST     0X08            
5510: DB         ???                     
5511: DB         ???                     
5512: FF         RST     0X38            
5513: FF         RST     0X38            
5514: FF         RST     0X38            
5515: FF         RST     0X38            
5516: E7         RST     0X20            
5517: E7         RST     0X20            
5518: DB         ???                     
5519: DB         ???                     
551A: BB         CP      E               
551B: BB         CP      E               
551C: B7         OR      A               
551D: B7         OR      A               
551E: CF         RST     0X08            
551F: CF         RST     0X08            
5520: FF         RST     0X38            
5521: FF         RST     0X38            
5522: E7         RST     0X20            
5523: E7         RST     0X20            
5524: DB         ???                     
5525: DB         ???                     
5526: BF         CP      A               
5527: BF         CP      A               
5528: BB         CP      E               
5529: BB         CP      E               
552A: C7         RST     0X00            
552B: C7         RST     0X00            
552C: FF         RST     0X38            
552D: FF         RST     0X38            
552E: 87         ADD     A,A             
552F: 87         ADD     A,A             
5530: E7         RST     0X20            
5531: E7         RST     0X20            
5532: DB         ???                     
5533: DB         ???                     
5534: FF         RST     0X38            
5535: FF         RST     0X38            
5536: EF         RST     0X28            
5537: EF         RST     0X28            
5538: EF         RST     0X28            
5539: EF         RST     0X28            
553A: DF         RST     0X18            
553B: DF         RST     0X18            
553C: DF         RST     0X18            
553D: DF         RST     0X18            
553E: FF         RST     0X38            
553F: FF         RST     0X38            
5540: FF         RST     0X38            
5541: FF         RST     0X38            
5542: E7         RST     0X20            
5543: E7         RST     0X20            
5544: DB         ???                     
5545: DB         ???                     
5546: D7         RST     0X10            
5547: D7         RST     0X10            
5548: BB         CP      E               
5549: BB         CP      E               
554A: BB         CP      E               
554B: BB         CP      E               
554C: 47         LD      B,A             
554D: 47         LD      B,A             
554E: 7F         LD      A,A             
554F: 7F         LD      A,A             
5550: F6 F6      OR      $F6             
5552: FF         RST     0X38            
5553: FF         RST     0X38            
5554: F9         LD      SP,HL           
5555: F9         LD      SP,HL           
5556: F5         PUSH    AF              
5557: F5         PUSH    AF              
5558: ED         ???                     
5559: ED         ???                     
555A: C1         POP     BC              
555B: C1         POP     BC              
555C: BD         CP      L               
555D: BD         CP      L               
555E: 7D         LD      A,L             
555F: 7D         LD      A,L             
5560: ED         ???                     
5561: ED         ???                     
5562: FF         RST     0X38            
5563: FF         RST     0X38            
5564: C3 C3 BD   JP      $BDC3           
5567: BD         CP      L               
5568: BD         CP      L               
5569: BD         CP      L               
556A: 7B         LD      A,E             
556B: 7B         LD      A,E             
556C: 7B         LD      A,E             
556D: 7B         LD      A,E             
556E: 87         ADD     A,A             
556F: 87         ADD     A,A             
5570: ED         ???                     
5571: ED         ???                     
5572: FF         RST     0X38            
5573: FF         RST     0X38            
5574: BB         CP      E               
5575: BB         CP      E               
5576: BB         CP      E               
5577: BB         CP      E               
5578: BB         CP      E               
5579: BB         CP      E               
557A: 77         LD      (HL),A          
557B: 77         LD      (HL),A          
557C: 77         LD      (HL),A          
557D: 77         LD      (HL),A          
557E: 8F         ADC     A,A             
557F: 8F         ADC     A,A             
5580: 00         NOP                     
5581: 00         NOP                     
5582: 00         NOP                     
5583: 00         NOP                     
5584: 44         LD      B,H             
5585: 00         NOP                     
5586: 28 00      JR      Z,$5588         
5588: 10 00      STOP    $00             
558A: 28 00      JR      Z,$558C         
558C: 44         LD      B,H             
558D: 00         NOP                     
558E: 00         NOP                     
558F: 00         NOP                     
5590: 00         NOP                     
5591: 00         NOP                     
5592: 00         NOP                     
5593: 00         NOP                     
5594: 44         LD      B,H             
5595: 00         NOP                     
5596: 28 00      JR      Z,$5598         
5598: 10 00      STOP    $00             
559A: 28 00      JR      Z,$559C         
559C: 44         LD      B,H             
559D: 00         NOP                     
559E: 00         NOP                     
559F: 00         NOP                     
55A0: 00         NOP                     
55A1: 00         NOP                     
55A2: 00         NOP                     
55A3: 00         NOP                     
55A4: 44         LD      B,H             
55A5: 00         NOP                     
55A6: 28 00      JR      Z,$55A8         
55A8: 10 00      STOP    $00             
55AA: 28 00      JR      Z,$55AC         
55AC: 44         LD      B,H             
55AD: 00         NOP                     
55AE: 00         NOP                     
55AF: 00         NOP                     
55B0: 00         NOP                     
55B1: 00         NOP                     
55B2: 00         NOP                     
55B3: 00         NOP                     
55B4: 44         LD      B,H             
55B5: 00         NOP                     
55B6: 28 00      JR      Z,$55B8         
55B8: 10 00      STOP    $00             
55BA: 28 00      JR      Z,$55BC         
55BC: 44         LD      B,H             
55BD: 00         NOP                     
55BE: 00         NOP                     
55BF: 00         NOP                     
55C0: 00         NOP                     
55C1: 00         NOP                     
55C2: 00         NOP                     
55C3: 00         NOP                     
55C4: 44         LD      B,H             
55C5: 00         NOP                     
55C6: 28 00      JR      Z,$55C8         
55C8: 10 00      STOP    $00             
55CA: 28 00      JR      Z,$55CC         
55CC: 44         LD      B,H             
55CD: 00         NOP                     
55CE: 00         NOP                     
55CF: 00         NOP                     
55D0: 00         NOP                     
55D1: 00         NOP                     
55D2: 00         NOP                     
55D3: 00         NOP                     
55D4: 44         LD      B,H             
55D5: 00         NOP                     
55D6: 28 00      JR      Z,$55D8         
55D8: 10 00      STOP    $00             
55DA: 28 00      JR      Z,$55DC         
55DC: 44         LD      B,H             
55DD: 00         NOP                     
55DE: 00         NOP                     
55DF: 00         NOP                     
55E0: 00         NOP                     
55E1: 00         NOP                     
55E2: 00         NOP                     
55E3: 00         NOP                     
55E4: 44         LD      B,H             
55E5: 00         NOP                     
55E6: 28 00      JR      Z,$55E8         
55E8: 10 00      STOP    $00             
55EA: 28 00      JR      Z,$55EC         
55EC: 44         LD      B,H             
55ED: 00         NOP                     
55EE: 00         NOP                     
55EF: 00         NOP                     
55F0: 00         NOP                     
55F1: 00         NOP                     
55F2: 00         NOP                     
55F3: 00         NOP                     
55F4: 44         LD      B,H             
55F5: 00         NOP                     
55F6: 28 00      JR      Z,$55F8         
55F8: 10 00      STOP    $00             
55FA: 28 00      JR      Z,$55FC         
55FC: 44         LD      B,H             
55FD: 00         NOP                     
55FE: 00         NOP                     
55FF: 00         NOP                     
5600: 00         NOP                     
5601: 00         NOP                     
5602: 00         NOP                     
5603: 00         NOP                     
5604: 44         LD      B,H             
5605: 00         NOP                     
5606: 28 00      JR      Z,$5608         
5608: 10 00      STOP    $00             
560A: 28 00      JR      Z,$560C         
560C: 44         LD      B,H             
560D: 00         NOP                     
560E: 00         NOP                     
560F: 00         NOP                     
5610: 00         NOP                     
5611: 00         NOP                     
5612: 00         NOP                     
5613: 00         NOP                     
5614: 44         LD      B,H             
5615: 00         NOP                     
5616: 28 00      JR      Z,$5618         
5618: 10 00      STOP    $00             
561A: 28 00      JR      Z,$561C         
561C: 44         LD      B,H             
561D: 00         NOP                     
561E: 00         NOP                     
561F: 00         NOP                     
5620: 00         NOP                     
5621: 00         NOP                     
5622: 00         NOP                     
5623: 00         NOP                     
5624: 44         LD      B,H             
5625: 00         NOP                     
5626: 28 00      JR      Z,$5628         
5628: 10 00      STOP    $00             
562A: 28 00      JR      Z,$562C         
562C: 44         LD      B,H             
562D: 00         NOP                     
562E: 00         NOP                     
562F: 00         NOP                     
5630: 00         NOP                     
5631: 00         NOP                     
5632: 00         NOP                     
5633: 00         NOP                     
5634: 44         LD      B,H             
5635: 00         NOP                     
5636: 28 00      JR      Z,$5638         
5638: 10 00      STOP    $00             
563A: 28 00      JR      Z,$563C         
563C: 44         LD      B,H             
563D: 00         NOP                     
563E: 00         NOP                     
563F: 00         NOP                     
5640: 00         NOP                     
5641: 00         NOP                     
5642: 00         NOP                     
5643: 00         NOP                     
5644: 44         LD      B,H             
5645: 00         NOP                     
5646: 28 00      JR      Z,$5648         
5648: 10 00      STOP    $00             
564A: 28 00      JR      Z,$564C         
564C: 44         LD      B,H             
564D: 00         NOP                     
564E: 00         NOP                     
564F: 00         NOP                     
5650: 00         NOP                     
5651: 00         NOP                     
5652: 00         NOP                     
5653: 00         NOP                     
5654: 44         LD      B,H             
5655: 00         NOP                     
5656: 28 00      JR      Z,$5658         
5658: 10 00      STOP    $00             
565A: 28 00      JR      Z,$565C         
565C: 44         LD      B,H             
565D: 00         NOP                     
565E: 00         NOP                     
565F: 00         NOP                     
5660: 00         NOP                     
5661: 00         NOP                     
5662: 00         NOP                     
5663: 00         NOP                     
5664: 44         LD      B,H             
5665: 00         NOP                     
5666: 28 00      JR      Z,$5668         
5668: 10 00      STOP    $00             
566A: 28 00      JR      Z,$566C         
566C: 44         LD      B,H             
566D: 00         NOP                     
566E: 00         NOP                     
566F: 00         NOP                     
5670: 00         NOP                     
5671: 00         NOP                     
5672: 00         NOP                     
5673: 00         NOP                     
5674: 44         LD      B,H             
5675: 00         NOP                     
5676: 28 00      JR      Z,$5678         
5678: 10 00      STOP    $00             
567A: 28 00      JR      Z,$567C         
567C: 44         LD      B,H             
567D: 00         NOP                     
567E: 00         NOP                     
567F: 00         NOP                     
5680: 00         NOP                     
5681: 00         NOP                     
5682: 00         NOP                     
5683: 00         NOP                     
5684: 44         LD      B,H             
5685: 00         NOP                     
5686: 28 00      JR      Z,$5688         
5688: 10 00      STOP    $00             
568A: 28 00      JR      Z,$568C         
568C: 44         LD      B,H             
568D: 00         NOP                     
568E: 00         NOP                     
568F: 00         NOP                     
5690: 00         NOP                     
5691: 00         NOP                     
5692: 00         NOP                     
5693: 00         NOP                     
5694: 44         LD      B,H             
5695: 00         NOP                     
5696: 28 00      JR      Z,$5698         
5698: 10 00      STOP    $00             
569A: 28 00      JR      Z,$569C         
569C: 44         LD      B,H             
569D: 00         NOP                     
569E: 00         NOP                     
569F: 00         NOP                     
56A0: 00         NOP                     
56A1: 00         NOP                     
56A2: 00         NOP                     
56A3: 00         NOP                     
56A4: 44         LD      B,H             
56A5: 00         NOP                     
56A6: 28 00      JR      Z,$56A8         
56A8: 10 00      STOP    $00             
56AA: 28 00      JR      Z,$56AC         
56AC: 44         LD      B,H             
56AD: 00         NOP                     
56AE: 00         NOP                     
56AF: 00         NOP                     
56B0: 00         NOP                     
56B1: 00         NOP                     
56B2: 00         NOP                     
56B3: 00         NOP                     
56B4: 44         LD      B,H             
56B5: 00         NOP                     
56B6: 28 00      JR      Z,$56B8         
56B8: 10 00      STOP    $00             
56BA: 28 00      JR      Z,$56BC         
56BC: 44         LD      B,H             
56BD: 00         NOP                     
56BE: 00         NOP                     
56BF: 00         NOP                     
56C0: 00         NOP                     
56C1: 00         NOP                     
56C2: 00         NOP                     
56C3: 00         NOP                     
56C4: 44         LD      B,H             
56C5: 00         NOP                     
56C6: 28 00      JR      Z,$56C8         
56C8: 10 00      STOP    $00             
56CA: 28 00      JR      Z,$56CC         
56CC: 44         LD      B,H             
56CD: 00         NOP                     
56CE: 00         NOP                     
56CF: 00         NOP                     
56D0: 00         NOP                     
56D1: 00         NOP                     
56D2: 00         NOP                     
56D3: 00         NOP                     
56D4: 44         LD      B,H             
56D5: 00         NOP                     
56D6: 28 00      JR      Z,$56D8         
56D8: 10 00      STOP    $00             
56DA: 28 00      JR      Z,$56DC         
56DC: 44         LD      B,H             
56DD: 00         NOP                     
56DE: 00         NOP                     
56DF: 00         NOP                     
56E0: 00         NOP                     
56E1: 00         NOP                     
56E2: 00         NOP                     
56E3: 00         NOP                     
56E4: 44         LD      B,H             
56E5: 00         NOP                     
56E6: 28 00      JR      Z,$56E8         
56E8: 10 00      STOP    $00             
56EA: 28 00      JR      Z,$56EC         
56EC: 44         LD      B,H             
56ED: 00         NOP                     
56EE: 00         NOP                     
56EF: 00         NOP                     
56F0: 00         NOP                     
56F1: 00         NOP                     
56F2: 00         NOP                     
56F3: 00         NOP                     
56F4: 44         LD      B,H             
56F5: 00         NOP                     
56F6: 28 00      JR      Z,$56F8         
56F8: 10 00      STOP    $00             
56FA: 28 00      JR      Z,$56FC         
56FC: 44         LD      B,H             
56FD: 00         NOP                     
56FE: 00         NOP                     
56FF: 00         NOP                     
5700: C3 C3 99   JP      $99C3           
5703: 99         SBC     C               
5704: 99         SBC     C               
5705: 99         SBC     C               
5706: 99         SBC     C               
5707: 99         SBC     C               
5708: 99         SBC     C               
5709: 99         SBC     C               
570A: 99         SBC     C               
570B: 99         SBC     C               
570C: C3 C3 FF   JP      $FFC3           
570F: FF         RST     0X38            
5710: E7         RST     0X20            
5711: E7         RST     0X20            
5712: C7         RST     0X00            
5713: C7         RST     0X00            
5714: E7         RST     0X20            
5715: E7         RST     0X20            
5716: E7         RST     0X20            
5717: E7         RST     0X20            
5718: E7         RST     0X20            
5719: E7         RST     0X20            
571A: E7         RST     0X20            
571B: E7         RST     0X20            
571C: E7         RST     0X20            
571D: E7         RST     0X20            
571E: FF         RST     0X38            
571F: FF         RST     0X38            
5720: C3 C3 99   JP      $99C3           
5723: 99         SBC     C               
5724: F9         LD      SP,HL           
5725: F9         LD      SP,HL           
5726: E3         ???                     
5727: E3         ???                     
5728: CF         RST     0X08            
5729: CF         RST     0X08            
572A: 9F         SBC     A               
572B: 9F         SBC     A               
572C: 81         ADD     A,C             
572D: 81         ADD     A,C             
572E: FF         RST     0X38            
572F: FF         RST     0X38            
5730: C3 C3 99   JP      $99C3           
5733: 99         SBC     C               
5734: F9         LD      SP,HL           
5735: F9         LD      SP,HL           
5736: E3         ???                     
5737: E3         ???                     
5738: F9         LD      SP,HL           
5739: F9         LD      SP,HL           
573A: 99         SBC     C               
573B: 99         SBC     C               
573C: C3 C3 FF   JP      $FFC3           
573F: FF         RST     0X38            
5740: F3         DI                      
5741: F3         DI                      
5742: E3         ???                     
5743: E3         ???                     
5744: C3 C3 93   JP      $93C3           
5747: 93         SUB     E               
5748: 93         SUB     E               
5749: 93         SUB     E               
574A: 81         ADD     A,C             
574B: 81         ADD     A,C             
574C: F3         DI                      
574D: F3         DI                      
574E: FF         RST     0X38            
574F: FF         RST     0X38            
5750: 81         ADD     A,C             
5751: 81         ADD     A,C             
5752: 9F         SBC     A               
5753: 9F         SBC     A               
5754: 9F         SBC     A               
5755: 9F         SBC     A               
5756: 83         ADD     A,E             
5757: 83         ADD     A,E             
5758: F9         LD      SP,HL           
5759: F9         LD      SP,HL           
575A: F9         LD      SP,HL           
575B: F9         LD      SP,HL           
575C: 83         ADD     A,E             
575D: 83         ADD     A,E             
575E: FF         RST     0X38            
575F: FF         RST     0X38            
5760: C3 C3 99   JP      $99C3           
5763: 99         SBC     C               
5764: 9F         SBC     A               
5765: 9F         SBC     A               
5766: 83         ADD     A,E             
5767: 83         ADD     A,E             
5768: 99         SBC     C               
5769: 99         SBC     C               
576A: 99         SBC     C               
576B: 99         SBC     C               
576C: C3 C3 FF   JP      $FFC3           
576F: FF         RST     0X38            
5770: 81         ADD     A,C             
5771: 81         ADD     A,C             
5772: F9         LD      SP,HL           
5773: F9         LD      SP,HL           
5774: F3         DI                      
5775: F3         DI                      
5776: E7         RST     0X20            
5777: E7         RST     0X20            
5778: E7         RST     0X20            
5779: E7         RST     0X20            
577A: E7         RST     0X20            
577B: E7         RST     0X20            
577C: E7         RST     0X20            
577D: E7         RST     0X20            
577E: FF         RST     0X38            
577F: FF         RST     0X38            
5780: C3 C3 99   JP      $99C3           
5783: 99         SBC     C               
5784: 99         SBC     C               
5785: 99         SBC     C               
5786: C3 C3 99   JP      $99C3           
5789: 99         SBC     C               
578A: 99         SBC     C               
578B: 99         SBC     C               
578C: C3 C3 FF   JP      $FFC3           
578F: FF         RST     0X38            
5790: C3 C3 99   JP      $99C3           
5793: 99         SBC     C               
5794: 99         SBC     C               
5795: 99         SBC     C               
5796: C1         POP     BC              
5797: C1         POP     BC              
5798: F9         LD      SP,HL           
5799: F9         LD      SP,HL           
579A: 99         SBC     C               
579B: 99         SBC     C               
579C: C3 C3 FF   JP      $FFC3           
579F: FF         RST     0X38            
57A0: EB         ???                     
57A1: EB         ???                     
57A2: EB         ???                     
57A3: EB         ???                     
57A4: FF         RST     0X38            
57A5: FF         RST     0X38            
57A6: FF         RST     0X38            
57A7: FF         RST     0X38            
57A8: FF         RST     0X38            
57A9: FF         RST     0X38            
57AA: FF         RST     0X38            
57AB: FF         RST     0X38            
57AC: FF         RST     0X38            
57AD: FF         RST     0X38            
57AE: FF         RST     0X38            
57AF: FF         RST     0X38            
57B0: 00         NOP                     
57B1: 00         NOP                     
57B2: 00         NOP                     
57B3: 00         NOP                     
57B4: 44         LD      B,H             
57B5: 00         NOP                     
57B6: 28 00      JR      Z,$57B8         
57B8: 10 00      STOP    $00             
57BA: 28 00      JR      Z,$57BC         
57BC: 44         LD      B,H             
57BD: 00         NOP                     
57BE: 00         NOP                     
57BF: 00         NOP                     
57C0: FF         RST     0X38            
57C1: 00         NOP                     
57C2: FF         RST     0X38            
57C3: 00         NOP                     
57C4: FF         RST     0X38            
57C5: 00         NOP                     
57C6: FF         RST     0X38            
57C7: 00         NOP                     
57C8: FF         RST     0X38            
57C9: 00         NOP                     
57CA: FF         RST     0X38            
57CB: 00         NOP                     
57CC: FF         RST     0X38            
57CD: 00         NOP                     
57CE: FF         RST     0X38            
57CF: 00         NOP                     
57D0: 00         NOP                     
57D1: FF         RST     0X38            
57D2: 00         NOP                     
57D3: FF         RST     0X38            
57D4: 00         NOP                     
57D5: FF         RST     0X38            
57D6: 00         NOP                     
57D7: FF         RST     0X38            
57D8: 00         NOP                     
57D9: FF         RST     0X38            
57DA: 00         NOP                     
57DB: FF         RST     0X38            
57DC: 00         NOP                     
57DD: FF         RST     0X38            
57DE: 00         NOP                     
57DF: FF         RST     0X38            
57E0: FF         RST     0X38            
57E1: FF         RST     0X38            
57E2: FF         RST     0X38            
57E3: FF         RST     0X38            
57E4: FF         RST     0X38            
57E5: FF         RST     0X38            
57E6: FF         RST     0X38            
57E7: FF         RST     0X38            
57E8: FF         RST     0X38            
57E9: FF         RST     0X38            
57EA: FF         RST     0X38            
57EB: FF         RST     0X38            
57EC: FF         RST     0X38            
57ED: FF         RST     0X38            
57EE: FF         RST     0X38            
57EF: FF         RST     0X38            
57F0: 00         NOP                     
57F1: 00         NOP                     
57F2: 00         NOP                     
57F3: 00         NOP                     
57F4: 00         NOP                     
57F5: 00         NOP                     
57F6: 00         NOP                     
57F7: 00         NOP                     
57F8: 00         NOP                     
57F9: 00         NOP                     
57FA: 00         NOP                     
57FB: 00         NOP                     
57FC: 00         NOP                     
57FD: 00         NOP                     
57FE: 00         NOP                     
57FF: 00         NOP                     
5800: C3 C3 99   JP      $99C3           
5803: 99         SBC     C               
5804: 99         SBC     C               
5805: 99         SBC     C               
5806: 99         SBC     C               
5807: 99         SBC     C               
5808: 81         ADD     A,C             
5809: 81         ADD     A,C             
580A: 99         SBC     C               
580B: 99         SBC     C               
580C: 99         SBC     C               
580D: 99         SBC     C               
580E: FF         RST     0X38            
580F: FF         RST     0X38            
5810: 03         INC     BC              
5811: 03         INC     BC              
5812: 99         SBC     C               
5813: 99         SBC     C               
5814: 99         SBC     C               
5815: 99         SBC     C               
5816: 83         ADD     A,E             
5817: 83         ADD     A,E             
5818: 99         SBC     C               
5819: 99         SBC     C               
581A: 99         SBC     C               
581B: 99         SBC     C               
581C: 03         INC     BC              
581D: 03         INC     BC              
581E: FF         RST     0X38            
581F: FF         RST     0X38            
5820: FF         RST     0X38            
5821: FF         RST     0X38            
5822: 81         ADD     A,C             
5823: 81         ADD     A,C             
5824: 9F         SBC     A               
5825: 9F         SBC     A               
5826: 9F         SBC     A               
5827: 9F         SBC     A               
5828: 9F         SBC     A               
5829: 9F         SBC     A               
582A: 9F         SBC     A               
582B: 9F         SBC     A               
582C: 81         ADD     A,C             
582D: 81         ADD     A,C             
582E: FF         RST     0X38            
582F: FF         RST     0X38            
5830: FF         RST     0X38            
5831: FF         RST     0X38            
5832: 83         ADD     A,E             
5833: 83         ADD     A,E             
5834: 99         SBC     C               
5835: 99         SBC     C               
5836: 99         SBC     C               
5837: 99         SBC     C               
5838: 99         SBC     C               
5839: 99         SBC     C               
583A: 99         SBC     C               
583B: 99         SBC     C               
583C: 83         ADD     A,E             
583D: 83         ADD     A,E             
583E: FF         RST     0X38            
583F: FF         RST     0X38            
5840: FF         RST     0X38            
5841: FF         RST     0X38            
5842: 81         ADD     A,C             
5843: 81         ADD     A,C             
5844: 9F         SBC     A               
5845: 9F         SBC     A               
5846: 83         ADD     A,E             
5847: 83         ADD     A,E             
5848: 9F         SBC     A               
5849: 9F         SBC     A               
584A: 9F         SBC     A               
584B: 9F         SBC     A               
584C: 81         ADD     A,C             
584D: 81         ADD     A,C             
584E: FF         RST     0X38            
584F: FF         RST     0X38            
5850: FF         RST     0X38            
5851: FF         RST     0X38            
5852: 81         ADD     A,C             
5853: 81         ADD     A,C             
5854: 9F         SBC     A               
5855: 9F         SBC     A               
5856: 83         ADD     A,E             
5857: 83         ADD     A,E             
5858: 9F         SBC     A               
5859: 9F         SBC     A               
585A: 9F         SBC     A               
585B: 9F         SBC     A               
585C: 9F         SBC     A               
585D: 9F         SBC     A               
585E: FF         RST     0X38            
585F: FF         RST     0X38            
5860: C7         RST     0X00            
5861: C7         RST     0X00            
5862: C7         RST     0X00            
5863: C7         RST     0X00            
5864: 11 01 29   LD      DE,$2901        
5867: 11 11 01   LD      DE,$0111        
586A: 01 C7 C7   LD      BC,$C7C7        
586D: C7         RST     0X00            
586E: C7         RST     0X00            
586F: FF         RST     0X38            
5870: FF         RST     0X38            
5871: FF         RST     0X38            
5872: 00         NOP                     
5873: 00         NOP                     
5874: 00         NOP                     
5875: 81         ADD     A,C             
5876: 00         NOP                     
5877: 42         LD      B,D             
5878: 00         NOP                     
5879: 3C         INC     A               
587A: 00         NOP                     
587B: 18 00      JR      $587D           
587D: 00         NOP                     
587E: FF         RST     0X38            
587F: FF         RST     0X38            
5880: CF         RST     0X08            
5881: CF         RST     0X08            
5882: 6F         LD      L,A             
5883: 27         DAA                     
5884: FF         RST     0X38            
5885: 07         RLCA                    
5886: FF         RST     0X38            
5887: 27         DAA                     
5888: F3         DI                      
5889: CD C3 CD   CALL    $CDC3           
588C: E1         POP     HL              
588D: E1         POP     HL              
588E: DF         RST     0X18            
588F: C3 C3 C3   JP      $C3C3           
5892: FF         RST     0X38            
5893: C7         RST     0X00            
5894: 24         INC     H               
5895: 3C         INC     A               
5896: 4E         LD      C,(HL)          
5897: 28 5E      JR      Z,$58F7         
5899: 38 7C      JR      C,$5917         
589B: 64         LD      H,H             
589C: DB         ???                     
589D: C3 C3 C3   JP      $C3C3           
58A0: 9F         SBC     A               
58A1: 9F         SBC     A               
58A2: 93         SUB     E               
58A3: 93         SUB     E               
58A4: D1         POP     DE              
58A5: FD         ???                     
58A6: C0         RET     NZ              
58A7: C6 C3      ADD     $C3             
58A9: C3 C3 E3   JP      $E3C3           
58AC: 87         ADD     A,A             
58AD: 87         ADD     A,A             
58AE: 8F         ADC     A,A             
58AF: 8F         ADC     A,A             
58B0: FF         RST     0X38            
58B1: FF         RST     0X38            
58B2: BD         CP      L               
58B3: BD         CP      L               
58B4: DB         ???                     
58B5: DB         ???                     
58B6: E7         RST     0X20            
58B7: E7         RST     0X20            
58B8: E7         RST     0X20            
58B9: E7         RST     0X20            
58BA: DB         ???                     
58BB: DB         ???                     
58BC: BD         CP      L               
58BD: BD         CP      L               
58BE: FF         RST     0X38            
58BF: FF         RST     0X38            
58C0: C3 C3 81   JP      $81C3           
58C3: 81         ADD     A,C             
58C4: 6C         LD      L,H             
58C5: 6C         LD      L,H             
58C6: 44         LD      B,H             
58C7: 44         LD      B,H             
58C8: 81         ADD     A,C             
58C9: 00         NOP                     
58CA: 87         ADD     A,A             
58CB: B3         OR      E               
58CC: 87         ADD     A,A             
58CD: 87         ADD     A,A             
58CE: B7         OR      A               
58CF: B7         OR      A               
58D0: CF         RST     0X08            
58D1: 83         ADD     A,E             
58D2: FF         RST     0X38            
58D3: 01 FF 74   LD      BC,$74FF        
58D6: FB         EI                      
58D7: FA 53 52   LD      A,($5253)       
58DA: 53         LD      D,E             
58DB: 52         LD      D,D             
58DC: 87         ADD     A,A             
58DD: 87         ADD     A,A             
58DE: FF         RST     0X38            
58DF: FF         RST     0X38            
58E0: E7         RST     0X20            
58E1: 83         ADD     A,E             
58E2: FF         RST     0X38            
58E3: 21 FF 60   LD      HL,$60FF        
58E6: DF         RST     0X18            
58E7: DC AB AB   CALL    C,$ABAB         
58EA: AB         XOR     E               
58EB: AA         XOR     D               
58EC: C7         RST     0X00            
58ED: 44         LD      B,H             
58EE: FF         RST     0X38            
58EF: 3C         INC     A               
58F0: C7         RST     0X00            
58F1: 83         ADD     A,E             
58F2: FF         RST     0X38            
58F3: 11 FF 7C   LD      DE,$7CFF        
58F6: AB         XOR     E               
58F7: AB         XOR     E               
58F8: A8         XOR     B               
58F9: A8         XOR     B               
58FA: 4C         LD      C,H             
58FB: 44         LD      B,H             
58FC: 7D         LD      A,L             
58FD: 7D         LD      A,L             
58FE: 83         ADD     A,E             
58FF: 83         ADD     A,E             
5900: FF         RST     0X38            
5901: FF         RST     0X38            
5902: FC         ???                     
5903: FC         ???                     
5904: 18 18      JR      $591E           
5906: 0A         LD      A,(BC)          
5907: 24         INC     H               
5908: 40         LD      B,B             
5909: 28 1C      JR      Z,$5927         
590B: 1C         INC     E               
590C: 3F         CCF                     
590D: 3F         CCF                     
590E: FF         RST     0X38            
590F: FF         RST     0X38            
5910: C3 C3 BD   JP      $BDC3           
5913: 81         ADD     A,C             
5914: BD         CP      L               
5915: 81         ADD     A,C             
5916: 81         ADD     A,C             
5917: C3 81 FF   JP      $FF81           
591A: 99         SBC     C               
591B: E7         RST     0X20            
591C: C3 BD E7   JP      $E7BD           
591F: C3 FC FC   JP      $FCFC           
5922: BC         CP      H               
5923: BE         CP      (HL)            
5924: CA 85 01   JP      Z,$0185         
5927: 7A         LD      A,D             
5928: 81         ADD     A,C             
5929: 04         INC     B               
592A: 80         ADD     A,B             
592B: F9         LD      SP,HL           
592C: 03         INC     BC              
592D: 01 87 83   LD      BC,$8387        
5930: EC         ???                     
5931: E4         ???                     
5932: E9         JP      (HL)            
5933: E0 E3      LDFF00  ($E3),A         
5935: E1         POP     HL              
5936: E7         RST     0X20            
5937: E3         ???                     
5938: CF         RST     0X08            
5939: C7         RST     0X00            
593A: 9F         SBC     A               
593B: 8F         ADC     A,A             
593C: 3F         CCF                     
593D: 1F         RRA                     
593E: 7F         LD      A,A             
593F: 3F         CCF                     
5940: F8 F8      LDHL    SP,$F8          
5942: FD         ???                     
5943: FD         ???                     
5944: FF         RST     0X38            
5945: C1         POP     BC              
5946: 87         ADD     A,A             
5947: 81         ADD     A,C             
5948: 13         INC     DE              
5949: 11 45 45   LD      DE,$4545        
594C: 11 11 83   LD      DE,$8311        
594F: 83         ADD     A,E             
5950: FF         RST     0X38            
5951: 24         INC     H               
5952: FF         RST     0X38            
5953: 81         ADD     A,C             
5954: FF         RST     0X38            
5955: E7         RST     0X20            
5956: E7         RST     0X20            
5957: DB         ???                     
5958: C3 81 FF   JP      $FF81           
595B: 81         ADD     A,C             
595C: C3 81 FF   JP      $FF81           
595F: C3 FE FE   JP      $FEFE           
5962: FE FE      CP      $FE             
5964: FD         ???                     
5965: FD         ???                     
5966: FD         ???                     
5967: FD         ???                     
5968: F3         DI                      
5969: F3         DI                      
596A: 1B         DEC     DE              
596B: 0B         DEC     BC              
596C: 0F         RRCA                    
596D: 07         RLCA                    
596E: FF         RST     0X38            
596F: 8F         ADC     A,A             
5970: F9         LD      SP,HL           
5971: F9         LD      SP,HL           
5972: FB         EI                      
5973: FB         EI                      
5974: FB         EI                      
5975: 7B         LD      A,E             
5976: 7B         LD      A,E             
5977: 7B         LD      A,E             
5978: 3B         DEC     SP              
5979: 3B         DEC     SP              
597A: 7B         LD      A,E             
597B: 7B         LD      A,E             
597C: B7         OR      A               
597D: 33         INC     SP              
597E: CF         RST     0X08            
597F: 87         ADD     A,A             
5980: F5         PUSH    AF              
5981: E1         POP     HL              
5982: DF         RST     0X18            
5983: DE FE      SBC     $FE             
5985: BE         CP      (HL)            
5986: BF         CP      A               
5987: BE         CP      (HL)            
5988: FE FE      CP      $FE             
598A: 5D         LD      E,L             
598B: BD         CP      L               
598C: B7         OR      A               
598D: 13         INC     DE              
598E: 5F         LD      E,A             
598F: BF         CP      A               
5990: E3         ???                     
5991: E3         ???                     
5992: E7         RST     0X20            
5993: D1         POP     DE              
5994: C0         RET     NZ              
5995: B8         CP      B               
5996: C0         RET     NZ              
5997: B8         CP      B               
5998: E7         RST     0X20            
5999: D8         RET     C               
599A: F0 E8      LD      A,($E8)         
599C: F8 F0      LDHL    SP,$F0          
599E: FD         ???                     
599F: F9         LD      SP,HL           
59A0: E1         POP     HL              
59A1: E1         POP     HL              
59A2: D2 CC C0   JP      NC,$C0CC        
59A5: D2 C0 D2   JP      NC,$D2C0        
59A8: D2 CC 81   JP      NC,$81CC        
59AB: 81         ADD     A,C             
59AC: 3F         CCF                     
59AD: 1F         RRA                     
59AE: 7F         LD      A,A             
59AF: 3F         CCF                     
59B0: 00         NOP                     
59B1: 00         NOP                     
59B2: 00         NOP                     
59B3: 00         NOP                     
59B4: 44         LD      B,H             
59B5: 00         NOP                     
59B6: 28 00      JR      Z,$59B8         
59B8: 10 00      STOP    $00             
59BA: 28 00      JR      Z,$59BC         
59BC: 44         LD      B,H             
59BD: 00         NOP                     
59BE: 00         NOP                     
59BF: 00         NOP                     
59C0: 00         NOP                     
59C1: 00         NOP                     
59C2: 00         NOP                     
59C3: 00         NOP                     
59C4: 44         LD      B,H             
59C5: 00         NOP                     
59C6: 28 00      JR      Z,$59C8         
59C8: 10 00      STOP    $00             
59CA: 28 00      JR      Z,$59CC         
59CC: 44         LD      B,H             
59CD: 00         NOP                     
59CE: 00         NOP                     
59CF: 00         NOP                     
59D0: 00         NOP                     
59D1: 00         NOP                     
59D2: 00         NOP                     
59D3: 00         NOP                     
59D4: 44         LD      B,H             
59D5: 00         NOP                     
59D6: 28 00      JR      Z,$59D8         
59D8: 10 00      STOP    $00             
59DA: 28 00      JR      Z,$59DC         
59DC: 44         LD      B,H             
59DD: 00         NOP                     
59DE: 00         NOP                     
59DF: 00         NOP                     
59E0: 00         NOP                     
59E1: 00         NOP                     
59E2: 00         NOP                     
59E3: 00         NOP                     
59E4: 44         LD      B,H             
59E5: 00         NOP                     
59E6: 28 00      JR      Z,$59E8         
59E8: 10 00      STOP    $00             
59EA: 28 00      JR      Z,$59EC         
59EC: 44         LD      B,H             
59ED: 00         NOP                     
59EE: 00         NOP                     
59EF: 00         NOP                     
59F0: 00         NOP                     
59F1: 00         NOP                     
59F2: 00         NOP                     
59F3: 00         NOP                     
59F4: 44         LD      B,H             
59F5: 00         NOP                     
59F6: 28 00      JR      Z,$59F8         
59F8: 10 00      STOP    $00             
59FA: 28 00      JR      Z,$59FC         
59FC: 44         LD      B,H             
59FD: 00         NOP                     
59FE: 00         NOP                     
59FF: 00         NOP                     
5A00: 00         NOP                     
5A01: 00         NOP                     
5A02: 00         NOP                     
5A03: 00         NOP                     
5A04: 44         LD      B,H             
5A05: 00         NOP                     
5A06: 28 00      JR      Z,$5A08         
5A08: 10 00      STOP    $00             
5A0A: 28 00      JR      Z,$5A0C         
5A0C: 44         LD      B,H             
5A0D: 00         NOP                     
5A0E: 00         NOP                     
5A0F: 00         NOP                     
5A10: 00         NOP                     
5A11: 00         NOP                     
5A12: 00         NOP                     
5A13: 00         NOP                     
5A14: 44         LD      B,H             
5A15: 00         NOP                     
5A16: 28 00      JR      Z,$5A18         
5A18: 10 00      STOP    $00             
5A1A: 28 00      JR      Z,$5A1C         
5A1C: 44         LD      B,H             
5A1D: 00         NOP                     
5A1E: 00         NOP                     
5A1F: 00         NOP                     
5A20: 00         NOP                     
5A21: 00         NOP                     
5A22: 00         NOP                     
5A23: 00         NOP                     
5A24: 44         LD      B,H             
5A25: 00         NOP                     
5A26: 28 00      JR      Z,$5A28         
5A28: 10 00      STOP    $00             
5A2A: 28 00      JR      Z,$5A2C         
5A2C: 44         LD      B,H             
5A2D: 00         NOP                     
5A2E: 00         NOP                     
5A2F: 00         NOP                     
5A30: 00         NOP                     
5A31: 00         NOP                     
5A32: 00         NOP                     
5A33: 00         NOP                     
5A34: 44         LD      B,H             
5A35: 00         NOP                     
5A36: 28 00      JR      Z,$5A38         
5A38: 10 00      STOP    $00             
5A3A: 28 00      JR      Z,$5A3C         
5A3C: 44         LD      B,H             
5A3D: 00         NOP                     
5A3E: 00         NOP                     
5A3F: 00         NOP                     
5A40: 00         NOP                     
5A41: 00         NOP                     
5A42: 00         NOP                     
5A43: 00         NOP                     
5A44: 44         LD      B,H             
5A45: 00         NOP                     
5A46: 28 00      JR      Z,$5A48         
5A48: 10 00      STOP    $00             
5A4A: 28 00      JR      Z,$5A4C         
5A4C: 44         LD      B,H             
5A4D: 00         NOP                     
5A4E: 00         NOP                     
5A4F: 00         NOP                     
5A50: 00         NOP                     
5A51: 00         NOP                     
5A52: 00         NOP                     
5A53: 00         NOP                     
5A54: 44         LD      B,H             
5A55: 00         NOP                     
5A56: 28 00      JR      Z,$5A58         
5A58: 10 00      STOP    $00             
5A5A: 28 00      JR      Z,$5A5C         
5A5C: 44         LD      B,H             
5A5D: 00         NOP                     
5A5E: 00         NOP                     
5A5F: 00         NOP                     
5A60: 00         NOP                     
5A61: 00         NOP                     
5A62: 00         NOP                     
5A63: 00         NOP                     
5A64: 44         LD      B,H             
5A65: 00         NOP                     
5A66: 28 00      JR      Z,$5A68         
5A68: 10 00      STOP    $00             
5A6A: 28 00      JR      Z,$5A6C         
5A6C: 44         LD      B,H             
5A6D: 00         NOP                     
5A6E: 00         NOP                     
5A6F: 00         NOP                     
5A70: 00         NOP                     
5A71: 00         NOP                     
5A72: 00         NOP                     
5A73: 00         NOP                     
5A74: 44         LD      B,H             
5A75: 00         NOP                     
5A76: 28 00      JR      Z,$5A78         
5A78: 10 00      STOP    $00             
5A7A: 28 00      JR      Z,$5A7C         
5A7C: 44         LD      B,H             
5A7D: 00         NOP                     
5A7E: 00         NOP                     
5A7F: 00         NOP                     
5A80: 00         NOP                     
5A81: 00         NOP                     
5A82: 00         NOP                     
5A83: 00         NOP                     
5A84: 44         LD      B,H             
5A85: 00         NOP                     
5A86: 28 00      JR      Z,$5A88         
5A88: 10 00      STOP    $00             
5A8A: 28 00      JR      Z,$5A8C         
5A8C: 44         LD      B,H             
5A8D: 00         NOP                     
5A8E: 00         NOP                     
5A8F: 00         NOP                     
5A90: 00         NOP                     
5A91: 00         NOP                     
5A92: 00         NOP                     
5A93: 00         NOP                     
5A94: 44         LD      B,H             
5A95: 00         NOP                     
5A96: 28 00      JR      Z,$5A98         
5A98: 10 00      STOP    $00             
5A9A: 28 00      JR      Z,$5A9C         
5A9C: 44         LD      B,H             
5A9D: 00         NOP                     
5A9E: 00         NOP                     
5A9F: 00         NOP                     
5AA0: 00         NOP                     
5AA1: 00         NOP                     
5AA2: 00         NOP                     
5AA3: 00         NOP                     
5AA4: 44         LD      B,H             
5AA5: 00         NOP                     
5AA6: 28 00      JR      Z,$5AA8         
5AA8: 10 00      STOP    $00             
5AAA: 28 00      JR      Z,$5AAC         
5AAC: 44         LD      B,H             
5AAD: 00         NOP                     
5AAE: 00         NOP                     
5AAF: 00         NOP                     
5AB0: 00         NOP                     
5AB1: 00         NOP                     
5AB2: 00         NOP                     
5AB3: 00         NOP                     
5AB4: 44         LD      B,H             
5AB5: 00         NOP                     
5AB6: 28 00      JR      Z,$5AB8         
5AB8: 10 00      STOP    $00             
5ABA: 28 00      JR      Z,$5ABC         
5ABC: 44         LD      B,H             
5ABD: 00         NOP                     
5ABE: 00         NOP                     
5ABF: 00         NOP                     
5AC0: 00         NOP                     
5AC1: 00         NOP                     
5AC2: 00         NOP                     
5AC3: 00         NOP                     
5AC4: 44         LD      B,H             
5AC5: 00         NOP                     
5AC6: 28 00      JR      Z,$5AC8         
5AC8: 10 00      STOP    $00             
5ACA: 28 00      JR      Z,$5ACC         
5ACC: 44         LD      B,H             
5ACD: 00         NOP                     
5ACE: 00         NOP                     
5ACF: 00         NOP                     
5AD0: 00         NOP                     
5AD1: 00         NOP                     
5AD2: 00         NOP                     
5AD3: 00         NOP                     
5AD4: 44         LD      B,H             
5AD5: 00         NOP                     
5AD6: 28 00      JR      Z,$5AD8         
5AD8: 10 00      STOP    $00             
5ADA: 28 00      JR      Z,$5ADC         
5ADC: 44         LD      B,H             
5ADD: 00         NOP                     
5ADE: 00         NOP                     
5ADF: 00         NOP                     
5AE0: 00         NOP                     
5AE1: 00         NOP                     
5AE2: 00         NOP                     
5AE3: 00         NOP                     
5AE4: 44         LD      B,H             
5AE5: 00         NOP                     
5AE6: 28 00      JR      Z,$5AE8         
5AE8: 10 00      STOP    $00             
5AEA: 28 00      JR      Z,$5AEC         
5AEC: 44         LD      B,H             
5AED: 00         NOP                     
5AEE: 00         NOP                     
5AEF: 00         NOP                     
5AF0: 00         NOP                     
5AF1: 00         NOP                     
5AF2: 00         NOP                     
5AF3: 00         NOP                     
5AF4: 44         LD      B,H             
5AF5: 00         NOP                     
5AF6: 28 00      JR      Z,$5AF8         
5AF8: 10 00      STOP    $00             
5AFA: 28 00      JR      Z,$5AFC         
5AFC: 44         LD      B,H             
5AFD: 00         NOP                     
5AFE: 00         NOP                     
5AFF: 00         NOP                     
5B00: 00         NOP                     
5B01: 00         NOP                     
5B02: 00         NOP                     
5B03: 00         NOP                     
5B04: 44         LD      B,H             
5B05: 00         NOP                     
5B06: 28 00      JR      Z,$5B08         
5B08: 10 00      STOP    $00             
5B0A: 28 00      JR      Z,$5B0C         
5B0C: 44         LD      B,H             
5B0D: 00         NOP                     
5B0E: 00         NOP                     
5B0F: 00         NOP                     
5B10: 00         NOP                     
5B11: 00         NOP                     
5B12: 00         NOP                     
5B13: 00         NOP                     
5B14: 44         LD      B,H             
5B15: 00         NOP                     
5B16: 28 00      JR      Z,$5B18         
5B18: 10 00      STOP    $00             
5B1A: 28 00      JR      Z,$5B1C         
5B1C: 44         LD      B,H             
5B1D: 00         NOP                     
5B1E: 00         NOP                     
5B1F: 00         NOP                     
5B20: 00         NOP                     
5B21: 00         NOP                     
5B22: 00         NOP                     
5B23: 00         NOP                     
5B24: 44         LD      B,H             
5B25: 00         NOP                     
5B26: 28 00      JR      Z,$5B28         
5B28: 10 00      STOP    $00             
5B2A: 28 00      JR      Z,$5B2C         
5B2C: 44         LD      B,H             
5B2D: 00         NOP                     
5B2E: 00         NOP                     
5B2F: 00         NOP                     
5B30: 00         NOP                     
5B31: 00         NOP                     
5B32: 00         NOP                     
5B33: 00         NOP                     
5B34: 44         LD      B,H             
5B35: 00         NOP                     
5B36: 28 00      JR      Z,$5B38         
5B38: 10 00      STOP    $00             
5B3A: 28 00      JR      Z,$5B3C         
5B3C: 44         LD      B,H             
5B3D: 00         NOP                     
5B3E: 00         NOP                     
5B3F: 00         NOP                     
5B40: 00         NOP                     
5B41: 00         NOP                     
5B42: 00         NOP                     
5B43: 00         NOP                     
5B44: 44         LD      B,H             
5B45: 00         NOP                     
5B46: 28 00      JR      Z,$5B48         
5B48: 10 00      STOP    $00             
5B4A: 28 00      JR      Z,$5B4C         
5B4C: 44         LD      B,H             
5B4D: 00         NOP                     
5B4E: 00         NOP                     
5B4F: 00         NOP                     
5B50: 00         NOP                     
5B51: 00         NOP                     
5B52: 00         NOP                     
5B53: 00         NOP                     
5B54: 44         LD      B,H             
5B55: 00         NOP                     
5B56: 28 00      JR      Z,$5B58         
5B58: 10 00      STOP    $00             
5B5A: 28 00      JR      Z,$5B5C         
5B5C: 44         LD      B,H             
5B5D: 00         NOP                     
5B5E: 00         NOP                     
5B5F: 00         NOP                     
5B60: 00         NOP                     
5B61: 00         NOP                     
5B62: 00         NOP                     
5B63: 00         NOP                     
5B64: 44         LD      B,H             
5B65: 00         NOP                     
5B66: 28 00      JR      Z,$5B68         
5B68: 10 00      STOP    $00             
5B6A: 28 00      JR      Z,$5B6C         
5B6C: 44         LD      B,H             
5B6D: 00         NOP                     
5B6E: 00         NOP                     
5B6F: 00         NOP                     
5B70: 00         NOP                     
5B71: 00         NOP                     
5B72: 00         NOP                     
5B73: 00         NOP                     
5B74: 44         LD      B,H             
5B75: 00         NOP                     
5B76: 28 00      JR      Z,$5B78         
5B78: 10 00      STOP    $00             
5B7A: 28 00      JR      Z,$5B7C         
5B7C: 44         LD      B,H             
5B7D: 00         NOP                     
5B7E: 00         NOP                     
5B7F: 00         NOP                     
5B80: 00         NOP                     
5B81: 00         NOP                     
5B82: 00         NOP                     
5B83: 00         NOP                     
5B84: 44         LD      B,H             
5B85: 00         NOP                     
5B86: 28 00      JR      Z,$5B88         
5B88: 10 00      STOP    $00             
5B8A: 28 00      JR      Z,$5B8C         
5B8C: 44         LD      B,H             
5B8D: 00         NOP                     
5B8E: 00         NOP                     
5B8F: 00         NOP                     
5B90: 00         NOP                     
5B91: 00         NOP                     
5B92: 00         NOP                     
5B93: 00         NOP                     
5B94: 44         LD      B,H             
5B95: 00         NOP                     
5B96: 28 00      JR      Z,$5B98         
5B98: 10 00      STOP    $00             
5B9A: 28 00      JR      Z,$5B9C         
5B9C: 44         LD      B,H             
5B9D: 00         NOP                     
5B9E: 00         NOP                     
5B9F: 00         NOP                     
5BA0: 00         NOP                     
5BA1: 00         NOP                     
5BA2: 00         NOP                     
5BA3: 00         NOP                     
5BA4: 44         LD      B,H             
5BA5: 00         NOP                     
5BA6: 28 00      JR      Z,$5BA8         
5BA8: 10 00      STOP    $00             
5BAA: 28 00      JR      Z,$5BAC         
5BAC: 44         LD      B,H             
5BAD: 00         NOP                     
5BAE: 00         NOP                     
5BAF: 00         NOP                     
5BB0: 00         NOP                     
5BB1: 00         NOP                     
5BB2: 00         NOP                     
5BB3: 00         NOP                     
5BB4: 44         LD      B,H             
5BB5: 00         NOP                     
5BB6: 28 00      JR      Z,$5BB8         
5BB8: 10 00      STOP    $00             
5BBA: 28 00      JR      Z,$5BBC         
5BBC: 44         LD      B,H             
5BBD: 00         NOP                     
5BBE: 00         NOP                     
5BBF: 00         NOP                     
5BC0: 00         NOP                     
5BC1: 00         NOP                     
5BC2: 00         NOP                     
5BC3: 00         NOP                     
5BC4: 44         LD      B,H             
5BC5: 00         NOP                     
5BC6: 28 00      JR      Z,$5BC8         
5BC8: 10 00      STOP    $00             
5BCA: 28 00      JR      Z,$5BCC         
5BCC: 44         LD      B,H             
5BCD: 00         NOP                     
5BCE: 00         NOP                     
5BCF: 00         NOP                     
5BD0: 00         NOP                     
5BD1: 00         NOP                     
5BD2: 00         NOP                     
5BD3: 00         NOP                     
5BD4: 44         LD      B,H             
5BD5: 00         NOP                     
5BD6: 28 00      JR      Z,$5BD8         
5BD8: 10 00      STOP    $00             
5BDA: 28 00      JR      Z,$5BDC         
5BDC: 44         LD      B,H             
5BDD: 00         NOP                     
5BDE: 00         NOP                     
5BDF: 00         NOP                     
5BE0: 00         NOP                     
5BE1: 00         NOP                     
5BE2: 00         NOP                     
5BE3: 00         NOP                     
5BE4: 44         LD      B,H             
5BE5: 00         NOP                     
5BE6: 28 00      JR      Z,$5BE8         
5BE8: 10 00      STOP    $00             
5BEA: 28 00      JR      Z,$5BEC         
5BEC: 44         LD      B,H             
5BED: 00         NOP                     
5BEE: 00         NOP                     
5BEF: 00         NOP                     
5BF0: 00         NOP                     
5BF1: 00         NOP                     
5BF2: 00         NOP                     
5BF3: 00         NOP                     
5BF4: 44         LD      B,H             
5BF5: 00         NOP                     
5BF6: 28 00      JR      Z,$5BF8         
5BF8: 10 00      STOP    $00             
5BFA: 28 00      JR      Z,$5BFC         
5BFC: 44         LD      B,H             
5BFD: 00         NOP                     
5BFE: 00         NOP                     
5BFF: 00         NOP                     
5C00: F3         DI                      
5C01: 0F         RRCA                    
5C02: CF         RST     0X08            
5C03: 3F         CCF                     
5C04: 9C         SBC     H               
5C05: 7F         LD      A,A             
5C06: 38 FF      JR      C,$5C07         
5C08: 38 F7      JR      C,$5C01         
5C0A: 3B         DEC     SP              
5C0B: F4         ???                     
5C0C: 3F         CCF                     
5C0D: F3         DI                      
5C0E: 7F         LD      A,A             
5C0F: F4         ???                     
5C10: CF         RST     0X08            
5C11: F0 F3      LD      A,($F3)         
5C13: FC         ???                     
5C14: 39         ADD     HL,SP           
5C15: FE 1C      CP      $1C             
5C17: FF         RST     0X38            
5C18: 1C         INC     E               
5C19: EF         RST     0X28            
5C1A: DC 2F FC   CALL    C,$FC2F         
5C1D: CF         RST     0X08            
5C1E: FE 3F      CP      $3F             
5C20: B6         OR      (HL)            
5C21: 7F         LD      A,A             
5C22: 64         LD      H,H             
5C23: 3F         CCF                     
5C24: 69         LD      L,C             
5C25: 3E 58      LD      A,$58           
5C27: 6F         LD      L,A             
5C28: 4A         LD      C,D             
5C29: 7F         LD      A,A             
5C2A: 6C         LD      L,H             
5C2B: 7F         LD      A,A             
5C2C: D4 6F 85   CALL    NC,$856F        
5C2F: FE 6D      CP      $6D             
5C31: FE 26      CP      $26             
5C33: FC         ???                     
5C34: 96         SUB     (HL)            
5C35: 7C         LD      A,H             
5C36: 1E F4      LD      E,$F4           
5C38: 52         LD      D,D             
5C39: FE 36      CP      $36             
5C3B: FE 2B      CP      $2B             
5C3D: F6 A1      OR      $A1             
5C3F: 7F         LD      A,A             
5C40: DD         ???                     
5C41: FE EE      CP      $EE             
5C43: F3         DI                      
5C44: D3         ???                     
5C45: E1         POP     HL              
5C46: DF         RST     0X18            
5C47: EC         ???                     
5C48: DF         RST     0X18            
5C49: EC         ???                     
5C4A: DE E1      SBC     $E1             
5C4C: ED         ???                     
5C4D: F3         DI                      
5C4E: FF         RST     0X38            
5C4F: DF         RST     0X18            
5C50: FF         RST     0X38            
5C51: 0F         RRCA                    
5C52: D3         ???                     
5C53: 31 25 E3   LD      SP,$E325        
5C56: F3         DI                      
5C57: CF         RST     0X08            
5C58: CE 83      ADC     $83             
5C5A: CE 83      ADC     $83             
5C5C: 64         LD      H,H             
5C5D: 9F         SBC     A               
5C5E: E7         RST     0X20            
5C5F: 1F         RRA                     
5C60: FF         RST     0X38            
5C61: 00         NOP                     
5C62: FB         EI                      
5C63: 07         RLCA                    
5C64: EC         ???                     
5C65: 1F         RRA                     
5C66: D0         RET     NC              
5C67: 3F         CCF                     
5C68: E3         ???                     
5C69: 3C         INC     A               
5C6A: A7         AND     A               
5C6B: 78         LD      A,B             
5C6C: C7         RST     0X00            
5C6D: 78         LD      A,B             
5C6E: 47         LD      B,A             
5C6F: F8 FF      LDHL    SP,$FF          
5C71: 00         NOP                     
5C72: DF         RST     0X18            
5C73: E0 37      LDFF00  ($37),A         
5C75: F8 0B      LDHL    SP,$0B          
5C77: FC         ???                     
5C78: C7         RST     0X00            
5C79: 3C         INC     A               
5C7A: E5         PUSH    HL              
5C7B: 1E E3      LD      E,$E3           
5C7D: 1E E2      LD      E,$E2           
5C7F: 1F         RRA                     
5C80: 1E 1E      LD      E,$1E           
5C82: 21 21 50   LD      HL,$5021        
5C85: 43         LD      B,E             
5C86: 41         LD      B,C             
5C87: 44         LD      B,H             
5C88: C0         RET     NZ              
5C89: 48         LD      C,B             
5C8A: E0 A9      LDFF00  ($A9),A         
5C8C: F0 98      LD      A,($98)         
5C8E: F8 98      LDHL    SP,$98          
5C90: 78         LD      A,B             
5C91: 78         LD      A,B             
5C92: 84         ADD     A,H             
5C93: 84         ADD     A,H             
5C94: 12         LD      (DE),A          
5C95: 02         LD      (BC),A          
5C96: 02         LD      (BC),A          
5C97: E2         LDFF00  (C),A           
5C98: 07         RLCA                    
5C99: 12         LD      (DE),A          
5C9A: 0D         DEC     C               
5C9B: 0F         RRCA                    
5C9C: 09         ADD     HL,BC           
5C9D: 0F         RRCA                    
5C9E: 19         ADD     HL,DE           
5C9F: 5F         LD      E,A             
5CA0: FC         ???                     
5CA1: 00         NOP                     
5CA2: F8 00      LDHL    SP,$00          
5CA4: F8 00      LDHL    SP,$00          
5CA6: F8 00      LDHL    SP,$00          
5CA8: C0         RET     NZ              
5CA9: 00         NOP                     
5CAA: 80         ADD     A,B             
5CAB: 00         NOP                     
5CAC: 80         ADD     A,B             
5CAD: 00         NOP                     
5CAE: 80         ADD     A,B             
5CAF: 00         NOP                     
5CB0: 00         NOP                     
5CB1: 00         NOP                     
5CB2: 00         NOP                     
5CB3: 00         NOP                     
5CB4: 22         LD      (HLI),A         
5CB5: 22         LD      (HLI),A         
5CB6: 14         INC     D               
5CB7: 14         INC     D               
5CB8: 08 08 14   LD      ($1408),SP      
5CBB: 14         INC     D               
5CBC: 22         LD      (HLI),A         
5CBD: 22         LD      (HLI),A         
5CBE: 00         NOP                     
5CBF: 00         NOP                     
5CC0: 00         NOP                     
5CC1: FF         RST     0X38            
5CC2: 00         NOP                     
5CC3: FF         RST     0X38            
5CC4: FF         RST     0X38            
5CC5: FF         RST     0X38            
5CC6: FF         RST     0X38            
5CC7: 92         SUB     D               
5CC8: FF         RST     0X38            
5CC9: FF         RST     0X38            
5CCA: 00         NOP                     
5CCB: FF         RST     0X38            
5CCC: 00         NOP                     
5CCD: FF         RST     0X38            
5CCE: 00         NOP                     
5CCF: FF         RST     0X38            
5CD0: 07         RLCA                    
5CD1: FF         RST     0X38            
5CD2: F9         LD      SP,HL           
5CD3: F8 41      LDHL    SP,$41          
5CD5: 88         ADC     A,B             
5CD6: 45         LD      B,L             
5CD7: 88         ADC     A,B             
5CD8: 54         LD      D,H             
5CD9: 88         ADC     A,B             
5CDA: 54         LD      D,H             
5CDB: 88         ADC     A,B             
5CDC: 15         DEC     D               
5CDD: 88         ADC     A,B             
5CDE: 15         DEC     D               
5CDF: 88         ADC     A,B             
5CE0: FF         RST     0X38            
5CE1: F0 CB      LD      A,($CB)         
5CE3: 8C         ADC     A,H             
5CE4: A4         AND     H               
5CE5: C7         RST     0X00            
5CE6: CF         RST     0X08            
5CE7: F3         DI                      
5CE8: 73         LD      (HL),E          
5CE9: C1         POP     BC              
5CEA: 73         LD      (HL),E          
5CEB: C1         POP     BC              
5CEC: 26 F9      LD      H,$F9           
5CEE: E7         RST     0X20            
5CEF: F8 BB      LDHL    SP,$BB          
5CF1: 7F         LD      A,A             
5CF2: 77         LD      (HL),A          
5CF3: CF         RST     0X08            
5CF4: CB 87      SET     1,E             
5CF6: FB         EI                      
5CF7: 37         SCF                     
5CF8: FB         EI                      
5CF9: 37         SCF                     
5CFA: 7B         LD      A,E             
5CFB: 87         ADD     A,A             
5CFC: B7         OR      A               
5CFD: CF         RST     0X08            
5CFE: FF         RST     0X38            
5CFF: FB         EI                      
5D00: DC FB 8C   CALL    C,$8CFB         
5D03: FB         EI                      
5D04: 8F         ADC     A,A             
5D05: F8 8F      LDHL    SP,$8F          
5D07: F9         LD      SP,HL           
5D08: 8F         ADC     A,A             
5D09: FE 86      CP      $86             
5D0B: FD         ???                     
5D0C: C7         RST     0X00            
5D0D: FC         ???                     
5D0E: F7         RST     0X30            
5D0F: FD         ???                     
5D10: 33         INC     SP              
5D11: DF         RST     0X18            
5D12: 31 DF F9   LD      SP,$F9DF        
5D15: 1F         RRA                     
5D16: F1         POP     AF              
5D17: 9F         SBC     A               
5D18: F5         PUSH    AF              
5D19: 7F         LD      A,A             
5D1A: 61         LD      H,C             
5D1B: BF         CP      A               
5D1C: E1         POP     HL              
5D1D: 3F         CCF                     
5D1E: EB         ???                     
5D1F: BF         CP      A               
5D20: 88         ADC     A,B             
5D21: FF         RST     0X38            
5D22: B9         CP      C               
5D23: FF         RST     0X38            
5D24: DA CE DE   JP      C,$DECE         
5D27: 8C         ADC     A,H             
5D28: FE 8C      CP      $8C             
5D2A: EF         RST     0X28            
5D2B: 9E         SBC     (HL)            
5D2C: 7F         LD      A,A             
5D2D: 5A         LD      E,D             
5D2E: 3B         DEC     SP              
5D2F: 31 11 FF   LD      SP,$FF11        
5D32: 9D         SBC     L               
5D33: FF         RST     0X38            
5D34: DB         ???                     
5D35: 73         LD      (HL),E          
5D36: FB         EI                      
5D37: 31 BF 71   LD      SP,$71BF        
5D3A: F7         RST     0X30            
5D3B: 79         LD      A,C             
5D3C: 7E         LD      A,(HL)          
5D3D: DA DC 8C   JP      C,$8CDC         
5D40: DE E3      SBC     $E3             
5D42: C2 FF C2   JP      NZ,$C2FF        
5D45: FF         RST     0X38            
5D46: C2 FF 43   JP      NZ,$43FF        
5D49: FE A3      CP      $A3             
5D4B: 7E         LD      A,(HL)          
5D4C: 5E         LD      E,(HL)          
5D4D: 3F         CCF                     
5D4E: 0F         RRCA                    
5D4F: 03         INC     BC              
5D50: 1C         INC     E               
5D51: 07         RLCA                    
5D52: 1F         RRA                     
5D53: 04         INC     B               
5D54: 65         LD      H,L             
5D55: 9E         SBC     (HL)            
5D56: 62         LD      H,D             
5D57: 9F         SBC     A               
5D58: 9E         SBC     (HL)            
5D59: 03         INC     BC              
5D5A: 9A         SBC     D               
5D5B: 07         RLCA                    
5D5C: 73         LD      (HL),E          
5D5D: 8F         ADC     A,A             
5D5E: FF         RST     0X38            
5D5F: FF         RST     0X38            
5D60: 00         NOP                     
5D61: FF         RST     0X38            
5D62: 07         RLCA                    
5D63: FF         RST     0X38            
5D64: 1C         INC     E               
5D65: FF         RST     0X38            
5D66: 30 FF      JR      NC,$5D67        
5D68: 63         LD      H,E             
5D69: FC         ???                     
5D6A: 67         LD      H,A             
5D6B: F8 C7      LDHL    SP,$C7          
5D6D: F8 C7      LDHL    SP,$C7          
5D6F: F8 00      LDHL    SP,$00          
5D71: FF         RST     0X38            
5D72: E0 FF      LDFF00  ($FF),A         
5D74: 38 FF      JR      C,$5D75         
5D76: 0C         INC     C               
5D77: FF         RST     0X38            
5D78: C6 3F      ADD     $3F             
5D7A: E6 1F      AND     $1F             
5D7C: E3         ???                     
5D7D: 1F         RRA                     
5D7E: E3         ???                     
5D7F: 1F         RRA                     
5D80: FC         ???                     
5D81: A4         AND     H               
5D82: FF         RST     0X38            
5D83: A7         AND     A               
5D84: FF         RST     0X38            
5D85: A2         AND     D               
5D86: FF         RST     0X38            
5D87: D2 FF 8A   JP      NC,$8AFF        
5D8A: 7F         LD      A,A             
5D8B: 44         LD      B,H             
5D8C: 3F         CCF                     
5D8D: 24         INC     H               
5D8E: 1F         RRA                     
5D8F: 1F         RRA                     
5D90: 29         ADD     HL,HL           
5D91: 3F         CCF                     
5D92: C9         RET                     
5D93: FF         RST     0X38            
5D94: C9         RET                     
5D95: 7F         LD      A,A             
5D96: C9         RET                     
5D97: 7F         LD      A,A             
5D98: DD         ???                     
5D99: 77         LD      (HL),A          
5D9A: FE 22      CP      $22             
5D9C: FC         ???                     
5D9D: 2C         INC     L               
5D9E: F9         LD      SP,HL           
5D9F: F8 3F      LDHL    SP,$3F          
5DA1: 00         NOP                     
5DA2: 1F         RRA                     
5DA3: 00         NOP                     
5DA4: 0F         RRCA                    
5DA5: 00         NOP                     
5DA6: 0F         RRCA                    
5DA7: 00         NOP                     
5DA8: 0F         RRCA                    
5DA9: 00         NOP                     
5DAA: 0F         RRCA                    
5DAB: 00         NOP                     
5DAC: 03         INC     BC              
5DAD: 00         NOP                     
5DAE: 01 00 00   LD      BC,$0000        
5DB1: 00         NOP                     
5DB2: 00         NOP                     
5DB3: 00         NOP                     
5DB4: 22         LD      (HLI),A         
5DB5: 22         LD      (HLI),A         
5DB6: 14         INC     D               
5DB7: 14         INC     D               
5DB8: 08 08 14   LD      ($1408),SP      
5DBB: 14         INC     D               
5DBC: 22         LD      (HLI),A         
5DBD: 22         LD      (HLI),A         
5DBE: 00         NOP                     
5DBF: 00         NOP                     
5DC0: 55         LD      D,L             
5DC1: 88         ADC     A,B             
5DC2: 51         LD      D,C             
5DC3: 88         ADC     A,B             
5DC4: 41         LD      B,C             
5DC5: 88         ADC     A,B             
5DC6: 45         LD      B,L             
5DC7: 88         ADC     A,B             
5DC8: 54         LD      D,H             
5DC9: 88         ADC     A,B             
5DCA: 54         LD      D,H             
5DCB: 88         ADC     A,B             
5DCC: 15         DEC     D               
5DCD: 88         ADC     A,B             
5DCE: 15         DEC     D               
5DCF: 88         ADC     A,B             
5DD0: 51         LD      D,C             
5DD1: 88         ADC     A,B             
5DD2: 51         LD      D,C             
5DD3: 88         ADC     A,B             
5DD4: 45         LD      B,L             
5DD5: 88         ADC     A,B             
5DD6: 40         LD      B,B             
5DD7: 8F         ADC     A,A             
5DD8: 07         RLCA                    
5DD9: F8 77      LDHL    SP,$77          
5DDB: 88         ADC     A,B             
5DDC: 77         LD      (HL),A          
5DDD: 8F         ADC     A,A             
5DDE: F8 FF      LDHL    SP,$FF          
5DE0: 38 E0      JR      C,$5DC2         
5DE2: F8 20      LDHL    SP,$20          
5DE4: A6         AND     (HL)            
5DE5: 79         LD      A,C             
5DE6: 46         LD      B,(HL)          
5DE7: F9         LD      SP,HL           
5DE8: 79         LD      A,C             
5DE9: C0         RET     NZ              
5DEA: 59         LD      E,C             
5DEB: E0 CE      LDFF00  ($CE),A         
5DED: F1         POP     AF              
5DEE: FF         RST     0X38            
5DEF: FF         RST     0X38            
5DF0: 7B         LD      A,E             
5DF1: C7         RST     0X00            
5DF2: 43         LD      B,E             
5DF3: FF         RST     0X38            
5DF4: 43         LD      B,E             
5DF5: FF         RST     0X38            
5DF6: 43         LD      B,E             
5DF7: FF         RST     0X38            
5DF8: C2 7F C5   JP      NZ,$C57F        
5DFB: 7E         LD      A,(HL)          
5DFC: 7A         LD      A,D             
5DFD: FC         ???                     
5DFE: F0 C0      LD      A,($C0)         
5E00: 01 01 06   LD      BC,$0601        
5E03: 07         RLCA                    
5E04: 0B         DEC     BC              
5E05: 0C         INC     C               
5E06: 16 18      LD      D,$18           
5E08: 17         RLA                     
5E09: 18 23      JR      $5E2E           
5E0B: 3F         CCF                     
5E0C: 2F         CPL                     
5E0D: 3C         INC     A               
5E0E: 74         LD      (HL),H          
5E0F: 38 FF      JR      C,$5E10         
5E11: FF         RST     0X38            
5E12: FE 08      CP      $08             
5E14: 1F         RRA                     
5E15: 04         INC     B               
5E16: 0F         RRCA                    
5E17: 07         RLCA                    
5E18: F8 0A      LDHL    SP,$0A          
5E1A: F2         ???                     
5E1B: F4         ???                     
5E1C: D3         ???                     
5E1D: 34         INC     (HL)            
5E1E: 78         LD      A,B             
5E1F: 13         INC     DE              
5E20: FF         RST     0X38            
5E21: FF         RST     0X38            
5E22: 7F         LD      A,A             
5E23: 10 F9      STOP    $F9             
5E25: 20 F0      JR      NZ,$5E17        
5E27: E0 1F      LDFF00  ($1F),A         
5E29: 50         LD      D,B             
5E2A: 4F         LD      C,A             
5E2B: 2F         CPL                     
5E2C: CB 2C      SET     1,E             
5E2E: 1E C8      LD      E,$C8           
5E30: 00         NOP                     
5E31: 00         NOP                     
5E32: C0         RET     NZ              
5E33: C0         RET     NZ              
5E34: B0         OR      B               
5E35: 70         LD      (HL),B          
5E36: C8         RET     Z               
5E37: 38 E8      JR      C,$5E21         
5E39: 18 C4      JR      $5DFF           
5E3B: FC         ???                     
5E3C: F4         ???                     
5E3D: 3C         INC     A               
5E3E: 6E         LD      L,(HL)          
5E3F: 1C         INC     E               
5E40: C0         RET     NZ              
5E41: 7F         LD      A,A             
5E42: 60         LD      H,B             
5E43: 3F         CCF                     
5E44: 78         LD      A,B             
5E45: 3F         CCF                     
5E46: D7         RST     0X10            
5E47: 4F         LD      C,A             
5E48: 8B         ADC     A,E             
5E49: 87         ADD     A,A             
5E4A: FD         ???                     
5E4B: 83         ADD     A,E             
5E4C: 86         ADD     A,(HL)          
5E4D: FE 7C      CP      $7C             
5E4F: 7C         LD      A,H             
5E50: 9F         SBC     A               
5E51: E0 8F      LDFF00  ($8F),A         
5E53: F0 87      LD      A,($87)         
5E55: F8 C0      LDHL    SP,$C0          
5E57: FF         RST     0X38            
5E58: F8 FF      LDHL    SP,$FF          
5E5A: 7F         LD      A,A             
5E5B: C7         RST     0X00            
5E5C: FF         RST     0X38            
5E5D: BB         CP      E               
5E5E: FE BB      CP      $BB             
5E60: F1         POP     AF              
5E61: 0F         RRCA                    
5E62: E1         POP     HL              
5E63: 1F         RRA                     
5E64: C1         POP     BC              
5E65: 3F         CCF                     
5E66: 03         INC     BC              
5E67: FF         RST     0X38            
5E68: 1F         RRA                     
5E69: FF         RST     0X38            
5E6A: FF         RST     0X38            
5E6B: E3         ???                     
5E6C: FF         RST     0X38            
5E6D: DD         ???                     
5E6E: 7F         LD      A,A             
5E6F: DD         ???                     
5E70: 03         INC     BC              
5E71: FE 06      CP      $06             
5E73: FC         ???                     
5E74: 1E FC      LD      E,$FC           
5E76: EF         RST     0X28            
5E77: F2         ???                     
5E78: D9         RETI                    
5E79: E1         POP     HL              
5E7A: DF         RST     0X18            
5E7B: E1         POP     HL              
5E7C: E1         POP     HL              
5E7D: 7F         LD      A,A             
5E7E: 7F         LD      A,A             
5E7F: 3E FF      LD      A,$FF           
5E81: FF         RST     0X38            
5E82: 7F         LD      A,A             
5E83: 10 F9      STOP    $F9             
5E85: 20 F0      JR      NZ,$5E77        
5E87: E0 1F      LDFF00  ($1F),A         
5E89: 50         LD      D,B             
5E8A: 4F         LD      C,A             
5E8B: 2F         CPL                     
5E8C: CB 2C      SET     1,E             
5E8E: 1E C8      LD      E,$C8           
5E90: FF         RST     0X38            
5E91: FF         RST     0X38            
5E92: FE 08      CP      $08             
5E94: 1F         RRA                     
5E95: 04         INC     B               
5E96: 0F         RRCA                    
5E97: 07         RLCA                    
5E98: F8 0A      LDHL    SP,$0A          
5E9A: F2         ???                     
5E9B: F4         ???                     
5E9C: D3         ???                     
5E9D: 34         INC     (HL)            
5E9E: 78         LD      A,B             
5E9F: 13         INC     DE              
5EA0: 00         NOP                     
5EA1: 00         NOP                     
5EA2: 42         LD      B,D             
5EA3: 42         LD      B,D             
5EA4: 24         INC     H               
5EA5: 24         INC     H               
5EA6: 18 18      JR      $5EC0           
5EA8: 18 18      JR      $5EC2           
5EAA: 24         INC     H               
5EAB: 24         INC     H               
5EAC: 42         LD      B,D             
5EAD: 42         LD      B,D             
5EAE: 00         NOP                     
5EAF: 00         NOP                     
5EB0: 00         NOP                     
5EB1: 00         NOP                     
5EB2: 42         LD      B,D             
5EB3: 42         LD      B,D             
5EB4: 24         INC     H               
5EB5: 24         INC     H               
5EB6: 18 18      JR      $5ED0           
5EB8: 18 18      JR      $5ED2           
5EBA: 24         INC     H               
5EBB: 24         INC     H               
5EBC: 42         LD      B,D             
5EBD: 42         LD      B,D             
5EBE: 00         NOP                     
5EBF: 00         NOP                     
5EC0: FF         RST     0X38            
5EC1: 87         ADD     A,A             
5EC2: FF         RST     0X38            
5EC3: F8 FF      LDHL    SP,$FF          
5EC5: 80         ADD     A,B             
5EC6: F8 C7      LDHL    SP,$C7          
5EC8: C7         RST     0X00            
5EC9: 78         LD      A,B             
5ECA: FF         RST     0X38            
5ECB: 43         LD      B,E             
5ECC: FF         RST     0X38            
5ECD: FE FF      CP      $FF             
5ECF: 80         ADD     A,B             
5ED0: FF         RST     0X38            
5ED1: E1         POP     HL              
5ED2: FF         RST     0X38            
5ED3: 1F         RRA                     
5ED4: FF         RST     0X38            
5ED5: 01 79 87   LD      BC,$8779        
5ED8: CF         RST     0X08            
5ED9: 31 FF FF   LD      SP,$FFFF        
5EDC: FF         RST     0X38            
5EDD: 02         LD      (BC),A          
5EDE: E3         ???                     
5EDF: 1E DB      LD      E,$DB           
5EE1: 18 AD      JR      $5E90           
5EE3: 2C         INC     L               
5EE4: 4A         LD      C,D             
5EE5: 4E         LD      C,(HL)          
5EE6: 89         ADC     A,C             
5EE7: 8F         ADC     A,A             
5EE8: 99         SBC     C               
5EE9: 9F         SBC     A               
5EEA: BD         CP      L               
5EEB: A7         AND     A               
5EEC: 7E         LD      A,(HL)          
5EED: 42         LD      B,D             
5EEE: BD         CP      L               
5EEF: 3C         INC     A               
5EF0: 00         NOP                     
5EF1: 00         NOP                     
5EF2: 42         LD      B,D             
5EF3: 42         LD      B,D             
5EF4: 24         INC     H               
5EF5: 24         INC     H               
5EF6: 18 18      JR      $5F10           
5EF8: 18 18      JR      $5F12           
5EFA: 24         INC     H               
5EFB: 24         INC     H               
5EFC: 42         LD      B,D             
5EFD: 42         LD      B,D             
5EFE: 00         NOP                     
5EFF: 00         NOP                     
5F00: 48         LD      C,B             
5F01: 70         LD      (HL),B          
5F02: D8         RET     C               
5F03: 60         LD      H,B             
5F04: 9F         SBC     A               
5F05: E0 9F      LDFF00  ($9F),A         
5F07: E0 9F      LDFF00  ($9F),A         
5F09: E0 8F      LDFF00  ($8F),A         
5F0B: F0 86      LD      A,($86)         
5F0D: F9         LD      SP,HL           
5F0E: 80         ADD     A,B             
5F0F: FF         RST     0X38            
5F10: 6C         LD      L,H             
5F11: 18 D7      JR      $5EEA           
5F13: 3F         CCF                     
5F14: AF         XOR     A               
5F15: 70         LD      (HL),B          
5F16: 5C         LD      E,H             
5F17: E0 58      LDFF00  ($58),A         
5F19: E0 98      LDFF00  ($98),A         
5F1B: E0 9C      LDFF00  ($9C),A         
5F1D: E0 9F      LDFF00  ($9F),A         
5F1F: E0 36      LDFF00  ($36),A         
5F21: 18 EB      JR      $5F0E           
5F23: FC         ???                     
5F24: C5         PUSH    BC              
5F25: 3E 62      LD      A,$62           
5F27: 1F         RRA                     
5F28: 32         LD      (HLD),A         
5F29: 0F         RRCA                    
5F2A: 31 0F 71   LD      SP,$710F        
5F2D: 0F         RRCA                    
5F2E: F1         POP     AF              
5F2F: 0F         RRCA                    
5F30: 32         LD      (HLD),A         
5F31: 0E 3B      LD      C,$3B           
5F33: 06 F9      LD      B,$F9           
5F35: 07         RLCA                    
5F36: F9         LD      SP,HL           
5F37: 07         RLCA                    
5F38: F9         LD      SP,HL           
5F39: 07         RLCA                    
5F3A: F1         POP     AF              
5F3B: 0F         RRCA                    
5F3C: 61         LD      H,C             
5F3D: 9F         SBC     A               
5F3E: 01 FF 78   LD      BC,$78FF        
5F41: 08 71 10   LD      ($1071),SP      
5F44: 3C         INC     A               
5F45: 2D         DEC     L               
5F46: 3E 2D      LD      A,$2D           
5F48: 2C         INC     L               
5F49: 33         INC     SP              
5F4A: 1F         RRA                     
5F4B: 1F         RRA                     
5F4C: 07         RLCA                    
5F4D: 00         NOP                     
5F4E: 00         NOP                     
5F4F: 00         NOP                     
5F50: FC         ???                     
5F51: 46         LD      B,(HL)          
5F52: F8 3C      LDHL    SP,$3C          
5F54: 90         SUB     B               
5F55: 78         LD      A,B             
5F56: 7B         LD      A,E             
5F57: F0 9F      LD      A,($9F)         
5F59: F3         DI                      
5F5A: 1F         RRA                     
5F5B: F3         DI                      
5F5C: CF         RST     0X08            
5F5D: 38 17      JR      C,$5F76         
5F5F: 0F         RRCA                    
5F60: 3E 62      LD      A,$62           
5F62: DF         RST     0X18            
5F63: 3C         INC     A               
5F64: 69         LD      L,C             
5F65: 1E FE      LD      E,$FE           
5F67: 0F         RRCA                    
5F68: F9         LD      SP,HL           
5F69: CF         RST     0X08            
5F6A: F8 CF      LDHL    SP,$CF          
5F6C: F3         DI                      
5F6D: 1C         INC     E               
5F6E: E8 F0      ADD     SP,$F0          
5F70: 3E 10      LD      A,$10           
5F72: 9E         SBC     (HL)            
5F73: 08 3C B4   LD      ($B43C),SP      
5F76: 7C         LD      A,H             
5F77: B4         OR      H               
5F78: 34         INC     (HL)            
5F79: CC F8 F8   CALL    Z,$F8F8         
5F7C: E0 00      LDFF00  ($00),A         
5F7E: 00         NOP                     
5F7F: 00         NOP                     
5F80: 36 18      LD      (HL),$18        
5F82: EB         ???                     
5F83: FC         ???                     
5F84: C5         PUSH    BC              
5F85: 3E 62      LD      A,$62           
5F87: 1F         RRA                     
5F88: 32         LD      (HLD),A         
5F89: 0F         RRCA                    
5F8A: 31 0F 71   LD      SP,$710F        
5F8D: 0F         RRCA                    
5F8E: F1         POP     AF              
5F8F: 0F         RRCA                    
5F90: 6C         LD      L,H             
5F91: 18 D7      JR      $5F6A           
5F93: 3F         CCF                     
5F94: AF         XOR     A               
5F95: 70         LD      (HL),B          
5F96: 5C         LD      E,H             
5F97: E0 58      LDFF00  ($58),A         
5F99: E0 98      LDFF00  ($98),A         
5F9B: E0 9C      LDFF00  ($9C),A         
5F9D: E0 9F      LDFF00  ($9F),A         
5F9F: E0 00      LDFF00  ($00),A         
5FA1: 00         NOP                     
5FA2: 42         LD      B,D             
5FA3: 42         LD      B,D             
5FA4: 24         INC     H               
5FA5: 24         INC     H               
5FA6: 18 18      JR      $5FC0           
5FA8: 18 18      JR      $5FC2           
5FAA: 24         INC     H               
5FAB: 24         INC     H               
5FAC: 42         LD      B,D             
5FAD: 42         LD      B,D             
5FAE: 00         NOP                     
5FAF: 00         NOP                     
5FB0: 00         NOP                     
5FB1: 00         NOP                     
5FB2: 42         LD      B,D             
5FB3: 42         LD      B,D             
5FB4: 24         INC     H               
5FB5: 24         INC     H               
5FB6: 18 18      JR      $5FD0           
5FB8: 18 18      JR      $5FD2           
5FBA: 24         INC     H               
5FBB: 24         INC     H               
5FBC: 42         LD      B,D             
5FBD: 42         LD      B,D             
5FBE: 00         NOP                     
5FBF: 00         NOP                     
5FC0: 87         ADD     A,A             
5FC1: F8 FF      LDHL    SP,$FF          
5FC3: C1         POP     BC              
5FC4: FE 7F      CP      $7F             
5FC6: FF         RST     0X38            
5FC7: 41         LD      B,C             
5FC8: 8F         ADC     A,A             
5FC9: F0 FC      LD      A,($FC)         
5FCB: 83         ADD     A,E             
5FCC: FF         RST     0X38            
5FCD: FC         ???                     
5FCE: FF         RST     0X38            
5FCF: C3 FF 01   JP      $01FF           
5FD2: FF         RST     0X38            
5FD3: F1         POP     AF              
5FD4: EF         RST     0X28            
5FD5: 1E FF      LD      E,$FF           
5FD7: F1         POP     AF              
5FD8: FF         RST     0X38            
5FD9: 01 73 8F   LD      BC,$8F73        
5FDC: FF         RST     0X38            
5FDD: 01 FF FF   LD      BC,$FFFF        
5FE0: E7         RST     0X20            
5FE1: 00         NOP                     
5FE2: DB         ???                     
5FE3: 18 A5      JR      $5F8A           
5FE5: 24         INC     H               
5FE6: 4E         LD      C,(HL)          
5FE7: 4A         LD      C,D             
5FE8: 4E         LD      C,(HL)          
5FE9: 4A         LD      C,D             
5FEA: 5E         LD      E,(HL)          
5FEB: 52         LD      D,D             
5FEC: BD         CP      L               
5FED: 3C         INC     A               
5FEE: C3 00 00   JP      $0000           
5FF1: 00         NOP                     
5FF2: 42         LD      B,D             
5FF3: 42         LD      B,D             
5FF4: 24         INC     H               
5FF5: 24         INC     H               
5FF6: 18 18      JR      $6010           
5FF8: 18 18      JR      $6012           
5FFA: 24         INC     H               
5FFB: 24         INC     H               
5FFC: 42         LD      B,D             
5FFD: 42         LD      B,D             
5FFE: 00         NOP                     
5FFF: 00         NOP                     
6000: E7         RST     0X20            
6001: 18 C3      JR      $5FC6           
6003: 3C         INC     A               
6004: 00         NOP                     
6005: FF         RST     0X38            
6006: 18 FF      JR      $6007           
6008: 3C         INC     A               
6009: FF         RST     0X38            
600A: FF         RST     0X38            
600B: FF         RST     0X38            
600C: C3 FF 66   JP      $66FF           
600F: 81         ADD     A,C             
6010: C3 C3 24   JP      $24C3           
6013: E7         RST     0X20            
6014: DB         ???                     
6015: 3C         INC     A               
6016: E7         RST     0X20            
6017: 18 FF      JR      $6018           
6019: 00         NOP                     
601A: FF         RST     0X38            
601B: 00         NOP                     
601C: FF         RST     0X38            
601D: 00         NOP                     
601E: FF         RST     0X38            
601F: 00         NOP                     
6020: 9F         SBC     A               
6021: E0 DF      LDFF00  ($DF),A         
6023: E0 E7      LDFF00  ($E7),A         
6025: F8 EF      LDHL    SP,$EF          
6027: 70         LD      (HL),B          
6028: FF         RST     0X38            
6029: 60         LD      H,B             
602A: DF         RST     0X18            
602B: 60         LD      H,B             
602C: 9F         SBC     A               
602D: E0 9F      LDFF00  ($9F),A         
602F: E0 F9      LDFF00  ($F9),A         
6031: 07         RLCA                    
6032: FB         EI                      
6033: 07         RLCA                    
6034: E7         RST     0X20            
6035: 1F         RRA                     
6036: F7         RST     0X30            
6037: 0E FF      LD      C,$FF           
6039: 06 FB      LD      B,$FB           
603B: 06 F9      LD      B,$F9           
603D: 07         RLCA                    
603E: F9         LD      SP,HL           
603F: 07         RLCA                    
6040: F3         DI                      
6041: 0C         INC     C               
6042: F9         LD      SP,HL           
6043: 06 F8      LD      B,$F8           
6045: 07         RLCA                    
6046: F8 07      LDHL    SP,$07          
6048: E3         ???                     
6049: 1F         RRA                     
604A: F1         POP     AF              
604B: 0F         RRCA                    
604C: F9         LD      SP,HL           
604D: 07         RLCA                    
604E: F9         LD      SP,HL           
604F: 07         RLCA                    
6050: CF         RST     0X08            
6051: 30 9F      JR      NC,$5FF2        
6053: 60         LD      H,B             
6054: 1F         RRA                     
6055: E0 1F      LDFF00  ($1F),A         
6057: E0 C7      LDFF00  ($C7),A         
6059: F8 8F      LDHL    SP,$8F          
605B: F0 9F      LD      A,($9F)         
605D: E0 9F      LDFF00  ($9F),A         
605F: E0 F1      LDFF00  ($F1),A         
6061: 0F         RRCA                    
6062: F7         RST     0X30            
6063: 08 FF 00   LD      ($00FF),SP      
6066: FF         RST     0X38            
6067: 00         NOP                     
6068: FF         RST     0X38            
6069: 00         NOP                     
606A: FF         RST     0X38            
606B: 00         NOP                     
606C: FF         RST     0X38            
606D: 00         NOP                     
606E: FF         RST     0X38            
606F: 00         NOP                     
6070: 8F         ADC     A,A             
6071: F0 EF      LD      A,($EF)         
6073: 10 FF      STOP    $FF             
6075: 00         NOP                     
6076: FF         RST     0X38            
6077: 00         NOP                     
6078: FF         RST     0X38            
6079: 00         NOP                     
607A: FF         RST     0X38            
607B: 00         NOP                     
607C: FF         RST     0X38            
607D: 00         NOP                     
607E: FF         RST     0X38            
607F: 00         NOP                     
6080: 8F         ADC     A,A             
6081: F0 83      LD      A,($83)         
6083: FC         ???                     
6084: 40         LD      B,B             
6085: FF         RST     0X38            
6086: B8         CP      B               
6087: 7F         LD      A,A             
6088: 6C         LD      L,H             
6089: 1F         RRA                     
608A: 17         RLA                     
608B: 0F         RRCA                    
608C: 0F         RRCA                    
608D: 07         RLCA                    
608E: 04         INC     B               
608F: 03         INC     BC              
6090: F1         POP     AF              
6091: 0F         RRCA                    
6092: C1         POP     BC              
6093: 3F         CCF                     
6094: 02         LD      (BC),A          
6095: FF         RST     0X38            
6096: 1D         DEC     E               
6097: FE 36      CP      $36             
6099: F8 E8      LDHL    SP,$E8          
609B: F0 F0      LD      A,($F0)         
609D: E0 20      LDFF00  ($20),A         
609F: C0         RET     NZ              
60A0: 07         RLCA                    
60A1: 03         INC     BC              
60A2: 0C         INC     C               
60A3: 07         RLCA                    
60A4: 0B         DEC     BC              
60A5: 0C         INC     C               
60A6: 77         LD      (HL),A          
60A7: 38 CF      JR      C,$6078         
60A9: 70         LD      (HL),B          
60AA: 9F         SBC     A               
60AB: E0 9F      LDFF00  ($9F),A         
60AD: E0 9F      LDFF00  ($9F),A         
60AF: E0 E0      LDFF00  ($E0),A         
60B1: C0         RET     NZ              
60B2: 30 E0      JR      NC,$6094        
60B4: D0         RET     NC              
60B5: 30 EE      JR      NC,$60A5        
60B7: 1C         INC     E               
60B8: F3         DI                      
60B9: 0E F9      LD      C,$F9           
60BB: 07         RLCA                    
60BC: F9         LD      SP,HL           
60BD: 07         RLCA                    
60BE: F9         LD      SP,HL           
60BF: 07         RLCA                    
60C0: 00         NOP                     
60C1: 00         NOP                     
60C2: 00         NOP                     
60C3: F8 00      LDHL    SP,$00          
60C5: 64         LD      H,H             
60C6: 00         NOP                     
60C7: 54         LD      D,H             
60C8: 00         NOP                     
60C9: 4A         LD      C,D             
60CA: 00         NOP                     
60CB: 21 00 1F   LD      HL,$1F00        
60CE: 00         NOP                     
60CF: 00         NOP                     
60D0: 00         NOP                     
60D1: 00         NOP                     
60D2: 10 00      STOP    $00             
60D4: 54         LD      D,H             
60D5: 00         NOP                     
60D6: 28 00      JR      Z,$60D8         
60D8: 00         NOP                     
60D9: 00         NOP                     
60DA: 00         NOP                     
60DB: 00         NOP                     
60DC: 00         NOP                     
60DD: 00         NOP                     
60DE: 00         NOP                     
60DF: 00         NOP                     
60E0: E9         JP      (HL)            
60E1: 18 E9      JR      $60CC           
60E3: 18 EB      JR      $60D0           
60E5: 18 F7      JR      $60DE           
60E7: 0C         INC     C               
60E8: F3         DI                      
60E9: 0F         RRCA                    
60EA: F8 07      LDHL    SP,$07          
60EC: FF         RST     0X38            
60ED: 00         NOP                     
60EE: FF         RST     0X38            
60EF: 00         NOP                     
60F0: F8 0F      LDHL    SP,$0F          
60F2: FF         RST     0X38            
60F3: 07         RLCA                    
60F4: F8 20      LDHL    SP,$20          
60F6: F8 70      LDHL    SP,$70          
60F8: 9C         SBC     H               
60F9: F0 0F      LD      A,($0F)         
60FB: FF         RST     0X38            
60FC: E7         RST     0X20            
60FD: 1F         RRA                     
60FE: FF         RST     0X38            
60FF: 00         NOP                     
6100: 1F         RRA                     
6101: F0 FF      LD      A,($FF)         
6103: E0 FF      LDFF00  ($FF),A         
6105: 0C         INC     C               
6106: FF         RST     0X38            
6107: 1F         RRA                     
6108: F0 1F      LD      A,($1F)         
610A: E3         ???                     
610B: FC         ???                     
610C: CF         RST     0X08            
610D: F0 FF      LD      A,($FF)         
610F: 00         NOP                     
6110: 37         SCF                     
6111: 18 17      JR      $612A           
6113: 18 A7      JR      $60BC           
6115: 38 CF      JR      C,$60E6         
6117: F0 3F      LD      A,($3F)         
6119: C0         RET     NZ              
611A: FF         RST     0X38            
611B: 00         NOP                     
611C: FF         RST     0X38            
611D: 00         NOP                     
611E: FF         RST     0X38            
611F: 00         NOP                     
6120: FF         RST     0X38            
6121: 00         NOP                     
6122: 9F         SBC     A               
6123: 60         LD      H,B             
6124: 1F         RRA                     
6125: E0 3F      LDFF00  ($3F),A         
6127: C0         RET     NZ              
6128: F9         LD      SP,HL           
6129: 06 F8      LD      B,$F8           
612B: 07         RLCA                    
612C: FC         ???                     
612D: 03         INC     BC              
612E: FF         RST     0X38            
612F: 00         NOP                     
6130: E7         RST     0X20            
6131: 18 C0      JR      $60F3           
6133: 3F         CCF                     
6134: 1F         RRA                     
6135: FF         RST     0X38            
6136: 38 FF      JR      C,$6137         
6138: E3         ???                     
6139: F8 C3      LDHL    SP,$C3          
613B: F0 A7      LD      A,($A7)         
613D: D0         RET     NC              
613E: 63         LD      H,E             
613F: 90         SUB     B               
6140: E7         RST     0X20            
6141: 18 03      JR      $6146           
6143: FC         ???                     
6144: F8 FF      LDHL    SP,$FF          
6146: 1C         INC     E               
6147: FF         RST     0X38            
6148: C7         RST     0X00            
6149: 1F         RRA                     
614A: C3 0F C5   JP      $C50F           
614D: 0B         DEC     BC              
614E: E6 09      AND     $09             
6150: C7         RST     0X00            
6151: 10 C7      STOP    $C7             
6153: 10 A3      STOP    $A3             
6155: 10 A3      STOP    $A3             
6157: 10 A3      STOP    $A3             
6159: 10 C7      STOP    $C7             
615B: 10 C3      STOP    $C3             
615D: 10 C3      STOP    $C3             
615F: 10 C3      STOP    $C3             
6161: 08 C3 08   LD      ($08C3),SP      
6164: E3         ???                     
6165: 08 C3 08   LD      ($08C3),SP      
6168: C5         PUSH    BC              
6169: 08 C5 08   LD      ($08C5),SP      
616C: E1         POP     HL              
616D: 08 E3 08   LD      ($08E3),SP      
6170: 68         LD      L,B             
6171: 97         SUB     A               
6172: 40         LD      B,B             
6173: B8         CP      B               
6174: 48         LD      C,B             
6175: A0         AND     B               
6176: 85         ADD     A,L             
6177: 40         LD      B,B             
6178: 0F         RRCA                    
6179: 87         ADD     A,A             
617A: 1F         RRA                     
617B: 4F         LD      C,A             
617C: 1F         RRA                     
617D: 3F         CCF                     
617E: 7F         LD      A,A             
617F: 3F         CCF                     
6180: 16 E9      LD      D,$E9           
6182: 06 19      LD      B,$19           
6184: 1A         LD      A,(DE)          
6185: 05         DEC     B               
6186: A0         AND     B               
6187: 03         INC     BC              
6188: F0 E1      LD      A,($E1)         
618A: F8 F2      LDHL    SP,$F2          
618C: F8 FC      LDHL    SP,$FC          
618E: FC         ???                     
618F: FC         ???                     
6190: 00         NOP                     
6191: 00         NOP                     
6192: 42         LD      B,D             
6193: 42         LD      B,D             
6194: 24         INC     H               
6195: 24         INC     H               
6196: 18 18      JR      $61B0           
6198: 18 18      JR      $61B2           
619A: 24         INC     H               
619B: 24         INC     H               
619C: 42         LD      B,D             
619D: 42         LD      B,D             
619E: 00         NOP                     
619F: 00         NOP                     
61A0: 00         NOP                     
61A1: 00         NOP                     
61A2: 42         LD      B,D             
61A3: 42         LD      B,D             
61A4: 24         INC     H               
61A5: 24         INC     H               
61A6: 18 18      JR      $61C0           
61A8: 18 18      JR      $61C2           
61AA: 24         INC     H               
61AB: 24         INC     H               
61AC: 42         LD      B,D             
61AD: 42         LD      B,D             
61AE: 00         NOP                     
61AF: 00         NOP                     
61B0: 00         NOP                     
61B1: 00         NOP                     
61B2: 42         LD      B,D             
61B3: 42         LD      B,D             
61B4: 24         INC     H               
61B5: 24         INC     H               
61B6: 18 18      JR      $61D0           
61B8: 18 18      JR      $61D2           
61BA: 24         INC     H               
61BB: 24         INC     H               
61BC: 42         LD      B,D             
61BD: 42         LD      B,D             
61BE: 00         NOP                     
61BF: 00         NOP                     
61C0: 00         NOP                     
61C1: 00         NOP                     
61C2: 10 00      STOP    $00             
61C4: 54         LD      D,H             
61C5: 00         NOP                     
61C6: 28 00      JR      Z,$61C8         
61C8: 00         NOP                     
61C9: 00         NOP                     
61CA: 00         NOP                     
61CB: 00         NOP                     
61CC: 00         NOP                     
61CD: 00         NOP                     
61CE: 00         NOP                     
61CF: 00         NOP                     
61D0: 00         NOP                     
61D1: 00         NOP                     
61D2: 00         NOP                     
61D3: 1F         RRA                     
61D4: 00         NOP                     
61D5: 26 00      LD      H,$00           
61D7: 2A         LD      A,(HLI)         
61D8: 00         NOP                     
61D9: 52         LD      D,D             
61DA: 00         NOP                     
61DB: 84         ADD     A,H             
61DC: 00         NOP                     
61DD: F8 00      LDHL    SP,$00          
61DF: 00         NOP                     
61E0: 00         NOP                     
61E1: 00         NOP                     
61E2: 42         LD      B,D             
61E3: 42         LD      B,D             
61E4: 24         INC     H               
61E5: 24         INC     H               
61E6: 18 18      JR      $6200           
61E8: 18 18      JR      $6202           
61EA: 24         INC     H               
61EB: 24         INC     H               
61EC: 42         LD      B,D             
61ED: 42         LD      B,D             
61EE: 00         NOP                     
61EF: 00         NOP                     
61F0: C3 FF 81   JP      $81FF           
61F3: FF         RST     0X38            
61F4: 3C         INC     A               
61F5: C3 FF 00   JP      $00FF           
61F8: 99         SBC     C               
61F9: 00         NOP                     
61FA: 00         NOP                     
61FB: 00         NOP                     
61FC: 00         NOP                     
61FD: 00         NOP                     
61FE: 00         NOP                     
61FF: 00         NOP                     
6200: 00         NOP                     
6201: 00         NOP                     
6202: 07         RLCA                    
6203: 07         RLCA                    
6204: 1F         RRA                     
6205: 18 2F      JR      $6236           
6207: 30 50      JR      NC,$6259        
6209: 6F         LD      L,A             
620A: 83         ADD     A,E             
620B: FF         RST     0X38            
620C: 9C         SBC     H               
620D: FF         RST     0X38            
620E: EB         ???                     
620F: EC         ???                     
6210: 03         INC     BC              
6211: 03         INC     BC              
6212: 85         ADD     A,L             
6213: 86         ADD     A,(HL)          
6214: 49         LD      C,C             
6215: CE A9      ADC     $A9             
6217: 6E         LD      L,(HL)          
6218: 55         LD      D,L             
6219: BF         CP      A               
621A: 8E         ADC     A,(HL)          
621B: FA 5A F2   LD      A,($F25A)       
621E: 9B         SBC     E               
621F: 72         LD      (HL),D          
6220: E0 E0      LDFF00  ($E0),A         
6222: 91         SUB     C               
6223: 71         LD      (HL),C          
6224: 92         SUB     D               
6225: 73         LD      (HL),E          
6226: 95         SUB     L               
6227: 76         HALT                    
6228: A8         XOR     B               
6229: FF         RST     0X38            
622A: 71         LD      (HL),C          
622B: 5F         LD      E,A             
622C: 52         LD      D,D             
622D: 5F         LD      E,A             
622E: D9         RETI                    
622F: 4E         LD      C,(HL)          
6230: 00         NOP                     
6231: 00         NOP                     
6232: E0 E0      LDFF00  ($E0),A         
6234: F8 18      LDHL    SP,$18          
6236: F4         ???                     
6237: 0C         INC     C               
6238: 02         LD      (BC),A          
6239: FE C1      CP      $C1             
623B: FF         RST     0X38            
623C: 39         ADD     HL,SP           
623D: FF         RST     0X38            
623E: D7         RST     0X10            
623F: 37         SCF                     
6240: 89         ADC     A,C             
6241: F9         LD      SP,HL           
6242: 93         SUB     E               
6243: F3         DI                      
6244: A7         AND     A               
6245: E5         PUSH    HL              
6246: 47         LD      B,A             
6247: 45         LD      B,L             
6248: 07         RLCA                    
6249: 05         DEC     B               
624A: 03         INC     BC              
624B: 07         RLCA                    
624C: 07         RLCA                    
624D: 05         DEC     B               
624E: 09         ADD     HL,BC           
624F: 08 41 BF   LD      ($BF41),SP      
6252: 42         LD      B,D             
6253: BF         CP      A               
6254: 05         DEC     B               
6255: FE 0F      CP      $0F             
6257: FE 1F      CP      $1F             
6259: F9         LD      SP,HL           
625A: 3E F8      LD      A,$F8           
625C: FF         RST     0X38            
625D: E9         JP      (HL)            
625E: FF         RST     0X38            
625F: 46         LD      B,(HL)          
6260: E1         POP     HL              
6261: FE 30      CP      $30             
6263: FF         RST     0X38            
6264: D8         RET     C               
6265: 3F         CCF                     
6266: EC         ???                     
6267: 3F         CCF                     
6268: FE CF      CP      $CF             
626A: 7B         LD      A,E             
626B: 0F         RRCA                    
626C: FF         RST     0X38            
626D: 93         SUB     E               
626E: FF         RST     0X38            
626F: 72         LD      (HL),D          
6270: 49         LD      C,C             
6271: CF         RST     0X08            
6272: 65         LD      H,L             
6273: E7         RST     0X20            
6274: 73         LD      (HL),E          
6275: D3         ???                     
6276: 70         LD      (HL),B          
6277: D0         RET     NC              
6278: 70         LD      (HL),B          
6279: D0         RET     NC              
627A: 70         LD      (HL),B          
627B: D0         RET     NC              
627C: E0 A0      LDFF00  ($A0),A         
627E: 90         SUB     B               
627F: 10 F7      STOP    $F7             
6281: 07         RLCA                    
6282: EA 0D C7   LD      ($C70D),A       
6285: 07         RLCA                    
6286: 80         ADD     A,B             
6287: 00         NOP                     
6288: 87         ADD     A,A             
6289: 07         RLCA                    
628A: 1B         DEC     DE              
628B: 18 37      JR      $62C4           
628D: 27         DAA                     
628E: 39         ADD     HL,SP           
628F: 2C         INC     L               
6290: AE         XOR     (HL)            
6291: AE         XOR     (HL)            
6292: 55         LD      D,L             
6293: DB         ???                     
6294: FE DE      CP      $DE             
6296: 71         LD      (HL),C          
6297: 70         LD      (HL),B          
6298: DF         RST     0X18            
6299: D0         RET     NC              
629A: 5F         LD      E,A             
629B: D0         RET     NC              
629C: FF         RST     0X38            
629D: D8         RET     C               
629E: B7         OR      A               
629F: 7C         LD      A,H             
62A0: FE 00      CP      $00             
62A2: CD 30 8C   CALL    $8C30           
62A5: 53         LD      D,E             
62A6: 8A         ADC     A,D             
62A7: 54         LD      D,H             
62A8: A0         AND     B               
62A9: 5F         LD      E,A             
62AA: C1         POP     BC              
62AB: 20 A0      JR      NZ,$624D        
62AD: 40         LD      B,B             
62AE: 27         DAA                     
62AF: 40         LD      B,B             
62B0: 01 78 13   LD      BC,$1378        
62B3: 88         ADC     A,B             
62B4: 13         INC     DE              
62B5: E8 2F      ADD     SP,$2F          
62B7: 10 D7      STOP    $D7             
62B9: 08 37 C8   LD      ($C837),SP      
62BC: 56         LD      D,(HL)          
62BD: 28 8E      JR      Z,$624D         
62BF: 30 F8      JR      NC,$62B9        
62C1: 00         NOP                     
62C2: E0 00      LDFF00  ($00),A         
62C4: C0         RET     NZ              
62C5: 00         NOP                     
62C6: 80         ADD     A,B             
62C7: 00         NOP                     
62C8: 80         ADD     A,B             
62C9: 00         NOP                     
62CA: 00         NOP                     
62CB: 00         NOP                     
62CC: 00         NOP                     
62CD: 00         NOP                     
62CE: 00         NOP                     
62CF: 00         NOP                     
62D0: 01 00 03   LD      BC,$0300        
62D3: 00         NOP                     
62D4: 07         RLCA                    
62D5: 00         NOP                     
62D6: 07         RLCA                    
62D7: 00         NOP                     
62D8: 0F         RRCA                    
62D9: 00         NOP                     
62DA: 0F         RRCA                    
62DB: 00         NOP                     
62DC: 1F         RRA                     
62DD: 00         NOP                     
62DE: 1F         RRA                     
62DF: 00         NOP                     
62E0: F8 01      LDHL    SP,$01          
62E2: E1         POP     HL              
62E3: 02         LD      (BC),A          
62E4: C3 04 86   JP      $8604           
62E7: 09         ADD     HL,BC           
62E8: 8F         ADC     A,A             
62E9: 10 0F      STOP    $0F             
62EB: 20 1E      JR      NZ,$630B        
62ED: 41         LD      B,C             
62EE: 2C         INC     L               
62EF: 93         SUB     E               
62F0: 01 C0 83   LD      BC,$83C0        
62F3: 40         LD      B,B             
62F4: 07         RLCA                    
62F5: C0         RET     NZ              
62F6: C7         RST     0X00            
62F7: 20 8F      JR      NZ,$6288        
62F9: 70         LD      (HL),B          
62FA: 0F         RRCA                    
62FB: E0 1F      LDFF00  ($1F),A         
62FD: C0         RET     NZ              
62FE: 1F         RRA                     
62FF: 80         ADD     A,B             
6300: 16 19      LD      D,$19           
6302: 2C         INC     L               
6303: 33         INC     SP              
6304: 38 27      JR      C,$632D         
6306: 51         LD      D,C             
6307: 6F         LD      L,A             
6308: 41         LD      B,C             
6309: 7F         LD      A,A             
630A: 41         LD      B,C             
630B: 7F         LD      A,A             
630C: 83         ADD     A,E             
630D: FF         RST     0X38            
630E: 85         ADD     A,L             
630F: FD         ???                     
6310: 19         ADD     HL,DE           
6311: F1         POP     AF              
6312: 4C         LD      C,H             
6313: FC         ???                     
6314: 86         ADD     A,(HL)          
6315: FC         ???                     
6316: 33         INC     SP              
6317: CF         RST     0X08            
6318: 78         LD      A,B             
6319: 87         ADD     A,A             
631A: 70         LD      (HL),B          
631B: 8F         ADC     A,A             
631C: 60         LD      H,B             
631D: 9F         SBC     A               
631E: 61         LD      H,C             
631F: 9F         SBC     A               
6320: 98         SBC     B               
6321: 8F         ADC     A,A             
6322: 30 3F      JR      NC,$6363        
6324: 63         LD      H,E             
6325: 3F         CCF                     
6326: CC F3 8E   CALL    Z,$8EF3         
6329: F1         POP     AF              
632A: 87         ADD     A,A             
632B: F8 83      LDHL    SP,$83          
632D: FC         ???                     
632E: C1         POP     BC              
632F: FE E8      CP      $E8             
6331: 18 34      JR      $6367           
6333: CC 14 EC   CALL    Z,$EC14         
6336: 82         ADD     A,D             
6337: FE 42      CP      $42             
6339: FE 42      CP      $42             
633B: FE 61      CP      $61             
633D: FF         RST     0X38            
633E: 71         LD      (HL),C          
633F: FF         RST     0X38            
6340: 11 10 1F   LD      DE,$1F10        
6343: 10 1F      STOP    $1F             
6345: 10 0F      STOP    $0F             
6347: 0F         RRCA                    
6348: 02         LD      (BC),A          
6349: 01 03 00   LD      BC,$0003        
634C: 01 00 00   LD      BC,$0000        
634F: 00         NOP                     
6350: FE 70      CP      $70             
6352: FE 08      CP      $08             
6354: FF         RST     0X38            
6355: 09         ADD     HL,BC           
6356: FF         RST     0X38            
6357: C6 7E      ADD     $7E             
6359: E0 BE      LDFF00  ($BE),A         
635B: 70         LD      (HL),B          
635C: FF         RST     0X38            
635D: 08 07 07   LD      ($0707),SP      
6360: 7F         LD      A,A             
6361: 02         LD      (BC),A          
6362: 7F         LD      A,A             
6363: 1E FF      LD      E,$FF           
6365: 90         SUB     B               
6366: FF         RST     0X38            
6367: 61         LD      H,C             
6368: 7E         LD      A,(HL)          
6369: 07         RLCA                    
636A: 79         LD      A,C             
636B: 0E FF      LD      C,$FF           
636D: 10 E0      STOP    $E0             
636F: E0 D8      LDFF00  ($D8),A         
6371: 08 F8 08   LD      ($08F8),SP      
6374: F8 08      LDHL    SP,$08          
6376: F0 F0      LD      A,($F0)         
6378: 80         ADD     A,B             
6379: 00         NOP                     
637A: 80         ADD     A,B             
637B: 00         NOP                     
637C: 00         NOP                     
637D: 00         NOP                     
637E: 00         NOP                     
637F: 00         NOP                     
6380: 73         LD      (HL),E          
6381: 58         LD      E,B             
6382: 7E         LD      A,(HL)          
6383: 51         LD      D,C             
6384: AC         XOR     H               
6385: F3         DI                      
6386: B1         OR      C               
6387: EE A3      XOR     $A3             
6389: FC         ???                     
638A: 80         ADD     A,B             
638B: FF         RST     0X38            
638C: C0         RET     NZ              
638D: 7F         LD      A,A             
638E: FF         RST     0X38            
638F: 3F         CCF                     
6390: 26 DC      LD      H,$DC           
6392: 6A         LD      L,D             
6393: 9E         SBC     (HL)            
6394: CA 3E 96   JP      Z,$963E         
6397: 7E         LD      A,(HL)          
6398: 26 FC      LD      H,$FC           
639A: CC F8 38   CALL    Z,$38F8         
639D: F0 F0      LD      A,($F0)         
639F: C0         RET     NZ              
63A0: 3C         INC     A               
63A1: 43         LD      B,E             
63A2: 1C         INC     E               
63A3: 23         INC     HL              
63A4: 18 27      JR      $63CD           
63A6: 08 27 13   LD      ($1327),SP      
63A9: 4C         LD      C,H             
63AA: BF         CP      A               
63AB: 00         NOP                     
63AC: 7F         LD      A,A             
63AD: 80         ADD     A,B             
63AE: 7C         LD      A,H             
63AF: 00         NOP                     
63B0: 4C         LD      C,H             
63B1: 90         SUB     B               
63B2: 00         NOP                     
63B3: DE 38      SBC     $38             
63B5: C1         POP     BC              
63B6: 78         LD      A,B             
63B7: 86         ADD     A,(HL)          
63B8: F0 00      LD      A,($00)         
63BA: E0 00      LDFF00  ($00),A         
63BC: 80         ADD     A,B             
63BD: 00         NOP                     
63BE: 00         NOP                     
63BF: 00         NOP                     
63C0: 00         NOP                     
63C1: 00         NOP                     
63C2: 00         NOP                     
63C3: 00         NOP                     
63C4: 00         NOP                     
63C5: 00         NOP                     
63C6: 03         INC     BC              
63C7: 00         NOP                     
63C8: 0F         RRCA                    
63C9: 00         NOP                     
63CA: 3F         CCF                     
63CB: 00         NOP                     
63CC: 7F         LD      A,A             
63CD: 00         NOP                     
63CE: FF         RST     0X38            
63CF: 00         NOP                     
63D0: 3E 00      LD      A,$00           
63D2: 7E         LD      A,(HL)          
63D3: 00         NOP                     
63D4: FE 00      CP      $00             
63D6: FC         ???                     
63D7: 00         NOP                     
63D8: FC         ???                     
63D9: 00         NOP                     
63DA: F8 00      LDHL    SP,$00          
63DC: E0 00      LDFF00  ($00),A         
63DE: 00         NOP                     
63DF: 00         NOP                     
63E0: 38 C7      JR      C,$63A9         
63E2: 00         NOP                     
63E3: 3E 00      LD      A,$00           
63E5: 1C         INC     E               
63E6: 03         INC     BC              
63E7: 00         NOP                     
63E8: 0F         RRCA                    
63E9: 20 0F      JR      NZ,$63FA        
63EB: 50         LD      D,B             
63EC: 0F         RRCA                    
63ED: 70         LD      (HL),B          
63EE: FF         RST     0X38            
63EF: 00         NOP                     
63F0: 3E 00      LD      A,$00           
63F2: 1E 60      LD      E,$60           
63F4: 8E         ADC     A,(HL)          
63F5: 50         LD      D,B             
63F6: 64         LD      H,H             
63F7: 88         ADC     A,B             
63F8: B0         OR      B               
63F9: 44         LD      B,H             
63FA: D8         RET     C               
63FB: 22         LD      (HLI),A         
63FC: EC         ???                     
63FD: 13         INC     DE              
63FE: 00         NOP                     
63FF: 0E 03      LD      C,$03           
6401: 03         INC     BC              
6402: 06 04      LD      B,$04           
6404: 3D         DEC     A               
6405: 3E 47      LD      A,$47           
6407: 47         LD      B,A             
6408: 9E         SBC     (HL)            
6409: 82         ADD     A,D             
640A: B6         OR      (HL)            
640B: 8A         ADC     A,D             
640C: E6 9A      AND     $9A             
640E: 7C         LD      A,H             
640F: 44         LD      B,H             
6410: 80         ADD     A,B             
6411: 80         ADD     A,B             
6412: F0 70      LD      A,($70)         
6414: D8         RET     C               
6415: 88         ADC     A,B             
6416: A8         XOR     B               
6417: D8         RET     C               
6418: 5C         LD      E,H             
6419: 7C         LD      A,H             
641A: 36 22      LD      (HL),$22        
641C: 3E 22      LD      A,$22           
641E: 3E 3E      LD      A,$3E           
6420: 3F         CCF                     
6421: 38 47      JR      C,$646A         
6423: 44         LD      B,H             
6424: D7         RST     0X10            
6425: D4 C7 C4   CALL    NC,$C4C7        
6428: FB         EI                      
6429: FC         ???                     
642A: E0 BF      LDFF00  ($BF),A         
642C: B8         CP      B               
642D: 9F         SBC     A               
642E: D7         RST     0X10            
642F: CF         RST     0X08            
6430: FD         ???                     
6431: 03         INC     BC              
6432: FD         ???                     
6433: 03         INC     BC              
6434: F9         LD      SP,HL           
6435: 07         RLCA                    
6436: F1         POP     AF              
6437: 7F         LD      A,A             
6438: 8B         ADC     A,E             
6439: 8F         ADC     A,A             
643A: AF         XOR     A               
643B: AD         XOR     L               
643C: 8D         ADC     A,L             
643D: 89         ADC     A,C             
643E: FB         EI                      
643F: F3         DI                      
6440: 00         NOP                     
6441: 00         NOP                     
6442: 1E 1E      LD      E,$1E           
6444: 31 31 38   LD      SP,$3831        
6447: 28 3D      JR      Z,$6486         
6449: 25         DEC     H               
644A: 1E 12      LD      E,$12           
644C: 1C         INC     E               
644D: 14         INC     D               
644E: 08 08 07   LD      ($0708),SP      
6451: 07         RLCA                    
6452: 08 08 70   LD      ($7008),SP      
6455: 70         LD      (HL),B          
6456: 91         SUB     C               
6457: 90         SUB     B               
6458: 10 10      STOP    $10             
645A: 9C         SBC     H               
645B: 1C         INC     E               
645C: 7F         LD      A,A             
645D: 7F         LD      A,A             
645E: FF         RST     0X38            
645F: FC         ???                     
6460: F8 F8      LDHL    SP,$F8          
6462: 3C         INC     A               
6463: 24         INC     H               
6464: 3F         CCF                     
6465: 13         INC     DE              
6466: 1E 12      LD      E,$12           
6468: 1E 12      LD      E,$12           
646A: 3E 3E      LD      A,$3E           
646C: FE FE      CP      $FE             
646E: FF         RST     0X38            
646F: 7F         LD      A,A             
6470: 00         NOP                     
6471: 00         NOP                     
6472: 0E 0E      LD      C,$0E           
6474: 91         SUB     C               
6475: 91         SUB     C               
6476: 63         LD      H,E             
6477: 63         LD      H,E             
6478: 27         DAA                     
6479: 25         DEC     H               
647A: 6F         LD      L,A             
647B: 69         LD      L,C             
647C: FF         RST     0X38            
647D: B1         OR      C               
647E: FE 2A      CP      $2A             
6480: 97         SUB     A               
6481: 9C         SBC     H               
6482: A7         AND     A               
6483: BC         CP      H               
6484: C7         RST     0X00            
6485: FC         ???                     
6486: 97         SUB     A               
6487: FC         ???                     
6488: 97         SUB     A               
6489: ED         ???                     
648A: 47         LD      B,A             
648B: 7E         LD      A,(HL)          
648C: 29         ADD     HL,HL           
648D: 39         ADD     HL,SP           
648E: 10 10      STOP    $10             
6490: FF         RST     0X38            
6491: 7F         LD      A,A             
6492: FF         RST     0X38            
6493: F3         DI                      
6494: FF         RST     0X38            
6495: F3         DI                      
6496: BF         CP      A               
6497: B3         OR      E               
6498: 9F         SBC     A               
6499: 93         SUB     E               
649A: FE 72      CP      $72             
649C: FF         RST     0X38            
649D: 01 FF 80   LD      BC,$80FF        
64A0: FF         RST     0X38            
64A1: 04         INC     B               
64A2: FF         RST     0X38            
64A3: 94         SUB     H               
64A4: EF         RST     0X28            
64A5: C4 FF C5   CALL    NZ,$C5FF        
64A8: 7E         LD      A,(HL)          
64A9: 67         LD      H,A             
64AA: 7C         LD      A,H             
64AB: 57         LD      D,A             
64AC: F8 8F      LDHL    SP,$8F          
64AE: F8 0F      LDHL    SP,$0F          
64B0: FD         ???                     
64B1: 27         DAA                     
64B2: F9         LD      SP,HL           
64B3: 2F         CPL                     
64B4: F1         POP     AF              
64B5: FF         RST     0X38            
64B6: 85         ADD     A,L             
64B7: FF         RST     0X38            
64B8: 85         ADD     A,L             
64B9: FB         EI                      
64BA: 81         ADD     A,C             
64BB: FF         RST     0X38            
64BC: B9         CP      C               
64BD: FF         RST     0X38            
64BE: C6 C6      ADD     $C6             
64C0: FF         RST     0X38            
64C1: FF         RST     0X38            
64C2: DB         ???                     
64C3: E7         RST     0X20            
64C4: D3         ???                     
64C5: E7         RST     0X20            
64C6: DB         ???                     
64C7: E7         RST     0X20            
64C8: CB F7      SET     1,E             
64CA: DB         ???                     
64CB: E7         RST     0X20            
64CC: CB E7      SET     1,E             
64CE: DB         ???                     
64CF: E7         RST     0X20            
64D0: E0 A0      LDFF00  ($A0),A         
64D2: BF         CP      A               
64D3: DF         RST     0X18            
64D4: 98         SBC     B               
64D5: E8 CB      ADD     SP,$CB          
64D7: FB         EI                      
64D8: F9         LD      SP,HL           
64D9: B9         CP      C               
64DA: BD         CP      L               
64DB: DD         ???                     
64DC: 54         LD      D,H             
64DD: 7C         LD      A,H             
64DE: 3F         CCF                     
64DF: 3F         CCF                     
64E0: DB         ???                     
64E1: 18 AD      JR      $6490           
64E3: 2C         INC     L               
64E4: 4A         LD      C,D             
64E5: 4E         LD      C,(HL)          
64E6: 89         ADC     A,C             
64E7: 8F         ADC     A,A             
64E8: 99         SBC     C               
64E9: 9F         SBC     A               
64EA: BD         CP      L               
64EB: A7         AND     A               
64EC: 7E         LD      A,(HL)          
64ED: 42         LD      B,D             
64EE: BD         CP      L               
64EF: 3C         INC     A               
64F0: 02         LD      (BC),A          
64F1: 00         NOP                     
64F2: 22         LD      (HLI),A         
64F3: 00         NOP                     
64F4: 02         LD      (BC),A          
64F5: 00         NOP                     
64F6: 82         ADD     A,D             
64F7: 00         NOP                     
64F8: 0A         LD      A,(BC)          
64F9: 00         NOP                     
64FA: 02         LD      (BC),A          
64FB: 00         NOP                     
64FC: FC         ???                     
64FD: 00         NOP                     
64FE: 00         NOP                     
64FF: 00         NOP                     
6500: 38 38      JR      C,$653A         
6502: 00         NOP                     
6503: 00         NOP                     
6504: 00         NOP                     
6505: 00         NOP                     
6506: 03         INC     BC              
6507: 03         INC     BC              
6508: 0F         RRCA                    
6509: 0C         INC     C               
650A: 1E 10      LD      E,$10           
650C: 3E 20      LD      A,$20           
650E: 3F         CCF                     
650F: 20 66      JR      NZ,$6577        
6511: 42         LD      B,D             
6512: E5         PUSH    HL              
6513: 83         ADD     A,E             
6514: F9         LD      SP,HL           
6515: 87         ADD     A,A             
6516: E1         POP     HL              
6517: FF         RST     0X38            
6518: F9         LD      SP,HL           
6519: 1F         RRA                     
651A: 3E 06      LD      A,$06           
651C: 3A         LD      A,(HLD)         
651D: 06 FE      LD      B,$FE           
651F: 02         LD      (BC),A          
6520: E0 A0      LDFF00  ($A0),A         
6522: BF         CP      A               
6523: DF         RST     0X18            
6524: 9F         SBC     A               
6525: E4         ???                     
6526: C4 FF FF   CALL    NZ,$FFFF        
6529: BF         CP      A               
652A: BF         CP      A               
652B: D1         POP     DE              
652C: 51         LD      D,C             
652D: 7F         LD      A,A             
652E: 3F         CCF                     
652F: 3F         CCF                     
6530: 07         RLCA                    
6531: 05         DEC     B               
6532: FD         ???                     
6533: FB         EI                      
6534: F9         LD      SP,HL           
6535: 27         DAA                     
6536: 23         INC     HL              
6537: FF         RST     0X38            
6538: FF         RST     0X38            
6539: FD         ???                     
653A: FD         ???                     
653B: 0B         DEC     BC              
653C: 0A         LD      A,(BC)          
653D: FE FC      CP      $FC             
653F: FC         ???                     
6540: 09         ADD     HL,BC           
6541: 09         ADD     HL,BC           
6542: 1D         DEC     E               
6543: 15         DEC     D               
6544: 1F         RRA                     
6545: 13         INC     DE              
6546: 1F         RRA                     
6547: 11 1B 15   LD      DE,$151B        
654A: 3B         DEC     SP              
654B: 31 4F 4A   LD      SP,$4A4F        
654E: 8F         ADC     A,A             
654F: 8C         ADC     A,H             
6550: FF         RST     0X38            
6551: FC         ???                     
6552: F7         RST     0X30            
6553: F4         ???                     
6554: E7         RST     0X20            
6555: E4         ???                     
6556: 0F         RRCA                    
6557: 0F         RRCA                    
6558: 10 10      STOP    $10             
655A: E0 E0      LDFF00  ($E0),A         
655C: C2 40 C0   JP      NZ,$C040        
655F: 40         LD      B,B             
6560: FF         RST     0X38            
6561: 7F         LD      A,A             
6562: FF         RST     0X38            
6563: 7F         LD      A,A             
6564: DF         RST     0X18            
6565: 5F         LD      E,A             
6566: CF         RST     0X08            
6567: 4F         LD      C,A             
6568: C1         POP     BC              
6569: C1         POP     BC              
656A: 61         LD      H,C             
656B: 61         LD      H,C             
656C: 7F         LD      A,A             
656D: 5F         LD      E,A             
656E: FF         RST     0X38            
656F: 88         ADC     A,B             
6570: FC         ???                     
6571: 24         INC     H               
6572: FE 22      CP      $22             
6574: FE 62      CP      $62             
6576: FE 92      CP      $92             
6578: FE 0A      CP      $0A             
657A: FE 26      CP      $26             
657C: DD         ???                     
657D: 07         RLCA                    
657E: FD         ???                     
657F: C7         RST     0X00            
6580: 12         LD      (DE),A          
6581: 10 38      STOP    $38             
6583: 28 3F      JR      Z,$65C4         
6585: 27         DAA                     
6586: 3F         CCF                     
6587: 24         INC     H               
6588: 3F         CCF                     
6589: 24         INC     H               
658A: 1F         RRA                     
658B: 14         INC     D               
658C: 0F         RRCA                    
658D: 0F         RRCA                    
658E: 00         NOP                     
658F: 00         NOP                     
6590: FF         RST     0X38            
6591: E3         ???                     
6592: 9C         SBC     H               
6593: 9C         SBC     H               
6594: 84         ADD     A,H             
6595: 84         ADD     A,H             
6596: FE FE      CP      $FE             
6598: 87         ADD     A,A             
6599: FD         ???                     
659A: FF         RST     0X38            
659B: FC         ???                     
659C: 07         RLCA                    
659D: 04         INC     B               
659E: 03         INC     BC              
659F: 03         INC     BC              
65A0: F8 EF      LDHL    SP,$EF          
65A2: 14         INC     D               
65A3: 1F         RRA                     
65A4: 14         INC     D               
65A5: 1F         RRA                     
65A6: 17         RLA                     
65A7: 1F         RRA                     
65A8: E4         ???                     
65A9: FC         ???                     
65AA: E4         ???                     
65AB: 3C         INC     A               
65AC: E8 38      ADD     SP,$38          
65AE: F0 F0      LD      A,($F0)         
65B0: C2 C2 E2   JP      NZ,$E2C2        
65B3: A2         AND     D               
65B4: FE 9E      CP      $9E             
65B6: FE 92      CP      $92             
65B8: 7E         LD      A,(HL)          
65B9: 52         LD      D,D             
65BA: 3C         INC     A               
65BB: 3C         INC     A               
65BC: 00         NOP                     
65BD: 00         NOP                     
65BE: 00         NOP                     
65BF: 00         NOP                     
65C0: DB         ???                     
65C1: E7         RST     0X20            
65C2: CB F7      SET     1,E             
65C4: DB         ???                     
65C5: E7         RST     0X20            
65C6: DB         ???                     
65C7: E7         RST     0X20            
65C8: D3         ???                     
65C9: E7         RST     0X20            
65CA: 5A         LD      E,D             
65CB: E7         RST     0X20            
65CC: 7E         LD      A,(HL)          
65CD: 24         INC     H               
65CE: 3C         INC     A               
65CF: 18 07      JR      $65D8           
65D1: 05         DEC     B               
65D2: FD         ???                     
65D3: FB         EI                      
65D4: 19         ADD     HL,DE           
65D5: 17         RLA                     
65D6: D3         ???                     
65D7: DF         RST     0X18            
65D8: 9F         SBC     A               
65D9: 9D         SBC     L               
65DA: BD         CP      L               
65DB: AB         XOR     E               
65DC: 2A         LD      A,(HLI)         
65DD: 3E FC      LD      A,$FC           
65DF: FC         ???                     
65E0: E7         RST     0X20            
65E1: 00         NOP                     
65E2: DB         ???                     
65E3: 18 A5      JR      $658A           
65E5: 24         INC     H               
65E6: 4E         LD      C,(HL)          
65E7: 4A         LD      C,D             
65E8: 4E         LD      C,(HL)          
65E9: 4A         LD      C,D             
65EA: 5E         LD      E,(HL)          
65EB: 52         LD      D,D             
65EC: BD         CP      L               
65ED: 3C         INC     A               
65EE: C3 00 55   JP      $5500           
65F1: FF         RST     0X38            
65F2: 00         NOP                     
65F3: FF         RST     0X38            
65F4: AA         XOR     D               
65F5: 55         LD      D,L             
65F6: FF         RST     0X38            
65F7: 00         NOP                     
65F8: 00         NOP                     
65F9: 00         NOP                     
65FA: 00         NOP                     
65FB: 00         NOP                     
65FC: 00         NOP                     
65FD: 00         NOP                     
65FE: 00         NOP                     
65FF: 00         NOP                     
6600: 18 18      JR      $661A           
6602: 28 28      JR      Z,$662C         
6604: 2E 2E      LD      L,$2E           
6606: 5F         LD      E,A             
6607: 49         LD      C,C             
6608: BF         CP      A               
6609: 9F         SBC     A               
660A: B1         OR      C               
660B: B1         OR      C               
660C: F5         PUSH    AF              
660D: F5         PUSH    AF              
660E: B1         OR      C               
660F: B1         OR      C               
6610: 00         NOP                     
6611: 00         NOP                     
6612: 03         INC     BC              
6613: 03         INC     BC              
6614: 05         DEC     B               
6615: 05         DEC     B               
6616: 75         LD      (HL),L          
6617: 75         LD      (HL),L          
6618: F7         RST     0X30            
6619: 95         SUB     L               
661A: F7         RST     0X30            
661B: F5         PUSH    AF              
661C: F7         RST     0X30            
661D: F7         RST     0X30            
661E: FD         ???                     
661F: FD         ???                     
6620: 04         INC     B               
6621: 04         INC     B               
6622: 03         INC     BC              
6623: 03         INC     BC              
6624: 1E 1E      LD      E,$1E           
6626: 36 32      LD      (HL),$32        
6628: 76         HALT                    
6629: 52         LD      D,D             
662A: F7         RST     0X30            
662B: D3         ???                     
662C: F7         RST     0X30            
662D: D0         RET     NC              
662E: F0 D0      LD      A,($D0)         
6630: 40         LD      B,B             
6631: 40         LD      B,B             
6632: 80         ADD     A,B             
6633: 80         ADD     A,B             
6634: F0 F0      LD      A,($F0)         
6636: D8         RET     C               
6637: 98         SBC     B               
6638: DC 94 DE   CALL    C,$DE94         
663B: 96         SUB     (HL)            
663C: DE 16      SBC     $16             
663E: 1E 16      LD      E,$16           
6640: FE FF      CP      $FF             
6642: CF         RST     0X08            
6643: 81         ADD     A,C             
6644: 9F         SBC     A               
6645: A0         AND     B               
6646: BB         CP      E               
6647: 80         ADD     A,B             
6648: BF         CP      A               
6649: 80         ADD     A,B             
664A: BF         CP      A               
664B: 80         ADD     A,B             
664C: 92         SUB     D               
664D: 80         ADD     A,B             
664E: CC 80 7F   CALL    Z,$7F80         
6651: FF         RST     0X38            
6652: FF         RST     0X38            
6653: 81         ADD     A,C             
6654: DF         RST     0X18            
6655: 21 FB 01   LD      HL,$01FB        
6658: FF         RST     0X38            
6659: 01 FF 01   LD      BC,$01FF        
665C: 19         ADD     HL,DE           
665D: 01 C3 01   LD      BC,$01C3        
6660: 0F         RRCA                    
6661: 0F         RRCA                    
6662: 18 10      JR      $6674           
6664: 2B         DEC     HL              
6665: 30 4B      JR      NC,$66B2        
6667: 70         LD      (HL),B          
6668: 8B         ADC     A,E             
6669: F0 8B      LD      A,($8B)         
666B: F0 8B      LD      A,($8B)         
666D: F0 8B      LD      A,($8B)         
666F: F0 FF      LD      A,($FF)         
6671: FF         RST     0X38            
6672: 00         NOP                     
6673: 00         NOP                     
6674: FF         RST     0X38            
6675: 00         NOP                     
6676: FF         RST     0X38            
6677: 00         NOP                     
6678: FF         RST     0X38            
6679: 00         NOP                     
667A: FF         RST     0X38            
667B: 00         NOP                     
667C: FF         RST     0X38            
667D: 00         NOP                     
667E: FF         RST     0X38            
667F: 00         NOP                     
6680: F0 F0      LD      A,($F0)         
6682: 18 08      JR      $668C           
6684: D4 0C D2   CALL    NC,$D20C        
6687: 0E D1      LD      C,$D1           
6689: 0F         RRCA                    
668A: D1         POP     DE              
668B: 0F         RRCA                    
668C: D1         POP     DE              
668D: 0F         RRCA                    
668E: D1         POP     DE              
668F: 0F         RRCA                    
6690: 8B         ADC     A,E             
6691: F0 8B      LD      A,($8B)         
6693: F0 8B      LD      A,($8B)         
6695: F0 8B      LD      A,($8B)         
6697: F0 8B      LD      A,($8B)         
6699: F0 8B      LD      A,($8B)         
669B: F0 8B      LD      A,($8B)         
669D: F0 8B      LD      A,($8B)         
669F: F0 7F      LD      A,($7F)         
66A1: 7F         LD      A,A             
66A2: C0         RET     NZ              
66A3: 80         ADD     A,B             
66A4: 80         ADD     A,B             
66A5: 80         ADD     A,B             
66A6: 90         SUB     B               
66A7: 9F         SBC     A               
66A8: 90         SUB     B               
66A9: 9F         SBC     A               
66AA: FF         RST     0X38            
66AB: 9F         SBC     A               
66AC: 9F         SBC     A               
66AD: 9F         SBC     A               
66AE: 9F         SBC     A               
66AF: 9F         SBC     A               
66B0: FE FE      CP      $FE             
66B2: 81         ADD     A,C             
66B3: 01 81 01   LD      BC,$0181        
66B6: 89         ADC     A,C             
66B7: F9         LD      SP,HL           
66B8: 89         ADC     A,C             
66B9: F9         LD      SP,HL           
66BA: FF         RST     0X38            
66BB: F9         LD      SP,HL           
66BC: F9         LD      SP,HL           
66BD: F9         LD      SP,HL           
66BE: F9         LD      SP,HL           
66BF: F9         LD      SP,HL           
66C0: 00         NOP                     
66C1: 00         NOP                     
66C2: 00         NOP                     
66C3: 00         NOP                     
66C4: 18 18      JR      $66DE           
66C6: 24         INC     H               
66C7: 24         INC     H               
66C8: 5A         LD      E,D             
66C9: 42         LD      B,D             
66CA: 5A         LD      E,D             
66CB: 42         LD      B,D             
66CC: 46         LD      B,(HL)          
66CD: 66         LD      H,(HL)          
66CE: 4A         LD      C,D             
66CF: 5E         LD      E,(HL)          
66D0: 7F         LD      A,A             
66D1: 3F         CCF                     
66D2: C0         RET     NZ              
66D3: 40         LD      B,B             
66D4: 87         ADD     A,A             
66D5: 8F         ADC     A,A             
66D6: 88         ADC     A,B             
66D7: 88         ADC     A,B             
66D8: C7         RST     0X00            
66D9: CF         RST     0X08            
66DA: 80         ADD     A,B             
66DB: 80         ADD     A,B             
66DC: 8F         ADC     A,A             
66DD: 8F         ADC     A,A             
66DE: 40         LD      B,B             
66DF: C0         RET     NZ              
66E0: EF         RST     0X28            
66E1: 00         NOP                     
66E2: C7         RST     0X00            
66E3: 00         NOP                     
66E4: BB         CP      E               
66E5: 00         NOP                     
66E6: 7C         LD      A,H             
66E7: 00         NOP                     
66E8: 7C         LD      A,H             
66E9: 00         NOP                     
66EA: BB         CP      E               
66EB: 00         NOP                     
66EC: C7         RST     0X00            
66ED: 00         NOP                     
66EE: EF         RST     0X28            
66EF: 00         NOP                     
66F0: 00         NOP                     
66F1: 00         NOP                     
66F2: 01 00 01   LD      BC,$0100        
66F5: 00         NOP                     
66F6: 01 00 01   LD      BC,$0100        
66F9: 00         NOP                     
66FA: 01 00 01   LD      BC,$0100        
66FD: 00         NOP                     
66FE: 7F         LD      A,A             
66FF: 00         NOP                     
6700: 9F         SBC     A               
6701: 9F         SBC     A               
6702: 9F         SBC     A               
6703: 9E         SBC     (HL)            
6704: BF         CP      A               
6705: 9F         SBC     A               
6706: B3         OR      E               
6707: B3         OR      E               
6708: E9         JP      (HL)            
6709: A9         XOR     C               
670A: C4 C4 06   CALL    NZ,$06C4        
670D: 06 05      LD      B,$05           
670F: 05         DEC     B               
6710: F5         PUSH    AF              
6711: 15         DEC     D               
6712: FF         RST     0X38            
6713: DD         ???                     
6714: F7         RST     0X30            
6715: D7         RST     0X10            
6716: F7         RST     0X30            
6717: F5         PUSH    AF              
6718: 97         SUB     A               
6719: 95         SUB     L               
671A: 27         DAA                     
671B: 25         DEC     H               
671C: C7         RST     0X00            
671D: C5         PUSH    BC              
671E: 43         LD      B,E             
671F: 43         LD      B,E             
6720: FF         RST     0X38            
6721: DF         RST     0X18            
6722: FF         RST     0X38            
6723: DF         RST     0X18            
6724: FF         RST     0X38            
6725: C0         RET     NZ              
6726: FF         RST     0X38            
6727: DF         RST     0X18            
6728: F0 B0      LD      A,($B0)         
672A: F5         PUSH    AF              
672B: B5         OR      L               
672C: F0 B0      LD      A,($B0)         
672E: FF         RST     0X38            
672F: FF         RST     0X38            
6730: FE F6      CP      $F6             
6732: FE F6      CP      $F6             
6734: FE 06      CP      $06             
6736: FE F6      CP      $F6             
6738: 1E 1A      LD      E,$1A           
673A: 5E         LD      E,(HL)          
673B: 5A         LD      E,D             
673C: 1E 1A      LD      E,$1A           
673E: FE FE      CP      $FE             
6740: 9F         SBC     A               
6741: FF         RST     0X38            
6742: FF         RST     0X38            
6743: F1         POP     AF              
6744: F3         DI                      
6745: 9D         SBC     L               
6746: B3         OR      E               
6747: DF         RST     0X18            
6748: FF         RST     0X38            
6749: FC         ???                     
674A: FE 85      CP      $85             
674C: 8C         ADC     A,H             
674D: F7         RST     0X30            
674E: FF         RST     0X38            
674F: FF         RST     0X38            
6750: F9         LD      SP,HL           
6751: FF         RST     0X38            
6752: FF         RST     0X38            
6753: 8F         ADC     A,A             
6754: CF         RST     0X08            
6755: B9         CP      C               
6756: CD FB FF   CALL    $FFFB           
6759: 3F         CCF                     
675A: 7F         LD      A,A             
675B: A1         AND     C               
675C: 31 EF FF   LD      SP,$FFEF        
675F: FF         RST     0X38            
6760: 88         ADC     A,B             
6761: F0 8F      LD      A,($8F)         
6763: F0 90      LD      A,($90)         
6765: EF         RST     0X28            
6766: 90         SUB     B               
6767: EF         RST     0X28            
6768: A0         AND     B               
6769: DF         RST     0X18            
676A: A0         AND     B               
676B: DF         RST     0X18            
676C: C0         RET     NZ              
676D: BF         CP      A               
676E: C0         RET     NZ              
676F: BF         CP      A               
6770: 00         NOP                     
6771: 00         NOP                     
6772: FF         RST     0X38            
6773: 00         NOP                     
6774: 00         NOP                     
6775: FF         RST     0X38            
6776: 00         NOP                     
6777: FF         RST     0X38            
6778: 00         NOP                     
6779: FF         RST     0X38            
677A: 00         NOP                     
677B: FF         RST     0X38            
677C: 00         NOP                     
677D: FF         RST     0X38            
677E: 00         NOP                     
677F: FF         RST     0X38            
6780: 11 0F F1   LD      DE,$F10F        
6783: 0F         RRCA                    
6784: 09         ADD     HL,BC           
6785: F7         RST     0X30            
6786: 09         ADD     HL,BC           
6787: F7         RST     0X30            
6788: 05         DEC     B               
6789: FB         EI                      
678A: 05         DEC     B               
678B: FB         EI                      
678C: 03         INC     BC              
678D: FD         ???                     
678E: 03         INC     BC              
678F: FD         ???                     
6790: D1         POP     DE              
6791: 0F         RRCA                    
6792: D1         POP     DE              
6793: 0F         RRCA                    
6794: D1         POP     DE              
6795: 0F         RRCA                    
6796: D1         POP     DE              
6797: 0F         RRCA                    
6798: D1         POP     DE              
6799: 0F         RRCA                    
679A: D1         POP     DE              
679B: 0F         RRCA                    
679C: D1         POP     DE              
679D: 0F         RRCA                    
679E: D1         POP     DE              
679F: 0F         RRCA                    
67A0: 9F         SBC     A               
67A1: 9F         SBC     A               
67A2: 80         ADD     A,B             
67A3: 80         ADD     A,B             
67A4: C0         RET     NZ              
67A5: 80         ADD     A,B             
67A6: BF         CP      A               
67A7: C0         RET     NZ              
67A8: 80         ADD     A,B             
67A9: BF         CP      A               
67AA: C0         RET     NZ              
67AB: 84         ADD     A,H             
67AC: 7B         LD      A,E             
67AD: 44         LD      B,H             
67AE: 3F         CCF                     
67AF: 3F         CCF                     
67B0: F9         LD      SP,HL           
67B1: F9         LD      SP,HL           
67B2: 81         ADD     A,C             
67B3: 01 83 01   LD      BC,$0183        
67B6: 7D         LD      A,L             
67B7: 83         ADD     A,E             
67B8: 01 FD 03   LD      BC,$03FD        
67BB: 11 EE 12   LD      DE,$12EE        
67BE: FC         ???                     
67BF: FC         ???                     
67C0: 4A         LD      C,D             
67C1: 56         LD      D,(HL)          
67C2: 4A         LD      C,D             
67C3: 56         LD      D,(HL)          
67C4: 4A         LD      C,D             
67C5: 46         LD      B,(HL)          
67C6: 4A         LD      C,D             
67C7: 56         LD      D,(HL)          
67C8: 6A         LD      L,D             
67C9: 56         LD      D,(HL)          
67CA: 6A         LD      L,D             
67CB: 56         LD      D,(HL)          
67CC: 3C         INC     A               
67CD: 3C         INC     A               
67CE: 00         NOP                     
67CF: 00         NOP                     
67D0: FF         RST     0X38            
67D1: FF         RST     0X38            
67D2: 00         NOP                     
67D3: 00         NOP                     
67D4: B3         OR      E               
67D5: B3         OR      E               
67D6: 12         LD      (DE),A          
67D7: 12         LD      (DE),A          
67D8: 1E 9E      LD      E,$9E           
67DA: 92         SUB     D               
67DB: 92         SUB     D               
67DC: 33         INC     SP              
67DD: B3         OR      E               
67DE: 00         NOP                     
67DF: 00         NOP                     
67E0: FF         RST     0X38            
67E1: FF         RST     0X38            
67E2: 00         NOP                     
67E3: 00         NOP                     
67E4: 39         ADD     HL,SP           
67E5: 39         ADD     HL,SP           
67E6: 44         LD      B,H             
67E7: 44         LD      B,H             
67E8: 44         LD      B,H             
67E9: 44         LD      B,H             
67EA: 44         LD      B,H             
67EB: 44         LD      B,H             
67EC: 39         ADD     HL,SP           
67ED: 39         ADD     HL,SP           
67EE: 00         NOP                     
67EF: 00         NOP                     
67F0: FC         ???                     
67F1: FC         ???                     
67F2: 03         INC     BC              
67F3: 02         LD      (BC),A          
67F4: E1         POP     HL              
67F5: F1         POP     AF              
67F6: 91         SUB     C               
67F7: 91         SUB     C               
67F8: E3         ???                     
67F9: F3         DI                      
67FA: 81         ADD     A,C             
67FB: 81         ADD     A,C             
67FC: C1         POP     BC              
67FD: C1         POP     BC              
67FE: 02         LD      (BC),A          
67FF: 03         INC     BC              
6800: 8F         ADC     A,A             
6801: F0 C8      LD      A,($C8)         
6803: B7         OR      A               
6804: A8         XOR     B               
6805: D7         RST     0X10            
6806: 98         SBC     B               
6807: E7         RST     0X20            
6808: 8F         ADC     A,A             
6809: F0 C0      LD      A,($C0)         
680B: BF         CP      A               
680C: A0         AND     B               
680D: DF         RST     0X18            
680E: 90         SUB     B               
680F: EF         RST     0X28            
6810: F1         POP     AF              
6811: 0F         RRCA                    
6812: 03         INC     BC              
6813: FD         ???                     
6814: 05         DEC     B               
6815: FB         EI                      
6816: 09         ADD     HL,BC           
6817: F7         RST     0X30            
6818: F1         POP     AF              
6819: 0F         RRCA                    
681A: 13         INC     DE              
681B: ED         ???                     
681C: 15         DEC     D               
681D: EB         ???                     
681E: 19         ADD     HL,DE           
681F: E7         RST     0X20            
6820: 3F         CCF                     
6821: FF         RST     0X38            
6822: 7F         LD      A,A             
6823: C0         RET     NZ              
6824: FF         RST     0X38            
6825: 87         ADD     A,A             
6826: F8 88      LDHL    SP,$88          
6828: F0 90      LD      A,($90)         
682A: F0 90      LD      A,($90)         
682C: F2         ???                     
682D: 90         SUB     B               
682E: F0 90      LD      A,($90)         
6830: FC         ???                     
6831: FF         RST     0X38            
6832: FE 03      CP      $03             
6834: FF         RST     0X38            
6835: E1         POP     HL              
6836: 1F         RRA                     
6837: 11 4F 09   LD      DE,$094F        
683A: 0F         RRCA                    
683B: 09         ADD     HL,BC           
683C: 0F         RRCA                    
683D: 09         ADD     HL,BC           
683E: 0F         RRCA                    
683F: 09         ADD     HL,BC           
6840: 00         NOP                     
6841: 00         NOP                     
6842: 00         NOP                     
6843: 00         NOP                     
6844: 10 00      STOP    $00             
6846: 03         INC     BC              
6847: 03         INC     BC              
6848: 07         RLCA                    
6849: 04         INC     B               
684A: 0F         RRCA                    
684B: 08 0F 08   LD      ($080F),SP      
684E: 0F         RRCA                    
684F: 09         ADD     HL,BC           
6850: 00         NOP                     
6851: 00         NOP                     
6852: 00         NOP                     
6853: 00         NOP                     
6854: 00         NOP                     
6855: 00         NOP                     
6856: C0         RET     NZ              
6857: C0         RET     NZ              
6858: E2         LDFF00  (C),A           
6859: 20 F0      JR      NZ,$684B        
685B: 10 F0      STOP    $F0             
685D: 10 F0      STOP    $F0             
685F: 90         SUB     B               
6860: 00         NOP                     
6861: 00         NOP                     
6862: 18 18      JR      $687C           
6864: 24         INC     H               
6865: 24         INC     H               
6866: 33         INC     SP              
6867: 23         INC     HL              
6868: 38 20      JR      C,$688A         
686A: 70         LD      (HL),B          
686B: 40         LD      B,B             
686C: 6C         LD      L,H             
686D: 4C         LD      C,H             
686E: E4         ???                     
686F: 84         ADD     A,H             
6870: 00         NOP                     
6871: 00         NOP                     
6872: 38 38      JR      C,$68AC         
6874: 58         LD      E,B             
6875: 48         LD      C,B             
6876: B8         CP      B               
6877: 88         ADC     A,B             
6878: 1C         INC     E               
6879: 04         INC     B               
687A: 0E 02      LD      C,$02           
687C: 6E         LD      L,(HL)          
687D: 62         LD      H,D             
687E: 4F         LD      C,A             
687F: 41         LD      B,C             
6880: F0 90      LD      A,($90)         
6882: F2         ???                     
6883: 90         SUB     B               
6884: F0 90      LD      A,($90)         
6886: F0 90      LD      A,($90)         
6888: F0 90      LD      A,($90)         
688A: F1         POP     AF              
688B: 90         SUB     B               
688C: F0 90      LD      A,($90)         
688E: F0 90      LD      A,($90)         
6890: FF         RST     0X38            
6891: FF         RST     0X38            
6892: FF         RST     0X38            
6893: 00         NOP                     
6894: FF         RST     0X38            
6895: FF         RST     0X38            
6896: 00         NOP                     
6897: 00         NOP                     
6898: 00         NOP                     
6899: 00         NOP                     
689A: 10 00      STOP    $00             
689C: 04         INC     B               
689D: 00         NOP                     
689E: 00         NOP                     
689F: 00         NOP                     
68A0: FF         RST     0X38            
68A1: FF         RST     0X38            
68A2: 81         ADD     A,C             
68A3: 81         ADD     A,C             
68A4: BD         CP      L               
68A5: 81         ADD     A,C             
68A6: BD         CP      L               
68A7: 81         ADD     A,C             
68A8: 81         ADD     A,C             
68A9: 81         ADD     A,C             
68AA: FF         RST     0X38            
68AB: FF         RST     0X38            
68AC: DB         ???                     
68AD: DB         ???                     
68AE: FF         RST     0X38            
68AF: FF         RST     0X38            
68B0: FF         RST     0X38            
68B1: 00         NOP                     
68B2: 04         INC     B               
68B3: FB         EI                      
68B4: 04         INC     B               
68B5: FB         EI                      
68B6: 04         INC     B               
68B7: FB         EI                      
68B8: FF         RST     0X38            
68B9: 00         NOP                     
68BA: 80         ADD     A,B             
68BB: 7F         LD      A,A             
68BC: 80         ADD     A,B             
68BD: 7F         LD      A,A             
68BE: 80         ADD     A,B             
68BF: 7F         LD      A,A             
68C0: FF         RST     0X38            
68C1: 87         ADD     A,A             
68C2: FF         RST     0X38            
68C3: F8 FF      LDHL    SP,$FF          
68C5: 80         ADD     A,B             
68C6: F8 C7      LDHL    SP,$C7          
68C8: C7         RST     0X00            
68C9: 78         LD      A,B             
68CA: FF         RST     0X38            
68CB: 43         LD      B,E             
68CC: FF         RST     0X38            
68CD: FE FF      CP      $FF             
68CF: 80         ADD     A,B             
68D0: FF         RST     0X38            
68D1: E1         POP     HL              
68D2: FF         RST     0X38            
68D3: 1F         RRA                     
68D4: FF         RST     0X38            
68D5: 01 79 87   LD      BC,$8779        
68D8: CF         RST     0X08            
68D9: 31 FF FF   LD      SP,$FFFF        
68DC: FF         RST     0X38            
68DD: 02         LD      (BC),A          
68DE: E3         ???                     
68DF: 1E 00      LD      E,$00           
68E1: 00         NOP                     
68E2: 80         ADD     A,B             
68E3: 00         NOP                     
68E4: 80         ADD     A,B             
68E5: 00         NOP                     
68E6: 80         ADD     A,B             
68E7: 00         NOP                     
68E8: 80         ADD     A,B             
68E9: 00         NOP                     
68EA: 80         ADD     A,B             
68EB: 00         NOP                     
68EC: 80         ADD     A,B             
68ED: 00         NOP                     
68EE: 7E         LD      A,(HL)          
68EF: 00         NOP                     
68F0: BF         CP      A               
68F1: 40         LD      B,B             
68F2: DF         RST     0X18            
68F3: 20 EF      JR      NZ,$68E4        
68F5: 10 F7      STOP    $F7             
68F7: 08 EB 14   LD      ($14EB),SP      
68FA: DD         ???                     
68FB: 22         LD      (HLI),A         
68FC: BE         CP      (HL)            
68FD: 41         LD      B,C             
68FE: 7F         LD      A,A             
68FF: 80         ADD     A,B             
6900: CF         RST     0X08            
6901: F0 A0      LD      A,($A0)         
6903: BF         CP      A               
6904: 9F         SBC     A               
6905: DF         RST     0X18            
6906: 80         ADD     A,B             
6907: E0 80      LDFF00  ($80),A         
6909: FF         RST     0X38            
690A: C0         RET     NZ              
690B: FF         RST     0X38            
690C: FF         RST     0X38            
690D: 7F         LD      A,A             
690E: FF         RST     0X38            
690F: 3F         CCF                     
6910: F3         DI                      
6911: 0F         RRCA                    
6912: 05         DEC     B               
6913: FD         ???                     
6914: F9         LD      SP,HL           
6915: FB         EI                      
6916: 01 07 01   LD      BC,$0107        
6919: FF         RST     0X38            
691A: 03         INC     BC              
691B: FF         RST     0X38            
691C: FF         RST     0X38            
691D: FE FF      CP      $FF             
691F: FC         ???                     
6920: F0 90      LD      A,($90)         
6922: F8 88      LDHL    SP,$88          
6924: FC         ???                     
6925: 84         ADD     A,H             
6926: FF         RST     0X38            
6927: 83         ADD     A,E             
6928: FF         RST     0X38            
6929: 80         ADD     A,B             
692A: FF         RST     0X38            
692B: C0         RET     NZ              
692C: BF         CP      A               
692D: E0 9F      LDFF00  ($9F),A         
692F: FF         RST     0X38            
6930: 0F         RRCA                    
6931: 09         ADD     HL,BC           
6932: 1F         RRA                     
6933: 11 3F 21   LD      DE,$213F        
6936: FF         RST     0X38            
6937: C1         POP     BC              
6938: FF         RST     0X38            
6939: 01 FF 03   LD      BC,$03FF        
693C: FD         ???                     
693D: 07         RLCA                    
693E: F9         LD      SP,HL           
693F: FF         RST     0X38            
6940: 0F         RRCA                    
6941: 09         ADD     HL,BC           
6942: 07         RLCA                    
6943: 04         INC     B               
6944: 43         LD      B,E             
6945: 03         INC     BC              
6946: 00         NOP                     
6947: 00         NOP                     
6948: 00         NOP                     
6949: 00         NOP                     
694A: 21 00 00   LD      HL,$0000        
694D: 00         NOP                     
694E: 00         NOP                     
694F: 00         NOP                     
6950: F0 90      LD      A,($90)         
6952: E0 20      LDFF00  ($20),A         
6954: C0         RET     NZ              
6955: C0         RET     NZ              
6956: 04         INC     B               
6957: 00         NOP                     
6958: 00         NOP                     
6959: 00         NOP                     
695A: 04         INC     B               
695B: 00         NOP                     
695C: 00         NOP                     
695D: 00         NOP                     
695E: 00         NOP                     
695F: 00         NOP                     
6960: EB         ???                     
6961: 8B         ADC     A,E             
6962: CE AA      ADC     $AA             
6964: E4         ???                     
6965: A4         AND     H               
6966: E4         ???                     
6967: A4         AND     H               
6968: EE AE      XOR     $AE             
696A: F9         LD      SP,HL           
696B: 99         SBC     C               
696C: 79         LD      A,C             
696D: 48         LD      C,B             
696E: 7F         LD      A,A             
696F: 48         LD      C,B             
6970: 1F         RRA                     
6971: 01 37 09   LD      BC,$0937        
6974: 3F         CCF                     
6975: 09         ADD     HL,BC           
6976: 3F         CCF                     
6977: 09         ADD     HL,BC           
6978: 7F         LD      A,A             
6979: 19         ADD     HL,DE           
697A: FF         RST     0X38            
697B: E1         POP     HL              
697C: FE 22      CP      $22             
697E: FE 46      CP      $46             
6980: 0F         RRCA                    
6981: 09         ADD     HL,BC           
6982: 0F         RRCA                    
6983: 09         ADD     HL,BC           
6984: 2F         CPL                     
6985: 09         ADD     HL,BC           
6986: 0F         RRCA                    
6987: 09         ADD     HL,BC           
6988: 0F         RRCA                    
6989: 09         ADD     HL,BC           
698A: 0F         RRCA                    
698B: 09         ADD     HL,BC           
698C: 0F         RRCA                    
698D: 09         ADD     HL,BC           
698E: 0F         RRCA                    
698F: 09         ADD     HL,BC           
6990: 00         NOP                     
6991: 00         NOP                     
6992: 10 00      STOP    $00             
6994: 00         NOP                     
6995: 00         NOP                     
6996: FF         RST     0X38            
6997: FF         RST     0X38            
6998: FF         RST     0X38            
6999: 00         NOP                     
699A: FF         RST     0X38            
699B: 00         NOP                     
699C: FF         RST     0X38            
699D: 00         NOP                     
699E: FF         RST     0X38            
699F: FF         RST     0X38            
69A0: DB         ???                     
69A1: A5         AND     L               
69A2: DF         RST     0X18            
69A3: A1         AND     C               
69A4: D7         RST     0X10            
69A5: A9         XOR     C               
69A6: F7         RST     0X30            
69A7: 89         ADC     A,C             
69A8: 81         ADD     A,C             
69A9: 81         ADD     A,C             
69AA: FF         RST     0X38            
69AB: FF         RST     0X38            
69AC: DB         ???                     
69AD: DB         ???                     
69AE: FF         RST     0X38            
69AF: FF         RST     0X38            
69B0: FF         RST     0X38            
69B1: 00         NOP                     
69B2: 00         NOP                     
69B3: FF         RST     0X38            
69B4: FF         RST     0X38            
69B5: FF         RST     0X38            
69B6: 00         NOP                     
69B7: 00         NOP                     
69B8: 00         NOP                     
69B9: FF         RST     0X38            
69BA: 00         NOP                     
69BB: FF         RST     0X38            
69BC: FF         RST     0X38            
69BD: FF         RST     0X38            
69BE: FF         RST     0X38            
69BF: FF         RST     0X38            
69C0: 87         ADD     A,A             
69C1: F8 FF      LDHL    SP,$FF          
69C3: C1         POP     BC              
69C4: FE 7F      CP      $7F             
69C6: FF         RST     0X38            
69C7: 41         LD      B,C             
69C8: 8F         ADC     A,A             
69C9: F0 FC      LD      A,($FC)         
69CB: 83         ADD     A,E             
69CC: FF         RST     0X38            
69CD: FC         ???                     
69CE: FF         RST     0X38            
69CF: C3 FF 01   JP      $01FF           
69D2: FF         RST     0X38            
69D3: F1         POP     AF              
69D4: EF         RST     0X28            
69D5: 1E FF      LD      E,$FF           
69D7: F1         POP     AF              
69D8: FF         RST     0X38            
69D9: 01 73 8F   LD      BC,$8F73        
69DC: FF         RST     0X38            
69DD: 01 FF FF   LD      BC,$FFFF        
69E0: FF         RST     0X38            
69E1: FF         RST     0X38            
69E2: 81         ADD     A,C             
69E3: 81         ADD     A,C             
69E4: CB B5      SET     1,E             
69E6: CB B5      SET     1,E             
69E8: DB         ???                     
69E9: A5         AND     L               
69EA: E7         RST     0X20            
69EB: 99         SBC     C               
69EC: C3 BD FF   JP      $FFBD           
69EF: FF         RST     0X38            
69F0: FF         RST     0X38            
69F1: FF         RST     0X38            
69F2: FF         RST     0X38            
69F3: FF         RST     0X38            
69F4: 55         LD      D,L             
69F5: FF         RST     0X38            
69F6: 00         NOP                     
69F7: FF         RST     0X38            
69F8: AA         XOR     D               
69F9: 55         LD      D,L             
69FA: FF         RST     0X38            
69FB: 00         NOP                     
69FC: 00         NOP                     
69FD: 00         NOP                     
69FE: FF         RST     0X38            
69FF: FF         RST     0X38            
6A00: 3F         CCF                     
6A01: 3F         CCF                     
6A02: 40         LD      B,B             
6A03: 40         LD      B,B             
6A04: 90         SUB     B               
6A05: 8F         ADC     A,A             
6A06: AF         XOR     A               
6A07: 9F         SBC     A               
6A08: 9B         SBC     E               
6A09: B4         OR      H               
6A0A: BF         CP      A               
6A0B: A0         AND     B               
6A0C: B6         OR      (HL)            
6A0D: A9         XOR     C               
6A0E: BF         CP      A               
6A0F: A0         AND     B               
6A10: F8 F8      LDHL    SP,$F8          
6A12: 04         INC     B               
6A13: 04         INC     B               
6A14: 12         LD      (DE),A          
6A15: E2         LDFF00  (C),A           
6A16: EA F2 72   LD      ($72F2),A       
6A19: 9A         SBC     D               
6A1A: EA 1A FA   LD      ($FA1A),A       
6A1D: 0A         LD      A,(BC)          
6A1E: BA         CP      D               
6A1F: 4A         LD      C,D             
6A20: 2E 30      LD      L,$30           
6A22: 24         INC     H               
6A23: 38 24      JR      C,$6A49         
6A25: 38 2E      JR      C,$6A55         
6A27: 30 6E      JR      NC,$6A97        
6A29: 70         LD      (HL),B          
6A2A: E4         ???                     
6A2B: B8         CP      B               
6A2C: A4         AND     H               
6A2D: B8         CP      B               
6A2E: AC         XOR     H               
6A2F: B0         OR      B               
6A30: 28 18      JR      Z,$6A4A         
6A32: 68         LD      L,B             
6A33: 18 48      JR      $6A7D           
6A35: 38 48      JR      C,$6A7F         
6A37: 38 6C      JR      C,$6AA5         
6A39: 1C         INC     E               
6A3A: 2E 1A      LD      L,$1A           
6A3C: 0A         LD      A,(BC)          
6A3D: 3A         LD      A,(HLD)         
6A3E: 4A         LD      C,D             
6A3F: 3A         LD      A,(HLD)         
6A40: CE 9A      ADC     $9A             
6A42: D6 8E      SUB     $8E             
6A44: FA BE C6   LD      A,($C6BE)       
6A47: C6 AA      ADD     $AA             
6A49: 82         ADD     A,D             
6A4A: AB         XOR     E               
6A4B: AA         XOR     D               
6A4C: AB         XOR     E               
6A4D: AB         XOR     E               
6A4E: EE AB      XOR     $AB             
6A50: 73         LD      (HL),E          
6A51: 59         LD      E,C             
6A52: 6B         LD      L,E             
6A53: 71         LD      (HL),C          
6A54: 5F         LD      E,A             
6A55: 7D         LD      A,L             
6A56: 63         LD      H,E             
6A57: 63         LD      H,E             
6A58: 55         LD      D,L             
6A59: 41         LD      B,C             
6A5A: D5         PUSH    DE              
6A5B: 55         LD      D,L             
6A5C: D5         PUSH    DE              
6A5D: D5         PUSH    DE              
6A5E: 77         LD      (HL),A          
6A5F: D5         PUSH    DE              
6A60: 3B         DEC     SP              
6A61: 3B         DEC     SP              
6A62: 3E 24      LD      A,$24           
6A64: 1F         RRA                     
6A65: 19         ADD     HL,DE           
6A66: 0F         RRCA                    
6A67: 0B         DEC     BC              
6A68: 1F         RRA                     
6A69: 1B         DEC     DE              
6A6A: FF         RST     0X38            
6A6B: FF         RST     0X38            
6A6C: 87         ADD     A,A             
6A6D: 82         ADD     A,D             
6A6E: AF         XOR     A               
6A6F: AB         XOR     E               
6A70: DC DC 7C   CALL    C,$7CDC         
6A73: 24         INC     H               
6A74: FE 9E      CP      $9E             
6A76: F5         PUSH    AF              
6A77: D5         PUSH    DE              
6A78: F5         PUSH    AF              
6A79: D5         PUSH    DE              
6A7A: FD         ???                     
6A7B: 9D         SBC     L               
6A7C: FD         ???                     
6A7D: 35         DEC     (HL)            
6A7E: FF         RST     0X38            
6A7F: CF         RST     0X08            
6A80: 8F         ADC     A,A             
6A81: 86         ADD     A,(HL)          
6A82: E6 80      AND     $80             
6A84: F2         ???                     
6A85: E0 D8      LDFF00  ($D8),A         
6A87: F0 BC      LD      A,($BC)         
6A89: D8         RET     C               
6A8A: F6 94      OR      $94             
6A8C: D2 92 DA   JP      NC,$DA92        
6A8F: 92         SUB     D               
6A90: FF         RST     0X38            
6A91: FF         RST     0X38            
6A92: FF         RST     0X38            
6A93: 81         ADD     A,C             
6A94: BD         CP      L               
6A95: FF         RST     0X38            
6A96: 81         ADD     A,C             
6A97: FF         RST     0X38            
6A98: FF         RST     0X38            
6A99: FF         RST     0X38            
6A9A: FF         RST     0X38            
6A9B: 81         ADD     A,C             
6A9C: BD         CP      L               
6A9D: FF         RST     0X38            
6A9E: 81         ADD     A,C             
6A9F: FF         RST     0X38            
6AA0: 3C         INC     A               
6AA1: 3C         INC     A               
6AA2: 5E         LD      E,(HL)          
6AA3: 62         LD      H,D             
6AA4: 83         ADD     A,E             
6AA5: FD         ???                     
6AA6: 81         ADD     A,C             
6AA7: E2         LDFF00  (C),A           
6AA8: 98         SBC     B               
6AA9: D9         RETI                    
6AAA: 98         SBC     B               
6AAB: D9         RETI                    
6AAC: A2         AND     D               
6AAD: C1         POP     BC              
6AAE: BE         CP      (HL)            
6AAF: E3         ???                     
6AB0: 3C         INC     A               
6AB1: 3C         INC     A               
6AB2: 7A         LD      A,D             
6AB3: 46         LD      B,(HL)          
6AB4: C1         POP     BC              
6AB5: BF         CP      A               
6AB6: 81         ADD     A,C             
6AB7: 47         LD      B,A             
6AB8: 19         ADD     HL,DE           
6AB9: 9B         SBC     E               
6ABA: 19         ADD     HL,DE           
6ABB: 9B         SBC     E               
6ABC: 45         LD      B,L             
6ABD: 83         ADD     A,E             
6ABE: 7D         LD      A,L             
6ABF: C7         RST     0X00            
6AC0: 00         NOP                     
6AC1: 00         NOP                     
6AC2: 3D         DEC     A               
6AC3: 00         NOP                     
6AC4: 45         LD      B,L             
6AC5: 00         NOP                     
6AC6: 45         LD      B,L             
6AC7: 00         NOP                     
6AC8: 48         LD      C,B             
6AC9: 00         NOP                     
6ACA: 57         LD      D,A             
6ACB: 00         NOP                     
6ACC: 68         LD      L,B             
6ACD: 00         NOP                     
6ACE: 08 00 00   LD      ($0000),SP      
6AD1: 00         NOP                     
6AD2: FC         ???                     
6AD3: 00         NOP                     
6AD4: 02         LD      (BC),A          
6AD5: 00         NOP                     
6AD6: 82         ADD     A,D             
6AD7: 00         NOP                     
6AD8: 72         LD      (HL),D          
6AD9: 00         NOP                     
6ADA: 0E 00      LD      C,$00           
6ADC: E0 00      LDFF00  ($00),A         
6ADE: 2E 00      LD      L,$00           
6AE0: 00         NOP                     
6AE1: FF         RST     0X38            
6AE2: 31 8E 3F   LD      SP,$3F8E        
6AE5: 80         ADD     A,B             
6AE6: 1F         RRA                     
6AE7: 80         ADD     A,B             
6AE8: 1F         RRA                     
6AE9: 80         ADD     A,B             
6AEA: 1F         RRA                     
6AEB: 80         ADD     A,B             
6AEC: 3C         INC     A               
6AED: 80         ADD     A,B             
6AEE: 00         NOP                     
6AEF: 83         ADD     A,E             
6AF0: 00         NOP                     
6AF1: FF         RST     0X38            
6AF2: FE 01      CP      $01             
6AF4: FE 01      CP      $01             
6AF6: DE 21      SBC     $21             
6AF8: DE 01      SBC     $01             
6AFA: FE 01      CP      $01             
6AFC: 7E         LD      A,(HL)          
6AFD: 01 00 81   LD      BC,$8100        
6B00: 8D         ADC     A,L             
6B01: 92         SUB     D               
6B02: C0         RET     NZ              
6B03: 8F         ADC     A,A             
6B04: A0         AND     B               
6B05: C0         RET     NZ              
6B06: 5F         LD      E,A             
6B07: 60         LD      H,B             
6B08: 20 3F      JR      NZ,$6B49        
6B0A: 3F         CCF                     
6B0B: 3F         CCF                     
6B0C: 27         DAA                     
6B0D: 38 26      JR      C,$6B35         
6B0F: 38 E2      JR      C,$6AF3         
6B11: 12         LD      (DE),A          
6B12: 06 E2      LD      B,$E2           
6B14: 0A         LD      A,(BC)          
6B15: 06 F4      LD      B,$F4           
6B17: 0C         INC     C               
6B18: 08 F8 F8   LD      ($F8F8),SP      
6B1B: F8 C8      LDHL    SP,$C8          
6B1D: 38 48      JR      C,$6B67         
6B1F: 38 AE      JR      C,$6ACF         
6B21: B0         OR      B               
6B22: A6         AND     (HL)            
6B23: B8         CP      B               
6B24: B4         OR      H               
6B25: 98         SBC     B               
6B26: DF         RST     0X18            
6B27: 8F         ADC     A,A             
6B28: A0         AND     B               
6B29: C0         RET     NZ              
6B2A: 5F         LD      E,A             
6B2B: 60         LD      H,B             
6B2C: 3F         CCF                     
6B2D: 3F         CCF                     
6B2E: 00         NOP                     
6B2F: 00         NOP                     
6B30: 6A         LD      L,D             
6B31: 1A         LD      A,(DE)          
6B32: 2A         LD      A,(HLI)         
6B33: 1A         LD      A,(DE)          
6B34: 1A         LD      A,(DE)          
6B35: 32         LD      (HLD),A         
6B36: F6 E2      OR      $E2             
6B38: 0A         LD      A,(BC)          
6B39: 06 F4      LD      B,$F4           
6B3B: 0C         INC     C               
6B3C: F8 F8      LDHL    SP,$F8          
6B3E: 00         NOP                     
6B3F: 00         NOP                     
6B40: FE AB      CP      $AB             
6B42: FF         RST     0X38            
6B43: AF         XOR     A               
6B44: FC         ???                     
6B45: FF         RST     0X38            
6B46: FD         ???                     
6B47: C7         RST     0X00            
6B48: CE 87      ADC     $87             
6B4A: 8B         ADC     A,E             
6B4B: 87         ADD     A,A             
6B4C: 97         SUB     A               
6B4D: 8C         ADC     A,H             
6B4E: F8 F8      LDHL    SP,$F8          
6B50: 7F         LD      A,A             
6B51: D5         PUSH    DE              
6B52: FF         RST     0X38            
6B53: F7         RST     0X30            
6B54: 3F         CCF                     
6B55: FF         RST     0X38            
6B56: BF         CP      A               
6B57: E3         ???                     
6B58: 73         LD      (HL),E          
6B59: E1         POP     HL              
6B5A: D1         POP     DE              
6B5B: E1         POP     HL              
6B5C: E9         JP      (HL)            
6B5D: 31 1F 1F   LD      SP,$1F1F        
6B60: 87         ADD     A,A             
6B61: 82         ADD     A,D             
6B62: 87         ADD     A,A             
6B63: 83         ADD     A,E             
6B64: AF         XOR     A               
6B65: AB         XOR     E               
6B66: 87         ADD     A,A             
6B67: 83         ADD     A,E             
6B68: 87         ADD     A,A             
6B69: 82         ADD     A,D             
6B6A: AF         XOR     A               
6B6B: AB         XOR     E               
6B6C: FF         RST     0X38            
6B6D: 83         ADD     A,E             
6B6E: FF         RST     0X38            
6B6F: FF         RST     0X38            
6B70: D9         RETI                    
6B71: 09         ADD     HL,BC           
6B72: FD         ???                     
6B73: 89         ADC     A,C             
6B74: F9         LD      SP,HL           
6B75: F9         LD      SP,HL           
6B76: FF         RST     0X38            
6B77: 8F         ADC     A,A             
6B78: FD         ???                     
6B79: 05         DEC     B               
6B7A: FD         ???                     
6B7B: FD         ???                     
6B7C: FE 86      CP      $86             
6B7E: FC         ???                     
6B7F: FC         ???                     
6B80: F1         POP     AF              
6B81: 61         LD      H,C             
6B82: 67         LD      H,A             
6B83: 01 4F 07   LD      BC,$074F        
6B86: 1B         DEC     DE              
6B87: 0F         RRCA                    
6B88: 3D         DEC     A               
6B89: 1B         DEC     DE              
6B8A: 6F         LD      L,A             
6B8B: 29         ADD     HL,HL           
6B8C: 4B         LD      C,E             
6B8D: 49         LD      C,C             
6B8E: 5B         LD      E,E             
6B8F: 49         LD      C,C             
6B90: FF         RST     0X38            
6B91: FF         RST     0X38            
6B92: FF         RST     0X38            
6B93: 81         ADD     A,C             
6B94: FF         RST     0X38            
6B95: 81         ADD     A,C             
6B96: 81         ADD     A,C             
6B97: 81         ADD     A,C             
6B98: 81         ADD     A,C             
6B99: 81         ADD     A,C             
6B9A: 81         ADD     A,C             
6B9B: FF         RST     0X38            
6B9C: 99         SBC     C               
6B9D: FF         RST     0X38            
6B9E: FF         RST     0X38            
6B9F: FF         RST     0X38            
6BA0: 9C         SBC     H               
6BA1: FF         RST     0X38            
6BA2: 40         LD      B,B             
6BA3: 7C         LD      A,H             
6BA4: 63         LD      H,E             
6BA5: 7B         LD      A,E             
6BA6: 7B         LD      A,E             
6BA7: 5B         LD      E,E             
6BA8: 79         LD      A,C             
6BA9: 49         LD      C,C             
6BAA: 5D         LD      E,L             
6BAB: 65         LD      H,L             
6BAC: 64         LD      H,H             
6BAD: 3C         INC     A               
6BAE: 3F         CCF                     
6BAF: 1F         RRA                     
6BB0: 39         ADD     HL,SP           
6BB1: FF         RST     0X38            
6BB2: 02         LD      (BC),A          
6BB3: 3E C6      LD      A,$C6           
6BB5: DE DE      SBC     $DE             
6BB7: DA 9E 92   JP      C,$929E         
6BBA: BA         CP      D               
6BBB: A6         AND     (HL)            
6BBC: 26 3C      LD      H,$3C           
6BBE: FC         ???                     
6BBF: F8 6C      LDHL    SP,$6C          
6BC1: 00         NOP                     
6BC2: 57         LD      D,A             
6BC3: 00         NOP                     
6BC4: 48         LD      C,B             
6BC5: 00         NOP                     
6BC6: 46         LD      B,(HL)          
6BC7: 00         NOP                     
6BC8: 42         LD      B,D             
6BC9: 00         NOP                     
6BCA: 42         LD      B,D             
6BCB: 00         NOP                     
6BCC: 3E 00      LD      A,$00           
6BCE: 00         NOP                     
6BCF: 00         NOP                     
6BD0: 2A         LD      A,(HLI)         
6BD1: 00         NOP                     
6BD2: EA 00 0A   LD      ($0A00),A       
6BD5: 00         NOP                     
6BD6: E6 00      AND     $00             
6BD8: 98         SBC     B               
6BD9: 00         NOP                     
6BDA: 84         ADD     A,H             
6BDB: 00         NOP                     
6BDC: FC         ???                     
6BDD: 00         NOP                     
6BDE: 00         NOP                     
6BDF: 00         NOP                     
6BE0: 00         NOP                     
6BE1: 00         NOP                     
6BE2: FF         RST     0X38            
6BE3: 00         NOP                     
6BE4: FF         RST     0X38            
6BE5: FF         RST     0X38            
6BE6: 7E         LD      A,(HL)          
6BE7: 81         ADD     A,C             
6BE8: 7E         LD      A,(HL)          
6BE9: 81         ADD     A,C             
6BEA: 00         NOP                     
6BEB: FF         RST     0X38            
6BEC: FF         RST     0X38            
6BED: FF         RST     0X38            
6BEE: FF         RST     0X38            
6BEF: FF         RST     0X38            
6BF0: FF         RST     0X38            
6BF1: FF         RST     0X38            
6BF2: 83         ADD     A,E             
6BF3: FF         RST     0X38            
6BF4: 01 FF FE   LD      BC,$FEFF        
6BF7: 01 00 01   LD      BC,$0100        
6BFA: 01 00 81   LD      BC,$8100        
6BFD: 00         NOP                     
6BFE: 7F         LD      A,A             
6BFF: 00         NOP                     
6C00: FD         ???                     
6C01: 1D         DEC     E               
6C02: E2         LDFF00  (C),A           
6C03: 3F         CCF                     
6C04: CD 73 E6   CALL    $E673           
6C07: 7A         LD      A,D             
6C08: F3         DI                      
6C09: 1E E7      LD      E,$E7           
6C0B: 3D         DEC     A               
6C0C: D7         RST     0X10            
6C0D: 6C         LD      L,H             
6C0E: A3         AND     E               
6C0F: DF         RST     0X18            
6C10: DF         RST     0X18            
6C11: D8         RET     C               
6C12: 27         DAA                     
6C13: FC         ???                     
6C14: B3         OR      E               
6C15: CE 4D      ADC     $4D             
6C17: 7F         LD      A,A             
6C18: DF         RST     0X18            
6C19: 73         LD      (HL),E          
6C1A: EF         RST     0X28            
6C1B: BC         CP      H               
6C1C: EB         ???                     
6C1D: 36 C5      LD      (HL),$C5        
6C1F: FB         EI                      
6C20: EF         RST     0X28            
6C21: 3E FF      LD      A,$FF           
6C23: 19         ADD     HL,DE           
6C24: CE 08      ADC     $08             
6C26: 8F         ADC     A,A             
6C27: 0C         INC     C               
6C28: 8F         ADC     A,A             
6C29: 0A         LD      A,(BC)          
6C2A: 0F         RRCA                    
6C2B: 09         ADD     HL,BC           
6C2C: 1E 18      LD      E,$18           
6C2E: 37         SCF                     
6C2F: 24         INC     H               
6C30: F5         PUSH    AF              
6C31: 7C         LD      A,H             
6C32: FB         EI                      
6C33: 98         SBC     B               
6C34: 77         LD      (HL),A          
6C35: 10 F7      STOP    $F7             
6C37: 30 FF      JR      NC,$6C38        
6C39: 50         LD      D,B             
6C3A: FF         RST     0X38            
6C3B: 90         SUB     B               
6C3C: 7F         LD      A,A             
6C3D: 18 FF      JR      $6C3E           
6C3F: 2C         INC     L               
6C40: FF         RST     0X38            
6C41: 0F         RRCA                    
6C42: F0 10      LD      A,($10)         
6C44: F0 20      LD      A,($20)         
6C46: F0 20      LD      A,($20)         
6C48: CB 40      SET     1,E             
6C4A: DC 40 F0   CALL    C,$F040         
6C4D: 80         ADD     A,B             
6C4E: 89         ADC     A,C             
6C4F: 90         SUB     B               
6C50: E1         POP     HL              
6C51: E0 39      LDFF00  ($39),A         
6C53: 18 3C      JR      $6C91           
6C55: 04         INC     B               
6C56: 26 02      LD      H,$02           
6C58: 2B         DEC     HL              
6C59: 09         ADD     HL,BC           
6C5A: CF         RST     0X08            
6C5B: 0D         DEC     C               
6C5C: 47         LD      B,A             
6C5D: 05         DEC     B               
6C5E: A6         AND     (HL)            
6C5F: 43         LD      B,E             
6C60: B2         OR      D               
6C61: 66         LD      H,(HL)          
6C62: F2         ???                     
6C63: 26 E2      LD      H,$E2           
6C65: 26 E2      LD      H,$E2           
6C67: 26 E0      LD      H,$E0           
6C69: 26 E0      LD      H,$E0           
6C6B: 26 E0      LD      H,$E0           
6C6D: 46         LD      B,(HL)          
6C6E: C6 80      ADD     $80             
6C70: 3B         DEC     SP              
6C71: 46         LD      B,(HL)          
6C72: 5F         LD      E,A             
6C73: 3C         INC     A               
6C74: 6F         LD      L,A             
6C75: 33         INC     SP              
6C76: 7D         LD      A,L             
6C77: 25         DEC     H               
6C78: 7F         LD      A,A             
6C79: 25         DEC     H               
6C7A: 3F         CCF                     
6C7B: 13         INC     DE              
6C7C: 18 08      JR      $6C86           
6C7E: 14         INC     D               
6C7F: 0C         INC     C               
6C80: FE 0E      CP      $0E             
6C82: F1         POP     AF              
6C83: 11 E8 28   LD      DE,$28E8        
6C86: DB         ???                     
6C87: 5B         LD      E,E             
6C88: D3         ???                     
6C89: 53         LD      D,E             
6C8A: C3 43 83   JP      $8343           
6C8D: 93         SUB     E               
6C8E: 81         ADD     A,C             
6C8F: 80         ADD     A,B             
6C90: 03         INC     BC              
6C91: 03         INC     BC              
6C92: 85         ADD     A,L             
6C93: 85         ADD     A,L             
6C94: 4B         LD      C,E             
6C95: 4A         LD      C,D             
6C96: 2F         CPL                     
6C97: 2E AF      LD      L,$AF           
6C99: A0         AND     B               
6C9A: AF         XOR     A               
6C9B: AC         XOR     H               
6C9C: FA 2A FD   LD      A,($FD2A)       
6C9F: 45         LD      B,L             
6CA0: F0 00      LD      A,($00)         
6CA2: C3 03 87   JP      $8703           
6CA5: 04         INC     B               
6CA6: 8E         ADC     A,(HL)          
6CA7: 08 3E 38   LD      ($383E),SP      
6CAA: 2D         DEC     L               
6CAB: 2A         LD      A,(HLI)         
6CAC: 1D         DEC     E               
6CAD: 1B         DEC     DE              
6CAE: 0A         LD      A,(BC)          
6CAF: 0E 01      LD      C,$01           
6CB1: 00         NOP                     
6CB2: C3 C0 E3   JP      $E3C0           
6CB5: 20 77      JR      NZ,$6D2E        
6CB7: 10 7F      STOP    $7F             
6CB9: 1C         INC     E               
6CBA: B7         OR      A               
6CBB: 54         LD      D,H             
6CBC: BF         CP      A               
6CBD: D8         RET     C               
6CBE: 5E         LD      E,(HL)          
6CBF: 70         LD      (HL),B          
6CC0: F8 00      LDHL    SP,$00          
6CC2: E0 00      LDFF00  ($00),A         
6CC4: C0         RET     NZ              
6CC5: 00         NOP                     
6CC6: 80         ADD     A,B             
6CC7: 00         NOP                     
6CC8: 80         ADD     A,B             
6CC9: 00         NOP                     
6CCA: 00         NOP                     
6CCB: 00         NOP                     
6CCC: 00         NOP                     
6CCD: 00         NOP                     
6CCE: 00         NOP                     
6CCF: 00         NOP                     
6CD0: 01 00 03   LD      BC,$0300        
6CD3: 00         NOP                     
6CD4: 07         RLCA                    
6CD5: 00         NOP                     
6CD6: 07         RLCA                    
6CD7: 00         NOP                     
6CD8: 0F         RRCA                    
6CD9: 00         NOP                     
6CDA: 0F         RRCA                    
6CDB: 00         NOP                     
6CDC: 1F         RRA                     
6CDD: 00         NOP                     
6CDE: 1F         RRA                     
6CDF: 00         NOP                     
6CE0: 00         NOP                     
6CE1: 00         NOP                     
6CE2: 42         LD      B,D             
6CE3: 42         LD      B,D             
6CE4: 24         INC     H               
6CE5: 24         INC     H               
6CE6: 18 18      JR      $6D00           
6CE8: 18 18      JR      $6D02           
6CEA: 24         INC     H               
6CEB: 24         INC     H               
6CEC: 42         LD      B,D             
6CED: 42         LD      B,D             
6CEE: 00         NOP                     
6CEF: 00         NOP                     
6CF0: 00         NOP                     
6CF1: 00         NOP                     
6CF2: 42         LD      B,D             
6CF3: 42         LD      B,D             
6CF4: 24         INC     H               
6CF5: 24         INC     H               
6CF6: 18 18      JR      $6D10           
6CF8: 18 18      JR      $6D12           
6CFA: 24         INC     H               
6CFB: 24         INC     H               
6CFC: 42         LD      B,D             
6CFD: 42         LD      B,D             
6CFE: 00         NOP                     
6CFF: 00         NOP                     
6D00: 80         ADD     A,B             
6D01: FF         RST     0X38            
6D02: B4         OR      H               
6D03: FB         EI                      
6D04: D8         RET     C               
6D05: D7         RST     0X10            
6D06: 29         ADD     HL,HL           
6D07: 37         SCF                     
6D08: 21 3F 62   LD      HL,$623F        
6D0B: 3F         CCF                     
6D0C: E5         PUSH    HL              
6D0D: 3E E7      LD      A,$E7           
6D0F: 3C         INC     A               
6D10: 01 FF 2D   LD      BC,$2DFF        
6D13: DF         RST     0X18            
6D14: 1F         RRA                     
6D15: EB         ???                     
6D16: 9C         SBC     H               
6D17: E8 84      ADD     SP,$84          
6D19: FC         ???                     
6D1A: 44         LD      B,H             
6D1B: FC         ???                     
6D1C: A4         AND     H               
6D1D: 7C         LD      A,H             
6D1E: E4         ???                     
6D1F: 3C         INC     A               
6D20: 67         LD      H,A             
6D21: 45         LD      B,L             
6D22: 4F         LD      C,A             
6D23: 42         LD      B,D             
6D24: 76         HALT                    
6D25: 48         LD      C,B             
6D26: 3B         DEC     SP              
6D27: 3C         INC     A               
6D28: 1F         RRA                     
6D29: 04         INC     B               
6D2A: 3D         DEC     A               
6D2B: 06 7E      LD      B,$7E           
6D2D: 03         INC     BC              
6D2E: FF         RST     0X38            
6D2F: 01 FE A6   LD      BC,$A6FE        
6D32: FE 62      CP      $62             
6D34: EE 12      XOR     $12             
6D36: DC 3C FC   CALL    C,$FC3C         
6D39: 20 B8      JR      NZ,$6CF3        
6D3B: 60         LD      H,B             
6D3C: 60         LD      H,B             
6D3D: C0         RET     NZ              
6D3E: 80         ADD     A,B             
6D3F: 80         ADD     A,B             
6D40: B9         CP      C               
6D41: 99         SBC     C               
6D42: B9         CP      C               
6D43: B9         CP      C               
6D44: B9         CP      C               
6D45: BF         CP      A               
6D46: B9         CP      C               
6D47: B9         CP      C               
6D48: B9         CP      C               
6D49: B8         CP      B               
6D4A: D0         RET     NC              
6D4B: 90         SUB     B               
6D4C: F4         ???                     
6D4D: 96         SUB     (HL)            
6D4E: 76         HALT                    
6D4F: D6 F6      SUB     $F6             
6D51: E3         ???                     
6D52: FB         EI                      
6D53: F2         ???                     
6D54: FB         EI                      
6D55: FA FB F9   LD      A,($F9FB)       
6D58: FB         EI                      
6D59: F9         LD      SP,HL           
6D5A: FB         EI                      
6D5B: 71         LD      (HL),C          
6D5C: 73         LD      (HL),E          
6D5D: 01 05 03   LD      BC,$0305        
6D60: C0         RET     NZ              
6D61: 80         ADD     A,B             
6D62: E6 80      AND     $80             
6D64: 7F         LD      A,A             
6D65: 60         LD      H,B             
6D66: 5B         LD      E,E             
6D67: 56         LD      D,(HL)          
6D68: 4E         LD      C,(HL)          
6D69: 4F         LD      C,A             
6D6A: 6F         LD      L,A             
6D6B: 4F         LD      C,A             
6D6C: 68         LD      L,B             
6D6D: 2F         CPL                     
6D6E: FF         RST     0X38            
6D6F: 18 14      JR      $6D85           
6D71: 0C         INC     C               
6D72: 34         INC     (HL)            
6D73: 0C         INC     C               
6D74: E4         ???                     
6D75: 7C         LD      A,H             
6D76: D8         RET     C               
6D77: 98         SBC     B               
6D78: 92         SUB     D               
6D79: 92         SUB     D               
6D7A: B5         OR      L               
6D7B: 95         SUB     L               
6D7C: EF         RST     0X28            
6D7D: A9         XOR     C               
6D7E: C6 C6      ADD     $C6             
6D80: E7         RST     0X20            
6D81: E3         ???                     
6D82: 7F         LD      A,A             
6D83: 3C         INC     A               
6D84: 0F         RRCA                    
6D85: 00         NOP                     
6D86: E7         RST     0X20            
6D87: E7         RST     0X20            
6D88: B8         CP      B               
6D89: B8         CP      B               
6D8A: C7         RST     0X00            
6D8B: 87         ADD     A,A             
6D8C: 7F         LD      A,A             
6D8D: 58         LD      E,B             
6D8E: FF         RST     0X38            
6D8F: 70         LD      (HL),B          
6D90: FD         ???                     
6D91: 85         ADD     A,L             
6D92: FF         RST     0X38            
6D93: 1D         DEC     E               
6D94: F5         PUSH    AF              
6D95: 17         RLA                     
6D96: FA 0A FA   LD      A,($FA0A)       
6D99: 8A         ADC     A,D             
6D9A: FE 0A      CP      $0A             
6D9C: FE 12      CP      $12             
6D9E: 1C         INC     E               
6D9F: 1E 0D      LD      E,$0D           
6DA1: 0B         DEC     BC              
6DA2: 3D         DEC     A               
6DA3: 3A         LD      A,(HLD)         
6DA4: 2D         DEC     L               
6DA5: 2B         DEC     HL              
6DA6: 1A         LD      A,(DE)          
6DA7: 1E 0D      LD      E,$0D           
6DA9: 0B         DEC     BC              
6DAA: 1D         DEC     E               
6DAB: 0A         LD      A,(BC)          
6DAC: 3D         DEC     A               
6DAD: 06 7F      LD      B,$7F           
6DAF: 03         INC     BC              
6DB0: BE         CP      (HL)            
6DB1: D0         RET     NC              
6DB2: BE         CP      (HL)            
6DB3: 5C         LD      E,H             
6DB4: B4         OR      H               
6DB5: D4 58 78   CALL    NC,$7858        
6DB8: B8         CP      B               
6DB9: D0         RET     NC              
6DBA: B8         CP      B               
6DBB: 50         LD      D,B             
6DBC: B8         CP      B               
6DBD: 60         LD      H,B             
6DBE: E0 C0      LDFF00  ($C0),A         
6DC0: 00         NOP                     
6DC1: 00         NOP                     
6DC2: 00         NOP                     
6DC3: 00         NOP                     
6DC4: 00         NOP                     
6DC5: 00         NOP                     
6DC6: 03         INC     BC              
6DC7: 00         NOP                     
6DC8: 0F         RRCA                    
6DC9: 00         NOP                     
6DCA: 3F         CCF                     
6DCB: 00         NOP                     
6DCC: 7F         LD      A,A             
6DCD: 00         NOP                     
6DCE: FF         RST     0X38            
6DCF: 00         NOP                     
6DD0: 3E 00      LD      A,$00           
6DD2: 7E         LD      A,(HL)          
6DD3: 00         NOP                     
6DD4: FE 00      CP      $00             
6DD6: FC         ???                     
6DD7: 00         NOP                     
6DD8: FC         ???                     
6DD9: 00         NOP                     
6DDA: F8 00      LDHL    SP,$00          
6DDC: E0 00      LDFF00  ($00),A         
6DDE: 00         NOP                     
6DDF: 00         NOP                     
6DE0: 00         NOP                     
6DE1: 00         NOP                     
6DE2: 42         LD      B,D             
6DE3: 42         LD      B,D             
6DE4: 24         INC     H               
6DE5: 24         INC     H               
6DE6: 18 18      JR      $6E00           
6DE8: 18 18      JR      $6E02           
6DEA: 24         INC     H               
6DEB: 24         INC     H               
6DEC: 42         LD      B,D             
6DED: 42         LD      B,D             
6DEE: 00         NOP                     
6DEF: 00         NOP                     
6DF0: 00         NOP                     
6DF1: 00         NOP                     
6DF2: 42         LD      B,D             
6DF3: 42         LD      B,D             
6DF4: 24         INC     H               
6DF5: 24         INC     H               
6DF6: 18 18      JR      $6E10           
6DF8: 18 18      JR      $6E12           
6DFA: 24         INC     H               
6DFB: 24         INC     H               
6DFC: 42         LD      B,D             
6DFD: 42         LD      B,D             
6DFE: 00         NOP                     
6DFF: 00         NOP                     
6E00: 00         NOP                     
6E01: 00         NOP                     
6E02: 03         INC     BC              
6E03: 03         INC     BC              
6E04: 06 04      LD      B,$04           
6E06: 0E 08      LD      C,$08           
6E08: 0F         RRCA                    
6E09: 08 0F 08   LD      ($080F),SP      
6E0C: 07         RLCA                    
6E0D: 04         INC     B               
6E0E: 07         RLCA                    
6E0F: 04         INC     B               
6E10: 00         NOP                     
6E11: 00         NOP                     
6E12: C0         RET     NZ              
6E13: C0         RET     NZ              
6E14: 60         LD      H,B             
6E15: 20 70      JR      NZ,$6E87        
6E17: 10 F0      STOP    $F0             
6E19: 10 F0      STOP    $F0             
6E1B: 10 D0      STOP    $D0             
6E1D: 30 20      JR      NC,$6E3F        
6E1F: E0 F8      LDFF00  ($F8),A         
6E21: 90         SUB     B               
6E22: BF         CP      A               
6E23: C8         RET     Z               
6E24: 5F         LD      E,A             
6E25: 67         LD      H,A             
6E26: EF         RST     0X28            
6E27: B0         OR      B               
6E28: B8         CP      B               
6E29: 9F         SBC     A               
6E2A: D7         RST     0X10            
6E2B: 8F         ADC     A,A             
6E2C: A0         AND     B               
6E2D: C0         RET     NZ              
6E2E: 9F         SBC     A               
6E2F: E0 79      LDFF00  ($79),A         
6E31: 27         DAA                     
6E32: F2         ???                     
6E33: 4E         LD      C,(HL)          
6E34: F2         ???                     
6E35: 8E         ADC     A,(HL)          
6E36: C7         RST     0X00            
6E37: 3D         DEC     A               
6E38: 1D         DEC     E               
6E39: F9         LD      SP,HL           
6E3A: EB         ???                     
6E3B: F1         POP     AF              
6E3C: 05         DEC     B               
6E3D: 03         INC     BC              
6E3E: F9         LD      SP,HL           
6E3F: 07         RLCA                    
6E40: 00         NOP                     
6E41: 00         NOP                     
6E42: 00         NOP                     
6E43: 00         NOP                     
6E44: 88         ADC     A,B             
6E45: 00         NOP                     
6E46: D5         PUSH    DE              
6E47: 08 7F 88   LD      ($887F),SP      
6E4A: EA DD 37   LD      ($37DD),A       
6E4D: FF         RST     0X38            
6E4E: FF         RST     0X38            
6E4F: 00         NOP                     
6E50: D0         RET     NC              
6E51: 60         LD      H,B             
6E52: C0         RET     NZ              
6E53: 60         LD      H,B             
6E54: EC         ???                     
6E55: 40         LD      B,B             
6E56: F8 40      LDHL    SP,$40          
6E58: E0 50      LDFF00  ($50),A         
6E5A: D0         RET     NC              
6E5B: 60         LD      H,B             
6E5C: FE 60      CP      $60             
6E5E: E8 70      ADD     SP,$70          
6E60: 00         NOP                     
6E61: 00         NOP                     
6E62: 00         NOP                     
6E63: 00         NOP                     
6E64: 38 00      JR      C,$6E66         
6E66: 50         LD      D,B             
6E67: 20 A0      JR      NZ,$6E09        
6E69: 40         LD      B,B             
6E6A: AC         XOR     H               
6E6B: C0         RET     NZ              
6E6C: F8 C0      LDHL    SP,$C0          
6E6E: 70         LD      (HL),B          
6E6F: C0         RET     NZ              
6E70: 0F         RRCA                    
6E71: 03         INC     BC              
6E72: 1D         DEC     E               
6E73: 03         INC     BC              
6E74: 27         DAA                     
6E75: 00         NOP                     
6E76: 06 00      LD      B,$00           
6E78: 04         INC     B               
6E79: 00         NOP                     
6E7A: 00         NOP                     
6E7B: 00         NOP                     
6E7C: 00         NOP                     
6E7D: 00         NOP                     
6E7E: 00         NOP                     
6E7F: 00         NOP                     
6E80: FF         RST     0X38            
6E81: 00         NOP                     
6E82: DF         RST     0X18            
6E83: E0 37      LDFF00  ($37),A         
6E85: F8 4B      LDHL    SP,$4B          
6E87: 3C         INC     A               
6E88: 17         RLA                     
6E89: 0C         INC     C               
6E8A: 0D         DEC     C               
6E8B: 06 3B      LD      B,$3B           
6E8D: 06 0F      LD      B,$0F           
6E8F: 02         LD      (BC),A          
6E90: FF         RST     0X38            
6E91: 00         NOP                     
6E92: FB         EI                      
6E93: 07         RLCA                    
6E94: EC         ???                     
6E95: 1F         RRA                     
6E96: D2 3C E8   JP      NC,$E83C        
6E99: 30 B0      JR      NC,$6E4B        
6E9B: 60         LD      H,B             
6E9C: DC 60 F0   CALL    C,$F060         
6E9F: 40         LD      B,B             
6EA0: FF         RST     0X38            
6EA1: 7E         LD      A,(HL)          
6EA2: BD         CP      L               
6EA3: C3 C3 81   JP      $81C3           
6EA6: C3 81 E3   JP      $E381           
6EA9: 81         ADD     A,C             
6EAA: C7         RST     0X00            
6EAB: 81         ADD     A,C             
6EAC: C3 81 C3   JP      $C381           
6EAF: 81         ADD     A,C             
6EB0: FF         RST     0X38            
6EB1: FF         RST     0X38            
6EB2: 00         NOP                     
6EB3: FF         RST     0X38            
6EB4: C3 3C 81   JP      $813C           
6EB7: 42         LD      B,D             
6EB8: 18 99      JR      $6E53           
6EBA: 18 99      JR      $6E55           
6EBC: 81         ADD     A,C             
6EBD: 42         LD      B,D             
6EBE: C3 3C FF   JP      $FF3C           
6EC1: FF         RST     0X38            
6EC2: DB         ???                     
6EC3: E7         RST     0X20            
6EC4: D3         ???                     
6EC5: E7         RST     0X20            
6EC6: DB         ???                     
6EC7: E7         RST     0X20            
6EC8: CB F7      SET     1,E             
6ECA: DB         ???                     
6ECB: E7         RST     0X20            
6ECC: CB E7      SET     1,E             
6ECE: DB         ???                     
6ECF: E7         RST     0X20            
6ED0: 87         ADD     A,A             
6ED1: FF         RST     0X38            
6ED2: 84         ADD     A,H             
6ED3: FC         ???                     
6ED4: CB FB      SET     1,E             
6ED6: FB         EI                      
6ED7: BB         CP      E               
6ED8: B9         CP      C               
6ED9: C9         RET                     
6EDA: 8D         ADC     A,L             
6EDB: FD         ???                     
6EDC: 44         LD      B,H             
6EDD: 7C         LD      A,H             
6EDE: 3F         CCF                     
6EDF: 3F         CCF                     
6EE0: 0F         RRCA                    
6EE1: 08 19 10   LD      ($1019),SP      
6EE4: 33         INC     SP              
6EE5: 20 67      JR      NZ,$6F4E        
6EE7: 40         LD      B,B             
6EE8: 7F         LD      A,A             
6EE9: 47         LD      B,A             
6EEA: 58         LD      E,B             
6EEB: 68         LD      L,B             
6EEC: 2F         CPL                     
6EED: 3F         CCF                     
6EEE: 13         INC     DE              
6EEF: 13         INC     DE              
6EF0: 02         LD      (BC),A          
6EF1: 00         NOP                     
6EF2: 22         LD      (HLI),A         
6EF3: 00         NOP                     
6EF4: 02         LD      (BC),A          
6EF5: 00         NOP                     
6EF6: 82         ADD     A,D             
6EF7: 00         NOP                     
6EF8: 0A         LD      A,(BC)          
6EF9: 00         NOP                     
6EFA: 02         LD      (BC),A          
6EFB: 00         NOP                     
6EFC: FC         ???                     
6EFD: 00         NOP                     
6EFE: 00         NOP                     
6EFF: 00         NOP                     
6F00: 0F         RRCA                    
6F01: 08 19 10   LD      ($1019),SP      
6F04: 33         INC     SP              
6F05: 20 67      JR      NZ,$6F6E        
6F07: 40         LD      B,B             
6F08: 7F         LD      A,A             
6F09: 47         LD      B,A             
6F0A: F8 88      LDHL    SP,$88          
6F0C: F3         DI                      
6F0D: 93         SUB     E               
6F0E: F3         DI                      
6F0F: 93         SUB     E               
6F10: A0         AND     B               
6F11: 60         LD      H,B             
6F12: D0         RET     NC              
6F13: 30 E8      JR      NC,$6EFD        
6F15: 18 F4      JR      $6F0B           
6F17: 0C         INC     C               
6F18: F2         ???                     
6F19: 8E         ADC     A,(HL)          
6F1A: 7A         LD      A,D             
6F1B: 46         LD      B,(HL)          
6F1C: 39         ADD     HL,SP           
6F1D: 27         DAA                     
6F1E: 39         ADD     HL,SP           
6F1F: 27         DAA                     
6F20: 81         ADD     A,C             
6F21: FF         RST     0X38            
6F22: C1         POP     BC              
6F23: FF         RST     0X38            
6F24: E1         POP     HL              
6F25: BF         CP      A               
6F26: BE         CP      (HL)            
6F27: DF         RST     0X18            
6F28: 9F         SBC     A               
6F29: E8 88      ADD     SP,$88          
6F2B: FF         RST     0X38            
6F2C: 48         LD      C,B             
6F2D: 7F         LD      A,A             
6F2E: 3F         CCF                     
6F2F: 3F         CCF                     
6F30: 81         ADD     A,C             
6F31: 7F         LD      A,A             
6F32: 81         ADD     A,C             
6F33: 7F         LD      A,A             
6F34: E3         ???                     
6F35: FF         RST     0X38            
6F36: FF         RST     0X38            
6F37: 1D         DEC     E               
6F38: 1D         DEC     E               
6F39: F3         DI                      
6F3A: 11 FF 12   LD      DE,$12FF        
6F3D: FE FC      CP      $FC             
6F3F: FC         ???                     
6F40: FF         RST     0X38            
6F41: 00         NOP                     
6F42: BB         CP      E               
6F43: FF         RST     0X38            
6F44: 54         LD      D,H             
6F45: EF         RST     0X28            
6F46: AA         XOR     D               
6F47: 44         LD      B,H             
6F48: 44         LD      B,H             
6F49: 00         NOP                     
6F4A: 00         NOP                     
6F4B: 00         NOP                     
6F4C: 00         NOP                     
6F4D: 00         NOP                     
6F4E: 00         NOP                     
6F4F: 00         NOP                     
6F50: 0B         DEC     BC              
6F51: 06 03      LD      B,$03           
6F53: 06 37      LD      B,$37           
6F55: 02         LD      (BC),A          
6F56: 1F         RRA                     
6F57: 02         LD      (BC),A          
6F58: 07         RLCA                    
6F59: 0A         LD      A,(BC)          
6F5A: 0B         DEC     BC              
6F5B: 06 7F      LD      B,$7F           
6F5D: 06 17      LD      B,$17           
6F5F: 0E F0      LD      C,$F0           
6F61: C0         RET     NZ              
6F62: B8         CP      B               
6F63: C0         RET     NZ              
6F64: E4         ???                     
6F65: 00         NOP                     
6F66: 60         LD      H,B             
6F67: 00         NOP                     
6F68: 20 00      JR      NZ,$6F6A        
6F6A: 00         NOP                     
6F6B: 00         NOP                     
6F6C: 00         NOP                     
6F6D: 00         NOP                     
6F6E: 00         NOP                     
6F6F: 00         NOP                     
6F70: 00         NOP                     
6F71: 00         NOP                     
6F72: 00         NOP                     
6F73: 00         NOP                     
6F74: 1C         INC     E               
6F75: 00         NOP                     
6F76: 0A         LD      A,(BC)          
6F77: 04         INC     B               
6F78: 05         DEC     B               
6F79: 02         LD      (BC),A          
6F7A: 35         DEC     (HL)            
6F7B: 03         INC     BC              
6F7C: 1F         RRA                     
6F7D: 03         INC     BC              
6F7E: 0E 03      LD      C,$03           
6F80: DD         ???                     
6F81: 06 5D      LD      B,$5D           
6F83: 26 67      LD      H,$67           
6F85: 1C         INC     E               
6F86: E7         RST     0X20            
6F87: 1C         INC     E               
6F88: 8B         ADC     A,E             
6F89: 7C         LD      A,H             
6F8A: 77         LD      (HL),A          
6F8B: F8 BF      LDHL    SP,$BF          
6F8D: C0         RET     NZ              
6F8E: FF         RST     0X38            
6F8F: 00         NOP                     
6F90: BB         CP      E               
6F91: 60         LD      H,B             
6F92: BA         CP      D               
6F93: 64         LD      H,H             
6F94: E6 38      AND     $38             
6F96: E7         RST     0X20            
6F97: 38 D1      JR      C,$6F6A         
6F99: 3E EE      LD      A,$EE           
6F9B: 1F         RRA                     
6F9C: FD         ???                     
6F9D: 03         INC     BC              
6F9E: FF         RST     0X38            
6F9F: 00         NOP                     
6FA0: BD         CP      L               
6FA1: C3 81 FF   JP      $FF81           
6FA4: 81         ADD     A,C             
6FA5: FF         RST     0X38            
6FA6: C3 FF FF   JP      $FFFF           
6FA9: BD         CP      L               
6FAA: BD         CP      L               
6FAB: C3 81 FF   JP      $FF81           
6FAE: FF         RST     0X38            
6FAF: FF         RST     0X38            
6FB0: FF         RST     0X38            
6FB1: 00         NOP                     
6FB2: C3 3C 81   JP      $813C           
6FB5: 42         LD      B,D             
6FB6: 18 99      JR      $6F51           
6FB8: 18 99      JR      $6F53           
6FBA: 81         ADD     A,C             
6FBB: 42         LD      B,D             
6FBC: C3 3C FF   JP      $FF3C           
6FBF: FF         RST     0X38            
6FC0: DB         ???                     
6FC1: E7         RST     0X20            
6FC2: CB F7      SET     1,E             
6FC4: DB         ???                     
6FC5: E7         RST     0X20            
6FC6: DB         ???                     
6FC7: E7         RST     0X20            
6FC8: D3         ???                     
6FC9: E7         RST     0X20            
6FCA: 5A         LD      E,D             
6FCB: E7         RST     0X20            
6FCC: 7E         LD      A,(HL)          
6FCD: 24         INC     H               
6FCE: 3C         INC     A               
6FCF: 18 E1      JR      $6FB2           
6FD1: FF         RST     0X38            
6FD2: 21 3F D3   LD      HL,$D33F        
6FD5: DF         RST     0X18            
6FD6: DF         RST     0X18            
6FD7: DD         ???                     
6FD8: 9D         SBC     L               
6FD9: 93         SUB     E               
6FDA: B1         OR      C               
6FDB: BF         CP      A               
6FDC: 22         LD      (HLI),A         
6FDD: 3E FC      LD      A,$FC           
6FDF: FC         ???                     
6FE0: A0         AND     B               
6FE1: 60         LD      H,B             
6FE2: D0         RET     NC              
6FE3: 30 E8      JR      NC,$6FCD        
6FE5: 18 F4      JR      $6FDB           
6FE7: 0C         INC     C               
6FE8: F2         ???                     
6FE9: 8E         ADC     A,(HL)          
6FEA: 66         LD      H,(HL)          
6FEB: 5E         LD      E,(HL)          
6FEC: 7C         LD      A,H             
6FED: 7C         LD      A,H             
6FEE: C8         RET     Z               
6FEF: C8         RET     Z               
6FF0: 44         LD      B,H             
6FF1: FF         RST     0X38            
6FF2: FF         RST     0X38            
6FF3: FF         RST     0X38            
6FF4: EE 11      XOR     $11             
6FF6: EE 11      XOR     $11             
6FF8: EE 11      XOR     $11             
6FFA: FF         RST     0X38            
6FFB: FF         RST     0X38            
6FFC: 00         NOP                     
6FFD: 00         NOP                     
6FFE: 00         NOP                     
6FFF: 00         NOP                     
7000: A2         AND     D               
7001: FF         RST     0X38            
7002: A2         AND     D               
7003: FF         RST     0X38            
7004: A2         AND     D               
7005: FF         RST     0X38            
7006: A2         AND     D               
7007: FF         RST     0X38            
7008: A2         AND     D               
7009: FF         RST     0X38            
700A: E2         LDFF00  (C),A           
700B: FF         RST     0X38            
700C: 9E         SBC     (HL)            
700D: FF         RST     0X38            
700E: 97         SUB     A               
700F: FB         EI                      
7010: FF         RST     0X38            
7011: 03         INC     BC              
7012: 06 FA      LD      B,$FA           
7014: 1A         LD      A,(DE)          
7015: F6 07      OR      $07             
7017: FA 4B F6   LD      A,($F64B)       
701A: 17         RLA                     
701B: FA 03 FF   LD      A,($FF03)       
701E: FF         RST     0X38            
701F: FF         RST     0X38            
7020: FB         EI                      
7021: 06 A6      LD      B,$A6           
7023: 5B         LD      E,E             
7024: C2 3F AA   JP      NZ,$AA3F        
7027: 5F         LD      E,A             
7028: C2 3F E2   JP      NZ,$E23F        
702B: 1F         RRA                     
702C: 82         ADD     A,D             
702D: 7F         LD      A,A             
702E: FF         RST     0X38            
702F: FF         RST     0X38            
7030: C9         RET                     
7031: 3F         CCF                     
7032: 19         ADD     HL,DE           
7033: FF         RST     0X38            
7034: 09         ADD     HL,BC           
7035: FF         RST     0X38            
7036: 49         LD      C,C             
7037: FF         RST     0X38            
7038: 49         LD      C,C             
7039: FF         RST     0X38            
703A: 0F         RRCA                    
703B: FF         RST     0X38            
703C: 35         DEC     (HL)            
703D: FF         RST     0X38            
703E: F5         PUSH    AF              
703F: CF         RST     0X08            
7040: 93         SUB     E               
7041: FC         ???                     
7042: 98         SBC     B               
7043: FF         RST     0X38            
7044: 90         SUB     B               
7045: FF         RST     0X38            
7046: 92         SUB     D               
7047: FF         RST     0X38            
7048: 92         SUB     D               
7049: FF         RST     0X38            
704A: F0 FF      LD      A,($FF)         
704C: AC         XOR     H               
704D: FF         RST     0X38            
704E: AF         XOR     A               
704F: F3         DI                      
7050: 45         LD      B,L             
7051: FF         RST     0X38            
7052: 45         LD      B,L             
7053: FF         RST     0X38            
7054: 45         LD      B,L             
7055: FF         RST     0X38            
7056: 45         LD      B,L             
7057: FF         RST     0X38            
7058: 45         LD      B,L             
7059: FF         RST     0X38            
705A: 47         LD      B,A             
705B: FF         RST     0X38            
705C: 79         LD      A,C             
705D: FF         RST     0X38            
705E: E9         JP      (HL)            
705F: DF         RST     0X18            
7060: 18 30      JR      $7092           
7062: D7         RST     0X10            
7063: 30 D5      JR      NC,$703A        
7065: 30 D7      JR      NC,$703E        
7067: 30 D7      JR      NC,$7040        
7069: 30 D7      JR      NC,$7042        
706B: 30 17      JR      NC,$7084        
706D: F8 FF      LDHL    SP,$FF          
706F: FF         RST     0X38            
7070: 8E         ADC     A,(HL)          
7071: 00         NOP                     
7072: F1         POP     AF              
7073: 00         NOP                     
7074: FF         RST     0X38            
7075: 00         NOP                     
7076: FF         RST     0X38            
7077: 00         NOP                     
7078: FF         RST     0X38            
7079: 00         NOP                     
707A: 7F         LD      A,A             
707B: 80         ADD     A,B             
707C: 33         INC     SP              
707D: CC FF FF   CALL    Z,$FFFF         
7080: 00         NOP                     
7081: 00         NOP                     
7082: 03         INC     BC              
7083: 03         INC     BC              
7084: 04         INC     B               
7085: 07         RLCA                    
7086: 08 0F 10   LD      ($100F),SP      
7089: 1F         RRA                     
708A: 20 3F      JR      NZ,$70CB        
708C: 71         LD      (HL),C          
708D: 4E         LD      C,(HL)          
708E: 5B         LD      E,E             
708F: 64         LD      H,H             
7090: 00         NOP                     
7091: 00         NOP                     
7092: E0 E0      LDFF00  ($E0),A         
7094: 90         SUB     B               
7095: 70         LD      (HL),B          
7096: 88         ADC     A,B             
7097: 78         LD      A,B             
7098: 84         ADD     A,H             
7099: 7C         LD      A,H             
709A: 82         ADD     A,D             
709B: 7E         LD      A,(HL)          
709C: C6 3A      ADD     $3A             
709E: 6E         LD      L,(HL)          
709F: 92         SUB     D               
70A0: FC         ???                     
70A1: 00         NOP                     
70A2: F8 00      LDHL    SP,$00          
70A4: F8 00      LDHL    SP,$00          
70A6: F8 00      LDHL    SP,$00          
70A8: C0         RET     NZ              
70A9: 00         NOP                     
70AA: 80         ADD     A,B             
70AB: 00         NOP                     
70AC: 80         ADD     A,B             
70AD: 00         NOP                     
70AE: 80         ADD     A,B             
70AF: 00         NOP                     
70B0: FF         RST     0X38            
70B1: 0F         RRCA                    
70B2: F0 10      LD      A,($10)         
70B4: EE 20      XOR     $20             
70B6: EF         RST     0X28            
70B7: 26 DF      LD      H,$DF           
70B9: 4F         LD      C,A             
70BA: DF         RST     0X18            
70BB: 4F         LD      C,A             
70BC: DF         RST     0X18            
70BD: 58         LD      E,B             
70BE: BF         CP      A               
70BF: 90         SUB     B               
70C0: FF         RST     0X38            
70C1: 39         ADD     HL,SP           
70C2: E6 A6      AND     $A6             
70C4: 78         LD      A,B             
70C5: 60         LD      H,B             
70C6: 7C         LD      A,H             
70C7: 38 C4      JR      C,$708D         
70C9: 7C         LD      A,H             
70CA: CC F4 DD   CALL    Z,$DDF4         
70CD: FC         ???                     
70CE: DF         RST     0X18            
70CF: 7D         LD      A,L             
70D0: FF         RST     0X38            
70D1: 9C         SBC     H               
70D2: 67         LD      H,A             
70D3: 65         LD      H,L             
70D4: 1E 06      LD      E,$06           
70D6: 3E 1C      LD      A,$1C           
70D8: 23         INC     HL              
70D9: 3E 33      LD      A,$33           
70DB: 2F         CPL                     
70DC: BB         CP      E               
70DD: 3F         CCF                     
70DE: FB         EI                      
70DF: BE         CP      (HL)            
70E0: FF         RST     0X38            
70E1: F0 0F      LD      A,($0F)         
70E3: 08 77 04   LD      ($0477),SP      
70E6: F7         RST     0X30            
70E7: 64         LD      H,H             
70E8: FB         EI                      
70E9: F2         ???                     
70EA: FB         EI                      
70EB: F2         ???                     
70EC: FB         EI                      
70ED: 1A         LD      A,(DE)          
70EE: FD         ???                     
70EF: 09         ADD     HL,BC           
70F0: FF         RST     0X38            
70F1: FF         RST     0X38            
70F2: FF         RST     0X38            
70F3: C0         RET     NZ              
70F4: E0 C0      LDFF00  ($C0),A         
70F6: FF         RST     0X38            
70F7: FF         RST     0X38            
70F8: FF         RST     0X38            
70F9: FF         RST     0X38            
70FA: FF         RST     0X38            
70FB: C0         RET     NZ              
70FC: E0 C0      LDFF00  ($C0),A         
70FE: FF         RST     0X38            
70FF: FF         RST     0X38            
7100: 93         SUB     E               
7101: FC         ???                     
7102: 98         SBC     B               
7103: FF         RST     0X38            
7104: 90         SUB     B               
7105: FF         RST     0X38            
7106: 92         SUB     D               
7107: FF         RST     0X38            
7108: 92         SUB     D               
7109: FF         RST     0X38            
710A: F0 7F      LD      A,($7F)         
710C: 3E 1F      LD      A,$1F           
710E: 03         INC     BC              
710F: 01 DF 60   LD      BC,$60DF        
7112: 65         LD      H,L             
7113: DA 43 FC   JP      C,$FC43         
7116: 55         LD      D,L             
7117: FA 47 F8   LD      A,($F847)       
711A: 47         LD      B,A             
711B: F8 41      LDHL    SP,$41          
711D: FE FF      CP      $FF             
711F: FF         RST     0X38            
7120: FF         RST     0X38            
7121: C0         RET     NZ              
7122: 60         LD      H,B             
7123: 5F         LD      E,A             
7124: 58         LD      E,B             
7125: 6F         LD      L,A             
7126: E0 5F      LDFF00  ($5F),A         
7128: D2 6F E8   JP      NC,$E86F        
712B: 5F         LD      E,A             
712C: C0         RET     NZ              
712D: FF         RST     0X38            
712E: FF         RST     0X38            
712F: FF         RST     0X38            
7130: 45         LD      B,L             
7131: FF         RST     0X38            
7132: 45         LD      B,L             
7133: FF         RST     0X38            
7134: 45         LD      B,L             
7135: FF         RST     0X38            
7136: 45         LD      B,L             
7137: FF         RST     0X38            
7138: 45         LD      B,L             
7139: FF         RST     0X38            
713A: 47         LD      B,A             
713B: FE 7C      CP      $7C             
713D: F8 C0      LDHL    SP,$C0          
713F: 80         ADD     A,B             
7140: A2         AND     D               
7141: FF         RST     0X38            
7142: A2         AND     D               
7143: FF         RST     0X38            
7144: A2         AND     D               
7145: FF         RST     0X38            
7146: A2         AND     D               
7147: FF         RST     0X38            
7148: A2         AND     D               
7149: FF         RST     0X38            
714A: E2         LDFF00  (C),A           
714B: 7F         LD      A,A             
714C: 3E 1F      LD      A,$1F           
714E: 03         INC     BC              
714F: 01 C9 3F   LD      BC,$3FC9        
7152: 19         ADD     HL,DE           
7153: FF         RST     0X38            
7154: 09         ADD     HL,BC           
7155: FF         RST     0X38            
7156: 49         LD      C,C             
7157: FF         RST     0X38            
7158: 49         LD      C,C             
7159: FF         RST     0X38            
715A: 0F         RRCA                    
715B: FE 7C      CP      $7C             
715D: F8 C0      LDHL    SP,$C0          
715F: 80         ADD     A,B             
7160: 00         NOP                     
7161: FF         RST     0X38            
7162: 07         RLCA                    
7163: FF         RST     0X38            
7164: 1C         INC     E               
7165: FF         RST     0X38            
7166: 30 FF      JR      NC,$7167        
7168: 63         LD      H,E             
7169: FC         ???                     
716A: 67         LD      H,A             
716B: F8 C7      LDHL    SP,$C7          
716D: F8 C7      LDHL    SP,$C7          
716F: F8 00      LDHL    SP,$00          
7171: FF         RST     0X38            
7172: E0 FF      LDFF00  ($FF),A         
7174: 38 FF      JR      C,$7175         
7176: 0C         INC     C               
7177: FF         RST     0X38            
7178: C6 3F      ADD     $3F             
717A: E6 1F      AND     $1F             
717C: E3         ???                     
717D: 1F         RRA                     
717E: E3         ???                     
717F: 1F         RRA                     
7180: DB         ???                     
7181: 67         LD      H,A             
7182: C4 7C CB   CALL    NZ,$CB7C        
7185: 7B         LD      A,E             
7186: CB 7B      SET     1,E             
7188: C9         RET                     
7189: 79         LD      A,C             
718A: 45         LD      B,L             
718B: 7D         LD      A,L             
718C: 64         LD      H,H             
718D: 3C         INC     A               
718E: 3F         CCF                     
718F: 1F         RRA                     
7190: DB         ???                     
7191: E6 23      AND     $23             
7193: 3E D3      LD      A,$D3           
7195: DE D3      SBC     $D3             
7197: DE 93      SBC     $93             
7199: 9E         SBC     (HL)            
719A: A2         AND     D               
719B: BE         CP      (HL)            
719C: 26 3C      LD      H,$3C           
719E: FC         ???                     
719F: F8 3F      LDHL    SP,$3F          
71A1: 00         NOP                     
71A2: 1F         RRA                     
71A3: 00         NOP                     
71A4: 0F         RRCA                    
71A5: 00         NOP                     
71A6: 0F         RRCA                    
71A7: 00         NOP                     
71A8: 0F         RRCA                    
71A9: 00         NOP                     
71AA: 0F         RRCA                    
71AB: 00         NOP                     
71AC: 03         INC     BC              
71AD: 00         NOP                     
71AE: 01 00 BF   LD      BC,$BF00        
71B1: 90         SUB     B               
71B2: BF         CP      A               
71B3: 92         SUB     D               
71B4: BF         CP      A               
71B5: 92         SUB     D               
71B6: BF         CP      A               
71B7: 92         SUB     D               
71B8: BF         CP      A               
71B9: 97         SUB     A               
71BA: BF         CP      A               
71BB: 9C         SBC     H               
71BC: FF         RST     0X38            
71BD: 78         LD      A,B             
71BE: FF         RST     0X38            
71BF: FF         RST     0X38            
71C0: E6 7E      AND     $7E             
71C2: FE 3C      CP      $3C             
71C4: F8 18      LDHL    SP,$18          
71C6: FA 4A F8   LD      A,($F84A)       
71C9: C8         RET     Z               
71CA: FE 7C      CP      $7C             
71CC: FF         RST     0X38            
71CD: 0E FF      LD      C,$FF           
71CF: FF         RST     0X38            
71D0: 67         LD      H,A             
71D1: 7E         LD      A,(HL)          
71D2: 7F         LD      A,A             
71D3: 3C         INC     A               
71D4: 1F         RRA                     
71D5: 18 5F      JR      $7236           
71D7: 52         LD      D,D             
71D8: 1F         RRA                     
71D9: 13         INC     DE              
71DA: 7F         LD      A,A             
71DB: 3E FF      LD      A,$FF           
71DD: 70         LD      (HL),B          
71DE: FF         RST     0X38            
71DF: FF         RST     0X38            
71E0: FD         ???                     
71E1: 09         ADD     HL,BC           
71E2: FD         ???                     
71E3: 49         LD      C,C             
71E4: FD         ???                     
71E5: 49         LD      C,C             
71E6: FD         ???                     
71E7: 49         LD      C,C             
71E8: FD         ???                     
71E9: E9         JP      (HL)            
71EA: FD         ???                     
71EB: 39         ADD     HL,SP           
71EC: FF         RST     0X38            
71ED: 1E FF      LD      E,$FF           
71EF: FF         RST     0X38            
71F0: FF         RST     0X38            
71F1: FF         RST     0X38            
71F2: FF         RST     0X38            
71F3: 03         INC     BC              
71F4: 07         RLCA                    
71F5: 03         INC     BC              
71F6: FF         RST     0X38            
71F7: FF         RST     0X38            
71F8: FF         RST     0X38            
71F9: FF         RST     0X38            
71FA: FF         RST     0X38            
71FB: 03         INC     BC              
71FC: 07         RLCA                    
71FD: 03         INC     BC              
71FE: FF         RST     0X38            
71FF: FF         RST     0X38            
7200: FF         RST     0X38            
7201: 00         NOP                     
7202: FF         RST     0X38            
7203: 03         INC     BC              
7204: F4         ???                     
7205: 07         RLCA                    
7206: C4 07 E8   CALL    NZ,$E807        
7209: 0F         RRCA                    
720A: F1         POP     AF              
720B: 3E C3      LD      A,$C3           
720D: 7C         LD      A,H             
720E: C7         RST     0X00            
720F: 78         LD      A,B             
7210: E3         ???                     
7211: FF         RST     0X38            
7212: 1C         INC     E               
7213: FF         RST     0X38            
7214: 18 E7      JR      $71FD           
7216: 31 CE 03   LD      SP,$03CE        
7219: FC         ???                     
721A: C3 3C C1   JP      $C13C           
721D: 3E 80      LD      A,$80           
721F: 7F         LD      A,A             
7220: C7         RST     0X00            
7221: FF         RST     0X38            
7222: 38 FF      JR      C,$7223         
7224: 18 E7      JR      $720D           
7226: 8C         ADC     A,H             
7227: 73         LD      (HL),E          
7228: C0         RET     NZ              
7229: 3F         CCF                     
722A: C3 3C 83   JP      $833C           
722D: 7C         LD      A,H             
722E: 01 FE FF   LD      BC,$FFFE        
7231: 00         NOP                     
7232: FF         RST     0X38            
7233: C0         RET     NZ              
7234: 2F         CPL                     
7235: E0 23      LDFF00  ($23),A         
7237: E0 17      LDFF00  ($17),A         
7239: F0 8F      LD      A,($8F)         
723B: 7C         LD      A,H             
723C: C3 3E C3   JP      $C33E           
723F: 3E 87      LD      A,$87           
7241: FF         RST     0X38            
7242: C2 FF C0   JP      NZ,$C0FF        
7245: 7F         LD      A,A             
7246: A0         AND     B               
7247: 3F         CCF                     
7248: 78         LD      A,B             
7249: 5F         LD      E,A             
724A: 6F         LD      L,A             
724B: 5F         LD      E,A             
724C: 28 3F      JR      Z,$728D         
724E: 9E         SBC     (HL)            
724F: 19         ADD     HL,DE           
7250: 1C         INC     E               
7251: FF         RST     0X38            
7252: 1C         INC     E               
7253: FF         RST     0X38            
7254: 1C         INC     E               
7255: FF         RST     0X38            
7256: 48         LD      C,B             
7257: FF         RST     0X38            
7258: E0 FF      LDFF00  ($FF),A         
725A: 72         LD      (HL),D          
725B: FF         RST     0X38            
725C: 7E         LD      A,(HL)          
725D: DF         RST     0X18            
725E: 39         ADD     HL,SP           
725F: CF         RST     0X08            
7260: 38 FF      JR      C,$7261         
7262: 38 FF      JR      C,$7263         
7264: 38 FF      JR      C,$7265         
7266: 10 FF      STOP    $FF             
7268: 04         INC     B               
7269: FF         RST     0X38            
726A: 1F         RRA                     
726B: FF         RST     0X38            
726C: 36 FB      LD      (HL),$FB        
726E: ED         ???                     
726F: F3         DI                      
7270: E1         POP     HL              
7271: FF         RST     0X38            
7272: 43         LD      B,E             
7273: FF         RST     0X38            
7274: 03         INC     BC              
7275: FE 05      CP      $05             
7277: FC         ???                     
7278: 1E FA      LD      E,$FA           
727A: F2         ???                     
727B: FE 1D      CP      $1D             
727D: FC         ???                     
727E: 79         LD      A,C             
727F: 98         SBC     B               
7280: FF         RST     0X38            
7281: 60         LD      H,B             
7282: DF         RST     0X18            
7283: 53         LD      D,E             
7284: FF         RST     0X38            
7285: 54         LD      D,H             
7286: DC 6F EB   CALL    C,$EB6F         
7289: 3F         CCF                     
728A: FD         ???                     
728B: 13         INC     DE              
728C: F9         LD      SP,HL           
728D: 27         DAA                     
728E: E3         ???                     
728F: 3E FF      LD      A,$FF           
7291: 3C         INC     A               
7292: FB         EI                      
7293: C6 23      ADD     $23             
7295: FF         RST     0X38            
7296: 7D         LD      A,L             
7297: FF         RST     0X38            
7298: F9         LD      SP,HL           
7299: 8F         ADC     A,A             
729A: F6 26      OR      $26             
729C: D9         RETI                    
729D: 50         LD      D,B             
729E: FF         RST     0X38            
729F: 50         LD      D,B             
72A0: 00         NOP                     
72A1: 00         NOP                     
72A2: 42         LD      B,D             
72A3: 42         LD      B,D             
72A4: 24         INC     H               
72A5: 24         INC     H               
72A6: 18 18      JR      $72C0           
72A8: 18 18      JR      $72C2           
72AA: 24         INC     H               
72AB: 24         INC     H               
72AC: 42         LD      B,D             
72AD: 42         LD      B,D             
72AE: 00         NOP                     
72AF: 00         NOP                     
72B0: 00         NOP                     
72B1: 00         NOP                     
72B2: 42         LD      B,D             
72B3: 42         LD      B,D             
72B4: 24         INC     H               
72B5: 24         INC     H               
72B6: 18 18      JR      $72D0           
72B8: 18 18      JR      $72D2           
72BA: 24         INC     H               
72BB: 24         INC     H               
72BC: 42         LD      B,D             
72BD: 42         LD      B,D             
72BE: 00         NOP                     
72BF: 00         NOP                     
72C0: 00         NOP                     
72C1: 00         NOP                     
72C2: 40         LD      B,B             
72C3: 00         NOP                     
72C4: 00         NOP                     
72C5: 3C         INC     A               
72C6: 24         INC     H               
72C7: 42         LD      B,D             
72C8: 7E         LD      A,(HL)          
72C9: 81         ADD     A,C             
72CA: 66         LD      H,(HL)          
72CB: 99         SBC     C               
72CC: 5B         LD      E,E             
72CD: A4         AND     H               
72CE: 69         LD      L,C             
72CF: 96         SUB     (HL)            
72D0: 00         NOP                     
72D1: 0C         INC     C               
72D2: 04         INC     B               
72D3: 12         LD      (DE),A          
72D4: 08 14 00   LD      ($0014),SP      
72D7: 14         INC     D               
72D8: 00         NOP                     
72D9: 14         INC     D               
72DA: 00         NOP                     
72DB: 08 00 80   LD      ($8000),SP      
72DE: 00         NOP                     
72DF: B8         CP      B               
72E0: 38 FF      JR      C,$72E1         
72E2: 38 FF      JR      C,$72E3         
72E4: 38 FF      JR      C,$72E5         
72E6: 10 FF      STOP    $FF             
72E8: 00         NOP                     
72E9: FF         RST     0X38            
72EA: 21 FE 43   LD      HL,$43FE        
72ED: FC         ???                     
72EE: 47         LD      B,A             
72EF: F8 87      LDHL    SP,$87          
72F1: FF         RST     0X38            
72F2: 43         LD      B,E             
72F3: FF         RST     0X38            
72F4: E0 7F      LDFF00  ($7F),A         
72F6: B0         OR      B               
72F7: 3F         CCF                     
72F8: 70         LD      (HL),B          
72F9: 5F         LD      E,A             
72FA: 71         LD      (HL),C          
72FB: 5E         LD      E,(HL)          
72FC: 63         LD      H,E             
72FD: 7C         LD      A,H             
72FE: C7         RST     0X00            
72FF: 78         LD      A,B             
7300: 87         ADD     A,A             
7301: F8 96      LDHL    SP,$96          
7303: F9         LD      SP,HL           
7304: B0         OR      B               
7305: FF         RST     0X38            
7306: A0         AND     B               
7307: FF         RST     0X38            
7308: A0         AND     B               
7309: FF         RST     0X38            
730A: 83         ADD     A,E             
730B: FF         RST     0X38            
730C: 87         ADD     A,A             
730D: FF         RST     0X38            
730E: 87         ADD     A,A             
730F: FF         RST     0X38            
7310: 18 E7      JR      $72F9           
7312: 39         ADD     HL,SP           
7313: C6 33      ADD     $33             
7315: CC 03 FC   CALL    Z,$FC03         
7318: 03         INC     BC              
7319: FC         ???                     
731A: 03         INC     BC              
731B: FC         ???                     
731C: 01 FE 0C   LD      BC,$0CFE        
731F: FF         RST     0X38            
7320: 18 E7      JR      $7309           
7322: 9C         SBC     H               
7323: 63         LD      H,E             
7324: CC 33 C0   CALL    Z,$C033         
7327: 3F         CCF                     
7328: C0         RET     NZ              
7329: 3F         CCF                     
732A: C0         RET     NZ              
732B: 3F         CCF                     
732C: 80         ADD     A,B             
732D: 7F         LD      A,A             
732E: 30 FF      JR      NC,$732F        
7330: C1         POP     BC              
7331: 3F         CCF                     
7332: 09         ADD     HL,BC           
7333: FF         RST     0X38            
7334: 0D         DEC     C               
7335: FF         RST     0X38            
7336: 05         DEC     B               
7337: FF         RST     0X38            
7338: 05         DEC     B               
7339: FF         RST     0X38            
733A: C1         POP     BC              
733B: FF         RST     0X38            
733C: E1         POP     HL              
733D: FF         RST     0X38            
733E: E1         POP     HL              
733F: FF         RST     0X38            
7340: AC         XOR     H               
7341: 33         INC     SP              
7342: 79         LD      A,C             
7343: 47         LD      B,A             
7344: 77         LD      (HL),A          
7345: 4F         LD      C,A             
7346: 6C         LD      L,H             
7347: 5F         LD      E,A             
7348: 3F         CCF                     
7349: 38 82      JR      C,$72CD         
734B: 00         NOP                     
734C: C6 00      ADD     $00             
734E: FF         RST     0X38            
734F: 00         NOP                     
7350: 7B         LD      A,E             
7351: 84         ADD     A,H             
7352: F3         DI                      
7353: 8C         ADC     A,H             
7354: EF         RST     0X28            
7355: 9C         SBC     H               
7356: FD         ???                     
7357: 9E         SBC     (HL)            
7358: F3         DI                      
7359: 9E         SBC     (HL)            
735A: F3         DI                      
735B: 92         SUB     D               
735C: 61         LD      H,C             
735D: 61         LD      H,C             
735E: 0C         INC     C               
735F: 00         NOP                     
7360: DF         RST     0X18            
7361: 21 ED 33   LD      HL,$33ED        
7364: BE         CP      (HL)            
7365: 73         LD      (HL),E          
7366: DE 73      SBC     $73             
7368: DF         RST     0X18            
7369: 72         LD      (HL),D          
736A: EC         ???                     
736B: 4C         LD      C,H             
736C: 91         SUB     C               
736D: 80         ADD     A,B             
736E: 3F         CCF                     
736F: 00         NOP                     
7370: 75         LD      (HL),L          
7371: 8C         ADC     A,H             
7372: BE         CP      (HL)            
7373: C2 CE F2   JP      NZ,$F2CE        
7376: 36 FA      LD      (HL),$FA        
7378: FC         ???                     
7379: 1C         INC     E               
737A: C1         POP     BC              
737B: 00         NOP                     
737C: E3         ???                     
737D: 00         NOP                     
737E: FF         RST     0X38            
737F: 00         NOP                     
7380: EF         RST     0X28            
7381: 3C         INC     A               
7382: FB         EI                      
7383: 36 DA      LD      (HL),$DA        
7385: 66         LD      H,(HL)          
7386: 42         LD      B,D             
7387: 7E         LD      A,(HL)          
7388: 46         LD      B,(HL)          
7389: 7E         LD      A,(HL)          
738A: 3E 3C      LD      A,$3C           
738C: 8D         ADC     A,L             
738D: 00         NOP                     
738E: E3         ???                     
738F: 00         NOP                     
7390: FF         RST     0X38            
7391: 78         LD      A,B             
7392: B7         OR      A               
7393: CC B3 FE   CALL    Z,$FEB3         
7396: DB         ???                     
7397: CE 3B      ADC     $3B             
7399: 0E EE      LD      C,$EE           
739B: 0E F1      LD      C,$F1           
739D: 00         NOP                     
739E: FF         RST     0X38            
739F: 00         NOP                     
73A0: 00         NOP                     
73A1: 00         NOP                     
73A2: 42         LD      B,D             
73A3: 42         LD      B,D             
73A4: 24         INC     H               
73A5: 24         INC     H               
73A6: 18 18      JR      $73C0           
73A8: 18 18      JR      $73C2           
73AA: 24         INC     H               
73AB: 24         INC     H               
73AC: 42         LD      B,D             
73AD: 42         LD      B,D             
73AE: 00         NOP                     
73AF: 00         NOP                     
73B0: 00         NOP                     
73B1: 00         NOP                     
73B2: 42         LD      B,D             
73B3: 42         LD      B,D             
73B4: 24         INC     H               
73B5: 24         INC     H               
73B6: 18 18      JR      $73D0           
73B8: 18 18      JR      $73D2           
73BA: 24         INC     H               
73BB: 24         INC     H               
73BC: 42         LD      B,D             
73BD: 42         LD      B,D             
73BE: 00         NOP                     
73BF: 00         NOP                     
73C0: 39         ADD     HL,SP           
73C1: 46         LD      B,(HL)          
73C2: 01 3A 01   LD      BC,$013A        
73C5: 02         LD      (BC),A          
73C6: 01 62 41   LD      BC,$4162        
73C9: 92         SUB     D               
73CA: 20 D2      JR      NZ,$739E        
73CC: 00         NOP                     
73CD: 52         LD      D,D             
73CE: 00         NOP                     
73CF: 61         LD      H,C             
73D0: 28 C4      JR      Z,$7396         
73D2: 68         LD      L,B             
73D3: 94         SUB     H               
73D4: D8         RET     C               
73D5: 24         INC     H               
73D6: 80         ADD     A,B             
73D7: 78         LD      A,B             
73D8: 00         NOP                     
73D9: 40         LD      B,B             
73DA: 00         NOP                     
73DB: 40         LD      B,B             
73DC: 00         NOP                     
73DD: 40         LD      B,B             
73DE: 01 80 1C   LD      BC,$1C80        
73E1: FF         RST     0X38            
73E2: 1C         INC     E               
73E3: FF         RST     0X38            
73E4: 08 FF 00   LD      ($00FF),SP      
73E7: FF         RST     0X38            
73E8: 10 FF      STOP    $FF             
73EA: 8C         ADC     A,H             
73EB: 7F         LD      A,A             
73EC: C2 3F E2   JP      NZ,$E23F        
73EF: 1F         RRA                     
73F0: E1         POP     HL              
73F1: FF         RST     0X38            
73F2: C3 FF 23   JP      $23FF           
73F5: FE 25      CP      $25             
73F7: FC         ???                     
73F8: 1E FA      LD      E,$FA           
73FA: 8E         ADC     A,(HL)          
73FB: 7E         LD      A,(HL)          
73FC: C2 3E E3   JP      NZ,$E33E        
73FF: 1E E1      LD      E,$E1           
7401: 1F         RRA                     
7402: 7F         LD      A,A             
7403: 82         ADD     A,D             
7404: 3E FC      LD      A,$FC           
7406: 7F         LD      A,A             
7407: E5         PUSH    HL              
7408: 67         LD      H,A             
7409: C5         PUSH    BC              
740A: DD         ???                     
740B: C6 FE      ADD     $FE             
740D: C7         RST     0X00            
740E: DD         ???                     
740F: E7         RST     0X20            
7410: FF         RST     0X38            
7411: FF         RST     0X38            
7412: 3F         CCF                     
7413: 1F         RRA                     
7414: DF         RST     0X18            
7415: 08 F9 8E   LD      ($8EF9),SP      
7418: F8 8F      LDHL    SP,$8F          
741A: EB         ???                     
741B: 1F         RRA                     
741C: 11 FF E5   LD      DE,$E5FF        
741F: FF         RST     0X38            
7420: FF         RST     0X38            
7421: F8 CE      LDHL    SP,$CE          
7423: 8D         ADC     A,L             
7424: FC         ???                     
7425: C7         RST     0X00            
7426: FE 67      CP      $67             
7428: 7E         LD      A,(HL)          
7429: BF         CP      A               
742A: 3F         CCF                     
742B: C7         RST     0X00            
742C: 81         ADD     A,C             
742D: FF         RST     0X38            
742E: BC         CP      H               
742F: FF         RST     0X38            
7430: FF         RST     0X38            
7431: 00         NOP                     
7432: 1F         RRA                     
7433: E0 1F      LDFF00  ($1F),A         
7435: FF         RST     0X38            
7436: 3F         CCF                     
7437: F1         POP     AF              
7438: 71         LD      (HL),C          
7439: E1         POP     HL              
743A: ED         ???                     
743B: C3 DF 83   JP      $83DF           
743E: 6B         LD      L,E             
743F: D7         RST     0X10            
7440: 06 FC      LD      B,$FC           
7442: F4         ???                     
7443: 0C         INC     C               
7444: E8 1C      ADD     SP,$1C          
7446: 08 FE 08   LD      ($08FE),SP      
7449: FD         ???                     
744A: 0A         LD      A,(BC)          
744B: FC         ???                     
744C: 1B         DEC     DE              
744D: FC         ???                     
744E: FB         EI                      
744F: FC         ???                     
7450: 0A         LD      A,(BC)          
7451: 06 16      LD      B,$16           
7453: 0C         INC     C               
7454: 34         INC     (HL)            
7455: 0C         INC     C               
7456: 6D         LD      L,L             
7457: 18 ED      JR      $7446           
7459: 18 17      JR      $7472           
745B: F8 13      LDHL    SP,$13          
745D: 3C         INC     A               
745E: D8         RET     C               
745F: 3F         CCF                     
7460: 50         LD      D,B             
7461: 60         LD      H,B             
7462: 68         LD      L,B             
7463: 30 2C      JR      NC,$7491        
7465: 30 B6      JR      NC,$741D        
7467: 18 B7      JR      $7420           
7469: 18 E8      JR      $7453           
746B: 1F         RRA                     
746C: C8         RET     Z               
746D: 3C         INC     A               
746E: 1B         DEC     DE              
746F: FC         ???                     
7470: 60         LD      H,B             
7471: 3F         CCF                     
7472: 2F         CPL                     
7473: 30 17      JR      NC,$748C        
7475: 38 10      JR      C,$7487         
7477: 7F         LD      A,A             
7478: 10 BF      STOP    $BF             
747A: 50         LD      D,B             
747B: 3F         CCF                     
747C: D8         RET     C               
747D: 3F         CCF                     
747E: DF         RST     0X18            
747F: 3F         CCF                     
7480: FF         RST     0X38            
7481: FF         RST     0X38            
7482: FF         RST     0X38            
7483: FF         RST     0X38            
7484: 0C         INC     C               
7485: FF         RST     0X38            
7486: 00         NOP                     
7487: FF         RST     0X38            
7488: 40         LD      B,B             
7489: FF         RST     0X38            
748A: 07         RLCA                    
748B: FF         RST     0X38            
748C: 1B         DEC     DE              
748D: FC         ???                     
748E: E8 30      ADD     SP,$30          
7490: FF         RST     0X38            
7491: FF         RST     0X38            
7492: FF         RST     0X38            
7493: FF         RST     0X38            
7494: 0C         INC     C               
7495: FF         RST     0X38            
7496: 00         NOP                     
7497: FF         RST     0X38            
7498: 00         NOP                     
7499: FF         RST     0X38            
749A: E0 FF      LDFF00  ($FF),A         
749C: DF         RST     0X18            
749D: 38 17      JR      C,$74B6         
749F: 0C         INC     C               
74A0: 3C         INC     A               
74A1: FF         RST     0X38            
74A2: 43         LD      B,E             
74A3: C3 F9 81   JP      $81F9           
74A6: FC         ???                     
74A7: F8 46      LDHL    SP,$46          
74A9: FC         ???                     
74AA: 5B         LD      E,E             
74AB: E6 2D      AND     $2D             
74AD: F3         DI                      
74AE: FE FD      CP      $FD             
74B0: 02         LD      (BC),A          
74B1: FF         RST     0X38            
74B2: 04         INC     B               
74B3: FF         RST     0X38            
74B4: 8E         ADC     A,(HL)          
74B5: FF         RST     0X38            
74B6: DD         ???                     
74B7: F9         LD      SP,HL           
74B8: 7E         LD      A,(HL)          
74B9: 64         LD      H,H             
74BA: 66         LD      H,(HL)          
74BB: 42         LD      B,D             
74BC: C2 82 C2   JP      NZ,$C282        
74BF: 82         ADD     A,D             
74C0: C5         PUSH    BC              
74C1: 03         INC     BC              
74C2: C2 01 60   JP      NZ,$6001        
74C5: 80         ADD     A,B             
74C6: 38 C0      JR      C,$7488         
74C8: B4         OR      H               
74C9: D8         RET     C               
74CA: BA         CP      D               
74CB: DC AE CC   CALL    C,$CCAE         
74CE: B6         OR      (HL)            
74CF: C4 A3 C0   CALL    NZ,$C0A3        
74D2: 43         LD      B,E             
74D3: 80         ADD     A,B             
74D4: 06 01      LD      B,$01           
74D6: 1C         INC     E               
74D7: 03         INC     BC              
74D8: 2D         DEC     L               
74D9: 1B         DEC     DE              
74DA: 5D         LD      E,L             
74DB: 3B         DEC     SP              
74DC: 75         LD      (HL),L          
74DD: 33         INC     SP              
74DE: 6D         LD      L,L             
74DF: 23         INC     HL              
74E0: 40         LD      B,B             
74E1: FF         RST     0X38            
74E2: 20 FF      JR      NZ,$74E3        
74E4: 71         LD      (HL),C          
74E5: FF         RST     0X38            
74E6: BB         CP      E               
74E7: 9F         SBC     A               
74E8: 7E         LD      A,(HL)          
74E9: 26 66      LD      H,$66           
74EB: 42         LD      B,D             
74EC: 5B         LD      E,E             
74ED: 59         LD      E,C             
74EE: 5B         LD      E,E             
74EF: 59         LD      E,C             
74F0: 3C         INC     A               
74F1: FF         RST     0X38            
74F2: C2 C3 9F   JP      NZ,$9FC3        
74F5: 81         ADD     A,C             
74F6: 3F         CCF                     
74F7: 1F         RRA                     
74F8: 62         LD      H,D             
74F9: 3F         CCF                     
74FA: DA 67 B4   JP      C,$B467         
74FD: CF         RST     0X08            
74FE: 7F         LD      A,A             
74FF: BF         CP      A               
7500: EE F3      XOR     $F3             
7502: F7         RST     0X30            
7503: 99         SBC     C               
7504: FB         EI                      
7505: 8C         ADC     A,H             
7506: BE         CP      (HL)            
7507: C7         RST     0X00            
7508: DF         RST     0X18            
7509: E1         POP     HL              
750A: 6F         LD      L,A             
750B: F0 F3      LD      A,($F3)         
750D: FC         ???                     
750E: FF         RST     0X38            
750F: FF         RST     0X38            
7510: 05         DEC     B               
7511: FB         EI                      
7512: E1         POP     HL              
7513: FF         RST     0X38            
7514: 31 1F D9   LD      SP,$D91F        
7517: 0F         RRCA                    
7518: F9         LD      SP,HL           
7519: CF         RST     0X08            
751A: FB         EI                      
751B: 0F         RRCA                    
751C: EF         RST     0X28            
751D: 1F         RRA                     
751E: FF         RST     0X38            
751F: FF         RST     0X38            
7520: E4         ???                     
7521: C7         RST     0X00            
7522: DC 87 F4   CALL    C,$F487         
7525: 8F         ADC     A,A             
7526: EC         ???                     
7527: 9F         SBC     A               
7528: F9         LD      SP,HL           
7529: FF         RST     0X38            
752A: C3 FE 07   JP      $07FE           
752D: FC         ???                     
752E: FF         RST     0X38            
752F: FF         RST     0X38            
7530: 6E         LD      L,(HL)          
7531: C7         RST     0X00            
7532: 7C         LD      A,H             
7533: C7         RST     0X00            
7534: 7E         LD      A,(HL)          
7535: C3 DB E5   JP      $E5DB           
7538: EB         ???                     
7539: F1         POP     AF              
753A: F1         POP     AF              
753B: 7F         LD      A,A             
753C: FF         RST     0X38            
753D: 7F         LD      A,A             
753E: FF         RST     0X38            
753F: FF         RST     0X38            
7540: FB         EI                      
7541: 1C         INC     E               
7542: DB         ???                     
7543: 3C         INC     A               
7544: 9B         SBC     E               
7545: 7C         LD      A,H             
7546: 09         ADD     HL,BC           
7547: FE 0C      CP      $0C             
7549: FF         RST     0X38            
754A: 06 FF      LD      B,$FF           
754C: 03         INC     BC              
754D: FF         RST     0X38            
754E: FF         RST     0X38            
754F: FF         RST     0X38            
7550: D7         RST     0X10            
7551: 3F         CCF                     
7552: D0         RET     NC              
7553: 38 D3      JR      C,$7528         
7555: 3C         INC     A               
7556: F1         POP     AF              
7557: 1E E8      LD      E,$E8           
7559: 1F         RRA                     
755A: 64         LD      H,H             
755B: 9F         SBC     A               
755C: 02         LD      (BC),A          
755D: FF         RST     0X38            
755E: FF         RST     0X38            
755F: FF         RST     0X38            
7560: EB         ???                     
7561: FC         ???                     
7562: 0B         DEC     BC              
7563: 1C         INC     E               
7564: CB 3C      SET     1,E             
7566: 8F         ADC     A,A             
7567: 78         LD      A,B             
7568: 17         RLA                     
7569: F8 26      LDHL    SP,$26          
756B: F9         LD      SP,HL           
756C: 40         LD      B,B             
756D: FF         RST     0X38            
756E: FF         RST     0X38            
756F: FF         RST     0X38            
7570: DF         RST     0X18            
7571: 38 DB      JR      C,$754E         
7573: 3C         INC     A               
7574: D9         RETI                    
7575: 3E 90      LD      A,$90           
7577: 7F         LD      A,A             
7578: 30 FF      JR      NC,$7579        
757A: 60         LD      H,B             
757B: FF         RST     0X38            
757C: C0         RET     NZ              
757D: FF         RST     0X38            
757E: FF         RST     0X38            
757F: FF         RST     0X38            
7580: D0         RET     NC              
7581: E0 73      LDFF00  ($73),A         
7583: C3 F3 43   JP      $43F3           
7586: 71         LD      (HL),C          
7587: 41         LD      B,C             
7588: 59         LD      E,C             
7589: 61         LD      H,C             
758A: AC         XOR     H               
758B: 70         LD      (HL),B          
758C: 17         RLA                     
758D: F8 FF      LDHL    SP,$FF          
758F: FF         RST     0X38            
7590: 0B         DEC     BC              
7591: 07         RLCA                    
7592: CE C3      ADC     $C3             
7594: CF         RST     0X08            
7595: C2 8E 82   JP      NZ,$828E        
7598: 9A         SBC     D               
7599: 86         ADD     A,(HL)          
759A: 35         DEC     (HL)            
759B: 0E E8      LD      C,$E8           
759D: 1F         RRA                     
759E: FF         RST     0X38            
759F: FF         RST     0X38            
75A0: C3 C2 F9   JP      $F9C2           
75A3: 81         ADD     A,C             
75A4: FC         ???                     
75A5: F8 46      LDHL    SP,$46          
75A7: FC         ???                     
75A8: 5B         LD      E,E             
75A9: E6 5D      AND     $5D             
75AB: E3         ???                     
75AC: 2F         CPL                     
75AD: F3         DI                      
75AE: FD         ???                     
75AF: FE F6      CP      $F6             
75B1: B2         OR      D               
75B2: FE B2      CP      $B2             
75B4: BA         CP      D               
75B5: C6 85      ADD     $85             
75B7: FC         ???                     
75B8: CE 79      ADC     $79             
75BA: 7D         LD      A,L             
75BB: F3         DI                      
75BC: F2         ???                     
75BD: FF         RST     0X38            
75BE: ED         ???                     
75BF: 1F         RRA                     
75C0: BE         CP      (HL)            
75C1: C4 B4 CF   CALL    NZ,$CFB4        
75C4: AF         XOR     A               
75C5: DF         RST     0X18            
75C6: 9C         SBC     H               
75C7: F0 B0      LD      A,($B0)         
75C9: E0 60      LDFF00  ($60),A         
75CB: C0         RET     NZ              
75CC: CF         RST     0X08            
75CD: 80         ADD     A,B             
75CE: B8         CP      B               
75CF: 07         RLCA                    
75D0: 7D         LD      A,L             
75D1: 23         INC     HL              
75D2: 2D         DEC     L               
75D3: F3         DI                      
75D4: F5         PUSH    AF              
75D5: FB         EI                      
75D6: 39         ADD     HL,SP           
75D7: 0F         RRCA                    
75D8: 0D         DEC     C               
75D9: 07         RLCA                    
75DA: 06 03      LD      B,$03           
75DC: F3         DI                      
75DD: 01 1D E0   LD      BC,$E01D        
75E0: 67         LD      H,A             
75E1: 41         LD      B,C             
75E2: 5F         LD      E,A             
75E3: 61         LD      H,C             
75E4: 4D         LD      C,L             
75E5: 73         LD      (HL),E          
75E6: A1         AND     C               
75E7: 3F         CCF                     
75E8: 73         LD      (HL),E          
75E9: 9E         SBC     (HL)            
75EA: BE         CP      (HL)            
75EB: CF         RST     0X08            
75EC: 4F         LD      C,A             
75ED: FF         RST     0X38            
75EE: B7         OR      A               
75EF: F8 C3      LDHL    SP,$C3          
75F1: 43         LD      B,E             
75F2: 9F         SBC     A               
75F3: 81         ADD     A,C             
75F4: 3F         CCF                     
75F5: 1F         RRA                     
75F6: 62         LD      H,D             
75F7: 3F         CCF                     
75F8: DA 67 BA   JP      C,$BA67         
75FB: C7         RST     0X00            
75FC: F4         ???                     
75FD: CF         RST     0X08            
75FE: BF         CP      A               
75FF: 7F         LD      A,A             
7600: FE F1      CP      $F1             
7602: 8F         ADC     A,A             
7603: CF         RST     0X08            
7604: 55         LD      D,L             
7605: E4         ???                     
7606: 23         INC     HL              
7607: FC         ???                     
7608: 25         DEC     H               
7609: F3         DI                      
760A: 6F         LD      L,A             
760B: F3         DI                      
760C: C2 CF CA   JP      NZ,$CACF        
760F: 87         ADD     A,A             
7610: FD         ???                     
7611: FE 4E      CP      $4E             
7613: 93         SUB     E               
7614: 69         LD      L,C             
7615: 93         SUB     E               
7616: F1         POP     AF              
7617: FD         ???                     
7618: DB         ???                     
7619: BD         CP      L               
761A: 8F         ADC     A,A             
761B: DD         ???                     
761C: 77         LD      (HL),A          
761D: CD C7 FF   CALL    $FFC7           
7620: B2         OR      D               
7621: C1         POP     BC              
7622: 8D         ADC     A,L             
7623: F3         DI                      
7624: 83         ADD     A,E             
7625: CF         RST     0X08            
7626: AB         XOR     E               
7627: C7         RST     0X00            
7628: B1         OR      C               
7629: CF         RST     0X08            
762A: 80         ADD     A,B             
762B: F1         POP     AF              
762C: D8         RET     C               
762D: E1         POP     HL              
762E: CE F1      ADC     $F1             
7630: 9D         SBC     L               
7631: E3         ???                     
7632: C1         POP     BC              
7633: FF         RST     0X38            
7634: AB         XOR     E               
7635: C7         RST     0X00            
7636: CD 83 BD   CALL    $BD83           
7639: C3 D9 E7   JP      $E7D9           
763C: 23         INC     HL              
763D: FF         RST     0X38            
763E: 1E 3F      LD      E,$3F           
7640: 00         NOP                     
7641: 00         NOP                     
7642: 88         ADC     A,B             
7643: 00         NOP                     
7644: D5         PUSH    DE              
7645: 08 7F 88   LD      ($887F),SP      
7648: EA DD FF   LD      ($FFDD),A       
764B: FF         RST     0X38            
764C: 70         LD      (HL),B          
764D: FF         RST     0X38            
764E: 00         NOP                     
764F: FF         RST     0X38            
7650: 38 F0      JR      C,$7642         
7652: 20 F0      JR      NZ,$7644        
7654: 36 E0      LD      (HL),$E0        
7656: 3C         INC     A               
7657: E0 30      LDFF00  ($30),A         
7659: E8 28      ADD     SP,$28          
765B: F0 3F      LD      A,($3F)         
765D: F0 34      LD      A,($34)         
765F: F8 00      LDHL    SP,$00          
7661: 00         NOP                     
7662: 18 00      JR      $7664           
7664: 28 10      JR      Z,$7676         
7666: 40         LD      B,B             
7667: 30 96      JR      NC,$75FF        
7669: 60         LD      H,B             
766A: DC E0 48   CALL    C,$48E0         
766D: F0 20      LD      A,($20)         
766F: F0 14      LD      A,($14)         
7671: 0F         RRCA                    
7672: 1E 07      LD      E,$07           
7674: 3B         DEC     SP              
7675: 07         RLCA                    
7676: 4F         LD      C,A             
7677: 00         NOP                     
7678: 0C         INC     C               
7679: 00         NOP                     
767A: 08 00 00   LD      ($0000),SP      
767D: 00         NOP                     
767E: 00         NOP                     
767F: 00         NOP                     
7680: 03         INC     BC              
7681: FC         ???                     
7682: 01 FE F0   LD      BC,$F0FE        
7685: FF         RST     0X38            
7686: 18 FF      JR      $7687           
7688: 2C         INC     L               
7689: 1F         RRA                     
768A: 16 0F      LD      D,$0F           
768C: 76         HALT                    
768D: 0F         RRCA                    
768E: 1E 07      LD      E,$07           
7690: C0         RET     NZ              
7691: 3F         CCF                     
7692: 80         ADD     A,B             
7693: 7F         LD      A,A             
7694: 07         RLCA                    
7695: FF         RST     0X38            
7696: 0C         INC     C               
7697: FF         RST     0X38            
7698: 1A         LD      A,(DE)          
7699: FC         ???                     
769A: 34         INC     (HL)            
769B: F8 37      LDHL    SP,$37          
769D: F8 3C      LDHL    SP,$3C          
769F: F0 FF      LD      A,($FF)         
76A1: 60         LD      H,B             
76A2: DF         RST     0X18            
76A3: 53         LD      D,E             
76A4: FF         RST     0X38            
76A5: 54         LD      D,H             
76A6: DC 6F EB   CALL    C,$EB6F         
76A9: 3F         CCF                     
76AA: FD         ???                     
76AB: 13         INC     DE              
76AC: F9         LD      SP,HL           
76AD: 27         DAA                     
76AE: E3         ???                     
76AF: 3E FF      LD      A,$FF           
76B1: 3C         INC     A               
76B2: FB         EI                      
76B3: C6 23      ADD     $23             
76B5: FF         RST     0X38            
76B6: 7D         LD      A,L             
76B7: FF         RST     0X38            
76B8: F9         LD      SP,HL           
76B9: 8F         ADC     A,A             
76BA: F6 26      OR      $26             
76BC: D9         RETI                    
76BD: 50         LD      D,B             
76BE: FF         RST     0X38            
76BF: 50         LD      D,B             
76C0: F0 0F      LD      A,($0F)         
76C2: C0         RET     NZ              
76C3: 3F         CCF                     
76C4: 80         ADD     A,B             
76C5: 7F         LD      A,A             
76C6: 20 1F      JR      NZ,$76E7        
76C8: C0         RET     NZ              
76C9: 07         RLCA                    
76CA: 00         NOP                     
76CB: 7F         LD      A,A             
76CC: 00         NOP                     
76CD: 7F         LD      A,A             
76CE: 80         ADD     A,B             
76CF: 3F         CCF                     
76D0: 7F         LD      A,A             
76D1: 80         ADD     A,B             
76D2: 1F         RRA                     
76D3: E0 0F      LDFF00  ($0F),A         
76D5: F0 07      LD      A,($07)         
76D7: F8 03      LDHL    SP,$03          
76D9: F8 03      LDHL    SP,$03          
76DB: F8 07      LDHL    SP,$07          
76DD: F0 0F      LD      A,($0F)         
76DF: E0 FE      LDFF00  ($FE),A         
76E1: FF         RST     0X38            
76E2: C5         PUSH    BC              
76E3: 03         INC     BC              
76E4: 9A         SBC     D               
76E5: E1         POP     HL              
76E6: E5         PUSH    HL              
76E7: F8 FB      LDHL    SP,$FB          
76E9: FC         ???                     
76EA: ED         ???                     
76EB: CE B7      ADC     $B7             
76ED: CE 87      ADC     $87             
76EF: FE 7F      CP      $7F             
76F1: FF         RST     0X38            
76F2: A3         AND     E               
76F3: C0         RET     NZ              
76F4: 59         LD      E,C             
76F5: 87         ADD     A,A             
76F6: A7         AND     A               
76F7: 1F         RRA                     
76F8: DF         RST     0X18            
76F9: 3F         CCF                     
76FA: B7         OR      A               
76FB: 73         LD      (HL),E          
76FC: ED         ???                     
76FD: 73         LD      (HL),E          
76FE: E1         POP     HL              
76FF: 7F         LD      A,A             
7700: D3         ???                     
7701: 8F         ADC     A,A             
7702: E1         POP     HL              
7703: 93         SUB     E               
7704: 82         ADD     A,D             
7705: E1         POP     HL              
7706: DC E2 63   CALL    C,$63E2         
7709: FC         ???                     
770A: 39         ADD     HL,SP           
770B: FE 76      CP      $76             
770D: EF         RST     0X28            
770E: F3         DI                      
770F: C1         POP     BC              
7710: 86         ADD     A,(HL)          
7711: CF         RST     0X08            
7712: 64         LD      H,H             
7713: 9F         SBC     A               
7714: CC FF 78   CALL    Z,$78FF         
7717: 3F         CCF                     
7718: 18 3F      JR      $7759           
771A: CC 3F AE   CALL    Z,$AE3F         
771D: 43         LD      B,E             
771E: 35         DEC     (HL)            
771F: C3 E0 7F   JP      $7FE0           
7722: 7E         LD      A,(HL)          
7723: FF         RST     0X38            
7724: 53         LD      D,E             
7725: E7         RST     0X20            
7726: AD         XOR     L               
7727: C3 B9 C7   JP      $C7B9           
772A: B1         OR      C               
772B: CF         RST     0X08            
772C: 81         ADD     A,C             
772D: FF         RST     0X38            
772E: C3 FF EF   JP      $EFFF           
7731: 1F         RRA                     
7732: 44         LD      B,H             
7733: BF         CP      A               
7734: 06 E7      LD      B,$E7           
7736: AA         XOR     D               
7737: C7         RST     0X00            
7738: BA         CP      D               
7739: C7         RST     0X00            
773A: 82         ADD     A,D             
773B: FF         RST     0X38            
773C: 9B         SBC     E               
773D: E7         RST     0X20            
773E: C7         RST     0X00            
773F: FF         RST     0X38            
7740: 00         NOP                     
7741: FF         RST     0X38            
7742: 00         NOP                     
7743: FF         RST     0X38            
7744: FF         RST     0X38            
7745: FF         RST     0X38            
7746: 54         LD      D,H             
7747: EF         RST     0X28            
7748: AA         XOR     D               
7749: 44         LD      B,H             
774A: 44         LD      B,H             
774B: 00         NOP                     
774C: 00         NOP                     
774D: 00         NOP                     
774E: 00         NOP                     
774F: 00         NOP                     
7750: 14         INC     D               
7751: 0F         RRCA                    
7752: 04         INC     B               
7753: 0F         RRCA                    
7754: 6C         LD      L,H             
7755: 07         RLCA                    
7756: 3C         INC     A               
7757: 07         RLCA                    
7758: 0C         INC     C               
7759: 17         RLA                     
775A: 14         INC     D               
775B: 0F         RRCA                    
775C: FC         ???                     
775D: 0F         RRCA                    
775E: 2C         INC     L               
775F: 1F         RRA                     
7760: 28 F0      JR      Z,$7752         
7762: 68         LD      L,B             
7763: F0 DC      LD      A,($DC)         
7765: E0 F2      LDFF00  ($F2),A         
7767: 00         NOP                     
7768: 30 00      JR      NC,$776A        
776A: 10 00      STOP    $00             
776C: 00         NOP                     
776D: 00         NOP                     
776E: 00         NOP                     
776F: 00         NOP                     
7770: 00         NOP                     
7771: 00         NOP                     
7772: 38 00      JR      C,$7774         
7774: 14         INC     D               
7775: 08 0A 04   LD      ($040A),SP      
7778: 6B         LD      L,E             
7779: 06 3F      LD      B,$3F           
777B: 07         RLCA                    
777C: 1E 07      LD      E,$07           
777E: 04         INC     B               
777F: 0F         RRCA                    
7780: 58         LD      E,B             
7781: 0F         RRCA                    
7782: 68         LD      L,B             
7783: 1F         RRA                     
7784: 48         LD      C,B             
7785: 3F         CCF                     
7786: 98         SBC     B               
7787: 7F         LD      A,A             
7788: 30 FF      JR      NC,$7789        
778A: E0 FF      LDFF00  ($FF),A         
778C: 01 FE 03   LD      BC,$03FE        
778F: FC         ???                     
7790: 16 F8      LD      D,$F8           
7792: 16 F8      LD      D,$F8           
7794: 13         INC     DE              
7795: FC         ???                     
7796: 18 FF      JR      $7797           
7798: 0C         INC     C               
7799: FF         RST     0X38            
779A: 07         RLCA                    
779B: FF         RST     0X38            
779C: 80         ADD     A,B             
779D: 7F         LD      A,A             
779E: C0         RET     NZ              
779F: 3F         CCF                     
77A0: EF         RST     0X28            
77A1: 3C         INC     A               
77A2: FB         EI                      
77A3: 36 DA      LD      (HL),$DA        
77A5: 66         LD      H,(HL)          
77A6: 42         LD      B,D             
77A7: 7E         LD      A,(HL)          
77A8: 46         LD      B,(HL)          
77A9: 7E         LD      A,(HL)          
77AA: 3E 3C      LD      A,$3C           
77AC: 8D         ADC     A,L             
77AD: 00         NOP                     
77AE: E3         ???                     
77AF: 00         NOP                     
77B0: FF         RST     0X38            
77B1: 78         LD      A,B             
77B2: B7         OR      A               
77B3: CC B3 FE   CALL    Z,$FEB3         
77B6: DB         ???                     
77B7: CE 3B      ADC     $3B             
77B9: 0E EE      LD      C,$EE           
77BB: 0E F1      LD      C,$F1           
77BD: 00         NOP                     
77BE: FF         RST     0X38            
77BF: 00         NOP                     
77C0: C0         RET     NZ              
77C1: 0F         RRCA                    
77C2: F0 00      LD      A,($00)         
77C4: FF         RST     0X38            
77C5: 00         NOP                     
77C6: CF         RST     0X08            
77C7: 00         NOP                     
77C8: FF         RST     0X38            
77C9: 00         NOP                     
77CA: FE 00      CP      $00             
77CC: FF         RST     0X38            
77CD: 00         NOP                     
77CE: FF         RST     0X38            
77CF: 00         NOP                     
77D0: 19         ADD     HL,DE           
77D1: 80         ADD     A,B             
77D2: 7F         LD      A,A             
77D3: 00         NOP                     
77D4: 87         ADD     A,A             
77D5: 78         LD      A,B             
77D6: 03         INC     BC              
77D7: FC         ???                     
77D8: 0F         RRCA                    
77D9: F0 01      LD      A,($01)         
77DB: FC         ???                     
77DC: 03         INC     BC              
77DD: 78         LD      A,B             
77DE: 87         ADD     A,A             
77DF: 00         NOP                     
77E0: CF         RST     0X08            
77E1: FE 7F      CP      $7F             
77E3: FE BE      CP      $BE             
77E5: 7F         LD      A,A             
77E6: 7C         LD      A,H             
77E7: 9F         SBC     A               
77E8: 37         SCF                     
77E9: F8 58      LDHL    SP,$58          
77EB: E0 A7      LDFF00  ($A7),A         
77ED: C0         RET     NZ              
77EE: 5C         LD      E,H             
77EF: 83         ADD     A,E             
77F0: F3         DI                      
77F1: 7F         LD      A,A             
77F2: FE 7F      CP      $7F             
77F4: 7D         LD      A,L             
77F5: FE 3E      CP      $3E             
77F7: F9         LD      SP,HL           
77F8: EC         ???                     
77F9: 1F         RRA                     
77FA: 1A         LD      A,(DE)          
77FB: 07         RLCA                    
77FC: E5         PUSH    HL              
77FD: 03         INC     BC              
77FE: 3A         LD      A,(HLD)         
77FF: C1         POP     BC              
7800: 38 38      JR      C,$783A         
7802: 46         LD      B,(HL)          
7803: 46         LD      B,(HL)          
7804: 99         SBC     C               
7805: 81         ADD     A,C             
7806: F0 88      LD      A,($88)         
7808: 7F         LD      A,A             
7809: 78         LD      A,B             
780A: 09         ADD     HL,BC           
780B: 0E 05      LD      C,$05           
780D: 06 73      LD      B,$73           
780F: 73         LD      (HL),E          
7810: 01 01 02   LD      BC,$0201        
7813: 02         LD      (BC),A          
7814: 06 04      LD      B,$04           
7816: C6 C4      ADD     $C4             
7818: 3F         CCF                     
7819: 3C         INC     A               
781A: 75         LD      (HL),L          
781B: 06 CA      LD      B,$CA           
781D: 65         LD      H,L             
781E: A5         AND     L               
781F: C8         RET     Z               
7820: 80         ADD     A,B             
7821: 80         ADD     A,B             
7822: 46         LD      B,(HL)          
7823: 46         LD      B,(HL)          
7824: 25         DEC     H               
7825: 25         DEC     H               
7826: 66         LD      H,(HL)          
7827: 24         INC     H               
7828: F2         ???                     
7829: 12         LD      (DE),A          
782A: DF         RST     0X18            
782B: 3C         INC     A               
782C: 2C         INC     L               
782D: D0         RET     NC              
782E: D5         PUSH    DE              
782F: 0A         LD      A,(BC)          
7830: 3C         INC     A               
7831: 3C         INC     A               
7832: 62         LD      H,D             
7833: 42         LD      B,D             
7834: 8D         ADC     A,L             
7835: 81         ADD     A,C             
7836: DE AE      SBC     $AE             
7838: 30 10      JR      NC,$784A        
783A: B0         OR      B               
783B: 10 10      STOP    $10             
783D: F0 20      LD      A,($20)         
783F: 60         LD      H,B             
7840: 01 01 01   LD      BC,$0101        
7843: 01 1F 1D   LD      BC,$1D1F        
7846: 37         SCF                     
7847: 23         INC     HL              
7848: 3E 21      LD      A,$21           
784A: 2F         CPL                     
784B: 30 10      JR      NC,$785D        
784D: 1F         RRA                     
784E: 1A         LD      A,(DE)          
784F: 0F         RRCA                    
7850: BF         CP      A               
7851: 5C         LD      E,H             
7852: BF         CP      A               
7853: 5E         LD      E,(HL)          
7854: BF         CP      A               
7855: 5F         LD      E,A             
7856: AF         XOR     A               
7857: 4F         LD      C,A             
7858: F3         DI                      
7859: 03         INC     BC              
785A: DD         ???                     
785B: 31 7F 9C   LD      SP,$9C7F        
785E: BF         CP      A               
785F: 1F         RRA                     
7860: FD         ???                     
7861: 3E FF      LD      A,$FF           
7863: 3F         CCF                     
7864: FF         RST     0X38            
7865: 7C         LD      A,H             
7866: FF         RST     0X38            
7867: 7C         LD      A,H             
7868: E7         RST     0X20            
7869: 60         LD      H,B             
786A: DE 41      SBC     $41             
786C: FF         RST     0X38            
786D: 0C         INC     C               
786E: FF         RST     0X38            
786F: FC         ???                     
7870: FF         RST     0X38            
7871: 39         ADD     HL,SP           
7872: C7         RST     0X00            
7873: C7         RST     0X00            
7874: 80         ADD     A,B             
7875: 80         ADD     A,B             
7876: F8 F8      LDHL    SP,$F8          
7878: CC 84 64   CALL    Z,$6484         
787B: 9C         SBC     H               
787C: 88         ADC     A,B             
787D: 78         LD      A,B             
787E: D8         RET     C               
787F: F0 F8      LD      A,($F8)         
7881: F8 FC      LDHL    SP,$FC          
7883: 44         LD      B,H             
7884: BF         CP      A               
7885: AF         XOR     A               
7886: 91         SUB     C               
7887: 91         SUB     C               
7888: C7         RST     0X00            
7889: 86         ADD     A,(HL)          
788A: FC         ???                     
788B: 98         SBC     B               
788C: F6 66      OR      $66             
788E: FE 2E      CP      $2E             
7890: 3F         CCF                     
7891: 3F         CCF                     
7892: 7F         LD      A,A             
7893: 44         LD      B,H             
7894: FA EA 12   LD      A,($12EA)       
7897: 12         LD      (DE),A          
7898: C6 C2      ADD     $C2             
789A: 7E         LD      A,(HL)          
789B: 32         LD      (HLD),A         
789C: DF         RST     0X18            
789D: CC FF E8   CALL    Z,$E8FF         
78A0: 00         NOP                     
78A1: 00         NOP                     
78A2: 3C         INC     A               
78A3: 3C         INC     A               
78A4: 66         LD      H,(HL)          
78A5: 42         LD      B,D             
78A6: D7         RST     0X10            
78A7: 81         ADD     A,C             
78A8: CA 81 A6   JP      Z,$A681         
78AB: D9         RETI                    
78AC: DA BD E7   JP      C,$E7BD         
78AF: A5         AND     L               
78B0: 00         NOP                     
78B1: 00         NOP                     
78B2: 78         LD      A,B             
78B3: 78         LD      A,B             
78B4: DC 84 8E   CALL    C,$8E84         
78B7: 02         LD      (BC),A          
78B8: D6 02      SUB     $02             
78BA: 4A         LD      C,D             
78BB: 36 B6      LD      (HL),$B6        
78BD: 7A         LD      A,D             
78BE: CE 4A      ADC     $4A             
78C0: 00         NOP                     
78C1: 00         NOP                     
78C2: 40         LD      B,B             
78C3: 00         NOP                     
78C4: 00         NOP                     
78C5: 3C         INC     A               
78C6: 24         INC     H               
78C7: 42         LD      B,D             
78C8: 7E         LD      A,(HL)          
78C9: 81         ADD     A,C             
78CA: 66         LD      H,(HL)          
78CB: 99         SBC     C               
78CC: 5B         LD      E,E             
78CD: A4         AND     H               
78CE: 69         LD      L,C             
78CF: 96         SUB     (HL)            
78D0: 00         NOP                     
78D1: 0C         INC     C               
78D2: 04         INC     B               
78D3: 12         LD      (DE),A          
78D4: 08 14 00   LD      ($0014),SP      
78D7: 14         INC     D               
78D8: 00         NOP                     
78D9: 14         INC     D               
78DA: 00         NOP                     
78DB: 08 00 80   LD      ($8000),SP      
78DE: 00         NOP                     
78DF: B8         CP      B               
78E0: 0F         RRCA                    
78E1: 0F         RRCA                    
78E2: 10 10      STOP    $10             
78E4: 20 20      JR      NZ,$7906        
78E6: 2F         CPL                     
78E7: 20 3F      JR      NZ,$7928        
78E9: 27         DAA                     
78EA: 3C         INC     A               
78EB: 2C         INC     L               
78EC: 3F         CCF                     
78ED: 2F         CPL                     
78EE: 79         LD      A,C             
78EF: 69         LD      L,C             
78F0: F0 F0      LD      A,($F0)         
78F2: 08 08 04   LD      ($0408),SP      
78F5: 04         INC     B               
78F6: F4         ???                     
78F7: 04         INC     B               
78F8: FC         ???                     
78F9: E4         ???                     
78FA: 3C         INC     A               
78FB: 34         INC     (HL)            
78FC: FC         ???                     
78FD: F4         ???                     
78FE: 9E         SBC     (HL)            
78FF: 96         SUB     (HL)            
7900: 88         ADC     A,B             
7901: 88         ADC     A,B             
7902: A4         AND     H               
7903: 84         ADD     A,H             
7904: 73         LD      (HL),E          
7905: 43         LD      B,E             
7906: 3A         LD      A,(HLD)         
7907: 20 2F      JR      NZ,$7938        
7909: 30 6D      JR      NC,$7978        
790B: 52         LD      D,D             
790C: FF         RST     0X38            
790D: 9C         SBC     H               
790E: E3         ???                     
790F: E3         ???                     
7910: A4         AND     H               
7911: C8         RET     Z               
7912: BA         CP      D               
7913: E4         ???                     
7914: C0         RET     NZ              
7915: C3 39 00   JP      $0039           
7918: 1C         INC     E               
7919: 01 F6 09   LD      BC,$09F6        
791C: 75         LD      (HL),L          
791D: 9A         SBC     D               
791E: FF         RST     0X38            
791F: EC         ???                     
7920: 12         LD      (DE),A          
7921: 09         ADD     HL,BC           
7922: 23         INC     HL              
7923: 11 C3 21   LD      DE,$21C3        
7926: 1B         DEC     DE              
7927: 05         DEC     B               
7928: 11 08 26   LD      DE,$2608        
792B: 10 EA      STOP    $EA             
792D: 14         INC     D               
792E: EB         ???                     
792F: 34         INC     (HL)            
7930: A0         AND     B               
7931: 60         LD      H,B             
7932: 40         LD      B,B             
7933: C0         RET     NZ              
7934: 8C         ADC     A,H             
7935: 8C         ADC     A,H             
7936: 14         INC     D               
7937: 14         INC     D               
7938: E8 E8      ADD     SP,$E8          
793A: 5C         LD      E,H             
793B: 0C         INC     C               
793C: FA 02 AD   LD      A,($AD02)       
793F: 51         LD      D,C             
7940: 16 0C      LD      D,$0C           
7942: 18 08      JR      $794C           
7944: 1C         INC     E               
7945: 10 33      STOP    $33             
7947: 10 33      STOP    $33             
7949: 20 3D      JR      NZ,$7988        
794B: 23         INC     HL              
794C: 3F         CCF                     
794D: 3E 00      LD      A,$00           
794F: 00         NOP                     
7950: 27         DAA                     
7951: 03         INC     BC              
7952: FD         ???                     
7953: 01 EC 10   LD      BC,$10EC        
7956: 96         SUB     (HL)            
7957: 78         LD      A,B             
7958: 77         LD      (HL),A          
7959: F8 8B      LDHL    SP,$8B          
795B: FC         ???                     
795C: FB         EI                      
795D: 0C         INC     C               
795E: 07         RLCA                    
795F: 07         RLCA                    
7960: C7         RST     0X00            
7961: C0         RET     NZ              
7962: BF         CP      A               
7963: 80         ADD     A,B             
7964: 63         LD      H,E             
7965: 1C         INC     E               
7966: DB         ???                     
7967: 3C         INC     A               
7968: E7         RST     0X20            
7969: 3F         CCF                     
796A: BF         CP      A               
796B: 60         LD      H,B             
796C: 60         LD      H,B             
796D: C0         RET     NZ              
796E: C0         RET     NZ              
796F: 80         ADD     A,B             
7970: E8 30      ADD     SP,$30          
7972: 18 10      JR      $7984           
7974: 38 08      JR      C,$797E         
7976: C4 04 44   CALL    NZ,$4404        
7979: 84         ADD     A,H             
797A: FC         ???                     
797B: C4 7C 3C   CALL    NZ,$3C7C        
797E: 00         NOP                     
797F: 00         NOP                     
7980: FC         ???                     
7981: 2C         INC     L               
7982: B1         OR      C               
7983: 60         LD      H,B             
7984: FC         ???                     
7985: E5         PUSH    HL              
7986: 9C         SBC     H               
7987: 9D         SBC     L               
7988: 44         LD      B,H             
7989: C5         PUSH    BC              
798A: BC         CP      H               
798B: 9C         SBC     H               
798C: 6D         LD      L,L             
798D: F5         PUSH    AF              
798E: FB         EI                      
798F: 07         RLCA                    
7990: 7F         LD      A,A             
7991: 68         LD      L,B             
7992: 1B         DEC     DE              
7993: 0C         INC     C               
7994: 7C         LD      A,H             
7995: 4F         LD      C,A             
7996: 70         LD      (HL),B          
7997: 72         LD      (HL),D          
7998: 44         LD      B,H             
7999: 46         LD      B,(HL)          
799A: 7B         LD      A,E             
799B: 72         LD      (HL),D          
799C: 6D         LD      L,L             
799D: 5E         LD      E,(HL)          
799E: BF         CP      A               
799F: C0         RET     NZ              
79A0: E7         RST     0X20            
79A1: A5         AND     L               
79A2: BE         CP      (HL)            
79A3: FD         ???                     
79A4: FF         RST     0X38            
79A5: A5         AND     L               
79A6: E7         RST     0X20            
79A7: BD         CP      L               
79A8: FE BD      CP      $BD             
79AA: FF         RST     0X38            
79AB: A5         AND     L               
79AC: E6 E7      AND     $E7             
79AE: 00         NOP                     
79AF: 00         NOP                     
79B0: CE 4A      ADC     $4A             
79B2: FE 7A      CP      $7A             
79B4: FE 4A      CP      $4A             
79B6: 4A         LD      C,D             
79B7: FE FE      CP      $FE             
79B9: 7A         LD      A,D             
79BA: CE 7A      ADC     $7A             
79BC: C6 CE      ADD     $CE             
79BE: 00         NOP                     
79BF: 00         NOP                     
79C0: 39         ADD     HL,SP           
79C1: 46         LD      B,(HL)          
79C2: 01 3A 01   LD      BC,$013A        
79C5: 02         LD      (BC),A          
79C6: 01 62 41   LD      BC,$4162        
79C9: 92         SUB     D               
79CA: 20 D2      JR      NZ,$799E        
79CC: 00         NOP                     
79CD: 52         LD      D,D             
79CE: 00         NOP                     
79CF: 61         LD      H,C             
79D0: 28 C4      JR      Z,$7996         
79D2: 68         LD      L,B             
79D3: 94         SUB     H               
79D4: D8         RET     C               
79D5: 24         INC     H               
79D6: 80         ADD     A,B             
79D7: 78         LD      A,B             
79D8: 00         NOP                     
79D9: 40         LD      B,B             
79DA: 00         NOP                     
79DB: 40         LD      B,B             
79DC: 00         NOP                     
79DD: 40         LD      B,B             
79DE: 01 80 BF   LD      BC,$BF80        
79E1: AF         XOR     A               
79E2: BA         CP      D               
79E3: AA         XOR     D               
79E4: BF         CP      A               
79E5: AF         XOR     A               
79E6: BF         CP      A               
79E7: A0         AND     B               
79E8: BF         CP      A               
79E9: BF         CP      A               
79EA: 80         ADD     A,B             
79EB: 80         ADD     A,B             
79EC: FF         RST     0X38            
79ED: 98         SBC     B               
79EE: 67         LD      H,A             
79EF: 67         LD      H,A             
79F0: FD         ???                     
79F1: F5         PUSH    AF              
79F2: 5D         LD      E,L             
79F3: 55         LD      D,L             
79F4: FD         ???                     
79F5: F5         PUSH    AF              
79F6: FD         ???                     
79F7: 05         DEC     B               
79F8: FD         ???                     
79F9: FD         ???                     
79FA: 01 01 FF   LD      BC,$FF01        
79FD: 19         ADD     HL,DE           
79FE: E6 E6      AND     $E6             
7A00: FF         RST     0X38            
7A01: F0 9F      LD      A,($9F)         
7A03: 98         SBC     B               
7A04: EC         ???                     
7A05: 4C         LD      C,H             
7A06: E7         RST     0X20            
7A07: 24         INC     H               
7A08: E5         PUSH    HL              
7A09: 24         INC     H               
7A0A: E6 24      AND     $24             
7A0C: EF         RST     0X28            
7A0D: 24         INC     H               
7A0E: CF         RST     0X08            
7A0F: 49         LD      C,C             
7A10: FF         RST     0X38            
7A11: 00         NOP                     
7A12: 87         ADD     A,A             
7A13: 00         NOP                     
7A14: 60         LD      H,B             
7A15: 00         NOP                     
7A16: FF         RST     0X38            
7A17: 00         NOP                     
7A18: FF         RST     0X38            
7A19: 39         ADD     HL,SP           
7A1A: 7E         LD      A,(HL)          
7A1B: 47         LD      B,A             
7A1C: 8C         ADC     A,H             
7A1D: F3         DI                      
7A1E: E6 F9      AND     $F9             
7A20: FF         RST     0X38            
7A21: 00         NOP                     
7A22: FF         RST     0X38            
7A23: 0F         RRCA                    
7A24: FF         RST     0X38            
7A25: 30 FF      JR      NC,$7A26        
7A27: C0         RET     NZ              
7A28: F8 07      LDHL    SP,$07          
7A2A: C0         RET     NZ              
7A2B: 3F         CCF                     
7A2C: 00         NOP                     
7A2D: FF         RST     0X38            
7A2E: 0F         RRCA                    
7A2F: FF         RST     0X38            
7A30: FF         RST     0X38            
7A31: 00         NOP                     
7A32: FF         RST     0X38            
7A33: F0 FE      LD      A,($FE)         
7A35: 0C         INC     C               
7A36: FF         RST     0X38            
7A37: 03         INC     BC              
7A38: 1F         RRA                     
7A39: E0 03      LDFF00  ($03),A         
7A3B: FC         ???                     
7A3C: 00         NOP                     
7A3D: FF         RST     0X38            
7A3E: F0 FF      LD      A,($FF)         
7A40: C7         RST     0X00            
7A41: 00         NOP                     
7A42: 83         ADD     A,E             
7A43: 00         NOP                     
7A44: 38 00      JR      C,$7A46         
7A46: FF         RST     0X38            
7A47: 00         NOP                     
7A48: FF         RST     0X38            
7A49: 9C         SBC     H               
7A4A: 7F         LD      A,A             
7A4B: E2         LDFF00  (C),A           
7A4C: 31 CF 67   LD      SP,$67CF        
7A4F: 9F         SBC     A               
7A50: FF         RST     0X38            
7A51: 0F         RRCA                    
7A52: F9         LD      SP,HL           
7A53: 19         ADD     HL,DE           
7A54: 76         HALT                    
7A55: 32         LD      (HLD),A         
7A56: E4         ???                     
7A57: 24         INC     H               
7A58: E4         ???                     
7A59: 24         INC     H               
7A5A: 24         INC     H               
7A5B: 24         INC     H               
7A5C: F4         ???                     
7A5D: 24         INC     H               
7A5E: F2         ???                     
7A5F: 92         SUB     D               
7A60: E2         LDFF00  (C),A           
7A61: 43         LD      B,E             
7A62: F1         POP     AF              
7A63: 21 F9 10   LD      HL,$10F9        
7A66: FE 38      CP      $38             
7A68: C6 44      ADD     $44             
7A6A: 87         ADD     A,A             
7A6B: 84         ADD     A,H             
7A6C: 83         ADD     A,E             
7A6D: 82         ADD     A,D             
7A6E: 81         ADD     A,C             
7A6F: 81         ADD     A,C             
7A70: 10 F0      STOP    $F0             
7A72: F1         POP     AF              
7A73: F0 61      LD      A,($61)         
7A75: 60         LD      H,B             
7A76: 61         LD      H,C             
7A77: 21 E1 21   LD      HL,$21E1        
7A7A: E3         ???                     
7A7B: 21 C3 41   LD      HL,$41C3        
7A7E: 83         ADD     A,E             
7A7F: 83         ADD     A,E             
7A80: 08 0F 8F   LD      ($8F0F),SP      
7A83: 0F         RRCA                    
7A84: 86         ADD     A,(HL)          
7A85: 06 86      LD      B,$86           
7A87: 84         ADD     A,H             
7A88: 87         ADD     A,A             
7A89: 84         ADD     A,H             
7A8A: C7         RST     0X00            
7A8B: 84         ADD     A,H             
7A8C: C3 82 C1   JP      $C182           
7A8F: C1         POP     BC              
7A90: 47         LD      B,A             
7A91: C2 8F 84   JP      NZ,$848F        
7A94: 9F         SBC     A               
7A95: 08 7F 1C   LD      ($1C7F),SP      
7A98: 63         LD      H,E             
7A99: 22         LD      (HLI),A         
7A9A: E1         POP     HL              
7A9B: 21 C1 41   LD      HL,$41C1        
7A9E: 81         ADD     A,C             
7A9F: 81         ADD     A,C             
7AA0: FF         RST     0X38            
7AA1: 1E E1      LD      E,$E1           
7AA3: 21 C0 43   LD      HL,$43C0        
7AA6: C0         RET     NZ              
7AA7: 44         LD      B,H             
7AA8: C0         RET     NZ              
7AA9: 48         LD      C,B             
7AAA: E0 A9      LDFF00  ($A9),A         
7AAC: F0 98      LD      A,($98)         
7AAE: FC         ???                     
7AAF: 9C         SBC     H               
7AB0: FF         RST     0X38            
7AB1: 78         LD      A,B             
7AB2: 97         SUB     A               
7AB3: 84         ADD     A,H             
7AB4: 03         INC     BC              
7AB5: 02         LD      (BC),A          
7AB6: 03         INC     BC              
7AB7: E2         LDFF00  (C),A           
7AB8: 07         RLCA                    
7AB9: 16 0B      LD      D,$0B           
7ABB: 0E 09      LD      C,$09           
7ABD: 0F         RRCA                    
7ABE: 39         ADD     HL,SP           
7ABF: 3F         CCF                     
7AC0: FF         RST     0X38            
7AC1: 87         ADD     A,A             
7AC2: FF         RST     0X38            
7AC3: F8 FF      LDHL    SP,$FF          
7AC5: 80         ADD     A,B             
7AC6: F8 C7      LDHL    SP,$C7          
7AC8: C7         RST     0X00            
7AC9: 78         LD      A,B             
7ACA: FF         RST     0X38            
7ACB: 43         LD      B,E             
7ACC: FF         RST     0X38            
7ACD: FE FF      CP      $FF             
7ACF: 80         ADD     A,B             
7AD0: FF         RST     0X38            
7AD1: E1         POP     HL              
7AD2: FF         RST     0X38            
7AD3: 1F         RRA                     
7AD4: FF         RST     0X38            
7AD5: 01 79 87   LD      BC,$8779        
7AD8: CF         RST     0X08            
7AD9: 31 FF FF   LD      SP,$FFFF        
7ADC: FF         RST     0X38            
7ADD: 02         LD      (BC),A          
7ADE: E3         ???                     
7ADF: 1E DB      LD      E,$DB           
7AE1: 18 AD      JR      $7A90           
7AE3: 2C         INC     L               
7AE4: 4A         LD      C,D             
7AE5: 4E         LD      C,(HL)          
7AE6: 89         ADC     A,C             
7AE7: 8F         ADC     A,A             
7AE8: 99         SBC     C               
7AE9: 9F         SBC     A               
7AEA: BD         CP      L               
7AEB: A7         AND     A               
7AEC: 7E         LD      A,(HL)          
7AED: 42         LD      B,D             
7AEE: BD         CP      L               
7AEF: 3C         INC     A               
7AF0: 02         LD      (BC),A          
7AF1: 00         NOP                     
7AF2: 22         LD      (HLI),A         
7AF3: 00         NOP                     
7AF4: 02         LD      (BC),A          
7AF5: 00         NOP                     
7AF6: 82         ADD     A,D             
7AF7: 00         NOP                     
7AF8: 0A         LD      A,(BC)          
7AF9: 00         NOP                     
7AFA: 02         LD      (BC),A          
7AFB: 00         NOP                     
7AFC: FC         ???                     
7AFD: 00         NOP                     
7AFE: 00         NOP                     
7AFF: 00         NOP                     
7B00: 5B         LD      E,E             
7B01: 4A         LD      C,D             
7B02: D3         ???                     
7B03: 92         SUB     D               
7B04: D7         RST     0X10            
7B05: 94         SUB     H               
7B06: D7         RST     0X10            
7B07: 94         SUB     H               
7B08: D7         RST     0X10            
7B09: 94         SUB     H               
7B0A: DF         RST     0X18            
7B0B: 9C         SBC     H               
7B0C: CD 8E C4   CALL    $C48E           
7B0F: 47         LD      B,A             
7B10: 92         SUB     D               
7B11: 1D         DEC     E               
7B12: 09         ADD     HL,BC           
7B13: 0F         RRCA                    
7B14: 0A         LD      A,(BC)          
7B15: 0E 0C      LD      C,$0C           
7B17: 0C         INC     C               
7B18: 0C         INC     C               
7B19: 0C         INC     C               
7B1A: B8         CP      B               
7B1B: 38 E8      JR      C,$7B05         
7B1D: 28 F8      JR      Z,$7B17         
7B1F: 38 70      JR      C,$7B91         
7B21: F0 80      LD      A,($80)         
7B23: 80         ADD     A,B             
7B24: 00         NOP                     
7B25: 00         NOP                     
7B26: 0F         RRCA                    
7B27: 00         NOP                     
7B28: 3F         CCF                     
7B29: 07         RLCA                    
7B2A: 7F         LD      A,A             
7B2B: 18 F0      JR      $7B1D           
7B2D: 20 E1      JR      NZ,$7B10        
7B2F: 61         LD      H,C             
7B30: 0E 0F      LD      C,$0F           
7B32: 01 01 00   LD      BC,$0001        
7B35: 00         NOP                     
7B36: F0 00      LD      A,($00)         
7B38: FC         ???                     
7B39: E0 FE      LDFF00  ($FE),A         
7B3B: 18 0F      JR      $7B4C           
7B3D: 04         INC     B               
7B3E: 87         ADD     A,A             
7B3F: 86         ADD     A,(HL)          
7B40: 49         LD      C,C             
7B41: B8         CP      B               
7B42: 90         SUB     B               
7B43: F0 50      LD      A,($50)         
7B45: 70         LD      (HL),B          
7B46: 30 30      JR      NC,$7B78        
7B48: 30 30      JR      NC,$7B7A        
7B4A: 1D         DEC     E               
7B4B: 1C         INC     E               
7B4C: 17         RLA                     
7B4D: 14         INC     D               
7B4E: 1F         RRA                     
7B4F: 1C         INC     E               
7B50: DA 52 CB   JP      C,$CB52         
7B53: 49         LD      C,C             
7B54: EB         ???                     
7B55: 29         ADD     HL,HL           
7B56: EB         ???                     
7B57: 29         ADD     HL,HL           
7B58: EB         ???                     
7B59: 29         ADD     HL,HL           
7B5A: FB         EI                      
7B5B: 39         ADD     HL,SP           
7B5C: B3         OR      E               
7B5D: 71         LD      (HL),C          
7B5E: 23         INC     HL              
7B5F: E2         LDFF00  (C),A           
7B60: B8         CP      B               
7B61: A0         AND     B               
7B62: DC 90 6E   CALL    C,$6E90         
7B65: 48         LD      C,B             
7B66: 5B         LD      E,E             
7B67: 6C         LD      L,H             
7B68: 39         ADD     HL,SP           
7B69: 3E 84      LD      A,$84           
7B6B: 07         RLCA                    
7B6C: F3         DI                      
7B6D: 03         INC     BC              
7B6E: F8 00      LDHL    SP,$00          
7B70: 03         INC     BC              
7B71: 03         INC     BC              
7B72: 07         RLCA                    
7B73: 03         INC     BC              
7B74: 0F         RRCA                    
7B75: 03         INC     BC              
7B76: FB         EI                      
7B77: 07         RLCA                    
7B78: F3         DI                      
7B79: 0F         RRCA                    
7B7A: 04         INC     B               
7B7B: FC         ???                     
7B7C: F8 F8      LDHL    SP,$F8          
7B7E: 07         RLCA                    
7B7F: 00         NOP                     
7B80: C0         RET     NZ              
7B81: C0         RET     NZ              
7B82: E0 C0      LDFF00  ($C0),A         
7B84: F0 C0      LD      A,($C0)         
7B86: DF         RST     0X18            
7B87: E0 CF      LDFF00  ($CF),A         
7B89: F0 20      LD      A,($20)         
7B8B: 3F         CCF                     
7B8C: 1F         RRA                     
7B8D: 1F         RRA                     
7B8E: C0         RET     NZ              
7B8F: 00         NOP                     
7B90: 1D         DEC     E               
7B91: 05         DEC     B               
7B92: 3B         DEC     SP              
7B93: 09         ADD     HL,BC           
7B94: 76         HALT                    
7B95: 12         LD      (DE),A          
7B96: DA 36 9C   JP      C,$9C36         
7B99: 7C         LD      A,H             
7B9A: 21 E0 CF   LD      HL,$CFE0        
7B9D: C0         RET     NZ              
7B9E: 1F         RRA                     
7B9F: 00         NOP                     
7BA0: FF         RST     0X38            
7BA1: 97         SUB     A               
7BA2: FF         RST     0X38            
7BA3: B2         OR      D               
7BA4: FF         RST     0X38            
7BA5: D2 FF 8A   JP      NC,$8AFF        
7BA8: 7F         LD      A,A             
7BA9: 44         LD      B,H             
7BAA: 3F         CCF                     
7BAB: 24         INC     H               
7BAC: 9F         SBC     A               
7BAD: 1F         RRA                     
7BAE: E0 00      LDFF00  ($00),A         
7BB0: E9         JP      (HL)            
7BB1: FF         RST     0X38            
7BB2: C9         RET                     
7BB3: 7F         LD      A,A             
7BB4: C9         RET                     
7BB5: 7F         LD      A,A             
7BB6: DD         ???                     
7BB7: 77         LD      (HL),A          
7BB8: FE 22      CP      $22             
7BBA: FC         ???                     
7BBB: 2C         INC     L               
7BBC: F9         LD      SP,HL           
7BBD: F8 03      LDHL    SP,$03          
7BBF: 00         NOP                     
7BC0: 87         ADD     A,A             
7BC1: F8 FF      LDHL    SP,$FF          
7BC3: C1         POP     BC              
7BC4: FE 7F      CP      $7F             
7BC6: FF         RST     0X38            
7BC7: 41         LD      B,C             
7BC8: 8F         ADC     A,A             
7BC9: F0 FC      LD      A,($FC)         
7BCB: 83         ADD     A,E             
7BCC: FF         RST     0X38            
7BCD: FC         ???                     
7BCE: FF         RST     0X38            
7BCF: C3 FF 01   JP      $01FF           
7BD2: FF         RST     0X38            
7BD3: F1         POP     AF              
7BD4: EF         RST     0X28            
7BD5: 1E FF      LD      E,$FF           
7BD7: F1         POP     AF              
7BD8: FF         RST     0X38            
7BD9: 01 73 8F   LD      BC,$8F73        
7BDC: FF         RST     0X38            
7BDD: 01 FF FF   LD      BC,$FFFF        
7BE0: E7         RST     0X20            
7BE1: 00         NOP                     
7BE2: DB         ???                     
7BE3: 18 A5      JR      $7B8A           
7BE5: 24         INC     H               
7BE6: 4E         LD      C,(HL)          
7BE7: 4A         LD      C,D             
7BE8: 4E         LD      C,(HL)          
7BE9: 4A         LD      C,D             
7BEA: 5E         LD      E,(HL)          
7BEB: 52         LD      D,D             
7BEC: BD         CP      L               
7BED: 3C         INC     A               
7BEE: C3 00 C3   JP      $C300           
7BF1: FF         RST     0X38            
7BF2: 81         ADD     A,C             
7BF3: FF         RST     0X38            
7BF4: 00         NOP                     
7BF5: FF         RST     0X38            
7BF6: 00         NOP                     
7BF7: FF         RST     0X38            
7BF8: 3C         INC     A               
7BF9: C3 C3 81   JP      $81C3           
7BFC: 7E         LD      A,(HL)          
7BFD: 7E         LD      A,(HL)          
7BFE: 81         ADD     A,C             
7BFF: 00         NOP                     
7C00: FF         RST     0X38            
7C01: 00         NOP                     
7C02: FF         RST     0X38            
7C03: 00         NOP                     
7C04: FF         RST     0X38            
7C05: 03         INC     BC              
7C06: FE 0C      CP      $0C             
7C08: F8 10      LDHL    SP,$10          
7C0A: F0 20      LD      A,($20)         
7C0C: C0         RET     NZ              
7C0D: 40         LD      B,B             
7C0E: 80         ADD     A,B             
7C0F: 80         ADD     A,B             
7C10: FF         RST     0X38            
7C11: 0F         RRCA                    
7C12: FF         RST     0X38            
7C13: 70         LD      (HL),B          
7C14: DF         RST     0X18            
7C15: 80         ADD     A,B             
7C16: 0F         RRCA                    
7C17: 00         NOP                     
7C18: 03         INC     BC              
7C19: 00         NOP                     
7C1A: 00         NOP                     
7C1B: 00         NOP                     
7C1C: 00         NOP                     
7C1D: 00         NOP                     
7C1E: 00         NOP                     
7C1F: 00         NOP                     
7C20: FF         RST     0X38            
7C21: F0 FF      LD      A,($FF)         
7C23: 0F         RRCA                    
7C24: F9         LD      SP,HL           
7C25: 00         NOP                     
7C26: F0 00      LD      A,($00)         
7C28: C0         RET     NZ              
7C29: 00         NOP                     
7C2A: 00         NOP                     
7C2B: 00         NOP                     
7C2C: 00         NOP                     
7C2D: 00         NOP                     
7C2E: 00         NOP                     
7C2F: 00         NOP                     
7C30: FF         RST     0X38            
7C31: 00         NOP                     
7C32: FF         RST     0X38            
7C33: 00         NOP                     
7C34: FF         RST     0X38            
7C35: C0         RET     NZ              
7C36: 7F         LD      A,A             
7C37: 30 1F      JR      NC,$7C58        
7C39: 08 07 04   LD      ($0407),SP      
7C3C: 03         INC     BC              
7C3D: 02         LD      (BC),A          
7C3E: 01 01 C0   LD      BC,$C001        
7C41: 80         ADD     A,B             
7C42: C0         RET     NZ              
7C43: 80         ADD     A,B             
7C44: C0         RET     NZ              
7C45: 80         ADD     A,B             
7C46: C0         RET     NZ              
7C47: 80         ADD     A,B             
7C48: C0         RET     NZ              
7C49: 80         ADD     A,B             
7C4A: C0         RET     NZ              
7C4B: 80         ADD     A,B             
7C4C: C0         RET     NZ              
7C4D: 80         ADD     A,B             
7C4E: C0         RET     NZ              
7C4F: 80         ADD     A,B             
7C50: 03         INC     BC              
7C51: 01 03 01   LD      BC,$0103        
7C54: 03         INC     BC              
7C55: 01 03 01   LD      BC,$0103        
7C58: 03         INC     BC              
7C59: 01 03 01   LD      BC,$0103        
7C5C: 03         INC     BC              
7C5D: 01 03 01   LD      BC,$0103        
7C60: FF         RST     0X38            
7C61: 00         NOP                     
7C62: FB         EI                      
7C63: 07         RLCA                    
7C64: EC         ???                     
7C65: 1F         RRA                     
7C66: D0         RET     NC              
7C67: 3F         CCF                     
7C68: E3         ???                     
7C69: 3C         INC     A               
7C6A: A7         AND     A               
7C6B: 78         LD      A,B             
7C6C: C7         RST     0X00            
7C6D: 78         LD      A,B             
7C6E: 47         LD      B,A             
7C6F: F8 FF      LDHL    SP,$FF          
7C71: 00         NOP                     
7C72: DF         RST     0X18            
7C73: E0 37      LDFF00  ($37),A         
7C75: F8 0B      LDHL    SP,$0B          
7C77: FC         ???                     
7C78: C7         RST     0X00            
7C79: 3C         INC     A               
7C7A: E5         PUSH    HL              
7C7B: 1E E3      LD      E,$E3           
7C7D: 1E E2      LD      E,$E2           
7C7F: 1F         RRA                     
7C80: 1E 1E      LD      E,$1E           
7C82: 21 21 50   LD      HL,$5021        
7C85: 43         LD      B,E             
7C86: 41         LD      B,C             
7C87: 44         LD      B,H             
7C88: C0         RET     NZ              
7C89: 48         LD      C,B             
7C8A: E0 A9      LDFF00  ($A9),A         
7C8C: F0 98      LD      A,($98)         
7C8E: F8 98      LDHL    SP,$98          
7C90: 78         LD      A,B             
7C91: 78         LD      A,B             
7C92: 84         ADD     A,H             
7C93: 84         ADD     A,H             
7C94: 12         LD      (DE),A          
7C95: 02         LD      (BC),A          
7C96: 02         LD      (BC),A          
7C97: E2         LDFF00  (C),A           
7C98: 07         RLCA                    
7C99: 12         LD      (DE),A          
7C9A: 0D         DEC     C               
7C9B: 0F         RRCA                    
7C9C: 09         ADD     HL,BC           
7C9D: 0F         RRCA                    
7C9E: 19         ADD     HL,DE           
7C9F: 5F         LD      E,A             
7CA0: FC         ???                     
7CA1: 00         NOP                     
7CA2: F8 00      LDHL    SP,$00          
7CA4: F8 00      LDHL    SP,$00          
7CA6: F8 00      LDHL    SP,$00          
7CA8: C0         RET     NZ              
7CA9: 00         NOP                     
7CAA: 80         ADD     A,B             
7CAB: 00         NOP                     
7CAC: 80         ADD     A,B             
7CAD: 00         NOP                     
7CAE: 80         ADD     A,B             
7CAF: 00         NOP                     
7CB0: 67         LD      H,A             
7CB1: F8 63      LDHL    SP,$63          
7CB3: FC         ???                     
7CB4: B1         OR      C               
7CB5: 7E         LD      A,(HL)          
7CB6: B8         CP      B               
7CB7: 7F         LD      A,A             
7CB8: DC 3F 6E   CALL    C,$6E3F         
7CBB: 1F         RRA                     
7CBC: 37         SCF                     
7CBD: 0F         RRCA                    
7CBE: 1B         DEC     DE              
7CBF: 07         RLCA                    
7CC0: E6 1F      AND     $1F             
7CC2: C6 3F      ADD     $3F             
7CC4: 8D         ADC     A,L             
7CC5: 7E         LD      A,(HL)          
7CC6: 1D         DEC     E               
7CC7: FE 3B      CP      $3B             
7CC9: FC         ???                     
7CCA: 76         HALT                    
7CCB: F8 EC      LDHL    SP,$EC          
7CCD: F0 D8      LD      A,($D8)         
7CCF: E0 07      LDFF00  ($07),A         
7CD1: FF         RST     0X38            
7CD2: F9         LD      SP,HL           
7CD3: F8 41      LDHL    SP,$41          
7CD5: 88         ADC     A,B             
7CD6: 45         LD      B,L             
7CD7: 88         ADC     A,B             
7CD8: 54         LD      D,H             
7CD9: 88         ADC     A,B             
7CDA: 54         LD      D,H             
7CDB: 88         ADC     A,B             
7CDC: 15         DEC     D               
7CDD: 88         ADC     A,B             
7CDE: 15         DEC     D               
7CDF: 88         ADC     A,B             
7CE0: 3C         INC     A               
7CE1: 00         NOP                     
7CE2: 7E         LD      A,(HL)          
7CE3: 00         NOP                     
7CE4: FF         RST     0X38            
7CE5: 00         NOP                     
7CE6: FF         RST     0X38            
7CE7: 00         NOP                     
7CE8: FF         RST     0X38            
7CE9: 00         NOP                     
7CEA: FF         RST     0X38            
7CEB: 00         NOP                     
7CEC: 7E         LD      A,(HL)          
7CED: 00         NOP                     
7CEE: 3C         INC     A               
7CEF: 00         NOP                     
7CF0: 00         NOP                     
7CF1: 00         NOP                     
7CF2: 00         NOP                     
7CF3: 00         NOP                     
7CF4: 18 18      JR      $7D0E           
7CF6: 3C         INC     A               
7CF7: 3C         INC     A               
7CF8: 7E         LD      A,(HL)          
7CF9: 7E         LD      A,(HL)          
7CFA: FF         RST     0X38            
7CFB: FF         RST     0X38            
7CFC: FF         RST     0X38            
7CFD: FF         RST     0X38            
7CFE: FF         RST     0X38            
7CFF: FF         RST     0X38            
7D00: FF         RST     0X38            
7D01: 01 FE 02   LD      BC,$02FE        
7D04: FF         RST     0X38            
7D05: 04         INC     B               
7D06: FF         RST     0X38            
7D07: 04         INC     B               
7D08: FF         RST     0X38            
7D09: 08 FF 08   LD      ($08FF),SP      
7D0C: EE 10      XOR     $10             
7D0E: FE 10      CP      $10             
7D10: FF         RST     0X38            
7D11: 80         ADD     A,B             
7D12: FF         RST     0X38            
7D13: 40         LD      B,B             
7D14: 7F         LD      A,A             
7D15: 20 3F      JR      NZ,$7D56        
7D17: 20 3F      JR      NZ,$7D58        
7D19: 10 1F      STOP    $1F             
7D1B: 10 1F      STOP    $1F             
7D1D: 08 0F 08   LD      ($080F),SP      
7D20: FC         ???                     
7D21: F0 30      LD      A,($30)         
7D23: E0 E0      LDFF00  ($E0),A         
7D25: 20 60      JR      NZ,$7D87        
7D27: 20 E0      JR      NZ,$7D09        
7D29: 40         LD      B,B             
7D2A: C0         RET     NZ              
7D2B: 40         LD      B,B             
7D2C: C0         RET     NZ              
7D2D: C0         RET     NZ              
7D2E: C0         RET     NZ              
7D2F: C0         RET     NZ              
7D30: 0F         RRCA                    
7D31: 0F         RRCA                    
7D32: 1C         INC     E               
7D33: 07         RLCA                    
7D34: 3F         CCF                     
7D35: 04         INC     B               
7D36: 3E 04      LD      A,$04           
7D38: 3F         CCF                     
7D39: 02         LD      (BC),A          
7D3A: 3F         CCF                     
7D3B: 02         LD      (BC),A          
7D3C: 1F         RRA                     
7D3D: 03         INC     BC              
7D3E: 0F         RRCA                    
7D3F: 03         INC     BC              
7D40: E0 80      LDFF00  ($80),A         
7D42: E0 80      LDFF00  ($80),A         
7D44: A0         AND     B               
7D45: C0         RET     NZ              
7D46: F0 C0      LD      A,($C0)         
7D48: F0 C0      LD      A,($C0)         
7D4A: D8         RET     C               
7D4B: E0 DC      LDFF00  ($DC),A         
7D4D: E0 EF      LDFF00  ($EF),A         
7D4F: F0 07      LD      A,($07)         
7D51: 01 07 01   LD      BC,$0107        
7D54: 05         DEC     B               
7D55: 03         INC     BC              
7D56: 0F         RRCA                    
7D57: 03         INC     BC              
7D58: 0F         RRCA                    
7D59: 03         INC     BC              
7D5A: 1B         DEC     DE              
7D5B: 07         RLCA                    
7D5C: 3B         DEC     SP              
7D5D: 07         RLCA                    
7D5E: F7         RST     0X30            
7D5F: 0F         RRCA                    
7D60: 00         NOP                     
7D61: FF         RST     0X38            
7D62: 07         RLCA                    
7D63: FF         RST     0X38            
7D64: 1C         INC     E               
7D65: FF         RST     0X38            
7D66: 30 FF      JR      NC,$7D67        
7D68: 63         LD      H,E             
7D69: FC         ???                     
7D6A: 67         LD      H,A             
7D6B: F8 C7      LDHL    SP,$C7          
7D6D: F8 C7      LDHL    SP,$C7          
7D6F: F8 00      LDHL    SP,$00          
7D71: FF         RST     0X38            
7D72: E0 FF      LDFF00  ($FF),A         
7D74: 38 FF      JR      C,$7D75         
7D76: 0C         INC     C               
7D77: FF         RST     0X38            
7D78: C6 3F      ADD     $3F             
7D7A: E6 1F      AND     $1F             
7D7C: E3         ???                     
7D7D: 1F         RRA                     
7D7E: E3         ???                     
7D7F: 1F         RRA                     
7D80: FC         ???                     
7D81: A4         AND     H               
7D82: FF         RST     0X38            
7D83: A7         AND     A               
7D84: FF         RST     0X38            
7D85: A2         AND     D               
7D86: FF         RST     0X38            
7D87: D2 FF 8A   JP      NC,$8AFF        
7D8A: 7F         LD      A,A             
7D8B: 44         LD      B,H             
7D8C: 3F         CCF                     
7D8D: 24         INC     H               
7D8E: 1F         RRA                     
7D8F: 1F         RRA                     
7D90: 29         ADD     HL,HL           
7D91: 3F         CCF                     
7D92: C9         RET                     
7D93: FF         RST     0X38            
7D94: C9         RET                     
7D95: 7F         LD      A,A             
7D96: C9         RET                     
7D97: 7F         LD      A,A             
7D98: DD         ???                     
7D99: 77         LD      (HL),A          
7D9A: FE 22      CP      $22             
7D9C: FC         ???                     
7D9D: 2C         INC     L               
7D9E: F9         LD      SP,HL           
7D9F: F8 3F      LDHL    SP,$3F          
7DA1: 00         NOP                     
7DA2: 1F         RRA                     
7DA3: 00         NOP                     
7DA4: 0F         RRCA                    
7DA5: 00         NOP                     
7DA6: 0F         RRCA                    
7DA7: 00         NOP                     
7DA8: 0F         RRCA                    
7DA9: 00         NOP                     
7DAA: 0F         RRCA                    
7DAB: 00         NOP                     
7DAC: 03         INC     BC              
7DAD: 00         NOP                     
7DAE: 01 00 C0   LD      BC,$C000        
7DB1: 00         NOP                     
7DB2: F0 00      LD      A,($00)         
7DB4: FF         RST     0X38            
7DB5: 00         NOP                     
7DB6: 7F         LD      A,A             
7DB7: 80         ADD     A,B             
7DB8: 1F         RRA                     
7DB9: E0 07      LDFF00  ($07),A         
7DBB: F8 80      LDHL    SP,$80          
7DBD: FF         RST     0X38            
7DBE: C0         RET     NZ              
7DBF: FF         RST     0X38            
7DC0: 03         INC     BC              
7DC1: 00         NOP                     
7DC2: 0F         RRCA                    
7DC3: 00         NOP                     
7DC4: FF         RST     0X38            
7DC5: 00         NOP                     
7DC6: FE 01      CP      $01             
7DC8: F8 07      LDHL    SP,$07          
7DCA: E0 1F      LDFF00  ($1F),A         
7DCC: 01 FF 03   LD      BC,$03FF        
7DCF: FF         RST     0X38            
7DD0: 51         LD      D,C             
7DD1: 88         ADC     A,B             
7DD2: 51         LD      D,C             
7DD3: 88         ADC     A,B             
7DD4: 45         LD      B,L             
7DD5: 88         ADC     A,B             
7DD6: 40         LD      B,B             
7DD7: 8F         ADC     A,A             
7DD8: 07         RLCA                    
7DD9: F8 77      LDHL    SP,$77          
7DDB: 88         ADC     A,B             
7DDC: 77         LD      (HL),A          
7DDD: 8F         ADC     A,A             
7DDE: F8 FF      LDHL    SP,$FF          
7DE0: 00         NOP                     
7DE1: 00         NOP                     
7DE2: 00         NOP                     
7DE3: 00         NOP                     
7DE4: 00         NOP                     
7DE5: 00         NOP                     
7DE6: FF         RST     0X38            
7DE7: 00         NOP                     
7DE8: FF         RST     0X38            
7DE9: 00         NOP                     
7DEA: FF         RST     0X38            
7DEB: 00         NOP                     
7DEC: FF         RST     0X38            
7DED: 00         NOP                     
7DEE: 00         NOP                     
7DEF: FF         RST     0X38            
7DF0: FF         RST     0X38            
7DF1: FF         RST     0X38            
7DF2: FF         RST     0X38            
7DF3: 7E         LD      A,(HL)          
7DF4: 7E         LD      A,(HL)          
7DF5: 3C         INC     A               
7DF6: 3C         INC     A               
7DF7: 00         NOP                     
7DF8: 81         ADD     A,C             
7DF9: 81         ADD     A,C             
7DFA: C3 42 FF   JP      $FF42           
7DFD: 3C         INC     A               
7DFE: 00         NOP                     
7DFF: FF         RST     0X38            
7E00: BD         CP      L               
7E01: 7E         LD      A,(HL)          
7E02: 5A         LD      E,D             
7E03: E7         RST     0X20            
7E04: A5         AND     L               
7E05: C3 A5 C3   JP      $C3A5           
7E08: A5         AND     L               
7E09: C3 A5 C3   JP      $C3A5           
7E0C: AD         XOR     L               
7E0D: C3 A5 C3   JP      $C3A5           
7E10: BD         CP      L               
7E11: 7E         LD      A,(HL)          
7E12: 5A         LD      E,D             
7E13: E7         RST     0X20            
7E14: A5         AND     L               
7E15: C3 FF FF   JP      $FFFF           
7E18: 80         ADD     A,B             
7E19: 80         ADD     A,B             
7E1A: 00         NOP                     
7E1B: 00         NOP                     
7E1C: 7F         LD      A,A             
7E1D: 00         NOP                     
7E1E: FF         RST     0X38            
7E1F: 3E BD      LD      A,$BD           
7E21: 7E         LD      A,(HL)          
7E22: 5A         LD      E,D             
7E23: E7         RST     0X20            
7E24: A5         AND     L               
7E25: C3 FF FF   JP      $FFFF           
7E28: 00         NOP                     
7E29: 00         NOP                     
7E2A: 00         NOP                     
7E2B: 00         NOP                     
7E2C: FF         RST     0X38            
7E2D: 00         NOP                     
7E2E: FF         RST     0X38            
7E2F: 1C         INC     E               
7E30: BD         CP      L               
7E31: 7E         LD      A,(HL)          
7E32: 5A         LD      E,D             
7E33: E7         RST     0X20            
7E34: A5         AND     L               
7E35: C3 FF FF   JP      $FFFF           
7E38: 00         NOP                     
7E39: 00         NOP                     
7E3A: 00         NOP                     
7E3B: 00         NOP                     
7E3C: FF         RST     0X38            
7E3D: 00         NOP                     
7E3E: FF         RST     0X38            
7E3F: 7E         LD      A,(HL)          
7E40: BD         CP      L               
7E41: 7E         LD      A,(HL)          
7E42: 5A         LD      E,D             
7E43: E7         RST     0X20            
7E44: A5         AND     L               
7E45: C3 FF FF   JP      $FFFF           
7E48: 01 01 00   LD      BC,$0001        
7E4B: 00         NOP                     
7E4C: FE 00      CP      $00             
7E4E: FF         RST     0X38            
7E4F: FE BD      CP      $BD             
7E51: 7E         LD      A,(HL)          
7E52: 5A         LD      E,D             
7E53: E7         RST     0X20            
7E54: A5         AND     L               
7E55: C3 A5 C3   JP      $C3A5           
7E58: A5         AND     L               
7E59: C3 A5 C3   JP      $C3A5           
7E5C: AD         XOR     L               
7E5D: C3 A5 C3   JP      $C3A5           
7E60: FF         RST     0X38            
7E61: 00         NOP                     
7E62: FB         EI                      
7E63: 07         RLCA                    
7E64: EC         ???                     
7E65: 1F         RRA                     
7E66: D0         RET     NC              
7E67: 3F         CCF                     
7E68: E3         ???                     
7E69: 3C         INC     A               
7E6A: A7         AND     A               
7E6B: 78         LD      A,B             
7E6C: C7         RST     0X00            
7E6D: 78         LD      A,B             
7E6E: 47         LD      B,A             
7E6F: F8 FF      LDHL    SP,$FF          
7E71: 00         NOP                     
7E72: DF         RST     0X18            
7E73: E0 37      LDFF00  ($37),A         
7E75: F8 0B      LDHL    SP,$0B          
7E77: FC         ???                     
7E78: C7         RST     0X00            
7E79: 3C         INC     A               
7E7A: E5         PUSH    HL              
7E7B: 1E E3      LD      E,$E3           
7E7D: 1E E2      LD      E,$E2           
7E7F: 1F         RRA                     
7E80: 1E 1E      LD      E,$1E           
7E82: 21 21 50   LD      HL,$5021        
7E85: 43         LD      B,E             
7E86: 41         LD      B,C             
7E87: 44         LD      B,H             
7E88: C0         RET     NZ              
7E89: 48         LD      C,B             
7E8A: E0 A9      LDFF00  ($A9),A         
7E8C: F0 98      LD      A,($98)         
7E8E: F8 98      LDHL    SP,$98          
7E90: 78         LD      A,B             
7E91: 78         LD      A,B             
7E92: 84         ADD     A,H             
7E93: 84         ADD     A,H             
7E94: 12         LD      (DE),A          
7E95: 02         LD      (BC),A          
7E96: 02         LD      (BC),A          
7E97: E2         LDFF00  (C),A           
7E98: 07         RLCA                    
7E99: 12         LD      (DE),A          
7E9A: 0D         DEC     C               
7E9B: 0F         RRCA                    
7E9C: 09         ADD     HL,BC           
7E9D: 0F         RRCA                    
7E9E: 19         ADD     HL,DE           
7E9F: 5F         LD      E,A             
7EA0: FC         ???                     
7EA1: 00         NOP                     
7EA2: F8 00      LDHL    SP,$00          
7EA4: F8 00      LDHL    SP,$00          
7EA6: F8 00      LDHL    SP,$00          
7EA8: C0         RET     NZ              
7EA9: 00         NOP                     
7EAA: 80         ADD     A,B             
7EAB: 00         NOP                     
7EAC: 80         ADD     A,B             
7EAD: 00         NOP                     
7EAE: 80         ADD     A,B             
7EAF: 00         NOP                     
7EB0: 00         NOP                     
7EB1: 00         NOP                     
7EB2: 42         LD      B,D             
7EB3: 42         LD      B,D             
7EB4: 24         INC     H               
7EB5: 24         INC     H               
7EB6: 18 18      JR      $7ED0           
7EB8: 18 18      JR      $7ED2           
7EBA: 24         INC     H               
7EBB: 24         INC     H               
7EBC: 42         LD      B,D             
7EBD: 42         LD      B,D             
7EBE: 00         NOP                     
7EBF: 00         NOP                     
7EC0: 00         NOP                     
7EC1: FF         RST     0X38            
7EC2: 00         NOP                     
7EC3: FF         RST     0X38            
7EC4: FF         RST     0X38            
7EC5: FF         RST     0X38            
7EC6: FF         RST     0X38            
7EC7: 92         SUB     D               
7EC8: FF         RST     0X38            
7EC9: FF         RST     0X38            
7ECA: 00         NOP                     
7ECB: FF         RST     0X38            
7ECC: 00         NOP                     
7ECD: FF         RST     0X38            
7ECE: 00         NOP                     
7ECF: FF         RST     0X38            
7ED0: 07         RLCA                    
7ED1: FF         RST     0X38            
7ED2: F9         LD      SP,HL           
7ED3: F8 41      LDHL    SP,$41          
7ED5: 88         ADC     A,B             
7ED6: 45         LD      B,L             
7ED7: 88         ADC     A,B             
7ED8: 54         LD      D,H             
7ED9: 88         ADC     A,B             
7EDA: 54         LD      D,H             
7EDB: 88         ADC     A,B             
7EDC: 15         DEC     D               
7EDD: 88         ADC     A,B             
7EDE: 15         DEC     D               
7EDF: 88         ADC     A,B             
7EE0: DB         ???                     
7EE1: 18 AD      JR      $7E90           
7EE3: 2C         INC     L               
7EE4: 4A         LD      C,D             
7EE5: 4E         LD      C,(HL)          
7EE6: 89         ADC     A,C             
7EE7: 8F         ADC     A,A             
7EE8: 99         SBC     C               
7EE9: 9F         SBC     A               
7EEA: BD         CP      L               
7EEB: A7         AND     A               
7EEC: 7E         LD      A,(HL)          
7EED: 42         LD      B,D             
7EEE: BD         CP      L               
7EEF: 3C         INC     A               
7EF0: 00         NOP                     
7EF1: 00         NOP                     
7EF2: 42         LD      B,D             
7EF3: 42         LD      B,D             
7EF4: 24         INC     H               
7EF5: 24         INC     H               
7EF6: 18 18      JR      $7F10           
7EF8: 18 18      JR      $7F12           
7EFA: 24         INC     H               
7EFB: 24         INC     H               
7EFC: 42         LD      B,D             
7EFD: 42         LD      B,D             
7EFE: 00         NOP                     
7EFF: 00         NOP                     
7F00: A5         AND     L               
7F01: C3 A5 C3   JP      $C3A5           
7F04: A5         AND     L               
7F05: C3 BD C3   JP      $C3BD           
7F08: 99         SBC     C               
7F09: E7         RST     0X20            
7F0A: 81         ADD     A,C             
7F0B: FF         RST     0X38            
7F0C: 42         LD      B,D             
7F0D: FF         RST     0X38            
7F0E: BD         CP      L               
7F0F: 7E         LD      A,(HL)          
7F10: FF         RST     0X38            
7F11: 11 FF 11   LD      DE,$11FF        
7F14: FF         RST     0X38            
7F15: 1E FF      LD      E,$FF           
7F17: 14         INC     D               
7F18: FF         RST     0X38            
7F19: 14         INC     D               
7F1A: FF         RST     0X38            
7F1B: 33         INC     SP              
7F1C: FF         RST     0X38            
7F1D: 80         ADD     A,B             
7F1E: FF         RST     0X38            
7F1F: FF         RST     0X38            
7F20: FF         RST     0X38            
7F21: 14         INC     D               
7F22: FF         RST     0X38            
7F23: 14         INC     D               
7F24: FF         RST     0X38            
7F25: 22         LD      (HLI),A         
7F26: FF         RST     0X38            
7F27: 3E FF      LD      A,$FF           
7F29: 22         LD      (HLI),A         
7F2A: FF         RST     0X38            
7F2B: 63         LD      H,E             
7F2C: FF         RST     0X38            
7F2D: 00         NOP                     
7F2E: FF         RST     0X38            
7F2F: FF         RST     0X38            
7F30: FF         RST     0X38            
7F31: 22         LD      (HLI),A         
7F32: FF         RST     0X38            
7F33: 20 FF      JR      NZ,$7F34        
7F35: 38 FF      JR      C,$7F36         
7F37: 20 FF      JR      NZ,$7F38        
7F39: 20 FF      JR      NZ,$7F3A        
7F3B: 70         LD      (HL),B          
7F3C: FF         RST     0X38            
7F3D: 00         NOP                     
7F3E: FF         RST     0X38            
7F3F: FF         RST     0X38            
7F40: FF         RST     0X38            
7F41: 92         SUB     D               
7F42: FF         RST     0X38            
7F43: 10 FF      STOP    $FF             
7F45: 10 FF      STOP    $FF             
7F47: 10 FF      STOP    $FF             
7F49: 10 FF      STOP    $FF             
7F4B: 38 FF      JR      C,$7F4C         
7F4D: 01 FF FF   LD      BC,$FFFF        
7F50: A5         AND     L               
7F51: C3 A5 C3   JP      $C3A5           
7F54: A5         AND     L               
7F55: C3 BD C3   JP      $C3BD           
7F58: 99         SBC     C               
7F59: E7         RST     0X20            
7F5A: 81         ADD     A,C             
7F5B: FF         RST     0X38            
7F5C: 42         LD      B,D             
7F5D: FF         RST     0X38            
7F5E: BD         CP      L               
7F5F: 7E         LD      A,(HL)          
7F60: 00         NOP                     
7F61: FF         RST     0X38            
7F62: 07         RLCA                    
7F63: FF         RST     0X38            
7F64: 1C         INC     E               
7F65: FF         RST     0X38            
7F66: 30 FF      JR      NC,$7F67        
7F68: 63         LD      H,E             
7F69: FC         ???                     
7F6A: 67         LD      H,A             
7F6B: F8 C7      LDHL    SP,$C7          
7F6D: F8 C7      LDHL    SP,$C7          
7F6F: F8 00      LDHL    SP,$00          
7F71: FF         RST     0X38            
7F72: E0 FF      LDFF00  ($FF),A         
7F74: 38 FF      JR      C,$7F75         
7F76: 0C         INC     C               
7F77: FF         RST     0X38            
7F78: C6 3F      ADD     $3F             
7F7A: E6 1F      AND     $1F             
7F7C: E3         ???                     
7F7D: 1F         RRA                     
7F7E: E3         ???                     
7F7F: 1F         RRA                     
7F80: FC         ???                     
7F81: A4         AND     H               
7F82: FF         RST     0X38            
7F83: A7         AND     A               
7F84: FF         RST     0X38            
7F85: A2         AND     D               
7F86: FF         RST     0X38            
7F87: D2 FF 8A   JP      NC,$8AFF        
7F8A: 7F         LD      A,A             
7F8B: 44         LD      B,H             
7F8C: 3F         CCF                     
7F8D: 24         INC     H               
7F8E: 1F         RRA                     
7F8F: 1F         RRA                     
7F90: 29         ADD     HL,HL           
7F91: 3F         CCF                     
7F92: C9         RET                     
7F93: FF         RST     0X38            
7F94: C9         RET                     
7F95: 7F         LD      A,A             
7F96: C9         RET                     
7F97: 7F         LD      A,A             
7F98: DD         ???                     
7F99: 77         LD      (HL),A          
7F9A: FE 22      CP      $22             
7F9C: FC         ???                     
7F9D: 2C         INC     L               
7F9E: F9         LD      SP,HL           
7F9F: F8 3F      LDHL    SP,$3F          
7FA1: 00         NOP                     
7FA2: 1F         RRA                     
7FA3: 00         NOP                     
7FA4: 0F         RRCA                    
7FA5: 00         NOP                     
7FA6: 0F         RRCA                    
7FA7: 00         NOP                     
7FA8: 0F         RRCA                    
7FA9: 00         NOP                     
7FAA: 0F         RRCA                    
7FAB: 00         NOP                     
7FAC: 03         INC     BC              
7FAD: 00         NOP                     
7FAE: 01 00 00   LD      BC,$0000        
7FB1: 00         NOP                     
7FB2: 42         LD      B,D             
7FB3: 42         LD      B,D             
7FB4: 24         INC     H               
7FB5: 24         INC     H               
7FB6: 18 18      JR      $7FD0           
7FB8: 18 18      JR      $7FD2           
7FBA: 24         INC     H               
7FBB: 24         INC     H               
7FBC: 42         LD      B,D             
7FBD: 42         LD      B,D             
7FBE: 00         NOP                     
7FBF: 00         NOP                     
7FC0: 55         LD      D,L             
7FC1: 88         ADC     A,B             
7FC2: 51         LD      D,C             
7FC3: 88         ADC     A,B             
7FC4: 41         LD      B,C             
7FC5: 88         ADC     A,B             
7FC6: 45         LD      B,L             
7FC7: 88         ADC     A,B             
7FC8: 54         LD      D,H             
7FC9: 88         ADC     A,B             
7FCA: 54         LD      D,H             
7FCB: 88         ADC     A,B             
7FCC: 15         DEC     D               
7FCD: 88         ADC     A,B             
7FCE: 15         DEC     D               
7FCF: 88         ADC     A,B             
7FD0: 51         LD      D,C             
7FD1: 88         ADC     A,B             
7FD2: 51         LD      D,C             
7FD3: 88         ADC     A,B             
7FD4: 45         LD      B,L             
7FD5: 88         ADC     A,B             
7FD6: 40         LD      B,B             
7FD7: 8F         ADC     A,A             
7FD8: 07         RLCA                    
7FD9: F8 77      LDHL    SP,$77          
7FDB: 88         ADC     A,B             
7FDC: 77         LD      (HL),A          
7FDD: 8F         ADC     A,A             
7FDE: F8 FF      LDHL    SP,$FF          
7FE0: E7         RST     0X20            
7FE1: 00         NOP                     
7FE2: DB         ???                     
7FE3: 18 A5      JR      $7F8A           
7FE5: 24         INC     H               
7FE6: 4E         LD      C,(HL)          
7FE7: 4A         LD      C,D             
7FE8: 4E         LD      C,(HL)          
7FE9: 4A         LD      C,D             
7FEA: 5E         LD      E,(HL)          
7FEB: 52         LD      D,D             
7FEC: BD         CP      L               
7FED: 3C         INC     A               
7FEE: C3 00 00   JP      $0000           
7FF1: 00         NOP                     
7FF2: 42         LD      B,D             
7FF3: 42         LD      B,D             
7FF4: 24         INC     H               
7FF5: 24         INC     H               
7FF6: 18 18      JR      $8010           
7FF8: 18 18      JR      $8012           
7FFA: 24         INC     H               
7FFB: 24         INC     H               
7FFC: 42         LD      B,D             
7FFD: 42         LD      B,D             
7FFE: 00         NOP                     
7FFF: 00         NOP                     
```
