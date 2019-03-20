![Bank 03](GBZelda.jpg)

# Bank 03

>>> cpu Z80GB

>>> memoryTable ram 
[RAM Usage](RAMUse.md)

>>> memoryTable hard 
[Hardware Info](../Hardware.md)

```code
4000: 03         INC     BC              
4001: 19         ADD     HL,DE           
4002: 03         INC     BC              
4003: 18 03      JR      $4008           
4005: 03         INC     BC              
4006: 03         INC     BC              
4007: 07         RLCA                    
4008: 18 03      JR      $400D           
400A: 03         INC     BC              
400B: 03         INC     BC              
400C: 03         INC     BC              
400D: 06 04      LD      B,$04           
400F: 06 04      LD      B,$04           
4011: 04         INC     B               
4012: 04         INC     B               
4013: 03         INC     BC              
4014: 07         RLCA                    
4015: 06 06      LD      B,$06           
4017: 06 06      LD      B,$06           
4019: 06 06      LD      B,$06           
401B: 06 06      LD      B,$06           
401D: 06 15      LD      B,$15           
401F: 06 06      LD      B,$06           
4021: 06 06      LD      B,$06           
4023: 06 03      LD      B,$03           
4025: 03         INC     BC              
4026: 03         INC     BC              
4027: 06 19      LD      B,$19           
4029: 04         INC     B               
402A: 04         INC     B               
402B: 15         DEC     D               
402C: 07         RLCA                    
402D: 03         INC     BC              
402E: 03         INC     BC              
402F: 03         INC     BC              
4030: 03         INC     BC              
4031: 03         INC     BC              
4032: 03         INC     BC              
4033: 03         INC     BC              
4034: 03         INC     BC              
4035: 03         INC     BC              
4036: 03         INC     BC              
4037: 03         INC     BC              
4038: 03         INC     BC              
4039: 03         INC     BC              
403A: 03         INC     BC              
403B: 03         INC     BC              
403C: 03         INC     BC              
403D: 03         INC     BC              
403E: 05         DEC     B               
403F: 05         DEC     B               
4040: 05         DEC     B               
4041: 06 18      LD      B,$18           
4043: 15         DEC     D               
4044: 15         DEC     D               
4045: 15         DEC     D               
4046: 15         DEC     D               
4047: 15         DEC     D               
4048: 15         DEC     D               
4049: 15         DEC     D               
404A: 03         INC     BC              
404B: 03         INC     BC              
404C: 04         INC     B               
404D: 04         INC     B               
404E: 04         INC     B               
404F: 04         INC     B               
4050: 06 04      LD      B,$04           
4052: 04         INC     B               
4053: 04         INC     B               
4054: 04         INC     B               
4055: 04         INC     B               
4056: 04         INC     B               
4057: 04         INC     B               
4058: 04         INC     B               
4059: 04         INC     B               
405A: 04         INC     B               
405B: 04         INC     B               
405C: 04         INC     B               
405D: 05         DEC     B               
405E: 05         DEC     B               
405F: 07         RLCA                    
4060: 05         DEC     B               
4061: 19         ADD     HL,DE           
4062: 05         DEC     B               
4063: 05         DEC     B               
4064: 18 05      JR      $406B           
4066: 15         DEC     D               
4067: 05         DEC     B               
4068: 15         DEC     D               
4069: 18 05      JR      $4070           
406B: 18 05      JR      $4072           
406D: 05         DEC     B               
406E: 06 19      LD      B,$19           
4070: 06 06      LD      B,$06           
4072: 06 06      LD      B,$06           
4074: 18 18      JR      $408E           
4076: 18 06      JR      $407E           
4078: 06 06      LD      B,$06           
407A: 06 06      LD      B,$06           
407C: 06 06      LD      B,$06           
407E: 06 18      LD      B,$18           
4080: 06 06      LD      B,$06           
4082: 06 06      LD      B,$06           
4084: 06 06      LD      B,$06           
4086: 06 06      LD      B,$06           
4088: 06 06      LD      B,$06           
408A: 06 06      LD      B,$06           
408C: 06 06      LD      B,$06           
408E: 06 19      LD      B,$19           
4090: 06 06      LD      B,$06           
4092: 06 06      LD      B,$06           
4094: 07         RLCA                    
4095: 06 19      LD      B,$19           
4097: 19         ADD     HL,DE           
4098: 07         RLCA                    
4099: 07         RLCA                    
409A: 07         RLCA                    
409B: 07         RLCA                    
409C: 07         RLCA                    
409D: 19         ADD     HL,DE           
409E: 07         RLCA                    
409F: 07         RLCA                    
40A0: 07         RLCA                    
40A1: 07         RLCA                    
40A2: 07         RLCA                    
40A3: 07         RLCA                    
40A4: 07         RLCA                    
40A5: 07         RLCA                    
40A6: 07         RLCA                    
40A7: 07         RLCA                    
40A8: 07         RLCA                    
40A9: 07         RLCA                    
40AA: 19         ADD     HL,DE           
40AB: 19         ADD     HL,DE           
40AC: 19         ADD     HL,DE           
40AD: 07         RLCA                    
40AE: 07         RLCA                    
40AF: 07         RLCA                    
40B0: 07         RLCA                    
40B1: 07         RLCA                    
40B2: 15         DEC     D               
40B3: 07         RLCA                    
40B4: 07         RLCA                    
40B5: 07         RLCA                    
40B6: 07         RLCA                    
40B7: 07         RLCA                    
40B8: 07         RLCA                    
40B9: 18 18      JR      $40D3           
40BB: 07         RLCA                    
40BC: 18 18      JR      $40D6           
40BE: 18 18      JR      $40D8           
40C0: 18 18      JR      $40DA           
40C2: 18 18      JR      $40DC           
40C4: 18 15      JR      $40DB           
40C6: 15         DEC     D               
40C7: 18 18      JR      $40E1           
40C9: 18 18      JR      $40E3           
40CB: 18 15      JR      $40E2           
40CD: 19         ADD     HL,DE           
40CE: 18 19      JR      $40E9           
40D0: 18 18      JR      $40EA           
40D2: 18 18      JR      $40EC           
40D4: 19         ADD     HL,DE           
40D5: 19         ADD     HL,DE           
40D6: 19         ADD     HL,DE           
40D7: 19         ADD     HL,DE           
40D8: 19         ADD     HL,DE           
40D9: 19         ADD     HL,DE           
40DA: 19         ADD     HL,DE           
40DB: 19         ADD     HL,DE           
40DC: 19         ADD     HL,DE           
40DD: 19         ADD     HL,DE           
40DE: 19         ADD     HL,DE           
40DF: 19         ADD     HL,DE           
40E0: 15         DEC     D               
40E1: 15         DEC     D               
40E2: 15         DEC     D               
40E3: 15         DEC     D               
40E4: 15         DEC     D               
40E5: 06 15      LD      B,$15           
40E7: 15         DEC     D               
40E8: 17         RLA                     
40E9: 42         LD      B,D             
40EA: C2 D2 C2   JP      NZ,$C2D2        
40ED: C2 D2 C2   JP      NZ,$C2D2        
40F0: C2 C3 12   JP      NZ,$12C3        
40F3: 42         LD      B,D             
40F4: 12         LD      (DE),A          
40F5: 42         LD      B,D             
40F6: 12         LD      (DE),A          
40F7: 12         LD      (DE),A          
40F8: 92         SUB     D               
40F9: 12         LD      (DE),A          
40FA: 18 12      JR      $410E           
40FC: 11 12 02   LD      DE,$0212        
40FF: 02         LD      (BC),A          
4100: 02         LD      (BC),A          
4101: 12         LD      (DE),A          
4102: 02         LD      (BC),A          
4103: 12         LD      (DE),A          
4104: 12         LD      (DE),A          
4105: 11 02 12   LD      DE,$1202        
4108: 12         LD      (DE),A          
4109: 12         LD      (DE),A          
410A: 02         LD      (BC),A          
410B: 42         LD      B,D             
410C: 92         SUB     D               
410D: 12         LD      (DE),A          
410E: E2         LDFF00  (C),A           
410F: E2         LDFF00  (C),A           
4110: 02         LD      (BC),A          
4111: 12         LD      (DE),A          
4112: 02         LD      (BC),A          
4113: 02         LD      (BC),A          
4114: 41         LD      B,C             
4115: 12         LD      (DE),A          
4116: B1         OR      C               
4117: B1         OR      C               
4118: B1         OR      C               
4119: B1         OR      C               
411A: B1         OR      C               
411B: B2         OR      D               
411C: B2         OR      D               
411D: B1         OR      C               
411E: B2         OR      D               
411F: B2         OR      D               
4120: B2         OR      D               
4121: B1         OR      C               
4122: 92         SUB     D               
4123: B2         OR      D               
4124: B1         OR      C               
4125: B2         OR      D               
4126: B1         OR      C               
4127: 82         ADD     A,D             
4128: 92         SUB     D               
4129: 84         ADD     A,H             
412A: 92         SUB     D               
412B: 82         ADD     A,D             
412C: C0         RET     NZ              
412D: C0         RET     NZ              
412E: C2 82 82   JP      NZ,$8282        
4131: 82         ADD     A,D             
4132: 82         ADD     A,D             
4133: 82         ADD     A,D             
4134: 82         ADD     A,D             
4135: 41         LD      B,C             
4136: 82         ADD     A,D             
4137: 82         ADD     A,D             
4138: 82         ADD     A,D             
4139: 12         LD      (DE),A          
413A: 02         LD      (BC),A          
413B: 42         LD      B,D             
413C: 42         LD      B,D             
413D: C2 02 02   JP      NZ,$0202        
4140: 02         LD      (BC),A          
4141: 42         LD      B,D             
4142: 08 48 00   LD      ($0048),SP      
4145: 91         SUB     C               
4146: 02         LD      (BC),A          
4147: 00         NOP                     
4148: 00         NOP                     
4149: 02         LD      (BC),A          
414A: C2 08 02   JP      NZ,$0208        
414D: C0         RET     NZ              
414E: 00         NOP                     
414F: 82         ADD     A,D             
4150: 02         LD      (BC),A          
4151: C0         RET     NZ              
4152: C2 92 82   JP      NZ,$8292        
4155: 92         SUB     D               
4156: 12         LD      (DE),A          
4157: C1         POP     BC              
4158: 92         SUB     D               
4159: 92         SUB     D               
415A: 92         SUB     D               
415B: 92         SUB     D               
415C: 92         SUB     D               
415D: 93         SUB     E               
415E: 92         SUB     D               
415F: 92         SUB     D               
4160: 92         SUB     D               
4161: 92         SUB     D               
4162: 92         SUB     D               
4163: 52         LD      D,D             
4164: 92         SUB     D               
4165: 00         NOP                     
4166: 42         LD      B,D             
4167: 02         LD      (BC),A          
4168: 82         ADD     A,D             
4169: 92         SUB     D               
416A: 00         NOP                     
416B: 42         LD      B,D             
416C: C2 D1 D2   JP      NZ,$D2D1        
416F: D1         POP     DE              
4170: 12         LD      (DE),A          
4171: 84         ADD     A,H             
4172: 0C         INC     C               
4173: C2 C2 92   JP      NZ,$92C2        
4176: 92         SUB     D               
4177: 08 12 12   LD      ($1212),SP      
417A: 13         INC     DE              
417B: 14         INC     D               
417C: 12         LD      (DE),A          
417D: 80         ADD     A,B             
417E: 92         SUB     D               
417F: 92         SUB     D               
4180: C0         RET     NZ              
4181: D2 12 C0   JP      NC,$C012        
4184: D2 12 94   JP      NC,$9412        
4187: C0         RET     NZ              
4188: 12         LD      (DE),A          
4189: 12         LD      (DE),A          
418A: 12         LD      (DE),A          
418B: 14         INC     D               
418C: C4 C4 C4   CALL    NZ,$C4C4        
418F: C2 8A 92   JP      NZ,$928A        
4192: 02         LD      (BC),A          
4193: 12         LD      (DE),A          
4194: 12         LD      (DE),A          
4195: 12         LD      (DE),A          
4196: 92         SUB     D               
4197: 12         LD      (DE),A          
4198: B2         OR      D               
4199: 02         LD      (BC),A          
419A: 82         ADD     A,D             
419B: C0         RET     NZ              
419C: 82         ADD     A,D             
419D: 92         SUB     D               
419E: 82         ADD     A,D             
419F: 92         SUB     D               
41A0: 94         SUB     H               
41A1: 95         SUB     L               
41A2: 12         LD      (DE),A          
41A3: 13         INC     DE              
41A4: 12         LD      (DE),A          
41A5: 12         LD      (DE),A          
41A6: 13         INC     DE              
41A7: 16 52      LD      D,$52           
41A9: C0         RET     NZ              
41AA: D2 D2 94   JP      NC,$94D2        
41AD: 98         SBC     B               
41AE: 12         LD      (DE),A          
41AF: 12         LD      (DE),A          
41B0: D0         RET     NC              
41B1: D2 C1 88   JP      NC,$88C1        
41B4: 02         LD      (BC),A          
41B5: 52         LD      D,D             
41B6: 85         ADD     A,L             
41B7: 84         ADD     A,H             
41B8: C2 82 82   JP      NZ,$8282        
41BB: 82         ADD     A,D             
41BC: D2 D2 D2   JP      NC,$D2D2        
41BF: 82         ADD     A,D             
41C0: 02         LD      (BC),A          
41C1: C2 C8 42   JP      NZ,$42C8        
41C4: 48         LD      C,B             
41C5: C4 C2 C2   CALL    NZ,$C2C2        
41C8: C2 D3 D2   JP      NZ,$D2D3        
41CB: 42         LD      B,D             
41CC: 12         LD      (DE),A          
41CD: 13         INC     DE              
41CE: D2 50 C0   JP      NC,$C050        
41D1: 00         NOP                     
41D2: 00         NOP                     
41D3: 00         NOP                     
41D4: 01 01 01   LD      BC,$0101        
41D7: 00         NOP                     
41D8: 06 00      LD      B,$00           
41DA: 00         NOP                     
41DB: 00         NOP                     
41DC: 00         NOP                     
41DD: 00         NOP                     
41DE: 00         NOP                     
41DF: 00         NOP                     
41E0: 00         NOP                     
41E1: 80         ADD     A,B             
41E2: 00         NOP                     
41E3: 08 00 01   LD      ($0100),SP      
41E6: 00         NOP                     
41E7: 00         NOP                     
41E8: 03         INC     BC              
41E9: 03         INC     BC              
41EA: 00         NOP                     
41EB: 00         NOP                     
41EC: 00         NOP                     
41ED: 00         NOP                     
41EE: 10 02      STOP    $02             
41F0: 00         NOP                     
41F1: 00         NOP                     
41F2: 00         NOP                     
41F3: 00         NOP                     
41F4: 00         NOP                     
41F5: 00         NOP                     
41F6: 00         NOP                     
41F7: 80         ADD     A,B             
41F8: 80         ADD     A,B             
41F9: 82         ADD     A,D             
41FA: 00         NOP                     
41FB: 00         NOP                     
41FC: 80         ADD     A,B             
41FD: 00         NOP                     
41FE: 80         ADD     A,B             
41FF: 1D         DEC     E               
4200: 1D         DEC     E               
4201: 1D         DEC     E               
4202: 1D         DEC     E               
4203: 1D         DEC     E               
4204: 01 1D 1D   LD      BC,$1D1D        
4207: 1D         DEC     E               
4208: 1D         DEC     E               
4209: 1D         DEC     E               
420A: 1D         DEC     E               
420B: 9D         SBC     L               
420C: 1D         DEC     E               
420D: 1D         DEC     E               
420E: 1D         DEC     E               
420F: 1D         DEC     E               
4210: 98         SBC     B               
4211: 98         SBC     B               
4212: 98         SBC     B               
4213: 98         SBC     B               
4214: 98         SBC     B               
4215: 98         SBC     B               
4216: 98         SBC     B               
4217: 00         NOP                     
4218: 84         ADD     A,H             
4219: 84         ADD     A,H             
421A: 84         ADD     A,H             
421B: 84         ADD     A,H             
421C: 98         SBC     B               
421D: 98         SBC     B               
421E: 00         NOP                     
421F: 98         SBC     B               
4220: 98         SBC     B               
4221: 98         SBC     B               
4222: 00         NOP                     
4223: 00         NOP                     
4224: 00         NOP                     
4225: 00         NOP                     
4226: 80         ADD     A,B             
4227: 00         NOP                     
4228: 00         NOP                     
4229: 00         NOP                     
422A: 00         NOP                     
422B: 88         ADC     A,B             
422C: 08 00 80   LD      ($8000),SP      
422F: 80         ADD     A,B             
4230: 80         ADD     A,B             
4231: A8         XOR     B               
4232: 80         ADD     A,B             
4233: 00         NOP                     
4234: 00         NOP                     
4235: 00         NOP                     
4236: 00         NOP                     
4237: 00         NOP                     
4238: 00         NOP                     
4239: 80         ADD     A,B             
423A: 00         NOP                     
423B: 00         NOP                     
423C: 80         ADD     A,B             
423D: 98         SBC     B               
423E: 00         NOP                     
423F: 80         ADD     A,B             
4240: 00         NOP                     
4241: 00         NOP                     
4242: 98         SBC     B               
4243: 98         SBC     B               
4244: 98         SBC     B               
4245: 98         SBC     B               
4246: 98         SBC     B               
4247: 98         SBC     B               
4248: 98         SBC     B               
4249: 98         SBC     B               
424A: 80         ADD     A,B             
424B: 98         SBC     B               
424C: 00         NOP                     
424D: 98         SBC     B               
424E: 08 10 00   LD      ($0010),SP      
4251: 80         ADD     A,B             
4252: 98         SBC     B               
4253: 00         NOP                     
4254: 20 00      JR      NZ,$4256        
4256: 00         NOP                     
4257: 00         NOP                     
4258: 38 00      JR      C,$425A         
425A: 88         ADC     A,B             
425B: 08 04 04   LD      ($0404),SP      
425E: 84         ADD     A,H             
425F: 84         ADD     A,H             
4260: 88         ADC     A,B             
4261: 00         NOP                     
4262: 00         NOP                     
4263: 00         NOP                     
4264: 80         ADD     A,B             
4265: 00         NOP                     
4266: 00         NOP                     
4267: 80         ADD     A,B             
4268: 80         ADD     A,B             
4269: 00         NOP                     
426A: 00         NOP                     
426B: 00         NOP                     
426C: 00         NOP                     
426D: 00         NOP                     
426E: 00         NOP                     
426F: A4         AND     H               
4270: 00         NOP                     
4271: 00         NOP                     
4272: 00         NOP                     
4273: 00         NOP                     
4274: 00         NOP                     
4275: 2C         INC     L               
4276: 2C         INC     L               
4277: 2C         INC     L               
4278: 30 A4      JR      NC,$421E        
427A: 80         ADD     A,B             
427B: 00         NOP                     
427C: 00         NOP                     
427D: 00         NOP                     
427E: 00         NOP                     
427F: 80         ADD     A,B             
4280: 00         NOP                     
4281: 1D         DEC     E               
4282: 00         NOP                     
4283: 98         SBC     B               
4284: 00         NOP                     
4285: 98         SBC     B               
4286: 98         SBC     B               
4287: B4         OR      H               
4288: 98         SBC     B               
4289: 98         SBC     B               
428A: 98         SBC     B               
428B: 00         NOP                     
428C: 00         NOP                     
428D: 00         NOP                     
428E: 00         NOP                     
428F: 00         NOP                     
4290: 80         ADD     A,B             
4291: 00         NOP                     
4292: 00         NOP                     
4293: 18 18      JR      $42AD           
4295: B4         OR      H               
4296: B4         OR      H               
4297: 06 00      LD      B,$00           
4299: 34         INC     (HL)            
429A: 98         SBC     B               
429B: 00         NOP                     
429C: 80         ADD     A,B             
429D: 00         NOP                     
429E: 00         NOP                     
429F: 98         SBC     B               
42A0: 98         SBC     B               
42A1: 00         NOP                     
42A2: 98         SBC     B               
42A3: 98         SBC     B               
42A4: 98         SBC     B               
42A5: 98         SBC     B               
42A6: 00         NOP                     
42A7: 18 BD      JR      $4266           
42A9: 80         ADD     A,B             
42AA: 2D         DEC     L               
42AB: 2D         DEC     L               
42AC: 00         NOP                     
42AD: 0A         LD      A,(BC)          
42AE: 00         NOP                     
42AF: 00         NOP                     
42B0: 00         NOP                     
42B1: 00         NOP                     
42B2: 00         NOP                     
42B3: 00         NOP                     
42B4: 00         NOP                     
42B5: 00         NOP                     
42B6: 84         ADD     A,H             
42B7: 38 00      JR      C,$42B9         
42B9: 00         NOP                     
42BA: 00         NOP                     
42BB: 00         NOP                     
42BC: 00         NOP                     
42BD: 02         LD      (BC),A          
42BE: 00         NOP                     
42BF: 00         NOP                     
42C0: 00         NOP                     
42C1: 00         NOP                     
42C2: 00         NOP                     
42C3: 00         NOP                     
42C4: 00         NOP                     
42C5: 0D         DEC     C               
42C6: 01 0D 01   LD      BC,$010D        
42C9: 01 08 13   LD      BC,$1308        
42CC: 13         INC     DE              
42CD: 13         INC     DE              
42CE: 00         NOP                     
42CF: 01 06 2C   LD      BC,$2C06        
42D2: 2C         INC     L               
42D3: 0C         INC     C               
42D4: 00         NOP                     
42D5: 2A         LD      A,(HLI)         
42D6: 00         NOP                     
42D7: 00         NOP                     
42D8: 00         NOP                     
42D9: 2A         LD      A,(HLI)         
42DA: 2F         CPL                     
42DB: 0B         DEC     BC              
42DC: 0C         INC     C               
42DD: 0E 01      LD      C,$01           
42DF: 01 06 06   LD      BC,$0606        
42E2: 09         ADD     HL,BC           
42E3: 04         INC     B               
42E4: 01 00 0E   LD      BC,$0E00        
42E7: 01 00 00   LD      BC,$0000        
42EA: 00         NOP                     
42EB: 00         NOP                     
42EC: 00         NOP                     
42ED: 00         NOP                     
42EE: 00         NOP                     
42EF: 00         NOP                     
42F0: 00         NOP                     
42F1: 00         NOP                     
42F2: 00         NOP                     
42F3: 00         NOP                     
42F4: 00         NOP                     
42F5: 00         NOP                     
42F6: 00         NOP                     
42F7: 00         NOP                     
42F8: 00         NOP                     
42F9: 00         NOP                     
42FA: 00         NOP                     
42FB: 00         NOP                     
42FC: 00         NOP                     
42FD: 00         NOP                     
42FE: 00         NOP                     
42FF: 00         NOP                     
4300: 00         NOP                     
4301: 00         NOP                     
4302: 00         NOP                     
4303: 00         NOP                     
4304: 00         NOP                     
4305: 00         NOP                     
4306: 00         NOP                     
4307: 0E 00      LD      C,$00           
4309: 00         NOP                     
430A: 00         NOP                     
430B: 20 13      JR      NZ,$4320        
430D: 00         NOP                     
430E: 00         NOP                     
430F: 00         NOP                     
4310: 0B         DEC     BC              
4311: 0B         DEC     BC              
4312: 30 0E      JR      NC,$4322        
4314: 18 1D      JR      $4333           
4316: 1A         LD      A,(DE)          
4317: 19         ADD     HL,DE           
4318: 1C         INC     E               
4319: 10 11      STOP    $11             
431B: 12         LD      (DE),A          
431C: 00         NOP                     
431D: 1F         RRA                     
431E: 1E 00      LD      E,$00           
4320: 1B         DEC     DE              
4321: 22         LD      (HLI),A         
4322: 00         NOP                     
4323: 00         NOP                     
4324: 00         NOP                     
4325: 00         NOP                     
4326: 00         NOP                     
4327: 00         NOP                     
4328: 00         NOP                     
4329: 00         NOP                     
432A: 00         NOP                     
432B: 00         NOP                     
432C: 00         NOP                     
432D: 00         NOP                     
432E: 00         NOP                     
432F: 00         NOP                     
4330: 00         NOP                     
4331: 00         NOP                     
4332: 00         NOP                     
4333: 00         NOP                     
4334: 00         NOP                     
4335: 21 00 29   LD      HL,$2900        
4338: 00         NOP                     
4339: 29         ADD     HL,HL           
433A: 00         NOP                     
433B: 00         NOP                     
433C: 13         INC     DE              
433D: 00         NOP                     
433E: 00         NOP                     
433F: 00         NOP                     
4340: 00         NOP                     
4341: 00         NOP                     
4342: 13         INC     DE              
4343: 15         DEC     D               
4344: 14         INC     D               
4345: 01 01 01   LD      BC,$0101        
4348: 01 13 24   LD      BC,$2413        
434B: 2D         DEC     L               
434C: 2E 13      LD      L,$13           
434E: 25         DEC     H               
434F: 23         INC     HL              
4350: 00         NOP                     
4351: 00         NOP                     
4352: 00         NOP                     
4353: 00         NOP                     
4354: 00         NOP                     
4355: 00         NOP                     
4356: 00         NOP                     
4357: 00         NOP                     
4358: 00         NOP                     
4359: 00         NOP                     
435A: 00         NOP                     
435B: 00         NOP                     
435C: 00         NOP                     
435D: 00         NOP                     
435E: 00         NOP                     
435F: 00         NOP                     
4360: 00         NOP                     
4361: 00         NOP                     
4362: 00         NOP                     
4363: 00         NOP                     
4364: 00         NOP                     
4365: 00         NOP                     
4366: 00         NOP                     
4367: 00         NOP                     
4368: 00         NOP                     
4369: 00         NOP                     
436A: 00         NOP                     
436B: 02         LD      (BC),A          
436C: 00         NOP                     
436D: 00         NOP                     
436E: 00         NOP                     
436F: 00         NOP                     
4370: 00         NOP                     
4371: 00         NOP                     
4372: 00         NOP                     
4373: 00         NOP                     
4374: 0F         RRCA                    
4375: 2B         DEC     HL              
4376: 00         NOP                     
4377: 00         NOP                     
4378: 00         NOP                     
4379: 13         INC     DE              
437A: 00         NOP                     
437B: 00         NOP                     
437C: 00         NOP                     
437D: 00         NOP                     
437E: 00         NOP                     
437F: 00         NOP                     
4380: 00         NOP                     
4381: 01 00 00   LD      BC,$0000        
4384: 00         NOP                     
4385: 00         NOP                     
4386: 00         NOP                     
4387: 00         NOP                     
4388: 00         NOP                     
4389: 00         NOP                     
438A: 00         NOP                     
438B: 00         NOP                     
438C: 00         NOP                     
438D: 00         NOP                     
438E: 00         NOP                     
438F: 00         NOP                     
4390: 00         NOP                     
4391: 00         NOP                     
4392: 00         NOP                     
4393: 00         NOP                     
4394: 00         NOP                     
4395: 00         NOP                     
4396: 00         NOP                     
4397: 00         NOP                     
4398: 00         NOP                     
4399: 00         NOP                     
439A: 00         NOP                     
439B: 00         NOP                     
439C: 00         NOP                     
439D: 28 00      JR      Z,$439F         
439F: 13         INC     DE              
43A0: 00         NOP                     
43A1: 26 00      LD      H,$00           
43A3: 00         NOP                     
43A4: 12         LD      (DE),A          
43A5: 12         LD      (DE),A          
43A6: 0A         LD      A,(BC)          
43A7: 12         LD      (DE),A          
43A8: 12         LD      (DE),A          
43A9: 0A         LD      A,(BC)          
43AA: 02         LD      (BC),A          
43AB: 02         LD      (BC),A          
43AC: 02         LD      (BC),A          
43AD: 08 12 08   LD      ($0812),SP      
43B0: 12         LD      (DE),A          
43B1: 08 00 40   LD      ($4000),SP      
43B4: 11 11 11   LD      DE,$1111        
43B7: 00         NOP                     
43B8: 08 12 12   LD      ($1212),SP      
43BB: 12         LD      (DE),A          
43BC: 08 11 08   LD      ($0811),SP      
43BF: 08 08 10   LD      ($1008),SP      
43C2: 08 08 08   LD      ($0808),SP      
43C5: 08 12 08   LD      ($0812),SP      
43C8: 08 08 08   LD      ($0808),SP      
43CB: 52         LD      D,D             
43CC: 08 08 0A   LD      ($0A08),SP      
43CF: 12         LD      (DE),A          
43D0: 08 0A 0A   LD      ($0A0A),SP      
43D3: 13         INC     DE              
43D4: 0A         LD      A,(BC)          
43D5: 0A         LD      A,(BC)          
43D6: 0A         LD      A,(BC)          
43D7: 0A         LD      A,(BC)          
43D8: 0A         LD      A,(BC)          
43D9: 0A         LD      A,(BC)          
43DA: 08 0A 0A   LD      ($0A0A),SP      
43DD: 08 0A 0A   LD      ($0A0A),SP      
43E0: 1B         DEC     DE              
43E1: 1A         LD      A,(DE)          
43E2: 02         LD      (BC),A          
43E3: 02         LD      (BC),A          
43E4: 02         LD      (BC),A          
43E5: 02         LD      (BC),A          
43E6: 02         LD      (BC),A          
43E7: 02         LD      (BC),A          
43E8: 02         LD      (BC),A          
43E9: 42         LD      B,D             
43EA: 02         LD      (BC),A          
43EB: 02         LD      (BC),A          
43EC: 02         LD      (BC),A          
43ED: 02         LD      (BC),A          
43EE: 02         LD      (BC),A          
43EF: 02         LD      (BC),A          
43F0: 12         LD      (DE),A          
43F1: 00         NOP                     
43F2: 02         LD      (BC),A          
43F3: 02         LD      (BC),A          
43F4: 30 08      JR      NC,$43FE        
43F6: 02         LD      (BC),A          
43F7: 02         LD      (BC),A          
43F8: 02         LD      (BC),A          
43F9: 08 08 08   LD      ($0808),SP      
43FC: 12         LD      (DE),A          
43FD: D0         RET     NC              
43FE: 90         SUB     B               
43FF: 90         SUB     B               
4400: D0         RET     NC              
4401: 90         SUB     B               
4402: D4 84 D4   CALL    NC,$D484        
4405: 02         LD      (BC),A          
4406: D0         RET     NC              
4407: 90         SUB     B               
4408: 02         LD      (BC),A          
4409: 80         ADD     A,B             
440A: 02         LD      (BC),A          
440B: 42         LD      B,D             
440C: 12         LD      (DE),A          
440D: 02         LD      (BC),A          
440E: 02         LD      (BC),A          
440F: 02         LD      (BC),A          
4410: 02         LD      (BC),A          
4411: 43         LD      B,E             
4412: 00         NOP                     
4413: 00         NOP                     
4414: 00         NOP                     
4415: 00         NOP                     
4416: 00         NOP                     
4417: 00         NOP                     
4418: 00         NOP                     
4419: 00         NOP                     
441A: 00         NOP                     
441B: 00         NOP                     
441C: 00         NOP                     
441D: 00         NOP                     
441E: 20 00      JR      NZ,$4420        
4420: 02         LD      (BC),A          
4421: 02         LD      (BC),A          
4422: 02         LD      (BC),A          
4423: 40         LD      B,B             
4424: 00         NOP                     
4425: 84         ADD     A,H             
4426: 40         LD      B,B             
4427: 00         NOP                     
4428: 00         NOP                     
4429: 00         NOP                     
442A: 02         LD      (BC),A          
442B: 84         ADD     A,H             
442C: C4 94 00   CALL    NZ,$0094        
442F: 00         NOP                     
4430: 00         NOP                     
4431: 00         NOP                     
4432: 84         ADD     A,H             
4433: 00         NOP                     
4434: 00         NOP                     
4435: 00         NOP                     
4436: C4 10 00   CALL    NZ,$0010        
4439: 00         NOP                     
443A: 00         NOP                     
443B: 00         NOP                     
443C: 00         NOP                     
443D: 10 00      STOP    $00             
443F: 00         NOP                     
4440: 00         NOP                     
4441: 42         LD      B,D             
4442: 02         LD      (BC),A          
4443: 00         NOP                     
4444: 00         NOP                     
4445: 00         NOP                     
4446: 00         NOP                     
4447: 02         LD      (BC),A          
4448: 02         LD      (BC),A          
4449: 02         LD      (BC),A          
444A: 02         LD      (BC),A          
444B: 42         LD      B,D             
444C: 42         LD      B,D             
444D: 00         NOP                     
444E: 10 10      STOP    $10             
4450: 08 18 00   LD      ($0018),SP      
4453: 13         INC     DE              
4454: 00         NOP                     
4455: 12         LD      (DE),A          
4456: 00         NOP                     
4457: 02         LD      (BC),A          
4458: 02         LD      (BC),A          
4459: 02         LD      (BC),A          
445A: 02         LD      (BC),A          
445B: 02         LD      (BC),A          
445C: 02         LD      (BC),A          
445D: 00         NOP                     
445E: 01 00 84   LD      BC,$8400        
4461: 11 84 00   LD      DE,$0084        
4464: 00         NOP                     
4465: 03         INC     BC              
4466: 02         LD      (BC),A          
4467: 02         LD      (BC),A          
4468: 02         LD      (BC),A          
4469: 02         LD      (BC),A          
446A: 02         LD      (BC),A          
446B: 02         LD      (BC),A          
446C: 02         LD      (BC),A          
446D: 02         LD      (BC),A          
446E: 02         LD      (BC),A          
446F: 02         LD      (BC),A          
4470: 02         LD      (BC),A          
4471: 02         LD      (BC),A          
4472: 02         LD      (BC),A          
4473: 02         LD      (BC),A          
4474: 00         NOP                     
4475: 00         NOP                     
4476: 00         NOP                     
4477: 00         NOP                     
4478: 00         NOP                     
4479: 03         INC     BC              
447A: 02         LD      (BC),A          
447B: 42         LD      B,D             
447C: 42         LD      B,D             
447D: 02         LD      (BC),A          
447E: 02         LD      (BC),A          
447F: 02         LD      (BC),A          
4480: 02         LD      (BC),A          
4481: 02         LD      (BC),A          
4482: 02         LD      (BC),A          
4483: 12         LD      (DE),A          
4484: 02         LD      (BC),A          
4485: 02         LD      (BC),A          
4486: 02         LD      (BC),A          
4487: 02         LD      (BC),A          
4488: 00         NOP                     
4489: 02         LD      (BC),A          
448A: 00         NOP                     
448B: 02         LD      (BC),A          
448C: 02         LD      (BC),A          
448D: 01 01 01   LD      BC,$0101        
4490: 00         NOP                     
4491: 00         NOP                     
4492: 01 02 01   LD      BC,$0102        
4495: 02         LD      (BC),A          
4496: 03         INC     BC              
4497: 03         INC     BC              
4498: 02         LD      (BC),A          
4499: 00         NOP                     
449A: 00         NOP                     
449B: 00         NOP                     
449C: 00         NOP                     
449D: 01 01 01   LD      BC,$0101        
44A0: 00         NOP                     
44A1: 00         NOP                     
44A2: 02         LD      (BC),A          
44A3: 02         LD      (BC),A          
44A4: 02         LD      (BC),A          
44A5: 02         LD      (BC),A          
44A6: 03         INC     BC              
44A7: 03         INC     BC              
44A8: 02         LD      (BC),A          
44A9: 00         NOP                     
44AA: 00         NOP                     
44AB: 00         NOP                     
44AC: 00         NOP                     
44AD: 01 01 01   LD      BC,$0101        
44B0: 00         NOP                     
44B1: 00         NOP                     
44B2: 02         LD      (BC),A          
44B3: 02         LD      (BC),A          
44B4: 02         LD      (BC),A          
44B5: 02         LD      (BC),A          
44B6: 01 03 02   LD      BC,$0203        
44B9: 00         NOP                     
44BA: 00         NOP                     
44BB: 00         NOP                     
44BC: 00         NOP                     
44BD: 01 01 01   LD      BC,$0101        
44C0: 00         NOP                     
44C1: 00         NOP                     
44C2: 02         LD      (BC),A          
44C3: 01 02 01   LD      BC,$0102        
44C6: 01 03 02   LD      BC,$0203        
44C9: 00         NOP                     
44CA: 00         NOP                     
44CB: 00         NOP                     
44CC: 00         NOP                     
44CD: 00         NOP                     
44CE: 03         INC     BC              
44CF: 03         INC     BC              
44D0: 00         NOP                     
44D1: 00         NOP                     
44D2: 00         NOP                     
44D3: 01 00 01   LD      BC,$0100        
44D6: 00         NOP                     
44D7: 00         NOP                     
44D8: 01 00 00   LD      BC,$0000        
44DB: 00         NOP                     
44DC: 00         NOP                     
44DD: 00         NOP                     
44DE: 00         NOP                     
44DF: 03         INC     BC              
44E0: 00         NOP                     
44E1: 00         NOP                     
44E2: 00         NOP                     
44E3: 01 00 01   LD      BC,$0100        
44E6: 00         NOP                     
44E7: 00         NOP                     
44E8: 01 00 00   LD      BC,$0000        
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
44F5: 02         LD      (BC),A          
44F6: 03         INC     BC              
44F7: 00         NOP                     
44F8: 00         NOP                     
44F9: 00         NOP                     
44FA: 00         NOP                     
44FB: 00         NOP                     
44FC: 00         NOP                     
44FD: 00         NOP                     
44FE: 00         NOP                     
44FF: 00         NOP                     
4500: 00         NOP                     
4501: 00         NOP                     
4502: 01 03 01   LD      BC,$0103        
4505: 02         LD      (BC),A          
4506: 03         INC     BC              
4507: 01 01 00   LD      BC,$0001        
450A: 00         NOP                     
450B: 00         NOP                     
450C: 00         NOP                     
450D: 00         NOP                     
450E: 00         NOP                     
450F: 00         NOP                     
4510: 00         NOP                     
4511: 00         NOP                     
4512: 03         INC     BC              
4513: 01 02 04   LD      BC,$0402        
4516: 00         NOP                     
4517: 00         NOP                     
4518: 01 00 00   LD      BC,$0000        
451B: 00         NOP                     
451C: 00         NOP                     
451D: 00         NOP                     
451E: 00         NOP                     
451F: 00         NOP                     
4520: 00         NOP                     
4521: 00         NOP                     
4522: 00         NOP                     
4523: 00         NOP                     
4524: 00         NOP                     
4525: 00         NOP                     
4526: 00         NOP                     
4527: 00         NOP                     
4528: 00         NOP                     
4529: 00         NOP                     
452A: 00         NOP                     
452B: 00         NOP                     
452C: 00         NOP                     
452D: 00         NOP                     
452E: 00         NOP                     
452F: 00         NOP                     
4530: 00         NOP                     
4531: 00         NOP                     
4532: 00         NOP                     
4533: 01 01 01   LD      BC,$0101        
4536: 01 03 01   LD      BC,$0103        
4539: 00         NOP                     
453A: 00         NOP                     
453B: 00         NOP                     
453C: 00         NOP                     
453D: 00         NOP                     
453E: 00         NOP                     
453F: 00         NOP                     
4540: 00         NOP                     
4541: 00         NOP                     
4542: 00         NOP                     
4543: 01 03 01   LD      BC,$0103        
4546: 00         NOP                     
4547: 00         NOP                     
4548: 00         NOP                     
4549: 00         NOP                     
454A: 00         NOP                     
454B: 00         NOP                     
454C: 00         NOP                     
454D: 00         NOP                     
454E: 00         NOP                     
454F: 00         NOP                     
4550: 00         NOP                     
4551: 00         NOP                     
4552: 01 01 03   LD      BC,$0301        
4555: 01 01 01   LD      BC,$0101        
4558: 03         INC     BC              
4559: 00         NOP                     
455A: 00         NOP                     
455B: 00         NOP                     
455C: 00         NOP                     
455D: 00         NOP                     
455E: 00         NOP                     
455F: 00         NOP                     
4560: 00         NOP                     
4561: 00         NOP                     
4562: 00         NOP                     
4563: 00         NOP                     
4564: 00         NOP                     
4565: 00         NOP                     
4566: 00         NOP                     
4567: 00         NOP                     
4568: 00         NOP                     
4569: 00         NOP                     
456A: 00         NOP                     
456B: 00         NOP                     
456C: 00         NOP                     
456D: 00         NOP                     
456E: 00         NOP                     
456F: 00         NOP                     
4570: 00         NOP                     
4571: 00         NOP                     
4572: 00         NOP                     
4573: 00         NOP                     
4574: 00         NOP                     
4575: 00         NOP                     
4576: 00         NOP                     
4577: 00         NOP                     
4578: 00         NOP                     
4579: 00         NOP                     
457A: 00         NOP                     
457B: 00         NOP                     
457C: 00         NOP                     
457D: 01 01 01   LD      BC,$0101        
4580: 01 01 02   LD      BC,$0201        
4583: 01 02 02   LD      BC,$0202        
4586: 02         LD      (BC),A          
4587: 03         INC     BC              
4588: 03         INC     BC              
4589: 00         NOP                     
458A: 00         NOP                     
458B: 00         NOP                     
458C: 00         NOP                     
458D: 00         NOP                     
458E: 00         NOP                     
458F: 00         NOP                     
4590: 00         NOP                     
4591: 00         NOP                     
4592: 02         LD      (BC),A          
4593: 02         LD      (BC),A          
4594: 02         LD      (BC),A          
4595: 04         INC     B               
4596: 00         NOP                     
4597: 01 02 00   LD      BC,$0002        
459A: 00         NOP                     
459B: 00         NOP                     
459C: 00         NOP                     
459D: 01 02 02   LD      BC,$0202        
45A0: 00         NOP                     
45A1: 00         NOP                     
45A2: 00         NOP                     
45A3: 00         NOP                     
45A4: 03         INC     BC              
45A5: 00         NOP                     
45A6: 00         NOP                     
45A7: 00         NOP                     
45A8: 00         NOP                     
45A9: 00         NOP                     
45AA: 00         NOP                     
45AB: 00         NOP                     
45AC: 00         NOP                     
45AD: 00         NOP                     
45AE: 00         NOP                     
45AF: 00         NOP                     
45B0: 00         NOP                     
45B1: 00         NOP                     
45B2: 00         NOP                     
45B3: 00         NOP                     
45B4: 02         LD      (BC),A          
45B5: 00         NOP                     
45B6: 00         NOP                     
45B7: 00         NOP                     
45B8: 00         NOP                     
45B9: 00         NOP                     
45BA: 00         NOP                     
45BB: 00         NOP                     
45BC: 00         NOP                     
45BD: 01 01 01   LD      BC,$0101        
45C0: 01 02 02   LD      BC,$0202        
45C3: 02         LD      (BC),A          
45C4: 02         LD      (BC),A          
45C5: 02         LD      (BC),A          
45C6: 00         NOP                     
45C7: 02         LD      (BC),A          
45C8: 02         LD      (BC),A          
45C9: 00         NOP                     
45CA: 00         NOP                     
45CB: 00         NOP                     
45CC: 00         NOP                     
45CD: 01 01 01   LD      BC,$0101        
45D0: 01 02 02   LD      BC,$0202        
45D3: 02         LD      (BC),A          
45D4: 02         LD      (BC),A          
45D5: 04         INC     B               
45D6: 00         NOP                     
45D7: 02         LD      (BC),A          
45D8: 02         LD      (BC),A          
45D9: 00         NOP                     
45DA: 00         NOP                     
45DB: 00         NOP                     
45DC: 00         NOP                     
45DD: 00         NOP                     
45DE: 01 01 01   LD      BC,$0101        
45E1: 02         LD      (BC),A          
45E2: 01 00 00   LD      BC,$0000        
45E5: 00         NOP                     
45E6: 00         NOP                     
45E7: 01 00 00   LD      BC,$0000        
45EA: 00         NOP                     
45EB: 00         NOP                     
45EC: 00         NOP                     
45ED: 00         NOP                     
45EE: 00         NOP                     
45EF: 00         NOP                     
45F0: 00         NOP                     
45F1: 00         NOP                     
45F2: 00         NOP                     
45F3: 00         NOP                     
45F4: 00         NOP                     
45F5: 00         NOP                     
45F6: 00         NOP                     
45F7: 01 00 00   LD      BC,$0000        
45FA: 00         NOP                     
45FB: 00         NOP                     
45FC: 00         NOP                     
45FD: 00         NOP                     
45FE: 00         NOP                     
45FF: 00         NOP                     
4600: 00         NOP                     
4601: 00         NOP                     
4602: 00         NOP                     
4603: 00         NOP                     
4604: 00         NOP                     
4605: 00         NOP                     
4606: 00         NOP                     
4607: 01 00 00   LD      BC,$0000        
460A: 00         NOP                     
460B: 00         NOP                     
460C: 00         NOP                     
460D: 01 01 01   LD      BC,$0101        
4610: 01 01 00   LD      BC,$0001        
4613: 00         NOP                     
4614: 00         NOP                     
4615: 00         NOP                     
4616: 00         NOP                     
4617: 00         NOP                     
4618: 00         NOP                     
4619: 00         NOP                     
461A: 00         NOP                     
461B: 00         NOP                     
461C: 00         NOP                     
461D: 01 01 01   LD      BC,$0101        
4620: 01 01 00   LD      BC,$0001        
4623: 00         NOP                     
4624: 02         LD      (BC),A          
4625: 00         NOP                     
4626: 00         NOP                     
4627: 02         LD      (BC),A          
4628: 02         LD      (BC),A          
4629: 00         NOP                     
462A: 00         NOP                     
462B: 00         NOP                     
462C: 00         NOP                     
462D: 01 01 01   LD      BC,$0101        
4630: 01 01 00   LD      BC,$0001        
4633: 00         NOP                     
4634: 00         NOP                     
4635: 00         NOP                     
4636: 00         NOP                     
4637: 02         LD      (BC),A          
4638: 00         NOP                     
4639: 00         NOP                     
463A: 00         NOP                     
463B: 00         NOP                     
463C: 00         NOP                     
463D: 01 01 01   LD      BC,$0101        
4640: 01 01 01   LD      BC,$0101        
4643: 00         NOP                     
4644: 02         LD      (BC),A          
4645: 00         NOP                     
4646: 00         NOP                     
4647: 01 00 00   LD      BC,$0000        
464A: 00         NOP                     
464B: 00         NOP                     
464C: 00         NOP                     
464D: 01 01 01   LD      BC,$0101        
4650: 01 01 00   LD      BC,$0001        
4653: 00         NOP                     
4654: 00         NOP                     
4655: 00         NOP                     
4656: 00         NOP                     
4657: 01 00 00   LD      BC,$0000        
465A: 00         NOP                     
465B: 00         NOP                     
465C: 00         NOP                     
465D: 01 01 01   LD      BC,$0101        
4660: 01 01 00   LD      BC,$0001        
4663: 00         NOP                     
4664: 02         LD      (BC),A          
4665: 00         NOP                     
4666: 00         NOP                     
4667: 00         NOP                     
4668: 00         NOP                     
4669: 00         NOP                     
466A: 00         NOP                     
466B: 00         NOP                     
466C: 00         NOP                     
466D: 01 01 01   LD      BC,$0101        
4670: 01 01 01   LD      BC,$0101        
4673: 02         LD      (BC),A          
4674: 02         LD      (BC),A          
4675: 00         NOP                     
4676: 00         NOP                     
4677: 02         LD      (BC),A          
4678: 00         NOP                     
4679: 00         NOP                     
467A: 00         NOP                     
467B: 00         NOP                     
467C: 00         NOP                     
467D: 01 01 01   LD      BC,$0101        
4680: 01 01 00   LD      BC,$0001        
4683: 00         NOP                     
4684: 00         NOP                     
4685: 00         NOP                     
4686: 00         NOP                     
4687: 02         LD      (BC),A          
4688: 00         NOP                     
4689: 00         NOP                     
468A: 00         NOP                     
468B: 00         NOP                     
468C: 00         NOP                     
468D: 01 01 01   LD      BC,$0101        
4690: 01 01 01   LD      BC,$0101        
4693: 00         NOP                     
4694: 00         NOP                     
4695: 00         NOP                     
4696: 00         NOP                     
4697: 02         LD      (BC),A          
4698: 01 00 00   LD      BC,$0000        
469B: 00         NOP                     
469C: 00         NOP                     
469D: 01 01 01   LD      BC,$0101        
46A0: 01 01 01   LD      BC,$0101        
46A3: 02         LD      (BC),A          
46A4: 01 02 00   LD      BC,$0002        
46A7: 01 02 00   LD      BC,$0002        
46AA: 00         NOP                     
46AB: 00         NOP                     
46AC: 00         NOP                     
46AD: 01 01 01   LD      BC,$0101        
46B0: 01 01 01   LD      BC,$0101        
46B3: 02         LD      (BC),A          
46B4: 01 02 00   LD      BC,$0002        
46B7: 01 02 00   LD      BC,$0002        
46BA: 00         NOP                     
46BB: 00         NOP                     
46BC: 00         NOP                     
46BD: 00         NOP                     
46BE: 00         NOP                     
46BF: 00         NOP                     
46C0: 00         NOP                     
46C1: 00         NOP                     
46C2: 00         NOP                     
46C3: 00         NOP                     
46C4: 01 00 00   LD      BC,$0000        
46C7: 00         NOP                     
46C8: 00         NOP                     
46C9: 00         NOP                     
46CA: 00         NOP                     
46CB: 00         NOP                     
46CC: 00         NOP                     
46CD: 01 01 01   LD      BC,$0101        
46D0: 01 01 01   LD      BC,$0101        
46D3: 01 02 01   LD      BC,$0102        
46D6: 00         NOP                     
46D7: 03         INC     BC              
46D8: 00         NOP                     
46D9: 00         NOP                     
46DA: 00         NOP                     
46DB: 00         NOP                     
46DC: 00         NOP                     
46DD: 01 01 01   LD      BC,$0101        
46E0: 01 01 01   LD      BC,$0101        
46E3: 01 00 00   LD      BC,$0000        
46E6: 00         NOP                     
46E7: 01 02 00   LD      BC,$0002        
46EA: 00         NOP                     
46EB: 00         NOP                     
46EC: 00         NOP                     
46ED: 01 01 01   LD      BC,$0101        
46F0: 01 01 01   LD      BC,$0101        
46F3: 02         LD      (BC),A          
46F4: 01 02 00   LD      BC,$0002        
46F7: 01 02 00   LD      BC,$0002        
46FA: 00         NOP                     
46FB: 00         NOP                     
46FC: 00         NOP                     
46FD: 01 01 01   LD      BC,$0101        
4700: 01 01 01   LD      BC,$0101        
4703: 02         LD      (BC),A          
4704: 01 02 00   LD      BC,$0002        
4707: 01 02 00   LD      BC,$0002        
470A: 00         NOP                     
470B: 00         NOP                     
470C: 00         NOP                     
470D: 00         NOP                     
470E: 00         NOP                     
470F: 00         NOP                     
4710: 00         NOP                     
4711: 00         NOP                     
4712: 00         NOP                     
4713: 00         NOP                     
4714: 00         NOP                     
4715: 00         NOP                     
4716: 00         NOP                     
4717: 00         NOP                     
4718: 00         NOP                     
4719: 00         NOP                     
471A: 00         NOP                     
471B: 00         NOP                     
471C: 00         NOP                     
471D: 00         NOP                     
471E: 00         NOP                     
471F: 01 01 01   LD      BC,$0101        
4722: 00         NOP                     
4723: 02         LD      (BC),A          
4724: 00         NOP                     
4725: 02         LD      (BC),A          
4726: 00         NOP                     
4727: 03         INC     BC              
4728: 00         NOP                     
4729: 00         NOP                     
472A: 00         NOP                     
472B: 00         NOP                     
472C: 00         NOP                     
472D: 01 01 01   LD      BC,$0101        
4730: 00         NOP                     
4731: 00         NOP                     
4732: 02         LD      (BC),A          
4733: 02         LD      (BC),A          
4734: 02         LD      (BC),A          
4735: 02         LD      (BC),A          
4736: 00         NOP                     
4737: 00         NOP                     
4738: 02         LD      (BC),A          
4739: 00         NOP                     
473A: 00         NOP                     
473B: 00         NOP                     
473C: 00         NOP                     
473D: 01 01 01   LD      BC,$0101        
4740: 00         NOP                     
4741: 00         NOP                     
4742: 02         LD      (BC),A          
4743: 00         NOP                     
4744: 00         NOP                     
4745: 05         DEC     B               
4746: 02         LD      (BC),A          
4747: 03         INC     BC              
4748: 03         INC     BC              
4749: 00         NOP                     
474A: 00         NOP                     
474B: 00         NOP                     
474C: 00         NOP                     
474D: 00         NOP                     
474E: 00         NOP                     
474F: 00         NOP                     
4750: 00         NOP                     
4751: 00         NOP                     
4752: 00         NOP                     
4753: 00         NOP                     
4754: 00         NOP                     
4755: 05         DEC     B               
4756: 00         NOP                     
4757: 00         NOP                     
4758: 00         NOP                     
4759: 00         NOP                     
475A: 00         NOP                     
475B: 00         NOP                     
475C: 00         NOP                     
475D: 01 01 01   LD      BC,$0101        
4760: 01 01 01   LD      BC,$0101        
4763: 02         LD      (BC),A          
4764: 01 04 00   LD      BC,$0004        
4767: 01 02 00   LD      BC,$0002        
476A: 00         NOP                     
476B: 00         NOP                     
476C: 00         NOP                     
476D: 00         NOP                     
476E: 00         NOP                     
476F: 00         NOP                     
4770: 00         NOP                     
4771: 00         NOP                     
4772: 00         NOP                     
4773: 00         NOP                     
4774: 02         LD      (BC),A          
4775: 04         INC     B               
4776: 00         NOP                     
4777: 02         LD      (BC),A          
4778: 02         LD      (BC),A          
4779: 00         NOP                     
477A: 00         NOP                     
477B: 00         NOP                     
477C: 00         NOP                     
477D: 01 01 01   LD      BC,$0101        
4780: 01 01 01   LD      BC,$0101        
4783: 01 02 04   LD      BC,$0402        
4786: 00         NOP                     
4787: 03         INC     BC              
4788: 02         LD      (BC),A          
4789: 00         NOP                     
478A: 00         NOP                     
478B: 00         NOP                     
478C: 00         NOP                     
478D: 01 01 01   LD      BC,$0101        
4790: 01 01 02   LD      BC,$0201        
4793: 02         LD      (BC),A          
4794: 01 01 00   LD      BC,$0001        
4797: 03         INC     BC              
4798: 02         LD      (BC),A          
4799: 00         NOP                     
479A: 00         NOP                     
479B: 00         NOP                     
479C: 00         NOP                     
479D: 00         NOP                     
479E: 01 02 40   LD      BC,$4002        
47A1: 00         NOP                     
47A2: 00         NOP                     
47A3: 00         NOP                     
47A4: 00         NOP                     
47A5: 00         NOP                     
47A6: 02         LD      (BC),A          
47A7: 01 40 00   LD      BC,$0040        
47AA: 00         NOP                     
47AB: 00         NOP                     
47AC: 00         NOP                     
47AD: 00         NOP                     
47AE: 04         INC     B               
47AF: 02         LD      (BC),A          
47B0: 40         LD      B,B             
47B1: 00         NOP                     
47B2: 00         NOP                     
47B3: 00         NOP                     
47B4: 00         NOP                     
47B5: 00         NOP                     
47B6: 08 04 40   LD      ($4004),SP      
47B9: 00         NOP                     
47BA: 00         NOP                     
47BB: 00         NOP                     
47BC: 00         NOP                     
47BD: 00         NOP                     
47BE: 10 08      STOP    $08             
47C0: 40         LD      B,B             
47C1: 00         NOP                     
47C2: 00         NOP                     
47C3: 00         NOP                     
47C4: 00         NOP                     
47C5: 00         NOP                     
47C6: 01 04 40   LD      BC,$4004        
47C9: 00         NOP                     
47CA: 00         NOP                     
47CB: 00         NOP                     
47CC: 00         NOP                     
47CD: 00         NOP                     
47CE: FF         RST     0X38            
47CF: 02         LD      (BC),A          
47D0: 40         LD      B,B             
47D1: 00         NOP                     
47D2: 00         NOP                     
47D3: 00         NOP                     
47D4: 00         NOP                     
47D5: 00         NOP                     
47D6: 01 04 40   LD      BC,$4004        
47D9: 00         NOP                     
47DA: 00         NOP                     
47DB: 00         NOP                     
47DC: 00         NOP                     
47DD: 00         NOP                     
47DE: FF         RST     0X38            
47DF: 18 FE      JR      $47DF           
47E1: 02         LD      (BC),A          
47E2: FD                              
47E3: 00         NOP                     
47E4: 00         NOP                     
47E5: 00         NOP                     
47E6: FF         RST     0X38            
47E7: FD                              
47E8: FE 00      CP      $00             
47EA: 00         NOP                     
47EB: 00         NOP                     
47EC: 00         NOP                     
47ED: 00         NOP                     
47EE: 01 04 FE   LD      BC,$FE04        
47F1: 00         NOP                     
47F2: 00         NOP                     
47F3: 00         NOP                     
47F4: 00         NOP                     
47F5: 00         NOP                     
47F6: FF         RST     0X38            
47F7: 02         LD      (BC),A          
47F8: 40         LD      B,B             
47F9: 00         NOP                     
47FA: 00         NOP                     
47FB: 00         NOP                     
47FC: 00         NOP                     
47FD: 00         NOP                     
47FE: 01 02 40   LD      BC,$4002        
4801: 00         NOP                     
4802: 00         NOP                     
4803: 00         NOP                     
4804: 00         NOP                     
4805: 00         NOP                     
4806: 01 02 40   LD      BC,$4002        
4809: 00         NOP                     
480A: 00         NOP                     
480B: 00         NOP                     
480C: 00         NOP                     
480D: 00         NOP                     
480E: 01 02 40   LD      BC,$4002        
4811: 00         NOP                     
4812: 00         NOP                     
4813: 00         NOP                     
4814: 00         NOP                     
4815: 00         NOP                     
4816: 01 02 40   LD      BC,$4002        
4819: 00         NOP                     
481A: 00         NOP                     
481B: 00         NOP                     
481C: 00         NOP                     
481D: 01 02 02   LD      BC,$0202        
4820: 04         INC     B               
4821: 04         INC     B               
4822: 04         INC     B               
4823: 04         INC     B               
4824: 04         INC     B               
4825: 04         INC     B               
4826: 04         INC     B               
4827: 04         INC     B               
4828: 04         INC     B               
4829: 04         INC     B               
482A: 04         INC     B               
482B: 04         INC     B               
482C: 04         INC     B               
482D: 0C         INC     C               
482E: 3F         CCF                     
482F: 08 08 08   LD      ($0808),SP      
4832: 0C         INC     C               
4833: 00         NOP                     
4834: 00         NOP                     
4835: 04         INC     B               
4836: 06 08      LD      B,$08           
4838: 0A         LD      A,(BC)          
4839: 04         INC     B               
483A: 14         INC     D               
483B: 0A         LD      A,(BC)          
483C: 18 04      JR      $4842           
483E: 02         LD      (BC),A          
483F: 08 08 02   LD      ($0208),SP      
4842: 04         INC     B               
4843: FF         RST     0X38            
4844: 00         NOP                     
4845: 02         LD      (BC),A          
4846: 04         INC     B               
4847: 02         LD      (BC),A          
4848: 03         INC     BC              
4849: 01 01 08   LD      BC,$0801        
484C: 06 02      LD      B,$02           
484E: 04         INC     B               
484F: 04         INC     B               
4850: 08 08 18   LD      ($1808),SP      
4853: 08 04 08   LD      ($0804),SP      
4856: 10 08      STOP    $08             
4858: 10 08      STOP    $08             
485A: 08 04 08   LD      ($0804),SP      
485D: 08 08 08   LD      ($0808),SP      
4860: 08 08 08   LD      ($0808),SP      
4863: 0C         INC     C               
4864: 00         NOP                     
4865: 00         NOP                     
4866: 08 08 08   LD      ($0808),SP      
4869: 0C         INC     C               
486A: 0C         INC     C               
486B: 14         INC     D               
486C: 10 20      STOP    $20             
486E: 08 08 04   LD      ($0408),SP      
4871: 04         INC     B               
4872: 04         INC     B               
4873: 04         INC     B               
4874: 04         INC     B               
4875: 00         NOP                     
4876: 14         INC     D               
4877: 08 04 08   LD      ($0804),SP      
487A: 04         INC     B               
487B: 04         INC     B               
487C: 08 08 04   LD      ($0408),SP      
487F: 02         LD      (BC),A          
4880: 06 01      LD      B,$01           
4882: 03         INC     BC              
4883: 03         INC     BC              
4884: 03         INC     BC              
4885: 0D         DEC     C               
4886: 08 0A 02   LD      ($020A),SP      
4889: 07         RLCA                    
488A: 0B         DEC     BC              
488B: 00         NOP                     
488C: 04         INC     B               
488D: 00         NOP                     
488E: 08 04 0E   LD      ($0E04),SP      
4891: 0E 0E      LD      C,$0E           
4893: 0E 0E      LD      C,$0E           
4895: 00         NOP                     
4896: 03         INC     BC              
4897: 03         INC     BC              
4898: 03         INC     BC              
4899: 03         INC     BC              
489A: 03         INC     BC              
489B: 03         INC     BC              
489C: 03         INC     BC              
489D: 03         INC     BC              
489E: 03         INC     BC              
489F: 03         INC     BC              
48A0: 02         LD      (BC),A          
48A1: 00         NOP                     
48A2: 00         NOP                     
48A3: 02         LD      (BC),A          
48A4: 00         NOP                     
48A5: 00         NOP                     
48A6: 00         NOP                     
48A7: 00         NOP                     
48A8: 06 06      LD      B,$06           
48AA: 0D         DEC     C               
48AB: 0E 00      LD      C,$00           
48AD: 09         ADD     HL,BC           
48AE: 03         INC     BC              
48AF: 06 CD      LD      B,$CD           
48B1: CF         RST     0X08            
48B2: 38 F0      JR      C,$48A4         
48B4: F6 21      OR      $21             
48B6: E0 C3      LDFF00  ($C3),A         
48B8: 09         ADD     HL,BC           
48B9: 77         LD      (HL),A          
48BA: 21 60 C4   LD      HL,$C460        
48BD: 09         ADD     HL,BC           
48BE: 36 FF      LD      (HL),$FF        
48C0: 21 A0 C3   LD      HL,$C3A0        
48C3: 09         ADD     HL,BC           
48C4: 5E         LD      E,(HL)          
48C5: 50         LD      D,B             
48C6: 21 E9 40   LD      HL,$40E9        
48C9: 19         ADD     HL,DE           
48CA: 7E         LD      A,(HL)          
48CB: 21 40 C3   LD      HL,$C340        
48CE: 09         ADD     HL,BC           
48CF: 77         LD      (HL),A          
48D0: 21 D2 41   LD      HL,$41D2        
48D3: 19         ADD     HL,DE           
48D4: 7E         LD      A,(HL)          
48D5: 21 50 C3   LD      HL,$C350        
48D8: 09         ADD     HL,BC           
48D9: 77         LD      (HL),A          
48DA: CD EA 48   CALL    $48EA           
48DD: 21 A4 43   LD      HL,$43A4        
48E0: 19         ADD     HL,DE           
48E1: 7E         LD      A,(HL)          
48E2: 21 30 C4   LD      HL,$C430        
48E5: 09         ADD     HL,BC           
48E6: 77         LD      (HL),A          
48E7: C3 65 3B   JP      $3B65           
48EA: D5         PUSH    DE              
48EB: 21 BB 42   LD      HL,$42BB        
48EE: 19         ADD     HL,DE           
48EF: 5E         LD      E,(HL)          
48F0: 21 D0 C4   LD      HL,$C4D0        
48F3: 09         ADD     HL,BC           
48F4: 73         LD      (HL),E          
48F5: 50         LD      D,B             
48F6: 21 1D 48   LD      HL,$481D        
48F9: 19         ADD     HL,DE           
48FA: 7E         LD      A,(HL)          
48FB: 21 60 C3   LD      HL,$C360        
48FE: 09         ADD     HL,BC           
48FF: 77         LD      (HL),A          
4900: D1         POP     DE              
4901: C9         RET                     
4902: 3E 01      LD      A,$01           
4904: EA 8F C1   LD      ($C18F),A       
4907: C3 B7 3F   JP      $3FB7           
490A: 21 30 C4   LD      HL,$C430        
490D: 09         ADD     HL,BC           
490E: 7E         LD      A,(HL)          
490F: E6 80      AND     $80             
4911: 28 5A      JR      Z,$496D         
4913: F0 F8      LD      A,($F8)         
4915: E6 30      AND     $30             
4917: 28 03      JR      Z,$491C         
4919: C3 B7 3F   JP      $3FB7           
491C: F0 EB      LD      A,($EB)         
491E: FE 5F      CP      $5F             
4920: 20 23      JR      NZ,$4945        
4922: F0 F6      LD      A,($F6)         
4924: FE 95      CP      $95             
4926: 28 1D      JR      Z,$4945         
4928: FE 92      CP      $92             
492A: 28 19      JR      Z,$4945         
492C: FE 84      CP      $84             
492E: 28 07      JR      Z,$4937         
4930: FA 84 D9   LD      A,($D984)       
4933: E6 30      AND     $30             
4935: 28 CB      JR      Z,$4902         
4937: FA 92 D9   LD      A,($D992)       
493A: E6 30      AND     $30             
493C: 28 C4      JR      Z,$4902         
493E: FA 95 D9   LD      A,($D995)       
4941: E6 30      AND     $30             
4943: 28 BD      JR      Z,$4902         
4945: FA A5 DB   LD      A,($DBA5)       
4948: A7         AND     A               
4949: 28 12      JR      Z,$495D         
494B: FA 78 D4   LD      A,($D478)       
494E: A7         AND     A               
494F: 20 0F      JR      NZ,$4960        
4951: 21 30 C4   LD      HL,$C430        
4954: 09         ADD     HL,BC           
4955: 7E         LD      A,(HL)          
4956: E6 04      AND     $04             
4958: 28 03      JR      Z,$495D         
495A: EA CF C1   LD      ($C1CF),A       
495D: CD D2 27   CALL    $27D2           
4960: AF         XOR     A               
4961: EA BD C1   LD      ($C1BD),A       
4964: 3C         INC     A               
4965: EA BE C1   LD      ($C1BE),A       
4968: 3E 20      LD      A,$20           
496A: EA 65 C1   LD      ($C165),A       
496D: 21 80 C2   LD      HL,$C280        
4970: 09         ADD     HL,BC           
4971: 36 05      LD      (HL),$05        
4973: F0 EB      LD      A,($EB)         
4975: C7         RST     0X00            
4976: 09         ADD     HL,BC           
4977: 4D         LD      C,L             
4978: 09         ADD     HL,BC           
4979: 4D         LD      C,L             
497A: 09         ADD     HL,BC           
497B: 4D         LD      C,L             
497C: 09         ADD     HL,BC           
497D: 4D         LD      C,L             
497E: 09         ADD     HL,BC           
497F: 4D         LD      C,L             
4980: 09         ADD     HL,BC           
4981: 4D         LD      C,L             
4982: 0D         DEC     C               
4983: 52         LD      D,D             
4984: 23         INC     HL              
4985: 51         LD      D,C             
4986: 09         ADD     HL,BC           
4987: 4D         LD      C,L             
4988: 67         LD      H,A             
4989: 50         LD      D,B             
498A: 09         ADD     HL,BC           
498B: 4D         LD      C,L             
498C: 67         LD      H,A             
498D: 50         LD      D,B             
498E: 09         ADD     HL,BC           
498F: 4D         LD      C,L             
4990: 09         ADD     HL,BC           
4991: 4D         LD      C,L             
4992: 19         ADD     HL,DE           
4993: 4D         LD      C,L             
4994: 09         ADD     HL,BC           
4995: 4D         LD      C,L             
4996: 6D         LD      L,L             
4997: 50         LD      D,B             
4998: 6D         LD      L,L             
4999: 50         LD      D,B             
499A: 6D         LD      L,L             
499B: 50         LD      D,B             
499C: 34         INC     (HL)            
499D: 5A         LD      E,D             
499E: 99         SBC     C               
499F: 4F         LD      C,A             
49A0: 5F         LD      E,A             
49A1: 4F         LD      C,A             
49A2: 85         ADD     A,L             
49A3: 4F         LD      C,A             
49A4: 7B         LD      A,E             
49A5: 4F         LD      C,A             
49A6: 09         ADD     HL,BC           
49A7: 4D         LD      C,L             
49A8: 09         ADD     HL,BC           
49A9: 4D         LD      C,L             
49AA: 09         ADD     HL,BC           
49AB: 4D         LD      C,L             
49AC: 77         LD      (HL),A          
49AD: 4B         LD      C,E             
49AE: 09         ADD     HL,BC           
49AF: 4D         LD      C,L             
49B0: 8E         ADC     A,(HL)          
49B1: 4F         LD      C,A             
49B2: 8D         ADC     A,L             
49B3: 3B         DEC     SP              
49B4: 8D         ADC     A,L             
49B5: 3B         DEC     SP              
49B6: 09         ADD     HL,BC           
49B7: 4D         LD      C,L             
49B8: 8E         ADC     A,(HL)          
49B9: 4F         LD      C,A             
49BA: 09         ADD     HL,BC           
49BB: 4D         LD      C,L             
49BC: 8D         ADC     A,L             
49BD: 3B         DEC     SP              
49BE: 09         ADD     HL,BC           
49BF: 4D         LD      C,L             
49C0: 1E 4D      LD      E,$4D           
49C2: 1E 4D      LD      E,$4D           
49C4: 09         ADD     HL,BC           
49C5: 4D         LD      C,L             
49C6: 09         ADD     HL,BC           
49C7: 4D         LD      C,L             
49C8: DB                              
49C9: 3D         DEC     A               
49CA: 09         ADD     HL,BC           
49CB: 4D         LD      C,L             
49CC: 09         ADD     HL,BC           
49CD: 4D         LD      C,L             
49CE: 09         ADD     HL,BC           
49CF: 4D         LD      C,L             
49D0: D6 4F      SUB     $4F             
49D2: 32         LD      (HLD),A         
49D3: 50         LD      D,B             
49D4: 32         LD      (HLD),A         
49D5: 50         LD      D,B             
49D6: E5         PUSH    HL              
49D7: 4F         LD      C,A             
49D8: 7E         LD      A,(HL)          
49D9: 4C         LD      C,H             
49DA: 32         LD      (HLD),A         
49DB: 50         LD      D,B             
49DC: 32         LD      (HLD),A         
49DD: 50         LD      D,B             
49DE: 32         LD      (HLD),A         
49DF: 50         LD      D,B             
49E0: 13         INC     DE              
49E1: 4D         LD      C,L             
49E2: 32         LD      (HLD),A         
49E3: 50         LD      D,B             
49E4: 32         LD      (HLD),A         
49E5: 50         LD      D,B             
49E6: 32         LD      (HLD),A         
49E7: 50         LD      D,B             
49E8: 59         LD      E,C             
49E9: 50         LD      D,B             
49EA: 13         INC     DE              
49EB: 4D         LD      C,L             
49EC: D6 4F      SUB     $4F             
49EE: D6 4F      SUB     $4F             
49F0: B2         OR      D               
49F1: 4F         LD      C,A             
49F2: 86         ADD     A,(HL)          
49F3: 4C         LD      C,H             
49F4: EC                              
49F5: 4C         LD      C,H             
49F6: FF         RST     0X38            
49F7: 4C         LD      C,H             
49F8: 79         LD      A,C             
49F9: 4C         LD      C,H             
49FA: 09         ADD     HL,BC           
49FB: 4D         LD      C,L             
49FC: 59         LD      E,C             
49FD: 50         LD      D,B             
49FE: 13         INC     DE              
49FF: 4D         LD      C,L             
4A00: 13         INC     DE              
4A01: 4D         LD      C,L             
4A02: 13         INC     DE              
4A03: 4D         LD      C,L             
4A04: 13         INC     DE              
4A05: 4D         LD      C,L             
4A06: 13         INC     DE              
4A07: 4D         LD      C,L             
4A08: 13         INC     DE              
4A09: 4D         LD      C,L             
4A0A: 09         ADD     HL,BC           
4A0B: 4D         LD      C,L             
4A0C: 09         ADD     HL,BC           
4A0D: 4D         LD      C,L             
4A0E: 09         ADD     HL,BC           
4A0F: 4D         LD      C,L             
4A10: 00         NOP                     
4A11: 4D         LD      C,L             
4A12: 09         ADD     HL,BC           
4A13: 4D         LD      C,L             
4A14: F2                              
4A15: 4C         LD      C,H             
4A16: 09         ADD     HL,BC           
4A17: 4D         LD      C,L             
4A18: 09         ADD     HL,BC           
4A19: 4D         LD      C,L             
4A1A: 09         ADD     HL,BC           
4A1B: 4D         LD      C,L             
4A1C: 09         ADD     HL,BC           
4A1D: 4D         LD      C,L             
4A1E: F2                              
4A1F: 4C         LD      C,H             
4A20: 09         ADD     HL,BC           
4A21: 4D         LD      C,L             
4A22: 09         ADD     HL,BC           
4A23: 4D         LD      C,L             
4A24: 09         ADD     HL,BC           
4A25: 4D         LD      C,L             
4A26: 09         ADD     HL,BC           
4A27: 4D         LD      C,L             
4A28: E6 3D      AND     $3D             
4A2A: F1         POP     AF              
4A2B: 3D         DEC     A               
4A2C: FC                              
4A2D: 3D         DEC     A               
4A2E: 07         RLCA                    
4A2F: 3E 12      LD      A,$12           
4A31: 3E 09      LD      A,$09           
4A33: 4D         LD      C,L             
4A34: 09         ADD     HL,BC           
4A35: 4D         LD      C,L             
4A36: 1D         DEC     E               
4A37: 3E 28      LD      A,$28           
4A39: 50         LD      D,B             
4A3A: 28 3E      JR      Z,$4A7A         
4A3C: 33         INC     SP              
4A3D: 3E 14      LD      A,$14           
4A3F: 4D         LD      C,L             
4A40: 3E 3E      LD      A,$3E           
4A42: 09         ADD     HL,BC           
4A43: 4D         LD      C,L             
4A44: 13         INC     DE              
4A45: 4D         LD      C,L             
4A46: 13         INC     DE              
4A47: 4D         LD      C,L             
4A48: E6 4B      AND     $4B             
4A4A: D8         RET     C               
4A4B: 4C         LD      C,H             
4A4C: 13         INC     DE              
4A4D: 4D         LD      C,L             
4A4E: 13         INC     DE              
4A4F: 4D         LD      C,L             
4A50: 61         LD      H,C             
4A51: 4C         LD      C,H             
4A52: 13         INC     DE              
4A53: 4D         LD      C,L             
4A54: 13         INC     DE              
4A55: 4D         LD      C,L             
4A56: EC                              
4A57: 4C         LD      C,H             
4A58: 2B         DEC     HL              
4A59: 4C         LD      C,H             
4A5A: 39         ADD     HL,SP           
4A5B: 4C         LD      C,H             
4A5C: EC                              
4A5D: 4C         LD      C,H             
4A5E: EC                              
4A5F: 4C         LD      C,H             
4A60: EC                              
4A61: 4C         LD      C,H             
4A62: 3A         LD      A,(HLD)         
4A63: 4C         LD      C,H             
4A64: EC                              
4A65: 4C         LD      C,H             
4A66: 13         INC     DE              
4A67: 4D         LD      C,L             
4A68: CB 4C      SET     1,E             
4A6A: 13         INC     DE              
4A6B: 4D         LD      C,L             
4A6C: EC                              
4A6D: 4C         LD      C,H             
4A6E: 3B         DEC     SP              
4A6F: 50         LD      D,B             
4A70: 13         INC     DE              
4A71: 4D         LD      C,L             
4A72: 13         INC     DE              
4A73: 4D         LD      C,L             
4A74: 13         INC     DE              
4A75: 4D         LD      C,L             
4A76: A0         AND     B               
4A77: 4B         LD      C,E             
4A78: 13         INC     DE              
4A79: 4D         LD      C,L             
4A7A: 13         INC     DE              
4A7B: 4D         LD      C,L             
4A7C: BF         CP      A               
4A7D: 4B         LD      C,E             
4A7E: 46         LD      B,(HL)          
4A7F: 4C         LD      C,H             
4A80: 13         INC     DE              
4A81: 4D         LD      C,L             
4A82: 06 4C      LD      B,$4C           
4A84: F4                              
4A85: 4B         LD      C,E             
4A86: 13         INC     DE              
4A87: 4D         LD      C,L             
4A88: 13         INC     DE              
4A89: 4D         LD      C,L             
4A8A: 13         INC     DE              
4A8B: 4D         LD      C,L             
4A8C: 13         INC     DE              
4A8D: 4D         LD      C,L             
4A8E: 13         INC     DE              
4A8F: 4D         LD      C,L             
4A90: 13         INC     DE              
4A91: 4D         LD      C,L             
4A92: 3B         DEC     SP              
4A93: 50         LD      D,B             
4A94: 13         INC     DE              
4A95: 4D         LD      C,L             
4A96: 13         INC     DE              
4A97: 4D         LD      C,L             
4A98: DA 4B 13   JP      C,$134B         
4A9B: 4D         LD      C,L             
4A9C: 13         INC     DE              
4A9D: 4D         LD      C,L             
4A9E: 13         INC     DE              
4A9F: 4D         LD      C,L             
4AA0: A4         AND     H               
4AA1: 4B         LD      C,E             
4AA2: 13         INC     DE              
4AA3: 4D         LD      C,L             
4AA4: 13         INC     DE              
4AA5: 4D         LD      C,L             
4AA6: 4A         LD      C,D             
4AA7: 4B         LD      C,E             
4AA8: 13         INC     DE              
4AA9: 4D         LD      C,L             
4AAA: 13         INC     DE              
4AAB: 4D         LD      C,L             
4AAC: 13         INC     DE              
4AAD: 4D         LD      C,L             
4AAE: 5F         LD      E,A             
4AAF: 4F         LD      C,A             
4AB0: 13         INC     DE              
4AB1: 4D         LD      C,L             
4AB2: D4 4B 13   CALL    NC,$134B        
4AB5: 4D         LD      C,L             
4AB6: 13         INC     DE              
4AB7: 4D         LD      C,L             
4AB8: 61         LD      H,C             
4AB9: 4B         LD      C,E             
4ABA: 13         INC     DE              
4ABB: 4D         LD      C,L             
4ABC: 13         INC     DE              
4ABD: 4D         LD      C,L             
4ABE: 67         LD      H,A             
4ABF: 4B         LD      C,E             
4AC0: 13         INC     DE              
4AC1: 4D         LD      C,L             
4AC2: 13         INC     DE              
4AC3: 4D         LD      C,L             
4AC4: 13         INC     DE              
4AC5: 4D         LD      C,L             
4AC6: 13         INC     DE              
4AC7: 4D         LD      C,L             
4AC8: 13         INC     DE              
4AC9: 4D         LD      C,L             
4ACA: 13         INC     DE              
4ACB: 4D         LD      C,L             
4ACC: 13         INC     DE              
4ACD: 4D         LD      C,L             
4ACE: 13         INC     DE              
4ACF: 4D         LD      C,L             
4AD0: C7         RST     0X00            
4AD1: 4B         LD      C,E             
4AD2: 09         ADD     HL,BC           
4AD3: 4D         LD      C,L             
4AD4: 20 50      JR      NZ,$4B26        
4AD6: 13         INC     DE              
4AD7: 4D         LD      C,L             
4AD8: 13         INC     DE              
4AD9: 4D         LD      C,L             
4ADA: 13         INC     DE              
4ADB: 4D         LD      C,L             
4ADC: 3B         DEC     SP              
4ADD: 50         LD      D,B             
4ADE: 98         SBC     B               
4ADF: 4B         LD      C,E             
4AE0: 13         INC     DE              
4AE1: 4D         LD      C,L             
4AE2: 13         INC     DE              
4AE3: 4D         LD      C,L             
4AE4: 13         INC     DE              
4AE5: 4D         LD      C,L             
4AE6: C3 4B 13   JP      $134B           
4AE9: 4D         LD      C,L             
4AEA: 89         ADC     A,C             
4AEB: 4B         LD      C,E             
4AEC: 97         SUB     A               
4AED: 4B         LD      C,E             
4AEE: 3B         DEC     SP              
4AEF: 50         LD      D,B             
4AF0: 13         INC     DE              
4AF1: 4D         LD      C,L             
4AF2: 13         INC     DE              
4AF3: 4D         LD      C,L             
4AF4: 13         INC     DE              
4AF5: 4D         LD      C,L             
4AF6: 13         INC     DE              
4AF7: 4D         LD      C,L             
4AF8: 7E         LD      A,(HL)          
4AF9: 4B         LD      C,E             
4AFA: 58         LD      E,B             
4AFB: 4B         LD      C,E             
4AFC: 13         INC     DE              
4AFD: 4D         LD      C,L             
4AFE: 13         INC     DE              
4AFF: 4D         LD      C,L             
4B00: 13         INC     DE              
4B01: 4D         LD      C,L             
4B02: 13         INC     DE              
4B03: 4D         LD      C,L             
4B04: 13         INC     DE              
4B05: 4D         LD      C,L             
4B06: 13         INC     DE              
4B07: 4D         LD      C,L             
4B08: 13         INC     DE              
4B09: 4D         LD      C,L             
4B0A: 13         INC     DE              
4B0B: 4D         LD      C,L             
4B0C: 13         INC     DE              
4B0D: 4D         LD      C,L             
4B0E: 13         INC     DE              
4B0F: 4D         LD      C,L             
4B10: 13         INC     DE              
4B11: 4D         LD      C,L             
4B12: 13         INC     DE              
4B13: 4D         LD      C,L             
4B14: 13         INC     DE              
4B15: 4D         LD      C,L             
4B16: 13         INC     DE              
4B17: 4D         LD      C,L             
4B18: 13         INC     DE              
4B19: 4D         LD      C,L             
4B1A: 13         INC     DE              
4B1B: 4D         LD      C,L             
4B1C: 13         INC     DE              
4B1D: 4D         LD      C,L             
4B1E: 13         INC     DE              
4B1F: 4D         LD      C,L             
4B20: 13         INC     DE              
4B21: 4D         LD      C,L             
4B22: 13         INC     DE              
4B23: 4D         LD      C,L             
4B24: 13         INC     DE              
4B25: 4D         LD      C,L             
4B26: 13         INC     DE              
4B27: 4D         LD      C,L             
4B28: 13         INC     DE              
4B29: 4D         LD      C,L             
4B2A: 13         INC     DE              
4B2B: 4D         LD      C,L             
4B2C: 5F         LD      E,A             
4B2D: 4F         LD      C,A             
4B2E: 13         INC     DE              
4B2F: 4D         LD      C,L             
4B30: 13         INC     DE              
4B31: 4D         LD      C,L             
4B32: 13         INC     DE              
4B33: 4D         LD      C,L             
4B34: 13         INC     DE              
4B35: 4D         LD      C,L             
4B36: 13         INC     DE              
4B37: 4D         LD      C,L             
4B38: 13         INC     DE              
4B39: 4D         LD      C,L             
4B3A: 13         INC     DE              
4B3B: 4D         LD      C,L             
4B3C: 13         INC     DE              
4B3D: 4D         LD      C,L             
4B3E: 13         INC     DE              
4B3F: 4D         LD      C,L             
4B40: F8 4B      LDHL    SP,$4B          
4B42: B7         OR      A               
4B43: 4B         LD      C,E             
4B44: 13         INC     DE              
4B45: 4D         LD      C,L             
4B46: 13         INC     DE              
4B47: 4D         LD      C,L             
4B48: 01 04 21   LD      BC,$2104        
4B4B: 60         LD      H,B             
4B4C: C4 09 5E   CALL    NZ,$5E09        
4B4F: 50         LD      D,B             
4B50: 21 48 4B   LD      HL,$4B48        
4B53: 19         ADD     HL,DE           
4B54: 7E         LD      A,(HL)          
4B55: C3 87 3B   JP      $3B87           
4B58: 21 10 C2   LD      HL,$C210        
4B5B: 09         ADD     HL,BC           
4B5C: 7E         LD      A,(HL)          
4B5D: D6 03      SUB     $03             
4B5F: 77         LD      (HL),A          
4B60: C9         RET                     
4B61: CD 8C 08   CALL    $088C           
4B64: 36 30      LD      (HL),$30        
4B66: C9         RET                     
4B67: F0 F6      LD      A,($F6)         
4B69: FE 65      CP      $65             
4B6B: C0         RET     NZ              
4B6C: F0 EC      LD      A,($EC)         
4B6E: FE 50      CP      $50             
4B70: D8         RET     C               
4B71: 21 B0 C2   LD      HL,$C2B0        
4B74: 09         ADD     HL,BC           
4B75: 34         INC     (HL)            
4B76: C9         RET                     
4B77: 21 60 C3   LD      HL,$C360        
4B7A: 09         ADD     HL,BC           
4B7B: 36 02      LD      (HL),$02        
4B7D: C9         RET                     
4B7E: 21 74 DB   LD      HL,$DB74        
4B81: FA 73 DB   LD      A,($DB73)       
4B84: B6         OR      (HL)            
4B85: C2 B7 3F   JP      NZ,$3FB7        
4B88: C9         RET                     
4B89: 21 10 C3   LD      HL,$C310        
4B8C: 09         ADD     HL,BC           
4B8D: 36 10      LD      (HL),$10        
4B8F: CD ED 27   CALL    $27ED           
4B92: 21 D0 C3   LD      HL,$C3D0        
4B95: 09         ADD     HL,BC           
4B96: 77         LD      (HL),A          
4B97: C9         RET                     
4B98: CD 3B 50   CALL    $503B           
4B9B: 3E 02      LD      A,$02           
4B9D: C3 87 3B   JP      $3B87           
4BA0: 3E 33      LD      A,$33           
4BA2: 18 02      JR      $4BA6           
4BA4: 3E 40      LD      A,$40           
4BA6: 5F         LD      E,A             
4BA7: FA 4E DB   LD      A,($DB4E)       
4BAA: A7         AND     A               
4BAB: C8         RET     Z               
4BAC: 7B         LD      A,E             
4BAD: EA 68 D3   LD      ($D368),A       
4BB0: E0 B0      LDFF00  ($B0),A         
4BB2: E0 BD      LDFF00  ($BD),A         
4BB4: E0 BF      LDFF00  ($BF),A         
4BB6: C9         RET                     
4BB7: AF         XOR     A               
4BB8: EA 19 D2   LD      ($D219),A       
4BBB: CD D2 27   CALL    $27D2           
4BBE: C9         RET                     
4BBF: 3E 24      LD      A,$24           
4BC1: 18 EA      JR      $4BAD           
4BC3: 3E 3A      LD      A,$3A           
4BC5: 18 E6      JR      $4BAD           
4BC7: AF         XOR     A               
4BC8: EA 68 C1   LD      ($C168),A       
4BCB: 21 10 C2   LD      HL,$C210        
4BCE: 09         ADD     HL,BC           
4BCF: 7E         LD      A,(HL)          
4BD0: D6 04      SUB     $04             
4BD2: 77         LD      (HL),A          
4BD3: C9         RET                     
4BD4: CD ED 27   CALL    $27ED           
4BD7: C3 87 3B   JP      $3B87           
4BDA: CD 87 08   CALL    $0887           
4BDD: CD ED 27   CALL    $27ED           
4BE0: E6 3F      AND     $3F             
4BE2: C6 10      ADD     $10             
4BE4: 77         LD      (HL),A          
4BE5: C9         RET                     
4BE6: 21 10 C2   LD      HL,$C210        
4BE9: 09         ADD     HL,BC           
4BEA: 7E         LD      A,(HL)          
4BEB: C6 0A      ADD     $0A             
4BED: 77         LD      (HL),A          
4BEE: 21 C0 C2   LD      HL,$C2C0        
4BF1: 09         ADD     HL,BC           
4BF2: 77         LD      (HL),A          
4BF3: C9         RET                     
4BF4: AF         XOR     A               
4BF5: E0 B0      LDFF00  ($B0),A         
4BF7: C9         RET                     
4BF8: CD 24 4C   CALL    $4C24           
4BFB: F0 EE      LD      A,($EE)         
4BFD: CB 37      SET     1,E             
4BFF: E6 01      AND     $01             
4C01: C6 04      ADD     $04             
4C03: C3 87 3B   JP      $3B87           
4C06: F0 EE      LD      A,($EE)         
4C08: CB 37      SET     1,E             
4C0A: E6 01      AND     $01             
4C0C: 5F         LD      E,A             
4C0D: F0 EF      LD      A,($EF)         
4C0F: CB 37      SET     1,E             
4C11: 3C         INC     A               
4C12: 17         RLA                     
4C13: E6 02      AND     $02             
4C15: B3         OR      E               
4C16: CD 87 3B   CALL    $3B87           
4C19: FE 01      CP      $01             
4C1B: 20 07      JR      NZ,$4C24        
4C1D: FA 4B DB   LD      A,($DB4B)       
4C20: A7         AND     A               
4C21: C2 B7 3F   JP      NZ,$3FB7        
4C24: 21 10 C3   LD      HL,$C310        
4C27: 09         ADD     HL,BC           
4C28: 36 13      LD      (HL),$13        
4C2A: C9         RET                     
4C2B: 21 80 C3   LD      HL,$C380        
4C2E: 09         ADD     HL,BC           
4C2F: 36 02      LD      (HL),$02        
4C31: CD 8D 3B   CALL    $3B8D           
4C34: CD 91 08   CALL    $0891           
4C37: 36 20      LD      (HL),$20        
4C39: C9         RET                     
4C3A: F0 F6      LD      A,($F6)         
4C3C: FE D9      CP      $D9             
4C3E: 3E 32      LD      A,$32           
4C40: 20 02      JR      NZ,$4C44        
4C42: 3E 37      LD      A,$37           
4C44: 18 0F      JR      $4C55           
4C46: 21 10 C3   LD      HL,$C310        
4C49: 09         ADD     HL,BC           
4C4A: 36 10      LD      (HL),$10        
4C4C: FA A9 C5   LD      A,($C5A9)       
4C4F: A7         AND     A               
4C50: C2 B7 3F   JP      NZ,$3FB7        
4C53: 3E 0C      LD      A,$0C           
4C55: CD A6 4B   CALL    $4BA6           
4C58: 11 20 C2   LD      DE,$C220        
4C5B: 21 00 C2   LD      HL,$C200        
4C5E: C3 4A 50   JP      $504A           
4C61: F0 F6      LD      A,($F6)         
4C63: FE E2      CP      $E2             
4C65: 20 0A      JR      NZ,$4C71        
4C67: FA 56 DB   LD      A,($DB56)       
4C6A: FE 80      CP      $80             
4C6C: 28 0A      JR      Z,$4C78         
4C6E: C3 B7 3F   JP      $3FB7           
4C71: FA 56 DB   LD      A,($DB56)       
4C74: A7         AND     A               
4C75: C2 B7 3F   JP      NZ,$3FB7        
4C78: C9         RET                     
4C79: F0 F8      LD      A,($F8)         
4C7B: 1F         RRA                     
4C7C: 18 02      JR      $4C80           
4C7E: F0 F8      LD      A,($F8)         
4C80: E6 10      AND     $10             
4C82: C2 B7 3F   JP      NZ,$3FB7        
4C85: C9         RET                     
4C86: F0 F6      LD      A,($F6)         
4C88: FE C0      CP      $C0             
4C8A: 38 1D      JR      C,$4CA9         
4C8C: FA 74 DB   LD      A,($DB74)       
4C8F: A7         AND     A               
4C90: CA B7 3F   JP      Z,$3FB7         
4C93: FA 73 DB   LD      A,($DB73)       
4C96: A7         AND     A               
4C97: C2 B7 3F   JP      NZ,$3FB7        
4C9A: 3C         INC     A               
4C9B: EA C8 C3   LD      ($C3C8),A       
4C9E: 3E 2F      LD      A,$2F           
4CA0: E0 B1      LDFF00  ($B1),A         
4CA2: E0 B0      LDFF00  ($B0),A         
4CA4: E0 BD      LDFF00  ($BD),A         
4CA6: CD CA 27   CALL    $27CA           
4CA9: FA 03 00   LD      A,($0003)       
4CAC: A7         AND     A               
4CAD: 28 3D      JR      Z,$4CEC         
4CAF: FA 4F DB   LD      A,($DB4F)       
4CB2: A7         AND     A               
4CB3: 20 37      JR      NZ,$4CEC        
4CB5: FA 50 DB   LD      A,($DB50)       
4CB8: A7         AND     A               
4CB9: 20 09      JR      NZ,$4CC4        
4CBB: EA 96 DB   LD      ($DB96),A       
4CBE: 3E 01      LD      A,$01           
4CC0: EA 95 DB   LD      ($DB95),A       
4CC3: C9         RET                     
4CC4: 21 A0 C3   LD      HL,$C3A0        
4CC7: 09         ADD     HL,BC           
4CC8: 36 6B      LD      (HL),$6B        
4CCA: C9         RET                     
4CCB: FA 56 DB   LD      A,($DB56)       
4CCE: FE 80      CP      $80             
4CD0: 20 05      JR      NZ,$4CD7        
4CD2: 3E 0E      LD      A,$0E           
4CD4: EA 68 D3   LD      ($D368),A       
4CD7: C9         RET                     
4CD8: FA A5 DB   LD      A,($DBA5)       
4CDB: A7         AND     A               
4CDC: 20 0E      JR      NZ,$4CEC        
4CDE: FA 77 D4   LD      A,($D477)       
4CE1: A7         AND     A               
4CE2: C0         RET     NZ              
4CE3: 21 10 C2   LD      HL,$C210        
4CE6: 09         ADD     HL,BC           
4CE7: 7E         LD      A,(HL)          
4CE8: D6 10      SUB     $10             
4CEA: 77         LD      (HL),A          
4CEB: C9         RET                     
4CEC: 21 80 C3   LD      HL,$C380        
4CEF: 09         ADD     HL,BC           
4CF0: 36 03      LD      (HL),$03        
4CF2: FA 44 DB   LD      A,($DB44)       
4CF5: A7         AND     A               
4CF6: 20 05      JR      NZ,$4CFD        
4CF8: 3E 1C      LD      A,$1C           
4CFA: CD AD 4B   CALL    $4BAD           
4CFD: 18 06      JR      $4D05           
4CFF: C9         RET                     
4D00: 3E 07      LD      A,$07           
4D02: CD A6 4B   CALL    $4BA6           
4D05: 3E 01      LD      A,$01           
4D07: 18 05      JR      $4D0E           
4D09: CD ED 27   CALL    $27ED           
4D0C: E6 03      AND     $03             
4D0E: 21 80 C3   LD      HL,$C380        
4D11: 09         ADD     HL,BC           
4D12: 77         LD      (HL),A          
4D13: C9         RET                     
4D14: 3E 03      LD      A,$03           
4D16: E0 FF      LDFF00  ($FF),A         
4D18: C9         RET                     
4D19: 3E FF      LD      A,$FF           
4D1B: C3 87 3B   JP      $3B87           
4D1E: 34         INC     (HL)            
4D1F: 00         NOP                     
4D20: 34         INC     (HL)            
4D21: 20 34      JR      NZ,$4D57        
4D23: 10 34      STOP    $34             
4D25: 30 CD      JR      NC,$4CF4        
4D27: 91         SUB     C               
4D28: 08 28 26   LD      ($2628),SP      
4D2B: F0 E7      LD      A,($E7)         
4D2D: 1F         RRA                     
4D2E: 1F         RRA                     
4D2F: 1F         RRA                     
4D30: E6 01      AND     $01             
4D32: E0 F1      LDFF00  ($F1),A         
4D34: 11 1E 4D   LD      DE,$4D1E        
4D37: CD 3B 3C   CALL    $3C3B           
4D3A: 21 B0 C3   LD      HL,$C3B0        
4D3D: 09         ADD     HL,BC           
4D3E: 7E         LD      A,(HL)          
4D3F: E0 F1      LDFF00  ($F1),A         
4D41: CD 3D 39   CALL    $393D           
4D44: CD 50 7F   CALL    $7F50           
4D47: CD 6C 7F   CALL    $7F6C           
4D4A: CD D5 60   CALL    $60D5           
4D4D: CD AF 3D   CALL    $3DAF           
4D50: C9         RET                     
4D51: F0 EB      LD      A,($EB)         
4D53: FE 1F      CP      $1F             
4D55: 20 0F      JR      NZ,$4D66        
4D57: 21 A0 C3   LD      HL,$C3A0        
4D5A: 09         ADD     HL,BC           
4D5B: 36 1E      LD      (HL),$1E        
4D5D: 21 80 C2   LD      HL,$C280        
4D60: 09         ADD     HL,BC           
4D61: 36 05      LD      (HL),$05        
4D63: C3 C0 48   JP      $48C0           
4D66: 21 80 C4   LD      HL,$C480        
4D69: 09         ADD     HL,BC           
4D6A: 36 1F      LD      (HL),$1F        
4D6C: 21 80 C2   LD      HL,$C280        
4D6F: 09         ADD     HL,BC           
4D70: 36 01      LD      (HL),$01        
4D72: 21 40 C3   LD      HL,$C340        
4D75: 09         ADD     HL,BC           
4D76: 36 04      LD      (HL),$04        
4D78: 21 F4 FF   LD      HL,$FFF4        
4D7B: 36 13      LD      (HL),$13        
4D7D: C9         RET                     
4D7E: 00         NOP                     
4D7F: 00         NOP                     
4D80: 04         INC     B               
4D81: 00         NOP                     
4D82: 00         NOP                     
4D83: 01 03 06   LD      BC,$0603        
4D86: 24         INC     H               
4D87: 00         NOP                     
4D88: 24         INC     H               
4D89: 00         NOP                     
4D8A: 3E 00      LD      A,$00           
4D8C: 1E 00      LD      E,$00           
4D8E: 1E 60      LD      E,$60           
4D90: CD 91 08   CALL    $0891           
4D93: 20 26      JR      NZ,$4DBB        
4D95: 21 30 C4   LD      HL,$C430        
4D98: 09         ADD     HL,BC           
4D99: 7E         LD      A,(HL)          
4D9A: E6 02      AND     $02             
4D9C: 20 05      JR      NZ,$4DA3        
4D9E: 21 60 D4   LD      HL,$D460        
4DA1: 36 01      LD      (HL),$01        
4DA3: F0 EB      LD      A,($EB)         
4DA5: FE A8      CP      $A8             
4DA7: 20 0F      JR      NZ,$4DB8        
4DA9: 3E 16      LD      A,$16           
4DAB: EA 6F DB   LD      ($DB6F),A       
4DAE: 3E 50      LD      A,$50           
4DB0: EA 70 DB   LD      ($DB70),A       
4DB3: 3E 27      LD      A,$27           
4DB5: EA 71 DB   LD      ($DB71),A       
4DB8: C3 B7 3F   JP      $3FB7           
4DBB: FE 40      CP      $40             
4DBD: 38 1E      JR      C,$4DDD         
4DBF: F0 EB      LD      A,($EB)         
4DC1: FE 09      CP      $09             
4DC3: 28 08      JR      Z,$4DCD         
4DC5: FE 0B      CP      $0B             
4DC7: 28 04      JR      Z,$4DCD         
4DC9: FE 14      CP      $14             
4DCB: 20 09      JR      NZ,$4DD6        
4DCD: CD 58 59   CALL    $5958           
4DD0: CD 58 59   CALL    $5958           
4DD3: CD 58 59   CALL    $5958           
4DD6: CD 3D 39   CALL    $393D           
4DD9: CD 50 7F   CALL    $7F50           
4DDC: C9         RET                     
4DDD: 1F         RRA                     
4DDE: 1F         RRA                     
4DDF: 1F         RRA                     
4DE0: 1F         RRA                     
4DE1: E6 03      AND     $03             
4DE3: 21 B0 C3   LD      HL,$C3B0        
4DE6: 09         ADD     HL,BC           
4DE7: 77         LD      (HL),A          
4DE8: E0 F1      LDFF00  ($F1),A         
4DEA: 5F         LD      E,A             
4DEB: 50         LD      D,B             
4DEC: 21 7E 4D   LD      HL,$4D7E        
4DEF: 19         ADD     HL,DE           
4DF0: F0 EC      LD      A,($EC)         
4DF2: 86         ADD     A,(HL)          
4DF3: E0 EC      LDFF00  ($EC),A         
4DF5: 7B         LD      A,E             
4DF6: FE 03      CP      $03             
4DF8: 20 0B      JR      NZ,$4E05        
4DFA: AF         XOR     A               
4DFB: E0 F1      LDFF00  ($F1),A         
4DFD: 11 8C 4D   LD      DE,$4D8C        
4E00: CD 3B 3C   CALL    $3C3B           
4E03: 18 06      JR      $4E0B           
4E05: 11 86 4D   LD      DE,$4D86        
4E08: CD D0 3C   CALL    $3CD0           
4E0B: CD 50 7F   CALL    $7F50           
4E0E: CD 91 08   CALL    $0891           
4E11: FE 3F      CP      $3F             
4E13: 20 05      JR      NZ,$4E1A        
4E15: 21 F2 FF   LD      HL,$FFF2        
4E18: 36 18      LD      (HL),$18        
4E1A: 1F         RRA                     
4E1B: 1F         RRA                     
4E1C: 1F         RRA                     
4E1D: 1F         RRA                     
4E1E: E6 03      AND     $03             
4E20: 5F         LD      E,A             
4E21: 50         LD      D,B             
4E22: 21 82 4D   LD      HL,$4D82        
4E25: 19         ADD     HL,DE           
4E26: 5E         LD      E,(HL)          
4E27: F0 98      LD      A,($98)         
4E29: F5         PUSH    AF              
4E2A: 21 B0 C4   LD      HL,$C4B0        
4E2D: 09         ADD     HL,BC           
4E2E: 7E         LD      A,(HL)          
4E2F: E0 98      LDFF00  ($98),A         
4E31: F0 99      LD      A,($99)         
4E33: F5         PUSH    AF              
4E34: 21 C0 C4   LD      HL,$C4C0        
4E37: 09         ADD     HL,BC           
4E38: 7E         LD      A,(HL)          
4E39: E0 99      LDFF00  ($99),A         
4E3B: 7B         LD      A,E             
4E3C: CD 99 7E   CALL    $7E99           
4E3F: F1         POP     AF              
4E40: E0 99      LDFF00  ($99),A         
4E42: F1         POP     AF              
4E43: E0 98      LDFF00  ($98),A         
4E45: CD F7 7E   CALL    $7EF7           
4E48: C9         RET                     
4E49: CD 3D 39   CALL    $393D           
4E4C: CD 50 7F   CALL    $7F50           
4E4F: 21 10 C4   LD      HL,$C410        
4E52: 09         ADD     HL,BC           
4E53: 36 02      LD      (HL),$02        
4E55: CD D5 60   CALL    $60D5           
4E58: 21 10 C4   LD      HL,$C410        
4E5B: 09         ADD     HL,BC           
4E5C: 70         LD      (HL),B          
4E5D: CD 23 67   CALL    $6723           
4E60: CD 97 54   CALL    $5497           
4E63: F0 EB      LD      A,($EB)         
4E65: FE 5C      CP      $5C             
4E67: 20 1E      JR      NZ,$4E87        
4E69: 21 A0 C2   LD      HL,$C2A0        
4E6C: 09         ADD     HL,BC           
4E6D: 7E         LD      A,(HL)          
4E6E: A7         AND     A               
4E6F: 28 16      JR      Z,$4E87         
4E71: 21 20 C4   LD      HL,$C420        
4E74: 09         ADD     HL,BC           
4E75: 36 20      LD      (HL),$20        
4E77: 21 F3 FF   LD      HL,$FFF3        
4E7A: 36 07      LD      (HL),$07        
4E7C: 21 40 C4   LD      HL,$C440        
4E7F: 09         ADD     HL,BC           
4E80: 7E         LD      A,(HL)          
4E81: 3C         INC     A               
4E82: 77         LD      (HL),A          
4E83: FE 03      CP      $03             
4E85: 28 1D      JR      Z,$4EA4         
4E87: 3E 0B      LD      A,$0B           
4E89: EA 9E C1   LD      ($C19E),A       
4E8C: CD A6 75   CALL    $75A6           
4E8F: 21 40 C2   LD      HL,$C240        
4E92: 09         ADD     HL,BC           
4E93: 7E         LD      A,(HL)          
4E94: 21 50 C2   LD      HL,$C250        
4E97: 09         ADD     HL,BC           
4E98: B6         OR      (HL)            
4E99: 20 1E      JR      NZ,$4EB9        
4E9B: CD 6B 72   CALL    $726B           
4E9E: F0 EB      LD      A,($EB)         
4EA0: FE 5C      CP      $5C             
4EA2: 20 15      JR      NZ,$4EB9        
4EA4: 21 80 C2   LD      HL,$C280        
4EA7: 09         ADD     HL,BC           
4EA8: 36 05      LD      (HL),$05        
4EAA: CD 8D 3B   CALL    $3B8D           
4EAD: 36 01      LD      (HL),$01        
4EAF: CD 91 08   CALL    $0891           
4EB2: 36 80      LD      (HL),$80        
4EB4: 21 D0 C2   LD      HL,$C2D0        
4EB7: 09         ADD     HL,BC           
4EB8: 70         LD      (HL),B          
4EB9: C9         RET                     
4EBA: 10 F0      STOP    $F0             
4EBC: CD 3D 39   CALL    $393D           
4EBF: CD 50 7F   CALL    $7F50           
4EC2: CD 6C 7F   CALL    $7F6C           
4EC5: CD D5 60   CALL    $60D5           
4EC8: CD AF 3D   CALL    $3DAF           
4ECB: CD 40 6E   CALL    $6E40           
4ECE: FA 00 DB   LD      A,($DB00)       
4ED1: FE 03      CP      $03             
4ED3: 20 08      JR      NZ,$4EDD        
4ED5: F0 CC      LD      A,($CC)         
4ED7: E6 20      AND     $20             
4ED9: 20 0F      JR      NZ,$4EEA        
4EDB: 18 4A      JR      $4F27           
4EDD: FA 01 DB   LD      A,($DB01)       
4EE0: FE 03      CP      $03             
4EE2: 20 43      JR      NZ,$4F27        
4EE4: F0 CC      LD      A,($CC)         
4EE6: E6 10      AND     $10             
4EE8: 28 3D      JR      Z,$4F27         
4EEA: FA CF C3   LD      A,($C3CF)       
4EED: A7         AND     A               
4EEE: 20 37      JR      NZ,$4F27        
4EF0: 21 40 C3   LD      HL,$C340        
4EF3: 09         ADD     HL,BC           
4EF4: 7E         LD      A,(HL)          
4EF5: E5         PUSH    HL              
4EF6: F5         PUSH    AF              
4EF7: F6 80      OR      $80             
4EF9: 77         LD      (HL),A          
4EFA: CD 8E 6C   CALL    $6C8E           
4EFD: CB 13      SET     1,E             
4EFF: F1         POP     AF              
4F00: E1         POP     HL              
4F01: 77         LD      (HL),A          
4F02: CB 1B      SET     1,E             
4F04: 30 21      JR      NC,$4F27        
4F06: 3E 01      LD      A,$01           
4F08: EA CF C3   LD      ($C3CF),A       
4F0B: 21 80 C2   LD      HL,$C280        
4F0E: 09         ADD     HL,BC           
4F0F: 36 07      LD      (HL),$07        
4F11: 3E 02      LD      A,$02           
4F13: E0 F3      LDFF00  ($F3),A         
4F15: 21 90 C4   LD      HL,$C490        
4F18: 09         ADD     HL,BC           
4F19: 70         LD      (HL),B          
4F1A: CD 91 08   CALL    $0891           
4F1D: 36 02      LD      (HL),$02        
4F1F: F0 9E      LD      A,($9E)         
4F21: EA 5D C1   LD      ($C15D),A       
4F24: C3 92 57   JP      $5792           
4F27: 21 00 C3   LD      HL,$C300        
4F2A: 09         ADD     HL,BC           
4F2B: 7E         LD      A,(HL)          
4F2C: A7         AND     A               
4F2D: 20 0B      JR      NZ,$4F3A        
4F2F: 21 80 C2   LD      HL,$C280        
4F32: 09         ADD     HL,BC           
4F33: 36 05      LD      (HL),$05        
4F35: 21 20 C3   LD      HL,$C320        
4F38: 09         ADD     HL,BC           
4F39: 70         LD      (HL),B          
4F3A: FE 3C      CP      $3C             
4F3C: 30 18      JR      NC,$4F56        
4F3E: CB 3F      SET     1,E             
4F40: CB 3F      SET     1,E             
4F42: E6 01      AND     $01             
4F44: 5F         LD      E,A             
4F45: 50         LD      D,B             
4F46: 21 BA 4E   LD      HL,$4EBA        
4F49: 19         ADD     HL,DE           
4F4A: 7E         LD      A,(HL)          
4F4B: 21 40 C2   LD      HL,$C240        
4F4E: 09         ADD     HL,BC           
4F4F: 77         LD      (HL),A          
4F50: CD 04 7F   CALL    $7F04           
4F53: CD AF 3D   CALL    $3DAF           
4F56: C9         RET                     
4F57: 0C         INC     C               
4F58: 0C         INC     C               
4F59: F4                              
4F5A: F4                              
4F5B: 0C         INC     C               
4F5C: F4                              
4F5D: 0C         INC     C               
4F5E: F4                              
4F5F: CD ED 27   CALL    $27ED           
4F62: E6 03      AND     $03             
4F64: 5F         LD      E,A             
4F65: 50         LD      D,B             
4F66: 21 57 4F   LD      HL,$4F57        
4F69: 19         ADD     HL,DE           
4F6A: 7E         LD      A,(HL)          
4F6B: 21 40 C2   LD      HL,$C240        
4F6E: 09         ADD     HL,BC           
4F6F: 77         LD      (HL),A          
4F70: 21 5B 4F   LD      HL,$4F5B        
4F73: 19         ADD     HL,DE           
4F74: 7E         LD      A,(HL)          
4F75: 21 50 C2   LD      HL,$C250        
4F78: 09         ADD     HL,BC           
4F79: 77         LD      (HL),A          
4F7A: C9         RET                     
4F7B: 21 C0 C2   LD      HL,$C2C0        
4F7E: 09         ADD     HL,BC           
4F7F: 36 04      LD      (HL),$04        
4F81: 3E 03      LD      A,$03           
4F83: 18 02      JR      $4F87           
4F85: 3E FD      LD      A,$FD           
4F87: 21 10 C2   LD      HL,$C210        
4F8A: 09         ADD     HL,BC           
4F8B: 86         ADD     A,(HL)          
4F8C: 77         LD      (HL),A          
4F8D: C9         RET                     
4F8E: CD 91 08   CALL    $0891           
4F91: 36 80      LD      (HL),$80        
4F93: 21 B0 C3   LD      HL,$C3B0        
4F96: 09         ADD     HL,BC           
4F97: 35         DEC     (HL)            
4F98: C9         RET                     
4F99: F0 EE      LD      A,($EE)         
4F9B: E6 10      AND     $10             
4F9D: 3E 00      LD      A,$00           
4F9F: 20 02      JR      NZ,$4FA3        
4FA1: 3E 03      LD      A,$03           
4FA3: 21 80 C3   LD      HL,$C380        
4FA6: 09         ADD     HL,BC           
4FA7: 77         LD      (HL),A          
4FA8: E5         PUSH    HL              
4FA9: CD 58 59   CALL    $5958           
4FAC: E1         POP     HL              
4FAD: 7E         LD      A,(HL)          
4FAE: EE 01      XOR     $01             
4FB0: 77         LD      (HL),A          
4FB1: C9         RET                     
4FB2: 21 D0 C2   LD      HL,$C2D0        
4FB5: 09         ADD     HL,BC           
4FB6: 36 02      LD      (HL),$02        
4FB8: F0 F6      LD      A,($F6)         
4FBA: FE A4      CP      $A4             
4FBC: 28 04      JR      Z,$4FC2         
4FBE: FE D2      CP      $D2             
4FC0: 20 04      JR      NZ,$4FC6        
4FC2: 35         DEC     (HL)            
4FC3: CD 3B 50   CALL    $503B           
4FC6: CD DC 4F   CALL    $4FDC           
4FC9: C9         RET                     
4FCA: 21 D0 C2   LD      HL,$C2D0        
4FCD: 09         ADD     HL,BC           
4FCE: 36 01      LD      (HL),$01        
4FD0: FA A5 DB   LD      A,($DBA5)       
4FD3: A7         AND     A               
4FD4: 28 06      JR      Z,$4FDC         
4FD6: 21 D0 C2   LD      HL,$C2D0        
4FD9: 09         ADD     HL,BC           
4FDA: 36 02      LD      (HL),$02        
4FDC: 21 30 C4   LD      HL,$C430        
4FDF: 09         ADD     HL,BC           
4FE0: 7E         LD      A,(HL)          
4FE1: F6 11      OR      $11             
4FE3: 77         LD      (HL),A          
4FE4: C9         RET                     
4FE5: F0 F6      LD      A,($F6)         
4FE7: FE F8      CP      $F8             
4FE9: 20 11      JR      NZ,$4FFC        
4FEB: F0 F8      LD      A,($F8)         
4FED: CB 67      SET     1,E             
4FEF: C2 B7 3F   JP      NZ,$3FB7        
4FF2: CB 6F      SET     1,E             
4FF4: CA B7 3F   JP      Z,$3FB7         
4FF7: 3E 02      LD      A,$02           
4FF9: C3 87 3B   JP      $3B87           
4FFC: FE 7A      CP      $7A             
4FFE: 20 0C      JR      NZ,$500C        
5000: F0 F8      LD      A,($F8)         
5002: E6 10      AND     $10             
5004: C2 B7 3F   JP      NZ,$3FB7        
5007: 3E 04      LD      A,$04           
5009: C3 87 3B   JP      $3B87           
500C: FE 7C      CP      $7C             
500E: 20 0F      JR      NZ,$501F        
5010: FA 69 D9   LD      A,($D969)       
5013: E6 10      AND     $10             
5015: CA B7 3F   JP      Z,$3FB7         
5018: F0 F8      LD      A,($F8)         
501A: E6 10      AND     $10             
501C: C2 B7 3F   JP      NZ,$3FB7        
501F: C9         RET                     
5020: FA 0E DB   LD      A,($DB0E)       
5023: FE 0E      CP      $0E             
5025: 28 14      JR      Z,$503B         
5027: C9         RET                     
5028: FA A5 DB   LD      A,($DBA5)       
502B: A7         AND     A               
502C: C8         RET     Z               
502D: CD 8D 3B   CALL    $3B8D           
5030: 18 09      JR      $503B           
5032: CD CA 4F   CALL    $4FCA           
5035: FA A5 DB   LD      A,($DBA5)       
5038: A7         AND     A               
5039: 20 26      JR      NZ,$5061        
503B: 11 20 C2   LD      DE,$C220        
503E: 21 00 C2   LD      HL,$C200        
5041: CD 4A 50   CALL    $504A           
5044: 11 30 C2   LD      DE,$C230        
5047: 21 10 C2   LD      HL,$C210        
504A: 09         ADD     HL,BC           
504B: 7E         LD      A,(HL)          
504C: C6 08      ADD     $08             
504E: 77         LD      (HL),A          
504F: 17         RLA                     
5050: D5         PUSH    DE              
5051: E1         POP     HL              
5052: 09         ADD     HL,BC           
5053: 1F         RRA                     
5054: 7E         LD      A,(HL)          
5055: CE 00      ADC     $00             
5057: 77         LD      (HL),A          
5058: C9         RET                     
5059: 11 20 C2   LD      DE,$C220        
505C: 21 00 C2   LD      HL,$C200        
505F: 18 E9      JR      $504A           
5061: CD 87 08   CALL    $0887           
5064: 36 80      LD      (HL),$80        
5066: C9         RET                     
5067: CD 8C 08   CALL    $088C           
506A: 36 A0      LD      (HL),$A0        
506C: C9         RET                     
506D: F0 EB      LD      A,($EB)         
506F: FE 12      CP      $12             
5071: 20 0D      JR      NZ,$5080        
5073: 21 D0 C2   LD      HL,$C2D0        
5076: 09         ADD     HL,BC           
5077: 36 01      LD      (HL),$01        
5079: 21 10 C3   LD      HL,$C310        
507C: 09         ADD     HL,BC           
507D: 36 10      LD      (HL),$10        
507F: C9         RET                     
5080: CD 8D 3B   CALL    $3B8D           
5083: C9         RET                     
5084: 60         LD      H,B             
5085: 00         NOP                     
5086: 62         LD      H,D             
5087: 00         NOP                     
5088: 62         LD      H,D             
5089: 20 60      JR      NZ,$50EB        
508B: 20 64      JR      NZ,$50F1        
508D: 00         NOP                     
508E: 66         LD      H,(HL)          
508F: 00         NOP                     
5090: 66         LD      H,(HL)          
5091: 20 64      JR      NZ,$50F7        
5093: 20 68      JR      NZ,$50FD        
5095: 00         NOP                     
5096: 6A         LD      L,D             
5097: 00         NOP                     
5098: 6C         LD      L,H             
5099: 00         NOP                     
509A: 6E         LD      L,(HL)          
509B: 00         NOP                     
509C: 6A         LD      L,D             
509D: 20 68      JR      NZ,$5107        
509F: 20 6E      JR      NZ,$510F        
50A1: 20 6C      JR      NZ,$510F        
50A3: 20 70      JR      NZ,$5115        
50A5: 00         NOP                     
50A6: 72         LD      (HL),D          
50A7: 00         NOP                     
50A8: 72         LD      (HL),D          
50A9: 20 70      JR      NZ,$511B        
50AB: 20 0C      JR      NZ,$50B9        
50AD: F4                              
50AE: 00         NOP                     
50AF: 00         NOP                     
50B0: 00         NOP                     
50B1: 00         NOP                     
50B2: F4                              
50B3: 0C         INC     C               
50B4: 21 C0 C2   LD      HL,$C2C0        
50B7: 09         ADD     HL,BC           
50B8: 7E         LD      A,(HL)          
50B9: A7         AND     A               
50BA: 28 46      JR      Z,$5102         
50BC: 11 A4 50   LD      DE,$50A4        
50BF: CD 3B 3C   CALL    $3C3B           
50C2: CD 4A 7F   CALL    $7F4A           
50C5: CD 6C 7F   CALL    $7F6C           
50C8: CD 3D 6E   CALL    $6E3D           
50CB: CD F7 7E   CALL    $7EF7           
50CE: CD 92 78   CALL    $7892           
50D1: CD 91 08   CALL    $0891           
50D4: 20 20      JR      NZ,$50F6        
50D6: CD ED 27   CALL    $27ED           
50D9: E6 1F      AND     $1F             
50DB: C6 20      ADD     $20             
50DD: 77         LD      (HL),A          
50DE: E6 03      AND     $03             
50E0: 5F         LD      E,A             
50E1: 50         LD      D,B             
50E2: 21 AC 50   LD      HL,$50AC        
50E5: 19         ADD     HL,DE           
50E6: 7E         LD      A,(HL)          
50E7: 21 40 C2   LD      HL,$C240        
50EA: 09         ADD     HL,BC           
50EB: 77         LD      (HL),A          
50EC: 21 B0 50   LD      HL,$50B0        
50EF: 19         ADD     HL,DE           
50F0: 7E         LD      A,(HL)          
50F1: 21 50 C2   LD      HL,$C250        
50F4: 09         ADD     HL,BC           
50F5: 77         LD      (HL),A          
50F6: F0 E7      LD      A,($E7)         
50F8: 1F         RRA                     
50F9: 1F         RRA                     
50FA: 1F         RRA                     
50FB: 1F         RRA                     
50FC: E6 01      AND     $01             
50FE: CD 87 3B   CALL    $3B87           
5101: C9         RET                     
5102: 11 84 50   LD      DE,$5084        
5105: CD 97 58   CALL    $5897           
5108: C9         RET                     
5109: 62         LD      H,D             
510A: 70         LD      (HL),B          
510B: 63         LD      H,E             
510C: 71         LD      (HL),C          
510D: 03         INC     BC              
510E: 04         INC     B               
510F: 05         DEC     B               
5110: 06 07      LD      B,$07           
5112: 08 09 0A   LD      ($0A09),SP      
5115: 0B         DEC     BC              
5116: 0C         INC     C               
5117: 02         LD      (BC),A          
5118: 01 00 00   LD      BC,$0000        
511B: 00         NOP                     
511C: 00         NOP                     
511D: 01 32 14   LD      BC,$1432        
5120: 64         LD      H,H             
5121: C8         RET     Z               
5122: F4                              
5123: 3E 2A      LD      A,$2A           
5125: EA 11 C1   LD      ($C111),A       
5128: 3E 04      LD      A,$04           
512A: E0 F4      LDFF00  ($F4),A         
512C: 11 09 51   LD      DE,$5109        
512F: 06 A1      LD      B,$A1           
5131: CD 56 52   CALL    $5256           
5134: 21 10 C2   LD      HL,$C210        
5137: 09         ADD     HL,BC           
5138: 7E         LD      A,(HL)          
5139: D6 08      SUB     $08             
513B: 77         LD      (HL),A          
513C: 21 50 C2   LD      HL,$C250        
513F: 09         ADD     HL,BC           
5140: 36 FC      LD      (HL),$FC        
5142: 21 B0 C3   LD      HL,$C3B0        
5145: 09         ADD     HL,BC           
5146: 7E         LD      A,(HL)          
5147: E0 E8      LDFF00  ($E8),A         
5149: 50         LD      D,B             
514A: FE 11      CP      $11             
514C: 20 0C      JR      NZ,$515A        
514E: F5         PUSH    AF              
514F: FA 01 C5   LD      A,($C501)       
5152: 5F         LD      E,A             
5153: 21 F0 C2   LD      HL,$C2F0        
5156: 19         ADD     HL,DE           
5157: 36 38      LD      (HL),$38        
5159: F1         POP     AF              
515A: 5F         LD      E,A             
515B: FE 21      CP      $21             
515D: D2 D8 51   JP      NC,$51D8        
5160: FE 20      CP      $20             
5162: 20 03      JR      NZ,$5167        
5164: C3 92 63   JP      $6392           
5167: FE 1B      CP      $1B             
5169: 38 1B      JR      C,$5186         
516B: FE 20      CP      $20             
516D: 30 17      JR      NC,$5186        
516F: 21 03 51   LD      HL,$5103        
5172: 19         ADD     HL,DE           
5173: 7E         LD      A,(HL)          
5174: EA 90 DB   LD      ($DB90),A       
5177: 21 FE 50   LD      HL,$50FE        
517A: 19         ADD     HL,DE           
517B: 7E         LD      A,(HL)          
517C: EA 8F DB   LD      ($DB8F),A       
517F: 3E 18      LD      A,$18           
5181: EA CE C3   LD      ($C3CE),A       
5184: 18 52      JR      $51D8           
5186: FE 16      CP      $16             
5188: 38 13      JR      C,$519D         
518A: FE 1B      CP      $1B             
518C: 30 0F      JR      NC,$519D        
518E: D6 16      SUB     $16             
5190: 5F         LD      E,A             
5191: 16 00      LD      D,$00           
5193: 21 CC DB   LD      HL,$DBCC        
5196: 19         ADD     HL,DE           
5197: 34         INC     (HL)            
5198: CD E2 27   CALL    $27E2           
519B: 18 3B      JR      $51D8           
519D: FE 0C      CP      $0C             
519F: 30 32      JR      NC,$51D3        
51A1: F0 E8      LD      A,($E8)         
51A3: FE 01      CP      $01             
51A5: 20 04      JR      NZ,$51AB        
51A7: 21 44 DB   LD      HL,$DB44        
51AA: 34         INC     (HL)            
51AB: FE 00      CP      $00             
51AD: 20 0B      JR      NZ,$51BA        
51AF: FA 43 DB   LD      A,($DB43)       
51B2: FE 02      CP      $02             
51B4: 28 04      JR      Z,$51BA         
51B6: 21 43 DB   LD      HL,$DB43        
51B9: 34         INC     (HL)            
51BA: F0 E8      LD      A,($E8)         
51BC: FE 0A      CP      $0A             
51BE: 20 08      JR      NZ,$51C8        
51C0: 21 4D DB   LD      HL,$DB4D        
51C3: 7E         LD      A,(HL)          
51C4: C6 01      ADD     $01             
51C6: 27         DAA                     
51C7: 77         LD      (HL),A          
51C8: 50         LD      D,B             
51C9: 21 0D 51   LD      HL,$510D        
51CC: 19         ADD     HL,DE           
51CD: 56         LD      D,(HL)          
51CE: CD 97 64   CALL    $6497           
51D1: 18 05      JR      $51D8           
51D3: 21 00 DB   LD      HL,$DB00        
51D6: 19         ADD     HL,DE           
51D7: 34         INC     (HL)            
51D8: CD E2 51   CALL    $51E2           
51DB: 7E         LD      A,(HL)          
51DC: F6 10      OR      $10             
51DE: 77         LD      (HL),A          
51DF: E0 F8      LDFF00  ($F8),A         
51E1: C9         RET                     
51E2: FA A5 DB   LD      A,($DBA5)       
51E5: 57         LD      D,A             
51E6: 21 00 D8   LD      HL,$D800        
51E9: F0 F6      LD      A,($F6)         
51EB: 5F         LD      E,A             
51EC: F0 F7      LD      A,($F7)         
51EE: FE 1A      CP      $1A             
51F0: 30 05      JR      NC,$51F7        
51F2: FE 06      CP      $06             
51F4: 38 01      JR      C,$51F7         
51F6: 14         INC     D               
51F7: 19         ADD     HL,DE           
51F8: C9         RET                     
51F9: 6A         LD      L,D             
51FA: 7A         LD      A,D             
51FB: 6B         LD      L,E             
51FC: 7B         LD      A,E             
51FD: 10 12      STOP    $12             
51FF: 11 13 F8   LD      DE,$F813        
5202: F9         LD      SP,HL           
5203: FA FB 0E   LD      A,($0EFB)       
5206: 1E 0F      LD      E,$0F           
5208: 1F         RRA                     
5209: 68         LD      L,B             
520A: 77         LD      (HL),A          
520B: 69         LD      L,C             
520C: 4B         LD      C,E             
520D: CD D0 7E   CALL    $7ED0           
5210: 16 00      LD      D,$00           
5212: 21 B6 52   LD      HL,$52B6        
5215: 19         ADD     HL,DE           
5216: 7E         LD      A,(HL)          
5217: 21 40 C2   LD      HL,$C240        
521A: 09         ADD     HL,BC           
521B: 77         LD      (HL),A          
521C: 21 BA 52   LD      HL,$52BA        
521F: 19         ADD     HL,DE           
5220: 7E         LD      A,(HL)          
5221: 21 50 C2   LD      HL,$C250        
5224: 09         ADD     HL,BC           
5225: 77         LD      (HL),A          
5226: CD BE 52   CALL    $52BE           
5229: CD 92 78   CALL    $7892           
522C: 21 A0 C2   LD      HL,$C2A0        
522F: 09         ADD     HL,BC           
5230: 7E         LD      A,(HL)          
5231: A7         AND     A               
5232: 28 03      JR      Z,$5237         
5234: C3 B7 3F   JP      $3FB7           
5237: 3E 11      LD      A,$11           
5239: E0 F4      LDFF00  ($F4),A         
523B: 11 09 52   LD      DE,$5209        
523E: 06 C6      LD      B,$C6           
5240: FA A5 DB   LD      A,($DBA5)       
5243: A7         AND     A               
5244: 28 10      JR      Z,$5256         
5246: 11 FD 51   LD      DE,$51FD        
5249: 06 0D      LD      B,$0D           
524B: F0 F6      LD      A,($F6)         
524D: FE C7      CP      $C7             
524F: 20 05      JR      NZ,$5256        
5251: 11 F9 51   LD      DE,$51F9        
5254: 06 BE      LD      B,$BE           
5256: D5         PUSH    DE              
5257: 78         LD      A,B             
5258: F5         PUSH    AF              
5259: 06 00      LD      B,$00           
525B: F0 EF      LD      A,($EF)         
525D: D6 0F      SUB     $0F             
525F: E0 CD      LDFF00  ($CD),A         
5261: F0 EE      LD      A,($EE)         
5263: D6 07      SUB     $07             
5265: E0 CE      LDFF00  ($CE),A         
5267: CB 37      SET     1,E             
5269: E6 0F      AND     $0F             
526B: 5F         LD      E,A             
526C: F0 CD      LD      A,($CD)         
526E: E6 F0      AND     $F0             
5270: B3         OR      E               
5271: 5F         LD      E,A             
5272: 16 00      LD      D,$00           
5274: 21 11 D7   LD      HL,$D711        
5277: 19         ADD     HL,DE           
5278: F1         POP     AF              
5279: 77         LD      (HL),A          
527A: CD 39 28   CALL    $2839           
527D: FA 00 D6   LD      A,($D600)       
5280: 5F         LD      E,A             
5281: 16 00      LD      D,$00           
5283: 21 01 D6   LD      HL,$D601        
5286: 19         ADD     HL,DE           
5287: C6 0A      ADD     $0A             
5289: EA 00 D6   LD      ($D600),A       
528C: D1         POP     DE              
528D: F0 CF      LD      A,($CF)         
528F: 22         LD      (HLI),A         
5290: F0 D0      LD      A,($D0)         
5292: 22         LD      (HLI),A         
5293: 3E 81      LD      A,$81           
5295: 22         LD      (HLI),A         
5296: 1A         LD      A,(DE)          
5297: 13         INC     DE              
5298: 22         LD      (HLI),A         
5299: 1A         LD      A,(DE)          
529A: 13         INC     DE              
529B: 22         LD      (HLI),A         
529C: F0 CF      LD      A,($CF)         
529E: 22         LD      (HLI),A         
529F: F0 D0      LD      A,($D0)         
52A1: 3C         INC     A               
52A2: 22         LD      (HLI),A         
52A3: 3E 81      LD      A,$81           
52A5: 22         LD      (HLI),A         
52A6: 1A         LD      A,(DE)          
52A7: 13         INC     DE              
52A8: 22         LD      (HLI),A         
52A9: 1A         LD      A,(DE)          
52AA: 22         LD      (HLI),A         
52AB: AF         XOR     A               
52AC: 77         LD      (HL),A          
52AD: C9         RET                     
52AE: 6E         LD      L,(HL)          
52AF: 00         NOP                     
52B0: 6E         LD      L,(HL)          
52B1: 20 F8      JR      NZ,$52AB        
52B3: 10 FA      STOP    $FA             
52B5: 10 F8      STOP    $F8             
52B7: 08 00 00   LD      ($0000),SP      
52BA: 00         NOP                     
52BB: 00         NOP                     
52BC: 08 F8 FA   LD      ($FAF8),SP      
52BF: A5         AND     L               
52C0: DB                              
52C1: E0 F1      LDFF00  ($F1),A         
52C3: 11 AE 52   LD      DE,$52AE        
52C6: CD 3B 3C   CALL    $3C3B           
52C9: CD 4A 7F   CALL    $7F4A           
52CC: CD F7 7E   CALL    $7EF7           
52CF: CD 43 53   CALL    $5343           
52D2: CD 93 6C   CALL    $6C93           
52D5: 30 08      JR      NC,$52DF        
52D7: CD 4A 09   CALL    $094A           
52DA: 3E 03      LD      A,$03           
52DC: EA 44 C1   LD      ($C144),A       
52DF: F0 F6      LD      A,($F6)         
52E1: FE C7      CP      $C7             
52E3: 28 06      JR      Z,$52EB         
52E5: FA A5 DB   LD      A,($DBA5)       
52E8: A7         AND     A               
52E9: 20 04      JR      NZ,$52EF        
52EB: 3E 02      LD      A,$02           
52ED: E0 A1      LDFF00  ($A1),A         
52EF: 21 D0 C3   LD      HL,$C3D0        
52F2: 09         ADD     HL,BC           
52F3: 7E         LD      A,(HL)          
52F4: 3C         INC     A               
52F5: 77         LD      (HL),A          
52F6: FE 21      CP      $21             
52F8: 20 48      JR      NZ,$5342        
52FA: 21 10 C4   LD      HL,$C410        
52FD: 09         ADD     HL,BC           
52FE: 77         LD      (HL),A          
52FF: CD 92 78   CALL    $7892           
5302: 21 80 C2   LD      HL,$C280        
5305: 09         ADD     HL,BC           
5306: 7E         LD      A,(HL)          
5307: A7         AND     A               
5308: 28 38      JR      Z,$5342         
530A: FE 02      CP      $02             
530C: 28 34      JR      Z,$5342         
530E: CD B7 3F   CALL    $3FB7           
5311: 11 05 52   LD      DE,$5205        
5314: 06 C4      LD      B,$C4           
5316: FA A5 DB   LD      A,($DBA5)       
5319: A7         AND     A               
531A: 28 05      JR      Z,$5321         
531C: 11 01 52   LD      DE,$5201        
531F: 06 A6      LD      B,$A6           
5321: CD 56 52   CALL    $5256           
5324: FA 8E C1   LD      A,($C18E)       
5327: E6 1F      AND     $1F             
5329: FE 02      CP      $02             
532B: 28 12      JR      Z,$533F         
532D: FE 07      CP      $07             
532F: 20 11      JR      NZ,$5342        
5331: CD 92 78   CALL    $7892           
5334: FA 03 C5   LD      A,($C503)       
5337: FE A7      CP      $A7             
5339: 28 04      JR      Z,$533F         
533B: FE A6      CP      $A6             
533D: 20 03      JR      NZ,$5342        
533F: CD EC 08   CALL    $08EC           
5342: C9         RET                     
5343: 1E 0F      LD      E,$0F           
5345: 50         LD      D,B             
5346: 21 80 C2   LD      HL,$C280        
5349: 19         ADD     HL,DE           
534A: 7E         LD      A,(HL)          
534B: FE 05      CP      $05             
534D: 38 3E      JR      C,$538D         
534F: 21 40 C3   LD      HL,$C340        
5352: 19         ADD     HL,DE           
5353: 7E         LD      A,(HL)          
5354: E6 40      AND     $40             
5356: 20 35      JR      NZ,$538D        
5358: 21 00 C2   LD      HL,$C200        
535B: 19         ADD     HL,DE           
535C: F0 EE      LD      A,($EE)         
535E: 96         SUB     (HL)            
535F: C6 0C      ADD     $0C             
5361: FE 18      CP      $18             
5363: 30 28      JR      NC,$538D        
5365: 21 10 C2   LD      HL,$C210        
5368: 19         ADD     HL,DE           
5369: 7E         LD      A,(HL)          
536A: 21 10 C3   LD      HL,$C310        
536D: 19         ADD     HL,DE           
536E: 96         SUB     (HL)            
536F: 21 EC FF   LD      HL,$FFEC        
5372: 96         SUB     (HL)            
5373: C6 0C      ADD     $0C             
5375: FE 18      CP      $18             
5377: 30 14      JR      NC,$538D        
5379: 21 40 C3   LD      HL,$C340        
537C: 19         ADD     HL,DE           
537D: 7E         LD      A,(HL)          
537E: E6 20      AND     $20             
5380: 20 0B      JR      NZ,$538D        
5382: C5         PUSH    BC              
5383: D5         PUSH    DE              
5384: C1         POP     BC              
5385: D5         PUSH    DE              
5386: 3E 08      LD      A,$08           
5388: CD E1 6F   CALL    $6FE1           
538B: D1         POP     DE              
538C: C1         POP     BC              
538D: 1D         DEC     E               
538E: 7B         LD      A,E             
538F: FE FF      CP      $FF             
5391: C2 46 53   JP      NZ,$5346        
5394: C9         RET                     
5395: 16 00      LD      D,$00           
5397: 79         LD      A,C             
5398: EA 0C C5   LD      ($C50C),A       
539B: CD 8C 08   CALL    $088C           
539E: E0 D7      LDFF00  ($D7),A         
53A0: CA 10 54   JP      Z,$5410         
53A3: FE 01      CP      $01             
53A5: 20 5D      JR      NZ,$5404        
53A7: 21 90 C3   LD      HL,$C390        
53AA: 09         ADD     HL,BC           
53AB: 7E         LD      A,(HL)          
53AC: A7         AND     A               
53AD: 28 29      JR      Z,$53D8         
53AF: CD ED 27   CALL    $27ED           
53B2: E6 03      AND     $03             
53B4: 20 22      JR      NZ,$53D8        
53B6: 3E 2F      LD      A,$2F           
53B8: CD F8 64   CALL    $64F8           
53BB: 38 1B      JR      C,$53D8         
53BD: F0 D7      LD      A,($D7)         
53BF: 21 00 C2   LD      HL,$C200        
53C2: 19         ADD     HL,DE           
53C3: 77         LD      (HL),A          
53C4: F0 D8      LD      A,($D8)         
53C6: 21 10 C2   LD      HL,$C210        
53C9: 19         ADD     HL,DE           
53CA: 77         LD      (HL),A          
53CB: F0 DA      LD      A,($DA)         
53CD: 21 10 C3   LD      HL,$C310        
53D0: 19         ADD     HL,DE           
53D1: 77         LD      (HL),A          
53D2: 21 50 C4   LD      HL,$C450        
53D5: 19         ADD     HL,DE           
53D6: 36 80      LD      (HL),$80        
53D8: F0 F1      LD      A,($F1)         
53DA: A7         AND     A               
53DB: 20 24      JR      NZ,$5401        
53DD: F0 F7      LD      A,($F7)         
53DF: FE 1E      CP      $1E             
53E1: 28 04      JR      Z,$53E7         
53E3: FE 10      CP      $10             
53E5: 20 1A      JR      NZ,$5401        
53E7: FA 73 DB   LD      A,($DB73)       
53EA: A7         AND     A               
53EB: 28 14      JR      Z,$5401         
53ED: CD ED 27   CALL    $27ED           
53F0: E6 3F      AND     $3F             
53F2: 20 08      JR      NZ,$53FC        
53F4: 3E 28      LD      A,$28           
53F6: CD 97 21   CALL    $2197           
53F9: C3 B7 3F   JP      $3FB7           
53FC: 3E 99      LD      A,$99           
53FE: CD 85 21   CALL    $2185           
5401: C3 B7 3F   JP      $3FB7           
5404: CD F6 37   CALL    $37F6           
5407: C9         RET                     
5408: F0 10      LD      A,($10)         
540A: F2                              
540B: 10 F4      STOP    $F4             
540D: 10 F6      STOP    $F6             
540F: 10 11      STOP    $11             
5411: 08 54 CD   LD      ($CD54),SP      
5414: 3B         DEC     SP              
5415: 3C         INC     A               
5416: CD 4A 7F   CALL    $7F4A           
5419: 3E 0B      LD      A,$0B           
541B: EA 9E C1   LD      ($C19E),A       
541E: CD A6 75   CALL    $75A6           
5421: CD D5 60   CALL    $60D5           
5424: 21 80 C2   LD      HL,$C280        
5427: 09         ADD     HL,BC           
5428: 7E         LD      A,(HL)          
5429: FE 02      CP      $02             
542B: CA 63 54   JP      Z,$5463         
542E: 21 10 C3   LD      HL,$C310        
5431: 09         ADD     HL,BC           
5432: 7E         LD      A,(HL)          
5433: A7         AND     A               
5434: 28 0B      JR      Z,$5441         
5436: 21 A0 C2   LD      HL,$C2A0        
5439: 09         ADD     HL,BC           
543A: 7E         LD      A,(HL)          
543B: A7         AND     A               
543C: 28 25      JR      Z,$5463         
543E: CD 97 54   CALL    $5497           
5441: 21 F4 FF   LD      HL,$FFF4        
5444: 36 05      LD      (HL),$05        
5446: 1E 1F      LD      E,$1F           
5448: F0 F1      LD      A,($F1)         
544A: FE FF      CP      $FF             
544C: 28 08      JR      Z,$5456         
544E: FE 01      CP      $01             
5450: 28 04      JR      Z,$5456         
5452: 36 09      LD      (HL),$09        
5454: 1E 0F      LD      E,$0F           
5456: 21 F0 C2   LD      HL,$C2F0        
5459: 09         ADD     HL,BC           
545A: 73         LD      (HL),E          
545B: 21 40 C3   LD      HL,$C340        
545E: 09         ADD     HL,BC           
545F: 7E         LD      A,(HL)          
5460: C6 02      ADD     $02             
5462: 77         LD      (HL),A          
5463: C9         RET                     
5464: 3E 05      LD      A,$05           
5466: CD F8 64   CALL    $64F8           
5469: 38 2B      JR      C,$5496         
546B: F0 D7      LD      A,($D7)         
546D: 21 00 C2   LD      HL,$C200        
5470: 19         ADD     HL,DE           
5471: 77         LD      (HL),A          
5472: F0 D8      LD      A,($D8)         
5474: 21 DA FF   LD      HL,$FFDA        
5477: 96         SUB     (HL)            
5478: 21 10 C2   LD      HL,$C210        
547B: 19         ADD     HL,DE           
547C: 77         LD      (HL),A          
547D: 21 B0 C3   LD      HL,$C3B0        
5480: 19         ADD     HL,DE           
5481: 36 00      LD      (HL),$00        
5483: 21 F0 C2   LD      HL,$C2F0        
5486: 19         ADD     HL,DE           
5487: 36 0F      LD      (HL),$0F        
5489: 21 40 C3   LD      HL,$C340        
548C: 19         ADD     HL,DE           
548D: 36 C4      LD      (HL),$C4        
548F: 3E 09      LD      A,$09           
5491: E0 F4      LDFF00  ($F4),A         
5493: CD B7 3F   CALL    $3FB7           
5496: C9         RET                     
5497: 21 A0 C2   LD      HL,$C2A0        
549A: 09         ADD     HL,BC           
549B: 7E         LD      A,(HL)          
549C: A7         AND     A               
549D: 28 46      JR      Z,$54E5         
549F: FA 8E C1   LD      A,($C18E)       
54A2: E6 1F      AND     $1F             
54A4: FE 0D      CP      $0D             
54A6: 20 20      JR      NZ,$54C8        
54A8: FA 03 C5   LD      A,($C503)       
54AB: FE A0      CP      $A0             
54AD: 28 07      JR      Z,$54B6         
54AF: FA 0D C5   LD      A,($C50D)       
54B2: FE A0      CP      $A0             
54B4: 20 2F      JR      NZ,$54E5        
54B6: 3E 30      LD      A,$30           
54B8: E0 CE      LDFF00  ($CE),A         
54BA: 3E 20      LD      A,$20           
54BC: E0 CD      LDFF00  ($CD),A         
54BE: 3E 19      LD      A,$19           
54C0: E0 DF      LDFF00  ($DF),A         
54C2: CD 7D 3E   CALL    $3E7D           
54C5: C3 EC 08   JP      $08EC           
54C8: FE 0B      CP      $0B             
54CA: 20 19      JR      NZ,$54E5        
54CC: FA 0D C5   LD      A,($C50D)       
54CF: FE 35      CP      $35             
54D1: 38 12      JR      C,$54E5         
54D3: FE 3D      CP      $3D             
54D5: 38 0B      JR      C,$54E2         
54D7: FA 03 C5   LD      A,($C503)       
54DA: FE 35      CP      $35             
54DC: 38 07      JR      C,$54E5         
54DE: FE 3D      CP      $3D             
54E0: 30 03      JR      NC,$54E5        
54E2: CD EC 08   CALL    $08EC           
54E5: C9         RET                     
54E6: 32         LD      (HLD),A         
54E7: 00         NOP                     
54E8: 32         LD      (HLD),A         
54E9: 60         LD      H,B             
54EA: 30 00      JR      NC,$54EC        
54EC: 30 60      JR      NC,$554E        
54EE: 00         NOP                     
54EF: 00         NOP                     
54F0: 3C         INC     A               
54F1: 00         NOP                     
54F2: 00         NOP                     
54F3: 08 3C 20   LD      ($203C),SP      
54F6: FF         RST     0X38            
54F7: FF         RST     0X38            
54F8: FF         RST     0X38            
54F9: FF         RST     0X38            
54FA: FF         RST     0X38            
54FB: FF         RST     0X38            
54FC: FF         RST     0X38            
54FD: FF         RST     0X38            
54FE: 00         NOP                     
54FF: 00         NOP                     
5500: 3A         LD      A,(HLD)         
5501: 00         NOP                     
5502: 00         NOP                     
5503: 08 3A 20   LD      ($203A),SP      
5506: FF         RST     0X38            
5507: FF         RST     0X38            
5508: FF         RST     0X38            
5509: FF         RST     0X38            
550A: FF         RST     0X38            
550B: FF         RST     0X38            
550C: FF         RST     0X38            
550D: FF         RST     0X38            
550E: FA FA 3A   LD      A,($3AFA)       
5511: 00         NOP                     
5512: FA 02 3A   LD      A,($3A02)       
5515: 20 06      JR      NZ,$551D        
5517: 06 3A      LD      B,$3A           
5519: 00         NOP                     
551A: 06 0E      LD      B,$0E           
551C: 3A         LD      A,(HLD)         
551D: 20 04      JR      NZ,$5523        
551F: FC                              
5520: 30 00      JR      NC,$5522        
5522: 04         INC     B               
5523: 04         INC     B               
5524: 30 20      JR      NC,$5546        
5526: FC                              
5527: 04         INC     B               
5528: 30 00      JR      NC,$552A        
552A: FC                              
552B: 0C         INC     C               
552C: 30 20      JR      NC,$554E        
552E: 00         NOP                     
552F: 00         NOP                     
5530: 3A         LD      A,(HLD)         
5531: 00         NOP                     
5532: 00         NOP                     
5533: 08 3A 20   LD      ($203A),SP      
5536: FF         RST     0X38            
5537: FF         RST     0X38            
5538: FF         RST     0X38            
5539: FF         RST     0X38            
553A: FF         RST     0X38            
553B: FF         RST     0X38            
553C: FF         RST     0X38            
553D: FF         RST     0X38            
553E: F8 F8      LDHL    SP,$F8          
5540: 3A         LD      A,(HLD)         
5541: 00         NOP                     
5542: F8 00      LDHL    SP,$00          
5544: 3A         LD      A,(HLD)         
5545: 20 08      JR      NZ,$554F        
5547: 08 3A 00   LD      ($003A),SP      
554A: 08 10 3A   LD      ($3A10),SP      
554D: 20 08      JR      NZ,$5557        
554F: F8 3A      LDHL    SP,$3A          
5551: 00         NOP                     
5552: 08 00 3A   LD      ($3A00),SP      
5555: 20 F8      JR      NZ,$554F        
5557: 08 3A 00   LD      ($003A),SP      
555A: F8 10      LDHL    SP,$10          
555C: 3A         LD      A,(HLD)         
555D: 20 F8      JR      NZ,$5557        
555F: F8 10      LDHL    SP,$10          
5561: 00         NOP                     
5562: F8 00      LDHL    SP,$00          
5564: 12         LD      (DE),A          
5565: 00         NOP                     
5566: F8 08      LDHL    SP,$08          
5568: 12         LD      (DE),A          
5569: 20 F8      JR      NZ,$5563        
556B: 10 10      STOP    $10             
556D: 20 08      JR      NZ,$5577        
556F: F8 10      LDHL    SP,$10          
5571: 40         LD      B,B             
5572: 08 00 12   LD      ($1200),SP      
5575: 40         LD      B,B             
5576: 08 08 12   LD      ($1208),SP      
5579: 60         LD      H,B             
557A: 08 10 10   LD      ($1010),SP      
557D: 60         LD      H,B             
557E: 21 30 C4   LD      HL,$C430        
5581: 09         ADD     HL,BC           
5582: 7E         LD      A,(HL)          
5583: E6 80      AND     $80             
5585: 28 03      JR      Z,$558A         
5587: C3 45 39   JP      $3945           
558A: 21 80 C4   LD      HL,$C480        
558D: 09         ADD     HL,BC           
558E: 7E         LD      A,(HL)          
558F: A7         AND     A               
5590: CA 7A 3F   JP      Z,$3F7A         
5593: F5         PUSH    AF              
5594: 21 A0 C4   LD      HL,$C4A0        
5597: 09         ADD     HL,BC           
5598: 7E         LD      A,(HL)          
5599: 21 EE 54   LD      HL,$54EE        
559C: A7         AND     A               
559D: 28 03      JR      Z,$55A2         
559F: 21 2E 55   LD      HL,$552E        
55A2: F1         POP     AF              
55A3: FE 20      CP      $20             
55A5: 30 2E      JR      NC,$55D5        
55A7: 17         RLA                     
55A8: E6 30      AND     $30             
55AA: 5F         LD      E,A             
55AB: 50         LD      D,B             
55AC: 19         ADD     HL,DE           
55AD: FE 30      CP      $30             
55AF: 20 0A      JR      NZ,$55BB        
55B1: E5         PUSH    HL              
55B2: 21 A0 C4   LD      HL,$C4A0        
55B5: 09         ADD     HL,BC           
55B6: 7E         LD      A,(HL)          
55B7: E1         POP     HL              
55B8: A7         AND     A               
55B9: 20 07      JR      NZ,$55C2        
55BB: 0E 04      LD      C,$04           
55BD: CD 26 3D   CALL    $3D26           
55C0: 18 0C      JR      $55CE           
55C2: 0E 08      LD      C,$08           
55C4: CD 26 3D   CALL    $3D26           
55C7: 3E 04      LD      A,$04           
55C9: CD D0 3D   CALL    $3DD0           
55CC: 18 00      JR      $55CE           
55CE: CD 4A 7F   CALL    $7F4A           
55D1: CD 6C 7F   CALL    $7F6C           
55D4: C9         RET                     
55D5: CD 3D 39   CALL    $393D           
55D8: CD 50 7F   CALL    $7F50           
55DB: 21 10 C4   LD      HL,$C410        
55DE: 09         ADD     HL,BC           
55DF: 7E         LD      A,(HL)          
55E0: A7         AND     A               
55E1: 20 16      JR      NZ,$55F9        
55E3: 21 80 C4   LD      HL,$C480        
55E6: 09         ADD     HL,BC           
55E7: 36 1F      LD      (HL),$1F        
55E9: FA 7C D4   LD      A,($D47C)       
55EC: FE 01      CP      $01             
55EE: 20 04      JR      NZ,$55F4        
55F0: 3E 12      LD      A,$12           
55F2: E0 F3      LDFF00  ($F3),A         
55F4: 21 F4 FF   LD      HL,$FFF4        
55F7: 36 13      LD      (HL),$13        
55F9: CD 6C 7F   CALL    $7F6C           
55FC: C9         RET                     
55FD: 2E 2E      LD      L,$2E           
55FF: 2D         DEC     L               
5600: 2D         DEC     L               
5601: 37         SCF                     
5602: 2D         DEC     L               
5603: FF         RST     0X38            
5604: FF         RST     0X38            
5605: 2F         CPL                     
5606: 37         SCF                     
5607: 38 2E      JR      C,$5637         
5609: 2F         CPL                     
560A: 2F         CPL                     
560B: 03         INC     BC              
560C: 01 01 00   LD      BC,$0001        
560F: 03         INC     BC              
5610: 03         INC     BC              
5611: 03         INC     BC              
5612: 03         INC     BC              
5613: 01 00 00   LD      BC,$0000        
5616: 00         NOP                     
5617: 03         INC     BC              
5618: 00         NOP                     
5619: 01 01 01   LD      BC,$0101        
561C: 00         NOP                     
561D: 01 01 01   LD      BC,$0101        
5620: 01 01 00   LD      BC,$0001        
5623: 00         NOP                     
5624: 00         NOP                     
5625: 01 00 2E   LD      BC,$2E00        
5628: 2D         DEC     L               
5629: 38 2F      JR      C,$565A         
562B: 2E 2D      LD      L,$2D           
562D: 38 37      JR      C,$5666         
562F: F0 EB      LD      A,($EB)         
5631: FE 23      CP      $23             
5633: 20 0D      JR      NZ,$5642        
5635: 21 B0 C2   LD      HL,$C2B0        
5638: 09         ADD     HL,BC           
5639: 7E         LD      A,(HL)          
563A: A7         AND     A               
563B: 28 05      JR      Z,$5642         
563D: 3E 31      LD      A,$31           
563F: C3 D0 56   JP      $56D0           
5642: 21 E0 C4   LD      HL,$C4E0        
5645: 09         ADD     HL,BC           
5646: 7E         LD      A,(HL)          
5647: FE FF      CP      $FF             
5649: C8         RET     Z               
564A: A7         AND     A               
564B: C2 D0 56   JP      NZ,$56D0        
564E: FA 71 D4   LD      A,($D471)       
5651: 3C         INC     A               
5652: EA 71 D4   LD      ($D471),A       
5655: FE 0C      CP      $0C             
5657: 38 16      JR      C,$566F         
5659: AF         XOR     A               
565A: EA 71 D4   LD      ($D471),A       
565D: FA BE C1   LD      A,($C1BE)       
5660: 21 7C D4   LD      HL,$D47C        
5663: B6         OR      (HL)            
5664: 21 F9 FF   LD      HL,$FFF9        
5667: B6         OR      (HL)            
5668: 20 05      JR      NZ,$566F        
566A: 3E 34      LD      A,$34           
566C: C3 D0 56   JP      $56D0           
566F: 21 D0 C4   LD      HL,$C4D0        
5672: 09         ADD     HL,BC           
5673: 50         LD      D,B             
5674: 5E         LD      E,(HL)          
5675: 21 7F 48   LD      HL,$487F        
5678: 19         ADD     HL,DE           
5679: 7E         LD      A,(HL)          
567A: A7         AND     A               
567B: C8         RET     Z               
567C: 5F         LD      E,A             
567D: 16 1E      LD      D,$1E           
567F: FA 5B DB   LD      A,($DB5B)       
5682: FE 07      CP      $07             
5684: 38 08      JR      C,$568E         
5686: 16 23      LD      D,$23           
5688: FE 0B      CP      $0B             
568A: 38 02      JR      C,$568E         
568C: 16 28      LD      D,$28           
568E: 21 15 D4   LD      HL,$D415        
5691: 34         INC     (HL)            
5692: 7E         LD      A,(HL)          
5693: BA         CP      D               
5694: 38 12      JR      C,$56A8         
5696: 70         LD      (HL),B          
5697: FA BE C1   LD      A,($C1BE)       
569A: 21 F9 FF   LD      HL,$FFF9        
569D: B6         OR      (HL)            
569E: 21 7C D4   LD      HL,$D47C        
56A1: B6         OR      (HL)            
56A2: 20 04      JR      NZ,$56A8        
56A4: 3E 33      LD      A,$33           
56A6: 18 28      JR      $56D0           
56A8: 50         LD      D,B             
56A9: 21 0A 56   LD      HL,$560A        
56AC: FA 63 C1   LD      A,($C163)       
56AF: A7         AND     A               
56B0: 28 03      JR      Z,$56B5         
56B2: 21 18 56   LD      HL,$5618        
56B5: 19         ADD     HL,DE           
56B6: CD ED 27   CALL    $27ED           
56B9: A6         AND     (HL)            
56BA: C0         RET     NZ              
56BB: 21 FC 55   LD      HL,$55FC        
56BE: 19         ADD     HL,DE           
56BF: 7E         LD      A,(HL)          
56C0: FE FF      CP      $FF             
56C2: 20 0C      JR      NZ,$56D0        
56C4: CD ED 27   CALL    $27ED           
56C7: E6 07      AND     $07             
56C9: 5F         LD      E,A             
56CA: 50         LD      D,B             
56CB: 21 27 56   LD      HL,$5627        
56CE: 19         ADD     HL,DE           
56CF: 7E         LD      A,(HL)          
56D0: CD F8 64   CALL    $64F8           
56D3: D8         RET     C               
56D4: 21 B0 C2   LD      HL,$C2B0        
56D7: 09         ADD     HL,BC           
56D8: 7E         LD      A,(HL)          
56D9: 21 B0 C2   LD      HL,$C2B0        
56DC: 19         ADD     HL,DE           
56DD: 77         LD      (HL),A          
56DE: F0 D7      LD      A,($D7)         
56E0: 21 00 C2   LD      HL,$C200        
56E3: 19         ADD     HL,DE           
56E4: 77         LD      (HL),A          
56E5: F0 D8      LD      A,($D8)         
56E7: 21 10 C2   LD      HL,$C210        
56EA: 19         ADD     HL,DE           
56EB: 77         LD      (HL),A          
56EC: 21 50 C4   LD      HL,$C450        
56EF: 19         ADD     HL,DE           
56F0: 36 80      LD      (HL),$80        
56F2: 21 F0 C2   LD      HL,$C2F0        
56F5: 19         ADD     HL,DE           
56F6: 36 18      LD      (HL),$18        
56F8: 21 80 C4   LD      HL,$C480        
56FB: 19         ADD     HL,DE           
56FC: 36 03      LD      (HL),$03        
56FE: F0 F9      LD      A,($F9)         
5700: A7         AND     A               
5701: 20 36      JR      NZ,$5739        
5703: 21 A0 C3   LD      HL,$C3A0        
5706: 19         ADD     HL,DE           
5707: 7E         LD      A,(HL)          
5708: FE 30      CP      $30             
570A: 20 0C      JR      NZ,$5718        
570C: F0 EB      LD      A,($EB)         
570E: FE 88      CP      $88             
5710: 20 06      JR      NZ,$5718        
5712: 21 B0 C3   LD      HL,$C3B0        
5715: 19         ADD     HL,DE           
5716: 36 03      LD      (HL),$03        
5718: FE 3C      CP      $3C             
571A: 20 15      JR      NZ,$5731        
571C: F0 F6      LD      A,($F6)         
571E: FE 58      CP      $58             
5720: 28 04      JR      Z,$5726         
5722: FE 5A      CP      $5A             
5724: 20 0B      JR      NZ,$5731        
5726: C5         PUSH    BC              
5727: D5         PUSH    DE              
5728: D5         PUSH    DE              
5729: C1         POP     BC              
572A: 3E 10      LD      A,$10           
572C: CD 99 7E   CALL    $7E99           
572F: D1         POP     DE              
5730: C1         POP     BC              
5731: 21 20 C3   LD      HL,$C320        
5734: 19         ADD     HL,DE           
5735: 36 18      LD      (HL),$18        
5737: 18 06      JR      $573F           
5739: 21 50 C2   LD      HL,$C250        
573C: 19         ADD     HL,DE           
573D: 36 EC      LD      (HL),$EC        
573F: 21 10 C3   LD      HL,$C310        
5742: 09         ADD     HL,BC           
5743: 7E         LD      A,(HL)          
5744: 21 10 C3   LD      HL,$C310        
5747: 19         ADD     HL,DE           
5748: 77         LD      (HL),A          
5749: C9         RET                     
574A: 01 08 08   LD      BC,$0808        
574D: 10 01      STOP    $01             
574F: 04         INC     B               
5750: 04         INC     B               
5751: 0A         LD      A,(BC)          
5752: 37         SCF                     
5753: 37         SCF                     
5754: 37         SCF                     
5755: 01 39 39   LD      BC,$3939        
5758: 39         ADD     HL,SP           
5759: 01 3B 3B   LD      BC,$3B3B        
575C: 3B         DEC     SP              
575D: 01 3D 3D   LD      BC,$3D3D        
5760: 3D         DEC     A               
5761: 01 10 10   LD      BC,$1010        
5764: 08 00 F0   LD      ($F000),SP      
5767: F0 F8      LD      A,($F8)         
5769: 00         NOP                     
576A: 00         NOP                     
576B: 00         NOP                     
576C: 00         NOP                     
576D: 00         NOP                     
576E: FF         RST     0X38            
576F: FF         RST     0X38            
5770: FF         RST     0X38            
5771: FF         RST     0X38            
5772: 00         NOP                     
5773: 00         NOP                     
5774: 00         NOP                     
5775: 00         NOP                     
5776: 00         NOP                     
5777: 00         NOP                     
5778: 00         NOP                     
5779: 00         NOP                     
577A: 00         NOP                     
577B: 00         NOP                     
577C: 00         NOP                     
577D: 00         NOP                     
577E: 00         NOP                     
577F: 00         NOP                     
5780: 08 00 00   LD      ($0000),SP      
5783: 00         NOP                     
5784: 08 0E 00   LD      ($000E),SP      
5787: 00         NOP                     
5788: 08 0E 00   LD      ($000E),SP      
578B: 00         NOP                     
578C: 08 0E 00   LD      ($000E),SP      
578F: 00         NOP                     
5790: 00         NOP                     
5791: 0E F0      LD      C,$F0           
5793: EB                              
5794: EA A8 C5   LD      ($C5A8),A       
5797: FE 02      CP      $02             
5799: 20 0A      JR      NZ,$57A5        
579B: 21 20 C4   LD      HL,$C420        
579E: 09         ADD     HL,BC           
579F: 70         LD      (HL),B          
57A0: CD 3D 67   CALL    $673D           
57A3: 18 03      JR      $57A8           
57A5: CD 3D 39   CALL    $393D           
57A8: 21 90 C4   LD      HL,$C490        
57AB: 09         ADD     HL,BC           
57AC: 7E         LD      A,(HL)          
57AD: 5F         LD      E,A             
57AE: 50         LD      D,B             
57AF: FE 04      CP      $04             
57B1: 28 2F      JR      Z,$57E2         
57B3: FA 5D C1   LD      A,($C15D)       
57B6: E0 9E      LDFF00  ($9E),A         
57B8: E5         PUSH    HL              
57B9: CD 91 08   CALL    $0891           
57BC: E1         POP     HL              
57BD: A7         AND     A               
57BE: 20 22      JR      NZ,$57E2        
57C0: 34         INC     (HL)            
57C1: 21 4A 57   LD      HL,$574A        
57C4: F0 EB      LD      A,($EB)         
57C6: FE 02      CP      $02             
57C8: 28 0E      JR      Z,$57D8         
57CA: FA 43 DB   LD      A,($DB43)       
57CD: FE 02      CP      $02             
57CF: 30 07      JR      NC,$57D8        
57D1: FA 7C D4   LD      A,($D47C)       
57D4: FE 01      CP      $01             
57D6: 20 03      JR      NZ,$57DB        
57D8: 21 4E 57   LD      HL,$574E        
57DB: 19         ADD     HL,DE           
57DC: 7E         LD      A,(HL)          
57DD: 21 E0 C2   LD      HL,$C2E0        
57E0: 09         ADD     HL,BC           
57E1: 77         LD      (HL),A          
57E2: 7B         LD      A,E             
57E3: FE 00      CP      $00             
57E5: 20 01      JR      NZ,$57E8        
57E7: 1C         INC     E               
57E8: CD EF 57   CALL    $57EF           
57EB: CD 40 58   CALL    $5840           
57EE: C9         RET                     
57EF: F0 9E      LD      A,($9E)         
57F1: CB 27      SET     1,E             
57F3: CB 27      SET     1,E             
57F5: 83         ADD     A,E             
57F6: 5F         LD      E,A             
57F7: 16 00      LD      D,$00           
57F9: 21 51 57   LD      HL,$5751        
57FC: 19         ADD     HL,DE           
57FD: 7E         LD      A,(HL)          
57FE: EA 5C C1   LD      ($C15C),A       
5801: 21 61 57   LD      HL,$5761        
5804: 19         ADD     HL,DE           
5805: 7E         LD      A,(HL)          
5806: 21 98 FF   LD      HL,$FF98        
5809: 86         ADD     A,(HL)          
580A: 21 00 C2   LD      HL,$C200        
580D: 09         ADD     HL,BC           
580E: 77         LD      (HL),A          
580F: 21 71 57   LD      HL,$5771        
5812: 19         ADD     HL,DE           
5813: 7E         LD      A,(HL)          
5814: 21 99 FF   LD      HL,$FF99        
5817: 86         ADD     A,(HL)          
5818: 21 3B C1   LD      HL,$C13B        
581B: 86         ADD     A,(HL)          
581C: 21 10 C2   LD      HL,$C210        
581F: 09         ADD     HL,BC           
5820: 77         LD      (HL),A          
5821: F0 F9      LD      A,($F9)         
5823: A7         AND     A               
5824: 28 0B      JR      Z,$5831         
5826: E5         PUSH    HL              
5827: 21 81 57   LD      HL,$5781        
582A: 19         ADD     HL,DE           
582B: 5E         LD      E,(HL)          
582C: E1         POP     HL              
582D: 7E         LD      A,(HL)          
582E: 93         SUB     E               
582F: 77         LD      (HL),A          
5830: C9         RET                     
5831: 21 81 57   LD      HL,$5781        
5834: 19         ADD     HL,DE           
5835: 7E         LD      A,(HL)          
5836: 21 A2 FF   LD      HL,$FFA2        
5839: 86         ADD     A,(HL)          
583A: 21 10 C3   LD      HL,$C310        
583D: 09         ADD     HL,BC           
583E: 77         LD      (HL),A          
583F: C9         RET                     
5840: CD 31 38   CALL    $3831           
5843: C9         RET                     
5844: 11 56 58   LD      DE,$5856        
5847: FA 95 DB   LD      A,($DB95)       
584A: FE 01      CP      $01             
584C: 28 04      JR      Z,$5852         
584E: 3E 30      LD      A,$30           
5850: E0 F5      LDFF00  ($F5),A         
5852: CD 97 58   CALL    $5897           
5855: C9         RET                     
5856: 30 00      JR      NC,$5858        
5858: 30 20      JR      NC,$587A        
585A: 32         LD      (HLD),A         
585B: 00         NOP                     
585C: 32         LD      (HLD),A         
585D: 20 30      JR      NZ,$588F        
585F: 40         LD      B,B             
5860: 30 60      JR      NC,$58C2        
5862: 32         LD      (HLD),A         
5863: 40         LD      B,B             
5864: 32         LD      (HLD),A         
5865: 60         LD      H,B             
5866: 34         INC     (HL)            
5867: 00         NOP                     
5868: 36 00      LD      (HL),$00        
586A: 38 00      JR      C,$586C         
586C: 3A         LD      A,(HLD)         
586D: 00         NOP                     
586E: 36 20      LD      (HL),$20        
5870: 34         INC     (HL)            
5871: 20 3A      JR      NZ,$58AD        
5873: 20 38      JR      NZ,$58AD        
5875: 20 08      JR      NZ,$587F        
5877: F8 00      LDHL    SP,$00          
5879: 00         NOP                     
587A: 00         NOP                     
587B: 00         NOP                     
587C: F8 08      LDHL    SP,$08          
587E: 06 04      LD      B,$04           
5880: 02         LD      (BC),A          
5881: 00         NOP                     
5882: F0 F7      LD      A,($F7)         
5884: FE 15      CP      $15             
5886: 20 08      JR      NZ,$5890        
5888: FA 56 DB   LD      A,($DB56)       
588B: FE 80      CP      $80             
588D: C2 B7 3F   JP      NZ,$3FB7        
5890: 79         LD      A,C             
5891: EA 53 D1   LD      ($D153),A       
5894: 11 74 59   LD      DE,$5974        
5897: CD 3B 3C   CALL    $3C3B           
589A: CD 4A 7F   CALL    $7F4A           
589D: 21 10 C4   LD      HL,$C410        
58A0: 09         ADD     HL,BC           
58A1: 7E         LD      A,(HL)          
58A2: A7         AND     A               
58A3: 28 0E      JR      Z,$58B3         
58A5: 21 90 C2   LD      HL,$C290        
58A8: 09         ADD     HL,BC           
58A9: 3E 01      LD      A,$01           
58AB: 77         LD      (HL),A          
58AC: E0 F0      LDFF00  ($F0),A         
58AE: CD 91 08   CALL    $0891           
58B1: 36 40      LD      (HL),$40        
58B3: CD 6C 7F   CALL    $7F6C           
58B6: CD 3D 6E   CALL    $6E3D           
58B9: F0 F0      LD      A,($F0)         
58BB: A7         AND     A               
58BC: 28 75      JR      Z,$5933         
58BE: CD 91 08   CALL    $0891           
58C1: 28 2F      JR      Z,$58F2         
58C3: FE 0A      CP      $0A             
58C5: 20 1D      JR      NZ,$58E4        
58C7: CD 8C 08   CALL    $088C           
58CA: 20 18      JR      NZ,$58E4        
58CC: CD D0 7E   CALL    $7ED0           
58CF: 21 80 C3   LD      HL,$C380        
58D2: 09         ADD     HL,BC           
58D3: 7B         LD      A,E             
58D4: BE         CP      (HL)            
58D5: 20 0D      JR      NZ,$58E4        
58D7: F0 EB      LD      A,($EB)         
58D9: FE 24      CP      $24             
58DB: 28 07      JR      Z,$58E4         
58DD: FE 09      CP      $09             
58DF: 28 07      JR      Z,$58E8         
58E1: CD A4 59   CALL    $59A4           
58E4: CD 92 78   CALL    $7892           
58E7: C9         RET                     
58E8: FA 95 DB   LD      A,($DB95)       
58EB: FE 01      CP      $01             
58ED: C8         RET     Z               
58EE: CD F5 59   CALL    $59F5           
58F1: C9         RET                     
58F2: CD ED 27   CALL    $27ED           
58F5: E6 1F      AND     $1F             
58F7: F6 20      OR      $20             
58F9: 77         LD      (HL),A          
58FA: 21 90 C2   LD      HL,$C290        
58FD: 09         ADD     HL,BC           
58FE: 36 00      LD      (HL),$00        
5900: 21 B0 C2   LD      HL,$C2B0        
5903: 09         ADD     HL,BC           
5904: 7E         LD      A,(HL)          
5905: 3C         INC     A               
5906: E6 03      AND     $03             
5908: 77         LD      (HL),A          
5909: FE 00      CP      $00             
590B: 20 05      JR      NZ,$5912        
590D: CD D0 7E   CALL    $7ED0           
5910: 18 03      JR      $5915           
5912: CD ED 27   CALL    $27ED           
5915: E6 03      AND     $03             
5917: 21 80 C3   LD      HL,$C380        
591A: 09         ADD     HL,BC           
591B: 77         LD      (HL),A          
591C: 5F         LD      E,A             
591D: 50         LD      D,B             
591E: 21 76 58   LD      HL,$5876        
5921: 19         ADD     HL,DE           
5922: 7E         LD      A,(HL)          
5923: 21 40 C2   LD      HL,$C240        
5926: 09         ADD     HL,BC           
5927: 77         LD      (HL),A          
5928: 21 7A 58   LD      HL,$587A        
592B: 19         ADD     HL,DE           
592C: 7E         LD      A,(HL)          
592D: 21 50 C2   LD      HL,$C250        
5930: 09         ADD     HL,BC           
5931: 77         LD      (HL),A          
5932: C9         RET                     
5933: 21 A0 C2   LD      HL,$C2A0        
5936: 09         ADD     HL,BC           
5937: 7E         LD      A,(HL)          
5938: E6 0F      AND     $0F             
593A: 20 05      JR      NZ,$5941        
593C: CD 91 08   CALL    $0891           
593F: 20 11      JR      NZ,$5952        
5941: CD ED 27   CALL    $27ED           
5944: E6 0F      AND     $0F             
5946: F6 10      OR      $10             
5948: 77         LD      (HL),A          
5949: 21 90 C2   LD      HL,$C290        
594C: 09         ADD     HL,BC           
594D: 36 01      LD      (HL),$01        
594F: CD AF 3D   CALL    $3DAF           
5952: CD F7 7E   CALL    $7EF7           
5955: CD 92 78   CALL    $7892           
5958: 21 80 C3   LD      HL,$C380        
595B: 09         ADD     HL,BC           
595C: 5E         LD      E,(HL)          
595D: 50         LD      D,B             
595E: 21 7E 58   LD      HL,$587E        
5961: 19         ADD     HL,DE           
5962: E5         PUSH    HL              
5963: 21 D0 C3   LD      HL,$C3D0        
5966: 09         ADD     HL,BC           
5967: 34         INC     (HL)            
5968: 7E         LD      A,(HL)          
5969: 1F         RRA                     
596A: 1F         RRA                     
596B: 1F         RRA                     
596C: E1         POP     HL              
596D: E6 01      AND     $01             
596F: B6         OR      (HL)            
5970: CD 87 3B   CALL    $3B87           
5973: C9         RET                     
5974: 60         LD      H,B             
5975: 00         NOP                     
5976: 62         LD      H,D             
5977: 00         NOP                     
5978: 62         LD      H,D             
5979: 20 60      JR      NZ,$59DB        
597B: 20 64      JR      NZ,$59E1        
597D: 00         NOP                     
597E: 66         LD      H,(HL)          
597F: 00         NOP                     
5980: 66         LD      H,(HL)          
5981: 20 64      JR      NZ,$59E7        
5983: 20 68      JR      NZ,$59ED        
5985: 00         NOP                     
5986: 6A         LD      L,D             
5987: 00         NOP                     
5988: 6C         LD      L,H             
5989: 00         NOP                     
598A: 6E         LD      L,(HL)          
598B: 00         NOP                     
598C: 6A         LD      L,D             
598D: 20 68      JR      NZ,$59F7        
598F: 20 6E      JR      NZ,$59FF        
5991: 20 6C      JR      NZ,$59FF        
5993: 20 08      JR      NZ,$599D        
5995: F8 04      LDHL    SP,$04          
5997: FC                              
5998: FC                              
5999: FC                              
599A: F8 00      LDHL    SP,$00          
599C: 20 E0      JR      NZ,$597E        
599E: 00         NOP                     
599F: 00         NOP                     
59A0: 00         NOP                     
59A1: 00         NOP                     
59A2: E0 20      LDFF00  ($20),A         
59A4: 3E 0C      LD      A,$0C           
59A6: CD F8 64   CALL    $64F8           
59A9: 38 3D      JR      C,$59E8         
59AB: C5         PUSH    BC              
59AC: F0 D9      LD      A,($D9)         
59AE: 4F         LD      C,A             
59AF: 21 94 59   LD      HL,$5994        
59B2: 09         ADD     HL,BC           
59B3: F0 D7      LD      A,($D7)         
59B5: 86         ADD     A,(HL)          
59B6: 21 00 C2   LD      HL,$C200        
59B9: 19         ADD     HL,DE           
59BA: 77         LD      (HL),A          
59BB: 21 98 59   LD      HL,$5998        
59BE: 09         ADD     HL,BC           
59BF: F0 D8      LD      A,($D8)         
59C1: 86         ADD     A,(HL)          
59C2: 21 10 C2   LD      HL,$C210        
59C5: 19         ADD     HL,DE           
59C6: 77         LD      (HL),A          
59C7: 21 9C 59   LD      HL,$599C        
59CA: 09         ADD     HL,BC           
59CB: 7E         LD      A,(HL)          
59CC: 21 40 C2   LD      HL,$C240        
59CF: 19         ADD     HL,DE           
59D0: 77         LD      (HL),A          
59D1: 21 A0 59   LD      HL,$59A0        
59D4: 09         ADD     HL,BC           
59D5: 7E         LD      A,(HL)          
59D6: 21 50 C2   LD      HL,$C250        
59D9: 19         ADD     HL,DE           
59DA: 77         LD      (HL),A          
59DB: F0 D9      LD      A,($D9)         
59DD: 21 B0 C3   LD      HL,$C3B0        
59E0: 19         ADD     HL,DE           
59E1: 77         LD      (HL),A          
59E2: 21 80 C3   LD      HL,$C380        
59E5: 19         ADD     HL,DE           
59E6: 77         LD      (HL),A          
59E7: C1         POP     BC              
59E8: C9         RET                     
59E9: 08 F8 00   LD      ($00F8),SP      
59EC: 00         NOP                     
59ED: F8 08      LDHL    SP,$08          
59EF: 20 E0      JR      NZ,$59D1        
59F1: 00         NOP                     
59F2: 00         NOP                     
59F3: E0 20      LDFF00  ($20),A         
59F5: 3E 0A      LD      A,$0A           
59F7: CD F8 64   CALL    $64F8           
59FA: 38 37      JR      C,$5A33         
59FC: C5         PUSH    BC              
59FD: F0 D9      LD      A,($D9)         
59FF: 21 80 C3   LD      HL,$C380        
5A02: 19         ADD     HL,DE           
5A03: 77         LD      (HL),A          
5A04: 4F         LD      C,A             
5A05: 21 E9 59   LD      HL,$59E9        
5A08: 09         ADD     HL,BC           
5A09: F0 D7      LD      A,($D7)         
5A0B: 86         ADD     A,(HL)          
5A0C: 21 00 C2   LD      HL,$C200        
5A0F: 19         ADD     HL,DE           
5A10: 77         LD      (HL),A          
5A11: 21 EB 59   LD      HL,$59EB        
5A14: 09         ADD     HL,BC           
5A15: F0 D8      LD      A,($D8)         
5A17: 86         ADD     A,(HL)          
5A18: 21 10 C2   LD      HL,$C210        
5A1B: 19         ADD     HL,DE           
5A1C: 77         LD      (HL),A          
5A1D: 21 EF 59   LD      HL,$59EF        
5A20: 09         ADD     HL,BC           
5A21: 7E         LD      A,(HL)          
5A22: 21 40 C2   LD      HL,$C240        
5A25: 19         ADD     HL,DE           
5A26: 77         LD      (HL),A          
5A27: 21 F1 59   LD      HL,$59F1        
5A2A: 09         ADD     HL,BC           
5A2B: 7E         LD      A,(HL)          
5A2C: 21 50 C2   LD      HL,$C250        
5A2F: 19         ADD     HL,DE           
5A30: 77         LD      (HL),A          
5A31: C1         POP     BC              
5A32: A7         AND     A               
5A33: C9         RET                     
5A34: C9         RET                     
5A35: AA         XOR     D               
5A36: 10 AA      STOP    $AA             
5A38: 30 11      JR      NC,$5A4B        
5A3A: 35         DEC     (HL)            
5A3B: 5A         LD      E,D             
5A3C: CD 3B 3C   CALL    $3C3B           
5A3F: CD 91 08   CALL    $0891           
5A42: CA CC 60   JP      Z,$60CC         
5A45: 3D         DEC     A               
5A46: 20 1A      JR      NZ,$5A62        
5A48: 3E 18      LD      A,$18           
5A4A: EA 68 D3   LD      ($D368),A       
5A4D: 21 5B DB   LD      HL,$DB5B        
5A50: 34         INC     (HL)            
5A51: 21 93 DB   LD      HL,$DB93        
5A54: 36 FF      LD      (HL),$FF        
5A56: CD E2 51   CALL    $51E2           
5A59: 7E         LD      A,(HL)          
5A5A: F6 20      OR      $20             
5A5C: 77         LD      (HL),A          
5A5D: E0 F8      LDFF00  ($F8),A         
5A5F: C3 B7 3F   JP      $3FB7           
5A62: F0 98      LD      A,($98)         
5A64: 21 00 C2   LD      HL,$C200        
5A67: 09         ADD     HL,BC           
5A68: 77         LD      (HL),A          
5A69: F0 99      LD      A,($99)         
5A6B: 21 10 C2   LD      HL,$C210        
5A6E: 09         ADD     HL,BC           
5A6F: D6 0C      SUB     $0C             
5A71: 77         LD      (HL),A          
5A72: F0 A2      LD      A,($A2)         
5A74: 21 10 C3   LD      HL,$C310        
5A77: 09         ADD     HL,BC           
5A78: 77         LD      (HL),A          
5A79: 3E 6C      LD      A,$6C           
5A7B: E0 9D      LDFF00  ($9D),A         
5A7D: 3E 03      LD      A,$03           
5A7F: E0 9E      LDFF00  ($9E),A         
5A81: AF         XOR     A               
5A82: EA 37 C1   LD      ($C137),A       
5A85: EA 6A C1   LD      ($C16A),A       
5A88: EA 22 C1   LD      ($C122),A       
5A8B: EA 21 C1   LD      ($C121),A       
5A8E: 21 70 C4   LD      HL,$C470        
5A91: 09         ADD     HL,BC           
5A92: 77         LD      (HL),A          
5A93: 3E 02      LD      A,$02           
5A95: E0 A1      LDFF00  ($A1),A         
5A97: C9         RET                     
5A98: AC         XOR     H               
5A99: 00         NOP                     
5A9A: AC         XOR     H               
5A9B: 20 F0      JR      NZ,$5A8D        
5A9D: F8 E6      LDHL    SP,$E6          
5A9F: 10 C2      STOP    $C2             
5AA1: B7         OR      A               
5AA2: 3F         CCF                     
5AA3: F0 F0      LD      A,($F0)         
5AA5: C7         RST     0X00            
5AA6: 95         SUB     L               
5AA7: 5B         LD      E,E             
5AA8: B8         CP      B               
5AA9: 5A         LD      E,D             
5AAA: C4 5A CC   CALL    NZ,$CC5A        
5AAD: 5A         LD      E,D             
5AAE: D4 5A E2   CALL    NC,$E25A        
5AB1: 5A         LD      E,D             
5AB2: 05         DEC     B               
5AB3: 5B         LD      E,E             
5AB4: 3C         INC     A               
5AB5: 5B         LD      E,E             
5AB6: 53         LD      D,E             
5AB7: 5B         LD      E,E             
5AB8: CD 62 5A   CALL    $5A62           
5ABB: CD 91 08   CALL    $0891           
5ABE: 20 03      JR      NZ,$5AC3        
5AC0: CD 8D 3B   CALL    $3B8D           
5AC3: C9         RET                     
5AC4: 3E 03      LD      A,$03           
5AC6: E0 90      LDFF00  ($90),A         
5AC8: CD 8D 3B   CALL    $3B8D           
5ACB: C9         RET                     
5ACC: 3E 04      LD      A,$04           
5ACE: E0 90      LDFF00  ($90),A         
5AD0: CD 8D 3B   CALL    $3B8D           
5AD3: C9         RET                     
5AD4: 3E 4F      LD      A,$4F           
5AD6: CD 97 21   CALL    $2197           
5AD9: CD 8D 3B   CALL    $3B8D           
5ADC: 3E 01      LD      A,$01           
5ADE: EA AB C1   LD      ($C1AB),A       
5AE1: C9         RET                     
5AE2: CD 62 5A   CALL    $5A62           
5AE5: 11 98 5A   LD      DE,$5A98        
5AE8: CD 3B 3C   CALL    $3C3B           
5AEB: CD 75 5B   CALL    $5B75           
5AEE: 21 D0 C3   LD      HL,$C3D0        
5AF1: 09         ADD     HL,BC           
5AF2: 34         INC     (HL)            
5AF3: 7E         LD      A,(HL)          
5AF4: FE A8      CP      $A8             
5AF6: CA 8D 3B   JP      Z,$3B8D         
5AF9: FE 38      CP      $38             
5AFB: 20 07      JR      NZ,$5B04        
5AFD: FA 5C DB   LD      A,($DB5C)       
5B00: 3C         INC     A               
5B01: EA 5C DB   LD      ($DB5C),A       
5B04: C9         RET                     
5B05: CD 62 5A   CALL    $5A62           
5B08: 11 98 5A   LD      DE,$5A98        
5B0B: CD 3B 3C   CALL    $3C3B           
5B0E: AF         XOR     A               
5B0F: EA AB C1   LD      ($C1AB),A       
5B12: CD 75 5B   CALL    $5B75           
5B15: FA 9F C1   LD      A,($C19F)       
5B18: A7         AND     A               
5B19: 20 20      JR      NZ,$5B3B        
5B1B: FA 5C DB   LD      A,($DB5C)       
5B1E: FE 04      CP      $04             
5B20: 20 16      JR      NZ,$5B38        
5B22: 3E 19      LD      A,$19           
5B24: E0 F2      LDFF00  ($F2),A         
5B26: AF         XOR     A               
5B27: EA 5C DB   LD      ($DB5C),A       
5B2A: 21 93 DB   LD      HL,$DB93        
5B2D: 36 40      LD      (HL),$40        
5B2F: 21 5B DB   LD      HL,$DB5B        
5B32: 34         INC     (HL)            
5B33: 3E 50      LD      A,$50           
5B35: CD 97 21   CALL    $2197           
5B38: CD 8D 3B   CALL    $3B8D           
5B3B: C9         RET                     
5B3C: CD 62 5A   CALL    $5A62           
5B3F: 11 98 5A   LD      DE,$5A98        
5B42: CD 3B 3C   CALL    $3C3B           
5B45: FA 9F C1   LD      A,($C19F)       
5B48: A7         AND     A               
5B49: 20 07      JR      NZ,$5B52        
5B4B: 3E 05      LD      A,$05           
5B4D: E0 90      LDFF00  ($90),A         
5B4F: CD 8D 3B   CALL    $3B8D           
5B52: C9         RET                     
5B53: 3E 06      LD      A,$06           
5B55: E0 90      LDFF00  ($90),A         
5B57: CD B7 3F   CALL    $3FB7           
5B5A: 3E 0D      LD      A,$0D           
5B5C: E0 A5      LDFF00  ($A5),A         
5B5E: C3 D8 51   JP      $51D8           
5B61: 9A         SBC     D               
5B62: 00         NOP                     
5B63: 9A         SBC     D               
5B64: 20 9C      JR      NZ,$5B02        
5B66: 00         NOP                     
5B67: 9A         SBC     D               
5B68: 20 9E      JR      NZ,$5B08        
5B6A: 00         NOP                     
5B6B: 9A         SBC     D               
5B6C: 20 9E      JR      NZ,$5B0C        
5B6E: 00         NOP                     
5B6F: 9C         SBC     H               
5B70: 20 9E      JR      NZ,$5B10        
5B72: 00         NOP                     
5B73: 9E         SBC     (HL)            
5B74: 20 FA      JR      NZ,$5B70        
5B76: 9F         SBC     A               
5B77: C1         POP     BC              
5B78: A7         AND     A               
5B79: 28 19      JR      Z,$5B94         
5B7B: E6 80      AND     $80             
5B7D: 3E 23      LD      A,$23           
5B7F: 28 02      JR      Z,$5B83         
5B81: 3E 6B      LD      A,$6B           
5B83: E0 EC      LDFF00  ($EC),A         
5B85: FA 5C DB   LD      A,($DB5C)       
5B88: E0 F1      LDFF00  ($F1),A         
5B8A: 3E 8B      LD      A,$8B           
5B8C: E0 EE      LDFF00  ($EE),A         
5B8E: 11 61 5B   LD      DE,$5B61        
5B91: CD 3B 3C   CALL    $3C3B           
5B94: C9         RET                     
5B95: 11 98 5A   LD      DE,$5A98        
5B98: CD 3B 3C   CALL    $3C3B           
5B9B: C3 CC 60   JP      $60CC           
5B9E: AE         XOR     (HL)            
5B9F: 10 11      STOP    $11             
5BA1: 9E         SBC     (HL)            
5BA2: 5B         LD      E,E             
5BA3: CD D0 3C   CALL    $3CD0           
5BA6: 18 18      JR      $5BC0           
5BA8: 14         INC     D               
5BA9: 00         NOP                     
5BAA: 14         INC     D               
5BAB: 20 14      JR      NZ,$5BC1        
5BAD: 10 14      STOP    $14             
5BAF: 30 11      JR      NC,$5BC2        
5BB1: A8         XOR     B               
5BB2: 5B         LD      E,E             
5BB3: CD 3B 3C   CALL    $3C3B           
5BB6: F0 E7      LD      A,($E7)         
5BB8: 1F         RRA                     
5BB9: 1F         RRA                     
5BBA: 1F         RRA                     
5BBB: E6 01      AND     $01             
5BBD: CD 87 3B   CALL    $3B87           
5BC0: C3 CC 60   JP      $60CC           
5BC3: 74         LD      (HL),H          
5BC4: 00         NOP                     
5BC5: 76         HALT                    
5BC6: 00         NOP                     
5BC7: 76         HALT                    
5BC8: 20 74      JR      NZ,$5C3E        
5BCA: 20 11      JR      NZ,$5BDD        
5BCC: C3 5B CD   JP      $CD5B           
5BCF: 3B         DEC     SP              
5BD0: 3C         INC     A               
5BD1: CD 4A 7F   CALL    $7F4A           
5BD4: CD D4 62   CALL    $62D4           
5BD7: C9         RET                     
5BD8: 86         ADD     A,(HL)          
5BD9: 10 84      STOP    $84             
5BDB: 10 11      STOP    $11             
5BDD: D8         RET     C               
5BDE: 5B         LD      E,E             
5BDF: FA 4E DB   LD      A,($DB4E)       
5BE2: A7         AND     A               
5BE3: 20 0A      JR      NZ,$5BEF        
5BE5: F0 F8      LD      A,($F8)         
5BE7: E6 10      AND     $10             
5BE9: C2 B7 3F   JP      NZ,$3FB7        
5BEC: 11 DA 5B   LD      DE,$5BDA        
5BEF: CD D0 3C   CALL    $3CD0           
5BF2: F0 F0      LD      A,($F0)         
5BF4: C7         RST     0X00            
5BF5: FD                              
5BF6: 5B         LD      E,E             
5BF7: 27         DAA                     
5BF8: 5C         LD      E,H             
5BF9: 46         LD      B,(HL)          
5BFA: 5C         LD      E,H             
5BFB: 56         LD      D,(HL)          
5BFC: 5C         LD      E,H             
5BFD: CD 91 08   CALL    $0891           
5C00: CA CC 60   JP      Z,$60CC         
5C03: FE 10      CP      $10             
5C05: 20 07      JR      NZ,$5C0E        
5C07: 35         DEC     (HL)            
5C08: 3E 9B      LD      A,$9B           
5C0A: CD 97 21   CALL    $2197           
5C0D: AF         XOR     A               
5C0E: 3D         DEC     A               
5C0F: 20 13      JR      NZ,$5C24        
5C11: 3E 31      LD      A,$31           
5C13: EA 68 D3   LD      ($D368),A       
5C16: 3E 05      LD      A,$05           
5C18: E0 B0      LDFF00  ($B0),A         
5C1A: E0 BF      LDFF00  ($BF),A         
5C1C: CD 87 08   CALL    $0887           
5C1F: 36 52      LD      (HL),$52        
5C21: CD 8D 3B   CALL    $3B8D           
5C24: C3 62 5A   JP      $5A62           
5C27: CD 62 5A   CALL    $5A62           
5C2A: CD 87 08   CALL    $0887           
5C2D: 20 16      JR      NZ,$5C45        
5C2F: 3E FF      LD      A,$FF           
5C31: CD 87 3B   CALL    $3B87           
5C34: CD 91 08   CALL    $0891           
5C37: 36 20      LD      (HL),$20        
5C39: 3E 20      LD      A,$20           
5C3B: EA 21 C1   LD      ($C121),A       
5C3E: 3E 03      LD      A,$03           
5C40: E0 F4      LDFF00  ($F4),A         
5C42: CD 8D 3B   CALL    $3B8D           
5C45: C9         RET                     
5C46: CD 91 08   CALL    $0891           
5C49: 20 0A      JR      NZ,$5C55        
5C4B: 36 20      LD      (HL),$20        
5C4D: 3E 00      LD      A,$00           
5C4F: CD 87 3B   CALL    $3B87           
5C52: CD 8D 3B   CALL    $3B8D           
5C55: C9         RET                     
5C56: CD 62 5A   CALL    $5A62           
5C59: 3E 6B      LD      A,$6B           
5C5B: E0 9D      LDFF00  ($9D),A         
5C5D: 21 00 C2   LD      HL,$C200        
5C60: 09         ADD     HL,BC           
5C61: F0 98      LD      A,($98)         
5C63: D6 04      SUB     $04             
5C65: 77         LD      (HL),A          
5C66: CD 91 08   CALL    $0891           
5C69: 20 13      JR      NZ,$5C7E        
5C6B: EA 67 C1   LD      ($C167),A       
5C6E: 16 01      LD      D,$01           
5C70: CD 97 64   CALL    $6497           
5C73: 3E 01      LD      A,$01           
5C75: EA 4E DB   LD      ($DB4E),A       
5C78: CD D8 51   CALL    $51D8           
5C7B: C3 B7 3F   JP      $3FB7           
5C7E: FE 1A      CP      $1A             
5C80: 20 0B      JR      NZ,$5C8D        
5C82: F0 EF      LD      A,($EF)         
5C84: D6 0C      SUB     $0C             
5C86: CD 51 6C   CALL    $6C51           
5C89: 3E 07      LD      A,$07           
5C8B: E0 F2      LDFF00  ($F2),A         
5C8D: C9         RET                     
5C8E: 8A         ADC     A,D             
5C8F: 10 F0      STOP    $F0             
5C91: F8 E6      LDHL    SP,$E6          
5C93: 10 C2      STOP    $C2             
5C95: B7         OR      A               
5C96: 3F         CCF                     
5C97: 11 8E 5C   LD      DE,$5C8E        
5C9A: CD D0 3C   CALL    $3CD0           
5C9D: CD 91 08   CALL    $0891           
5CA0: CA CC 60   JP      Z,$60CC         
5CA3: FE 10      CP      $10             
5CA5: 20 07      JR      NZ,$5CAE        
5CA7: 35         DEC     (HL)            
5CA8: 3E 93      LD      A,$93           
5CAA: CD 97 21   CALL    $2197           
5CAD: AF         XOR     A               
5CAE: 3D         DEC     A               
5CAF: 20 0B      JR      NZ,$5CBC        
5CB1: 16 06      LD      D,$06           
5CB3: CD 97 64   CALL    $6497           
5CB6: CD D8 51   CALL    $51D8           
5CB9: C3 B7 3F   JP      $3FB7           
5CBC: C3 62 5A   JP      $5A62           
5CBF: CA 10 C0   JP      Z,$C010         
5CC2: 10 C2      STOP    $C2             
5CC4: 10 C4      STOP    $C4             
5CC6: 10 C6      STOP    $C6             
5CC8: 10 CA      STOP    $CA             
5CCA: 10 00      STOP    $00             
5CCC: A3         AND     E               
5CCD: A4         AND     H               
5CCE: A5         AND     L               
5CCF: 00         NOP                     
5CD0: CD 31 5D   CALL    $5D31           
5CD3: 30 0B      JR      NC,$5CE0        
5CD5: 21 CE D8   LD      HL,$D8CE        
5CD8: CB E6      SET     1,E             
5CDA: 21 F8 D9   LD      HL,$D9F8        
5CDD: CB EE      SET     1,E             
5CDF: C9         RET                     
5CE0: F0 F6      LD      A,($F6)         
5CE2: FE 80      CP      $80             
5CE4: CA 90 5C   JP      Z,$5C90         
5CE7: 11 BF 5C   LD      DE,$5CBF        
5CEA: CD D0 3C   CALL    $3CD0           
5CED: CD 91 08   CALL    $0891           
5CF0: CA 1D 5D   JP      Z,$5D1D         
5CF3: FE 10      CP      $10             
5CF5: 20 1D      JR      NZ,$5D14        
5CF7: 35         DEC     (HL)            
5CF8: F0 F1      LD      A,($F1)         
5CFA: 3D         DEC     A               
5CFB: 5F         LD      E,A             
5CFC: 50         LD      D,B             
5CFD: 21 CB 5C   LD      HL,$5CCB        
5D00: 19         ADD     HL,DE           
5D01: 7E         LD      A,(HL)          
5D02: CD 97 21   CALL    $2197           
5D05: F0 F1      LD      A,($F1)         
5D07: 3D         DEC     A               
5D08: 5F         LD      E,A             
5D09: 50         LD      D,B             
5D0A: 21 11 DB   LD      HL,$DB11        
5D0D: 19         ADD     HL,DE           
5D0E: 36 01      LD      (HL),$01        
5D10: CD D8 51   CALL    $51D8           
5D13: AF         XOR     A               
5D14: 3D         DEC     A               
5D15: 20 03      JR      NZ,$5D1A        
5D17: C3 B7 3F   JP      $3FB7           
5D1A: C3 62 5A   JP      $5A62           
5D1D: CD 4A 7F   CALL    $7F4A           
5D20: CD D4 62   CALL    $62D4           
5D23: 21 10 C3   LD      HL,$C310        
5D26: 09         ADD     HL,BC           
5D27: 7E         LD      A,(HL)          
5D28: A7         AND     A               
5D29: 20 03      JR      NZ,$5D2E        
5D2B: CD 10 63   CALL    $6310           
5D2E: C3 D5 60   JP      $60D5           
5D31: FA A5 DB   LD      A,($DBA5)       
5D34: A7         AND     A               
5D35: 20 44      JR      NZ,$5D7B        
5D37: F0 F6      LD      A,($F6)         
5D39: FE CE      CP      $CE             
5D3B: 20 3E      JR      NZ,$5D7B        
5D3D: F0 EF      LD      A,($EF)         
5D3F: D6 48      SUB     $48             
5D41: C6 03      ADD     $03             
5D43: FE 06      CP      $06             
5D45: 30 34      JR      NC,$5D7B        
5D47: F0 EE      LD      A,($EE)         
5D49: D6 50      SUB     $50             
5D4B: C6 03      ADD     $03             
5D4D: FE 06      CP      $06             
5D4F: 30 2A      JR      NC,$5D7B        
5D51: 21 10 C3   LD      HL,$C310        
5D54: 09         ADD     HL,BC           
5D55: 7E         LD      A,(HL)          
5D56: A7         AND     A               
5D57: 20 22      JR      NZ,$5D7B        
5D59: 21 80 C2   LD      HL,$C280        
5D5C: 09         ADD     HL,BC           
5D5D: 7E         LD      A,(HL)          
5D5E: FE 05      CP      $05             
5D60: 20 19      JR      NZ,$5D7B        
5D62: 36 02      LD      (HL),$02        
5D64: 21 B0 C4   LD      HL,$C4B0        
5D67: 09         ADD     HL,BC           
5D68: 36 50      LD      (HL),$50        
5D6A: 21 C0 C4   LD      HL,$C4C0        
5D6D: 09         ADD     HL,BC           
5D6E: 36 48      LD      (HL),$48        
5D70: CD 91 08   CALL    $0891           
5D73: 36 2F      LD      (HL),$2F        
5D75: 3E 18      LD      A,$18           
5D77: E0 F2      LDFF00  ($F2),A         
5D79: 37         SCF                     
5D7A: C9         RET                     
5D7B: A7         AND     A               
5D7C: C9         RET                     
5D7D: A8         XOR     B               
5D7E: 10 CD      STOP    $CD             
5D80: 03         INC     BC              
5D81: 62         LD      H,D             
5D82: CD AC 60   CALL    $60AC           
5D85: 11 7D 5D   LD      DE,$5D7D        
5D88: CD D0 3C   CALL    $3CD0           
5D8B: C3 CC 60   JP      $60CC           
5D8E: 5E         LD      E,(HL)          
5D8F: 00         NOP                     
5D90: 5E         LD      E,(HL)          
5D91: 20 21      JR      NZ,$5DB4        
5D93: 4B         LD      C,E             
5D94: DB                              
5D95: FA 4C DB   LD      A,($DB4C)       
5D98: B6         OR      (HL)            
5D99: C2 B7 3F   JP      NZ,$3FB7        
5D9C: 11 8E 5D   LD      DE,$5D8E        
5D9F: CD 3B 3C   CALL    $3C3B           
5DA2: CD 91 08   CALL    $0891           
5DA5: CA CC 60   JP      Z,$60CC         
5DA8: FE 10      CP      $10             
5DAA: 20 07      JR      NZ,$5DB3        
5DAC: 35         DEC     (HL)            
5DAD: 3E 0F      LD      A,$0F           
5DAF: CD 97 21   CALL    $2197           
5DB2: AF         XOR     A               
5DB3: 3D         DEC     A               
5DB4: 20 11      JR      NZ,$5DC7        
5DB6: 3E 0A      LD      A,$0A           
5DB8: E0 A5      LDFF00  ($A5),A         
5DBA: 16 0C      LD      D,$0C           
5DBC: CD 97 64   CALL    $6497           
5DBF: 3E 01      LD      A,$01           
5DC1: EA 4B DB   LD      ($DB4B),A       
5DC4: C3 B7 3F   JP      $3FB7           
5DC7: C3 62 5A   JP      $5A62           
5DCA: 70         LD      (HL),B          
5DCB: 00         NOP                     
5DCC: 72         LD      (HL),D          
5DCD: 00         NOP                     
5DCE: 74         LD      (HL),H          
5DCF: 00         NOP                     
5DD0: 76         HALT                    
5DD1: 00         NOP                     
5DD2: 78         LD      A,B             
5DD3: 00         NOP                     
5DD4: 7A         LD      A,D             
5DD5: 00         NOP                     
5DD6: 7C         LD      A,H             
5DD7: 00         NOP                     
5DD8: 7E         LD      A,(HL)          
5DD9: 00         NOP                     
5DDA: 21 B0 C2   LD      HL,$C2B0        
5DDD: 09         ADD     HL,BC           
5DDE: 7E         LD      A,(HL)          
5DDF: C7         RST     0X00            
5DE0: DA 5E CA   JP      C,$CA5E         
5DE3: 5E         LD      E,(HL)          
5DE4: 20 5E      JR      NZ,$5E44        
5DE6: E4                              
5DE7: E4                              
5DE8: E4                              
5DE9: E4                              
5DEA: 90         SUB     B               
5DEB: 90         SUB     B               
5DEC: 90         SUB     B               
5DED: 90         SUB     B               
5DEE: 40         LD      B,B             
5DEF: 40         LD      B,B             
5DF0: 40         LD      B,B             
5DF1: 40         LD      B,B             
5DF2: 00         NOP                     
5DF3: 00         NOP                     
5DF4: 00         NOP                     
5DF5: 00         NOP                     
5DF6: 00         NOP                     
5DF7: 00         NOP                     
5DF8: 00         NOP                     
5DF9: 00         NOP                     
5DFA: 00         NOP                     
5DFB: 00         NOP                     
5DFC: 00         NOP                     
5DFD: 00         NOP                     
5DFE: 00         NOP                     
5DFF: 00         NOP                     
5E00: 00         NOP                     
5E01: 00         NOP                     
5E02: 00         NOP                     
5E03: 1C         INC     E               
5E04: 1C         INC     E               
5E05: 1C         INC     E               
5E06: 1C         INC     E               
5E07: 1C         INC     E               
5E08: 1C         INC     E               
5E09: 1C         INC     E               
5E0A: 1C         INC     E               
5E0B: 1C         INC     E               
5E0C: 1C         INC     E               
5E0D: 1C         INC     E               
5E0E: 1C         INC     E               
5E0F: 1C         INC     E               
5E10: 1C         INC     E               
5E11: 1C         INC     E               
5E12: 1C         INC     E               
5E13: 08 08 08   LD      ($0808),SP      
5E16: 08 04 04   LD      ($0404),SP      
5E19: 04         INC     B               
5E1A: 04         INC     B               
5E1B: 00         NOP                     
5E1C: 00         NOP                     
5E1D: 00         NOP                     
5E1E: 00         NOP                     
5E1F: 00         NOP                     
5E20: CD A0 3E   CALL    $3EA0           
5E23: 3E 01      LD      A,$01           
5E25: EA 67 C1   LD      ($C167),A       
5E28: CD 87 08   CALL    $0887           
5E2B: 20 43      JR      NZ,$5E70        
5E2D: CD B7 3F   CALL    $3FB7           
5E30: AF         XOR     A               
5E31: E0 9D      LDFF00  ($9D),A         
5E33: FA 01 D2   LD      A,($D201)       
5E36: 5F         LD      E,A             
5E37: 50         LD      D,B             
5E38: 21 90 C2   LD      HL,$C290        
5E3B: 19         ADD     HL,DE           
5E3C: 34         INC     (HL)            
5E3D: CD 2A 09   CALL    $092A           
5E40: F0 F7      LD      A,($F7)         
5E42: C7         RST     0X00            
5E43: 53         LD      D,E             
5E44: 5E         LD      E,(HL)          
5E45: 59         LD      E,C             
5E46: 5E         LD      E,(HL)          
5E47: 5F         LD      E,A             
5E48: 5E         LD      E,(HL)          
5E49: 60         LD      H,B             
5E4A: 5E         LD      E,(HL)          
5E4B: 65         LD      H,L             
5E4C: 5E         LD      E,(HL)          
5E4D: 66         LD      H,(HL)          
5E4E: 5E         LD      E,(HL)          
5E4F: 6B         LD      L,E             
5E50: 5E         LD      E,(HL)          
5E51: 65         LD      H,L             
5E52: 5E         LD      E,(HL)          
5E53: 3E 80      LD      A,$80           
5E55: EA 56 DB   LD      ($DB56),A       
5E58: C9         RET                     
5E59: 3E 02      LD      A,$02           
5E5B: EA 48 DB   LD      ($DB48),A       
5E5E: C9         RET                     
5E5F: C9         RET                     
5E60: 3E 02      LD      A,$02           
5E62: EA 79 DB   LD      ($DB79),A       
5E65: C9         RET                     
5E66: AF         XOR     A               
5E67: EA 74 DB   LD      ($DB74),A       
5E6A: C9         RET                     
5E6B: AF         XOR     A               
5E6C: EA 7B DB   LD      ($DB7B),A       
5E6F: C9         RET                     
5E70: FE 50      CP      $50             
5E72: 30 4D      JR      NC,$5EC1        
5E74: 21 C0 C2   LD      HL,$C2C0        
5E77: 09         ADD     HL,BC           
5E78: 7E         LD      A,(HL)          
5E79: FE 19      CP      $19             
5E7B: 30 44      JR      NC,$5EC1        
5E7D: F0 E7      LD      A,($E7)         
5E7F: E6 07      AND     $07             
5E81: 20 1F      JR      NZ,$5EA2        
5E83: 7E         LD      A,(HL)          
5E84: A7         AND     A               
5E85: 20 05      JR      NZ,$5E8C        
5E87: 3E 2C      LD      A,$2C           
5E89: E0 F4      LDFF00  ($F4),A         
5E8B: AF         XOR     A               
5E8C: 34         INC     (HL)            
5E8D: FE 18      CP      $18             
5E8F: 20 11      JR      NZ,$5EA2        
5E91: 3E 9F      LD      A,$9F           
5E93: CD F8 64   CALL    $64F8           
5E96: 21 B0 C2   LD      HL,$C2B0        
5E99: 19         ADD     HL,DE           
5E9A: 36 01      LD      (HL),$01        
5E9C: 21 E0 C2   LD      HL,$C2E0        
5E9F: 19         ADD     HL,DE           
5EA0: 36 60      LD      (HL),$60        
5EA2: F0 E7      LD      A,($E7)         
5EA4: E6 03      AND     $03             
5EA6: 21 C0 C2   LD      HL,$C2C0        
5EA9: 09         ADD     HL,BC           
5EAA: 86         ADD     A,(HL)          
5EAB: 5F         LD      E,A             
5EAC: 50         LD      D,B             
5EAD: 21 E6 5D   LD      HL,$5DE6        
5EB0: 19         ADD     HL,DE           
5EB1: 7E         LD      A,(HL)          
5EB2: EA 97 DB   LD      ($DB97),A       
5EB5: 21 03 5E   LD      HL,$5E03        
5EB8: 19         ADD     HL,DE           
5EB9: 7E         LD      A,(HL)          
5EBA: EA 98 DB   LD      ($DB98),A       
5EBD: AF         XOR     A               
5EBE: EA 99 DB   LD      ($DB99),A       
5EC1: C9         RET                     
5EC2: 6C         LD      L,H             
5EC3: 00         NOP                     
5EC4: FF         RST     0X38            
5EC5: FF         RST     0X38            
5EC6: 6C         LD      L,H             
5EC7: 00         NOP                     
5EC8: 6E         LD      L,(HL)          
5EC9: 00         NOP                     
5ECA: 11 C2 5E   LD      DE,$5EC2        
5ECD: CD 3B 3C   CALL    $3C3B           
5ED0: CD F7 7E   CALL    $7EF7           
5ED3: CD 91 08   CALL    $0891           
5ED6: CA B7 3F   JP      Z,$3FB7         
5ED9: C9         RET                     
5EDA: 79         LD      A,C             
5EDB: EA 01 D2   LD      ($D201),A       
5EDE: F0 F8      LD      A,($F8)         
5EE0: E6 10      AND     $10             
5EE2: C2 B7 3F   JP      NZ,$3FB7        
5EE5: F0 F7      LD      A,($F7)         
5EE7: E6 03      AND     $03             
5EE9: E0 F1      LDFF00  ($F1),A         
5EEB: CD 0E 38   CALL    $380E           
5EEE: 11 CA 5D   LD      DE,$5DCA        
5EF1: CD 3B 3C   CALL    $3C3B           
5EF4: F0 F0      LD      A,($F0)         
5EF6: C7         RST     0X00            
5EF7: 01 5F 38   LD      BC,$385F        
5EFA: 5F         LD      E,A             
5EFB: 5F         LD      E,A             
5EFC: 5F         LD      E,A             
5EFD: E8 5F      ADD     SP,$5F          
5EFF: EB                              
5F00: 5F         LD      E,A             
5F01: CD 91 08   CALL    $0891           
5F04: CA CC 60   JP      Z,$60CC         
5F07: FE 10      CP      $10             
5F09: 20 1F      JR      NZ,$5F2A        
5F0B: 35         DEC     (HL)            
5F0C: CD 8D 3B   CALL    $3B8D           
5F0F: F0 F7      LD      A,($F7)         
5F11: C6 00      ADD     $00             
5F13: CD 85 21   CALL    $2185           
5F16: F0 F7      LD      A,($F7)         
5F18: 5F         LD      E,A             
5F19: 50         LD      D,B             
5F1A: 21 65 DB   LD      HL,$DB65        
5F1D: 19         ADD     HL,DE           
5F1E: 7E         LD      A,(HL)          
5F1F: F6 02      OR      $02             
5F21: 77         LD      (HL),A          
5F22: CD E2 51   CALL    $51E2           
5F25: 7E         LD      A,(HL)          
5F26: F6 10      OR      $10             
5F28: 77         LD      (HL),A          
5F29: AF         XOR     A               
5F2A: 3D         DEC     A               
5F2B: 20 00      JR      NZ,$5F2D        
5F2D: C3 62 5A   JP      $5A62           
5F30: 20 28      JR      NZ,$5F5A        
5F32: 29         ADD     HL,HL           
5F33: 2A         LD      A,(HLI)         
5F34: 2B         DEC     HL              
5F35: 2C         INC     L               
5F36: 2D         DEC     L               
5F37: 2E FA      LD      L,$FA           
5F39: 69         LD      L,C             
5F3A: D3                              
5F3B: A7         AND     A               
5F3C: 20 1A      JR      NZ,$5F58        
5F3E: FA 9F C1   LD      A,($C19F)       
5F41: A7         AND     A               
5F42: 20 14      JR      NZ,$5F58        
5F44: F0 F7      LD      A,($F7)         
5F46: 5F         LD      E,A             
5F47: 50         LD      D,B             
5F48: 21 30 5F   LD      HL,$5F30        
5F4B: 19         ADD     HL,DE           
5F4C: 7E         LD      A,(HL)          
5F4D: EA 68 D3   LD      ($D368),A       
5F50: CD 8D 3B   CALL    $3B8D           
5F53: CD 91 08   CALL    $0891           
5F56: 36 FF      LD      (HL),$FF        
5F58: C3 62 5A   JP      $5A62           
5F5B: 0A         LD      A,(BC)          
5F5C: FA 04 FC   LD      A,($FC04)       
5F5F: CD 91 08   CALL    $0891           
5F62: 20 27      JR      NZ,$5F8B        
5F64: 3E 2B      LD      A,$2B           
5F66: E0 F2      LDFF00  ($F2),A         
5F68: 3E 39      LD      A,$39           
5F6A: CD F8 64   CALL    $64F8           
5F6D: F0 D7      LD      A,($D7)         
5F6F: 3D         DEC     A               
5F70: 21 00 C2   LD      HL,$C200        
5F73: 19         ADD     HL,DE           
5F74: 77         LD      (HL),A          
5F75: F0 D8      LD      A,($D8)         
5F77: 21 10 C2   LD      HL,$C210        
5F7A: 19         ADD     HL,DE           
5F7B: 77         LD      (HL),A          
5F7C: 21 B0 C2   LD      HL,$C2B0        
5F7F: 19         ADD     HL,DE           
5F80: 36 02      LD      (HL),$02        
5F82: 21 50 C4   LD      HL,$C450        
5F85: 19         ADD     HL,DE           
5F86: 36 80      LD      (HL),$80        
5F88: C3 8D 3B   JP      $3B8D           
5F8B: 21 D0 C2   LD      HL,$C2D0        
5F8E: 09         ADD     HL,BC           
5F8F: 35         DEC     (HL)            
5F90: 7E         LD      A,(HL)          
5F91: FE FF      CP      $FF             
5F93: 20 50      JR      NZ,$5FE5        
5F95: 36 17      LD      (HL),$17        
5F97: 21 40 C4   LD      HL,$C440        
5F9A: 09         ADD     HL,BC           
5F9B: 34         INC     (HL)            
5F9C: 7E         LD      A,(HL)          
5F9D: E6 01      AND     $01             
5F9F: E0 E8      LDFF00  ($E8),A         
5FA1: 3E 39      LD      A,$39           
5FA3: CD F8 64   CALL    $64F8           
5FA6: C5         PUSH    BC              
5FA7: 21 B0 C2   LD      HL,$C2B0        
5FAA: 19         ADD     HL,DE           
5FAB: 34         INC     (HL)            
5FAC: F0 E8      LD      A,($E8)         
5FAE: 4F         LD      C,A             
5FAF: 21 5B 5F   LD      HL,$5F5B        
5FB2: 09         ADD     HL,BC           
5FB3: F0 D7      LD      A,($D7)         
5FB5: 86         ADD     A,(HL)          
5FB6: 21 00 C2   LD      HL,$C200        
5FB9: 19         ADD     HL,DE           
5FBA: 77         LD      (HL),A          
5FBB: 21 5D 5F   LD      HL,$5F5D        
5FBE: 09         ADD     HL,BC           
5FBF: 7E         LD      A,(HL)          
5FC0: 21 40 C2   LD      HL,$C240        
5FC3: 19         ADD     HL,DE           
5FC4: 77         LD      (HL),A          
5FC5: F0 D8      LD      A,($D8)         
5FC7: 21 10 C2   LD      HL,$C210        
5FCA: 19         ADD     HL,DE           
5FCB: C6 F8      ADD     $F8             
5FCD: 77         LD      (HL),A          
5FCE: 21 50 C2   LD      HL,$C250        
5FD1: 19         ADD     HL,DE           
5FD2: 36 FD      LD      (HL),$FD        
5FD4: 21 E0 C2   LD      HL,$C2E0        
5FD7: 19         ADD     HL,DE           
5FD8: 36 38      LD      (HL),$38        
5FDA: CD ED 27   CALL    $27ED           
5FDD: E6 01      AND     $01             
5FDF: 21 B0 C3   LD      HL,$C3B0        
5FE2: 19         ADD     HL,DE           
5FE3: 77         LD      (HL),A          
5FE4: C1         POP     BC              
5FE5: C3 62 5A   JP      $5A62           
5FE8: C3 62 5A   JP      $5A62           
5FEB: C9         RET                     
5FEC: 80         ADD     A,B             
5FED: 10 CD      STOP    $CD             
5FEF: 03         INC     BC              
5FF0: 62         LD      H,D             
5FF1: CD AC 60   CALL    $60AC           
5FF4: 11 EC 5F   LD      DE,$5FEC        
5FF7: CD D0 3C   CALL    $3CD0           
5FFA: C3 CC 60   JP      $60CC           
5FFD: 9E         SBC     (HL)            
5FFE: 10 FA      STOP    $FA             
6000: 4E         LD      C,(HL)          
6001: DB                              
6002: FE 02      CP      $02             
6004: D2 B7 3F   JP      NC,$3FB7        
6007: F0 F8      LD      A,($F8)         
6009: E6 10      AND     $10             
600B: C2 B7 3F   JP      NZ,$3FB7        
600E: F0 F6      LD      A,($F6)         
6010: FE E3      CP      $E3             
6012: 20 07      JR      NZ,$601B        
6014: F0 F8      LD      A,($F8)         
6016: E6 40      AND     $40             
6018: CA B7 3F   JP      Z,$3FB7         
601B: CD 03 62   CALL    $6203           
601E: 11 FD 5F   LD      DE,$5FFD        
6021: CD D0 3C   CALL    $3CD0           
6024: C3 CC 60   JP      $60CC           
6027: CA 10 F0   JP      Z,$F010         
602A: F8 E6      LDHL    SP,$E6          
602C: 10 C2      STOP    $C2             
602E: B7         OR      A               
602F: 3F         CCF                     
6030: CD 03 62   CALL    $6203           
6033: 11 27 60   LD      DE,$6027        
6036: CD D0 3C   CALL    $3CD0           
6039: CD 91 08   CALL    $0891           
603C: CA CC 60   JP      Z,$60CC         
603F: FE 10      CP      $10             
6041: 20 35      JR      NZ,$6078        
6043: 35         DEC     (HL)            
6044: FA A5 DB   LD      A,($DBA5)       
6047: A7         AND     A               
6048: 20 0B      JR      NZ,$6055        
604A: F0 F6      LD      A,($F6)         
604C: FE C6      CP      $C6             
604E: 20 05      JR      NZ,$6055        
6050: 3E 05      LD      A,$05           
6052: EA 15 DB   LD      ($DB15),A       
6055: 21 15 DB   LD      HL,$DB15        
6058: CD 98 63   CALL    $6398           
605B: CD D8 51   CALL    $51D8           
605E: 21 F8 FF   LD      HL,$FFF8        
6061: CB A6      SET     1,E             
6063: 1E A2      LD      E,$A2           
6065: FA 15 DB   LD      A,($DB15)       
6068: FE 06      CP      $06             
606A: 28 07      JR      Z,$6073         
606C: 1E E8      LD      E,$E8           
606E: FE 05      CP      $05             
6070: 20 01      JR      NZ,$6073        
6072: 1C         INC     E               
6073: 7B         LD      A,E             
6074: CD 97 21   CALL    $2197           
6077: AF         XOR     A               
6078: 3D         DEC     A               
6079: 20 03      JR      NZ,$607E        
607B: C3 B7 3F   JP      $3FB7           
607E: C3 62 5A   JP      $5A62           
6081: 8E         ADC     A,(HL)          
6082: 10 FA      STOP    $FA             
6084: 4B         LD      C,E             
6085: DB                              
6086: A7         AND     A               
6087: C2 B7 3F   JP      NZ,$3FB7        
608A: CD 03 62   CALL    $6203           
608D: CD AC 60   CALL    $60AC           
6090: 11 81 60   LD      DE,$6081        
6093: CD D0 3C   CALL    $3CD0           
6096: C3 CC 60   JP      $60CC           
6099: 2A         LD      A,(HLI)         
609A: 40         LD      B,B             
609B: 2A         LD      A,(HLI)         
609C: 60         LD      H,B             
609D: CD 03 62   CALL    $6203           
60A0: CD AC 60   CALL    $60AC           
60A3: 11 99 60   LD      DE,$6099        
60A6: CD 3B 3C   CALL    $3C3B           
60A9: C3 CC 60   JP      $60CC           
60AC: CD 87 08   CALL    $0887           
60AF: FE 1C      CP      $1C             
60B1: 30 0A      JR      NC,$60BD        
60B3: A7         AND     A               
60B4: CA B7 3F   JP      Z,$3FB7         
60B7: E6 01      AND     $01             
60B9: 3D         DEC     A               
60BA: CD 87 3B   CALL    $3B87           
60BD: C9         RET                     
60BE: A6         AND     (HL)            
60BF: 10 CD      STOP    $CD             
60C1: 03         INC     BC              
60C2: 62         LD      H,D             
60C3: CD AC 60   CALL    $60AC           
60C6: 11 BE 60   LD      DE,$60BE        
60C9: CD D0 3C   CALL    $3CD0           
60CC: CD 4A 7F   CALL    $7F4A           
60CF: CD D4 62   CALL    $62D4           
60D2: CD 10 63   CALL    $6310           
60D5: CD F7 7E   CALL    $7EF7           
60D8: CD 96 6B   CALL    $6B96           
60DB: CD 92 78   CALL    $7892           
60DE: F0 F9      LD      A,($F9)         
60E0: A7         AND     A               
60E1: 28 22      JR      Z,$6105         
60E3: 21 A0 C2   LD      HL,$C2A0        
60E6: 09         ADD     HL,BC           
60E7: 7E         LD      A,(HL)          
60E8: E6 08      AND     $08             
60EA: CA 78 61   JP      Z,$6178         
60ED: 21 10 C2   LD      HL,$C210        
60F0: 09         ADD     HL,BC           
60F1: 7E         LD      A,(HL)          
60F2: E6 F0      AND     $F0             
60F4: C6 05      ADD     $05             
60F6: 77         LD      (HL),A          
60F7: 21 50 C2   LD      HL,$C250        
60FA: 09         ADD     HL,BC           
60FB: 7E         LD      A,(HL)          
60FC: 2F         CPL                     
60FD: CB 2F      SET     1,E             
60FF: FE F8      CP      $F8             
6101: 38 31      JR      C,$6134         
6103: 18 20      JR      $6125           
6105: 21 10 C3   LD      HL,$C310        
6108: 09         ADD     HL,BC           
6109: 7E         LD      A,(HL)          
610A: E6 80      AND     $80             
610C: 28 6A      JR      Z,$6178         
610E: AF         XOR     A               
610F: 77         LD      (HL),A          
6110: 21 70 C4   LD      HL,$C470        
6113: 09         ADD     HL,BC           
6114: 7E         LD      A,(HL)          
6115: 21 20 C3   LD      HL,$C320        
6118: 09         ADD     HL,BC           
6119: FE 02      CP      $02             
611B: 28 08      JR      Z,$6125         
611D: 7E         LD      A,(HL)          
611E: CB 2F      SET     1,E             
6120: 2F         CPL                     
6121: FE 07      CP      $07             
6123: 30 0F      JR      NC,$6134        
6125: AF         XOR     A               
6126: E5         PUSH    HL              
6127: 21 40 C2   LD      HL,$C240        
612A: 09         ADD     HL,BC           
612B: 77         LD      (HL),A          
612C: 21 50 C2   LD      HL,$C250        
612F: 09         ADD     HL,BC           
6130: 77         LD      (HL),A          
6131: E1         POP     HL              
6132: 18 24      JR      $6158           
6134: F5         PUSH    AF              
6135: E5         PUSH    HL              
6136: F0 EB      LD      A,($EB)         
6138: FE 30      CP      $30             
613A: 20 06      JR      NZ,$6142        
613C: 3E 17      LD      A,$17           
613E: E0 F4      LDFF00  ($F4),A         
6140: 18 14      JR      $6156           
6142: FE 02      CP      $02             
6144: 20 10      JR      NZ,$6156        
6146: 21 80 C2   LD      HL,$C280        
6149: 09         ADD     HL,BC           
614A: 7E         LD      A,(HL)          
614B: A7         AND     A               
614C: 28 08      JR      Z,$6156         
614E: FE 02      CP      $02             
6150: 28 04      JR      Z,$6156         
6152: 3E 09      LD      A,$09           
6154: E0 F2      LDFF00  ($F2),A         
6156: E1         POP     HL              
6157: F1         POP     AF              
6158: 77         LD      (HL),A          
6159: 21 40 C2   LD      HL,$C240        
615C: 09         ADD     HL,BC           
615D: 7E         LD      A,(HL)          
615E: CB 2F      SET     1,E             
6160: FE FF      CP      $FF             
6162: 20 01      JR      NZ,$6165        
6164: AF         XOR     A               
6165: 77         LD      (HL),A          
6166: F0 F9      LD      A,($F9)         
6168: A7         AND     A               
6169: 20 0D      JR      NZ,$6178        
616B: 21 50 C2   LD      HL,$C250        
616E: 09         ADD     HL,BC           
616F: 7E         LD      A,(HL)          
6170: CB 2F      SET     1,E             
6172: FE FF      CP      $FF             
6174: 20 01      JR      NZ,$6177        
6176: AF         XOR     A               
6177: 77         LD      (HL),A          
6178: C9         RET                     
6179: 20 20      JR      NZ,$619B        
617B: 20 00      JR      NZ,$617D        
617D: CD 03 62   CALL    $6203           
6180: CD AC 60   CALL    $60AC           
6183: 11 79 61   LD      DE,$6179        
6186: CD D0 3C   CALL    $3CD0           
6189: CD 4A 7F   CALL    $7F4A           
618C: CD D4 62   CALL    $62D4           
618F: CD 10 63   CALL    $6310           
6192: 21 40 C2   LD      HL,$C240        
6195: 09         ADD     HL,BC           
6196: 7E         LD      A,(HL)          
6197: 07         RLCA                    
6198: E6 01      AND     $01             
619A: CD 87 3B   CALL    $3B87           
619D: CD F7 7E   CALL    $7EF7           
61A0: CD E5 61   CALL    $61E5           
61A3: CD 92 78   CALL    $7892           
61A6: CD AB 7E   CALL    $7EAB           
61A9: 7A         LD      A,D             
61AA: CB 7F      SET     1,E             
61AC: 28 00      JR      Z,$61AE         
61AE: FE 20      CP      $20             
61B0: 38 0C      JR      C,$61BE         
61B2: CD BB 7E   CALL    $7EBB           
61B5: 7A         LD      A,D             
61B6: CB 7F      SET     1,E             
61B8: 28 00      JR      Z,$61BA         
61BA: FE 20      CP      $20             
61BC: 30 21      JR      NC,$61DF        
61BE: CD 91 08   CALL    $0891           
61C1: 20 21      JR      NZ,$61E4        
61C3: 36 30      LD      (HL),$30        
61C5: CD ED 27   CALL    $27ED           
61C8: E6 0F      AND     $0F             
61CA: D6 08      SUB     $08             
61CC: 21 40 C2   LD      HL,$C240        
61CF: 09         ADD     HL,BC           
61D0: 77         LD      (HL),A          
61D1: CD ED 27   CALL    $27ED           
61D4: E6 0F      AND     $0F             
61D6: D6 08      SUB     $08             
61D8: 21 50 C2   LD      HL,$C250        
61DB: 09         ADD     HL,BC           
61DC: 77         LD      (HL),A          
61DD: 18 05      JR      $61E4           
61DF: 3E 09      LD      A,$09           
61E1: CD 99 7E   CALL    $7E99           
61E4: C9         RET                     
61E5: F0 E7      LD      A,($E7)         
61E7: E6 03      AND     $03             
61E9: 20 17      JR      NZ,$6202        
61EB: 21 10 C3   LD      HL,$C310        
61EE: 09         ADD     HL,BC           
61EF: 7E         LD      A,(HL)          
61F0: FE 10      CP      $10             
61F2: 28 0E      JR      Z,$6202         
61F4: CB 7F      SET     1,E             
61F6: 28 03      JR      Z,$61FB         
61F8: 34         INC     (HL)            
61F9: 18 07      JR      $6202           
61FB: FE 10      CP      $10             
61FD: 30 02      JR      NC,$6201        
61FF: 34         INC     (HL)            
6200: C9         RET                     
6201: 35         DEC     (HL)            
6202: C9         RET                     
6203: 21 D0 C2   LD      HL,$C2D0        
6206: 09         ADD     HL,BC           
6207: 7E         LD      A,(HL)          
6208: A7         AND     A               
6209: CA C2 62   JP      Z,$62C2         
620C: FA 24 C1   LD      A,($C124)       
620F: A7         AND     A               
6210: C2 C1 62   JP      NZ,$62C1        
6213: 7E         LD      A,(HL)          
6214: FE 02      CP      $02             
6216: 20 50      JR      NZ,$6268        
6218: F0 EB      LD      A,($EB)         
621A: FE 3D      CP      $3D             
621C: 28 07      JR      Z,$6225         
621E: FA A5 DB   LD      A,($DBA5)       
6221: A7         AND     A               
6222: C2 C1 62   JP      NZ,$62C1        
6225: CD E0 7D   CALL    $7DE0           
6228: F0 EB      LD      A,($EB)         
622A: FE 2D      CP      $2D             
622C: 28 1E      JR      Z,$624C         
622E: FE 3D      CP      $3D             
6230: 20 22      JR      NZ,$6254        
6232: F0 F6      LD      A,($F6)         
6234: FE DA      CP      $DA             
6236: 28 1C      JR      Z,$6254         
6238: FE A5      CP      $A5             
623A: 28 18      JR      Z,$6254         
623C: FE 74      CP      $74             
623E: 28 14      JR      Z,$6254         
6240: FE 3A      CP      $3A             
6242: 28 10      JR      Z,$6254         
6244: FE A8      CP      $A8             
6246: 28 0C      JR      Z,$6254         
6248: FE B2      CP      $B2             
624A: 28 08      JR      Z,$6254         
624C: F0 AF      LD      A,($AF)         
624E: FE 04      CP      $04             
6250: 28 0E      JR      Z,$6260         
6252: 18 06      JR      $625A           
6254: 21 40 C4   LD      HL,$C440        
6257: 09         ADD     HL,BC           
6258: 36 01      LD      (HL),$01        
625A: F0 AF      LD      A,($AF)         
625C: FE CC      CP      $CC             
625E: 20 61      JR      NZ,$62C1        
6260: 21 30 C4   LD      HL,$C430        
6263: 09         ADD     HL,BC           
6264: 36 0A      LD      (HL),$0A        
6266: 18 28      JR      $6290           
6268: FA 57 C1   LD      A,($C157)       
626B: A7         AND     A               
626C: 28 53      JR      Z,$62C1         
626E: FA 78 C1   LD      A,($C178)       
6271: A7         AND     A               
6272: 28 4D      JR      Z,$62C1         
6274: F0 EE      LD      A,($EE)         
6276: C6 08      ADD     $08             
6278: 21 79 C1   LD      HL,$C179        
627B: 96         SUB     (HL)            
627C: C6 10      ADD     $10             
627E: FE 20      CP      $20             
6280: 30 3F      JR      NC,$62C1        
6282: F0 EF      LD      A,($EF)         
6284: C6 08      ADD     $08             
6286: 21 7A C1   LD      HL,$C17A        
6289: 96         SUB     (HL)            
628A: C6 10      ADD     $10             
628C: FE 20      CP      $20             
628E: 30 31      JR      NC,$62C1        
6290: 21 D0 C2   LD      HL,$C2D0        
6293: 09         ADD     HL,BC           
6294: 70         LD      (HL),B          
6295: 21 40 C4   LD      HL,$C440        
6298: 09         ADD     HL,BC           
6299: 70         LD      (HL),B          
629A: CD 8C 08   CALL    $088C           
629D: 36 18      LD      (HL),$18        
629F: 3E 0C      LD      A,$0C           
62A1: CD 17 7E   CALL    $7E17           
62A4: F0 D8      LD      A,($D8)         
62A6: 2F         CPL                     
62A7: 3C         INC     A               
62A8: 21 40 C2   LD      HL,$C240        
62AB: 09         ADD     HL,BC           
62AC: 77         LD      (HL),A          
62AD: F0 D7      LD      A,($D7)         
62AF: 2F         CPL                     
62B0: 3C         INC     A               
62B1: 21 50 C2   LD      HL,$C250        
62B4: 09         ADD     HL,BC           
62B5: 77         LD      (HL),A          
62B6: 21 20 C3   LD      HL,$C320        
62B9: 09         ADD     HL,BC           
62BA: 36 20      LD      (HL),$20        
62BC: CD 87 08   CALL    $0887           
62BF: 36 80      LD      (HL),$80        
62C1: F1         POP     AF              
62C2: C9         RET                     
62C3: 01 01 00   LD      BC,$0001        
62C6: 00         NOP                     
62C7: 01 00 01   LD      BC,$0100        
62CA: 01 00 00   LD      BC,$0000        
62CD: 01 01 00   LD      BC,$0001        
62D0: 00         NOP                     
62D1: 01 00 00   LD      BC,$0000        
62D4: 21 90 C3   LD      HL,$C390        
62D7: 09         ADD     HL,BC           
62D8: 7E         LD      A,(HL)          
62D9: A7         AND     A               
62DA: 28 33      JR      Z,$630F         
62DC: D1         POP     DE              
62DD: 3D         DEC     A               
62DE: 5F         LD      E,A             
62DF: 50         LD      D,B             
62E0: 21 80 C2   LD      HL,$C280        
62E3: 19         ADD     HL,DE           
62E4: 7E         LD      A,(HL)          
62E5: A7         AND     A               
62E6: 28 4E      JR      Z,$6336         
62E8: 21 A0 C3   LD      HL,$C3A0        
62EB: 19         ADD     HL,DE           
62EC: 7E         LD      A,(HL)          
62ED: FE 01      CP      $01             
62EF: 28 04      JR      Z,$62F5         
62F1: FE 03      CP      $03             
62F3: 20 41      JR      NZ,$6336        
62F5: 21 00 C2   LD      HL,$C200        
62F8: 19         ADD     HL,DE           
62F9: 7E         LD      A,(HL)          
62FA: 21 00 C2   LD      HL,$C200        
62FD: 09         ADD     HL,BC           
62FE: 77         LD      (HL),A          
62FF: 21 10 C2   LD      HL,$C210        
6302: 19         ADD     HL,DE           
6303: 7E         LD      A,(HL)          
6304: 21 10 C2   LD      HL,$C210        
6307: 09         ADD     HL,BC           
6308: 77         LD      (HL),A          
6309: AF         XOR     A               
630A: 21 10 C3   LD      HL,$C310        
630D: 09         ADD     HL,BC           
630E: 77         LD      (HL),A          
630F: C9         RET                     
6310: CD 8C 08   CALL    $088C           
6313: 20 FA      JR      NZ,$630F        
6315: F0 EB      LD      A,($EB)         
6317: D6 2D      SUB     $2D             
6319: 5F         LD      E,A             
631A: 50         LD      D,B             
631B: 21 C3 62   LD      HL,$62C3        
631E: 19         ADD     HL,DE           
631F: 7E         LD      A,(HL)          
6320: A7         AND     A               
6321: 28 0E      JR      Z,$6331         
6323: 21 10 C4   LD      HL,$C410        
6326: 09         ADD     HL,BC           
6327: 7E         LD      A,(HL)          
6328: F5         PUSH    AF              
6329: E5         PUSH    HL              
632A: 70         LD      (HL),B          
632B: CD 40 6E   CALL    $6E40           
632E: E1         POP     HL              
632F: F1         POP     AF              
6330: 77         LD      (HL),A          
6331: CD 87 6C   CALL    $6C87           
6334: 30 D9      JR      NC,$630F        
6336: 21 60 C4   LD      HL,$C460        
6339: 09         ADD     HL,BC           
633A: 7E         LD      A,(HL)          
633B: CD A2 3F   CALL    $3FA2           
633E: F0 EB      LD      A,($EB)         
6340: D6 2D      SUB     $2D             
6342: FE 02      CP      $02             
6344: 30 07      JR      NC,$634D        
6346: 21 F2 FF   LD      HL,$FFF2        
6349: 36 14      LD      (HL),$14        
634B: 18 05      JR      $6352           
634D: 21 F3 FF   LD      HL,$FFF3        
6350: 36 01      LD      (HL),$01        
6352: C7         RST     0X00            
6353: E5         PUSH    HL              
6354: 64         LD      H,H             
6355: ED                              
6356: 64         LD      H,H             
6357: F4                              
6358: 64         LD      H,H             
6359: B4         OR      H               
635A: 64         LD      H,H             
635B: 72         LD      (HL),D          
635C: 64         LD      H,H             
635D: 71         LD      (HL),C          
635E: 64         LD      H,H             
635F: 21 64 1B   LD      HL,$1B64        
6362: 64         LD      H,H             
6363: 09         ADD     HL,BC           
6364: 64         LD      H,H             
6365: D5         PUSH    DE              
6366: 63         LD      H,E             
6367: A2         AND     D               
6368: 63         LD      H,E             
6369: AA         XOR     D               
636A: 63         LD      H,E             
636B: B7         OR      A               
636C: 63         LD      H,E             
636D: EC                              
636E: 63         LD      H,E             
636F: 75         LD      (HL),L          
6370: 63         LD      H,E             
6371: EC                              
6372: 63         LD      H,E             
6373: 8D         ADC     A,L             
6374: 63         LD      H,E             
6375: 3E 0B      LD      A,$0B           
6377: E0 A5      LDFF00  ($A5),A         
6379: 16 0C      LD      D,$0C           
637B: CD 97 64   CALL    $6497           
637E: 21 76 DB   LD      HL,$DB76        
6381: 11 4C DB   LD      DE,$DB4C        
6384: 1A         LD      A,(DE)          
6385: BE         CP      (HL)            
6386: 30 04      JR      NC,$638C        
6388: C6 01      ADD     $01             
638A: 27         DAA                     
638B: 12         LD      (DE),A          
638C: C9         RET                     
638D: 3E EF      LD      A,$EF           
638F: CD 97 21   CALL    $2197           
6392: CD D8 51   CALL    $51D8           
6395: 21 0F DB   LD      HL,$DB0F        
6398: 7E         LD      A,(HL)          
6399: FE 99      CP      $99             
639B: 28 04      JR      Z,$63A1         
639D: C6 01      ADD     $01             
639F: 27         DAA                     
63A0: 77         LD      (HL),A          
63A1: C9         RET                     
63A2: 21 78 DB   LD      HL,$DB78        
63A5: 11 45 DB   LD      DE,$DB45        
63A8: 18 DA      JR      $6384           
63AA: 16 02      LD      D,$02           
63AC: CD 97 64   CALL    $6497           
63AF: 21 77 DB   LD      HL,$DB77        
63B2: 11 4D DB   LD      DE,$DB4D        
63B5: 18 CD      JR      $6384           
63B7: AF         XOR     A               
63B8: EA 6C D4   LD      ($D46C),A       
63BB: EA CB C3   LD      ($C3CB),A       
63BE: 3E 1B      LD      A,$1B           
63C0: EA 68 D3   LD      ($D368),A       
63C3: EA 67 C1   LD      ($C167),A       
63C6: F0 98      LD      A,($98)         
63C8: F5         PUSH    AF              
63C9: C6 04      ADD     $04             
63CB: E0 98      LDFF00  ($98),A         
63CD: CD 43 64   CALL    $6443           
63D0: F1         POP     AF              
63D1: E0 98      LDFF00  ($98),A         
63D3: 18 22      JR      $63F7           
63D5: AF         XOR     A               
63D6: EA 7C D4   LD      ($D47C),A       
63D9: 3E 25      LD      A,$25           
63DB: EA 68 D3   LD      ($D368),A       
63DE: EA 6C D4   LD      ($D46C),A       
63E1: CD 91 08   CALL    $0891           
63E4: 3E 70      LD      A,$70           
63E6: 77         LD      (HL),A          
63E7: EA 11 C1   LD      ($C111),A       
63EA: 18 14      JR      $6400           
63EC: 3E 10      LD      A,$10           
63EE: EA 68 D3   LD      ($D368),A       
63F1: 18 04      JR      $63F7           
63F3: 3E 01      LD      A,$01           
63F5: E0 F2      LDFF00  ($F2),A         
63F7: CD 91 08   CALL    $0891           
63FA: 3E 68      LD      A,$68           
63FC: 77         LD      (HL),A          
63FD: EA 11 C1   LD      ($C111),A       
6400: 21 80 C2   LD      HL,$C280        
6403: 09         ADD     HL,BC           
6404: 36 05      LD      (HL),$05        
6406: C3 3B 09   JP      $093B           
6409: 3E 10      LD      A,$10           
640B: EA 68 D3   LD      ($D368),A       
640E: CD 8D 3B   CALL    $3B8D           
6411: 18 ED      JR      $6400           
6413: E4                              
6414: 14         INC     D               
6415: E4                              
6416: 14         INC     D               
6417: D4 D4 04   CALL    NC,$04D4        
641A: 04         INC     B               
641B: 3E 02      LD      A,$02           
641D: 1E 05      LD      E,$05           
641F: 18 04      JR      $6425           
6421: 3E 01      LD      A,$01           
6423: 1E 01      LD      E,$01           
6425: EA 7C D4   LD      ($D47C),A       
6428: 7B         LD      A,E             
6429: EA A9 C1   LD      ($C1A9),A       
642C: 3E 30      LD      A,$30           
642E: EA AA C1   LD      ($C1AA),A       
6431: EA 11 C1   LD      ($C111),A       
6434: AF         XOR     A               
6435: EA 7A D4   LD      ($D47A),A       
6438: 3E 27      LD      A,$27           
643A: EA 68 D3   LD      ($D368),A       
643D: 3E 49      LD      A,$49           
643F: E0 BD      LDFF00  ($BD),A         
6441: E0 BF      LDFF00  ($BF),A         
6443: 1E 03      LD      E,$03           
6445: 16 00      LD      D,$00           
6447: D5         PUSH    DE              
6448: 21 13 64   LD      HL,$6413        
644B: 19         ADD     HL,DE           
644C: F0 98      LD      A,($98)         
644E: 86         ADD     A,(HL)          
644F: E0 D7      LDFF00  ($D7),A         
6451: 21 17 64   LD      HL,$6417        
6454: 19         ADD     HL,DE           
6455: F0 99      LD      A,($99)         
6457: 86         ADD     A,(HL)          
6458: E0 D8      LDFF00  ($D8),A         
645A: 3E 07      LD      A,$07           
645C: CD 53 09   CALL    $0953           
645F: 21 20 C5   LD      HL,$C520        
6462: 19         ADD     HL,DE           
6463: 36 22      LD      (HL),$22        
6465: 21 90 C5   LD      HL,$C590        
6468: 19         ADD     HL,DE           
6469: D1         POP     DE              
646A: 73         LD      (HL),E          
646B: 1D         DEC     E               
646C: 7B         LD      A,E             
646D: FE FF      CP      $FF             
646F: 20 D6      JR      NZ,$6447        
6471: C9         RET                     
6472: FA 4E DB   LD      A,($DB4E)       
6475: A7         AND     A               
6476: 20 15      JR      NZ,$648D        
6478: 3E 0F      LD      A,$0F           
647A: EA 68 D3   LD      ($D368),A       
647D: EA 67 C1   LD      ($C167),A       
6480: CD C6 63   CALL    $63C6           
6483: CD 91 08   CALL    $0891           
6486: 36 A0      LD      (HL),$A0        
6488: 3E FF      LD      A,$FF           
648A: E0 BF      LDFF00  ($BF),A         
648C: C9         RET                     
648D: 21 B0 C2   LD      HL,$C2B0        
6490: 09         ADD     HL,BC           
6491: 7E         LD      A,(HL)          
6492: EA 44 DB   LD      ($DB44),A       
6495: 16 04      LD      D,$04           
6497: 21 00 DB   LD      HL,$DB00        
649A: 1E 0C      LD      E,$0C           
649C: 2A         LD      A,(HLI)         
649D: BA         CP      D               
649E: 28 13      JR      Z,$64B3         
64A0: 1D         DEC     E               
64A1: 20 F9      JR      NZ,$649C        
64A3: 21 00 DB   LD      HL,$DB00        
64A6: 7E         LD      A,(HL)          
64A7: A7         AND     A               
64A8: 20 02      JR      NZ,$64AC        
64AA: 72         LD      (HL),D          
64AB: C9         RET                     
64AC: 23         INC     HL              
64AD: 1C         INC     E               
64AE: 7B         LD      A,E             
64AF: FE 0C      CP      $0C             
64B1: 20 F3      JR      NZ,$64A6        
64B3: C9         RET                     
64B4: F0 F6      LD      A,($F6)         
64B6: FE 80      CP      $80             
64B8: 20 08      JR      NZ,$64C2        
64BA: 3E 10      LD      A,$10           
64BC: EA 68 D3   LD      ($D368),A       
64BF: C3 F7 63   JP      $63F7           
64C2: F0 F6      LD      A,($F6)         
64C4: FE 7C      CP      $7C             
64C6: 20 05      JR      NZ,$64CD        
64C8: 21 69 D9   LD      HL,$D969        
64CB: CB E6      SET     1,E             
64CD: F0 F1      LD      A,($F1)         
64CF: A7         AND     A               
64D0: 28 08      JR      Z,$64DA         
64D2: 3E 10      LD      A,$10           
64D4: EA 68 D3   LD      ($D368),A       
64D7: C3 F7 63   JP      $63F7           
64DA: CD D8 51   CALL    $51D8           
64DD: 21 D0 DB   LD      HL,$DBD0        
64E0: 34         INC     (HL)            
64E1: CD E2 27   CALL    $27E2           
64E4: C9         RET                     
64E5: 3E 08      LD      A,$08           
64E7: 21 93 DB   LD      HL,$DB93        
64EA: 86         ADD     A,(HL)          
64EB: 77         LD      (HL),A          
64EC: C9         RET                     
64ED: 3E 01      LD      A,$01           
64EF: 21 90 DB   LD      HL,$DB90        
64F2: 18 F6      JR      $64EA           
64F4: 3E 30      LD      A,$30           
64F6: 18 EF      JR      $64E7           
64F8: 1E 0F      LD      E,$0F           
64FA: F5         PUSH    AF              
64FB: 16 00      LD      D,$00           
64FD: 21 80 C2   LD      HL,$C280        
6500: 19         ADD     HL,DE           
6501: 7E         LD      A,(HL)          
6502: A7         AND     A               
6503: 28 09      JR      Z,$650E         
6505: 1D         DEC     E               
6506: 7B         LD      A,E             
6507: FE FF      CP      $FF             
6509: 20 F2      JR      NZ,$64FD        
650B: F1         POP     AF              
650C: 37         SCF                     
650D: C9         RET                     
650E: 36 05      LD      (HL),$05        
6510: F1         POP     AF              
6511: 21 A0 C3   LD      HL,$C3A0        
6514: 19         ADD     HL,DE           
6515: 77         LD      (HL),A          
6516: 21 00 C2   LD      HL,$C200        
6519: 09         ADD     HL,BC           
651A: 7E         LD      A,(HL)          
651B: E0 D7      LDFF00  ($D7),A         
651D: 21 10 C2   LD      HL,$C210        
6520: 09         ADD     HL,BC           
6521: 7E         LD      A,(HL)          
6522: E0 D8      LDFF00  ($D8),A         
6524: 21 80 C3   LD      HL,$C380        
6527: 09         ADD     HL,BC           
6528: 7E         LD      A,(HL)          
6529: E0 D9      LDFF00  ($D9),A         
652B: 21 10 C3   LD      HL,$C310        
652E: 09         ADD     HL,BC           
652F: 7E         LD      A,(HL)          
6530: E0 DA      LDFF00  ($DA),A         
6532: CD 52 65   CALL    $6552           
6535: 21 10 C4   LD      HL,$C410        
6538: 19         ADD     HL,DE           
6539: 36 01      LD      (HL),$01        
653B: 21 20 C2   LD      HL,$C220        
653E: 09         ADD     HL,BC           
653F: 7E         LD      A,(HL)          
6540: 21 20 C2   LD      HL,$C220        
6543: 19         ADD     HL,DE           
6544: 77         LD      (HL),A          
6545: 21 30 C2   LD      HL,$C230        
6548: 09         ADD     HL,BC           
6549: 7E         LD      A,(HL)          
654A: 21 30 C2   LD      HL,$C230        
654D: 19         ADD     HL,DE           
654E: 77         LD      (HL),A          
654F: 37         SCF                     
6550: 3F         CCF                     
6551: C9         RET                     
6552: C5         PUSH    BC              
6553: D5         PUSH    DE              
6554: D5         PUSH    DE              
6555: C1         POP     BC              
6556: CD B0 48   CALL    $48B0           
6559: D1         POP     DE              
655A: C1         POP     BC              
655B: C9         RET                     
655C: 80         ADD     A,B             
655D: 10 F8      STOP    $F8             
655F: F8 32      LDHL    SP,$32          
6561: 00         NOP                     
6562: F8 00      LDHL    SP,$00          
6564: 32         LD      (HLD),A         
6565: 20 F8      JR      NZ,$655F        
6567: 08 32 00   LD      ($0032),SP      
656A: F8 10      LDHL    SP,$10          
656C: 32         LD      (HLD),A         
656D: 20 08      JR      NZ,$6577        
656F: F8 32      LDHL    SP,$32          
6571: 00         NOP                     
6572: 08 00 32   LD      ($3200),SP      
6575: 20 08      JR      NZ,$657F        
6577: 08 32 00   LD      ($0032),SP      
657A: 08 10 32   LD      ($3210),SP      
657D: 20 F8      JR      NZ,$6577        
657F: F8 10      LDHL    SP,$10          
6581: 00         NOP                     
6582: F8 00      LDHL    SP,$00          
6584: 12         LD      (DE),A          
6585: 00         NOP                     
6586: F8 08      LDHL    SP,$08          
6588: 12         LD      (DE),A          
6589: 20 F8      JR      NZ,$6583        
658B: 10 10      STOP    $10             
658D: 20 08      JR      NZ,$6597        
658F: F8 10      LDHL    SP,$10          
6591: 40         LD      B,B             
6592: 08 00 12   LD      ($1200),SP      
6595: 40         LD      B,B             
6596: 08 08 12   LD      ($1208),SP      
6599: 60         LD      H,B             
659A: 08 10 10   LD      ($1010),SP      
659D: 60         LD      H,B             
659E: FC                              
659F: FC                              
65A0: 30 10      JR      NC,$65B2        
65A2: FC                              
65A3: 04         INC     B               
65A4: 30 30      JR      NC,$65D6        
65A6: FC                              
65A7: 04         INC     B               
65A8: 30 10      JR      NC,$65BA        
65AA: FC                              
65AB: 0C         INC     C               
65AC: 30 30      JR      NC,$65DE        
65AE: 04         INC     B               
65AF: FC                              
65B0: 30 10      JR      NC,$65C2        
65B2: 04         INC     B               
65B3: 04         INC     B               
65B4: 30 30      JR      NC,$65E6        
65B6: 04         INC     B               
65B7: 04         INC     B               
65B8: 30 10      JR      NC,$65CA        
65BA: 04         INC     B               
65BB: 0C         INC     C               
65BC: 30 30      JR      NC,$65EE        
65BE: FC                              
65BF: FC                              
65C0: 30 00      JR      NC,$65C2        
65C2: FC                              
65C3: 04         INC     B               
65C4: 30 20      JR      NC,$65E6        
65C6: FC                              
65C7: 04         INC     B               
65C8: 30 00      JR      NC,$65CA        
65CA: FC                              
65CB: 0C         INC     C               
65CC: 30 20      JR      NC,$65EE        
65CE: 04         INC     B               
65CF: FC                              
65D0: 30 00      JR      NC,$65D2        
65D2: 04         INC     B               
65D3: 04         INC     B               
65D4: 30 20      JR      NC,$65F6        
65D6: 04         INC     B               
65D7: 04         INC     B               
65D8: 30 00      JR      NC,$65DA        
65DA: 04         INC     B               
65DB: 0C         INC     C               
65DC: 30 20      JR      NC,$65FE        
65DE: 21 B0 C3   LD      HL,$C3B0        
65E1: 09         ADD     HL,BC           
65E2: 7E         LD      A,(HL)          
65E3: CB 27      SET     1,E             
65E5: CB 27      SET     1,E             
65E7: CB 27      SET     1,E             
65E9: CB 27      SET     1,E             
65EB: CB 27      SET     1,E             
65ED: 5F         LD      E,A             
65EE: 50         LD      D,B             
65EF: 21 5E 65   LD      HL,$655E        
65F2: 19         ADD     HL,DE           
65F3: 0E 08      LD      C,$08           
65F5: CD 26 3D   CALL    $3D26           
65F8: C9         RET                     
65F9: 00         NOP                     
65FA: 00         NOP                     
65FB: 00         NOP                     
65FC: 00         NOP                     
65FD: 00         NOP                     
65FE: 00         NOP                     
65FF: 00         NOP                     
6600: 00         NOP                     
6601: 01 01 01   LD      BC,$0101        
6604: 01 01 01   LD      BC,$0101        
6607: 01 01 02   LD      BC,$0201        
660A: 02         LD      (BC),A          
660B: 02         LD      (BC),A          
660C: 02         LD      (BC),A          
660D: 03         INC     BC              
660E: 03         INC     BC              
660F: 03         INC     BC              
6610: 03         INC     BC              
6611: CD 7F 66   CALL    $667F           
6614: CD 4A 7F   CALL    $7F4A           
6617: CD 91 08   CALL    $0891           
661A: A7         AND     A               
661B: C2 21 66   JP      NZ,$6621        
661E: C3 B7 3F   JP      $3FB7           
6621: 5F         LD      E,A             
6622: 21 40 C4   LD      HL,$C440        
6625: 09         ADD     HL,BC           
6626: 7E         LD      A,(HL)          
6627: FE 4C      CP      $4C             
6629: 7B         LD      A,E             
662A: CA 7E 66   JP      Z,$667E         
662D: FE 0E      CP      $0E             
662F: 38 12      JR      C,$6643         
6631: FE 17      CP      $17             
6633: 30 0E      JR      NC,$6643        
6635: F5         PUSH    AF              
6636: D6 0E      SUB     $0E             
6638: 5F         LD      E,A             
6639: 50         LD      D,B             
663A: D5         PUSH    DE              
663B: CD 1C 69   CALL    $691C           
663E: D1         POP     DE              
663F: CD 8D 67   CALL    $678D           
6642: F1         POP     AF              
6643: FE 12      CP      $12             
6645: 20 37      JR      NZ,$667E        
6647: 21 40 C4   LD      HL,$C440        
664A: 09         ADD     HL,BC           
664B: 7E         LD      A,(HL)          
664C: A7         AND     A               
664D: 20 05      JR      NZ,$6654        
664F: CD D8 77   CALL    $77D8           
6652: 18 25      JR      $6679           
6654: F0 EE      LD      A,($EE)         
6656: 21 98 FF   LD      HL,$FF98        
6659: 96         SUB     (HL)            
665A: C6 18      ADD     $18             
665C: FE 30      CP      $30             
665E: 30 19      JR      NC,$6679        
6660: F0 EF      LD      A,($EF)         
6662: 21 99 FF   LD      HL,$FF99        
6665: 96         SUB     (HL)            
6666: C6 18      ADD     $18             
6668: FE 30      CP      $30             
666A: 30 0D      JR      NC,$6679        
666C: CD F1 6C   CALL    $6CF1           
666F: 21 9A FF   LD      HL,$FF9A        
6672: CB 26      SET     1,E             
6674: 21 9B FF   LD      HL,$FF9B        
6677: CB 26      SET     1,E             
6679: 3E 04      LD      A,$04           
667B: EA 02 C5   LD      ($C502),A       
667E: C9         RET                     
667F: CD 91 08   CALL    $0891           
6682: 5F         LD      E,A             
6683: 50         LD      D,B             
6684: 21 F9 65   LD      HL,$65F9        
6687: 19         ADD     HL,DE           
6688: 7E         LD      A,(HL)          
6689: CD 87 3B   CALL    $3B87           
668C: 21 40 C3   LD      HL,$C340        
668F: 09         ADD     HL,BC           
6690: 7E         LD      A,(HL)          
6691: E6 F0      AND     $F0             
6693: F6 08      OR      $08             
6695: 77         LD      (HL),A          
6696: CD DE 65   CALL    $65DE           
6699: FA A5 DB   LD      A,($DBA5)       
669C: A7         AND     A               
669D: 28 15      JR      Z,$66B4         
669F: 1E E4      LD      E,$E4           
66A1: FA 24 C1   LD      A,($C124)       
66A4: A7         AND     A               
66A5: 20 09      JR      NZ,$66B0        
66A7: CD 91 08   CALL    $0891           
66AA: E6 04      AND     $04             
66AC: 28 02      JR      Z,$66B0         
66AE: 1E 84      LD      E,$84           
66B0: 21 97 DB   LD      HL,$DB97        
66B3: 73         LD      (HL),E          
66B4: C9         RET                     
66B5: 11 EA 54   LD      DE,$54EA        
66B8: CD 3B 3C   CALL    $3C3B           
66BB: CD 4A 7F   CALL    $7F4A           
66BE: C9         RET                     
66BF: F0 EC      LD      A,($EC)         
66C1: C6 10      ADD     $10             
66C3: FE A0      CP      $A0             
66C5: D2 B7 3F   JP      NC,$3FB7        
66C8: CD 91 08   CALL    $0891           
66CB: FE 18      CP      $18             
66CD: DA 11 66   JP      C,$6611         
66D0: 20 04      JR      NZ,$66D6        
66D2: 35         DEC     (HL)            
66D3: CD D7 08   CALL    $08D7           
66D6: 21 4E C1   LD      HL,$C14E        
66D9: 34         INC     (HL)            
66DA: FE 22      CP      $22             
66DC: 38 D7      JR      C,$66B5         
66DE: FE 48      CP      $48             
66E0: 20 06      JR      NZ,$66E8        
66E2: 21 20 C4   LD      HL,$C420        
66E5: 09         ADD     HL,BC           
66E6: 36 30      LD      (HL),$30        
66E8: CD 3D 67   CALL    $673D           
66EB: CD 31 5D   CALL    $5D31           
66EE: CD 4A 7F   CALL    $7F4A           
66F1: CD D5 60   CALL    $60D5           
66F4: 21 00 C3   LD      HL,$C300        
66F7: 09         ADD     HL,BC           
66F8: 36 FF      LD      (HL),$FF        
66FA: CD 8C 08   CALL    $088C           
66FD: 21 40 C4   LD      HL,$C440        
6700: 09         ADD     HL,BC           
6701: B6         OR      (HL)            
6702: 20 1F      JR      NZ,$6723        
6704: FA 00 DB   LD      A,($DB00)       
6707: FE 02      CP      $02             
6709: 20 08      JR      NZ,$6713        
670B: F0 CC      LD      A,($CC)         
670D: E6 20      AND     $20             
670F: 20 0F      JR      NZ,$6720        
6711: 18 10      JR      $6723           
6713: FA 01 DB   LD      A,($DB01)       
6716: FE 02      CP      $02             
6718: 20 09      JR      NZ,$6723        
671A: F0 CC      LD      A,($CC)         
671C: E6 10      AND     $10             
671E: 28 03      JR      Z,$6723         
6720: CD EA 4E   CALL    $4EEA           
6723: 21 A0 C2   LD      HL,$C2A0        
6726: 09         ADD     HL,BC           
6727: 7E         LD      A,(HL)          
6728: E6 03      AND     $03             
672A: 28 03      JR      Z,$672F         
672C: CD 4F 6B   CALL    $6B4F           
672F: F0 F9      LD      A,($F9)         
6731: A7         AND     A               
6732: 20 08      JR      NZ,$673C        
6734: 7E         LD      A,(HL)          
6735: E6 0C      AND     $0C             
6737: 28 03      JR      Z,$673C         
6739: CD 5E 6B   CALL    $6B5E           
673C: C9         RET                     
673D: 21 EC FF   LD      HL,$FFEC        
6740: 34         INC     (HL)            
6741: 34         INC     (HL)            
6742: 11 5C 65   LD      DE,$655C        
6745: CD D0 3C   CALL    $3CD0           
6748: C3 BA 3D   JP      $3DBA           
674B: F8 08      LDHL    SP,$08          
674D: 18 F8      JR      $6747           
674F: 08 18 F8   LD      ($F818),SP      
6752: 08 18 F8   LD      ($F818),SP      
6755: F8 F8      LDHL    SP,$F8          
6757: 08 08 08   LD      ($0808),SP      
675A: 18 18      JR      $6774           
675C: 18 48      JR      $67A6           
675E: 48         LD      C,B             
675F: 00         NOP                     
6760: 90         SUB     B               
6761: 00         NOP                     
6762: 70         LD      (HL),B          
6763: 38 38      JR      C,$679D         
6765: 3D         DEC     A               
6766: 3D         DEC     A               
6767: 3E 3E      LD      A,$3E           
6769: 72         LD      (HL),D          
676A: 72         LD      (HL),D          
676B: 73         LD      (HL),E          
676C: 73         LD      (HL),E          
676D: 69         LD      L,C             
676E: 79         LD      A,C             
676F: 69         LD      L,C             
6770: 79         LD      A,C             
6771: 64         LD      H,H             
6772: 66         LD      H,(HL)          
6773: 65         LD      H,L             
6774: 67         LD      H,A             
6775: 04         INC     B               
6776: 08 02 01   LD      ($0102),SP      
6779: 08 04 01   LD      ($0104),SP      
677C: 02         LD      (BC),A          
677D: F8 08      LDHL    SP,$08          
677F: FF         RST     0X38            
6780: 01 72 73   LD      BC,$7372        
6783: 73         LD      (HL),E          
6784: 72         LD      (HL),D          
6785: 00         NOP                     
6786: 10 F0      STOP    $F0             
6788: 10 00      STOP    $00             
678A: 00         NOP                     
678B: 10 00      STOP    $00             
678D: F0 F9      LD      A,($F9)         
678F: A7         AND     A               
6790: C2 C5 68   JP      NZ,$68C5        
6793: C5         PUSH    BC              
6794: 21 00 C2   LD      HL,$C200        
6797: 09         ADD     HL,BC           
6798: 7E         LD      A,(HL)          
6799: D6 08      SUB     $08             
679B: 21 4B 67   LD      HL,$674B        
679E: 19         ADD     HL,DE           
679F: 86         ADD     A,(HL)          
67A0: E6 F0      AND     $F0             
67A2: E0 CE      LDFF00  ($CE),A         
67A4: CB 37      SET     1,E             
67A6: 21 10 C2   LD      HL,$C210        
67A9: 09         ADD     HL,BC           
67AA: 4F         LD      C,A             
67AB: 7E         LD      A,(HL)          
67AC: D6 10      SUB     $10             
67AE: 21 54 67   LD      HL,$6754        
67B1: 19         ADD     HL,DE           
67B2: 86         ADD     A,(HL)          
67B3: E6 F0      AND     $F0             
67B5: E0 CD      LDFF00  ($CD),A         
67B7: B1         OR      C               
67B8: 4F         LD      C,A             
67B9: 06 00      LD      B,$00           
67BB: 21 11 D7   LD      HL,$D711        
67BE: 7C         LD      A,H             
67BF: 09         ADD     HL,BC           
67C0: 67         LD      H,A             
67C1: 79         LD      A,C             
67C2: E0 E9      LDFF00  ($E9),A         
67C4: 7E         LD      A,(HL)          
67C5: E0 AF      LDFF00  ($AF),A         
67C7: 5F         LD      E,A             
67C8: FE BB      CP      $BB             
67CA: 38 5C      JR      C,$6828         
67CC: FE BF      CP      $BF             
67CE: 30 58      JR      NC,$6828        
67D0: FA A5 DB   LD      A,($DBA5)       
67D3: A7         AND     A               
67D4: 20 52      JR      NZ,$6828        
67D6: 3E 02      LD      A,$02           
67D8: E0 F2      LDFF00  ($F2),A         
67DA: F0 CD      LD      A,($CD)         
67DC: E6 E0      AND     $E0             
67DE: E0 CD      LDFF00  ($CD),A         
67E0: F0 CE      LD      A,($CE)         
67E2: E6 E0      AND     $E0             
67E4: E0 CE      LDFF00  ($CE),A         
67E6: CD CE 68   CALL    $68CE           
67E9: 79         LD      A,C             
67EA: E6 EE      AND     $EE             
67EC: 4F         LD      C,A             
67ED: 21 11 D7   LD      HL,$D711        
67F0: 09         ADD     HL,BC           
67F1: 3E 09      LD      A,$09           
67F3: 22         LD      (HLI),A         
67F4: 32         LD      (HLD),A         
67F5: 7D         LD      A,L             
67F6: C6 10      ADD     $10             
67F8: 6F         LD      L,A             
67F9: 3E 09      LD      A,$09           
67FB: 22         LD      (HLI),A         
67FC: 36 09      LD      (HL),$09        
67FE: 0E 03      LD      C,$03           
6800: 06 00      LD      B,$00           
6802: CD 22 68   CALL    $6822           
6805: 21 85 67   LD      HL,$6785        
6808: 09         ADD     HL,BC           
6809: 7E         LD      A,(HL)          
680A: 21 CE FF   LD      HL,$FFCE        
680D: 86         ADD     A,(HL)          
680E: 77         LD      (HL),A          
680F: 21 89 67   LD      HL,$6789        
6812: 09         ADD     HL,BC           
6813: 7E         LD      A,(HL)          
6814: 21 CD FF   LD      HL,$FFCD        
6817: 86         ADD     A,(HL)          
6818: 77         LD      (HL),A          
6819: 0D         DEC     C               
681A: 79         LD      A,C             
681B: FE FF      CP      $FF             
681D: 20 E3      JR      NZ,$6802        
681F: C3 C4 68   JP      $68C4           
6822: 11 81 67   LD      DE,$6781        
6825: C3 52 68   JP      $6852           
6828: FA A5 DB   LD      A,($DBA5)       
682B: 57         LD      D,A             
682C: CD DB 29   CALL    $29DB           
682F: D6 99      SUB     $99             
6831: DA C4 68   JP      C,$68C4         
6834: FE 04      CP      $04             
6836: D2 C4 68   JP      NC,$68C4        
6839: 4F         LD      C,A             
683A: 3E 02      LD      A,$02           
683C: E0 F2      LDFF00  ($F2),A         
683E: FA A5 DB   LD      A,($DBA5)       
6841: A7         AND     A               
6842: 20 21      JR      NZ,$6865        
6844: C1         POP     BC              
6845: F0 E9      LD      A,($E9)         
6847: 5F         LD      E,A             
6848: 50         LD      D,B             
6849: 21 11 D7   LD      HL,$D711        
684C: 19         ADD     HL,DE           
684D: 36 E1      LD      (HL),$E1        
684F: 11 71 67   LD      DE,$6771        
6852: D5         PUSH    DE              
6853: 21 00 D8   LD      HL,$D800        
6856: F0 F6      LD      A,($F6)         
6858: 5F         LD      E,A             
6859: 16 00      LD      D,$00           
685B: 19         ADD     HL,DE           
685C: 7E         LD      A,(HL)          
685D: F6 04      OR      $04             
685F: 77         LD      (HL),A          
6860: E0 F8      LDFF00  ($F8),A         
6862: C3 7A 52   JP      $527A           
6865: 21 00 D9   LD      HL,$D900        
6868: F0 F6      LD      A,($F6)         
686A: 5F         LD      E,A             
686B: 16 00      LD      D,$00           
686D: F0 F7      LD      A,($F7)         
686F: FE 1A      CP      $1A             
6871: 30 05      JR      NC,$6878        
6873: FE 06      CP      $06             
6875: 38 01      JR      C,$6878         
6877: 14         INC     D               
6878: 19         ADD     HL,DE           
6879: E5         PUSH    HL              
687A: D1         POP     DE              
687B: 21 75 67   LD      HL,$6775        
687E: 09         ADD     HL,BC           
687F: 1A         LD      A,(DE)          
6880: B6         OR      (HL)            
6881: 12         LD      (DE),A          
6882: E0 F8      LDFF00  ($F8),A         
6884: 21 7D 67   LD      HL,$677D        
6887: 09         ADD     HL,BC           
6888: FA AE DB   LD      A,($DBAE)       
688B: 86         ADD     A,(HL)          
688C: 5F         LD      E,A             
688D: 16 00      LD      D,$00           
688F: CD 25 2B   CALL    $2B25           
6892: E5         PUSH    HL              
6893: D1         POP     DE              
6894: 21 79 67   LD      HL,$6779        
6897: 09         ADD     HL,BC           
6898: 1A         LD      A,(DE)          
6899: B6         OR      (HL)            
689A: 12         LD      (DE),A          
689B: F0 CE      LD      A,($CE)         
689D: CB 37      SET     1,E             
689F: E6 0F      AND     $0F             
68A1: 5F         LD      E,A             
68A2: F0 CD      LD      A,($CD)         
68A4: E6 F0      AND     $F0             
68A6: B3         OR      E               
68A7: 5F         LD      E,A             
68A8: 16 00      LD      D,$00           
68AA: 21 11 D7   LD      HL,$D711        
68AD: 19         ADD     HL,DE           
68AE: E5         PUSH    HL              
68AF: D1         POP     DE              
68B0: 21 65 67   LD      HL,$6765        
68B3: 09         ADD     HL,BC           
68B4: 7E         LD      A,(HL)          
68B5: 12         LD      (DE),A          
68B6: 79         LD      A,C             
68B7: 17         RLA                     
68B8: E6 04      AND     $04             
68BA: 4F         LD      C,A             
68BB: 21 69 67   LD      HL,$6769        
68BE: 09         ADD     HL,BC           
68BF: C1         POP     BC              
68C0: E5         PUSH    HL              
68C1: C3 7A 52   JP      $527A           
68C4: C1         POP     BC              
68C5: C9         RET                     
68C6: 08 18 08   LD      ($0818),SP      
68C9: 18 10      JR      $68DB           
68CB: 10 20      STOP    $20             
68CD: 20 C5      JR      NZ,$6894        
68CF: 0E 03      LD      C,$03           
68D1: 06 00      LD      B,$00           
68D3: 3E 05      LD      A,$05           
68D5: CD F8 64   CALL    $64F8           
68D8: 38 28      JR      C,$6902         
68DA: 21 F0 C2   LD      HL,$C2F0        
68DD: 19         ADD     HL,DE           
68DE: 36 0F      LD      (HL),$0F        
68E0: F0 CE      LD      A,($CE)         
68E2: 21 C6 68   LD      HL,$68C6        
68E5: 09         ADD     HL,BC           
68E6: 86         ADD     A,(HL)          
68E7: 21 00 C2   LD      HL,$C200        
68EA: 19         ADD     HL,DE           
68EB: 77         LD      (HL),A          
68EC: F0 CD      LD      A,($CD)         
68EE: 21 CA 68   LD      HL,$68CA        
68F1: 09         ADD     HL,BC           
68F2: 86         ADD     A,(HL)          
68F3: 21 DA FF   LD      HL,$FFDA        
68F6: 96         SUB     (HL)            
68F7: 21 10 C2   LD      HL,$C210        
68FA: 19         ADD     HL,DE           
68FB: 77         LD      (HL),A          
68FC: 21 40 C3   LD      HL,$C340        
68FF: 19         ADD     HL,DE           
6900: 36 C4      LD      (HL),$C4        
6902: 0D         DEC     C               
6903: 79         LD      A,C             
6904: FE FF      CP      $FF             
6906: 20 CB      JR      NZ,$68D3        
6908: C1         POP     BC              
6909: C9         RET                     
690A: F8 08      LDHL    SP,$08          
690C: 18 F8      JR      $6906           
690E: 08 18 F8   LD      ($F818),SP      
6911: 08 18 F8   LD      ($F818),SP      
6914: F8 F8      LDHL    SP,$F8          
6916: 08 08 08   LD      ($0808),SP      
6919: 18 18      JR      $6933           
691B: 18 C5      JR      $68E2           
691D: 21 0A 69   LD      HL,$690A        
6920: 19         ADD     HL,DE           
6921: F0 EE      LD      A,($EE)         
6923: 86         ADD     A,(HL)          
6924: D6 08      SUB     $08             
6926: E6 F0      AND     $F0             
6928: E0 CE      LDFF00  ($CE),A         
692A: CB 37      SET     1,E             
692C: 4F         LD      C,A             
692D: 21 13 69   LD      HL,$6913        
6930: 19         ADD     HL,DE           
6931: F0 EC      LD      A,($EC)         
6933: 86         ADD     A,(HL)          
6934: D6 10      SUB     $10             
6936: E6 F0      AND     $F0             
6938: E0 CD      LDFF00  ($CD),A         
693A: B1         OR      C               
693B: 5F         LD      E,A             
693C: 21 11 D7   LD      HL,$D711        
693F: 19         ADD     HL,DE           
6940: 7C         LD      A,H             
6941: FE D7      CP      $D7             
6943: C2 BB 69   JP      NZ,$69BB        
6946: FA A5 DB   LD      A,($DBA5)       
6949: A7         AND     A               
694A: 7E         LD      A,(HL)          
694B: E0 AF      LDFF00  ($AF),A         
694D: 20 11      JR      NZ,$6960        
694F: E0 E9      LDFF00  ($E9),A         
6951: FE 0A      CP      $0A             
6953: 28 2A      JR      Z,$697F         
6955: FE D3      CP      $D3             
6957: 28 26      JR      Z,$697F         
6959: FE 5C      CP      $5C             
695B: 28 22      JR      Z,$697F         
695D: C3 BB 69   JP      $69BB           
6960: FE A9      CP      $A9             
6962: C2 BB 69   JP      NZ,$69BB        
6965: F0 F6      LD      A,($F6)         
6967: 4F         LD      C,A             
6968: 06 00      LD      B,$00           
696A: F0 F7      LD      A,($F7)         
696C: FE 1A      CP      $1A             
696E: 30 05      JR      NC,$6975        
6970: FE 06      CP      $06             
6972: 38 01      JR      C,$6975         
6974: 04         INC     B               
6975: 21 00 D9   LD      HL,$D900        
6978: 09         ADD     HL,BC           
6979: 7E         LD      A,(HL)          
697A: F6 40      OR      $40             
697C: 77         LD      (HL),A          
697D: E0 F8      LDFF00  ($F8),A         
697F: CD A6 20   CALL    $20A6           
6982: 3E 05      LD      A,$05           
6984: CD F8 64   CALL    $64F8           
6987: 38 32      JR      C,$69BB         
6989: AF         XOR     A               
698A: EA 9B C1   LD      ($C19B),A       
698D: 21 00 C2   LD      HL,$C200        
6990: 19         ADD     HL,DE           
6991: F0 CE      LD      A,($CE)         
6993: C6 08      ADD     $08             
6995: 77         LD      (HL),A          
6996: 21 10 C2   LD      HL,$C210        
6999: 19         ADD     HL,DE           
699A: F0 CD      LD      A,($CD)         
699C: C6 10      ADD     $10             
699E: 77         LD      (HL),A          
699F: 21 B0 C3   LD      HL,$C3B0        
69A2: 19         ADD     HL,DE           
69A3: FA A5 DB   LD      A,($DBA5)       
69A6: EE 01      XOR     $01             
69A8: 77         LD      (HL),A          
69A9: E0 F1      LDFF00  ($F1),A         
69AB: F0 E9      LD      A,($E9)         
69AD: FE 0A      CP      $0A             
69AF: 20 05      JR      NZ,$69B6        
69B1: 3E FF      LD      A,$FF           
69B3: 77         LD      (HL),A          
69B4: E0 F1      LDFF00  ($F1),A         
69B6: D5         PUSH    DE              
69B7: C1         POP     BC              
69B8: CD 41 54   CALL    $5441           
69BB: C1         POP     BC              
69BC: C9         RET                     
69BD: 6C         LD      L,H             
69BE: 74         LD      (HL),H          
69BF: 6D         LD      L,L             
69C0: 75         LD      (HL),L          
69C1: 36 00      LD      (HL),$00        
69C3: 36 20      LD      (HL),$20        
69C5: 36 10      LD      (HL),$10        
69C7: 36 30      LD      (HL),$30        
69C9: 21 4D C1   LD      HL,$C14D        
69CC: 34         INC     (HL)            
69CD: 3E 0A      LD      A,$0A           
69CF: EA 9E C1   LD      ($C19E),A       
69D2: CD A6 75   CALL    $75A6           
69D5: F0 E7      LD      A,($E7)         
69D7: 1F         RRA                     
69D8: 1F         RRA                     
69D9: 1F         RRA                     
69DA: E6 01      AND     $01             
69DC: 21 B0 C3   LD      HL,$C3B0        
69DF: 09         ADD     HL,BC           
69E0: 77         LD      (HL),A          
69E1: CD 8C 08   CALL    $088C           
69E4: 28 0A      JR      Z,$69F0         
69E6: 3D         DEC     A               
69E7: CA B7 3F   JP      Z,$3FB7         
69EA: 11 1E 4D   LD      DE,$4D1E        
69ED: C3 3B 3C   JP      $3C3B           
69F0: 11 C1 69   LD      DE,$69C1        
69F3: CD F2 6A   CALL    $6AF2           
69F6: CD 4A 7F   CALL    $7F4A           
69F9: FA A5 DB   LD      A,($DBA5)       
69FC: A7         AND     A               
69FD: F0 AF      LD      A,($AF)         
69FF: 28 06      JR      Z,$6A07         
6A01: FE 8A      CP      $8A             
6A03: 28 0A      JR      Z,$6A0F         
6A05: 18 2D      JR      $6A34           
6A07: FE D3      CP      $D3             
6A09: 28 04      JR      Z,$6A0F         
6A0B: FE 5C      CP      $5C             
6A0D: 20 25      JR      NZ,$6A34        
6A0F: 21 A0 C2   LD      HL,$C2A0        
6A12: 09         ADD     HL,BC           
6A13: 70         LD      (HL),B          
6A14: CD 8C 08   CALL    $088C           
6A17: 70         LD      (HL),B          
6A18: F0 E9      LD      A,($E9)         
6A1A: 5F         LD      E,A             
6A1B: 50         LD      D,B             
6A1C: CD A6 20   CALL    $20A6           
6A1F: F0 CE      LD      A,($CE)         
6A21: C6 08      ADD     $08             
6A23: E0 D7      LDFF00  ($D7),A         
6A25: F0 CD      LD      A,($CD)         
6A27: C6 10      ADD     $10             
6A29: E0 D8      LDFF00  ($D8),A         
6A2B: 3E 08      LD      A,$08           
6A2D: CD 53 09   CALL    $0953           
6A30: 3E 13      LD      A,$13           
6A32: E0 F4      LDFF00  ($F4),A         
6A34: C9         RET                     
6A35: 6C         LD      L,H             
6A36: 00         NOP                     
6A37: 6C         LD      L,H             
6A38: 20 5C      JR      NZ,$6A96        
6A3A: 00         NOP                     
6A3B: 5C         LD      E,H             
6A3C: 20 CD      JR      NZ,$6A0B        
6A3E: 91         SUB     C               
6A3F: 08 20 03   LD      ($0320),SP      
6A42: CD F9 6B   CALL    $6BF9           
6A45: 11 35 6A   LD      DE,$6A35        
6A48: C3 F2 6A   JP      $6AF2           
6A4B: 21 4D C1   LD      HL,$C14D        
6A4E: 34         INC     (HL)            
6A4F: F0 F0      LD      A,($F0)         
6A51: A7         AND     A               
6A52: 20 37      JR      NZ,$6A8B        
6A54: CD 91 08   CALL    $0891           
6A57: C2 EF 6A   JP      NZ,$6AEF        
6A5A: 3E 05      LD      A,$05           
6A5C: EA 9E C1   LD      ($C19E),A       
6A5F: CD A6 75   CALL    $75A6           
6A62: CD EF 6A   CALL    $6AEF           
6A65: F0 F1      LD      A,($F1)         
6A67: FE 02      CP      $02             
6A69: 20 15      JR      NZ,$6A80        
6A6B: FA 8E C1   LD      A,($C18E)       
6A6E: E6 1F      AND     $1F             
6A70: FE 0F      CP      $0F             
6A72: 20 0C      JR      NZ,$6A80        
6A74: F0 AF      LD      A,($AF)         
6A76: FE C0      CP      $C0             
6A78: 20 06      JR      NZ,$6A80        
6A7A: CD EC 08   CALL    $08EC           
6A7D: CD B7 3F   CALL    $3FB7           
6A80: C9         RET                     
6A81: 80         ADD     A,B             
6A82: 10 04      STOP    $04             
6A84: FC                              
6A85: 00         NOP                     
6A86: 00         NOP                     
6A87: FE FE      CP      $FE             
6A89: FA 04 CD   LD      A,($CD04)       
6A8C: 91         SUB     C               
6A8D: 08 28 21   LD      ($2128),SP      
6A90: 3E 02      LD      A,$02           
6A92: CD F8 64   CALL    $64F8           
6A95: 38 17      JR      C,$6AAE         
6A97: F0 D7      LD      A,($D7)         
6A99: 21 00 C2   LD      HL,$C200        
6A9C: 19         ADD     HL,DE           
6A9D: 77         LD      (HL),A          
6A9E: F0 D8      LD      A,($D8)         
6AA0: 21 10 C2   LD      HL,$C210        
6AA3: 19         ADD     HL,DE           
6AA4: 77         LD      (HL),A          
6AA5: 21 E0 C2   LD      HL,$C2E0        
6AA8: 19         ADD     HL,DE           
6AA9: 36 17      LD      (HL),$17        
6AAB: CD D7 08   CALL    $08D7           
6AAE: C3 B7 3F   JP      $3FB7           
6AB1: F0 F1      LD      A,($F1)         
6AB3: F5         PUSH    AF              
6AB4: 5F         LD      E,A             
6AB5: 50         LD      D,B             
6AB6: AF         XOR     A               
6AB7: E0 F1      LDFF00  ($F1),A         
6AB9: 21 83 6A   LD      HL,$6A83        
6ABC: 19         ADD     HL,DE           
6ABD: F0 EE      LD      A,($EE)         
6ABF: 86         ADD     A,(HL)          
6AC0: E0 EE      LDFF00  ($EE),A         
6AC2: 21 87 6A   LD      HL,$6A87        
6AC5: 19         ADD     HL,DE           
6AC6: F0 EC      LD      A,($EC)         
6AC8: 86         ADD     A,(HL)          
6AC9: E0 EC      LDFF00  ($EC),A         
6ACB: 11 81 6A   LD      DE,$6A81        
6ACE: CD D0 3C   CALL    $3CD0           
6AD1: CD BA 3D   CALL    $3DBA           
6AD4: F1         POP     AF              
6AD5: E0 F1      LDFF00  ($F1),A         
6AD7: 11 E1 6B   LD      DE,$6BE1        
6ADA: CD 3B 3C   CALL    $3C3B           
6ADD: 3E 0C      LD      A,$0C           
6ADF: EA 9E C1   LD      ($C19E),A       
6AE2: CD A6 75   CALL    $75A6           
6AE5: 18 0E      JR      $6AF5           
6AE7: CD 91 08   CALL    $0891           
6AEA: 20 03      JR      NZ,$6AEF        
6AEC: CD F9 6B   CALL    $6BF9           
6AEF: 11 E1 6B   LD      DE,$6BE1        
6AF2: CD 3B 3C   CALL    $3C3B           
6AF5: CD 4A 7F   CALL    $7F4A           
6AF8: CD 91 08   CALL    $0891           
6AFB: 20 6A      JR      NZ,$6B67        
6AFD: CD F7 7E   CALL    $7EF7           
6B00: CD AA 7C   CALL    $7CAA           
6B03: 21 A0 C2   LD      HL,$C2A0        
6B06: 09         ADD     HL,BC           
6B07: 7E         LD      A,(HL)          
6B08: A7         AND     A               
6B09: 28 52      JR      Z,$6B5D         
6B0B: CD 91 08   CALL    $0891           
6B0E: F0 EB      LD      A,($EB)         
6B10: FE 04      CP      $04             
6B12: 20 06      JR      NZ,$6B1A        
6B14: CD 8C 08   CALL    $088C           
6B17: 36 30      LD      (HL),$30        
6B19: C9         RET                     
6B1A: 36 18      LD      (HL),$18        
6B1C: 21 20 C3   LD      HL,$C320        
6B1F: 09         ADD     HL,BC           
6B20: 36 10      LD      (HL),$10        
6B22: 21 A0 C2   LD      HL,$C2A0        
6B25: 09         ADD     HL,BC           
6B26: 7E         LD      A,(HL)          
6B27: 3C         INC     A               
6B28: 28 04      JR      Z,$6B2E         
6B2A: 3E 07      LD      A,$07           
6B2C: E0 F2      LDFF00  ($F2),A         
6B2E: CD DC 08   CALL    $08DC           
6B31: F0 EB      LD      A,($EB)         
6B33: FE 00      CP      $00             
6B35: 20 15      JR      NZ,$6B4C        
6B37: CD 47 6B   CALL    $6B47           
6B3A: 21 40 C2   LD      HL,$C240        
6B3D: 09         ADD     HL,BC           
6B3E: 7E         LD      A,(HL)          
6B3F: 2F         CPL                     
6B40: 3C         INC     A               
6B41: CB 2F      SET     1,E             
6B43: CB 2F      SET     1,E             
6B45: 77         LD      (HL),A          
6B46: C9         RET                     
6B47: 21 50 C2   LD      HL,$C250        
6B4A: 18 F1      JR      $6B3D           
6B4C: CD 5E 6B   CALL    $6B5E           
6B4F: 21 40 C2   LD      HL,$C240        
6B52: 09         ADD     HL,BC           
6B53: 7E         LD      A,(HL)          
6B54: 2F         CPL                     
6B55: 3C         INC     A               
6B56: CB 2F      SET     1,E             
6B58: CB 2F      SET     1,E             
6B5A: CB 2F      SET     1,E             
6B5C: 77         LD      (HL),A          
6B5D: C9         RET                     
6B5E: 21 50 C2   LD      HL,$C250        
6B61: 18 EF      JR      $6B52           
6B63: 00         NOP                     
6B64: 03         INC     BC              
6B65: 01 02 FE   LD      BC,$FE02        
6B68: 01 20 03   LD      BC,$0320        
6B6B: C3 B7 3F   JP      $3FB7           
6B6E: F0 EB      LD      A,($EB)         
6B70: FE 0A      CP      $0A             
6B72: 28 15      JR      Z,$6B89         
6B74: CD 91 08   CALL    $0891           
6B77: CB 3F      SET     1,E             
6B79: CB 3F      SET     1,E             
6B7B: CB 3F      SET     1,E             
6B7D: E6 03      AND     $03             
6B7F: 5F         LD      E,A             
6B80: 50         LD      D,B             
6B81: 21 63 6B   LD      HL,$6B63        
6B84: 19         ADD     HL,DE           
6B85: 7E         LD      A,(HL)          
6B86: CD 87 3B   CALL    $3B87           
6B89: CD F7 7E   CALL    $7EF7           
6B8C: 18 08      JR      $6B96           
6B8E: 02         LD      (BC),A          
6B8F: 01 02 02   LD      BC,$0202        
6B92: 40         LD      B,B             
6B93: 08 40 40   LD      ($4040),SP      
6B96: F0 F9      LD      A,($F9)         
6B98: A7         AND     A               
6B99: 20 0C      JR      NZ,$6BA7        
6B9B: CD 30 7F   CALL    $7F30           
6B9E: 21 20 C3   LD      HL,$C320        
6BA1: 09         ADD     HL,BC           
6BA2: 7E         LD      A,(HL)          
6BA3: D6 02      SUB     $02             
6BA5: 77         LD      (HL),A          
6BA6: C9         RET                     
6BA7: 21 70 C4   LD      HL,$C470        
6BAA: 09         ADD     HL,BC           
6BAB: 7E         LD      A,(HL)          
6BAC: 5F         LD      E,A             
6BAD: 50         LD      D,B             
6BAE: A7         AND     A               
6BAF: 28 15      JR      Z,$6BC6         
6BB1: F0 E7      LD      A,($E7)         
6BB3: E6 07      AND     $07             
6BB5: 20 0F      JR      NZ,$6BC6        
6BB7: 21 40 C2   LD      HL,$C240        
6BBA: 09         ADD     HL,BC           
6BBB: 7E         LD      A,(HL)          
6BBC: A7         AND     A               
6BBD: 28 07      JR      Z,$6BC6         
6BBF: E6 80      AND     $80             
6BC1: 28 02      JR      Z,$6BC5         
6BC3: 34         INC     (HL)            
6BC4: 34         INC     (HL)            
6BC5: 35         DEC     (HL)            
6BC6: 21 8E 6B   LD      HL,$6B8E        
6BC9: 19         ADD     HL,DE           
6BCA: 7E         LD      A,(HL)          
6BCB: 21 50 C2   LD      HL,$C250        
6BCE: 09         ADD     HL,BC           
6BCF: 86         ADD     A,(HL)          
6BD0: 77         LD      (HL),A          
6BD1: 21 92 6B   LD      HL,$6B92        
6BD4: 19         ADD     HL,DE           
6BD5: 96         SUB     (HL)            
6BD6: E6 80      AND     $80             
6BD8: 20 06      JR      NZ,$6BE0        
6BDA: 7E         LD      A,(HL)          
6BDB: 21 50 C2   LD      HL,$C250        
6BDE: 09         ADD     HL,BC           
6BDF: 77         LD      (HL),A          
6BE0: C9         RET                     
6BE1: 2E 20      LD      L,$20           
6BE3: 2C         INC     L               
6BE4: 20 2C      JR      NZ,$6C12        
6BE6: 00         NOP                     
6BE7: 2E 00      LD      L,$00           
6BE9: 2A         LD      A,(HLI)         
6BEA: 40         LD      B,B             
6BEB: 2A         LD      A,(HLI)         
6BEC: 60         LD      H,B             
6BED: 2A         LD      A,(HLI)         
6BEE: 00         NOP                     
6BEF: 2A         LD      A,(HLI)         
6BF0: 20 01      JR      NZ,$6BF3        
6BF2: 00         NOP                     
6BF3: 03         INC     BC              
6BF4: 02         LD      (BC),A          
6BF5: 02         LD      (BC),A          
6BF6: 0A         LD      A,(BC)          
6BF7: 0E 06      LD      C,$06           
6BF9: FA 1C C1   LD      A,($C11C)       
6BFC: FE 02      CP      $02             
6BFE: 30 76      JR      NC,$6C76        
6C00: F0 A2      LD      A,($A2)         
6C02: A7         AND     A               
6C03: 20 71      JR      NZ,$6C76        
6C05: 21 EE FF   LD      HL,$FFEE        
6C08: F0 98      LD      A,($98)         
6C0A: 96         SUB     (HL)            
6C0B: C6 06      ADD     $06             
6C0D: FE 0C      CP      $0C             
6C0F: 30 65      JR      NC,$6C76        
6C11: 21 EC FF   LD      HL,$FFEC        
6C14: F0 99      LD      A,($99)         
6C16: 96         SUB     (HL)            
6C17: C6 06      ADD     $06             
6C19: FE 0C      CP      $0C             
6C1B: 30 59      JR      NC,$6C76        
6C1D: FA 5B C1   LD      A,($C15B)       
6C20: A7         AND     A               
6C21: 28 54      JR      Z,$6C77         
6C23: F0 EB      LD      A,($EB)         
6C25: FE 2B      CP      $2B             
6C27: 20 34      JR      NZ,$6C5D        
6C29: FA 44 DB   LD      A,($DB44)       
6C2C: FE 02      CP      $02             
6C2E: 38 47      JR      C,$6C77         
6C30: F0 9E      LD      A,($9E)         
6C32: 5F         LD      E,A             
6C33: 50         LD      D,B             
6C34: 21 F5 6B   LD      HL,$6BF5        
6C37: 19         ADD     HL,DE           
6C38: 5E         LD      E,(HL)          
6C39: 21 80 C3   LD      HL,$C380        
6C3C: 09         ADD     HL,BC           
6C3D: 7E         LD      A,(HL)          
6C3E: 93         SUB     E               
6C3F: E6 0F      AND     $0F             
6C41: FE 05      CP      $05             
6C43: 30 32      JR      NC,$6C77        
6C45: 21 A0 C2   LD      HL,$C2A0        
6C48: 09         ADD     HL,BC           
6C49: 36 02      LD      (HL),$02        
6C4B: 3E 07      LD      A,$07           
6C4D: E0 F2      LDFF00  ($F2),A         
6C4F: F0 EF      LD      A,($EF)         
6C51: E0 D8      LDFF00  ($D8),A         
6C53: F0 EE      LD      A,($EE)         
6C55: E0 D7      LDFF00  ($D7),A         
6C57: 3E 05      LD      A,$05           
6C59: CD 53 09   CALL    $0953           
6C5C: C9         RET                     
6C5D: 21 80 C3   LD      HL,$C380        
6C60: 09         ADD     HL,BC           
6C61: 5E         LD      E,(HL)          
6C62: 50         LD      D,B             
6C63: 21 F1 6B   LD      HL,$6BF1        
6C66: 19         ADD     HL,DE           
6C67: F0 9E      LD      A,($9E)         
6C69: BE         CP      (HL)            
6C6A: 20 0B      JR      NZ,$6C77        
6C6C: 3E 16      LD      A,$16           
6C6E: E0 F2      LDFF00  ($F2),A         
6C70: 21 A0 C2   LD      HL,$C2A0        
6C73: 09         ADD     HL,BC           
6C74: 36 FF      LD      (HL),$FF        
6C76: C9         RET                     
6C77: CD DC 6C   CALL    $6CDC           
6C7A: F0 EB      LD      A,($EB)         
6C7C: FE 2B      CP      $2B             
6C7E: 28 04      JR      Z,$6C84         
6C80: FE 0C      CP      $0C             
6C82: 20 EC      JR      NZ,$6C70        
6C84: C3 B7 3F   JP      $3FB7           
6C87: F0 E7      LD      A,($E7)         
6C89: A9         XOR     C               
6C8A: 1F         RRA                     
6C8B: D2 E7 6C   JP      NC,$6CE7        
6C8E: F0 A2      LD      A,($A2)         
6C90: A7         AND     A               
6C91: 20 E3      JR      NZ,$6C76        
6C93: FA 1C C1   LD      A,($C11C)       
6C96: FE 02      CP      $02             
6C98: 30 DC      JR      NC,$6C76        
6C9A: C5         PUSH    BC              
6C9B: CB 21      SET     1,E             
6C9D: CB 21      SET     1,E             
6C9F: 21 80 D5   LD      HL,$D580        
6CA2: 09         ADD     HL,BC           
6CA3: C1         POP     BC              
6CA4: F0 EE      LD      A,($EE)         
6CA6: 86         ADD     A,(HL)          
6CA7: E5         PUSH    HL              
6CA8: 21 98 FF   LD      HL,$FF98        
6CAB: 96         SUB     (HL)            
6CAC: D6 08      SUB     $08             
6CAE: FE 80      CP      $80             
6CB0: 38 02      JR      C,$6CB4         
6CB2: 2F         CPL                     
6CB3: 3C         INC     A               
6CB4: E1         POP     HL              
6CB5: F5         PUSH    AF              
6CB6: 23         INC     HL              
6CB7: 3E 04      LD      A,$04           
6CB9: 86         ADD     A,(HL)          
6CBA: 5F         LD      E,A             
6CBB: F1         POP     AF              
6CBC: BB         CP      E               
6CBD: D2 E7 6C   JP      NC,$6CE7        
6CC0: 23         INC     HL              
6CC1: F0 EC      LD      A,($EC)         
6CC3: 86         ADD     A,(HL)          
6CC4: E5         PUSH    HL              
6CC5: 21 99 FF   LD      HL,$FF99        
6CC8: 96         SUB     (HL)            
6CC9: D6 08      SUB     $08             
6CCB: FE 80      CP      $80             
6CCD: 38 02      JR      C,$6CD1         
6CCF: 2F         CPL                     
6CD0: 3C         INC     A               
6CD1: E1         POP     HL              
6CD2: F5         PUSH    AF              
6CD3: 23         INC     HL              
6CD4: 3E 04      LD      A,$04           
6CD6: 86         ADD     A,(HL)          
6CD7: 5F         LD      E,A             
6CD8: F1         POP     AF              
6CD9: BB         CP      E               
6CDA: 30 0B      JR      NC,$6CE7        
6CDC: 21 40 C3   LD      HL,$C340        
6CDF: 09         ADD     HL,BC           
6CE0: 7E         LD      A,(HL)          
6CE1: E6 80      AND     $80             
6CE3: 28 04      JR      Z,$6CE9         
6CE5: 37         SCF                     
6CE6: C9         RET                     
6CE7: A7         AND     A               
6CE8: C9         RET                     
6CE9: F0 9D      LD      A,($9D)         
6CEB: D6 4E      SUB     $4E             
6CED: FE 02      CP      $02             
6CEF: 38 F4      JR      C,$6CE5         
6CF1: F0 EB      LD      A,($EB)         
6CF3: FE AC      CP      $AC             
6CF5: 20 1E      JR      NZ,$6D15        
6CF7: CD BB 7E   CALL    $7EBB           
6CFA: 7B         LD      A,E             
6CFB: FE 02      CP      $02             
6CFD: 20 5A      JR      NZ,$6D59        
6CFF: CD 8D 3B   CALL    $3B8D           
6D02: 36 05      LD      (HL),$05        
6D04: 3E 02      LD      A,$02           
6D06: EA 46 C1   LD      ($C146),A       
6D09: 3E F0      LD      A,$F0           
6D0B: E0 9B      LDFF00  ($9B),A         
6D0D: CD AF 3D   CALL    $3DAF           
6D10: 3E 0E      LD      A,$0E           
6D12: E0 F3      LDFF00  ($F3),A         
6D14: C9         RET                     
6D15: F0 EB      LD      A,($EB)         
6D17: FE 9F      CP      $9F             
6D19: 20 3E      JR      NZ,$6D59        
6D1B: FA 46 C1   LD      A,($C146)       
6D1E: A7         AND     A               
6D1F: 28 38      JR      Z,$6D59         
6D21: F0 B7      LD      A,($B7)         
6D23: A7         AND     A               
6D24: 20 11      JR      NZ,$6D37        
6D26: F0 F9      LD      A,($F9)         
6D28: A7         AND     A               
6D29: 20 06      JR      NZ,$6D31        
6D2B: F0 A3      LD      A,($A3)         
6D2D: EE 80      XOR     $80             
6D2F: 18 02      JR      $6D33           
6D31: F0 9B      LD      A,($9B)         
6D33: E6 80      AND     $80             
6D35: 20 22      JR      NZ,$6D59        
6D37: 3E 02      LD      A,$02           
6D39: E0 B7      LDFF00  ($B7),A         
6D3B: 21 90 C2   LD      HL,$C290        
6D3E: 09         ADD     HL,BC           
6D3F: 36 02      LD      (HL),$02        
6D41: CD 91 08   CALL    $0891           
6D44: 36 30      LD      (HL),$30        
6D46: 3E 0E      LD      A,$0E           
6D48: E0 F3      LDFF00  ($F3),A         
6D4A: F0 F9      LD      A,($F9)         
6D4C: A7         AND     A               
6D4D: 20 05      JR      NZ,$6D54        
6D4F: 3E 10      LD      A,$10           
6D51: E0 A3      LDFF00  ($A3),A         
6D53: C9         RET                     
6D54: 3E F0      LD      A,$F0           
6D56: E0 9B      LDFF00  ($9B),A         
6D58: C9         RET                     
6D59: F0 EB      LD      A,($EB)         
6D5B: FE 1C      CP      $1C             
6D5D: 20 0B      JR      NZ,$6D6A        
6D5F: CD 91 08   CALL    $0891           
6D62: 36 80      LD      (HL),$80        
6D64: CD 8D 3B   CALL    $3B8D           
6D67: 36 04      LD      (HL),$04        
6D69: C9         RET                     
6D6A: FE 8E      CP      $8E             
6D6C: 28 0B      JR      Z,$6D79         
6D6E: FE 82      CP      $82             
6D70: 28 07      JR      Z,$6D79         
6D72: FA 3E C1   LD      A,($C13E)       
6D75: A7         AND     A               
6D76: C2 1F 6E   JP      NZ,$6E1F        
6D79: F0 EB      LD      A,($EB)         
6D7B: FE E4      CP      $E4             
6D7D: 20 10      JR      NZ,$6D8F        
6D7F: F0 F0      LD      A,($F0)         
6D81: FE 04      CP      $04             
6D83: 20 0A      JR      NZ,$6D8F        
6D85: CD 8D 3B   CALL    $3B8D           
6D88: 36 08      LD      (HL),$08        
6D8A: 3E 03      LD      A,$03           
6D8C: E0 F3      LDFF00  ($F3),A         
6D8E: C9         RET                     
6D8F: FA C7 DB   LD      A,($DBC7)       
6D92: 21 C6 C1   LD      HL,$C1C6        
6D95: B6         OR      (HL)            
6D96: 21 66 C1   LD      HL,$C166        
6D99: B6         OR      (HL)            
6D9A: 21 A9 C1   LD      HL,$C1A9        
6D9D: B6         OR      (HL)            
6D9E: C2 1F 6E   JP      NZ,$6E1F        
6DA1: 3E 03      LD      A,$03           
6DA3: E0 F3      LDFF00  ($F3),A         
6DA5: 21 D0 C4   LD      HL,$C4D0        
6DA8: 09         ADD     HL,BC           
6DA9: 50         LD      D,B             
6DAA: 5E         LD      E,(HL)          
6DAB: 21 4E 48   LD      HL,$484E        
6DAE: 19         ADD     HL,DE           
6DAF: 5E         LD      E,(HL)          
6DB0: FA 7C D4   LD      A,($D47C)       
6DB3: FE 02      CP      $02             
6DB5: 20 09      JR      NZ,$6DC0        
6DB7: 7B         LD      A,E             
6DB8: FE 04      CP      $04             
6DBA: 20 02      JR      NZ,$6DBE        
6DBC: 1E 00      LD      E,$00           
6DBE: CB 3B      SET     1,E             
6DC0: FA 94 DB   LD      A,($DB94)       
6DC3: 83         ADD     A,E             
6DC4: EA 94 DB   LD      ($DB94),A       
6DC7: 3E 50      LD      A,$50           
6DC9: EA C7 DB   LD      ($DBC7),A       
6DCC: AF         XOR     A               
6DCD: EA 71 D4   LD      ($D471),A       
6DD0: FA 7C D4   LD      A,($D47C)       
6DD3: A7         AND     A               
6DD4: 28 1E      JR      Z,$6DF4         
6DD6: 21 7A D4   LD      HL,$D47A        
6DD9: 34         INC     (HL)            
6DDA: 7E         LD      A,(HL)          
6DDB: FE 03      CP      $03             
6DDD: 38 15      JR      C,$6DF4         
6DDF: AF         XOR     A               
6DE0: EA 7C D4   LD      ($D47C),A       
6DE3: FA BE C1   LD      A,($C1BE)       
6DE6: A7         AND     A               
6DE7: 20 0B      JR      NZ,$6DF4        
6DE9: F0 B0      LD      A,($B0)         
6DEB: FE 22      CP      $22             
6DED: 28 03      JR      Z,$6DF2         
6DEF: EA 68 D3   LD      ($D368),A       
6DF2: E0 BF      LDFF00  ($BF),A         
6DF4: CD 42 09   CALL    $0942           
6DF7: 3E 10      LD      A,$10           
6DF9: EA 3E C1   LD      ($C13E),A       
6DFC: F0 EB      LD      A,($EB)         
6DFE: 1E 18      LD      E,$18           
6E00: FE 82      CP      $82             
6E02: CA BC 6F   JP      Z,$6FBC         
6E05: FE 5A      CP      $5A             
6E07: 20 06      JR      NZ,$6E0F        
6E09: 21 A0 C2   LD      HL,$C2A0        
6E0C: 09         ADD     HL,BC           
6E0D: 36 01      LD      (HL),$01        
6E0F: FE 59      CP      $59             
6E11: 3E 14      LD      A,$14           
6E13: 20 02      JR      NZ,$6E17        
6E15: 3E 18      LD      A,$18           
6E17: CD 69 75   CALL    $7569           
6E1A: F0 F9      LD      A,($F9)         
6E1C: A7         AND     A               
6E1D: 20 04      JR      NZ,$6E23        
6E1F: 37         SCF                     
6E20: C9         RET                     
6E21: 0C         INC     C               
6E22: F4                              
6E23: F0 9C      LD      A,($9C)         
6E25: FE 02      CP      $02             
6E27: 28 F6      JR      Z,$6E1F         
6E29: CD AB 7E   CALL    $7EAB           
6E2C: 50         LD      D,B             
6E2D: 21 21 6E   LD      HL,$6E21        
6E30: 19         ADD     HL,DE           
6E31: 7E         LD      A,(HL)          
6E32: E0 9A      LDFF00  ($9A),A         
6E34: 3E F4      LD      A,$F4           
6E36: E0 9B      LDFF00  ($9B),A         
6E38: AF         XOR     A               
6E39: E0 9C      LDFF00  ($9C),A         
6E3B: 37         SCF                     
6E3C: C9         RET                     
6E3D: CD 87 6C   CALL    $6C87           
6E40: FA 40 C1   LD      A,($C140)       
6E43: FE 00      CP      $00             
6E45: CA EA 73   JP      Z,$73EA         
6E48: 21 20 C4   LD      HL,$C420        
6E4B: 09         ADD     HL,BC           
6E4C: 7E         LD      A,(HL)          
6E4D: A7         AND     A               
6E4E: 28 05      JR      Z,$6E55         
6E50: FE 18      CP      $18             
6E52: DA EA 73   JP      C,$73EA         
6E55: FA AC C1   LD      A,($C1AC)       
6E58: A7         AND     A               
6E59: 28 05      JR      Z,$6E60         
6E5B: 3D         DEC     A               
6E5C: B9         CP      C               
6E5D: CA EA 73   JP      Z,$73EA         
6E60: 21 10 C4   LD      HL,$C410        
6E63: 09         ADD     HL,BC           
6E64: 7E         LD      A,(HL)          
6E65: A7         AND     A               
6E66: C2 EA 73   JP      NZ,$73EA        
6E69: 11 EE FF   LD      DE,$FFEE        
6E6C: C5         PUSH    BC              
6E6D: CB 21      SET     1,E             
6E6F: CB 21      SET     1,E             
6E71: 21 80 D5   LD      HL,$D580        
6E74: 09         ADD     HL,BC           
6E75: C1         POP     BC              
6E76: 1A         LD      A,(DE)          
6E77: 86         ADD     A,(HL)          
6E78: E5         PUSH    HL              
6E79: 21 40 C1   LD      HL,$C140        
6E7C: 96         SUB     (HL)            
6E7D: FE 80      CP      $80             
6E7F: 38 02      JR      C,$6E83         
6E81: 2F         CPL                     
6E82: 3C         INC     A               
6E83: E1         POP     HL              
6E84: F5         PUSH    AF              
6E85: 23         INC     HL              
6E86: FA 41 C1   LD      A,($C141)       
6E89: 86         ADD     A,(HL)          
6E8A: 5F         LD      E,A             
6E8B: F1         POP     AF              
6E8C: BB         CP      E               
6E8D: D2 EA 73   JP      NC,$73EA        
6E90: 23         INC     HL              
6E91: E5         PUSH    HL              
6E92: 11 EC FF   LD      DE,$FFEC        
6E95: E1         POP     HL              
6E96: 1A         LD      A,(DE)          
6E97: 86         ADD     A,(HL)          
6E98: E5         PUSH    HL              
6E99: 21 42 C1   LD      HL,$C142        
6E9C: 96         SUB     (HL)            
6E9D: FE 80      CP      $80             
6E9F: 38 02      JR      C,$6EA3         
6EA1: 2F         CPL                     
6EA2: 3C         INC     A               
6EA3: E1         POP     HL              
6EA4: F5         PUSH    AF              
6EA5: 23         INC     HL              
6EA6: FA 43 C1   LD      A,($C143)       
6EA9: 86         ADD     A,(HL)          
6EAA: 5F         LD      E,A             
6EAB: F1         POP     AF              
6EAC: BB         CP      E               
6EAD: D2 EA 73   JP      NC,$73EA        
6EB0: 21 40 C3   LD      HL,$C340        
6EB3: 09         ADD     HL,BC           
6EB4: 7E         LD      A,(HL)          
6EB5: E6 20      AND     $20             
6EB7: C2 36 63   JP      NZ,$6336        
6EBA: FA B0 C5   LD      A,($C5B0)       
6EBD: A7         AND     A               
6EBE: C2 FE 6F   JP      NZ,$6FFE        
6EC1: FA 4A C1   LD      A,($C14A)       
6EC4: E0 E9      LDFF00  ($E9),A         
6EC6: CD 42 09   CALL    $0942           
6EC9: F0 EB      LD      A,($EB)         
6ECB: FE E2      CP      $E2             
6ECD: 20 17      JR      NZ,$6EE6        
6ECF: FA 44 DB   LD      A,($DB44)       
6ED2: FE 02      CP      $02             
6ED4: C0         RET     NZ              
6ED5: F0 9E      LD      A,($9E)         
6ED7: FE 02      CP      $02             
6ED9: C0         RET     NZ              
6EDA: 3E 04      LD      A,$04           
6EDC: E0 9B      LDFF00  ($9B),A         
6EDE: 3E 08      LD      A,$08           
6EE0: EA 3E C1   LD      ($C13E),A       
6EE3: C3 8D 3B   JP      $3B8D           
6EE6: FE 55      CP      $55             
6EE8: 20 22      JR      NZ,$6F0C        
6EEA: F0 F0      LD      A,($F0)         
6EEC: FE 02      CP      $02             
6EEE: C2 A8 6F   JP      NZ,$6FA8        
6EF1: 21 40 C2   LD      HL,$C240        
6EF4: 09         ADD     HL,BC           
6EF5: 7E         LD      A,(HL)          
6EF6: 2F         CPL                     
6EF7: 3C         INC     A               
6EF8: 77         LD      (HL),A          
6EF9: 21 50 C2   LD      HL,$C250        
6EFC: 09         ADD     HL,BC           
6EFD: 7E         LD      A,(HL)          
6EFE: 2F         CPL                     
6EFF: 3C         INC     A               
6F00: 77         LD      (HL),A          
6F01: CD 91 08   CALL    $0891           
6F04: 36 40      LD      (HL),$40        
6F06: CD 8C 08   CALL    $088C           
6F09: 36 08      LD      (HL),$08        
6F0B: C9         RET                     
6F0C: FE 51      CP      $51             
6F0E: 20 25      JR      NZ,$6F35        
6F10: 21 30 C4   LD      HL,$C430        
6F13: 09         ADD     HL,BC           
6F14: E6 40      AND     $40             
6F16: CA A8 6F   JP      Z,$6FA8         
6F19: 21 B0 C2   LD      HL,$C2B0        
6F1C: 09         ADD     HL,BC           
6F1D: 7E         LD      A,(HL)          
6F1E: 2F         CPL                     
6F1F: 3C         INC     A               
6F20: 77         LD      (HL),A          
6F21: CD 71 6F   CALL    $6F71           
6F24: CD 8C 08   CALL    $088C           
6F27: 36 0C      LD      (HL),$0C        
6F29: 3E 01      LD      A,$01           
6F2B: EA 60 C1   LD      ($C160),A       
6F2E: AF         XOR     A               
6F2F: EA 22 C1   LD      ($C122),A       
6F32: C3 4C 71   JP      $714C           
6F35: FE 58      CP      $58             
6F37: 20 06      JR      NZ,$6F3F        
6F39: CD A8 6F   CALL    $6FA8           
6F3C: C3 70 6C   JP      $6C70           
6F3F: FE 2C      CP      $2C             
6F41: 20 3F      JR      NZ,$6F82        
6F43: 21 90 C2   LD      HL,$C290        
6F46: 09         ADD     HL,BC           
6F47: 7E         LD      A,(HL)          
6F48: FE 03      CP      $03             
6F4A: 28 25      JR      Z,$6F71         
6F4C: 36 03      LD      (HL),$03        
6F4E: 21 20 C3   LD      HL,$C320        
6F51: 09         ADD     HL,BC           
6F52: 36 20      LD      (HL),$20        
6F54: CD 91 08   CALL    $0891           
6F57: 36 FF      LD      (HL),$FF        
6F59: F0 9E      LD      A,($9E)         
6F5B: 5F         LD      E,A             
6F5C: 50         LD      D,B             
6F5D: 21 7A 6F   LD      HL,$6F7A        
6F60: 19         ADD     HL,DE           
6F61: 7E         LD      A,(HL)          
6F62: 21 40 C2   LD      HL,$C240        
6F65: 09         ADD     HL,BC           
6F66: 77         LD      (HL),A          
6F67: 21 7E 6F   LD      HL,$6F7E        
6F6A: 19         ADD     HL,DE           
6F6B: 7E         LD      A,(HL)          
6F6C: 21 50 C2   LD      HL,$C250        
6F6F: 09         ADD     HL,BC           
6F70: 77         LD      (HL),A          
6F71: CD A8 6F   CALL    $6FA8           
6F74: 21 10 C4   LD      HL,$C410        
6F77: 09         ADD     HL,BC           
6F78: 70         LD      (HL),B          
6F79: C9         RET                     
6F7A: 10 F0      STOP    $F0             
6F7C: 00         NOP                     
6F7D: 00         NOP                     
6F7E: 00         NOP                     
6F7F: 00         NOP                     
6F80: F0 10      LD      A,($10)         
6F82: FE 9C      CP      $9C             
6F84: 28 04      JR      Z,$6F8A         
6F86: FE 15      CP      $15             
6F88: 20 19      JR      NZ,$6FA3        
6F8A: F0 9E      LD      A,($9E)         
6F8C: E6 02      AND     $02             
6F8E: 20 06      JR      NZ,$6F96        
6F90: 21 40 C2   LD      HL,$C240        
6F93: 09         ADD     HL,BC           
6F94: 18 04      JR      $6F9A           
6F96: 21 50 C2   LD      HL,$C250        
6F99: 09         ADD     HL,BC           
6F9A: 7E         LD      A,(HL)          
6F9B: 2F         CPL                     
6F9C: 3C         INC     A               
6F9D: 77         LD      (HL),A          
6F9E: CD A8 6F   CALL    $6FA8           
6FA1: 70         LD      (HL),B          
6FA2: C9         RET                     
6FA3: FE 5A      CP      $5A             
6FA5: CA 39 6F   JP      Z,$6F39         
6FA8: 3E 09      LD      A,$09           
6FAA: E0 F2      LDFF00  ($F2),A         
6FAC: CD 42 09   CALL    $0942           
6FAF: 3E 0C      LD      A,$0C           
6FB1: EA 3E C1   LD      ($C13E),A       
6FB4: F0 EB      LD      A,($EB)         
6FB6: FE 82      CP      $82             
6FB8: 20 14      JR      NZ,$6FCE        
6FBA: 1E 10      LD      E,$10           
6FBC: D5         PUSH    DE              
6FBD: CD AB 7E   CALL    $7EAB           
6FC0: 7B         LD      A,E             
6FC1: A7         AND     A               
6FC2: D1         POP     DE              
6FC3: 7B         LD      A,E             
6FC4: 28 02      JR      Z,$6FC8         
6FC6: 2F         CPL                     
6FC7: 3C         INC     A               
6FC8: E0 9A      LDFF00  ($9A),A         
6FCA: AF         XOR     A               
6FCB: E0 9B      LDFF00  ($9B),A         
6FCD: C9         RET                     
6FCE: 3E 12      LD      A,$12           
6FD0: CD 69 75   CALL    $7569           
6FD3: 21 E9 FF   LD      HL,$FFE9        
6FD6: F0 CB      LD      A,($CB)         
6FD8: E6 0F      AND     $0F             
6FDA: 3E 08      LD      A,$08           
6FDC: B6         OR      (HL)            
6FDD: 28 02      JR      Z,$6FE1         
6FDF: 3E 20      LD      A,$20           
6FE1: CD 17 7E   CALL    $7E17           
6FE4: F0 D7      LD      A,($D7)         
6FE6: 2F         CPL                     
6FE7: 3C         INC     A               
6FE8: 21 00 C4   LD      HL,$C400        
6FEB: 09         ADD     HL,BC           
6FEC: 77         LD      (HL),A          
6FED: F0 D8      LD      A,($D8)         
6FEF: 2F         CPL                     
6FF0: 3C         INC     A               
6FF1: 21 F0 C3   LD      HL,$C3F0        
6FF4: 09         ADD     HL,BC           
6FF5: 77         LD      (HL),A          
6FF6: CD DF 73   CALL    $73DF           
6FF9: C9         RET                     
6FFA: 00         NOP                     
6FFB: 01 02 03   LD      BC,$0302        
6FFE: F0 EB      LD      A,($EB)         
7000: FE E2      CP      $E2             
7002: C8         RET     Z               
7003: FE E6      CP      $E6             
7005: 20 28      JR      NZ,$702F        
7007: FA 19 D2   LD      A,($D219)       
700A: C7         RST     0X00            
700B: 13         INC     DE              
700C: 4D         LD      C,L             
700D: 17         RLA                     
700E: 70         LD      (HL),B          
700F: 1D         DEC     E               
7010: 70         LD      (HL),B          
7011: 2D         DEC     L               
7012: 70         LD      (HL),B          
7013: 2D         DEC     L               
7014: 70         LD      (HL),B          
7015: 59         LD      E,C             
7016: 70         LD      (HL),B          
7017: CD 8D 3B   CALL    $3B8D           
701A: 36 06      LD      (HL),$06        
701C: C9         RET                     
701D: FA 21 C1   LD      A,($C121)       
7020: A7         AND     A               
7021: 20 06      JR      NZ,$7029        
7023: FA 6A C1   LD      A,($C16A)       
7026: FE 04      CP      $04             
7028: D0         RET     NC              
7029: CD 8D 3B   CALL    $3B8D           
702C: C9         RET                     
702D: F0 EB      LD      A,($EB)         
702F: FE B9      CP      $B9             
7031: 20 26      JR      NZ,$7059        
7033: F0 EA      LD      A,($EA)         
7035: FE 05      CP      $05             
7037: 20 20      JR      NZ,$7059        
7039: CD 8D 3B   CALL    $3B8D           
703C: 36 01      LD      (HL),$01        
703E: CD 91 08   CALL    $0891           
7041: 36 40      LD      (HL),$40        
7043: 3E 40      LD      A,$40           
7045: EA 64 D4   LD      ($D464),A       
7048: AF         XOR     A               
7049: EA 37 C1   LD      ($C137),A       
704C: EA 6A C1   LD      ($C16A),A       
704F: EA 21 C1   LD      ($C121),A       
7052: 3E 1C      LD      A,$1C           
7054: E0 F4      LDFF00  ($F4),A         
7056: C3 F1 6C   JP      $6CF1           
7059: F0 EB      LD      A,($EB)         
705B: FE 55      CP      $55             
705D: 20 27      JR      NZ,$7086        
705F: 3E 30      LD      A,$30           
7061: CD 17 7E   CALL    $7E17           
7064: F0 D7      LD      A,($D7)         
7066: 2F         CPL                     
7067: 3C         INC     A               
7068: 21 50 C2   LD      HL,$C250        
706B: 09         ADD     HL,BC           
706C: 77         LD      (HL),A          
706D: F0 D8      LD      A,($D8)         
706F: 2F         CPL                     
7070: 3C         INC     A               
7071: 21 40 C2   LD      HL,$C240        
7074: 09         ADD     HL,BC           
7075: 77         LD      (HL),A          
7076: CD 8D 3B   CALL    $3B8D           
7079: 36 02      LD      (HL),$02        
707B: CD 91 08   CALL    $0891           
707E: 36 40      LD      (HL),$40        
7080: CD 8C 08   CALL    $088C           
7083: 36 08      LD      (HL),$08        
7085: C9         RET                     
7086: FE 65      CP      $65             
7088: 20 0A      JR      NZ,$7094        
708A: CD F4 6D   CALL    $6DF4           
708D: 3E 08      LD      A,$08           
708F: EA 3E C1   LD      ($C13E),A       
7092: 18 3D      JR      $70D1           
7094: FE 5B      CP      $5B             
7096: 20 39      JR      NZ,$70D1        
7098: F0 E8      LD      A,($E8)         
709A: A7         AND     A               
709B: 20 23      JR      NZ,$70C0        
709D: 21 B0 C2   LD      HL,$C2B0        
70A0: 09         ADD     HL,BC           
70A1: 7E         LD      A,(HL)          
70A2: FE 04      CP      $04             
70A4: C2 B4 70   JP      NZ,$70B4        
70A7: FA 4A C1   LD      A,($C14A)       
70AA: A7         AND     A               
70AB: 28 66      JR      Z,$7113         
70AD: 21 00 C3   LD      HL,$C300        
70B0: 09         ADD     HL,BC           
70B1: 36 0C      LD      (HL),$0C        
70B3: C9         RET                     
70B4: FA 4A C1   LD      A,($C14A)       
70B7: A7         AND     A               
70B8: 28 0A      JR      Z,$70C4         
70BA: CD F4 6D   CALL    $6DF4           
70BD: C3 13 71   JP      $7113           
70C0: CD F4 6D   CALL    $6DF4           
70C3: C9         RET                     
70C4: 3E 04      LD      A,$04           
70C6: EA 3E C1   LD      ($C13E),A       
70C9: 3E 10      LD      A,$10           
70CB: CD 69 75   CALL    $7569           
70CE: C3 13 71   JP      $7113           
70D1: 21 30 C4   LD      HL,$C430        
70D4: 09         ADD     HL,BC           
70D5: 7E         LD      A,(HL)          
70D6: E6 40      AND     $40             
70D8: 28 39      JR      Z,$7113         
70DA: F0 EB      LD      A,($EB)         
70DC: FE 51      CP      $51             
70DE: CA 19 6F   JP      Z,$6F19         
70E1: FE 5C      CP      $5C             
70E3: 20 13      JR      NZ,$70F8        
70E5: FA 7C D4   LD      A,($D47C)       
70E8: FE 01      CP      $01             
70EA: 3E 20      LD      A,$20           
70EC: 20 02      JR      NZ,$70F0        
70EE: 3E 30      LD      A,$30           
70F0: CD E1 6F   CALL    $6FE1           
70F3: 21 20 C4   LD      HL,$C420        
70F6: 09         ADD     HL,BC           
70F7: 70         LD      (HL),B          
70F8: 79         LD      A,C             
70F9: 3C         INC     A               
70FA: EA AC C1   LD      ($C1AC),A       
70FD: CD 93 09   CALL    $0993           
7100: 21 10 C4   LD      HL,$C410        
7103: 09         ADD     HL,BC           
7104: 36 10      LD      (HL),$10        
7106: 21 F0 C3   LD      HL,$C3F0        
7109: 09         ADD     HL,BC           
710A: 70         LD      (HL),B          
710B: 21 00 C4   LD      HL,$C400        
710E: 09         ADD     HL,BC           
710F: 70         LD      (HL),B          
7110: C3 F4 6D   JP      $6DF4           
7113: F0 EB      LD      A,($EB)         
7115: FE 8E      CP      $8E             
7117: 20 05      JR      NZ,$711E        
7119: CD 42 09   CALL    $0942           
711C: 18 41      JR      $715F           
711E: FE 24      CP      $24             
7120: 20 36      JR      NZ,$7158        
7122: 21 C0 C2   LD      HL,$C2C0        
7125: 09         ADD     HL,BC           
7126: 7E         LD      A,(HL)          
7127: A7         AND     A               
7128: 20 2E      JR      NZ,$7158        
712A: F0 9E      LD      A,($9E)         
712C: 5F         LD      E,A             
712D: 50         LD      D,B             
712E: 21 FA 6F   LD      HL,$6FFA        
7131: 19         ADD     HL,DE           
7132: 7E         LD      A,(HL)          
7133: 21 80 C3   LD      HL,$C380        
7136: 09         ADD     HL,BC           
7137: BE         CP      (HL)            
7138: 28 25      JR      Z,$715F         
713A: CD 42 09   CALL    $0942           
713D: 3E 10      LD      A,$10           
713F: EA 3E C1   LD      ($C13E),A       
7142: 3E 10      LD      A,$10           
7144: CD 69 75   CALL    $7569           
7147: 3E 10      LD      A,$10           
7149: CD E1 6F   CALL    $6FE1           
714C: F0 EE      LD      A,($EE)         
714E: E0 D7      LDFF00  ($D7),A         
7150: F0 EC      LD      A,($EC)         
7152: E0 D8      LDFF00  ($D8),A         
7154: CD A1 09   CALL    $09A1           
7157: C9         RET                     
7158: F0 EB      LD      A,($EB)         
715A: FE 15      CP      $15             
715C: CA EA 73   JP      Z,$73EA         
715F: 3E 01      LD      A,$01           
7161: EA 60 C1   LD      ($C160),A       
7164: FA 6A C1   LD      A,($C16A)       
7167: FE 05      CP      $05             
7169: 20 05      JR      NZ,$7170        
716B: 3E 0C      LD      A,$0C           
716D: EA 6D C1   LD      ($C16D),A       
7170: AF         XOR     A               
7171: EA 22 C1   LD      ($C122),A       
7174: 3E 30      LD      A,$30           
7176: CD E1 6F   CALL    $6FE1           
7179: 21 F2 FF   LD      HL,$FFF2        
717C: 36 09      LD      (HL),$09        
717E: FA 7C D4   LD      A,($D47C)       
7181: FE 01      CP      $01             
7183: 20 23      JR      NZ,$71A8        
7185: CD A8 71   CALL    $71A8           
7188: 21 10 C4   LD      HL,$C410        
718B: 09         ADD     HL,BC           
718C: 36 20      LD      (HL),$20        
718E: 21 A0 C4   LD      HL,$C4A0        
7191: 09         ADD     HL,BC           
7192: 36 01      LD      (HL),$01        
7194: 3E 11      LD      A,$11           
7196: E0 F3      LDFF00  ($F3),A         
7198: 21 80 C2   LD      HL,$C280        
719B: 09         ADD     HL,BC           
719C: 7E         LD      A,(HL)          
719D: FE 01      CP      $01             
719F: 20 06      JR      NZ,$71A7        
71A1: 21 80 C4   LD      HL,$C480        
71A4: 09         ADD     HL,BC           
71A5: 36 40      LD      (HL),$40        
71A7: C9         RET                     
71A8: 79         LD      A,C             
71A9: 3C         INC     A               
71AA: EA AC C1   LD      ($C1AC),A       
71AD: FA 7C D4   LD      A,($D47C)       
71B0: E6 01      AND     $01             
71B2: 21 21 C1   LD      HL,$C121        
71B5: B6         OR      (HL)            
71B6: 21 4A C1   LD      HL,$C14A        
71B9: B6         OR      (HL)            
71BA: FA 4E DB   LD      A,($DB4E)       
71BD: 28 01      JR      Z,$71C0         
71BF: 3C         INC     A               
71C0: 3D         DEC     A               
71C1: EA 9E C1   LD      ($C19E),A       
71C4: 21 D0 C4   LD      HL,$C4D0        
71C7: 09         ADD     HL,BC           
71C8: 5E         LD      E,(HL)          
71C9: 50         LD      D,B             
71CA: CB 23      SET     1,E             
71CC: CB 12      SET     1,E             
71CE: CB 23      SET     1,E             
71D0: CB 12      SET     1,E             
71D2: CB 23      SET     1,E             
71D4: CB 12      SET     1,E             
71D6: CB 23      SET     1,E             
71D8: CB 12      SET     1,E             
71DA: 21 8D 44   LD      HL,$448D        
71DD: 19         ADD     HL,DE           
71DE: FA 9E C1   LD      A,($C19E)       
71E1: 5F         LD      E,A             
71E2: 50         LD      D,B             
71E3: 19         ADD     HL,DE           
71E4: 5E         LD      E,(HL)          
71E5: D5         PUSH    DE              
71E6: FA 9E C1   LD      A,($C19E)       
71E9: 17         RLA                     
71EA: 17         RLA                     
71EB: 17         RLA                     
71EC: E6 F8      AND     $F8             
71EE: 5F         LD      E,A             
71EF: 21 9D 47   LD      HL,$479D        
71F2: 19         ADD     HL,DE           
71F3: D1         POP     DE              
71F4: 19         ADD     HL,DE           
71F5: 7E         LD      A,(HL)          
71F6: A7         AND     A               
71F7: C8         RET     Z               
71F8: F5         PUSH    AF              
71F9: F0 EB      LD      A,($EB)         
71FB: FE E6      CP      $E6             
71FD: 20 1A      JR      NZ,$7219        
71FF: FA 19 D2   LD      A,($D219)       
7202: FE 04      CP      $04             
7204: 20 13      JR      NZ,$7219        
7206: FA 4A C1   LD      A,($C14A)       
7209: F5         PUSH    AF              
720A: CD F4 6D   CALL    $6DF4           
720D: F1         POP     AF              
720E: A7         AND     A               
720F: 20 08      JR      NZ,$7219        
7211: FA 21 C1   LD      A,($C121)       
7214: A7         AND     A               
7215: 20 02      JR      NZ,$7219        
7217: F1         POP     AF              
7218: C9         RET                     
7219: 21 30 C4   LD      HL,$C430        
721C: 09         ADD     HL,BC           
721D: 7E         LD      A,(HL)          
721E: 21 F2 FF   LD      HL,$FFF2        
7221: 36 03      LD      (HL),$03        
7223: E6 80      AND     $80             
7225: 28 05      JR      Z,$722C         
7227: 21 F3 FF   LD      HL,$FFF3        
722A: 36 07      LD      (HL),$07        
722C: 21 A0 C3   LD      HL,$C3A0        
722F: 09         ADD     HL,BC           
7230: 7E         LD      A,(HL)          
7231: FE 6C      CP      $6C             
7233: 20 04      JR      NZ,$7239        
7235: 3E 13      LD      A,$13           
7237: E0 F3      LDFF00  ($F3),A         
7239: F1         POP     AF              
723A: FE F0      CP      $F0             
723C: 38 7B      JR      C,$72B9         
723E: FE FE      CP      $FE             
7240: 20 22      JR      NZ,$7264        
7242: 21 F4 FF   LD      HL,$FFF4        
7245: 36 12      LD      (HL),$12        
7247: CD DF 73   CALL    $73DF           
724A: 21 80 C2   LD      HL,$C280        
724D: 09         ADD     HL,BC           
724E: 36 03      LD      (HL),$03        
7250: CD 91 08   CALL    $0891           
7253: 36 60      LD      (HL),$60        
7255: 21 40 C3   LD      HL,$C340        
7258: 09         ADD     HL,BC           
7259: 34         INC     (HL)            
725A: 34         INC     (HL)            
725B: 21 30 C4   LD      HL,$C430        
725E: 09         ADD     HL,BC           
725F: 7E         LD      A,(HL)          
7260: E6 C2      AND     $C2             
7262: 77         LD      (HL),A          
7263: C9         RET                     
7264: FE FF      CP      $FF             
7266: 20 15      JR      NZ,$727D        
7268: CD DF 73   CALL    $73DF           
726B: 21 80 C2   LD      HL,$C280        
726E: 09         ADD     HL,BC           
726F: 36 06      LD      (HL),$06        
7271: 21 00 C3   LD      HL,$C300        
7274: 09         ADD     HL,BC           
7275: 36 FF      LD      (HL),$FF        
7277: 21 20 C3   LD      HL,$C320        
727A: 09         ADD     HL,BC           
727B: 70         LD      (HL),B          
727C: C9         RET                     
727D: FE FD      CP      $FD             
727F: 20 37      JR      NZ,$72B8        
7281: 21 A0 C3   LD      HL,$C3A0        
7284: 09         ADD     HL,BC           
7285: 7E         LD      A,(HL)          
7286: FE B9      CP      $B9             
7288: 20 0B      JR      NZ,$7295        
728A: 21 B0 C2   LD      HL,$C2B0        
728D: 09         ADD     HL,BC           
728E: 7E         LD      A,(HL)          
728F: A7         AND     A               
7290: 20 26      JR      NZ,$72B8        
7292: 34         INC     (HL)            
7293: 18 0A      JR      $729F           
7295: 36 2F      LD      (HL),$2F        
7297: CD B0 48   CALL    $48B0           
729A: CD 87 08   CALL    $0887           
729D: 36 80      LD      (HL),$80        
729F: 21 00 C2   LD      HL,$C200        
72A2: 09         ADD     HL,BC           
72A3: 7E         LD      A,(HL)          
72A4: E0 D7      LDFF00  ($D7),A         
72A6: 21 10 C2   LD      HL,$C210        
72A9: 09         ADD     HL,BC           
72AA: 7E         LD      A,(HL)          
72AB: 21 10 C3   LD      HL,$C310        
72AE: 09         ADD     HL,BC           
72AF: 96         SUB     (HL)            
72B0: E0 D8      LDFF00  ($D8),A         
72B2: 3E 02      LD      A,$02           
72B4: CD 53 09   CALL    $0953           
72B7: C9         RET                     
72B8: C9         RET                     
72B9: 5F         LD      E,A             
72BA: 21 60 C3   LD      HL,$C360        
72BD: 09         ADD     HL,BC           
72BE: 7E         LD      A,(HL)          
72BF: 93         SUB     E               
72C0: 77         LD      (HL),A          
72C1: 38 03      JR      C,$72C6         
72C3: C2 BA 73   JP      NZ,$73BA        
72C6: 21 80 C2   LD      HL,$C280        
72C9: 09         ADD     HL,BC           
72CA: 36 01      LD      (HL),$01        
72CC: 21 30 C4   LD      HL,$C430        
72CF: 09         ADD     HL,BC           
72D0: 7E         LD      A,(HL)          
72D1: CB 7F      SET     1,E             
72D3: 28 6D      JR      Z,$7342         
72D5: CB 57      SET     1,E             
72D7: 20 2F      JR      NZ,$7308        
72D9: 1E 0F      LD      E,$0F           
72DB: 50         LD      D,B             
72DC: 7B         LD      A,E             
72DD: B9         CP      C               
72DE: 28 12      JR      Z,$72F2         
72E0: 21 80 C2   LD      HL,$C280        
72E3: 19         ADD     HL,DE           
72E4: 7E         LD      A,(HL)          
72E5: FE 05      CP      $05             
72E7: 20 09      JR      NZ,$72F2        
72E9: 21 30 C4   LD      HL,$C430        
72EC: 19         ADD     HL,DE           
72ED: 7E         LD      A,(HL)          
72EE: E6 80      AND     $80             
72F0: 20 16      JR      NZ,$7308        
72F2: 1D         DEC     E               
72F3: 7B         LD      A,E             
72F4: FE FF      CP      $FF             
72F6: 20 E4      JR      NZ,$72DC        
72F8: FA AF DB   LD      A,($DBAF)       
72FB: F5         PUSH    AF              
72FC: 3E 03      LD      A,$03           
72FE: CD B9 07   CALL    $07B9           
7301: CD D2 27   CALL    $27D2           
7304: F1         POP     AF              
7305: EA AF DB   LD      ($DBAF),A       
7308: 3E 03      LD      A,$03           
730A: EA A7 C5   LD      ($C5A7),A       
730D: 21 C0 C2   LD      HL,$C2C0        
7310: 09         ADD     HL,BC           
7311: 70         LD      (HL),B          
7312: 21 A0 C3   LD      HL,$C3A0        
7315: 09         ADD     HL,BC           
7316: 7E         LD      A,(HL)          
7317: 1E B7      LD      E,$B7           
7319: FE 5A      CP      $5A             
731B: 28 0C      JR      Z,$7329         
731D: 1E B9      LD      E,$B9           
731F: FE 63      CP      $63             
7321: 28 11      JR      Z,$7334         
7323: 1E BD      LD      E,$BD           
7325: FE 62      CP      $62             
7327: 20 19      JR      NZ,$7342        
7329: 7B         LD      A,E             
732A: CD 97 21   CALL    $2197           
732D: 3E 5E      LD      A,$5E           
732F: EA 68 D3   LD      ($D368),A       
7332: 18 0E      JR      $7342           
7334: F0 99      LD      A,($99)         
7336: F5         PUSH    AF              
7337: 3E 10      LD      A,$10           
7339: E0 99      LDFF00  ($99),A         
733B: 7B         LD      A,E             
733C: CD 97 21   CALL    $2197           
733F: F1         POP     AF              
7340: E0 99      LDFF00  ($99),A         
7342: CD 8D 3B   CALL    $3B8D           
7345: 70         LD      (HL),B          
7346: 21 80 C4   LD      HL,$C480        
7349: 09         ADD     HL,BC           
734A: 36 2F      LD      (HL),$2F        
734C: 21 20 C4   LD      HL,$C420        
734F: 09         ADD     HL,BC           
7350: AF         XOR     A               
7351: 77         LD      (HL),A          
7352: 21 30 C4   LD      HL,$C430        
7355: 09         ADD     HL,BC           
7356: 7E         LD      A,(HL)          
7357: E6 80      AND     $80             
7359: 20 0A      JR      NZ,$7365        
735B: 21 40 C3   LD      HL,$C340        
735E: 09         ADD     HL,BC           
735F: 7E         LD      A,(HL)          
7360: E6 F0      AND     $F0             
7362: F6 04      OR      $04             
7364: 77         LD      (HL),A          
7365: 21 A0 C3   LD      HL,$C3A0        
7368: 09         ADD     HL,BC           
7369: 7E         LD      A,(HL)          
736A: FE 12      CP      $12             
736C: 20 4C      JR      NZ,$73BA        
736E: 1E 0F      LD      E,$0F           
7370: 50         LD      D,B             
7371: 7B         LD      A,E             
7372: B9         CP      C               
7373: 28 39      JR      Z,$73AE         
7375: 21 A0 C3   LD      HL,$C3A0        
7378: 19         ADD     HL,DE           
7379: 7E         LD      A,(HL)          
737A: FE 10      CP      $10             
737C: 28 04      JR      Z,$7382         
737E: FE 11      CP      $11             
7380: 20 2C      JR      NZ,$73AE        
7382: 21 90 C2   LD      HL,$C290        
7385: 19         ADD     HL,DE           
7386: 7E         LD      A,(HL)          
7387: A7         AND     A               
7388: 20 24      JR      NZ,$73AE        
738A: 21 80 C2   LD      HL,$C280        
738D: 19         ADD     HL,DE           
738E: 7E         LD      A,(HL)          
738F: A7         AND     A               
7390: 28 1C      JR      Z,$73AE         
7392: 36 01      LD      (HL),$01        
7394: 21 80 C4   LD      HL,$C480        
7397: 19         ADD     HL,DE           
7398: 36 1F      LD      (HL),$1F        
739A: CD ED 27   CALL    $27ED           
739D: E6 03      AND     $03             
739F: C5         PUSH    BC              
73A0: 4F         LD      C,A             
73A1: 06 00      LD      B,$00           
73A3: 21 EB 73   LD      HL,$73EB        
73A6: 09         ADD     HL,BC           
73A7: 7E         LD      A,(HL)          
73A8: 21 E0 C4   LD      HL,$C4E0        
73AB: 19         ADD     HL,DE           
73AC: 77         LD      (HL),A          
73AD: C1         POP     BC              
73AE: 1D         DEC     E               
73AF: 7B         LD      A,E             
73B0: FE FF      CP      $FF             
73B2: 20 BD      JR      NZ,$7371        
73B4: 21 E0 C4   LD      HL,$C4E0        
73B7: 09         ADD     HL,BC           
73B8: 36 2E      LD      (HL),$2E        
73BA: 21 A0 C3   LD      HL,$C3A0        
73BD: 09         ADD     HL,BC           
73BE: 7E         LD      A,(HL)          
73BF: 21 20 C4   LD      HL,$C420        
73C2: 09         ADD     HL,BC           
73C3: FE E6      CP      $E6             
73C5: 20 09      JR      NZ,$73D0        
73C7: FA 19 D2   LD      A,($D219)       
73CA: FE 03      CP      $03             
73CC: 28 06      JR      Z,$73D4         
73CE: 18 0D      JR      $73DD           
73D0: FE 59      CP      $59             
73D2: 20 09      JR      NZ,$73DD        
73D4: 36 28      LD      (HL),$28        
73D6: 21 00 C3   LD      HL,$C300        
73D9: 09         ADD     HL,BC           
73DA: 36 C8      LD      (HL),$C8        
73DC: C9         RET                     
73DD: 36 18      LD      (HL),$18        
73DF: 21 A0 C4   LD      HL,$C4A0        
73E2: 09         ADD     HL,BC           
73E3: 70         LD      (HL),B          
73E4: 21 10 C4   LD      HL,$C410        
73E7: 09         ADD     HL,BC           
73E8: 36 0A      LD      (HL),$0A        
73EA: C9         RET                     
73EB: 2D         DEC     L               
73EC: 2E 38      LD      L,$38           
73EE: 37         SCF                     
73EF: 21 AC C1   LD      HL,$C1AC        
73F2: FA 3E C1   LD      A,($C13E)       
73F5: B6         OR      (HL)            
73F6: 21 B6 FF   LD      HL,$FFB6        
73F9: B6         OR      (HL)            
73FA: 21 21 C1   LD      HL,$C121        
73FD: B6         OR      (HL)            
73FE: C2 E5 74   JP      NZ,$74E5        
7401: FA 40 C1   LD      A,($C140)       
7404: FE 00      CP      $00             
7406: CA E5 74   JP      Z,$74E5         
7409: 21 80 C3   LD      HL,$C380        
740C: 09         ADD     HL,BC           
740D: F0 9E      LD      A,($9E)         
740F: BE         CP      (HL)            
7410: CA E5 74   JP      Z,$74E5         
7413: 11 EE FF   LD      DE,$FFEE        
7416: 21 C0 D5   LD      HL,$D5C0        
7419: 1A         LD      A,(DE)          
741A: 86         ADD     A,(HL)          
741B: E5         PUSH    HL              
741C: 21 40 C1   LD      HL,$C140        
741F: 96         SUB     (HL)            
7420: FE 80      CP      $80             
7422: 38 02      JR      C,$7426         
7424: 2F         CPL                     
7425: 3C         INC     A               
7426: E1         POP     HL              
7427: F5         PUSH    AF              
7428: 23         INC     HL              
7429: FA 41 C1   LD      A,($C141)       
742C: 86         ADD     A,(HL)          
742D: 5F         LD      E,A             
742E: F1         POP     AF              
742F: BB         CP      E               
7430: D2 E5 74   JP      NC,$74E5        
7433: 23         INC     HL              
7434: 11 EC FF   LD      DE,$FFEC        
7437: 1A         LD      A,(DE)          
7438: 86         ADD     A,(HL)          
7439: E5         PUSH    HL              
743A: 21 42 C1   LD      HL,$C142        
743D: 96         SUB     (HL)            
743E: FE 80      CP      $80             
7440: 38 02      JR      C,$7444         
7442: 2F         CPL                     
7443: 3C         INC     A               
7444: E1         POP     HL              
7445: F5         PUSH    AF              
7446: 23         INC     HL              
7447: FA 43 C1   LD      A,($C143)       
744A: 86         ADD     A,(HL)          
744B: 5F         LD      E,A             
744C: F1         POP     AF              
744D: BB         CP      E               
744E: D2 E5 74   JP      NC,$74E5        
7451: CD 42 09   CALL    $0942           
7454: 3E 08      LD      A,$08           
7456: EA 3E C1   LD      ($C13E),A       
7459: 3E 12      LD      A,$12           
745B: CD 69 75   CALL    $7569           
745E: 3E 18      LD      A,$18           
7460: CD 17 7E   CALL    $7E17           
7463: F0 D7      LD      A,($D7)         
7465: 2F         CPL                     
7466: 3C         INC     A               
7467: 21 00 C4   LD      HL,$C400        
746A: 09         ADD     HL,BC           
746B: 77         LD      (HL),A          
746C: F0 D8      LD      A,($D8)         
746E: 2F         CPL                     
746F: 3C         INC     A               
7470: 21 F0 C3   LD      HL,$C3F0        
7473: 09         ADD     HL,BC           
7474: 77         LD      (HL),A          
7475: CD DF 73   CALL    $73DF           
7478: 36 08      LD      (HL),$08        
747A: AF         XOR     A               
747B: EA 22 C1   LD      ($C122),A       
747E: CD DC 08   CALL    $08DC           
7481: 21 21 C1   LD      HL,$C121        
7484: FA 6A C1   LD      A,($C16A)       
7487: B6         OR      (HL)            
7488: 28 05      JR      Z,$748F         
748A: 3E 0C      LD      A,$0C           
748C: EA 6D C1   LD      ($C16D),A       
748F: F0 EB      LD      A,($EB)         
7491: FE BE      CP      $BE             
7493: 20 30      JR      NZ,$74C5        
7495: 3E 09      LD      A,$09           
7497: E0 F2      LDFF00  ($F2),A         
7499: FA 05 D2   LD      A,($D205)       
749C: FE 00      CP      $00             
749E: 28 23      JR      Z,$74C3         
74A0: FE 01      CP      $01             
74A2: 28 15      JR      Z,$74B9         
74A4: FE 04      CP      $04             
74A6: 28 11      JR      Z,$74B9         
74A8: FE 03      CP      $03             
74AA: CA 75 75   JP      Z,$7575         
74AD: 3E 20      LD      A,$20           
74AF: EA 3E C1   LD      ($C13E),A       
74B2: 3E 20      LD      A,$20           
74B4: CD 69 75   CALL    $7569           
74B7: 18 27      JR      $74E0           
74B9: 3E 10      LD      A,$10           
74BB: EA 3E C1   LD      ($C13E),A       
74BE: 3E 20      LD      A,$20           
74C0: CD 69 75   CALL    $7569           
74C3: 18 1B      JR      $74E0           
74C5: F0 9E      LD      A,($9E)         
74C7: 5F         LD      E,A             
74C8: 50         LD      D,B             
74C9: 21 E8 74   LD      HL,$74E8        
74CC: 19         ADD     HL,DE           
74CD: FA 40 C1   LD      A,($C140)       
74D0: 86         ADD     A,(HL)          
74D1: E0 D7      LDFF00  ($D7),A         
74D3: 21 EC 74   LD      HL,$74EC        
74D6: 19         ADD     HL,DE           
74D7: FA 42 C1   LD      A,($C142)       
74DA: 86         ADD     A,(HL)          
74DB: E0 D8      LDFF00  ($D8),A         
74DD: CD A1 09   CALL    $09A1           
74E0: 3E 0C      LD      A,$0C           
74E2: E0 B6      LDFF00  ($B6),A         
74E4: C9         RET                     
74E5: C3 F0 74   JP      $74F0           
74E8: 00         NOP                     
74E9: F0 F8      LD      A,($F8)         
74EB: FC                              
74EC: FC                              
74ED: FC                              
74EE: F0 00      LD      A,($00)         
74F0: F0 E7      LD      A,($E7)         
74F2: A9         XOR     C               
74F3: 1F         RRA                     
74F4: 30 7E      JR      NC,$7574        
74F6: F0 98      LD      A,($98)         
74F8: C6 08      ADD     $08             
74FA: E0 D7      LDFF00  ($D7),A         
74FC: F0 99      LD      A,($99)         
74FE: C6 08      ADD     $08             
7500: E0 D9      LDFF00  ($D9),A         
7502: 11 EE FF   LD      DE,$FFEE        
7505: 21 C0 D5   LD      HL,$D5C0        
7508: 1A         LD      A,(DE)          
7509: 86         ADD     A,(HL)          
750A: E5         PUSH    HL              
750B: 21 D7 FF   LD      HL,$FFD7        
750E: 96         SUB     (HL)            
750F: FE 80      CP      $80             
7511: 38 02      JR      C,$7515         
7513: 2F         CPL                     
7514: 3C         INC     A               
7515: E1         POP     HL              
7516: F5         PUSH    AF              
7517: 23         INC     HL              
7518: 3E 04      LD      A,$04           
751A: 86         ADD     A,(HL)          
751B: 5F         LD      E,A             
751C: F1         POP     AF              
751D: BB         CP      E               
751E: 30 54      JR      NC,$7574        
7520: 23         INC     HL              
7521: 11 EC FF   LD      DE,$FFEC        
7524: 1A         LD      A,(DE)          
7525: 86         ADD     A,(HL)          
7526: E5         PUSH    HL              
7527: 21 D9 FF   LD      HL,$FFD9        
752A: 96         SUB     (HL)            
752B: FE 80      CP      $80             
752D: 38 02      JR      C,$7531         
752F: 2F         CPL                     
7530: 3C         INC     A               
7531: E1         POP     HL              
7532: F5         PUSH    AF              
7533: 23         INC     HL              
7534: 3E 05      LD      A,$05           
7536: 86         ADD     A,(HL)          
7537: 5F         LD      E,A             
7538: F1         POP     AF              
7539: BB         CP      E               
753A: 30 38      JR      NC,$7574        
753C: FA C7 DB   LD      A,($DBC7)       
753F: A7         AND     A               
7540: 20 32      JR      NZ,$7574        
7542: CD F1 6C   CALL    $6CF1           
7545: F0 EB      LD      A,($EB)         
7547: FE BE      CP      $BE             
7549: 20 29      JR      NZ,$7574        
754B: FA 05 D2   LD      A,($D205)       
754E: A7         AND     A               
754F: 28 23      JR      Z,$7574         
7551: FE 01      CP      $01             
7553: 28 1F      JR      Z,$7574         
7555: FE 04      CP      $04             
7557: 28 1B      JR      Z,$7574         
7559: FE 02      CP      $02             
755B: 20 18      JR      NZ,$7575        
755D: CD 8C 08   CALL    $088C           
7560: 36 A0      LD      (HL),$A0        
7562: 3E 20      LD      A,$20           
7564: EA 3E C1   LD      ($C13E),A       
7567: 3E 30      LD      A,$30           
7569: CD 17 7E   CALL    $7E17           
756C: F0 D7      LD      A,($D7)         
756E: E0 9B      LDFF00  ($9B),A         
7570: F0 D8      LD      A,($D8)         
7572: E0 9A      LDFF00  ($9A),A         
7574: C9         RET                     
7575: 21 D0 C3   LD      HL,$C3D0        
7578: 09         ADD     HL,BC           
7579: 7E         LD      A,(HL)          
757A: FE 22      CP      $22             
757C: 38 F6      JR      C,$7574         
757E: 3E 0A      LD      A,$0A           
7580: EA 1C C1   LD      ($C11C),A       
7583: 21 80 C3   LD      HL,$C380        
7586: 09         ADD     HL,BC           
7587: 7E         LD      A,(HL)          
7588: A7         AND     A               
7589: 3E 30      LD      A,$30           
758B: 28 02      JR      Z,$758F         
758D: 3E D0      LD      A,$D0           
758F: E0 9A      LDFF00  ($9A),A         
7591: AF         XOR     A               
7592: E0 9B      LDFF00  ($9B),A         
7594: 3E 30      LD      A,$30           
7596: E0 A3      LDFF00  ($A3),A         
7598: 3E 0B      LD      A,$0B           
759A: E0 F2      LDFF00  ($F2),A         
759C: C9         RET                     
759D: 3E 20      LD      A,$20           
759F: EA 3E C1   LD      ($C13E),A       
75A2: 3E 20      LD      A,$20           
75A4: 18 C3      JR      $7569           
75A6: 1E 0F      LD      E,$0F           
75A8: 16 00      LD      D,$00           
75AA: 7B         LD      A,E             
75AB: B9         CP      C               
75AC: CA 9D 77   JP      Z,$779D         
75AF: F0 E7      LD      A,($E7)         
75B1: AB         XOR     E               
75B2: E6 01      AND     $01             
75B4: C2 9D 77   JP      NZ,$779D        
75B7: 21 80 C2   LD      HL,$C280        
75BA: 19         ADD     HL,DE           
75BB: 7E         LD      A,(HL)          
75BC: FE 05      CP      $05             
75BE: DA 9D 77   JP      C,$779D         
75C1: 21 40 C3   LD      HL,$C340        
75C4: 19         ADD     HL,DE           
75C5: 7E         LD      A,(HL)          
75C6: E6 40      AND     $40             
75C8: C2 9D 77   JP      NZ,$779D        
75CB: 21 00 C2   LD      HL,$C200        
75CE: 19         ADD     HL,DE           
75CF: F0 EE      LD      A,($EE)         
75D1: 96         SUB     (HL)            
75D2: C6 0C      ADD     $0C             
75D4: FE 18      CP      $18             
75D6: D2 9D 77   JP      NC,$779D        
75D9: 21 10 C2   LD      HL,$C210        
75DC: 19         ADD     HL,DE           
75DD: 7E         LD      A,(HL)          
75DE: 21 10 C3   LD      HL,$C310        
75E1: 19         ADD     HL,DE           
75E2: 96         SUB     (HL)            
75E3: 21 EC FF   LD      HL,$FFEC        
75E6: 96         SUB     (HL)            
75E7: C6 0C      ADD     $0C             
75E9: FE 18      CP      $18             
75EB: D2 9D 77   JP      NC,$779D        
75EE: 21 B0 C3   LD      HL,$C3B0        
75F1: 19         ADD     HL,DE           
75F2: 7E         LD      A,(HL)          
75F3: FE FF      CP      $FF             
75F5: CA 9D 77   JP      Z,$779D         
75F8: F0 EB      LD      A,($EB)         
75FA: FE 55      CP      $55             
75FC: 20 04      JR      NZ,$7602        
75FE: CD 91 08   CALL    $0891           
7601: 70         LD      (HL),B          
7602: 21 A0 C3   LD      HL,$C3A0        
7605: 19         ADD     HL,DE           
7606: 7E         LD      A,(HL)          
7607: FE 55      CP      $55             
7609: 20 29      JR      NZ,$7634        
760B: 21 40 C2   LD      HL,$C240        
760E: 09         ADD     HL,BC           
760F: 7E         LD      A,(HL)          
7610: 21 40 C2   LD      HL,$C240        
7613: 19         ADD     HL,DE           
7614: 77         LD      (HL),A          
7615: 21 50 C2   LD      HL,$C250        
7618: 09         ADD     HL,BC           
7619: 7E         LD      A,(HL)          
761A: 21 50 C2   LD      HL,$C250        
761D: 19         ADD     HL,DE           
761E: 77         LD      (HL),A          
761F: 21 E0 C2   LD      HL,$C2E0        
7622: 19         ADD     HL,DE           
7623: 36 40      LD      (HL),$40        
7625: 21 90 C2   LD      HL,$C290        
7628: 19         ADD     HL,DE           
7629: 36 02      LD      (HL),$02        
762B: 21 F0 C2   LD      HL,$C2F0        
762E: 19         ADD     HL,DE           
762F: 36 08      LD      (HL),$08        
7631: C3 9D 77   JP      $779D           
7634: 21 40 C3   LD      HL,$C340        
7637: 19         ADD     HL,DE           
7638: 7E         LD      A,(HL)          
7639: E6 20      AND     $20             
763B: C2 19 77   JP      NZ,$7719        
763E: F0 EB      LD      A,($EB)         
7640: FE 08      CP      $08             
7642: 28 28      JR      Z,$766C         
7644: 21 A0 C3   LD      HL,$C3A0        
7647: 19         ADD     HL,DE           
7648: 7E         LD      A,(HL)          
7649: FE E6      CP      $E6             
764B: 20 0D      JR      NZ,$765A        
764D: FA 19 D2   LD      A,($D219)       
7650: FE 05      CP      $05             
7652: 20 06      JR      NZ,$765A        
7654: F0 F1      LD      A,($F1)         
7656: FE 02      CP      $02             
7658: 20 09      JR      NZ,$7663        
765A: 21 50 C3   LD      HL,$C350        
765D: 19         ADD     HL,DE           
765E: 7E         LD      A,(HL)          
765F: E6 80      AND     $80             
7661: 28 09      JR      Z,$766C         
7663: 21 A0 C2   LD      HL,$C2A0        
7666: 09         ADD     HL,BC           
7667: 36 01      LD      (HL),$01        
7669: C3 3B 77   JP      $773B           
766C: F0 EB      LD      A,($EB)         
766E: FE 08      CP      $08             
7670: 20 3E      JR      NZ,$76B0        
7672: 21 A0 C3   LD      HL,$C3A0        
7675: 19         ADD     HL,DE           
7676: 7E         LD      A,(HL)          
7677: FE CA      CP      $CA             
7679: 20 09      JR      NZ,$7684        
767B: 21 90 C2   LD      HL,$C290        
767E: 19         ADD     HL,DE           
767F: 7E         LD      A,(HL)          
7680: A7         AND     A               
7681: 20 2D      JR      NZ,$76B0        
7683: 34         INC     (HL)            
7684: FE 3F      CP      $3F             
7686: 20 28      JR      NZ,$76B0        
7688: FA A5 DB   LD      A,($DBA5)       
768B: A7         AND     A               
768C: 20 22      JR      NZ,$76B0        
768E: 21 90 C2   LD      HL,$C290        
7691: 19         ADD     HL,DE           
7692: 7E         LD      A,(HL)          
7693: A7         AND     A               
7694: 20 1A      JR      NZ,$76B0        
7696: 34         INC     (HL)            
7697: 21 50 C4   LD      HL,$C450        
769A: 19         ADD     HL,DE           
769B: 36 7F      LD      (HL),$7F        
769D: 21 20 C4   LD      HL,$C420        
76A0: 19         ADD     HL,DE           
76A1: 36 10      LD      (HL),$10        
76A3: 3E 03      LD      A,$03           
76A5: EA AF DB   LD      ($DBAF),A       
76A8: CD D2 27   CALL    $27D2           
76AB: 3E 18      LD      A,$18           
76AD: EA AF DB   LD      ($DBAF),A       
76B0: 21 50 C3   LD      HL,$C350        
76B3: 19         ADD     HL,DE           
76B4: 7E         LD      A,(HL)          
76B5: E6 80      AND     $80             
76B7: C2 9D 77   JP      NZ,$779D        
76BA: 21 10 C4   LD      HL,$C410        
76BD: 19         ADD     HL,DE           
76BE: 7E         LD      A,(HL)          
76BF: A7         AND     A               
76C0: C2 9D 77   JP      NZ,$779D        
76C3: 21 A0 C3   LD      HL,$C3A0        
76C6: 19         ADD     HL,DE           
76C7: 7E         LD      A,(HL)          
76C8: FE 24      CP      $24             
76CA: 20 48      JR      NZ,$7714        
76CC: 21 80 C3   LD      HL,$C380        
76CF: 19         ADD     HL,DE           
76D0: 7E         LD      A,(HL)          
76D1: EE 01      XOR     $01             
76D3: 21 80 C3   LD      HL,$C380        
76D6: 09         ADD     HL,BC           
76D7: BE         CP      (HL)            
76D8: 20 3A      JR      NZ,$7714        
76DA: 21 C0 C2   LD      HL,$C2C0        
76DD: 19         ADD     HL,DE           
76DE: 7E         LD      A,(HL)          
76DF: A7         AND     A               
76E0: 20 32      JR      NZ,$7714        
76E2: F0 EB      LD      A,($EB)         
76E4: FE 03      CP      $03             
76E6: C2 63 76   JP      NZ,$7663        
76E9: 36 01      LD      (HL),$01        
76EB: D5         PUSH    DE              
76EC: 3E 32      LD      A,$32           
76EE: CD F8 64   CALL    $64F8           
76F1: 38 1E      JR      C,$7711         
76F3: F0 D7      LD      A,($D7)         
76F5: 21 00 C2   LD      HL,$C200        
76F8: 19         ADD     HL,DE           
76F9: 77         LD      (HL),A          
76FA: F0 D8      LD      A,($D8)         
76FC: 21 10 C2   LD      HL,$C210        
76FF: 19         ADD     HL,DE           
7700: 77         LD      (HL),A          
7701: 21 90 C3   LD      HL,$C390        
7704: 19         ADD     HL,DE           
7705: 79         LD      A,C             
7706: 3C         INC     A               
7707: 77         LD      (HL),A          
7708: F0 D9      LD      A,($D9)         
770A: E6 01      AND     $01             
770C: 21 B0 C3   LD      HL,$C3B0        
770F: 19         ADD     HL,DE           
7710: 77         LD      (HL),A          
7711: D1         POP     DE              
7712: 18 27      JR      $773B           
7714: CD A5 77   CALL    $77A5           
7717: 18 22      JR      $773B           
7719: F0 EB      LD      A,($EB)         
771B: FE 01      CP      $01             
771D: 28 04      JR      Z,$7723         
771F: FE 03      CP      $03             
7721: 20 15      JR      NZ,$7738        
7723: CD 91 08   CALL    $0891           
7726: AF         XOR     A               
7727: 77         LD      (HL),A          
7728: 21 40 C3   LD      HL,$C340        
772B: 19         ADD     HL,DE           
772C: 7E         LD      A,(HL)          
772D: E6 20      AND     $20             
772F: 28 0A      JR      Z,$773B         
7731: 79         LD      A,C             
7732: 3C         INC     A               
7733: 21 90 C3   LD      HL,$C390        
7736: 19         ADD     HL,DE           
7737: 77         LD      (HL),A          
7738: C3 9D 77   JP      $779D           
773B: F0 EB      LD      A,($EB)         
773D: FE A8      CP      $A8             
773F: 28 1D      JR      Z,$775E         
7741: FE 01      CP      $01             
7743: 28 53      JR      Z,$7798         
7745: FE 03      CP      $03             
7747: 28 4F      JR      Z,$7798         
7749: FE 05      CP      $05             
774B: 20 08      JR      NZ,$7755        
774D: D5         PUSH    DE              
774E: CD 41 54   CALL    $5441           
7751: D1         POP     DE              
7752: C3 9D 77   JP      $779D           
7755: 21 80 C2   LD      HL,$C280        
7758: 09         ADD     HL,BC           
7759: 7E         LD      A,(HL)          
775A: FE 08      CP      $08             
775C: 20 22      JR      NZ,$7780        
775E: 21 80 C4   LD      HL,$C480        
7761: 09         ADD     HL,BC           
7762: 7E         LD      A,(HL)          
7763: A7         AND     A               
7764: 20 37      JR      NZ,$779D        
7766: 36 0C      LD      (HL),$0C        
7768: 21 40 C2   LD      HL,$C240        
776B: 09         ADD     HL,BC           
776C: CB 2E      SET     1,E             
776E: CB 2E      SET     1,E             
7770: 7E         LD      A,(HL)          
7771: 2F         CPL                     
7772: 77         LD      (HL),A          
7773: 21 50 C2   LD      HL,$C250        
7776: 09         ADD     HL,BC           
7777: CB 2E      SET     1,E             
7779: CB 2E      SET     1,E             
777B: 7E         LD      A,(HL)          
777C: 2F         CPL                     
777D: 77         LD      (HL),A          
777E: 18 18      JR      $7798           
7780: 21 A0 C2   LD      HL,$C2A0        
7783: 09         ADD     HL,BC           
7784: 7E         LD      A,(HL)          
7785: A7         AND     A               
7786: 20 10      JR      NZ,$7798        
7788: F0 EB      LD      A,($EB)         
778A: FE 00      CP      $00             
778C: 20 05      JR      NZ,$7793        
778E: F0 F0      LD      A,($F0)         
7790: A7         AND     A               
7791: 20 03      JR      NZ,$7796        
7793: CD B7 3F   CALL    $3FB7           
7796: 18 05      JR      $779D           
7798: CD 91 08   CALL    $0891           
779B: AF         XOR     A               
779C: 77         LD      (HL),A          
779D: 1D         DEC     E               
779E: 7B         LD      A,E             
779F: FE FF      CP      $FF             
77A1: C2 AA 75   JP      NZ,$75AA        
77A4: C9         RET                     
77A5: F0 EB      LD      A,($EB)         
77A7: FE 00      CP      $00             
77A9: 20 0B      JR      NZ,$77B6        
77AB: F0 F0      LD      A,($F0)         
77AD: A7         AND     A               
77AE: 28 06      JR      Z,$77B6         
77B0: CD 91 08   CALL    $0891           
77B3: 36 03      LD      (HL),$03        
77B5: C9         RET                     
77B6: 21 40 C2   LD      HL,$C240        
77B9: 09         ADD     HL,BC           
77BA: 7E         LD      A,(HL)          
77BB: 21 F0 C3   LD      HL,$C3F0        
77BE: 19         ADD     HL,DE           
77BF: 77         LD      (HL),A          
77C0: 21 50 C2   LD      HL,$C250        
77C3: 09         ADD     HL,BC           
77C4: 7E         LD      A,(HL)          
77C5: 21 00 C4   LD      HL,$C400        
77C8: 19         ADD     HL,DE           
77C9: 77         LD      (HL),A          
77CA: C5         PUSH    BC              
77CB: D5         PUSH    DE              
77CC: C1         POP     BC              
77CD: D5         PUSH    DE              
77CE: CD D4 77   CALL    $77D4           
77D1: D1         POP     DE              
77D2: C1         POP     BC              
77D3: C9         RET                     
77D4: CD C4 71   CALL    $71C4           
77D7: C9         RET                     
77D8: 1E 0F      LD      E,$0F           
77DA: 16 00      LD      D,$00           
77DC: 21 80 C2   LD      HL,$C280        
77DF: 19         ADD     HL,DE           
77E0: 7E         LD      A,(HL)          
77E1: FE 05      CP      $05             
77E3: 38 4E      JR      C,$7833         
77E5: 21 40 C3   LD      HL,$C340        
77E8: 19         ADD     HL,DE           
77E9: 7E         LD      A,(HL)          
77EA: E6 60      AND     $60             
77EC: 20 45      JR      NZ,$7833        
77EE: 21 50 C3   LD      HL,$C350        
77F1: 19         ADD     HL,DE           
77F2: 7E         LD      A,(HL)          
77F3: E6 80      AND     $80             
77F5: 20 3C      JR      NZ,$7833        
77F7: 21 00 C2   LD      HL,$C200        
77FA: 19         ADD     HL,DE           
77FB: F0 EE      LD      A,($EE)         
77FD: 96         SUB     (HL)            
77FE: C6 18      ADD     $18             
7800: FE 30      CP      $30             
7802: 30 2F      JR      NC,$7833        
7804: 21 10 C2   LD      HL,$C210        
7807: 19         ADD     HL,DE           
7808: 7E         LD      A,(HL)          
7809: 21 10 C3   LD      HL,$C310        
780C: 19         ADD     HL,DE           
780D: 96         SUB     (HL)            
780E: 21 EC FF   LD      HL,$FFEC        
7811: 96         SUB     (HL)            
7812: C6 18      ADD     $18             
7814: FE 30      CP      $30             
7816: 30 1B      JR      NC,$7833        
7818: 3E 07      LD      A,$07           
781A: EA 9E C1   LD      ($C19E),A       
781D: CD A5 77   CALL    $77A5           
7820: 3E 30      LD      A,$30           
7822: CD 3A 78   CALL    $783A           
7825: 21 00 C4   LD      HL,$C400        
7828: 19         ADD     HL,DE           
7829: F0 D7      LD      A,($D7)         
782B: 77         LD      (HL),A          
782C: 21 F0 C3   LD      HL,$C3F0        
782F: 19         ADD     HL,DE           
7830: F0 D8      LD      A,($D8)         
7832: 77         LD      (HL),A          
7833: 1D         DEC     E               
7834: 7B         LD      A,E             
7835: FE FF      CP      $FF             
7837: 20 A3      JR      NZ,$77DC        
7839: C9         RET                     
783A: E0 D7      LDFF00  ($D7),A         
783C: F0 98      LD      A,($98)         
783E: F5         PUSH    AF              
783F: 21 00 C2   LD      HL,$C200        
7842: 19         ADD     HL,DE           
7843: 7E         LD      A,(HL)          
7844: E0 98      LDFF00  ($98),A         
7846: F0 99      LD      A,($99)         
7848: F5         PUSH    AF              
7849: 21 10 C2   LD      HL,$C210        
784C: 19         ADD     HL,DE           
784D: 7E         LD      A,(HL)          
784E: E0 99      LDFF00  ($99),A         
7850: D5         PUSH    DE              
7851: F0 D7      LD      A,($D7)         
7853: CD 17 7E   CALL    $7E17           
7856: D1         POP     DE              
7857: F1         POP     AF              
7858: E0 99      LDFF00  ($99),A         
785A: F1         POP     AF              
785B: E0 98      LDFF00  ($98),A         
785D: C9         RET                     
785E: 0D         DEC     C               
785F: 02         LD      (BC),A          
7860: 08 08 0A   LD      ($0A08),SP      
7863: 06 08      LD      B,$08           
7865: 08 10 FF   LD      ($FF10),SP      
7868: 08 08 0D   LD      ($0D08),SP      
786B: 02         LD      (BC),A          
786C: 08 08 08   LD      ($0808),SP      
786F: 08 02 0D   LD      ($0D02),SP      
7872: 08 08 06   LD      ($0608),SP      
7875: 0A         LD      A,(BC)          
7876: 08 08 FF   LD      ($FF08),SP      
7879: 10 08      STOP    $08             
787B: 08 02 0D   LD      ($0D02),SP      
787E: 01 02 04   LD      BC,$0402        
7881: 08 00 00   LD      ($0000),SP      
7884: FF         RST     0X38            
7885: 01 01 FF   LD      BC,$FF01        
7888: 01 FF 01   LD      BC,$01FF        
788B: FF         RST     0X38            
788C: 00         NOP                     
788D: 00         NOP                     
788E: 01 01 FF   LD      BC,$FF01        
7891: FF         RST     0X38            
7892: 21 70 C4   LD      HL,$C470        
7895: 09         ADD     HL,BC           
7896: 7E         LD      A,(HL)          
7897: E0 D7      LDFF00  ($D7),A         
7899: AF         XOR     A               
789A: 77         LD      (HL),A          
789B: E0 D8      LDFF00  ($D8),A         
789D: EA 03 C5   LD      ($C503),A       
78A0: EA 0D C5   LD      ($C50D),A       
78A3: 21 10 C3   LD      HL,$C310        
78A6: 09         ADD     HL,BC           
78A7: 7E         LD      A,(HL)          
78A8: CB 7F      SET     1,E             
78AA: 20 04      JR      NZ,$78B0        
78AC: A7         AND     A               
78AD: C2 17 7A   JP      NZ,$7A17        
78B0: 21 F0 C4   LD      HL,$C4F0        
78B3: 09         ADD     HL,BC           
78B4: 70         LD      (HL),B          
78B5: 21 30 C4   LD      HL,$C430        
78B8: 09         ADD     HL,BC           
78B9: 7E         LD      A,(HL)          
78BA: CB 67      SET     1,E             
78BC: C2 17 7A   JP      NZ,$7A17        
78BF: CD E0 7D   CALL    $7DE0           
78C2: 18 1E      JR      $78E2           
78C4: 1E 02      LD      E,$02           
78C6: F0 EB      LD      A,($EB)         
78C8: FE CC      CP      $CC             
78CA: 28 3A      JR      Z,$7906         
78CC: FE A0      CP      $A0             
78CE: 28 36      JR      Z,$7906         
78D0: FE D5      CP      $D5             
78D2: 28 32      JR      Z,$7906         
78D4: FE 6D      CP      $6D             
78D6: 28 2E      JR      Z,$7906         
78D8: FE C1      CP      $C1             
78DA: 28 2A      JR      Z,$7906         
78DC: CD B7 3F   CALL    $3FB7           
78DF: C3 5B 79   JP      $795B           
78E2: 1E 01      LD      E,$01           
78E4: F0 AF      LD      A,($AF)         
78E6: FE 67      CP      $67             
78E8: 28 1C      JR      Z,$7906         
78EA: F0 DA      LD      A,($DA)         
78EC: A7         AND     A               
78ED: CA 17 7A   JP      Z,$7A17         
78F0: FE 0B      CP      $0B             
78F2: 28 D0      JR      Z,$78C4         
78F4: FE 07      CP      $07             
78F6: 28 CC      JR      Z,$78C4         
78F8: FE B0      CP      $B0             
78FA: 28 0A      JR      Z,$7906         
78FC: 1C         INC     E               
78FD: FE 05      CP      $05             
78FF: 28 05      JR      Z,$7906         
7901: FE 06      CP      $06             
7903: 20 06      JR      NZ,$790B        
7905: 1C         INC     E               
7906: 21 70 C4   LD      HL,$C470        
7909: 09         ADD     HL,BC           
790A: 73         LD      (HL),E          
790B: 21 30 C4   LD      HL,$C430        
790E: 09         ADD     HL,BC           
790F: 7E         LD      A,(HL)          
7910: E6 08      AND     $08             
7912: 28 5E      JR      Z,$7972         
7914: 21 70 C4   LD      HL,$C470        
7917: 09         ADD     HL,BC           
7918: F0 D7      LD      A,($D7)         
791A: BE         CP      (HL)            
791B: 28 55      JR      Z,$7972         
791D: 7E         LD      A,(HL)          
791E: FE 03      CP      $03             
7920: 28 50      JR      Z,$7972         
7922: F0 D7      LD      A,($D7)         
7924: FE 03      CP      $03             
7926: 28 4A      JR      Z,$7972         
7928: F0 F9      LD      A,($F9)         
792A: A7         AND     A               
792B: 20 0F      JR      NZ,$793C        
792D: 21 20 C3   LD      HL,$C320        
7930: 09         ADD     HL,BC           
7931: 7E         LD      A,(HL)          
7932: CB 7F      SET     1,E             
7934: 28 3C      JR      Z,$7972         
7936: FE E7      CP      $E7             
7938: 30 38      JR      NC,$7972        
793A: 18 17      JR      $7953           
793C: F0 EB      LD      A,($EB)         
793E: FE AC      CP      $AC             
7940: 28 11      JR      Z,$7953         
7942: 21 50 C2   LD      HL,$C250        
7945: 09         ADD     HL,BC           
7946: 7E         LD      A,(HL)          
7947: CB 7F      SET     1,E             
7949: 20 08      JR      NZ,$7953        
794B: 36 00      LD      (HL),$00        
794D: 21 40 C2   LD      HL,$C240        
7950: 09         ADD     HL,BC           
7951: CB 2E      SET     1,E             
7953: 21 80 C4   LD      HL,$C480        
7956: 09         ADD     HL,BC           
7957: 7E         LD      A,(HL)          
7958: A7         AND     A               
7959: 20 17      JR      NZ,$7972        
795B: 21 00 C2   LD      HL,$C200        
795E: 09         ADD     HL,BC           
795F: 7E         LD      A,(HL)          
7960: E0 D7      LDFF00  ($D7),A         
7962: 21 10 C2   LD      HL,$C210        
7965: 09         ADD     HL,BC           
7966: 7E         LD      A,(HL)          
7967: E0 D8      LDFF00  ($D8),A         
7969: 3E 0E      LD      A,$0E           
796B: E0 F2      LDFF00  ($F2),A         
796D: 3E 01      LD      A,$01           
796F: CD 53 09   CALL    $0953           
7972: F0 DA      LD      A,($DA)         
7974: 3C         INC     A               
7975: FE F1      CP      $F1             
7977: 38 22      JR      C,$799B         
7979: D6 F1      SUB     $F1             
797B: 5F         LD      E,A             
797C: 50         LD      D,B             
797D: F0 E7      LD      A,($E7)         
797F: E6 03      AND     $03             
7981: 20 16      JR      NZ,$7999        
7983: 21 82 78   LD      HL,$7882        
7986: 19         ADD     HL,DE           
7987: 7E         LD      A,(HL)          
7988: 21 00 C2   LD      HL,$C200        
798B: 09         ADD     HL,BC           
798C: 86         ADD     A,(HL)          
798D: 77         LD      (HL),A          
798E: 21 8A 78   LD      HL,$788A        
7991: 19         ADD     HL,DE           
7992: 7E         LD      A,(HL)          
7993: 21 10 C2   LD      HL,$C210        
7996: 09         ADD     HL,BC           
7997: 86         ADD     A,(HL)          
7998: 77         LD      (HL),A          
7999: 18 7C      JR      $7A17           
799B: F0 AF      LD      A,($AF)         
799D: FE 61      CP      $61             
799F: 28 0A      JR      Z,$79AB         
79A1: F0 DA      LD      A,($DA)         
79A3: FE 50      CP      $50             
79A5: 28 04      JR      Z,$79AB         
79A7: FE 51      CP      $51             
79A9: 20 6C      JR      NZ,$7A17        
79AB: F0 EB      LD      A,($EB)         
79AD: FE 6D      CP      $6D             
79AF: 28 66      JR      Z,$7A17         
79B1: FE D5      CP      $D5             
79B3: 28 62      JR      Z,$7A17         
79B5: FE 36      CP      $36             
79B7: 28 5E      JR      Z,$7A17         
79B9: FE C1      CP      $C1             
79BB: 20 0D      JR      NZ,$79CA        
79BD: FA 1C C1   LD      A,($C11C)       
79C0: FE 06      CP      $06             
79C2: 20 53      JR      NZ,$7A17        
79C4: F0 AF      LD      A,($AF)         
79C6: FE 61      CP      $61             
79C8: 20 4D      JR      NZ,$7A17        
79CA: 21 10 C4   LD      HL,$C410        
79CD: 09         ADD     HL,BC           
79CE: 7E         LD      A,(HL)          
79CF: A7         AND     A               
79D0: 28 45      JR      Z,$7A17         
79D2: 35         DEC     (HL)            
79D3: 21 20 C4   LD      HL,$C420        
79D6: 09         ADD     HL,BC           
79D7: 36 00      LD      (HL),$00        
79D9: 21 80 C2   LD      HL,$C280        
79DC: 09         ADD     HL,BC           
79DD: 36 02      LD      (HL),$02        
79DF: F0 CE      LD      A,($CE)         
79E1: C6 08      ADD     $08             
79E3: 21 B0 C4   LD      HL,$C4B0        
79E6: 09         ADD     HL,BC           
79E7: 77         LD      (HL),A          
79E8: F0 CD      LD      A,($CD)         
79EA: C6 10      ADD     $10             
79EC: 21 C0 C4   LD      HL,$C4C0        
79EF: 09         ADD     HL,BC           
79F0: 77         LD      (HL),A          
79F1: CD 91 08   CALL    $0891           
79F4: 36 6F      LD      (HL),$6F        
79F6: F0 EB      LD      A,($EB)         
79F8: FE 14      CP      $14             
79FA: 28 1B      JR      Z,$7A17         
79FC: FE 0B      CP      $0B             
79FE: 28 17      JR      Z,$7A17         
7A00: FE 09      CP      $09             
7A02: 28 13      JR      Z,$7A17         
7A04: 36 48      LD      (HL),$48        
7A06: 21 10 C4   LD      HL,$C410        
7A09: 09         ADD     HL,BC           
7A0A: 7E         LD      A,(HL)          
7A0B: A7         AND     A               
7A0C: 20 09      JR      NZ,$7A17        
7A0E: CD 91 08   CALL    $0891           
7A11: 36 2F      LD      (HL),$2F        
7A13: 3E 18      LD      A,$18           
7A15: E0 F2      LDFF00  ($F2),A         
7A17: F0 EB      LD      A,($EB)         
7A19: FE 6D      CP      $6D             
7A1B: CA 83 7A   JP      Z,$7A83         
7A1E: AF         XOR     A               
7A1F: EA 03 C5   LD      ($C503),A       
7A22: 21 50 C3   LD      HL,$C350        
7A25: 09         ADD     HL,BC           
7A26: 7E         LD      A,(HL)          
7A27: E6 03      AND     $03             
7A29: CB 27      SET     1,E             
7A2B: CB 27      SET     1,E             
7A2D: E0 D7      LDFF00  ($D7),A         
7A2F: 21 A0 C2   LD      HL,$C2A0        
7A32: 09         ADD     HL,BC           
7A33: AF         XOR     A               
7A34: 77         LD      (HL),A          
7A35: 21 40 C2   LD      HL,$C240        
7A38: 09         ADD     HL,BC           
7A39: 7E         LD      A,(HL)          
7A3A: FE 00      CP      $00             
7A3C: 28 1E      JR      Z,$7A5C         
7A3E: 11 00 00   LD      DE,$0000        
7A41: E6 80      AND     $80             
7A43: 28 01      JR      Z,$7A46         
7A45: 1C         INC     E               
7A46: CD CC 7A   CALL    $7ACC           
7A49: 38 11      JR      C,$7A5C         
7A4B: F0 AF      LD      A,($AF)         
7A4D: EA 03 C5   LD      ($C503),A       
7A50: F0 BE      LD      A,($BE)         
7A52: A7         AND     A               
7A53: 20 07      JR      NZ,$7A5C        
7A55: 21 00 C2   LD      HL,$C200        
7A58: 09         ADD     HL,BC           
7A59: F0 EE      LD      A,($EE)         
7A5B: 77         LD      (HL),A          
7A5C: 21 50 C2   LD      HL,$C250        
7A5F: 09         ADD     HL,BC           
7A60: 7E         LD      A,(HL)          
7A61: FE 00      CP      $00             
7A63: 28 1E      JR      Z,$7A83         
7A65: 11 02 00   LD      DE,$0002        
7A68: E6 80      AND     $80             
7A6A: 20 01      JR      NZ,$7A6D        
7A6C: 1C         INC     E               
7A6D: CD CC 7A   CALL    $7ACC           
7A70: 38 11      JR      C,$7A83         
7A72: F0 AF      LD      A,($AF)         
7A74: EA 0D C5   LD      ($C50D),A       
7A77: F0 BE      LD      A,($BE)         
7A79: A7         AND     A               
7A7A: 20 07      JR      NZ,$7A83        
7A7C: 21 10 C2   LD      HL,$C210        
7A7F: 09         ADD     HL,BC           
7A80: F0 EF      LD      A,($EF)         
7A82: 77         LD      (HL),A          
7A83: C9         RET                     
7A84: 01 00 01   LD      BC,$0100        
7A87: 00         NOP                     
7A88: 00         NOP                     
7A89: 01 00 01   LD      BC,$0100        
7A8C: 01 01 00   LD      BC,$0001        
7A8F: 00         NOP                     
7A90: 00         NOP                     
7A91: 00         NOP                     
7A92: 01 01 01   LD      BC,$0101        
7A95: 00         NOP                     
7A96: 01 00 00   LD      BC,$0000        
7A99: 01 00 01   LD      BC,$0100        
7A9C: 01 01 00   LD      BC,$0001        
7A9F: 00         NOP                     
7AA0: 00         NOP                     
7AA1: 00         NOP                     
7AA2: 01 01 00   LD      BC,$0001        
7AA5: 01 01 01   LD      BC,$0101        
7AA8: 01 00 01   LD      BC,$0100        
7AAB: 01 01 01   LD      BC,$0101        
7AAE: 00         NOP                     
7AAF: 01 01 01   LD      BC,$0101        
7AB2: 01 00 01   LD      BC,$0100        
7AB5: 00         NOP                     
7AB6: 00         NOP                     
7AB7: 00         NOP                     
7AB8: 00         NOP                     
7AB9: 01 00 00   LD      BC,$0000        
7ABC: 00         NOP                     
7ABD: 00         NOP                     
7ABE: 01 00 00   LD      BC,$0000        
7AC1: 00         NOP                     
7AC2: 00         NOP                     
7AC3: 01 00 01   LD      BC,$0100        
7AC6: 01 00 01   LD      BC,$0100        
7AC9: 00         NOP                     
7ACA: 00         NOP                     
7ACB: 01 C5 21   LD      BC,$21C5        
7ACE: 00         NOP                     
7ACF: C2 09 7E   JP      NZ,$7E09        
7AD2: D6 08      SUB     $08             
7AD4: F5         PUSH    AF              
7AD5: F0 D7      LD      A,($D7)         
7AD7: 4F         LD      C,A             
7AD8: F1         POP     AF              
7AD9: 21 5E 78   LD      HL,$785E        
7ADC: 09         ADD     HL,BC           
7ADD: 19         ADD     HL,DE           
7ADE: 86         ADD     A,(HL)          
7ADF: E0 DB      LDFF00  ($DB),A         
7AE1: CB 37      SET     1,E             
7AE3: E6 0F      AND     $0F             
7AE5: E0 D8      LDFF00  ($D8),A         
7AE7: C1         POP     BC              
7AE8: C5         PUSH    BC              
7AE9: 7B         LD      A,E             
7AEA: FE 03      CP      $03             
7AEC: 20 1F      JR      NZ,$7B0D        
7AEE: F0 EB      LD      A,($EB)         
7AF0: FE A8      CP      $A8             
7AF2: 28 04      JR      Z,$7AF8         
7AF4: FE 05      CP      $05             
7AF6: 20 15      JR      NZ,$7B0D        
7AF8: 21 10 C2   LD      HL,$C210        
7AFB: 09         ADD     HL,BC           
7AFC: 7E         LD      A,(HL)          
7AFD: 21 10 C3   LD      HL,$C310        
7B00: 09         ADD     HL,BC           
7B01: 4E         LD      C,(HL)          
7B02: CB 79      SET     1,E             
7B04: 28 02      JR      Z,$7B08         
7B06: 0E 00      LD      C,$00           
7B08: CB 39      SET     1,E             
7B0A: 91         SUB     C               
7B0B: 18 05      JR      $7B12           
7B0D: 21 10 C2   LD      HL,$C210        
7B10: 09         ADD     HL,BC           
7B11: 7E         LD      A,(HL)          
7B12: D6 10      SUB     $10             
7B14: F5         PUSH    AF              
7B15: F0 D7      LD      A,($D7)         
7B17: 4F         LD      C,A             
7B18: F1         POP     AF              
7B19: 21 6E 78   LD      HL,$786E        
7B1C: 09         ADD     HL,BC           
7B1D: 19         ADD     HL,DE           
7B1E: 86         ADD     A,(HL)          
7B1F: E0 DC      LDFF00  ($DC),A         
7B21: E6 F0      AND     $F0             
7B23: 21 D8 FF   LD      HL,$FFD8        
7B26: B6         OR      (HL)            
7B27: 4F         LD      C,A             
7B28: 21 11 D7   LD      HL,$D711        
7B2B: 7C         LD      A,H             
7B2C: 09         ADD     HL,BC           
7B2D: 67         LD      H,A             
7B2E: C1         POP     BC              
7B2F: 7E         LD      A,(HL)          
7B30: E0 AF      LDFF00  ($AF),A         
7B32: FE 20      CP      $20             
7B34: CA 7A 7C   JP      Z,$7C7A         
7B37: D5         PUSH    DE              
7B38: 5F         LD      E,A             
7B39: FA A5 DB   LD      A,($DBA5)       
7B3C: 57         LD      D,A             
7B3D: CD E8 29   CALL    $29E8           
7B40: D1         POP     DE              
7B41: E0 DA      LDFF00  ($DA),A         
7B43: F0 EB      LD      A,($EB)         
7B45: FE CC      CP      $CC             
7B47: 28 04      JR      Z,$7B4D         
7B49: FE 99      CP      $99             
7B4B: 20 0F      JR      NZ,$7B5C        
7B4D: F0 DA      LD      A,($DA)         
7B4F: FE 05      CP      $05             
7B51: CA A6 7C   JP      Z,$7CA6         
7B54: FE 07      CP      $07             
7B56: CA A6 7C   JP      Z,$7CA6         
7B59: C3 74 7C   JP      $7C74           
7B5C: F0 DA      LD      A,($DA)         
7B5E: A7         AND     A               
7B5F: CA A6 7C   JP      Z,$7CA6         
7B62: FE 0B      CP      $0B             
7B64: 28 08      JR      Z,$7B6E         
7B66: FE 50      CP      $50             
7B68: 28 04      JR      Z,$7B6E         
7B6A: FE 51      CP      $51             
7B6C: 20 1C      JR      NZ,$7B8A        
7B6E: 21 10 C3   LD      HL,$C310        
7B71: 09         ADD     HL,BC           
7B72: 7E         LD      A,(HL)          
7B73: A7         AND     A               
7B74: C2 A6 7C   JP      NZ,$7CA6        
7B77: 21 10 C4   LD      HL,$C410        
7B7A: 09         ADD     HL,BC           
7B7B: 7E         LD      A,(HL)          
7B7C: A7         AND     A               
7B7D: CA 74 7C   JP      Z,$7C74         
7B80: F0 EB      LD      A,($EB)         
7B82: FE 59      CP      $59             
7B84: CA 74 7C   JP      Z,$7C74         
7B87: C3 A6 7C   JP      $7CA6           
7B8A: FE 7C      CP      $7C             
7B8C: DA E3 7B   JP      C,$7BE3         
7B8F: FE 90      CP      $90             
7B91: D2 E3 7B   JP      NC,$7BE3        
7B94: FE 80      CP      $80             
7B96: F0 EB      LD      A,($EB)         
7B98: 38 0C      JR      C,$7BA6         
7B9A: FE A8      CP      $A8             
7B9C: CA A6 7C   JP      Z,$7CA6         
7B9F: FE 02      CP      $02             
7BA1: CA A6 7C   JP      Z,$7CA6         
7BA4: 18 14      JR      $7BBA           
7BA6: FE 16      CP      $16             
7BA8: CA 99 7C   JP      Z,$7C99         
7BAB: FE 17      CP      $17             
7BAD: CA 99 7C   JP      Z,$7C99         
7BB0: 21 30 C4   LD      HL,$C430        
7BB3: 09         ADD     HL,BC           
7BB4: 7E         LD      A,(HL)          
7BB5: E6 80      AND     $80             
7BB7: C2 99 7C   JP      NZ,$7C99        
7BBA: D5         PUSH    DE              
7BBB: F0 DA      LD      A,($DA)         
7BBD: D6 7C      SUB     $7C             
7BBF: CB 27      SET     1,E             
7BC1: CB 27      SET     1,E             
7BC3: 5F         LD      E,A             
7BC4: 16 00      LD      D,$00           
7BC6: 21 84 7A   LD      HL,$7A84        
7BC9: 19         ADD     HL,DE           
7BCA: F0 DB      LD      A,($DB)         
7BCC: 1F         RRA                     
7BCD: 1F         RRA                     
7BCE: 1F         RRA                     
7BCF: E6 01      AND     $01             
7BD1: 5F         LD      E,A             
7BD2: F0 DC      LD      A,($DC)         
7BD4: 1F         RRA                     
7BD5: 1F         RRA                     
7BD6: E6 02      AND     $02             
7BD8: B3         OR      E               
7BD9: 5F         LD      E,A             
7BDA: 16 00      LD      D,$00           
7BDC: 19         ADD     HL,DE           
7BDD: 7E         LD      A,(HL)          
7BDE: D1         POP     DE              
7BDF: A7         AND     A               
7BE0: CA A6 7C   JP      Z,$7CA6         
7BE3: F0 DA      LD      A,($DA)         
7BE5: FE D0      CP      $D0             
7BE7: 38 41      JR      C,$7C2A         
7BE9: FE D4      CP      $D4             
7BEB: 30 3D      JR      NC,$7C2A        
7BED: D6 D0      SUB     $D0             
7BEF: 21 D0 C5   LD      HL,$C5D0        
7BF2: 09         ADD     HL,BC           
7BF3: BE         CP      (HL)            
7BF4: 28 23      JR      Z,$7C19         
7BF6: F0 EB      LD      A,($EB)         
7BF8: FE A8      CP      $A8             
7BFA: 28 78      JR      Z,$7C74         
7BFC: 21 F0 C4   LD      HL,$C4F0        
7BFF: 09         ADD     HL,BC           
7C00: 7E         LD      A,(HL)          
7C01: A7         AND     A               
7C02: 28 70      JR      Z,$7C74         
7C04: F0 E7      LD      A,($E7)         
7C06: E6 03      AND     $03             
7C08: 28 1D      JR      Z,$7C27         
7C0A: FA A5 DB   LD      A,($DBA5)       
7C0D: A7         AND     A               
7C0E: 20 06      JR      NZ,$7C16        
7C10: F0 E7      LD      A,($E7)         
7C12: E6 01      AND     $01             
7C14: 28 11      JR      Z,$7C27         
7C16: 35         DEC     (HL)            
7C17: 18 0E      JR      $7C27           
7C19: 21 10 C3   LD      HL,$C310        
7C1C: 09         ADD     HL,BC           
7C1D: 7E         LD      A,(HL)          
7C1E: A7         AND     A               
7C1F: CA 74 7C   JP      Z,$7C74         
7C22: 21 F0 C4   LD      HL,$C4F0        
7C25: 09         ADD     HL,BC           
7C26: 34         INC     (HL)            
7C27: C3 A6 7C   JP      $7CA6           
7C2A: FE FF      CP      $FF             
7C2C: 28 6B      JR      Z,$7C99         
7C2E: FE A0      CP      $A0             
7C30: 30 74      JR      NC,$7CA6        
7C32: FE 10      CP      $10             
7C34: 30 3E      JR      NC,$7C74        
7C36: FE 01      CP      $01             
7C38: 28 56      JR      Z,$7C90         
7C3A: FE 03      CP      $03             
7C3C: 28 52      JR      Z,$7C90         
7C3E: FE 04      CP      $04             
7C40: 20 64      JR      NZ,$7CA6        
7C42: F0 EB      LD      A,($EB)         
7C44: FE A8      CP      $A8             
7C46: CA A6 7C   JP      Z,$7CA6         
7C49: FE 02      CP      $02             
7C4B: CA A6 7C   JP      Z,$7CA6         
7C4E: FE 03      CP      $03             
7C50: 20 07      JR      NZ,$7C59        
7C52: FA F9 D6   LD      A,($D6F9)       
7C55: A7         AND     A               
7C56: C2 A6 7C   JP      NZ,$7CA6        
7C59: F0 AF      LD      A,($AF)         
7C5B: FE DB      CP      $DB             
7C5D: 38 3A      JR      C,$7C99         
7C5F: FE DD      CP      $DD             
7C61: 30 36      JR      NC,$7C99        
7C63: D5         PUSH    DE              
7C64: D6 DB      SUB     $DB             
7C66: 5F         LD      E,A             
7C67: 16 00      LD      D,$00           
7C69: 21 A8 7C   LD      HL,$7CA8        
7C6C: 19         ADD     HL,DE           
7C6D: D1         POP     DE              
7C6E: FA FB D6   LD      A,($D6FB)       
7C71: AE         XOR     (HL)            
7C72: 28 32      JR      Z,$7CA6         
7C74: F0 DA      LD      A,($DA)         
7C76: FE 60      CP      $60             
7C78: 20 16      JR      NZ,$7C90        
7C7A: F0 EB      LD      A,($EB)         
7C7C: FE 03      CP      $03             
7C7E: 20 10      JR      NZ,$7C90        
7C80: CD 91 08   CALL    $0891           
7C83: FE 26      CP      $26             
7C85: 38 03      JR      C,$7C8A         
7C87: CD B7 3F   CALL    $3FB7           
7C8A: 21 90 C2   LD      HL,$C290        
7C8D: 09         ADD     HL,BC           
7C8E: 36 01      LD      (HL),$01        
7C90: 21 30 C4   LD      HL,$C430        
7C93: 09         ADD     HL,BC           
7C94: 7E         LD      A,(HL)          
7C95: E6 01      AND     $01             
7C97: 20 0D      JR      NZ,$7CA6        
7C99: 21 7E 78   LD      HL,$787E        
7C9C: 19         ADD     HL,DE           
7C9D: 7E         LD      A,(HL)          
7C9E: 21 A0 C2   LD      HL,$C2A0        
7CA1: 09         ADD     HL,BC           
7CA2: B6         OR      (HL)            
7CA3: 77         LD      (HL),A          
7CA4: A7         AND     A               
7CA5: C9         RET                     
7CA6: 37         SCF                     
7CA7: C9         RET                     
7CA8: 00         NOP                     
7CA9: 02         LD      (BC),A          
7CAA: 11 00 00   LD      DE,$0000        
7CAD: C5         PUSH    BC              
7CAE: 21 00 C2   LD      HL,$C200        
7CB1: 09         ADD     HL,BC           
7CB2: 7E         LD      A,(HL)          
7CB3: E0 DB      LDFF00  ($DB),A         
7CB5: E6 F0      AND     $F0             
7CB7: E0 CE      LDFF00  ($CE),A         
7CB9: CB 37      SET     1,E             
7CBB: 21 10 C2   LD      HL,$C210        
7CBE: 09         ADD     HL,BC           
7CBF: 4F         LD      C,A             
7CC0: 7E         LD      A,(HL)          
7CC1: D6 08      SUB     $08             
7CC3: E0 DC      LDFF00  ($DC),A         
7CC5: E6 F0      AND     $F0             
7CC7: E0 CD      LDFF00  ($CD),A         
7CC9: B1         OR      C               
7CCA: 4F         LD      C,A             
7CCB: E0 E9      LDFF00  ($E9),A         
7CCD: 06 00      LD      B,$00           
7CCF: 21 11 D7   LD      HL,$D711        
7CD2: 7C         LD      A,H             
7CD3: 09         ADD     HL,BC           
7CD4: 67         LD      H,A             
7CD5: C1         POP     BC              
7CD6: 7E         LD      A,(HL)          
7CD7: E0 AF      LDFF00  ($AF),A         
7CD9: FE AC      CP      $AC             
7CDB: CA D5 7D   JP      Z,$7DD5         
7CDE: FE AB      CP      $AB             
7CE0: 20 5B      JR      NZ,$7D3D        
7CE2: F0 EB      LD      A,($EB)         
7CE4: FE 04      CP      $04             
7CE6: 20 55      JR      NZ,$7D3D        
7CE8: FA A5 DB   LD      A,($DBA5)       
7CEB: A7         AND     A               
7CEC: 28 4F      JR      Z,$7D3D         
7CEE: E5         PUSH    HL              
7CEF: 3E 12      LD      A,$12           
7CF1: E0 F4      LDFF00  ($F4),A         
7CF3: 3E 08      LD      A,$08           
7CF5: CD F8 64   CALL    $64F8           
7CF8: 38 42      JR      C,$7D3C         
7CFA: E1         POP     HL              
7CFB: 36 AC      LD      (HL),$AC        
7CFD: C5         PUSH    BC              
7CFE: D5         PUSH    DE              
7CFF: C1         POP     BC              
7D00: 54         LD      D,H             
7D01: 5D         LD      E,L             
7D02: 21 B0 C2   LD      HL,$C2B0        
7D05: 09         ADD     HL,BC           
7D06: 72         LD      (HL),D          
7D07: 21 C0 C2   LD      HL,$C2C0        
7D0A: 09         ADD     HL,BC           
7D0B: 73         LD      (HL),E          
7D0C: F0 CE      LD      A,($CE)         
7D0E: 21 00 C2   LD      HL,$C200        
7D11: 09         ADD     HL,BC           
7D12: 77         LD      (HL),A          
7D13: F0 CD      LD      A,($CD)         
7D15: 21 10 C2   LD      HL,$C210        
7D18: 09         ADD     HL,BC           
7D19: 77         LD      (HL),A          
7D1A: 21 90 C2   LD      HL,$C290        
7D1D: 09         ADD     HL,BC           
7D1E: 36 01      LD      (HL),$01        
7D20: CD 87 08   CALL    $0887           
7D23: 36 80      LD      (HL),$80        
7D25: C1         POP     BC              
7D26: 21 A2 C1   LD      HL,$C1A2        
7D29: 34         INC     (HL)            
7D2A: FA CD C3   LD      A,($C3CD)       
7D2D: A7         AND     A               
7D2E: 28 05      JR      Z,$7D35         
7D30: D6 04      SUB     $04             
7D32: EA CD C3   LD      ($C3CD),A       
7D35: 11 BD 69   LD      DE,$69BD        
7D38: D5         PUSH    DE              
7D39: C3 7A 52   JP      $527A           
7D3C: E1         POP     HL              
7D3D: 7E         LD      A,(HL)          
7D3E: 5F         LD      E,A             
7D3F: FA A5 DB   LD      A,($DBA5)       
7D42: 57         LD      D,A             
7D43: CD E8 29   CALL    $29E8           
7D46: E0 D8      LDFF00  ($D8),A         
7D48: A7         AND     A               
7D49: CA D5 7D   JP      Z,$7DD5         
7D4C: E0 DA      LDFF00  ($DA),A         
7D4E: FE FF      CP      $FF             
7D50: CA D7 7D   JP      Z,$7DD7         
7D53: FE D0      CP      $D0             
7D55: 38 3B      JR      C,$7D92         
7D57: FE D4      CP      $D4             
7D59: 30 37      JR      NC,$7D92        
7D5B: D6 D0      SUB     $D0             
7D5D: 21 D0 C5   LD      HL,$C5D0        
7D60: 09         ADD     HL,BC           
7D61: BE         CP      (HL)            
7D62: 28 1E      JR      Z,$7D82         
7D64: 21 F0 C4   LD      HL,$C4F0        
7D67: 09         ADD     HL,BC           
7D68: 7E         LD      A,(HL)          
7D69: A7         AND     A               
7D6A: 28 49      JR      Z,$7DB5         
7D6C: F0 E7      LD      A,($E7)         
7D6E: E6 03      AND     $03             
7D70: 28 63      JR      Z,$7DD5         
7D72: FA A5 DB   LD      A,($DBA5)       
7D75: A7         AND     A               
7D76: 20 06      JR      NZ,$7D7E        
7D78: F0 E7      LD      A,($E7)         
7D7A: E6 01      AND     $01             
7D7C: 28 57      JR      Z,$7DD5         
7D7E: 35         DEC     (HL)            
7D7F: C3 D5 7D   JP      $7DD5           
7D82: 21 10 C3   LD      HL,$C310        
7D85: 09         ADD     HL,BC           
7D86: 7E         LD      A,(HL)          
7D87: A7         AND     A               
7D88: 28 2B      JR      Z,$7DB5         
7D8A: 21 F0 C4   LD      HL,$C4F0        
7D8D: 09         ADD     HL,BC           
7D8E: 34         INC     (HL)            
7D8F: C3 D5 7D   JP      $7DD5           
7D92: FE 7C      CP      $7C             
7D94: DA 9F 7D   JP      C,$7D9F         
7D97: FE 90      CP      $90             
7D99: D2 9F 7D   JP      NC,$7D9F        
7D9C: C3 D5 7D   JP      $7DD5           
7D9F: F0 DA      LD      A,($DA)         
7DA1: FE A0      CP      $A0             
7DA3: 30 30      JR      NC,$7DD5        
7DA5: FE 50      CP      $50             
7DA7: 28 2C      JR      Z,$7DD5         
7DA9: FE 51      CP      $51             
7DAB: 28 28      JR      Z,$7DD5         
7DAD: FE 10      CP      $10             
7DAF: 30 04      JR      NC,$7DB5        
7DB1: FE 01      CP      $01             
7DB3: 20 20      JR      NZ,$7DD5        
7DB5: 21 A0 C2   LD      HL,$C2A0        
7DB8: 09         ADD     HL,BC           
7DB9: 36 01      LD      (HL),$01        
7DBB: F0 EB      LD      A,($EB)         
7DBD: FE 01      CP      $01             
7DBF: 20 04      JR      NZ,$7DC5        
7DC1: CD 91 08   CALL    $0891           
7DC4: C8         RET     Z               
7DC5: 21 00 C2   LD      HL,$C200        
7DC8: 09         ADD     HL,BC           
7DC9: F0 EE      LD      A,($EE)         
7DCB: 77         LD      (HL),A          
7DCC: 21 10 C2   LD      HL,$C210        
7DCF: 09         ADD     HL,BC           
7DD0: F0 EF      LD      A,($EF)         
7DD2: 77         LD      (HL),A          
7DD3: 37         SCF                     
7DD4: C9         RET                     
7DD5: A7         AND     A               
7DD6: C9         RET                     
7DD7: F0 EB      LD      A,($EB)         
7DD9: FE 01      CP      $01             
7DDB: 28 D8      JR      Z,$7DB5         
7DDD: C3 B7 3F   JP      $3FB7           
7DE0: C5         PUSH    BC              
7DE1: 21 00 C2   LD      HL,$C200        
7DE4: 09         ADD     HL,BC           
7DE5: 7E         LD      A,(HL)          
7DE6: D6 01      SUB     $01             
7DE8: E0 DB      LDFF00  ($DB),A         
7DEA: E6 F0      AND     $F0             
7DEC: E0 CE      LDFF00  ($CE),A         
7DEE: CB 37      SET     1,E             
7DF0: 21 10 C2   LD      HL,$C210        
7DF3: 09         ADD     HL,BC           
7DF4: 4F         LD      C,A             
7DF5: 7E         LD      A,(HL)          
7DF6: D6 07      SUB     $07             
7DF8: E0 DC      LDFF00  ($DC),A         
7DFA: E6 F0      AND     $F0             
7DFC: E0 CD      LDFF00  ($CD),A         
7DFE: B1         OR      C               
7DFF: 4F         LD      C,A             
7E00: 06 00      LD      B,$00           
7E02: 21 11 D7   LD      HL,$D711        
7E05: 7C         LD      A,H             
7E06: 09         ADD     HL,BC           
7E07: 67         LD      H,A             
7E08: C1         POP     BC              
7E09: 7E         LD      A,(HL)          
7E0A: E0 AF      LDFF00  ($AF),A         
7E0C: 5F         LD      E,A             
7E0D: FA A5 DB   LD      A,($DBA5)       
7E10: 57         LD      D,A             
7E11: CD E8 29   CALL    $29E8           
7E14: E0 DA      LDFF00  ($DA),A         
7E16: C9         RET                     
7E17: E0 D8      LDFF00  ($D8),A         
7E19: A7         AND     A               
7E1A: CA 95 7E   JP      Z,$7E95         
7E1D: CD BB 7E   CALL    $7EBB           
7E20: 1D         DEC     E               
7E21: 1D         DEC     E               
7E22: 7B         LD      A,E             
7E23: E0 D9      LDFF00  ($D9),A         
7E25: 7A         LD      A,D             
7E26: CB 7F      SET     1,E             
7E28: 28 02      JR      Z,$7E2C         
7E2A: 2F         CPL                     
7E2B: 3C         INC     A               
7E2C: E0 E3      LDFF00  ($E3),A         
7E2E: CD AB 7E   CALL    $7EAB           
7E31: 7B         LD      A,E             
7E32: E0 DA      LDFF00  ($DA),A         
7E34: 7A         LD      A,D             
7E35: CB 7F      SET     1,E             
7E37: 28 02      JR      Z,$7E3B         
7E39: 2F         CPL                     
7E3A: 3C         INC     A               
7E3B: E0 E4      LDFF00  ($E4),A         
7E3D: 1E 00      LD      E,$00           
7E3F: 21 E3 FF   LD      HL,$FFE3        
7E42: F0 E4      LD      A,($E4)         
7E44: BE         CP      (HL)            
7E45: 30 09      JR      NC,$7E50        
7E47: 1C         INC     E               
7E48: F5         PUSH    AF              
7E49: F0 E3      LD      A,($E3)         
7E4B: E0 E4      LDFF00  ($E4),A         
7E4D: F1         POP     AF              
7E4E: E0 E3      LDFF00  ($E3),A         
7E50: AF         XOR     A               
7E51: E0 E2      LDFF00  ($E2),A         
7E53: E0 D7      LDFF00  ($D7),A         
7E55: F0 D8      LD      A,($D8)         
7E57: 57         LD      D,A             
7E58: F0 E2      LD      A,($E2)         
7E5A: 21 E3 FF   LD      HL,$FFE3        
7E5D: 86         ADD     A,(HL)          
7E5E: 38 06      JR      C,$7E66         
7E60: 21 E4 FF   LD      HL,$FFE4        
7E63: BE         CP      (HL)            
7E64: 38 05      JR      C,$7E6B         
7E66: 96         SUB     (HL)            
7E67: 21 D7 FF   LD      HL,$FFD7        
7E6A: 34         INC     (HL)            
7E6B: E0 E2      LDFF00  ($E2),A         
7E6D: 15         DEC     D               
7E6E: 20 E8      JR      NZ,$7E58        
7E70: 7B         LD      A,E             
7E71: A7         AND     A               
7E72: 28 0A      JR      Z,$7E7E         
7E74: F0 D7      LD      A,($D7)         
7E76: F5         PUSH    AF              
7E77: F0 D8      LD      A,($D8)         
7E79: E0 D7      LDFF00  ($D7),A         
7E7B: F1         POP     AF              
7E7C: E0 D8      LDFF00  ($D8),A         
7E7E: F0 D9      LD      A,($D9)         
7E80: A7         AND     A               
7E81: F0 D7      LD      A,($D7)         
7E83: 20 04      JR      NZ,$7E89        
7E85: 2F         CPL                     
7E86: 3C         INC     A               
7E87: E0 D7      LDFF00  ($D7),A         
7E89: F0 DA      LD      A,($DA)         
7E8B: A7         AND     A               
7E8C: F0 D8      LD      A,($D8)         
7E8E: 28 04      JR      Z,$7E94         
7E90: 2F         CPL                     
7E91: 3C         INC     A               
7E92: E0 D8      LDFF00  ($D8),A         
7E94: C9         RET                     
7E95: AF         XOR     A               
7E96: E0 D7      LDFF00  ($D7),A         
7E98: C9         RET                     
7E99: CD 17 7E   CALL    $7E17           
7E9C: F0 D7      LD      A,($D7)         
7E9E: 21 50 C2   LD      HL,$C250        
7EA1: 09         ADD     HL,BC           
7EA2: 77         LD      (HL),A          
7EA3: F0 D8      LD      A,($D8)         
7EA5: 21 40 C2   LD      HL,$C240        
7EA8: 09         ADD     HL,BC           
7EA9: 77         LD      (HL),A          
7EAA: C9         RET                     
7EAB: 1E 00      LD      E,$00           
7EAD: F0 98      LD      A,($98)         
7EAF: 21 00 C2   LD      HL,$C200        
7EB2: 09         ADD     HL,BC           
7EB3: 96         SUB     (HL)            
7EB4: CB 7F      SET     1,E             
7EB6: 28 01      JR      Z,$7EB9         
7EB8: 1C         INC     E               
7EB9: 57         LD      D,A             
7EBA: C9         RET                     
7EBB: 1E 02      LD      E,$02           
7EBD: F0 99      LD      A,($99)         
7EBF: 21 10 C2   LD      HL,$C210        
7EC2: 09         ADD     HL,BC           
7EC3: 96         SUB     (HL)            
7EC4: 21 10 C3   LD      HL,$C310        
7EC7: 09         ADD     HL,BC           
7EC8: 86         ADD     A,(HL)          
7EC9: CB 7F      SET     1,E             
7ECB: 20 01      JR      NZ,$7ECE        
7ECD: 1C         INC     E               
7ECE: 57         LD      D,A             
7ECF: C9         RET                     
7ED0: CD AB 7E   CALL    $7EAB           
7ED3: 7B         LD      A,E             
7ED4: E0 D7      LDFF00  ($D7),A         
7ED6: 7A         LD      A,D             
7ED7: CB 7F      SET     1,E             
7ED9: 28 02      JR      Z,$7EDD         
7EDB: 2F         CPL                     
7EDC: 3C         INC     A               
7EDD: F5         PUSH    AF              
7EDE: CD BB 7E   CALL    $7EBB           
7EE1: 7B         LD      A,E             
7EE2: E0 D8      LDFF00  ($D8),A         
7EE4: 7A         LD      A,D             
7EE5: CB 7F      SET     1,E             
7EE7: 28 02      JR      Z,$7EEB         
7EE9: 2F         CPL                     
7EEA: 3C         INC     A               
7EEB: D1         POP     DE              
7EEC: BA         CP      D               
7EED: 30 04      JR      NC,$7EF3        
7EEF: F0 D7      LD      A,($D7)         
7EF1: 18 02      JR      $7EF5           
7EF3: F0 D8      LD      A,($D8)         
7EF5: 5F         LD      E,A             
7EF6: C9         RET                     
7EF7: CD 04 7F   CALL    $7F04           
7EFA: C5         PUSH    BC              
7EFB: 79         LD      A,C             
7EFC: C6 10      ADD     $10             
7EFE: 4F         LD      C,A             
7EFF: CD 04 7F   CALL    $7F04           
7F02: C1         POP     BC              
7F03: C9         RET                     
7F04: 21 40 C2   LD      HL,$C240        
7F07: 09         ADD     HL,BC           
7F08: 7E         LD      A,(HL)          
7F09: A7         AND     A               
7F0A: 28 23      JR      Z,$7F2F         
7F0C: F5         PUSH    AF              
7F0D: CB 37      SET     1,E             
7F0F: E6 F0      AND     $F0             
7F11: 21 60 C2   LD      HL,$C260        
7F14: 09         ADD     HL,BC           
7F15: 86         ADD     A,(HL)          
7F16: 77         LD      (HL),A          
7F17: CB 12      SET     1,E             
7F19: 21 00 C2   LD      HL,$C200        
7F1C: 09         ADD     HL,BC           
7F1D: F1         POP     AF              
7F1E: 1E 00      LD      E,$00           
7F20: CB 7F      SET     1,E             
7F22: 28 02      JR      Z,$7F26         
7F24: 1E F0      LD      E,$F0           
7F26: CB 37      SET     1,E             
7F28: E6 0F      AND     $0F             
7F2A: B3         OR      E               
7F2B: CB 1A      SET     1,E             
7F2D: 8E         ADC     A,(HL)          
7F2E: 77         LD      (HL),A          
7F2F: C9         RET                     
7F30: 21 20 C3   LD      HL,$C320        
7F33: 09         ADD     HL,BC           
7F34: 7E         LD      A,(HL)          
7F35: A7         AND     A               
7F36: 28 F7      JR      Z,$7F2F         
7F38: F5         PUSH    AF              
7F39: CB 37      SET     1,E             
7F3B: E6 F0      AND     $F0             
7F3D: 21 30 C3   LD      HL,$C330        
7F40: 09         ADD     HL,BC           
7F41: 86         ADD     A,(HL)          
7F42: 77         LD      (HL),A          
7F43: CB 12      SET     1,E             
7F45: 21 10 C3   LD      HL,$C310        
7F48: 18 D2      JR      $7F1C           
7F4A: F0 EA      LD      A,($EA)         
7F4C: FE 05      CP      $05             
7F4E: 20 1A      JR      NZ,$7F6A        
7F50: FA 95 DB   LD      A,($DB95)       
7F53: FE 07      CP      $07             
7F55: 28 13      JR      Z,$7F6A         
7F57: FA 9F C1   LD      A,($C19F)       
7F5A: 21 A8 C1   LD      HL,$C1A8        
7F5D: B6         OR      (HL)            
7F5E: 21 4F C1   LD      HL,$C14F        
7F61: B6         OR      (HL)            
7F62: 20 06      JR      NZ,$7F6A        
7F64: FA 24 C1   LD      A,($C124)       
7F67: A7         AND     A               
7F68: 28 01      JR      Z,$7F6B         
7F6A: F1         POP     AF              
7F6B: C9         RET                     
7F6C: 21 10 C4   LD      HL,$C410        
7F6F: 09         ADD     HL,BC           
7F70: 7E         LD      A,(HL)          
7F71: A7         AND     A               
7F72: 28 44      JR      Z,$7FB8         
7F74: 3D         DEC     A               
7F75: 77         LD      (HL),A          
7F76: CD B8 3E   CALL    $3EB8           
7F79: 21 40 C2   LD      HL,$C240        
7F7C: 09         ADD     HL,BC           
7F7D: 7E         LD      A,(HL)          
7F7E: F5         PUSH    AF              
7F7F: 21 50 C2   LD      HL,$C250        
7F82: 09         ADD     HL,BC           
7F83: 7E         LD      A,(HL)          
7F84: F5         PUSH    AF              
7F85: 21 F0 C3   LD      HL,$C3F0        
7F88: 09         ADD     HL,BC           
7F89: 7E         LD      A,(HL)          
7F8A: 21 40 C2   LD      HL,$C240        
7F8D: 09         ADD     HL,BC           
7F8E: 77         LD      (HL),A          
7F8F: 21 00 C4   LD      HL,$C400        
7F92: 09         ADD     HL,BC           
7F93: 7E         LD      A,(HL)          
7F94: 21 50 C2   LD      HL,$C250        
7F97: 09         ADD     HL,BC           
7F98: 77         LD      (HL),A          
7F99: CD F7 7E   CALL    $7EF7           
7F9C: 21 30 C4   LD      HL,$C430        
7F9F: 09         ADD     HL,BC           
7FA0: 7E         LD      A,(HL)          
7FA1: E6 20      AND     $20             
7FA3: 20 03      JR      NZ,$7FA8        
7FA5: CD 92 78   CALL    $7892           
7FA8: 21 50 C2   LD      HL,$C250        
7FAB: 09         ADD     HL,BC           
7FAC: F1         POP     AF              
7FAD: 77         LD      (HL),A          
7FAE: 21 40 C2   LD      HL,$C240        
7FB1: 09         ADD     HL,BC           
7FB2: F1         POP     AF              
7FB3: 77         LD      (HL),A          
7FB4: F1         POP     AF              
7FB5: CD D9 3E   CALL    $3ED9           
7FB8: C9         RET                     
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
