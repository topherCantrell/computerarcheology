![Bank 08](GBZelda.jpg)

# Bank 08

>>> cpu Z80GB

>>> binary 4000:roms/zelda.gb[20000:24000]

>>> memoryTable ram 

[RAM Usage](RAMUse.md)

>>> memoryTable hard 

[Hardware Info](../Hardware.md)

```code
4000: 1C              INC     E                   
4001: 1C              INC     E                   
4002: 3E 3C           LD      A,$3C               
4004: 3E 3E           LD      A,$3E               
4006: 3E 30           LD      A,$30               
4008: 0F              RRCA                        
4009: 36 36           LD      (HL),$36            
400B: 0F              RRCA                        
400C: 0F              RRCA                        
400D: 34              INC     (HL)                
400E: 0F              RRCA                        
400F: 3E 20           LD      A,$20               
4011: 20 0F           JR      NZ,$4022            ; {}
4013: 38 28           JR      C,$403D             ; {}
4015: 28 32           JR      Z,$4049             ; {}
4017: 32              LD      (HLD),A             
4018: 20 20           JR      NZ,$403A            ; {}
401A: 38 38           JR      C,$4054             ; {}
401C: 28 28           JR      Z,$4046             ; {}
401E: 32              LD      (HLD),A             
401F: 32              LD      (HLD),A             
4020: 0F              RRCA                        
4021: 26 0F           LD      H,$0F               
4023: 24              INC     H                   
4024: 0F              RRCA                        
4025: 1E 2A           LD      E,$2A               
4027: 0F              RRCA                        
4028: 26 26           LD      H,$26               
402A: 2E 2E           LD      L,$2E               
402C: 0F              RRCA                        
402D: 2A              LD      A,(HLI)             
402E: 2A              LD      A,(HLI)             
402F: 2A              LD      A,(HLI)             
4030: 0F              RRCA                        
4031: 24              INC     H                   
4032: 2E 2E           LD      L,$2E               
4034: 3A              LD      A,(HLD)             
4035: 0F              RRCA                        
4036: 26 2C           LD      H,$2C               
4038: 22              LD      (HLI),A             
4039: 22              LD      (HLI),A             
403A: 22              LD      (HLI),A             
403B: 0F              RRCA                        
403C: 3A              LD      A,(HLD)             
403D: 3A              LD      A,(HLD)             
403E: 0F              RRCA                        
403F: 2C              INC     L                   
4040: FF              RST     0X38                
4041: 00              NOP                         
4042: 00              NOP                         
4043: 00              NOP                         
4044: FF              RST     0X38                
4045: 01 00 05        LD      BC,$0500            
4048: 00              NOP                         
4049: 09              ADD     HL,BC               
404A: 00              NOP                         
404B: 00              NOP                         
404C: 05              DEC     B                   
404D: 05              DEC     B                   
404E: 05              DEC     B                   
404F: FF              RST     0X38                
4050: 00              NOP                         
4051: 00              NOP                         
4052: FF              RST     0X38                
4053: FF              RST     0X38                
4054: 02              LD      (BC),A              
4055: 01 01 01        LD      BC,$0101            
4058: FF              RST     0X38                
4059: FF              RST     0X38                
405A: FF              RST     0X38                
405B: FF              RST     0X38                
405C: FF              RST     0X38                
405D: FF              RST     0X38                
405E: FF              RST     0X38                
405F: FF              RST     0X38                
4060: FF              RST     0X38                
4061: FF              RST     0X38                
4062: FF              RST     0X38                
4063: FF              RST     0X38                
4064: FF              RST     0X38                
4065: 00              NOP                         
4066: FF              RST     0X38                
4067: 00              NOP                         
4068: FF              RST     0X38                
4069: 00              NOP                         
406A: FF              RST     0X38                
406B: FF              RST     0X38                
406C: 02              LD      (BC),A              
406D: 00              NOP                         
406E: FF              RST     0X38                
406F: 0E FF           LD      C,$FF               
4071: FF              RST     0X38                
4072: FF              RST     0X38                
4073: FF              RST     0X38                
4074: FF              RST     0X38                
4075: FF              RST     0X38                
4076: 01 FF FF        LD      BC,$FFFF            
4079: FF              RST     0X38                
407A: FF              RST     0X38                
407B: FF              RST     0X38                
407C: FF              RST     0X38                
407D: FF              RST     0X38                
407E: FF              RST     0X38                
407F: FF              RST     0X38                
4080: 02              LD      (BC),A              
4081: 02              LD      (BC),A              
4082: FF              RST     0X38                
4083: 02              LD      (BC),A              
4084: 02              LD      (BC),A              
4085: 09              ADD     HL,BC               
4086: 09              ADD     HL,BC               
4087: FF              RST     0X38                
4088: 02              LD      (BC),A              
4089: 02              LD      (BC),A              
408A: 09              ADD     HL,BC               
408B: 02              LD      (BC),A              
408C: 09              ADD     HL,BC               
408D: 09              ADD     HL,BC               
408E: 09              ADD     HL,BC               
408F: 09              ADD     HL,BC               
4090: 09              ADD     HL,BC               
4091: FF              RST     0X38                
4092: 01 01 05        LD      BC,$0501            
4095: 00              NOP                         
4096: 00              NOP                         
4097: 00              NOP                         
4098: 00              NOP                         
4099: 0A              LD      A,(BC)              
409A: 0A              LD      A,(BC)              
409B: 0A              LD      A,(BC)              
409C: 0A              LD      A,(BC)              
409D: 00              NOP                         
409E: 00              NOP                         
409F: 00              NOP                         
40A0: 09              ADD     HL,BC               
40A1: 00              NOP                         
40A2: 00              NOP                         
40A3: 09              ADD     HL,BC               
40A4: 09              ADD     HL,BC               
40A5: 00              NOP                         
40A6: 00              NOP                         
40A7: 09              ADD     HL,BC               
40A8: 09              ADD     HL,BC               
40A9: 09              ADD     HL,BC               
40AA: 09              ADD     HL,BC               
40AB: 00              NOP                         
40AC: 00              NOP                         
40AD: FF              RST     0X38                
40AE: 02              LD      (BC),A              
40AF: FF              RST     0X38                
40B0: 09              ADD     HL,BC               
40B1: 00              NOP                         
40B2: 00              NOP                         
40B3: FF              RST     0X38                
40B4: 00              NOP                         
40B5: 00              NOP                         
40B6: 00              NOP                         
40B7: FF              RST     0X38                
40B8: FF              RST     0X38                
40B9: 00              NOP                         
40BA: 01 05 00        LD      BC,$0005            
40BD: 00              NOP                         
40BE: 00              NOP                         
40BF: 00              NOP                         
40C0: FF              RST     0X38                
40C1: 05              DEC     B                   
40C2: FF              RST     0X38                
40C3: FF              RST     0X38                
40C4: FF              RST     0X38                
40C5: 06 07           LD      B,$07               
40C7: 07              RLCA                        
40C8: 07              RLCA                        
40C9: FF              RST     0X38                
40CA: FF              RST     0X38                
40CB: 06 06           LD      B,$06               
40CD: FF              RST     0X38                
40CE: FF              RST     0X38                
40CF: FF              RST     0X38                
40D0: 09              ADD     HL,BC               
40D1: FF              RST     0X38                
40D2: FF              RST     0X38                
40D3: FF              RST     0X38                
40D4: 07              RLCA                        
40D5: FF              RST     0X38                
40D6: FF              RST     0X38                
40D7: 07              RLCA                        
40D8: FF              RST     0X38                
40D9: 07              RLCA                        
40DA: 05              DEC     B                   
40DB: FF              RST     0X38                
40DC: FF              RST     0X38                
40DD: 05              DEC     B                   
40DE: 05              DEC     B                   
40DF: 05              DEC     B                   
40E0: FF              RST     0X38                
40E1: 01 FF FF        LD      BC,$FFFF            
40E4: FF              RST     0X38                
40E5: FF              RST     0X38                
40E6: FF              RST     0X38                
40E7: FF              RST     0X38                
40E8: FF              RST     0X38                
40E9: FF              RST     0X38                
40EA: FF              RST     0X38                
40EB: FF              RST     0X38                
40EC: 19              ADD     HL,DE               
40ED: FF              RST     0X38                
40EE: FF              RST     0X38                
40EF: FF              RST     0X38                
40F0: 03              INC     BC                  
40F1: 0E 03           LD      C,$03               
40F3: 0E FF           LD      C,$FF               
40F5: 0E 0E           LD      C,$0E               
40F7: 0E 0E           LD      C,$0E               
40F9: 0E 0E           LD      C,$0E               
40FB: FF              RST     0X38                
40FC: 0E 0E           LD      C,$0E               
40FE: FF              RST     0X38                
40FF: 0E 0E           LD      C,$0E               
4101: 0E 0E           LD      C,$0E               
4103: 09              ADD     HL,BC               
4104: 00              NOP                         
4105: 0E 09           LD      C,$09               
4107: FF              RST     0X38                
4108: FF              RST     0X38                
4109: 0E 09           LD      C,$09               
410B: 00              NOP                         
410C: 0E FF           LD      C,$FF               
410E: 02              LD      (BC),A              
410F: 0E 0E           LD      C,$0E               
4111: 0E 02           LD      C,$02               
4113: FF              RST     0X38                
4114: 01 01 01        LD      BC,$0101            
4117: 09              ADD     HL,BC               
4118: 00              NOP                         
4119: 00              NOP                         
411A: 00              NOP                         
411B: 00              NOP                         
411C: 00              NOP                         
411D: 00              NOP                         
411E: 00              NOP                         
411F: 00              NOP                         
4120: 0F              RRCA                        
4121: 0F              RRCA                        
4122: 0F              RRCA                        
4123: 08 00 0C        LD      ($0C00),SP          
4126: 0C              INC     C                   
4127: 03              INC     BC                  
4128: 0C              INC     C                   
4129: 0C              INC     C                   
412A: 0C              INC     C                   
412B: 00              NOP                         
412C: 00              NOP                         
412D: 00              NOP                         
412E: 0C              INC     C                   
412F: 00              NOP                         
4130: 03              INC     BC                  
4131: 03              INC     BC                  
4132: 00              NOP                         
4133: 19              ADD     HL,DE               
4134: 00              NOP                         
4135: 08 0C 03        LD      ($030C),SP          
4138: 0C              INC     C                   
4139: 0C              INC     C                   
413A: 08 19 0C        LD      ($0C19),SP          
413D: 05              DEC     B                   
413E: 0C              INC     C                   
413F: 00              NOP                         
4140: 00              NOP                         
4141: 03              INC     BC                  
4142: 03              INC     BC                  
4143: 03              INC     BC                  
4144: 03              INC     BC                  
4145: 03              INC     BC                  
4146: 03              INC     BC                  
4147: 03              INC     BC                  
4148: 03              INC     BC                  
4149: 03              INC     BC                  
414A: 03              INC     BC                  
414B: 03              INC     BC                  
414C: 03              INC     BC                  
414D: FF              RST     0X38                
414E: 01 FF 03        LD      BC,$03FF            
4151: 03              INC     BC                  
4152: 03              INC     BC                  
4153: FF              RST     0X38                
4154: 03              INC     BC                  
4155: 03              INC     BC                  
4156: FF              RST     0X38                
4157: 0B              DEC     BC                  
4158: FF              RST     0X38                
4159: 03              INC     BC                  
415A: FF              RST     0X38                
415B: FF              RST     0X38                
415C: FF              RST     0X38                
415D: 07              RLCA                        
415E: 07              RLCA                        
415F: FF              RST     0X38                
4160: FF              RST     0X38                
4161: 06 FF           LD      B,$FF               
4163: FF              RST     0X38                
4164: 00              NOP                         
4165: FF              RST     0X38                
4166: FF              RST     0X38                
4167: FF              RST     0X38                
4168: FF              RST     0X38                
4169: 0E 0E           LD      C,$0E               
416B: FF              RST     0X38                
416C: FF              RST     0X38                
416D: 0E 0E           LD      C,$0E               
416F: 00              NOP                         
4170: FF              RST     0X38                
4171: 00              NOP                         
4172: FF              RST     0X38                
4173: FF              RST     0X38                
4174: FF              RST     0X38                
4175: FF              RST     0X38                
4176: FF              RST     0X38                
4177: 00              NOP                         
4178: FF              RST     0X38                
4179: 17              RLA                         
417A: 17              RLA                         
417B: 17              RLA                         
417C: FF              RST     0X38                
417D: 03              INC     BC                  
417E: FF              RST     0X38                
417F: FF              RST     0X38                
4180: FF              RST     0X38                
4181: FF              RST     0X38                
4182: 0A              LD      A,(BC)              
4183: 0A              LD      A,(BC)              
4184: 0A              LD      A,(BC)              
4185: FF              RST     0X38                
4186: FF              RST     0X38                
4187: FF              RST     0X38                
4188: 0A              LD      A,(BC)              
4189: 0A              LD      A,(BC)              
418A: FF              RST     0X38                
418B: 0B              DEC     BC                  
418C: FF              RST     0X38                
418D: 0D              DEC     C                   
418E: FF              RST     0X38                
418F: FF              RST     0X38                
4190: 0A              LD      A,(BC)              
4191: 0A              LD      A,(BC)              
4192: FF              RST     0X38                
4193: 00              NOP                         
4194: FF              RST     0X38                
4195: FF              RST     0X38                
4196: FF              RST     0X38                
4197: FF              RST     0X38                
4198: FF              RST     0X38                
4199: FF              RST     0X38                
419A: FF              RST     0X38                
419B: FF              RST     0X38                
419C: 09              ADD     HL,BC               
419D: 01 00 00        LD      BC,$0000            
41A0: FF              RST     0X38                
41A1: FF              RST     0X38                
41A2: FF              RST     0X38                
41A3: FF              RST     0X38                
41A4: FF              RST     0X38                
41A5: FF              RST     0X38                
41A6: FF              RST     0X38                
41A7: FF              RST     0X38                
41A8: FF              RST     0X38                
41A9: FF              RST     0X38                
41AA: FF              RST     0X38                
41AB: FF              RST     0X38                
41AC: FF              RST     0X38                
41AD: FF              RST     0X38                
41AE: FF              RST     0X38                
41AF: 01 0C FF        LD      BC,$FF0C            
41B2: FF              RST     0X38                
41B3: FF              RST     0X38                
41B4: 1A              LD      A,(DE)              
41B5: FF              RST     0X38                
41B6: FF              RST     0X38                
41B7: FF              RST     0X38                
41B8: FF              RST     0X38                
41B9: FF              RST     0X38                
41BA: 0C              INC     C                   
41BB: 0C              INC     C                   
41BC: 0C              INC     C                   
41BD: 0C              INC     C                   
41BE: 0C              INC     C                   
41BF: 01 0C 0C        LD      BC,$0C0C            
41C2: 0C              INC     C                   
41C3: 0C              INC     C                   
41C4: 0C              INC     C                   
41C5: 0C              INC     C                   
41C6: 0C              INC     C                   
41C7: 0C              INC     C                   
41C8: 0C              INC     C                   
41C9: 0C              INC     C                   
41CA: 0C              INC     C                   
41CB: 0C              INC     C                   
41CC: 05              DEC     B                   
41CD: 05              DEC     B                   
41CE: 05              DEC     B                   
41CF: 01 05 05        LD      BC,$0505            
41D2: 05              DEC     B                   
41D3: 05              DEC     B                   
41D4: 05              DEC     B                   
41D5: 05              DEC     B                   
41D6: 05              DEC     B                   
41D7: 05              DEC     B                   
41D8: 05              DEC     B                   
41D9: 04              INC     B                   
41DA: 05              DEC     B                   
41DB: 04              INC     B                   
41DC: 04              INC     B                   
41DD: 04              INC     B                   
41DE: 00              NOP                         
41DF: 08 04 04        LD      ($0404),SP          
41E2: 08 08 00        LD      ($0008),SP          
41E5: 08 08 08        LD      ($0808),SP          
41E8: 08 08 08        LD      ($0808),SP          
41EB: 05              DEC     B                   
41EC: 05              DEC     B                   
41ED: 08 0C 0C        LD      ($0C0C),SP          
41F0: 08 04 05        LD      ($0504),SP          
41F3: 0C              INC     C                   
41F4: 04              INC     B                   
41F5: 00              NOP                         
41F6: 05              DEC     B                   
41F7: 05              DEC     B                   
41F8: 0C              INC     C                   
41F9: 0C              INC     C                   
41FA: 0C              INC     C                   
41FB: 0C              INC     C                   
41FC: 0C              INC     C                   
41FD: 05              DEC     B                   
41FE: 0C              INC     C                   
41FF: 0C              INC     C                   
4200: 0C              INC     C                   
4201: 0C              INC     C                   
4202: 03              INC     BC                  
4203: 03              INC     BC                  
4204: 00              NOP                         
4205: 03              INC     BC                  
4206: FF              RST     0X38                
4207: 08 00 0C        LD      ($0C00),SP          
420A: 0C              INC     C                   
420B: 04              INC     B                   
420C: 04              INC     B                   
420D: 0C              INC     C                   
420E: 0C              INC     C                   
420F: 0C              INC     C                   
4210: 0C              INC     C                   
4211: 0C              INC     C                   
4212: FF              RST     0X38                
4213: 01 00 01        LD      BC,$0100            
4216: 01 08 00        LD      BC,$0008            
4219: 08 08 08        LD      ($0808),SP          
421C: 08 08 0C        LD      ($0C08),SP          
421F: 0C              INC     C                   
4220: FF              RST     0X38                
4221: 08 08 04        LD      ($0408),SP          
4224: 0C              INC     C                   
4225: 0C              INC     C                   
4226: 0C              INC     C                   
4227: 0C              INC     C                   
4228: 00              NOP                         
4229: 08 0C 0C        LD      ($0C0C),SP          
422C: 0C              INC     C                   
422D: 0C              INC     C                   
422E: 0C              INC     C                   
422F: 0C              INC     C                   
4230: 0C              INC     C                   
4231: 0C              INC     C                   
4232: 0C              INC     C                   
4233: 0C              INC     C                   
4234: 0C              INC     C                   
4235: 00              NOP                         
4236: 0C              INC     C                   
4237: 0C              INC     C                   
4238: 00              NOP                         
4239: 0C              INC     C                   
423A: 0C              INC     C                   
423B: 18 05           JR      $4242               ; {}
423D: 00              NOP                         
423E: 08 00 65        LD      ($6500),SP          ; {}
4241: 66              LD      H,(HL)              
4242: 67              LD      H,A                 
4243: 68              LD      L,B                 
4244: 69              LD      L,C                 
4245: 6D              LD      L,L                 
4246: 45              LD      B,L                 
4247: 46              LD      B,(HL)              
4248: 46              LD      B,(HL)              
4249: 00              NOP                         
424A: 4E              LD      C,(HL)              
424B: 4E              LD      C,(HL)              
424C: 4E              LD      C,(HL)              
424D: 4E              LD      C,(HL)              
424E: 44              LD      B,H                 
424F: 50              LD      D,B                 
4250: 20 74           JR      NZ,$42C6            ; {}
4252: 6B              LD      L,E                 
4253: 6C              LD      L,H                 
4254: 6D              LD      L,L                 
4255: 6D              LD      L,L                 
4256: 37              SCF                         
4257: 37              SCF                         
4258: 4F              LD      C,A                 
4259: 1C              INC     E                   
425A: 4F              LD      C,A                 
425B: 4E              LD      C,(HL)              
425C: 4E              LD      C,(HL)              
425D: 4E              LD      C,(HL)              
425E: 50              LD      D,B                 
425F: 4E              LD      C,(HL)              
4260: 02              LD      (BC),A              
4261: 7D              LD      A,L                 
4262: 00              NOP                         
4263: 0E 48           LD      C,$48               
4265: 47              LD      B,A                 
4266: 37              SCF                         
4267: 06 06           LD      B,$06               
4269: 00              NOP                         
426A: 51              LD      D,C                 
426B: 50              LD      D,B                 
426C: 50              LD      D,B                 
426D: 62              LD      H,D                 
426E: 62              LD      H,D                 
426F: 62              LD      H,D                 
4270: 02              LD      (BC),A              
4271: 7D              LD      A,L                 
4272: 00              NOP                         
4273: 0E 48           LD      C,$48               
4275: 47              LD      B,A                 
4276: 37              SCF                         
4277: 06 06           LD      B,$06               
4279: 00              NOP                         
427A: 51              LD      D,C                 
427B: 51              LD      D,C                 
427C: 00              NOP                         
427D: 62              LD      H,D                 
427E: 62              LD      H,D                 
427F: 62              LD      H,D                 
4280: 00              NOP                         
4281: 41              LD      B,C                 
4282: 7E              LD      A,(HL)              
4283: 7E              LD      A,(HL)              
4284: 7A              LD      A,D                 
4285: 06 28           LD      B,$28               
4287: 28 11           JR      Z,$429A             ; {}
4289: 11 64 63        LD      DE,$6364            
428C: 2D              DEC     L                   
428D: 2D              DEC     L                   
428E: 2D              DEC     L                   
428F: 2D              DEC     L                   
4290: 01 2E 74        LD      BC,$742E            
4293: 7F              LD      A,A                 
4294: 38 28           JR      C,$42BE             ; {}
4296: 28 29           JR      Z,$42C1             ; {}
4298: 11 11 11        LD      DE,$1111            
429B: 64              LD      H,H                 
429C: 2D              DEC     L                   
429D: 2D              DEC     L                   
429E: 2D              DEC     L                   
429F: 2D              DEC     L                   
42A0: 00              NOP                         
42A1: 00              NOP                         
42A2: 7E              LD      A,(HL)              
42A3: 00              NOP                         
42A4: 00              NOP                         
42A5: 28 29           JR      Z,$42D0             ; {}
42A7: 05              DEC     B                   
42A8: 58              LD      E,B                 
42A9: 59              LD      E,C                 
42AA: 5A              LD      E,D                 
42AB: 00              NOP                         
42AC: 2D              DEC     L                   
42AD: 2D              DEC     L                   
42AE: 2D              DEC     L                   
42AF: 2D              DEC     L                   
42B0: 7E              LD      A,(HL)              
42B1: 7E              LD      A,(HL)              
42B2: 7E              LD      A,(HL)              
42B3: 7E              LD      A,(HL)              
42B4: 3A              LD      A,(HLD)             
42B5: 3A              LD      A,(HLD)             
42B6: 28 29           JR      Z,$42E1             ; {}
42B8: 5B              LD      E,E                 
42B9: 5C              LD      E,H                 
42BA: 00              NOP                         
42BB: 12              LD      (DE),A              
42BC: 2D              DEC     L                   
42BD: 2D              DEC     L                   
42BE: 2D              DEC     L                   
42BF: 2D              DEC     L                   
42C0: 3D              DEC     A                   
42C1: 03              INC     BC                  
42C2: 0A              LD      A,(BC)              
42C3: 0B              DEC     BC                  
42C4: 39              ADD     HL,SP               
42C5: 61              LD      H,C                 
42C6: 18 18           JR      $42E0               ; {}
42C8: 4A              LD      C,D                 
42C9: 2C              INC     L                   
42CA: 72              LD      (HL),D              
42CB: 00              NOP                         
42CC: 2A              LD      A,(HLI)             
42CD: 6F              LD      L,A                 
42CE: 2D              DEC     L                   
42CF: 2D              DEC     L                   
42D0: 00              NOP                         
42D1: 00              NOP                         
42D2: 43              LD      B,E                 
42D3: 0A              LD      A,(BC)              
42D4: 40              LD      B,B                 
42D5: 3E 00           LD      A,$00               
42D7: 00              NOP                         
42D8: 75              LD      (HL),L              
42D9: 5F              LD      E,A                 
42DA: 73              LD      (HL),E              
42DB: 70              LD      (HL),B              
42DC: 2A              LD      A,(HLI)             
42DD: 6F              LD      L,A                 
42DE: 2D              DEC     L                   
42DF: 2D              DEC     L                   
42E0: 13              INC     DE                  
42E1: 0C              INC     C                   
42E2: 0A              LD      A,(BC)              
42E3: 00              NOP                         
42E4: 3B              DEC     SP                  
42E5: 00              NOP                         
42E6: 3B              DEC     SP                  
42E7: 3B              DEC     SP                  
42E8: 5F              LD      E,A                 
42E9: 54              LD      D,H                 
42EA: 37              SCF                         
42EB: 71              LD      (HL),C              
42EC: 6E              LD      L,(HL)              
42ED: 6E              LD      L,(HL)              
42EE: 6E              LD      L,(HL)              
42EF: 00              NOP                         
42F0: 0F              RRCA                        
42F1: 0C              INC     C                   
42F2: 09              ADD     HL,BC               
42F3: 09              ADD     HL,BC               
42F4: 00              NOP                         
42F5: 3B              DEC     SP                  
42F6: 3B              DEC     SP                  
42F7: 3B              DEC     SP                  
42F8: 77              LD      (HL),A              
42F9: 72              LD      (HL),D              
42FA: 70              LD      (HL),B              
42FB: 4B              LD      C,E                 
42FC: 6E              LD      L,(HL)              
42FD: 6E              LD      L,(HL)              
42FE: 6E              LD      L,(HL)              
42FF: 6E              LD      L,(HL)              
4300: 08 08 07        LD      ($0708),SP          
4303: 07              RLCA                        
4304: 3C              INC     A                   
4305: 3C              INC     A                   
4306: 3C              INC     A                   
4307: 00              NOP                         
4308: 78              LD      A,B                 
4309: 23              INC     HL                  
430A: 26 57           LD      H,$57               
430C: 34              INC     (HL)                
430D: 35              DEC     (HL)                
430E: 1D              DEC     E                   
430F: 7B              LD      A,E                 
4310: 07              RLCA                        
4311: 07              RLCA                        
4312: 07              RLCA                        
4313: 07              RLCA                        
4314: 3C              INC     A                   
4315: 3C              INC     A                   
4316: 3C              INC     A                   
4317: 7A              LD      A,D                 
4318: 79              LD      A,C                 
4319: 26 1F           LD      H,$1F               
431B: 53              LD      D,E                 
431C: 2F              CPL                         
431D: 34              INC     (HL)                
431E: 00              NOP                         
431F: 4D              LD      C,L                 
4320: 07              RLCA                        
4321: 07              RLCA                        
4322: 00              NOP                         
4323: 42              LD      B,D                 
4324: 00              NOP                         
4325: 90              SUB     B                   
4326: 91              SUB     C                   
4327: 26 26           LD      H,$26               
4329: 25              DEC     H                   
432A: 36 33           LD      (HL),$33            
432C: 31 30 7C        LD      SP,$7C30            
432F: 4D              LD      C,L                 
4330: 07              RLCA                        
4331: 07              RLCA                        
4332: 07              RLCA                        
4333: 00              NOP                         
4334: 90              SUB     B                   
4335: 90              SUB     B                   
4336: 91              SUB     C                   
4337: 00              NOP                         
4338: 1F              RRA                         
4339: 26 1F           LD      H,$1F               
433B: 00              NOP                         
433C: 30 21           JR      NC,$435F            ; {}
433E: 4C              LD      C,H                 
433F: 7C              LD      A,H                 
4340: 01 03 0E        LD      BC,$0E03            
4343: 07              RLCA                        
4344: 07              RLCA                        
4345: 00              NOP                         
4346: 05              DEC     B                   
4347: 01 00 03        LD      BC,$0300            
434A: 1C              INC     E                   
434B: 05              DEC     B                   
434C: 01 01 01        LD      BC,$0101            
434F: 00              NOP                         
4350: 00              NOP                         
4351: 02              LD      (BC),A              
4352: 00              NOP                         
4353: 03              INC     BC                  
4354: 03              INC     BC                  
4355: 03              INC     BC                  
4356: 03              INC     BC                  
4357: 03              INC     BC                  
4358: 33              INC     SP                  
4359: 33              INC     SP                  
435A: 33              INC     SP                  
435B: 33              INC     SP                  
435C: 00              NOP                         
435D: 00              NOP                         
435E: 63              LD      H,E                 
435F: 63              LD      H,E                 
4360: 14              INC     D                   
4361: 00              NOP                         
4362: 14              INC     D                   
4363: 14              INC     D                   
4364: 00              NOP                         
4365: 06 13           LD      B,$13               
4367: 06 13           LD      B,$13               
4369: 13              INC     DE                  
436A: 0E 08           LD      C,$08               
436C: 13              INC     DE                  
436D: 08 06 07        LD      ($0706),SP          
4370: 06 06           LD      B,$06               
4372: 00              NOP                         
4373: 00              NOP                         
4374: 1B              DEC     DE                  
4375: 1B              DEC     DE                  
4376: 06 1B           LD      B,$1B               
4378: 06 00           LD      B,$00               
437A: 33              INC     SP                  
437B: 33              INC     SP                  
437C: 33              INC     SP                  
437D: 33              INC     SP                  
437E: 33              INC     SP                  
437F: 33              INC     SP                  
4380: 18 18           JR      $439A               ; {}
4382: 18 18           JR      $439C               ; {}
4384: 00              NOP                         
4385: 15              DEC     D                   
4386: 00              NOP                         
4387: 00              NOP                         
4388: 17              RLA                         
4389: 00              NOP                         
438A: 17              RLA                         
438B: 17              RLA                         
438C: 06 17           LD      B,$17               
438E: 06 00           LD      B,$00               
4390: 18 3C           JR      $43CE               ; {}
4392: 3C              INC     A                   
4393: 3C              INC     A                   
4394: 17              RLA                         
4395: 17              RLA                         
4396: 17              RLA                         
4397: 17              RLA                         
4398: 17              RLA                         
4399: 0E 16           LD      C,$16               
439B: 00              NOP                         
439C: 17              RLA                         
439D: 01 33 33        LD      BC,$3333            
43A0: 00              NOP                         
43A1: 00              NOP                         
43A2: 0E 31           LD      C,$31               
43A4: 19              ADD     HL,DE               
43A5: 30 32           JR      NC,$43D9            ; {}
43A7: 32              LD      (HLD),A             
43A8: 00              NOP                         
43A9: 00              NOP                         
43AA: 32              LD      (HLD),A             
43AB: 32              LD      (HLD),A             
43AC: 00              NOP                         
43AD: 32              LD      (HLD),A             
43AE: 30 30           JR      NC,$43E0            ; {}
43B0: 00              NOP                         
43B1: 30 32           JR      NC,$43E5            ; {}
43B3: 00              NOP                         
43B4: 30 30           JR      NC,$43E6            ; {}
43B6: 00              NOP                         
43B7: 30 30           JR      NC,$43E9            ; {}
43B9: 30 30           JR      NC,$43EB            ; {}
43BB: 30 33           JR      NC,$43F0            ; {}
43BD: 33              INC     SP                  
43BE: 00              NOP                         
43BF: 01 1E 1E        LD      BC,$1E1E            
43C2: 0F              RRCA                        
43C3: 1E 1E           LD      E,$1E               
43C5: 1D              DEC     E                   
43C6: 00              NOP                         
43C7: 00              NOP                         
43C8: 24              INC     H                   
43C9: 24              INC     H                   
43CA: 24              INC     H                   
43CB: 00              NOP                         
43CC: 24              INC     H                   
43CD: 24              INC     H                   
43CE: 24              INC     H                   
43CF: 24              INC     H                   
43D0: 24              INC     H                   
43D1: 00              NOP                         
43D2: 1E 1F           LD      E,$1F               
43D4: 1F              RRA                         
43D5: 1E 1E           LD      E,$1E               
43D7: 04              INC     B                   
43D8: 04              INC     B                   
43D9: 00              NOP                         
43DA: 00              NOP                         
43DB: 04              INC     B                   
43DC: 04              INC     B                   
43DD: 04              INC     B                   
43DE: 04              INC     B                   
43DF: 04              INC     B                   
43E0: 04              INC     B                   
43E1: 04              INC     B                   
43E2: 33              INC     SP                  
43E3: 33              INC     SP                  
43E4: 33              INC     SP                  
43E5: 33              INC     SP                  
43E6: 33              INC     SP                  
43E7: 33              INC     SP                  
43E8: 33              INC     SP                  
43E9: 33              INC     SP                  
43EA: 64              LD      H,H                 
43EB: 64              LD      H,H                 
43EC: 80              ADD     A,B                 
43ED: 00              NOP                         
43EE: 00              NOP                         
43EF: 00              NOP                         
43F0: 28 28           JR      Z,$441A             ; {}
43F2: 28 28           JR      Z,$441C             ; {}
43F4: 61              LD      H,C                 
43F5: 0F              RRCA                        
43F6: 61              LD      H,C                 
43F7: 00              NOP                         
43F8: 00              NOP                         
43F9: 28 28           JR      Z,$4423             ; {}
43FB: 00              NOP                         
43FC: 25              DEC     H                   
43FD: 26 61           LD      H,$61               
43FF: 29              ADD     HL,HL               
4400: 27              DAA                         
4401: 00              NOP                         
4402: 28 61           JR      Z,$4465             ; {}
4404: 00              NOP                         
4405: 26 00           LD      H,$00               
4407: 29              ADD     HL,HL               
4408: 2A              LD      A,(HLI)             
4409: 00              NOP                         
440A: 00              NOP                         
440B: 62              LD      H,D                 
440C: 00              NOP                         
440D: 61              LD      H,C                 
440E: 00              NOP                         
440F: 27              DAA                         
4410: 61              LD      H,C                 
4411: 61              LD      H,C                 
4412: 27              DAA                         
4413: 27              DAA                         
4414: 27              DAA                         
4415: 27              DAA                         
4416: 00              NOP                         
4417: 61              LD      H,C                 
4418: 63              LD      H,E                 
4419: 63              LD      H,E                 
441A: 33              INC     SP                  
441B: 33              INC     SP                  
441C: 33              INC     SP                  
441D: 33              INC     SP                  
441E: 00              NOP                         
441F: 00              NOP                         
4420: 44              LD      B,H                 
4421: 44              LD      B,H                 
4422: 44              LD      B,H                 
4423: 00              NOP                         
4424: 4A              LD      C,D                 
4425: 67              LD      H,A                 
4426: 67              LD      H,A                 
4427: 00              NOP                         
4428: 7F              LD      A,A                 
4429: 00              NOP                         
442A: 00              NOP                         
442B: 33              INC     SP                  
442C: 33              INC     SP                  
442D: 00              NOP                         
442E: 6E              LD      L,(HL)              
442F: 1A              LD      A,(DE)              
4430: 67              LD      H,A                 
4431: 67              LD      H,A                 
4432: 00              NOP                         
4433: 80              ADD     A,B                 
4434: 4A              LD      C,D                 
4435: 7E              LD      A,(HL)              
4436: 67              LD      H,A                 
4437: 00              NOP                         
4438: 7F              LD      A,A                 
4439: 7F              LD      A,A                 
443A: 3D              DEC     A                   
443B: 80              ADD     A,B                 
443C: 10 00           ;;STOP    $00                 
443E: 6E              LD      L,(HL)              
443F: 1A              LD      A,(DE)              
4440: 00              NOP                         
4441: 00              NOP                         
4442: 3F              CCF                         
4443: 2C              INC     L                   
4444: 2C              INC     L                   
4445: 5E              LD      E,(HL)              
4446: 34              INC     (HL)                
4447: 39              ADD     HL,SP               
4448: 00              NOP                         
4449: 5F              LD      E,A                 
444A: 60              LD      H,B                 
444B: 3E 39           LD      A,$39               
444D: 2B              DEC     HL                  
444E: 2B              DEC     HL                  
444F: 00              NOP                         
4450: 39              ADD     HL,SP               
4451: 2D              DEC     L                   
4452: 2D              DEC     L                   
4453: 2D              DEC     L                   
4454: 2D              DEC     L                   
4455: 2D              DEC     L                   
4456: 2D              DEC     L                   
4457: 2E 2D           LD      L,$2D               
4459: 2D              DEC     L                   
445A: 2D              DEC     L                   
445B: 2E 00           LD      L,$00               
445D: 2D              DEC     L                   
445E: 2D              DEC     L                   
445F: 00              NOP                         
4460: 36 00           LD      (HL),$00            
4462: 35              DEC     (HL)                
4463: 0F              RRCA                        
4464: 37              SCF                         
4465: 35              DEC     (HL)                
4466: 35              DEC     (HL)                
4467: 00              NOP                         
4468: 37              SCF                         
4469: 00              NOP                         
446A: 38 35           JR      C,$44A1             ; {}
446C: 0F              RRCA                        
446D: 35              DEC     (HL)                
446E: 68              LD      L,B                 
446F: 01 0F 5C        LD      BC,$5C0F            
4472: 56              LD      D,(HL)              
4473: 00              NOP                         
4474: 50              LD      D,B                 
4475: 5C              LD      E,H                 
4476: 00              NOP                         
4477: 51              LD      D,C                 
4478: 56              LD      D,(HL)              
4479: 58              LD      E,B                 
447A: 5B              LD      E,E                 
447B: 5B              LD      E,E                 
447C: 00              NOP                         
447D: 54              LD      D,H                 
447E: 00              NOP                         
447F: 51              LD      D,C                 
4480: 5A              LD      E,D                 
4481: 00              NOP                         
4482: 59              LD      E,C                 
4483: 59              LD      E,C                 
4484: 00              NOP                         
4485: 57              LD      D,A                 
4486: 5A              LD      E,D                 
4487: 59              LD      E,C                 
4488: 59              LD      E,C                 
4489: 00              NOP                         
448A: 5C              LD      E,H                 
448B: 5C              LD      E,H                 
448C: 52              LD      D,D                 
448D: 00              NOP                         
448E: 55              LD      D,L                 
448F: 00              NOP                         
4490: 5C              LD      E,H                 
4491: 5C              LD      E,H                 
4492: 00              NOP                         
4493: 53              LD      D,E                 
4494: 52              LD      D,D                 
4495: 52              LD      D,D                 
4496: 00              NOP                         
4497: 5B              LD      E,E                 
4498: 00              NOP                         
4499: 5C              LD      E,H                 
449A: 00              NOP                         
449B: 53              LD      D,E                 
449C: 52              LD      D,D                 
449D: 5B              LD      E,E                 
449E: 5A              LD      E,D                 
449F: 53              LD      D,E                 
44A0: 33              INC     SP                  
44A1: 33              INC     SP                  
44A2: 33              INC     SP                  
44A3: 33              INC     SP                  
44A4: 33              INC     SP                  
44A5: 33              INC     SP                  
44A6: 33              INC     SP                  
44A7: 33              INC     SP                  
44A8: 33              INC     SP                  
44A9: 33              INC     SP                  
44AA: 33              INC     SP                  
44AB: 33              INC     SP                  
44AC: 01 01 01        LD      BC,$0101            
44AF: 3D              DEC     A                   
44B0: 01 01 01        LD      BC,$0101            
44B3: 01 6F 01        LD      BC,$016F            
44B6: 01 01 01        LD      BC,$0101            
44B9: 01 01 01        LD      BC,$0101            
44BC: 01 01 01        LD      BC,$0101            
44BF: 3D              DEC     A                   
44C0: 66              LD      H,(HL)              
44C1: 66              LD      H,(HL)              
44C2: 66              LD      H,(HL)              
44C3: 01 01 66        LD      BC,$6601            
44C6: 66              LD      H,(HL)              
44C7: 66              LD      H,(HL)              
44C8: 65              LD      H,L                 
44C9: 65              LD      H,L                 
44CA: 65              LD      H,L                 
44CB: 65              LD      H,L                 
44CC: 66              LD      H,(HL)              
44CD: 66              LD      H,(HL)              
44CE: 65              LD      H,L                 
44CF: 3D              DEC     A                   
44D0: 65              LD      H,L                 
44D1: 65              LD      H,L                 
44D2: 65              LD      H,L                 
44D3: 65              LD      H,L                 
44D4: 66              LD      H,(HL)              
44D5: 66              LD      H,(HL)              
44D6: 66              LD      H,(HL)              
44D7: 0D              DEC     C                   
44D8: 0D              DEC     C                   
44D9: 09              ADD     HL,BC               
44DA: 65              LD      H,L                 
44DB: 09              ADD     HL,BC               
44DC: 09              ADD     HL,BC               
44DD: 09              ADD     HL,BC               
44DE: 00              NOP                         
44DF: 49              LD      C,C                 
44E0: 10 11           ;;STOP    $11                 
44E2: 20 2F           JR      NZ,$4513            ; {}
44E4: 01 0A 0A        LD      BC,$0A0A            
44E7: 0B              DEC     BC                  
44E8: 0C              INC     C                   
44E9: 09              ADD     HL,BC               
44EA: 4B              LD      C,E                 
44EB: 65              LD      H,L                 
44EC: 65              LD      H,L                 
44ED: 4C              LD      C,H                 
44EE: 65              LD      H,L                 
44EF: 65              LD      H,L                 
44F0: 10 12           ;;STOP    $12                 
44F2: 0B              DEC     BC                  
44F3: 65              LD      H,L                 
44F4: 09              ADD     HL,BC               
44F5: 01 65 65        LD      BC,$6565            
44F8: 65              LD      H,L                 
44F9: 65              LD      H,L                 
44FA: 65              LD      H,L                 
44FB: 65              LD      H,L                 
44FC: 65              LD      H,L                 
44FD: 65              LD      H,L                 
44FE: 0D              DEC     C                   
44FF: 0D              DEC     C                   
4500: 00              NOP                         
4501: 00              NOP                         
4502: 21 21 21        LD      HL,$2121            
4505: 21 21 22        LD      HL,$2221            
4508: 66              LD      H,(HL)              
4509: 65              LD      H,L                 
450A: 65              LD      H,L                 
450B: 09              ADD     HL,BC               
450C: 09              ADD     HL,BC               
450D: 66              LD      H,(HL)              
450E: 0D              DEC     C                   
450F: 0D              DEC     C                   
4510: 67              LD      H,A                 
4511: 67              LD      H,A                 
4512: 21 21 21        LD      HL,$2121            
4515: 21 21 40        LD      HL,$4021            
4518: 66              LD      H,(HL)              
4519: 41              LD      B,C                 
451A: 10 4D           ;;STOP    $4D                 
451C: 4D              LD      C,L                 
451D: 46              LD      B,(HL)              
451E: 66              LD      H,(HL)              
451F: 66              LD      H,(HL)              
4520: 3A              LD      A,(HLD)             
4521: 4E              LD      C,(HL)              
4522: 3A              LD      A,(HLD)             
4523: 09              ADD     HL,BC               
4524: 66              LD      H,(HL)              
4525: 66              LD      H,(HL)              
4526: 65              LD      H,L                 
4527: 65              LD      H,L                 
4528: 3B              DEC     SP                  
4529: 47              LD      B,A                 
452A: 65              LD      H,L                 
452B: 65              LD      H,L                 
452C: 65              LD      H,L                 
452D: 65              LD      H,L                 
452E: 65              LD      H,L                 
452F: 65              LD      H,L                 
4530: 3A              LD      A,(HLD)             
4531: 67              LD      H,A                 
4532: 67              LD      H,A                 
4533: 67              LD      H,A                 
4534: 66              LD      H,(HL)              
4535: 42              LD      B,D                 
4536: 65              LD      H,L                 
4537: 65              LD      H,L                 
4538: 3B              DEC     SP                  
4539: 67              LD      H,A                 
453A: 67              LD      H,A                 
453B: 43              LD      B,E                 
453C: 01 45 48        LD      BC,$4845            
453F: 00              NOP                         
4540: A4              AND     H                   
4541: FF              RST     0X38                
4542: FF              RST     0X38                
4543: FF              RST     0X38                
4544: A4              AND     H                   
4545: 8E              ADC     A,(HL)              
4546: 7C              LD      A,H                 
4547: C8              RET     Z                   
4548: A4              AND     H                   
4549: 4A              LD      C,D                 
454A: 7C              LD      A,H                 
454B: 93              SUB     E                   
454C: A4              AND     H                   
454D: E5              PUSH    HL                  
454E: FF              RST     0X38                
454F: 4E              LD      C,(HL)              
4550: A4              AND     H                   
4551: 91              SUB     C                   
4552: 83              ADD     A,E                 
4553: A2              AND     D                   
4554: A4              AND     H                   
4555: 42              LD      B,D                 
4556: 8A              ADC     A,D                 
4557: FF              RST     0X38                
4558: A4              AND     H                   
4559: 42              LD      B,D                 
455A: 83              ADD     A,E                 
455B: A2              AND     D                   
455C: A4              AND     H                   
455D: 81              ADD     A,C                 
455E: E3                              
455F: A2              AND     D                   
4560: A4              AND     H                   
4561: E5              PUSH    HL                  
4562: E3                              
4563: FF              RST     0X38                
4564: A4              AND     H                   
4565: E5              PUSH    HL                  
4566: 43              LD      B,E                 
4567: E7              RST     0X20                
4568: A4              AND     H                   
4569: E5              PUSH    HL                  
456A: E6 FF           AND     $FF                 
456C: A4              AND     H                   
456D: E5              PUSH    HL                  
456E: E6 E7           AND     $E7                 
4570: A4              AND     H                   
4571: E5              PUSH    HL                  
4572: 43              LD      B,E                 
4573: A4              AND     H                   
4574: A4              AND     H                   
4575: 8E              ADC     A,(HL)              
4576: 83              ADD     A,E                 
4577: A4              AND     H                   
4578: A4              AND     H                   
4579: 4A              LD      C,D                 
457A: 83              ADD     A,E                 
457B: 40              LD      B,B                 
457C: A4              AND     H                   
457D: E5              PUSH    HL                  
457E: 4C              LD      C,H                 
457F: E7              RST     0X20                
4580: A4              AND     H                   
4581: 4D              LD      C,L                 
4582: 83              ADD     A,E                 
4583: FF              RST     0X38                
4584: A4              AND     H                   
4585: 42              LD      B,D                 
4586: 92              SUB     D                   
4587: 5A              LD      E,D                 
4588: A4              AND     H                   
4589: 61              LD      H,C                 
458A: 92              SUB     D                   
458B: 67              LD      H,A                 
458C: A4              AND     H                   
458D: E5              PUSH    HL                  
458E: FF              RST     0X38                
458F: FF              RST     0X38                
4590: A4              AND     H                   
4591: E3                              
4592: 8B              ADC     A,E                 
4593: FF              RST     0X38                
4594: A4              AND     H                   
4595: E3                              
4596: 83              ADD     A,E                 
4597: 76              HALT                        
4598: A4              AND     H                   
4599: 81              ADD     A,C                 
459A: 79              LD      A,C                 
459B: 76              HALT                        
459C: A4              AND     H                   
459D: 61              LD      H,C                 
459E: 8B              ADC     A,E                 
459F: FF              RST     0X38                
45A0: A4              AND     H                   
45A1: 6C              LD      L,H                 
45A2: 8B              ADC     A,E                 
45A3: 6B              LD      L,E                 
45A4: A4              AND     H                   
45A5: FF              RST     0X38                
45A6: 8B              ADC     A,E                 
45A7: FF              RST     0X38                
45A8: A4              AND     H                   
45A9: E3                              
45AA: 8B              ADC     A,E                 
45AB: A2              AND     D                   
45AC: A4              AND     H                   
45AD: E5              PUSH    HL                  
45AE: FF              RST     0X38                
45AF: FF              RST     0X38                
45B0: A4              AND     H                   
45B1: 4A              LD      C,D                 
45B2: 8F              ADC     A,A                 
45B3: 6D              LD      L,L                 
45B4: A4              AND     H                   
45B5: 81              ADD     A,C                 
45B6: 6E              LD      L,(HL)              
45B7: 52              LD      D,D                 
45B8: A4              AND     H                   
45B9: 4D              LD      C,L                 
45BA: 43              LD      B,E                 
45BB: A2              AND     D                   
45BC: A4              AND     H                   
45BD: 61              LD      H,C                 
45BE: 79              LD      A,C                 
45BF: 76              HALT                        
45C0: A4              AND     H                   
45C1: C6 7C           ADD     $7C                 
45C3: 41              LD      B,C                 
45C4: A4              AND     H                   
45C5: C5              PUSH    BC                  
45C6: 6E              LD      L,(HL)              
45C7: 6F              LD      L,A                 
45C8: A4              AND     H                   
45C9: C5              PUSH    BC                  
45CA: FF              RST     0X38                
45CB: 70              LD      (HL),B              
45CC: A4              AND     H                   
45CD: 61              LD      H,C                 
45CE: FF              RST     0X38                
45CF: 71              LD      (HL),C              
45D0: A4              AND     H                   
45D1: 61              LD      H,C                 
45D2: FF              RST     0X38                
45D3: 72              LD      (HL),D              
45D4: A4              AND     H                   
45D5: 61              LD      H,C                 
45D6: 79              LD      A,C                 
45D7: 73              LD      (HL),E              
45D8: A4              AND     H                   
45D9: 61              LD      H,C                 
45DA: 79              LD      A,C                 
45DB: FF              RST     0X38                
45DC: A4              AND     H                   
45DD: E3                              
45DE: 79              LD      A,C                 
45DF: 76              HALT                        
45E0: A4              AND     H                   
45E1: 42              LD      B,D                 
45E2: 82              ADD     A,D                 
45E3: A2              AND     D                   
45E4: A4              AND     H                   
45E5: 42              LD      B,D                 
45E6: FF              RST     0X38                
45E7: FF              RST     0X38                
45E8: A4              AND     H                   
45E9: 61              LD      H,C                 
45EA: 78              LD      A,B                 
45EB: A2              AND     D                   
45EC: A4              AND     H                   
45ED: 81              ADD     A,C                 
45EE: 8F              ADC     A,A                 
45EF: E7              RST     0X20                
45F0: A4              AND     H                   
45F1: E3                              
45F2: 8B              ADC     A,E                 
45F3: 8C              ADC     A,H                 
45F4: A4              AND     H                   
45F5: 87              ADD     A,A                 
45F6: 78              LD      A,B                 
45F7: A2              AND     D                   
45F8: A4              AND     H                   
45F9: 6C              LD      L,H                 
45FA: 7C              LD      A,H                 
45FB: C8              RET     Z                   
45FC: A4              AND     H                   
45FD: C4 E6 CF        CALL    NZ,$CFE6            
4600: A4              AND     H                   
4601: FF              RST     0X38                
4602: 6E              LD      L,(HL)              
4603: 6F              LD      L,A                 
4604: A4              AND     H                   
4605: FF              RST     0X38                
4606: E6 CF           AND     $CF                 
4608: A4              AND     H                   
4609: FF              RST     0X38                
460A: 83              ADD     A,E                 
460B: FF              RST     0X38                
460C: A4              AND     H                   
460D: C4 79 76        CALL    NZ,$7679            ; {}
4610: A4              AND     H                   
4611: C4 FF FF        CALL    NZ,$FFFF            ; {hard.ISWITCH}
4614: A4              AND     H                   
4615: C4 43 CF        CALL    NZ,$CF43            
4618: A4              AND     H                   
4619: FF              RST     0X38                
461A: 79              LD      A,C                 
461B: FF              RST     0X38                
461C: A4              AND     H                   
461D: FF              RST     0X38                
461E: FF              RST     0X38                
461F: A2              AND     D                   
4620: A4              AND     H                   
4621: 61              LD      H,C                 
4622: 79              LD      A,C                 
4623: A2              AND     D                   
4624: A4              AND     H                   
4625: E5              PUSH    HL                  
4626: FF              RST     0X38                
4627: FF              RST     0X38                
4628: A4              AND     H                   
4629: E5              PUSH    HL                  
462A: 82              ADD     A,D                 
462B: A2              AND     D                   
462C: A4              AND     H                   
462D: E3                              
462E: 83              ADD     A,E                 
462F: A2              AND     D                   
4630: A4              AND     H                   
4631: 91              SUB     C                   
4632: 83              ADD     A,E                 
4633: 76              HALT                        
4634: A4              AND     H                   
4635: FF              RST     0X38                
4636: 7C              LD      A,H                 
4637: A2              AND     D                   
4638: A4              AND     H                   
4639: E3                              
463A: 8B              ADC     A,E                 
463B: A2              AND     D                   
463C: A4              AND     H                   
463D: E3                              
463E: FF              RST     0X38                
463F: 76              HALT                        
4640: A4              AND     H                   
4641: FF              RST     0X38                
4642: E6 A2           AND     $A2                 
4644: A4              AND     H                   
4645: FF              RST     0X38                
4646: 7C              LD      A,H                 
4647: A2              AND     D                   
4648: A4              AND     H                   
4649: 81              ADD     A,C                 
464A: E3                              
464B: D4 A4 E5        CALL    NC,$E5A4            
464E: E6 DC           AND     $DC                 
4650: A4              AND     H                   
4651: 87              ADD     A,A                 
4652: D6 D7           SUB     $D7                 
4654: A4              AND     H                   
4655: 50              LD      D,B                 
4656: 51              LD      D,C                 
4657: A2              AND     D                   
4658: A4              AND     H                   
4659: 6C              LD      L,H                 
465A: 8F              ADC     A,A                 
465B: A2              AND     D                   
465C: A4              AND     H                   
465D: 4A              LD      C,D                 
465E: 83              ADD     A,E                 
465F: A2              AND     D                   
4660: A4              AND     H                   
4661: 4A              LD      C,D                 
4662: 83              ADD     A,E                 
4663: FF              RST     0X38                
4664: A4              AND     H                   
4665: 81              ADD     A,C                 
4666: 8F              ADC     A,A                 
4667: 76              HALT                        
4668: A4              AND     H                   
4669: E3                              
466A: 8B              ADC     A,E                 
466B: FF              RST     0X38                
466C: A4              AND     H                   
466D: FF              RST     0X38                
466E: 79              LD      A,C                 
466F: FF              RST     0X38                
4670: A4              AND     H                   
4671: 81              ADD     A,C                 
4672: 6E              LD      L,(HL)              
4673: FF              RST     0X38                
4674: A4              AND     H                   
4675: 81              ADD     A,C                 
4676: 6E              LD      L,(HL)              
4677: 8C              ADC     A,H                 
4678: A4              AND     H                   
4679: 87              ADD     A,A                 
467A: 8F              ADC     A,A                 
467B: 76              HALT                        
467C: A4              AND     H                   
467D: FF              RST     0X38                
467E: 8F              ADC     A,A                 
467F: FF              RST     0X38                
4680: A4              AND     H                   
4681: 87              ADD     A,A                 
4682: FF              RST     0X38                
4683: FF              RST     0X38                
4684: A4              AND     H                   
4685: 87              ADD     A,A                 
4686: 83              ADD     A,E                 
4687: 76              HALT                        
4688: A4              AND     H                   
4689: 87              ADD     A,A                 
468A: 83              ADD     A,E                 
468B: 98              SBC     B                   
468C: A4              AND     H                   
468D: FF              RST     0X38                
468E: 79              LD      A,C                 
468F: 76              HALT                        
4690: A4              AND     H                   
4691: E3                              
4692: 83              ADD     A,E                 
4693: A2              AND     D                   
4694: A4              AND     H                   
4695: 61              LD      H,C                 
4696: 79              LD      A,C                 
4697: 93              SUB     E                   
4698: A4              AND     H                   
4699: FF              RST     0X38                
469A: 79              LD      A,C                 
469B: 93              SUB     E                   
469C: A4              AND     H                   
469D: C4 79 FF        CALL    NZ,$FF79            
46A0: A4              AND     H                   
46A1: FF              RST     0X38                
46A2: 92              SUB     D                   
46A3: 5A              LD      E,D                 
46A4: A4              AND     H                   
46A5: 61              LD      H,C                 
46A6: 92              SUB     D                   
46A7: 8C              ADC     A,H                 
46A8: A4              AND     H                   
46A9: 42              LD      B,D                 
46AA: 92              SUB     D                   
46AB: FF              RST     0X38                
46AC: A4              AND     H                   
46AD: 61              LD      H,C                 
46AE: FF              RST     0X38                
46AF: FF              RST     0X38                
46B0: A4              AND     H                   
46B1: 61              LD      H,C                 
46B2: FF              RST     0X38                
46B3: 8C              ADC     A,H                 
46B4: A4              AND     H                   
46B5: FF              RST     0X38                
46B6: 83              ADD     A,E                 
46B7: 93              SUB     E                   
46B8: A4              AND     H                   
46B9: 61              LD      H,C                 
46BA: 8B              ADC     A,E                 
46BB: FF              RST     0X38                
46BC: A4              AND     H                   
46BD: E3                              
46BE: FF              RST     0X38                
46BF: FF              RST     0X38                
46C0: A4              AND     H                   
46C1: 61              LD      H,C                 
46C2: FF              RST     0X38                
46C3: 67              LD      H,A                 
46C4: A4              AND     H                   
46C5: FF              RST     0X38                
46C6: FF              RST     0X38                
46C7: A2              AND     D                   
46C8: A4              AND     H                   
46C9: 87              ADD     A,A                 
46CA: E3                              
46CB: 93              SUB     E                   
46CC: A4              AND     H                   
46CD: 87              ADD     A,A                 
46CE: FF              RST     0X38                
46CF: FF              RST     0X38                
46D0: A4              AND     H                   
46D1: 87              ADD     A,A                 
46D2: 92              SUB     D                   
46D3: 5A              LD      E,D                 
46D4: A4              AND     H                   
46D5: C6 9C           ADD     $9C                 
46D7: 98              SBC     B                   
46D8: A4              AND     H                   
46D9: C6 9C           ADD     $9C                 
46DB: FF              RST     0X38                
46DC: A4              AND     H                   
46DD: FF              RST     0X38                
46DE: 9C              SBC     H                   
46DF: 93              SUB     E                   
46E0: A4              AND     H                   
46E1: 81              ADD     A,C                 
46E2: FF              RST     0X38                
46E3: FF              RST     0X38                
46E4: A4              AND     H                   
46E5: FF              RST     0X38                
46E6: 9C              SBC     H                   
46E7: 98              SBC     B                   
46E8: A4              AND     H                   
46E9: FF              RST     0X38                
46EA: 83              ADD     A,E                 
46EB: FF              RST     0X38                
46EC: A4              AND     H                   
46ED: 81              ADD     A,C                 
46EE: FF              RST     0X38                
46EF: 93              SUB     E                   
46F0: A4              AND     H                   
46F1: 81              ADD     A,C                 
46F2: 9C              SBC     H                   
46F3: 93              SUB     E                   
46F4: A4              AND     H                   
46F5: 44              LD      B,H                 
46F6: 9C              SBC     H                   
46F7: 98              SBC     B                   
46F8: A4              AND     H                   
46F9: 91              SUB     C                   
46FA: 78              LD      A,B                 
46FB: A2              AND     D                   
46FC: A4              AND     H                   
46FD: FF              RST     0X38                
46FE: 78              LD      A,B                 
46FF: A2              AND     D                   
4700: A4              AND     H                   
4701: 61              LD      H,C                 
4702: FF              RST     0X38                
4703: A2              AND     D                   
4704: A4              AND     H                   
4705: FF              RST     0X38                
4706: 79              LD      A,C                 
4707: A2              AND     D                   
4708: A4              AND     H                   
4709: 61              LD      H,C                 
470A: 83              ADD     A,E                 
470B: FF              RST     0X38                
470C: A4              AND     H                   
470D: FF              RST     0X38                
470E: 83              ADD     A,E                 
470F: A2              AND     D                   
4710: A4              AND     H                   
4711: FF              RST     0X38                
4712: 7C              LD      A,H                 
4713: FF              RST     0X38                
4714: A4              AND     H                   
4715: E3                              
4716: 8B              ADC     A,E                 
4717: A2              AND     D                   
4718: A4              AND     H                   
4719: E3                              
471A: 83              ADD     A,E                 
471B: FF              RST     0X38                
471C: A4              AND     H                   
471D: FF              RST     0X38                
471E: 83              ADD     A,E                 
471F: 76              HALT                        
4720: A4              AND     H                   
4721: 61              LD      H,C                 
4722: 83              ADD     A,E                 
4723: FF              RST     0X38                
4724: A4              AND     H                   
4725: 61              LD      H,C                 
4726: FF              RST     0X38                
4727: 76              HALT                        
4728: A4              AND     H                   
4729: 61              LD      H,C                 
472A: FF              RST     0X38                
472B: A2              AND     D                   
472C: A4              AND     H                   
472D: 81              ADD     A,C                 
472E: 6E              LD      L,(HL)              
472F: FF              RST     0X38                
4730: A4              AND     H                   
4731: 81              ADD     A,C                 
4732: FF              RST     0X38                
4733: 8C              ADC     A,H                 
4734: A4              AND     H                   
4735: 4A              LD      C,D                 
4736: 7C              LD      A,H                 
4737: 93              SUB     E                   
4738: A4              AND     H                   
4739: 91              SUB     C                   
473A: 7C              LD      A,H                 
473B: A2              AND     D                   
473C: A4              AND     H                   
473D: 4D              LD      C,L                 
473E: 7C              LD      A,H                 
473F: FF              RST     0X38                
4740: A4              AND     H                   
4741: FF              RST     0X38                
4742: FF              RST     0X38                
4743: FF              RST     0X38                
4744: A4              AND     H                   
4745: FF              RST     0X38                
4746: FF              RST     0X38                
4747: FF              RST     0X38                
4748: A4              AND     H                   
4749: FF              RST     0X38                
474A: FF              RST     0X38                
474B: FF              RST     0X38                
474C: A4              AND     H                   
474D: FF              RST     0X38                
474E: FF              RST     0X38                
474F: FF              RST     0X38                
4750: A4              AND     H                   
4751: FF              RST     0X38                
4752: FF              RST     0X38                
4753: FF              RST     0X38                
4754: A4              AND     H                   
4755: FF              RST     0X38                
4756: FF              RST     0X38                
4757: FF              RST     0X38                
4758: A4              AND     H                   
4759: FF              RST     0X38                
475A: FF              RST     0X38                
475B: FF              RST     0X38                
475C: A4              AND     H                   
475D: FF              RST     0X38                
475E: FF              RST     0X38                
475F: FF              RST     0X38                
4760: A4              AND     H                   
4761: FF              RST     0X38                
4762: FF              RST     0X38                
4763: FF              RST     0X38                
4764: A4              AND     H                   
4765: FF              RST     0X38                
4766: FF              RST     0X38                
4767: FF              RST     0X38                
4768: A4              AND     H                   
4769: FF              RST     0X38                
476A: FF              RST     0X38                
476B: FF              RST     0X38                
476C: A4              AND     H                   
476D: FF              RST     0X38                
476E: FF              RST     0X38                
476F: FF              RST     0X38                
4770: A4              AND     H                   
4771: FF              RST     0X38                
4772: FF              RST     0X38                
4773: FF              RST     0X38                
4774: A4              AND     H                   
4775: FF              RST     0X38                
4776: FF              RST     0X38                
4777: FF              RST     0X38                
4778: A4              AND     H                   
4779: FF              RST     0X38                
477A: FF              RST     0X38                
477B: FF              RST     0X38                
477C: A4              AND     H                   
477D: FF              RST     0X38                
477E: FF              RST     0X38                
477F: FF              RST     0X38                
4780: A4              AND     H                   
4781: 81              ADD     A,C                 
4782: 8F              ADC     A,A                 
4783: D4 A4 81        CALL    NC,$81A4            
4786: 79              LD      A,C                 
4787: FF              RST     0X38                
4788: FF              RST     0X38                
4789: FF              RST     0X38                
478A: FF              RST     0X38                
478B: FF              RST     0X38                
478C: 90              SUB     B                   
478D: 91              SUB     C                   
478E: 92              SUB     D                   
478F: 98              SBC     B                   
4790: 90              SUB     B                   
4791: 91              SUB     C                   
4792: AB              XOR     E                   
4793: FF              RST     0X38                
4794: 90              SUB     B                   
4795: 91              SUB     C                   
4796: 92              SUB     D                   
4797: 93              SUB     E                   
4798: 90              SUB     B                   
4799: 91              SUB     C                   
479A: 94              SUB     H                   
479B: 9F              SBC     A                   
479C: 90              SUB     B                   
479D: 91              SUB     C                   
479E: B0              OR      B                   
479F: B1              OR      C                   
47A0: 90              SUB     B                   
47A1: 91              SUB     C                   
47A2: 9C              SBC     H                   
47A3: 93              SUB     E                   
47A4: 90              SUB     B                   
47A5: 91              SUB     C                   
47A6: 97              SUB     A                   
47A7: 9B              SBC     E                   
47A8: FF              RST     0X38                
47A9: FF              RST     0X38                
47AA: B6              OR      (HL)                
47AB: B7              OR      A                   
47AC: A4              AND     H                   
47AD: 4C              LD      C,H                 
47AE: 49              LD      C,C                 
47AF: 46              LD      B,(HL)              
47B0: A4              AND     H                   
47B1: FF              RST     0X38                
47B2: 45              LD      B,L                 
47B3: 6D              LD      L,L                 
47B4: A4              AND     H                   
47B5: FF              RST     0X38                
47B6: 47              LD      B,A                 
47B7: 48              LD      C,B                 
47B8: A4              AND     H                   
47B9: FF              RST     0X38                
47BA: 4C              LD      C,H                 
47BB: 4B              LD      C,E                 
47BC: 90              SUB     B                   
47BD: 91              SUB     C                   
47BE: 96              SUB     (HL)                
47BF: FF              RST     0X38                
47C0: FF              RST     0X38                
47C1: FF              RST     0X38                
47C2: 4F              LD      C,A                 
47C3: 50              LD      D,B                 
47C4: FF              RST     0X38                
47C5: FF              RST     0X38                
47C6: 4F              LD      C,A                 
47C7: 51              LD      D,C                 
47C8: A4              AND     H                   
47C9: 87              ADD     A,A                 
47CA: 84              ADD     A,H                 
47CB: 89              ADC     A,C                 
47CC: A4              AND     H                   
47CD: FF              RST     0X38                
47CE: 88              ADC     A,B                 
47CF: C7              RST     0X00                
47D0: A0              AND     B                   
47D1: A1              AND     C                   
47D2: 84              ADD     A,H                 
47D3: 83              ADD     A,E                 
47D4: 90              SUB     B                   
47D5: 91              SUB     C                   
47D6: 54              LD      D,H                 
47D7: A6              AND     (HL)                
47D8: 90              SUB     B                   
47D9: 91              SUB     C                   
47DA: 97              SUB     A                   
47DB: 93              SUB     E                   
47DC: 90              SUB     B                   
47DD: 91              SUB     C                   
47DE: AA              XOR     D                   
47DF: FF              RST     0X38                
47E0: 90              SUB     B                   
47E1: 91              SUB     C                   
47E2: B4              OR      H                   
47E3: B5              OR      L                   
47E4: 90              SUB     B                   
47E5: 91              SUB     C                   
47E6: 9C              SBC     H                   
47E7: 9E              SBC     (HL)                
47E8: 90              SUB     B                   
47E9: 91              SUB     C                   
47EA: 9C              SBC     H                   
47EB: 9D              SBC     L                   
47EC: 68              LD      L,B                 
47ED: 91              SUB     C                   
47EE: 56              LD      D,(HL)              
47EF: 60              LD      H,B                 
47F0: AC              XOR     H                   
47F1: AD              XOR     L                   
47F2: AE              XOR     (HL)                
47F3: AF              XOR     A                   
47F4: 90              SUB     B                   
47F5: 91              SUB     C                   
47F6: 58              LD      E,B                 
47F7: 9B              SBC     E                   
47F8: 90              SUB     B                   
47F9: 91              SUB     C                   
47FA: A6              AND     (HL)                
47FB: 59              LD      E,C                 
47FC: FF              RST     0X38                
47FD: FF              RST     0X38                
47FE: B8              CP      B                   
47FF: B9              CP      C                   
4800: 90              SUB     B                   
4801: 91              SUB     C                   
4802: 62              LD      H,D                 
4803: 63              LD      H,E                 
4804: 90              SUB     B                   
4805: 91              SUB     C                   
4806: A8              XOR     B                   
4807: 9F              SBC     A                   
4808: A4              AND     H                   
4809: DF              RST     0X18                
480A: A3              AND     E                   
480B: FF              RST     0X38                
480C: 90              SUB     B                   
480D: 91              SUB     C                   
480E: 92              SUB     D                   
480F: 9A              SBC     D                   
4810: A4              AND     H                   
4811: 5B              LD      E,E                 
4812: 5C              LD      E,H                 
4813: FF              RST     0X38                
4814: A6              AND     (HL)                
4815: 91              SUB     C                   
4816: 97              SUB     A                   
4817: 9B              SBC     E                   
4818: 90              SUB     B                   
4819: 91              SUB     C                   
481A: 9C              SBC     H                   
481B: 60              LD      H,B                 
481C: FF              RST     0X38                
481D: FF              RST     0X38                
481E: B2              OR      D                   
481F: B3              OR      E                   
4820: A6              AND     (HL)                
4821: 91              SUB     C                   
4822: 57              LD      D,A                 
4823: FF              RST     0X38                
4824: A6              AND     (HL)                
4825: 91              SUB     C                   
4826: 95              SUB     L                   
4827: 98              SBC     B                   
4828: A6              AND     (HL)                
4829: 91              SUB     C                   
482A: 5E              LD      E,(HL)              
482B: 60              LD      H,B                 
482C: A6              AND     (HL)                
482D: 91              SUB     C                   
482E: AA              XOR     D                   
482F: 93              SUB     E                   
4830: A6              AND     (HL)                
4831: 91              SUB     C                   
4832: 58              LD      E,B                 
4833: 99              SBC     C                   
4834: 90              SUB     B                   
4835: 91              SUB     C                   
4836: 95              SUB     L                   
4837: 93              SUB     E                   
4838: 5F              LD      E,A                 
4839: 91              SUB     C                   
483A: 55              LD      D,L                 
483B: 99              SBC     C                   
483C: 66              LD      H,(HL)              
483D: 91              SUB     C                   
483E: 5E              LD      E,(HL)              
483F: 59              LD      E,C                 
4840: 66              LD      H,(HL)              
4841: 91              SUB     C                   
4842: 54              LD      D,H                 
4843: 59              LD      E,C                 
4844: 8D              ADC     A,L                 
4845: 8E              ADC     A,(HL)              
4846: 8F              ADC     A,A                 
4847: 6A              LD      L,D                 
4848: 68              LD      L,B                 
4849: 91              SUB     C                   
484A: 9B              SBC     E                   
484B: 60              LD      H,B                 
484C: 68              LD      L,B                 
484D: 91              SUB     C                   
484E: 94              SUB     H                   
484F: 9F              SBC     A                   
4850: 68              LD      L,B                 
4851: 91              SUB     C                   
4852: 9C              SBC     H                   
4853: 60              LD      H,B                 
4854: 5F              LD      E,A                 
4855: 65              LD      H,L                 
4856: 5D              LD      E,L                 
4857: 64              LD      H,H                 
4858: FF              RST     0X38                
4859: 91              SUB     C                   
485A: 55              LD      D,L                 
485B: FF              RST     0X38                
485C: 5F              LD      E,A                 
485D: 91              SUB     C                   
485E: 95              SUB     L                   
485F: 99              SBC     C                   
4860: 5F              LD      E,A                 
4861: 91              SUB     C                   
4862: 5E              LD      E,(HL)              
4863: 99              SBC     C                   
4864: 5F              LD      E,A                 
4865: 91              SUB     C                   
4866: A9              XOR     C                   
4867: FF              RST     0X38                
4868: 5F              LD      E,A                 
4869: 91              SUB     C                   
486A: 94              SUB     H                   
486B: 9F              SBC     A                   
486C: 90              SUB     B                   
486D: 91              SUB     C                   
486E: 55              LD      D,L                 
486F: 93              SUB     E                   
4870: A4              AND     H                   
4871: FF              RST     0X38                
4872: 7C              LD      A,H                 
4873: FF              RST     0X38                
4874: BC              CP      H                   
4875: BD              CP      L                   
4876: BE              CP      (HL)                
4877: BF              CP      A                   
4878: A6              AND     (HL)                
4879: 91              SUB     C                   
487A: 9C              SBC     H                   
487B: 9D              SBC     L                   
487C: FF              RST     0X38                
487D: D5              PUSH    DE                  
487E: 78              LD      A,B                 
487F: 53              LD      D,E                 
4880: 90              SUB     B                   
4881: 91              SUB     C                   
4882: FF              RST     0X38                
4883: FF              RST     0X38                
4884: 5F              LD      E,A                 
4885: 91              SUB     C                   
4886: 55              LD      D,L                 
4887: 98              SBC     B                   
4888: A4              AND     H                   
4889: FF              RST     0X38                
488A: FF              RST     0X38                
488B: 69              LD      L,C                 
488C: A4              AND     H                   
488D: FF              RST     0X38                
488E: 4C              LD      C,H                 
488F: 74              LD      (HL),H              
4890: A0              AND     B                   
4891: A1              AND     C                   
4892: 75              LD      (HL),L              
4893: 4E              LD      C,(HL)              
4894: A4              AND     H                   
4895: 7D              LD      A,L                 
4896: 7E              LD      A,(HL)              
4897: 7F              LD      A,A                 
4898: A4              AND     H                   
4899: FF              RST     0X38                
489A: FF              RST     0X38                
489B: C7              RST     0X00                
489C: C0              RET     NZ                  
489D: C1              POP     BC                  
489E: C2 C3 A4        JP      NZ,$A4C3            
48A1: CC CD CE        CALL    Z,$CECD             
48A4: A4              AND     H                   
48A5: C9              RET                         
48A6: CA CB A4        JP      Z,$A4CB             
48A9: D1              POP     DE                  
48AA: D2 6A DD        JP      NC,$DD6A            
48AD: E5              PUSH    HL                  
48AE: D3                              
48AF: DD                              
48B0: DD                              
48B1: FF              RST     0X38                
48B2: DE FF           SBC     $FF                 
48B4: A4              AND     H                   
48B5: 8D              ADC     A,L                 
48B6: FF              RST     0X38                
48B7: FF              RST     0X38                
48B8: FF              RST     0X38                
48B9: DF              RST     0X18                
48BA: 49              LD      C,C                 
48BB: FF              RST     0X38                
48BC: FF              RST     0X38                
48BD: C4 FF FF        CALL    NZ,$FFFF            ; {hard.ISWITCH}
48C0: A4              AND     H                   
48C1: 80              ADD     A,B                 
48C2: 7C              LD      A,H                 
48C3: A5              AND     L                   
48C4: FF              RST     0X38                
48C5: FF              RST     0X38                
48C6: FF              RST     0X38                
48C7: FF              RST     0X38                
48C8: FF              RST     0X38                
48C9: FF              RST     0X38                
48CA: BA              CP      D                   
48CB: BB              CP      E                   
48CC: 77              LD      (HL),A              
48CD: 91              SUB     C                   
48CE: A7              AND     A                   
48CF: FF              RST     0X38                
48D0: 7B              LD      A,E                 
48D1: 91              SUB     C                   
48D2: 7A              LD      A,D                 
48D3: AB              XOR     E                   
48D4: 7B              LD      A,E                 
48D5: 91              SUB     C                   
48D6: 57              LD      D,A                 
48D7: 99              SBC     C                   
48D8: 77              LD      (HL),A              
48D9: 91              SUB     C                   
48DA: 7A              LD      A,D                 
48DB: AA              XOR     D                   
48DC: 7B              LD      A,E                 
48DD: 91              SUB     C                   
48DE: 54              LD      D,H                 
48DF: 99              SBC     C                   
48E0: 7B              LD      A,E                 
48E1: 91              SUB     C                   
48E2: 56              LD      D,(HL)              
48E3: FF              RST     0X38                
48E4: 77              LD      (HL),A              
48E5: 91              SUB     C                   
48E6: 54              LD      D,H                 
48E7: 99              SBC     C                   
48E8: 7B              LD      A,E                 
48E9: 91              SUB     C                   
48EA: FF              RST     0X38                
48EB: FF              RST     0X38                
48EC: 5F              LD      E,A                 
48ED: 91              SUB     C                   
48EE: 9D              SBC     L                   
48EF: 99              SBC     C                   
48F0: 7B              LD      A,E                 
48F1: 91              SUB     C                   
48F2: 96              SUB     (HL)                
48F3: 99              SBC     C                   
48F4: 7B              LD      A,E                 
48F5: 91              SUB     C                   
48F6: 7A              LD      A,D                 
48F7: 99              SBC     C                   
48F8: 77              LD      (HL),A              
48F9: 91              SUB     C                   
48FA: 7A              LD      A,D                 
48FB: 99              SBC     C                   
48FC: 77              LD      (HL),A              
48FD: 91              SUB     C                   
48FE: 96              SUB     (HL)                
48FF: 99              SBC     C                   
4900: 5F              LD      E,A                 
4901: 91              SUB     C                   
4902: 55              LD      D,L                 
4903: 93              SUB     E                   
4904: FF              RST     0X38                
4905: 91              SUB     C                   
4906: 95              SUB     L                   
4907: 93              SUB     E                   
4908: 90              SUB     B                   
4909: 91              SUB     C                   
490A: 55              LD      D,L                 
490B: 93              SUB     E                   
490C: A6              AND     (HL)                
490D: 91              SUB     C                   
490E: 95              SUB     L                   
490F: 60              LD      H,B                 
4910: A6              AND     (HL)                
4911: 91              SUB     C                   
4912: 95              SUB     L                   
4913: 99              SBC     C                   
4914: 5F              LD      E,A                 
4915: D9              RETI                        
4916: DA DB 5F        JP      C,$5FDB             ; {}
4919: D9              RETI                        
491A: DA 64 FF        JP      C,$FF64             
491D: 91              SUB     C                   
491E: 90              SUB     B                   
491F: 76              HALT                        
4920: FF              RST     0X38                
4921: 91              SUB     C                   
4922: 90              SUB     B                   
4923: 98              SBC     B                   
4924: FF              RST     0X38                
4925: 4A              LD      C,D                 
4926: 90              SUB     B                   
4927: 76              HALT                        
4928: 5F              LD      E,A                 
4929: FF              RST     0X38                
492A: FF              RST     0X38                
492B: FF              RST     0X38                
492C: FF              RST     0X38                
492D: FF              RST     0X38                
492E: FF              RST     0X38                
492F: FF              RST     0X38                
4930: FF              RST     0X38                
4931: FF              RST     0X38                
4932: FF              RST     0X38                
4933: FF              RST     0X38                
4934: FF              RST     0X38                
4935: FF              RST     0X38                
4936: FF              RST     0X38                
4937: FF              RST     0X38                
4938: FF              RST     0X38                
4939: FF              RST     0X38                
493A: FF              RST     0X38                
493B: FF              RST     0X38                
493C: FF              RST     0X38                
493D: 91              SUB     C                   
493E: 90              SUB     B                   
493F: A6              AND     (HL)                
4940: A4              AND     H                   
4941: FF              RST     0X38                
4942: FF              RST     0X38                
4943: F4                              
4944: E8 E9           ADD     SP,$E9              
4946: EA EB FF        LD      ($FFEB),A           
4949: FF              RST     0X38                
494A: FF              RST     0X38                
494B: FF              RST     0X38                
494C: FF              RST     0X38                
494D: FF              RST     0X38                
494E: FF              RST     0X38                
494F: FF              RST     0X38                
4950: FF              RST     0X38                
4951: FF              RST     0X38                
4952: FF              RST     0X38                
4953: FF              RST     0X38                
4954: FF              RST     0X38                
4955: FF              RST     0X38                
4956: FF              RST     0X38                
4957: FF              RST     0X38                
4958: FF              RST     0X38                
4959: FF              RST     0X38                
495A: FF              RST     0X38                
495B: FF              RST     0X38                
495C: FF              RST     0X38                
495D: FF              RST     0X38                
495E: FF              RST     0X38                
495F: FF              RST     0X38                
4960: FF              RST     0X38                
4961: FF              RST     0X38                
4962: FF              RST     0X38                
4963: FF              RST     0X38                
4964: FF              RST     0X38                
4965: FF              RST     0X38                
4966: FF              RST     0X38                
4967: FF              RST     0X38                
4968: FF              RST     0X38                
4969: FF              RST     0X38                
496A: FF              RST     0X38                
496B: FF              RST     0X38                
496C: FF              RST     0X38                
496D: FF              RST     0X38                
496E: FF              RST     0X38                
496F: FF              RST     0X38                
4970: FF              RST     0X38                
4971: FF              RST     0X38                
4972: FF              RST     0X38                
4973: FF              RST     0X38                
4974: FF              RST     0X38                
4975: FF              RST     0X38                
4976: FF              RST     0X38                
4977: FF              RST     0X38                
4978: FF              RST     0X38                
4979: FF              RST     0X38                
497A: FF              RST     0X38                
497B: FF              RST     0X38                
497C: FF              RST     0X38                
497D: FF              RST     0X38                
497E: FF              RST     0X38                
497F: FF              RST     0X38                
4980: A4              AND     H                   
4981: FF              RST     0X38                
4982: 86              ADD     A,(HL)              
4983: FF              RST     0X38                
4984: A4              AND     H                   
4985: FF              RST     0X38                
4986: 8B              ADC     A,E                 
4987: FF              RST     0X38                
4988: A4              AND     H                   
4989: 4D              LD      C,L                 
498A: FF              RST     0X38                
498B: FF              RST     0X38                
498C: 7C              LD      A,H                 
498D: 7C              LD      A,H                 
498E: 7C              LD      A,H                 
498F: 7C              LD      A,H                 
4990: 7D              LD      A,L                 
4991: 7D              LD      A,L                 
4992: 7D              LD      A,L                 
4993: 7D              LD      A,L                 
4994: 7E              LD      A,(HL)              
4995: 7E              LD      A,(HL)              
4996: 7E              LD      A,(HL)              
4997: 7E              LD      A,(HL)              
4998: 76              HALT                        
4999: 76              HALT                        
499A: 76              HALT                        
499B: 76              HALT                        
499C: 5A              LD      E,D                 
499D: 7F              LD      A,A                 
499E: 7F              LD      A,A                 
499F: 5A              LD      E,D                 
49A0: 7C              LD      A,H                 
49A1: 7C              LD      A,H                 
49A2: 7C              LD      A,H                 
49A3: 00              NOP                         
49A4: 7C              LD      A,H                 
49A5: 7C              LD      A,H                 
49A6: 01 02 7C        LD      BC,$7C02            
49A9: 7C              LD      A,H                 
49AA: 03              INC     BC                  
49AB: 7C              LD      A,H                 
49AC: 0C              INC     C                   
49AD: 0D              DEC     C                   
49AE: 1C              INC     E                   
49AF: 1D              DEC     E                   
49B0: 72              LD      (HL),D              
49B1: 73              LD      (HL),E              
49B2: 73              LD      (HL),E              
49B3: 72              LD      (HL),D              
49B4: 75              LD      (HL),L              
49B5: 75              LD      (HL),L              
49B6: 75              LD      (HL),L              
49B7: 75              LD      (HL),L              
49B8: 74              LD      (HL),H              
49B9: 74              LD      (HL),H              
49BA: 74              LD      (HL),H              
49BB: 74              LD      (HL),H              
49BC: 0F              RRCA                        
49BD: 0F              RRCA                        
49BE: 0F              RRCA                        
49BF: 0F              RRCA                        
49C0: 0E 0E           LD      C,$0E               
49C2: 0E 0E           LD      C,$0E               
49C4: 6D              LD      L,L                 
49C5: 6D              LD      L,L                 
49C6: 6D              LD      L,L                 
49C7: 6D              LD      L,L                 
49C8: 5A              LD      E,D                 
49C9: 7F              LD      A,A                 
49CA: 04              INC     B                   
49CB: 04              INC     B                   
49CC: 14              INC     D                   
49CD: 14              INC     D                   
49CE: 7F              LD      A,A                 
49CF: 5A              LD      E,D                 
49D0: 5A              LD      E,D                 
49D1: 15              DEC     D                   
49D2: 7F              LD      A,A                 
49D3: 15              DEC     D                   
49D4: 05              DEC     B                   
49D5: 7F              LD      A,A                 
49D6: 05              DEC     B                   
49D7: 5A              LD      E,D                 
49D8: 5A              LD      E,D                 
49D9: 7F              LD      A,A                 
49DA: 7F              LD      A,A                 
49DB: 17              RLA                         
49DC: 5A              LD      E,D                 
49DD: 7F              LD      A,A                 
49DE: 06 5A           LD      B,$5A               
49E0: 5A              LD      E,D                 
49E1: 07              RLCA                        
49E2: 7F              LD      A,A                 
49E3: 5A              LD      E,D                 
49E4: 16 7F           LD      D,$7F               
49E6: 7F              LD      A,A                 
49E7: 5A              LD      E,D                 
49E8: 5A              LD      E,D                 
49E9: 15              DEC     D                   
49EA: 04              INC     B                   
49EB: 18 05           JR      $49F2               ; {}
49ED: 7F              LD      A,A                 
49EE: 19              ADD     HL,DE               
49EF: 04              INC     B                   
49F0: 14              INC     D                   
49F1: 08 7F 15        LD      ($157F),SP          
49F4: 09              ADD     HL,BC               
49F5: 14              INC     D                   
49F6: 05              DEC     B                   
49F7: 5A              LD      E,D                 
49F8: 6C              LD      L,H                 
49F9: 6C              LD      L,H                 
49FA: 6C              LD      L,H                 
49FB: 6C              LD      L,H                 
49FC: 7F              LD      A,A                 
49FD: 7F              LD      A,A                 
49FE: 7F              LD      A,A                 
49FF: 7F              LD      A,A                 
4A00: 7D              LD      A,L                 
4A01: 7D              LD      A,L                 
4A02: 16 5C           LD      D,$5C               
4A04: 6C              LD      L,H                 
4A05: 6D              LD      L,L                 
4A06: 6E              LD      L,(HL)              
4A07: 6F              LD      L,A                 
4A08: 6E              LD      L,(HL)              
4A09: 6F              LD      L,A                 
4A0A: 6E              LD      L,(HL)              
4A0B: 6F              LD      L,A                 
4A0C: F0 F2           LD      A,($F2)             
4A0E: F1              POP     AF                  
4A0F: F3              DI                          
4A10: 0E 01           LD      C,$01               
4A12: 10 11           ;;STOP    $11                 
4A14: 4A              LD      C,D                 
4A15: 4B              LD      C,E                 
4A16: 5A              LD      E,D                 
4A17: 5B              LD      E,E                 
4A18: 0E 0F           LD      C,$0F               
4A1A: 1E 1F           LD      E,$1F               
4A1C: 0A              LD      A,(BC)              
4A1D: 0B              DEC     BC                  
4A1E: 1A              LD      A,(DE)              
4A1F: 1B              DEC     DE                  
4A20: 20 21           JR      NZ,$4A43            ; {}
4A22: 30 31           JR      NC,$4A55            ; {}
4A24: 22              LD      (HLI),A             
4A25: 23              INC     HL                  
4A26: 32              LD      (HLD),A             
4A27: 33              INC     SP                  
4A28: 24              INC     H                   
4A29: 25              DEC     H                   
4A2A: 34              INC     (HL)                
4A2B: 35              DEC     (HL)                
4A2C: 26 27           LD      H,$27               
4A2E: 36 37           LD      (HL),$37            
4A30: 28 21           JR      Z,$4A53             ; {}
4A32: 30 31           JR      NC,$4A65            ; {}
4A34: 22              LD      (HLI),A             
4A35: 29              ADD     HL,HL               
4A36: 32              LD      (HLD),A             
4A37: 33              INC     SP                  
4A38: 4C              LD      C,H                 
4A39: 4A              LD      C,D                 
4A3A: 48              LD      C,B                 
4A3B: 5C              LD      E,H                 
4A3C: 4A              LD      C,D                 
4A3D: 4A              LD      C,D                 
4A3E: 45              LD      B,L                 
4A3F: 45              LD      B,L                 
4A40: 4A              LD      C,D                 
4A41: 4D              LD      C,L                 
4A42: 5D              LD      E,L                 
4A43: 59              LD      E,C                 
4A44: 48              LD      C,B                 
4A45: 51              LD      D,C                 
4A46: 44              LD      B,H                 
4A47: 56              LD      D,(HL)              
4A48: 45              LD      B,L                 
4A49: 45              LD      B,L                 
4A4A: 55              LD      D,L                 
4A4B: 56              LD      D,(HL)              
4A4C: 0C              INC     C                   
4A4D: 0D              DEC     C                   
4A4E: 1C              INC     E                   
4A4F: 1D              DEC     E                   
4A50: 4E              LD      C,(HL)              
4A51: 49              LD      C,C                 
4A52: 45              LD      B,L                 
4A53: 52              LD      D,D                 
4A54: 49              LD      C,C                 
4A55: 4F              LD      C,A                 
4A56: 51              LD      D,C                 
4A57: 45              LD      B,L                 
4A58: 48              LD      C,B                 
4A59: 51              LD      D,C                 
4A5A: 54              LD      D,H                 
4A5B: 56              LD      D,(HL)              
4A5C: 52              LD      D,D                 
4A5D: 59              LD      E,C                 
4A5E: 55              LD      D,L                 
4A5F: 57              LD      D,A                 
4A60: 45              LD      B,L                 
4A61: 2A              LD      A,(HLI)             
4A62: 55              LD      D,L                 
4A63: 3A              LD      A,(HLD)             
4A64: 2B              DEC     HL                  
4A65: 45              LD      B,L                 
4A66: 3B              DEC     SP                  
4A67: 56              LD      D,(HL)              
4A68: 48              LD      C,B                 
4A69: 49              LD      C,C                 
4A6A: 48              LD      C,B                 
4A6B: 49              LD      C,C                 
4A6C: 49              LD      C,C                 
4A6D: 59              LD      E,C                 
4A6E: 49              LD      C,C                 
4A6F: 59              LD      E,C                 
4A70: 44              LD      B,H                 
4A71: 56              LD      D,(HL)              
4A72: 54              LD      D,H                 
4A73: 56              LD      D,(HL)              
4A74: 55              LD      D,L                 
4A75: 56              LD      D,(HL)              
4A76: 55              LD      D,L                 
4A77: 56              LD      D,(HL)              
4A78: 55              LD      D,L                 
4A79: 47              LD      B,A                 
4A7A: 55              LD      D,L                 
4A7B: 57              LD      D,A                 
4A7C: 45              LD      B,L                 
4A7D: 41              LD      B,C                 
4A7E: 43              LD      B,E                 
4A7F: 49              LD      C,C                 
4A80: 42              LD      B,D                 
4A81: 45              LD      B,L                 
4A82: 49              LD      C,C                 
4A83: 40              LD      B,B                 
4A84: 44              LD      B,H                 
4A85: 56              LD      D,(HL)              
4A86: 44              LD      B,H                 
4A87: 56              LD      D,(HL)              
4A88: 55              LD      D,L                 
4A89: 47              LD      B,A                 
4A8A: 55              LD      D,L                 
4A8B: 47              LD      B,A                 
4A8C: 09              ADD     HL,BC               
4A8D: 7C              LD      A,H                 
4A8E: 16 0D           LD      D,$0D               
4A90: 7C              LD      A,H                 
4A91: 7C              LD      A,H                 
4A92: 1D              DEC     E                   
4A93: 1E 7C           LD      E,$7C               
4A95: 19              ADD     HL,DE               
4A96: 1F              RRA                         
4A97: 18 74           JR      $4B0D               ; {}
4A99: 74              LD      (HL),H              
4A9A: 56              LD      D,(HL)              
4A9B: 56              LD      D,(HL)              
4A9C: 6E              LD      L,(HL)              
4A9D: 5A              LD      E,D                 
4A9E: 5A              LD      E,D                 
4A9F: 6F              LD      L,A                 
4AA0: 50              LD      D,B                 
4AA1: 53              LD      D,E                 
4AA2: 46              LD      B,(HL)              
4AA3: 58              LD      E,B                 
4AA4: 43              LD      B,E                 
4AA5: 49              LD      C,C                 
4AA6: 48              LD      C,B                 
4AA7: 49              LD      C,C                 
4AA8: 49              LD      C,C                 
4AA9: 40              LD      B,B                 
4AAA: 49              LD      C,C                 
4AAB: 59              LD      E,C                 
4AAC: 45              LD      B,L                 
4AAD: 2A              LD      A,(HLI)             
4AAE: 55              LD      D,L                 
4AAF: 56              LD      D,(HL)              
4AB0: 2B              DEC     HL                  
4AB1: 45              LD      B,L                 
4AB2: 55              LD      D,L                 
4AB3: 56              LD      D,(HL)              
4AB4: 7F              LD      A,A                 
4AB5: 7F              LD      A,A                 
4AB6: 56              LD      D,(HL)              
4AB7: 56              LD      D,(HL)              
4AB8: 48              LD      C,B                 
4AB9: 49              LD      C,C                 
4ABA: 45              LD      B,L                 
4ABB: 52              LD      D,D                 
4ABC: 49              LD      C,C                 
4ABD: 59              LD      E,C                 
4ABE: 51              LD      D,C                 
4ABF: 45              LD      B,L                 
4AC0: 7C              LD      A,H                 
4AC1: 7C              LD      A,H                 
4AC2: 45              LD      B,L                 
4AC3: 45              LD      B,L                 
4AC4: 52              LD      D,D                 
4AC5: 59              LD      E,C                 
4AC6: 55              LD      D,L                 
4AC7: 47              LD      B,A                 
4AC8: 02              LD      (BC),A              
4AC9: 1E 12           LD      E,$12               
4ACB: 13              INC     DE                  
4ACC: 7D              LD      A,L                 
4ACD: 7D              LD      A,L                 
4ACE: 45              LD      B,L                 
4ACF: 45              LD      B,L                 
4AD0: 0A              LD      A,(BC)              
4AD1: 0B              DEC     BC                  
4AD2: 1A              LD      A,(DE)              
4AD3: 1B              DEC     DE                  
4AD4: 5E              LD      E,(HL)              
4AD5: 5E              LD      E,(HL)              
4AD6: 5F              LD      E,A                 
4AD7: 5F              LD      E,A                 
4AD8: 5B              LD      E,E                 
4AD9: 5B              LD      E,E                 
4ADA: 5B              LD      E,E                 
4ADB: 5B              LD      E,E                 
4ADC: 08 09 18        LD      ($1809),SP          
4ADF: 19              ADD     HL,DE               
4AE0: 06 07           LD      B,$07               
4AE2: 09              ADD     HL,BC               
4AE3: 7C              LD      A,H                 
4AE4: 07              RLCA                        
4AE5: 08 7C 19        LD      ($197C),SP          
4AE8: 09              ADD     HL,BC               
4AE9: 7C              LD      A,H                 
4AEA: 16 17           LD      D,$17               
4AEC: 7C              LD      A,H                 
4AED: 19              ADD     HL,DE               
4AEE: 17              RLA                         
4AEF: 18 7C           JR      $4B6D               ; {}
4AF1: 7C              LD      A,H                 
4AF2: 17              RLA                         
4AF3: 17              RLA                         
4AF4: 07              RLCA                        
4AF5: 07              RLCA                        
4AF6: 7C              LD      A,H                 
4AF7: 7C              LD      A,H                 
4AF8: 2C              INC     L                   
4AF9: 2D              DEC     L                   
4AFA: 3C              INC     A                   
4AFB: 3D              DEC     A                   
4AFC: F4                              
4AFD: F6 F5           OR      $F5                 
4AFF: F7              RST     0X30                
4B00: 7D              LD      A,L                 
4B01: 7D              LD      A,L                 
4B02: 5D              LD      E,L                 
4B03: 17              RLA                         
4B04: 02              LD      (BC),A              
4B05: 03              INC     BC                  
4B06: 12              LD      (DE),A              
4B07: 13              INC     DE                  
4B08: 04              INC     B                   
4B09: 05              DEC     B                   
4B0A: 04              INC     B                   
4B0B: 05              DEC     B                   
4B0C: 04              INC     B                   
4B0D: 05              DEC     B                   
4B0E: 14              INC     D                   
4B0F: 15              DEC     D                   
4B10: 0A              LD      A,(BC)              
4B11: 0B              DEC     BC                  
4B12: 1A              LD      A,(DE)              
4B13: 1B              DEC     DE                  
4B14: 0C              INC     C                   
4B15: 0C              INC     C                   
4B16: 1C              INC     E                   
4B17: 1C              INC     E                   
4B18: 10 7F           ;;STOP    $7F                 
4B1A: 12              LD      (DE),A              
4B1B: 7F              LD      A,A                 
4B1C: 7F              LD      A,A                 
4B1D: 7F              LD      A,A                 
4B1E: 0E 7F           LD      C,$7F               
4B20: 0E 11           LD      C,$11               
4B22: 7F              LD      A,A                 
4B23: 13              INC     DE                  
4B24: 04              INC     B                   
4B25: 05              DEC     B                   
4B26: 14              INC     D                   
4B27: 15              DEC     D                   
4B28: 06 07           LD      B,$07               
4B2A: 16 17           LD      D,$17               
4B2C: 08 09 18        LD      ($1809),SP          
4B2F: 19              ADD     HL,DE               
4B30: 0A              LD      A,(BC)              
4B31: 0B              DEC     BC                  
4B32: 1A              LD      A,(DE)              
4B33: 1B              DEC     DE                  
4B34: 0A              LD      A,(BC)              
4B35: 0A              LD      A,(BC)              
4B36: 0A              LD      A,(BC)              
4B37: 0A              LD      A,(BC)              
4B38: 0A              LD      A,(BC)              
4B39: 0A              LD      A,(BC)              
4B3A: 1A              LD      A,(DE)              
4B3B: 1A              LD      A,(DE)              
4B3C: 0B              DEC     BC                  
4B3D: 0B              DEC     BC                  
4B3E: 1B              DEC     DE                  
4B3F: 1B              DEC     DE                  
4B40: 00              NOP                         
4B41: 01 0E 1E        LD      BC,$1E0E            
4B44: 42              LD      B,D                 
4B45: 41              LD      B,C                 
4B46: 51              LD      D,C                 
4B47: 52              LD      D,D                 
4B48: 38 39           JR      C,$4B83             ; {}
4B4A: 54              LD      D,H                 
4B4B: 57              LD      D,A                 
4B4C: 0A              LD      A,(BC)              
4B4D: 0B              DEC     BC                  
4B4E: 1A              LD      A,(DE)              
4B4F: 1B              DEC     DE                  
4B50: 04              INC     B                   
4B51: 7F              LD      A,A                 
4B52: 04              INC     B                   
4B53: 0E 00           LD      C,$00               
4B55: 01 04 11        LD      BC,$1104            
4B58: 02              LD      (BC),A              
4B59: 03              INC     BC                  
4B5A: 12              LD      (DE),A              
4B5B: 05              DEC     B                   
4B5C: 07              RLCA                        
4B5D: 06 06           LD      B,$06               
4B5F: 07              RLCA                        
4B60: 07              RLCA                        
4B61: 0B              DEC     BC                  
4B62: 06 1B           LD      B,$1B               
4B64: 0E 06           LD      C,$06               
4B66: 1E 07           LD      E,$07               
4B68: 0F              RRCA                        
4B69: 1F              RRA                         
4B6A: 0F              RRCA                        
4B6B: 1F              RRA                         
4B6C: 0D              DEC     C                   
4B6D: 0D              DEC     C                   
4B6E: 1C              INC     E                   
4B6F: 1C              INC     E                   
4B70: 1C              INC     E                   
4B71: 1C              INC     E                   
4B72: 1D              DEC     E                   
4B73: 1D              DEC     E                   
4B74: 0D              DEC     C                   
4B75: 0D              DEC     C                   
4B76: 1D              DEC     E                   
4B77: 1D              DEC     E                   
4B78: 0C              INC     C                   
4B79: 0C              INC     C                   
4B7A: 0C              INC     C                   
4B7B: 0C              INC     C                   
4B7C: 7C              LD      A,H                 
4B7D: 0A              LD      A,(BC)              
4B7E: 0A              LD      A,(BC)              
4B7F: 7F              LD      A,A                 
4B80: 1A              LD      A,(DE)              
4B81: 7C              LD      A,H                 
4B82: 7F              LD      A,A                 
4B83: 1A              LD      A,(DE)              
4B84: 1A              LD      A,(DE)              
4B85: 0A              LD      A,(BC)              
4B86: 7F              LD      A,A                 
4B87: 7F              LD      A,A                 
4B88: 0E 05           LD      C,$05               
4B8A: 7F              LD      A,A                 
4B8B: 05              DEC     B                   
4B8C: 7C              LD      A,H                 
4B8D: 7C              LD      A,H                 
4B8E: 06 5C           LD      B,$5C               
4B90: 7C              LD      A,H                 
4B91: 7C              LD      A,H                 
4B92: 5D              LD      E,L                 
4B93: 07              RLCA                        
4B94: 24              INC     H                   
4B95: 25              DEC     H                   
4B96: 0E 0F           LD      C,$0F               
4B98: 26 27           LD      H,$27               
4B9A: 10 11           ;;STOP    $11                 
4B9C: 12              LD      (DE),A              
4B9D: 7C              LD      A,H                 
4B9E: 00              NOP                         
4B9F: 00              NOP                         
4BA0: 01 01 7C        LD      BC,$7C01            
4BA3: 12              LD      (DE),A              
4BA4: 02              LD      (BC),A              
4BA5: 7C              LD      A,H                 
4BA6: 02              LD      (BC),A              
4BA7: 12              LD      (DE),A              
4BA8: 12              LD      (DE),A              
4BA9: 03              INC     BC                  
4BAA: 7C              LD      A,H                 
4BAB: 03              INC     BC                  
4BAC: 12              LD      (DE),A              
4BAD: 7C              LD      A,H                 
4BAE: 7C              LD      A,H                 
4BAF: 04              INC     B                   
4BB0: 12              LD      (DE),A              
4BB1: 7C              LD      A,H                 
4BB2: 05              DEC     B                   
4BB3: 12              LD      (DE),A              
4BB4: 12              LD      (DE),A              
4BB5: 06 7C           LD      B,$7C               
4BB7: 12              LD      (DE),A              
4BB8: 07              RLCA                        
4BB9: 7C              LD      A,H                 
4BBA: 7C              LD      A,H                 
4BBB: 12              LD      (DE),A              
4BBC: 12              LD      (DE),A              
4BBD: 03              INC     BC                  
4BBE: 00              NOP                         
4BBF: 09              ADD     HL,BC               
4BC0: 02              LD      (BC),A              
4BC1: 7C              LD      A,H                 
4BC2: 08 00 01        LD      ($0100),SP          
4BC5: 0B              DEC     BC                  
4BC6: 7C              LD      A,H                 
4BC7: 03              INC     BC                  
4BC8: 0A              LD      A,(BC)              
4BC9: 01 02 12        LD      BC,$1202            
4BCC: 12              LD      (DE),A              
4BCD: 7C              LD      A,H                 
4BCE: 7C              LD      A,H                 
4BCF: 12              LD      (DE),A              
4BD0: 00              NOP                         
4BD1: 6C              LD      L,H                 
4BD2: 10 6D           ;;STOP    $6D                 
4BD4: 12              LD      (DE),A              
4BD5: 7C              LD      A,H                 
4BD6: 13              INC     DE                  
4BD7: 14              INC     D                   
4BD8: 0B              DEC     BC                  
4BD9: 0B              DEC     BC                  
4BDA: 1B              DEC     DE                  
4BDB: 1B              DEC     DE                  
4BDC: 00              NOP                         
4BDD: 0B              DEC     BC                  
4BDE: 10 1B           ;;STOP    $1B                 
4BE0: 0B              DEC     BC                  
4BE1: 01 1B 11        LD      BC,$111B            
4BE4: 0B              DEC     BC                  
4BE5: 0B              DEC     BC                  
4BE6: 0B              DEC     BC                  
4BE7: 0B              DEC     BC                  
4BE8: 00              NOP                         
4BE9: 0B              DEC     BC                  
4BEA: 00              NOP                         
4BEB: 0B              DEC     BC                  
4BEC: 0B              DEC     BC                  
4BED: 01 0B 01        LD      BC,$010B            
4BF0: 09              ADD     HL,BC               
4BF1: 09              ADD     HL,BC               
4BF2: 19              ADD     HL,DE               
4BF3: 19              ADD     HL,DE               
4BF4: 08 18 08        LD      ($0818),SP          
4BF7: 18 02           JR      $4BFB               ; {}
4BF9: 09              ADD     HL,BC               
4BFA: 08 04 09        LD      ($0904),SP          
4BFD: 03              INC     BC                  
4BFE: 05              DEC     B                   
4BFF: 18 08           JR      $4C09               ; {}
4C01: 14              INC     D                   
4C02: 12              LD      (DE),A              
4C03: 19              ADD     HL,DE               
4C04: 15              DEC     D                   
4C05: 18 19           JR      $4C20               ; {}
4C07: 13              INC     DE                  
4C08: 02              LD      (BC),A              
4C09: 03              INC     BC                  
4C0A: 08 18 60        LD      ($6018),SP          ; {}
4C0D: 61              LD      H,C                 
4C0E: 70              LD      (HL),B              
4C0F: 71              LD      (HL),C              
4C10: 62              LD      H,D                 
4C11: 63              LD      H,E                 
4C12: 70              LD      (HL),B              
4C13: 71              LD      (HL),C              
4C14: 00              NOP                         
4C15: 01 00 01        LD      BC,$0100            
4C18: 08 18 12        LD      ($1218),SP          
4C1B: 13              INC     DE                  
4C1C: 0B              DEC     BC                  
4C1D: 0B              DEC     BC                  
4C1E: 0B              DEC     BC                  
4C1F: 1E 0B           LD      E,$0B               
4C21: 0B              DEC     BC                  
4C22: 1E 1E           LD      E,$1E               
4C24: 0B              DEC     BC                  
4C25: 0B              DEC     BC                  
4C26: 1E 0B           LD      E,$0B               
4C28: 0B              DEC     BC                  
4C29: 1E 1B           LD      E,$1B               
4C2B: 1E 1E           LD      E,$1E               
4C2D: 0B              DEC     BC                  
4C2E: 1E 1B           LD      E,$1B               
4C30: 14              INC     D                   
4C31: 7F              LD      A,A                 
4C32: 0B              DEC     BC                  
4C33: 1B              DEC     DE                  
4C34: 7F              LD      A,A                 
4C35: 0E 1E           LD      C,$1E               
4C37: 1E 0A           LD      E,$0A               
4C39: 0A              LD      A,(BC)              
4C3A: 1A              LD      A,(DE)              
4C3B: 1A              LD      A,(DE)              
4C3C: 1A              LD      A,(DE)              
4C3D: 1A              LD      A,(DE)              
4C3E: 1A              LD      A,(DE)              
4C3F: 1A              LD      A,(DE)              
4C40: 1E 1E           LD      E,$1E               
4C42: 09              ADD     HL,BC               
4C43: 08 09 04        LD      ($0409),SP          
4C46: 19              ADD     HL,DE               
4C47: 14              INC     D                   
4C48: 1E 1E           LD      E,$1E               
4C4A: 18 08           JR      $4C54               ; {}
4C4C: 05              DEC     B                   
4C4D: 04              INC     B                   
4C4E: 15              DEC     D                   
4C4F: 14              INC     D                   
4C50: 1E 1E           LD      E,$1E               
4C52: 18 09           JR      $4C5D               ; {}
4C54: 05              DEC     B                   
4C55: 09              ADD     HL,BC               
4C56: 15              DEC     D                   
4C57: 19              ADD     HL,DE               
4C58: 0E 0F           LD      C,$0F               
4C5A: 0F              RRCA                        
4C5B: 0E 1E           LD      C,$1E               
4C5D: 1E 09           LD      E,$09               
4C5F: 09              ADD     HL,BC               
4C60: 09              ADD     HL,BC               
4C61: 09              ADD     HL,BC               
4C62: 19              ADD     HL,DE               
4C63: 19              ADD     HL,DE               
4C64: 00              NOP                         
4C65: 01 10 11        LD      BC,$1110            
4C68: 02              LD      (BC),A              
4C69: 03              INC     BC                  
4C6A: 12              LD      (DE),A              
4C6B: 13              INC     DE                  
4C6C: 06 07           LD      B,$07               
4C6E: 16 17           LD      D,$17               
4C70: 0C              INC     C                   
4C71: 0D              DEC     C                   
4C72: 1C              INC     E                   
4C73: 1D              DEC     E                   
4C74: FC                              
4C75: FD                              
4C76: FE FF           CP      $FF                 
4C78: 04              INC     B                   
4C79: 05              DEC     B                   
4C7A: 14              INC     D                   
4C7B: 15              DEC     D                   
4C7C: 06 07           LD      B,$07               
4C7E: 16 17           LD      D,$17               
4C80: 08 09 18        LD      ($1809),SP          
4C83: 19              ADD     HL,DE               
4C84: 0A              LD      A,(BC)              
4C85: 0B              DEC     BC                  
4C86: 1A              LD      A,(DE)              
4C87: 1B              DEC     DE                  
4C88: 7F              LD      A,A                 
4C89: 15              DEC     D                   
4C8A: 1C              INC     E                   
4C8B: 0C              INC     C                   
4C8C: 02              LD      (BC),A              
4C8D: 03              INC     BC                  
4C8E: 0D              DEC     C                   
4C8F: 1D              DEC     E                   
4C90: 7F              LD      A,A                 
4C91: 7F              LD      A,A                 
4C92: 0F              RRCA                        
4C93: 0F              RRCA                        
4C94: 0C              INC     C                   
4C95: 0C              INC     C                   
4C96: 1C              INC     E                   
4C97: 1C              INC     E                   
4C98: 02              LD      (BC),A              
4C99: 01 12 11        LD      BC,$1112            
4C9C: 0E 0F           LD      C,$0F               
4C9E: 1E 1F           LD      E,$1F               
4CA0: 0E 0F           LD      C,$0F               
4CA2: 1E 1F           LD      E,$1F               
4CA4: 68              LD      L,B                 
4CA5: 69              LD      L,C                 
4CA6: 77              LD      (HL),A              
4CA7: 4B              LD      C,E                 
4CA8: 0F              RRCA                        
4CA9: 01 10 11        LD      BC,$1110            
4CAC: 08 09 18        LD      ($1809),SP          
4CAF: 19              ADD     HL,DE               
4CB0: 02              LD      (BC),A              
4CB1: 1F              RRA                         
4CB2: 12              LD      (DE),A              
4CB3: 13              INC     DE                  
4CB4: 0E 1E           LD      C,$1E               
4CB6: 1E 0E           LD      E,$0E               
4CB8: 7E              LD      A,(HL)              
4CB9: 7E              LD      A,(HL)              
4CBA: 1F              RRA                         
4CBB: 1F              RRA                         
4CBC: 6A              LD      L,D                 
4CBD: 6B              LD      L,E                 
4CBE: 7A              LD      A,D                 
4CBF: 7B              LD      A,E                 
4CC0: 04              INC     B                   
4CC1: 05              DEC     B                   
4CC2: 14              INC     D                   
4CC3: 15              DEC     D                   
4CC4: 06 07           LD      B,$07               
4CC6: 16 17           LD      D,$17               
4CC8: 6C              LD      L,H                 
4CC9: 6C              LD      L,H                 
4CCA: 6C              LD      L,H                 
4CCB: 6C              LD      L,H                 
4CCC: 6D              LD      L,L                 
4CCD: 6D              LD      L,L                 
4CCE: 6D              LD      L,L                 
4CCF: 6D              LD      L,L                 
4CD0: 6E              LD      L,(HL)              
4CD1: 6E              LD      L,(HL)              
4CD2: 6E              LD      L,(HL)              
4CD3: 6E              LD      L,(HL)              
4CD4: 6F              LD      L,A                 
4CD5: 6F              LD      L,A                 
4CD6: 6F              LD      L,A                 
4CD7: 6F              LD      L,A                 
4CD8: F4                              
4CD9: F6 F5           OR      $F5                 
4CDB: F7              RST     0X30                
4CDC: F8 FA           LD      HL,SP+$FA           
4CDE: F9              LD      SP,HL               
4CDF: FB              EI                          
4CE0: 0A              LD      A,(BC)              
4CE1: 0B              DEC     BC                  
4CE2: 1A              LD      A,(DE)              
4CE3: 1B              DEC     DE                  
4CE4: 0C              INC     C                   
4CE5: 0D              DEC     C                   
4CE6: 1C              INC     E                   
4CE7: 1D              DEC     E                   
4CE8: 0E 0F           LD      C,$0F               
4CEA: 1E 1F           LD      E,$1F               
4CEC: 45              LD      B,L                 
4CED: 45              LD      B,L                 
4CEE: 55              LD      D,L                 
4CEF: 56              LD      D,(HL)              
4CF0: 6D              LD      L,L                 
4CF1: 6D              LD      L,L                 
4CF2: 6D              LD      L,L                 
4CF3: 6D              LD      L,L                 
4CF4: 4A              LD      C,D                 
4CF5: 4A              LD      C,D                 
4CF6: 45              LD      B,L                 
4CF7: 45              LD      B,L                 
4CF8: 0C              INC     C                   
4CF9: 0D              DEC     C                   
4CFA: 1C              INC     E                   
4CFB: 1D              DEC     E                   
4CFC: 6E              LD      L,(HL)              
4CFD: 5A              LD      E,D                 
4CFE: 5A              LD      E,D                 
4CFF: 6F              LD      L,A                 
4D00: 49              LD      C,C                 
4D01: 40              LD      B,B                 
4D02: 49              LD      C,C                 
4D03: 59              LD      E,C                 
4D04: 43              LD      B,E                 
4D05: 49              LD      C,C                 
4D06: 48              LD      C,B                 
4D07: 49              LD      C,C                 
4D08: 00              NOP                         
4D09: 00              NOP                         
4D0A: 00              NOP                         
4D0B: 00              NOP                         
4D0C: 5B              LD      E,E                 
4D0D: 5B              LD      E,E                 
4D0E: 5B              LD      E,E                 
4D0F: 5B              LD      E,E                 
4D10: 64              LD      H,H                 
4D11: 65              LD      H,L                 
4D12: 66              LD      H,(HL)              
4D13: 67              LD      H,A                 
4D14: 2E 2F           LD      L,$2F               
4D16: 3E 3F           LD      A,$3F               
4D18: 7E              LD      A,(HL)              
4D19: 7E              LD      A,(HL)              
4D1A: 1F              RRA                         
4D1B: 1F              RRA                         
4D1C: 15              DEC     D                   
4D1D: 16 17           LD      D,$17               
4D1F: 18 7D           JR      $4D9E               ; {}
4D21: 7D              LD      A,L                 
4D22: 7D              LD      A,L                 
4D23: 7D              LD      A,L                 
4D24: 74              LD      (HL),H              
4D25: 0C              INC     C                   
4D26: 74              LD      (HL),H              
4D27: 1C              INC     E                   
4D28: 1E 1E           LD      E,$1E               
4D2A: 7E              LD      A,(HL)              
4D2B: 7E              LD      A,(HL)              
4D2C: 68              LD      L,B                 
4D2D: 69              LD      L,C                 
4D2E: 78              LD      A,B                 
4D2F: 79              LD      A,C                 
4D30: 6E              LD      L,(HL)              
4D31: 6E              LD      L,(HL)              
4D32: 6E              LD      L,(HL)              
4D33: 6E              LD      L,(HL)              
4D34: 48              LD      C,B                 
4D35: 49              LD      C,C                 
4D36: 48              LD      C,B                 
4D37: 5F              LD      E,A                 
4D38: 6C              LD      L,H                 
4D39: 6C              LD      L,H                 
4D3A: 6C              LD      L,H                 
4D3B: 6C              LD      L,H                 
4D3C: 6D              LD      L,L                 
4D3D: 6D              LD      L,L                 
4D3E: 6D              LD      L,L                 
4D3F: 6D              LD      L,L                 
4D40: 6F              LD      L,A                 
4D41: 6F              LD      L,A                 
4D42: 6F              LD      L,A                 
4D43: 6F              LD      L,A                 
4D44: 6E              LD      L,(HL)              
4D45: 6E              LD      L,(HL)              
4D46: 6E              LD      L,(HL)              
4D47: 6E              LD      L,(HL)              
4D48: 6F              LD      L,A                 
4D49: 6F              LD      L,A                 
4D4A: 7D              LD      A,L                 
4D4B: 7D              LD      A,L                 
4D4C: 48              LD      C,B                 
4D4D: 7F              LD      A,A                 
4D4E: 48              LD      C,B                 
4D4F: 7F              LD      A,A                 
4D50: 48              LD      C,B                 
4D51: 5E              LD      E,(HL)              
4D52: 48              LD      C,B                 
4D53: 49              LD      C,C                 
4D54: 49              LD      C,C                 
4D55: 59              LD      E,C                 
4D56: 5F              LD      E,A                 
4D57: 59              LD      E,C                 
4D58: 7F              LD      A,A                 
4D59: 59              LD      E,C                 
4D5A: 7F              LD      A,A                 
4D5B: 59              LD      E,C                 
4D5C: 5E              LD      E,(HL)              
4D5D: 59              LD      E,C                 
4D5E: 49              LD      C,C                 
4D5F: 59              LD      E,C                 
4D60: 7F              LD      A,A                 
4D61: 7F              LD      A,A                 
4D62: 7F              LD      A,A                 
4D63: 7F              LD      A,A                 
4D64: 7E              LD      A,(HL)              
4D65: 7E              LD      A,(HL)              
4D66: 7E              LD      A,(HL)              
4D67: 7E              LD      A,(HL)              
4D68: 7D              LD      A,L                 
4D69: 7D              LD      A,L                 
4D6A: 7D              LD      A,L                 
4D6B: 7D              LD      A,L                 
4D6C: 7C              LD      A,H                 
4D6D: 7C              LD      A,H                 
4D6E: 7C              LD      A,H                 
4D6F: 7C              LD      A,H                 
4D70: 7E              LD      A,(HL)              
4D71: 7E              LD      A,(HL)              
4D72: 7E              LD      A,(HL)              
4D73: 7E              LD      A,(HL)              
4D74: 5A              LD      E,D                 
4D75: 5A              LD      E,D                 
4D76: 5A              LD      E,D                 
4D77: 5A              LD      E,D                 
4D78: 6E              LD      L,(HL)              
4D79: 6F              LD      L,A                 
4D7A: 6F              LD      L,A                 
4D7B: 6E              LD      L,(HL)              
4D7C: 7C              LD      A,H                 
4D7D: 7D              LD      A,L                 
4D7E: 7D              LD      A,L                 
4D7F: 7C              LD      A,H                 
4D80: 10 29           ;;STOP    $29                 
4D82: 12              LD      (DE),A              
4D83: 39              ADD     HL,SP               
4D84: 2A              LD      A,(HLI)             
4D85: 2B              DEC     HL                  
4D86: 12              LD      (DE),A              
4D87: 13              INC     DE                  
4D88: 10 11           ;;STOP    $11                 
4D8A: 2A              LD      A,(HLI)             
4D8B: 2B              DEC     HL                  
4D8C: 3A              LD      A,(HLD)             
4D8D: 3B              DEC     SP                  
4D8E: 12              LD      (DE),A              
4D8F: 13              INC     DE                  
4D90: 10 11           ;;STOP    $11                 
4D92: 3A              LD      A,(HLD)             
4D93: 3B              DEC     SP                  
4D94: 10 11           ;;STOP    $11                 
4D96: 12              LD      (DE),A              
4D97: 13              INC     DE                  
4D98: 6D              LD      L,L                 
4D99: 6D              LD      L,L                 
4D9A: 6D              LD      L,L                 
4D9B: 6D              LD      L,L                 
4D9C: 18 19           JR      $4DB7               ; {}
4D9E: 1A              LD      A,(DE)              
4D9F: 1B              DEC     DE                  
4DA0: 10 68           ;;STOP    $68                 
4DA2: 12              LD      (DE),A              
4DA3: 68              LD      L,B                 
4DA4: 68              LD      L,B                 
4DA5: 11 68 13        LD      DE,$1368            
4DA8: 68              LD      L,B                 
4DA9: 68              LD      L,B                 
4DAA: 12              LD      (DE),A              
4DAB: 13              INC     DE                  
4DAC: 10 11           ;;STOP    $11                 
4DAE: 68              LD      L,B                 
4DAF: 68              LD      L,B                 
4DB0: 10 68           ;;STOP    $68                 
4DB2: 68              LD      L,B                 
4DB3: 68              LD      L,B                 
4DB4: 68              LD      L,B                 
4DB5: 11 68 68        LD      DE,$6868            
4DB8: 68              LD      L,B                 
4DB9: 68              LD      L,B                 
4DBA: 12              LD      (DE),A              
4DBB: 68              LD      L,B                 
4DBC: 68              LD      L,B                 
4DBD: 68              LD      L,B                 
4DBE: 68              LD      L,B                 
4DBF: 13              INC     DE                  
4DC0: 1C              INC     E                   
4DC1: 1D              DEC     E                   
4DC2: 1E 1F           LD      E,$1F               
4DC4: 10 68           ;;STOP    $68                 
4DC6: 68              LD      L,B                 
4DC7: 13              INC     DE                  
4DC8: 68              LD      L,B                 
4DC9: 11 12 68        LD      DE,$6812            
4DCC: 6C              LD      L,H                 
4DCD: 6C              LD      L,H                 
4DCE: 6C              LD      L,H                 
4DCF: 6C              LD      L,H                 
4DD0: 48              LD      C,B                 
4DD1: 48              LD      C,B                 
4DD2: 48              LD      C,B                 
4DD3: 48              LD      C,B                 
4DD4: 76              HALT                        
4DD5: 76              HALT                        
4DD6: 49              LD      C,C                 
4DD7: 49              LD      C,C                 
4DD8: 76              HALT                        
4DD9: 76              HALT                        
4DDA: 48              LD      C,B                 
4DDB: 48              LD      C,B                 
4DDC: 48              LD      C,B                 
4DDD: 48              LD      C,B                 
4DDE: 49              LD      C,C                 
4DDF: 49              LD      C,C                 
4DE0: F0 F2           LD      A,($F2)             
4DE2: F1              POP     AF                  
4DE3: F3              DI                          
4DE4: 28 28           JR      Z,$4E0E             ; {}
4DE6: 38 38           JR      C,$4E20             ; {}
4DE8: 29              ADD     HL,HL               
4DE9: 29              ADD     HL,HL               
4DEA: 39              ADD     HL,SP               
4DEB: 39              ADD     HL,SP               
4DEC: 2A              LD      A,(HLI)             
4DED: 2B              DEC     HL                  
4DEE: 2A              LD      A,(HLI)             
4DEF: 2B              DEC     HL                  
4DF0: 3A              LD      A,(HLD)             
4DF1: 3B              DEC     SP                  
4DF2: 3A              LD      A,(HLD)             
4DF3: 3B              DEC     SP                  
4DF4: 20 28           JR      NZ,$4E1E            ; {}
4DF6: 2A              LD      A,(HLI)             
4DF7: 30 28           JR      NC,$4E21            ; {}
4DF9: 21 31 3B        LD      HL,$3B31            
4DFC: 2A              LD      A,(HLI)             
4DFD: 32              LD      (HLD),A             
4DFE: 22              LD      (HLI),A             
4DFF: 39              ADD     HL,SP               
4E00: 33              INC     SP                  
4E01: 3B              DEC     SP                  
4E02: 39              ADD     HL,SP               
4E03: 23              INC     HL                  
4E04: 24              INC     H                   
4E05: 2B              DEC     HL                  
4E06: 38 34           JR      C,$4E3C             ; {}
4E08: 3A              LD      A,(HLD)             
4E09: 25              DEC     H                   
4E0A: 35              DEC     (HL)                
4E0B: 38 29           JR      C,$4E36             ; {}
4E0D: 36 26           LD      (HL),$26            
4E0F: 2B              DEC     HL                  
4E10: 37              SCF                         
4E11: 29              ADD     HL,HL               
4E12: 3A              LD      A,(HLD)             
4E13: 27              DAA                         
4E14: 28 40           JR      Z,$4E56             ; {}
4E16: 38 50           JR      C,$4E68             ; {}
4E18: 41              LD      B,C                 
4E19: 28 51           JR      Z,$4E6C             ; {}
4E1B: 38 29           JR      C,$4E46             ; {}
4E1D: 42              LD      B,D                 
4E1E: 39              ADD     HL,SP               
4E1F: 52              LD      D,D                 
4E20: 43              LD      B,E                 
4E21: 29              ADD     HL,HL               
4E22: 53              LD      D,E                 
4E23: 39              ADD     HL,SP               
4E24: 2A              LD      A,(HLI)             
4E25: 2B              DEC     HL                  
4E26: 44              LD      B,H                 
4E27: 45              LD      B,L                 
4E28: 54              LD      D,H                 
4E29: 55              LD      D,L                 
4E2A: 2A              LD      A,(HLI)             
4E2B: 2B              DEC     HL                  
4E2C: 3A              LD      A,(HLD)             
4E2D: 3B              DEC     SP                  
4E2E: 46              LD      B,(HL)              
4E2F: 47              LD      B,A                 
4E30: 56              LD      D,(HL)              
4E31: 57              LD      D,A                 
4E32: 3A              LD      A,(HLD)             
4E33: 3B              DEC     SP                  
4E34: 28 40           JR      Z,$4E76             ; {}
4E36: 38 58           JR      C,$4E90             ; {}
4E38: 41              LD      B,C                 
4E39: 28 59           JR      Z,$4E94             ; {}
4E3B: 38 29           JR      C,$4E66             ; {}
4E3D: 4A              LD      C,D                 
4E3E: 39              ADD     HL,SP               
4E3F: 52              LD      D,D                 
4E40: 4B              LD      C,E                 
4E41: 29              ADD     HL,HL               
4E42: 53              LD      D,E                 
4E43: 39              ADD     HL,SP               
4E44: 2A              LD      A,(HLI)             
4E45: 2B              DEC     HL                  
4E46: 44              LD      B,H                 
4E47: 4D              LD      C,L                 
4E48: 54              LD      D,H                 
4E49: 5D              LD      E,L                 
4E4A: 2A              LD      A,(HLI)             
4E4B: 2B              DEC     HL                  
4E4C: 3A              LD      A,(HLD)             
4E4D: 3B              DEC     SP                  
4E4E: 4E              LD      C,(HL)              
4E4F: 47              LD      B,A                 
4E50: 5E              LD      E,(HL)              
4E51: 57              LD      D,A                 
4E52: 3A              LD      A,(HLD)             
4E53: 3B              DEC     SP                  
4E54: 72              LD      (HL),D              
4E55: 73              LD      (HL),E              
4E56: 72              LD      (HL),D              
4E57: 73              LD      (HL),E              
4E58: 69              LD      L,C                 
4E59: 69              LD      L,C                 
4E5A: 79              LD      A,C                 
4E5B: 79              LD      A,C                 
4E5C: 2C              INC     L                   
4E5D: 2C              INC     L                   
4E5E: 3C              INC     A                   
4E5F: 3C              INC     A                   
4E60: 2D              DEC     L                   
4E61: 2D              DEC     L                   
4E62: 3D              DEC     A                   
4E63: 3D              DEC     A                   
4E64: 2E 2F           LD      L,$2F               
4E66: 2E 2F           LD      L,$2F               
4E68: 3E 3F           LD      A,$3F               
4E6A: 3E 3F           LD      A,$3F               
4E6C: 28 11           JR      Z,$4E7F             ; {}
4E6E: 38 13           JR      C,$4E83             ; {}
4E70: 10 28           ;;STOP    $28                 
4E72: 12              LD      (DE),A              
4E73: 38 29           JR      C,$4E9E             ; {}
4E75: 66              LD      H,(HL)              
4E76: 39              ADD     HL,SP               
4E77: 52              LD      D,D                 
4E78: 67              LD      H,A                 
4E79: 29              ADD     HL,HL               
4E7A: 53              LD      D,E                 
4E7B: 39              ADD     HL,SP               
4E7C: 28 28           JR      Z,$4EA6             ; {}
4E7E: 38 38           JR      C,$4EB8             ; {}
4E80: 29              ADD     HL,HL               
4E81: 29              ADD     HL,HL               
4E82: 39              ADD     HL,SP               
4E83: 39              ADD     HL,SP               
4E84: 2A              LD      A,(HLI)             
4E85: 2B              DEC     HL                  
4E86: 2A              LD      A,(HLI)             
4E87: 2B              DEC     HL                  
4E88: 3A              LD      A,(HLD)             
4E89: 3B              DEC     SP                  
4E8A: 3A              LD      A,(HLD)             
4E8B: 3B              DEC     SP                  
4E8C: 08 09 18        LD      ($1809),SP          
4E8F: 19              ADD     HL,DE               
4E90: 7E              LD      A,(HL)              
4E91: 7E              LD      A,(HL)              
4E92: 72              LD      (HL),D              
4E93: 73              LD      (HL),E              
4E94: 44              LD      B,H                 
4E95: 45              LD      B,L                 
4E96: 54              LD      D,H                 
4E97: 55              LD      D,L                 
4E98: 0C              INC     C                   
4E99: 0D              DEC     C                   
4E9A: 0E 0F           LD      C,$0F               
4E9C: 00              NOP                         
4E9D: 01 02 03        LD      BC,$0302            
4EA0: 04              INC     B                   
4EA1: 05              DEC     B                   
4EA2: 12              LD      (DE),A              
4EA3: 11 02 01        LD      DE,$0102            
4EA6: 12              LD      (DE),A              
4EA7: 11 02 01        LD      DE,$0102            
4EAA: 14              INC     D                   
4EAB: 15              DEC     D                   
4EAC: 04              INC     B                   
4EAD: 05              DEC     B                   
4EAE: 10 11           ;;STOP    $11                 
4EB0: 00              NOP                         
4EB1: 01 10 11        LD      BC,$1110            
4EB4: 00              NOP                         
4EB5: 01 14 15        LD      BC,$1514            
4EB8: 04              INC     B                   
4EB9: 05              DEC     B                   
4EBA: 10 13           ;;STOP    $13                 
4EBC: 00              NOP                         
4EBD: 03              INC     BC                  
4EBE: 10 13           ;;STOP    $13                 
4EC0: 00              NOP                         
4EC1: 03              INC     BC                  
4EC2: 14              INC     D                   
4EC3: 15              DEC     D                   
4EC4: 06 07           LD      B,$07               
4EC6: 12              LD      (DE),A              
4EC7: 11 02 01        LD      DE,$0102            
4ECA: 16 17           LD      D,$17               
4ECC: 06 07           LD      B,$07               
4ECE: 10 11           ;;STOP    $11                 
4ED0: 00              NOP                         
4ED1: 01 16 17        LD      BC,$1716            
4ED4: 06 07           LD      B,$07               
4ED6: 10 13           ;;STOP    $13                 
4ED8: 00              NOP                         
4ED9: 03              INC     BC                  
4EDA: 16 17           LD      D,$17               
4EDC: 64              LD      H,H                 
4EDD: 65              LD      H,L                 
4EDE: 74              LD      (HL),H              
4EDF: 75              LD      (HL),L              
4EE0: 66              LD      H,(HL)              
4EE1: 67              LD      H,A                 
4EE2: 76              HALT                        
4EE3: 77              LD      (HL),A              
4EE4: 68              LD      L,B                 
4EE5: 69              LD      L,C                 
4EE6: 78              LD      A,B                 
4EE7: 79              LD      A,C                 
4EE8: 0A              LD      A,(BC)              
4EE9: 0B              DEC     BC                  
4EEA: 0A              LD      A,(BC)              
4EEB: 0B              DEC     BC                  
4EEC: 0A              LD      A,(BC)              
4EED: 0B              DEC     BC                  
4EEE: 0A              LD      A,(BC)              
4EEF: 0B              DEC     BC                  
4EF0: 1A              LD      A,(DE)              
4EF1: 1B              DEC     DE                  
4EF2: 1A              LD      A,(DE)              
4EF3: 1B              DEC     DE                  
4EF4: 1A              LD      A,(DE)              
4EF5: 1B              DEC     DE                  
4EF6: 1A              LD      A,(DE)              
4EF7: 1B              DEC     DE                  
4EF8: 1C              INC     E                   
4EF9: 1D              DEC     E                   
4EFA: 1C              INC     E                   
4EFB: 1D              DEC     E                   
4EFC: 1C              INC     E                   
4EFD: 1D              DEC     E                   
4EFE: 1C              INC     E                   
4EFF: 1D              DEC     E                   
4F00: 0E 0F           LD      C,$0F               
4F02: 1E 1F           LD      E,$1F               
4F04: 08 09 18        LD      ($1809),SP          
4F07: 19              ADD     HL,DE               
4F08: 7E              LD      A,(HL)              
4F09: 7E              LD      A,(HL)              
4F0A: 1E 1F           LD      E,$1F               
4F0C: 7E              LD      A,(HL)              
4F0D: 7E              LD      A,(HL)              
4F0E: 18 19           JR      $4F29               ; {}
4F10: 20 21           JR      NZ,$4F33            ; {}
4F12: 30 31           JR      NC,$4F45            ; {}
4F14: 22              LD      (HLI),A             
4F15: 23              INC     HL                  
4F16: 32              LD      (HLD),A             
4F17: 33              INC     SP                  
4F18: 7E              LD      A,(HL)              
4F19: 7E              LD      A,(HL)              
4F1A: 30 31           JR      NC,$4F4D            ; {}
4F1C: 7E              LD      A,(HL)              
4F1D: 7E              LD      A,(HL)              
4F1E: 32              LD      (HLD),A             
4F1F: 33              INC     SP                  
4F20: 24              INC     H                   
4F21: 25              DEC     H                   
4F22: 34              INC     (HL)                
4F23: 35              DEC     (HL)                
4F24: 26 27           LD      H,$27               
4F26: 36 37           LD      (HL),$37            
4F28: 28 29           JR      Z,$4F53             ; {}
4F2A: 38 39           JR      C,$4F65             ; {}
4F2C: 7E              LD      A,(HL)              
4F2D: 7E              LD      A,(HL)              
4F2E: 38 7E           JR      C,$4FAE             ; {}
4F30: 7E              LD      A,(HL)              
4F31: 7E              LD      A,(HL)              
4F32: 7E              LD      A,(HL)              
4F33: 39              ADD     HL,SP               
4F34: 2A              LD      A,(HLI)             
4F35: 2B              DEC     HL                  
4F36: 3A              LD      A,(HLD)             
4F37: 3B              DEC     SP                  
4F38: 2C              INC     L                   
4F39: 2D              DEC     L                   
4F3A: 3C              INC     A                   
4F3B: 3D              DEC     A                   
4F3C: 2E 2F           LD      L,$2F               
4F3E: 3E 3F           LD      A,$3F               
4F40: 40              LD      B,B                 
4F41: 41              LD      B,C                 
4F42: 50              LD      D,B                 
4F43: 51              LD      D,C                 
4F44: 42              LD      B,D                 
4F45: 43              LD      B,E                 
4F46: 52              LD      D,D                 
4F47: 53              LD      D,E                 
4F48: 00              NOP                         
4F49: 00              NOP                         
4F4A: 00              NOP                         
4F4B: 00              NOP                         
4F4C: 46              LD      B,(HL)              
4F4D: 47              LD      B,A                 
4F4E: 56              LD      D,(HL)              
4F4F: 57              LD      D,A                 
4F50: 48              LD      C,B                 
4F51: 49              LD      C,C                 
4F52: 58              LD      E,B                 
4F53: 59              LD      E,C                 
4F54: 4A              LD      C,D                 
4F55: 4B              LD      C,E                 
4F56: 5A              LD      E,D                 
4F57: 5B              LD      E,E                 
4F58: 4E              LD      C,(HL)              
4F59: 4F              LD      C,A                 
4F5A: 5E              LD      E,(HL)              
4F5B: 5F              LD      E,A                 
4F5C: 60              LD      H,B                 
4F5D: 61              LD      H,C                 
4F5E: 70              LD      (HL),B              
4F5F: 71              LD      (HL),C              
4F60: 6C              LD      L,H                 
4F61: 6C              LD      L,H                 
4F62: 7D              LD      A,L                 
4F63: 7D              LD      A,L                 
4F64: 7D              LD      A,L                 
4F65: 7D              LD      A,L                 
4F66: 7D              LD      A,L                 
4F67: 7D              LD      A,L                 
4F68: 6D              LD      L,L                 
4F69: 6E              LD      L,(HL)              
4F6A: 0C              INC     C                   
4F6B: 0D              DEC     C                   
4F6C: 6F              LD      L,A                 
4F6D: 6F              LD      L,A                 
4F6E: 7E              LD      A,(HL)              
4F6F: 7E              LD      A,(HL)              
4F70: 7E              LD      A,(HL)              
4F71: 7E              LD      A,(HL)              
4F72: 7E              LD      A,(HL)              
4F73: 7E              LD      A,(HL)              
4F74: 6C              LD      L,H                 
4F75: 6D              LD      L,L                 
4F76: 6E              LD      L,(HL)              
4F77: 6F              LD      L,A                 
4F78: 00              NOP                         
4F79: 01 02 03        LD      BC,$0302            
4F7C: 04              INC     B                   
4F7D: 05              DEC     B                   
4F7E: 06 07           LD      B,$07               
4F80: 04              INC     B                   
4F81: 05              DEC     B                   
4F82: 06 07           LD      B,$07               
4F84: 6C              LD      L,H                 
4F85: 6D              LD      L,L                 
4F86: 6E              LD      L,(HL)              
4F87: 6F              LD      L,A                 
4F88: 6C              LD      L,H                 
4F89: 6D              LD      L,L                 
4F8A: 6E              LD      L,(HL)              
4F8B: 6F              LD      L,A                 
4F8C: 18 19           JR      $4FA7               ; {}
4F8E: 1A              LD      A,(DE)              
4F8F: 1B              DEC     DE                  
4F90: 29              ADD     HL,HL               
4F91: 11 39 13        LD      DE,$1339            
4F94: 08 09 0A        LD      ($0A09),SP          
4F97: 0B              DEC     BC                  
4F98: F0 F2           LD      A,($F2)             
4F9A: F1              POP     AF                  
4F9B: F3              DI                          
4F9C: 4C              LD      C,H                 
4F9D: 4D              LD      C,L                 
4F9E: 5C              LD      E,H                 
4F9F: 5D              LD      E,L                 
4FA0: 04              INC     B                   
4FA1: 05              DEC     B                   
4FA2: 06 07           LD      B,$07               
4FA4: 08 09 0A        LD      ($0A09),SP          
4FA7: 0B              DEC     BC                  
4FA8: 68              LD      L,B                 
4FA9: 68              LD      L,B                 
4FAA: 68              LD      L,B                 
4FAB: 68              LD      L,B                 
4FAC: 68              LD      L,B                 
4FAD: 11 12 13        LD      DE,$1312            
4FB0: 10 68           ;;STOP    $68                 
4FB2: 12              LD      (DE),A              
4FB3: 13              INC     DE                  
4FB4: 10 11           ;;STOP    $11                 
4FB6: 68              LD      L,B                 
4FB7: 13              INC     DE                  
4FB8: 10 11           ;;STOP    $11                 
4FBA: 12              LD      (DE),A              
4FBB: 68              LD      L,B                 
4FBC: 78              LD      A,B                 
4FBD: 78              LD      A,B                 
4FBE: 78              LD      A,B                 
4FBF: 78              LD      A,B                 
4FC0: 78              LD      A,B                 
4FC1: 78              LD      A,B                 
4FC2: 78              LD      A,B                 
4FC3: 78              LD      A,B                 
4FC4: FC                              
4FC5: FD                              
4FC6: FE FF           CP      $FF                 
4FC8: FE FF           CP      $FF                 
4FCA: 12              LD      (DE),A              
4FCB: 13              INC     DE                  
4FCC: 0C              INC     C                   
4FCD: 04              INC     B                   
4FCE: 0E 05           LD      C,$05               
4FD0: 04              INC     B                   
4FD1: 0D              DEC     C                   
4FD2: 05              DEC     B                   
4FD3: 0F              RRCA                        
4FD4: 04              INC     B                   
4FD5: 05              DEC     B                   
4FD6: 04              INC     B                   
4FD7: 05              DEC     B                   
4FD8: 06 07           LD      B,$07               
4FDA: 08 09 0A        LD      ($0A09),SP          
4FDD: 0B              DEC     BC                  
4FDE: 06 07           LD      B,$07               
4FE0: 60              LD      H,B                 
4FE1: 61              LD      H,C                 
4FE2: 70              LD      (HL),B              
4FE3: 71              LD      (HL),C              
4FE4: 62              LD      H,D                 
4FE5: 63              LD      H,E                 
4FE6: 70              LD      (HL),B              
4FE7: 71              LD      (HL),C              
4FE8: 0C              INC     C                   
4FE9: 0D              DEC     C                   
4FEA: 0E 0F           LD      C,$0F               
4FEC: 00              NOP                         
4FED: 01 02 03        LD      BC,$0302            
4FF0: 28 00           JR      Z,$4FF2             ; {}
4FF2: 38 02           JR      C,$4FF6             ; {}
4FF4: 01 28 03        LD      BC,$0328            
4FF7: 38 F8           JR      C,$4FF1             ; {}
4FF9: FA F9 FB        LD      A,($FBF9)           
4FFC: F8 FA           LD      HL,SP+$FA           
4FFE: F9              LD      SP,HL               
4FFF: FB              EI                          
5000: 0C              INC     C                   
5001: 0D              DEC     C                   
5002: 0E 0F           LD      C,$0F               
5004: FC                              
5005: FE FD           CP      $FD                 
5007: FF              RST     0X38                
5008: 14              INC     D                   
5009: 15              DEC     D                   
500A: 16 17           LD      D,$17               
500C: 64              LD      H,H                 
500D: 65              LD      H,L                 
500E: 74              LD      (HL),H              
500F: 75              LD      (HL),L              
5010: 6C              LD      L,H                 
5011: 6D              LD      L,L                 
5012: 74              LD      (HL),H              
5013: 75              LD      (HL),L              
5014: 7C              LD      A,H                 
5015: 7C              LD      A,H                 
5016: 7C              LD      A,H                 
5017: 7C              LD      A,H                 
5018: 76              HALT                        
5019: 76              HALT                        
501A: 77              LD      (HL),A              
501B: 77              LD      (HL),A              
501C: 76              HALT                        
501D: 76              HALT                        
501E: 7E              LD      A,(HL)              
501F: 7E              LD      A,(HL)              
5020: 7E              LD      A,(HL)              
5021: 7E              LD      A,(HL)              
5022: 77              LD      (HL),A              
5023: 77              LD      (HL),A              
5024: 28 00           JR      Z,$5026             ; {}
5026: 38 02           JR      C,$502A             ; {}
5028: 01 28 03        LD      BC,$0328            
502B: 38 10           JR      C,$503D             ; {}
502D: 0B              DEC     BC                  
502E: 12              LD      (DE),A              
502F: 0B              DEC     BC                  
5030: 0B              DEC     BC                  
5031: 0B              DEC     BC                  
5032: 06 06           LD      B,$06               
5034: 0B              DEC     BC                  
5035: 11 0B 13        LD      DE,$130B            
5038: 10 0B           ;;STOP    $0B                 
503A: 12              LD      (DE),A              
503B: 00              NOP                         
503C: 06 07           LD      B,$07               
503E: 01 09 08        LD      BC,$0809            
5041: 06 09           LD      B,$09               
5043: 00              NOP                         
5044: 0B              DEC     BC                  
5045: 11 01 13        LD      DE,$1301            
5048: 29              ADD     HL,HL               
5049: 02              LD      (BC),A              
504A: 39              ADD     HL,SP               
504B: 04              INC     B                   
504C: 03              INC     BC                  
504D: 0A              LD      A,(BC)              
504E: 05              DEC     B                   
504F: 7F              LD      A,A                 
5050: 0A              LD      A,(BC)              
5051: 02              LD      (BC),A              
5052: 7F              LD      A,A                 
5053: 04              INC     B                   
5054: 03              INC     BC                  
5055: 29              ADD     HL,HL               
5056: 05              DEC     B                   
5057: 39              ADD     HL,SP               
5058: 6A              LD      L,D                 
5059: 6B              LD      L,E                 
505A: 7A              LD      A,D                 
505B: 7B              LD      A,E                 
505C: 6A              LD      L,D                 
505D: 6B              LD      L,E                 
505E: 7A              LD      A,D                 
505F: 7B              LD      A,E                 
5060: F4                              
5061: F6 F5           OR      $F5                 
5063: F7              RST     0X30                
5064: 00              NOP                         
5065: 7F              LD      A,A                 
5066: 01 7F 7F        LD      BC,$7F7F            
5069: 02              LD      (BC),A              
506A: 7F              LD      A,A                 
506B: 03              INC     BC                  
506C: 00              NOP                         
506D: 00              NOP                         
506E: 01 01 02        LD      BC,$0201            
5071: 02              LD      (BC),A              
5072: 03              INC     BC                  
5073: 03              INC     BC                  
5074: 08 09 0A        LD      ($0A09),SP          
5077: 0B              DEC     BC                  
5078: 0A              LD      A,(BC)              
5079: 0B              DEC     BC                  
507A: 06 07           LD      B,$07               
507C: 6E              LD      L,(HL)              
507D: 6E              LD      L,(HL)              
507E: 4C              LD      C,H                 
507F: 4C              LD      C,H                 
5080: 4F              LD      C,A                 
5081: 4F              LD      C,A                 
5082: 6E              LD      L,(HL)              
5083: 6E              LD      L,(HL)              
5084: 6E              LD      L,(HL)              
5085: 5C              LD      E,H                 
5086: 6E              LD      L,(HL)              
5087: 5C              LD      E,H                 
5088: 5F              LD      E,A                 
5089: 6E              LD      L,(HL)              
508A: 5F              LD      E,A                 
508B: 6E              LD      L,(HL)              
508C: 08 09 0A        LD      ($0A09),SP          
508F: 0B              DEC     BC                  
5090: 04              INC     B                   
5091: 05              DEC     B                   
5092: 06 07           LD      B,$07               
5094: 0B              DEC     BC                  
5095: 0B              DEC     BC                  
5096: 12              LD      (DE),A              
5097: 13              INC     DE                  
5098: 0C              INC     C                   
5099: 0D              DEC     C                   
509A: 0E 0F           LD      C,$0F               
509C: 0C              INC     C                   
509D: 0C              INC     C                   
509E: 0C              INC     C                   
509F: 0C              INC     C                   
50A0: 0D              DEC     C                   
50A1: 0D              DEC     C                   
50A2: 0D              DEC     C                   
50A3: 0D              DEC     C                   
50A4: 0E 0E           LD      C,$0E               
50A6: 0E 0E           LD      C,$0E               
50A8: 0F              RRCA                        
50A9: 0F              RRCA                        
50AA: 0F              RRCA                        
50AB: 0F              RRCA                        
50AC: 7F              LD      A,A                 
50AD: 7F              LD      A,A                 
50AE: 0B              DEC     BC                  
50AF: 0B              DEC     BC                  
50B0: 6F              LD      L,A                 
50B1: 6F              LD      L,A                 
50B2: 6F              LD      L,A                 
50B3: 6F              LD      L,A                 
50B4: 08 08 09        LD      ($0908),SP          
50B7: 0B              DEC     BC                  
50B8: 08 08 0B        LD      ($0B08),SP          
50BB: 0A              LD      A,(BC)              
50BC: 05              DEC     B                   
50BD: 07              RLCA                        
50BE: 04              INC     B                   
50BF: 04              INC     B                   
50C0: 07              RLCA                        
50C1: 06 04           LD      B,$04               
50C3: 04              INC     B                   
50C4: 6A              LD      L,D                 
50C5: 6B              LD      L,E                 
50C6: 7A              LD      A,D                 
50C7: 7B              LD      A,E                 
50C8: 5B              LD      E,E                 
50C9: 5B              LD      E,E                 
50CA: 5B              LD      E,E                 
50CB: 5B              LD      E,E                 
50CC: 04              INC     B                   
50CD: 05              DEC     B                   
50CE: 06 07           LD      B,$07               
50D0: 08 09 0A        LD      ($0A09),SP          
50D3: 0B              DEC     BC                  
50D4: 0C              INC     C                   
50D5: 0D              DEC     C                   
50D6: 0E 0F           LD      C,$0F               
50D8: 0C              INC     C                   
50D9: 0D              DEC     C                   
50DA: 0E 0F           LD      C,$0F               
50DC: 1C              INC     E                   
50DD: 1D              DEC     E                   
50DE: 1E 1F           LD      E,$1F               
50E0: 0E 0F           LD      C,$0F               
50E2: 1E 1F           LD      E,$1F               
50E4: 20 21           JR      NZ,$5107            ; {}
50E6: 30 31           JR      NC,$5119            ; {}
50E8: 22              LD      (HLI),A             
50E9: 23              INC     HL                  
50EA: 32              LD      (HLD),A             
50EB: 33              INC     SP                  
50EC: 6A              LD      L,D                 
50ED: 7A              LD      A,D                 
50EE: 50              LD      D,B                 
50EF: 61              LD      H,C                 
50F0: 7A              LD      A,D                 
50F1: 7A              LD      A,D                 
50F2: 44              LD      B,H                 
50F3: 45              LD      B,L                 
50F4: 7A              LD      A,D                 
50F5: 6B              LD      L,E                 
50F6: 4C              LD      C,H                 
50F7: 53              LD      D,E                 
50F8: 4C              LD      C,H                 
50F9: 4D              LD      C,L                 
50FA: 5C              LD      E,H                 
50FB: 5D              LD      E,L                 
50FC: 00              NOP                         
50FD: 01 02 03        LD      BC,$0302            
5100: 04              INC     B                   
5101: 05              DEC     B                   
5102: 06 07           LD      B,$07               
5104: 08 09 0A        LD      ($0A09),SP          
5107: 0B              DEC     BC                  
5108: 0C              INC     C                   
5109: 0D              DEC     C                   
510A: 0E 0F           LD      C,$0F               
510C: 00              NOP                         
510D: 00              NOP                         
510E: 00              NOP                         
510F: 00              NOP                         
5110: 01 00 00        LD      BC,$0000            
5113: 00              NOP                         
5114: 00              NOP                         
5115: 01 01 01        LD      BC,$0101            
5118: 00              NOP                         
5119: 00              NOP                         
511A: 06 00           LD      B,$00               
511C: 00              NOP                         
511D: 00              NOP                         
511E: 07              RLCA                        
511F: 00              NOP                         
5120: 00              NOP                         
5121: 00              NOP                         
5122: 00              NOP                         
5123: 00              NOP                         
5124: 00              NOP                         
5125: 00              NOP                         
5126: 00              NOP                         
5127: 00              NOP                         
5128: 00              NOP                         
5129: 00              NOP                         
512A: 00              NOP                         
512B: 05              DEC     B                   
512C: 01 01 05        LD      BC,$0501            
512F: 04              INC     B                   
5130: 30 01           JR      NC,$5133            ; {}
5132: 01 00 00        LD      BC,$0000            
5135: 01 01 01        LD      BC,$0101            
5138: 01 01 01        LD      BC,$0101            
513B: 01 01 01        LD      BC,$0101            
513E: 01 01 05        LD      BC,$0501            
5141: 01 01 01        LD      BC,$0101            
5144: 01 01 01        LD      BC,$0101            
5147: 01 01 01        LD      BC,$0101            
514A: 01 01 01        LD      BC,$0101            
514D: 01 01 01        LD      BC,$0101            
5150: 01 01 01        LD      BC,$0101            
5153: 10 00           ;;STOP    $00                 
5155: 01 01 01        LD      BC,$0101            
5158: 01 01 10        LD      BC,$1001            
515B: 01 01 01        LD      BC,$0101            
515E: 01 01 01        LD      BC,$0101            
5161: 01 01 0A        LD      BC,$0A01            
5164: C0              RET     NZ                  
5165: 01 01 01        LD      BC,$0101            
5168: 01 01 01        LD      BC,$0101            
516B: 01 30 01        LD      BC,$0130            
516E: 01 01 01        LD      BC,$0101            
5171: 01 01 01        LD      BC,$0101            
5174: 01 01 01        LD      BC,$0101            
5177: 01 01 01        LD      BC,$0101            
517A: 01 01 01        LD      BC,$0101            
517D: 01 60 01        LD      BC,$0160            
5180: C0              RET     NZ                  
5181: 01 01 01        LD      BC,$0101            
5184: 01 01 01        LD      BC,$0101            
5187: 02              LD      (BC),A              
5188: 08 08 08        LD      ($0808),SP          
518B: 50              LD      D,B                 
518C: 01 01 01        LD      BC,$0101            
518F: 01 01 01        LD      BC,$0101            
5192: 01 01 01        LD      BC,$0101            
5195: 01 01 01        LD      BC,$0101            
5198: 01 01 01        LD      BC,$0101            
519B: 01 01 01        LD      BC,$0101            
519E: 01 01 01        LD      BC,$0101            
51A1: 01 01 01        LD      BC,$0101            
51A4: 01 01 01        LD      BC,$0101            
51A7: 01 01 01        LD      BC,$0101            
51AA: 01 01 01        LD      BC,$0101            
51AD: 01 01 01        LD      BC,$0101            
51B0: 60              LD      H,B                 
51B1: 60              LD      H,B                 
51B2: 01 01 00        LD      BC,$0001            
51B5: 01 01 01        LD      BC,$0101            
51B8: 01 01 01        LD      BC,$0101            
51BB: 01 01 01        LD      BC,$0101            
51BE: 01 01 01        LD      BC,$0101            
51C1: 01 01 00        LD      BC,$0001            
51C4: 01 01 01        LD      BC,$0101            
51C7: 01 01 00        LD      BC,$0001            
51CA: 99              SBC     C                   
51CB: 01 01 01        LD      BC,$0101            
51CE: 01 01 C0        LD      BC,$C001            
51D1: 01 01 01        LD      BC,$0101            
51D4: 01 01 09        LD      BC,$0901            
51D7: 01 60 01        LD      BC,$0160            
51DA: 01 03 09        LD      BC,$0903            
51DD: 01 01 F4        LD      BC,$F401            
51E0: F5              PUSH    AF                  
51E1: F6 F7           OR      $F7                 
51E3: 30 60           JR      NC,$5245            ; {}
51E5: 01 01 01        LD      BC,$0101            
51E8: 01 07 01        LD      BC,$0107            
51EB: 08 00 01        LD      ($0100),SP          
51EE: 01 01 02        LD      BC,$0201            
51F1: 03              INC     BC                  
51F2: 03              INC     BC                  
51F3: 03              INC     BC                  
51F4: 01 01 81        LD      BC,$8101            
51F7: 03              INC     BC                  
51F8: 50              LD      D,B                 
51F9: 01 01 07        LD      BC,$0701            
51FC: 07              RLCA                        
51FD: 07              RLCA                        
51FE: 07              RLCA                        
51FF: 50              LD      D,B                 
5200: D1              POP     DE                  
5201: 01 01 D0        LD      BC,$D001            
5204: 01 01 01        LD      BC,$0101            
5207: 01 01 01        LD      BC,$0101            
520A: 01 01 01        LD      BC,$0101            
520D: 01 01 FF        LD      BC,$FF01            
5210: 00              NOP                         
5211: 50              LD      D,B                 
5212: 00              NOP                         
5213: 00              NOP                         
5214: 00              NOP                         
5215: 00              NOP                         
5216: 0B              DEC     BC                  
5217: 00              NOP                         
5218: 7D              LD      A,L                 
5219: 7E              LD      A,(HL)              
521A: 7F              LD      A,A                 
521B: 7E              LD      A,(HL)              
521C: 7F              LD      A,A                 
521D: 00              NOP                         
521E: 07              RLCA                        
521F: 00              NOP                         
5220: 81              ADD     A,C                 
5221: 80              ADD     A,B                 
5222: 82              ADD     A,D                 
5223: 83              ADD     A,E                 
5224: 84              ADD     A,H                 
5225: 85              ADD     A,L                 
5226: 86              ADD     A,(HL)              
5227: 87              ADD     A,A                 
5228: 00              NOP                         
5229: 8C              ADC     A,H                 
522A: 8D              ADC     A,L                 
522B: 05              DEC     B                   
522C: 51              LD      D,C                 
522D: 51              LD      D,C                 
522E: 51              LD      D,C                 
522F: 51              LD      D,C                 
5230: 30 D3           JR      NC,$5205            ; {}
5232: D2 D0 D1        JP      NC,$D1D0            
5235: 01 01 01        LD      BC,$0101            
5238: 01 01 01        LD      BC,$0101            
523B: 01 01 90        LD      BC,$9001            
523E: 90              SUB     B                   
523F: 91              SUB     C                   
5240: 91              SUB     C                   
5241: 92              SUB     D                   
5242: 92              SUB     D                   
5243: 93              SUB     E                   
5244: 93              SUB     E                   
5245: D3                              
5246: D3                              
5247: D2 D2 D0        JP      NC,$D0D2            
524A: D0              RET     NC                  
524B: D1              POP     DE                  
524C: D1              POP     DE                  
524D: 00              NOP                         
524E: 00              NOP                         
524F: 99              SBC     C                   
5250: 9A              SBC     D                   
5251: 9B              SBC     E                   
5252: 9C              SBC     H                   
5253: 7C              LD      A,H                 
5254: 7D              LD      A,L                 
5255: 01 01 99        LD      BC,$9901            
5258: 9A              SBC     D                   
5259: 9B              SBC     E                   
525A: 9C              SBC     H                   
525B: B0              OR      B                   
525C: 00              NOP                         
525D: 00              NOP                         
525E: 60              LD      H,B                 
525F: 60              LD      H,B                 
5260: 01 01 01        LD      BC,$0101            
5263: 01 01 01        LD      BC,$0101            
5266: 01 01 01        LD      BC,$0101            
5269: 01 01 01        LD      BC,$0101            
526C: 01 01 01        LD      BC,$0101            
526F: 01 01 01        LD      BC,$0101            
5272: B1              OR      C                   
5273: B1              OR      C                   
5274: B1              OR      C                   
5275: B1              OR      C                   
5276: B1              OR      C                   
5277: B0              OR      B                   
5278: 01 00 00        LD      BC,$0000            
527B: 00              NOP                         
527C: 01 01 00        LD      BC,$0001            
527F: 00              NOP                         
5280: 00              NOP                         
5281: 00              NOP                         
5282: B0              OR      B                   
5283: B0              OR      B                   
5284: B0              OR      B                   
5285: 00              NOP                         
5286: 00              NOP                         
5287: 00              NOP                         
5288: 00              NOP                         
5289: 00              NOP                         
528A: 00              NOP                         
528B: 01 00 B0        LD      BC,$B000            
528E: B0              OR      B                   
528F: 00              NOP                         
5290: B0              OR      B                   
5291: B0              OR      B                   
5292: 00              NOP                         
5293: B0              OR      B                   
5294: B0              OR      B                   
5295: B0              OR      B                   
5296: 01 01 60        LD      BC,$6001            
5299: 00              NOP                         
529A: 01 01 7C        LD      BC,$7C01            
529D: 00              NOP                         
529E: 30 60           JR      NC,$5300            ; {}
52A0: 01 01 00        LD      BC,$0001            
52A3: 88              ADC     A,B                 
52A4: 89              ADC     A,C                 
52A5: 8A              ADC     A,D                 
52A6: 8B              ADC     A,E                 
52A7: 0A              LD      A,(BC)              
52A8: 02              LD      (BC),A              
52A9: 01 7E 01        LD      BC,$017E            
52AC: 01 00 00        LD      BC,$0000            
52AF: 00              NOP                         
52B0: 60              LD      H,B                 
52B1: 60              LD      H,B                 
52B2: 03              INC     BC                  
52B3: 03              INC     BC                  
52B4: 98              SBC     B                   
52B5: 98              SBC     B                   
52B6: 60              LD      H,B                 
52B7: 60              LD      H,B                 
52B8: 03              INC     BC                  
52B9: 30 00           JR      NC,$52BB            ; {}
52BB: 01 01 01        LD      BC,$0101            
52BE: 50              LD      D,B                 
52BF: 50              LD      D,B                 
52C0: 50              LD      D,B                 
52C1: 7C              LD      A,H                 
52C2: 7D              LD      A,L                 
52C3: 00              NOP                         
52C4: 00              NOP                         
52C5: 00              NOP                         
52C6: 8B              ADC     A,E                 
52C7: 8A              ADC     A,D                 
52C8: 8B              ADC     A,E                 
52C9: 8A              ADC     A,D                 
52CA: 01 7C 7D        LD      BC,$7D7C            
52CD: 01 00 00        LD      BC,$0000            
52D0: 01 7C 7D        LD      BC,$7D7C            
52D3: 01 01 01        LD      BC,$0101            
52D6: 01 D3 D2        LD      BC,$D2D3            
52D9: D0              RET     NC                  
52DA: D1              POP     DE                  
52DB: 08 09 7E        LD      ($7E09),SP          ; {}
52DE: 01 F0 F1        LD      BC,$F1F0            
52E1: F2                              
52E2: F3              DI                          
52E3: 7F              LD      A,A                 
52E4: E0 01           LD      ($FF00+$01),A       
52E6: 01 01 01        LD      BC,$0101            
52E9: 60              LD      H,B                 
52EA: 00              NOP                         
52EB: 04              INC     B                   
52EC: 04              INC     B                   
52ED: 30 01           JR      NC,$52F0            ; {}
52EF: 00              NOP                         
52F0: 00              NOP                         
52F1: 00              NOP                         
52F2: 00              NOP                         
52F3: 00              NOP                         
52F4: 00              NOP                         
52F5: 00              NOP                         
52F6: 00              NOP                         
52F7: 00              NOP                         
52F8: 00              NOP                         
52F9: 00              NOP                         
52FA: 00              NOP                         
52FB: 01 01 01        LD      BC,$0101            
52FE: 01 01 01        LD      BC,$0101            
5301: 01 01 01        LD      BC,$0101            
5304: 01 01 01        LD      BC,$0101            
5307: 01 01 01        LD      BC,$0101            
530A: 01 01 01        LD      BC,$0101            
530D: 01 FE FF        LD      BC,$FFFE            
5310: 98              SBC     B                   
5311: 00              NOP                         
5312: 13              INC     DE                  
5313: 00              NOP                         
5314: 01 02 03        LD      BC,$0302            
5317: 00              NOP                         
5318: 01 02 03        LD      BC,$0302            
531B: 00              NOP                         
531C: 01 02 03        LD      BC,$0302            
531F: 00              NOP                         
5320: 01 02 03        LD      BC,$0302            
5323: 00              NOP                         
5324: 01 02 03        LD      BC,$0302            
5327: 98              SBC     B                   
5328: 20 13           JR      NZ,$533D            ; {}
532A: 10 11           ;;STOP    $11                 
532C: 12              LD      (DE),A              
532D: 13              INC     DE                  
532E: 10 11           ;;STOP    $11                 
5330: 12              LD      (DE),A              
5331: 13              INC     DE                  
5332: 10 11           ;;STOP    $11                 
5334: 12              LD      (DE),A              
5335: 13              INC     DE                  
5336: 10 11           ;;STOP    $11                 
5338: 12              LD      (DE),A              
5339: 13              INC     DE                  
533A: 10 11           ;;STOP    $11                 
533C: 12              LD      (DE),A              
533D: 13              INC     DE                  
533E: 98              SBC     B                   
533F: 40              LD      B,B                 
5340: 13              INC     DE                  
5341: 02              LD      (BC),A              
5342: 03              INC     BC                  
5343: 04              INC     B                   
5344: 05              DEC     B                   
5345: 06 07           LD      B,$07               
5347: 06 07           LD      B,$07               
5349: 07              RLCA                        
534A: 06 06           LD      B,$06               
534C: 07              RLCA                        
534D: 06 07           LD      B,$07               
534F: 07              RLCA                        
5350: 07              RLCA                        
5351: 06 08           LD      B,$08               
5353: 00              NOP                         
5354: 01 98 60        LD      BC,$6098            
5357: 13              INC     DE                  
5358: 12              LD      (DE),A              
5359: 13              INC     DE                  
535A: 09              ADD     HL,BC               
535B: 0A              LD      A,(BC)              
535C: 0B              DEC     BC                  
535D: 14              INC     D                   
535E: 0C              INC     C                   
535F: 0D              DEC     C                   
5360: 0E 0F           LD      C,$0F               
5362: 0B              DEC     BC                  
5363: 15              DEC     D                   
5364: 14              INC     D                   
5365: 15              DEC     D                   
5366: 0B              DEC     BC                  
5367: 14              INC     D                   
5368: 16 17           LD      D,$17               
536A: 10 11           ;;STOP    $11                 
536C: 98              SBC     B                   
536D: 80              ADD     A,B                 
536E: 13              INC     DE                  
536F: 00              NOP                         
5370: 03              INC     BC                  
5371: 18 19           JR      $538C               ; {}
5373: 1A              LD      A,(DE)              
5374: 1B              DEC     DE                  
5375: 1C              INC     E                   
5376: 1D              DEC     E                   
5377: 1E 1F           LD      E,$1F               
5379: 20 21           JR      NZ,$539C            ; {}
537B: 22              LD      (HLI),A             
537C: 1E 20           LD      E,$20               
537E: 22              LD      (HLI),A             
537F: 24              INC     H                   
5380: 25              DEC     H                   
5381: 00              NOP                         
5382: 03              INC     BC                  
5383: 98              SBC     B                   
5384: A0              AND     B                   
5385: 13              INC     DE                  
5386: 10 13           ;;STOP    $13                 
5388: 26 27           LD      H,$27               
538A: 28 29           JR      Z,$53B5             ; {}
538C: 2A              LD      A,(HLI)             
538D: 2B              DEC     HL                  
538E: 2C              INC     L                   
538F: 22              LD      (HLI),A             
5390: 21 37 21        LD      HL,$2137            
5393: 22              LD      (HLI),A             
5394: 1F              RRA                         
5395: 20 42           JR      NZ,$53D9            ; {}
5397: 2D              DEC     L                   
5398: 10 13           ;;STOP    $13                 
539A: 98              SBC     B                   
539B: C0              RET     NZ                  
539C: 13              INC     DE                  
539D: 02              LD      (BC),A              
539E: 03              INC     BC                  
539F: 18 2E           JR      $53CF               ; {}
53A1: 2F              CPL                         
53A2: 30 42           JR      NC,$53E6            ; {}
53A4: 1D              DEC     E                   
53A5: 40              LD      B,B                 
53A6: 21 1F 22        LD      HL,$221F            
53A9: 20 1F           JR      NZ,$53CA            ; {}
53AB: 37              SCF                         
53AC: 21 40 31        LD      HL,$3140            
53AF: 00              NOP                         
53B0: 01 98 E0        LD      BC,$E098            
53B3: 13              INC     DE                  
53B4: 12              LD      (DE),A              
53B5: 13              INC     DE                  
53B6: 32              LD      (HLD),A             
53B7: 33              INC     SP                  
53B8: 34              INC     (HL)                
53B9: 42              LD      B,D                 
53BA: 35              DEC     (HL)                
53BB: 36 1D           LD      (HL),$1D            
53BD: 22              LD      (HLI),A             
53BE: 20 1F           JR      NZ,$53DF            ; {}
53C0: 39              ADD     HL,SP               
53C1: 37              SCF                         
53C2: 38 39           JR      C,$53FD             ; {}
53C4: 42              LD      B,D                 
53C5: 2D              DEC     L                   
53C6: 10 11           ;;STOP    $11                 
53C8: 99              SBC     C                   
53C9: 00              NOP                         
53CA: 13              INC     DE                  
53CB: 00              NOP                         
53CC: 03              INC     BC                  
53CD: 3A              LD      A,(HLD)             
53CE: 3B              DEC     SP                  
53CF: 2B              DEC     HL                  
53D0: 2C              INC     L                   
53D1: 3C              INC     A                   
53D2: 1D              DEC     E                   
53D3: 3D              DEC     A                   
53D4: 3E 3F           LD      A,$3F               
53D6: 42              LD      B,D                 
53D7: 40              LD      B,B                 
53D8: 40              LD      B,B                 
53D9: 40              LD      B,B                 
53DA: 40              LD      B,B                 
53DB: 3C              INC     A                   
53DC: 31 00 03        LD      SP,$0300            
53DF: 99              SBC     C                   
53E0: 20 13           JR      NZ,$53F5            ; {}
53E2: 10 13           ;;STOP    $13                 
53E4: 18 41           JR      $5427               ; {}
53E6: 42              LD      B,D                 
53E7: 3C              INC     A                   
53E8: 1D              DEC     E                   
53E9: 42              LD      B,D                 
53EA: 43              LD      B,E                 
53EB: 44              LD      B,H                 
53EC: 45              LD      B,L                 
53ED: 40              LD      B,B                 
53EE: 42              LD      B,D                 
53EF: 40              LD      B,B                 
53F0: 42              LD      B,D                 
53F1: 1D              DEC     E                   
53F2: 46              LD      B,(HL)              
53F3: 31 10 13        LD      SP,$1310            
53F6: 99              SBC     C                   
53F7: 40              LD      B,B                 
53F8: 13              INC     DE                  
53F9: 02              LD      (BC),A              
53FA: 03              INC     BC                  
53FB: 18 47           JR      $5444               ; {}
53FD: 48              LD      C,B                 
53FE: 49              LD      C,C                 
53FF: 4A              LD      C,D                 
5400: 4B              LD      C,E                 
5401: 48              LD      C,B                 
5402: 49              LD      C,C                 
5403: 4A              LD      C,D                 
5404: 4C              LD      C,H                 
5405: 4D              LD      C,L                 
5406: 4E              LD      C,(HL)              
5407: 3C              INC     A                   
5408: 4F              LD      C,A                 
5409: 50              LD      D,B                 
540A: 2D              DEC     L                   
540B: 00              NOP                         
540C: 01 99 60        LD      BC,$6099            
540F: 13              INC     DE                  
5410: 12              LD      (DE),A              
5411: 13              INC     DE                  
5412: 51              LD      D,C                 
5413: 52              LD      D,D                 
5414: 53              LD      D,E                 
5415: 54              LD      D,H                 
5416: 55              LD      D,L                 
5417: 56              LD      D,(HL)              
5418: 57              LD      D,A                 
5419: 58              LD      E,B                 
541A: 56              LD      D,(HL)              
541B: 58              LD      E,B                 
541C: 59              LD      E,C                 
541D: 5A              LD      E,D                 
541E: 5B              LD      E,E                 
541F: 5C              LD      E,H                 
5420: 5D              LD      E,L                 
5421: 2D              DEC     L                   
5422: 10 11           ;;STOP    $11                 
5424: 99              SBC     C                   
5425: 80              ADD     A,B                 
5426: 13              INC     DE                  
5427: 02              LD      (BC),A              
5428: 03              INC     BC                  
5429: 5E              LD      E,(HL)              
542A: 5F              LD      E,A                 
542B: 60              LD      H,B                 
542C: 61              LD      H,C                 
542D: 62              LD      H,D                 
542E: 63              LD      H,E                 
542F: 64              LD      H,H                 
5430: 65              LD      H,L                 
5431: 63              LD      H,E                 
5432: 64              LD      H,H                 
5433: 66              LD      H,(HL)              
5434: 67              LD      H,A                 
5435: 68              LD      L,B                 
5436: 69              LD      L,C                 
5437: 6A              LD      L,D                 
5438: 31 00 03        LD      SP,$0300            
543B: 99              SBC     C                   
543C: A0              AND     B                   
543D: 13              INC     DE                  
543E: 10 13           ;;STOP    $13                 
5440: 18 6B           JR      $54AD               ; {}
5442: 6C              LD      L,H                 
5443: 6D              LD      L,L                 
5444: 70              LD      (HL),B              
5445: 6E              LD      L,(HL)              
5446: 6F              LD      L,A                 
5447: 70              LD      (HL),B              
5448: 6E              LD      L,(HL)              
5449: 6F              LD      L,A                 
544A: 71              LD      (HL),C              
544B: 72              LD      (HL),D              
544C: 42              LD      B,D                 
544D: 73              LD      (HL),E              
544E: 50              LD      D,B                 
544F: 2D              DEC     L                   
5450: 10 13           ;;STOP    $13                 
5452: 99              SBC     C                   
5453: C0              RET     NZ                  
5454: 13              INC     DE                  
5455: 02              LD      (BC),A              
5456: 03              INC     BC                  
5457: 26 41           LD      H,$41               
5459: 42              LD      B,D                 
545A: 1D              DEC     E                   
545B: 3C              INC     A                   
545C: 1D              DEC     E                   
545D: 74              LD      (HL),H              
545E: 75              LD      (HL),L              
545F: 76              HALT                        
5460: 1D              DEC     E                   
5461: 40              LD      B,B                 
5462: 1D              DEC     E                   
5463: 35              DEC     (HL)                
5464: 36 77           LD      (HL),$77            
5466: 78              LD      A,B                 
5467: 00              NOP                         
5468: 01 99 E0        LD      BC,$E099            
546B: 13              INC     DE                  
546C: 12              LD      (DE),A              
546D: 13              INC     DE                  
546E: 79              LD      A,C                 
546F: 10 7B           ;;STOP    $7B                 
5471: 7A              LD      A,D                 
5472: 7B              LD      A,E                 
5473: 7A              LD      A,D                 
5474: 7C              LD      A,H                 
5475: 7D              LD      A,L                 
5476: 23              INC     HL                  
5477: 7A              LD      A,D                 
5478: 7B              LD      A,E                 
5479: 7B              LD      A,E                 
547A: 7A              LD      A,D                 
547B: 7A              LD      A,D                 
547C: 7F              LD      A,A                 
547D: 13              INC     DE                  
547E: 10 11           ;;STOP    $11                 
5480: 9A              SBC     D                   
5481: 00              NOP                         
5482: 13              INC     DE                  
5483: 00              NOP                         
5484: 01 02 03        LD      BC,$0302            
5487: 00              NOP                         
5488: 01 02 03        LD      BC,$0302            
548B: 00              NOP                         
548C: 01 02 03        LD      BC,$0302            
548F: 00              NOP                         
5490: 01 02 03        LD      BC,$0302            
5493: 00              NOP                         
5494: 01 02 03        LD      BC,$0302            
5497: 9A              SBC     D                   
5498: 20 13           JR      NZ,$54AD            ; {}
549A: 10 11           ;;STOP    $11                 
549C: 12              LD      (DE),A              
549D: 13              INC     DE                  
549E: 10 11           ;;STOP    $11                 
54A0: 12              LD      (DE),A              
54A1: 13              INC     DE                  
54A2: 10 11           ;;STOP    $11                 
54A4: 12              LD      (DE),A              
54A5: 13              INC     DE                  
54A6: 10 11           ;;STOP    $11                 
54A8: 12              LD      (DE),A              
54A9: 13              INC     DE                  
54AA: 10 11           ;;STOP    $11                 
54AC: 12              LD      (DE),A              
54AD: 13              INC     DE                  
54AE: 00              NOP                         
54AF: 98              SBC     B                   
54B0: 00              NOP                         
54B1: 53              LD      D,E                 
54B2: 05              DEC     B                   
54B3: 98              SBC     B                   
54B4: 20 53           JR      NZ,$5509            ; {}
54B6: 05              DEC     B                   
54B7: 98              SBC     B                   
54B8: 40              LD      B,B                 
54B9: 53              LD      D,E                 
54BA: 05              DEC     B                   
54BB: 98              SBC     B                   
54BC: 60              LD      H,B                 
54BD: 53              LD      D,E                 
54BE: 05              DEC     B                   
54BF: 98              SBC     B                   
54C0: 80              ADD     A,B                 
54C1: 53              LD      D,E                 
54C2: 05              DEC     B                   
54C3: 98              SBC     B                   
54C4: A0              AND     B                   
54C5: 53              LD      D,E                 
54C6: 05              DEC     B                   
54C7: 98              SBC     B                   
54C8: C0              RET     NZ                  
54C9: 53              LD      D,E                 
54CA: 05              DEC     B                   
54CB: 98              SBC     B                   
54CC: E0 53           LD      ($FF00+$53),A       
54CE: 05              DEC     B                   
54CF: 99              SBC     C                   
54D0: 00              NOP                         
54D1: 53              LD      D,E                 
54D2: 05              DEC     B                   
54D3: 99              SBC     C                   
54D4: 20 53           JR      NZ,$5529            ; {}
54D6: 05              DEC     B                   
54D7: 99              SBC     C                   
54D8: 40              LD      B,B                 
54D9: 53              LD      D,E                 
54DA: 05              DEC     B                   
54DB: 99              SBC     C                   
54DC: 60              LD      H,B                 
54DD: 53              LD      D,E                 
54DE: 05              DEC     B                   
54DF: 99              SBC     C                   
54E0: 80              ADD     A,B                 
54E1: 53              LD      D,E                 
54E2: 05              DEC     B                   
54E3: 99              SBC     C                   
54E4: A0              AND     B                   
54E5: 53              LD      D,E                 
54E6: 05              DEC     B                   
54E7: 99              SBC     C                   
54E8: C0              RET     NZ                  
54E9: 53              LD      D,E                 
54EA: 05              DEC     B                   
54EB: 99              SBC     C                   
54EC: E0 53           LD      ($FF00+$53),A       
54EE: 05              DEC     B                   
54EF: 9A              SBC     D                   
54F0: 00              NOP                         
54F1: 53              LD      D,E                 
54F2: 05              DEC     B                   
54F3: 9A              SBC     D                   
54F4: 20 53           JR      NZ,$5549            ; {}
54F6: 05              DEC     B                   
54F7: 98              SBC     B                   
54F8: 00              NOP                         
54F9: 53              LD      D,E                 
54FA: 05              DEC     B                   
54FB: 98              SBC     B                   
54FC: 20 53           JR      NZ,$5551            ; {}
54FE: 05              DEC     B                   
54FF: 98              SBC     B                   
5500: 40              LD      B,B                 
5501: 13              INC     DE                  
5502: 05              DEC     B                   
5503: 05              DEC     B                   
5504: 05              DEC     B                   
5505: 05              DEC     B                   
5506: 05              DEC     B                   
5507: 7B              LD      A,E                 
5508: 7C              LD      A,H                 
5509: 7C              LD      A,H                 
550A: 7C              LD      A,H                 
550B: 7C              LD      A,H                 
550C: 7C              LD      A,H                 
550D: 7C              LD      A,H                 
550E: 7C              LD      A,H                 
550F: 7C              LD      A,H                 
5510: 7E              LD      A,(HL)              
5511: 05              DEC     B                   
5512: 05              DEC     B                   
5513: 05              DEC     B                   
5514: 05              DEC     B                   
5515: 05              DEC     B                   
5516: 98              SBC     B                   
5517: 60              LD      H,B                 
5518: 13              INC     DE                  
5519: 05              DEC     B                   
551A: 05              DEC     B                   
551B: 05              DEC     B                   
551C: 05              DEC     B                   
551D: 05              DEC     B                   
551E: 7F              LD      A,A                 
551F: 00              NOP                         
5520: 01 02 03        LD      BC,$0302            
5523: 04              INC     B                   
5524: 05              DEC     B                   
5525: 06 07           LD      B,$07               
5527: 7F              LD      A,A                 
5528: 05              DEC     B                   
5529: 05              DEC     B                   
552A: 05              DEC     B                   
552B: 05              DEC     B                   
552C: 05              DEC     B                   
552D: 98              SBC     B                   
552E: 80              ADD     A,B                 
552F: 13              INC     DE                  
5530: 05              DEC     B                   
5531: 05              DEC     B                   
5532: 05              DEC     B                   
5533: 05              DEC     B                   
5534: 05              DEC     B                   
5535: 7F              LD      A,A                 
5536: 10 11           ;;STOP    $11                 
5538: 12              LD      (DE),A              
5539: 13              INC     DE                  
553A: 14              INC     D                   
553B: 15              DEC     D                   
553C: 16 17           LD      D,$17               
553E: 7F              LD      A,A                 
553F: 05              DEC     B                   
5540: 05              DEC     B                   
5541: 05              DEC     B                   
5542: 05              DEC     B                   
5543: 05              DEC     B                   
5544: 98              SBC     B                   
5545: A0              AND     B                   
5546: 13              INC     DE                  
5547: 05              DEC     B                   
5548: 05              DEC     B                   
5549: 05              DEC     B                   
554A: 05              DEC     B                   
554B: 05              DEC     B                   
554C: 7F              LD      A,A                 
554D: 20 21           JR      NZ,$5570            ; {}
554F: 22              LD      (HLI),A             
5550: 23              INC     HL                  
5551: 24              INC     H                   
5552: 25              DEC     H                   
5553: 26 27           LD      H,$27               
5555: 7F              LD      A,A                 
5556: 05              DEC     B                   
5557: 05              DEC     B                   
5558: 05              DEC     B                   
5559: 05              DEC     B                   
555A: 05              DEC     B                   
555B: 98              SBC     B                   
555C: C0              RET     NZ                  
555D: 13              INC     DE                  
555E: 05              DEC     B                   
555F: 05              DEC     B                   
5560: 05              DEC     B                   
5561: 05              DEC     B                   
5562: 05              DEC     B                   
5563: 7F              LD      A,A                 
5564: 30 31           JR      NC,$5597            ; {}
5566: 32              LD      (HLD),A             
5567: 33              INC     SP                  
5568: 34              INC     (HL)                
5569: 35              DEC     (HL)                
556A: 36 37           LD      (HL),$37            
556C: 7F              LD      A,A                 
556D: 05              DEC     B                   
556E: 05              DEC     B                   
556F: 05              DEC     B                   
5570: 05              DEC     B                   
5571: 05              DEC     B                   
5572: 98              SBC     B                   
5573: E0 13           LD      ($FF00+$13),A       
5575: 05              DEC     B                   
5576: 05              DEC     B                   
5577: 05              DEC     B                   
5578: 05              DEC     B                   
5579: 05              DEC     B                   
557A: 7F              LD      A,A                 
557B: 40              LD      B,B                 
557C: 41              LD      B,C                 
557D: 42              LD      B,D                 
557E: 43              LD      B,E                 
557F: 44              LD      B,H                 
5580: 45              LD      B,L                 
5581: 46              LD      B,(HL)              
5582: 47              LD      B,A                 
5583: 7F              LD      A,A                 
5584: 05              DEC     B                   
5585: 05              DEC     B                   
5586: 05              DEC     B                   
5587: 05              DEC     B                   
5588: 05              DEC     B                   
5589: 99              SBC     C                   
558A: 00              NOP                         
558B: 13              INC     DE                  
558C: 05              DEC     B                   
558D: 05              DEC     B                   
558E: 05              DEC     B                   
558F: 05              DEC     B                   
5590: 05              DEC     B                   
5591: 7F              LD      A,A                 
5592: 50              LD      D,B                 
5593: 51              LD      D,C                 
5594: 52              LD      D,D                 
5595: 53              LD      D,E                 
5596: 54              LD      D,H                 
5597: 55              LD      D,L                 
5598: 56              LD      D,(HL)              
5599: 57              LD      D,A                 
559A: 7F              LD      A,A                 
559B: 05              DEC     B                   
559C: 05              DEC     B                   
559D: 05              DEC     B                   
559E: 05              DEC     B                   
559F: 05              DEC     B                   
55A0: 99              SBC     C                   
55A1: 20 13           JR      NZ,$55B6            ; {}
55A3: 05              DEC     B                   
55A4: 05              DEC     B                   
55A5: 05              DEC     B                   
55A6: 05              DEC     B                   
55A7: 05              DEC     B                   
55A8: 7F              LD      A,A                 
55A9: 60              LD      H,B                 
55AA: 61              LD      H,C                 
55AB: 62              LD      H,D                 
55AC: 63              LD      H,E                 
55AD: 64              LD      H,H                 
55AE: 65              LD      H,L                 
55AF: 66              LD      H,(HL)              
55B0: 67              LD      H,A                 
55B1: 7F              LD      A,A                 
55B2: 05              DEC     B                   
55B3: 05              DEC     B                   
55B4: 05              DEC     B                   
55B5: 05              DEC     B                   
55B6: 05              DEC     B                   
55B7: 99              SBC     C                   
55B8: 40              LD      B,B                 
55B9: 13              INC     DE                  
55BA: 05              DEC     B                   
55BB: 05              DEC     B                   
55BC: 05              DEC     B                   
55BD: 05              DEC     B                   
55BE: 05              DEC     B                   
55BF: 7F              LD      A,A                 
55C0: 70              LD      (HL),B              
55C1: 71              LD      (HL),C              
55C2: 72              LD      (HL),D              
55C3: 73              LD      (HL),E              
55C4: 74              LD      (HL),H              
55C5: 75              LD      (HL),L              
55C6: 76              HALT                        
55C7: 77              LD      (HL),A              
55C8: 7F              LD      A,A                 
55C9: 05              DEC     B                   
55CA: 05              DEC     B                   
55CB: 05              DEC     B                   
55CC: 05              DEC     B                   
55CD: 05              DEC     B                   
55CE: 99              SBC     C                   
55CF: 60              LD      H,B                 
55D0: 13              INC     DE                  
55D1: 05              DEC     B                   
55D2: 05              DEC     B                   
55D3: 05              DEC     B                   
55D4: 05              DEC     B                   
55D5: 05              DEC     B                   
55D6: 7F              LD      A,A                 
55D7: 08 09 0A        LD      ($0A09),SP          
55DA: 0B              DEC     BC                  
55DB: 0C              INC     C                   
55DC: 0D              DEC     C                   
55DD: 0E 0F           LD      C,$0F               
55DF: 7F              LD      A,A                 
55E0: 68              LD      L,B                 
55E1: 05              DEC     B                   
55E2: 05              DEC     B                   
55E3: 05              DEC     B                   
55E4: 05              DEC     B                   
55E5: 99              SBC     C                   
55E6: 80              ADD     A,B                 
55E7: 13              INC     DE                  
55E8: 05              DEC     B                   
55E9: 05              DEC     B                   
55EA: 05              DEC     B                   
55EB: 05              DEC     B                   
55EC: 05              DEC     B                   
55ED: 7F              LD      A,A                 
55EE: 18 19           JR      $5609               ; {}
55F0: 1A              LD      A,(DE)              
55F1: 1B              DEC     DE                  
55F2: 1C              INC     E                   
55F3: 1D              DEC     E                   
55F4: 1E 1F           LD      E,$1F               
55F6: 7F              LD      A,A                 
55F7: 78              LD      A,B                 
55F8: 79              LD      A,C                 
55F9: 05              DEC     B                   
55FA: 05              DEC     B                   
55FB: 05              DEC     B                   
55FC: 99              SBC     C                   
55FD: A0              AND     B                   
55FE: 13              INC     DE                  
55FF: 05              DEC     B                   
5600: 05              DEC     B                   
5601: 05              DEC     B                   
5602: 05              DEC     B                   
5603: 05              DEC     B                   
5604: 7D              LD      A,L                 
5605: 3E 4D           LD      A,$4D               
5607: 4E              LD      C,(HL)              
5608: 58              LD      E,B                 
5609: 69              LD      L,C                 
560A: 6A              LD      L,D                 
560B: 6B              LD      L,E                 
560C: 6C              LD      L,H                 
560D: 6D              LD      L,L                 
560E: 6E              LD      L,(HL)              
560F: 6F              LD      L,A                 
5610: 05              DEC     B                   
5611: 05              DEC     B                   
5612: 05              DEC     B                   
5613: 99              SBC     C                   
5614: C0              RET     NZ                  
5615: 13              INC     DE                  
5616: 05              DEC     B                   
5617: 05              DEC     B                   
5618: 05              DEC     B                   
5619: 05              DEC     B                   
561A: 05              DEC     B                   
561B: 05              DEC     B                   
561C: 05              DEC     B                   
561D: 05              DEC     B                   
561E: 05              DEC     B                   
561F: 05              DEC     B                   
5620: 28 29           JR      Z,$564B             ; {}
5622: 2A              LD      A,(HLI)             
5623: 2B              DEC     HL                  
5624: 2C              INC     L                   
5625: 2D              DEC     L                   
5626: 2E 2F           LD      L,$2F               
5628: 05              DEC     B                   
5629: 05              DEC     B                   
562A: 99              SBC     C                   
562B: E0 13           LD      ($FF00+$13),A       
562D: 05              DEC     B                   
562E: 05              DEC     B                   
562F: 05              DEC     B                   
5630: 05              DEC     B                   
5631: 05              DEC     B                   
5632: 05              DEC     B                   
5633: 05              DEC     B                   
5634: 05              DEC     B                   
5635: 05              DEC     B                   
5636: 05              DEC     B                   
5637: 38 39           JR      C,$5672             ; {}
5639: 3A              LD      A,(HLD)             
563A: 3B              DEC     SP                  
563B: 3C              INC     A                   
563C: 3D              DEC     A                   
563D: 3D              DEC     A                   
563E: 3F              CCF                         
563F: 05              DEC     B                   
5640: 05              DEC     B                   
5641: 9A              SBC     D                   
5642: 00              NOP                         
5643: 13              INC     DE                  
5644: 05              DEC     B                   
5645: 05              DEC     B                   
5646: 05              DEC     B                   
5647: 05              DEC     B                   
5648: 05              DEC     B                   
5649: 05              DEC     B                   
564A: 05              DEC     B                   
564B: 05              DEC     B                   
564C: 05              DEC     B                   
564D: 05              DEC     B                   
564E: 48              LD      C,B                 
564F: 49              LD      C,C                 
5650: 4A              LD      C,D                 
5651: 4B              LD      C,E                 
5652: 4C              LD      C,H                 
5653: 3D              DEC     A                   
5654: 3D              DEC     A                   
5655: 4F              LD      C,A                 
5656: 05              DEC     B                   
5657: 05              DEC     B                   
5658: 9A              SBC     D                   
5659: 20 13           JR      NZ,$566E            ; {}
565B: 05              DEC     B                   
565C: 05              DEC     B                   
565D: 05              DEC     B                   
565E: 05              DEC     B                   
565F: 05              DEC     B                   
5660: 05              DEC     B                   
5661: 05              DEC     B                   
5662: 05              DEC     B                   
5663: 05              DEC     B                   
5664: 05              DEC     B                   
5665: 05              DEC     B                   
5666: 59              LD      E,C                 
5667: 5A              LD      E,D                 
5668: 5B              LD      E,E                 
5669: 5C              LD      E,H                 
566A: 5D              LD      E,L                 
566B: 5E              LD      E,(HL)              
566C: 5F              LD      E,A                 
566D: 05              DEC     B                   
566E: 05              DEC     B                   
566F: 00              NOP                         
5670: 98              SBC     B                   
5671: 00              NOP                         
5672: 53              LD      D,E                 
5673: 7C              LD      A,H                 
5674: 98              SBC     B                   
5675: 20 53           JR      NZ,$56CA            ; {}
5677: 7C              LD      A,H                 
5678: 98              SBC     B                   
5679: 40              LD      B,B                 
567A: 53              LD      D,E                 
567B: 7C              LD      A,H                 
567C: 98              SBC     B                   
567D: 60              LD      H,B                 
567E: 13              INC     DE                  
567F: 06 7C           LD      B,$7C               
5681: 7C              LD      A,H                 
5682: 7C              LD      A,H                 
5683: 7C              LD      A,H                 
5684: 7C              LD      A,H                 
5685: 7C              LD      A,H                 
5686: 7C              LD      A,H                 
5687: 7C              LD      A,H                 
5688: 7C              LD      A,H                 
5689: 7C              LD      A,H                 
568A: 7C              LD      A,H                 
568B: 7C              LD      A,H                 
568C: 7C              LD      A,H                 
568D: 7C              LD      A,H                 
568E: 7C              LD      A,H                 
568F: 7C              LD      A,H                 
5690: 7C              LD      A,H                 
5691: 7C              LD      A,H                 
5692: 09              ADD     HL,BC               
5693: 98              SBC     B                   
5694: 80              ADD     A,B                 
5695: 13              INC     DE                  
5696: 7F              LD      A,A                 
5697: 16 7C           LD      D,$7C               
5699: 7C              LD      A,H                 
569A: 7C              LD      A,H                 
569B: 7C              LD      A,H                 
569C: 7C              LD      A,H                 
569D: 7C              LD      A,H                 
569E: 7C              LD      A,H                 
569F: 7C              LD      A,H                 
56A0: 7C              LD      A,H                 
56A1: 7C              LD      A,H                 
56A2: 7C              LD      A,H                 
56A3: 7C              LD      A,H                 
56A4: 7C              LD      A,H                 
56A5: 7C              LD      A,H                 
56A6: 7C              LD      A,H                 
56A7: 7C              LD      A,H                 
56A8: 17              RLA                         
56A9: 7F              LD      A,A                 
56AA: 98              SBC     B                   
56AB: A0              AND     B                   
56AC: 13              INC     DE                  
56AD: 7F              LD      A,A                 
56AE: 7F              LD      A,A                 
56AF: 06 07           LD      B,$07               
56B1: 7C              LD      A,H                 
56B2: 7C              LD      A,H                 
56B3: 7C              LD      A,H                 
56B4: 7C              LD      A,H                 
56B5: 7C              LD      A,H                 
56B6: 7C              LD      A,H                 
56B7: 7C              LD      A,H                 
56B8: 7C              LD      A,H                 
56B9: 08 09 06        LD      ($0609),SP          
56BC: 07              RLCA                        
56BD: 08 09 7F        LD      ($7F09),SP          ; {}
56C0: 7F              LD      A,A                 
56C1: 98              SBC     B                   
56C2: C0              RET     NZ                  
56C3: 13              INC     DE                  
56C4: 0D              DEC     C                   
56C5: 0E 0F           LD      C,$0F               
56C7: 20 7C           JR      NZ,$5745            ; {}
56C9: 7C              LD      A,H                 
56CA: 7C              LD      A,H                 
56CB: 7C              LD      A,H                 
56CC: 7C              LD      A,H                 
56CD: 7C              LD      A,H                 
56CE: 7C              LD      A,H                 
56CF: 7C              LD      A,H                 
56D0: 17              RLA                         
56D1: 7F              LD      A,A                 
56D2: 7F              LD      A,A                 
56D3: 16 0A           LD      D,$0A               
56D5: 0B              DEC     BC                  
56D6: 0C              INC     C                   
56D7: 0D              DEC     C                   
56D8: 98              SBC     B                   
56D9: E0 13           LD      ($FF00+$13),A       
56DB: 1D              DEC     E                   
56DC: 1E 1F           LD      E,$1F               
56DE: 30 06           JR      NC,$56E6            ; {}
56E0: 07              RLCA                        
56E1: 7C              LD      A,H                 
56E2: 7C              LD      A,H                 
56E3: 7C              LD      A,H                 
56E4: 7C              LD      A,H                 
56E5: 08 09 7F        LD      ($7F09),SP          ; {}
56E8: 7F              LD      A,A                 
56E9: 7F              LD      A,A                 
56EA: 7F              LD      A,A                 
56EB: 1A              LD      A,(DE)              
56EC: 1B              DEC     DE                  
56ED: 1C              INC     E                   
56EE: 1D              DEC     E                   
56EF: 99              SBC     C                   
56F0: 00              NOP                         
56F1: 13              INC     DE                  
56F2: 24              INC     H                   
56F3: 25              DEC     H                   
56F4: 26 27           LD      H,$27               
56F6: 7F              LD      A,A                 
56F7: 16 7C           LD      D,$7C               
56F9: 7C              LD      A,H                 
56FA: 7C              LD      A,H                 
56FB: 7C              LD      A,H                 
56FC: 17              RLA                         
56FD: 7F              LD      A,A                 
56FE: 7F              LD      A,A                 
56FF: 7F              LD      A,A                 
5700: 7F              LD      A,A                 
5701: 7F              LD      A,A                 
5702: 21 22 23        LD      HL,$2322            
5705: 24              INC     H                   
5706: 99              SBC     C                   
5707: 20 13           JR      NZ,$571C            ; {}
5709: 34              INC     (HL)                
570A: 35              DEC     (HL)                
570B: 36 37           LD      (HL),$37            
570D: 50              LD      D,B                 
570E: 51              LD      D,C                 
570F: 50              LD      D,B                 
5710: 51              LD      D,C                 
5711: 50              LD      D,B                 
5712: 51              LD      D,C                 
5713: 50              LD      D,B                 
5714: 51              LD      D,C                 
5715: 50              LD      D,B                 
5716: 51              LD      D,C                 
5717: 50              LD      D,B                 
5718: 51              LD      D,C                 
5719: 31 32 33        LD      SP,$3332            
571C: 34              INC     (HL)                
571D: 99              SBC     C                   
571E: 40              LD      B,B                 
571F: 13              INC     DE                  
5720: 2B              DEC     HL                  
5721: 2C              INC     L                   
5722: 2D              DEC     L                   
5723: 2E 52           LD      L,$52               
5725: 53              LD      D,E                 
5726: 52              LD      D,D                 
5727: 53              LD      D,E                 
5728: 52              LD      D,D                 
5729: 53              LD      D,E                 
572A: 52              LD      D,D                 
572B: 53              LD      D,E                 
572C: 52              LD      D,D                 
572D: 53              LD      D,E                 
572E: 52              LD      D,D                 
572F: 53              LD      D,E                 
5730: 28 29           JR      Z,$575B             ; {}
5732: 2A              LD      A,(HLI)             
5733: 2B              DEC     HL                  
5734: 99              SBC     C                   
5735: 60              LD      H,B                 
5736: 13              INC     DE                  
5737: 3B              DEC     SP                  
5738: 3C              INC     A                   
5739: 54              LD      D,H                 
573A: 55              LD      D,L                 
573B: 54              LD      D,H                 
573C: 55              LD      D,L                 
573D: 54              LD      D,H                 
573E: 55              LD      D,L                 
573F: 54              LD      D,H                 
5740: 55              LD      D,L                 
5741: 54              LD      D,H                 
5742: 55              LD      D,L                 
5743: 54              LD      D,H                 
5744: 55              LD      D,L                 
5745: 54              LD      D,H                 
5746: 55              LD      D,L                 
5747: 54              LD      D,H                 
5748: 55              LD      D,L                 
5749: 3A              LD      A,(HLD)             
574A: 3B              DEC     SP                  
574B: 99              SBC     C                   
574C: 80              ADD     A,B                 
574D: 13              INC     DE                  
574E: 3E 3F           LD      A,$3F               
5750: 56              LD      D,(HL)              
5751: 57              LD      D,A                 
5752: 56              LD      D,(HL)              
5753: 57              LD      D,A                 
5754: 56              LD      D,(HL)              
5755: 57              LD      D,A                 
5756: 56              LD      D,(HL)              
5757: 57              LD      D,A                 
5758: 56              LD      D,(HL)              
5759: 57              LD      D,A                 
575A: 56              LD      D,(HL)              
575B: 57              LD      D,A                 
575C: 56              LD      D,(HL)              
575D: 57              LD      D,A                 
575E: 56              LD      D,(HL)              
575F: 57              LD      D,A                 
5760: 3D              DEC     A                   
5761: 3E 99           LD      A,$99               
5763: A0              AND     B                   
5764: 13              INC     DE                  
5765: 3E 3F           LD      A,$3F               
5767: 00              NOP                         
5768: 01 00 01        LD      BC,$0100            
576B: 00              NOP                         
576C: 01 00 01        LD      BC,$0100            
576F: 00              NOP                         
5770: 01 00 01        LD      BC,$0100            
5773: 00              NOP                         
5774: 01 00 01        LD      BC,$0100            
5777: 3D              DEC     A                   
5778: 3E 99           LD      A,$99               
577A: C0              RET     NZ                  
577B: 13              INC     DE                  
577C: 3E 3F           LD      A,$3F               
577E: 10 11           ;;STOP    $11                 
5780: 10 11           ;;STOP    $11                 
5782: 10 11           ;;STOP    $11                 
5784: 10 11           ;;STOP    $11                 
5786: 10 11           ;;STOP    $11                 
5788: 10 11           ;;STOP    $11                 
578A: 04              INC     B                   
578B: 05              DEC     B                   
578C: 10 11           ;;STOP    $11                 
578E: 3D              DEC     A                   
578F: 3E 99           LD      A,$99               
5791: E0 13           LD      ($FF00+$13),A       
5793: 43              LD      B,E                 
5794: 44              LD      B,H                 
5795: 45              LD      B,L                 
5796: 46              LD      B,(HL)              
5797: 04              INC     B                   
5798: 05              DEC     B                   
5799: 02              LD      (BC),A              
579A: 18 19           JR      $57B5               ; {}
579C: 38 39           JR      C,$57D7             ; {}
579E: 4E              LD      C,(HL)              
579F: 4F              LD      C,A                 
57A0: 03              INC     BC                  
57A1: 14              INC     D                   
57A2: 15              DEC     D                   
57A3: 40              LD      B,B                 
57A4: 41              LD      B,C                 
57A5: 42              LD      B,D                 
57A6: 43              LD      B,E                 
57A7: 9A              SBC     D                   
57A8: 00              NOP                         
57A9: 13              INC     DE                  
57AA: 4A              LD      C,D                 
57AB: 4B              LD      C,E                 
57AC: 4C              LD      C,H                 
57AD: 4D              LD      C,L                 
57AE: 14              INC     D                   
57AF: 15              DEC     D                   
57B0: 12              LD      (DE),A              
57B1: 13              INC     DE                  
57B2: 12              LD      (DE),A              
57B3: 13              INC     DE                  
57B4: 12              LD      (DE),A              
57B5: 13              INC     DE                  
57B6: 12              LD      (DE),A              
57B7: 13              INC     DE                  
57B8: 12              LD      (DE),A              
57B9: 13              INC     DE                  
57BA: 47              LD      B,A                 
57BB: 48              LD      C,B                 
57BC: 49              LD      C,C                 
57BD: 4A              LD      C,D                 
57BE: 9A              SBC     D                   
57BF: 20 13           JR      NZ,$57D4            ; {}
57C1: 12              LD      (DE),A              
57C2: 13              INC     DE                  
57C3: 12              LD      (DE),A              
57C4: 13              INC     DE                  
57C5: 12              LD      (DE),A              
57C6: 13              INC     DE                  
57C7: 12              LD      (DE),A              
57C8: 13              INC     DE                  
57C9: 12              LD      (DE),A              
57CA: 13              INC     DE                  
57CB: 12              LD      (DE),A              
57CC: 13              INC     DE                  
57CD: 12              LD      (DE),A              
57CE: 13              INC     DE                  
57CF: 12              LD      (DE),A              
57D0: 13              INC     DE                  
57D1: 12              LD      (DE),A              
57D2: 13              INC     DE                  
57D3: 12              LD      (DE),A              
57D4: 13              INC     DE                  
57D5: 9A              SBC     D                   
57D6: 40              LD      B,B                 
57D7: 53              LD      D,E                 
57D8: 7C              LD      A,H                 
57D9: 9A              SBC     D                   
57DA: 60              LD      H,B                 
57DB: 53              LD      D,E                 
57DC: 7C              LD      A,H                 
57DD: 9A              SBC     D                   
57DE: 80              ADD     A,B                 
57DF: 53              LD      D,E                 
57E0: 7C              LD      A,H                 
57E1: 9A              SBC     D                   
57E2: A0              AND     B                   
57E3: 53              LD      D,E                 
57E4: 7C              LD      A,H                 
57E5: 9A              SBC     D                   
57E6: C0              RET     NZ                  
57E7: 53              LD      D,E                 
57E8: 7C              LD      A,H                 
57E9: 9A              SBC     D                   
57EA: E0 53           LD      ($FF00+$53),A       
57EC: 7C              LD      A,H                 
57ED: 9B              SBC     E                   
57EE: 00              NOP                         
57EF: 53              LD      D,E                 
57F0: 7C              LD      A,H                 
57F1: 9B              SBC     E                   
57F2: 20 53           JR      NZ,$5847            ; {}
57F4: 7C              LD      A,H                 
57F5: 9B              SBC     E                   
57F6: 40              LD      B,B                 
57F7: 53              LD      D,E                 
57F8: 7C              LD      A,H                 
57F9: 9B              SBC     E                   
57FA: 60              LD      H,B                 
57FB: 53              LD      D,E                 
57FC: 7C              LD      A,H                 
57FD: 9B              SBC     E                   
57FE: 80              ADD     A,B                 
57FF: 53              LD      D,E                 
5800: 7C              LD      A,H                 
5801: 9B              SBC     E                   
5802: A0              AND     B                   
5803: 53              LD      D,E                 
5804: 7C              LD      A,H                 
5805: 9B              SBC     E                   
5806: C0              RET     NZ                  
5807: 53              LD      D,E                 
5808: 7C              LD      A,H                 
5809: 9B              SBC     E                   
580A: E0 53           LD      ($FF00+$53),A       
580C: 7C              LD      A,H                 
580D: 00              NOP                         
580E: 98              SBC     B                   
580F: 00              NOP                         
5810: 13              INC     DE                  
5811: 7F              LD      A,A                 
5812: 7F              LD      A,A                 
5813: 7F              LD      A,A                 
5814: 7F              LD      A,A                 
5815: 7F              LD      A,A                 
5816: 7F              LD      A,A                 
5817: 7F              LD      A,A                 
5818: 7F              LD      A,A                 
5819: 04              INC     B                   
581A: 05              DEC     B                   
581B: 06 07           LD      B,$07               
581D: 7F              LD      A,A                 
581E: 7F              LD      A,A                 
581F: 7F              LD      A,A                 
5820: 7F              LD      A,A                 
5821: 7F              LD      A,A                 
5822: 7F              LD      A,A                 
5823: 7F              LD      A,A                 
5824: 7F              LD      A,A                 
5825: 98              SBC     B                   
5826: 20 13           JR      NZ,$583B            ; {}
5828: 7F              LD      A,A                 
5829: 7F              LD      A,A                 
582A: 7F              LD      A,A                 
582B: 7F              LD      A,A                 
582C: 7F              LD      A,A                 
582D: 7F              LD      A,A                 
582E: 7F              LD      A,A                 
582F: 7F              LD      A,A                 
5830: 30 7F           JR      NC,$58B1            ; {}
5832: 7F              LD      A,A                 
5833: 40              LD      B,B                 
5834: 7F              LD      A,A                 
5835: 7F              LD      A,A                 
5836: 7F              LD      A,A                 
5837: 7F              LD      A,A                 
5838: 7F              LD      A,A                 
5839: 7F              LD      A,A                 
583A: 7F              LD      A,A                 
583B: 7F              LD      A,A                 
583C: 98              SBC     B                   
583D: 40              LD      B,B                 
583E: 13              INC     DE                  
583F: 7F              LD      A,A                 
5840: 7F              LD      A,A                 
5841: 7F              LD      A,A                 
5842: 7F              LD      A,A                 
5843: 7F              LD      A,A                 
5844: 00              NOP                         
5845: 01 02 03        LD      BC,$0302            
5848: 03              INC     BC                  
5849: 01 01 02        LD      BC,$0201            
584C: 08 09 7F        LD      ($7F09),SP          ; {}
584F: 7F              LD      A,A                 
5850: 7F              LD      A,A                 
5851: 7F              LD      A,A                 
5852: 7F              LD      A,A                 
5853: 98              SBC     B                   
5854: 60              LD      H,B                 
5855: 13              INC     DE                  
5856: 7F              LD      A,A                 
5857: 7F              LD      A,A                 
5858: 7F              LD      A,A                 
5859: 7F              LD      A,A                 
585A: 7F              LD      A,A                 
585B: 10 11           ;;STOP    $11                 
585D: 12              LD      (DE),A              
585E: 13              INC     DE                  
585F: 14              INC     D                   
5860: 15              DEC     D                   
5861: 16 17           LD      D,$17               
5863: 18 19           JR      $587E               ; {}
5865: 7F              LD      A,A                 
5866: 7F              LD      A,A                 
5867: 7F              LD      A,A                 
5868: 7F              LD      A,A                 
5869: 7F              LD      A,A                 
586A: 98              SBC     B                   
586B: 80              ADD     A,B                 
586C: 13              INC     DE                  
586D: 7F              LD      A,A                 
586E: 7F              LD      A,A                 
586F: 7F              LD      A,A                 
5870: 7F              LD      A,A                 
5871: 7F              LD      A,A                 
5872: 20 21           JR      NZ,$5895            ; {}
5874: 22              LD      (HLI),A             
5875: 23              INC     HL                  
5876: 24              INC     H                   
5877: 25              DEC     H                   
5878: 26 27           LD      H,$27               
587A: 28 29           JR      Z,$58A5             ; {}
587C: 7F              LD      A,A                 
587D: 7F              LD      A,A                 
587E: 7F              LD      A,A                 
587F: 7F              LD      A,A                 
5880: 7F              LD      A,A                 
5881: 98              SBC     B                   
5882: A0              AND     B                   
5883: 13              INC     DE                  
5884: 7F              LD      A,A                 
5885: 7F              LD      A,A                 
5886: 7F              LD      A,A                 
5887: 7F              LD      A,A                 
5888: 7F              LD      A,A                 
5889: 10 31           ;;STOP    $31                 
588B: 32              LD      (HLD),A             
588C: 33              INC     SP                  
588D: 34              INC     (HL)                
588E: 35              DEC     (HL)                
588F: 36 37           LD      (HL),$37            
5891: 38 39           JR      C,$58CC             ; {}
5893: 7F              LD      A,A                 
5894: 7F              LD      A,A                 
5895: 7F              LD      A,A                 
5896: 7F              LD      A,A                 
5897: 7F              LD      A,A                 
5898: 98              SBC     B                   
5899: C0              RET     NZ                  
589A: 13              INC     DE                  
589B: 7F              LD      A,A                 
589C: 7F              LD      A,A                 
589D: 7F              LD      A,A                 
589E: 7F              LD      A,A                 
589F: 7F              LD      A,A                 
58A0: 20 41           JR      NZ,$58E3            ; {}
58A2: 42              LD      B,D                 
58A3: 43              LD      B,E                 
58A4: 44              LD      B,H                 
58A5: 45              LD      B,L                 
58A6: 46              LD      B,(HL)              
58A7: 47              LD      B,A                 
58A8: 48              LD      C,B                 
58A9: 49              LD      C,C                 
58AA: 7F              LD      A,A                 
58AB: 7F              LD      A,A                 
58AC: 7F              LD      A,A                 
58AD: 7F              LD      A,A                 
58AE: 7F              LD      A,A                 
58AF: 98              SBC     B                   
58B0: E0 13           LD      ($FF00+$13),A       
58B2: 7F              LD      A,A                 
58B3: 7F              LD      A,A                 
58B4: 7F              LD      A,A                 
58B5: 7F              LD      A,A                 
58B6: 7F              LD      A,A                 
58B7: 50              LD      D,B                 
58B8: 51              LD      D,C                 
58B9: 52              LD      D,D                 
58BA: 53              LD      D,E                 
58BB: 54              LD      D,H                 
58BC: 55              LD      D,L                 
58BD: 56              LD      D,(HL)              
58BE: 57              LD      D,A                 
58BF: 58              LD      E,B                 
58C0: 59              LD      E,C                 
58C1: 7F              LD      A,A                 
58C2: 7F              LD      A,A                 
58C3: 7F              LD      A,A                 
58C4: 7F              LD      A,A                 
58C5: 7F              LD      A,A                 
58C6: 99              SBC     C                   
58C7: 00              NOP                         
58C8: 13              INC     DE                  
58C9: 7F              LD      A,A                 
58CA: 7F              LD      A,A                 
58CB: 7F              LD      A,A                 
58CC: 7F              LD      A,A                 
58CD: 7F              LD      A,A                 
58CE: 60              LD      H,B                 
58CF: 61              LD      H,C                 
58D0: 62              LD      H,D                 
58D1: 63              LD      H,E                 
58D2: 45              LD      B,L                 
58D3: 65              LD      H,L                 
58D4: 66              LD      H,(HL)              
58D5: 67              LD      H,A                 
58D6: 68              LD      L,B                 
58D7: 69              LD      L,C                 
58D8: 7F              LD      A,A                 
58D9: 7F              LD      A,A                 
58DA: 7F              LD      A,A                 
58DB: 7F              LD      A,A                 
58DC: 7F              LD      A,A                 
58DD: 99              SBC     C                   
58DE: 20 13           JR      NZ,$58F3            ; {}
58E0: 7F              LD      A,A                 
58E1: 7F              LD      A,A                 
58E2: 7F              LD      A,A                 
58E3: 7F              LD      A,A                 
58E4: 7F              LD      A,A                 
58E5: 70              LD      (HL),B              
58E6: 71              LD      (HL),C              
58E7: 72              LD      (HL),D              
58E8: 73              LD      (HL),E              
58E9: 75              LD      (HL),L              
58EA: 75              LD      (HL),L              
58EB: 76              HALT                        
58EC: 77              LD      (HL),A              
58ED: 78              LD      A,B                 
58EE: 79              LD      A,C                 
58EF: 7F              LD      A,A                 
58F0: 7F              LD      A,A                 
58F1: 7F              LD      A,A                 
58F2: 7F              LD      A,A                 
58F3: 7F              LD      A,A                 
58F4: 99              SBC     C                   
58F5: 40              LD      B,B                 
58F6: 13              INC     DE                  
58F7: 7F              LD      A,A                 
58F8: 7F              LD      A,A                 
58F9: 7F              LD      A,A                 
58FA: 7F              LD      A,A                 
58FB: 7F              LD      A,A                 
58FC: 0A              LD      A,(BC)              
58FD: 0B              DEC     BC                  
58FE: 0C              INC     C                   
58FF: 0D              DEC     C                   
5900: 0E 0F           LD      C,$0F               
5902: 77              LD      (HL),A              
5903: 4B              LD      C,E                 
5904: 4C              LD      C,H                 
5905: 4D              LD      C,L                 
5906: 7F              LD      A,A                 
5907: 7F              LD      A,A                 
5908: 7F              LD      A,A                 
5909: 7F              LD      A,A                 
590A: 7F              LD      A,A                 
590B: 99              SBC     C                   
590C: 60              LD      H,B                 
590D: 13              INC     DE                  
590E: 7F              LD      A,A                 
590F: 7F              LD      A,A                 
5910: 7F              LD      A,A                 
5911: 7F              LD      A,A                 
5912: 7F              LD      A,A                 
5913: 1A              LD      A,(DE)              
5914: 1B              DEC     DE                  
5915: 1C              INC     E                   
5916: 1D              DEC     E                   
5917: 1E 1F           LD      E,$1F               
5919: 5A              LD      E,D                 
591A: 5B              LD      E,E                 
591B: 5C              LD      E,H                 
591C: 5D              LD      E,L                 
591D: 7F              LD      A,A                 
591E: 7F              LD      A,A                 
591F: 7F              LD      A,A                 
5920: 7F              LD      A,A                 
5921: 7F              LD      A,A                 
5922: 99              SBC     C                   
5923: 80              ADD     A,B                 
5924: 13              INC     DE                  
5925: 7F              LD      A,A                 
5926: 7F              LD      A,A                 
5927: 7F              LD      A,A                 
5928: 7F              LD      A,A                 
5929: 7F              LD      A,A                 
592A: 2A              LD      A,(HLI)             
592B: 2B              DEC     HL                  
592C: 2C              INC     L                   
592D: 2D              DEC     L                   
592E: 2E 2F           LD      L,$2F               
5930: 6A              LD      L,D                 
5931: 6B              LD      L,E                 
5932: 1B              DEC     DE                  
5933: 6D              LD      L,L                 
5934: 7F              LD      A,A                 
5935: 7F              LD      A,A                 
5936: 7F              LD      A,A                 
5937: 7F              LD      A,A                 
5938: 7F              LD      A,A                 
5939: 99              SBC     C                   
593A: A0              AND     B                   
593B: 13              INC     DE                  
593C: 7F              LD      A,A                 
593D: 7F              LD      A,A                 
593E: 7F              LD      A,A                 
593F: 7F              LD      A,A                 
5940: 7F              LD      A,A                 
5941: 3A              LD      A,(HLD)             
5942: 3B              DEC     SP                  
5943: 3C              INC     A                   
5944: 3D              DEC     A                   
5945: 3E 3F           LD      A,$3F               
5947: 7A              LD      A,D                 
5948: 7B              LD      A,E                 
5949: 7C              LD      A,H                 
594A: 7D              LD      A,L                 
594B: 7F              LD      A,A                 
594C: 7F              LD      A,A                 
594D: 7F              LD      A,A                 
594E: 7F              LD      A,A                 
594F: 7F              LD      A,A                 
5950: 99              SBC     C                   
5951: C0              RET     NZ                  
5952: 13              INC     DE                  
5953: 7F              LD      A,A                 
5954: 7F              LD      A,A                 
5955: 7F              LD      A,A                 
5956: 7F              LD      A,A                 
5957: 6E              LD      L,(HL)              
5958: 4A              LD      C,D                 
5959: 64              LD      H,H                 
595A: 64              LD      H,H                 
595B: 6C              LD      L,H                 
595C: 64              LD      H,H                 
595D: 4A              LD      C,D                 
595E: 4A              LD      C,D                 
595F: 6C              LD      L,H                 
5960: 4A              LD      C,D                 
5961: 64              LD      H,H                 
5962: 6F              LD      L,A                 
5963: 7F              LD      A,A                 
5964: 7F              LD      A,A                 
5965: 7F              LD      A,A                 
5966: 7F              LD      A,A                 
5967: 99              SBC     C                   
5968: E0 13           LD      ($FF00+$13),A       
596A: 7F              LD      A,A                 
596B: 7F              LD      A,A                 
596C: 7F              LD      A,A                 
596D: 7F              LD      A,A                 
596E: 7F              LD      A,A                 
596F: 7F              LD      A,A                 
5970: 04              INC     B                   
5971: 05              DEC     B                   
5972: 7F              LD      A,A                 
5973: 4E              LD      C,(HL)              
5974: 4F              LD      C,A                 
5975: 7F              LD      A,A                 
5976: 06 07           LD      B,$07               
5978: 7F              LD      A,A                 
5979: 7F              LD      A,A                 
597A: 7F              LD      A,A                 
597B: 7F              LD      A,A                 
597C: 7F              LD      A,A                 
597D: 7F              LD      A,A                 
597E: 9A              SBC     D                   
597F: 00              NOP                         
5980: 13              INC     DE                  
5981: 7F              LD      A,A                 
5982: 7F              LD      A,A                 
5983: 7F              LD      A,A                 
5984: 7F              LD      A,A                 
5985: 7F              LD      A,A                 
5986: 7F              LD      A,A                 
5987: 30 7F           JR      NC,$5A08            ; {}
5989: 7F              LD      A,A                 
598A: 4E              LD      C,(HL)              
598B: 4F              LD      C,A                 
598C: 7F              LD      A,A                 
598D: 7F              LD      A,A                 
598E: 40              LD      B,B                 
598F: 7F              LD      A,A                 
5990: 7F              LD      A,A                 
5991: 7F              LD      A,A                 
5992: 7F              LD      A,A                 
5993: 7F              LD      A,A                 
5994: 7F              LD      A,A                 
5995: 9A              SBC     D                   
5996: 20 13           JR      NZ,$59AB            ; {}
5998: 7F              LD      A,A                 
5999: 7F              LD      A,A                 
599A: 7F              LD      A,A                 
599B: 7F              LD      A,A                 
599C: 7F              LD      A,A                 
599D: 7F              LD      A,A                 
599E: 40              LD      B,B                 
599F: 7F              LD      A,A                 
59A0: 7F              LD      A,A                 
59A1: 5E              LD      E,(HL)              
59A2: 5F              LD      E,A                 
59A3: 7F              LD      A,A                 
59A4: 7F              LD      A,A                 
59A5: 30 7F           JR      NC,$5A26            ; {}
59A7: 7F              LD      A,A                 
59A8: 7F              LD      A,A                 
59A9: 7F              LD      A,A                 
59AA: 7F              LD      A,A                 
59AB: 7F              LD      A,A                 
59AC: 00              NOP                         
59AD: 9B              SBC     E                   
59AE: E0 53           LD      ($FF00+$53),A       
59B0: 7C              LD      A,H                 
59B1: 98              SBC     B                   
59B2: 00              NOP                         
59B3: 53              LD      D,E                 
59B4: 7C              LD      A,H                 
59B5: 98              SBC     B                   
59B6: 20 53           JR      NZ,$5A0B            ; {}
59B8: 7C              LD      A,H                 
59B9: 98              SBC     B                   
59BA: 40              LD      B,B                 
59BB: 53              LD      D,E                 
59BC: 7C              LD      A,H                 
59BD: 98              SBC     B                   
59BE: 60              LD      H,B                 
59BF: 53              LD      D,E                 
59C0: 7C              LD      A,H                 
59C1: 98              SBC     B                   
59C2: 80              ADD     A,B                 
59C3: 53              LD      D,E                 
59C4: 7C              LD      A,H                 
59C5: 98              SBC     B                   
59C6: A0              AND     B                   
59C7: 53              LD      D,E                 
59C8: 7C              LD      A,H                 
59C9: 98              SBC     B                   
59CA: C0              RET     NZ                  
59CB: 53              LD      D,E                 
59CC: 7C              LD      A,H                 
59CD: 98              SBC     B                   
59CE: C0              RET     NZ                  
59CF: 03              INC     BC                  
59D0: 2A              LD      A,(HLI)             
59D1: 2B              DEC     HL                  
59D2: 04              INC     B                   
59D3: 14              INC     D                   
59D4: 98              SBC     B                   
59D5: CE 03           ADC     $03                 
59D7: 2A              LD      A,(HLI)             
59D8: 2B              DEC     HL                  
59D9: 04              INC     B                   
59DA: 14              INC     D                   
59DB: 98              SBC     B                   
59DC: E0 53           LD      ($FF00+$53),A       
59DE: 7C              LD      A,H                 
59DF: 98              SBC     B                   
59E0: E0 03           LD      ($FF00+$03),A       
59E2: 39              ADD     HL,SP               
59E3: 7F              LD      A,A                 
59E4: 7F              LD      A,A                 
59E5: 1E 98           LD      E,$98               
59E7: EE 05           XOR     $05                 
59E9: 39              ADD     HL,SP               
59EA: 7F              LD      A,A                 
59EB: 7F              LD      A,A                 
59EC: 1E 3A           LD      E,$3A               
59EE: 3B              DEC     SP                  
59EF: 99              SBC     C                   
59F0: 00              NOP                         
59F1: 13              INC     DE                  
59F2: 7F              LD      A,A                 
59F3: 7F              LD      A,A                 
59F4: 7F              LD      A,A                 
59F5: 7F              LD      A,A                 
59F6: 04              INC     B                   
59F7: 14              INC     D                   
59F8: 7C              LD      A,H                 
59F9: 7C              LD      A,H                 
59FA: 2A              LD      A,(HLI)             
59FB: 2B              DEC     HL                  
59FC: 04              INC     B                   
59FD: 14              INC     D                   
59FE: 2A              LD      A,(HLI)             
59FF: 2B              DEC     HL                  
5A00: 7F              LD      A,A                 
5A01: 7F              LD      A,A                 
5A02: 7F              LD      A,A                 
5A03: 7F              LD      A,A                 
5A04: 7F              LD      A,A                 
5A05: 7F              LD      A,A                 
5A06: 99              SBC     C                   
5A07: 20 53           JR      NZ,$5A5C            ; {}
5A09: 7F              LD      A,A                 
5A0A: 99              SBC     C                   
5A0B: 25              DEC     H                   
5A0C: 03              INC     BC                  
5A0D: 1E 3A           LD      E,$3A               
5A0F: 3B              DEC     SP                  
5A10: 39              ADD     HL,SP               
5A11: 99              SBC     C                   
5A12: 2B              DEC     HL                  
5A13: 01 1E 39        LD      BC,$391E            
5A16: 99              SBC     C                   
5A17: 40              LD      B,B                 
5A18: 53              LD      D,E                 
5A19: 7F              LD      A,A                 
5A1A: 99              SBC     C                   
5A1B: 60              LD      H,B                 
5A1C: 53              LD      D,E                 
5A1D: 7F              LD      A,A                 
5A1E: 99              SBC     C                   
5A1F: 80              ADD     A,B                 
5A20: 53              LD      D,E                 
5A21: 7F              LD      A,A                 
5A22: 99              SBC     C                   
5A23: A0              AND     B                   
5A24: 53              LD      D,E                 
5A25: 7F              LD      A,A                 
5A26: 99              SBC     C                   
5A27: C0              RET     NZ                  
5A28: 53              LD      D,E                 
5A29: 7F              LD      A,A                 
5A2A: 99              SBC     C                   
5A2B: E0 53           LD      ($FF00+$53),A       
5A2D: 7F              LD      A,A                 
5A2E: 9A              SBC     D                   
5A2F: 00              NOP                         
5A30: 53              LD      D,E                 
5A31: 7F              LD      A,A                 
5A32: 9A              SBC     D                   
5A33: 20 53           JR      NZ,$5A88            ; {}
5A35: 7F              LD      A,A                 
5A36: 99              SBC     C                   
5A37: 86              ADD     A,(HL)              
5A38: 07              RLCA                        
5A39: 24              INC     H                   
5A3A: 25              DEC     H                   
5A3B: 26 26           LD      H,$26               
5A3D: 29              ADD     HL,HL               
5A3E: 29              ADD     HL,HL               
5A3F: 27              DAA                         
5A40: 28 99           JR      Z,$59DB             ; {}
5A42: A7              AND     A                   
5A43: 05              DEC     B                   
5A44: 34              INC     (HL)                
5A45: 35              DEC     (HL)                
5A46: 36 36           LD      (HL),$36            
5A48: 37              SCF                         
5A49: 38 99           JR      C,$59E4             ; {}
5A4B: C7              RST     0X00                
5A4C: 05              DEC     B                   
5A4D: 24              INC     H                   
5A4E: 25              DEC     H                   
5A4F: 26 26           LD      H,$26               
5A51: 27              DAA                         
5A52: 28 99           JR      Z,$59ED             ; {}
5A54: E7              RST     0X20                
5A55: 05              DEC     B                   
5A56: 24              INC     H                   
5A57: 25              DEC     H                   
5A58: 26 26           LD      H,$26               
5A5A: 27              DAA                         
5A5B: 28 9A           JR      Z,$59F7             ; {}
5A5D: 06 07           LD      B,$07               
5A5F: 24              INC     H                   
5A60: 25              DEC     H                   
5A61: 26 26           LD      H,$26               
5A63: 29              ADD     HL,HL               
5A64: 29              ADD     HL,HL               
5A65: 27              DAA                         
5A66: 28 9A           JR      Z,$5A02             ; {}
5A68: 26 07           LD      H,$07               
5A6A: 24              INC     H                   
5A6B: 25              DEC     H                   
5A6C: 26 26           LD      H,$26               
5A6E: 29              ADD     HL,HL               
5A6F: 29              ADD     HL,HL               
5A70: 27              DAA                         
5A71: 28 00           JR      Z,$5A73             ; {}
5A73: 99              SBC     C                   
5A74: E0 13           LD      ($FF00+$13),A       
5A76: 1B              DEC     DE                  
5A77: 1B              DEC     DE                  
5A78: 48              LD      C,B                 
5A79: 49              LD      C,C                 
5A7A: 30 31           JR      NC,$5AAD            ; {}
5A7C: 32              LD      (HLD),A             
5A7D: 33              INC     SP                  
5A7E: 7F              LD      A,A                 
5A7F: 5A              LD      E,D                 
5A80: 74              LD      (HL),H              
5A81: 74              LD      (HL),H              
5A82: 7F              LD      A,A                 
5A83: 5A              LD      E,D                 
5A84: 30 31           JR      NC,$5AB7            ; {}
5A86: 32              LD      (HLD),A             
5A87: 33              INC     SP                  
5A88: 30 31           JR      NC,$5ABB            ; {}
5A8A: 98              SBC     B                   
5A8B: 00              NOP                         
5A8C: 13              INC     DE                  
5A8D: 1B              DEC     DE                  
5A8E: 1B              DEC     DE                  
5A8F: 48              LD      C,B                 
5A90: 49              LD      C,C                 
5A91: 1A              LD      A,(DE)              
5A92: 5A              LD      E,D                 
5A93: 5A              LD      E,D                 
5A94: 7F              LD      A,A                 
5A95: 5A              LD      E,D                 
5A96: 7F              LD      A,A                 
5A97: 5A              LD      E,D                 
5A98: 7F              LD      A,A                 
5A99: 5A              LD      E,D                 
5A9A: 7F              LD      A,A                 
5A9B: 74              LD      (HL),H              
5A9C: 74              LD      (HL),H              
5A9D: 5A              LD      E,D                 
5A9E: 7F              LD      A,A                 
5A9F: 24              INC     H                   
5AA0: 25              DEC     H                   
5AA1: 98              SBC     B                   
5AA2: 20 13           JR      NZ,$5AB7            ; {}
5AA4: 1B              DEC     DE                  
5AA5: 1B              DEC     DE                  
5AA6: 48              LD      C,B                 
5AA7: 49              LD      C,C                 
5AA8: 5A              LD      E,D                 
5AA9: 1A              LD      A,(DE)              
5AAA: 7F              LD      A,A                 
5AAB: 5A              LD      E,D                 
5AAC: 7F              LD      A,A                 
5AAD: 5A              LD      E,D                 
5AAE: 7F              LD      A,A                 
5AAF: 5A              LD      E,D                 
5AB0: 7F              LD      A,A                 
5AB1: 5A              LD      E,D                 
5AB2: 74              LD      (HL),H              
5AB3: 74              LD      (HL),H              
5AB4: 7F              LD      A,A                 
5AB5: 5A              LD      E,D                 
5AB6: 34              INC     (HL)                
5AB7: 35              DEC     (HL)                
5AB8: 98              SBC     B                   
5AB9: 40              LD      B,B                 
5ABA: 13              INC     DE                  
5ABB: 1B              DEC     DE                  
5ABC: 1B              DEC     DE                  
5ABD: 48              LD      C,B                 
5ABE: 49              LD      C,C                 
5ABF: 5E              LD      E,(HL)              
5AC0: 5E              LD      E,(HL)              
5AC1: 5E              LD      E,(HL)              
5AC2: 5E              LD      E,(HL)              
5AC3: 5E              LD      E,(HL)              
5AC4: 5E              LD      E,(HL)              
5AC5: 5A              LD      E,D                 
5AC6: 7F              LD      A,A                 
5AC7: 5A              LD      E,D                 
5AC8: 7F              LD      A,A                 
5AC9: 74              LD      (HL),H              
5ACA: 74              LD      (HL),H              
5ACB: 5A              LD      E,D                 
5ACC: 7F              LD      A,A                 
5ACD: 20 21           JR      NZ,$5AF0            ; {}
5ACF: 98              SBC     B                   
5AD0: 60              LD      H,B                 
5AD1: 13              INC     DE                  
5AD2: 1B              DEC     DE                  
5AD3: 1B              DEC     DE                  
5AD4: 48              LD      C,B                 
5AD5: 49              LD      C,C                 
5AD6: 5F              LD      E,A                 
5AD7: 5F              LD      E,A                 
5AD8: 5F              LD      E,A                 
5AD9: 5F              LD      E,A                 
5ADA: 5F              LD      E,A                 
5ADB: 5F              LD      E,A                 
5ADC: 7F              LD      A,A                 
5ADD: 5A              LD      E,D                 
5ADE: 7F              LD      A,A                 
5ADF: 5A              LD      E,D                 
5AE0: 74              LD      (HL),H              
5AE1: 74              LD      (HL),H              
5AE2: 7F              LD      A,A                 
5AE3: 5A              LD      E,D                 
5AE4: 30 31           JR      NC,$5B17            ; {}
5AE6: 98              SBC     B                   
5AE7: 80              ADD     A,B                 
5AE8: 13              INC     DE                  
5AE9: 1B              DEC     DE                  
5AEA: 1B              DEC     DE                  
5AEB: 48              LD      C,B                 
5AEC: 49              LD      C,C                 
5AED: 2C              INC     L                   
5AEE: 2D              DEC     L                   
5AEF: 2E 2F           LD      L,$2F               
5AF1: 2C              INC     L                   
5AF2: 2D              DEC     L                   
5AF3: 5A              LD      E,D                 
5AF4: 7F              LD      A,A                 
5AF5: 5A              LD      E,D                 
5AF6: 7F              LD      A,A                 
5AF7: 74              LD      (HL),H              
5AF8: 74              LD      (HL),H              
5AF9: 5A              LD      E,D                 
5AFA: 7F              LD      A,A                 
5AFB: 24              INC     H                   
5AFC: 25              DEC     H                   
5AFD: 98              SBC     B                   
5AFE: A0              AND     B                   
5AFF: 13              INC     DE                  
5B00: 1B              DEC     DE                  
5B01: 1B              DEC     DE                  
5B02: 48              LD      C,B                 
5B03: 49              LD      C,C                 
5B04: 3C              INC     A                   
5B05: 3D              DEC     A                   
5B06: 3E 3F           LD      A,$3F               
5B08: 3C              INC     A                   
5B09: 3D              DEC     A                   
5B0A: 7F              LD      A,A                 
5B0B: 5A              LD      E,D                 
5B0C: 7F              LD      A,A                 
5B0D: 5A              LD      E,D                 
5B0E: 74              LD      (HL),H              
5B0F: 74              LD      (HL),H              
5B10: 7F              LD      A,A                 
5B11: 5A              LD      E,D                 
5B12: 34              INC     (HL)                
5B13: 35              DEC     (HL)                
5B14: 98              SBC     B                   
5B15: C0              RET     NZ                  
5B16: 13              INC     DE                  
5B17: 1B              DEC     DE                  
5B18: 1B              DEC     DE                  
5B19: 48              LD      C,B                 
5B1A: 49              LD      C,C                 
5B1B: 5A              LD      E,D                 
5B1C: 7F              LD      A,A                 
5B1D: 5A              LD      E,D                 
5B1E: 7F              LD      A,A                 
5B1F: 5A              LD      E,D                 
5B20: 7F              LD      A,A                 
5B21: 5A              LD      E,D                 
5B22: 7F              LD      A,A                 
5B23: 74              LD      (HL),H              
5B24: 74              LD      (HL),H              
5B25: 74              LD      (HL),H              
5B26: 74              LD      (HL),H              
5B27: 1A              LD      A,(DE)              
5B28: 5A              LD      E,D                 
5B29: 20 21           JR      NZ,$5B4C            ; {}
5B2B: 98              SBC     B                   
5B2C: E0 13           LD      ($FF00+$13),A       
5B2E: 1B              DEC     DE                  
5B2F: 1B              DEC     DE                  
5B30: 48              LD      C,B                 
5B31: 49              LD      C,C                 
5B32: 7F              LD      A,A                 
5B33: 5A              LD      E,D                 
5B34: 7F              LD      A,A                 
5B35: 5A              LD      E,D                 
5B36: 7F              LD      A,A                 
5B37: 5A              LD      E,D                 
5B38: 7F              LD      A,A                 
5B39: 5A              LD      E,D                 
5B3A: 74              LD      (HL),H              
5B3B: 74              LD      (HL),H              
5B3C: 74              LD      (HL),H              
5B3D: 74              LD      (HL),H              
5B3E: 5A              LD      E,D                 
5B3F: 1A              LD      A,(DE)              
5B40: 30 31           JR      NC,$5B73            ; {}
5B42: 99              SBC     C                   
5B43: 00              NOP                         
5B44: 13              INC     DE                  
5B45: 1B              DEC     DE                  
5B46: 1B              DEC     DE                  
5B47: 48              LD      C,B                 
5B48: 49              LD      C,C                 
5B49: 5A              LD      E,D                 
5B4A: 7F              LD      A,A                 
5B4B: 5A              LD      E,D                 
5B4C: 7F              LD      A,A                 
5B4D: 5A              LD      E,D                 
5B4E: 7F              LD      A,A                 
5B4F: 74              LD      (HL),H              
5B50: 74              LD      (HL),H              
5B51: 74              LD      (HL),H              
5B52: 74              LD      (HL),H              
5B53: 5A              LD      E,D                 
5B54: 7F              LD      A,A                 
5B55: 14              INC     D                   
5B56: 16 24           LD      D,$24               
5B58: 25              DEC     H                   
5B59: 99              SBC     C                   
5B5A: 20 13           JR      NZ,$5B6F            ; {}
5B5C: 1B              DEC     DE                  
5B5D: 1B              DEC     DE                  
5B5E: 48              LD      C,B                 
5B5F: 49              LD      C,C                 
5B60: 7F              LD      A,A                 
5B61: 5A              LD      E,D                 
5B62: 7F              LD      A,A                 
5B63: 5A              LD      E,D                 
5B64: 7F              LD      A,A                 
5B65: 5A              LD      E,D                 
5B66: 74              LD      (HL),H              
5B67: 74              LD      (HL),H              
5B68: 74              LD      (HL),H              
5B69: 74              LD      (HL),H              
5B6A: 7F              LD      A,A                 
5B6B: 5A              LD      E,D                 
5B6C: 15              DEC     D                   
5B6D: 17              RLA                         
5B6E: 34              INC     (HL)                
5B6F: 35              DEC     (HL)                
5B70: 99              SBC     C                   
5B71: 40              LD      B,B                 
5B72: 13              INC     DE                  
5B73: 1B              DEC     DE                  
5B74: 1B              DEC     DE                  
5B75: 48              LD      C,B                 
5B76: 49              LD      C,C                 
5B77: 5A              LD      E,D                 
5B78: 7F              LD      A,A                 
5B79: 5A              LD      E,D                 
5B7A: 7F              LD      A,A                 
5B7B: 5A              LD      E,D                 
5B7C: 7F              LD      A,A                 
5B7D: 74              LD      (HL),H              
5B7E: 74              LD      (HL),H              
5B7F: 5A              LD      E,D                 
5B80: 7F              LD      A,A                 
5B81: 5A              LD      E,D                 
5B82: 7F              LD      A,A                 
5B83: 14              INC     D                   
5B84: 16 20           LD      D,$20               
5B86: 21 99 60        LD      HL,$6099            
5B89: 13              INC     DE                  
5B8A: 1B              DEC     DE                  
5B8B: 1B              DEC     DE                  
5B8C: 48              LD      C,B                 
5B8D: 49              LD      C,C                 
5B8E: 7F              LD      A,A                 
5B8F: 5A              LD      E,D                 
5B90: 7F              LD      A,A                 
5B91: 5A              LD      E,D                 
5B92: 7F              LD      A,A                 
5B93: 5A              LD      E,D                 
5B94: 74              LD      (HL),H              
5B95: 74              LD      (HL),H              
5B96: 7F              LD      A,A                 
5B97: 5A              LD      E,D                 
5B98: 7F              LD      A,A                 
5B99: 5A              LD      E,D                 
5B9A: 15              DEC     D                   
5B9B: 17              RLA                         
5B9C: 30 31           JR      NC,$5BCF            ; {}
5B9E: 99              SBC     C                   
5B9F: 80              ADD     A,B                 
5BA0: 13              INC     DE                  
5BA1: 1B              DEC     DE                  
5BA2: 1B              DEC     DE                  
5BA3: 48              LD      C,B                 
5BA4: 49              LD      C,C                 
5BA5: 5A              LD      E,D                 
5BA6: 7F              LD      A,A                 
5BA7: 5A              LD      E,D                 
5BA8: 7F              LD      A,A                 
5BA9: 5A              LD      E,D                 
5BAA: 7F              LD      A,A                 
5BAB: 74              LD      (HL),H              
5BAC: 74              LD      (HL),H              
5BAD: 5A              LD      E,D                 
5BAE: 7F              LD      A,A                 
5BAF: 5A              LD      E,D                 
5BB0: 7F              LD      A,A                 
5BB1: 20 21           JR      NZ,$5BD4            ; {}
5BB3: 22              LD      (HLI),A             
5BB4: 29              ADD     HL,HL               
5BB5: 99              SBC     C                   
5BB6: A0              AND     B                   
5BB7: 13              INC     DE                  
5BB8: 1B              DEC     DE                  
5BB9: 1B              DEC     DE                  
5BBA: 48              LD      C,B                 
5BBB: 49              LD      C,C                 
5BBC: 7F              LD      A,A                 
5BBD: 5A              LD      E,D                 
5BBE: 7F              LD      A,A                 
5BBF: 5A              LD      E,D                 
5BC0: 7F              LD      A,A                 
5BC1: 5A              LD      E,D                 
5BC2: 74              LD      (HL),H              
5BC3: 74              LD      (HL),H              
5BC4: 7F              LD      A,A                 
5BC5: 5A              LD      E,D                 
5BC6: 7F              LD      A,A                 
5BC7: 5A              LD      E,D                 
5BC8: 30 31           JR      NC,$5BFB            ; {}
5BCA: 32              LD      (HLD),A             
5BCB: 33              INC     SP                  
5BCC: 99              SBC     C                   
5BCD: C0              RET     NZ                  
5BCE: 13              INC     DE                  
5BCF: 1B              DEC     DE                  
5BD0: 1B              DEC     DE                  
5BD1: 48              LD      C,B                 
5BD2: 49              LD      C,C                 
5BD3: 20 21           JR      NZ,$5BF6            ; {}
5BD5: 22              LD      (HLI),A             
5BD6: 23              INC     HL                  
5BD7: 5A              LD      E,D                 
5BD8: 7F              LD      A,A                 
5BD9: 74              LD      (HL),H              
5BDA: 74              LD      (HL),H              
5BDB: 5A              LD      E,D                 
5BDC: 7F              LD      A,A                 
5BDD: 20 21           JR      NZ,$5C00            ; {}
5BDF: 22              LD      (HLI),A             
5BE0: 29              ADD     HL,HL               
5BE1: 28 21           JR      Z,$5C04             ; {}
5BE3: 99              SBC     C                   
5BE4: E0 13           LD      ($FF00+$13),A       
5BE6: 1B              DEC     DE                  
5BE7: 1B              DEC     DE                  
5BE8: 48              LD      C,B                 
5BE9: 49              LD      C,C                 
5BEA: 30 31           JR      NC,$5C1D            ; {}
5BEC: 32              LD      (HLD),A             
5BED: 33              INC     SP                  
5BEE: 7F              LD      A,A                 
5BEF: 5A              LD      E,D                 
5BF0: 74              LD      (HL),H              
5BF1: 74              LD      (HL),H              
5BF2: 7F              LD      A,A                 
5BF3: 5A              LD      E,D                 
5BF4: 30 31           JR      NC,$5C27            ; {}
5BF6: 32              LD      (HLD),A             
5BF7: 33              INC     SP                  
5BF8: 30 31           JR      NC,$5C2B            ; {}
5BFA: 9A              SBC     D                   
5BFB: 00              NOP                         
5BFC: 13              INC     DE                  
5BFD: 1B              DEC     DE                  
5BFE: 1B              DEC     DE                  
5BFF: 48              LD      C,B                 
5C00: 49              LD      C,C                 
5C01: 24              INC     H                   
5C02: 25              DEC     H                   
5C03: 26 27           LD      H,$27               
5C05: 5A              LD      E,D                 
5C06: 7F              LD      A,A                 
5C07: 74              LD      (HL),H              
5C08: 74              LD      (HL),H              
5C09: 5A              LD      E,D                 
5C0A: 7F              LD      A,A                 
5C0B: 24              INC     H                   
5C0C: 25              DEC     H                   
5C0D: 28 21           JR      Z,$5C30             ; {}
5C0F: 22              LD      (HLI),A             
5C10: 29              ADD     HL,HL               
5C11: 9A              SBC     D                   
5C12: 20 13           JR      NZ,$5C27            ; {}
5C14: 1B              DEC     DE                  
5C15: 1B              DEC     DE                  
5C16: 48              LD      C,B                 
5C17: 49              LD      C,C                 
5C18: 34              INC     (HL)                
5C19: 35              DEC     (HL)                
5C1A: 36 37           LD      (HL),$37            
5C1C: 7F              LD      A,A                 
5C1D: 5A              LD      E,D                 
5C1E: 74              LD      (HL),H              
5C1F: 74              LD      (HL),H              
5C20: 7F              LD      A,A                 
5C21: 5A              LD      E,D                 
5C22: 34              INC     (HL)                
5C23: 35              DEC     (HL)                
5C24: 30 31           JR      NC,$5C57            ; {}
5C26: 32              LD      (HLD),A             
5C27: 33              INC     SP                  
5C28: 00              NOP                         
5C29: 98              SBC     B                   
5C2A: 00              NOP                         
5C2B: 13              INC     DE                  
5C2C: 26 27           LD      H,$27               
5C2E: 5A              LD      E,D                 
5C2F: 7F              LD      A,A                 
5C30: 44              LD      B,H                 
5C31: 56              LD      D,(HL)              
5C32: 55              LD      D,L                 
5C33: 56              LD      D,(HL)              
5C34: 55              LD      D,L                 
5C35: 56              LD      D,(HL)              
5C36: 55              LD      D,L                 
5C37: 56              LD      D,(HL)              
5C38: 55              LD      D,L                 
5C39: 56              LD      D,(HL)              
5C3A: 55              LD      D,L                 
5C3B: 56              LD      D,(HL)              
5C3C: 55              LD      D,L                 
5C3D: 56              LD      D,(HL)              
5C3E: 55              LD      D,L                 
5C3F: 56              LD      D,(HL)              
5C40: 98              SBC     B                   
5C41: 20 13           JR      NZ,$5C56            ; {}
5C43: 36 37           LD      (HL),$37            
5C45: 7F              LD      A,A                 
5C46: 5A              LD      E,D                 
5C47: 54              LD      D,H                 
5C48: 56              LD      D,(HL)              
5C49: 55              LD      D,L                 
5C4A: 56              LD      D,(HL)              
5C4B: 55              LD      D,L                 
5C4C: 56              LD      D,(HL)              
5C4D: 55              LD      D,L                 
5C4E: 56              LD      D,(HL)              
5C4F: 55              LD      D,L                 
5C50: 56              LD      D,(HL)              
5C51: 55              LD      D,L                 
5C52: 56              LD      D,(HL)              
5C53: 55              LD      D,L                 
5C54: 56              LD      D,(HL)              
5C55: 55              LD      D,L                 
5C56: 56              LD      D,(HL)              
5C57: 98              SBC     B                   
5C58: 40              LD      B,B                 
5C59: 13              INC     DE                  
5C5A: 22              LD      (HLI),A             
5C5B: 23              INC     HL                  
5C5C: 5A              LD      E,D                 
5C5D: 7F              LD      A,A                 
5C5E: 5A              LD      E,D                 
5C5F: 7F              LD      A,A                 
5C60: EF              RST     0X28                
5C61: EF              RST     0X28                
5C62: EF              RST     0X28                
5C63: EF              RST     0X28                
5C64: EF              RST     0X28                
5C65: EF              RST     0X28                
5C66: EF              RST     0X28                
5C67: EF              RST     0X28                
5C68: EF              RST     0X28                
5C69: EF              RST     0X28                
5C6A: 5A              LD      E,D                 
5C6B: 7F              LD      A,A                 
5C6C: 5A              LD      E,D                 
5C6D: 7F              LD      A,A                 
5C6E: 98              SBC     B                   
5C6F: 60              LD      H,B                 
5C70: 13              INC     DE                  
5C71: 32              LD      (HLD),A             
5C72: 33              INC     SP                  
5C73: 7F              LD      A,A                 
5C74: 5A              LD      E,D                 
5C75: 7F              LD      A,A                 
5C76: 5A              LD      E,D                 
5C77: EF              RST     0X28                
5C78: EF              RST     0X28                
5C79: EF              RST     0X28                
5C7A: EF              RST     0X28                
5C7B: EF              RST     0X28                
5C7C: EF              RST     0X28                
5C7D: EF              RST     0X28                
5C7E: EF              RST     0X28                
5C7F: EF              RST     0X28                
5C80: EF              RST     0X28                
5C81: 7F              LD      A,A                 
5C82: 5A              LD      E,D                 
5C83: 7F              LD      A,A                 
5C84: 5A              LD      E,D                 
5C85: 98              SBC     B                   
5C86: 80              ADD     A,B                 
5C87: 13              INC     DE                  
5C88: 26 27           LD      H,$27               
5C8A: 5A              LD      E,D                 
5C8B: 7F              LD      A,A                 
5C8C: EF              RST     0X28                
5C8D: EF              RST     0X28                
5C8E: EF              RST     0X28                
5C8F: EF              RST     0X28                
5C90: 1A              LD      A,(DE)              
5C91: 5A              LD      E,D                 
5C92: 1A              LD      A,(DE)              
5C93: 5A              LD      E,D                 
5C94: 1A              LD      A,(DE)              
5C95: 5A              LD      E,D                 
5C96: EF              RST     0X28                
5C97: EF              RST     0X28                
5C98: EF              RST     0X28                
5C99: EF              RST     0X28                
5C9A: 5A              LD      E,D                 
5C9B: 7F              LD      A,A                 
5C9C: 98              SBC     B                   
5C9D: A0              AND     B                   
5C9E: 13              INC     DE                  
5C9F: 36 37           LD      (HL),$37            
5CA1: 7F              LD      A,A                 
5CA2: 5A              LD      E,D                 
5CA3: EF              RST     0X28                
5CA4: EF              RST     0X28                
5CA5: EF              RST     0X28                
5CA6: EF              RST     0X28                
5CA7: 5A              LD      E,D                 
5CA8: 1A              LD      A,(DE)              
5CA9: 5A              LD      E,D                 
5CAA: 1A              LD      A,(DE)              
5CAB: 5A              LD      E,D                 
5CAC: 1A              LD      A,(DE)              
5CAD: EF              RST     0X28                
5CAE: EF              RST     0X28                
5CAF: EF              RST     0X28                
5CB0: EF              RST     0X28                
5CB1: 7F              LD      A,A                 
5CB2: 5A              LD      E,D                 
5CB3: 98              SBC     B                   
5CB4: C0              RET     NZ                  
5CB5: 13              INC     DE                  
5CB6: 22              LD      (HLI),A             
5CB7: 23              INC     HL                  
5CB8: 5A              LD      E,D                 
5CB9: 7F              LD      A,A                 
5CBA: EF              RST     0X28                
5CBB: EF              RST     0X28                
5CBC: 1A              LD      A,(DE)              
5CBD: 5A              LD      E,D                 
5CBE: EF              RST     0X28                
5CBF: EF              RST     0X28                
5CC0: E0 E1           LD      ($FF00+$E1),A       
5CC2: EF              RST     0X28                
5CC3: EF              RST     0X28                
5CC4: 1A              LD      A,(DE)              
5CC5: 5A              LD      E,D                 
5CC6: EF              RST     0X28                
5CC7: EF              RST     0X28                
5CC8: 5A              LD      E,D                 
5CC9: 7F              LD      A,A                 
5CCA: 98              SBC     B                   
5CCB: E0 13           LD      ($FF00+$13),A       
5CCD: 32              LD      (HLD),A             
5CCE: 33              INC     SP                  
5CCF: 7F              LD      A,A                 
5CD0: 5A              LD      E,D                 
5CD1: EF              RST     0X28                
5CD2: EF              RST     0X28                
5CD3: 5A              LD      E,D                 
5CD4: 1A              LD      A,(DE)              
5CD5: EF              RST     0X28                
5CD6: EF              RST     0X28                
5CD7: F0 F1           LD      A,($F1)             
5CD9: EF              RST     0X28                
5CDA: EF              RST     0X28                
5CDB: 5A              LD      E,D                 
5CDC: 1A              LD      A,(DE)              
5CDD: EF              RST     0X28                
5CDE: EF              RST     0X28                
5CDF: 7F              LD      A,A                 
5CE0: 5A              LD      E,D                 
5CE1: 99              SBC     C                   
5CE2: 00              NOP                         
5CE3: 13              INC     DE                  
5CE4: 26 27           LD      H,$27               
5CE6: 5A              LD      E,D                 
5CE7: 7F              LD      A,A                 
5CE8: EF              RST     0X28                
5CE9: EF              RST     0X28                
5CEA: 1A              LD      A,(DE)              
5CEB: 5A              LD      E,D                 
5CEC: EF              RST     0X28                
5CED: EF              RST     0X28                
5CEE: E2              LD      (C),A               
5CEF: E3                              
5CF0: EF              RST     0X28                
5CF1: EF              RST     0X28                
5CF2: 1A              LD      A,(DE)              
5CF3: 5A              LD      E,D                 
5CF4: EF              RST     0X28                
5CF5: EF              RST     0X28                
5CF6: 5A              LD      E,D                 
5CF7: 7F              LD      A,A                 
5CF8: 99              SBC     C                   
5CF9: 20 13           JR      NZ,$5D0E            ; {}
5CFB: 36 37           LD      (HL),$37            
5CFD: 7F              LD      A,A                 
5CFE: 5A              LD      E,D                 
5CFF: EF              RST     0X28                
5D00: EF              RST     0X28                
5D01: 5A              LD      E,D                 
5D02: 1A              LD      A,(DE)              
5D03: EF              RST     0X28                
5D04: EF              RST     0X28                
5D05: F2                              
5D06: F3              DI                          
5D07: EF              RST     0X28                
5D08: EF              RST     0X28                
5D09: 5A              LD      E,D                 
5D0A: 1A              LD      A,(DE)              
5D0B: EF              RST     0X28                
5D0C: EF              RST     0X28                
5D0D: 7F              LD      A,A                 
5D0E: 5A              LD      E,D                 
5D0F: 99              SBC     C                   
5D10: 40              LD      B,B                 
5D11: 13              INC     DE                  
5D12: 22              LD      (HLI),A             
5D13: 23              INC     HL                  
5D14: 5A              LD      E,D                 
5D15: 7F              LD      A,A                 
5D16: EF              RST     0X28                
5D17: EF              RST     0X28                
5D18: 1A              LD      A,(DE)              
5D19: 5A              LD      E,D                 
5D1A: EF              RST     0X28                
5D1B: EF              RST     0X28                
5D1C: EF              RST     0X28                
5D1D: EF              RST     0X28                
5D1E: EF              RST     0X28                
5D1F: EF              RST     0X28                
5D20: 1A              LD      A,(DE)              
5D21: 5A              LD      E,D                 
5D22: EF              RST     0X28                
5D23: EF              RST     0X28                
5D24: 5A              LD      E,D                 
5D25: 7F              LD      A,A                 
5D26: 99              SBC     C                   
5D27: 60              LD      H,B                 
5D28: 13              INC     DE                  
5D29: 32              LD      (HLD),A             
5D2A: 33              INC     SP                  
5D2B: 7F              LD      A,A                 
5D2C: 5A              LD      E,D                 
5D2D: EF              RST     0X28                
5D2E: EF              RST     0X28                
5D2F: 5A              LD      E,D                 
5D30: 1A              LD      A,(DE)              
5D31: EF              RST     0X28                
5D32: EF              RST     0X28                
5D33: EF              RST     0X28                
5D34: EF              RST     0X28                
5D35: EF              RST     0X28                
5D36: EF              RST     0X28                
5D37: 5A              LD      E,D                 
5D38: 1A              LD      A,(DE)              
5D39: EF              RST     0X28                
5D3A: EF              RST     0X28                
5D3B: 7F              LD      A,A                 
5D3C: 5A              LD      E,D                 
5D3D: 99              SBC     C                   
5D3E: 80              ADD     A,B                 
5D3F: 13              INC     DE                  
5D40: 26 27           LD      H,$27               
5D42: 5A              LD      E,D                 
5D43: 7F              LD      A,A                 
5D44: EF              RST     0X28                
5D45: EF              RST     0X28                
5D46: EF              RST     0X28                
5D47: EF              RST     0X28                
5D48: 1A              LD      A,(DE)              
5D49: 5A              LD      E,D                 
5D4A: 1A              LD      A,(DE)              
5D4B: 5A              LD      E,D                 
5D4C: 1A              LD      A,(DE)              
5D4D: 5A              LD      E,D                 
5D4E: EF              RST     0X28                
5D4F: EF              RST     0X28                
5D50: EF              RST     0X28                
5D51: EF              RST     0X28                
5D52: 74              LD      (HL),H              
5D53: 74              LD      (HL),H              
5D54: 99              SBC     C                   
5D55: A0              AND     B                   
5D56: 13              INC     DE                  
5D57: 36 37           LD      (HL),$37            
5D59: 7F              LD      A,A                 
5D5A: 5A              LD      E,D                 
5D5B: EF              RST     0X28                
5D5C: EF              RST     0X28                
5D5D: EF              RST     0X28                
5D5E: EF              RST     0X28                
5D5F: 5A              LD      E,D                 
5D60: 1A              LD      A,(DE)              
5D61: 5A              LD      E,D                 
5D62: 1A              LD      A,(DE)              
5D63: 5A              LD      E,D                 
5D64: 1A              LD      A,(DE)              
5D65: EF              RST     0X28                
5D66: EF              RST     0X28                
5D67: EF              RST     0X28                
5D68: EF              RST     0X28                
5D69: 74              LD      (HL),H              
5D6A: 74              LD      (HL),H              
5D6B: 99              SBC     C                   
5D6C: C0              RET     NZ                  
5D6D: 13              INC     DE                  
5D6E: 22              LD      (HLI),A             
5D6F: 23              INC     HL                  
5D70: 5A              LD      E,D                 
5D71: 7F              LD      A,A                 
5D72: 5A              LD      E,D                 
5D73: 7F              LD      A,A                 
5D74: EF              RST     0X28                
5D75: EF              RST     0X28                
5D76: EF              RST     0X28                
5D77: EF              RST     0X28                
5D78: EF              RST     0X28                
5D79: EF              RST     0X28                
5D7A: EF              RST     0X28                
5D7B: EF              RST     0X28                
5D7C: EF              RST     0X28                
5D7D: EF              RST     0X28                
5D7E: 5A              LD      E,D                 
5D7F: 7F              LD      A,A                 
5D80: 5A              LD      E,D                 
5D81: 7F              LD      A,A                 
5D82: 99              SBC     C                   
5D83: E0 13           LD      ($FF00+$13),A       
5D85: 32              LD      (HLD),A             
5D86: 33              INC     SP                  
5D87: 7F              LD      A,A                 
5D88: 5A              LD      E,D                 
5D89: 7F              LD      A,A                 
5D8A: 5A              LD      E,D                 
5D8B: EF              RST     0X28                
5D8C: EF              RST     0X28                
5D8D: EF              RST     0X28                
5D8E: EF              RST     0X28                
5D8F: EF              RST     0X28                
5D90: EF              RST     0X28                
5D91: EF              RST     0X28                
5D92: EF              RST     0X28                
5D93: EF              RST     0X28                
5D94: EF              RST     0X28                
5D95: 7F              LD      A,A                 
5D96: 5A              LD      E,D                 
5D97: 7F              LD      A,A                 
5D98: 5A              LD      E,D                 
5D99: 9A              SBC     D                   
5D9A: 00              NOP                         
5D9B: 13              INC     DE                  
5D9C: 26 27           LD      H,$27               
5D9E: 5A              LD      E,D                 
5D9F: 7F              LD      A,A                 
5DA0: 5A              LD      E,D                 
5DA1: 7F              LD      A,A                 
5DA2: 5A              LD      E,D                 
5DA3: 7F              LD      A,A                 
5DA4: 5A              LD      E,D                 
5DA5: 7F              LD      A,A                 
5DA6: 5A              LD      E,D                 
5DA7: 7F              LD      A,A                 
5DA8: 5A              LD      E,D                 
5DA9: 7F              LD      A,A                 
5DAA: 5A              LD      E,D                 
5DAB: 7F              LD      A,A                 
5DAC: 5A              LD      E,D                 
5DAD: 7F              LD      A,A                 
5DAE: 5A              LD      E,D                 
5DAF: 7F              LD      A,A                 
5DB0: 9A              SBC     D                   
5DB1: 20 13           JR      NZ,$5DC6            ; {}
5DB3: 36 37           LD      (HL),$37            
5DB5: 7F              LD      A,A                 
5DB6: 5A              LD      E,D                 
5DB7: 7F              LD      A,A                 
5DB8: 5A              LD      E,D                 
5DB9: 7F              LD      A,A                 
5DBA: 5A              LD      E,D                 
5DBB: 7F              LD      A,A                 
5DBC: 5A              LD      E,D                 
5DBD: 7F              LD      A,A                 
5DBE: 5A              LD      E,D                 
5DBF: 7F              LD      A,A                 
5DC0: 5A              LD      E,D                 
5DC1: 7F              LD      A,A                 
5DC2: 5A              LD      E,D                 
5DC3: 7F              LD      A,A                 
5DC4: 5A              LD      E,D                 
5DC5: 7F              LD      A,A                 
5DC6: 5A              LD      E,D                 
5DC7: 00              NOP                         
5DC8: 98              SBC     B                   
5DC9: 00              NOP                         
5DCA: 13              INC     DE                  
5DCB: 24              INC     H                   
5DCC: 25              DEC     H                   
5DCD: 26 27           LD      H,$27               
5DCF: 24              INC     H                   
5DD0: 25              DEC     H                   
5DD1: 26 27           LD      H,$27               
5DD3: 75              LD      (HL),L              
5DD4: 75              LD      (HL),L              
5DD5: 75              LD      (HL),L              
5DD6: 75              LD      (HL),L              
5DD7: 75              LD      (HL),L              
5DD8: 75              LD      (HL),L              
5DD9: 24              INC     H                   
5DDA: 25              DEC     H                   
5DDB: 26 27           LD      H,$27               
5DDD: 24              INC     H                   
5DDE: 25              DEC     H                   
5DDF: 98              SBC     B                   
5DE0: 20 13           JR      NZ,$5DF5            ; {}
5DE2: 34              INC     (HL)                
5DE3: 35              DEC     (HL)                
5DE4: 36 37           LD      (HL),$37            
5DE6: 34              INC     (HL)                
5DE7: 35              DEC     (HL)                
5DE8: 36 37           LD      (HL),$37            
5DEA: 75              LD      (HL),L              
5DEB: 75              LD      (HL),L              
5DEC: 75              LD      (HL),L              
5DED: 75              LD      (HL),L              
5DEE: 75              LD      (HL),L              
5DEF: 75              LD      (HL),L              
5DF0: 34              INC     (HL)                
5DF1: 35              DEC     (HL)                
5DF2: 36 37           LD      (HL),$37            
5DF4: 34              INC     (HL)                
5DF5: 35              DEC     (HL)                
5DF6: 98              SBC     B                   
5DF7: 40              LD      B,B                 
5DF8: 13              INC     DE                  
5DF9: 74              LD      (HL),H              
5DFA: 74              LD      (HL),H              
5DFB: 74              LD      (HL),H              
5DFC: 74              LD      (HL),H              
5DFD: E6 E7           AND     $E7                 
5DFF: E7              RST     0X20                
5E00: E7              RST     0X20                
5E01: E7              RST     0X20                
5E02: E8 75           ADD     SP,$75              
5E04: 75              LD      (HL),L              
5E05: 5A              LD      E,D                 
5E06: 7F              LD      A,A                 
5E07: 5A              LD      E,D                 
5E08: 7F              LD      A,A                 
5E09: 5A              LD      E,D                 
5E0A: 7F              LD      A,A                 
5E0B: 5A              LD      E,D                 
5E0C: 7F              LD      A,A                 
5E0D: 98              SBC     B                   
5E0E: 60              LD      H,B                 
5E0F: 13              INC     DE                  
5E10: 74              LD      (HL),H              
5E11: 74              LD      (HL),H              
5E12: 74              LD      (HL),H              
5E13: 74              LD      (HL),H              
5E14: E9              JP      (HL)                
5E15: 7C              LD      A,H                 
5E16: 7C              LD      A,H                 
5E17: 7C              LD      A,H                 
5E18: 7C              LD      A,H                 
5E19: F9              LD      SP,HL               
5E1A: 75              LD      (HL),L              
5E1B: 75              LD      (HL),L              
5E1C: 7F              LD      A,A                 
5E1D: 5A              LD      E,D                 
5E1E: 7F              LD      A,A                 
5E1F: 5A              LD      E,D                 
5E20: 7F              LD      A,A                 
5E21: 5A              LD      E,D                 
5E22: 7F              LD      A,A                 
5E23: 5A              LD      E,D                 
5E24: 98              SBC     B                   
5E25: 80              ADD     A,B                 
5E26: 13              INC     DE                  
5E27: 5A              LD      E,D                 
5E28: 7F              LD      A,A                 
5E29: 74              LD      (HL),H              
5E2A: 74              LD      (HL),H              
5E2B: E9              JP      (HL)                
5E2C: 7C              LD      A,H                 
5E2D: 7C              LD      A,H                 
5E2E: 7C              LD      A,H                 
5E2F: 7C              LD      A,H                 
5E30: F9              LD      SP,HL               
5E31: 5E              LD      E,(HL)              
5E32: 5E              LD      E,(HL)              
5E33: 1A              LD      A,(DE)              
5E34: 5A              LD      E,D                 
5E35: 5A              LD      E,D                 
5E36: 7F              LD      A,A                 
5E37: 5A              LD      E,D                 
5E38: 7F              LD      A,A                 
5E39: 5A              LD      E,D                 
5E3A: 7F              LD      A,A                 
5E3B: 98              SBC     B                   
5E3C: A0              AND     B                   
5E3D: 13              INC     DE                  
5E3E: 7F              LD      A,A                 
5E3F: 5A              LD      E,D                 
5E40: 74              LD      (HL),H              
5E41: 74              LD      (HL),H              
5E42: F6 F7           OR      $F7                 
5E44: F7              RST     0X30                
5E45: F7              RST     0X30                
5E46: F7              RST     0X30                
5E47: F8 5F           LD      HL,SP+$5F           
5E49: 5F              LD      E,A                 
5E4A: 5A              LD      E,D                 
5E4B: 1A              LD      A,(DE)              
5E4C: 7F              LD      A,A                 
5E4D: 5A              LD      E,D                 
5E4E: 7F              LD      A,A                 
5E4F: 5A              LD      E,D                 
5E50: 7F              LD      A,A                 
5E51: 5A              LD      E,D                 
5E52: 98              SBC     B                   
5E53: C0              RET     NZ                  
5E54: 13              INC     DE                  
5E55: 5A              LD      E,D                 
5E56: 7F              LD      A,A                 
5E57: 74              LD      (HL),H              
5E58: 74              LD      (HL),H              
5E59: 2C              INC     L                   
5E5A: 2D              DEC     L                   
5E5B: 2E 2F           LD      L,$2F               
5E5D: 2C              INC     L                   
5E5E: 2D              DEC     L                   
5E5F: 2E 2F           LD      L,$2F               
5E61: EC                              
5E62: EC                              
5E63: 75              LD      (HL),L              
5E64: 75              LD      (HL),L              
5E65: 5A              LD      E,D                 
5E66: 7F              LD      A,A                 
5E67: 5A              LD      E,D                 
5E68: 7F              LD      A,A                 
5E69: 98              SBC     B                   
5E6A: E0 13           LD      ($FF00+$13),A       
5E6C: 7F              LD      A,A                 
5E6D: 5A              LD      E,D                 
5E6E: 74              LD      (HL),H              
5E6F: 74              LD      (HL),H              
5E70: 3C              INC     A                   
5E71: 3D              DEC     A                   
5E72: 3E 3F           LD      A,$3F               
5E74: 3C              INC     A                   
5E75: 3D              DEC     A                   
5E76: 3E 3F           LD      A,$3F               
5E78: FC                              
5E79: FC                              
5E7A: 75              LD      (HL),L              
5E7B: 75              LD      (HL),L              
5E7C: 7F              LD      A,A                 
5E7D: 5A              LD      E,D                 
5E7E: 7F              LD      A,A                 
5E7F: 5A              LD      E,D                 
5E80: 99              SBC     C                   
5E81: 00              NOP                         
5E82: 13              INC     DE                  
5E83: 5A              LD      E,D                 
5E84: 7F              LD      A,A                 
5E85: 74              LD      (HL),H              
5E86: 74              LD      (HL),H              
5E87: 74              LD      (HL),H              
5E88: 74              LD      (HL),H              
5E89: 74              LD      (HL),H              
5E8A: 74              LD      (HL),H              
5E8B: 74              LD      (HL),H              
5E8C: EC                              
5E8D: 75              LD      (HL),L              
5E8E: 75              LD      (HL),L              
5E8F: 75              LD      (HL),L              
5E90: 75              LD      (HL),L              
5E91: 75              LD      (HL),L              
5E92: 75              LD      (HL),L              
5E93: 75              LD      (HL),L              
5E94: 75              LD      (HL),L              
5E95: 5A              LD      E,D                 
5E96: 7F              LD      A,A                 
5E97: 99              SBC     C                   
5E98: 20 13           JR      NZ,$5EAD            ; {}
5E9A: 7F              LD      A,A                 
5E9B: 5A              LD      E,D                 
5E9C: 74              LD      (HL),H              
5E9D: 74              LD      (HL),H              
5E9E: 74              LD      (HL),H              
5E9F: 74              LD      (HL),H              
5EA0: 74              LD      (HL),H              
5EA1: 74              LD      (HL),H              
5EA2: 74              LD      (HL),H              
5EA3: FC                              
5EA4: 75              LD      (HL),L              
5EA5: 75              LD      (HL),L              
5EA6: 75              LD      (HL),L              
5EA7: 75              LD      (HL),L              
5EA8: 75              LD      (HL),L              
5EA9: 75              LD      (HL),L              
5EAA: 75              LD      (HL),L              
5EAB: 75              LD      (HL),L              
5EAC: 7F              LD      A,A                 
5EAD: 5A              LD      E,D                 
5EAE: 99              SBC     C                   
5EAF: 40              LD      B,B                 
5EB0: 13              INC     DE                  
5EB1: 5A              LD      E,D                 
5EB2: 7F              LD      A,A                 
5EB3: 5A              LD      E,D                 
5EB4: 7F              LD      A,A                 
5EB5: 1A              LD      A,(DE)              
5EB6: 5A              LD      E,D                 
5EB7: 75              LD      (HL),L              
5EB8: 75              LD      (HL),L              
5EB9: 75              LD      (HL),L              
5EBA: 75              LD      (HL),L              
5EBB: 75              LD      (HL),L              
5EBC: 75              LD      (HL),L              
5EBD: 75              LD      (HL),L              
5EBE: 75              LD      (HL),L              
5EBF: 75              LD      (HL),L              
5EC0: 75              LD      (HL),L              
5EC1: 5A              LD      E,D                 
5EC2: 7F              LD      A,A                 
5EC3: 5A              LD      E,D                 
5EC4: 7F              LD      A,A                 
5EC5: 99              SBC     C                   
5EC6: 60              LD      H,B                 
5EC7: 13              INC     DE                  
5EC8: 7F              LD      A,A                 
5EC9: 5A              LD      E,D                 
5ECA: 7F              LD      A,A                 
5ECB: 5A              LD      E,D                 
5ECC: 5A              LD      E,D                 
5ECD: 1A              LD      A,(DE)              
5ECE: 75              LD      (HL),L              
5ECF: 75              LD      (HL),L              
5ED0: 75              LD      (HL),L              
5ED1: 75              LD      (HL),L              
5ED2: 75              LD      (HL),L              
5ED3: 75              LD      (HL),L              
5ED4: 75              LD      (HL),L              
5ED5: 75              LD      (HL),L              
5ED6: 75              LD      (HL),L              
5ED7: 75              LD      (HL),L              
5ED8: 7F              LD      A,A                 
5ED9: 5A              LD      E,D                 
5EDA: 7F              LD      A,A                 
5EDB: 5A              LD      E,D                 
5EDC: 99              SBC     C                   
5EDD: 80              ADD     A,B                 
5EDE: 13              INC     DE                  
5EDF: 74              LD      (HL),H              
5EE0: 74              LD      (HL),H              
5EE1: 74              LD      (HL),H              
5EE2: 74              LD      (HL),H              
5EE3: 5A              LD      E,D                 
5EE4: 7F              LD      A,A                 
5EE5: 5A              LD      E,D                 
5EE6: 7F              LD      A,A                 
5EE7: 5A              LD      E,D                 
5EE8: 7F              LD      A,A                 
5EE9: 5A              LD      E,D                 
5EEA: 7F              LD      A,A                 
5EEB: 5A              LD      E,D                 
5EEC: 7F              LD      A,A                 
5EED: 5A              LD      E,D                 
5EEE: 7F              LD      A,A                 
5EEF: 1A              LD      A,(DE)              
5EF0: 5A              LD      E,D                 
5EF1: 5A              LD      E,D                 
5EF2: 7F              LD      A,A                 
5EF3: 99              SBC     C                   
5EF4: A0              AND     B                   
5EF5: 13              INC     DE                  
5EF6: 74              LD      (HL),H              
5EF7: 74              LD      (HL),H              
5EF8: 74              LD      (HL),H              
5EF9: 74              LD      (HL),H              
5EFA: 7F              LD      A,A                 
5EFB: 5A              LD      E,D                 
5EFC: 7F              LD      A,A                 
5EFD: 5A              LD      E,D                 
5EFE: 7F              LD      A,A                 
5EFF: 5A              LD      E,D                 
5F00: 7F              LD      A,A                 
5F01: 5A              LD      E,D                 
5F02: 7F              LD      A,A                 
5F03: 5A              LD      E,D                 
5F04: 7F              LD      A,A                 
5F05: 5A              LD      E,D                 
5F06: 5A              LD      E,D                 
5F07: 1A              LD      A,(DE)              
5F08: 7F              LD      A,A                 
5F09: 5A              LD      E,D                 
5F0A: 99              SBC     C                   
5F0B: C0              RET     NZ                  
5F0C: 13              INC     DE                  
5F0D: 22              LD      (HLI),A             
5F0E: 23              INC     HL                  
5F0F: 74              LD      (HL),H              
5F10: 74              LD      (HL),H              
5F11: 74              LD      (HL),H              
5F12: 74              LD      (HL),H              
5F13: 74              LD      (HL),H              
5F14: 74              LD      (HL),H              
5F15: 74              LD      (HL),H              
5F16: 74              LD      (HL),H              
5F17: 74              LD      (HL),H              
5F18: 74              LD      (HL),H              
5F19: 74              LD      (HL),H              
5F1A: 74              LD      (HL),H              
5F1B: 74              LD      (HL),H              
5F1C: 74              LD      (HL),H              
5F1D: 74              LD      (HL),H              
5F1E: 74              LD      (HL),H              
5F1F: 74              LD      (HL),H              
5F20: 74              LD      (HL),H              
5F21: 99              SBC     C                   
5F22: E0 13           LD      ($FF00+$13),A       
5F24: 32              LD      (HLD),A             
5F25: 33              INC     SP                  
5F26: 74              LD      (HL),H              
5F27: 74              LD      (HL),H              
5F28: 74              LD      (HL),H              
5F29: 74              LD      (HL),H              
5F2A: 74              LD      (HL),H              
5F2B: 74              LD      (HL),H              
5F2C: 74              LD      (HL),H              
5F2D: 74              LD      (HL),H              
5F2E: 74              LD      (HL),H              
5F2F: 74              LD      (HL),H              
5F30: 74              LD      (HL),H              
5F31: 74              LD      (HL),H              
5F32: 74              LD      (HL),H              
5F33: 74              LD      (HL),H              
5F34: 74              LD      (HL),H              
5F35: 74              LD      (HL),H              
5F36: 74              LD      (HL),H              
5F37: 74              LD      (HL),H              
5F38: 9A              SBC     D                   
5F39: 00              NOP                         
5F3A: 13              INC     DE                  
5F3B: 26 27           LD      H,$27               
5F3D: 5A              LD      E,D                 
5F3E: 7F              LD      A,A                 
5F3F: 5A              LD      E,D                 
5F40: 7F              LD      A,A                 
5F41: 5A              LD      E,D                 
5F42: 7F              LD      A,A                 
5F43: 5A              LD      E,D                 
5F44: 7F              LD      A,A                 
5F45: 5A              LD      E,D                 
5F46: 7F              LD      A,A                 
5F47: 5A              LD      E,D                 
5F48: 7F              LD      A,A                 
5F49: 5A              LD      E,D                 
5F4A: 7F              LD      A,A                 
5F4B: 5A              LD      E,D                 
5F4C: 7F              LD      A,A                 
5F4D: 5A              LD      E,D                 
5F4E: 7F              LD      A,A                 
5F4F: 9A              SBC     D                   
5F50: 20 13           JR      NZ,$5F65            ; {}
5F52: 36 37           LD      (HL),$37            
5F54: 7F              LD      A,A                 
5F55: 5A              LD      E,D                 
5F56: 7F              LD      A,A                 
5F57: 5A              LD      E,D                 
5F58: 7F              LD      A,A                 
5F59: 5A              LD      E,D                 
5F5A: 7F              LD      A,A                 
5F5B: 5A              LD      E,D                 
5F5C: 7F              LD      A,A                 
5F5D: 5A              LD      E,D                 
5F5E: 7F              LD      A,A                 
5F5F: 5A              LD      E,D                 
5F60: 7F              LD      A,A                 
5F61: 5A              LD      E,D                 
5F62: 7F              LD      A,A                 
5F63: 5A              LD      E,D                 
5F64: 7F              LD      A,A                 
5F65: 5A              LD      E,D                 
5F66: 00              NOP                         
5F67: 98              SBC     B                   
5F68: 00              NOP                         
5F69: 13              INC     DE                  
5F6A: 92              SUB     D                   
5F6B: 7C              LD      A,H                 
5F6C: 92              SUB     D                   
5F6D: 7C              LD      A,H                 
5F6E: 92              SUB     D                   
5F6F: 83              ADD     A,E                 
5F70: 5A              LD      E,D                 
5F71: 7F              LD      A,A                 
5F72: 5A              LD      E,D                 
5F73: 7F              LD      A,A                 
5F74: 5A              LD      E,D                 
5F75: 7F              LD      A,A                 
5F76: 75              LD      (HL),L              
5F77: 75              LD      (HL),L              
5F78: 82              ADD     A,D                 
5F79: 7C              LD      A,H                 
5F7A: 92              SUB     D                   
5F7B: 7C              LD      A,H                 
5F7C: 24              INC     H                   
5F7D: 25              DEC     H                   
5F7E: 98              SBC     B                   
5F7F: 20 13           JR      NZ,$5F94            ; {}
5F81: 7C              LD      A,H                 
5F82: 92              SUB     D                   
5F83: 7C              LD      A,H                 
5F84: 84              ADD     A,H                 
5F85: 80              ADD     A,B                 
5F86: 89              ADC     A,C                 
5F87: 7F              LD      A,A                 
5F88: 5A              LD      E,D                 
5F89: 7F              LD      A,A                 
5F8A: 5A              LD      E,D                 
5F8B: 7F              LD      A,A                 
5F8C: 5A              LD      E,D                 
5F8D: 75              LD      (HL),L              
5F8E: 75              LD      (HL),L              
5F8F: 82              ADD     A,D                 
5F90: 92              SUB     D                   
5F91: 7C              LD      A,H                 
5F92: 92              SUB     D                   
5F93: 8E              ADC     A,(HL)              
5F94: 8F              ADC     A,A                 
5F95: 98              SBC     B                   
5F96: 40              LD      B,B                 
5F97: 13              INC     DE                  
5F98: 92              SUB     D                   
5F99: 7C              LD      A,H                 
5F9A: 92              SUB     D                   
5F9B: 83              ADD     A,E                 
5F9C: 5A              LD      E,D                 
5F9D: 7F              LD      A,A                 
5F9E: 5A              LD      E,D                 
5F9F: 7F              LD      A,A                 
5FA0: 5A              LD      E,D                 
5FA1: 7F              LD      A,A                 
5FA2: 5A              LD      E,D                 
5FA3: 7F              LD      A,A                 
5FA4: 75              LD      (HL),L              
5FA5: 75              LD      (HL),L              
5FA6: 82              ADD     A,D                 
5FA7: 7C              LD      A,H                 
5FA8: 92              SUB     D                   
5FA9: 7C              LD      A,H                 
5FAA: 28 21           JR      Z,$5FCD             ; {}
5FAC: 98              SBC     B                   
5FAD: 60              LD      H,B                 
5FAE: 13              INC     DE                  
5FAF: 7C              LD      A,H                 
5FB0: 84              ADD     A,H                 
5FB1: 80              ADD     A,B                 
5FB2: 89              ADC     A,C                 
5FB3: 7F              LD      A,A                 
5FB4: 5A              LD      E,D                 
5FB5: 7F              LD      A,A                 
5FB6: 5A              LD      E,D                 
5FB7: 7F              LD      A,A                 
5FB8: 5A              LD      E,D                 
5FB9: 7F              LD      A,A                 
5FBA: 5A              LD      E,D                 
5FBB: 75              LD      (HL),L              
5FBC: 75              LD      (HL),L              
5FBD: 88              ADC     A,B                 
5FBE: 80              ADD     A,B                 
5FBF: 85              ADD     A,L                 
5FC0: 92              SUB     D                   
5FC1: 30 31           JR      NC,$5FF4            ; {}
5FC3: 98              SBC     B                   
5FC4: 80              ADD     A,B                 
5FC5: 13              INC     DE                  
5FC6: 92              SUB     D                   
5FC7: 83              ADD     A,E                 
5FC8: 8C              ADC     A,H                 
5FC9: 8D              ADC     A,L                 
5FCA: 5A              LD      E,D                 
5FCB: 7F              LD      A,A                 
5FCC: 14              INC     D                   
5FCD: 16 14           LD      D,$14               
5FCF: 16 5A           LD      D,$5A               
5FD1: 7F              LD      A,A                 
5FD2: 5A              LD      E,D                 
5FD3: 7F              LD      A,A                 
5FD4: 1A              LD      A,(DE)              
5FD5: 5A              LD      E,D                 
5FD6: 82              ADD     A,D                 
5FD7: 7C              LD      A,H                 
5FD8: 24              INC     H                   
5FD9: 25              DEC     H                   
5FDA: 98              SBC     B                   
5FDB: A0              AND     B                   
5FDC: 13              INC     DE                  
5FDD: 7C              LD      A,H                 
5FDE: 83              ADD     A,E                 
5FDF: 9C              SBC     H                   
5FE0: 9D              SBC     L                   
5FE1: 7F              LD      A,A                 
5FE2: 5A              LD      E,D                 
5FE3: 15              DEC     D                   
5FE4: 17              RLA                         
5FE5: 15              DEC     D                   
5FE6: 17              RLA                         
5FE7: 7F              LD      A,A                 
5FE8: 5A              LD      E,D                 
5FE9: 7F              LD      A,A                 
5FEA: 5A              LD      E,D                 
5FEB: 5A              LD      E,D                 
5FEC: 1A              LD      A,(DE)              
5FED: 82              ADD     A,D                 
5FEE: 92              SUB     D                   
5FEF: 8E              ADC     A,(HL)              
5FF0: 8F              ADC     A,A                 
5FF1: 98              SBC     B                   
5FF2: C0              RET     NZ                  
5FF3: 13              INC     DE                  
5FF4: 92              SUB     D                   
5FF5: 83              ADD     A,E                 
5FF6: 5A              LD      E,D                 
5FF7: 7F              LD      A,A                 
5FF8: 14              INC     D                   
5FF9: 16 20           LD      D,$20               
5FFB: 21 22 23        LD      HL,$2322            
5FFE: 14              INC     D                   
5FFF: 16 1A           LD      D,$1A               
6001: 5A              LD      E,D                 
6002: 75              LD      (HL),L              
6003: 75              LD      (HL),L              
6004: 82              ADD     A,D                 
6005: 7C              LD      A,H                 
6006: 28 21           JR      Z,$6029             ; {}
6008: 98              SBC     B                   
6009: E0 13           LD      ($FF00+$13),A       
600B: 7C              LD      A,H                 
600C: 83              ADD     A,E                 
600D: 7F              LD      A,A                 
600E: 5A              LD      E,D                 
600F: 15              DEC     D                   
6010: 17              RLA                         
6011: 30 31           JR      NC,$6044            ; {}
6013: 32              LD      (HLD),A             
6014: 33              INC     SP                  
6015: 15              DEC     D                   
6016: 17              RLA                         
6017: 5A              LD      E,D                 
6018: 1A              LD      A,(DE)              
6019: 75              LD      (HL),L              
601A: 75              LD      (HL),L              
601B: 82              ADD     A,D                 
601C: 92              SUB     D                   
601D: 30 31           JR      NC,$6050            ; {}
601F: 99              SBC     C                   
6020: 00              NOP                         
6021: 13              INC     DE                  
6022: 92              SUB     D                   
6023: 83              ADD     A,E                 
6024: 5A              LD      E,D                 
6025: 7F              LD      A,A                 
6026: 14              INC     D                   
6027: 16 24           LD      D,$24               
6029: 25              DEC     H                   
602A: 26 27           LD      H,$27               
602C: 14              INC     D                   
602D: 16 5A           LD      D,$5A               
602F: 7F              LD      A,A                 
6030: 75              LD      (HL),L              
6031: 75              LD      (HL),L              
6032: 82              ADD     A,D                 
6033: 7C              LD      A,H                 
6034: 24              INC     H                   
6035: 25              DEC     H                   
6036: 99              SBC     C                   
6037: 20 13           JR      NZ,$604C            ; {}
6039: 7C              LD      A,H                 
603A: 83              ADD     A,E                 
603B: 7F              LD      A,A                 
603C: 5A              LD      E,D                 
603D: 15              DEC     D                   
603E: 17              RLA                         
603F: 34              INC     (HL)                
6040: 35              DEC     (HL)                
6041: 36 37           LD      (HL),$37            
6043: 15              DEC     D                   
6044: 17              RLA                         
6045: 7F              LD      A,A                 
6046: 5A              LD      E,D                 
6047: 75              LD      (HL),L              
6048: 75              LD      (HL),L              
6049: 82              ADD     A,D                 
604A: 92              SUB     D                   
604B: 8E              ADC     A,(HL)              
604C: 8F              ADC     A,A                 
604D: 99              SBC     C                   
604E: 40              LD      B,B                 
604F: 13              INC     DE                  
6050: 92              SUB     D                   
6051: 83              ADD     A,E                 
6052: 5A              LD      E,D                 
6053: 7F              LD      A,A                 
6054: 5A              LD      E,D                 
6055: 7F              LD      A,A                 
6056: 14              INC     D                   
6057: 16 14           LD      D,$14               
6059: 16 5A           LD      D,$5A               
605B: 7F              LD      A,A                 
605C: 75              LD      (HL),L              
605D: 75              LD      (HL),L              
605E: 75              LD      (HL),L              
605F: 75              LD      (HL),L              
6060: 82              ADD     A,D                 
6061: 7C              LD      A,H                 
6062: 28 21           JR      Z,$6085             ; {}
6064: 99              SBC     C                   
6065: 60              LD      H,B                 
6066: 13              INC     DE                  
6067: 7C              LD      A,H                 
6068: 83              ADD     A,E                 
6069: 7F              LD      A,A                 
606A: 5A              LD      E,D                 
606B: 7F              LD      A,A                 
606C: 5A              LD      E,D                 
606D: 15              DEC     D                   
606E: 17              RLA                         
606F: 15              DEC     D                   
6070: 17              RLA                         
6071: 7F              LD      A,A                 
6072: 5A              LD      E,D                 
6073: 75              LD      (HL),L              
6074: 75              LD      (HL),L              
6075: 75              LD      (HL),L              
6076: 75              LD      (HL),L              
6077: 82              ADD     A,D                 
6078: 92              SUB     D                   
6079: 30 31           JR      NC,$60AC            ; {}
607B: 99              SBC     C                   
607C: 80              ADD     A,B                 
607D: 13              INC     DE                  
607E: 92              SUB     D                   
607F: 83              ADD     A,E                 
6080: 5A              LD      E,D                 
6081: 7F              LD      A,A                 
6082: 5A              LD      E,D                 
6083: 7F              LD      A,A                 
6084: 1A              LD      A,(DE)              
6085: 5A              LD      E,D                 
6086: 8C              ADC     A,H                 
6087: 8D              ADC     A,L                 
6088: 5A              LD      E,D                 
6089: 7F              LD      A,A                 
608A: 75              LD      (HL),L              
608B: 75              LD      (HL),L              
608C: 8A              ADC     A,D                 
608D: 81              ADD     A,C                 
608E: 92              SUB     D                   
608F: 7C              LD      A,H                 
6090: 24              INC     H                   
6091: 25              DEC     H                   
6092: 99              SBC     C                   
6093: A0              AND     B                   
6094: 13              INC     DE                  
6095: 7C              LD      A,H                 
6096: 83              ADD     A,E                 
6097: 7F              LD      A,A                 
6098: 5A              LD      E,D                 
6099: 7F              LD      A,A                 
609A: 5A              LD      E,D                 
609B: 5A              LD      E,D                 
609C: 1A              LD      A,(DE)              
609D: 9C              SBC     H                   
609E: 9D              SBC     L                   
609F: 7F              LD      A,A                 
60A0: 5A              LD      E,D                 
60A1: 75              LD      (HL),L              
60A2: 75              LD      (HL),L              
60A3: 82              ADD     A,D                 
60A4: 92              SUB     D                   
60A5: 7C              LD      A,H                 
60A6: 92              SUB     D                   
60A7: 8E              ADC     A,(HL)              
60A8: 8F              ADC     A,A                 
60A9: 99              SBC     C                   
60AA: C0              RET     NZ                  
60AB: 13              INC     DE                  
60AC: 92              SUB     D                   
60AD: 86              ADD     A,(HL)              
60AE: 81              ADD     A,C                 
60AF: 81              ADD     A,C                 
60B0: 81              ADD     A,C                 
60B1: 8B              ADC     A,E                 
60B2: 5A              LD      E,D                 
60B3: 7F              LD      A,A                 
60B4: 5A              LD      E,D                 
60B5: 7F              LD      A,A                 
60B6: 5A              LD      E,D                 
60B7: 7F              LD      A,A                 
60B8: 75              LD      (HL),L              
60B9: 75              LD      (HL),L              
60BA: 82              ADD     A,D                 
60BB: 7C              LD      A,H                 
60BC: 92              SUB     D                   
60BD: 7C              LD      A,H                 
60BE: 28 21           JR      Z,$60E1             ; {}
60C0: 99              SBC     C                   
60C1: E0 13           LD      ($FF00+$13),A       
60C3: 7C              LD      A,H                 
60C4: 92              SUB     D                   
60C5: 7C              LD      A,H                 
60C6: 92              SUB     D                   
60C7: 7C              LD      A,H                 
60C8: 83              ADD     A,E                 
60C9: 7F              LD      A,A                 
60CA: 5A              LD      E,D                 
60CB: 7F              LD      A,A                 
60CC: 5A              LD      E,D                 
60CD: 7F              LD      A,A                 
60CE: 5A              LD      E,D                 
60CF: 75              LD      (HL),L              
60D0: 75              LD      (HL),L              
60D1: 82              ADD     A,D                 
60D2: 92              SUB     D                   
60D3: 7C              LD      A,H                 
60D4: 92              SUB     D                   
60D5: 30 31           JR      NC,$6108            ; {}
60D7: 9A              SBC     D                   
60D8: 00              NOP                         
60D9: 13              INC     DE                  
60DA: 92              SUB     D                   
60DB: 7C              LD      A,H                 
60DC: 92              SUB     D                   
60DD: 7C              LD      A,H                 
60DE: 92              SUB     D                   
60DF: 83              ADD     A,E                 
60E0: 5A              LD      E,D                 
60E1: 7F              LD      A,A                 
60E2: 5A              LD      E,D                 
60E3: 7F              LD      A,A                 
60E4: 75              LD      (HL),L              
60E5: 75              LD      (HL),L              
60E6: 75              LD      (HL),L              
60E7: 75              LD      (HL),L              
60E8: 82              ADD     A,D                 
60E9: 7C              LD      A,H                 
60EA: 92              SUB     D                   
60EB: 7C              LD      A,H                 
60EC: 24              INC     H                   
60ED: 25              DEC     H                   
60EE: 9A              SBC     D                   
60EF: 20 13           JR      NZ,$6104            ; {}
60F1: 7C              LD      A,H                 
60F2: 92              SUB     D                   
60F3: 7C              LD      A,H                 
60F4: 92              SUB     D                   
60F5: 7C              LD      A,H                 
60F6: 83              ADD     A,E                 
60F7: 7F              LD      A,A                 
60F8: 5A              LD      E,D                 
60F9: 7F              LD      A,A                 
60FA: 5A              LD      E,D                 
60FB: 75              LD      (HL),L              
60FC: 75              LD      (HL),L              
60FD: 75              LD      (HL),L              
60FE: 75              LD      (HL),L              
60FF: 82              ADD     A,D                 
6100: 92              SUB     D                   
6101: 7C              LD      A,H                 
6102: 92              SUB     D                   
6103: 8E              ADC     A,(HL)              
6104: 8F              ADC     A,A                 
6105: 00              NOP                         
6106: 98              SBC     B                   
6107: 00              NOP                         
6108: 13              INC     DE                  
6109: 76              HALT                        
610A: 76              HALT                        
610B: 49              LD      C,C                 
610C: 59              LD      E,C                 
610D: AC              XOR     H                   
610E: AD              XOR     L                   
610F: AC              XOR     H                   
6110: AD              XOR     L                   
6111: AC              XOR     H                   
6112: AD              XOR     L                   
6113: AC              XOR     H                   
6114: AD              XOR     L                   
6115: AC              XOR     H                   
6116: AD              XOR     L                   
6117: 44              LD      B,H                 
6118: 56              LD      D,(HL)              
6119: 48              LD      C,B                 
611A: 51              LD      D,C                 
611B: 45              LD      B,L                 
611C: 45              LD      B,L                 
611D: 98              SBC     B                   
611E: 20 13           JR      NZ,$6133            ; {}
6120: 76              HALT                        
6121: 76              HALT                        
6122: 49              LD      C,C                 
6123: 59              LD      E,C                 
6124: BC              CP      H                   
6125: BD              CP      L                   
6126: BC              CP      H                   
6127: BD              CP      L                   
6128: BC              CP      H                   
6129: BD              CP      L                   
612A: BC              CP      H                   
612B: BD              CP      L                   
612C: BC              CP      H                   
612D: BD              CP      L                   
612E: 44              LD      B,H                 
612F: 56              LD      D,(HL)              
6130: 44              LD      B,H                 
6131: 56              LD      D,(HL)              
6132: 55              LD      D,L                 
6133: 56              LD      D,(HL)              
6134: 98              SBC     B                   
6135: 40              LD      B,B                 
6136: 13              INC     DE                  
6137: 45              LD      B,L                 
6138: 45              LD      B,L                 
6139: 52              LD      D,D                 
613A: 59              LD      E,C                 
613B: AC              XOR     H                   
613C: AD              XOR     L                   
613D: AC              XOR     H                   
613E: AD              XOR     L                   
613F: AC              XOR     H                   
6140: AD              XOR     L                   
6141: AC              XOR     H                   
6142: AD              XOR     L                   
6143: AA              XOR     D                   
6144: AB              XOR     E                   
6145: 44              LD      B,H                 
6146: 56              LD      D,(HL)              
6147: 44              LD      B,H                 
6148: 56              LD      D,(HL)              
6149: 55              LD      D,L                 
614A: 56              LD      D,(HL)              
614B: 98              SBC     B                   
614C: 60              LD      H,B                 
614D: 13              INC     DE                  
614E: 55              LD      D,L                 
614F: 56              LD      D,(HL)              
6150: 55              LD      D,L                 
6151: 47              LD      B,A                 
6152: BC              CP      H                   
6153: BD              CP      L                   
6154: BC              CP      H                   
6155: BD              CP      L                   
6156: BC              CP      H                   
6157: BD              CP      L                   
6158: BC              CP      H                   
6159: BD              CP      L                   
615A: BA              CP      D                   
615B: BB              CP      E                   
615C: 54              LD      D,H                 
615D: 56              LD      D,(HL)              
615E: 44              LD      B,H                 
615F: 56              LD      D,(HL)              
6160: 55              LD      D,L                 
6161: 56              LD      D,(HL)              
6162: 98              SBC     B                   
6163: 80              ADD     A,B                 
6164: 13              INC     DE                  
6165: 55              LD      D,L                 
6166: 56              LD      D,(HL)              
6167: 55              LD      D,L                 
6168: 47              LD      B,A                 
6169: AC              XOR     H                   
616A: AD              XOR     L                   
616B: AC              XOR     H                   
616C: AD              XOR     L                   
616D: AC              XOR     H                   
616E: AD              XOR     L                   
616F: AC              XOR     H                   
6170: AD              XOR     L                   
6171: AC              XOR     H                   
6172: AD              XOR     L                   
6173: AC              XOR     H                   
6174: AD              XOR     L                   
6175: 44              LD      B,H                 
6176: 56              LD      D,(HL)              
6177: 55              LD      D,L                 
6178: 56              LD      D,(HL)              
6179: 98              SBC     B                   
617A: A0              AND     B                   
617B: 13              INC     DE                  
617C: 55              LD      D,L                 
617D: 56              LD      D,(HL)              
617E: 55              LD      D,L                 
617F: 57              LD      D,A                 
6180: BC              CP      H                   
6181: BD              CP      L                   
6182: BC              CP      H                   
6183: BD              CP      L                   
6184: BC              CP      H                   
6185: BD              CP      L                   
6186: BC              CP      H                   
6187: BD              CP      L                   
6188: BC              CP      H                   
6189: BD              CP      L                   
618A: BC              CP      H                   
618B: BD              CP      L                   
618C: 54              LD      D,H                 
618D: 56              LD      D,(HL)              
618E: 55              LD      D,L                 
618F: 56              LD      D,(HL)              
6190: 98              SBC     B                   
6191: C0              RET     NZ                  
6192: 13              INC     DE                  
6193: AC              XOR     H                   
6194: AD              XOR     L                   
6195: AC              XOR     H                   
6196: AD              XOR     L                   
6197: AC              XOR     H                   
6198: AD              XOR     L                   
6199: AC              XOR     H                   
619A: AD              XOR     L                   
619B: AC              XOR     H                   
619C: AD              XOR     L                   
619D: AE              XOR     (HL)                
619E: AF              XOR     A                   
619F: AC              XOR     H                   
61A0: AD              XOR     L                   
61A1: AC              XOR     H                   
61A2: AD              XOR     L                   
61A3: AA              XOR     D                   
61A4: AB              XOR     E                   
61A5: AC              XOR     H                   
61A6: AD              XOR     L                   
61A7: 98              SBC     B                   
61A8: E0 13           LD      ($FF00+$13),A       
61AA: BC              CP      H                   
61AB: BD              CP      L                   
61AC: BC              CP      H                   
61AD: BD              CP      L                   
61AE: BC              CP      H                   
61AF: BD              CP      L                   
61B0: BC              CP      H                   
61B1: BD              CP      L                   
61B2: BC              CP      H                   
61B3: BD              CP      L                   
61B4: BE              CP      (HL)                
61B5: BF              CP      A                   
61B6: BC              CP      H                   
61B7: BD              CP      L                   
61B8: BC              CP      H                   
61B9: BD              CP      L                   
61BA: BA              CP      D                   
61BB: BB              CP      E                   
61BC: BC              CP      H                   
61BD: BD              CP      L                   
61BE: 99              SBC     C                   
61BF: 00              NOP                         
61C0: 13              INC     DE                  
61C1: 4A              LD      C,D                 
61C2: 4A              LD      C,D                 
61C3: 4A              LD      C,D                 
61C4: 4D              LD      C,L                 
61C5: AC              XOR     H                   
61C6: AD              XOR     L                   
61C7: AC              XOR     H                   
61C8: AD              XOR     L                   
61C9: AE              XOR     (HL)                
61CA: AF              XOR     A                   
61CB: AC              XOR     H                   
61CC: AD              XOR     L                   
61CD: AC              XOR     H                   
61CE: AD              XOR     L                   
61CF: A8              XOR     B                   
61D0: A9              XOR     C                   
61D1: AC              XOR     H                   
61D2: AD              XOR     L                   
61D3: AC              XOR     H                   
61D4: AD              XOR     L                   
61D5: 99              SBC     C                   
61D6: 20 13           JR      NZ,$61EB            ; {}
61D8: 45              LD      B,L                 
61D9: 45              LD      B,L                 
61DA: 5D              LD      E,L                 
61DB: 59              LD      E,C                 
61DC: BC              CP      H                   
61DD: BD              CP      L                   
61DE: BC              CP      H                   
61DF: BD              CP      L                   
61E0: BE              CP      (HL)                
61E1: BF              CP      A                   
61E2: BC              CP      H                   
61E3: BD              CP      L                   
61E4: BC              CP      H                   
61E5: BD              CP      L                   
61E6: B8              CP      B                   
61E7: B9              CP      C                   
61E8: BC              CP      H                   
61E9: BD              CP      L                   
61EA: BC              CP      H                   
61EB: BD              CP      L                   
61EC: 99              SBC     C                   
61ED: 40              LD      B,B                 
61EE: 13              INC     DE                  
61EF: 76              HALT                        
61F0: 76              HALT                        
61F1: 49              LD      C,C                 
61F2: 59              LD      E,C                 
61F3: 1C              INC     E                   
61F4: 1D              DEC     E                   
61F5: 1C              INC     E                   
61F6: 1D              DEC     E                   
61F7: 1C              INC     E                   
61F8: 1D              DEC     E                   
61F9: 1C              INC     E                   
61FA: 1D              DEC     E                   
61FB: 1C              INC     E                   
61FC: 1D              DEC     E                   
61FD: 1C              INC     E                   
61FE: 1D              DEC     E                   
61FF: 1C              INC     E                   
6200: 1D              DEC     E                   
6201: 1C              INC     E                   
6202: 1D              DEC     E                   
6203: 99              SBC     C                   
6204: 60              LD      H,B                 
6205: 13              INC     DE                  
6206: 76              HALT                        
6207: 76              HALT                        
6208: 49              LD      C,C                 
6209: 59              LD      E,C                 
620A: 1E 1F           LD      E,$1F               
620C: 1E 1F           LD      E,$1F               
620E: 1E 1F           LD      E,$1F               
6210: 1E 1F           LD      E,$1F               
6212: 1E 1F           LD      E,$1F               
6214: 1E 1F           LD      E,$1F               
6216: 1E 1F           LD      E,$1F               
6218: 1E 1F           LD      E,$1F               
621A: 99              SBC     C                   
621B: 80              ADD     A,B                 
621C: 13              INC     DE                  
621D: 45              LD      B,L                 
621E: 45              LD      B,L                 
621F: 52              LD      D,D                 
6220: 59              LD      E,C                 
6221: 1E 1F           LD      E,$1F               
6223: 1E 1F           LD      E,$1F               
6225: 1E 1F           LD      E,$1F               
6227: 1E 1F           LD      E,$1F               
6229: 1E 1F           LD      E,$1F               
622B: 1E 1F           LD      E,$1F               
622D: 1E 1F           LD      E,$1F               
622F: 1E 1F           LD      E,$1F               
6231: 99              SBC     C                   
6232: A0              AND     B                   
6233: 13              INC     DE                  
6234: 55              LD      D,L                 
6235: 56              LD      D,(HL)              
6236: 55              LD      D,L                 
6237: 47              LD      B,A                 
6238: 1E 1F           LD      E,$1F               
623A: 1E 1F           LD      E,$1F               
623C: 1E 1F           LD      E,$1F               
623E: 1E 1F           LD      E,$1F               
6240: 1E 1F           LD      E,$1F               
6242: 1E 1F           LD      E,$1F               
6244: 1E 1F           LD      E,$1F               
6246: 1E 1F           LD      E,$1F               
6248: 99              SBC     C                   
6249: C0              RET     NZ                  
624A: 13              INC     DE                  
624B: 55              LD      D,L                 
624C: 56              LD      D,(HL)              
624D: 55              LD      D,L                 
624E: 47              LD      B,A                 
624F: 1E 1F           LD      E,$1F               
6251: 1E 1F           LD      E,$1F               
6253: 1E 1F           LD      E,$1F               
6255: 1E 1F           LD      E,$1F               
6257: 1E 1F           LD      E,$1F               
6259: 1E 1F           LD      E,$1F               
625B: 1E 1F           LD      E,$1F               
625D: 1E 1F           LD      E,$1F               
625F: 99              SBC     C                   
6260: E0 13           LD      ($FF00+$13),A       
6262: 55              LD      D,L                 
6263: 56              LD      D,(HL)              
6264: 55              LD      D,L                 
6265: 57              LD      D,A                 
6266: 1E 1F           LD      E,$1F               
6268: 1E 1F           LD      E,$1F               
626A: 1E 1F           LD      E,$1F               
626C: 1E 1F           LD      E,$1F               
626E: 1E 1F           LD      E,$1F               
6270: 1E 1F           LD      E,$1F               
6272: 1E 1F           LD      E,$1F               
6274: 1E 1F           LD      E,$1F               
6276: 9A              SBC     D                   
6277: 00              NOP                         
6278: 13              INC     DE                  
6279: 1E 1F           LD      E,$1F               
627B: 1E 1F           LD      E,$1F               
627D: 1E 1F           LD      E,$1F               
627F: 1E 1F           LD      E,$1F               
6281: 1E 1F           LD      E,$1F               
6283: 1E 1F           LD      E,$1F               
6285: 1E 1F           LD      E,$1F               
6287: 1E 1F           LD      E,$1F               
6289: 1E 1F           LD      E,$1F               
628B: 1E 1F           LD      E,$1F               
628D: 9A              SBC     D                   
628E: 20 13           JR      NZ,$62A3            ; {}
6290: 1E 1F           LD      E,$1F               
6292: 1E 1F           LD      E,$1F               
6294: 1E 1F           LD      E,$1F               
6296: 1E 1F           LD      E,$1F               
6298: 1E 1F           LD      E,$1F               
629A: 1E 1F           LD      E,$1F               
629C: 1E 1F           LD      E,$1F               
629E: 1E 1F           LD      E,$1F               
62A0: 1E 1F           LD      E,$1F               
62A2: 1E 1F           LD      E,$1F               
62A4: 00              NOP                         
62A5: 98              SBC     B                   
62A6: 00              NOP                         
62A7: 53              LD      D,E                 
62A8: AC              XOR     H                   
62A9: 98              SBC     B                   
62AA: 20 53           JR      NZ,$62FF            ; {}
62AC: AC              XOR     H                   
62AD: 98              SBC     B                   
62AE: 40              LD      B,B                 
62AF: 53              LD      D,E                 
62B0: AC              XOR     H                   
62B1: 98              SBC     B                   
62B2: 60              LD      H,B                 
62B3: 53              LD      D,E                 
62B4: AC              XOR     H                   
62B5: 98              SBC     B                   
62B6: 80              ADD     A,B                 
62B7: 53              LD      D,E                 
62B8: AC              XOR     H                   
62B9: 98              SBC     B                   
62BA: A0              AND     B                   
62BB: 53              LD      D,E                 
62BC: AC              XOR     H                   
62BD: 98              SBC     B                   
62BE: C0              RET     NZ                  
62BF: 53              LD      D,E                 
62C0: AC              XOR     H                   
62C1: 98              SBC     B                   
62C2: E0 53           LD      ($FF00+$53),A       
62C4: AC              XOR     H                   
62C5: 99              SBC     C                   
62C6: 00              NOP                         
62C7: 53              LD      D,E                 
62C8: AC              XOR     H                   
62C9: 99              SBC     C                   
62CA: 20 53           JR      NZ,$631F            ; {}
62CC: AC              XOR     H                   
62CD: 99              SBC     C                   
62CE: 40              LD      B,B                 
62CF: 53              LD      D,E                 
62D0: AC              XOR     H                   
62D1: 99              SBC     C                   
62D2: 60              LD      H,B                 
62D3: 53              LD      D,E                 
62D4: AC              XOR     H                   
62D5: 99              SBC     C                   
62D6: 80              ADD     A,B                 
62D7: 53              LD      D,E                 
62D8: AC              XOR     H                   
62D9: 99              SBC     C                   
62DA: A0              AND     B                   
62DB: 53              LD      D,E                 
62DC: AC              XOR     H                   
62DD: 99              SBC     C                   
62DE: C0              RET     NZ                  
62DF: 53              LD      D,E                 
62E0: AC              XOR     H                   
62E1: 99              SBC     C                   
62E2: E0 53           LD      ($FF00+$53),A       
62E4: AC              XOR     H                   
62E5: 9A              SBC     D                   
62E6: 00              NOP                         
62E7: 53              LD      D,E                 
62E8: AC              XOR     H                   
62E9: 9A              SBC     D                   
62EA: 20 53           JR      NZ,$633F            ; {}
62EC: AC              XOR     H                   
62ED: 98              SBC     B                   
62EE: 49              LD      C,C                 
62EF: 00              NOP                         
62F0: 1F              RRA                         
62F1: 98              SBC     B                   
62F2: 68              LD      L,B                 
62F3: 02              LD      (BC),A              
62F4: 06 15           LD      B,$15               
62F6: 0A              LD      A,(BC)              
62F7: 98              SBC     B                   
62F8: 88              ADC     A,B                 
62F9: 02              LD      (BC),A              
62FA: 16 15           LD      D,$15               
62FC: 1A              LD      A,(DE)              
62FD: 98              SBC     B                   
62FE: A7              AND     A                   
62FF: 04              INC     B                   
6300: 07              RLCA                        
6301: 15              DEC     D                   
6302: 15              DEC     D                   
6303: 15              DEC     D                   
6304: 19              ADD     HL,DE               
6305: 98              SBC     B                   
6306: C6 07           ADD     $07                 
6308: 07              RLCA                        
6309: 15              DEC     D                   
630A: 15              DEC     D                   
630B: 15              DEC     D                   
630C: 15              DEC     D                   
630D: 15              DEC     D                   
630E: 08 09 98        LD      ($9809),SP          
6311: E5              PUSH    HL                  
6312: 09              ADD     HL,BC               
6313: 07              RLCA                        
6314: 15              DEC     D                   
6315: 15              DEC     D                   
6316: 15              DEC     D                   
6317: 15              DEC     D                   
6318: 15              DEC     D                   
6319: 15              DEC     D                   
631A: 15              DEC     D                   
631B: 15              DEC     D                   
631C: 19              ADD     HL,DE               
631D: 99              SBC     C                   
631E: 03              INC     BC                  
631F: 0D              DEC     C                   
6320: 17              RLA                         
6321: 18 15           JR      $6338               ; {}
6323: 15              DEC     D                   
6324: 15              DEC     D                   
6325: 15              DEC     D                   
6326: 15              DEC     D                   
6327: 15              DEC     D                   
6328: 15              DEC     D                   
6329: 15              DEC     D                   
632A: 15              DEC     D                   
632B: 15              DEC     D                   
632C: 08 09 99        LD      ($9909),SP          
632F: 21 11 17        LD      HL,$1711            
6332: 18 15           JR      $6349               ; {}
6334: 15              DEC     D                   
6335: 15              DEC     D                   
6336: 15              DEC     D                   
6337: 15              DEC     D                   
6338: 15              DEC     D                   
6339: 15              DEC     D                   
633A: 15              DEC     D                   
633B: 15              DEC     D                   
633C: 15              DEC     D                   
633D: 15              DEC     D                   
633E: 15              DEC     D                   
633F: 15              DEC     D                   
6340: 15              DEC     D                   
6341: 08 09 99        LD      ($9909),SP          
6344: 40              LD      B,B                 
6345: 13              INC     DE                  
6346: 82              ADD     A,D                 
6347: 83              ADD     A,E                 
6348: 0C              INC     C                   
6349: 0D              DEC     C                   
634A: 0C              INC     C                   
634B: 0D              DEC     C                   
634C: 0E 0F           LD      C,$0F               
634E: 0E 0F           LD      C,$0F               
6350: 0E 0F           LD      C,$0F               
6352: 0E 0F           LD      C,$0F               
6354: 0C              INC     C                   
6355: 0D              DEC     C                   
6356: 0C              INC     C                   
6357: 0D              DEC     C                   
6358: 82              ADD     A,D                 
6359: 83              ADD     A,E                 
635A: 99              SBC     C                   
635B: 60              LD      H,B                 
635C: 01 92 93        LD      BC,$9392            
635F: 99              SBC     C                   
6360: 72              LD      (HL),D              
6361: 01 92 93        LD      BC,$9392            
6364: 00              NOP                         
6365: 9C              SBC     H                   
6366: 00              NOP                         
6367: 5F              LD      E,A                 
6368: A0              AND     B                   
6369: 9C              SBC     H                   
636A: 20 5F           JR      NZ,$63CB            ; {}
636C: A0              AND     B                   
636D: 9C              SBC     H                   
636E: 40              LD      B,B                 
636F: 5F              LD      E,A                 
6370: A0              AND     B                   
6371: 9C              SBC     H                   
6372: 60              LD      H,B                 
6373: 5F              LD      E,A                 
6374: A0              AND     B                   
6375: 9C              SBC     H                   
6376: 80              ADD     A,B                 
6377: 5F              LD      E,A                 
6378: A0              AND     B                   
6379: 9C              SBC     H                   
637A: A0              AND     B                   
637B: 5F              LD      E,A                 
637C: A0              AND     B                   
637D: 9C              SBC     H                   
637E: C0              RET     NZ                  
637F: 5F              LD      E,A                 
6380: A0              AND     B                   
6381: 9C              SBC     H                   
6382: E0 5F           LD      ($FF00+$5F),A       
6384: A0              AND     B                   
6385: 9D              SBC     L                   
6386: 00              NOP                         
6387: 5F              LD      E,A                 
6388: A0              AND     B                   
6389: 9D              SBC     L                   
638A: 20 5F           JR      NZ,$63EB            ; {}
638C: A0              AND     B                   
638D: 9D              SBC     L                   
638E: 40              LD      B,B                 
638F: 5F              LD      E,A                 
6390: A0              AND     B                   
6391: 9D              SBC     L                   
6392: 60              LD      H,B                 
6393: 5F              LD      E,A                 
6394: A0              AND     B                   
6395: 9D              SBC     L                   
6396: 80              ADD     A,B                 
6397: 5F              LD      E,A                 
6398: A0              AND     B                   
6399: 9D              SBC     L                   
639A: A0              AND     B                   
639B: 5F              LD      E,A                 
639C: A0              AND     B                   
639D: 9D              SBC     L                   
639E: C0              RET     NZ                  
639F: 5F              LD      E,A                 
63A0: A0              AND     B                   
63A1: 9D              SBC     L                   
63A2: E0 5F           LD      ($FF00+$5F),A       
63A4: A0              AND     B                   
63A5: 9E              SBC     (HL)                
63A6: 00              NOP                         
63A7: 5F              LD      E,A                 
63A8: A0              AND     B                   
63A9: 9E              SBC     (HL)                
63AA: 20 5F           JR      NZ,$640B            ; {}
63AC: A0              AND     B                   
63AD: 9E              SBC     (HL)                
63AE: 40              LD      B,B                 
63AF: 13              INC     DE                  
63B0: A0              AND     B                   
63B1: A0              AND     B                   
63B2: A0              AND     B                   
63B3: A0              AND     B                   
63B4: A0              AND     B                   
63B5: 83              ADD     A,E                 
63B6: 84              ADD     A,H                 
63B7: 85              ADD     A,L                 
63B8: 86              ADD     A,(HL)              
63B9: 87              ADD     A,A                 
63BA: 88              ADC     A,B                 
63BB: 89              ADC     A,C                 
63BC: 8A              ADC     A,D                 
63BD: 8B              ADC     A,E                 
63BE: 8C              ADC     A,H                 
63BF: A0              AND     B                   
63C0: A0              AND     B                   
63C1: A0              AND     B                   
63C2: A0              AND     B                   
63C3: A0              AND     B                   
63C4: 9E              SBC     (HL)                
63C5: 60              LD      H,B                 
63C6: 13              INC     DE                  
63C7: A0              AND     B                   
63C8: A0              AND     B                   
63C9: A0              AND     B                   
63CA: A0              AND     B                   
63CB: 92              SUB     D                   
63CC: 93              SUB     E                   
63CD: 94              SUB     H                   
63CE: 95              SUB     L                   
63CF: 96              SUB     (HL)                
63D0: 97              SUB     A                   
63D1: 98              SBC     B                   
63D2: 99              SBC     C                   
63D3: 9A              SBC     D                   
63D4: 9B              SBC     E                   
63D5: 9C              SBC     H                   
63D6: 9D              SBC     L                   
63D7: A0              AND     B                   
63D8: A0              AND     B                   
63D9: A0              AND     B                   
63DA: A0              AND     B                   
63DB: 9E              SBC     (HL)                
63DC: 80              ADD     A,B                 
63DD: 13              INC     DE                  
63DE: A0              AND     B                   
63DF: A0              AND     B                   
63E0: A0              AND     B                   
63E1: A1              AND     C                   
63E2: A2              AND     D                   
63E3: A3              AND     E                   
63E4: A4              AND     H                   
63E5: A5              AND     L                   
63E6: A6              AND     (HL)                
63E7: A7              AND     A                   
63E8: A8              XOR     B                   
63E9: A9              XOR     C                   
63EA: AA              XOR     D                   
63EB: AB              XOR     E                   
63EC: AC              XOR     H                   
63ED: AD              XOR     L                   
63EE: AE              XOR     (HL)                
63EF: A0              AND     B                   
63F0: A0              AND     B                   
63F1: A0              AND     B                   
63F2: 9E              SBC     (HL)                
63F3: A0              AND     B                   
63F4: 13              INC     DE                  
63F5: A0              AND     B                   
63F6: A0              AND     B                   
63F7: B0              OR      B                   
63F8: B1              OR      C                   
63F9: B2              OR      D                   
63FA: B3              OR      E                   
63FB: B4              OR      H                   
63FC: B5              OR      L                   
63FD: B6              OR      (HL)                
63FE: B7              OR      A                   
63FF: B8              CP      B                   
6400: B9              CP      C                   
6401: BA              CP      D                   
6402: BB              CP      E                   
6403: BC              CP      H                   
6404: BD              CP      L                   
6405: BE              CP      (HL)                
6406: BF              CP      A                   
6407: A0              AND     B                   
6408: A0              AND     B                   
6409: 9E              SBC     (HL)                
640A: C0              RET     NZ                  
640B: 13              INC     DE                  
640C: A0              AND     B                   
640D: A0              AND     B                   
640E: C0              RET     NZ                  
640F: C1              POP     BC                  
6410: C2 C3 C4        JP      NZ,$C4C3            
6413: C5              PUSH    BC                  
6414: C6 C7           ADD     $C7                 
6416: 8E              ADC     A,(HL)              
6417: 8F              ADC     A,A                 
6418: CA CB CC        JP      Z,$CCCB             
641B: CD CE CF        CALL    $CFCE               
641E: A0              AND     B                   
641F: A0              AND     B                   
6420: 9E              SBC     (HL)                
6421: E0 13           LD      ($FF00+$13),A       
6423: A0              AND     B                   
6424: A0              AND     B                   
6425: A0              AND     B                   
6426: 82              ADD     A,D                 
6427: F2                              
6428: F3              DI                          
6429: F4                              
642A: F5              PUSH    AF                  
642B: F6 F7           OR      $F7                 
642D: F8 F9           LD      HL,SP+$F9           
642F: FA FB FC        LD      A,($FCFB)           
6432: FD                              
6433: 8D              ADC     A,L                 
6434: A0              AND     B                   
6435: A0              AND     B                   
6436: A0              AND     B                   
6437: 9F              SBC     A                   
6438: 00              NOP                         
6439: 13              INC     DE                  
643A: A0              AND     B                   
643B: A0              AND     B                   
643C: A0              AND     B                   
643D: A0              AND     B                   
643E: A0              AND     B                   
643F: A0              AND     B                   
6440: 80              ADD     A,B                 
6441: 81              ADD     A,C                 
6442: 80              ADD     A,B                 
6443: 81              ADD     A,C                 
6444: 80              ADD     A,B                 
6445: 81              ADD     A,C                 
6446: 80              ADD     A,B                 
6447: 81              ADD     A,C                 
6448: A0              AND     B                   
6449: A0              AND     B                   
644A: A0              AND     B                   
644B: A0              AND     B                   
644C: A0              AND     B                   
644D: A0              AND     B                   
644E: 9F              SBC     A                   
644F: 20 13           JR      NZ,$6464            ; {}
6451: A0              AND     B                   
6452: A0              AND     B                   
6453: A0              AND     B                   
6454: A0              AND     B                   
6455: A0              AND     B                   
6456: A0              AND     B                   
6457: 90              SUB     B                   
6458: 91              SUB     C                   
6459: 90              SUB     B                   
645A: 91              SUB     C                   
645B: 90              SUB     B                   
645C: 91              SUB     C                   
645D: 90              SUB     B                   
645E: 91              SUB     C                   
645F: A0              AND     B                   
6460: A0              AND     B                   
6461: A0              AND     B                   
6462: A0              AND     B                   
6463: A0              AND     B                   
6464: A0              AND     B                   
6465: 9F              SBC     A                   
6466: 40              LD      B,B                 
6467: 13              INC     DE                  
6468: A0              AND     B                   
6469: A0              AND     B                   
646A: A0              AND     B                   
646B: A0              AND     B                   
646C: A0              AND     B                   
646D: A0              AND     B                   
646E: 80              ADD     A,B                 
646F: 81              ADD     A,C                 
6470: 80              ADD     A,B                 
6471: 81              ADD     A,C                 
6472: 80              ADD     A,B                 
6473: 81              ADD     A,C                 
6474: 80              ADD     A,B                 
6475: 81              ADD     A,C                 
6476: A0              AND     B                   
6477: A0              AND     B                   
6478: A0              AND     B                   
6479: A0              AND     B                   
647A: A0              AND     B                   
647B: A0              AND     B                   
647C: 9F              SBC     A                   
647D: 60              LD      H,B                 
647E: 13              INC     DE                  
647F: A0              AND     B                   
6480: A0              AND     B                   
6481: A0              AND     B                   
6482: A0              AND     B                   
6483: A0              AND     B                   
6484: A0              AND     B                   
6485: 90              SUB     B                   
6486: 91              SUB     C                   
6487: 90              SUB     B                   
6488: 91              SUB     C                   
6489: 90              SUB     B                   
648A: 91              SUB     C                   
648B: 90              SUB     B                   
648C: 91              SUB     C                   
648D: A0              AND     B                   
648E: A0              AND     B                   
648F: A0              AND     B                   
6490: A0              AND     B                   
6491: A0              AND     B                   
6492: A0              AND     B                   
6493: 9F              SBC     A                   
6494: 80              ADD     A,B                 
6495: 13              INC     DE                  
6496: A0              AND     B                   
6497: A0              AND     B                   
6498: A0              AND     B                   
6499: A0              AND     B                   
649A: A0              AND     B                   
649B: A0              AND     B                   
649C: 80              ADD     A,B                 
649D: 81              ADD     A,C                 
649E: 80              ADD     A,B                 
649F: 81              ADD     A,C                 
64A0: 80              ADD     A,B                 
64A1: 81              ADD     A,C                 
64A2: 80              ADD     A,B                 
64A3: 81              ADD     A,C                 
64A4: A0              AND     B                   
64A5: A0              AND     B                   
64A6: A0              AND     B                   
64A7: A0              AND     B                   
64A8: A0              AND     B                   
64A9: A0              AND     B                   
64AA: 9F              SBC     A                   
64AB: A0              AND     B                   
64AC: 13              INC     DE                  
64AD: A0              AND     B                   
64AE: A0              AND     B                   
64AF: A0              AND     B                   
64B0: A0              AND     B                   
64B1: A0              AND     B                   
64B2: A0              AND     B                   
64B3: 90              SUB     B                   
64B4: 91              SUB     C                   
64B5: 90              SUB     B                   
64B6: 91              SUB     C                   
64B7: 90              SUB     B                   
64B8: 91              SUB     C                   
64B9: 90              SUB     B                   
64BA: 91              SUB     C                   
64BB: A0              AND     B                   
64BC: A0              AND     B                   
64BD: A0              AND     B                   
64BE: A0              AND     B                   
64BF: A0              AND     B                   
64C0: A0              AND     B                   
64C1: 9F              SBC     A                   
64C2: C0              RET     NZ                  
64C3: 13              INC     DE                  
64C4: A0              AND     B                   
64C5: A0              AND     B                   
64C6: A0              AND     B                   
64C7: A0              AND     B                   
64C8: A0              AND     B                   
64C9: A0              AND     B                   
64CA: 80              ADD     A,B                 
64CB: 81              ADD     A,C                 
64CC: 80              ADD     A,B                 
64CD: 81              ADD     A,C                 
64CE: 80              ADD     A,B                 
64CF: 81              ADD     A,C                 
64D0: 80              ADD     A,B                 
64D1: 81              ADD     A,C                 
64D2: A0              AND     B                   
64D3: A0              AND     B                   
64D4: A0              AND     B                   
64D5: A0              AND     B                   
64D6: A0              AND     B                   
64D7: A0              AND     B                   
64D8: 9F              SBC     A                   
64D9: E0 13           LD      ($FF00+$13),A       
64DB: A0              AND     B                   
64DC: A0              AND     B                   
64DD: A0              AND     B                   
64DE: A0              AND     B                   
64DF: A0              AND     B                   
64E0: A0              AND     B                   
64E1: 90              SUB     B                   
64E2: 91              SUB     C                   
64E3: 90              SUB     B                   
64E4: 91              SUB     C                   
64E5: 90              SUB     B                   
64E6: 91              SUB     C                   
64E7: 90              SUB     B                   
64E8: 91              SUB     C                   
64E9: A0              AND     B                   
64EA: A0              AND     B                   
64EB: A0              AND     B                   
64EC: A0              AND     B                   
64ED: A0              AND     B                   
64EE: A0              AND     B                   
64EF: 98              SBC     B                   
64F0: 00              NOP                         
64F1: 5F              LD      E,A                 
64F2: A0              AND     B                   
64F3: 98              SBC     B                   
64F4: 20 5F           JR      NZ,$6555            ; {}
64F6: A0              AND     B                   
64F7: 98              SBC     B                   
64F8: 40              LD      B,B                 
64F9: 5F              LD      E,A                 
64FA: A0              AND     B                   
64FB: 98              SBC     B                   
64FC: 60              LD      H,B                 
64FD: 5F              LD      E,A                 
64FE: A0              AND     B                   
64FF: 98              SBC     B                   
6500: 80              ADD     A,B                 
6501: 5F              LD      E,A                 
6502: A0              AND     B                   
6503: 98              SBC     B                   
6504: A0              AND     B                   
6505: 5F              LD      E,A                 
6506: A0              AND     B                   
6507: 98              SBC     B                   
6508: C0              RET     NZ                  
6509: 5F              LD      E,A                 
650A: A0              AND     B                   
650B: 98              SBC     B                   
650C: E0 5F           LD      ($FF00+$5F),A       
650E: A0              AND     B                   
650F: 99              SBC     C                   
6510: 00              NOP                         
6511: 5F              LD      E,A                 
6512: A0              AND     B                   
6513: 99              SBC     C                   
6514: 20 5F           JR      NZ,$6575            ; {}
6516: A0              AND     B                   
6517: 99              SBC     C                   
6518: 40              LD      B,B                 
6519: 5F              LD      E,A                 
651A: A0              AND     B                   
651B: 99              SBC     C                   
651C: 60              LD      H,B                 
651D: 5F              LD      E,A                 
651E: A0              AND     B                   
651F: 99              SBC     C                   
6520: 80              ADD     A,B                 
6521: 5F              LD      E,A                 
6522: A0              AND     B                   
6523: 99              SBC     C                   
6524: A0              AND     B                   
6525: 5F              LD      E,A                 
6526: A0              AND     B                   
6527: 99              SBC     C                   
6528: C0              RET     NZ                  
6529: 5F              LD      E,A                 
652A: A0              AND     B                   
652B: 99              SBC     C                   
652C: E0 5F           LD      ($FF00+$5F),A       
652E: A0              AND     B                   
652F: 9A              SBC     D                   
6530: 00              NOP                         
6531: 5F              LD      E,A                 
6532: A0              AND     B                   
6533: 9A              SBC     D                   
6534: 20 5F           JR      NZ,$6595            ; {}
6536: A0              AND     B                   
6537: 9B              SBC     E                   
6538: 00              NOP                         
6539: 5F              LD      E,A                 
653A: A0              AND     B                   
653B: 9B              SBC     E                   
653C: 20 5F           JR      NZ,$659D            ; {}
653E: A0              AND     B                   
653F: 9B              SBC     E                   
6540: 40              LD      B,B                 
6541: 5F              LD      E,A                 
6542: A0              AND     B                   
6543: 9B              SBC     E                   
6544: 80              ADD     A,B                 
6545: 5F              LD      E,A                 
6546: A0              AND     B                   
6547: 9B              SBC     E                   
6548: A0              AND     B                   
6549: 5F              LD      E,A                 
654A: A0              AND     B                   
654B: 9B              SBC     E                   
654C: C0              RET     NZ                  
654D: 5F              LD      E,A                 
654E: A0              AND     B                   
654F: 9B              SBC     E                   
6550: E0 5F           LD      ($FF00+$5F),A       
6552: A0              AND     B                   
6553: 98              SBC     B                   
6554: 80              ADD     A,B                 
6555: 13              INC     DE                  
6556: A0              AND     B                   
6557: A0              AND     B                   
6558: A0              AND     B                   
6559: A0              AND     B                   
655A: A0              AND     B                   
655B: A0              AND     B                   
655C: A0              AND     B                   
655D: A0              AND     B                   
655E: A0              AND     B                   
655F: A0              AND     B                   
6560: A0              AND     B                   
6561: A0              AND     B                   
6562: A0              AND     B                   
6563: 03              INC     BC                  
6564: 04              INC     B                   
6565: 03              INC     BC                  
6566: 04              INC     B                   
6567: A0              AND     B                   
6568: A0              AND     B                   
6569: A0              AND     B                   
656A: 98              SBC     B                   
656B: A0              AND     B                   
656C: 13              INC     DE                  
656D: A0              AND     B                   
656E: A0              AND     B                   
656F: A0              AND     B                   
6570: A0              AND     B                   
6571: A0              AND     B                   
6572: A0              AND     B                   
6573: A0              AND     B                   
6574: A0              AND     B                   
6575: 03              INC     BC                  
6576: 04              INC     B                   
6577: A0              AND     B                   
6578: A0              AND     B                   
6579: 02              LD      (BC),A              
657A: 10 11           ;;STOP    $11                 
657C: 10 30           ;;STOP    $30                 
657E: 04              INC     B                   
657F: 03              INC     BC                  
6580: 04              INC     B                   
6581: 98              SBC     B                   
6582: C0              RET     NZ                  
6583: 13              INC     DE                  
6584: A0              AND     B                   
6585: A0              AND     B                   
6586: A0              AND     B                   
6587: A0              AND     B                   
6588: A0              AND     B                   
6589: 12              LD      (DE),A              
658A: 04              INC     B                   
658B: 03              INC     BC                  
658C: 30 30           JR      NC,$65BE            ; {}
658E: 30 04           JR      NC,$6594            ; {}
6590: 00              NOP                         
6591: 01 00 6B        LD      BC,$6B00            
6594: 30 30           JR      NC,$65C6            ; {}
6596: 30 30           JR      NC,$65C8            ; {}
6598: 98              SBC     B                   
6599: E0 13           LD      ($FF00+$13),A       
659B: A0              AND     B                   
659C: A0              AND     B                   
659D: A0              AND     B                   
659E: A0              AND     B                   
659F: 02              LD      (BC),A              
65A0: 5A              LD      E,D                 
65A1: 10 30           ;;STOP    $30                 
65A3: 30 30           JR      NC,$65D5            ; {}
65A5: 30 10           JR      NC,$65B7            ; {}
65A7: 04              INC     B                   
65A8: A0              AND     B                   
65A9: 03              INC     BC                  
65AA: 30 30           JR      NC,$65DC            ; {}
65AC: 11 10 11        LD      DE,$1110            
65AF: 99              SBC     C                   
65B0: 00              NOP                         
65B1: 13              INC     DE                  
65B2: A0              AND     B                   
65B3: A0              AND     B                   
65B4: A0              AND     B                   
65B5: A0              AND     B                   
65B6: 00              NOP                         
65B7: 01 00 10        LD      BC,$1000            
65BA: 11 21 00        LD      DE,$0021            
65BD: 00              NOP                         
65BE: 21 12 5A        LD      HL,$5A12            
65C1: 10 11           ;;STOP    $11                 
65C3: 01 00 01        LD      BC,$0100            
65C6: 99              SBC     C                   
65C7: 20 13           JR      NZ,$65DC            ; {}
65C9: 04              INC     B                   
65CA: A0              AND     B                   
65CB: A0              AND     B                   
65CC: A0              AND     B                   
65CD: A0              AND     B                   
65CE: A0              AND     B                   
65CF: A0              AND     B                   
65D0: 00              NOP                         
65D1: 01 A0 A0        LD      BC,$A0A0            
65D4: A0              AND     B                   
65D5: A0              AND     B                   
65D6: 00              NOP                         
65D7: 01 00 01        LD      BC,$0100            
65DA: A0              AND     B                   
65DB: A0              AND     B                   
65DC: A0              AND     B                   
65DD: 99              SBC     C                   
65DE: 40              LD      B,B                 
65DF: 13              INC     DE                  
65E0: 30 04           JR      NC,$65E6            ; {}
65E2: A0              AND     B                   
65E3: A0              AND     B                   
65E4: A0              AND     B                   
65E5: A0              AND     B                   
65E6: A0              AND     B                   
65E7: A0              AND     B                   
65E8: A0              AND     B                   
65E9: A0              AND     B                   
65EA: A0              AND     B                   
65EB: A0              AND     B                   
65EC: A0              AND     B                   
65ED: A0              AND     B                   
65EE: A0              AND     B                   
65EF: A0              AND     B                   
65F0: A0              AND     B                   
65F1: A0              AND     B                   
65F2: A0              AND     B                   
65F3: A0              AND     B                   
65F4: 99              SBC     C                   
65F5: 60              LD      H,B                 
65F6: 13              INC     DE                  
65F7: 10 0F           ;;STOP    $0F                 
65F9: A0              AND     B                   
65FA: A0              AND     B                   
65FB: A0              AND     B                   
65FC: A0              AND     B                   
65FD: A0              AND     B                   
65FE: A0              AND     B                   
65FF: A0              AND     B                   
6600: A0              AND     B                   
6601: A0              AND     B                   
6602: A0              AND     B                   
6603: A0              AND     B                   
6604: A0              AND     B                   
6605: A0              AND     B                   
6606: A0              AND     B                   
6607: 03              INC     BC                  
6608: 04              INC     B                   
6609: A0              AND     B                   
660A: A0              AND     B                   
660B: 99              SBC     C                   
660C: 80              ADD     A,B                 
660D: 13              INC     DE                  
660E: A0              AND     B                   
660F: A0              AND     B                   
6610: A0              AND     B                   
6611: A0              AND     B                   
6612: A0              AND     B                   
6613: A0              AND     B                   
6614: A0              AND     B                   
6615: A0              AND     B                   
6616: A0              AND     B                   
6617: A0              AND     B                   
6618: A0              AND     B                   
6619: A0              AND     B                   
661A: A0              AND     B                   
661B: A0              AND     B                   
661C: A0              AND     B                   
661D: 12              LD      (DE),A              
661E: 30 30           JR      NC,$6650            ; {}
6620: 04              INC     B                   
6621: A0              AND     B                   
6622: 99              SBC     C                   
6623: A0              AND     B                   
6624: 13              INC     DE                  
6625: A0              AND     B                   
6626: A0              AND     B                   
6627: A0              AND     B                   
6628: A0              AND     B                   
6629: A0              AND     B                   
662A: A0              AND     B                   
662B: A0              AND     B                   
662C: A0              AND     B                   
662D: A0              AND     B                   
662E: A0              AND     B                   
662F: A0              AND     B                   
6630: 03              INC     BC                  
6631: 04              INC     B                   
6632: A0              AND     B                   
6633: 02              LD      (BC),A              
6634: 5A              LD      E,D                 
6635: 20 10           JR      NZ,$6647            ; {}
6637: 0F              RRCA                        
6638: A0              AND     B                   
6639: 99              SBC     C                   
663A: C0              RET     NZ                  
663B: 13              INC     DE                  
663C: A0              AND     B                   
663D: A0              AND     B                   
663E: A0              AND     B                   
663F: A0              AND     B                   
6640: A0              AND     B                   
6641: A0              AND     B                   
6642: 12              LD      (DE),A              
6643: 04              INC     B                   
6644: 03              INC     BC                  
6645: 30 30           JR      NC,$6677            ; {}
6647: 30 0F           JR      NC,$6658            ; {}
6649: A0              AND     B                   
664A: 00              NOP                         
664B: 01 00 01        LD      BC,$0100            
664E: A0              AND     B                   
664F: A0              AND     B                   
6650: 99              SBC     C                   
6651: E0 13           LD      ($FF00+$13),A       
6653: A0              AND     B                   
6654: 12              LD      (DE),A              
6655: 04              INC     B                   
6656: A0              AND     B                   
6657: A0              AND     B                   
6658: A0              AND     B                   
6659: 00              NOP                         
665A: 20 10           JR      NZ,$666C            ; {}
665C: 10 10           ;;STOP    $10                 
665E: 30 04           JR      NC,$6664            ; {}
6660: A0              AND     B                   
6661: A0              AND     B                   
6662: A0              AND     B                   
6663: A0              AND     B                   
6664: A0              AND     B                   
6665: A0              AND     B                   
6666: A0              AND     B                   
6667: 9A              SBC     D                   
6668: 00              NOP                         
6669: 13              INC     DE                  
666A: A0              AND     B                   
666B: 00              NOP                         
666C: 10 04           ;;STOP    $04                 
666E: 03              INC     BC                  
666F: 04              INC     B                   
6670: 03              INC     BC                  
6671: 71              LD      (HL),C              
6672: 6B              LD      L,E                 
6673: 10 10           ;;STOP    $10                 
6675: 10 0F           ;;STOP    $0F                 
6677: A0              AND     B                   
6678: A0              AND     B                   
6679: A0              AND     B                   
667A: A0              AND     B                   
667B: 03              INC     BC                  
667C: 04              INC     B                   
667D: A0              AND     B                   
667E: 9A              SBC     D                   
667F: 20 13           JR      NZ,$6694            ; {}
6681: A0              AND     B                   
6682: 02              LD      (BC),A              
6683: 5A              LD      E,D                 
6684: 10 30           ;;STOP    $30                 
6686: 11 10 30        LD      DE,$3010            
6689: 11 11 11        LD      DE,$1111            
668C: 01 A0 A0        LD      BC,$A0A0            
668F: 12              LD      (DE),A              
6690: 04              INC     B                   
6691: 03              INC     BC                  
6692: 30 0F           JR      NC,$66A3            ; {}
6694: A0              AND     B                   
6695: 9A              SBC     D                   
6696: 40              LD      B,B                 
6697: 53              LD      D,E                 
6698: A0              AND     B                   
6699: 9A              SBC     D                   
669A: 60              LD      H,B                 
669B: 53              LD      D,E                 
669C: A0              AND     B                   
669D: 9A              SBC     D                   
669E: 80              ADD     A,B                 
669F: 53              LD      D,E                 
66A0: A0              AND     B                   
66A1: 9A              SBC     D                   
66A2: A0              AND     B                   
66A3: 53              LD      D,E                 
66A4: A0              AND     B                   
66A5: 9A              SBC     D                   
66A6: C0              RET     NZ                  
66A7: 53              LD      D,E                 
66A8: A0              AND     B                   
66A9: 9A              SBC     D                   
66AA: E0 53           LD      ($FF00+$53),A       
66AC: A0              AND     B                   
66AD: 9B              SBC     E                   
66AE: 00              NOP                         
66AF: 53              LD      D,E                 
66B0: A0              AND     B                   
66B1: 9B              SBC     E                   
66B2: 20 53           JR      NZ,$6707            ; {}
66B4: A0              AND     B                   
66B5: 9B              SBC     E                   
66B6: 40              LD      B,B                 
66B7: 53              LD      D,E                 
66B8: A0              AND     B                   
66B9: 9B              SBC     E                   
66BA: 60              LD      H,B                 
66BB: 53              LD      D,E                 
66BC: A0              AND     B                   
66BD: 9B              SBC     E                   
66BE: 80              ADD     A,B                 
66BF: 53              LD      D,E                 
66C0: A0              AND     B                   
66C1: 9B              SBC     E                   
66C2: A0              AND     B                   
66C3: 53              LD      D,E                 
66C4: A0              AND     B                   
66C5: 9B              SBC     E                   
66C6: C0              RET     NZ                  
66C7: 53              LD      D,E                 
66C8: A0              AND     B                   
66C9: 9B              SBC     E                   
66CA: E0 53           LD      ($FF00+$53),A       
66CC: A0              AND     B                   
66CD: 00              NOP                         
66CE: 98              SBC     B                   
66CF: 00              NOP                         
66D0: 5F              LD      E,A                 
66D1: AC              XOR     H                   
66D2: 98              SBC     B                   
66D3: 20 5F           JR      NZ,$6734            ; {}
66D5: AC              XOR     H                   
66D6: 98              SBC     B                   
66D7: 40              LD      B,B                 
66D8: 5F              LD      E,A                 
66D9: AC              XOR     H                   
66DA: 98              SBC     B                   
66DB: 60              LD      H,B                 
66DC: 5F              LD      E,A                 
66DD: AC              XOR     H                   
66DE: 98              SBC     B                   
66DF: 80              ADD     A,B                 
66E0: 5F              LD      E,A                 
66E1: AC              XOR     H                   
66E2: 98              SBC     B                   
66E3: A0              AND     B                   
66E4: 5F              LD      E,A                 
66E5: AC              XOR     H                   
66E6: 98              SBC     B                   
66E7: C0              RET     NZ                  
66E8: 5F              LD      E,A                 
66E9: AC              XOR     H                   
66EA: 98              SBC     B                   
66EB: E0 5F           LD      ($FF00+$5F),A       
66ED: AC              XOR     H                   
66EE: 99              SBC     C                   
66EF: 00              NOP                         
66F0: 5F              LD      E,A                 
66F1: AC              XOR     H                   
66F2: 99              SBC     C                   
66F3: 20 5F           JR      NZ,$6754            ; {}
66F5: AC              XOR     H                   
66F6: 99              SBC     C                   
66F7: 40              LD      B,B                 
66F8: 5F              LD      E,A                 
66F9: AC              XOR     H                   
66FA: 99              SBC     C                   
66FB: 60              LD      H,B                 
66FC: 5F              LD      E,A                 
66FD: AC              XOR     H                   
66FE: 99              SBC     C                   
66FF: 80              ADD     A,B                 
6700: 5F              LD      E,A                 
6701: AC              XOR     H                   
6702: 99              SBC     C                   
6703: A0              AND     B                   
6704: 5F              LD      E,A                 
6705: AC              XOR     H                   
6706: 99              SBC     C                   
6707: C0              RET     NZ                  
6708: 5F              LD      E,A                 
6709: AC              XOR     H                   
670A: 99              SBC     C                   
670B: E0 5F           LD      ($FF00+$5F),A       
670D: AC              XOR     H                   
670E: 9A              SBC     D                   
670F: 00              NOP                         
6710: 5F              LD      E,A                 
6711: AC              XOR     H                   
6712: 9A              SBC     D                   
6713: 20 5F           JR      NZ,$6774            ; {}
6715: AC              XOR     H                   
6716: 98              SBC     B                   
6717: 02              LD      (BC),A              
6718: 03              INC     BC                  
6719: E5              PUSH    HL                  
671A: E6 E1           AND     $E1                 
671C: E2              LD      (C),A               
671D: 98              SBC     B                   
671E: 22              LD      (HLI),A             
671F: 03              INC     BC                  
6720: F5              PUSH    AF                  
6721: F6 F1           OR      $F1                 
6723: F2                              
6724: 98              SBC     B                   
6725: 40              LD      B,B                 
6726: 07              RLCA                        
6727: E3                              
6728: E4                              
6729: E7              RST     0X20                
672A: E8 A0           ADD     SP,$A0              
672C: A1              AND     C                   
672D: 80              ADD     A,B                 
672E: 81              ADD     A,C                 
672F: 98              SBC     B                   
6730: 52              LD      D,D                 
6731: 01 E3 E4        LD      BC,$E4E3            
6734: 98              SBC     B                   
6735: 60              LD      H,B                 
6736: 07              RLCA                        
6737: F3              DI                          
6738: F4                              
6739: F7              RST     0X30                
673A: AE              XOR     (HL)                
673B: B0              OR      B                   
673C: B1              OR      C                   
673D: 90              SUB     B                   
673E: 91              SUB     C                   
673F: 98              SBC     B                   
6740: 72              LD      (HL),D              
6741: 01 F3 F4        LD      BC,$F4F3            
6744: 98              SBC     B                   
6745: 80              ADD     A,B                 
6746: 13              INC     DE                  
6747: E7              RST     0X20                
6748: E8 AE           ADD     SP,$AE              
674A: AE              XOR     (HL)                
674B: AE              XOR     (HL)                
674C: AE              XOR     (HL)                
674D: A0              AND     B                   
674E: A1              AND     C                   
674F: 80              ADD     A,B                 
6750: 81              ADD     A,C                 
6751: E3                              
6752: E4                              
6753: E1              POP     HL                  
6754: E2              LD      (C),A               
6755: AC              XOR     H                   
6756: AC              XOR     H                   
6757: E5              PUSH    HL                  
6758: E6 E7           AND     $E7                 
675A: E8 98           ADD     SP,$98              
675C: A0              AND     B                   
675D: 13              INC     DE                  
675E: F7              RST     0X30                
675F: AE              XOR     (HL)                
6760: AE              XOR     (HL)                
6761: AE              XOR     (HL)                
6762: AE              XOR     (HL)                
6763: AE              XOR     (HL)                
6764: B0              OR      B                   
6765: B1              OR      C                   
6766: 90              SUB     B                   
6767: 91              SUB     C                   
6768: F3              DI                          
6769: F4                              
676A: F1              POP     AF                  
676B: F2                              
676C: AC              XOR     H                   
676D: AC              XOR     H                   
676E: F5              PUSH    AF                  
676F: F6 F7           OR      $F7                 
6771: AE              XOR     (HL)                
6772: 98              SBC     B                   
6773: C0              RET     NZ                  
6774: 13              INC     DE                  
6775: 82              ADD     A,D                 
6776: 83              ADD     A,E                 
6777: 82              ADD     A,D                 
6778: 83              ADD     A,E                 
6779: 82              ADD     A,D                 
677A: 83              ADD     A,E                 
677B: 82              ADD     A,D                 
677C: 83              ADD     A,E                 
677D: 82              ADD     A,D                 
677E: 83              ADD     A,E                 
677F: 82              ADD     A,D                 
6780: 83              ADD     A,E                 
6781: 82              ADD     A,D                 
6782: 83              ADD     A,E                 
6783: 82              ADD     A,D                 
6784: 83              ADD     A,E                 
6785: 82              ADD     A,D                 
6786: 83              ADD     A,E                 
6787: 82              ADD     A,D                 
6788: 83              ADD     A,E                 
6789: 98              SBC     B                   
678A: E0 13           LD      ($FF00+$13),A       
678C: 92              SUB     D                   
678D: 93              SUB     E                   
678E: 92              SUB     D                   
678F: 93              SUB     E                   
6790: 92              SUB     D                   
6791: 93              SUB     E                   
6792: 92              SUB     D                   
6793: 93              SUB     E                   
6794: 92              SUB     D                   
6795: 93              SUB     E                   
6796: 92              SUB     D                   
6797: 93              SUB     E                   
6798: 92              SUB     D                   
6799: 93              SUB     E                   
679A: 92              SUB     D                   
679B: 93              SUB     E                   
679C: 92              SUB     D                   
679D: 93              SUB     E                   
679E: 92              SUB     D                   
679F: 93              SUB     E                   
67A0: 00              NOP                         
67A1: 98              SBC     B                   
67A2: 00              NOP                         
67A3: 5F              LD      E,A                 
67A4: AC              XOR     H                   
67A5: 98              SBC     B                   
67A6: 20 5F           JR      NZ,$6807            ; {}
67A8: AC              XOR     H                   
67A9: 98              SBC     B                   
67AA: 40              LD      B,B                 
67AB: 5F              LD      E,A                 
67AC: AC              XOR     H                   
67AD: 98              SBC     B                   
67AE: 60              LD      H,B                 
67AF: 5F              LD      E,A                 
67B0: AC              XOR     H                   
67B1: 98              SBC     B                   
67B2: 80              ADD     A,B                 
67B3: 5F              LD      E,A                 
67B4: AC              XOR     H                   
67B5: 98              SBC     B                   
67B6: A0              AND     B                   
67B7: 5F              LD      E,A                 
67B8: AC              XOR     H                   
67B9: 98              SBC     B                   
67BA: C0              RET     NZ                  
67BB: 5F              LD      E,A                 
67BC: AC              XOR     H                   
67BD: 98              SBC     B                   
67BE: E0 5F           LD      ($FF00+$5F),A       
67C0: AC              XOR     H                   
67C1: 99              SBC     C                   
67C2: 00              NOP                         
67C3: 5F              LD      E,A                 
67C4: AC              XOR     H                   
67C5: 99              SBC     C                   
67C6: 20 5F           JR      NZ,$6827            ; {}
67C8: AC              XOR     H                   
67C9: 99              SBC     C                   
67CA: 40              LD      B,B                 
67CB: 5F              LD      E,A                 
67CC: AC              XOR     H                   
67CD: 99              SBC     C                   
67CE: 60              LD      H,B                 
67CF: 5F              LD      E,A                 
67D0: AC              XOR     H                   
67D1: 99              SBC     C                   
67D2: 80              ADD     A,B                 
67D3: 5F              LD      E,A                 
67D4: AC              XOR     H                   
67D5: 99              SBC     C                   
67D6: A0              AND     B                   
67D7: 5F              LD      E,A                 
67D8: AC              XOR     H                   
67D9: 99              SBC     C                   
67DA: C0              RET     NZ                  
67DB: 5F              LD      E,A                 
67DC: AC              XOR     H                   
67DD: 99              SBC     C                   
67DE: E0 5F           LD      ($FF00+$5F),A       
67E0: AC              XOR     H                   
67E1: 9A              SBC     D                   
67E2: 00              NOP                         
67E3: 5F              LD      E,A                 
67E4: AC              XOR     H                   
67E5: 9A              SBC     D                   
67E6: 20 5F           JR      NZ,$6847            ; {}
67E8: AC              XOR     H                   
67E9: 98              SBC     B                   
67EA: 00              NOP                         
67EB: 07              RLCA                        
67EC: 56              LD      D,(HL)              
67ED: 73              LD      (HL),E              
67EE: AE              XOR     (HL)                
67EF: AE              XOR     (HL)                
67F0: AE              XOR     (HL)                
67F1: AE              XOR     (HL)                
67F2: AE              XOR     (HL)                
67F3: 3E 98           LD      A,$98               
67F5: 0E 05           LD      C,$05               
67F7: 56              LD      D,(HL)              
67F8: 73              LD      (HL),E              
67F9: AE              XOR     (HL)                
67FA: AE              XOR     (HL)                
67FB: AE              XOR     (HL)                
67FC: AE              XOR     (HL)                
67FD: 98              SBC     B                   
67FE: 20 07           JR      NZ,$6807            ; {}
6800: 72              LD      (HL),D              
6801: AE              XOR     (HL)                
6802: AE              XOR     (HL)                
6803: AE              XOR     (HL)                
6804: AE              XOR     (HL)                
6805: AE              XOR     (HL)                
6806: 3D              DEC     A                   
6807: 3F              CCF                         
6808: 98              SBC     B                   
6809: 2E 05           LD      L,$05               
680B: 72              LD      (HL),D              
680C: AE              XOR     (HL)                
680D: AE              XOR     (HL)                
680E: AE              XOR     (HL)                
680F: AE              XOR     (HL)                
6810: AE              XOR     (HL)                
6811: 98              SBC     B                   
6812: 40              LD      B,B                 
6813: 07              RLCA                        
6814: AE              XOR     (HL)                
6815: AE              XOR     (HL)                
6816: AE              XOR     (HL)                
6817: AE              XOR     (HL)                
6818: AE              XOR     (HL)                
6819: AE              XOR     (HL)                
681A: 74              LD      (HL),H              
681B: 67              LD      H,A                 
681C: 98              SBC     B                   
681D: 4E              LD      C,(HL)              
681E: 05              DEC     B                   
681F: 45              LD      B,L                 
6820: AE              XOR     (HL)                
6821: AE              XOR     (HL)                
6822: AE              XOR     (HL)                
6823: AE              XOR     (HL)                
6824: AE              XOR     (HL)                
6825: 98              SBC     B                   
6826: 60              LD      H,B                 
6827: 07              RLCA                        
6828: AE              XOR     (HL)                
6829: AE              XOR     (HL)                
682A: AE              XOR     (HL)                
682B: AE              XOR     (HL)                
682C: AE              XOR     (HL)                
682D: AE              XOR     (HL)                
682E: AE              XOR     (HL)                
682F: 75              LD      (HL),L              
6830: 98              SBC     B                   
6831: 6E              LD      L,(HL)              
6832: 05              DEC     B                   
6833: 78              LD      A,B                 
6834: 79              LD      A,C                 
6835: AE              XOR     (HL)                
6836: AE              XOR     (HL)                
6837: AE              XOR     (HL)                
6838: AE              XOR     (HL)                
6839: 98              SBC     B                   
683A: 80              ADD     A,B                 
683B: 07              RLCA                        
683C: 45              LD      B,L                 
683D: AE              XOR     (HL)                
683E: 2C              INC     L                   
683F: 2D              DEC     L                   
6840: 45              LD      B,L                 
6841: AE              XOR     (HL)                
6842: 2C              INC     L                   
6843: 2D              DEC     L                   
6844: 98              SBC     B                   
6845: 90              SUB     B                   
6846: 03              INC     BC                  
6847: 7A              LD      A,D                 
6848: 4B              LD      C,E                 
6849: AE              XOR     (HL)                
684A: 3E 98           LD      A,$98               
684C: A0              AND     B                   
684D: 06 78           LD      B,$78               
684F: 79              LD      A,C                 
6850: 3C              INC     A                   
6851: AC              XOR     H                   
6852: 78              LD      A,B                 
6853: 79              LD      A,C                 
6854: 3C              INC     A                   
6855: 98              SBC     B                   
6856: B1              OR      C                   
6857: 02              LD      (BC),A              
6858: 7B              LD      A,E                 
6859: 3D              DEC     A                   
685A: 3F              CCF                         
685B: 98              SBC     B                   
685C: C8              RET     Z                   
685D: 03              INC     BC                  
685E: 84              ADD     A,H                 
685F: 85              ADD     A,L                 
6860: 9D              SBC     L                   
6861: 9F              SBC     A                   
6862: 98              SBC     B                   
6863: E8 03           ADD     SP,$03              
6865: A2              AND     D                   
6866: A3              AND     E                   
6867: BF              CP      A                   
6868: F0 99           LD      A,($99)             
686A: 08 03 F8        LD      ($F803),SP          
686D: FA FC FD        LD      A,($FDFC)           
6870: 99              SBC     C                   
6871: 28 03           JR      Z,$6876             ; {}
6873: FE FF           CP      $FF                 
6875: 05              DEC     B                   
6876: 0B              DEC     BC                  
6877: 98              SBC     B                   
6878: E0 01           LD      ($FF00+$01),A       
687A: 74              LD      (HL),H              
687B: 67              LD      H,A                 
687C: 99              SBC     C                   
687D: 00              NOP                         
687E: 01 AE 75        LD      BC,$75AE            
6881: 99              SBC     C                   
6882: 20 01           JR      NZ,$6885            ; {}
6884: 2C              INC     L                   
6885: 2D              DEC     L                   
6886: 99              SBC     C                   
6887: 40              LD      B,B                 
6888: 00              NOP                         
6889: 3C              INC     A                   
688A: 99              SBC     C                   
688B: 44              LD      B,H                 
688C: 03              INC     BC                  
688D: 56              LD      D,(HL)              
688E: 73              LD      (HL),E              
688F: 74              LD      (HL),H              
6890: 67              LD      H,A                 
6891: 99              SBC     C                   
6892: 64              LD      H,H                 
6893: 03              INC     BC                  
6894: 72              LD      (HL),D              
6895: AE              XOR     (HL)                
6896: AE              XOR     (HL)                
6897: 75              LD      (HL),L              
6898: 99              SBC     C                   
6899: 84              ADD     A,H                 
689A: 03              INC     BC                  
689B: 7A              LD      A,D                 
689C: 4B              LD      C,E                 
689D: AE              XOR     (HL)                
689E: 3E 99           LD      A,$99               
68A0: A5              AND     L                   
68A1: 02              LD      (BC),A              
68A2: 7B              LD      A,E                 
68A3: 3D              DEC     A                   
68A4: 3F              CCF                         
68A5: 99              SBC     C                   
68A6: 92              SUB     D                   
68A7: 01 56 73        LD      BC,$7356            
68AA: 99              SBC     C                   
68AB: B2              OR      D                   
68AC: 01 72 AE        LD      BC,$AE72            
68AF: 99              SBC     C                   
68B0: D2 01 7A        JP      NC,$7A01            ; {}
68B3: 4B              LD      C,E                 
68B4: 99              SBC     C                   
68B5: F3              DI                          
68B6: 00              NOP                         
68B7: 7B              LD      A,E                 
68B8: 9A              SBC     D                   
68B9: 13              INC     DE                  
68BA: 00              NOP                         
68BB: 57              LD      D,A                 
68BC: 9A              SBC     D                   
68BD: 32              LD      (HLD),A             
68BE: 01 70 71        LD      BC,$7170            
68C1: 99              SBC     C                   
68C2: C2 02 56        JP      NZ,$5602            ; {}
68C5: 73              LD      (HL),E              
68C6: 66              LD      H,(HL)              
68C7: 99              SBC     C                   
68C8: E2              LD      (C),A               
68C9: 03              INC     BC                  
68CA: 72              LD      (HL),D              
68CB: AE              XOR     (HL)                
68CC: 76              HALT                        
68CD: 77              LD      (HL),A              
68CE: 9A              SBC     D                   
68CF: 00              NOP                         
68D0: 07              RLCA                        
68D1: 56              LD      D,(HL)              
68D2: 73              LD      (HL),E              
68D3: AE              XOR     (HL)                
68D4: AE              XOR     (HL)                
68D5: AE              XOR     (HL)                
68D6: AE              XOR     (HL)                
68D7: 74              LD      (HL),H              
68D8: 67              LD      H,A                 
68D9: 9A              SBC     D                   
68DA: 20 07           JR      NZ,$68E3            ; {}
68DC: 72              LD      (HL),D              
68DD: AE              XOR     (HL)                
68DE: AE              XOR     (HL)                
68DF: AE              XOR     (HL)                
68E0: AE              XOR     (HL)                
68E1: AE              XOR     (HL)                
68E2: AE              XOR     (HL)                
68E3: 75              LD      (HL),L              
68E4: 00              NOP                         
68E5: 98              SBC     B                   
68E6: 00              NOP                         
68E7: 5F              LD      E,A                 
68E8: AC              XOR     H                   
68E9: 98              SBC     B                   
68EA: 20 5F           JR      NZ,$694B            ; {}
68EC: AC              XOR     H                   
68ED: 98              SBC     B                   
68EE: 40              LD      B,B                 
68EF: 5F              LD      E,A                 
68F0: AC              XOR     H                   
68F1: 98              SBC     B                   
68F2: 60              LD      H,B                 
68F3: 5F              LD      E,A                 
68F4: AC              XOR     H                   
68F5: 98              SBC     B                   
68F6: 80              ADD     A,B                 
68F7: 5F              LD      E,A                 
68F8: AC              XOR     H                   
68F9: 98              SBC     B                   
68FA: A0              AND     B                   
68FB: 5F              LD      E,A                 
68FC: AC              XOR     H                   
68FD: 98              SBC     B                   
68FE: C0              RET     NZ                  
68FF: 5F              LD      E,A                 
6900: AC              XOR     H                   
6901: 98              SBC     B                   
6902: E0 5F           LD      ($FF00+$5F),A       
6904: AC              XOR     H                   
6905: 99              SBC     C                   
6906: 00              NOP                         
6907: 5F              LD      E,A                 
6908: AC              XOR     H                   
6909: 99              SBC     C                   
690A: 20 5F           JR      NZ,$696B            ; {}
690C: AC              XOR     H                   
690D: 99              SBC     C                   
690E: 40              LD      B,B                 
690F: 5F              LD      E,A                 
6910: AC              XOR     H                   
6911: 99              SBC     C                   
6912: 60              LD      H,B                 
6913: 5F              LD      E,A                 
6914: AC              XOR     H                   
6915: 99              SBC     C                   
6916: 80              ADD     A,B                 
6917: 5F              LD      E,A                 
6918: AC              XOR     H                   
6919: 99              SBC     C                   
691A: A0              AND     B                   
691B: 5F              LD      E,A                 
691C: AC              XOR     H                   
691D: 99              SBC     C                   
691E: C0              RET     NZ                  
691F: 5F              LD      E,A                 
6920: AC              XOR     H                   
6921: 99              SBC     C                   
6922: E0 5F           LD      ($FF00+$5F),A       
6924: AC              XOR     H                   
6925: 9A              SBC     D                   
6926: 00              NOP                         
6927: 5F              LD      E,A                 
6928: AC              XOR     H                   
6929: 9A              SBC     D                   
692A: 20 5F           JR      NZ,$698B            ; {}
692C: AC              XOR     H                   
692D: 9A              SBC     D                   
692E: 40              LD      B,B                 
692F: 5F              LD      E,A                 
6930: AC              XOR     H                   
6931: 9A              SBC     D                   
6932: 60              LD      H,B                 
6933: 5F              LD      E,A                 
6934: AC              XOR     H                   
6935: 9A              SBC     D                   
6936: 80              ADD     A,B                 
6937: 5F              LD      E,A                 
6938: AC              XOR     H                   
6939: 9A              SBC     D                   
693A: A0              AND     B                   
693B: 5F              LD      E,A                 
693C: AC              XOR     H                   
693D: 9A              SBC     D                   
693E: E0 5F           LD      ($FF00+$5F),A       
6940: AC              XOR     H                   
6941: 9B              SBC     E                   
6942: C0              RET     NZ                  
6943: 5F              LD      E,A                 
6944: AC              XOR     H                   
6945: 9B              SBC     E                   
6946: E0 5F           LD      ($FF00+$5F),A       
6948: AC              XOR     H                   
6949: 98              SBC     B                   
694A: 12              LD      (DE),A              
694B: 01 E5 E6        LD      BC,$E6E5            
694E: 98              SBC     B                   
694F: 32              LD      (HLD),A             
6950: 01 F5 F6        LD      BC,$F6F5            
6953: 98              SBC     B                   
6954: 40              LD      B,B                 
6955: 01 80 81        LD      BC,$8180            
6958: 98              SBC     B                   
6959: 4C              LD      C,H                 
695A: 07              RLCA                        
695B: E5              PUSH    HL                  
695C: E6 E1           AND     $E1                 
695E: E2              LD      (C),A               
695F: E3                              
6960: E4                              
6961: E7              RST     0X20                
6962: E8 98           ADD     SP,$98              
6964: 60              LD      H,B                 
6965: 01 90 91        LD      BC,$9190            
6968: 98              SBC     B                   
6969: 6C              LD      L,H                 
696A: 07              RLCA                        
696B: F5              PUSH    AF                  
696C: F6 F1           OR      $F1                 
696E: F2                              
696F: F3              DI                          
6970: F4                              
6971: F7              RST     0X30                
6972: AE              XOR     (HL)                
6973: 98              SBC     B                   
6974: 80              ADD     A,B                 
6975: 13              INC     DE                  
6976: A0              AND     B                   
6977: A1              AND     C                   
6978: E1              POP     HL                  
6979: E2              LD      (C),A               
697A: AC              XOR     H                   
697B: E3                              
697C: E4                              
697D: E1              POP     HL                  
697E: E2              LD      (C),A               
697F: AC              XOR     H                   
6980: E3                              
6981: E4                              
6982: E7              RST     0X20                
6983: E8 A0           ADD     SP,$A0              
6985: A1              AND     C                   
6986: E7              RST     0X20                
6987: E8 A0           ADD     SP,$A0              
6989: A1              AND     C                   
698A: 98              SBC     B                   
698B: A0              AND     B                   
698C: 13              INC     DE                  
698D: B0              OR      B                   
698E: B1              OR      C                   
698F: F1              POP     AF                  
6990: F2                              
6991: AC              XOR     H                   
6992: F3              DI                          
6993: F4                              
6994: F1              POP     AF                  
6995: F2                              
6996: AC              XOR     H                   
6997: F3              DI                          
6998: F4                              
6999: F7              RST     0X30                
699A: AE              XOR     (HL)                
699B: B0              OR      B                   
699C: B1              OR      C                   
699D: F7              RST     0X30                
699E: AE              XOR     (HL)                
699F: B0              OR      B                   
69A0: B1              OR      C                   
69A1: 98              SBC     B                   
69A2: C0              RET     NZ                  
69A3: 13              INC     DE                  
69A4: 82              ADD     A,D                 
69A5: 83              ADD     A,E                 
69A6: 82              ADD     A,D                 
69A7: 83              ADD     A,E                 
69A8: 82              ADD     A,D                 
69A9: 83              ADD     A,E                 
69AA: 82              ADD     A,D                 
69AB: 83              ADD     A,E                 
69AC: 82              ADD     A,D                 
69AD: 83              ADD     A,E                 
69AE: 82              ADD     A,D                 
69AF: 83              ADD     A,E                 
69B0: 82              ADD     A,D                 
69B1: 83              ADD     A,E                 
69B2: 82              ADD     A,D                 
69B3: 83              ADD     A,E                 
69B4: 82              ADD     A,D                 
69B5: 83              ADD     A,E                 
69B6: 82              ADD     A,D                 
69B7: 83              ADD     A,E                 
69B8: 98              SBC     B                   
69B9: E0 13           LD      ($FF00+$13),A       
69BB: 92              SUB     D                   
69BC: 93              SUB     E                   
69BD: 92              SUB     D                   
69BE: 93              SUB     E                   
69BF: 92              SUB     D                   
69C0: 93              SUB     E                   
69C1: 92              SUB     D                   
69C2: 93              SUB     E                   
69C3: 92              SUB     D                   
69C4: 93              SUB     E                   
69C5: 92              SUB     D                   
69C6: 93              SUB     E                   
69C7: 92              SUB     D                   
69C8: 93              SUB     E                   
69C9: 92              SUB     D                   
69CA: 93              SUB     E                   
69CB: 92              SUB     D                   
69CC: 93              SUB     E                   
69CD: 92              SUB     D                   
69CE: 93              SUB     E                   
69CF: 99              SBC     C                   
69D0: 68              LD      L,B                 
69D1: 03              INC     BC                  
69D2: 86              ADD     A,(HL)              
69D3: 87              ADD     A,A                 
69D4: 88              ADC     A,B                 
69D5: 89              ADC     A,C                 
69D6: 99              SBC     C                   
69D7: 86              ADD     A,(HL)              
69D8: 05              DEC     B                   
69D9: 94              SUB     H                   
69DA: 95              SUB     L                   
69DB: 96              SUB     (HL)                
69DC: 97              SUB     A                   
69DD: 98              SBC     B                   
69DE: 99              SBC     C                   
69DF: 99              SBC     C                   
69E0: A6              AND     (HL)                
69E1: 07              RLCA                        
69E2: A4              AND     H                   
69E3: A5              AND     L                   
69E4: A6              AND     (HL)                
69E5: A7              AND     A                   
69E6: A8              XOR     B                   
69E7: A9              XOR     C                   
69E8: AA              XOR     D                   
69E9: AB              XOR     E                   
69EA: 99              SBC     C                   
69EB: C4 0C B2        CALL    NZ,$B20C            
69EE: B3              OR      E                   
69EF: B4              OR      H                   
69F0: B5              OR      L                   
69F1: B6              OR      (HL)                
69F2: B7              OR      A                   
69F3: B8              CP      B                   
69F4: B9              CP      C                   
69F5: BA              CP      D                   
69F6: BB              CP      E                   
69F7: BC              CP      H                   
69F8: BD              CP      L                   
69F9: BE              CP      (HL)                
69FA: 99              SBC     C                   
69FB: E2              LD      (C),A               
69FC: 0F              RRCA                        
69FD: C0              RET     NZ                  
69FE: C1              POP     BC                  
69FF: C2 C3 C4        JP      NZ,$C4C3            
6A02: C5              PUSH    BC                  
6A03: C6 C7           ADD     $C7                 
6A05: C8              RET     Z                   
6A06: C9              RET                         
6A07: CA CB CC        JP      Z,$CCCB             
6A0A: CD CE CF        CALL    $CFCE               
6A0D: 9A              SBC     D                   
6A0E: 02              LD      (BC),A              
6A0F: 0F              RRCA                        
6A10: D0              RET     NC                  
6A11: D1              POP     DE                  
6A12: D2 D3 D4        JP      NC,$D4D3            
6A15: D5              PUSH    DE                  
6A16: D6 D7           SUB     $D7                 
6A18: D8              RET     C                   
6A19: D9              RETI                        
6A1A: DA DB DC        JP      C,$DCDB             
6A1D: DD                              
6A1E: DE DF           SBC     $DF                 
6A20: 9A              SBC     D                   
6A21: 22              LD      (HLI),A             
6A22: 0F              RRCA                        
6A23: E0 6C           LD      ($FF00+$6C),A       
6A25: 6D              LD      L,L                 
6A26: 6E              LD      L,(HL)              
6A27: 6F              LD      L,A                 
6A28: 6C              LD      L,H                 
6A29: 6D              LD      L,L                 
6A2A: 6E              LD      L,(HL)              
6A2B: 6F              LD      L,A                 
6A2C: 6C              LD      L,H                 
6A2D: 6D              LD      L,L                 
6A2E: 6E              LD      L,(HL)              
6A2F: 6F              LD      L,A                 
6A30: 6C              LD      L,H                 
6A31: 6D              LD      L,L                 
6A32: EF              RST     0X28                
6A33: 00              NOP                         
6A34: 98              SBC     B                   
6A35: 00              NOP                         
6A36: 53              LD      D,E                 
6A37: AC              XOR     H                   
6A38: 98              SBC     B                   
6A39: 20 53           JR      NZ,$6A8E            ; {}
6A3B: AC              XOR     H                   
6A3C: 98              SBC     B                   
6A3D: 28 03           JR      Z,$6A42             ; {}
6A3F: 50              LD      D,B                 
6A40: 51              LD      D,C                 
6A41: 52              LD      D,D                 
6A42: 53              LD      D,E                 
6A43: 98              SBC     B                   
6A44: 40              LD      B,B                 
6A45: 53              LD      D,E                 
6A46: AC              XOR     H                   
6A47: 98              SBC     B                   
6A48: 48              LD      C,B                 
6A49: 05              DEC     B                   
6A4A: 60              LD      H,B                 
6A4B: 61              LD      H,C                 
6A4C: 62              LD      H,D                 
6A4D: 63              LD      H,E                 
6A4E: 64              LD      H,H                 
6A4F: 65              LD      H,L                 
6A50: 98              SBC     B                   
6A51: 60              LD      H,B                 
6A52: 53              LD      D,E                 
6A53: AC              XOR     H                   
6A54: 98              SBC     B                   
6A55: 80              ADD     A,B                 
6A56: 53              LD      D,E                 
6A57: AC              XOR     H                   
6A58: 98              SBC     B                   
6A59: 92              SUB     D                   
6A5A: 01 E5 E6        LD      BC,$E6E5            
6A5D: 98              SBC     B                   
6A5E: A0              AND     B                   
6A5F: 53              LD      D,E                 
6A60: AC              XOR     H                   
6A61: 98              SBC     B                   
6A62: A4              AND     H                   
6A63: 01 64 65        LD      BC,$6564            
6A66: 98              SBC     B                   
6A67: B2              OR      D                   
6A68: 01 F5 F6        LD      BC,$F6F5            
6A6B: 98              SBC     B                   
6A6C: C0              RET     NZ                  
6A6D: 53              LD      D,E                 
6A6E: AC              XOR     H                   
6A6F: 98              SBC     B                   
6A70: C0              RET     NZ                  
6A71: 01 80 81        LD      BC,$8180            
6A74: 98              SBC     B                   
6A75: CC 07 E5        CALL    Z,$E507             
6A78: E6 E1           AND     $E1                 
6A7A: E2              LD      (C),A               
6A7B: E3                              
6A7C: E4                              
6A7D: E7              RST     0X20                
6A7E: E8 98           ADD     SP,$98              
6A80: E0 53           LD      ($FF00+$53),A       
6A82: AC              XOR     H                   
6A83: 98              SBC     B                   
6A84: E0 01           LD      ($FF00+$01),A       
6A86: 90              SUB     B                   
6A87: 91              SUB     C                   
6A88: 98              SBC     B                   
6A89: EC                              
6A8A: 07              RLCA                        
6A8B: F5              PUSH    AF                  
6A8C: F6 F1           OR      $F1                 
6A8E: F2                              
6A8F: F3              DI                          
6A90: F4                              
6A91: F7              RST     0X30                
6A92: AE              XOR     (HL)                
6A93: 99              SBC     C                   
6A94: 00              NOP                         
6A95: 13              INC     DE                  
6A96: A0              AND     B                   
6A97: A1              AND     C                   
6A98: E1              POP     HL                  
6A99: E2              LD      (C),A               
6A9A: AC              XOR     H                   
6A9B: E3                              
6A9C: E4                              
6A9D: E1              POP     HL                  
6A9E: E2              LD      (C),A               
6A9F: AC              XOR     H                   
6AA0: E3                              
6AA1: E4                              
6AA2: E7              RST     0X20                
6AA3: E8 A0           ADD     SP,$A0              
6AA5: A1              AND     C                   
6AA6: E7              RST     0X20                
6AA7: E8 A0           ADD     SP,$A0              
6AA9: A1              AND     C                   
6AAA: 99              SBC     C                   
6AAB: 20 13           JR      NZ,$6AC0            ; {}
6AAD: B0              OR      B                   
6AAE: B1              OR      C                   
6AAF: F1              POP     AF                  
6AB0: F2                              
6AB1: AC              XOR     H                   
6AB2: F3              DI                          
6AB3: F4                              
6AB4: F1              POP     AF                  
6AB5: F2                              
6AB6: AC              XOR     H                   
6AB7: F3              DI                          
6AB8: F4                              
6AB9: F7              RST     0X30                
6ABA: AE              XOR     (HL)                
6ABB: B0              OR      B                   
6ABC: B1              OR      C                   
6ABD: F7              RST     0X30                
6ABE: AE              XOR     (HL)                
6ABF: B0              OR      B                   
6AC0: B1              OR      C                   
6AC1: 99              SBC     C                   
6AC2: 40              LD      B,B                 
6AC3: 1F              RRA                         
6AC4: 82              ADD     A,D                 
6AC5: 83              ADD     A,E                 
6AC6: 82              ADD     A,D                 
6AC7: 83              ADD     A,E                 
6AC8: 82              ADD     A,D                 
6AC9: 83              ADD     A,E                 
6ACA: 82              ADD     A,D                 
6ACB: 83              ADD     A,E                 
6ACC: 82              ADD     A,D                 
6ACD: 83              ADD     A,E                 
6ACE: 82              ADD     A,D                 
6ACF: 83              ADD     A,E                 
6AD0: 82              ADD     A,D                 
6AD1: 83              ADD     A,E                 
6AD2: 82              ADD     A,D                 
6AD3: 83              ADD     A,E                 
6AD4: 82              ADD     A,D                 
6AD5: 83              ADD     A,E                 
6AD6: 82              ADD     A,D                 
6AD7: 83              ADD     A,E                 
6AD8: 82              ADD     A,D                 
6AD9: 83              ADD     A,E                 
6ADA: 82              ADD     A,D                 
6ADB: 83              ADD     A,E                 
6ADC: 82              ADD     A,D                 
6ADD: 83              ADD     A,E                 
6ADE: 82              ADD     A,D                 
6ADF: 83              ADD     A,E                 
6AE0: 82              ADD     A,D                 
6AE1: 83              ADD     A,E                 
6AE2: 82              ADD     A,D                 
6AE3: 83              ADD     A,E                 
6AE4: 99              SBC     C                   
6AE5: 60              LD      H,B                 
6AE6: 1F              RRA                         
6AE7: 92              SUB     D                   
6AE8: 93              SUB     E                   
6AE9: 92              SUB     D                   
6AEA: 93              SUB     E                   
6AEB: 92              SUB     D                   
6AEC: 93              SUB     E                   
6AED: 92              SUB     D                   
6AEE: 93              SUB     E                   
6AEF: 92              SUB     D                   
6AF0: 93              SUB     E                   
6AF1: 92              SUB     D                   
6AF2: 93              SUB     E                   
6AF3: 92              SUB     D                   
6AF4: 93              SUB     E                   
6AF5: 92              SUB     D                   
6AF6: 93              SUB     E                   
6AF7: 92              SUB     D                   
6AF8: 93              SUB     E                   
6AF9: 92              SUB     D                   
6AFA: 93              SUB     E                   
6AFB: 92              SUB     D                   
6AFC: 93              SUB     E                   
6AFD: 92              SUB     D                   
6AFE: 93              SUB     E                   
6AFF: 92              SUB     D                   
6B00: 93              SUB     E                   
6B01: 92              SUB     D                   
6B02: 93              SUB     E                   
6B03: 92              SUB     D                   
6B04: 93              SUB     E                   
6B05: 92              SUB     D                   
6B06: 93              SUB     E                   
6B07: 99              SBC     C                   
6B08: 80              ADD     A,B                 
6B09: 5F              LD      E,A                 
6B0A: AC              XOR     H                   
6B0B: 99              SBC     C                   
6B0C: A0              AND     B                   
6B0D: 5F              LD      E,A                 
6B0E: AC              XOR     H                   
6B0F: 99              SBC     C                   
6B10: C0              RET     NZ                  
6B11: 5F              LD      E,A                 
6B12: AC              XOR     H                   
6B13: 99              SBC     C                   
6B14: E0 5F           LD      ($FF00+$5F),A       
6B16: AC              XOR     H                   
6B17: 9A              SBC     D                   
6B18: 00              NOP                         
6B19: 5F              LD      E,A                 
6B1A: AC              XOR     H                   
6B1B: 9A              SBC     D                   
6B1C: 20 5F           JR      NZ,$6B7D            ; {}
6B1E: AC              XOR     H                   
6B1F: 00              NOP                         
6B20: 9B              SBC     E                   
6B21: C0              RET     NZ                  
6B22: 5F              LD      E,A                 
6B23: AC              XOR     H                   
6B24: 9B              SBC     E                   
6B25: E0 5F           LD      ($FF00+$5F),A       
6B27: AC              XOR     H                   
6B28: 98              SBC     B                   
6B29: 00              NOP                         
6B2A: 5F              LD      E,A                 
6B2B: AC              XOR     H                   
6B2C: 98              SBC     B                   
6B2D: 20 5F           JR      NZ,$6B8E            ; {}
6B2F: AC              XOR     H                   
6B30: 98              SBC     B                   
6B31: 40              LD      B,B                 
6B32: 5F              LD      E,A                 
6B33: AC              XOR     H                   
6B34: 98              SBC     B                   
6B35: 60              LD      H,B                 
6B36: 5F              LD      E,A                 
6B37: AC              XOR     H                   
6B38: 98              SBC     B                   
6B39: 80              ADD     A,B                 
6B3A: 5F              LD      E,A                 
6B3B: AC              XOR     H                   
6B3C: 98              SBC     B                   
6B3D: A0              AND     B                   
6B3E: 5F              LD      E,A                 
6B3F: AC              XOR     H                   
6B40: 98              SBC     B                   
6B41: C0              RET     NZ                  
6B42: 5F              LD      E,A                 
6B43: AC              XOR     H                   
6B44: 98              SBC     B                   
6B45: E0 5F           LD      ($FF00+$5F),A       
6B47: AC              XOR     H                   
6B48: 99              SBC     C                   
6B49: 00              NOP                         
6B4A: 5F              LD      E,A                 
6B4B: AC              XOR     H                   
6B4C: 99              SBC     C                   
6B4D: 20 5F           JR      NZ,$6BAE            ; {}
6B4F: AC              XOR     H                   
6B50: 99              SBC     C                   
6B51: 40              LD      B,B                 
6B52: 5F              LD      E,A                 
6B53: AC              XOR     H                   
6B54: 99              SBC     C                   
6B55: 60              LD      H,B                 
6B56: 5F              LD      E,A                 
6B57: AC              XOR     H                   
6B58: 99              SBC     C                   
6B59: 80              ADD     A,B                 
6B5A: 5F              LD      E,A                 
6B5B: AC              XOR     H                   
6B5C: 99              SBC     C                   
6B5D: A0              AND     B                   
6B5E: 5F              LD      E,A                 
6B5F: AC              XOR     H                   
6B60: 99              SBC     C                   
6B61: C0              RET     NZ                  
6B62: 5F              LD      E,A                 
6B63: AC              XOR     H                   
6B64: 99              SBC     C                   
6B65: E0 5F           LD      ($FF00+$5F),A       
6B67: AC              XOR     H                   
6B68: 9A              SBC     D                   
6B69: 00              NOP                         
6B6A: 5F              LD      E,A                 
6B6B: AC              XOR     H                   
6B6C: 9A              SBC     D                   
6B6D: 20 5F           JR      NZ,$6BCE            ; {}
6B6F: AC              XOR     H                   
6B70: 9A              SBC     D                   
6B71: 40              LD      B,B                 
6B72: 5F              LD      E,A                 
6B73: AC              XOR     H                   
6B74: 9A              SBC     D                   
6B75: 60              LD      H,B                 
6B76: 5F              LD      E,A                 
6B77: AC              XOR     H                   
6B78: 98              SBC     B                   
6B79: 01 05 58        LD      BC,$5805            
6B7C: 59              LD      E,C                 
6B7D: 5A              LD      E,D                 
6B7E: 5B              LD      E,E                 
6B7F: 5C              LD      E,H                 
6B80: 5D              LD      E,L                 
6B81: 98              SBC     B                   
6B82: 21 05 68        LD      HL,$6805            
6B85: 69              LD      L,C                 
6B86: 6A              LD      L,D                 
6B87: 6B              LD      L,E                 
6B88: 6C              LD      L,H                 
6B89: 6D              LD      L,L                 
6B8A: 98              SBC     B                   
6B8B: 31 02 58        LD      SP,$5802            
6B8E: 59              LD      E,C                 
6B8F: 5A              LD      E,D                 
6B90: 98              SBC     B                   
6B91: 51              LD      D,C                 
6B92: 02              LD      (BC),A              
6B93: 68              LD      L,B                 
6B94: 69              LD      L,C                 
6B95: 6A              LD      L,D                 
6B96: 98              SBC     B                   
6B97: 60              LD      H,B                 
6B98: 01 5C 5D        LD      BC,$5D5C            
6B9B: 98              SBC     B                   
6B9C: 80              ADD     A,B                 
6B9D: 07              RLCA                        
6B9E: 6C              LD      L,H                 
6B9F: 6D              LD      L,L                 
6BA0: AC              XOR     H                   
6BA1: AC              XOR     H                   
6BA2: 50              LD      D,B                 
6BA3: 51              LD      D,C                 
6BA4: 52              LD      D,D                 
6BA5: 53              LD      D,E                 
6BA6: 98              SBC     B                   
6BA7: A4              AND     H                   
6BA8: 05              DEC     B                   
6BA9: 60              LD      H,B                 
6BAA: 61              LD      H,C                 
6BAB: 62              LD      H,D                 
6BAC: 63              LD      H,E                 
6BAD: 64              LD      H,H                 
6BAE: 65              LD      H,L                 
6BAF: 99              SBC     C                   
6BB0: 40              LD      B,B                 
6BB1: 03              INC     BC                  
6BB2: 50              LD      D,B                 
6BB3: 51              LD      D,C                 
6BB4: 52              LD      D,D                 
6BB5: 53              LD      D,E                 
6BB6: 99              SBC     C                   
6BB7: 4F              LD      C,A                 
6BB8: 03              INC     BC                  
6BB9: 50              LD      D,B                 
6BBA: 51              LD      D,C                 
6BBB: 52              LD      D,D                 
6BBC: 53              LD      D,E                 
6BBD: 99              SBC     C                   
6BBE: 60              LD      H,B                 
6BBF: 03              INC     BC                  
6BC0: 60              LD      H,B                 
6BC1: 61              LD      H,C                 
6BC2: 62              LD      H,D                 
6BC3: 63              LD      H,E                 
6BC4: 99              SBC     C                   
6BC5: 6D              LD      L,L                 
6BC6: 05              DEC     B                   
6BC7: 64              LD      H,H                 
6BC8: 65              LD      H,L                 
6BC9: 60              LD      H,B                 
6BCA: 61              LD      H,C                 
6BCB: 62              LD      H,D                 
6BCC: 63              LD      H,E                 
6BCD: 99              SBC     C                   
6BCE: E3                              
6BCF: 01 64 65        LD      BC,$6564            
6BD2: 9A              SBC     D                   
6BD3: 00              NOP                         
6BD4: 01 64 65        LD      BC,$6564            
6BD7: 9A              SBC     D                   
6BD8: 10 01           ;;STOP    $01                 
6BDA: 64              LD      H,H                 
6BDB: 65              LD      H,L                 
6BDC: 00              NOP                         
6BDD: 98              SBC     B                   
6BDE: 00              NOP                         
6BDF: 5F              LD      E,A                 
6BE0: AC              XOR     H                   
6BE1: 98              SBC     B                   
6BE2: 20 5F           JR      NZ,$6C43            ; {}
6BE4: AC              XOR     H                   
6BE5: 98              SBC     B                   
6BE6: 40              LD      B,B                 
6BE7: 5F              LD      E,A                 
6BE8: AC              XOR     H                   
6BE9: 98              SBC     B                   
6BEA: 60              LD      H,B                 
6BEB: 5F              LD      E,A                 
6BEC: AC              XOR     H                   
6BED: 98              SBC     B                   
6BEE: 80              ADD     A,B                 
6BEF: 5F              LD      E,A                 
6BF0: AC              XOR     H                   
6BF1: 98              SBC     B                   
6BF2: A0              AND     B                   
6BF3: 5F              LD      E,A                 
6BF4: AC              XOR     H                   
6BF5: 98              SBC     B                   
6BF6: C0              RET     NZ                  
6BF7: 5F              LD      E,A                 
6BF8: AC              XOR     H                   
6BF9: 98              SBC     B                   
6BFA: E0 5F           LD      ($FF00+$5F),A       
6BFC: AC              XOR     H                   
6BFD: 99              SBC     C                   
6BFE: 00              NOP                         
6BFF: 5F              LD      E,A                 
6C00: AC              XOR     H                   
6C01: 99              SBC     C                   
6C02: 20 5F           JR      NZ,$6C63            ; {}
6C04: AC              XOR     H                   
6C05: 99              SBC     C                   
6C06: 40              LD      B,B                 
6C07: 5F              LD      E,A                 
6C08: AC              XOR     H                   
6C09: 99              SBC     C                   
6C0A: 60              LD      H,B                 
6C0B: 5F              LD      E,A                 
6C0C: AC              XOR     H                   
6C0D: 99              SBC     C                   
6C0E: 80              ADD     A,B                 
6C0F: 5F              LD      E,A                 
6C10: AC              XOR     H                   
6C11: 99              SBC     C                   
6C12: A0              AND     B                   
6C13: 5F              LD      E,A                 
6C14: AC              XOR     H                   
6C15: 99              SBC     C                   
6C16: C0              RET     NZ                  
6C17: 5F              LD      E,A                 
6C18: AC              XOR     H                   
6C19: 99              SBC     C                   
6C1A: E0 5F           LD      ($FF00+$5F),A       
6C1C: AC              XOR     H                   
6C1D: 9A              SBC     D                   
6C1E: 00              NOP                         
6C1F: 5F              LD      E,A                 
6C20: AC              XOR     H                   
6C21: 9A              SBC     D                   
6C22: 20 5F           JR      NZ,$6C83            ; {}
6C24: AC              XOR     H                   
6C25: 9A              SBC     D                   
6C26: 40              LD      B,B                 
6C27: 5F              LD      E,A                 
6C28: AC              XOR     H                   
6C29: 9A              SBC     D                   
6C2A: 60              LD      H,B                 
6C2B: 5F              LD      E,A                 
6C2C: AC              XOR     H                   
6C2D: 9A              SBC     D                   
6C2E: 80              ADD     A,B                 
6C2F: 5F              LD      E,A                 
6C30: AC              XOR     H                   
6C31: 9A              SBC     D                   
6C32: A0              AND     B                   
6C33: 5F              LD      E,A                 
6C34: AC              XOR     H                   
6C35: 9A              SBC     D                   
6C36: C0              RET     NZ                  
6C37: 5F              LD      E,A                 
6C38: AC              XOR     H                   
6C39: 9A              SBC     D                   
6C3A: E0 5F           LD      ($FF00+$5F),A       
6C3C: AC              XOR     H                   
6C3D: 9B              SBC     E                   
6C3E: 00              NOP                         
6C3F: 5F              LD      E,A                 
6C40: AC              XOR     H                   
6C41: 9B              SBC     E                   
6C42: 20 5F           JR      NZ,$6CA3            ; {}
6C44: AC              XOR     H                   
6C45: 9B              SBC     E                   
6C46: 40              LD      B,B                 
6C47: 5F              LD      E,A                 
6C48: AC              XOR     H                   
6C49: 9B              SBC     E                   
6C4A: 60              LD      H,B                 
6C4B: 5F              LD      E,A                 
6C4C: AC              XOR     H                   
6C4D: 9B              SBC     E                   
6C4E: 80              ADD     A,B                 
6C4F: 5F              LD      E,A                 
6C50: AC              XOR     H                   
6C51: 9B              SBC     E                   
6C52: A0              AND     B                   
6C53: 5F              LD      E,A                 
6C54: AC              XOR     H                   
6C55: 9B              SBC     E                   
6C56: C0              RET     NZ                  
6C57: 5F              LD      E,A                 
6C58: AC              XOR     H                   
6C59: 9B              SBC     E                   
6C5A: E0 5F           LD      ($FF00+$5F),A       
6C5C: AC              XOR     H                   
6C5D: 9A              SBC     D                   
6C5E: 40              LD      B,B                 
6C5F: 01 6C 6D        LD      BC,$6D6C            
6C62: 9A              SBC     D                   
6C63: 46              LD      B,(HL)              
6C64: 03              INC     BC                  
6C65: 50              LD      D,B                 
6C66: 51              LD      D,C                 
6C67: 52              LD      D,D                 
6C68: 53              LD      D,E                 
6C69: 9A              SBC     D                   
6C6A: 66              LD      H,(HL)              
6C6B: 03              INC     BC                  
6C6C: 60              LD      H,B                 
6C6D: 61              LD      H,C                 
6C6E: 62              LD      H,D                 
6C6F: 63              LD      H,E                 
6C70: 9A              SBC     D                   
6C71: 90              SUB     B                   
6C72: 03              INC     BC                  
6C73: E3                              
6C74: E4                              
6C75: E1              POP     HL                  
6C76: E2              LD      (C),A               
6C77: 9A              SBC     D                   
6C78: B0              OR      B                   
6C79: 03              INC     BC                  
6C7A: F3              DI                          
6C7B: F4                              
6C7C: F1              POP     AF                  
6C7D: F2                              
6C7E: 9A              SBC     D                   
6C7F: CE 05           ADC     $05                 
6C81: E3                              
6C82: E4                              
6C83: E7              RST     0X20                
6C84: E8 A0           ADD     SP,$A0              
6C86: A1              AND     C                   
6C87: 9A              SBC     D                   
6C88: EE 05           XOR     $05                 
6C8A: F3              DI                          
6C8B: F4                              
6C8C: F7              RST     0X30                
6C8D: AE              XOR     (HL)                
6C8E: B0              OR      B                   
6C8F: B1              OR      C                   
6C90: 9B              SBC     E                   
6C91: 04              INC     B                   
6C92: 03              INC     BC                  
6C93: 50              LD      D,B                 
6C94: 51              LD      D,C                 
6C95: 52              LD      D,D                 
6C96: 53              LD      D,E                 
6C97: 9B              SBC     E                   
6C98: 0E 05           LD      C,$05               
6C9A: 22              LD      (HLI),A             
6C9B: 23              INC     HL                  
6C9C: 02              LD      (BC),A              
6C9D: 03              INC     BC                  
6C9E: 23              INC     HL                  
6C9F: AE              XOR     (HL)                
6CA0: 9B              SBC     E                   
6CA1: 24              INC     H                   
6CA2: 03              INC     BC                  
6CA3: 60              LD      H,B                 
6CA4: 61              LD      H,C                 
6CA5: 62              LD      H,D                 
6CA6: 63              LD      H,E                 
6CA7: 9B              SBC     E                   
6CA8: 2E 05           LD      L,$05               
6CAA: 32              LD      (HLD),A             
6CAB: 33              INC     SP                  
6CAC: 12              LD      (DE),A              
6CAD: 13              INC     DE                  
6CAE: AE              XOR     (HL)                
6CAF: AE              XOR     (HL)                
6CB0: 9B              SBC     E                   
6CB1: 40              LD      B,B                 
6CB2: 03              INC     BC                  
6CB3: E3                              
6CB4: E4                              
6CB5: E1              POP     HL                  
6CB6: E2              LD      (C),A               
6CB7: 9B              SBC     E                   
6CB8: 4B              LD      C,E                 
6CB9: 01 64 65        LD      BC,$6564            
6CBC: 9B              SBC     E                   
6CBD: 50              LD      D,B                 
6CBE: 03              INC     BC                  
6CBF: 22              LD      (HLI),A             
6CC0: 23              INC     HL                  
6CC1: 02              LD      (BC),A              
6CC2: 03              INC     BC                  
6CC3: 9B              SBC     E                   
6CC4: 60              LD      H,B                 
6CC5: 03              INC     BC                  
6CC6: F3              DI                          
6CC7: F4                              
6CC8: F1              POP     AF                  
6CC9: F2                              
6CCA: 9B              SBC     E                   
6CCB: 70              LD      (HL),B              
6CCC: 03              INC     BC                  
6CCD: 32              LD      (HLD),A             
6CCE: 33              INC     SP                  
6CCF: 12              LD      (DE),A              
6CD0: 13              INC     DE                  
6CD1: 9B              SBC     E                   
6CD2: 80              ADD     A,B                 
6CD3: 08 E7 E8        LD      ($E8E7),SP          
6CD6: A0              AND     B                   
6CD7: A1              AND     C                   
6CD8: 80              ADD     A,B                 
6CD9: 81              ADD     A,C                 
6CDA: AC              XOR     H                   
6CDB: 64              LD      H,H                 
6CDC: 65              LD      H,L                 
6CDD: 9B              SBC     E                   
6CDE: 92              SUB     D                   
6CDF: 01 22 23        LD      BC,$2322            
6CE2: 9B              SBC     E                   
6CE3: A0              AND     B                   
6CE4: 05              DEC     B                   
6CE5: F7              RST     0X30                
6CE6: AE              XOR     (HL)                
6CE7: B0              OR      B                   
6CE8: B1              OR      C                   
6CE9: 90              SUB     B                   
6CEA: 91              SUB     C                   
6CEB: 9B              SBC     E                   
6CEC: B2              OR      D                   
6CED: 01 F5 F6        LD      BC,$F6F5            
6CF0: 9B              SBC     E                   
6CF1: C0              RET     NZ                  
6CF2: 05              DEC     B                   
6CF3: 03              INC     BC                  
6CF4: 00              NOP                         
6CF5: 01 AE 20        LD      BC,$20AE            
6CF8: 21 9B CC        LD      HL,$CC9B            
6CFB: 07              RLCA                        
6CFC: E5              PUSH    HL                  
6CFD: E6 E1           AND     $E1                 
6CFF: E2              LD      (C),A               
6D00: E3                              
6D01: E4                              
6D02: E7              RST     0X20                
6D03: E8 9B           ADD     SP,$9B              
6D05: E0 05           LD      ($FF00+$05),A       
6D07: 13              INC     DE                  
6D08: 10 11           ;;STOP    $11                 
6D0A: AE              XOR     (HL)                
6D0B: 30 31           JR      NC,$6D3E            ; {}
6D0D: 9B              SBC     E                   
6D0E: EC                              
6D0F: 07              RLCA                        
6D10: F5              PUSH    AF                  
6D11: F6 F1           OR      $F1                 
6D13: F2                              
6D14: F3              DI                          
6D15: F4                              
6D16: F7              RST     0X30                
6D17: AE              XOR     (HL)                
6D18: 98              SBC     B                   
6D19: 00              NOP                         
6D1A: 03              INC     BC                  
6D1B: AE              XOR     (HL)                
6D1C: AE              XOR     (HL)                
6D1D: 20 21           JR      NZ,$6D40            ; {}
6D1F: 98              SBC     B                   
6D20: 0A              LD      A,(BC)              
6D21: 09              ADD     HL,BC               
6D22: E3                              
6D23: E4                              
6D24: E7              RST     0X20                
6D25: E8 A0           ADD     SP,$A0              
6D27: A1              AND     C                   
6D28: E7              RST     0X20                
6D29: E8 A0           ADD     SP,$A0              
6D2B: A1              AND     C                   
6D2C: 98              SBC     B                   
6D2D: 20 03           JR      NZ,$6D32            ; {}
6D2F: AE              XOR     (HL)                
6D30: AE              XOR     (HL)                
6D31: 30 31           JR      NC,$6D64            ; {}
6D33: 98              SBC     B                   
6D34: 2A              LD      A,(HLI)             
6D35: 09              ADD     HL,BC               
6D36: F3              DI                          
6D37: F4                              
6D38: F7              RST     0X30                
6D39: AE              XOR     (HL)                
6D3A: B0              OR      B                   
6D3B: B1              OR      C                   
6D3C: F7              RST     0X30                
6D3D: 23              INC     HL                  
6D3E: B0              OR      B                   
6D3F: B1              OR      C                   
6D40: 98              SBC     B                   
6D41: 40              LD      B,B                 
6D42: 03              INC     BC                  
6D43: 02              LD      (BC),A              
6D44: 03              INC     BC                  
6D45: E1              POP     HL                  
6D46: E2              LD      (C),A               
6D47: 98              SBC     B                   
6D48: 4A              LD      C,D                 
6D49: 09              ADD     HL,BC               
6D4A: 22              LD      (HLI),A             
6D4B: 23              INC     HL                  
6D4C: 02              LD      (BC),A              
6D4D: 03              INC     BC                  
6D4E: 23              INC     HL                  
6D4F: AE              XOR     (HL)                
6D50: AE              XOR     (HL)                
6D51: AE              XOR     (HL)                
6D52: AE              XOR     (HL)                
6D53: AE              XOR     (HL)                
6D54: 98              SBC     B                   
6D55: 60              LD      H,B                 
6D56: 03              INC     BC                  
6D57: 12              LD      (DE),A              
6D58: 13              INC     DE                  
6D59: F1              POP     AF                  
6D5A: F2                              
6D5B: 98              SBC     B                   
6D5C: 6A              LD      L,D                 
6D5D: 09              ADD     HL,BC               
6D5E: 32              LD      (HLD),A             
6D5F: 33              INC     SP                  
6D60: 12              LD      (DE),A              
6D61: 13              INC     DE                  
6D62: 23              INC     HL                  
6D63: AE              XOR     (HL)                
6D64: 23              INC     HL                  
6D65: AE              XOR     (HL)                
6D66: AE              XOR     (HL)                
6D67: AE              XOR     (HL)                
6D68: 98              SBC     B                   
6D69: 80              ADD     A,B                 
6D6A: 03              INC     BC                  
6D6B: AE              XOR     (HL)                
6D6C: AE              XOR     (HL)                
6D6D: 20 21           JR      NZ,$6D90            ; {}
6D6F: 98              SBC     B                   
6D70: 8C              ADC     A,H                 
6D71: 07              RLCA                        
6D72: 22              LD      (HLI),A             
6D73: 23              INC     HL                  
6D74: 02              LD      (BC),A              
6D75: 03              INC     BC                  
6D76: 23              INC     HL                  
6D77: AE              XOR     (HL)                
6D78: AE              XOR     (HL)                
6D79: AE              XOR     (HL)                
6D7A: 98              SBC     B                   
6D7B: A0              AND     B                   
6D7C: 03              INC     BC                  
6D7D: AE              XOR     (HL)                
6D7E: AE              XOR     (HL)                
6D7F: 30 31           JR      NC,$6DB2            ; {}
6D81: 98              SBC     B                   
6D82: AC              XOR     H                   
6D83: 07              RLCA                        
6D84: 32              LD      (HLD),A             
6D85: 33              INC     SP                  
6D86: 12              LD      (DE),A              
6D87: 13              INC     DE                  
6D88: AE              XOR     (HL)                
6D89: AE              XOR     (HL)                
6D8A: AE              XOR     (HL)                
6D8B: AE              XOR     (HL)                
6D8C: 98              SBC     B                   
6D8D: C0              RET     NZ                  
6D8E: 03              INC     BC                  
6D8F: AE              XOR     (HL)                
6D90: AE              XOR     (HL)                
6D91: E1              POP     HL                  
6D92: E2              LD      (C),A               
6D93: 98              SBC     B                   
6D94: CC 07 E3        CALL    Z,$E307             
6D97: E4                              
6D98: E7              RST     0X20                
6D99: E8 AE           ADD     SP,$AE              
6D9B: AE              XOR     (HL)                
6D9C: AE              XOR     (HL)                
6D9D: AE              XOR     (HL)                
6D9E: 98              SBC     B                   
6D9F: E0 03           LD      ($FF00+$03),A       
6DA1: AE              XOR     (HL)                
6DA2: AE              XOR     (HL)                
6DA3: F1              POP     AF                  
6DA4: F2                              
6DA5: 98              SBC     B                   
6DA6: EC                              
6DA7: 07              RLCA                        
6DA8: F3              DI                          
6DA9: F4                              
6DAA: F7              RST     0X30                
6DAB: AE              XOR     (HL)                
6DAC: AE              XOR     (HL)                
6DAD: AE              XOR     (HL)                
6DAE: AE              XOR     (HL)                
6DAF: AE              XOR     (HL)                
6DB0: 99              SBC     C                   
6DB1: 00              NOP                         
6DB2: 05              DEC     B                   
6DB3: 02              LD      (BC),A              
6DB4: 03              INC     BC                  
6DB5: 00              NOP                         
6DB6: 01 80 81        LD      BC,$8180            
6DB9: 99              SBC     C                   
6DBA: 0A              LD      A,(BC)              
6DBB: 09              ADD     HL,BC               
6DBC: E5              PUSH    HL                  
6DBD: E6 E7           AND     $E7                 
6DBF: E8 AE           ADD     SP,$AE              
6DC1: AE              XOR     (HL)                
6DC2: AE              XOR     (HL)                
6DC3: AE              XOR     (HL)                
6DC4: AE              XOR     (HL)                
6DC5: AE              XOR     (HL)                
6DC6: 99              SBC     C                   
6DC7: 20 05           JR      NZ,$6DCE            ; {}
6DC9: 12              LD      (DE),A              
6DCA: 13              INC     DE                  
6DCB: 10 11           ;;STOP    $11                 
6DCD: 90              SUB     B                   
6DCE: 91              SUB     C                   
6DCF: 99              SBC     C                   
6DD0: 2A              LD      A,(HLI)             
6DD1: 09              ADD     HL,BC               
6DD2: F5              PUSH    AF                  
6DD3: F6 F7           OR      $F7                 
6DD5: AE              XOR     (HL)                
6DD6: AE              XOR     (HL)                
6DD7: AE              XOR     (HL)                
6DD8: AE              XOR     (HL)                
6DD9: AE              XOR     (HL)                
6DDA: AE              XOR     (HL)                
6DDB: AE              XOR     (HL)                
6DDC: 99              SBC     C                   
6DDD: 40              LD      B,B                 
6DDE: 13              INC     DE                  
6DDF: 23              INC     HL                  
6DE0: AE              XOR     (HL)                
6DE1: AE              XOR     (HL)                
6DE2: AE              XOR     (HL)                
6DE3: A0              AND     B                   
6DE4: A1              AND     C                   
6DE5: E1              POP     HL                  
6DE6: E2              LD      (C),A               
6DE7: AC              XOR     H                   
6DE8: AC              XOR     H                   
6DE9: 22              LD      (HLI),A             
6DEA: 23              INC     HL                  
6DEB: AE              XOR     (HL)                
6DEC: AE              XOR     (HL)                
6DED: AE              XOR     (HL)                
6DEE: AE              XOR     (HL)                
6DEF: AE              XOR     (HL)                
6DF0: AE              XOR     (HL)                
6DF1: AE              XOR     (HL)                
6DF2: AE              XOR     (HL)                
6DF3: 99              SBC     C                   
6DF4: 60              LD      H,B                 
6DF5: 13              INC     DE                  
6DF6: AE              XOR     (HL)                
6DF7: AE              XOR     (HL)                
6DF8: AE              XOR     (HL)                
6DF9: 23              INC     HL                  
6DFA: B0              OR      B                   
6DFB: B1              OR      C                   
6DFC: F1              POP     AF                  
6DFD: F2                              
6DFE: AC              XOR     H                   
6DFF: AC              XOR     H                   
6E00: 32              LD      (HLD),A             
6E01: 33              INC     SP                  
6E02: 23              INC     HL                  
6E03: AE              XOR     (HL)                
6E04: AE              XOR     (HL)                
6E05: AE              XOR     (HL)                
6E06: AE              XOR     (HL)                
6E07: AE              XOR     (HL)                
6E08: AE              XOR     (HL)                
6E09: AE              XOR     (HL)                
6E0A: 99              SBC     C                   
6E0B: 80              ADD     A,B                 
6E0C: 13              INC     DE                  
6E0D: 82              ADD     A,D                 
6E0E: 83              ADD     A,E                 
6E0F: 82              ADD     A,D                 
6E10: 83              ADD     A,E                 
6E11: 82              ADD     A,D                 
6E12: 83              ADD     A,E                 
6E13: 82              ADD     A,D                 
6E14: 83              ADD     A,E                 
6E15: 82              ADD     A,D                 
6E16: 83              ADD     A,E                 
6E17: 82              ADD     A,D                 
6E18: 83              ADD     A,E                 
6E19: 82              ADD     A,D                 
6E1A: 83              ADD     A,E                 
6E1B: 82              ADD     A,D                 
6E1C: 83              ADD     A,E                 
6E1D: 82              ADD     A,D                 
6E1E: 83              ADD     A,E                 
6E1F: 82              ADD     A,D                 
6E20: 83              ADD     A,E                 
6E21: 99              SBC     C                   
6E22: A0              AND     B                   
6E23: 13              INC     DE                  
6E24: 92              SUB     D                   
6E25: 93              SUB     E                   
6E26: 92              SUB     D                   
6E27: 93              SUB     E                   
6E28: 92              SUB     D                   
6E29: 93              SUB     E                   
6E2A: 92              SUB     D                   
6E2B: 93              SUB     E                   
6E2C: 92              SUB     D                   
6E2D: 93              SUB     E                   
6E2E: 92              SUB     D                   
6E2F: 93              SUB     E                   
6E30: 92              SUB     D                   
6E31: 93              SUB     E                   
6E32: 92              SUB     D                   
6E33: 93              SUB     E                   
6E34: 92              SUB     D                   
6E35: 93              SUB     E                   
6E36: 92              SUB     D                   
6E37: 93              SUB     E                   
6E38: 9C              SBC     H                   
6E39: 00              NOP                         
6E3A: 5F              LD      E,A                 
6E3B: AC              XOR     H                   
6E3C: 9C              SBC     H                   
6E3D: 20 5F           JR      NZ,$6E9E            ; {}
6E3F: AC              XOR     H                   
6E40: 9C              SBC     H                   
6E41: 40              LD      B,B                 
6E42: 5F              LD      E,A                 
6E43: AC              XOR     H                   
6E44: 9C              SBC     H                   
6E45: 60              LD      H,B                 
6E46: 5F              LD      E,A                 
6E47: AC              XOR     H                   
6E48: 9C              SBC     H                   
6E49: 80              ADD     A,B                 
6E4A: 5F              LD      E,A                 
6E4B: AC              XOR     H                   
6E4C: 9C              SBC     H                   
6E4D: A0              AND     B                   
6E4E: 5F              LD      E,A                 
6E4F: AC              XOR     H                   
6E50: 9C              SBC     H                   
6E51: C0              RET     NZ                  
6E52: 5F              LD      E,A                 
6E53: AC              XOR     H                   
6E54: 9C              SBC     H                   
6E55: E0 5F           LD      ($FF00+$5F),A       
6E57: AC              XOR     H                   
6E58: 9D              SBC     L                   
6E59: 00              NOP                         
6E5A: 5F              LD      E,A                 
6E5B: AC              XOR     H                   
6E5C: 9D              SBC     L                   
6E5D: 20 5F           JR      NZ,$6EBE            ; {}
6E5F: AC              XOR     H                   
6E60: 9D              SBC     L                   
6E61: 40              LD      B,B                 
6E62: 5F              LD      E,A                 
6E63: AC              XOR     H                   
6E64: 9D              SBC     L                   
6E65: 60              LD      H,B                 
6E66: 5F              LD      E,A                 
6E67: AC              XOR     H                   
6E68: 9D              SBC     L                   
6E69: 80              ADD     A,B                 
6E6A: 5F              LD      E,A                 
6E6B: AC              XOR     H                   
6E6C: 9D              SBC     L                   
6E6D: A0              AND     B                   
6E6E: 5F              LD      E,A                 
6E6F: AC              XOR     H                   
6E70: 9D              SBC     L                   
6E71: C0              RET     NZ                  
6E72: 5F              LD      E,A                 
6E73: AC              XOR     H                   
6E74: 9D              SBC     L                   
6E75: E0 5F           LD      ($FF00+$5F),A       
6E77: AC              XOR     H                   
6E78: 9E              SBC     (HL)                
6E79: 00              NOP                         
6E7A: 5F              LD      E,A                 
6E7B: AC              XOR     H                   
6E7C: 9E              SBC     (HL)                
6E7D: 20 5F           JR      NZ,$6EDE            ; {}
6E7F: AC              XOR     H                   
6E80: 00              NOP                         
6E81: 9A              SBC     D                   
6E82: 00              NOP                         
6E83: 53              LD      D,E                 
6E84: 7E              LD      A,(HL)              
6E85: 9A              SBC     D                   
6E86: 20 53           JR      NZ,$6EDB            ; {}
6E88: 7E              LD      A,(HL)              
6E89: 9A              SBC     D                   
6E8A: 40              LD      B,B                 
6E8B: 53              LD      D,E                 
6E8C: 7E              LD      A,(HL)              
6E8D: 9A              SBC     D                   
6E8E: 60              LD      H,B                 
6E8F: 53              LD      D,E                 
6E90: 7E              LD      A,(HL)              
6E91: 9A              SBC     D                   
6E92: 80              ADD     A,B                 
6E93: 53              LD      D,E                 
6E94: 7E              LD      A,(HL)              
6E95: 9A              SBC     D                   
6E96: A0              AND     B                   
6E97: 53              LD      D,E                 
6E98: 7E              LD      A,(HL)              
6E99: 9A              SBC     D                   
6E9A: C0              RET     NZ                  
6E9B: 53              LD      D,E                 
6E9C: 7E              LD      A,(HL)              
6E9D: 9A              SBC     D                   
6E9E: E0 53           LD      ($FF00+$53),A       
6EA0: 7E              LD      A,(HL)              
6EA1: 9B              SBC     E                   
6EA2: 00              NOP                         
6EA3: 53              LD      D,E                 
6EA4: 7E              LD      A,(HL)              
6EA5: 9B              SBC     E                   
6EA6: 20 53           JR      NZ,$6EFB            ; {}
6EA8: 7E              LD      A,(HL)              
6EA9: 9B              SBC     E                   
6EAA: 40              LD      B,B                 
6EAB: 53              LD      D,E                 
6EAC: 7E              LD      A,(HL)              
6EAD: 9B              SBC     E                   
6EAE: 60              LD      H,B                 
6EAF: 53              LD      D,E                 
6EB0: 7E              LD      A,(HL)              
6EB1: 9B              SBC     E                   
6EB2: 80              ADD     A,B                 
6EB3: 53              LD      D,E                 
6EB4: 7E              LD      A,(HL)              
6EB5: 9B              SBC     E                   
6EB6: A0              AND     B                   
6EB7: 53              LD      D,E                 
6EB8: 7E              LD      A,(HL)              
6EB9: 9B              SBC     E                   
6EBA: C0              RET     NZ                  
6EBB: 53              LD      D,E                 
6EBC: 7E              LD      A,(HL)              
6EBD: 9B              SBC     E                   
6EBE: E0 53           LD      ($FF00+$53),A       
6EC0: 7E              LD      A,(HL)              
6EC1: 00              NOP                         
6EC2: 98              SBC     B                   
6EC3: 00              NOP                         
6EC4: 13              INC     DE                  
6EC5: FC                              
6EC6: 3B              DEC     SP                  
6EC7: 52              LD      D,D                 
6EC8: 52              LD      D,D                 
6EC9: 52              LD      D,D                 
6ECA: 52              LD      D,D                 
6ECB: 52              LD      D,D                 
6ECC: 52              LD      D,D                 
6ECD: 52              LD      D,D                 
6ECE: 52              LD      D,D                 
6ECF: 52              LD      D,D                 
6ED0: 52              LD      D,D                 
6ED1: 52              LD      D,D                 
6ED2: 52              LD      D,D                 
6ED3: 52              LD      D,D                 
6ED4: 52              LD      D,D                 
6ED5: 52              LD      D,D                 
6ED6: 52              LD      D,D                 
6ED7: 3C              INC     A                   
6ED8: FC                              
6ED9: 9A              SBC     D                   
6EDA: 20 13           JR      NZ,$6EEF            ; {}
6EDC: FC                              
6EDD: 4B              LD      C,E                 
6EDE: 4F              LD      C,A                 
6EDF: 4E              LD      C,(HL)              
6EE0: 4E              LD      C,(HL)              
6EE1: 4E              LD      C,(HL)              
6EE2: 4E              LD      C,(HL)              
6EE3: 4D              LD      C,L                 
6EE4: 53              LD      D,E                 
6EE5: 53              LD      D,E                 
6EE6: 4F              LD      C,A                 
6EE7: 4E              LD      C,(HL)              
6EE8: 4D              LD      C,L                 
6EE9: 53              LD      D,E                 
6EEA: 53              LD      D,E                 
6EEB: 53              LD      D,E                 
6EEC: 53              LD      D,E                 
6EED: 53              LD      D,E                 
6EEE: 4C              LD      C,H                 
6EEF: FC                              
6EF0: 98              SBC     B                   
6EF1: 20 CF           JR      NZ,$6EC2            ; {}
6EF3: FC                              
6EF4: 98              SBC     B                   
6EF5: 33              INC     SP                  
6EF6: CF              RST     0X08                
6EF7: FC                              
6EF8: 98              SBC     B                   
6EF9: 21 CF 50        LD      HL,$50CF            
6EFC: 98              SBC     B                   
6EFD: 32              LD      (HLD),A             
6EFE: CF              RST     0X08                
6EFF: 51              LD      D,C                 
6F00: 00              NOP                         
6F01: 99              SBC     C                   
6F02: E6 0A           AND     $0A                 
6F04: 04              INC     B                   
6F05: 11 00 12        LD      DE,$1200            
6F08: 04              INC     B                   
6F09: 7E              LD      A,(HL)              
6F0A: 7E              LD      A,(HL)              
6F0B: 02              LD      (BC),A              
6F0C: 0E 0F           LD      C,$0F               
6F0E: 18 98           JR      $6EA8               ; {}
6F10: 00              NOP                         
6F11: 48              LD      C,B                 
6F12: 8F              ADC     A,A                 
6F13: 98              SBC     B                   
6F14: 01 00 9F        LD      BC,$9F00            
6F17: 98              SBC     B                   
6F18: 03              INC     BC                  
6F19: 00              NOP                         
6F1A: 9F              SBC     A                   
6F1B: 98              SBC     B                   
6F1C: 05              DEC     B                   
6F1D: 00              NOP                         
6F1E: 9F              SBC     A                   
6F1F: 98              SBC     B                   
6F20: 07              RLCA                        
6F21: 00              NOP                         
6F22: 9F              SBC     A                   
6F23: 98              SBC     B                   
6F24: 09              ADD     HL,BC               
6F25: 00              NOP                         
6F26: 9F              SBC     A                   
6F27: 98              SBC     B                   
6F28: 20 08           JR      NZ,$6F32            ; {}
6F2A: 9F              SBC     A                   
6F2B: 80              ADD     A,B                 
6F2C: 81              ADD     A,C                 
6F2D: 82              ADD     A,D                 
6F2E: 83              ADD     A,E                 
6F2F: 84              ADD     A,H                 
6F30: 89              ADC     A,C                 
6F31: 8F              ADC     A,A                 
6F32: 9F              SBC     A                   
6F33: 98              SBC     B                   
6F34: 40              LD      B,B                 
6F35: 08 8F 90        LD      ($908F),SP          
6F38: 91              SUB     C                   
6F39: 92              SUB     D                   
6F3A: 93              SUB     E                   
6F3B: 94              SUB     H                   
6F3C: AA              XOR     D                   
6F3D: 9F              SBC     A                   
6F3E: 8F              ADC     A,A                 
6F3F: 98              SBC     B                   
6F40: 60              LD      H,B                 
6F41: 08 9F 8A        LD      ($8A9F),SP          
6F44: 8B              ADC     A,E                 
6F45: 8C              ADC     A,H                 
6F46: 8D              ADC     A,L                 
6F47: 8E              ADC     A,(HL)              
6F48: AF              XOR     A                   
6F49: 8F              ADC     A,A                 
6F4A: 9F              SBC     A                   
6F4B: 98              SBC     B                   
6F4C: 80              ADD     A,B                 
6F4D: 52              LD      D,D                 
6F4E: 8F              ADC     A,A                 
6F4F: 98              SBC     B                   
6F50: 81              ADD     A,C                 
6F51: 00              NOP                         
6F52: 9F              SBC     A                   
6F53: 98              SBC     B                   
6F54: 83              ADD     A,E                 
6F55: 00              NOP                         
6F56: 9F              SBC     A                   
6F57: 98              SBC     B                   
6F58: 85              ADD     A,L                 
6F59: 00              NOP                         
6F5A: 9F              SBC     A                   
6F5B: 98              SBC     B                   
6F5C: 87              ADD     A,A                 
6F5D: 00              NOP                         
6F5E: 9F              SBC     A                   
6F5F: 98              SBC     B                   
6F60: 89              ADC     A,C                 
6F61: 00              NOP                         
6F62: 9F              SBC     A                   
6F63: 98              SBC     B                   
6F64: 8B              ADC     A,E                 
6F65: 00              NOP                         
6F66: 9F              SBC     A                   
6F67: 98              SBC     B                   
6F68: 8D              ADC     A,L                 
6F69: 00              NOP                         
6F6A: 9F              SBC     A                   
6F6B: 98              SBC     B                   
6F6C: 8F              ADC     A,A                 
6F6D: 00              NOP                         
6F6E: 9F              SBC     A                   
6F6F: 98              SBC     B                   
6F70: 91              SUB     C                   
6F71: 00              NOP                         
6F72: 9F              SBC     A                   
6F73: 98              SBC     B                   
6F74: 93              SUB     E                   
6F75: 00              NOP                         
6F76: 9F              SBC     A                   
6F77: 98              SBC     B                   
6F78: A0              AND     B                   
6F79: CB 9F           RES     1,E                 
6F7B: 98              SBC     B                   
6F7C: C0              RET     NZ                  
6F7D: 00              NOP                         
6F7E: 8F              ADC     A,A                 
6F7F: 99              SBC     C                   
6F80: 00              NOP                         
6F81: 00              NOP                         
6F82: 8F              ADC     A,A                 
6F83: 99              SBC     C                   
6F84: 40              LD      B,B                 
6F85: 00              NOP                         
6F86: 8F              ADC     A,A                 
6F87: 99              SBC     C                   
6F88: 80              ADD     A,B                 
6F89: 00              NOP                         
6F8A: 8F              ADC     A,A                 
6F8B: 99              SBC     C                   
6F8C: C0              RET     NZ                  
6F8D: 00              NOP                         
6F8E: 8F              ADC     A,A                 
6F8F: 9A              SBC     D                   
6F90: 00              NOP                         
6F91: 00              NOP                         
6F92: 8F              ADC     A,A                 
6F93: 9A              SBC     D                   
6F94: 20 00           JR      NZ,$6F96            ; {}
6F96: 9F              SBC     A                   
6F97: 9A              SBC     D                   
6F98: 21 50 8F        LD      HL,$8F50            
6F9B: 9A              SBC     D                   
6F9C: 22              LD      (HLI),A             
6F9D: 00              NOP                         
6F9E: 9F              SBC     A                   
6F9F: 9A              SBC     D                   
6FA0: 24              INC     H                   
6FA1: 00              NOP                         
6FA2: 9F              SBC     A                   
6FA3: 9A              SBC     D                   
6FA4: 26 00           LD      H,$00               
6FA6: 9F              SBC     A                   
6FA7: 9A              SBC     D                   
6FA8: 28 00           JR      Z,$6FAA             ; {}
6FAA: 9F              SBC     A                   
6FAB: 9A              SBC     D                   
6FAC: 2A              LD      A,(HLI)             
6FAD: 00              NOP                         
6FAE: 9F              SBC     A                   
6FAF: 9A              SBC     D                   
6FB0: 2C              INC     L                   
6FB1: 00              NOP                         
6FB2: 9F              SBC     A                   
6FB3: 9A              SBC     D                   
6FB4: 2E 00           LD      L,$00               
6FB6: 9F              SBC     A                   
6FB7: 9A              SBC     D                   
6FB8: 30 00           JR      NC,$6FBA            ; {}
6FBA: 9F              SBC     A                   
6FBB: 9A              SBC     D                   
6FBC: 32              LD      (HLD),A             
6FBD: 00              NOP                         
6FBE: 8F              ADC     A,A                 
6FBF: 98              SBC     B                   
6FC0: B3              OR      E                   
6FC1: CA 8F 98        JP      Z,$988F             
6FC4: D3                              
6FC5: 00              NOP                         
6FC6: 9F              SBC     A                   
6FC7: 99              SBC     C                   
6FC8: 13              INC     DE                  
6FC9: 00              NOP                         
6FCA: 9F              SBC     A                   
6FCB: 99              SBC     C                   
6FCC: 53              LD      D,E                 
6FCD: 00              NOP                         
6FCE: 9F              SBC     A                   
6FCF: 99              SBC     C                   
6FD0: 93              SUB     E                   
6FD1: 00              NOP                         
6FD2: 9F              SBC     A                   
6FD3: 99              SBC     C                   
6FD4: D3                              
6FD5: 00              NOP                         
6FD6: 9F              SBC     A                   
6FD7: 9A              SBC     D                   
6FD8: 13              INC     DE                  
6FD9: 00              NOP                         
6FDA: 9F              SBC     A                   
6FDB: 9A              SBC     D                   
6FDC: 33              INC     SP                  
6FDD: 00              NOP                         
6FDE: 9F              SBC     A                   
6FDF: 98              SBC     B                   
6FE0: 0A              LD      A,(BC)              
6FE1: 49              LD      C,C                 
6FE2: 7F              LD      A,A                 
6FE3: 98              SBC     B                   
6FE4: 29              ADD     HL,HL               
6FE5: 4A              LD      C,D                 
6FE6: 7F              LD      A,A                 
6FE7: 98              SBC     B                   
6FE8: 69              LD      L,C                 
6FE9: 4A              LD      C,D                 
6FEA: A2              AND     D                   
6FEB: 98              SBC     B                   
6FEC: 49              LD      C,C                 
6FED: 0A              LD      A,(BC)              
6FEE: A1              AND     C                   
6FEF: A0              AND     B                   
6FF0: A1              AND     C                   
6FF1: A5              AND     L                   
6FF2: A6              AND     (HL)                
6FF3: A0              AND     B                   
6FF4: A1              AND     C                   
6FF5: A5              AND     L                   
6FF6: A6              AND     (HL)                
6FF7: A0              AND     B                   
6FF8: A1              AND     C                   
6FF9: 98              SBC     B                   
6FFA: 2C              INC     L                   
6FFB: 01 A3 A4        LD      BC,$A4A3            
6FFE: 98              SBC     B                   
6FFF: 30 01           JR      NC,$7002            ; {}
7001: A3              AND     E                   
7002: A4              AND     H                   
7003: 98              SBC     B                   
7004: 6C              LD      L,H                 
7005: 01 A7 A8        LD      BC,$A8A7            
7008: 98              SBC     B                   
7009: 70              LD      (HL),B              
700A: 01 A7 A8        LD      BC,$A8A7            
700D: 98              SBC     B                   
700E: C4 00 AB        CALL    NZ,$AB00            
7011: 99              SBC     C                   
7012: 24              INC     H                   
7013: 00              NOP                         
7014: AC              XOR     H                   
7015: 99              SBC     C                   
7016: 84              ADD     A,H                 
7017: 00              NOP                         
7018: AD              XOR     L                   
7019: 99              SBC     C                   
701A: C2 4F A9        JP      NZ,$A94F            
701D: 00              NOP                         
701E: 98              SBC     B                   
701F: 00              NOP                         
7020: 50              LD      D,B                 
7021: 8F              ADC     A,A                 
7022: 98              SBC     B                   
7023: 01 00 9F        LD      BC,$9F00            
7026: 98              SBC     B                   
7027: 03              INC     BC                  
7028: 00              NOP                         
7029: 9F              SBC     A                   
702A: 98              SBC     B                   
702B: 05              DEC     B                   
702C: 00              NOP                         
702D: 9F              SBC     A                   
702E: 98              SBC     B                   
702F: 07              RLCA                        
7030: 00              NOP                         
7031: 9F              SBC     A                   
7032: 98              SBC     B                   
7033: 09              ADD     HL,BC               
7034: 00              NOP                         
7035: 9F              SBC     A                   
7036: 98              SBC     B                   
7037: 0B              DEC     BC                  
7038: 00              NOP                         
7039: 9F              SBC     A                   
703A: 98              SBC     B                   
703B: 0D              DEC     C                   
703C: 00              NOP                         
703D: 9F              SBC     A                   
703E: 98              SBC     B                   
703F: 0F              RRCA                        
7040: 00              NOP                         
7041: 9F              SBC     A                   
7042: 98              SBC     B                   
7043: 20 06           JR      NZ,$704B            ; {}
7045: 9F              SBC     A                   
7046: 85              ADD     A,L                 
7047: 86              ADD     A,(HL)              
7048: 87              ADD     A,A                 
7049: 88              ADC     A,B                 
704A: 8F              ADC     A,A                 
704B: 9F              SBC     A                   
704C: 98              SBC     B                   
704D: 40              LD      B,B                 
704E: 06 8F           LD      B,$8F               
7050: 95              SUB     L                   
7051: 96              SUB     (HL)                
7052: 97              SUB     A                   
7053: 98              SBC     B                   
7054: 99              SBC     C                   
7055: 8F              ADC     A,A                 
7056: 98              SBC     B                   
7057: 60              LD      H,B                 
7058: 06 9F           LD      B,$9F               
705A: 9A              SBC     D                   
705B: 9B              SBC     E                   
705C: 9C              SBC     H                   
705D: 9D              SBC     L                   
705E: 9E              SBC     (HL)                
705F: 9F              SBC     A                   
7060: 98              SBC     B                   
7061: 2F              CPL                         
7062: 00              NOP                         
7063: 8F              ADC     A,A                 
7064: 98              SBC     B                   
7065: 4F              LD      C,A                 
7066: 00              NOP                         
7067: 9F              SBC     A                   
7068: 98              SBC     B                   
7069: 6F              LD      L,A                 
706A: 00              NOP                         
706B: 8F              ADC     A,A                 
706C: 98              SBC     B                   
706D: 11 42 7F        LD      DE,$7F42            
7070: 98              SBC     B                   
7071: 30 43           JR      NC,$70B6            ; {}
7073: 7F              LD      A,A                 
7074: 98              SBC     B                   
7075: 50              LD      D,B                 
7076: 03              INC     BC                  
7077: A1              AND     C                   
7078: A0              AND     B                   
7079: A1              AND     C                   
707A: A0              AND     B                   
707B: 98              SBC     B                   
707C: 70              LD      (HL),B              
707D: 43              LD      B,E                 
707E: A2              AND     D                   
707F: 98              SBC     B                   
7080: 80              ADD     A,B                 
7081: 52              LD      D,D                 
7082: 8F              ADC     A,A                 
7083: 98              SBC     B                   
7084: 81              ADD     A,C                 
7085: 00              NOP                         
7086: 9F              SBC     A                   
7087: 98              SBC     B                   
7088: 83              ADD     A,E                 
7089: 00              NOP                         
708A: 9F              SBC     A                   
708B: 98              SBC     B                   
708C: 85              ADD     A,L                 
708D: 00              NOP                         
708E: 9F              SBC     A                   
708F: 98              SBC     B                   
7090: 87              ADD     A,A                 
7091: 00              NOP                         
7092: 9F              SBC     A                   
7093: 98              SBC     B                   
7094: 89              ADC     A,C                 
7095: 00              NOP                         
7096: 9F              SBC     A                   
7097: 98              SBC     B                   
7098: 8B              ADC     A,E                 
7099: 00              NOP                         
709A: 9F              SBC     A                   
709B: 98              SBC     B                   
709C: 8D              ADC     A,L                 
709D: 00              NOP                         
709E: 9F              SBC     A                   
709F: 98              SBC     B                   
70A0: 8F              ADC     A,A                 
70A1: 00              NOP                         
70A2: 9F              SBC     A                   
70A3: 98              SBC     B                   
70A4: 91              SUB     C                   
70A5: 00              NOP                         
70A6: 9F              SBC     A                   
70A7: 98              SBC     B                   
70A8: 93              SUB     E                   
70A9: 00              NOP                         
70AA: 9F              SBC     A                   
70AB: 98              SBC     B                   
70AC: A0              AND     B                   
70AD: C9              RET                         
70AE: 9F              SBC     A                   
70AF: 98              SBC     B                   
70B0: C0              RET     NZ                  
70B1: 00              NOP                         
70B2: 8F              ADC     A,A                 
70B3: 99              SBC     C                   
70B4: 00              NOP                         
70B5: 00              NOP                         
70B6: 8F              ADC     A,A                 
70B7: 99              SBC     C                   
70B8: 40              LD      B,B                 
70B9: 00              NOP                         
70BA: 8F              ADC     A,A                 
70BB: 99              SBC     C                   
70BC: 80              ADD     A,B                 
70BD: 00              NOP                         
70BE: 8F              ADC     A,A                 
70BF: 99              SBC     C                   
70C0: C0              RET     NZ                  
70C1: 00              NOP                         
70C2: 8F              ADC     A,A                 
70C3: 98              SBC     B                   
70C4: B3              OR      E                   
70C5: C9              RET                         
70C6: 8F              ADC     A,A                 
70C7: 98              SBC     B                   
70C8: D3                              
70C9: 00              NOP                         
70CA: 9F              SBC     A                   
70CB: 99              SBC     C                   
70CC: 13              INC     DE                  
70CD: 00              NOP                         
70CE: 9F              SBC     A                   
70CF: 99              SBC     C                   
70D0: 53              LD      D,E                 
70D1: 00              NOP                         
70D2: 9F              SBC     A                   
70D3: 99              SBC     C                   
70D4: 93              SUB     E                   
70D5: 00              NOP                         
70D6: 9F              SBC     A                   
70D7: 99              SBC     C                   
70D8: D3                              
70D9: 00              NOP                         
70DA: 9F              SBC     A                   
70DB: 9A              SBC     D                   
70DC: 20 52           JR      NZ,$7130            ; {}
70DE: 9F              SBC     A                   
70DF: 9A              SBC     D                   
70E0: 21 00 8F        LD      HL,$8F00            
70E3: 9A              SBC     D                   
70E4: 23              INC     HL                  
70E5: 00              NOP                         
70E6: 8F              ADC     A,A                 
70E7: 9A              SBC     D                   
70E8: 25              DEC     H                   
70E9: 00              NOP                         
70EA: 8F              ADC     A,A                 
70EB: 9A              SBC     D                   
70EC: 27              DAA                         
70ED: 00              NOP                         
70EE: 8F              ADC     A,A                 
70EF: 9A              SBC     D                   
70F0: 29              ADD     HL,HL               
70F1: 00              NOP                         
70F2: 8F              ADC     A,A                 
70F3: 9A              SBC     D                   
70F4: 2B              DEC     HL                  
70F5: 00              NOP                         
70F6: 8F              ADC     A,A                 
70F7: 9A              SBC     D                   
70F8: 2D              DEC     L                   
70F9: 00              NOP                         
70FA: 8F              ADC     A,A                 
70FB: 9A              SBC     D                   
70FC: 2F              CPL                         
70FD: 00              NOP                         
70FE: 8F              ADC     A,A                 
70FF: 9A              SBC     D                   
7100: 31 00 8F        LD      SP,$8F00            
7103: 9A              SBC     D                   
7104: 33              INC     SP                  
7105: 00              NOP                         
7106: 8F              ADC     A,A                 
7107: 98              SBC     B                   
7108: C2 06 00        JP      NZ,$0006            
710B: 01 02 03        LD      BC,$0302            
710E: 04              INC     B                   
710F: 05              DEC     B                   
7110: 06 99           LD      B,$99               
7112: 02              LD      (BC),A              
7113: 06 07           LD      B,$07               
7115: 08 09 0A        LD      ($0A09),SP          
7118: 0B              DEC     BC                  
7119: 0C              INC     C                   
711A: 0D              DEC     C                   
711B: 99              SBC     C                   
711C: 42              LD      B,D                 
711D: 06 0E           LD      B,$0E               
711F: 0F              RRCA                        
7120: 10 11           ;;STOP    $11                 
7122: 12              LD      (DE),A              
7123: 13              INC     DE                  
7124: 14              INC     D                   
7125: 99              SBC     C                   
7126: 82              ADD     A,D                 
7127: 04              INC     B                   
7128: 15              DEC     D                   
7129: 16 17           LD      D,$17               
712B: 18 19           JR      $7146               ; {}
712D: 98              SBC     B                   
712E: CB 06           RLC     1,E                 
7130: 1A              LD      A,(DE)              
7131: 1B              DEC     DE                  
7132: 1C              INC     E                   
7133: 1D              DEC     E                   
7134: 1E 1F           LD      E,$1F               
7136: 20 99           JR      NZ,$70D1            ; {}
7138: 0B              DEC     BC                  
7139: 06 21           LD      B,$21               
713B: 22              LD      (HLI),A             
713C: 23              INC     HL                  
713D: 24              INC     H                   
713E: 25              DEC     H                   
713F: 26 27           LD      H,$27               
7141: 99              SBC     C                   
7142: 4B              LD      C,E                 
7143: 06 28           LD      B,$28               
7145: 29              ADD     HL,HL               
7146: 2A              LD      A,(HLI)             
7147: 2B              DEC     HL                  
7148: 2C              INC     L                   
7149: 2D              DEC     L                   
714A: 2E 99           LD      L,$99               
714C: 8B              ADC     A,E                 
714D: 04              INC     B                   
714E: 2F              CPL                         
714F: 30 31           JR      NC,$7182            ; {}
7151: 32              LD      (HLD),A             
7152: 3E 00           LD      A,$00               
7154: 98              SBC     B                   
7155: 00              NOP                         
7156: 52              LD      D,D                 
7157: 8F              ADC     A,A                 
7158: 98              SBC     B                   
7159: 01 00 9F        LD      BC,$9F00            
715C: 98              SBC     B                   
715D: 03              INC     BC                  
715E: 00              NOP                         
715F: 9F              SBC     A                   
7160: 98              SBC     B                   
7161: 05              DEC     B                   
7162: 00              NOP                         
7163: 9F              SBC     A                   
7164: 98              SBC     B                   
7165: 07              RLCA                        
7166: 00              NOP                         
7167: 9F              SBC     A                   
7168: 98              SBC     B                   
7169: 09              ADD     HL,BC               
716A: 00              NOP                         
716B: 9F              SBC     A                   
716C: 98              SBC     B                   
716D: 0B              DEC     BC                  
716E: 00              NOP                         
716F: 9F              SBC     A                   
7170: 98              SBC     B                   
7171: 0D              DEC     C                   
7172: 00              NOP                         
7173: 9F              SBC     A                   
7174: 98              SBC     B                   
7175: 0F              RRCA                        
7176: 00              NOP                         
7177: 9F              SBC     A                   
7178: 98              SBC     B                   
7179: 11 00 9F        LD      DE,$9F00            
717C: 98              SBC     B                   
717D: 13              INC     DE                  
717E: 00              NOP                         
717F: 9F              SBC     A                   
7180: 98              SBC     B                   
7181: 20 D1           JR      NZ,$7154            ; {}
7183: 9F              SBC     A                   
7184: 98              SBC     B                   
7185: 40              LD      B,B                 
7186: 00              NOP                         
7187: 8F              ADC     A,A                 
7188: 98              SBC     B                   
7189: 80              ADD     A,B                 
718A: 00              NOP                         
718B: 8F              ADC     A,A                 
718C: 98              SBC     B                   
718D: C0              RET     NZ                  
718E: 00              NOP                         
718F: 8F              ADC     A,A                 
7190: 99              SBC     C                   
7191: 00              NOP                         
7192: 00              NOP                         
7193: 8F              ADC     A,A                 
7194: 99              SBC     C                   
7195: 40              LD      B,B                 
7196: 00              NOP                         
7197: 8F              ADC     A,A                 
7198: 99              SBC     C                   
7199: 80              ADD     A,B                 
719A: 00              NOP                         
719B: 8F              ADC     A,A                 
719C: 99              SBC     C                   
719D: C0              RET     NZ                  
719E: 00              NOP                         
719F: 8F              ADC     A,A                 
71A0: 9A              SBC     D                   
71A1: 00              NOP                         
71A2: 00              NOP                         
71A3: 8F              ADC     A,A                 
71A4: 98              SBC     B                   
71A5: 33              INC     SP                  
71A6: D1              POP     DE                  
71A7: 8F              ADC     A,A                 
71A8: 98              SBC     B                   
71A9: 53              LD      D,E                 
71AA: 00              NOP                         
71AB: 9F              SBC     A                   
71AC: 98              SBC     B                   
71AD: 93              SUB     E                   
71AE: 00              NOP                         
71AF: 9F              SBC     A                   
71B0: 98              SBC     B                   
71B1: D3                              
71B2: 00              NOP                         
71B3: 9F              SBC     A                   
71B4: 99              SBC     C                   
71B5: 13              INC     DE                  
71B6: 00              NOP                         
71B7: 9F              SBC     A                   
71B8: 99              SBC     C                   
71B9: 53              LD      D,E                 
71BA: 00              NOP                         
71BB: 9F              SBC     A                   
71BC: 99              SBC     C                   
71BD: 93              SUB     E                   
71BE: 00              NOP                         
71BF: 9F              SBC     A                   
71C0: 99              SBC     C                   
71C1: D3                              
71C2: 00              NOP                         
71C3: 9F              SBC     A                   
71C4: 9A              SBC     D                   
71C5: 13              INC     DE                  
71C6: 00              NOP                         
71C7: 9F              SBC     A                   
71C8: 9A              SBC     D                   
71C9: 21 50 8F        LD      HL,$8F50            
71CC: 9A              SBC     D                   
71CD: 22              LD      (HLI),A             
71CE: 00              NOP                         
71CF: 9F              SBC     A                   
71D0: 9A              SBC     D                   
71D1: 24              INC     H                   
71D2: 00              NOP                         
71D3: 9F              SBC     A                   
71D4: 9A              SBC     D                   
71D5: 26 00           LD      H,$00               
71D7: 9F              SBC     A                   
71D8: 9A              SBC     D                   
71D9: 28 00           JR      Z,$71DB             ; {}
71DB: 9F              SBC     A                   
71DC: 9A              SBC     D                   
71DD: 2A              LD      A,(HLI)             
71DE: 00              NOP                         
71DF: 9F              SBC     A                   
71E0: 9A              SBC     D                   
71E1: 2C              INC     L                   
71E2: 00              NOP                         
71E3: 9F              SBC     A                   
71E4: 9A              SBC     D                   
71E5: 2E 00           LD      L,$00               
71E7: 9F              SBC     A                   
71E8: 9A              SBC     D                   
71E9: 30 00           JR      NC,$71EB            ; {}
71EB: 9F              SBC     A                   
71EC: 9A              SBC     D                   
71ED: 32              LD      (HLD),A             
71EE: 00              NOP                         
71EF: 9F              SBC     A                   
71F0: 98              SBC     B                   
71F1: 42              LD      B,D                 
71F2: 0A              LD      A,(BC)              
71F3: 04              INC     B                   
71F4: 11 00 12        LD      DE,$1200            
71F7: 04              INC     B                   
71F8: 7E              LD      A,(HL)              
71F9: 16 07           LD      D,$07               
71FB: 08 02 07        LD      ($0702),SP          
71FE: 98              SBC     B                   
71FF: 8A              ADC     A,D                 
7200: 07              RLCA                        
7201: 0F              RRCA                        
7202: 0B              DEC     BC                  
7203: 00              NOP                         
7204: 18 04           JR      $720A               ; {}
7206: 11 7E 3C        LD      DE,$3C7E            
7209: 98              SBC     B                   
720A: C4 00 AB        CALL    NZ,$AB00            
720D: 99              SBC     C                   
720E: 24              INC     H                   
720F: 00              NOP                         
7210: AC              XOR     H                   
7211: 99              SBC     C                   
7212: 84              ADD     A,H                 
7213: 00              NOP                         
7214: AD              XOR     L                   
7215: 99              SBC     C                   
7216: C2 4F A9        JP      NZ,$A94F            
7219: 99              SBC     C                   
721A: E4                              
721B: 0D              DEC     C                   
721C: 11 04 13        LD      DE,$1304            
721F: 14              INC     D                   
7220: 11 0D 7E        LD      DE,$7E0D            
7223: 13              INC     DE                  
7224: 0E 7E           LD      C,$7E               
7226: 0C              INC     C                   
7227: 04              INC     B                   
7228: 0D              DEC     C                   
7229: 14              INC     D                   
722A: 00              NOP                         
722B: 98              SBC     B                   
722C: 00              NOP                         
722D: 52              LD      D,D                 
722E: 8F              ADC     A,A                 
722F: 98              SBC     B                   
7230: 01 00 9F        LD      BC,$9F00            
7233: 98              SBC     B                   
7234: 03              INC     BC                  
7235: 00              NOP                         
7236: 9F              SBC     A                   
7237: 98              SBC     B                   
7238: 05              DEC     B                   
7239: 00              NOP                         
723A: 9F              SBC     A                   
723B: 98              SBC     B                   
723C: 07              RLCA                        
723D: 00              NOP                         
723E: 9F              SBC     A                   
723F: 98              SBC     B                   
7240: 09              ADD     HL,BC               
7241: 00              NOP                         
7242: 9F              SBC     A                   
7243: 98              SBC     B                   
7244: 0B              DEC     BC                  
7245: 00              NOP                         
7246: 9F              SBC     A                   
7247: 98              SBC     B                   
7248: 0D              DEC     C                   
7249: 00              NOP                         
724A: 9F              SBC     A                   
724B: 98              SBC     B                   
724C: 0F              RRCA                        
724D: 00              NOP                         
724E: 9F              SBC     A                   
724F: 98              SBC     B                   
7250: 11 00 9F        LD      DE,$9F00            
7253: 98              SBC     B                   
7254: 13              INC     DE                  
7255: 00              NOP                         
7256: 9F              SBC     A                   
7257: 98              SBC     B                   
7258: 20 D1           JR      NZ,$722B            ; {}
725A: 9F              SBC     A                   
725B: 98              SBC     B                   
725C: 40              LD      B,B                 
725D: 00              NOP                         
725E: 8F              ADC     A,A                 
725F: 98              SBC     B                   
7260: 80              ADD     A,B                 
7261: 00              NOP                         
7262: 8F              ADC     A,A                 
7263: 98              SBC     B                   
7264: C0              RET     NZ                  
7265: 00              NOP                         
7266: 8F              ADC     A,A                 
7267: 99              SBC     C                   
7268: 00              NOP                         
7269: 00              NOP                         
726A: 8F              ADC     A,A                 
726B: 99              SBC     C                   
726C: 40              LD      B,B                 
726D: 00              NOP                         
726E: 8F              ADC     A,A                 
726F: 99              SBC     C                   
7270: 80              ADD     A,B                 
7271: 00              NOP                         
7272: 8F              ADC     A,A                 
7273: 99              SBC     C                   
7274: C0              RET     NZ                  
7275: 00              NOP                         
7276: 8F              ADC     A,A                 
7277: 9A              SBC     D                   
7278: 00              NOP                         
7279: 00              NOP                         
727A: 8F              ADC     A,A                 
727B: 98              SBC     B                   
727C: 33              INC     SP                  
727D: D1              POP     DE                  
727E: 8F              ADC     A,A                 
727F: 98              SBC     B                   
7280: 53              LD      D,E                 
7281: 00              NOP                         
7282: 9F              SBC     A                   
7283: 98              SBC     B                   
7284: 93              SUB     E                   
7285: 00              NOP                         
7286: 9F              SBC     A                   
7287: 98              SBC     B                   
7288: D3                              
7289: 00              NOP                         
728A: 9F              SBC     A                   
728B: 99              SBC     C                   
728C: 13              INC     DE                  
728D: 00              NOP                         
728E: 9F              SBC     A                   
728F: 99              SBC     C                   
7290: 53              LD      D,E                 
7291: 00              NOP                         
7292: 9F              SBC     A                   
7293: 99              SBC     C                   
7294: 93              SUB     E                   
7295: 00              NOP                         
7296: 9F              SBC     A                   
7297: 99              SBC     C                   
7298: D3                              
7299: 00              NOP                         
729A: 9F              SBC     A                   
729B: 9A              SBC     D                   
729C: 13              INC     DE                  
729D: 00              NOP                         
729E: 9F              SBC     A                   
729F: 9A              SBC     D                   
72A0: 21 50 8F        LD      HL,$8F50            
72A3: 9A              SBC     D                   
72A4: 22              LD      (HLI),A             
72A5: 00              NOP                         
72A6: 9F              SBC     A                   
72A7: 9A              SBC     D                   
72A8: 24              INC     H                   
72A9: 00              NOP                         
72AA: 9F              SBC     A                   
72AB: 9A              SBC     D                   
72AC: 26 00           LD      H,$00               
72AE: 9F              SBC     A                   
72AF: 9A              SBC     D                   
72B0: 28 00           JR      Z,$72B2             ; {}
72B2: 9F              SBC     A                   
72B3: 9A              SBC     D                   
72B4: 2A              LD      A,(HLI)             
72B5: 00              NOP                         
72B6: 9F              SBC     A                   
72B7: 9A              SBC     D                   
72B8: 2C              INC     L                   
72B9: 00              NOP                         
72BA: 9F              SBC     A                   
72BB: 9A              SBC     D                   
72BC: 2E 00           LD      L,$00               
72BE: 9F              SBC     A                   
72BF: 9A              SBC     D                   
72C0: 30 00           JR      NC,$72C2            ; {}
72C2: 9F              SBC     A                   
72C3: 9A              SBC     D                   
72C4: 32              LD      (HLD),A             
72C5: 00              NOP                         
72C6: 9F              SBC     A                   
72C7: 99              SBC     C                   
72C8: C2 4F A9        JP      NZ,$A94F            
72CB: 98              SBC     B                   
72CC: 42              LD      B,D                 
72CD: 0A              LD      A,(BC)              
72CE: 02              LD      (BC),A              
72CF: 0E 0F           LD      C,$0F               
72D1: 18 7E           JR      $7351               ; {}
72D3: 0F              RRCA                        
72D4: 0B              DEC     BC                  
72D5: 00              NOP                         
72D6: 18 04           JR      $72DC               ; {}
72D8: 11 98 84        LD      DE,$8498            
72DB: 0C              INC     C                   
72DC: 3F              CCF                         
72DD: 05              DEC     B                   
72DE: 11 0E 0C        LD      DE,$0C0E            
72E1: 3F              CCF                         
72E2: 7E              LD      A,(HL)              
72E3: 7E              LD      A,(HL)              
72E4: 7E              LD      A,(HL)              
72E5: 3F              CCF                         
72E6: 13              INC     DE                  
72E7: 0E 3F           LD      C,$3F               
72E9: 98              SBC     B                   
72EA: C3 00 AB        JP      $AB00               
72ED: 98              SBC     B                   
72EE: CC 00 AB        CALL    Z,$AB00             
72F1: 99              SBC     C                   
72F2: 23              INC     HL                  
72F3: 00              NOP                         
72F4: AC              XOR     H                   
72F5: 99              SBC     C                   
72F6: 2C              INC     L                   
72F7: 00              NOP                         
72F8: AC              XOR     H                   
72F9: 99              SBC     C                   
72FA: 83              ADD     A,E                 
72FB: 00              NOP                         
72FC: AD              XOR     L                   
72FD: 99              SBC     C                   
72FE: 8C              ADC     A,H                 
72FF: 00              NOP                         
7300: AD              XOR     L                   
7301: 99              SBC     C                   
7302: E4                              
7303: 0D              DEC     C                   
7304: 11 04 13        LD      DE,$1304            
7307: 14              INC     D                   
7308: 11 0D 7E        LD      DE,$7E0D            
730B: 13              INC     DE                  
730C: 0E 7E           LD      C,$7E               
730E: 0C              INC     C                   
730F: 04              INC     B                   
7310: 0D              DEC     C                   
7311: 14              INC     D                   
7312: 00              NOP                         
7313: 9C              SBC     H                   
7314: 00              NOP                         
7315: 53              LD      D,E                 
7316: 7F              LD      A,A                 
7317: 9C              SBC     H                   
7318: 20 53           JR      NZ,$736D            ; {}
731A: 7F              LD      A,A                 
731B: 9C              SBC     H                   
731C: 40              LD      B,B                 
731D: 53              LD      D,E                 
731E: 7F              LD      A,A                 
731F: 9C              SBC     H                   
7320: 60              LD      H,B                 
7321: 53              LD      D,E                 
7322: 7F              LD      A,A                 
7323: 9C              SBC     H                   
7324: 80              ADD     A,B                 
7325: 53              LD      D,E                 
7326: 7F              LD      A,A                 
7327: 9C              SBC     H                   
7328: A0              AND     B                   
7329: 53              LD      D,E                 
732A: 7F              LD      A,A                 
732B: 9C              SBC     H                   
732C: C0              RET     NZ                  
732D: 53              LD      D,E                 
732E: 7F              LD      A,A                 
732F: 9C              SBC     H                   
7330: E0 53           LD      ($FF00+$53),A       
7332: 7F              LD      A,A                 
7333: 9D              SBC     L                   
7334: 00              NOP                         
7335: 53              LD      D,E                 
7336: 7F              LD      A,A                 
7337: 9D              SBC     L                   
7338: 20 53           JR      NZ,$738D            ; {}
733A: 7F              LD      A,A                 
733B: 9D              SBC     L                   
733C: 40              LD      B,B                 
733D: 53              LD      D,E                 
733E: 7F              LD      A,A                 
733F: 9D              SBC     L                   
7340: 60              LD      H,B                 
7341: 53              LD      D,E                 
7342: 7F              LD      A,A                 
7343: 9D              SBC     L                   
7344: 80              ADD     A,B                 
7345: 53              LD      D,E                 
7346: 7F              LD      A,A                 
7347: 9D              SBC     L                   
7348: A0              AND     B                   
7349: 53              LD      D,E                 
734A: 7F              LD      A,A                 
734B: 9D              SBC     L                   
734C: C0              RET     NZ                  
734D: 53              LD      D,E                 
734E: 7F              LD      A,A                 
734F: 9D              SBC     L                   
7350: E0 53           LD      ($FF00+$53),A       
7352: 7F              LD      A,A                 
7353: 9E              SBC     (HL)                
7354: 00              NOP                         
7355: 53              LD      D,E                 
7356: 7F              LD      A,A                 
7357: 9E              SBC     (HL)                
7358: 20 53           JR      NZ,$73AD            ; {}
735A: 7F              LD      A,A                 
735B: 9C              SBC     H                   
735C: 00              NOP                         
735D: 0E BD           LD      C,$BD               
735F: 7F              LD      A,A                 
7360: 7F              LD      A,A                 
7361: 7F              LD      A,A                 
7362: BE              CP      (HL)                
7363: BB              CP      E                   
7364: 7F              LD      A,A                 
7365: 7F              LD      A,A                 
7366: 7F              LD      A,A                 
7367: BE              CP      (HL)                
7368: CF              RST     0X08                
7369: 7F              LD      A,A                 
736A: 7F              LD      A,A                 
736B: 7F              LD      A,A                 
736C: 7F              LD      A,A                 
736D: 9C              SBC     H                   
736E: 20 0E           JR      NZ,$737E            ; {}
7370: BC              CP      H                   
7371: 7F              LD      A,A                 
7372: 7F              LD      A,A                 
7373: 7F              LD      A,A                 
7374: BF              CP      A                   
7375: BC              CP      H                   
7376: 7F              LD      A,A                 
7377: 7F              LD      A,A                 
7378: 7F              LD      A,A                 
7379: BF              CP      A                   
737A: 7F              LD      A,A                 
737B: 7F              LD      A,A                 
737C: 7F              LD      A,A                 
737D: 7F              LD      A,A                 
737E: 7F              LD      A,A                 
737F: 9C              SBC     H                   
7380: 40              LD      B,B                 
7381: 53              LD      D,E                 
7382: CC 9C 68        CALL    Z,$689C             ; {}
7385: D3                              
7386: 8D              ADC     A,L                 
7387: 9C              SBC     H                   
7388: E9              JP      (HL)                
7389: 49              LD      C,C                 
738A: 7F              LD      A,A                 
738B: 9D              SBC     L                   
738C: 09              ADD     HL,BC               
738D: 49              LD      C,C                 
738E: 7F              LD      A,A                 
738F: 9D              SBC     L                   
7390: 0A              LD      A,(BC)              
7391: C8              RET     Z                   
7392: 7F              LD      A,A                 
7393: 9A              SBC     D                   
7394: 14              INC     D                   
7395: 0B              DEC     BC                  
7396: 7C              LD      A,H                 
7397: 7C              LD      A,H                 
7398: 7C              LD      A,H                 
7399: 7C              LD      A,H                 
739A: 7C              LD      A,H                 
739B: 7C              LD      A,H                 
739C: 7C              LD      A,H                 
739D: 7C              LD      A,H                 
739E: 7C              LD      A,H                 
739F: 7C              LD      A,H                 
73A0: 7C              LD      A,H                 
73A1: 7C              LD      A,H                 
73A2: 9A              SBC     D                   
73A3: 34              INC     (HL)                
73A4: 0B              DEC     BC                  
73A5: 7C              LD      A,H                 
73A6: 7C              LD      A,H                 
73A7: 7C              LD      A,H                 
73A8: 7C              LD      A,H                 
73A9: 7C              LD      A,H                 
73AA: 7C              LD      A,H                 
73AB: 7C              LD      A,H                 
73AC: 7C              LD      A,H                 
73AD: 7C              LD      A,H                 
73AE: 7C              LD      A,H                 
73AF: 7C              LD      A,H                 
73B0: 7C              LD      A,H                 
73B1: 9A              SBC     D                   
73B2: 54              LD      D,H                 
73B3: 0B              DEC     BC                  
73B4: 7C              LD      A,H                 
73B5: 7C              LD      A,H                 
73B6: 7C              LD      A,H                 
73B7: 7C              LD      A,H                 
73B8: 7C              LD      A,H                 
73B9: 7C              LD      A,H                 
73BA: 7C              LD      A,H                 
73BB: 7C              LD      A,H                 
73BC: 7C              LD      A,H                 
73BD: 7C              LD      A,H                 
73BE: 7C              LD      A,H                 
73BF: 7C              LD      A,H                 
73C0: 9A              SBC     D                   
73C1: 74              LD      (HL),H              
73C2: 0B              DEC     BC                  
73C3: 7C              LD      A,H                 
73C4: 7C              LD      A,H                 
73C5: 7C              LD      A,H                 
73C6: 7C              LD      A,H                 
73C7: 7C              LD      A,H                 
73C8: 7C              LD      A,H                 
73C9: 7C              LD      A,H                 
73CA: 7C              LD      A,H                 
73CB: 7C              LD      A,H                 
73CC: 7C              LD      A,H                 
73CD: 7C              LD      A,H                 
73CE: 7C              LD      A,H                 
73CF: 9A              SBC     D                   
73D0: 94              SUB     H                   
73D1: 0B              DEC     BC                  
73D2: 7C              LD      A,H                 
73D3: 7C              LD      A,H                 
73D4: 7C              LD      A,H                 
73D5: 7C              LD      A,H                 
73D6: 7C              LD      A,H                 
73D7: 7C              LD      A,H                 
73D8: 7C              LD      A,H                 
73D9: 7C              LD      A,H                 
73DA: 7C              LD      A,H                 
73DB: 7C              LD      A,H                 
73DC: 7C              LD      A,H                 
73DD: 7C              LD      A,H                 
73DE: 9A              SBC     D                   
73DF: B4              OR      H                   
73E0: 0B              DEC     BC                  
73E1: 7C              LD      A,H                 
73E2: 7C              LD      A,H                 
73E3: 7C              LD      A,H                 
73E4: 7C              LD      A,H                 
73E5: 7C              LD      A,H                 
73E6: 7C              LD      A,H                 
73E7: 7C              LD      A,H                 
73E8: 7C              LD      A,H                 
73E9: 7C              LD      A,H                 
73EA: 7C              LD      A,H                 
73EB: 7C              LD      A,H                 
73EC: 7C              LD      A,H                 
73ED: 9A              SBC     D                   
73EE: D4 0B 2C        CALL    NC,$2C0B            
73F1: 2D              DEC     L                   
73F2: 7C              LD      A,H                 
73F3: 7C              LD      A,H                 
73F4: 7C              LD      A,H                 
73F5: 7C              LD      A,H                 
73F6: 7C              LD      A,H                 
73F7: 7C              LD      A,H                 
73F8: 7C              LD      A,H                 
73F9: 7C              LD      A,H                 
73FA: 2A              LD      A,(HLI)             
73FB: 2B              DEC     HL                  
73FC: 9A              SBC     D                   
73FD: F4                              
73FE: 0B              DEC     BC                  
73FF: 7F              LD      A,A                 
7400: 3D              DEC     A                   
7401: 7C              LD      A,H                 
7402: 7C              LD      A,H                 
7403: 7C              LD      A,H                 
7404: 7C              LD      A,H                 
7405: 7C              LD      A,H                 
7406: 7C              LD      A,H                 
7407: 7C              LD      A,H                 
7408: 7C              LD      A,H                 
7409: 3A              LD      A,(HLD)             
740A: 7F              LD      A,A                 
740B: 9B              SBC     E                   
740C: 14              INC     D                   
740D: 0B              DEC     BC                  
740E: 7F              LD      A,A                 
740F: 7F              LD      A,A                 
7410: 2C              INC     L                   
7411: 2D              DEC     L                   
7412: 7C              LD      A,H                 
7413: 7C              LD      A,H                 
7414: 7C              LD      A,H                 
7415: 7C              LD      A,H                 
7416: 2A              LD      A,(HLI)             
7417: 2B              DEC     HL                  
7418: 7F              LD      A,A                 
7419: 7F              LD      A,A                 
741A: 9B              SBC     E                   
741B: 34              INC     (HL)                
741C: 0B              DEC     BC                  
741D: 7F              LD      A,A                 
741E: 7F              LD      A,A                 
741F: 7F              LD      A,A                 
7420: 3D              DEC     A                   
7421: 3E 3F           LD      A,$3F               
7423: 3E 3F           LD      A,$3F               
7425: 3A              LD      A,(HLD)             
7426: 7F              LD      A,A                 
7427: 7F              LD      A,A                 
7428: 7F              LD      A,A                 
7429: 98              SBC     B                   
742A: 14              INC     D                   
742B: 0B              DEC     BC                  
742C: 7C              LD      A,H                 
742D: 7C              LD      A,H                 
742E: 7C              LD      A,H                 
742F: 7C              LD      A,H                 
7430: 7C              LD      A,H                 
7431: 7C              LD      A,H                 
7432: 7C              LD      A,H                 
7433: 7C              LD      A,H                 
7434: 7C              LD      A,H                 
7435: 7C              LD      A,H                 
7436: 7C              LD      A,H                 
7437: 7C              LD      A,H                 
7438: 98              SBC     B                   
7439: 34              INC     (HL)                
743A: 0B              DEC     BC                  
743B: 7C              LD      A,H                 
743C: 7C              LD      A,H                 
743D: 7C              LD      A,H                 
743E: 7C              LD      A,H                 
743F: 7C              LD      A,H                 
7440: 7C              LD      A,H                 
7441: 7C              LD      A,H                 
7442: 7C              LD      A,H                 
7443: 7C              LD      A,H                 
7444: 7C              LD      A,H                 
7445: 7C              LD      A,H                 
7446: 7C              LD      A,H                 
7447: 98              SBC     B                   
7448: 54              LD      D,H                 
7449: 0B              DEC     BC                  
744A: 7C              LD      A,H                 
744B: 7C              LD      A,H                 
744C: 7C              LD      A,H                 
744D: 7C              LD      A,H                 
744E: 7C              LD      A,H                 
744F: 7C              LD      A,H                 
7450: 7C              LD      A,H                 
7451: 7C              LD      A,H                 
7452: 7C              LD      A,H                 
7453: 7C              LD      A,H                 
7454: 7C              LD      A,H                 
7455: 7C              LD      A,H                 
7456: 98              SBC     B                   
7457: 74              LD      (HL),H              
7458: 0B              DEC     BC                  
7459: 7C              LD      A,H                 
745A: 7C              LD      A,H                 
745B: 7C              LD      A,H                 
745C: 7C              LD      A,H                 
745D: 7C              LD      A,H                 
745E: 7C              LD      A,H                 
745F: 7C              LD      A,H                 
7460: 7C              LD      A,H                 
7461: 7C              LD      A,H                 
7462: 7C              LD      A,H                 
7463: 7C              LD      A,H                 
7464: 7C              LD      A,H                 
7465: 98              SBC     B                   
7466: 94              SUB     H                   
7467: 0B              DEC     BC                  
7468: 7C              LD      A,H                 
7469: 7C              LD      A,H                 
746A: 7C              LD      A,H                 
746B: 7C              LD      A,H                 
746C: 7C              LD      A,H                 
746D: 7C              LD      A,H                 
746E: 7C              LD      A,H                 
746F: 7C              LD      A,H                 
7470: 7C              LD      A,H                 
7471: 7C              LD      A,H                 
7472: 7C              LD      A,H                 
7473: 7C              LD      A,H                 
7474: 98              SBC     B                   
7475: B4              OR      H                   
7476: 0B              DEC     BC                  
7477: 7C              LD      A,H                 
7478: 7C              LD      A,H                 
7479: 7C              LD      A,H                 
747A: 7C              LD      A,H                 
747B: 7C              LD      A,H                 
747C: 7C              LD      A,H                 
747D: 7C              LD      A,H                 
747E: 7C              LD      A,H                 
747F: 7C              LD      A,H                 
7480: 7C              LD      A,H                 
7481: 7C              LD      A,H                 
7482: 7C              LD      A,H                 
7483: 98              SBC     B                   
7484: D4 0B 2C        CALL    NC,$2C0B            
7487: 2D              DEC     L                   
7488: 7C              LD      A,H                 
7489: 7C              LD      A,H                 
748A: 7C              LD      A,H                 
748B: 7C              LD      A,H                 
748C: 7C              LD      A,H                 
748D: 7C              LD      A,H                 
748E: 7C              LD      A,H                 
748F: 7C              LD      A,H                 
7490: 2A              LD      A,(HLI)             
7491: 2B              DEC     HL                  
7492: 98              SBC     B                   
7493: F4                              
7494: 0B              DEC     BC                  
7495: 7F              LD      A,A                 
7496: 3D              DEC     A                   
7497: 7C              LD      A,H                 
7498: 7C              LD      A,H                 
7499: 7C              LD      A,H                 
749A: 7C              LD      A,H                 
749B: 7C              LD      A,H                 
749C: 7C              LD      A,H                 
749D: 7C              LD      A,H                 
749E: 7C              LD      A,H                 
749F: 3A              LD      A,(HLD)             
74A0: 7F              LD      A,A                 
74A1: 99              SBC     C                   
74A2: 14              INC     D                   
74A3: 0B              DEC     BC                  
74A4: 7F              LD      A,A                 
74A5: 7F              LD      A,A                 
74A6: 2C              INC     L                   
74A7: 2D              DEC     L                   
74A8: 7C              LD      A,H                 
74A9: 7C              LD      A,H                 
74AA: 7C              LD      A,H                 
74AB: 7C              LD      A,H                 
74AC: 2A              LD      A,(HLI)             
74AD: 2B              DEC     HL                  
74AE: 7F              LD      A,A                 
74AF: 7F              LD      A,A                 
74B0: 99              SBC     C                   
74B1: 34              INC     (HL)                
74B2: 0B              DEC     BC                  
74B3: 7F              LD      A,A                 
74B4: 7F              LD      A,A                 
74B5: 7F              LD      A,A                 
74B6: 3D              DEC     A                   
74B7: 3E 3F           LD      A,$3F               
74B9: 3E 3F           LD      A,$3F               
74BB: 3A              LD      A,(HLD)             
74BC: 7F              LD      A,A                 
74BD: 7F              LD      A,A                 
74BE: 7F              LD      A,A                 
74BF: 00              NOP                         
74C0: 9C              SBC     H                   
74C1: 00              NOP                         
74C2: 5F              LD      E,A                 
74C3: 7E              LD      A,(HL)              
74C4: 9C              SBC     H                   
74C5: 20 5F           JR      NZ,$7526            ; {}
74C7: 7E              LD      A,(HL)              
74C8: 9C              SBC     H                   
74C9: 40              LD      B,B                 
74CA: 5F              LD      E,A                 
74CB: 7E              LD      A,(HL)              
74CC: 9C              SBC     H                   
74CD: 60              LD      H,B                 
74CE: 5F              LD      E,A                 
74CF: 7E              LD      A,(HL)              
74D0: 9C              SBC     H                   
74D1: 80              ADD     A,B                 
74D2: 5F              LD      E,A                 
74D3: 7E              LD      A,(HL)              
74D4: 9C              SBC     H                   
74D5: A0              AND     B                   
74D6: 5F              LD      E,A                 
74D7: 7E              LD      A,(HL)              
74D8: 9C              SBC     H                   
74D9: C0              RET     NZ                  
74DA: 5F              LD      E,A                 
74DB: 7E              LD      A,(HL)              
74DC: 9C              SBC     H                   
74DD: E0 5F           LD      ($FF00+$5F),A       
74DF: 7E              LD      A,(HL)              
74E0: 9D              SBC     L                   
74E1: 00              NOP                         
74E2: 5F              LD      E,A                 
74E3: 7E              LD      A,(HL)              
74E4: 9D              SBC     L                   
74E5: 20 5F           JR      NZ,$7546            ; {}
74E7: 7E              LD      A,(HL)              
74E8: 9D              SBC     L                   
74E9: 40              LD      B,B                 
74EA: 5F              LD      E,A                 
74EB: 7E              LD      A,(HL)              
74EC: 9D              SBC     L                   
74ED: 60              LD      H,B                 
74EE: 5F              LD      E,A                 
74EF: 7E              LD      A,(HL)              
74F0: 9D              SBC     L                   
74F1: 80              ADD     A,B                 
74F2: 5F              LD      E,A                 
74F3: 7E              LD      A,(HL)              
74F4: 9D              SBC     L                   
74F5: A0              AND     B                   
74F6: 5F              LD      E,A                 
74F7: 7E              LD      A,(HL)              
74F8: 9D              SBC     L                   
74F9: C0              RET     NZ                  
74FA: 5F              LD      E,A                 
74FB: 7E              LD      A,(HL)              
74FC: 9D              SBC     L                   
74FD: E0 5F           LD      ($FF00+$5F),A       
74FF: 7E              LD      A,(HL)              
7500: 9E              SBC     (HL)                
7501: 00              NOP                         
7502: 5F              LD      E,A                 
7503: 7E              LD      A,(HL)              
7504: 9E              SBC     (HL)                
7505: 20 5F           JR      NZ,$7566            ; {}
7507: 7E              LD      A,(HL)              
7508: 9E              SBC     (HL)                
7509: 40              LD      B,B                 
750A: 5F              LD      E,A                 
750B: 7E              LD      A,(HL)              
750C: 9E              SBC     (HL)                
750D: 60              LD      H,B                 
750E: 5F              LD      E,A                 
750F: 7E              LD      A,(HL)              
7510: 9E              SBC     (HL)                
7511: 80              ADD     A,B                 
7512: 5F              LD      E,A                 
7513: 7E              LD      A,(HL)              
7514: 9E              SBC     (HL)                
7515: A0              AND     B                   
7516: 5F              LD      E,A                 
7517: 7E              LD      A,(HL)              
7518: 9E              SBC     (HL)                
7519: C0              RET     NZ                  
751A: 5F              LD      E,A                 
751B: 7E              LD      A,(HL)              
751C: 9E              SBC     (HL)                
751D: E0 5F           LD      ($FF00+$5F),A       
751F: 7E              LD      A,(HL)              
7520: 9F              SBC     A                   
7521: 00              NOP                         
7522: 5F              LD      E,A                 
7523: 7E              LD      A,(HL)              
7524: 9F              SBC     A                   
7525: 20 5F           JR      NZ,$7586            ; {}
7527: 7E              LD      A,(HL)              
7528: 9F              SBC     A                   
7529: 40              LD      B,B                 
752A: 5F              LD      E,A                 
752B: 7E              LD      A,(HL)              
752C: 9F              SBC     A                   
752D: 60              LD      H,B                 
752E: 5F              LD      E,A                 
752F: 7E              LD      A,(HL)              
7530: 9F              SBC     A                   
7531: 80              ADD     A,B                 
7532: 5F              LD      E,A                 
7533: 7E              LD      A,(HL)              
7534: 9F              SBC     A                   
7535: A0              AND     B                   
7536: 5F              LD      E,A                 
7537: 7E              LD      A,(HL)              
7538: 9F              SBC     A                   
7539: C0              RET     NZ                  
753A: 5F              LD      E,A                 
753B: 7E              LD      A,(HL)              
753C: 9F              SBC     A                   
753D: E0 5F           LD      ($FF00+$5F),A       
753F: 7E              LD      A,(HL)              
7540: 9C              SBC     H                   
7541: A9              XOR     C                   
7542: 41              LD      B,C                 
7543: 7F              LD      A,A                 
7544: 9C              SBC     H                   
7545: C8              RET     Z                   
7546: 43              LD      B,E                 
7547: 7F              LD      A,A                 
7548: 9C              SBC     H                   
7549: E7              RST     0X20                
754A: 45              LD      B,L                 
754B: 7F              LD      A,A                 
754C: 9D              SBC     L                   
754D: 07              RLCA                        
754E: 45              LD      B,L                 
754F: 7F              LD      A,A                 
7550: 9D              SBC     L                   
7551: 28 43           JR      Z,$7596             ; {}
7553: 7F              LD      A,A                 
7554: 9D              SBC     L                   
7555: 49              LD      C,C                 
7556: 41              LD      B,C                 
7557: 7F              LD      A,A                 
7558: 00              NOP                         
7559: 98              SBC     B                   
755A: 65              LD      H,L                 
755B: 4B              LD      C,E                 
755C: 7F              LD      A,A                 
755D: 98              SBC     B                   
755E: 83              ADD     A,E                 
755F: 4D              LD      C,L                 
7560: 7F              LD      A,A                 
7561: 98              SBC     B                   
7562: A3              AND     E                   
7563: 4D              LD      C,L                 
7564: 7F              LD      A,A                 
7565: 98              SBC     B                   
7566: C3 4D 7F        JP      $7F4D               ; {}
7569: 98              SBC     B                   
756A: E3                              
756B: 4D              LD      C,L                 
756C: 7F              LD      A,A                 
756D: 99              SBC     C                   
756E: 03              INC     BC                  
756F: 4D              LD      C,L                 
7570: 7F              LD      A,A                 
7571: 99              SBC     C                   
7572: 23              INC     HL                  
7573: 4D              LD      C,L                 
7574: 7F              LD      A,A                 
7575: 99              SBC     C                   
7576: 43              LD      B,E                 
7577: 4D              LD      C,L                 
7578: 7F              LD      A,A                 
7579: 99              SBC     C                   
757A: 63              LD      H,E                 
757B: 4D              LD      C,L                 
757C: 7F              LD      A,A                 
757D: 99              SBC     C                   
757E: 83              ADD     A,E                 
757F: 4D              LD      C,L                 
7580: 7F              LD      A,A                 
7581: 99              SBC     C                   
7582: A3              AND     E                   
7583: 4D              LD      C,L                 
7584: 7F              LD      A,A                 
7585: 99              SBC     C                   
7586: C3 4D 7F        JP      $7F4D               ; {}
7589: 98              SBC     B                   
758A: 42              LD      B,D                 
758B: 0F              RRCA                        
758C: 90              SUB     B                   
758D: 91              SUB     C                   
758E: 92              SUB     D                   
758F: 93              SUB     E                   
7590: 94              SUB     H                   
7591: 98              SBC     B                   
7592: 99              SBC     C                   
7593: 98              SBC     B                   
7594: 99              SBC     C                   
7595: 98              SBC     B                   
7596: 99              SBC     C                   
7597: 98              SBC     B                   
7598: 99              SBC     C                   
7599: 98              SBC     B                   
759A: 99              SBC     C                   
759B: A4              AND     H                   
759C: 98              SBC     B                   
759D: 62              LD      H,D                 
759E: 02              LD      (BC),A              
759F: 95              SUB     L                   
75A0: 96              SUB     (HL)                
75A1: 97              SUB     A                   
75A2: 98              SBC     B                   
75A3: 82              ADD     A,D                 
75A4: 8B              ADC     A,E                 
75A5: 9E              SBC     (HL)                
75A6: 9C              SBC     H                   
75A7: 9E              SBC     (HL)                
75A8: 9C              SBC     H                   
75A9: 9E              SBC     (HL)                
75AA: 9C              SBC     H                   
75AB: 9E              SBC     (HL)                
75AC: 9C              SBC     H                   
75AD: 9E              SBC     (HL)                
75AE: 9C              SBC     H                   
75AF: 9E              SBC     (HL)                
75B0: A5              AND     L                   
75B1: 99              SBC     C                   
75B2: E3                              
75B3: 0E 9A           LD      C,$9A               
75B5: 9B              SBC     E                   
75B6: 9A              SBC     D                   
75B7: 9B              SBC     E                   
75B8: 9A              SBC     D                   
75B9: 9B              SBC     E                   
75BA: 9A              SBC     D                   
75BB: 9B              SBC     E                   
75BC: 9A              SBC     D                   
75BD: 9B              SBC     E                   
75BE: 9A              SBC     D                   
75BF: 9B              SBC     E                   
75C0: 9A              SBC     D                   
75C1: 9B              SBC     E                   
75C2: A6              AND     (HL)                
75C3: 98              SBC     B                   
75C4: 71              LD      (HL),C              
75C5: 8B              ADC     A,E                 
75C6: 9D              SBC     L                   
75C7: 9F              SBC     A                   
75C8: 9D              SBC     L                   
75C9: 9F              SBC     A                   
75CA: 9D              SBC     L                   
75CB: 9F              SBC     A                   
75CC: 9D              SBC     L                   
75CD: 9F              SBC     A                   
75CE: 9D              SBC     L                   
75CF: 9F              SBC     A                   
75D0: 9D              SBC     L                   
75D1: 9F              SBC     A                   
75D2: 9A              SBC     D                   
75D3: 03              INC     BC                  
75D4: 0E A7           LD      C,$A7               
75D6: A8              XOR     B                   
75D7: A7              AND     A                   
75D8: A8              XOR     B                   
75D9: A7              AND     A                   
75DA: A8              XOR     B                   
75DB: A7              AND     A                   
75DC: A8              XOR     B                   
75DD: A7              AND     A                   
75DE: A8              XOR     B                   
75DF: A7              AND     A                   
75E0: A8              XOR     B                   
75E1: A7              AND     A                   
75E2: A8              XOR     B                   
75E3: A7              AND     A                   
75E4: 98              SBC     B                   
75E5: 86              ADD     A,(HL)              
75E6: 47              LD      B,A                 
75E7: A2              AND     D                   
75E8: 98              SBC     B                   
75E9: A5              AND     L                   
75EA: 09              ADD     HL,BC               
75EB: A0              AND     B                   
75EC: 80              ADD     A,B                 
75ED: 81              ADD     A,C                 
75EE: 82              ADD     A,D                 
75EF: 83              ADD     A,E                 
75F0: 84              ADD     A,H                 
75F1: 85              ADD     A,L                 
75F2: 86              ADD     A,(HL)              
75F3: 87              ADD     A,A                 
75F4: A1              AND     C                   
75F5: 98              SBC     B                   
75F6: C5              PUSH    BC                  
75F7: 09              ADD     HL,BC               
75F8: A0              AND     B                   
75F9: 88              ADC     A,B                 
75FA: 89              ADC     A,C                 
75FB: 8A              ADC     A,D                 
75FC: 8B              ADC     A,E                 
75FD: 8C              ADC     A,H                 
75FE: 8D              ADC     A,L                 
75FF: 8E              ADC     A,(HL)              
7600: 8F              ADC     A,A                 
7601: A1              AND     C                   
7602: 98              SBC     B                   
7603: E6 47           AND     $47                 
7605: A3              AND     E                   
7606: 99              SBC     C                   
7607: 05              DEC     B                   
7608: 0A              LD      A,(BC)              
7609: A9              XOR     C                   
760A: AA              XOR     D                   
760B: AB              XOR     E                   
760C: AC              XOR     H                   
760D: AD              XOR     L                   
760E: B0              OR      B                   
760F: B1              OR      C                   
7610: B2              OR      D                   
7611: B3              OR      E                   
7612: B4              OR      H                   
7613: B5              OR      L                   
7614: 99              SBC     C                   
7615: 45              LD      B,L                 
7616: 07              RLCA                        
7617: A9              XOR     C                   
7618: AA              XOR     D                   
7619: AB              XOR     E                   
761A: AC              XOR     H                   
761B: AD              XOR     L                   
761C: B6              OR      (HL)                
761D: B7              OR      A                   
761E: B8              CP      B                   
761F: 99              SBC     C                   
7620: 85              ADD     A,L                 
7621: 05              DEC     B                   
7622: B0              OR      B                   
7623: B1              OR      C                   
7624: B2              OR      D                   
7625: B3              OR      E                   
7626: B4              OR      H                   
7627: B5              OR      L                   
7628: 99              SBC     C                   
7629: A5              AND     L                   
762A: 0A              LD      A,(BC)              
762B: C5              PUSH    BC                  
762C: C6 C7           ADD     $C7                 
762E: C8              RET     Z                   
762F: C9              RET                         
7630: CA A9 AA        JP      Z,$AAA9             
7633: CB CC           SET     1,E                 
7635: CD 00 98        CALL    $9800               
7638: A5              AND     L                   
7639: 4B              LD      C,E                 
763A: 7F              LD      A,A                 
763B: 98              SBC     B                   
763C: C3 4D 7F        JP      $7F4D               ; {}
763F: 98              SBC     B                   
7640: E3                              
7641: 4D              LD      C,L                 
7642: 7F              LD      A,A                 
7643: 99              SBC     C                   
7644: 03              INC     BC                  
7645: 4D              LD      C,L                 
7646: 7F              LD      A,A                 
7647: 99              SBC     C                   
7648: 23              INC     HL                  
7649: 4D              LD      C,L                 
764A: 7F              LD      A,A                 
764B: 99              SBC     C                   
764C: 43              LD      B,E                 
764D: 4D              LD      C,L                 
764E: 7F              LD      A,A                 
764F: 98              SBC     B                   
7650: 82              ADD     A,D                 
7651: 0F              RRCA                        
7652: 90              SUB     B                   
7653: 91              SUB     C                   
7654: 92              SUB     D                   
7655: 93              SUB     E                   
7656: 94              SUB     H                   
7657: 98              SBC     B                   
7658: 99              SBC     C                   
7659: 98              SBC     B                   
765A: 99              SBC     C                   
765B: 98              SBC     B                   
765C: 99              SBC     C                   
765D: 98              SBC     B                   
765E: 99              SBC     C                   
765F: 98              SBC     B                   
7660: 99              SBC     C                   
7661: A4              AND     H                   
7662: 98              SBC     B                   
7663: A2              AND     D                   
7664: 02              LD      (BC),A              
7665: 95              SUB     L                   
7666: 96              SUB     (HL)                
7667: 97              SUB     A                   
7668: 98              SBC     B                   
7669: C2 84 9E        JP      NZ,$9E84            
766C: 9C              SBC     H                   
766D: 9E              SBC     (HL)                
766E: 9C              SBC     H                   
766F: 9E              SBC     (HL)                
7670: 98              SBC     B                   
7671: B1              OR      C                   
7672: 85              ADD     A,L                 
7673: 9D              SBC     L                   
7674: 9F              SBC     A                   
7675: 9D              SBC     L                   
7676: 9F              SBC     A                   
7677: 9D              SBC     L                   
7678: 9F              SBC     A                   
7679: 99              SBC     C                   
767A: 62              LD      H,D                 
767B: 0F              RRCA                        
767C: A5              AND     L                   
767D: 9A              SBC     D                   
767E: 9B              SBC     E                   
767F: 9A              SBC     D                   
7680: 9B              SBC     E                   
7681: 9A              SBC     D                   
7682: 9B              SBC     E                   
7683: 9A              SBC     D                   
7684: 9B              SBC     E                   
7685: 9A              SBC     D                   
7686: 9B              SBC     E                   
7687: 9A              SBC     D                   
7688: 9B              SBC     E                   
7689: 9A              SBC     D                   
768A: 9B              SBC     E                   
768B: A6              AND     (HL)                
768C: 99              SBC     C                   
768D: 83              ADD     A,E                 
768E: 0E A7           LD      C,$A7               
7690: A8              XOR     B                   
7691: A7              AND     A                   
7692: A8              XOR     B                   
7693: A7              AND     A                   
7694: A8              XOR     B                   
7695: A7              AND     A                   
7696: A8              XOR     B                   
7697: A7              AND     A                   
7698: A8              XOR     B                   
7699: A7              AND     A                   
769A: A8              XOR     B                   
769B: A7              AND     A                   
769C: A8              XOR     B                   
769D: A7              AND     A                   
769E: 98              SBC     B                   
769F: E5              PUSH    HL                  
76A0: 09              ADD     HL,BC               
76A1: B9              CP      C                   
76A2: BA              CP      D                   
76A3: BB              CP      E                   
76A4: BC              CP      H                   
76A5: BD              CP      L                   
76A6: C0              RET     NZ                  
76A7: C1              POP     BC                  
76A8: C2 C3 C4        JP      NZ,$C4C3            
76AB: 99              SBC     C                   
76AC: 25              DEC     H                   
76AD: 07              RLCA                        
76AE: A9              XOR     C                   
76AF: AA              XOR     D                   
76B0: AB              XOR     E                   
76B1: AC              XOR     H                   
76B2: AD              XOR     L                   
76B3: B6              OR      (HL)                
76B4: B7              OR      A                   
76B5: B8              CP      B                   
76B6: 00              NOP                         
76B7: 98              SBC     B                   
76B8: 00              NOP                         
76B9: 5F              LD      E,A                 
76BA: 7F              LD      A,A                 
76BB: 98              SBC     B                   
76BC: 20 5F           JR      NZ,$771D            ; {}
76BE: 7F              LD      A,A                 
76BF: 98              SBC     B                   
76C0: 40              LD      B,B                 
76C1: 5F              LD      E,A                 
76C2: 7F              LD      A,A                 
76C3: 98              SBC     B                   
76C4: 60              LD      H,B                 
76C5: 5F              LD      E,A                 
76C6: 7F              LD      A,A                 
76C7: 98              SBC     B                   
76C8: 80              ADD     A,B                 
76C9: 1F              RRA                         
76CA: 80              ADD     A,B                 
76CB: 81              ADD     A,C                 
76CC: 82              ADD     A,D                 
76CD: 83              ADD     A,E                 
76CE: 80              ADD     A,B                 
76CF: 81              ADD     A,C                 
76D0: 82              ADD     A,D                 
76D1: 83              ADD     A,E                 
76D2: 80              ADD     A,B                 
76D3: 81              ADD     A,C                 
76D4: 82              ADD     A,D                 
76D5: 83              ADD     A,E                 
76D6: 80              ADD     A,B                 
76D7: 81              ADD     A,C                 
76D8: 82              ADD     A,D                 
76D9: 83              ADD     A,E                 
76DA: 80              ADD     A,B                 
76DB: 81              ADD     A,C                 
76DC: 82              ADD     A,D                 
76DD: 83              ADD     A,E                 
76DE: 80              ADD     A,B                 
76DF: 81              ADD     A,C                 
76E0: 82              ADD     A,D                 
76E1: 83              ADD     A,E                 
76E2: 80              ADD     A,B                 
76E3: 81              ADD     A,C                 
76E4: 82              ADD     A,D                 
76E5: 83              ADD     A,E                 
76E6: 80              ADD     A,B                 
76E7: 81              ADD     A,C                 
76E8: 82              ADD     A,D                 
76E9: 83              ADD     A,E                 
76EA: 98              SBC     B                   
76EB: A0              AND     B                   
76EC: 1F              RRA                         
76ED: 84              ADD     A,H                 
76EE: 85              ADD     A,L                 
76EF: 86              ADD     A,(HL)              
76F0: 87              ADD     A,A                 
76F1: 84              ADD     A,H                 
76F2: 85              ADD     A,L                 
76F3: 86              ADD     A,(HL)              
76F4: 87              ADD     A,A                 
76F5: 84              ADD     A,H                 
76F6: 85              ADD     A,L                 
76F7: 86              ADD     A,(HL)              
76F8: 87              ADD     A,A                 
76F9: 84              ADD     A,H                 
76FA: 85              ADD     A,L                 
76FB: 86              ADD     A,(HL)              
76FC: 87              ADD     A,A                 
76FD: 84              ADD     A,H                 
76FE: 85              ADD     A,L                 
76FF: 86              ADD     A,(HL)              
7700: 87              ADD     A,A                 
7701: 84              ADD     A,H                 
7702: 85              ADD     A,L                 
7703: 86              ADD     A,(HL)              
7704: 87              ADD     A,A                 
7705: 84              ADD     A,H                 
7706: 85              ADD     A,L                 
7707: 86              ADD     A,(HL)              
7708: 87              ADD     A,A                 
7709: 84              ADD     A,H                 
770A: 85              ADD     A,L                 
770B: 86              ADD     A,(HL)              
770C: 87              ADD     A,A                 
770D: 98              SBC     B                   
770E: C0              RET     NZ                  
770F: 1F              RRA                         
7710: 88              ADC     A,B                 
7711: 89              ADC     A,C                 
7712: 8A              ADC     A,D                 
7713: 8B              ADC     A,E                 
7714: 88              ADC     A,B                 
7715: 89              ADC     A,C                 
7716: 8A              ADC     A,D                 
7717: 8B              ADC     A,E                 
7718: 88              ADC     A,B                 
7719: 89              ADC     A,C                 
771A: 8A              ADC     A,D                 
771B: 8B              ADC     A,E                 
771C: 88              ADC     A,B                 
771D: 89              ADC     A,C                 
771E: 8A              ADC     A,D                 
771F: 8B              ADC     A,E                 
7720: 88              ADC     A,B                 
7721: 89              ADC     A,C                 
7722: 8A              ADC     A,D                 
7723: 8B              ADC     A,E                 
7724: 88              ADC     A,B                 
7725: 89              ADC     A,C                 
7726: 8A              ADC     A,D                 
7727: 8B              ADC     A,E                 
7728: 88              ADC     A,B                 
7729: 89              ADC     A,C                 
772A: 8A              ADC     A,D                 
772B: 8B              ADC     A,E                 
772C: 88              ADC     A,B                 
772D: 89              ADC     A,C                 
772E: 8A              ADC     A,D                 
772F: 8B              ADC     A,E                 
7730: 98              SBC     B                   
7731: E0 5F           LD      ($FF00+$5F),A       
7733: 7C              LD      A,H                 
7734: 99              SBC     C                   
7735: 00              NOP                         
7736: 5F              LD      E,A                 
7737: 7C              LD      A,H                 
7738: 99              SBC     C                   
7739: 20 5F           JR      NZ,$779A            ; {}
773B: 7C              LD      A,H                 
773C: 99              SBC     C                   
773D: 40              LD      B,B                 
773E: 1F              RRA                         
773F: 90              SUB     B                   
7740: 91              SUB     C                   
7741: 92              SUB     D                   
7742: 93              SUB     E                   
7743: 90              SUB     B                   
7744: 91              SUB     C                   
7745: 92              SUB     D                   
7746: 93              SUB     E                   
7747: 90              SUB     B                   
7748: 91              SUB     C                   
7749: 92              SUB     D                   
774A: 93              SUB     E                   
774B: 90              SUB     B                   
774C: 91              SUB     C                   
774D: 92              SUB     D                   
774E: 93              SUB     E                   
774F: 90              SUB     B                   
7750: 91              SUB     C                   
7751: 92              SUB     D                   
7752: 93              SUB     E                   
7753: 90              SUB     B                   
7754: 91              SUB     C                   
7755: 92              SUB     D                   
7756: 93              SUB     E                   
7757: 90              SUB     B                   
7758: 91              SUB     C                   
7759: 92              SUB     D                   
775A: 93              SUB     E                   
775B: 90              SUB     B                   
775C: 91              SUB     C                   
775D: 92              SUB     D                   
775E: 93              SUB     E                   
775F: 99              SBC     C                   
7760: 60              LD      H,B                 
7761: 1F              RRA                         
7762: 94              SUB     H                   
7763: 95              SUB     L                   
7764: 96              SUB     (HL)                
7765: 97              SUB     A                   
7766: 94              SUB     H                   
7767: 95              SUB     L                   
7768: 96              SUB     (HL)                
7769: 97              SUB     A                   
776A: 94              SUB     H                   
776B: 95              SUB     L                   
776C: 96              SUB     (HL)                
776D: 97              SUB     A                   
776E: 94              SUB     H                   
776F: 95              SUB     L                   
7770: 96              SUB     (HL)                
7771: 97              SUB     A                   
7772: 94              SUB     H                   
7773: 95              SUB     L                   
7774: 96              SUB     (HL)                
7775: 97              SUB     A                   
7776: 94              SUB     H                   
7777: 95              SUB     L                   
7778: 96              SUB     (HL)                
7779: 97              SUB     A                   
777A: 94              SUB     H                   
777B: 95              SUB     L                   
777C: 96              SUB     (HL)                
777D: 97              SUB     A                   
777E: 94              SUB     H                   
777F: 95              SUB     L                   
7780: 96              SUB     (HL)                
7781: 97              SUB     A                   
7782: 99              SBC     C                   
7783: 80              ADD     A,B                 
7784: 1F              RRA                         
7785: 8C              ADC     A,H                 
7786: 8D              ADC     A,L                 
7787: 8E              ADC     A,(HL)              
7788: 8F              ADC     A,A                 
7789: 8C              ADC     A,H                 
778A: 8D              ADC     A,L                 
778B: 8E              ADC     A,(HL)              
778C: 8F              ADC     A,A                 
778D: 8C              ADC     A,H                 
778E: 8D              ADC     A,L                 
778F: 8E              ADC     A,(HL)              
7790: 8F              ADC     A,A                 
7791: 8C              ADC     A,H                 
7792: 8D              ADC     A,L                 
7793: 8E              ADC     A,(HL)              
7794: 8F              ADC     A,A                 
7795: 8C              ADC     A,H                 
7796: 8D              ADC     A,L                 
7797: 8E              ADC     A,(HL)              
7798: 8F              ADC     A,A                 
7799: 8C              ADC     A,H                 
779A: 8D              ADC     A,L                 
779B: 8E              ADC     A,(HL)              
779C: 8F              ADC     A,A                 
779D: 8C              ADC     A,H                 
779E: 8D              ADC     A,L                 
779F: 8E              ADC     A,(HL)              
77A0: 8F              ADC     A,A                 
77A1: 8C              ADC     A,H                 
77A2: 8D              ADC     A,L                 
77A3: 8E              ADC     A,(HL)              
77A4: 8F              ADC     A,A                 
77A5: 99              SBC     C                   
77A6: A0              AND     B                   
77A7: 1F              RRA                         
77A8: 98              SBC     B                   
77A9: 99              SBC     C                   
77AA: 9A              SBC     D                   
77AB: 9B              SBC     E                   
77AC: 98              SBC     B                   
77AD: 99              SBC     C                   
77AE: 9A              SBC     D                   
77AF: 9B              SBC     E                   
77B0: 98              SBC     B                   
77B1: 99              SBC     C                   
77B2: 9A              SBC     D                   
77B3: 9B              SBC     E                   
77B4: 98              SBC     B                   
77B5: 99              SBC     C                   
77B6: 9A              SBC     D                   
77B7: 9B              SBC     E                   
77B8: 98              SBC     B                   
77B9: 99              SBC     C                   
77BA: 9A              SBC     D                   
77BB: 9B              SBC     E                   
77BC: 98              SBC     B                   
77BD: 99              SBC     C                   
77BE: 9A              SBC     D                   
77BF: 9B              SBC     E                   
77C0: 98              SBC     B                   
77C1: 99              SBC     C                   
77C2: 9A              SBC     D                   
77C3: 9B              SBC     E                   
77C4: 98              SBC     B                   
77C5: 99              SBC     C                   
77C6: 9A              SBC     D                   
77C7: 9B              SBC     E                   
77C8: 99              SBC     C                   
77C9: C0              RET     NZ                  
77CA: 1F              RRA                         
77CB: 7F              LD      A,A                 
77CC: 7F              LD      A,A                 
77CD: 9C              SBC     H                   
77CE: 9D              SBC     L                   
77CF: 7F              LD      A,A                 
77D0: 7F              LD      A,A                 
77D1: 9C              SBC     H                   
77D2: 9D              SBC     L                   
77D3: 7F              LD      A,A                 
77D4: 7F              LD      A,A                 
77D5: 9C              SBC     H                   
77D6: 9D              SBC     L                   
77D7: 7F              LD      A,A                 
77D8: 7F              LD      A,A                 
77D9: 9C              SBC     H                   
77DA: 9D              SBC     L                   
77DB: 7F              LD      A,A                 
77DC: 7F              LD      A,A                 
77DD: 9C              SBC     H                   
77DE: 9D              SBC     L                   
77DF: 7F              LD      A,A                 
77E0: 7F              LD      A,A                 
77E1: 9C              SBC     H                   
77E2: 9D              SBC     L                   
77E3: 7F              LD      A,A                 
77E4: 7F              LD      A,A                 
77E5: 9C              SBC     H                   
77E6: 9D              SBC     L                   
77E7: 7F              LD      A,A                 
77E8: 7F              LD      A,A                 
77E9: 9C              SBC     H                   
77EA: 9D              SBC     L                   
77EB: 99              SBC     C                   
77EC: E0 5F           LD      ($FF00+$5F),A       
77EE: 7F              LD      A,A                 
77EF: 9A              SBC     D                   
77F0: 00              NOP                         
77F1: 5F              LD      E,A                 
77F2: 7F              LD      A,A                 
77F3: 9A              SBC     D                   
77F4: 20 5F           JR      NZ,$7855            ; {}
77F6: 7F              LD      A,A                 
77F7: 9A              SBC     D                   
77F8: 40              LD      B,B                 
77F9: 5F              LD      E,A                 
77FA: 7F              LD      A,A                 
77FB: 9A              SBC     D                   
77FC: 60              LD      H,B                 
77FD: 5F              LD      E,A                 
77FE: 7F              LD      A,A                 
77FF: 00              NOP                         
7800: 98              SBC     B                   
7801: 00              NOP                         
7802: 5F              LD      E,A                 
7803: 7F              LD      A,A                 
7804: 98              SBC     B                   
7805: 20 5F           JR      NZ,$7866            ; {}
7807: 7F              LD      A,A                 
7808: 98              SBC     B                   
7809: 40              LD      B,B                 
780A: 1F              RRA                         
780B: 7F              LD      A,A                 
780C: 7F              LD      A,A                 
780D: 7F              LD      A,A                 
780E: 7F              LD      A,A                 
780F: 7F              LD      A,A                 
7810: 7F              LD      A,A                 
7811: 7F              LD      A,A                 
7812: 7F              LD      A,A                 
7813: A0              AND     B                   
7814: A1              AND     C                   
7815: A2              AND     D                   
7816: A3              AND     E                   
7817: A4              AND     H                   
7818: 7F              LD      A,A                 
7819: 7F              LD      A,A                 
781A: 7F              LD      A,A                 
781B: 7F              LD      A,A                 
781C: 7F              LD      A,A                 
781D: 7F              LD      A,A                 
781E: 7F              LD      A,A                 
781F: 7F              LD      A,A                 
7820: 7F              LD      A,A                 
7821: 7F              LD      A,A                 
7822: 7F              LD      A,A                 
7823: 7F              LD      A,A                 
7824: 7F              LD      A,A                 
7825: 7F              LD      A,A                 
7826: 7F              LD      A,A                 
7827: 7F              LD      A,A                 
7828: 7F              LD      A,A                 
7829: 7F              LD      A,A                 
782A: 7F              LD      A,A                 
782B: 98              SBC     B                   
782C: 60              LD      H,B                 
782D: 1F              RRA                         
782E: 7F              LD      A,A                 
782F: 7F              LD      A,A                 
7830: 7F              LD      A,A                 
7831: 7F              LD      A,A                 
7832: 7F              LD      A,A                 
7833: 7F              LD      A,A                 
7834: 7F              LD      A,A                 
7835: 27              DAA                         
7836: 28 29           JR      Z,$7861             ; {}
7838: 2A              LD      A,(HLI)             
7839: B3              OR      E                   
783A: B4              OR      H                   
783B: 7F              LD      A,A                 
783C: 7F              LD      A,A                 
783D: 7F              LD      A,A                 
783E: 7F              LD      A,A                 
783F: 7F              LD      A,A                 
7840: 7F              LD      A,A                 
7841: 7F              LD      A,A                 
7842: 7F              LD      A,A                 
7843: 7F              LD      A,A                 
7844: 7F              LD      A,A                 
7845: 7F              LD      A,A                 
7846: 7F              LD      A,A                 
7847: 7F              LD      A,A                 
7848: 7F              LD      A,A                 
7849: 7F              LD      A,A                 
784A: 7F              LD      A,A                 
784B: 7F              LD      A,A                 
784C: 7F              LD      A,A                 
784D: 7F              LD      A,A                 
784E: 98              SBC     B                   
784F: 80              ADD     A,B                 
7850: 1F              RRA                         
7851: 7F              LD      A,A                 
7852: 7F              LD      A,A                 
7853: 7F              LD      A,A                 
7854: 7F              LD      A,A                 
7855: 7F              LD      A,A                 
7856: 7F              LD      A,A                 
7857: 7F              LD      A,A                 
7858: A5              AND     L                   
7859: A6              AND     (HL)                
785A: A7              AND     A                   
785B: A8              XOR     B                   
785C: A9              XOR     C                   
785D: 7F              LD      A,A                 
785E: 7F              LD      A,A                 
785F: 7F              LD      A,A                 
7860: 7F              LD      A,A                 
7861: 7F              LD      A,A                 
7862: 7F              LD      A,A                 
7863: 7F              LD      A,A                 
7864: 7F              LD      A,A                 
7865: 7F              LD      A,A                 
7866: 7F              LD      A,A                 
7867: 7F              LD      A,A                 
7868: 7F              LD      A,A                 
7869: 7F              LD      A,A                 
786A: 7F              LD      A,A                 
786B: 7F              LD      A,A                 
786C: 7F              LD      A,A                 
786D: 7F              LD      A,A                 
786E: 7F              LD      A,A                 
786F: 7F              LD      A,A                 
7870: 7F              LD      A,A                 
7871: 98              SBC     B                   
7872: A0              AND     B                   
7873: 1F              RRA                         
7874: 7F              LD      A,A                 
7875: 7F              LD      A,A                 
7876: 9E              SBC     (HL)                
7877: 7F              LD      A,A                 
7878: 7F              LD      A,A                 
7879: 7F              LD      A,A                 
787A: 7F              LD      A,A                 
787B: B0              OR      B                   
787C: B1              OR      C                   
787D: B2              OR      D                   
787E: AA              XOR     D                   
787F: AB              XOR     E                   
7880: 7F              LD      A,A                 
7881: AC              XOR     H                   
7882: 7F              LD      A,A                 
7883: 7F              LD      A,A                 
7884: 7F              LD      A,A                 
7885: 7F              LD      A,A                 
7886: 7F              LD      A,A                 
7887: 7F              LD      A,A                 
7888: 7F              LD      A,A                 
7889: 7F              LD      A,A                 
788A: 7F              LD      A,A                 
788B: 7F              LD      A,A                 
788C: 7F              LD      A,A                 
788D: 7F              LD      A,A                 
788E: 7F              LD      A,A                 
788F: 7F              LD      A,A                 
7890: 7F              LD      A,A                 
7891: 7F              LD      A,A                 
7892: 7F              LD      A,A                 
7893: 7F              LD      A,A                 
7894: 98              SBC     B                   
7895: C0              RET     NZ                  
7896: 1F              RRA                         
7897: 7F              LD      A,A                 
7898: 7F              LD      A,A                 
7899: 9F              SBC     A                   
789A: AD              XOR     L                   
789B: 7F              LD      A,A                 
789C: B6              OR      (HL)                
789D: B7              OR      A                   
789E: A1              AND     C                   
789F: A2              AND     D                   
78A0: B9              CP      C                   
78A1: BA              CP      D                   
78A2: BB              CP      E                   
78A3: BC              CP      H                   
78A4: BD              CP      L                   
78A5: BE              CP      (HL)                
78A6: BF              CP      A                   
78A7: C0              RET     NZ                  
78A8: C1              POP     BC                  
78A9: 7F              LD      A,A                 
78AA: 7F              LD      A,A                 
78AB: 7F              LD      A,A                 
78AC: 7F              LD      A,A                 
78AD: 7F              LD      A,A                 
78AE: 7F              LD      A,A                 
78AF: 7F              LD      A,A                 
78B0: 7F              LD      A,A                 
78B1: 7F              LD      A,A                 
78B2: 7F              LD      A,A                 
78B3: 7F              LD      A,A                 
78B4: 7F              LD      A,A                 
78B5: 7F              LD      A,A                 
78B6: 7F              LD      A,A                 
78B7: 98              SBC     B                   
78B8: E0 1F           LD      ($FF00+$1F),A       
78BA: 7F              LD      A,A                 
78BB: 7F              LD      A,A                 
78BC: AE              XOR     (HL)                
78BD: AF              XOR     A                   
78BE: B5              OR      L                   
78BF: C2 C3 B1        JP      NZ,$B1C3            
78C2: B2              OR      D                   
78C3: C5              PUSH    BC                  
78C4: C6 C7           ADD     $C7                 
78C6: C8              RET     Z                   
78C7: C9              RET                         
78C8: CA CB CC        JP      Z,$CCCB             
78CB: CD 7F 7F        CALL    $7F7F               ; {}
78CE: 7F              LD      A,A                 
78CF: 7F              LD      A,A                 
78D0: 7F              LD      A,A                 
78D1: 7F              LD      A,A                 
78D2: 7F              LD      A,A                 
78D3: 7F              LD      A,A                 
78D4: 7F              LD      A,A                 
78D5: 7F              LD      A,A                 
78D6: 7F              LD      A,A                 
78D7: 7F              LD      A,A                 
78D8: 7F              LD      A,A                 
78D9: 7F              LD      A,A                 
78DA: 99              SBC     C                   
78DB: 00              NOP                         
78DC: 1F              RRA                         
78DD: 7F              LD      A,A                 
78DE: 7F              LD      A,A                 
78DF: CE CF           ADC     $CF                 
78E1: B8              CP      B                   
78E2: D0              RET     NC                  
78E3: D1              POP     DE                  
78E4: A2              AND     D                   
78E5: A3              AND     E                   
78E6: D2 D3 D4        JP      NC,$D4D3            
78E9: D5              PUSH    DE                  
78EA: D6 D7           SUB     $D7                 
78EC: D8              RET     C                   
78ED: D9              RETI                        
78EE: 7F              LD      A,A                 
78EF: 7F              LD      A,A                 
78F0: 7F              LD      A,A                 
78F1: 7F              LD      A,A                 
78F2: 7F              LD      A,A                 
78F3: 7F              LD      A,A                 
78F4: 7F              LD      A,A                 
78F5: 7F              LD      A,A                 
78F6: 7F              LD      A,A                 
78F7: 7F              LD      A,A                 
78F8: 7F              LD      A,A                 
78F9: 7F              LD      A,A                 
78FA: 7F              LD      A,A                 
78FB: 7F              LD      A,A                 
78FC: 7F              LD      A,A                 
78FD: 99              SBC     C                   
78FE: 20 1F           JR      NZ,$791F            ; {}
7900: 7F              LD      A,A                 
7901: 7F              LD      A,A                 
7902: 7F              LD      A,A                 
7903: DC DD DE        CALL    C,$DEDD             
7906: C4 B2 B3        CALL    NZ,$B3B2            
7909: DF              RST     0X18                
790A: E0 E1           LD      ($FF00+$E1),A       
790C: E2              LD      (C),A               
790D: E3                              
790E: E4                              
790F: E5              PUSH    HL                  
7910: 7F              LD      A,A                 
7911: 7F              LD      A,A                 
7912: 7F              LD      A,A                 
7913: 7F              LD      A,A                 
7914: 7F              LD      A,A                 
7915: 7F              LD      A,A                 
7916: 7F              LD      A,A                 
7917: 7F              LD      A,A                 
7918: 7F              LD      A,A                 
7919: 7F              LD      A,A                 
791A: 7F              LD      A,A                 
791B: 7F              LD      A,A                 
791C: 7F              LD      A,A                 
791D: 7F              LD      A,A                 
791E: 7F              LD      A,A                 
791F: 7F              LD      A,A                 
7920: 99              SBC     C                   
7921: 40              LD      B,B                 
7922: 1F              RRA                         
7923: 7F              LD      A,A                 
7924: 7F              LD      A,A                 
7925: 7F              LD      A,A                 
7926: 7F              LD      A,A                 
7927: E8 E9           ADD     SP,$E9              
7929: EA EB A4        LD      ($A4EB),A           
792C: 7F              LD      A,A                 
792D: EC                              
792E: ED                              
792F: EE EF           XOR     $EF                 
7931: F0 F1           LD      A,($F1)             
7933: F2                              
7934: F3              DI                          
7935: 7F              LD      A,A                 
7936: 7F              LD      A,A                 
7937: 7F              LD      A,A                 
7938: 7F              LD      A,A                 
7939: 7F              LD      A,A                 
793A: 7F              LD      A,A                 
793B: 7F              LD      A,A                 
793C: 7F              LD      A,A                 
793D: 7F              LD      A,A                 
793E: 7F              LD      A,A                 
793F: 7F              LD      A,A                 
7940: 7F              LD      A,A                 
7941: 7F              LD      A,A                 
7942: 7F              LD      A,A                 
7943: 99              SBC     C                   
7944: 60              LD      H,B                 
7945: 1F              RRA                         
7946: 7F              LD      A,A                 
7947: 7F              LD      A,A                 
7948: 7F              LD      A,A                 
7949: 7F              LD      A,A                 
794A: B0              OR      B                   
794B: B1              OR      C                   
794C: F4                              
794D: F5              PUSH    AF                  
794E: F6 F7           OR      $F7                 
7950: F8 F9           LD      HL,SP+$F9           
7952: FA FB FC        LD      A,($FCFB)           
7955: FD                              
7956: FE FF           CP      $FF                 
7958: 7F              LD      A,A                 
7959: 7F              LD      A,A                 
795A: 7F              LD      A,A                 
795B: 7F              LD      A,A                 
795C: 7F              LD      A,A                 
795D: 7F              LD      A,A                 
795E: 7F              LD      A,A                 
795F: 7F              LD      A,A                 
7960: 7F              LD      A,A                 
7961: 7F              LD      A,A                 
7962: 7F              LD      A,A                 
7963: 7F              LD      A,A                 
7964: 7F              LD      A,A                 
7965: 7F              LD      A,A                 
7966: 99              SBC     C                   
7967: 80              ADD     A,B                 
7968: 1F              RRA                         
7969: 7F              LD      A,A                 
796A: 7F              LD      A,A                 
796B: 7F              LD      A,A                 
796C: A0              AND     B                   
796D: A1              AND     C                   
796E: A2              AND     D                   
796F: A3              AND     E                   
7970: 00              NOP                         
7971: 01 02 03        LD      BC,$0302            
7974: 04              INC     B                   
7975: 05              DEC     B                   
7976: 06 07           LD      B,$07               
7978: 08 09 0A        LD      ($0A09),SP          
797B: 7F              LD      A,A                 
797C: 7F              LD      A,A                 
797D: 7F              LD      A,A                 
797E: 7F              LD      A,A                 
797F: 7F              LD      A,A                 
7980: 7F              LD      A,A                 
7981: 7F              LD      A,A                 
7982: 7F              LD      A,A                 
7983: 7F              LD      A,A                 
7984: 7F              LD      A,A                 
7985: 7F              LD      A,A                 
7986: 7F              LD      A,A                 
7987: 7F              LD      A,A                 
7988: 7F              LD      A,A                 
7989: 99              SBC     C                   
798A: A0              AND     B                   
798B: 1F              RRA                         
798C: 7F              LD      A,A                 
798D: 7F              LD      A,A                 
798E: 7F              LD      A,A                 
798F: B0              OR      B                   
7990: B1              OR      C                   
7991: B2              OR      D                   
7992: B3              OR      E                   
7993: 0B              DEC     BC                  
7994: 0C              INC     C                   
7995: 0D              DEC     C                   
7996: 0E 0F           LD      C,$0F               
7998: 10 11           ;;STOP    $11                 
799A: 12              LD      (DE),A              
799B: 13              INC     DE                  
799C: 7F              LD      A,A                 
799D: 7F              LD      A,A                 
799E: 7F              LD      A,A                 
799F: 7F              LD      A,A                 
79A0: 7F              LD      A,A                 
79A1: 7F              LD      A,A                 
79A2: 7F              LD      A,A                 
79A3: 7F              LD      A,A                 
79A4: 7F              LD      A,A                 
79A5: 7F              LD      A,A                 
79A6: 7F              LD      A,A                 
79A7: 7F              LD      A,A                 
79A8: 7F              LD      A,A                 
79A9: 7F              LD      A,A                 
79AA: 7F              LD      A,A                 
79AB: 7F              LD      A,A                 
79AC: 99              SBC     C                   
79AD: C0              RET     NZ                  
79AE: 1F              RRA                         
79AF: 7F              LD      A,A                 
79B0: 7F              LD      A,A                 
79B1: A0              AND     B                   
79B2: A1              AND     C                   
79B3: A2              AND     D                   
79B4: A3              AND     E                   
79B5: A4              AND     H                   
79B6: 7F              LD      A,A                 
79B7: 7F              LD      A,A                 
79B8: 7F              LD      A,A                 
79B9: 14              INC     D                   
79BA: 15              DEC     D                   
79BB: 16 17           LD      D,$17               
79BD: 18 19           JR      $79D8               ; {}
79BF: 7F              LD      A,A                 
79C0: 7F              LD      A,A                 
79C1: 7F              LD      A,A                 
79C2: 7F              LD      A,A                 
79C3: 7F              LD      A,A                 
79C4: 7F              LD      A,A                 
79C5: 7F              LD      A,A                 
79C6: 7F              LD      A,A                 
79C7: 7F              LD      A,A                 
79C8: 7F              LD      A,A                 
79C9: 7F              LD      A,A                 
79CA: 7F              LD      A,A                 
79CB: 7F              LD      A,A                 
79CC: 7F              LD      A,A                 
79CD: 7F              LD      A,A                 
79CE: 7F              LD      A,A                 
79CF: 99              SBC     C                   
79D0: E0 1F           LD      ($FF00+$1F),A       
79D2: 7F              LD      A,A                 
79D3: 7F              LD      A,A                 
79D4: B0              OR      B                   
79D5: B1              OR      C                   
79D6: B2              OR      D                   
79D7: B3              OR      E                   
79D8: B4              OR      H                   
79D9: 7F              LD      A,A                 
79DA: 7F              LD      A,A                 
79DB: DB                              
79DC: E6 E7           AND     $E7                 
79DE: 1A              LD      A,(DE)              
79DF: 1B              DEC     DE                  
79E0: 1C              INC     E                   
79E1: 1D              DEC     E                   
79E2: 7F              LD      A,A                 
79E3: 7F              LD      A,A                 
79E4: 7F              LD      A,A                 
79E5: 7F              LD      A,A                 
79E6: 7F              LD      A,A                 
79E7: 7F              LD      A,A                 
79E8: 7F              LD      A,A                 
79E9: 7F              LD      A,A                 
79EA: 7F              LD      A,A                 
79EB: 7F              LD      A,A                 
79EC: 7F              LD      A,A                 
79ED: 7F              LD      A,A                 
79EE: 7F              LD      A,A                 
79EF: 7F              LD      A,A                 
79F0: 7F              LD      A,A                 
79F1: 7F              LD      A,A                 
79F2: 9A              SBC     D                   
79F3: 00              NOP                         
79F4: 5F              LD      E,A                 
79F5: 7F              LD      A,A                 
79F6: 9A              SBC     D                   
79F7: 20 5F           JR      NZ,$7A58            ; {}
79F9: 7F              LD      A,A                 
79FA: 9A              SBC     D                   
79FB: 40              LD      B,B                 
79FC: 5F              LD      E,A                 
79FD: 7F              LD      A,A                 
79FE: 9A              SBC     D                   
79FF: 60              LD      H,B                 
7A00: 5F              LD      E,A                 
7A01: 7F              LD      A,A                 
7A02: 9B              SBC     E                   
7A03: A0              AND     B                   
7A04: 5F              LD      E,A                 
7A05: 7F              LD      A,A                 
7A06: 9B              SBC     E                   
7A07: C0              RET     NZ                  
7A08: 5F              LD      E,A                 
7A09: 7F              LD      A,A                 
7A0A: 00              NOP                         
7A0B: 98              SBC     B                   
7A0C: 00              NOP                         
7A0D: 1F              RRA                         
7A0E: 7C              LD      A,H                 
7A0F: 7C              LD      A,H                 
7A10: 7C              LD      A,H                 
7A11: 7C              LD      A,H                 
7A12: 7C              LD      A,H                 
7A13: 7C              LD      A,H                 
7A14: 7C              LD      A,H                 
7A15: 7C              LD      A,H                 
7A16: 7C              LD      A,H                 
7A17: 7C              LD      A,H                 
7A18: 7C              LD      A,H                 
7A19: 7C              LD      A,H                 
7A1A: 7C              LD      A,H                 
7A1B: 7C              LD      A,H                 
7A1C: 7C              LD      A,H                 
7A1D: 7C              LD      A,H                 
7A1E: 7C              LD      A,H                 
7A1F: 7C              LD      A,H                 
7A20: 7C              LD      A,H                 
7A21: 7C              LD      A,H                 
7A22: 44              LD      B,H                 
7A23: 45              LD      B,L                 
7A24: 7D              LD      A,L                 
7A25: 7D              LD      A,L                 
7A26: 7D              LD      A,L                 
7A27: 7D              LD      A,L                 
7A28: 7D              LD      A,L                 
7A29: 7D              LD      A,L                 
7A2A: 7D              LD      A,L                 
7A2B: 7D              LD      A,L                 
7A2C: 7D              LD      A,L                 
7A2D: 7D              LD      A,L                 
7A2E: 98              SBC     B                   
7A2F: 20 1F           JR      NZ,$7A50            ; {}
7A31: 7C              LD      A,H                 
7A32: 7C              LD      A,H                 
7A33: 7C              LD      A,H                 
7A34: 7C              LD      A,H                 
7A35: 7C              LD      A,H                 
7A36: 7C              LD      A,H                 
7A37: 7C              LD      A,H                 
7A38: 7C              LD      A,H                 
7A39: 7C              LD      A,H                 
7A3A: 7C              LD      A,H                 
7A3B: 7C              LD      A,H                 
7A3C: 7C              LD      A,H                 
7A3D: 7C              LD      A,H                 
7A3E: 7C              LD      A,H                 
7A3F: 7C              LD      A,H                 
7A40: 7C              LD      A,H                 
7A41: 40              LD      B,B                 
7A42: 41              LD      B,C                 
7A43: 42              LD      B,D                 
7A44: 43              LD      B,E                 
7A45: 7D              LD      A,L                 
7A46: 7D              LD      A,L                 
7A47: 7D              LD      A,L                 
7A48: 7D              LD      A,L                 
7A49: 7D              LD      A,L                 
7A4A: 7D              LD      A,L                 
7A4B: 7D              LD      A,L                 
7A4C: 7D              LD      A,L                 
7A4D: 7D              LD      A,L                 
7A4E: 7D              LD      A,L                 
7A4F: 7D              LD      A,L                 
7A50: 7D              LD      A,L                 
7A51: 98              SBC     B                   
7A52: 40              LD      B,B                 
7A53: 1F              RRA                         
7A54: 7C              LD      A,H                 
7A55: 7C              LD      A,H                 
7A56: 7C              LD      A,H                 
7A57: 7C              LD      A,H                 
7A58: 40              LD      B,B                 
7A59: 41              LD      B,C                 
7A5A: 42              LD      B,D                 
7A5B: 43              LD      B,E                 
7A5C: 47              LD      B,A                 
7A5D: 48              LD      C,B                 
7A5E: 49              LD      C,C                 
7A5F: 4A              LD      C,D                 
7A60: 40              LD      B,B                 
7A61: 41              LD      B,C                 
7A62: 42              LD      B,D                 
7A63: 43              LD      B,E                 
7A64: 7D              LD      A,L                 
7A65: 7D              LD      A,L                 
7A66: 7D              LD      A,L                 
7A67: 7D              LD      A,L                 
7A68: 7D              LD      A,L                 
7A69: 7D              LD      A,L                 
7A6A: 7D              LD      A,L                 
7A6B: 7D              LD      A,L                 
7A6C: 7D              LD      A,L                 
7A6D: 7D              LD      A,L                 
7A6E: 7D              LD      A,L                 
7A6F: 7D              LD      A,L                 
7A70: 7D              LD      A,L                 
7A71: 7D              LD      A,L                 
7A72: 7D              LD      A,L                 
7A73: 7D              LD      A,L                 
7A74: 98              SBC     B                   
7A75: 60              LD      H,B                 
7A76: 1F              RRA                         
7A77: 40              LD      B,B                 
7A78: 41              LD      B,C                 
7A79: 42              LD      B,D                 
7A7A: 43              LD      B,E                 
7A7B: 7D              LD      A,L                 
7A7C: 7D              LD      A,L                 
7A7D: 7D              LD      A,L                 
7A7E: 7D              LD      A,L                 
7A7F: 7D              LD      A,L                 
7A80: 7D              LD      A,L                 
7A81: 7D              LD      A,L                 
7A82: 7D              LD      A,L                 
7A83: 7D              LD      A,L                 
7A84: 7D              LD      A,L                 
7A85: 7D              LD      A,L                 
7A86: 7D              LD      A,L                 
7A87: 7D              LD      A,L                 
7A88: 7D              LD      A,L                 
7A89: 7D              LD      A,L                 
7A8A: 7D              LD      A,L                 
7A8B: 7D              LD      A,L                 
7A8C: 7D              LD      A,L                 
7A8D: 7D              LD      A,L                 
7A8E: 7D              LD      A,L                 
7A8F: 7D              LD      A,L                 
7A90: 7D              LD      A,L                 
7A91: 7D              LD      A,L                 
7A92: 7D              LD      A,L                 
7A93: 7D              LD      A,L                 
7A94: 7D              LD      A,L                 
7A95: 7D              LD      A,L                 
7A96: 7D              LD      A,L                 
7A97: 98              SBC     B                   
7A98: 80              ADD     A,B                 
7A99: 5F              LD      E,A                 
7A9A: 7D              LD      A,L                 
7A9B: 98              SBC     B                   
7A9C: A0              AND     B                   
7A9D: 5F              LD      E,A                 
7A9E: 7D              LD      A,L                 
7A9F: 98              SBC     B                   
7AA0: C0              RET     NZ                  
7AA1: 5F              LD      E,A                 
7AA2: 7D              LD      A,L                 
7AA3: 98              SBC     B                   
7AA4: E0 5F           LD      ($FF00+$5F),A       
7AA6: 7D              LD      A,L                 
7AA7: 99              SBC     C                   
7AA8: 00              NOP                         
7AA9: 1F              RRA                         
7AAA: 38 39           JR      C,$7AE5             ; {}
7AAC: 3A              LD      A,(HLD)             
7AAD: 3B              DEC     SP                  
7AAE: 38 39           JR      C,$7AE9             ; {}
7AB0: 3A              LD      A,(HLD)             
7AB1: 3B              DEC     SP                  
7AB2: 38 39           JR      C,$7AED             ; {}
7AB4: 3A              LD      A,(HLD)             
7AB5: 3B              DEC     SP                  
7AB6: 38 39           JR      C,$7AF1             ; {}
7AB8: 3A              LD      A,(HLD)             
7AB9: 3B              DEC     SP                  
7ABA: 38 39           JR      C,$7AF5             ; {}
7ABC: 3A              LD      A,(HLD)             
7ABD: 3B              DEC     SP                  
7ABE: 38 39           JR      C,$7AF9             ; {}
7AC0: 3A              LD      A,(HLD)             
7AC1: 3B              DEC     SP                  
7AC2: 38 39           JR      C,$7AFD             ; {}
7AC4: 3A              LD      A,(HLD)             
7AC5: 3B              DEC     SP                  
7AC6: 38 39           JR      C,$7B01             ; {}
7AC8: 3A              LD      A,(HLD)             
7AC9: 3B              DEC     SP                  
7ACA: 99              SBC     C                   
7ACB: 20 1F           JR      NZ,$7AEC            ; {}
7ACD: 3C              INC     A                   
7ACE: 3D              DEC     A                   
7ACF: 3E 3F           LD      A,$3F               
7AD1: 3C              INC     A                   
7AD2: 3D              DEC     A                   
7AD3: 3E 3F           LD      A,$3F               
7AD5: 3C              INC     A                   
7AD6: 3D              DEC     A                   
7AD7: 3E 3F           LD      A,$3F               
7AD9: 3C              INC     A                   
7ADA: 3D              DEC     A                   
7ADB: 3E 3F           LD      A,$3F               
7ADD: 3C              INC     A                   
7ADE: 3D              DEC     A                   
7ADF: 3E 3F           LD      A,$3F               
7AE1: 3C              INC     A                   
7AE2: 3D              DEC     A                   
7AE3: 3E 3F           LD      A,$3F               
7AE5: 3C              INC     A                   
7AE6: 3D              DEC     A                   
7AE7: 3E 3F           LD      A,$3F               
7AE9: 3C              INC     A                   
7AEA: 3D              DEC     A                   
7AEB: 3E 3F           LD      A,$3F               
7AED: 99              SBC     C                   
7AEE: 40              LD      B,B                 
7AEF: 1F              RRA                         
7AF0: 60              LD      H,B                 
7AF1: 61              LD      H,C                 
7AF2: 62              LD      H,D                 
7AF3: 63              LD      H,E                 
7AF4: 60              LD      H,B                 
7AF5: 61              LD      H,C                 
7AF6: 62              LD      H,D                 
7AF7: 63              LD      H,E                 
7AF8: 60              LD      H,B                 
7AF9: 61              LD      H,C                 
7AFA: 62              LD      H,D                 
7AFB: 63              LD      H,E                 
7AFC: 60              LD      H,B                 
7AFD: 61              LD      H,C                 
7AFE: 62              LD      H,D                 
7AFF: 63              LD      H,E                 
7B00: 60              LD      H,B                 
7B01: 61              LD      H,C                 
7B02: 62              LD      H,D                 
7B03: 63              LD      H,E                 
7B04: 60              LD      H,B                 
7B05: 61              LD      H,C                 
7B06: 62              LD      H,D                 
7B07: 63              LD      H,E                 
7B08: 60              LD      H,B                 
7B09: 61              LD      H,C                 
7B0A: 62              LD      H,D                 
7B0B: 63              LD      H,E                 
7B0C: 60              LD      H,B                 
7B0D: 61              LD      H,C                 
7B0E: 62              LD      H,D                 
7B0F: 63              LD      H,E                 
7B10: 99              SBC     C                   
7B11: 60              LD      H,B                 
7B12: 1F              RRA                         
7B13: 4E              LD      C,(HL)              
7B14: 4F              LD      C,A                 
7B15: 4E              LD      C,(HL)              
7B16: 4F              LD      C,A                 
7B17: 4E              LD      C,(HL)              
7B18: 4F              LD      C,A                 
7B19: 4E              LD      C,(HL)              
7B1A: 4F              LD      C,A                 
7B1B: 4E              LD      C,(HL)              
7B1C: 4F              LD      C,A                 
7B1D: 4E              LD      C,(HL)              
7B1E: 4F              LD      C,A                 
7B1F: 4E              LD      C,(HL)              
7B20: 4F              LD      C,A                 
7B21: 4E              LD      C,(HL)              
7B22: 4F              LD      C,A                 
7B23: 4E              LD      C,(HL)              
7B24: 4F              LD      C,A                 
7B25: 4E              LD      C,(HL)              
7B26: 4F              LD      C,A                 
7B27: 4E              LD      C,(HL)              
7B28: 4F              LD      C,A                 
7B29: 4E              LD      C,(HL)              
7B2A: 4F              LD      C,A                 
7B2B: 4E              LD      C,(HL)              
7B2C: 4F              LD      C,A                 
7B2D: 4E              LD      C,(HL)              
7B2E: 4F              LD      C,A                 
7B2F: 4E              LD      C,(HL)              
7B30: 4F              LD      C,A                 
7B31: 4E              LD      C,(HL)              
7B32: 4F              LD      C,A                 
7B33: 99              SBC     C                   
7B34: 80              ADD     A,B                 
7B35: 5F              LD      E,A                 
7B36: 7E              LD      A,(HL)              
7B37: 99              SBC     C                   
7B38: A0              AND     B                   
7B39: 5F              LD      E,A                 
7B3A: 7E              LD      A,(HL)              
7B3B: 99              SBC     C                   
7B3C: C0              RET     NZ                  
7B3D: 5F              LD      E,A                 
7B3E: 64              LD      H,H                 
7B3F: 99              SBC     C                   
7B40: E0 1F           LD      ($FF00+$1F),A       
7B42: 30 31           JR      NC,$7B75            ; {}
7B44: 32              LD      (HLD),A             
7B45: 33              INC     SP                  
7B46: 30 31           JR      NC,$7B79            ; {}
7B48: 32              LD      (HLD),A             
7B49: 33              INC     SP                  
7B4A: 30 31           JR      NC,$7B7D            ; {}
7B4C: 32              LD      (HLD),A             
7B4D: 33              INC     SP                  
7B4E: 30 31           JR      NC,$7B81            ; {}
7B50: 32              LD      (HLD),A             
7B51: 33              INC     SP                  
7B52: 30 31           JR      NC,$7B85            ; {}
7B54: 32              LD      (HLD),A             
7B55: 33              INC     SP                  
7B56: 30 31           JR      NC,$7B89            ; {}
7B58: 32              LD      (HLD),A             
7B59: 33              INC     SP                  
7B5A: 30 31           JR      NC,$7B8D            ; {}
7B5C: 32              LD      (HLD),A             
7B5D: 33              INC     SP                  
7B5E: 30 31           JR      NC,$7B91            ; {}
7B60: 32              LD      (HLD),A             
7B61: 33              INC     SP                  
7B62: 9A              SBC     D                   
7B63: 00              NOP                         
7B64: 1F              RRA                         
7B65: 34              INC     (HL)                
7B66: 35              DEC     (HL)                
7B67: 36 37           LD      (HL),$37            
7B69: 34              INC     (HL)                
7B6A: 35              DEC     (HL)                
7B6B: 36 37           LD      (HL),$37            
7B6D: 34              INC     (HL)                
7B6E: 35              DEC     (HL)                
7B6F: 36 37           LD      (HL),$37            
7B71: 34              INC     (HL)                
7B72: 35              DEC     (HL)                
7B73: 36 37           LD      (HL),$37            
7B75: 34              INC     (HL)                
7B76: 35              DEC     (HL)                
7B77: 36 37           LD      (HL),$37            
7B79: 34              INC     (HL)                
7B7A: 35              DEC     (HL)                
7B7B: 36 37           LD      (HL),$37            
7B7D: 34              INC     (HL)                
7B7E: 35              DEC     (HL)                
7B7F: 36 37           LD      (HL),$37            
7B81: 34              INC     (HL)                
7B82: 35              DEC     (HL)                
7B83: 36 37           LD      (HL),$37            
7B85: 9A              SBC     D                   
7B86: 20 5F           JR      NZ,$7BE7            ; {}
7B88: 7C              LD      A,H                 
7B89: 00              NOP                         
7B8A: 98              SBC     B                   
7B8B: 00              NOP                         
7B8C: 53              LD      D,E                 
7B8D: 7C              LD      A,H                 
7B8E: 98              SBC     B                   
7B8F: 20 53           JR      NZ,$7BE4            ; {}
7B91: 7C              LD      A,H                 
7B92: 98              SBC     B                   
7B93: 40              LD      B,B                 
7B94: 13              INC     DE                  
7B95: 7C              LD      A,H                 
7B96: 7C              LD      A,H                 
7B97: 80              ADD     A,B                 
7B98: 81              ADD     A,C                 
7B99: 82              ADD     A,D                 
7B9A: 83              ADD     A,E                 
7B9B: 84              ADD     A,H                 
7B9C: 85              ADD     A,L                 
7B9D: 86              ADD     A,(HL)              
7B9E: 87              ADD     A,A                 
7B9F: 88              ADC     A,B                 
7BA0: 89              ADC     A,C                 
7BA1: 8A              ADC     A,D                 
7BA2: 8B              ADC     A,E                 
7BA3: 8C              ADC     A,H                 
7BA4: 8D              ADC     A,L                 
7BA5: 8E              ADC     A,(HL)              
7BA6: 8F              ADC     A,A                 
7BA7: 7C              LD      A,H                 
7BA8: 7C              LD      A,H                 
7BA9: 98              SBC     B                   
7BAA: 60              LD      H,B                 
7BAB: 13              INC     DE                  
7BAC: 7C              LD      A,H                 
7BAD: 7C              LD      A,H                 
7BAE: 90              SUB     B                   
7BAF: 91              SUB     C                   
7BB0: 92              SUB     D                   
7BB1: 93              SUB     E                   
7BB2: 94              SUB     H                   
7BB3: 95              SUB     L                   
7BB4: 96              SUB     (HL)                
7BB5: 97              SUB     A                   
7BB6: 98              SBC     B                   
7BB7: 99              SBC     C                   
7BB8: 9A              SBC     D                   
7BB9: 9B              SBC     E                   
7BBA: 9C              SBC     H                   
7BBB: 9D              SBC     L                   
7BBC: 9E              SBC     (HL)                
7BBD: 9F              SBC     A                   
7BBE: 7C              LD      A,H                 
7BBF: 7C              LD      A,H                 
7BC0: 98              SBC     B                   
7BC1: 80              ADD     A,B                 
7BC2: 13              INC     DE                  
7BC3: 7C              LD      A,H                 
7BC4: 7C              LD      A,H                 
7BC5: A0              AND     B                   
7BC6: A1              AND     C                   
7BC7: A2              AND     D                   
7BC8: A3              AND     E                   
7BC9: A4              AND     H                   
7BCA: A5              AND     L                   
7BCB: A6              AND     (HL)                
7BCC: A7              AND     A                   
7BCD: A8              XOR     B                   
7BCE: A9              XOR     C                   
7BCF: AA              XOR     D                   
7BD0: AB              XOR     E                   
7BD1: AC              XOR     H                   
7BD2: AD              XOR     L                   
7BD3: AE              XOR     (HL)                
7BD4: AF              XOR     A                   
7BD5: 7C              LD      A,H                 
7BD6: 7C              LD      A,H                 
7BD7: 98              SBC     B                   
7BD8: A0              AND     B                   
7BD9: 13              INC     DE                  
7BDA: 7C              LD      A,H                 
7BDB: 7C              LD      A,H                 
7BDC: B0              OR      B                   
7BDD: B1              OR      C                   
7BDE: B2              OR      D                   
7BDF: B3              OR      E                   
7BE0: B4              OR      H                   
7BE1: B5              OR      L                   
7BE2: B6              OR      (HL)                
7BE3: B7              OR      A                   
7BE4: B8              CP      B                   
7BE5: B9              CP      C                   
7BE6: BA              CP      D                   
7BE7: BB              CP      E                   
7BE8: BC              CP      H                   
7BE9: BD              CP      L                   
7BEA: BE              CP      (HL)                
7BEB: BF              CP      A                   
7BEC: 7C              LD      A,H                 
7BED: 7C              LD      A,H                 
7BEE: 98              SBC     B                   
7BEF: C0              RET     NZ                  
7BF0: 13              INC     DE                  
7BF1: 7C              LD      A,H                 
7BF2: 7C              LD      A,H                 
7BF3: C0              RET     NZ                  
7BF4: C1              POP     BC                  
7BF5: C2 C3 C4        JP      NZ,$C4C3            
7BF8: C5              PUSH    BC                  
7BF9: C6 C7           ADD     $C7                 
7BFB: C8              RET     Z                   
7BFC: C9              RET                         
7BFD: CA CB CC        JP      Z,$CCCB             
7C00: CD CE CF        CALL    $CFCE               
7C03: 7C              LD      A,H                 
7C04: 7C              LD      A,H                 
7C05: 98              SBC     B                   
7C06: E0 13           LD      ($FF00+$13),A       
7C08: 7C              LD      A,H                 
7C09: 7C              LD      A,H                 
7C0A: D0              RET     NC                  
7C0B: D1              POP     DE                  
7C0C: D2 D3 D4        JP      NC,$D4D3            
7C0F: D5              PUSH    DE                  
7C10: D6 D7           SUB     $D7                 
7C12: D8              RET     C                   
7C13: D9              RETI                        
7C14: DA DB DC        JP      C,$DCDB             
7C17: DD                              
7C18: DE DF           SBC     $DF                 
7C1A: 7C              LD      A,H                 
7C1B: 7C              LD      A,H                 
7C1C: 99              SBC     C                   
7C1D: 00              NOP                         
7C1E: 13              INC     DE                  
7C1F: 7C              LD      A,H                 
7C20: 7C              LD      A,H                 
7C21: E0 E1           LD      ($FF00+$E1),A       
7C23: E2              LD      (C),A               
7C24: E3                              
7C25: E4                              
7C26: E5              PUSH    HL                  
7C27: E6 E7           AND     $E7                 
7C29: E8 E9           ADD     SP,$E9              
7C2B: EA EB EC        LD      ($ECEB),A           
7C2E: ED                              
7C2F: EE EF           XOR     $EF                 
7C31: 7C              LD      A,H                 
7C32: 7C              LD      A,H                 
7C33: 99              SBC     C                   
7C34: 20 13           JR      NZ,$7C49            ; {}
7C36: 7C              LD      A,H                 
7C37: 7C              LD      A,H                 
7C38: 7C              LD      A,H                 
7C39: 7C              LD      A,H                 
7C3A: 7C              LD      A,H                 
7C3B: 7C              LD      A,H                 
7C3C: 7C              LD      A,H                 
7C3D: 7C              LD      A,H                 
7C3E: 7C              LD      A,H                 
7C3F: 2B              DEC     HL                  
7C40: 2C              INC     L                   
7C41: 7C              LD      A,H                 
7C42: 7C              LD      A,H                 
7C43: 7C              LD      A,H                 
7C44: 7C              LD      A,H                 
7C45: 7C              LD      A,H                 
7C46: 7C              LD      A,H                 
7C47: 7C              LD      A,H                 
7C48: 7C              LD      A,H                 
7C49: 7C              LD      A,H                 
7C4A: 99              SBC     C                   
7C4B: 40              LD      B,B                 
7C4C: 13              INC     DE                  
7C4D: 7C              LD      A,H                 
7C4E: 7C              LD      A,H                 
7C4F: 7C              LD      A,H                 
7C50: 7C              LD      A,H                 
7C51: 7C              LD      A,H                 
7C52: 7C              LD      A,H                 
7C53: 7C              LD      A,H                 
7C54: 7C              LD      A,H                 
7C55: 50              LD      D,B                 
7C56: 51              LD      D,C                 
7C57: 52              LD      D,D                 
7C58: 53              LD      D,E                 
7C59: 7C              LD      A,H                 
7C5A: 7C              LD      A,H                 
7C5B: 7C              LD      A,H                 
7C5C: 7C              LD      A,H                 
7C5D: 7C              LD      A,H                 
7C5E: 7C              LD      A,H                 
7C5F: 7C              LD      A,H                 
7C60: 7C              LD      A,H                 
7C61: 99              SBC     C                   
7C62: 60              LD      H,B                 
7C63: 13              INC     DE                  
7C64: 7C              LD      A,H                 
7C65: 7C              LD      A,H                 
7C66: 7C              LD      A,H                 
7C67: 7C              LD      A,H                 
7C68: 7C              LD      A,H                 
7C69: 7C              LD      A,H                 
7C6A: 7C              LD      A,H                 
7C6B: 7C              LD      A,H                 
7C6C: 54              LD      D,H                 
7C6D: 55              LD      D,L                 
7C6E: 56              LD      D,(HL)              
7C6F: 57              LD      D,A                 
7C70: 7C              LD      A,H                 
7C71: 7C              LD      A,H                 
7C72: 7C              LD      A,H                 
7C73: 7C              LD      A,H                 
7C74: 7C              LD      A,H                 
7C75: 7C              LD      A,H                 
7C76: 7C              LD      A,H                 
7C77: 7C              LD      A,H                 
7C78: 99              SBC     C                   
7C79: 80              ADD     A,B                 
7C7A: 13              INC     DE                  
7C7B: 7C              LD      A,H                 
7C7C: 7C              LD      A,H                 
7C7D: 7C              LD      A,H                 
7C7E: 7C              LD      A,H                 
7C7F: 7C              LD      A,H                 
7C80: 7C              LD      A,H                 
7C81: 7C              LD      A,H                 
7C82: 7C              LD      A,H                 
7C83: 58              LD      E,B                 
7C84: 59              LD      E,C                 
7C85: 5A              LD      E,D                 
7C86: 5B              LD      E,E                 
7C87: 7C              LD      A,H                 
7C88: 7C              LD      A,H                 
7C89: 7C              LD      A,H                 
7C8A: 7C              LD      A,H                 
7C8B: 7C              LD      A,H                 
7C8C: 7C              LD      A,H                 
7C8D: 7C              LD      A,H                 
7C8E: 7C              LD      A,H                 
7C8F: 99              SBC     C                   
7C90: A0              AND     B                   
7C91: 13              INC     DE                  
7C92: 7C              LD      A,H                 
7C93: 7C              LD      A,H                 
7C94: 7C              LD      A,H                 
7C95: 7C              LD      A,H                 
7C96: 7C              LD      A,H                 
7C97: 7C              LD      A,H                 
7C98: 7C              LD      A,H                 
7C99: 7C              LD      A,H                 
7C9A: 5C              LD      E,H                 
7C9B: 5D              LD      E,L                 
7C9C: 5E              LD      E,(HL)              
7C9D: 5F              LD      E,A                 
7C9E: 7C              LD      A,H                 
7C9F: 7C              LD      A,H                 
7CA0: 7C              LD      A,H                 
7CA1: 7C              LD      A,H                 
7CA2: 7C              LD      A,H                 
7CA3: 7C              LD      A,H                 
7CA4: 7C              LD      A,H                 
7CA5: 7C              LD      A,H                 
7CA6: 99              SBC     C                   
7CA7: C0              RET     NZ                  
7CA8: 13              INC     DE                  
7CA9: 7C              LD      A,H                 
7CAA: 7C              LD      A,H                 
7CAB: 7C              LD      A,H                 
7CAC: 7C              LD      A,H                 
7CAD: 7C              LD      A,H                 
7CAE: 7C              LD      A,H                 
7CAF: 7C              LD      A,H                 
7CB0: 46              LD      B,(HL)              
7CB1: 7D              LD      A,L                 
7CB2: 7D              LD      A,L                 
7CB3: 7D              LD      A,L                 
7CB4: 7D              LD      A,L                 
7CB5: 4B              LD      C,E                 
7CB6: 7C              LD      A,H                 
7CB7: 7C              LD      A,H                 
7CB8: 7C              LD      A,H                 
7CB9: 7C              LD      A,H                 
7CBA: 7C              LD      A,H                 
7CBB: 7C              LD      A,H                 
7CBC: 7C              LD      A,H                 
7CBD: 99              SBC     C                   
7CBE: E0 13           LD      ($FF00+$13),A       
7CC0: 7C              LD      A,H                 
7CC1: 7C              LD      A,H                 
7CC2: 7C              LD      A,H                 
7CC3: 7C              LD      A,H                 
7CC4: 7C              LD      A,H                 
7CC5: 65              LD      H,L                 
7CC6: 66              LD      H,(HL)              
7CC7: 67              LD      H,A                 
7CC8: 68              LD      L,B                 
7CC9: 69              LD      L,C                 
7CCA: 6A              LD      L,D                 
7CCB: 6B              LD      L,E                 
7CCC: 6C              LD      L,H                 
7CCD: 6D              LD      L,L                 
7CCE: 6E              LD      L,(HL)              
7CCF: 7C              LD      A,H                 
7CD0: 7C              LD      A,H                 
7CD1: 7C              LD      A,H                 
7CD2: 7C              LD      A,H                 
7CD3: 7C              LD      A,H                 
7CD4: 9A              SBC     D                   
7CD5: 00              NOP                         
7CD6: 13              INC     DE                  
7CD7: 7C              LD      A,H                 
7CD8: 7C              LD      A,H                 
7CD9: 7C              LD      A,H                 
7CDA: 7C              LD      A,H                 
7CDB: 44              LD      B,H                 
7CDC: 45              LD      B,L                 
7CDD: 7D              LD      A,L                 
7CDE: 7D              LD      A,L                 
7CDF: 7D              LD      A,L                 
7CE0: 7D              LD      A,L                 
7CE1: 7D              LD      A,L                 
7CE2: 7D              LD      A,L                 
7CE3: 7D              LD      A,L                 
7CE4: 7D              LD      A,L                 
7CE5: 4C              LD      C,H                 
7CE6: 4D              LD      C,L                 
7CE7: 7C              LD      A,H                 
7CE8: 7C              LD      A,H                 
7CE9: 7C              LD      A,H                 
7CEA: 7C              LD      A,H                 
7CEB: 9A              SBC     D                   
7CEC: 20 13           JR      NZ,$7D01            ; {}
7CEE: 7C              LD      A,H                 
7CEF: 7C              LD      A,H                 
7CF0: 44              LD      B,H                 
7CF1: 45              LD      B,L                 
7CF2: 7D              LD      A,L                 
7CF3: 7D              LD      A,L                 
7CF4: 7D              LD      A,L                 
7CF5: 7D              LD      A,L                 
7CF6: 7D              LD      A,L                 
7CF7: 7D              LD      A,L                 
7CF8: 7D              LD      A,L                 
7CF9: 7D              LD      A,L                 
7CFA: 7D              LD      A,L                 
7CFB: 7D              LD      A,L                 
7CFC: 7D              LD      A,L                 
7CFD: 7D              LD      A,L                 
7CFE: 4C              LD      C,H                 
7CFF: 4D              LD      C,L                 
7D00: 7C              LD      A,H                 
7D01: 7C              LD      A,H                 
7D02: 00              NOP                         
7D03: FF              RST     0X38                
7D04: FF              RST     0X38                
7D05: FF              RST     0X38                
7D06: FF              RST     0X38                
7D07: FF              RST     0X38                
7D08: FF              RST     0X38                
7D09: FF              RST     0X38                
7D0A: FF              RST     0X38                
7D0B: FF              RST     0X38                
7D0C: FF              RST     0X38                
7D0D: FF              RST     0X38                
7D0E: FF              RST     0X38                
7D0F: FF              RST     0X38                
7D10: FF              RST     0X38                
7D11: FF              RST     0X38                
7D12: FF              RST     0X38                
7D13: FF              RST     0X38                
7D14: FF              RST     0X38                
7D15: FF              RST     0X38                
7D16: FF              RST     0X38                
7D17: FF              RST     0X38                
7D18: FF              RST     0X38                
7D19: FF              RST     0X38                
7D1A: FF              RST     0X38                
7D1B: FF              RST     0X38                
7D1C: FF              RST     0X38                
7D1D: FF              RST     0X38                
7D1E: FF              RST     0X38                
7D1F: FF              RST     0X38                
7D20: FF              RST     0X38                
7D21: FF              RST     0X38                
7D22: FF              RST     0X38                
7D23: FF              RST     0X38                
7D24: FF              RST     0X38                
7D25: FF              RST     0X38                
7D26: FF              RST     0X38                
7D27: FF              RST     0X38                
7D28: FF              RST     0X38                
7D29: FF              RST     0X38                
7D2A: FF              RST     0X38                
7D2B: FF              RST     0X38                
7D2C: FF              RST     0X38                
7D2D: FF              RST     0X38                
7D2E: FF              RST     0X38                
7D2F: FF              RST     0X38                
7D30: FF              RST     0X38                
7D31: FF              RST     0X38                
7D32: FF              RST     0X38                
7D33: FF              RST     0X38                
7D34: FF              RST     0X38                
7D35: FF              RST     0X38                
7D36: FF              RST     0X38                
7D37: FF              RST     0X38                
7D38: FF              RST     0X38                
7D39: FF              RST     0X38                
7D3A: FF              RST     0X38                
7D3B: FF              RST     0X38                
7D3C: FF              RST     0X38                
7D3D: FF              RST     0X38                
7D3E: FF              RST     0X38                
7D3F: FF              RST     0X38                
7D40: FF              RST     0X38                
7D41: FF              RST     0X38                
7D42: FF              RST     0X38                
7D43: FF              RST     0X38                
7D44: FF              RST     0X38                
7D45: FF              RST     0X38                
7D46: FF              RST     0X38                
7D47: FF              RST     0X38                
7D48: FF              RST     0X38                
7D49: FF              RST     0X38                
7D4A: FF              RST     0X38                
7D4B: FF              RST     0X38                
7D4C: FF              RST     0X38                
7D4D: FF              RST     0X38                
7D4E: FF              RST     0X38                
7D4F: FF              RST     0X38                
7D50: FF              RST     0X38                
7D51: FF              RST     0X38                
7D52: FF              RST     0X38                
7D53: FF              RST     0X38                
7D54: FF              RST     0X38                
7D55: FF              RST     0X38                
7D56: FF              RST     0X38                
7D57: FF              RST     0X38                
7D58: FF              RST     0X38                
7D59: FF              RST     0X38                
7D5A: FF              RST     0X38                
7D5B: FF              RST     0X38                
7D5C: FF              RST     0X38                
7D5D: FF              RST     0X38                
7D5E: FF              RST     0X38                
7D5F: FF              RST     0X38                
7D60: FF              RST     0X38                
7D61: FF              RST     0X38                
7D62: FF              RST     0X38                
7D63: FF              RST     0X38                
7D64: FF              RST     0X38                
7D65: FF              RST     0X38                
7D66: FF              RST     0X38                
7D67: FF              RST     0X38                
7D68: FF              RST     0X38                
7D69: FF              RST     0X38                
7D6A: FF              RST     0X38                
7D6B: FF              RST     0X38                
7D6C: FF              RST     0X38                
7D6D: FF              RST     0X38                
7D6E: FF              RST     0X38                
7D6F: FF              RST     0X38                
7D70: FF              RST     0X38                
7D71: FF              RST     0X38                
7D72: FF              RST     0X38                
7D73: FF              RST     0X38                
7D74: FF              RST     0X38                
7D75: FF              RST     0X38                
7D76: FF              RST     0X38                
7D77: FF              RST     0X38                
7D78: FF              RST     0X38                
7D79: FF              RST     0X38                
7D7A: FF              RST     0X38                
7D7B: FF              RST     0X38                
7D7C: FF              RST     0X38                
7D7D: FF              RST     0X38                
7D7E: FF              RST     0X38                
7D7F: FF              RST     0X38                
7D80: FF              RST     0X38                
7D81: FF              RST     0X38                
7D82: FF              RST     0X38                
7D83: FF              RST     0X38                
7D84: FF              RST     0X38                
7D85: FF              RST     0X38                
7D86: FF              RST     0X38                
7D87: FF              RST     0X38                
7D88: FF              RST     0X38                
7D89: FF              RST     0X38                
7D8A: FF              RST     0X38                
7D8B: FF              RST     0X38                
7D8C: FF              RST     0X38                
7D8D: FF              RST     0X38                
7D8E: FF              RST     0X38                
7D8F: FF              RST     0X38                
7D90: FF              RST     0X38                
7D91: FF              RST     0X38                
7D92: FF              RST     0X38                
7D93: FF              RST     0X38                
7D94: FF              RST     0X38                
7D95: FF              RST     0X38                
7D96: FF              RST     0X38                
7D97: FF              RST     0X38                
7D98: FF              RST     0X38                
7D99: FF              RST     0X38                
7D9A: FF              RST     0X38                
7D9B: FF              RST     0X38                
7D9C: FF              RST     0X38                
7D9D: FF              RST     0X38                
7D9E: FF              RST     0X38                
7D9F: FF              RST     0X38                
7DA0: FF              RST     0X38                
7DA1: FF              RST     0X38                
7DA2: FF              RST     0X38                
7DA3: FF              RST     0X38                
7DA4: FF              RST     0X38                
7DA5: FF              RST     0X38                
7DA6: FF              RST     0X38                
7DA7: FF              RST     0X38                
7DA8: FF              RST     0X38                
7DA9: FF              RST     0X38                
7DAA: FF              RST     0X38                
7DAB: FF              RST     0X38                
7DAC: FF              RST     0X38                
7DAD: FF              RST     0X38                
7DAE: FF              RST     0X38                
7DAF: FF              RST     0X38                
7DB0: FF              RST     0X38                
7DB1: FF              RST     0X38                
7DB2: FF              RST     0X38                
7DB3: FF              RST     0X38                
7DB4: FF              RST     0X38                
7DB5: FF              RST     0X38                
7DB6: FF              RST     0X38                
7DB7: FF              RST     0X38                
7DB8: FF              RST     0X38                
7DB9: FF              RST     0X38                
7DBA: FF              RST     0X38                
7DBB: FF              RST     0X38                
7DBC: FF              RST     0X38                
7DBD: FF              RST     0X38                
7DBE: FF              RST     0X38                
7DBF: FF              RST     0X38                
7DC0: FF              RST     0X38                
7DC1: FF              RST     0X38                
7DC2: FF              RST     0X38                
7DC3: FF              RST     0X38                
7DC4: FF              RST     0X38                
7DC5: FF              RST     0X38                
7DC6: FF              RST     0X38                
7DC7: FF              RST     0X38                
7DC8: FF              RST     0X38                
7DC9: FF              RST     0X38                
7DCA: FF              RST     0X38                
7DCB: FF              RST     0X38                
7DCC: FF              RST     0X38                
7DCD: FF              RST     0X38                
7DCE: FF              RST     0X38                
7DCF: FF              RST     0X38                
7DD0: FF              RST     0X38                
7DD1: FF              RST     0X38                
7DD2: FF              RST     0X38                
7DD3: FF              RST     0X38                
7DD4: FF              RST     0X38                
7DD5: FF              RST     0X38                
7DD6: FF              RST     0X38                
7DD7: FF              RST     0X38                
7DD8: FF              RST     0X38                
7DD9: FF              RST     0X38                
7DDA: FF              RST     0X38                
7DDB: FF              RST     0X38                
7DDC: FF              RST     0X38                
7DDD: FF              RST     0X38                
7DDE: FF              RST     0X38                
7DDF: FF              RST     0X38                
7DE0: FF              RST     0X38                
7DE1: FF              RST     0X38                
7DE2: FF              RST     0X38                
7DE3: FF              RST     0X38                
7DE4: FF              RST     0X38                
7DE5: FF              RST     0X38                
7DE6: FF              RST     0X38                
7DE7: FF              RST     0X38                
7DE8: FF              RST     0X38                
7DE9: FF              RST     0X38                
7DEA: FF              RST     0X38                
7DEB: FF              RST     0X38                
7DEC: FF              RST     0X38                
7DED: FF              RST     0X38                
7DEE: FF              RST     0X38                
7DEF: FF              RST     0X38                
7DF0: FF              RST     0X38                
7DF1: FF              RST     0X38                
7DF2: FF              RST     0X38                
7DF3: FF              RST     0X38                
7DF4: FF              RST     0X38                
7DF5: FF              RST     0X38                
7DF6: FF              RST     0X38                
7DF7: FF              RST     0X38                
7DF8: FF              RST     0X38                
7DF9: FF              RST     0X38                
7DFA: FF              RST     0X38                
7DFB: FF              RST     0X38                
7DFC: FF              RST     0X38                
7DFD: FF              RST     0X38                
7DFE: FF              RST     0X38                
7DFF: FF              RST     0X38                
7E00: FF              RST     0X38                
7E01: FF              RST     0X38                
7E02: FF              RST     0X38                
7E03: FF              RST     0X38                
7E04: FF              RST     0X38                
7E05: FF              RST     0X38                
7E06: FF              RST     0X38                
7E07: FF              RST     0X38                
7E08: FF              RST     0X38                
7E09: FF              RST     0X38                
7E0A: FF              RST     0X38                
7E0B: FF              RST     0X38                
7E0C: FF              RST     0X38                
7E0D: FF              RST     0X38                
7E0E: FF              RST     0X38                
7E0F: FF              RST     0X38                
7E10: FF              RST     0X38                
7E11: FF              RST     0X38                
7E12: FF              RST     0X38                
7E13: FF              RST     0X38                
7E14: FF              RST     0X38                
7E15: FF              RST     0X38                
7E16: FF              RST     0X38                
7E17: FF              RST     0X38                
7E18: FF              RST     0X38                
7E19: FF              RST     0X38                
7E1A: FF              RST     0X38                
7E1B: FF              RST     0X38                
7E1C: FF              RST     0X38                
7E1D: FF              RST     0X38                
7E1E: FF              RST     0X38                
7E1F: FF              RST     0X38                
7E20: FF              RST     0X38                
7E21: FF              RST     0X38                
7E22: FF              RST     0X38                
7E23: FF              RST     0X38                
7E24: FF              RST     0X38                
7E25: FF              RST     0X38                
7E26: FF              RST     0X38                
7E27: FF              RST     0X38                
7E28: FF              RST     0X38                
7E29: FF              RST     0X38                
7E2A: FF              RST     0X38                
7E2B: FF              RST     0X38                
7E2C: FF              RST     0X38                
7E2D: FF              RST     0X38                
7E2E: FF              RST     0X38                
7E2F: FF              RST     0X38                
7E30: FF              RST     0X38                
7E31: FF              RST     0X38                
7E32: FF              RST     0X38                
7E33: FF              RST     0X38                
7E34: FF              RST     0X38                
7E35: FF              RST     0X38                
7E36: FF              RST     0X38                
7E37: FF              RST     0X38                
7E38: FF              RST     0X38                
7E39: FF              RST     0X38                
7E3A: FF              RST     0X38                
7E3B: FF              RST     0X38                
7E3C: FF              RST     0X38                
7E3D: FF              RST     0X38                
7E3E: FF              RST     0X38                
7E3F: FF              RST     0X38                
7E40: FF              RST     0X38                
7E41: FF              RST     0X38                
7E42: FF              RST     0X38                
7E43: FF              RST     0X38                
7E44: FF              RST     0X38                
7E45: FF              RST     0X38                
7E46: FF              RST     0X38                
7E47: FF              RST     0X38                
7E48: FF              RST     0X38                
7E49: FF              RST     0X38                
7E4A: FF              RST     0X38                
7E4B: FF              RST     0X38                
7E4C: FF              RST     0X38                
7E4D: FF              RST     0X38                
7E4E: FF              RST     0X38                
7E4F: FF              RST     0X38                
7E50: FF              RST     0X38                
7E51: FF              RST     0X38                
7E52: FF              RST     0X38                
7E53: FF              RST     0X38                
7E54: FF              RST     0X38                
7E55: FF              RST     0X38                
7E56: FF              RST     0X38                
7E57: FF              RST     0X38                
7E58: FF              RST     0X38                
7E59: FF              RST     0X38                
7E5A: FF              RST     0X38                
7E5B: FF              RST     0X38                
7E5C: FF              RST     0X38                
7E5D: FF              RST     0X38                
7E5E: FF              RST     0X38                
7E5F: FF              RST     0X38                
7E60: FF              RST     0X38                
7E61: FF              RST     0X38                
7E62: FF              RST     0X38                
7E63: FF              RST     0X38                
7E64: FF              RST     0X38                
7E65: FF              RST     0X38                
7E66: FF              RST     0X38                
7E67: FF              RST     0X38                
7E68: FF              RST     0X38                
7E69: FF              RST     0X38                
7E6A: FF              RST     0X38                
7E6B: FF              RST     0X38                
7E6C: FF              RST     0X38                
7E6D: FF              RST     0X38                
7E6E: FF              RST     0X38                
7E6F: FF              RST     0X38                
7E70: FF              RST     0X38                
7E71: FF              RST     0X38                
7E72: FF              RST     0X38                
7E73: FF              RST     0X38                
7E74: FF              RST     0X38                
7E75: FF              RST     0X38                
7E76: FF              RST     0X38                
7E77: FF              RST     0X38                
7E78: FF              RST     0X38                
7E79: FF              RST     0X38                
7E7A: FF              RST     0X38                
7E7B: FF              RST     0X38                
7E7C: FF              RST     0X38                
7E7D: FF              RST     0X38                
7E7E: FF              RST     0X38                
7E7F: FF              RST     0X38                
7E80: FF              RST     0X38                
7E81: FF              RST     0X38                
7E82: FF              RST     0X38                
7E83: FF              RST     0X38                
7E84: FF              RST     0X38                
7E85: FF              RST     0X38                
7E86: FF              RST     0X38                
7E87: FF              RST     0X38                
7E88: FF              RST     0X38                
7E89: FF              RST     0X38                
7E8A: FF              RST     0X38                
7E8B: FF              RST     0X38                
7E8C: FF              RST     0X38                
7E8D: FF              RST     0X38                
7E8E: FF              RST     0X38                
7E8F: FF              RST     0X38                
7E90: FF              RST     0X38                
7E91: FF              RST     0X38                
7E92: FF              RST     0X38                
7E93: FF              RST     0X38                
7E94: FF              RST     0X38                
7E95: FF              RST     0X38                
7E96: FF              RST     0X38                
7E97: FF              RST     0X38                
7E98: FF              RST     0X38                
7E99: FF              RST     0X38                
7E9A: FF              RST     0X38                
7E9B: FF              RST     0X38                
7E9C: FF              RST     0X38                
7E9D: FF              RST     0X38                
7E9E: FF              RST     0X38                
7E9F: FF              RST     0X38                
7EA0: FF              RST     0X38                
7EA1: FF              RST     0X38                
7EA2: FF              RST     0X38                
7EA3: FF              RST     0X38                
7EA4: FF              RST     0X38                
7EA5: FF              RST     0X38                
7EA6: FF              RST     0X38                
7EA7: FF              RST     0X38                
7EA8: FF              RST     0X38                
7EA9: FF              RST     0X38                
7EAA: FF              RST     0X38                
7EAB: FF              RST     0X38                
7EAC: FF              RST     0X38                
7EAD: FF              RST     0X38                
7EAE: FF              RST     0X38                
7EAF: FF              RST     0X38                
7EB0: FF              RST     0X38                
7EB1: FF              RST     0X38                
7EB2: FF              RST     0X38                
7EB3: FF              RST     0X38                
7EB4: FF              RST     0X38                
7EB5: FF              RST     0X38                
7EB6: FF              RST     0X38                
7EB7: FF              RST     0X38                
7EB8: FF              RST     0X38                
7EB9: FF              RST     0X38                
7EBA: FF              RST     0X38                
7EBB: FF              RST     0X38                
7EBC: FF              RST     0X38                
7EBD: FF              RST     0X38                
7EBE: FF              RST     0X38                
7EBF: FF              RST     0X38                
7EC0: FF              RST     0X38                
7EC1: FF              RST     0X38                
7EC2: FF              RST     0X38                
7EC3: FF              RST     0X38                
7EC4: FF              RST     0X38                
7EC5: FF              RST     0X38                
7EC6: FF              RST     0X38                
7EC7: FF              RST     0X38                
7EC8: FF              RST     0X38                
7EC9: FF              RST     0X38                
7ECA: FF              RST     0X38                
7ECB: FF              RST     0X38                
7ECC: FF              RST     0X38                
7ECD: FF              RST     0X38                
7ECE: FF              RST     0X38                
7ECF: FF              RST     0X38                
7ED0: FF              RST     0X38                
7ED1: FF              RST     0X38                
7ED2: FF              RST     0X38                
7ED3: FF              RST     0X38                
7ED4: FF              RST     0X38                
7ED5: FF              RST     0X38                
7ED6: FF              RST     0X38                
7ED7: FF              RST     0X38                
7ED8: FF              RST     0X38                
7ED9: FF              RST     0X38                
7EDA: FF              RST     0X38                
7EDB: FF              RST     0X38                
7EDC: FF              RST     0X38                
7EDD: FF              RST     0X38                
7EDE: FF              RST     0X38                
7EDF: FF              RST     0X38                
7EE0: FF              RST     0X38                
7EE1: FF              RST     0X38                
7EE2: FF              RST     0X38                
7EE3: FF              RST     0X38                
7EE4: FF              RST     0X38                
7EE5: FF              RST     0X38                
7EE6: FF              RST     0X38                
7EE7: FF              RST     0X38                
7EE8: FF              RST     0X38                
7EE9: FF              RST     0X38                
7EEA: FF              RST     0X38                
7EEB: FF              RST     0X38                
7EEC: FF              RST     0X38                
7EED: FF              RST     0X38                
7EEE: FF              RST     0X38                
7EEF: FF              RST     0X38                
7EF0: FF              RST     0X38                
7EF1: FF              RST     0X38                
7EF2: FF              RST     0X38                
7EF3: FF              RST     0X38                
7EF4: FF              RST     0X38                
7EF5: FF              RST     0X38                
7EF6: FF              RST     0X38                
7EF7: FF              RST     0X38                
7EF8: FF              RST     0X38                
7EF9: FF              RST     0X38                
7EFA: FF              RST     0X38                
7EFB: FF              RST     0X38                
7EFC: FF              RST     0X38                
7EFD: FF              RST     0X38                
7EFE: FF              RST     0X38                
7EFF: FF              RST     0X38                
7F00: FF              RST     0X38                
7F01: FF              RST     0X38                
7F02: FF              RST     0X38                
7F03: FF              RST     0X38                
7F04: FF              RST     0X38                
7F05: FF              RST     0X38                
7F06: FF              RST     0X38                
7F07: FF              RST     0X38                
7F08: FF              RST     0X38                
7F09: FF              RST     0X38                
7F0A: FF              RST     0X38                
7F0B: FF              RST     0X38                
7F0C: FF              RST     0X38                
7F0D: FF              RST     0X38                
7F0E: FF              RST     0X38                
7F0F: FF              RST     0X38                
7F10: FF              RST     0X38                
7F11: FF              RST     0X38                
7F12: FF              RST     0X38                
7F13: FF              RST     0X38                
7F14: FF              RST     0X38                
7F15: FF              RST     0X38                
7F16: FF              RST     0X38                
7F17: FF              RST     0X38                
7F18: FF              RST     0X38                
7F19: FF              RST     0X38                
7F1A: FF              RST     0X38                
7F1B: FF              RST     0X38                
7F1C: FF              RST     0X38                
7F1D: FF              RST     0X38                
7F1E: FF              RST     0X38                
7F1F: FF              RST     0X38                
7F20: FF              RST     0X38                
7F21: FF              RST     0X38                
7F22: FF              RST     0X38                
7F23: FF              RST     0X38                
7F24: FF              RST     0X38                
7F25: FF              RST     0X38                
7F26: FF              RST     0X38                
7F27: FF              RST     0X38                
7F28: FF              RST     0X38                
7F29: FF              RST     0X38                
7F2A: FF              RST     0X38                
7F2B: FF              RST     0X38                
7F2C: FF              RST     0X38                
7F2D: FF              RST     0X38                
7F2E: FF              RST     0X38                
7F2F: FF              RST     0X38                
7F30: FF              RST     0X38                
7F31: FF              RST     0X38                
7F32: FF              RST     0X38                
7F33: FF              RST     0X38                
7F34: FF              RST     0X38                
7F35: FF              RST     0X38                
7F36: FF              RST     0X38                
7F37: FF              RST     0X38                
7F38: FF              RST     0X38                
7F39: FF              RST     0X38                
7F3A: FF              RST     0X38                
7F3B: FF              RST     0X38                
7F3C: FF              RST     0X38                
7F3D: FF              RST     0X38                
7F3E: FF              RST     0X38                
7F3F: FF              RST     0X38                
7F40: FF              RST     0X38                
7F41: FF              RST     0X38                
7F42: FF              RST     0X38                
7F43: FF              RST     0X38                
7F44: FF              RST     0X38                
7F45: FF              RST     0X38                
7F46: FF              RST     0X38                
7F47: FF              RST     0X38                
7F48: FF              RST     0X38                
7F49: FF              RST     0X38                
7F4A: FF              RST     0X38                
7F4B: FF              RST     0X38                
7F4C: FF              RST     0X38                
7F4D: FF              RST     0X38                
7F4E: FF              RST     0X38                
7F4F: FF              RST     0X38                
7F50: FF              RST     0X38                
7F51: FF              RST     0X38                
7F52: FF              RST     0X38                
7F53: FF              RST     0X38                
7F54: FF              RST     0X38                
7F55: FF              RST     0X38                
7F56: FF              RST     0X38                
7F57: FF              RST     0X38                
7F58: FF              RST     0X38                
7F59: FF              RST     0X38                
7F5A: FF              RST     0X38                
7F5B: FF              RST     0X38                
7F5C: FF              RST     0X38                
7F5D: FF              RST     0X38                
7F5E: FF              RST     0X38                
7F5F: FF              RST     0X38                
7F60: FF              RST     0X38                
7F61: FF              RST     0X38                
7F62: FF              RST     0X38                
7F63: FF              RST     0X38                
7F64: FF              RST     0X38                
7F65: FF              RST     0X38                
7F66: FF              RST     0X38                
7F67: FF              RST     0X38                
7F68: FF              RST     0X38                
7F69: FF              RST     0X38                
7F6A: FF              RST     0X38                
7F6B: FF              RST     0X38                
7F6C: FF              RST     0X38                
7F6D: FF              RST     0X38                
7F6E: FF              RST     0X38                
7F6F: FF              RST     0X38                
7F70: FF              RST     0X38                
7F71: FF              RST     0X38                
7F72: FF              RST     0X38                
7F73: FF              RST     0X38                
7F74: FF              RST     0X38                
7F75: FF              RST     0X38                
7F76: FF              RST     0X38                
7F77: FF              RST     0X38                
7F78: FF              RST     0X38                
7F79: FF              RST     0X38                
7F7A: FF              RST     0X38                
7F7B: FF              RST     0X38                
7F7C: FF              RST     0X38                
7F7D: FF              RST     0X38                
7F7E: FF              RST     0X38                
7F7F: FF              RST     0X38                
7F80: FF              RST     0X38                
7F81: FF              RST     0X38                
7F82: FF              RST     0X38                
7F83: FF              RST     0X38                
7F84: FF              RST     0X38                
7F85: FF              RST     0X38                
7F86: FF              RST     0X38                
7F87: FF              RST     0X38                
7F88: FF              RST     0X38                
7F89: FF              RST     0X38                
7F8A: FF              RST     0X38                
7F8B: FF              RST     0X38                
7F8C: FF              RST     0X38                
7F8D: FF              RST     0X38                
7F8E: FF              RST     0X38                
7F8F: FF              RST     0X38                
7F90: FF              RST     0X38                
7F91: FF              RST     0X38                
7F92: FF              RST     0X38                
7F93: FF              RST     0X38                
7F94: FF              RST     0X38                
7F95: FF              RST     0X38                
7F96: FF              RST     0X38                
7F97: FF              RST     0X38                
7F98: FF              RST     0X38                
7F99: FF              RST     0X38                
7F9A: FF              RST     0X38                
7F9B: FF              RST     0X38                
7F9C: FF              RST     0X38                
7F9D: FF              RST     0X38                
7F9E: FF              RST     0X38                
7F9F: FF              RST     0X38                
7FA0: FF              RST     0X38                
7FA1: FF              RST     0X38                
7FA2: FF              RST     0X38                
7FA3: FF              RST     0X38                
7FA4: FF              RST     0X38                
7FA5: FF              RST     0X38                
7FA6: FF              RST     0X38                
7FA7: FF              RST     0X38                
7FA8: FF              RST     0X38                
7FA9: FF              RST     0X38                
7FAA: FF              RST     0X38                
7FAB: FF              RST     0X38                
7FAC: FF              RST     0X38                
7FAD: FF              RST     0X38                
7FAE: FF              RST     0X38                
7FAF: FF              RST     0X38                
7FB0: FF              RST     0X38                
7FB1: FF              RST     0X38                
7FB2: FF              RST     0X38                
7FB3: FF              RST     0X38                
7FB4: FF              RST     0X38                
7FB5: FF              RST     0X38                
7FB6: FF              RST     0X38                
7FB7: FF              RST     0X38                
7FB8: FF              RST     0X38                
7FB9: FF              RST     0X38                
7FBA: FF              RST     0X38                
7FBB: FF              RST     0X38                
7FBC: FF              RST     0X38                
7FBD: FF              RST     0X38                
7FBE: FF              RST     0X38                
7FBF: FF              RST     0X38                
7FC0: FF              RST     0X38                
7FC1: FF              RST     0X38                
7FC2: FF              RST     0X38                
7FC3: FF              RST     0X38                
7FC4: FF              RST     0X38                
7FC5: FF              RST     0X38                
7FC6: FF              RST     0X38                
7FC7: FF              RST     0X38                
7FC8: FF              RST     0X38                
7FC9: FF              RST     0X38                
7FCA: FF              RST     0X38                
7FCB: FF              RST     0X38                
7FCC: FF              RST     0X38                
7FCD: FF              RST     0X38                
7FCE: FF              RST     0X38                
7FCF: FF              RST     0X38                
7FD0: FF              RST     0X38                
7FD1: FF              RST     0X38                
7FD2: FF              RST     0X38                
7FD3: FF              RST     0X38                
7FD4: FF              RST     0X38                
7FD5: FF              RST     0X38                
7FD6: FF              RST     0X38                
7FD7: FF              RST     0X38                
7FD8: FF              RST     0X38                
7FD9: FF              RST     0X38                
7FDA: FF              RST     0X38                
7FDB: FF              RST     0X38                
7FDC: FF              RST     0X38                
7FDD: FF              RST     0X38                
7FDE: FF              RST     0X38                
7FDF: FF              RST     0X38                
7FE0: FF              RST     0X38                
7FE1: FF              RST     0X38                
7FE2: FF              RST     0X38                
7FE3: FF              RST     0X38                
7FE4: FF              RST     0X38                
7FE5: FF              RST     0X38                
7FE6: FF              RST     0X38                
7FE7: FF              RST     0X38                
7FE8: FF              RST     0X38                
7FE9: FF              RST     0X38                
7FEA: FF              RST     0X38                
7FEB: FF              RST     0X38                
7FEC: FF              RST     0X38                
7FED: FF              RST     0X38                
7FEE: FF              RST     0X38                
7FEF: FF              RST     0X38                
7FF0: FF              RST     0X38                
7FF1: FF              RST     0X38                
7FF2: FF              RST     0X38                
7FF3: FF              RST     0X38                
7FF4: FF              RST     0X38                
7FF5: FF              RST     0X38                
7FF6: FF              RST     0X38                
7FF7: FF              RST     0X38                
7FF8: FF              RST     0X38                
7FF9: FF              RST     0X38                
7FFA: FF              RST     0X38                
7FFB: FF              RST     0X38                
7FFC: FF              RST     0X38                
7FFD: FF              RST     0X38                
7FFE: FF              RST     0X38                
7FFF: FF              RST     0X38                
```

