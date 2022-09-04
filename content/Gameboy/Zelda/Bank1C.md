![Bank 1C](GBZelda.jpg)

# Bank 1C

>>> cpu Z80GB

>>> binary 4000:roms/zelda.gb[70000:74000]

>>> memoryTable ram 

[RAM Usage](RAMUse.md)

>>> memoryTable hard 

[Hardware Info](../Hardware.md)

```code
4000: 01 00 5C        LD      BC,$5C00            
4003: 59              LD      E,C                 
4004: 5C              LD      E,H                 
4005: 1A              LD      A,(DE)              
4006: 5D              LD      E,L                 
4007: B9              CP      C                   
4008: 5D              LD      E,L                 
4009: 45              LD      B,L                 
400A: 5E              LD      E,(HL)              
400B: 93              SUB     E                   
400C: 5E              LD      E,(HL)              
400D: DA 5E 86        JP      C,$865E             
4010: 5F              LD      E,A                 
4011: C5              PUSH    BC                  
4012: 5F              LD      E,A                 
4013: 12              LD      (DE),A              
4014: 60              LD      H,B                 
4015: 72              LD      (HL),D              
4016: 60              LD      H,B                 
4017: 17              RLA                         
4018: 61              LD      H,C                 
4019: 64              LD      H,H                 
401A: 61              LD      H,C                 
401B: AC              XOR     H                   
401C: 61              LD      H,C                 
401D: FA 61 84        LD      A,($8461)           
4020: 62              LD      H,D                 
4021: EE 62           XOR     $62                 
4023: 3E 63           LD      A,$63               
4025: 6F              LD      L,A                 
4026: 63              LD      H,E                 
4027: 15              DEC     D                   
4028: 64              LD      H,H                 
4029: 71              LD      (HL),C              
402A: 64              LD      H,H                 
402B: D7              RST     0X10                
402C: 64              LD      H,H                 
402D: 11 65 7D        LD      DE,$7D65            
4030: 65              LD      H,L                 
4031: DA 65 19        JP      C,$1965             
4034: 66              LD      H,(HL)              
4035: 58              LD      E,B                 
4036: 66              LD      H,(HL)              
4037: 01 67 37        LD      BC,$3767            
403A: 67              LD      H,A                 
403B: 62              LD      H,D                 
403C: 67              LD      H,A                 
403D: BC              CP      H                   
403E: 67              LD      H,A                 
403F: F6 67           OR      $67                 
4041: 1E 68           LD      E,$68               
4043: 27              DAA                         
4044: 68              LD      L,B                 
4045: 68              LD      L,B                 
4046: 68              LD      L,B                 
4047: 81              ADD     A,C                 
4048: 68              LD      L,B                 
4049: 9A              SBC     D                   
404A: 68              LD      L,B                 
404B: F3              DI                          
404C: 68              LD      L,B                 
404D: 4F              LD      C,A                 
404E: 69              LD      L,C                 
404F: AB              XOR     E                   
4050: 69              LD      L,C                 
4051: 29              ADD     HL,HL               
4052: 6A              LD      L,D                 
4053: 80              ADD     A,B                 
4054: 6A              LD      L,D                 
4055: E1              POP     HL                  
4056: 6A              LD      L,D                 
4057: 2C              INC     L                   
4058: 6B              LD      L,E                 
4059: 2C              INC     L                   
405A: 6B              LD      L,E                 
405B: 5C              LD      E,H                 
405C: 6B              LD      L,E                 
405D: 8B              ADC     A,E                 
405E: 6B              LD      L,E                 
405F: CA 6B F7        JP      Z,$F76B             
4062: 6B              LD      L,E                 
4063: 38 6C           JR      C,$40D1             ; {}
4065: 67              LD      H,A                 
4066: 6C              LD      L,H                 
4067: 96              SUB     (HL)                
4068: 6C              LD      L,H                 
4069: C5              PUSH    BC                  
406A: 6C              LD      L,H                 
406B: 14              INC     D                   
406C: 6D              LD      L,L                 
406D: 34              INC     (HL)                
406E: 6D              LD      L,L                 
406F: 6E              LD      L,(HL)              
4070: 6D              LD      L,L                 
4071: 6E              LD      L,(HL)              
4072: 6D              LD      L,L                 
4073: B6              OR      (HL)                
4074: 6D              LD      L,L                 
4075: 06 6E           LD      B,$6E               
4077: 06 6E           LD      B,$6E               
4079: 32              LD      (HLD),A             
407A: 6E              LD      L,(HL)              
407B: 9D              SBC     L                   
407C: 6E              LD      L,(HL)              
407D: CC 6E E8        CALL    Z,$E86E             
4080: 6E              LD      L,(HL)              
4081: F3              DI                          
4082: 6E              LD      L,(HL)              
4083: 23              INC     HL                  
4084: 6F              LD      L,A                 
4085: 6B              LD      L,E                 
4086: 6F              LD      L,A                 
4087: AC              XOR     H                   
4088: 6F              LD      L,A                 
4089: 0B              DEC     BC                  
408A: 70              LD      (HL),B              
408B: 57              LD      D,A                 
408C: 70              LD      (HL),B              
408D: B8              CP      B                   
408E: 70              LD      (HL),B              
408F: E7              RST     0X20                
4090: 70              LD      (HL),B              
4091: 67              LD      H,A                 
4092: 71              LD      (HL),C              
4093: A8              XOR     B                   
4094: 71              LD      (HL),C              
4095: E9              JP      (HL)                
4096: 71              LD      (HL),C              
4097: 4A              LD      C,D                 
4098: 72              LD      (HL),D              
4099: 96              SUB     (HL)                
409A: 72              LD      (HL),D              
409B: C7              RST     0X00                
409C: 72              LD      (HL),D              
409D: 33              INC     SP                  
409E: 73              LD      (HL),E              
409F: A1              AND     C                   
40A0: 73              LD      (HL),E              
40A1: C2 73 13        JP      NZ,$1373            
40A4: 74              LD      (HL),H              
40A5: 49              LD      C,C                 
40A6: 74              LD      (HL),H              
40A7: 84              ADD     A,H                 
40A8: 74              LD      (HL),H              
40A9: CB 74           BIT     1,E                 
40AB: 88              ADC     A,B                 
40AC: 75              LD      (HL),L              
40AD: 38 76           JR      C,$4125             ; {}
40AF: 57              LD      D,A                 
40B0: 76              HALT                        
40B1: 78              LD      A,B                 
40B2: 76              HALT                        
40B3: 99              SBC     C                   
40B4: 76              HALT                        
40B5: BA              CP      D                   
40B6: 76              HALT                        
40B7: DB                              
40B8: 76              HALT                        
40B9: FC                              
40BA: 76              HALT                        
40BB: 1D              DEC     E                   
40BC: 77              LD      (HL),A              
40BD: 3E 77           LD      A,$77               
40BF: 4F              LD      C,A                 
40C0: 77              LD      (HL),A              
40C1: 4F              LD      C,A                 
40C2: 77              LD      (HL),A              
40C3: 60              LD      H,B                 
40C4: 77              LD      (HL),A              
40C5: 7C              LD      A,H                 
40C6: 77              LD      (HL),A              
40C7: 8A              ADC     A,D                 
40C8: 77              LD      (HL),A              
40C9: A7              AND     A                   
40CA: 77              LD      (HL),A              
40CB: B6              OR      (HL)                
40CC: 77              LD      (HL),A              
40CD: C7              RST     0X00                
40CE: 77              LD      (HL),A              
40CF: E8 77           ADD     SP,$77              
40D1: F7              RST     0X30                
40D2: 77              LD      (HL),A              
40D3: 06 78           LD      B,$78               
40D5: 16 78           LD      D,$78               
40D7: 27              DAA                         
40D8: 78              LD      A,B                 
40D9: 38 78           JR      C,$4153             ; {}
40DB: 59              LD      E,C                 
40DC: 78              LD      A,B                 
40DD: 6A              LD      L,D                 
40DE: 78              LD      A,B                 
40DF: 7B              LD      A,E                 
40E0: 78              LD      A,B                 
40E1: 8C              ADC     A,H                 
40E2: 78              LD      A,B                 
40E3: 9D              SBC     L                   
40E4: 78              LD      A,B                 
40E5: AE              XOR     (HL)                
40E6: 78              LD      A,B                 
40E7: BF              CP      A                   
40E8: 78              LD      A,B                 
40E9: CF              RST     0X08                
40EA: 78              LD      A,B                 
40EB: DE 78           SBC     $78                 
40ED: EE 78           XOR     $78                 
40EF: FE 78           CP      $78                 
40F1: 0E 79           LD      C,$79               
40F3: 1E 79           LD      E,$79               
40F5: 2E 79           LD      L,$79               
40F7: 3F              CCF                         
40F8: 79              LD      A,C                 
40F9: 5B              LD      E,E                 
40FA: 79              LD      A,C                 
40FB: 6C              LD      L,H                 
40FC: 79              LD      A,C                 
40FD: 9C              SBC     H                   
40FE: 79              LD      A,C                 
40FF: BD              CP      L                   
4100: 79              LD      A,C                 
4101: 00              NOP                         
4102: 57              LD      D,A                 
4103: 1D              DEC     E                   
4104: 57              LD      D,A                 
4105: 39              ADD     HL,SP               
4106: 57              LD      D,A                 
4107: 4A              LD      C,D                 
4108: 57              LD      D,A                 
4109: 5B              LD      E,E                 
410A: 57              LD      D,A                 
410B: 6C              LD      L,H                 
410C: 57              LD      D,A                 
410D: 7D              LD      A,L                 
410E: 57              LD      D,A                 
410F: 8E              ADC     A,(HL)              
4110: 57              LD      D,A                 
4111: 9F              SBC     A                   
4112: 57              LD      D,A                 
4113: B0              OR      B                   
4114: 57              LD      D,A                 
4115: C1              POP     BC                  
4116: 57              LD      D,A                 
4117: 0F              RRCA                        
4118: 58              LD      E,B                 
4119: 59              LD      E,C                 
411A: 58              LD      E,B                 
411B: 9A              SBC     D                   
411C: 58              LD      E,B                 
411D: F8 58           LD      HL,SP+$58           
411F: 36 59           LD      (HL),$59            
4121: 57              LD      D,A                 
4122: 59              LD      E,C                 
4123: 9F              SBC     A                   
4124: 59              LD      E,C                 
4125: E0 59           LD      ($FF00+$59),A       
4127: A1              AND     C                   
4128: 5A              LD      E,D                 
4129: E9              JP      (HL)                
412A: 5A              LD      E,D                 
412B: 3A              LD      A,(HLD)             
412C: 5B              LD      E,E                 
412D: 84              ADD     A,H                 
412E: 5B              LD      E,E                 
412F: C5              PUSH    BC                  
4130: 5B              LD      E,E                 
4131: 12              LD      (DE),A              
4132: 5C              LD      E,H                 
4133: 4E              LD      C,(HL)              
4134: 5C              LD      E,H                 
4135: 99              SBC     C                   
4136: 5C              LD      E,H                 
4137: 99              SBC     C                   
4138: 5C              LD      E,H                 
4139: E9              JP      (HL)                
413A: 5C              LD      E,H                 
413B: 4A              LD      C,D                 
413C: 5D              LD      E,L                 
413D: A2              AND     D                   
413E: 5D              LD      E,L                 
413F: A2              AND     D                   
4140: 5D              LD      E,L                 
4141: E8 5D           ADD     SP,$5D              
4143: E8 5D           ADD     SP,$5D              
4145: 28 5E           JR      Z,$41A5             ; {}
4147: 71              LD      (HL),C              
4148: 5E              LD      E,(HL)              
4149: 8D              ADC     A,L                 
414A: 5E              LD      E,(HL)              
414B: A7              AND     A                   
414C: 5E              LD      E,(HL)              
414D: C1              POP     BC                  
414E: 5E              LD      E,(HL)              
414F: 00              NOP                         
4150: 5F              LD      E,A                 
4151: C1              POP     BC                  
4152: 5F              LD      E,A                 
4153: 17              RLA                         
4154: 60              LD      H,B                 
4155: 6D              LD      L,L                 
4156: 60              LD      H,B                 
4157: A3              AND     E                   
4158: 60              LD      H,B                 
4159: CE 60           ADC     $60                 
415B: FD                              
415C: 60              LD      H,B                 
415D: 2D              DEC     L                   
415E: 61              LD      H,C                 
415F: 5E              LD      E,(HL)              
4160: 61              LD      H,C                 
4161: AB              XOR     E                   
4162: 61              LD      H,C                 
4163: CC 61 FC        CALL    Z,$FC61             
4166: 61              LD      H,C                 
4167: 3C              INC     A                   
4168: 62              LD      H,D                 
4169: 9D              SBC     L                   
416A: 62              LD      H,D                 
416B: D7              RST     0X10                
416C: 62              LD      H,D                 
416D: 55              LD      D,L                 
416E: 63              LD      H,E                 
416F: B3              OR      E                   
4170: 63              LD      H,E                 
4171: 2F              CPL                         
4172: 64              LD      H,H                 
4173: 2F              CPL                         
4174: 64              LD      H,H                 
4175: AE              XOR     (HL)                
4176: 64              LD      H,H                 
4177: 05              DEC     B                   
4178: 65              LD      H,L                 
4179: 05              DEC     B                   
417A: 65              LD      H,L                 
417B: 62              LD      H,D                 
417C: 65              LD      H,L                 
417D: 12              LD      (DE),A              
417E: 66              LD      H,(HL)              
417F: 12              LD      (DE),A              
4180: 66              LD      H,(HL)              
4181: 12              LD      (DE),A              
4182: 66              LD      H,(HL)              
4183: C3 67 54        JP      $5467               ; {}
4186: 68              LD      L,B                 
4187: B2              OR      D                   
4188: 69              LD      L,C                 
4189: 21 6A F2        LD      HL,$F26A            
418C: 6A              LD      L,D                 
418D: 32              LD      (HLD),A             
418E: 6C              LD      L,H                 
418F: D3                              
4190: 6C              LD      L,H                 
4191: 81              ADD     A,C                 
4192: 6D              LD      L,L                 
4193: 02              LD      (BC),A              
4194: 6F              LD      L,A                 
4195: FE 6F           CP      $6F                 
4197: CE 70           ADC     $70                 
4199: BD              CP      L                   
419A: 71              LD      (HL),C              
419B: FD                              
419C: 72              LD      (HL),D              
419D: 49              LD      C,C                 
419E: 73              LD      (HL),E              
419F: 49              LD      C,C                 
41A0: 73              LD      (HL),E              
41A1: 5A              LD      E,D                 
41A2: 75              LD      (HL),L              
41A3: 88              ADC     A,B                 
41A4: 77              LD      (HL),A              
41A5: 88              ADC     A,B                 
41A6: 77              LD      (HL),A              
41A7: C7              RST     0X00                
41A8: 77              LD      (HL),A              
41A9: C7              RST     0X00                
41AA: 77              LD      (HL),A              
41AB: C7              RST     0X00                
41AC: 77              LD      (HL),A              
41AD: D8              RET     C                   
41AE: 77              LD      (HL),A              
41AF: D8              RET     C                   
41B0: 77              LD      (HL),A              
41B1: 24              INC     H                   
41B2: 78              LD      A,B                 
41B3: 6E              LD      L,(HL)              
41B4: 78              LD      A,B                 
41B5: CC 79 F8        CALL    Z,$F879             
41B8: 79              LD      A,C                 
41B9: 78              LD      A,B                 
41BA: 7A              LD      A,D                 
41BB: 77              LD      (HL),A              
41BC: 7B              LD      A,E                 
41BD: A6              AND     (HL)                
41BE: 7B              LD      A,E                 
41BF: DC 7B 4D        CALL    C,$4D7B             ; {}
41C2: 7C              LD      A,H                 
41C3: 99              SBC     C                   
41C4: 7C              LD      A,H                 
41C5: 17              RLA                         
41C6: 7D              LD      A,L                 
41C7: 65              LD      H,L                 
41C8: 7D              LD      A,L                 
41C9: B3              OR      E                   
41CA: 7D              LD      A,L                 
41CB: 01 7E 70        LD      BC,$707E            
41CE: 7E              LD      A,(HL)              
41CF: D0              RET     NC                  
41D0: 7E              LD      A,(HL)              
41D1: 00              NOP                         
41D2: 67              LD      H,A                 
41D3: 50              LD      D,B                 
41D4: 67              LD      H,A                 
41D5: AC              XOR     H                   
41D6: 67              LD      H,A                 
41D7: AC              XOR     H                   
41D8: 67              LD      H,A                 
41D9: AC              XOR     H                   
41DA: 67              LD      H,A                 
41DB: FA 67 58        LD      A,($5867)           ; {}
41DE: 68              LD      L,B                 
41DF: A6              AND     (HL)                
41E0: 68              LD      L,B                 
41E1: 0E 69           LD      C,$69               
41E3: 4E              LD      C,(HL)              
41E4: 69              LD      L,C                 
41E5: 7F              LD      A,A                 
41E6: 69              LD      L,C                 
41E7: 9A              SBC     D                   
41E8: 69              LD      L,C                 
41E9: B5              OR      L                   
41EA: 69              LD      L,C                 
41EB: D5              PUSH    DE                  
41EC: 69              LD      L,C                 
41ED: 13              INC     DE                  
41EE: 6B              LD      L,E                 
41EF: 84              ADD     A,H                 
41F0: 6B              LD      L,E                 
41F1: C4 6B 02        CALL    NZ,$026B            
41F4: 6C              LD      L,H                 
41F5: 73              LD      (HL),E              
41F6: 6C              LD      L,H                 
41F7: 7C              LD      A,H                 
41F8: 6C              LD      L,H                 
41F9: 85              ADD     A,L                 
41FA: 6C              LD      L,H                 
41FB: BB              CP      E                   
41FC: 6C              LD      L,H                 
41FD: F2                              
41FE: 6C              LD      L,H                 
41FF: 51              LD      D,C                 
4200: 6D              LD      L,L                 
4201: 00              NOP                         
4202: 4A              LD      C,D                 
4203: 21 4A 3D        LD      HL,$3D4A            
4206: 4A              LD      C,D                 
4207: 5E              LD      E,(HL)              
4208: 4A              LD      C,D                 
4209: 79              LD      A,C                 
420A: 4A              LD      C,D                 
420B: 97              SUB     A                   
420C: 4A              LD      C,D                 
420D: B7              OR      A                   
420E: 4A              LD      C,D                 
420F: E7              RST     0X20                
4210: 4A              LD      C,D                 
4211: 05              DEC     B                   
4212: 4B              LD      C,E                 
4213: 31 4B 73        LD      SP,$734B            
4216: 4B              LD      C,E                 
4217: A1              AND     C                   
4218: 4B              LD      C,E                 
4219: CF              RST     0X08                
421A: 4B              LD      C,E                 
421B: FB              EI                          
421C: 4B              LD      C,E                 
421D: 29              ADD     HL,HL               
421E: 4C              LD      C,H                 
421F: 57              LD      D,A                 
4220: 4C              LD      C,H                 
4221: 9C              SBC     H                   
4222: 4C              LD      C,H                 
4223: FB              EI                          
4224: 4C              LD      C,H                 
4225: 4B              LD      C,E                 
4226: 4D              LD      C,L                 
4227: 8B              ADC     A,E                 
4228: 4D              LD      C,L                 
4229: B7              OR      A                   
422A: 4D              LD      C,L                 
422B: 0E 4E           LD      C,$4E               
422D: 1F              RRA                         
422E: 4E              LD      C,(HL)              
422F: 57              LD      D,A                 
4230: 4E              LD      C,(HL)              
4231: 57              LD      D,A                 
4232: 4E              LD      C,(HL)              
4233: D7              RST     0X10                
4234: 4E              LD      C,(HL)              
4235: 6E              LD      L,(HL)              
4236: 4F              LD      C,A                 
4237: E6 4F           AND     $4F                 
4239: 5B              LD      E,E                 
423A: 50              LD      D,B                 
423B: AB              XOR     E                   
423C: 50              LD      D,B                 
423D: 17              RLA                         
423E: 51              LD      D,C                 
423F: 96              SUB     (HL)                
4240: 51              LD      D,C                 
4241: 2C              INC     L                   
4242: 52              LD      D,D                 
4243: 90              SUB     B                   
4244: 52              LD      D,D                 
4245: F0 52           LD      A,($52)             
4247: 85              ADD     A,L                 
4248: 53              LD      D,E                 
4249: BA              CP      D                   
424A: 53              LD      D,E                 
424B: BA              CP      D                   
424C: 53              LD      D,E                 
424D: BA              CP      D                   
424E: 53              LD      D,E                 
424F: BA              CP      D                   
4250: 53              LD      D,E                 
4251: D5              PUSH    DE                  
4252: 53              LD      D,E                 
4253: 2D              DEC     L                   
4254: 54              LD      D,H                 
4255: 7D              LD      A,L                 
4256: 54              LD      D,H                 
4257: 2D              DEC     L                   
4258: 55              LD      D,L                 
4259: 69              LD      L,C                 
425A: 55              LD      D,L                 
425B: AA              XOR     D                   
425C: 55              LD      D,L                 
425D: 34              INC     (HL)                
425E: 56              LD      D,(HL)              
425F: 34              INC     (HL)                
4260: 56              LD      D,(HL)              
4261: 0F              RRCA                        
4262: 57              LD      D,A                 
4263: 4E              LD      C,(HL)              
4264: 57              LD      D,A                 
4265: D7              RST     0X10                
4266: 57              LD      D,A                 
4267: 77              LD      (HL),A              
4268: 58              LD      E,B                 
4269: 15              DEC     D                   
426A: 59              LD      E,C                 
426B: 73              LD      (HL),E              
426C: 59              LD      E,C                 
426D: 22              LD      (HLI),A             
426E: 5A              LD      E,D                 
426F: 70              LD      (HL),B              
4270: 5A              LD      E,D                 
4271: B0              OR      B                   
4272: 5A              LD      E,D                 
4273: DF              RST     0X18                
4274: 5A              LD      E,D                 
4275: 0E 5B           LD      C,$5B               
4277: 8E              ADC     A,(HL)              
4278: 5C              LD      E,H                 
4279: 34              INC     (HL)                
427A: 5D              LD      E,L                 
427B: 92              SUB     D                   
427C: 5D              LD      E,L                 
427D: 0A              LD      A,(BC)              
427E: 5E              LD      E,(HL)              
427F: 47              LD      B,A                 
4280: 5E              LD      E,(HL)              
4281: A7              AND     A                   
4282: 5E              LD      E,(HL)              
4283: 24              INC     H                   
4284: 5F              LD      E,A                 
4285: A1              AND     C                   
4286: 5F              LD      E,A                 
4287: 62              LD      H,D                 
4288: 60              LD      H,B                 
4289: 22              LD      (HLI),A             
428A: 61              LD      H,C                 
428B: 10 62           ;;STOP    $62                 
428D: 8E              ADC     A,(HL)              
428E: 62              LD      H,D                 
428F: 26 63           LD      H,$63               
4291: E7              RST     0X20                
4292: 63              LD      H,E                 
4293: 6F              LD      L,A                 
4294: 64              LD      H,H                 
4295: F7              RST     0X30                
4296: 64              LD      H,H                 
4297: D4 65 61        CALL    NC,$6165            ; {}
429A: 66              LD      H,(HL)              
429B: DF              RST     0X18                
429C: 66              LD      H,(HL)              
429D: 6F              LD      L,A                 
429E: 67              LD      H,A                 
429F: 80              ADD     A,B                 
42A0: 68              LD      L,B                 
42A1: 0E 69           LD      C,$69               
42A3: 3F              CCF                         
42A4: 69              LD      L,C                 
42A5: 7F              LD      A,A                 
42A6: 69              LD      L,C                 
42A7: B0              OR      B                   
42A8: 69              LD      L,C                 
42A9: E1              POP     HL                  
42AA: 69              LD      L,C                 
42AB: 12              LD      (DE),A              
42AC: 6A              LD      L,D                 
42AD: 51              LD      D,C                 
42AE: 6A              LD      L,D                 
42AF: 82              ADD     A,D                 
42B0: 6A              LD      L,D                 
42B1: B2              OR      D                   
42B2: 6A              LD      L,D                 
42B3: B2              OR      D                   
42B4: 6A              LD      L,D                 
42B5: CE 6A           ADC     $6A                 
42B7: EE 6A           XOR     $6A                 
42B9: 2D              DEC     L                   
42BA: 6B              LD      L,E                 
42BB: 79              LD      A,C                 
42BC: 6B              LD      L,E                 
42BD: D9              RETI                        
42BE: 6B              LD      L,E                 
42BF: 26 6C           LD      H,$6C               
42C1: 46              LD      B,(HL)              
42C2: 6C              LD      L,H                 
42C3: 75              LD      (HL),L              
42C4: 6C              LD      L,H                 
42C5: B6              OR      (HL)                
42C6: 6C              LD      L,H                 
42C7: F7              RST     0X30                
42C8: 6C              LD      L,H                 
42C9: 24              INC     H                   
42CA: 6D              LD      L,L                 
42CB: 61              LD      H,C                 
42CC: 6D              LD      L,L                 
42CD: 9E              SBC     (HL)                
42CE: 6D              LD      L,L                 
42CF: 7A              LD      A,D                 
42D0: 6E              LD      L,(HL)              
42D1: 06 6F           LD      B,$6F               
42D3: 76              HALT                        
42D4: 6F              LD      L,A                 
42D5: B3              OR      E                   
42D6: 6F              LD      L,A                 
42D7: E2              LD      (C),A               
42D8: 6F              LD      L,A                 
42D9: 70              LD      (HL),B              
42DA: 70              LD      (HL),B              
42DB: A0              AND     B                   
42DC: 70              LD      (HL),B              
42DD: 00              NOP                         
42DE: 00              NOP                         
42DF: 00              NOP                         
42E0: 00              NOP                         
42E1: DA 70 58        JP      C,$5870             ; {}
42E4: 71              LD      (HL),C              
42E5: 72              LD      (HL),D              
42E6: 71              LD      (HL),C              
42E7: C0              RET     NZ                  
42E8: 71              LD      (HL),C              
42E9: 11 72 2C        LD      DE,$2C72            
42EC: 72              LD      (HL),D              
42ED: 59              LD      E,C                 
42EE: 72              LD      (HL),D              
42EF: 77              LD      (HL),A              
42F0: 72              LD      (HL),D              
42F1: F6 72           OR      $72                 
42F3: 60              LD      H,B                 
42F4: 73              LD      (HL),E              
42F5: 60              LD      H,B                 
42F6: 73              LD      (HL),E              
42F7: 60              LD      H,B                 
42F8: 73              LD      (HL),E              
42F9: 60              LD      H,B                 
42FA: 73              LD      (HL),E              
42FB: 60              LD      H,B                 
42FC: 73              LD      (HL),E              
42FD: 60              LD      H,B                 
42FE: 73              LD      (HL),E              
42FF: 60              LD      H,B                 
4300: 73              LD      (HL),E              
4301: 00              NOP                         
4302: 40              LD      B,B                 
4303: 61              LD      H,C                 
4304: 40              LD      B,B                 
4305: 0E 41           LD      C,$41               
4307: 3D              DEC     A                   
4308: 41              LD      B,C                 
4309: 65              LD      H,L                 
430A: 41              LD      B,C                 
430B: 95              SUB     L                   
430C: 41              LD      B,C                 
430D: E1              POP     HL                  
430E: 41              LD      B,C                 
430F: 02              LD      (BC),A              
4310: 42              LD      B,D                 
4311: 2F              CPL                         
4312: 42              LD      B,D                 
4313: 78              LD      A,B                 
4314: 42              LD      B,D                 
4315: 05              DEC     B                   
4316: 43              LD      B,E                 
4317: 35              DEC     (HL)                
4318: 43              LD      B,E                 
4319: C2 43 49        JP      NZ,$4943            ; {}
431C: 44              LD      B,H                 
431D: 83              ADD     A,E                 
431E: 44              LD      B,H                 
431F: A3              AND     E                   
4320: 44              LD      B,H                 
4321: A3              AND     E                   
4322: 44              LD      B,H                 
4323: F2                              
4324: 44              LD      B,H                 
4325: 71              LD      (HL),C              
4326: 45              LD      B,L                 
4327: 20 46           JR      NZ,$436F            ; {}
4329: 50              LD      D,B                 
432A: 46              LD      B,(HL)              
432B: F1              POP     AF                  
432C: 46              LD      B,(HL)              
432D: 86              ADD     A,(HL)              
432E: 47              LD      B,A                 
432F: C7              RST     0X00                
4330: 47              LD      B,A                 
4331: 52              LD      D,D                 
4332: 48              LD      C,B                 
4333: B3              OR      E                   
4334: 48              LD      C,B                 
4335: DA 48 1B        JP      C,$1B48             
4338: 49              LD      C,C                 
4339: D3                              
433A: 49              LD      C,C                 
433B: 1E 4A           LD      E,$4A               
433D: 2F              CPL                         
433E: 4A              LD      C,D                 
433F: 50              LD      D,B                 
4340: 4A              LD      C,D                 
4341: 50              LD      D,B                 
4342: 4A              LD      C,D                 
4343: 91              SUB     C                   
4344: 4A              LD      C,D                 
4345: EF              RST     0X28                
4346: 4A              LD      C,D                 
4347: 30 4B           JR      NC,$4394            ; {}
4349: 41              LD      B,C                 
434A: 4B              LD      C,E                 
434B: 62              LD      H,D                 
434C: 4B              LD      C,E                 
434D: 8B              ADC     A,E                 
434E: 4B              LD      C,E                 
434F: D4 4B E5        CALL    NC,$E54B            
4352: 4B              LD      C,E                 
4353: 15              DEC     D                   
4354: 4C              LD      C,H                 
4355: 23              INC     HL                  
4356: 4C              LD      C,H                 
4357: 31 4C 3F        LD      SP,$3F4C            
435A: 4C              LD      C,H                 
435B: 4D              LD      C,L                 
435C: 4C              LD      C,H                 
435D: 6A              LD      L,D                 
435E: 4C              LD      C,H                 
435F: 99              SBC     C                   
4360: 4C              LD      C,H                 
4361: B7              OR      A                   
4362: 4C              LD      C,H                 
4363: D6 4C           SUB     $4C                 
4365: F5              PUSH    AF                  
4366: 4C              LD      C,H                 
4367: 16 4D           LD      D,$4D               
4369: 37              SCF                         
436A: 4D              LD      C,L                 
436B: 47              LD      B,A                 
436C: 4D              LD      C,L                 
436D: 68              LD      L,B                 
436E: 4D              LD      C,L                 
436F: 99              SBC     C                   
4370: 4D              LD      C,L                 
4371: C8              RET     Z                   
4372: 4D              LD      C,L                 
4373: F6 4D           OR      $4D                 
4375: 24              INC     H                   
4376: 4E              LD      C,(HL)              
4377: 45              LD      B,L                 
4378: 4E              LD      C,(HL)              
4379: 76              HALT                        
437A: 4E              LD      C,(HL)              
437B: A2              AND     D                   
437C: 4E              LD      C,(HL)              
437D: DA 4E 23        JP      C,$234E             
4380: 4F              LD      C,A                 
4381: 23              INC     HL                  
4382: 4F              LD      C,A                 
4383: 82              ADD     A,D                 
4384: 4F              LD      C,A                 
4385: CF              RST     0X08                
4386: 4F              LD      C,A                 
4387: E9              JP      (HL)                
4388: 4F              LD      C,A                 
4389: 2A              LD      A,(HLI)             
438A: 50              LD      D,B                 
438B: 2A              LD      A,(HLI)             
438C: 50              LD      D,B                 
438D: B4              OR      H                   
438E: 50              LD      D,B                 
438F: 80              ADD     A,B                 
4390: 51              LD      D,C                 
4391: 0F              RRCA                        
4392: 52              LD      D,D                 
4393: 2F              CPL                         
4394: 52              LD      D,D                 
4395: 8E              ADC     A,(HL)              
4396: 52              LD      D,D                 
4397: FE 52           CP      $52                 
4399: 39              ADD     HL,SP               
439A: 53              LD      D,E                 
439B: 59              LD      E,C                 
439C: 53              LD      D,E                 
439D: CA 53 2A        JP      Z,$2A53             
43A0: 54              LD      D,H                 
43A1: 96              SUB     (HL)                
43A2: 54              LD      D,H                 
43A3: D7              RST     0X10                
43A4: 54              LD      D,H                 
43A5: 21 55 3E        LD      HL,$3E55            
43A8: 56              LD      D,(HL)              
43A9: 77              LD      (HL),A              
43AA: 56              LD      D,(HL)              
43AB: D0              RET     NC                  
43AC: 56              LD      D,(HL)              
43AD: 3F              CCF                         
43AE: 57              LD      D,A                 
43AF: 6E              LD      L,(HL)              
43B0: 57              LD      D,A                 
43B1: 88              ADC     A,B                 
43B2: 57              LD      D,A                 
43B3: 93              SUB     E                   
43B4: 58              LD      E,B                 
43B5: 73              LD      (HL),E              
43B6: 59              LD      E,C                 
43B7: C2 59 FF        JP      NZ,$FF59            
43BA: 59              LD      E,C                 
43BB: 5D              LD      E,L                 
43BC: 5A              LD      E,D                 
43BD: A4              AND     H                   
43BE: 5A              LD      E,D                 
43BF: F3              DI                          
43C0: 5A              LD      E,D                 
43C1: F3              DI                          
43C2: 5A              LD      E,D                 
43C3: 14              INC     D                   
43C4: 5B              LD      E,E                 
43C5: 73              LD      (HL),E              
43C6: 5B              LD      E,E                 
43C7: AA              XOR     D                   
43C8: 5B              LD      E,E                 
43C9: EB                              
43CA: 5B              LD      E,E                 
43CB: 3C              INC     A                   
43CC: 5C              LD      E,H                 
43CD: 7B              LD      A,E                 
43CE: 5C              LD      E,H                 
43CF: A6              AND     (HL)                
43D0: 5C              LD      E,H                 
43D1: 46              LD      B,(HL)              
43D2: 5D              LD      E,L                 
43D3: F2                              
43D4: 5D              LD      E,L                 
43D5: 31 5E 6F        LD      SP,$6F5E            
43D8: 5E              LD      E,(HL)              
43D9: A0              AND     B                   
43DA: 5E              LD      E,(HL)              
43DB: CB 5E           BIT     1,E                 
43DD: F7              RST     0X30                
43DE: 5E              LD      E,(HL)              
43DF: F7              RST     0X30                
43E0: 5E              LD      E,(HL)              
43E1: F7              RST     0X30                
43E2: 5E              LD      E,(HL)              
43E3: 98              SBC     B                   
43E4: 5F              LD      E,A                 
43E5: BE              CP      (HL)                
43E6: 5F              LD      E,A                 
43E7: 2C              INC     L                   
43E8: 60              LD      H,B                 
43E9: 4B              LD      C,E                 
43EA: 60              LD      H,B                 
43EB: 6B              LD      L,E                 
43EC: 60              LD      H,B                 
43ED: C9              RET                         
43EE: 60              LD      H,B                 
43EF: C9              RET                         
43F0: 60              LD      H,B                 
43F1: 45              LD      B,L                 
43F2: 61              LD      H,C                 
43F3: 45              LD      B,L                 
43F4: 61              LD      H,C                 
43F5: 56              LD      D,(HL)              
43F6: 61              LD      H,C                 
43F7: 72              LD      (HL),D              
43F8: 61              LD      H,C                 
43F9: 8B              ADC     A,E                 
43FA: 61              LD      H,C                 
43FB: A6              AND     (HL)                
43FC: 61              LD      H,C                 
43FD: 40              LD      B,B                 
43FE: 62              LD      H,D                 
43FF: BC              CP      H                   
4400: 62              LD      H,D                 
4401: 78              LD      A,B                 
4402: 63              LD      H,E                 
4403: C7              RST     0X00                
4404: 63              LD      H,E                 
4405: 97              SUB     A                   
4406: 64              LD      H,H                 
4407: E6 64           AND     $64                 
4409: A6              AND     (HL)                
440A: 65              LD      H,L                 
440B: E5              PUSH    HL                  
440C: 65              LD      H,L                 
440D: F5              PUSH    AF                  
440E: 66              LD      H,(HL)              
440F: 34              INC     (HL)                
4410: 67              LD      H,A                 
4411: 32              LD      (HLD),A             
4412: 68              LD      L,B                 
4413: 71              LD      (HL),C              
4414: 68              LD      L,B                 
4415: 7E              LD      A,(HL)              
4416: 69              LD      L,C                 
4417: AD              XOR     L                   
4418: 69              LD      L,C                 
4419: 59              LD      E,C                 
441A: 6A              LD      L,D                 
441B: E8 6A           ADD     SP,$6A              
441D: 46              LD      B,(HL)              
441E: 6B              LD      L,E                 
441F: AF              XOR     A                   
4420: 6B              LD      L,E                 
4421: AF              XOR     A                   
4422: 6B              LD      L,E                 
4423: DE 6B           SBC     $6B                 
4425: 1F              RRA                         
4426: 6C              LD      L,H                 
4427: 3F              CCF                         
4428: 6C              LD      L,H                 
4429: 6F              LD      L,A                 
442A: 6C              LD      L,H                 
442B: 9E              SBC     (HL)                
442C: 6C              LD      L,H                 
442D: DE 6C           SBC     $6C                 
442F: 2E 6D           LD      L,$6D               
4431: 9C              SBC     H                   
4432: 6D              LD      L,L                 
4433: 0A              LD      A,(BC)              
4434: 6E              LD      L,(HL)              
4435: 78              LD      A,B                 
4436: 6E              LD      L,(HL)              
4437: E6 6E           AND     $6E                 
4439: 17              RLA                         
443A: 6F              LD      L,A                 
443B: 51              LD      D,C                 
443C: 6F              LD      L,A                 
443D: 77              LD      (HL),A              
443E: 6F              LD      L,A                 
443F: D6 6F           SUB     $6F                 
4441: D6 6F           SUB     $6F                 
4443: 85              ADD     A,L                 
4444: 71              LD      (HL),C              
4445: 01 72 52        LD      BC,$5272            
4448: 72              LD      (HL),D              
4449: 72              LD      (HL),D              
444A: 72              LD      (HL),D              
444B: B0              OR      B                   
444C: 72              LD      (HL),D              
444D: 11 73 4C        LD      DE,$4C73            
4450: 73              LD      (HL),E              
4451: 88              ADC     A,B                 
4452: 73              LD      (HL),E              
4453: 88              ADC     A,B                 
4454: 73              LD      (HL),E              
4455: 88              ADC     A,B                 
4456: 73              LD      (HL),E              
4457: 88              ADC     A,B                 
4458: 73              LD      (HL),E              
4459: 88              ADC     A,B                 
445A: 73              LD      (HL),E              
445B: 88              ADC     A,B                 
445C: 73              LD      (HL),E              
445D: 88              ADC     A,B                 
445E: 73              LD      (HL),E              
445F: 88              ADC     A,B                 
4460: 73              LD      (HL),E              
4461: 88              ADC     A,B                 
4462: 73              LD      (HL),E              
4463: B7              OR      A                   
4464: 73              LD      (HL),E              
4465: E7              RST     0X20                
4466: 73              LD      (HL),E              
4467: 18 74           JR      $44DD               ; {}
4469: 47              LD      B,A                 
446A: 74              LD      (HL),H              
446B: 76              HALT                        
446C: 74              LD      (HL),H              
446D: 86              ADD     A,(HL)              
446E: 74              LD      (HL),H              
446F: E3                              
4470: 74              LD      (HL),H              
4471: 0E 75           LD      C,$75               
4473: 3F              CCF                         
4474: 75              LD      (HL),L              
4475: 6E              LD      L,(HL)              
4476: 75              LD      (HL),L              
4477: AF              XOR     A                   
4478: 75              LD      (HL),L              
4479: C0              RET     NZ                  
447A: 75              LD      (HL),L              
447B: C0              RET     NZ                  
447C: 75              LD      (HL),L              
447D: C0              RET     NZ                  
447E: 75              LD      (HL),L              
447F: C0              RET     NZ                  
4480: 75              LD      (HL),L              
4481: C0              RET     NZ                  
4482: 75              LD      (HL),L              
4483: 68              LD      L,B                 
4484: 76              HALT                        
4485: 15              DEC     D                   
4486: 77              LD      (HL),A              
4487: A3              AND     E                   
4488: 77              LD      (HL),A              
4489: 74              LD      (HL),H              
448A: 78              LD      A,B                 
448B: F5              PUSH    AF                  
448C: 78              LD      A,B                 
448D: D3                              
448E: 79              LD      A,C                 
448F: B1              OR      C                   
4490: 7A              LD      A,D                 
4491: 60              LD      H,B                 
4492: 7B              LD      A,E                 
4493: CE 7B           ADC     $7B                 
4495: CE 7B           ADC     $7B                 
4497: 5A              LD      E,D                 
4498: 7C              LD      A,H                 
4499: 9B              SBC     E                   
449A: 7C              LD      A,H                 
449B: B6              OR      (HL)                
449C: 7D              LD      A,L                 
449D: 30 7E           JR      NC,$451D            ; {}
449F: A8              XOR     B                   
44A0: 7E              LD      A,(HL)              
44A1: F7              RST     0X30                
44A2: 7E              LD      A,(HL)              
44A3: 47              LD      B,A                 
44A4: 7F              LD      A,A                 
44A5: 98              SBC     B                   
44A6: 7F              LD      A,A                 
44A7: B7              OR      A                   
44A8: 7F              LD      A,A                 
44A9: B7              OR      A                   
44AA: 7F              LD      A,A                 
44AB: B7              OR      A                   
44AC: 7F              LD      A,A                 
44AD: B7              OR      A                   
44AE: 7F              LD      A,A                 
44AF: B7              OR      A                   
44B0: 7F              LD      A,A                 
44B1: B7              OR      A                   
44B2: 7F              LD      A,A                 
44B3: B7              OR      A                   
44B4: 7F              LD      A,A                 
44B5: B7              OR      A                   
44B6: 7F              LD      A,A                 
44B7: B7              OR      A                   
44B8: 7F              LD      A,A                 
44B9: B7              OR      A                   
44BA: 7F              LD      A,A                 
44BB: B7              OR      A                   
44BC: 7F              LD      A,A                 
44BD: B7              OR      A                   
44BE: 7F              LD      A,A                 
44BF: B7              OR      A                   
44C0: 7F              LD      A,A                 
44C1: B7              OR      A                   
44C2: 7F              LD      A,A                 
44C3: B7              OR      A                   
44C4: 7F              LD      A,A                 
44C5: B7              OR      A                   
44C6: 7F              LD      A,A                 
44C7: B7              OR      A                   
44C8: 7F              LD      A,A                 
44C9: B7              OR      A                   
44CA: 7F              LD      A,A                 
44CB: B7              OR      A                   
44CC: 7F              LD      A,A                 
44CD: B7              OR      A                   
44CE: 7F              LD      A,A                 
44CF: B7              OR      A                   
44D0: 7F              LD      A,A                 
44D1: B7              OR      A                   
44D2: 7F              LD      A,A                 
44D3: B7              OR      A                   
44D4: 7F              LD      A,A                 
44D5: B7              OR      A                   
44D6: 7F              LD      A,A                 
44D7: B7              OR      A                   
44D8: 7F              LD      A,A                 
44D9: B7              OR      A                   
44DA: 7F              LD      A,A                 
44DB: B7              OR      A                   
44DC: 7F              LD      A,A                 
44DD: B7              OR      A                   
44DE: 7F              LD      A,A                 
44DF: B7              OR      A                   
44E0: 7F              LD      A,A                 
44E1: B7              OR      A                   
44E2: 7F              LD      A,A                 
44E3: B7              OR      A                   
44E4: 7F              LD      A,A                 
44E5: B7              OR      A                   
44E6: 7F              LD      A,A                 
44E7: B7              OR      A                   
44E8: 7F              LD      A,A                 
44E9: B7              OR      A                   
44EA: 7F              LD      A,A                 
44EB: B7              OR      A                   
44EC: 7F              LD      A,A                 
44ED: 00              NOP                         
44EE: 7D              LD      A,L                 
44EF: 60              LD      H,B                 
44F0: 7D              LD      A,L                 
44F1: AE              XOR     (HL)                
44F2: 7D              LD      A,L                 
44F3: E7              RST     0X20                
44F4: 7D              LD      A,L                 
44F5: 23              INC     HL                  
44F6: 7E              LD      A,(HL)              
44F7: 3D              DEC     A                   
44F8: 7E              LD      A,(HL)              
44F9: 64              LD      H,H                 
44FA: 7E              LD      A,(HL)              
44FB: 6D              LD      L,L                 
44FC: 7E              LD      A,(HL)              
44FD: 99              SBC     C                   
44FE: 7E              LD      A,(HL)              
44FF: C3 7E 00        JP      $007E               
4502: 10 20           ;;STOP    $20                 
4504: 30 40           JR      NC,$4546            ; {}
4506: 50              LD      D,B                 
4507: 60              LD      H,B                 
4508: 70              LD      (HL),B              
4509: 80              ADD     A,B                 
450A: 90              SUB     B                   
450B: A0              AND     B                   
450C: B0              OR      B                   
450D: C0              RET     NZ                  
450E: D0              RET     NC                  
450F: E0 F0           LD      ($FF00+$F0),A       
4511: 00              NOP                         
4512: 10 20           ;;STOP    $20                 
4514: 30 40           JR      NC,$4556            ; {}
4516: 50              LD      D,B                 
4517: 60              LD      H,B                 
4518: 70              LD      (HL),B              
4519: 80              ADD     A,B                 
451A: 90              SUB     B                   
451B: A0              AND     B                   
451C: B0              OR      B                   
451D: C0              RET     NZ                  
451E: D0              RET     NC                  
451F: E0 F0           LD      ($FF00+$F0),A       
4521: 8D              ADC     A,L                 
4522: 8D              ADC     A,L                 
4523: 8D              ADC     A,L                 
4524: 8D              ADC     A,L                 
4525: 8D              ADC     A,L                 
4526: 8D              ADC     A,L                 
4527: 8D              ADC     A,L                 
4528: 8D              ADC     A,L                 
4529: 8D              ADC     A,L                 
452A: 8D              ADC     A,L                 
452B: 8D              ADC     A,L                 
452C: 8D              ADC     A,L                 
452D: 8D              ADC     A,L                 
452E: 8D              ADC     A,L                 
452F: 8D              ADC     A,L                 
4530: 8D              ADC     A,L                 
4531: 8E              ADC     A,(HL)              
4532: 8E              ADC     A,(HL)              
4533: 8E              ADC     A,(HL)              
4534: 8E              ADC     A,(HL)              
4535: 8E              ADC     A,(HL)              
4536: 8E              ADC     A,(HL)              
4537: 8E              ADC     A,(HL)              
4538: 8E              ADC     A,(HL)              
4539: 8E              ADC     A,(HL)              
453A: 8E              ADC     A,(HL)              
453B: 8E              ADC     A,(HL)              
453C: 8E              ADC     A,(HL)              
453D: 8E              ADC     A,(HL)              
453E: 8E              ADC     A,(HL)              
453F: 8E              ADC     A,(HL)              
4540: 8E              ADC     A,(HL)              
4541: D0              RET     NC                  
4542: D1              POP     DE                  
4543: D2 D3 D4        JP      NC,$D4D3            
4546: D5              PUSH    DE                  
4547: D6 D7           SUB     $D7                 
4549: D8              RET     C                   
454A: D9              RETI                        
454B: DA DB DC        JP      C,$DCDB             
454E: DD                              
454F: DE DF           SBC     $DF                 
4551: E0 E1           LD      ($FF00+$E1),A       
4553: E2              LD      (C),A               
4554: E3                              
4555: E4                              
4556: E5              PUSH    HL                  
4557: E6 E7           AND     $E7                 
4559: E8 E9           ADD     SP,$E9              
455B: EA EB EC        LD      ($ECEB),A           
455E: ED                              
455F: EE EF           XOR     $EF                 
4561: 98              SBC     B                   
4562: 98              SBC     B                   
4563: 98              SBC     B                   
4564: 98              SBC     B                   
4565: 98              SBC     B                   
4566: 98              SBC     B                   
4567: 98              SBC     B                   
4568: 98              SBC     B                   
4569: 98              SBC     B                   
456A: 98              SBC     B                   
456B: 98              SBC     B                   
456C: 98              SBC     B                   
456D: 98              SBC     B                   
456E: 98              SBC     B                   
456F: 98              SBC     B                   
4570: 98              SBC     B                   
4571: 98              SBC     B                   
4572: 98              SBC     B                   
4573: 98              SBC     B                   
4574: 98              SBC     B                   
4575: 98              SBC     B                   
4576: 98              SBC     B                   
4577: 98              SBC     B                   
4578: 98              SBC     B                   
4579: 98              SBC     B                   
457A: 98              SBC     B                   
457B: 98              SBC     B                   
457C: 98              SBC     B                   
457D: 98              SBC     B                   
457E: 98              SBC     B                   
457F: 98              SBC     B                   
4580: 98              SBC     B                   
4581: 99              SBC     C                   
4582: 99              SBC     C                   
4583: 99              SBC     C                   
4584: 99              SBC     C                   
4585: 99              SBC     C                   
4586: 99              SBC     C                   
4587: 99              SBC     C                   
4588: 99              SBC     C                   
4589: 99              SBC     C                   
458A: 99              SBC     C                   
458B: 99              SBC     C                   
458C: 99              SBC     C                   
458D: 99              SBC     C                   
458E: 99              SBC     C                   
458F: 99              SBC     C                   
4590: 99              SBC     C                   
4591: 99              SBC     C                   
4592: 99              SBC     C                   
4593: 99              SBC     C                   
4594: 99              SBC     C                   
4595: 99              SBC     C                   
4596: 99              SBC     C                   
4597: 99              SBC     C                   
4598: 99              SBC     C                   
4599: 99              SBC     C                   
459A: 99              SBC     C                   
459B: 99              SBC     C                   
459C: 99              SBC     C                   
459D: 99              SBC     C                   
459E: 99              SBC     C                   
459F: 99              SBC     C                   
45A0: 99              SBC     C                   
45A1: 42              LD      B,D                 
45A2: 43              LD      B,E                 
45A3: 44              LD      B,H                 
45A4: 45              LD      B,L                 
45A5: 46              LD      B,(HL)              
45A6: 47              LD      B,A                 
45A7: 48              LD      C,B                 
45A8: 49              LD      C,C                 
45A9: 4A              LD      C,D                 
45AA: 4B              LD      C,E                 
45AB: 4C              LD      C,H                 
45AC: 4D              LD      C,L                 
45AD: 4E              LD      C,(HL)              
45AE: 4F              LD      C,A                 
45AF: 50              LD      D,B                 
45B0: 51              LD      D,C                 
45B1: 82              ADD     A,D                 
45B2: 83              ADD     A,E                 
45B3: 84              ADD     A,H                 
45B4: 85              ADD     A,L                 
45B5: 86              ADD     A,(HL)              
45B6: 87              ADD     A,A                 
45B7: 88              ADC     A,B                 
45B8: 89              ADC     A,C                 
45B9: 8A              ADC     A,D                 
45BA: 8B              ADC     A,E                 
45BB: 8C              ADC     A,H                 
45BC: 8D              ADC     A,L                 
45BD: 8E              ADC     A,(HL)              
45BE: 8F              ADC     A,A                 
45BF: 90              SUB     B                   
45C0: 91              SUB     C                   
45C1: 62              LD      H,D                 
45C2: 63              LD      H,E                 
45C3: 64              LD      H,H                 
45C4: 65              LD      H,L                 
45C5: 66              LD      H,(HL)              
45C6: 67              LD      H,A                 
45C7: 68              LD      L,B                 
45C8: 69              LD      L,C                 
45C9: 6A              LD      L,D                 
45CA: 6B              LD      L,E                 
45CB: 6C              LD      L,H                 
45CC: 6D              LD      L,L                 
45CD: 6E              LD      L,(HL)              
45CE: 6F              LD      L,A                 
45CF: 70              LD      (HL),B              
45D0: 71              LD      (HL),C              
45D1: A2              AND     D                   
45D2: A3              AND     E                   
45D3: A4              AND     H                   
45D4: A5              AND     L                   
45D5: A6              AND     (HL)                
45D6: A7              AND     A                   
45D7: A8              XOR     B                   
45D8: A9              XOR     C                   
45D9: AA              XOR     D                   
45DA: AB              XOR     E                   
45DB: AC              XOR     H                   
45DC: AD              XOR     L                   
45DD: AE              XOR     (HL)                
45DE: AF              XOR     A                   
45DF: B0              OR      B                   
45E0: B1              OR      C                   
45E1: 00              NOP                         
45E2: 00              NOP                         
45E3: 00              NOP                         
45E4: 00              NOP                         
45E5: 00              NOP                         
45E6: 00              NOP                         
45E7: 00              NOP                         
45E8: 00              NOP                         
45E9: 00              NOP                         
45EA: 00              NOP                         
45EB: 00              NOP                         
45EC: 00              NOP                         
45ED: 00              NOP                         
45EE: 00              NOP                         
45EF: 00              NOP                         
45F0: 00              NOP                         
45F1: 00              NOP                         
45F2: 00              NOP                         
45F3: 00              NOP                         
45F4: 00              NOP                         
45F5: 00              NOP                         
45F6: 00              NOP                         
45F7: 00              NOP                         
45F8: 00              NOP                         
45F9: 00              NOP                         
45FA: 00              NOP                         
45FB: 00              NOP                         
45FC: 00              NOP                         
45FD: 00              NOP                         
45FE: 00              NOP                         
45FF: 00              NOP                         
4600: 00              NOP                         
4601: 7E              LD      A,(HL)              
4602: 3D              DEC     A                   
4603: 41              LD      B,C                 
4604: 00              NOP                         
4605: 8A              ADC     A,D                 
4606: 8B              ADC     A,E                 
4607: 44              LD      B,H                 
4608: 40              LD      B,B                 
4609: 45              LD      B,L                 
460A: 46              LD      B,(HL)              
460B: 8C              ADC     A,H                 
460C: 8D              ADC     A,L                 
460D: 3A              LD      A,(HLD)             
460E: 3F              CCF                         
460F: 3B              DEC     SP                  
4610: 00              NOP                         
4611: 70              LD      (HL),B              
4612: 71              LD      (HL),C              
4613: 72              LD      (HL),D              
4614: 73              LD      (HL),E              
4615: 74              LD      (HL),H              
4616: 75              LD      (HL),L              
4617: 76              HALT                        
4618: 77              LD      (HL),A              
4619: 78              LD      A,B                 
461A: 79              LD      A,C                 
461B: 42              LD      B,D                 
461C: 43              LD      B,E                 
461D: 8E              ADC     A,(HL)              
461E: 00              NOP                         
461F: 8F              ADC     A,A                 
4620: 3C              INC     A                   
4621: 00              NOP                         
4622: 00              NOP                         
4623: 01 02 03        LD      BC,$0302            
4626: 04              INC     B                   
4627: 05              DEC     B                   
4628: 06 07           LD      B,$07               
462A: 08 09 0A        LD      ($0A09),SP          
462D: 0B              DEC     BC                  
462E: 0C              INC     C                   
462F: 0D              DEC     C                   
4630: 0E 0F           LD      C,$0F               
4632: 10 11           ;;STOP    $11                 
4634: 12              LD      (DE),A              
4635: 13              INC     DE                  
4636: 14              INC     D                   
4637: 15              DEC     D                   
4638: 16 17           LD      D,$17               
463A: 18 19           JR      $4655               ; {}
463C: 00              NOP                         
463D: 00              NOP                         
463E: 00              NOP                         
463F: 40              LD      B,B                 
4640: 00              NOP                         
4641: 00              NOP                         
4642: 1A              LD      A,(DE)              
4643: 1B              DEC     DE                  
4644: 1C              INC     E                   
4645: 1D              DEC     E                   
4646: 1E 1F           LD      E,$1F               
4648: 20 21           JR      NZ,$466B            ; {}
464A: 22              LD      (HLI),A             
464B: 23              INC     HL                  
464C: 24              INC     H                   
464D: 25              DEC     H                   
464E: 26 27           LD      H,$27               
4650: 28 29           JR      Z,$467B             ; {}
4652: 2A              LD      A,(HLI)             
4653: 2B              DEC     HL                  
4654: 2C              INC     L                   
4655: 2D              DEC     L                   
4656: 2E 2F           LD      L,$2F               
4658: 30 31           JR      NC,$468B            ; {}
465A: 32              LD      (HLD),A             
465B: 3E 00           LD      A,$00               
465D: 00              NOP                         
465E: 00              NOP                         
465F: 00              NOP                         
4660: 00              NOP                         
4661: 47              LD      B,A                 
4662: 48              LD      C,B                 
4663: 49              LD      C,C                 
4664: 4A              LD      C,D                 
4665: 4B              LD      C,E                 
4666: 4C              LD      C,H                 
4667: 4D              LD      C,L                 
4668: 4E              LD      C,(HL)              
4669: 4F              LD      C,A                 
466A: 50              LD      D,B                 
466B: 51              LD      D,C                 
466C: 52              LD      D,D                 
466D: 53              LD      D,E                 
466E: 59              LD      E,C                 
466F: 5A              LD      E,D                 
4670: 5B              LD      E,E                 
4671: 5C              LD      E,H                 
4672: 5D              LD      E,L                 
4673: 59              LD      E,C                 
4674: 5A              LD      E,D                 
4675: 5B              LD      E,E                 
4676: 5C              LD      E,H                 
4677: 5D              LD      E,L                 
4678: 32              LD      (HLD),A             
4679: 6F              LD      L,A                 
467A: 6D              LD      L,L                 
467B: 6E              LD      L,(HL)              
467C: 00              NOP                         
467D: 00              NOP                         
467E: 00              NOP                         
467F: 00              NOP                         
4680: 00              NOP                         
4681: 3D              DEC     A                   
4682: 3C              INC     A                   
4683: 3F              CCF                         
4684: 7E              LD      A,(HL)              
4685: 39              ADD     HL,SP               
4686: 3A              LD      A,(HLD)             
4687: 3B              DEC     SP                  
4688: 7A              LD      A,D                 
4689: 7B              LD      A,E                 
468A: 00              NOP                         
468B: 00              NOP                         
468C: 00              NOP                         
468D: 00              NOP                         
468E: 00              NOP                         
468F: 00              NOP                         
4690: 00              NOP                         
4691: 70              LD      (HL),B              
4692: 71              LD      (HL),C              
4693: 72              LD      (HL),D              
4694: 73              LD      (HL),E              
4695: 74              LD      (HL),H              
4696: 75              LD      (HL),L              
4697: 76              HALT                        
4698: 77              LD      (HL),A              
4699: 78              LD      A,B                 
469A: 79              LD      A,C                 
469B: 9B              SBC     E                   
469C: 9C              SBC     H                   
469D: 9D              SBC     L                   
469E: 9E              SBC     (HL)                
469F: 9F              SBC     A                   
46A0: 38 00           JR      C,$46A2             ; {}
46A2: 00              NOP                         
46A3: 00              NOP                         
46A4: 00              NOP                         
46A5: 00              NOP                         
46A6: 00              NOP                         
46A7: 00              NOP                         
46A8: 00              NOP                         
46A9: 00              NOP                         
46AA: 00              NOP                         
46AB: 00              NOP                         
46AC: 00              NOP                         
46AD: 00              NOP                         
46AE: 00              NOP                         
46AF: 00              NOP                         
46B0: 00              NOP                         
46B1: 80              ADD     A,B                 
46B2: 81              ADD     A,C                 
46B3: 82              ADD     A,D                 
46B4: 83              ADD     A,E                 
46B5: 84              ADD     A,H                 
46B6: 85              ADD     A,L                 
46B7: 86              ADD     A,(HL)              
46B8: 87              ADD     A,A                 
46B9: 88              ADC     A,B                 
46BA: 89              ADC     A,C                 
46BB: 8A              ADC     A,D                 
46BC: 8B              ADC     A,E                 
46BD: 8C              ADC     A,H                 
46BE: 8D              ADC     A,L                 
46BF: 8E              ADC     A,(HL)              
46C0: 8F              ADC     A,A                 
46C1: 88              ADC     A,B                 
46C2: 90              SUB     B                   
46C3: 91              SUB     C                   
46C4: 92              SUB     D                   
46C5: 93              SUB     E                   
46C6: 94              SUB     H                   
46C7: 95              SUB     L                   
46C8: 89              ADC     A,C                 
46C9: 96              SUB     (HL)                
46CA: 97              SUB     A                   
46CB: 98              SBC     B                   
46CC: 99              SBC     C                   
46CD: 9A              SBC     D                   
46CE: 87              ADD     A,A                 
46CF: 86              ADD     A,(HL)              
46D0: 00              NOP                         
46D1: 34              INC     (HL)                
46D2: 35              DEC     (HL)                
46D3: 36 37           LD      (HL),$37            
46D5: 00              NOP                         
46D6: 00              NOP                         
46D7: 00              NOP                         
46D8: 00              NOP                         
46D9: 00              NOP                         
46DA: 00              NOP                         
46DB: 00              NOP                         
46DC: 00              NOP                         
46DD: 00              NOP                         
46DE: 7E              LD      A,(HL)              
46DF: 00              NOP                         
46E0: 00              NOP                         
46E1: 14              INC     D                   
46E2: 94              SUB     H                   
46E3: 14              INC     D                   
46E4: 14              INC     D                   
46E5: 14              INC     D                   
46E6: 14              INC     D                   
46E7: 14              INC     D                   
46E8: 14              INC     D                   
46E9: 14              INC     D                   
46EA: 14              INC     D                   
46EB: 14              INC     D                   
46EC: 14              INC     D                   
46ED: 14              INC     D                   
46EE: 14              INC     D                   
46EF: 14              INC     D                   
46F0: 94              SUB     H                   
46F1: 14              INC     D                   
46F2: 14              INC     D                   
46F3: 14              INC     D                   
46F4: 94              SUB     H                   
46F5: 14              INC     D                   
46F6: 14              INC     D                   
46F7: 94              SUB     H                   
46F8: 14              INC     D                   
46F9: 14              INC     D                   
46FA: 14              INC     D                   
46FB: 14              INC     D                   
46FC: 14              INC     D                   
46FD: 14              INC     D                   
46FE: 14              INC     D                   
46FF: 14              INC     D                   
4700: 14              INC     D                   
4701: 14              INC     D                   
4702: 14              INC     D                   
4703: 14              INC     D                   
4704: 14              INC     D                   
4705: 14              INC     D                   
4706: 14              INC     D                   
4707: 94              SUB     H                   
4708: 14              INC     D                   
4709: 14              INC     D                   
470A: 14              INC     D                   
470B: 14              INC     D                   
470C: 14              INC     D                   
470D: 14              INC     D                   
470E: 14              INC     D                   
470F: 14              INC     D                   
4710: 14              INC     D                   
4711: 14              INC     D                   
4712: 14              INC     D                   
4713: 14              INC     D                   
4714: 14              INC     D                   
4715: 14              INC     D                   
4716: 14              INC     D                   
4717: 94              SUB     H                   
4718: 14              INC     D                   
4719: 94              SUB     H                   
471A: 14              INC     D                   
471B: 14              INC     D                   
471C: 14              INC     D                   
471D: 14              INC     D                   
471E: 14              INC     D                   
471F: 14              INC     D                   
4720: 14              INC     D                   
4721: 14              INC     D                   
4722: 14              INC     D                   
4723: 14              INC     D                   
4724: 14              INC     D                   
4725: 14              INC     D                   
4726: 94              SUB     H                   
4727: 94              SUB     H                   
4728: 94              SUB     H                   
4729: 94              SUB     H                   
472A: 94              SUB     H                   
472B: 94              SUB     H                   
472C: 94              SUB     H                   
472D: 94              SUB     H                   
472E: 94              SUB     H                   
472F: 94              SUB     H                   
4730: 94              SUB     H                   
4731: 94              SUB     H                   
4732: 94              SUB     H                   
4733: 94              SUB     H                   
4734: 94              SUB     H                   
4735: 94              SUB     H                   
4736: 14              INC     D                   
4737: 14              INC     D                   
4738: 14              INC     D                   
4739: 14              INC     D                   
473A: 14              INC     D                   
473B: 14              INC     D                   
473C: 14              INC     D                   
473D: 14              INC     D                   
473E: 14              INC     D                   
473F: 14              INC     D                   
4740: 14              INC     D                   
4741: 14              INC     D                   
4742: 14              INC     D                   
4743: 14              INC     D                   
4744: 14              INC     D                   
4745: 14              INC     D                   
4746: 14              INC     D                   
4747: 14              INC     D                   
4748: 14              INC     D                   
4749: 14              INC     D                   
474A: 14              INC     D                   
474B: 14              INC     D                   
474C: 14              INC     D                   
474D: 14              INC     D                   
474E: 14              INC     D                   
474F: 14              INC     D                   
4750: 14              INC     D                   
4751: 14              INC     D                   
4752: 14              INC     D                   
4753: 14              INC     D                   
4754: 14              INC     D                   
4755: 14              INC     D                   
4756: 14              INC     D                   
4757: 14              INC     D                   
4758: 14              INC     D                   
4759: 14              INC     D                   
475A: 14              INC     D                   
475B: 14              INC     D                   
475C: 14              INC     D                   
475D: 14              INC     D                   
475E: 14              INC     D                   
475F: 14              INC     D                   
4760: 14              INC     D                   
4761: 16 16           LD      D,$16               
4763: 16 16           LD      D,$16               
4765: 16 16           LD      D,$16               
4767: 16 16           LD      D,$16               
4769: 16 16           LD      D,$16               
476B: 16 16           LD      D,$16               
476D: 16 16           LD      D,$16               
476F: 16 16           LD      D,$16               
4771: 96              SUB     (HL)                
4772: 96              SUB     (HL)                
4773: 96              SUB     (HL)                
4774: 96              SUB     (HL)                
4775: 96              SUB     (HL)                
4776: 96              SUB     (HL)                
4777: 96              SUB     (HL)                
4778: 96              SUB     (HL)                
4779: 96              SUB     (HL)                
477A: 96              SUB     (HL)                
477B: 96              SUB     (HL)                
477C: 96              SUB     (HL)                
477D: 96              SUB     (HL)                
477E: 96              SUB     (HL)                
477F: 96              SUB     (HL)                
4780: 96              SUB     (HL)                
4781: 96              SUB     (HL)                
4782: 96              SUB     (HL)                
4783: 96              SUB     (HL)                
4784: 96              SUB     (HL)                
4785: 96              SUB     (HL)                
4786: 96              SUB     (HL)                
4787: 96              SUB     (HL)                
4788: 96              SUB     (HL)                
4789: 96              SUB     (HL)                
478A: 96              SUB     (HL)                
478B: 96              SUB     (HL)                
478C: 96              SUB     (HL)                
478D: 96              SUB     (HL)                
478E: 96              SUB     (HL)                
478F: 96              SUB     (HL)                
4790: 96              SUB     (HL)                
4791: 96              SUB     (HL)                
4792: 96              SUB     (HL)                
4793: 96              SUB     (HL)                
4794: 96              SUB     (HL)                
4795: 96              SUB     (HL)                
4796: 96              SUB     (HL)                
4797: 96              SUB     (HL)                
4798: 96              SUB     (HL)                
4799: 96              SUB     (HL)                
479A: 96              SUB     (HL)                
479B: 96              SUB     (HL)                
479C: 96              SUB     (HL)                
479D: 96              SUB     (HL)                
479E: 96              SUB     (HL)                
479F: 96              SUB     (HL)                
47A0: 96              SUB     (HL)                
47A1: 96              SUB     (HL)                
47A2: 96              SUB     (HL)                
47A3: 96              SUB     (HL)                
47A4: 96              SUB     (HL)                
47A5: 96              SUB     (HL)                
47A6: 96              SUB     (HL)                
47A7: 96              SUB     (HL)                
47A8: 96              SUB     (HL)                
47A9: 96              SUB     (HL)                
47AA: 96              SUB     (HL)                
47AB: 96              SUB     (HL)                
47AC: 96              SUB     (HL)                
47AD: 96              SUB     (HL)                
47AE: 96              SUB     (HL)                
47AF: 96              SUB     (HL)                
47B0: 96              SUB     (HL)                
47B1: 96              SUB     (HL)                
47B2: 96              SUB     (HL)                
47B3: 96              SUB     (HL)                
47B4: 96              SUB     (HL)                
47B5: 96              SUB     (HL)                
47B6: 96              SUB     (HL)                
47B7: 96              SUB     (HL)                
47B8: 96              SUB     (HL)                
47B9: 96              SUB     (HL)                
47BA: 96              SUB     (HL)                
47BB: 16 16           LD      D,$16               
47BD: 16 16           LD      D,$16               
47BF: 16 16           LD      D,$16               
47C1: 16 96           LD      D,$96               
47C3: 96              SUB     (HL)                
47C4: 96              SUB     (HL)                
47C5: 96              SUB     (HL)                
47C6: 96              SUB     (HL)                
47C7: 16 16           LD      D,$16               
47C9: 09              ADD     HL,BC               
47CA: 89              ADC     A,C                 
47CB: 09              ADD     HL,BC               
47CC: 09              ADD     HL,BC               
47CD: 09              ADD     HL,BC               
47CE: 09              ADD     HL,BC               
47CF: 09              ADD     HL,BC               
47D0: 09              ADD     HL,BC               
47D1: 09              ADD     HL,BC               
47D2: 09              ADD     HL,BC               
47D3: 09              ADD     HL,BC               
47D4: 09              ADD     HL,BC               
47D5: 09              ADD     HL,BC               
47D6: 89              ADC     A,C                 
47D7: 89              ADC     A,C                 
47D8: 89              ADC     A,C                 
47D9: 09              ADD     HL,BC               
47DA: 09              ADD     HL,BC               
47DB: 09              ADD     HL,BC               
47DC: 09              ADD     HL,BC               
47DD: 09              ADD     HL,BC               
47DE: 09              ADD     HL,BC               
47DF: 89              ADC     A,C                 
47E0: 09              ADD     HL,BC               
47E1: 1C              INC     E                   
47E2: 1C              INC     E                   
47E3: 1C              INC     E                   
47E4: 1C              INC     E                   
47E5: 1C              INC     E                   
47E6: 1C              INC     E                   
47E7: 1C              INC     E                   
47E8: 1C              INC     E                   
47E9: 9C              SBC     H                   
47EA: 9C              SBC     H                   
47EB: 9C              SBC     H                   
47EC: 9C              SBC     H                   
47ED: 9C              SBC     H                   
47EE: 9C              SBC     H                   
47EF: 9C              SBC     H                   
47F0: 9C              SBC     H                   
47F1: 9C              SBC     H                   
47F2: 9C              SBC     H                   
47F3: 1C              INC     E                   
47F4: 1C              INC     E                   
47F5: 1C              INC     E                   
47F6: 1C              INC     E                   
47F7: 1C              INC     E                   
47F8: 1C              INC     E                   
47F9: 1C              INC     E                   
47FA: 1C              INC     E                   
47FB: 1C              INC     E                   
47FC: 1C              INC     E                   
47FD: 1C              INC     E                   
47FE: 1C              INC     E                   
47FF: 1C              INC     E                   
4800: 1C              INC     E                   
4801: 1C              INC     E                   
4802: 1C              INC     E                   
4803: 1C              INC     E                   
4804: 1C              INC     E                   
4805: 1C              INC     E                   
4806: 1C              INC     E                   
4807: 1C              INC     E                   
4808: 1C              INC     E                   
4809: 1C              INC     E                   
480A: 1C              INC     E                   
480B: 1C              INC     E                   
480C: 1C              INC     E                   
480D: 1C              INC     E                   
480E: 1C              INC     E                   
480F: 1C              INC     E                   
4810: 1C              INC     E                   
4811: 1C              INC     E                   
4812: 1C              INC     E                   
4813: 1C              INC     E                   
4814: 1C              INC     E                   
4815: 1C              INC     E                   
4816: 1C              INC     E                   
4817: 1C              INC     E                   
4818: 1C              INC     E                   
4819: 1C              INC     E                   
481A: 1C              INC     E                   
481B: 1C              INC     E                   
481C: 1C              INC     E                   
481D: 1C              INC     E                   
481E: 1C              INC     E                   
481F: 1C              INC     E                   
4820: 1C              INC     E                   
4821: 1C              INC     E                   
4822: 1C              INC     E                   
4823: 1C              INC     E                   
4824: 1C              INC     E                   
4825: 1C              INC     E                   
4826: 1C              INC     E                   
4827: 1C              INC     E                   
4828: 1C              INC     E                   
4829: 1C              INC     E                   
482A: 1C              INC     E                   
482B: 1C              INC     E                   
482C: 1C              INC     E                   
482D: 1C              INC     E                   
482E: 1C              INC     E                   
482F: 1C              INC     E                   
4830: 1C              INC     E                   
4831: 1C              INC     E                   
4832: 1C              INC     E                   
4833: 1C              INC     E                   
4834: 1C              INC     E                   
4835: 1C              INC     E                   
4836: 1C              INC     E                   
4837: 1C              INC     E                   
4838: 1C              INC     E                   
4839: 1C              INC     E                   
483A: 1C              INC     E                   
483B: 1C              INC     E                   
483C: 1C              INC     E                   
483D: 1C              INC     E                   
483E: 1C              INC     E                   
483F: 1C              INC     E                   
4840: 1C              INC     E                   
4841: 1C              INC     E                   
4842: 1C              INC     E                   
4843: 1C              INC     E                   
4844: 1C              INC     E                   
4845: 1C              INC     E                   
4846: 1C              INC     E                   
4847: 1C              INC     E                   
4848: 9C              SBC     H                   
4849: 1C              INC     E                   
484A: 1C              INC     E                   
484B: 1C              INC     E                   
484C: 1C              INC     E                   
484D: 1C              INC     E                   
484E: 1C              INC     E                   
484F: 1C              INC     E                   
4850: 1C              INC     E                   
4851: 1C              INC     E                   
4852: 1C              INC     E                   
4853: 1C              INC     E                   
4854: 1C              INC     E                   
4855: 1C              INC     E                   
4856: 1C              INC     E                   
4857: 1C              INC     E                   
4858: 1C              INC     E                   
4859: 1C              INC     E                   
485A: 1C              INC     E                   
485B: 1C              INC     E                   
485C: 1C              INC     E                   
485D: 1C              INC     E                   
485E: 1C              INC     E                   
485F: 1C              INC     E                   
4860: 1C              INC     E                   
4861: 1D              DEC     E                   
4862: 1D              DEC     E                   
4863: 1D              DEC     E                   
4864: 1D              DEC     E                   
4865: 1D              DEC     E                   
4866: 1D              DEC     E                   
4867: 1D              DEC     E                   
4868: 1D              DEC     E                   
4869: 1D              DEC     E                   
486A: 1D              DEC     E                   
486B: 1D              DEC     E                   
486C: 1D              DEC     E                   
486D: 1D              DEC     E                   
486E: 1D              DEC     E                   
486F: 1D              DEC     E                   
4870: 1D              DEC     E                   
4871: 1D              DEC     E                   
4872: 9D              SBC     L                   
4873: 1D              DEC     E                   
4874: 1D              DEC     E                   
4875: 9D              SBC     L                   
4876: 1D              DEC     E                   
4877: 1D              DEC     E                   
4878: 1D              DEC     E                   
4879: 1D              DEC     E                   
487A: 1D              DEC     E                   
487B: 1D              DEC     E                   
487C: 1D              DEC     E                   
487D: 1D              DEC     E                   
487E: 1D              DEC     E                   
487F: 1D              DEC     E                   
4880: 1D              DEC     E                   
4881: 1D              DEC     E                   
4882: 1D              DEC     E                   
4883: 1D              DEC     E                   
4884: 1D              DEC     E                   
4885: 1D              DEC     E                   
4886: 1D              DEC     E                   
4887: 1D              DEC     E                   
4888: 1D              DEC     E                   
4889: 1D              DEC     E                   
488A: 1D              DEC     E                   
488B: 1D              DEC     E                   
488C: 1D              DEC     E                   
488D: 1D              DEC     E                   
488E: 1D              DEC     E                   
488F: 1D              DEC     E                   
4890: 1D              DEC     E                   
4891: 1D              DEC     E                   
4892: 1D              DEC     E                   
4893: 1D              DEC     E                   
4894: 1D              DEC     E                   
4895: 1D              DEC     E                   
4896: 1D              DEC     E                   
4897: 1D              DEC     E                   
4898: 1D              DEC     E                   
4899: 1D              DEC     E                   
489A: 1D              DEC     E                   
489B: 1D              DEC     E                   
489C: 1D              DEC     E                   
489D: 1D              DEC     E                   
489E: 1D              DEC     E                   
489F: 1D              DEC     E                   
48A0: 1D              DEC     E                   
48A1: 1D              DEC     E                   
48A2: 9D              SBC     L                   
48A3: 1D              DEC     E                   
48A4: 1D              DEC     E                   
48A5: 1D              DEC     E                   
48A6: 1D              DEC     E                   
48A7: 1D              DEC     E                   
48A8: 1D              DEC     E                   
48A9: 1D              DEC     E                   
48AA: 1D              DEC     E                   
48AB: 1D              DEC     E                   
48AC: 1D              DEC     E                   
48AD: 1D              DEC     E                   
48AE: 1D              DEC     E                   
48AF: 1D              DEC     E                   
48B0: 1D              DEC     E                   
48B1: 1D              DEC     E                   
48B2: 1D              DEC     E                   
48B3: 1D              DEC     E                   
48B4: 1D              DEC     E                   
48B5: 1D              DEC     E                   
48B6: 9D              SBC     L                   
48B7: 1D              DEC     E                   
48B8: 1D              DEC     E                   
48B9: 9D              SBC     L                   
48BA: 9D              SBC     L                   
48BB: 1D              DEC     E                   
48BC: 1D              DEC     E                   
48BD: 1D              DEC     E                   
48BE: 1D              DEC     E                   
48BF: 1D              DEC     E                   
48C0: 1D              DEC     E                   
48C1: 1D              DEC     E                   
48C2: 1D              DEC     E                   
48C3: 1D              DEC     E                   
48C4: 1D              DEC     E                   
48C5: 1D              DEC     E                   
48C6: 1D              DEC     E                   
48C7: 1D              DEC     E                   
48C8: 1D              DEC     E                   
48C9: 1D              DEC     E                   
48CA: 1D              DEC     E                   
48CB: 1D              DEC     E                   
48CC: 9D              SBC     L                   
48CD: 1D              DEC     E                   
48CE: 1D              DEC     E                   
48CF: 1D              DEC     E                   
48D0: 1D              DEC     E                   
48D1: 1D              DEC     E                   
48D2: 1D              DEC     E                   
48D3: 1D              DEC     E                   
48D4: 1D              DEC     E                   
48D5: 1D              DEC     E                   
48D6: 9D              SBC     L                   
48D7: 1D              DEC     E                   
48D8: 1D              DEC     E                   
48D9: 1D              DEC     E                   
48DA: 1D              DEC     E                   
48DB: 1D              DEC     E                   
48DC: 1D              DEC     E                   
48DD: 1D              DEC     E                   
48DE: 1D              DEC     E                   
48DF: 9D              SBC     L                   
48E0: 9D              SBC     L                   
48E1: 1D              DEC     E                   
48E2: 1D              DEC     E                   
48E3: 1D              DEC     E                   
48E4: 1D              DEC     E                   
48E5: 1D              DEC     E                   
48E6: 1D              DEC     E                   
48E7: 1D              DEC     E                   
48E8: 1D              DEC     E                   
48E9: 1D              DEC     E                   
48EA: 1D              DEC     E                   
48EB: 1D              DEC     E                   
48EC: 1D              DEC     E                   
48ED: 1D              DEC     E                   
48EE: 1D              DEC     E                   
48EF: 1D              DEC     E                   
48F0: 1D              DEC     E                   
48F1: 9D              SBC     L                   
48F2: 9D              SBC     L                   
48F3: 1D              DEC     E                   
48F4: 9D              SBC     L                   
48F5: 9D              SBC     L                   
48F6: 9D              SBC     L                   
48F7: 9D              SBC     L                   
48F8: 1D              DEC     E                   
48F9: 1D              DEC     E                   
48FA: 1D              DEC     E                   
48FB: 1D              DEC     E                   
48FC: 1D              DEC     E                   
48FD: 1D              DEC     E                   
48FE: 1D              DEC     E                   
48FF: 1D              DEC     E                   
4900: 1D              DEC     E                   
4901: 1D              DEC     E                   
4902: 1D              DEC     E                   
4903: 1D              DEC     E                   
4904: 1D              DEC     E                   
4905: 1D              DEC     E                   
4906: 1D              DEC     E                   
4907: 1D              DEC     E                   
4908: 1D              DEC     E                   
4909: 1D              DEC     E                   
490A: 1D              DEC     E                   
490B: 1D              DEC     E                   
490C: 1D              DEC     E                   
490D: 1D              DEC     E                   
490E: 1D              DEC     E                   
490F: 1D              DEC     E                   
4910: 1D              DEC     E                   
4911: 1D              DEC     E                   
4912: 1D              DEC     E                   
4913: 1D              DEC     E                   
4914: 1D              DEC     E                   
4915: 1D              DEC     E                   
4916: 9D              SBC     L                   
4917: 9D              SBC     L                   
4918: 9D              SBC     L                   
4919: 9D              SBC     L                   
491A: 9D              SBC     L                   
491B: 9D              SBC     L                   
491C: 9D              SBC     L                   
491D: 1D              DEC     E                   
491E: 1D              DEC     E                   
491F: 1D              DEC     E                   
4920: 1D              DEC     E                   
4921: 1D              DEC     E                   
4922: 1D              DEC     E                   
4923: 1D              DEC     E                   
4924: 1D              DEC     E                   
4925: 1D              DEC     E                   
4926: 1D              DEC     E                   
4927: 1D              DEC     E                   
4928: 1D              DEC     E                   
4929: 1D              DEC     E                   
492A: 1D              DEC     E                   
492B: 1D              DEC     E                   
492C: 1D              DEC     E                   
492D: 1D              DEC     E                   
492E: 1D              DEC     E                   
492F: 1D              DEC     E                   
4930: 1D              DEC     E                   
4931: 1D              DEC     E                   
4932: 1D              DEC     E                   
4933: 1D              DEC     E                   
4934: 1D              DEC     E                   
4935: 1D              DEC     E                   
4936: 1D              DEC     E                   
4937: 1D              DEC     E                   
4938: 1D              DEC     E                   
4939: 1D              DEC     E                   
493A: 1D              DEC     E                   
493B: 1D              DEC     E                   
493C: 1D              DEC     E                   
493D: 1D              DEC     E                   
493E: 1D              DEC     E                   
493F: 1D              DEC     E                   
4940: 1D              DEC     E                   
4941: 1D              DEC     E                   
4942: 1D              DEC     E                   
4943: 1D              DEC     E                   
4944: 1D              DEC     E                   
4945: 1D              DEC     E                   
4946: 1D              DEC     E                   
4947: 1D              DEC     E                   
4948: 1D              DEC     E                   
4949: 1D              DEC     E                   
494A: 1D              DEC     E                   
494B: 1D              DEC     E                   
494C: 1D              DEC     E                   
494D: 1D              DEC     E                   
494E: 1D              DEC     E                   
494F: 1D              DEC     E                   
4950: 1D              DEC     E                   
4951: 1D              DEC     E                   
4952: 1D              DEC     E                   
4953: 1D              DEC     E                   
4954: 1D              DEC     E                   
4955: 1D              DEC     E                   
4956: 1D              DEC     E                   
4957: 09              ADD     HL,BC               
4958: 09              ADD     HL,BC               
4959: 09              ADD     HL,BC               
495A: 09              ADD     HL,BC               
495B: 09              ADD     HL,BC               
495C: 09              ADD     HL,BC               
495D: 09              ADD     HL,BC               
495E: 09              ADD     HL,BC               
495F: 09              ADD     HL,BC               
4960: 09              ADD     HL,BC               
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
4980: FF              RST     0X38                
4981: FF              RST     0X38                
4982: FF              RST     0X38                
4983: FF              RST     0X38                
4984: FF              RST     0X38                
4985: FF              RST     0X38                
4986: FF              RST     0X38                
4987: FF              RST     0X38                
4988: FF              RST     0X38                
4989: FF              RST     0X38                
498A: FF              RST     0X38                
498B: FF              RST     0X38                
498C: FF              RST     0X38                
498D: FF              RST     0X38                
498E: FF              RST     0X38                
498F: FF              RST     0X38                
4990: FF              RST     0X38                
4991: FF              RST     0X38                
4992: FF              RST     0X38                
4993: FF              RST     0X38                
4994: FF              RST     0X38                
4995: FF              RST     0X38                
4996: FF              RST     0X38                
4997: FF              RST     0X38                
4998: FF              RST     0X38                
4999: FF              RST     0X38                
499A: FF              RST     0X38                
499B: FF              RST     0X38                
499C: FF              RST     0X38                
499D: FF              RST     0X38                
499E: FF              RST     0X38                
499F: FF              RST     0X38                
49A0: FF              RST     0X38                
49A1: FF              RST     0X38                
49A2: FF              RST     0X38                
49A3: FF              RST     0X38                
49A4: FF              RST     0X38                
49A5: FF              RST     0X38                
49A6: FF              RST     0X38                
49A7: FF              RST     0X38                
49A8: FF              RST     0X38                
49A9: FF              RST     0X38                
49AA: FF              RST     0X38                
49AB: FF              RST     0X38                
49AC: FF              RST     0X38                
49AD: FF              RST     0X38                
49AE: FF              RST     0X38                
49AF: FF              RST     0X38                
49B0: FF              RST     0X38                
49B1: FF              RST     0X38                
49B2: FF              RST     0X38                
49B3: FF              RST     0X38                
49B4: FF              RST     0X38                
49B5: FF              RST     0X38                
49B6: FF              RST     0X38                
49B7: FF              RST     0X38                
49B8: FF              RST     0X38                
49B9: FF              RST     0X38                
49BA: FF              RST     0X38                
49BB: FF              RST     0X38                
49BC: FF              RST     0X38                
49BD: FF              RST     0X38                
49BE: FF              RST     0X38                
49BF: FF              RST     0X38                
49C0: FF              RST     0X38                
49C1: FF              RST     0X38                
49C2: FF              RST     0X38                
49C3: FF              RST     0X38                
49C4: FF              RST     0X38                
49C5: FF              RST     0X38                
49C6: FF              RST     0X38                
49C7: FF              RST     0X38                
49C8: FF              RST     0X38                
49C9: FF              RST     0X38                
49CA: FF              RST     0X38                
49CB: FF              RST     0X38                
49CC: FF              RST     0X38                
49CD: FF              RST     0X38                
49CE: FF              RST     0X38                
49CF: FF              RST     0X38                
49D0: FF              RST     0X38                
49D1: FF              RST     0X38                
49D2: FF              RST     0X38                
49D3: FF              RST     0X38                
49D4: FF              RST     0X38                
49D5: FF              RST     0X38                
49D6: FF              RST     0X38                
49D7: FF              RST     0X38                
49D8: FF              RST     0X38                
49D9: FF              RST     0X38                
49DA: FF              RST     0X38                
49DB: FF              RST     0X38                
49DC: FF              RST     0X38                
49DD: FF              RST     0X38                
49DE: FF              RST     0X38                
49DF: FF              RST     0X38                
49E0: FF              RST     0X38                
49E1: FF              RST     0X38                
49E2: FF              RST     0X38                
49E3: FF              RST     0X38                
49E4: FF              RST     0X38                
49E5: FF              RST     0X38                
49E6: FF              RST     0X38                
49E7: FF              RST     0X38                
49E8: FF              RST     0X38                
49E9: FF              RST     0X38                
49EA: FF              RST     0X38                
49EB: FF              RST     0X38                
49EC: FF              RST     0X38                
49ED: FF              RST     0X38                
49EE: FF              RST     0X38                
49EF: FF              RST     0X38                
49F0: FF              RST     0X38                
49F1: FF              RST     0X38                
49F2: FF              RST     0X38                
49F3: FF              RST     0X38                
49F4: FF              RST     0X38                
49F5: FF              RST     0X38                
49F6: FF              RST     0X38                
49F7: FF              RST     0X38                
49F8: FF              RST     0X38                
49F9: FF              RST     0X38                
49FA: FF              RST     0X38                
49FB: FF              RST     0X38                
49FC: FF              RST     0X38                
49FD: FF              RST     0X38                
49FE: FF              RST     0X38                
49FF: FF              RST     0X38                
4A00: 59              LD      E,C                 
4A01: 6F              LD      L,A                 
4A02: 75              LD      (HL),L              
4A03: 5E              LD      E,(HL)              
4A04: 76              HALT                        
4A05: 65              LD      H,L                 
4A06: 20 67           JR      NZ,$4A6F            ; {}
4A08: 6F              LD      L,A                 
4A09: 74              LD      (HL),H              
4A0A: 20 74           JR      NZ,$4A80            ; {}
4A0C: 68              LD      L,B                 
4A0D: 65              LD      H,L                 
4A0E: 20 20           JR      NZ,$4A30            ; {}
4A10: 46              LD      B,(HL)              
4A11: 75              LD      (HL),L              
4A12: 6C              LD      L,H                 
4A13: 6C              LD      L,H                 
4A14: 20 4D           JR      NZ,$4A63            ; {}
4A16: 6F              LD      L,A                 
4A17: 6F              LD      L,A                 
4A18: 6E              LD      L,(HL)              
4A19: 20 43           JR      NZ,$4A5E            ; {}
4A1B: 65              LD      H,L                 
4A1C: 6C              LD      L,H                 
4A1D: 6C              LD      L,H                 
4A1E: 6F              LD      L,A                 
4A1F: 21 FF 59        LD      HL,$59FF            
4A22: 6F              LD      L,A                 
4A23: 75              LD      (HL),L              
4A24: 5E              LD      E,(HL)              
4A25: 76              HALT                        
4A26: 65              LD      H,L                 
4A27: 20 67           JR      NZ,$4A90            ; {}
4A29: 6F              LD      L,A                 
4A2A: 74              LD      (HL),H              
4A2B: 20 74           JR      NZ,$4AA1            ; {}
4A2D: 68              LD      L,B                 
4A2E: 65              LD      H,L                 
4A2F: 20 20           JR      NZ,$4A51            ; {}
4A31: 43              LD      B,E                 
4A32: 6F              LD      L,A                 
4A33: 6E              LD      L,(HL)              
4A34: 63              LD      H,E                 
4A35: 68              LD      L,B                 
4A36: 20 48           JR      NZ,$4A80            ; {}
4A38: 6F              LD      L,A                 
4A39: 72              LD      (HL),D              
4A3A: 6E              LD      L,(HL)              
4A3B: 21 FF 59        LD      HL,$59FF            
4A3E: 6F              LD      L,A                 
4A3F: 75              LD      (HL),L              
4A40: 5E              LD      E,(HL)              
4A41: 76              HALT                        
4A42: 65              LD      H,L                 
4A43: 20 67           JR      NZ,$4AAC            ; {}
4A45: 6F              LD      L,A                 
4A46: 74              LD      (HL),H              
4A47: 20 74           JR      NZ,$4ABD            ; {}
4A49: 68              LD      L,B                 
4A4A: 65              LD      H,L                 
4A4B: 20 20           JR      NZ,$4A6D            ; {}
4A4D: 53              LD      D,E                 
4A4E: 65              LD      H,L                 
4A4F: 61              LD      H,C                 
4A50: 20 4C           JR      NZ,$4A9E            ; {}
4A52: 69              LD      L,C                 
4A53: 6C              LD      L,H                 
4A54: 79              LD      A,C                 
4A55: 5E              LD      E,(HL)              
4A56: 73              LD      (HL),E              
4A57: 20 42           JR      NZ,$4A9B            ; {}
4A59: 65              LD      H,L                 
4A5A: 6C              LD      L,H                 
4A5B: 6C              LD      L,H                 
4A5C: 21 FF 59        LD      HL,$59FF            
4A5F: 6F              LD      L,A                 
4A60: 75              LD      (HL),L              
4A61: 5E              LD      E,(HL)              
4A62: 76              HALT                        
4A63: 65              LD      H,L                 
4A64: 20 67           JR      NZ,$4ACD            ; {}
4A66: 6F              LD      L,A                 
4A67: 74              LD      (HL),H              
4A68: 20 74           JR      NZ,$4ADE            ; {}
4A6A: 68              LD      L,B                 
4A6B: 65              LD      H,L                 
4A6C: 20 20           JR      NZ,$4A8E            ; {}
4A6E: 53              LD      D,E                 
4A6F: 75              LD      (HL),L              
4A70: 72              LD      (HL),D              
4A71: 66              LD      H,(HL)              
4A72: 20 48           JR      NZ,$4ABC            ; {}
4A74: 61              LD      H,C                 
4A75: 72              LD      (HL),D              
4A76: 70              LD      (HL),B              
4A77: 21 FF 59        LD      HL,$59FF            
4A7A: 6F              LD      L,A                 
4A7B: 75              LD      (HL),L              
4A7C: 5E              LD      E,(HL)              
4A7D: 76              HALT                        
4A7E: 65              LD      H,L                 
4A7F: 20 67           JR      NZ,$4AE8            ; {}
4A81: 6F              LD      L,A                 
4A82: 74              LD      (HL),H              
4A83: 20 74           JR      NZ,$4AF9            ; {}
4A85: 68              LD      L,B                 
4A86: 65              LD      H,L                 
4A87: 20 20           JR      NZ,$4AA9            ; {}
4A89: 57              LD      D,A                 
4A8A: 69              LD      L,C                 
4A8B: 6E              LD      L,(HL)              
4A8C: 64              LD      H,H                 
4A8D: 20 4D           JR      NZ,$4ADC            ; {}
4A8F: 61              LD      H,C                 
4A90: 72              LD      (HL),D              
4A91: 69              LD      L,C                 
4A92: 6D              LD      L,L                 
4A93: 62              LD      H,D                 
4A94: 61              LD      H,C                 
4A95: 21 FF 59        LD      HL,$59FF            
4A98: 6F              LD      L,A                 
4A99: 75              LD      (HL),L              
4A9A: 5E              LD      E,(HL)              
4A9B: 76              HALT                        
4A9C: 65              LD      H,L                 
4A9D: 20 67           JR      NZ,$4B06            ; {}
4A9F: 6F              LD      L,A                 
4AA0: 74              LD      (HL),H              
4AA1: 20 74           JR      NZ,$4B17            ; {}
4AA3: 68              LD      L,B                 
4AA4: 65              LD      H,L                 
4AA5: 20 20           JR      NZ,$4AC7            ; {}
4AA7: 43              LD      B,E                 
4AA8: 6F              LD      L,A                 
4AA9: 72              LD      (HL),D              
4AAA: 61              LD      H,C                 
4AAB: 6C              LD      L,H                 
4AAC: 20 54           JR      NZ,$4B02            ; {}
4AAE: 72              LD      (HL),D              
4AAF: 69              LD      L,C                 
4AB0: 61              LD      H,C                 
4AB1: 6E              LD      L,(HL)              
4AB2: 67              LD      H,A                 
4AB3: 6C              LD      L,H                 
4AB4: 65              LD      H,L                 
4AB5: 21 FF 59        LD      HL,$59FF            
4AB8: 6F              LD      L,A                 
4AB9: 75              LD      (HL),L              
4ABA: 5E              LD      E,(HL)              
4ABB: 76              HALT                        
4ABC: 65              LD      H,L                 
4ABD: 20 67           JR      NZ,$4B26            ; {}
4ABF: 6F              LD      L,A                 
4AC0: 74              LD      (HL),H              
4AC1: 20 74           JR      NZ,$4B37            ; {}
4AC3: 68              LD      L,B                 
4AC4: 65              LD      H,L                 
4AC5: 20 20           JR      NZ,$4AE7            ; {}
4AC7: 4F              LD      C,A                 
4AC8: 72              LD      (HL),D              
4AC9: 67              LD      H,A                 
4ACA: 61              LD      H,C                 
4ACB: 6E              LD      L,(HL)              
4ACC: 20 6F           JR      NZ,$4B3D            ; {}
4ACE: 66              LD      H,(HL)              
4ACF: 20 20           JR      NZ,$4AF1            ; {}
4AD1: 20 20           JR      NZ,$4AF3            ; {}
4AD3: 20 20           JR      NZ,$4AF5            ; {}
4AD5: 20 20           JR      NZ,$4AF7            ; {}
4AD7: 20 20           JR      NZ,$4AF9            ; {}
4AD9: 45              LD      B,L                 
4ADA: 76              HALT                        
4ADB: 65              LD      H,L                 
4ADC: 6E              LD      L,(HL)              
4ADD: 69              LD      L,C                 
4ADE: 6E              LD      L,(HL)              
4ADF: 67              LD      H,A                 
4AE0: 20 43           JR      NZ,$4B25            ; {}
4AE2: 61              LD      H,C                 
4AE3: 6C              LD      L,H                 
4AE4: 6D              LD      L,L                 
4AE5: 21 FF 59        LD      HL,$59FF            
4AE8: 6F              LD      L,A                 
4AE9: 75              LD      (HL),L              
4AEA: 5E              LD      E,(HL)              
4AEB: 76              HALT                        
4AEC: 65              LD      H,L                 
4AED: 20 67           JR      NZ,$4B56            ; {}
4AEF: 6F              LD      L,A                 
4AF0: 74              LD      (HL),H              
4AF1: 20 74           JR      NZ,$4B67            ; {}
4AF3: 68              LD      L,B                 
4AF4: 65              LD      H,L                 
4AF5: 20 20           JR      NZ,$4B17            ; {}
4AF7: 54              LD      D,H                 
4AF8: 68              LD      L,B                 
4AF9: 75              LD      (HL),L              
4AFA: 6E              LD      L,(HL)              
4AFB: 64              LD      H,H                 
4AFC: 65              LD      H,L                 
4AFD: 72              LD      (HL),D              
4AFE: 20 44           JR      NZ,$4B44            ; {}
4B00: 72              LD      (HL),D              
4B01: 75              LD      (HL),L              
4B02: 6D              LD      L,L                 
4B03: 21 FF 54        LD      HL,$54FF            
4B06: 75              LD      (HL),L              
4B07: 72              LD      (HL),D              
4B08: 6E              LD      L,(HL)              
4B09: 20 61           JR      NZ,$4B6C            ; {}
4B0B: 73              LD      (HL),E              
4B0C: 69              LD      L,C                 
4B0D: 64              LD      H,H                 
4B0E: 65              LD      H,L                 
4B0F: 20 74           JR      NZ,$4B85            ; {}
4B11: 68              LD      L,B                 
4B12: 65              LD      H,L                 
4B13: 20 20           JR      NZ,$4B35            ; {}
4B15: 73              LD      (HL),E              
4B16: 70              LD      (HL),B              
4B17: 69              LD      L,C                 
4B18: 6E              LD      L,(HL)              
4B19: 65              LD      H,L                 
4B1A: 64              LD      H,H                 
4B1B: 20 6F           JR      NZ,$4B8C            ; {}
4B1D: 6E              LD      L,(HL)              
4B1E: 65              LD      H,L                 
4B1F: 73              LD      (HL),E              
4B20: 20 77           JR      NZ,$4B99            ; {}
4B22: 69              LD      L,C                 
4B23: 74              LD      (HL),H              
4B24: 68              LD      L,B                 
4B25: 61              LD      H,C                 
4B26: 20 73           JR      NZ,$4B9B            ; {}
4B28: 68              LD      L,B                 
4B29: 69              LD      L,C                 
4B2A: 65              LD      H,L                 
4B2B: 6C              LD      L,H                 
4B2C: 64              LD      H,H                 
4B2D: 2E 2E           LD      L,$2E               
4B2F: 2E FF           LD      L,$FF               
4B31: 46              LD      B,(HL)              
4B32: 69              LD      L,C                 
4B33: 72              LD      (HL),D              
4B34: 73              LD      (HL),E              
4B35: 74              LD      (HL),H              
4B36: 2C              INC     L                   
4B37: 20 64           JR      NZ,$4B9D            ; {}
4B39: 65              LD      H,L                 
4B3A: 66              LD      H,(HL)              
4B3B: 65              LD      H,L                 
4B3C: 61              LD      H,C                 
4B3D: 74              LD      (HL),H              
4B3E: 20 20           JR      NZ,$4B60            ; {}
4B40: 20 74           JR      NZ,$4BB6            ; {}
4B42: 68              LD      L,B                 
4B43: 65              LD      H,L                 
4B44: 20 69           JR      NZ,$4BAF            ; {}
4B46: 6D              LD      L,L                 
4B47: 70              LD      (HL),B              
4B48: 72              LD      (HL),D              
4B49: 69              LD      L,C                 
4B4A: 73              LD      (HL),E              
4B4B: 6F              LD      L,A                 
4B4C: 6E              LD      L,(HL)              
4B4D: 65              LD      H,L                 
4B4E: 64              LD      H,H                 
4B4F: 20 20           JR      NZ,$4B71            ; {}
4B51: 50              LD      D,B                 
4B52: 6F              LD      L,A                 
4B53: 6C              LD      L,H                 
4B54: 73              LD      (HL),E              
4B55: 20 56           JR      NZ,$4BAD            ; {}
4B57: 6F              LD      L,A                 
4B58: 69              LD      L,C                 
4B59: 63              LD      H,E                 
4B5A: 65              LD      H,L                 
4B5B: 2C              INC     L                   
4B5C: 20 20           JR      NZ,$4B7E            ; {}
4B5E: 20 20           JR      NZ,$4B80            ; {}
4B60: 20 4C           JR      NZ,$4BAE            ; {}
4B62: 61              LD      H,C                 
4B63: 73              LD      (HL),E              
4B64: 74              LD      (HL),H              
4B65: 2C              INC     L                   
4B66: 20 53           JR      NZ,$4BBB            ; {}
4B68: 74              LD      (HL),H              
4B69: 61              LD      H,C                 
4B6A: 6C              LD      L,H                 
4B6B: 66              LD      H,(HL)              
4B6C: 6F              LD      L,A                 
4B6D: 73              LD      (HL),E              
4B6E: 2E 2E           LD      L,$2E               
4B70: 2E FF           LD      L,$FF               
4B72: FF              RST     0X38                
4B73: 46              LD      B,(HL)              
4B74: 61              LD      H,C                 
4B75: 72              LD      (HL),D              
4B76: 20 61           JR      NZ,$4BD9            ; {}
4B78: 77              LD      (HL),A              
4B79: 61              LD      H,C                 
4B7A: 79              LD      A,C                 
4B7B: 2E 2E           LD      L,$2E               
4B7D: 2E 20           LD      L,$20               
4B7F: 20 20           JR      NZ,$4BA1            ; {}
4B81: 20 20           JR      NZ,$4BA3            ; {}
4B83: 44              LD      B,H                 
4B84: 6F              LD      L,A                 
4B85: 20 6E           JR      NZ,$4BF5            ; {}
4B87: 6F              LD      L,A                 
4B88: 74              LD      (HL),H              
4B89: 20 66           JR      NZ,$4BF1            ; {}
4B8B: 65              LD      H,L                 
4B8C: 61              LD      H,C                 
4B8D: 72              LD      (HL),D              
4B8E: 2C              INC     L                   
4B8F: 20 20           JR      NZ,$4BB1            ; {}
4B91: 20 20           JR      NZ,$4BB3            ; {}
4B93: 64              LD      H,H                 
4B94: 61              LD      H,C                 
4B95: 73              LD      (HL),E              
4B96: 68              LD      L,B                 
4B97: 20 61           JR      NZ,$4BFA            ; {}
4B99: 6E              LD      L,(HL)              
4B9A: 64              LD      H,H                 
4B9B: 20 66           JR      NZ,$4C03            ; {}
4B9D: 6C              LD      L,H                 
4B9E: 79              LD      A,C                 
4B9F: 21 FF 54        LD      HL,$54FF            
4BA2: 68              LD      L,B                 
4BA3: 65              LD      H,L                 
4BA4: 20 67           JR      NZ,$4C0D            ; {}
4BA6: 6C              LD      L,H                 
4BA7: 69              LD      L,C                 
4BA8: 6E              LD      L,(HL)              
4BA9: 74              LD      (HL),H              
4BAA: 20 6F           JR      NZ,$4C1B            ; {}
4BAC: 66              LD      H,(HL)              
4BAD: 20 74           JR      NZ,$4C23            ; {}
4BAF: 68              LD      L,B                 
4BB0: 65              LD      H,L                 
4BB1: 74              LD      (HL),H              
4BB2: 69              LD      L,C                 
4BB3: 6C              LD      L,H                 
4BB4: 65              LD      H,L                 
4BB5: 20 77           JR      NZ,$4C2E            ; {}
4BB7: 69              LD      L,C                 
4BB8: 6C              LD      L,H                 
4BB9: 6C              LD      L,H                 
4BBA: 20 62           JR      NZ,$4C1E            ; {}
4BBC: 65              LD      H,L                 
4BBD: 20 20           JR      NZ,$4BDF            ; {}
4BBF: 20 20           JR      NZ,$4BE1            ; {}
4BC1: 79              LD      A,C                 
4BC2: 6F              LD      L,A                 
4BC3: 75              LD      (HL),L              
4BC4: 72              LD      (HL),D              
4BC5: 20 67           JR      NZ,$4C2E            ; {}
4BC7: 75              LD      (HL),L              
4BC8: 69              LD      L,C                 
4BC9: 64              LD      H,H                 
4BCA: 65              LD      H,L                 
4BCB: 2E 2E           LD      L,$2E               
4BCD: 2E FF           LD      L,$FF               
4BCF: 44              LD      B,H                 
4BD0: 69              LD      L,C                 
4BD1: 76              HALT                        
4BD2: 65              LD      H,L                 
4BD3: 20 75           JR      NZ,$4C4A            ; {}
4BD5: 6E              LD      L,(HL)              
4BD6: 64              LD      H,H                 
4BD7: 65              LD      H,L                 
4BD8: 72              LD      (HL),D              
4BD9: 20 77           JR      NZ,$4C52            ; {}
4BDB: 68              LD      L,B                 
4BDC: 65              LD      H,L                 
4BDD: 72              LD      (HL),D              
4BDE: 65              LD      H,L                 
4BDF: 74              LD      (HL),H              
4BE0: 6F              LD      L,A                 
4BE1: 72              LD      (HL),D              
4BE2: 63              LD      H,E                 
4BE3: 68              LD      L,B                 
4BE4: 6C              LD      L,H                 
4BE5: 69              LD      L,C                 
4BE6: 67              LD      H,A                 
4BE7: 68              LD      L,B                 
4BE8: 74              LD      (HL),H              
4BE9: 20 62           JR      NZ,$4C4D            ; {}
4BEB: 65              LD      H,L                 
4BEC: 61              LD      H,C                 
4BED: 6D              LD      L,L                 
4BEE: 73              LD      (HL),E              
4BEF: 64              LD      H,H                 
4BF0: 6F              LD      L,A                 
4BF1: 20 63           JR      NZ,$4C56            ; {}
4BF3: 72              LD      (HL),D              
4BF4: 6F              LD      L,A                 
4BF5: 73              LD      (HL),E              
4BF6: 73              LD      (HL),E              
4BF7: 2E 2E           LD      L,$2E               
4BF9: 2E FF           LD      L,$FF               
4BFB: 45              LD      B,L                 
4BFC: 6E              LD      L,(HL)              
4BFD: 74              LD      (HL),H              
4BFE: 65              LD      H,L                 
4BFF: 72              LD      (HL),D              
4C00: 20 74           JR      NZ,$4C76            ; {}
4C02: 68              LD      L,B                 
4C03: 65              LD      H,L                 
4C04: 20 73           JR      NZ,$4C79            ; {}
4C06: 70              LD      (HL),B              
4C07: 61              LD      H,C                 
4C08: 63              LD      H,E                 
4C09: 65              LD      H,L                 
4C0A: 20 77           JR      NZ,$4C83            ; {}
4C0C: 68              LD      L,B                 
4C0D: 65              LD      H,L                 
4C0E: 72              LD      (HL),D              
4C0F: 65              LD      H,L                 
4C10: 20 74           JR      NZ,$4C86            ; {}
4C12: 68              LD      L,B                 
4C13: 65              LD      H,L                 
4C14: 20 65           JR      NZ,$4C7B            ; {}
4C16: 79              LD      A,C                 
4C17: 65              LD      H,L                 
4C18: 73              LD      (HL),E              
4C19: 20 20           JR      NZ,$4C3B            ; {}
4C1B: 68              LD      L,B                 
4C1C: 61              LD      H,C                 
4C1D: 76              HALT                        
4C1E: 65              LD      H,L                 
4C1F: 20 77           JR      NZ,$4C98            ; {}
4C21: 61              LD      H,C                 
4C22: 6C              LD      L,H                 
4C23: 6C              LD      L,H                 
4C24: 73              LD      (HL),E              
4C25: 2E 2E           LD      L,$2E               
4C27: 2E FF           LD      L,$FF               
4C29: 54              LD      D,H                 
4C2A: 68              LD      L,B                 
4C2B: 65              LD      H,L                 
4C2C: 20 72           JR      NZ,$4CA0            ; {}
4C2E: 69              LD      L,C                 
4C2F: 64              LD      H,H                 
4C30: 64              LD      H,H                 
4C31: 6C              LD      L,H                 
4C32: 65              LD      H,L                 
4C33: 20 69           JR      NZ,$4C9E            ; {}
4C35: 73              LD      (HL),E              
4C36: 20 20           JR      NZ,$4C58            ; {}
4C38: 20 73           JR      NZ,$4CAD            ; {}
4C3A: 6F              LD      L,A                 
4C3B: 6C              LD      L,H                 
4C3C: 76              HALT                        
4C3D: 65              LD      H,L                 
4C3E: 64              LD      H,H                 
4C3F: 20 77           JR      NZ,$4CB8            ; {}
4C41: 68              LD      L,B                 
4C42: 65              LD      H,L                 
4C43: 6E              LD      L,(HL)              
4C44: 20 74           JR      NZ,$4CBA            ; {}
4C46: 68              LD      L,B                 
4C47: 65              LD      H,L                 
4C48: 20 70           JR      NZ,$4CBA            ; {}
4C4A: 69              LD      L,C                 
4C4B: 6C              LD      L,H                 
4C4C: 6C              LD      L,H                 
4C4D: 61              LD      H,C                 
4C4E: 72              LD      (HL),D              
4C4F: 73              LD      (HL),E              
4C50: 20 66           JR      NZ,$4CB8            ; {}
4C52: 61              LD      H,C                 
4C53: 6C              LD      L,H                 
4C54: 6C              LD      L,H                 
4C55: 21 FF 46        LD      HL,$46FF            
4C58: 69              LD      L,C                 
4C59: 6C              LD      L,H                 
4C5A: 6C              LD      L,H                 
4C5B: 20 61           JR      NZ,$4CBE            ; {}
4C5D: 6C              LD      L,H                 
4C5E: 6C              LD      L,H                 
4C5F: 20 74           JR      NZ,$4CD5            ; {}
4C61: 68              LD      L,B                 
4C62: 65              LD      H,L                 
4C63: 20 20           JR      NZ,$4C85            ; {}
4C65: 20 20           JR      NZ,$4C87            ; {}
4C67: 68              LD      L,B                 
4C68: 6F              LD      L,A                 
4C69: 6C              LD      L,H                 
4C6A: 65              LD      H,L                 
4C6B: 73              LD      (HL),E              
4C6C: 20 77           JR      NZ,$4CE5            ; {}
4C6E: 69              LD      L,C                 
4C6F: 74              LD      (HL),H              
4C70: 68              LD      L,B                 
4C71: 20 74           JR      NZ,$4CE7            ; {}
4C73: 68              LD      L,B                 
4C74: 65              LD      H,L                 
4C75: 20 20           JR      NZ,$4C97            ; {}
4C77: 72              LD      (HL),D              
4C78: 6F              LD      L,A                 
4C79: 63              LD      H,E                 
4C7A: 6B              LD      L,E                 
4C7B: 20 74           JR      NZ,$4CF1            ; {}
4C7D: 68              LD      L,B                 
4C7E: 61              LD      H,C                 
4C7F: 74              LD      (HL),H              
4C80: 20 72           JR      NZ,$4CF4            ; {}
4C82: 6F              LD      L,A                 
4C83: 6C              LD      L,H                 
4C84: 6C              LD      L,H                 
4C85: 73              LD      (HL),E              
4C86: 2C              INC     L                   
4C87: 74              LD      (HL),H              
4C88: 68              LD      L,B                 
4C89: 69              LD      L,C                 
4C8A: 73              LD      (HL),E              
4C8B: 20 28           JR      NZ,$4CB5            ; {}
4C8D: EE 29           XOR     $29                 
4C8F: 20 69           JR      NZ,$4CFA            ; {}
4C91: 73              LD      (HL),E              
4C92: 20 74           JR      NZ,$4D08            ; {}
4C94: 68              LD      L,B                 
4C95: 65              LD      H,L                 
4C96: 20 6B           JR      NZ,$4D03            ; {}
4C98: 65              LD      H,L                 
4C99: 79              LD      A,C                 
4C9A: 21 FF 53        LD      HL,$53FF            
4C9D: 6F              LD      L,A                 
4C9E: 6D              LD      L,L                 
4C9F: 65              LD      H,L                 
4CA0: 74              LD      (HL),H              
4CA1: 68              LD      L,B                 
4CA2: 69              LD      L,C                 
4CA3: 6E              LD      L,(HL)              
4CA4: 67              LD      H,A                 
4CA5: 20 69           JR      NZ,$4D10            ; {}
4CA7: 73              LD      (HL),E              
4CA8: 20 20           JR      NZ,$4CCA            ; {}
4CAA: 20 20           JR      NZ,$4CCC            ; {}
4CAC: 69              LD      L,C                 
4CAD: 6E              LD      L,(HL)              
4CAE: 73              LD      (HL),E              
4CAF: 63              LD      H,E                 
4CB0: 72              LD      (HL),D              
4CB1: 69              LD      L,C                 
4CB2: 62              LD      H,D                 
4CB3: 65              LD      H,L                 
4CB4: 64              LD      H,H                 
4CB5: 20 6F           JR      NZ,$4D26            ; {}
4CB7: 6E              LD      L,(HL)              
4CB8: 20 74           JR      NZ,$4D2E            ; {}
4CBA: 68              LD      L,B                 
4CBB: 65              LD      H,L                 
4CBC: 73              LD      (HL),E              
4CBD: 74              LD      (HL),H              
4CBE: 6F              LD      L,A                 
4CBF: 6E              LD      L,(HL)              
4CC0: 65              LD      H,L                 
4CC1: 20 73           JR      NZ,$4D36            ; {}
4CC3: 6C              LD      L,H                 
4CC4: 61              LD      H,C                 
4CC5: 62              LD      H,D                 
4CC6: 2C              INC     L                   
4CC7: 20 62           JR      NZ,$4D2B            ; {}
4CC9: 75              LD      (HL),L              
4CCA: 74              LD      (HL),H              
4CCB: 20 79           JR      NZ,$4D46            ; {}
4CCD: 6F              LD      L,A                 
4CCE: 75              LD      (HL),L              
4CCF: 20 63           JR      NZ,$4D34            ; {}
4CD1: 61              LD      H,C                 
4CD2: 6E              LD      L,(HL)              
4CD3: 5E              LD      E,(HL)              
4CD4: 74              LD      (HL),H              
4CD5: 20 72           JR      NZ,$4D49            ; {}
4CD7: 65              LD      H,L                 
4CD8: 61              LD      H,C                 
4CD9: 64              LD      H,H                 
4CDA: 20 20           JR      NZ,$4CFC            ; {}
4CDC: 69              LD      L,C                 
4CDD: 74              LD      (HL),H              
4CDE: 20 62           JR      NZ,$4D42            ; {}
4CE0: 65              LD      H,L                 
4CE1: 63              LD      H,E                 
4CE2: 61              LD      H,C                 
4CE3: 75              LD      (HL),L              
4CE4: 73              LD      (HL),E              
4CE5: 65              LD      H,L                 
4CE6: 20 61           JR      NZ,$4D49            ; {}
4CE8: 20 20           JR      NZ,$4D0A            ; {}
4CEA: 20 20           JR      NZ,$4D0C            ; {}
4CEC: 70              LD      (HL),B              
4CED: 69              LD      L,C                 
4CEE: 65              LD      H,L                 
4CEF: 63              LD      H,E                 
4CF0: 65              LD      H,L                 
4CF1: 20 69           JR      NZ,$4D5C            ; {}
4CF3: 73              LD      (HL),E              
4CF4: 20 67           JR      NZ,$4D5D            ; {}
4CF6: 6F              LD      L,A                 
4CF7: 6E              LD      L,(HL)              
4CF8: 65              LD      H,L                 
4CF9: 2E FF           LD      L,$FF               
4CFB: 5E              LD      E,(HL)              
4CFC: 49              LD      C,C                 
4CFD: 5E              LD      E,(HL)              
4CFE: 76              HALT                        
4CFF: 65              LD      H,L                 
4D00: 20 67           JR      NZ,$4D69            ; {}
4D02: 6F              LD      L,A                 
4D03: 74              LD      (HL),H              
4D04: 20 77           JR      NZ,$4D7D            ; {}
4D06: 68              LD      L,B                 
4D07: 61              LD      H,C                 
4D08: 74              LD      (HL),H              
4D09: 20 20           JR      NZ,$4D2B            ; {}
4D0B: 77              LD      (HL),A              
4D0C: 61              LD      H,C                 
4D0D: 73              LD      (HL),E              
4D0E: 20 69           JR      NZ,$4D79            ; {}
4D10: 6E              LD      L,(HL)              
4D11: 73              LD      (HL),E              
4D12: 69              LD      L,C                 
4D13: 64              LD      H,H                 
4D14: 65              LD      H,L                 
4D15: 20 74           JR      NZ,$4D8B            ; {}
4D17: 68              LD      L,B                 
4D18: 69              LD      L,C                 
4D19: 73              LD      (HL),E              
4D1A: 20 62           JR      NZ,$4D7E            ; {}
4D1C: 6F              LD      L,A                 
4D1D: 78              LD      A,B                 
4D1E: 2E 20           LD      L,$20               
4D20: 20 43           JR      NZ,$4D65            ; {}
4D22: 6F              LD      L,A                 
4D23: 6D              LD      L,L                 
4D24: 65              LD      H,L                 
4D25: 20 61           JR      NZ,$4D88            ; {}
4D27: 6E              LD      L,(HL)              
4D28: 64              LD      H,H                 
4D29: 20 20           JR      NZ,$4D4B            ; {}
4D2B: 67              LD      H,A                 
4D2C: 65              LD      H,L                 
4D2D: 74              LD      (HL),H              
4D2E: 20 69           JR      NZ,$4D99            ; {}
4D30: 74              LD      (HL),H              
4D31: 2C              INC     L                   
4D32: 20 69           JR      NZ,$4D9D            ; {}
4D34: 66              LD      H,(HL)              
4D35: 20 79           JR      NZ,$4DB0            ; {}
4D37: 6F              LD      L,A                 
4D38: 75              LD      (HL),L              
4D39: 20 20           JR      NZ,$4D5B            ; {}
4D3B: 63              LD      H,E                 
4D3C: 61              LD      H,C                 
4D3D: 6E              LD      L,(HL)              
4D3E: 21 5E 20        LD      HL,$205E            
4D41: 20 4D           JR      NZ,$4D90            ; {}
4D43: 61              LD      H,C                 
4D44: 73              LD      (HL),E              
4D45: 74              LD      (HL),H              
4D46: 65              LD      H,L                 
4D47: 72              LD      (HL),D              
4D48: 20 DC           JR      NZ,$4D26            ; {}
4D4A: FF              RST     0X38                
4D4B: 47              LD      B,A                 
4D4C: 75              LD      (HL),L              
4D4D: 6C              LD      L,H                 
4D4E: 70              LD      (HL),B              
4D4F: 21 20 20        LD      HL,$2020            
4D52: 59              LD      E,C                 
4D53: 6F              LD      L,A                 
4D54: 75              LD      (HL),L              
4D55: 20 66           JR      NZ,$4DBD            ; {}
4D57: 6F              LD      L,A                 
4D58: 75              LD      (HL),L              
4D59: 6E              LD      L,(HL)              
4D5A: 64              LD      H,H                 
4D5B: 6D              LD      L,L                 
4D5C: 65              LD      H,L                 
4D5D: 21 20 20        LD      HL,$2020            
4D60: 59              LD      E,C                 
4D61: 6F              LD      L,A                 
4D62: 75              LD      (HL),L              
4D63: 5E              LD      E,(HL)              
4D64: 72              LD      (HL),D              
4D65: 65              LD      H,L                 
4D66: 20 61           JR      NZ,$4DC9            ; {}
4D68: 20 20           JR      NZ,$4D8A            ; {}
4D6A: 20 72           JR      NZ,$4DDE            ; {}
4D6C: 65              LD      H,L                 
4D6D: 61              LD      H,C                 
4D6E: 6C              LD      L,H                 
4D6F: 20 70           JR      NZ,$4DE1            ; {}
4D71: 65              LD      H,L                 
4D72: 73              LD      (HL),E              
4D73: 6B              LD      L,E                 
4D74: 79              LD      A,C                 
4D75: 20 6B           JR      NZ,$4DE2            ; {}
4D77: 69              LD      L,C                 
4D78: 64              LD      H,H                 
4D79: 2C              INC     L                   
4D7A: 20 79           JR      NZ,$4DF5            ; {}
4D7C: 6F              LD      L,A                 
4D7D: 75              LD      (HL),L              
4D7E: 20 6B           JR      NZ,$4DEB            ; {}
4D80: 6E              LD      L,(HL)              
4D81: 6F              LD      L,A                 
4D82: 77              LD      (HL),A              
4D83: 20 74           JR      NZ,$4DF9            ; {}
4D85: 68              LD      L,B                 
4D86: 61              LD      H,C                 
4D87: 74              LD      (HL),H              
4D88: 3F              CCF                         
4D89: 21 FF 41        LD      HL,$41FF            
4D8C: 72              LD      (HL),D              
4D8D: 72              LD      (HL),D              
4D8E: 67              LD      H,A                 
4D8F: 68              LD      L,B                 
4D90: 21 20 20        LD      HL,$2020            
4D93: 49              LD      C,C                 
4D94: 20 63           JR      NZ,$4DF9            ; {}
4D96: 61              LD      H,C                 
4D97: 6E              LD      L,(HL)              
4D98: 5E              LD      E,(HL)              
4D99: 74              LD      (HL),H              
4D9A: 20 62           JR      NZ,$4DFE            ; {}
4D9C: 65              LD      H,L                 
4D9D: 61              LD      H,C                 
4D9E: 74              LD      (HL),H              
4D9F: 20 79           JR      NZ,$4E1A            ; {}
4DA1: 6F              LD      L,A                 
4DA2: 75              LD      (HL),L              
4DA3: 21 20 20        LD      HL,$2020            
4DA6: 49              LD      C,C                 
4DA7: 5E              LD      E,(HL)              
4DA8: 6D              LD      L,L                 
4DA9: 20 20           JR      NZ,$4DCB            ; {}
4DAB: 6F              LD      L,A                 
4DAC: 75              LD      (HL),L              
4DAD: 74              LD      (HL),H              
4DAE: 74              LD      (HL),H              
4DAF: 61              LD      H,C                 
4DB0: 20 68           JR      NZ,$4E1A            ; {}
4DB2: 65              LD      H,L                 
4DB3: 72              LD      (HL),D              
4DB4: 65              LD      H,L                 
4DB5: 21 FF 59        LD      HL,$59FF            
4DB8: 6F              LD      L,A                 
4DB9: 75              LD      (HL),L              
4DBA: 20 61           JR      NZ,$4E1D            ; {}
4DBC: 67              LD      H,A                 
4DBD: 61              LD      H,C                 
4DBE: 69              LD      L,C                 
4DBF: 6E              LD      L,(HL)              
4DC0: 3F              CCF                         
4DC1: 21 20 20        LD      HL,$2020            
4DC4: 59              LD      E,C                 
4DC5: 6F              LD      L,A                 
4DC6: 75              LD      (HL),L              
4DC7: 6B              LD      L,E                 
4DC8: 65              LD      H,L                 
4DC9: 65              LD      H,L                 
4DCA: 70              LD      (HL),B              
4DCB: 20 67           JR      NZ,$4E34            ; {}
4DCD: 6F              LD      L,A                 
4DCE: 69              LD      L,C                 
4DCF: 6E              LD      L,(HL)              
4DD0: 67              LD      H,A                 
4DD1: 20 61           JR      NZ,$4E34            ; {}
4DD3: 6E              LD      L,(HL)              
4DD4: 64              LD      H,H                 
4DD5: 20 20           JR      NZ,$4DF7            ; {}
4DD7: 67              LD      H,A                 
4DD8: 6F              LD      L,A                 
4DD9: 69              LD      L,C                 
4DDA: 6E              LD      L,(HL)              
4DDB: 67              LD      H,A                 
4DDC: 2E 2E           LD      L,$2E               
4DDE: 2E 20           LD      L,$20               
4DE0: 49              LD      C,C                 
4DE1: 20 63           JR      NZ,$4E46            ; {}
4DE3: 61              LD      H,C                 
4DE4: 6E              LD      L,(HL)              
4DE5: 5E              LD      E,(HL)              
4DE6: 74              LD      (HL),H              
4DE7: 6F              LD      L,A                 
4DE8: 75              LD      (HL),L              
4DE9: 74              LD      (HL),H              
4DEA: 6C              LD      L,H                 
4DEB: 61              LD      H,C                 
4DEC: 73              LD      (HL),E              
4DED: 74              LD      (HL),H              
4DEE: 20 79           JR      NZ,$4E69            ; {}
4DF0: 6F              LD      L,A                 
4DF1: 75              LD      (HL),L              
4DF2: 21 20 20        LD      HL,$2020            
4DF5: 20 20           JR      NZ,$4E17            ; {}
4DF7: 41              LD      B,C                 
4DF8: 6C              LD      L,H                 
4DF9: 6C              LD      L,H                 
4DFA: 20 72           JR      NZ,$4E6E            ; {}
4DFC: 69              LD      L,C                 
4DFD: 67              LD      H,A                 
4DFE: 68              LD      L,B                 
4DFF: 74              LD      (HL),H              
4E00: 2C              INC     L                   
4E01: 20 6C           JR      NZ,$4E6F            ; {}
4E03: 65              LD      H,L                 
4E04: 74              LD      (HL),H              
4E05: 5E              LD      E,(HL)              
4E06: 73              LD      (HL),E              
4E07: 64              LD      H,H                 
4E08: 6F              LD      L,A                 
4E09: 20 69           JR      NZ,$4E74            ; {}
4E0B: 74              LD      (HL),H              
4E0C: 21 FF 57        LD      HL,$57FF            
4E0F: 4F              LD      C,A                 
4E10: 4F              LD      C,A                 
4E11: 46              LD      B,(HL)              
4E12: 21 20 44        LD      HL,$4420            
4E15: 69              LD      L,C                 
4E16: 67              LD      H,A                 
4E17: 21 20 52        LD      HL,$5220            
4E1A: 55              LD      D,L                 
4E1B: 46              LD      B,(HL)              
4E1C: 46              LD      B,(HL)              
4E1D: 21 FF 59        LD      HL,$59FF            
4E20: 6F              LD      L,A                 
4E21: 75              LD      (HL),L              
4E22: 20 70           JR      NZ,$4E94            ; {}
4E24: 75              LD      (HL),L              
4E25: 74              LD      (HL),H              
4E26: 20 74           JR      NZ,$4E9C            ; {}
4E28: 68              LD      L,B                 
4E29: 65              LD      H,L                 
4E2A: 20 20           JR      NZ,$4E4C            ; {}
4E2C: 20 20           JR      NZ,$4E4E            ; {}
4E2E: 20 6D           JR      NZ,$4E9D            ; {}
4E30: 69              LD      L,C                 
4E31: 73              LD      (HL),E              
4E32: 73              LD      (HL),E              
4E33: 69              LD      L,C                 
4E34: 6E              LD      L,(HL)              
4E35: 67              LD      H,A                 
4E36: 20 73           JR      NZ,$4EAB            ; {}
4E38: 63              LD      H,E                 
4E39: 61              LD      H,C                 
4E3A: 6C              LD      L,H                 
4E3B: 65              LD      H,L                 
4E3C: 20 69           JR      NZ,$4EA7            ; {}
4E3E: 6E              LD      L,(HL)              
4E3F: 74              LD      (HL),H              
4E40: 68              LD      L,B                 
4E41: 65              LD      H,L                 
4E42: 20 6D           JR      NZ,$4EB1            ; {}
4E44: 65              LD      H,L                 
4E45: 72              LD      (HL),D              
4E46: 6D              LD      L,L                 
4E47: 61              LD      H,C                 
4E48: 69              LD      L,C                 
4E49: 64              LD      H,H                 
4E4A: 20 20           JR      NZ,$4E6C            ; {}
4E4C: 20 20           JR      NZ,$4E6E            ; {}
4E4E: 20 73           JR      NZ,$4EC3            ; {}
4E50: 74              LD      (HL),H              
4E51: 61              LD      H,C                 
4E52: 74              LD      (HL),H              
4E53: 75              LD      (HL),L              
4E54: 65              LD      H,L                 
4E55: 21 FF 48        LD      HL,$48FF            
4E58: 65              LD      H,L                 
4E59: 79              LD      A,C                 
4E5A: 2C              INC     L                   
4E5B: 20 6D           JR      NZ,$4ECA            ; {}
4E5D: 61              LD      H,C                 
4E5E: 6E              LD      L,(HL)              
4E5F: 21 20 20        LD      HL,$2020            
4E62: 57              LD      D,A                 
4E63: 68              LD      L,B                 
4E64: 65              LD      H,L                 
4E65: 6E              LD      L,(HL)              
4E66: 20 79           JR      NZ,$4EE1            ; {}
4E68: 6F              LD      L,A                 
4E69: 75              LD      (HL),L              
4E6A: 20 77           JR      NZ,$4EE3            ; {}
4E6C: 61              LD      H,C                 
4E6D: 6E              LD      L,(HL)              
4E6E: 74              LD      (HL),H              
4E6F: 20 74           JR      NZ,$4EE5            ; {}
4E71: 6F              LD      L,A                 
4E72: 20 73           JR      NZ,$4EE7            ; {}
4E74: 61              LD      H,C                 
4E75: 76              HALT                        
4E76: 65              LD      H,L                 
4E77: 6A              LD      L,D                 
4E78: 75              LD      (HL),L              
4E79: 73              LD      (HL),E              
4E7A: 74              LD      (HL),H              
4E7B: 20 70           JR      NZ,$4EED            ; {}
4E7D: 75              LD      (HL),L              
4E7E: 73              LD      (HL),E              
4E7F: 68              LD      L,B                 
4E80: 20 61           JR      NZ,$4EE3            ; {}
4E82: 6C              LD      L,H                 
4E83: 6C              LD      L,H                 
4E84: 20 20           JR      NZ,$4EA6            ; {}
4E86: 20 74           JR      NZ,$4EFC            ; {}
4E88: 68              LD      L,B                 
4E89: 65              LD      H,L                 
4E8A: 20 42           JR      NZ,$4ECE            ; {}
4E8C: 75              LD      (HL),L              
4E8D: 74              LD      (HL),H              
4E8E: 74              LD      (HL),H              
4E8F: 6F              LD      L,A                 
4E90: 6E              LD      L,(HL)              
4E91: 73              LD      (HL),E              
4E92: 20 61           JR      NZ,$4EF5            ; {}
4E94: 74              LD      (HL),H              
4E95: 20 20           JR      NZ,$4EB7            ; {}
4E97: 6F              LD      L,A                 
4E98: 6E              LD      L,(HL)              
4E99: 63              LD      H,E                 
4E9A: 65              LD      H,L                 
4E9B: 21 20 20        LD      HL,$2020            
4E9E: 55              LD      D,L                 
4E9F: 68              LD      L,B                 
4EA0: 68              LD      L,B                 
4EA1: 2E 2E           LD      L,$2E               
4EA3: 2E 20           LD      L,$20               
4EA5: 20 20           JR      NZ,$4EC7            ; {}
4EA7: 44              LD      B,H                 
4EA8: 6F              LD      L,A                 
4EA9: 6E              LD      L,(HL)              
4EAA: 5E              LD      E,(HL)              
4EAB: 74              LD      (HL),H              
4EAC: 20 61           JR      NZ,$4F0F            ; {}
4EAE: 73              LD      (HL),E              
4EAF: 6B              LD      L,E                 
4EB0: 20 6D           JR      NZ,$4F1F            ; {}
4EB2: 65              LD      H,L                 
4EB3: 20 20           JR      NZ,$4ED5            ; {}
4EB5: 20 20           JR      NZ,$4ED7            ; {}
4EB7: 77              LD      (HL),A              
4EB8: 68              LD      L,B                 
4EB9: 61              LD      H,C                 
4EBA: 74              LD      (HL),H              
4EBB: 20 74           JR      NZ,$4F31            ; {}
4EBD: 68              LD      L,B                 
4EBE: 61              LD      H,C                 
4EBF: 74              LD      (HL),H              
4EC0: 20 6D           JR      NZ,$4F2F            ; {}
4EC2: 65              LD      H,L                 
4EC3: 61              LD      H,C                 
4EC4: 6E              LD      L,(HL)              
4EC5: 73              LD      (HL),E              
4EC6: 2C              INC     L                   
4EC7: 49              LD      C,C                 
4EC8: 5E              LD      E,(HL)              
4EC9: 6D              LD      L,L                 
4ECA: 20 6A           JR      NZ,$4F36            ; {}
4ECC: 75              LD      (HL),L              
4ECD: 73              LD      (HL),E              
4ECE: 74              LD      (HL),H              
4ECF: 20 61           JR      NZ,$4F32            ; {}
4ED1: 20 6B           JR      NZ,$4F3E            ; {}
4ED3: 69              LD      L,C                 
4ED4: 64              LD      H,H                 
4ED5: 21 FF 57        LD      HL,$57FF            
4ED8: 65              LD      H,L                 
4ED9: 6C              LD      L,H                 
4EDA: 6C              LD      L,H                 
4EDB: 2C              INC     L                   
4EDC: 20 69           JR      NZ,$4F47            ; {}
4EDE: 74              LD      (HL),H              
4EDF: 20 73           JR      NZ,$4F54            ; {}
4EE1: 65              LD      H,L                 
4EE2: 65              LD      H,L                 
4EE3: 6D              LD      L,L                 
4EE4: 73              LD      (HL),E              
4EE5: 20 20           JR      NZ,$4F07            ; {}
4EE7: 74              LD      (HL),H              
4EE8: 68              LD      L,B                 
4EE9: 61              LD      H,C                 
4EEA: 74              LD      (HL),H              
4EEB: 20 61           JR      NZ,$4F4E            ; {}
4EED: 66              LD      H,(HL)              
4EEE: 74              LD      (HL),H              
4EEF: 65              LD      H,L                 
4EF0: 72              LD      (HL),D              
4EF1: 20 79           JR      NZ,$4F6C            ; {}
4EF3: 6F              LD      L,A                 
4EF4: 75              LD      (HL),L              
4EF5: 20 20           JR      NZ,$4F17            ; {}
4EF7: 73              LD      (HL),E              
4EF8: 61              LD      H,C                 
4EF9: 76              HALT                        
4EFA: 65              LD      H,L                 
4EFB: 2C              INC     L                   
4EFC: 20 79           JR      NZ,$4F77            ; {}
4EFE: 6F              LD      L,A                 
4EFF: 75              LD      (HL),L              
4F00: 20 77           JR      NZ,$4F79            ; {}
4F02: 69              LD      L,C                 
4F03: 6C              LD      L,H                 
4F04: 6C              LD      L,H                 
4F05: 20 20           JR      NZ,$4F27            ; {}
4F07: 73              LD      (HL),E              
4F08: 74              LD      (HL),H              
4F09: 61              LD      H,C                 
4F0A: 72              LD      (HL),D              
4F0B: 74              LD      (HL),H              
4F0C: 20 61           JR      NZ,$4F6F            ; {}
4F0E: 74              LD      (HL),H              
4F0F: 20 74           JR      NZ,$4F85            ; {}
4F11: 68              LD      L,B                 
4F12: 65              LD      H,L                 
4F13: 20 20           JR      NZ,$4F35            ; {}
4F15: 20 20           JR      NZ,$4F37            ; {}
4F17: 6C              LD      L,H                 
4F18: 61              LD      H,C                 
4F19: 73              LD      (HL),E              
4F1A: 74              LD      (HL),H              
4F1B: 20 64           JR      NZ,$4F81            ; {}
4F1D: 6F              LD      L,A                 
4F1E: 6F              LD      L,A                 
4F1F: 72              LD      (HL),D              
4F20: 20 79           JR      NZ,$4F9B            ; {}
4F22: 6F              LD      L,A                 
4F23: 75              LD      (HL),L              
4F24: 20 20           JR      NZ,$4F46            ; {}
4F26: 20 77           JR      NZ,$4F9F            ; {}
4F28: 65              LD      H,L                 
4F29: 6E              LD      L,(HL)              
4F2A: 74              LD      (HL),H              
4F2B: 20 74           JR      NZ,$4FA1            ; {}
4F2D: 68              LD      L,B                 
4F2E: 72              LD      (HL),D              
4F2F: 6F              LD      L,A                 
4F30: 75              LD      (HL),L              
4F31: 67              LD      H,A                 
4F32: 68              LD      L,B                 
4F33: 2E 2E           LD      L,$2E               
4F35: 2E 20           LD      L,$20               
4F37: 49              LD      C,C                 
4F38: 5E              LD      E,(HL)              
4F39: 6D              LD      L,L                 
4F3A: 20 6E           JR      NZ,$4FAA            ; {}
4F3C: 6F              LD      L,A                 
4F3D: 74              LD      (HL),H              
4F3E: 20 72           JR      NZ,$4FB2            ; {}
4F40: 65              LD      H,L                 
4F41: 61              LD      H,C                 
4F42: 6C              LD      L,H                 
4F43: 6C              LD      L,H                 
4F44: 79              LD      A,C                 
4F45: 20 20           JR      NZ,$4F67            ; {}
4F47: 73              LD      (HL),E              
4F48: 75              LD      (HL),L              
4F49: 72              LD      (HL),D              
4F4A: 65              LD      H,L                 
4F4B: 20 77           JR      NZ,$4FC4            ; {}
4F4D: 68              LD      L,B                 
4F4E: 79              LD      A,C                 
4F4F: 20 74           JR      NZ,$4FC5            ; {}
4F51: 68              LD      L,B                 
4F52: 61              LD      H,C                 
4F53: 74              LD      (HL),H              
4F54: 20 69           JR      NZ,$4FBF            ; {}
4F56: 73              LD      (HL),E              
4F57: 5E              LD      E,(HL)              
4F58: 63              LD      H,E                 
4F59: 61              LD      H,C                 
4F5A: 75              LD      (HL),L              
4F5B: 73              LD      (HL),E              
4F5C: 65              LD      H,L                 
4F5D: 20 49           JR      NZ,$4FA8            ; {}
4F5F: 5E              LD      E,(HL)              
4F60: 6D              LD      L,L                 
4F61: 20 6A           JR      NZ,$4FCD            ; {}
4F63: 75              LD      (HL),L              
4F64: 73              LD      (HL),E              
4F65: 74              LD      (HL),H              
4F66: 20 61           JR      NZ,$4FC9            ; {}
4F68: 20 6B           JR      NZ,$4FD5            ; {}
4F6A: 69              LD      L,C                 
4F6B: 64              LD      H,H                 
4F6C: 21 FF 49        LD      HL,$49FF            
4F6F: 20 68           JR      NZ,$4FD9            ; {}
4F71: 65              LD      H,L                 
4F72: 61              LD      H,C                 
4F73: 72              LD      (HL),D              
4F74: 64              LD      H,H                 
4F75: 20 74           JR      NZ,$4FEB            ; {}
4F77: 68              LD      L,B                 
4F78: 61              LD      H,C                 
4F79: 74              LD      (HL),H              
4F7A: 20 79           JR      NZ,$4FF5            ; {}
4F7C: 6F              LD      L,A                 
4F7D: 75              LD      (HL),L              
4F7E: 63              LD      H,E                 
4F7F: 61              LD      H,C                 
4F80: 6E              LD      L,(HL)              
4F81: 20 70           JR      NZ,$4FF3            ; {}
4F83: 72              LD      (HL),D              
4F84: 65              LD      H,L                 
4F85: 73              LD      (HL),E              
4F86: 73              LD      (HL),E              
4F87: 20 53           JR      NZ,$4FDC            ; {}
4F89: 45              LD      B,L                 
4F8A: 4C              LD      C,H                 
4F8B: 45              LD      B,L                 
4F8C: 43              LD      B,E                 
4F8D: 54              LD      D,H                 
4F8E: 74              LD      (HL),H              
4F8F: 6F              LD      L,A                 
4F90: 20 6C           JR      NZ,$4FFE            ; {}
4F92: 6F              LD      L,A                 
4F93: 6F              LD      L,A                 
4F94: 6B              LD      L,E                 
4F95: 20 61           JR      NZ,$4FF8            ; {}
4F97: 74              LD      (HL),H              
4F98: 20 74           JR      NZ,$500E            ; {}
4F9A: 68              LD      L,B                 
4F9B: 65              LD      H,L                 
4F9C: 20 20           JR      NZ,$4FBE            ; {}
4F9E: 69              LD      L,C                 
4F9F: 73              LD      (HL),E              
4FA0: 6C              LD      L,H                 
4FA1: 61              LD      H,C                 
4FA2: 6E              LD      L,(HL)              
4FA3: 64              LD      H,H                 
4FA4: 20 6D           JR      NZ,$5013            ; {}
4FA6: 61              LD      H,C                 
4FA7: 70              LD      (HL),B              
4FA8: 2E 2E           LD      L,$2E               
4FAA: 2E 20           LD      L,$20               
4FAC: 20 20           JR      NZ,$4FCE            ; {}
4FAE: 42              LD      B,D                 
4FAF: 75              LD      (HL),L              
4FB0: 74              LD      (HL),H              
4FB1: 2C              INC     L                   
4FB2: 20 49           JR      NZ,$4FFD            ; {}
4FB4: 20 64           JR      NZ,$501A            ; {}
4FB6: 6F              LD      L,A                 
4FB7: 6E              LD      L,(HL)              
4FB8: 5E              LD      E,(HL)              
4FB9: 74              LD      (HL),H              
4FBA: 20 20           JR      NZ,$4FDC            ; {}
4FBC: 20 20           JR      NZ,$4FDE            ; {}
4FBE: 75              LD      (HL),L              
4FBF: 6E              LD      L,(HL)              
4FC0: 64              LD      H,H                 
4FC1: 65              LD      H,L                 
4FC2: 72              LD      (HL),D              
4FC3: 73              LD      (HL),E              
4FC4: 74              LD      (HL),H              
4FC5: 61              LD      H,C                 
4FC6: 6E              LD      L,(HL)              
4FC7: 64              LD      H,H                 
4FC8: 20 77           JR      NZ,$5041            ; {}
4FCA: 68              LD      L,B                 
4FCB: 61              LD      H,C                 
4FCC: 74              LD      (HL),H              
4FCD: 20 74           JR      NZ,$5043            ; {}
4FCF: 68              LD      L,B                 
4FD0: 65              LD      H,L                 
4FD1: 79              LD      A,C                 
4FD2: 20 6D           JR      NZ,$5041            ; {}
4FD4: 65              LD      H,L                 
4FD5: 61              LD      H,C                 
4FD6: 6E              LD      L,(HL)              
4FD7: 20 62           JR      NZ,$503B            ; {}
4FD9: 79              LD      A,C                 
4FDA: 20 20           JR      NZ,$4FFC            ; {}
4FDC: 20 20           JR      NZ,$4FFE            ; {}
4FDE: 74              LD      (HL),H              
4FDF: 68              LD      L,B                 
4FE0: 61              LD      H,C                 
4FE1: 74              LD      (HL),H              
4FE2: 2E 2E           LD      L,$2E               
4FE4: 2E FF           LD      L,$FF               
4FE6: 57              LD      D,A                 
4FE7: 68              LD      L,B                 
4FE8: 65              LD      H,L                 
4FE9: 6E              LD      L,(HL)              
4FEA: 20 79           JR      NZ,$5065            ; {}
4FEC: 6F              LD      L,A                 
4FED: 75              LD      (HL),L              
4FEE: 5E              LD      E,(HL)              
4FEF: 72              LD      (HL),D              
4FF0: 65              LD      H,L                 
4FF1: 20 20           JR      NZ,$5013            ; {}
4FF3: 20 20           JR      NZ,$5015            ; {}
4FF5: 20 72           JR      NZ,$5069            ; {}
4FF7: 75              LD      (HL),L              
4FF8: 6E              LD      L,(HL)              
4FF9: 6E              LD      L,(HL)              
4FFA: 69              LD      L,C                 
4FFB: 6E              LD      L,(HL)              
4FFC: 67              LD      H,A                 
4FFD: 20 6F           JR      NZ,$506E            ; {}
4FFF: 75              LD      (HL),L              
5000: 74              LD      (HL),H              
5001: 20 6F           JR      NZ,$5072            ; {}
5003: 66              LD      H,(HL)              
5004: 20 20           JR      NZ,$5026            ; {}
5006: 48              LD      C,B                 
5007: 65              LD      H,L                 
5008: 61              LD      H,C                 
5009: 72              LD      (HL),D              
500A: 74              LD      (HL),H              
500B: 73              LD      (HL),E              
500C: 2C              INC     L                   
500D: 20 79           JR      NZ,$5088            ; {}
500F: 6F              LD      L,A                 
5010: 75              LD      (HL),L              
5011: 5E              LD      E,(HL)              
5012: 64              LD      H,H                 
5013: 20 20           JR      NZ,$5035            ; {}
5015: 20 62           JR      NZ,$5079            ; {}
5017: 65              LD      H,L                 
5018: 74              LD      (HL),H              
5019: 74              LD      (HL),H              
501A: 65              LD      H,L                 
501B: 72              LD      (HL),D              
501C: 20 65           JR      NZ,$5083            ; {}
501E: 6E              LD      L,(HL)              
501F: 74              LD      (HL),H              
5020: 65              LD      H,L                 
5021: 72              LD      (HL),D              
5022: 20 61           JR      NZ,$5085            ; {}
5024: 20 20           JR      NZ,$5046            ; {}
5026: 68              LD      L,B                 
5027: 6F              LD      L,A                 
5028: 75              LD      (HL),L              
5029: 73              LD      (HL),E              
502A: 65              LD      H,L                 
502B: 20 6F           JR      NZ,$509C            ; {}
502D: 72              LD      (HL),D              
502E: 20 63           JR      NZ,$5093            ; {}
5030: 61              LD      H,C                 
5031: 76              HALT                        
5032: 65              LD      H,L                 
5033: 2E 2E           LD      L,$2E               
5035: 2E 57           LD      L,$57               
5037: 68              LD      L,B                 
5038: 79              LD      A,C                 
5039: 3F              CCF                         
503A: 20 20           JR      NZ,$505C            ; {}
503C: 49              LD      C,C                 
503D: 20 68           JR      NZ,$50A7            ; {}
503F: 61              LD      H,C                 
5040: 76              HALT                        
5041: 65              LD      H,L                 
5042: 20 6E           JR      NZ,$50B2            ; {}
5044: 6F              LD      L,A                 
5045: 20 69           JR      NZ,$50B0            ; {}
5047: 64              LD      H,H                 
5048: 65              LD      H,L                 
5049: 61              LD      H,C                 
504A: 2C              INC     L                   
504B: 20 49           JR      NZ,$5096            ; {}
504D: 5E              LD      E,(HL)              
504E: 6D              LD      L,L                 
504F: 20 6A           JR      NZ,$50BB            ; {}
5051: 75              LD      (HL),L              
5052: 73              LD      (HL),E              
5053: 74              LD      (HL),H              
5054: 20 61           JR      NZ,$50B7            ; {}
5056: 6B              LD      L,E                 
5057: 69              LD      L,C                 
5058: 64              LD      H,H                 
5059: 21 FF 48        LD      HL,$48FF            
505C: 65              LD      H,L                 
505D: 79              LD      A,C                 
505E: 2C              INC     L                   
505F: 20 64           JR      NZ,$50C5            ; {}
5061: 75              LD      (HL),L              
5062: 64              LD      H,H                 
5063: 65              LD      H,L                 
5064: 21 20 57        LD      HL,$5720            
5067: 68              LD      L,B                 
5068: 61              LD      H,C                 
5069: 74              LD      (HL),H              
506A: 20 64           JR      NZ,$50D0            ; {}
506C: 6F              LD      L,A                 
506D: 20 79           JR      NZ,$50E8            ; {}
506F: 6F              LD      L,A                 
5070: 75              LD      (HL),L              
5071: 20 74           JR      NZ,$50E7            ; {}
5073: 68              LD      L,B                 
5074: 69              LD      L,C                 
5075: 6E              LD      L,(HL)              
5076: 6B              LD      L,E                 
5077: 20 6F           JR      NZ,$50E8            ; {}
5079: 66              LD      H,(HL)              
507A: 20 4D           JR      NZ,$50C9            ; {}
507C: 61              LD      H,C                 
507D: 72              LD      (HL),D              
507E: 69              LD      L,C                 
507F: 6E              LD      L,(HL)              
5080: 3F              CCF                         
5081: 20 20           JR      NZ,$50A3            ; {}
5083: 55              LD      D,L                 
5084: 68              LD      L,B                 
5085: 68              LD      L,B                 
5086: 2E 2E           LD      L,$2E               
5088: 2E 20           LD      L,$20               
508A: 20 49           JR      NZ,$50D5            ; {}
508C: 20 64           JR      NZ,$50F2            ; {}
508E: 6F              LD      L,A                 
508F: 6E              LD      L,(HL)              
5090: 5E              LD      E,(HL)              
5091: 74              LD      (HL),H              
5092: 20 6B           JR      NZ,$50FF            ; {}
5094: 6E              LD      L,(HL)              
5095: 6F              LD      L,A                 
5096: 77              LD      (HL),A              
5097: 2C              INC     L                   
5098: 20 20           JR      NZ,$50BA            ; {}
509A: 20 49           JR      NZ,$50E5            ; {}
509C: 5E              LD      E,(HL)              
509D: 6D              LD      L,L                 
509E: 20 6A           JR      NZ,$510A            ; {}
50A0: 75              LD      (HL),L              
50A1: 73              LD      (HL),E              
50A2: 74              LD      (HL),H              
50A3: 20 61           JR      NZ,$5106            ; {}
50A5: 20 6B           JR      NZ,$5112            ; {}
50A7: 69              LD      L,C                 
50A8: 64              LD      H,H                 
50A9: 21 FF 57        LD      HL,$57FF            
50AC: 68              LD      L,B                 
50AD: 65              LD      H,L                 
50AE: 72              LD      (HL),D              
50AF: 65              LD      H,L                 
50B0: 20 61           JR      NZ,$5113            ; {}
50B2: 72              LD      (HL),D              
50B3: 65              LD      H,L                 
50B4: 20 79           JR      NZ,$512F            ; {}
50B6: 6F              LD      L,A                 
50B7: 75              LD      (HL),L              
50B8: 20 20           JR      NZ,$50DA            ; {}
50BA: 20 66           JR      NZ,$5122            ; {}
50BC: 72              LD      (HL),D              
50BD: 6F              LD      L,A                 
50BE: 6D              LD      L,L                 
50BF: 2C              INC     L                   
50C0: 20 62           JR      NZ,$5124            ; {}
50C2: 72              LD      (HL),D              
50C3: 6F              LD      L,A                 
50C4: 74              LD      (HL),H              
50C5: 68              LD      L,B                 
50C6: 65              LD      H,L                 
50C7: 72              LD      (HL),D              
50C8: 3F              CCF                         
50C9: 20 20           JR      NZ,$50EB            ; {}
50CB: 2E 2E           LD      L,$2E               
50CD: 2E 4F           LD      L,$4F               
50CF: 75              LD      (HL),L              
50D0: 74              LD      (HL),H              
50D1: 73              LD      (HL),E              
50D2: 69              LD      L,C                 
50D3: 64              LD      H,H                 
50D4: 65              LD      H,L                 
50D5: 20 74           JR      NZ,$514B            ; {}
50D7: 68              LD      L,B                 
50D8: 65              LD      H,L                 
50D9: 20 20           JR      NZ,$50FB            ; {}
50DB: 69              LD      L,C                 
50DC: 73              LD      (HL),E              
50DD: 6C              LD      L,H                 
50DE: 61              LD      H,C                 
50DF: 6E              LD      L,(HL)              
50E0: 64              LD      H,H                 
50E1: 3F              CCF                         
50E2: 20 20           JR      NZ,$5104            ; {}
50E4: 57              LD      D,A                 
50E5: 68              LD      L,B                 
50E6: 61              LD      H,C                 
50E7: 74              LD      (HL),H              
50E8: 20 69           JR      NZ,$5153            ; {}
50EA: 73              LD      (HL),E              
50EB: 5E              LD      E,(HL)              
50EC: 6F              LD      L,A                 
50ED: 75              LD      (HL),L              
50EE: 74              LD      (HL),H              
50EF: 73              LD      (HL),E              
50F0: 69              LD      L,C                 
50F1: 64              LD      H,H                 
50F2: 65              LD      H,L                 
50F3: 3F              CCF                         
50F4: 5E              LD      E,(HL)              
50F5: 20 20           JR      NZ,$5117            ; {}
50F7: 49              LD      C,C                 
50F8: 5E              LD      E,(HL)              
50F9: 76              HALT                        
50FA: 65              LD      H,L                 
50FB: 6E              LD      L,(HL)              
50FC: 65              LD      H,L                 
50FD: 76              HALT                        
50FE: 65              LD      H,L                 
50FF: 72              LD      (HL),D              
5100: 20 74           JR      NZ,$5176            ; {}
5102: 68              LD      L,B                 
5103: 6F              LD      L,A                 
5104: 75              LD      (HL),L              
5105: 67              LD      H,A                 
5106: 68              LD      L,B                 
5107: 74              LD      (HL),H              
5108: 20 20           JR      NZ,$512A            ; {}
510A: 20 61           JR      NZ,$516D            ; {}
510C: 62              LD      H,D                 
510D: 6F              LD      L,A                 
510E: 75              LD      (HL),L              
510F: 74              LD      (HL),H              
5110: 20 69           JR      NZ,$517B            ; {}
5112: 74              LD      (HL),H              
5113: 2E 2E           LD      L,$2E               
5115: 2E FF           LD      L,$FF               
5117: 54              LD      D,H                 
5118: 68              LD      L,B                 
5119: 65              LD      H,L                 
511A: 20 67           JR      NZ,$5183            ; {}
511C: 69              LD      L,C                 
511D: 61              LD      H,C                 
511E: 6E              LD      L,(HL)              
511F: 74              LD      (HL),H              
5120: 20 65           JR      NZ,$5187            ; {}
5122: 67              LD      H,A                 
5123: 67              LD      H,A                 
5124: 20 6F           JR      NZ,$5195            ; {}
5126: 6E              LD      L,(HL)              
5127: 74              LD      (HL),H              
5128: 6F              LD      L,A                 
5129: 70              LD      (HL),B              
512A: 20 54           JR      NZ,$5180            ; {}
512C: 61              LD      H,C                 
512D: 6D              LD      L,L                 
512E: 61              LD      H,C                 
512F: 72              LD      (HL),D              
5130: 61              LD      H,C                 
5131: 6E              LD      L,(HL)              
5132: 63              LD      H,E                 
5133: 68              LD      L,B                 
5134: 20 20           JR      NZ,$5156            ; {}
5136: 20 4D           JR      NZ,$5185            ; {}
5138: 6F              LD      L,A                 
5139: 75              LD      (HL),L              
513A: 6E              LD      L,(HL)              
513B: 74              LD      (HL),H              
513C: 61              LD      H,C                 
513D: 69              LD      L,C                 
513E: 6E              LD      L,(HL)              
513F: 3F              CCF                         
5140: 20 20           JR      NZ,$5162            ; {}
5142: 54              LD      D,H                 
5143: 68              LD      L,B                 
5144: 65              LD      H,L                 
5145: 79              LD      A,C                 
5146: 20 73           JR      NZ,$51BB            ; {}
5148: 61              LD      H,C                 
5149: 79              LD      A,C                 
514A: 20 74           JR      NZ,$51C0            ; {}
514C: 68              LD      L,B                 
514D: 65              LD      H,L                 
514E: 20 57           JR      NZ,$51A7            ; {}
5150: 69              LD      L,C                 
5151: 6E              LD      L,(HL)              
5152: 64              LD      H,H                 
5153: 20 20           JR      NZ,$5175            ; {}
5155: 20 20           JR      NZ,$5177            ; {}
5157: 46              LD      B,(HL)              
5158: 69              LD      L,C                 
5159: 73              LD      (HL),E              
515A: 68              LD      L,B                 
515B: 20 69           JR      NZ,$51C6            ; {}
515D: 73              LD      (HL),E              
515E: 20 73           JR      NZ,$51D3            ; {}
5160: 6C              LD      L,H                 
5161: 65              LD      H,L                 
5162: 65              LD      H,L                 
5163: 70              LD      (HL),B              
5164: 69              LD      L,C                 
5165: 6E              LD      L,(HL)              
5166: 67              LD      H,A                 
5167: 69              LD      L,C                 
5168: 6E              LD      L,(HL)              
5169: 73              LD      (HL),E              
516A: 69              LD      L,C                 
516B: 64              LD      H,H                 
516C: 65              LD      H,L                 
516D: 20 6F           JR      NZ,$51DE            ; {}
516F: 66              LD      H,(HL)              
5170: 20 69           JR      NZ,$51DB            ; {}
5172: 74              LD      (HL),H              
5173: 2E 2E           LD      L,$2E               
5175: 2E 20           LD      L,$20               
5177: 57              LD      D,A                 
5178: 68              LD      L,B                 
5179: 79              LD      A,C                 
517A: 3F              CCF                         
517B: 20 20           JR      NZ,$519D            ; {}
517D: 49              LD      C,C                 
517E: 20 64           JR      NZ,$51E4            ; {}
5180: 6F              LD      L,A                 
5181: 6E              LD      L,(HL)              
5182: 5E              LD      E,(HL)              
5183: 74              LD      (HL),H              
5184: 20 20           JR      NZ,$51A6            ; {}
5186: 20 6B           JR      NZ,$51F3            ; {}
5188: 6E              LD      L,(HL)              
5189: 6F              LD      L,A                 
518A: 77              LD      (HL),A              
518B: 20 65           JR      NZ,$51F2            ; {}
518D: 69              LD      L,C                 
518E: 74              LD      (HL),H              
518F: 68              LD      L,B                 
5190: 65              LD      H,L                 
5191: 72              LD      (HL),D              
5192: 2E 2E           LD      L,$2E               
5194: 2E FF           LD      L,$FF               
5196: 44              LD      B,H                 
5197: 75              LD      (HL),L              
5198: 64              LD      H,H                 
5199: 65              LD      H,L                 
519A: 21 20 20        LD      HL,$2020            
519D: 59              LD      E,C                 
519E: 6F              LD      L,A                 
519F: 75              LD      (HL),L              
51A0: 5E              LD      E,(HL)              
51A1: 72              LD      (HL),D              
51A2: 65              LD      H,L                 
51A3: 20 20           JR      NZ,$51C5            ; {}
51A5: 20 61           JR      NZ,$5208            ; {}
51A7: 73              LD      (HL),E              
51A8: 6B              LD      L,E                 
51A9: 69              LD      L,C                 
51AA: 6E              LD      L,(HL)              
51AB: 67              LD      H,A                 
51AC: 20 6D           JR      NZ,$521B            ; {}
51AE: 65              LD      H,L                 
51AF: 20 77           JR      NZ,$5228            ; {}
51B1: 68              LD      L,B                 
51B2: 65              LD      H,L                 
51B3: 6E              LD      L,(HL)              
51B4: 20 20           JR      NZ,$51D6            ; {}
51B6: 77              LD      (HL),A              
51B7: 65              LD      H,L                 
51B8: 20 73           JR      NZ,$522D            ; {}
51BA: 74              LD      (HL),H              
51BB: 61              LD      H,C                 
51BC: 72              LD      (HL),D              
51BD: 74              LD      (HL),H              
51BE: 65              LD      H,L                 
51BF: 64              LD      H,H                 
51C0: 20 74           JR      NZ,$5236            ; {}
51C2: 6F              LD      L,A                 
51C3: 20 20           JR      NZ,$51E5            ; {}
51C5: 20 6C           JR      NZ,$5233            ; {}
51C7: 69              LD      L,C                 
51C8: 76              HALT                        
51C9: 65              LD      H,L                 
51CA: 20 6F           JR      NZ,$523B            ; {}
51CC: 6E              LD      L,(HL)              
51CD: 20 74           JR      NZ,$5243            ; {}
51CF: 68              LD      L,B                 
51D0: 69              LD      L,C                 
51D1: 73              LD      (HL),E              
51D2: 20 20           JR      NZ,$51F4            ; {}
51D4: 20 20           JR      NZ,$51F6            ; {}
51D6: 69              LD      L,C                 
51D7: 73              LD      (HL),E              
51D8: 6C              LD      L,H                 
51D9: 61              LD      H,C                 
51DA: 6E              LD      L,(HL)              
51DB: 64              LD      H,H                 
51DC: 3F              CCF                         
51DD: 20 20           JR      NZ,$51FF            ; {}
51DF: 57              LD      D,A                 
51E0: 68              LD      L,B                 
51E1: 61              LD      H,C                 
51E2: 74              LD      (HL),H              
51E3: 20 64           JR      NZ,$5249            ; {}
51E5: 6F              LD      L,A                 
51E6: 79              LD      A,C                 
51E7: 6F              LD      L,A                 
51E8: 75              LD      (HL),L              
51E9: 20 6D           JR      NZ,$5258            ; {}
51EB: 65              LD      H,L                 
51EC: 61              LD      H,C                 
51ED: 6E              LD      L,(HL)              
51EE: 20 62           JR      NZ,$5252            ; {}
51F0: 79              LD      A,C                 
51F1: 20 20           JR      NZ,$5213            ; {}
51F3: 20 20           JR      NZ,$5215            ; {}
51F5: 20 5E           JR      NZ,$5255            ; {}
51F7: 77              LD      (HL),A              
51F8: 68              LD      L,B                 
51F9: 65              LD      H,L                 
51FA: 6E              LD      L,(HL)              
51FB: 3F              CCF                         
51FC: 5E              LD      E,(HL)              
51FD: 20 20           JR      NZ,$521F            ; {}
51FF: 57              LD      D,A                 
5200: 68              LD      L,B                 
5201: 6F              LD      L,A                 
5202: 61              LD      H,C                 
5203: 21 20 20        LD      HL,$2020            
5206: 54              LD      D,H                 
5207: 68              LD      L,B                 
5208: 65              LD      H,L                 
5209: 20 63           JR      NZ,$526E            ; {}
520B: 6F              LD      L,A                 
520C: 6E              LD      L,(HL)              
520D: 63              LD      H,E                 
520E: 65              LD      H,L                 
520F: 70              LD      (HL),B              
5210: 74              LD      (HL),H              
5211: 20 6A           JR      NZ,$527D            ; {}
5213: 75              LD      (HL),L              
5214: 73              LD      (HL),E              
5215: 74              LD      (HL),H              
5216: 6D              LD      L,L                 
5217: 61              LD      H,C                 
5218: 6B              LD      L,E                 
5219: 65              LD      H,L                 
521A: 73              LD      (HL),E              
521B: 20 6D           JR      NZ,$528A            ; {}
521D: 79              LD      A,C                 
521E: 20 68           JR      NZ,$5288            ; {}
5220: 65              LD      H,L                 
5221: 61              LD      H,C                 
5222: 64              LD      H,H                 
5223: 20 20           JR      NZ,$5245            ; {}
5225: 20 68           JR      NZ,$528F            ; {}
5227: 75              LD      (HL),L              
5228: 72              LD      (HL),D              
5229: 74              LD      (HL),H              
522A: 21 FF 4D        LD      HL,$4DFF            
522D: 61              LD      H,C                 
522E: 72              LD      (HL),D              
522F: 69              LD      L,C                 
5230: 6E              LD      L,(HL)              
5231: 3F              CCF                         
5232: 20 53           JR      NZ,$5287            ; {}
5234: 68              LD      L,B                 
5235: 65              LD      H,L                 
5236: 20 6C           JR      NZ,$52A4            ; {}
5238: 69              LD      L,C                 
5239: 6B              LD      L,E                 
523A: 65              LD      H,L                 
523B: 73              LD      (HL),E              
523C: 74              LD      (HL),H              
523D: 6F              LD      L,A                 
523E: 20 67           JR      NZ,$52A7            ; {}
5240: 6F              LD      L,A                 
5241: 20 73           JR      NZ,$52B6            ; {}
5243: 74              LD      (HL),H              
5244: 61              LD      H,C                 
5245: 72              LD      (HL),D              
5246: 65              LD      H,L                 
5247: 20 61           JR      NZ,$52AA            ; {}
5249: 74              LD      (HL),H              
524A: 20 20           JR      NZ,$526C            ; {}
524C: 74              LD      (HL),H              
524D: 68              LD      L,B                 
524E: 65              LD      H,L                 
524F: 20 6F           JR      NZ,$52C0            ; {}
5251: 63              LD      H,E                 
5252: 65              LD      H,L                 
5253: 61              LD      H,C                 
5254: 6E              LD      L,(HL)              
5255: 20 61           JR      NZ,$52B8            ; {}
5257: 6C              LD      L,H                 
5258: 6C              LD      L,H                 
5259: 20 62           JR      NZ,$52BD            ; {}
525B: 79              LD      A,C                 
525C: 68              LD      L,B                 
525D: 65              LD      H,L                 
525E: 72              LD      (HL),D              
525F: 73              LD      (HL),E              
5260: 65              LD      H,L                 
5261: 6C              LD      L,H                 
5262: 66              LD      H,(HL)              
5263: 2E 2E           LD      L,$2E               
5265: 2E 20           LD      L,$20               
5267: 20 57           JR      NZ,$52C0            ; {}
5269: 68              LD      L,B                 
526A: 79              LD      A,C                 
526B: 3F              CCF                         
526C: 48              LD      C,B                 
526D: 65              LD      H,L                 
526E: 79              LD      A,C                 
526F: 2C              INC     L                   
5270: 20 49           JR      NZ,$52BB            ; {}
5272: 5E              LD      E,(HL)              
5273: 6D              LD      L,L                 
5274: 20 6A           JR      NZ,$52E0            ; {}
5276: 75              LD      (HL),L              
5277: 73              LD      (HL),E              
5278: 74              LD      (HL),H              
5279: 20 61           JR      NZ,$52DC            ; {}
527B: 20 6B           JR      NZ,$52E8            ; {}
527D: 69              LD      L,C                 
527E: 64              LD      H,H                 
527F: 2C              INC     L                   
5280: 20 64           JR      NZ,$52E6            ; {}
5282: 6F              LD      L,A                 
5283: 6E              LD      L,(HL)              
5284: 5E              LD      E,(HL)              
5285: 74              LD      (HL),H              
5286: 20 61           JR      NZ,$52E9            ; {}
5288: 73              LD      (HL),E              
5289: 6B              LD      L,E                 
528A: 20 20           JR      NZ,$52AC            ; {}
528C: 6D              LD      L,L                 
528D: 65              LD      H,L                 
528E: 21 FF 48        LD      HL,$48FF            
5291: 65              LD      H,L                 
5292: 79              LD      A,C                 
5293: 2E 2E           LD      L,$2E               
5295: 2E 20           LD      L,$20               
5297: 57              LD      D,A                 
5298: 68              LD      L,B                 
5299: 65              LD      H,L                 
529A: 72              LD      (HL),D              
529B: 65              LD      H,L                 
529C: 5E              LD      E,(HL)              
529D: 72              LD      (HL),D              
529E: 65              LD      H,L                 
529F: 20 79           JR      NZ,$531A            ; {}
52A1: 6F              LD      L,A                 
52A2: 75              LD      (HL),L              
52A3: 20 74           JR      NZ,$5319            ; {}
52A5: 77              LD      (HL),A              
52A6: 6F              LD      L,A                 
52A7: 20 67           JR      NZ,$5310            ; {}
52A9: 6F              LD      L,A                 
52AA: 69              LD      L,C                 
52AB: 6E              LD      L,(HL)              
52AC: 67              LD      H,A                 
52AD: 20 20           JR      NZ,$52CF            ; {}
52AF: 20 74           JR      NZ,$5325            ; {}
52B1: 6F              LD      L,A                 
52B2: 67              LD      H,A                 
52B3: 65              LD      H,L                 
52B4: 74              LD      (HL),H              
52B5: 68              LD      L,B                 
52B6: 65              LD      H,L                 
52B7: 72              LD      (HL),D              
52B8: 3F              CCF                         
52B9: 20 20           JR      NZ,$52DB            ; {}
52BB: 48              LD      C,B                 
52BC: 75              LD      (HL),L              
52BD: 6E              LD      L,(HL)              
52BE: 68              LD      L,B                 
52BF: 3F              CCF                         
52C0: 55              LD      D,L                 
52C1: 68              LD      L,B                 
52C2: 2C              INC     L                   
52C3: 20 49           JR      NZ,$530E            ; {}
52C5: 20 64           JR      NZ,$532B            ; {}
52C7: 69              LD      L,C                 
52C8: 64              LD      H,H                 
52C9: 6E              LD      L,(HL)              
52CA: 5E              LD      E,(HL)              
52CB: 74              LD      (HL),H              
52CC: 20 20           JR      NZ,$52EE            ; {}
52CE: 20 20           JR      NZ,$52F0            ; {}
52D0: 6D              LD      L,L                 
52D1: 65              LD      H,L                 
52D2: 61              LD      H,C                 
52D3: 6E              LD      L,(HL)              
52D4: 20 61           JR      NZ,$5337            ; {}
52D6: 6E              LD      L,(HL)              
52D7: 79              LD      A,C                 
52D8: 74              LD      (HL),H              
52D9: 68              LD      L,B                 
52DA: 69              LD      L,C                 
52DB: 6E              LD      L,(HL)              
52DC: 67              LD      H,A                 
52DD: 2E 2E           LD      L,$2E               
52DF: 2E 49           LD      L,$49               
52E1: 5E              LD      E,(HL)              
52E2: 6D              LD      L,L                 
52E3: 20 6A           JR      NZ,$534F            ; {}
52E5: 75              LD      (HL),L              
52E6: 73              LD      (HL),E              
52E7: 74              LD      (HL),H              
52E8: 20 61           JR      NZ,$534B            ; {}
52EA: 20 6B           JR      NZ,$5357            ; {}
52EC: 69              LD      L,C                 
52ED: 64              LD      H,H                 
52EE: 21 FF 48        LD      HL,$48FF            
52F1: 65              LD      H,L                 
52F2: 79              LD      A,C                 
52F3: 20 68           JR      NZ,$535D            ; {}
52F5: 65              LD      H,L                 
52F6: 79              LD      A,C                 
52F7: 2C              INC     L                   
52F8: 20 62           JR      NZ,$535C            ; {}
52FA: 72              LD      (HL),D              
52FB: 6F              LD      L,A                 
52FC: 21 20 20        LD      HL,$2020            
52FF: 20 41           JR      NZ,$5342            ; {}
5301: 62              LD      H,D                 
5302: 6F              LD      L,A                 
5303: 75              LD      (HL),L              
5304: 74              LD      (HL),H              
5305: 20 74           JR      NZ,$537B            ; {}
5307: 68              LD      L,B                 
5308: 65              LD      H,L                 
5309: 20 44           JR      NZ,$534F            ; {}
530B: 72              LD      (HL),D              
530C: 65              LD      H,L                 
530D: 61              LD      H,C                 
530E: 6D              LD      L,L                 
530F: 20 53           JR      NZ,$5364            ; {}
5311: 68              LD      L,B                 
5312: 72              LD      (HL),D              
5313: 69              LD      L,C                 
5314: 6E              LD      L,(HL)              
5315: 65              LD      H,L                 
5316: 20 74           JR      NZ,$538C            ; {}
5318: 68              LD      L,B                 
5319: 65              LD      H,L                 
531A: 72              LD      (HL),D              
531B: 65              LD      H,L                 
531C: 2E 2E           LD      L,$2E               
531E: 2E 20           LD      L,$20               
5320: 54              LD      D,H                 
5321: 68              LD      L,B                 
5322: 65              LD      H,L                 
5323: 79              LD      A,C                 
5324: 20 73           JR      NZ,$5399            ; {}
5326: 61              LD      H,C                 
5327: 79              LD      A,C                 
5328: 20 74           JR      NZ,$539E            ; {}
532A: 68              LD      L,B                 
532B: 65              LD      H,L                 
532C: 72              LD      (HL),D              
532D: 65              LD      H,L                 
532E: 5E              LD      E,(HL)              
532F: 73              LD      (HL),E              
5330: 73              LD      (HL),E              
5331: 6F              LD      L,A                 
5332: 6D              LD      L,L                 
5333: 65              LD      H,L                 
5334: 74              LD      (HL),H              
5335: 68              LD      L,B                 
5336: 69              LD      L,C                 
5337: 6E              LD      L,(HL)              
5338: 67              LD      H,A                 
5339: 20 67           JR      NZ,$53A2            ; {}
533B: 6F              LD      L,A                 
533C: 6F              LD      L,A                 
533D: 64              LD      H,H                 
533E: 20 20           JR      NZ,$5360            ; {}
5340: 69              LD      L,C                 
5341: 6E              LD      L,(HL)              
5342: 73              LD      (HL),E              
5343: 69              LD      L,C                 
5344: 64              LD      H,H                 
5345: 65              LD      H,L                 
5346: 2E 2E           LD      L,$2E               
5348: 2E 20           LD      L,$20               
534A: 2E 2E           LD      L,$2E               
534C: 2E 20           LD      L,$20               
534E: 20 20           JR      NZ,$5370            ; {}
5350: 49              LD      C,C                 
5351: 20 62           JR      NZ,$53B5            ; {}
5353: 65              LD      H,L                 
5354: 74              LD      (HL),H              
5355: 74              LD      (HL),H              
5356: 65              LD      H,L                 
5357: 72              LD      (HL),D              
5358: 20 6E           JR      NZ,$53C8            ; {}
535A: 6F              LD      L,A                 
535B: 74              LD      (HL),H              
535C: 20 73           JR      NZ,$53D1            ; {}
535E: 61              LD      H,C                 
535F: 79              LD      A,C                 
5360: 61              LD      H,C                 
5361: 6E              LD      L,(HL)              
5362: 79              LD      A,C                 
5363: 74              LD      (HL),H              
5364: 68              LD      L,B                 
5365: 69              LD      L,C                 
5366: 6E              LD      L,(HL)              
5367: 67              LD      H,A                 
5368: 20 65           JR      NZ,$53CF            ; {}
536A: 6C              LD      L,H                 
536B: 73              LD      (HL),E              
536C: 65              LD      H,L                 
536D: 20 20           JR      NZ,$538F            ; {}
536F: 20 61           JR      NZ,$53D2            ; {}
5371: 73              LD      (HL),E              
5372: 20 49           JR      NZ,$53BD            ; {}
5374: 5E              LD      E,(HL)              
5375: 6D              LD      L,L                 
5376: 20 6A           JR      NZ,$53E2            ; {}
5378: 75              LD      (HL),L              
5379: 73              LD      (HL),E              
537A: 74              LD      (HL),H              
537B: 20 61           JR      NZ,$53DE            ; {}
537D: 20 20           JR      NZ,$539F            ; {}
537F: 20 6B           JR      NZ,$53EC            ; {}
5381: 69              LD      L,C                 
5382: 64              LD      H,H                 
5383: 21 FF 48        LD      HL,$48FF            
5386: 75              LD      (HL),L              
5387: 6E              LD      L,(HL)              
5388: 68              LD      L,B                 
5389: 3F              CCF                         
538A: 21 20 20        LD      HL,$2020            
538D: 4D              LD      C,L                 
538E: 61              LD      H,C                 
538F: 72              LD      (HL),D              
5390: 69              LD      L,C                 
5391: 6E              LD      L,(HL)              
5392: 5E              LD      E,(HL)              
5393: 73              LD      (HL),E              
5394: 20 6E           JR      NZ,$5404            ; {}
5396: 6F              LD      L,A                 
5397: 74              LD      (HL),H              
5398: 20 77           JR      NZ,$5411            ; {}
539A: 69              LD      L,C                 
539B: 74              LD      (HL),H              
539C: 68              LD      L,B                 
539D: 20 79           JR      NZ,$5418            ; {}
539F: 6F              LD      L,A                 
53A0: 75              LD      (HL),L              
53A1: 3F              CCF                         
53A2: 20 20           JR      NZ,$53C4            ; {}
53A4: 20 57           JR      NZ,$53FD            ; {}
53A6: 68              LD      L,B                 
53A7: 61              LD      H,C                 
53A8: 74              LD      (HL),H              
53A9: 20 68           JR      NZ,$5413            ; {}
53AB: 61              LD      H,C                 
53AC: 70              LD      (HL),B              
53AD: 70              LD      (HL),B              
53AE: 65              LD      H,L                 
53AF: 6E              LD      L,(HL)              
53B0: 65              LD      H,L                 
53B1: 64              LD      H,H                 
53B2: 20 74           JR      NZ,$5428            ; {}
53B4: 6F              LD      L,A                 
53B5: 68              LD      L,B                 
53B6: 65              LD      H,L                 
53B7: 72              LD      (HL),D              
53B8: 3F              CCF                         
53B9: FF              RST     0X38                
53BA: 54              LD      D,H                 
53BB: 73              LD      (HL),E              
53BC: 6B              LD      L,E                 
53BD: 20 74           JR      NZ,$5433            ; {}
53BF: 73              LD      (HL),E              
53C0: 6B              LD      L,E                 
53C1: 2E 2E           LD      L,$2E               
53C3: 2E 20           LD      L,$20               
53C5: 20 57           JR      NZ,$541E            ; {}
53C7: 68              LD      L,B                 
53C8: 61              LD      H,C                 
53C9: 74              LD      (HL),H              
53CA: 61              LD      H,C                 
53CB: 20 73           JR      NZ,$5440            ; {}
53CD: 68              LD      L,B                 
53CE: 61              LD      H,C                 
53CF: 6D              LD      L,L                 
53D0: 65              LD      H,L                 
53D1: 2E 2E           LD      L,$2E               
53D3: 2E FF           LD      L,$FF               
53D5: 4F              LD      C,A                 
53D6: 68              LD      L,B                 
53D7: 20 74           JR      NZ,$544D            ; {}
53D9: 68              LD      L,B                 
53DA: 61              LD      H,C                 
53DB: 6E              LD      L,(HL)              
53DC: 6B              LD      L,E                 
53DD: 20 79           JR      NZ,$5458            ; {}
53DF: 6F              LD      L,A                 
53E0: 75              LD      (HL),L              
53E1: 21 20 20        LD      HL,$2020            
53E4: 20 59           JR      NZ,$543F            ; {}
53E6: 6F              LD      L,A                 
53E7: 75              LD      (HL),L              
53E8: 20 61           JR      NZ,$544B            ; {}
53EA: 72              LD      (HL),D              
53EB: 65              LD      H,L                 
53EC: 20 69           JR      NZ,$5457            ; {}
53EE: 6E              LD      L,(HL)              
53EF: 64              LD      H,H                 
53F0: 65              LD      H,L                 
53F1: 65              LD      H,L                 
53F2: 64              LD      H,H                 
53F3: 20 61           JR      NZ,$5456            ; {}
53F5: 67              LD      H,A                 
53F6: 65              LD      H,L                 
53F7: 6E              LD      L,(HL)              
53F8: 65              LD      H,L                 
53F9: 72              LD      (HL),D              
53FA: 6F              LD      L,A                 
53FB: 75              LD      (HL),L              
53FC: 73              LD      (HL),E              
53FD: 20 70           JR      NZ,$546F            ; {}
53FF: 65              LD      H,L                 
5400: 72              LD      (HL),D              
5401: 73              LD      (HL),E              
5402: 6F              LD      L,A                 
5403: 6E              LD      L,(HL)              
5404: 21 41 68        LD      HL,$6841            
5407: 21 20 20        LD      HL,$2020            
540A: 49              LD      C,C                 
540B: 20 77           JR      NZ,$5484            ; {}
540D: 69              LD      L,C                 
540E: 6C              LD      L,H                 
540F: 6C              LD      L,H                 
5410: 20 67           JR      NZ,$5479            ; {}
5412: 69              LD      L,C                 
5413: 76              HALT                        
5414: 65              LD      H,L                 
5415: 79              LD      A,C                 
5416: 6F              LD      L,A                 
5417: 75              LD      (HL),L              
5418: 20 74           JR      NZ,$548E            ; {}
541A: 68              LD      L,B                 
541B: 69              LD      L,C                 
541C: 73              LD      (HL),E              
541D: 20 69           JR      NZ,$5488            ; {}
541F: 6E              LD      L,(HL)              
5420: 20 20           JR      NZ,$5442            ; {}
5422: 20 20           JR      NZ,$5444            ; {}
5424: 20 72           JR      NZ,$5498            ; {}
5426: 65              LD      H,L                 
5427: 74              LD      (HL),H              
5428: 75              LD      (HL),L              
5429: 72              LD      (HL),D              
542A: 6E              LD      L,(HL)              
542B: 21 FF 59        LD      HL,$59FF            
542E: 6F              LD      L,A                 
542F: 75              LD      (HL),L              
5430: 20 74           JR      NZ,$54A6            ; {}
5432: 72              LD      (HL),D              
5433: 61              LD      H,C                 
5434: 64              LD      H,H                 
5435: 65              LD      H,L                 
5436: 64              LD      H,H                 
5437: 20 79           JR      NZ,$54B2            ; {}
5439: 6F              LD      L,A                 
543A: 75              LD      (HL),L              
543B: 72              LD      (HL),D              
543C: 20 E0           JR      NZ,$541E            ; {}
543E: 20 66           JR      NZ,$54A6            ; {}
5440: 6F              LD      L,A                 
5441: 72              LD      (HL),D              
5442: 20 E1           JR      NZ,$5425            ; {}
5444: 21 20 20        LD      HL,$2020            
5447: 4D              LD      C,L                 
5448: 61              LD      H,C                 
5449: 79              LD      A,C                 
544A: 62              LD      H,D                 
544B: 65              LD      H,L                 
544C: 20 79           JR      NZ,$54C7            ; {}
544E: 6F              LD      L,A                 
544F: 75              LD      (HL),L              
5450: 20 63           JR      NZ,$54B5            ; {}
5452: 61              LD      H,C                 
5453: 6E              LD      L,(HL)              
5454: 20 74           JR      NZ,$54CA            ; {}
5456: 72              LD      (HL),D              
5457: 61              LD      H,C                 
5458: 64              LD      H,H                 
5459: 65              LD      H,L                 
545A: 20 20           JR      NZ,$547C            ; {}
545C: 20 74           JR      NZ,$54D2            ; {}
545E: 68              LD      L,B                 
545F: 65              LD      H,L                 
5460: 20 72           JR      NZ,$54D4            ; {}
5462: 69              LD      L,C                 
5463: 62              LD      H,D                 
5464: 62              LD      H,D                 
5465: 6F              LD      L,A                 
5466: 6E              LD      L,(HL)              
5467: 20 66           JR      NZ,$54CF            ; {}
5469: 6F              LD      L,A                 
546A: 72              LD      (HL),D              
546B: 20 20           JR      NZ,$548D            ; {}
546D: 73              LD      (HL),E              
546E: 6F              LD      L,A                 
546F: 6D              LD      L,L                 
5470: 65              LD      H,L                 
5471: 74              LD      (HL),H              
5472: 68              LD      L,B                 
5473: 69              LD      L,C                 
5474: 6E              LD      L,(HL)              
5475: 67              LD      H,A                 
5476: 20 65           JR      NZ,$54DD            ; {}
5478: 6C              LD      L,H                 
5479: 73              LD      (HL),E              
547A: 65              LD      H,L                 
547B: 21 FF 42        LD      HL,$42FF            
547E: 65              LD      H,L                 
547F: 63              LD      H,E                 
5480: 61              LD      H,C                 
5481: 75              LD      (HL),L              
5482: 73              LD      (HL),E              
5483: 65              LD      H,L                 
5484: 20 74           JR      NZ,$54FA            ; {}
5486: 68              LD      L,B                 
5487: 65              LD      H,L                 
5488: 79              LD      A,C                 
5489: 20 61           JR      NZ,$54EC            ; {}
548B: 6C              LD      L,H                 
548C: 6C              LD      L,H                 
548D: 6C              LD      L,H                 
548E: 6F              LD      L,A                 
548F: 6F              LD      L,A                 
5490: 6B              LD      L,E                 
5491: 20 61           JR      NZ,$54F4            ; {}
5493: 6C              LD      L,H                 
5494: 69              LD      L,C                 
5495: 6B              LD      L,E                 
5496: 65              LD      H,L                 
5497: 2C              INC     L                   
5498: 20 65           JR      NZ,$54FF            ; {}
549A: 76              HALT                        
549B: 65              LD      H,L                 
549C: 6E              LD      L,(HL)              
549D: 49              LD      C,C                 
549E: 20 61           JR      NZ,$5501            ; {}
54A0: 6D              LD      L,L                 
54A1: 20 73           JR      NZ,$5516            ; {}
54A3: 6F              LD      L,A                 
54A4: 6D              LD      L,L                 
54A5: 65              LD      H,L                 
54A6: 74              LD      (HL),H              
54A7: 69              LD      L,C                 
54A8: 6D              LD      L,L                 
54A9: 65              LD      H,L                 
54AA: 73              LD      (HL),E              
54AB: 20 20           JR      NZ,$54CD            ; {}
54AD: 63              LD      H,E                 
54AE: 6F              LD      L,A                 
54AF: 6E              LD      L,(HL)              
54B0: 66              LD      H,(HL)              
54B1: 75              LD      (HL),L              
54B2: 73              LD      (HL),E              
54B3: 65              LD      H,L                 
54B4: 64              LD      H,H                 
54B5: 2E 2E           LD      L,$2E               
54B7: 2E 20           LD      L,$20               
54B9: 20 20           JR      NZ,$54DB            ; {}
54BB: 20 20           JR      NZ,$54DD            ; {}
54BD: 42              LD      B,D                 
54BE: 79              LD      A,C                 
54BF: 20 74           JR      NZ,$5535            ; {}
54C1: 68              LD      L,B                 
54C2: 65              LD      H,L                 
54C3: 20 77           JR      NZ,$553C            ; {}
54C5: 61              LD      H,C                 
54C6: 79              LD      A,C                 
54C7: 2C              INC     L                   
54C8: 20 64           JR      NZ,$552E            ; {}
54CA: 6F              LD      L,A                 
54CB: 20 20           JR      NZ,$54ED            ; {}
54CD: 79              LD      A,C                 
54CE: 6F              LD      L,A                 
54CF: 75              LD      (HL),L              
54D0: 20 6B           JR      NZ,$553D            ; {}
54D2: 6E              LD      L,(HL)              
54D3: 6F              LD      L,A                 
54D4: 77              LD      (HL),A              
54D5: 20 59           JR      NZ,$5530            ; {}
54D7: 6F              LD      L,A                 
54D8: 73              LD      (HL),E              
54D9: 68              LD      L,B                 
54DA: 69              LD      L,C                 
54DB: 3F              CCF                         
54DC: 20 4D           JR      NZ,$552B            ; {}
54DE: 79              LD      A,C                 
54DF: 20 62           JR      NZ,$5543            ; {}
54E1: 61              LD      H,C                 
54E2: 62              LD      H,D                 
54E3: 79              LD      A,C                 
54E4: 20 6B           JR      NZ,$5551            ; {}
54E6: 65              LD      H,L                 
54E7: 65              LD      H,L                 
54E8: 70              LD      (HL),B              
54E9: 73              LD      (HL),E              
54EA: 20 6F           JR      NZ,$555B            ; {}
54EC: 6E              LD      L,(HL)              
54ED: 61              LD      H,C                 
54EE: 73              LD      (HL),E              
54EF: 6B              LD      L,E                 
54F0: 69              LD      L,C                 
54F1: 6E              LD      L,(HL)              
54F2: 67              LD      H,A                 
54F3: 20 66           JR      NZ,$555B            ; {}
54F5: 6F              LD      L,A                 
54F6: 72              LD      (HL),D              
54F7: 20 61           JR      NZ,$555A            ; {}
54F9: 20 20           JR      NZ,$551B            ; {}
54FB: 20 20           JR      NZ,$551D            ; {}
54FD: 59              LD      E,C                 
54FE: 6F              LD      L,A                 
54FF: 73              LD      (HL),E              
5500: 68              LD      L,B                 
5501: 69              LD      L,C                 
5502: 20 44           JR      NZ,$5548            ; {}
5504: 6F              LD      L,A                 
5505: 6C              LD      L,H                 
5506: 6C              LD      L,H                 
5507: 20 61           JR      NZ,$556A            ; {}
5509: 6E              LD      L,(HL)              
550A: 64              LD      H,H                 
550B: 20 49           JR      NZ,$5556            ; {}
550D: 64              LD      H,H                 
550E: 6F              LD      L,A                 
550F: 6E              LD      L,(HL)              
5510: 5E              LD      E,(HL)              
5511: 74              LD      (HL),H              
5512: 20 6B           JR      NZ,$557F            ; {}
5514: 6E              LD      L,(HL)              
5515: 6F              LD      L,A                 
5516: 77              LD      (HL),A              
5517: 20 77           JR      NZ,$5590            ; {}
5519: 68              LD      L,B                 
551A: 61              LD      H,C                 
551B: 74              LD      (HL),H              
551C: 20 74           JR      NZ,$5592            ; {}
551E: 6F              LD      L,A                 
551F: 20 64           JR      NZ,$5585            ; {}
5521: 6F              LD      L,A                 
5522: 20 61           JR      NZ,$5585            ; {}
5524: 62              LD      H,D                 
5525: 6F              LD      L,A                 
5526: 75              LD      (HL),L              
5527: 74              LD      (HL),H              
5528: 20 69           JR      NZ,$5593            ; {}
552A: 74              LD      (HL),H              
552B: 21 FF 4F        LD      HL,$4FFF            
552E: 68              LD      L,B                 
552F: 21 20 20        LD      HL,$2020            
5532: 57              LD      D,A                 
5533: 69              LD      L,C                 
5534: 6C              LD      L,H                 
5535: 6C              LD      L,H                 
5536: 20 79           JR      NZ,$55B1            ; {}
5538: 6F              LD      L,A                 
5539: 75              LD      (HL),L              
553A: 20 20           JR      NZ,$555C            ; {}
553C: 20 67           JR      NZ,$55A5            ; {}
553E: 69              LD      L,C                 
553F: 76              HALT                        
5540: 65              LD      H,L                 
5541: 20 74           JR      NZ,$55B7            ; {}
5543: 68              LD      L,B                 
5544: 61              LD      H,C                 
5545: 74              LD      (HL),H              
5546: 20 64           JR      NZ,$55AC            ; {}
5548: 6F              LD      L,A                 
5549: 6C              LD      L,H                 
554A: 6C              LD      L,H                 
554B: 20 20           JR      NZ,$556D            ; {}
554D: 74              LD      (HL),H              
554E: 6F              LD      L,A                 
554F: 20 6D           JR      NZ,$55BE            ; {}
5551: 79              LD      A,C                 
5552: 20 62           JR      NZ,$55B6            ; {}
5554: 61              LD      H,C                 
5555: 62              LD      H,D                 
5556: 79              LD      A,C                 
5557: 3F              CCF                         
5558: 21 20 20        LD      HL,$2020            
555B: 20 20           JR      NZ,$557D            ; {}
555D: 20 20           JR      NZ,$557F            ; {}
555F: 20 20           JR      NZ,$5581            ; {}
5561: 59              LD      E,C                 
5562: 65              LD      H,L                 
5563: 73              LD      (HL),E              
5564: 20 20           JR      NZ,$5586            ; {}
5566: 4E              LD      C,(HL)              
5567: 6F              LD      L,A                 
5568: FE 42           CP      $42                 
556A: 65              LD      H,L                 
556B: 63              LD      H,E                 
556C: 61              LD      H,C                 
556D: 75              LD      (HL),L              
556E: 73              LD      (HL),E              
556F: 65              LD      H,L                 
5570: 20 74           JR      NZ,$55E6            ; {}
5572: 68              LD      L,B                 
5573: 65              LD      H,L                 
5574: 79              LD      A,C                 
5575: 20 61           JR      NZ,$55D8            ; {}
5577: 6C              LD      L,H                 
5578: 6C              LD      L,H                 
5579: 6C              LD      L,H                 
557A: 6F              LD      L,A                 
557B: 6F              LD      L,A                 
557C: 6B              LD      L,E                 
557D: 20 61           JR      NZ,$55E0            ; {}
557F: 6C              LD      L,H                 
5580: 69              LD      L,C                 
5581: 6B              LD      L,E                 
5582: 65              LD      H,L                 
5583: 2C              INC     L                   
5584: 20 65           JR      NZ,$55EB            ; {}
5586: 76              HALT                        
5587: 65              LD      H,L                 
5588: 6E              LD      L,(HL)              
5589: 49              LD      C,C                 
558A: 20 61           JR      NZ,$55ED            ; {}
558C: 6D              LD      L,L                 
558D: 20 73           JR      NZ,$5602            ; {}
558F: 6F              LD      L,A                 
5590: 6D              LD      L,L                 
5591: 65              LD      H,L                 
5592: 74              LD      (HL),H              
5593: 69              LD      L,C                 
5594: 6D              LD      L,L                 
5595: 65              LD      H,L                 
5596: 73              LD      (HL),E              
5597: 20 20           JR      NZ,$55B9            ; {}
5599: 63              LD      H,E                 
559A: 6F              LD      L,A                 
559B: 6E              LD      L,(HL)              
559C: 66              LD      H,(HL)              
559D: 75              LD      (HL),L              
559E: 73              LD      (HL),E              
559F: 65              LD      H,L                 
55A0: 64              LD      H,H                 
55A1: 2E 2E           LD      L,$2E               
55A3: 2E 20           LD      L,$20               
55A5: 20 20           JR      NZ,$55C7            ; {}
55A7: 20 20           JR      NZ,$55C9            ; {}
55A9: FF              RST     0X38                
55AA: 41              LD      B,C                 
55AB: 68              LD      L,B                 
55AC: 65              LD      H,L                 
55AD: 6D              LD      L,L                 
55AE: 21 20 20        LD      HL,$2020            
55B1: 52              LD      D,D                 
55B2: 65              LD      H,L                 
55B3: 61              LD      H,C                 
55B4: 6C              LD      L,H                 
55B5: 6C              LD      L,H                 
55B6: 79              LD      A,C                 
55B7: 2C              INC     L                   
55B8: 20 49           JR      NZ,$5603            ; {}
55BA: 6D              LD      L,L                 
55BB: 75              LD      (HL),L              
55BC: 73              LD      (HL),E              
55BD: 74              LD      (HL),H              
55BE: 20 69           JR      NZ,$5629            ; {}
55C0: 6E              LD      L,(HL)              
55C1: 73              LD      (HL),E              
55C2: 69              LD      L,C                 
55C3: 73              LD      (HL),E              
55C4: 74              LD      (HL),H              
55C5: 20 74           JR      NZ,$563B            ; {}
55C7: 68              LD      L,B                 
55C8: 61              LD      H,C                 
55C9: 74              LD      (HL),H              
55CA: 79              LD      A,C                 
55CB: 6F              LD      L,A                 
55CC: 75              LD      (HL),L              
55CD: 20 6E           JR      NZ,$563D            ; {}
55CF: 6F              LD      L,A                 
55D0: 74              LD      (HL),H              
55D1: 20 62           JR      NZ,$5635            ; {}
55D3: 72              LD      (HL),D              
55D4: 69              LD      L,C                 
55D5: 6E              LD      L,(HL)              
55D6: 67              LD      H,A                 
55D7: 20 20           JR      NZ,$55F9            ; {}
55D9: 20 74           JR      NZ,$564F            ; {}
55DB: 68              LD      L,B                 
55DC: 61              LD      H,C                 
55DD: 74              LD      (HL),H              
55DE: 20 61           JR      NZ,$5641            ; {}
55E0: 77              LD      (HL),A              
55E1: 66              LD      H,(HL)              
55E2: 75              LD      (HL),L              
55E3: 6C              LD      L,H                 
55E4: 20 62           JR      NZ,$5648            ; {}
55E6: 65              LD      H,L                 
55E7: 61              LD      H,C                 
55E8: 73              LD      (HL),E              
55E9: 74              LD      (HL),H              
55EA: 69              LD      L,C                 
55EB: 6E              LD      L,(HL)              
55EC: 20 68           JR      NZ,$5656            ; {}
55EE: 65              LD      H,L                 
55EF: 72              LD      (HL),D              
55F0: 65              LD      H,L                 
55F1: 21 20 20        LD      HL,$2020            
55F4: 4C              LD      C,H                 
55F5: 65              LD      H,L                 
55F6: 61              LD      H,C                 
55F7: 76              HALT                        
55F8: 65              LD      H,L                 
55F9: 20 74           JR      NZ,$566F            ; {}
55FB: 68              LD      L,B                 
55FC: 61              LD      H,C                 
55FD: 74              LD      (HL),H              
55FE: 20 63           JR      NZ,$5663            ; {}
5600: 72              LD      (HL),D              
5601: 65              LD      H,L                 
5602: 61              LD      H,C                 
5603: 74              LD      (HL),H              
5604: 75              LD      (HL),L              
5605: 72              LD      (HL),D              
5606: 65              LD      H,L                 
5607: 20 20           JR      NZ,$5629            ; {}
5609: 20 6F           JR      NZ,$567A            ; {}
560B: 75              LD      (HL),L              
560C: 74              LD      (HL),H              
560D: 73              LD      (HL),E              
560E: 69              LD      L,C                 
560F: 64              LD      H,H                 
5610: 65              LD      H,L                 
5611: 20 61           JR      NZ,$5674            ; {}
5613: 6E              LD      L,(HL)              
5614: 64              LD      H,H                 
5615: 20 74           JR      NZ,$568B            ; {}
5617: 68              LD      L,B                 
5618: 65              LD      H,L                 
5619: 6E              LD      L,(HL)              
561A: 77              LD      (HL),A              
561B: 65              LD      H,L                 
561C: 20 63           JR      NZ,$5681            ; {}
561E: 61              LD      H,C                 
561F: 6E              LD      L,(HL)              
5620: 20 74           JR      NZ,$5696            ; {}
5622: 61              LD      H,C                 
5623: 6C              LD      L,H                 
5624: 6B              LD      L,E                 
5625: 21 20 20        LD      HL,$2020            
5628: 20 20           JR      NZ,$564A            ; {}
562A: 47              LD      B,A                 
562B: 6F              LD      L,A                 
562C: 6F              LD      L,A                 
562D: 64              LD      H,H                 
562E: 20 42           JR      NZ,$5672            ; {}
5630: 79              LD      A,C                 
5631: 65              LD      H,L                 
5632: 21 FF 48        LD      HL,$48FF            
5635: 6F              LD      L,A                 
5636: 20 68           JR      NZ,$56A0            ; {}
5638: 6F              LD      L,A                 
5639: 20 68           JR      NZ,$56A3            ; {}
563B: 6F              LD      L,A                 
563C: 21 20 20        LD      HL,$2020            
563F: 20 20           JR      NZ,$5661            ; {}
5641: 20 20           JR      NZ,$5663            ; {}
5643: 20 49           JR      NZ,$568E            ; {}
5645: 20 72           JR      NZ,$56B9            ; {}
5647: 65              LD      H,L                 
5648: 61              LD      H,C                 
5649: 6C              LD      L,H                 
564A: 6C              LD      L,H                 
564B: 79              LD      A,C                 
564C: 20 61           JR      NZ,$56AF            ; {}
564E: 70              LD      (HL),B              
564F: 70              LD      (HL),B              
5650: 72              LD      (HL),D              
5651: 65              LD      H,L                 
5652: 2D              DEC     L                   
5653: 20 63           JR      NZ,$56B8            ; {}
5655: 69              LD      L,C                 
5656: 61              LD      H,C                 
5657: 74              LD      (HL),H              
5658: 65              LD      H,L                 
5659: 20 77           JR      NZ,$56D2            ; {}
565B: 68              LD      L,B                 
565C: 61              LD      H,C                 
565D: 74              LD      (HL),H              
565E: 20 79           JR      NZ,$56D9            ; {}
5660: 6F              LD      L,A                 
5661: 75              LD      (HL),L              
5662: 20 20           JR      NZ,$5684            ; {}
5664: 64              LD      H,H                 
5665: 69              LD      L,C                 
5666: 64              LD      H,H                 
5667: 20 66           JR      NZ,$56CF            ; {}
5669: 6F              LD      L,A                 
566A: 72              LD      (HL),D              
566B: 20 6D           JR      NZ,$56DA            ; {}
566D: 79              LD      A,C                 
566E: 20 70           JR      NZ,$56E0            ; {}
5670: 6F              LD      L,A                 
5671: 6F              LD      L,A                 
5672: 72              LD      (HL),D              
5673: 2C              INC     L                   
5674: 70              LD      (HL),B              
5675: 72              LD      (HL),D              
5676: 65              LD      H,L                 
5677: 63              LD      H,E                 
5678: 69              LD      L,C                 
5679: 6F              LD      L,A                 
567A: 75              LD      (HL),L              
567B: 73              LD      (HL),E              
567C: 20 42           JR      NZ,$56C0            ; {}
567E: 6F              LD      L,A                 
567F: 77              LD      (HL),A              
5680: 57              LD      D,A                 
5681: 6F              LD      L,A                 
5682: 77              LD      (HL),A              
5683: 21 59 6F        LD      HL,$6F59            
5686: 75              LD      (HL),L              
5687: 20 61           JR      NZ,$56EA            ; {}
5689: 72              LD      (HL),D              
568A: 65              LD      H,L                 
568B: 20 73           JR      NZ,$5700            ; {}
568D: 75              LD      (HL),L              
568E: 63              LD      H,E                 
568F: 68              LD      L,B                 
5690: 20 61           JR      NZ,$56F3            ; {}
5692: 20 20           JR      NZ,$56B4            ; {}
5694: 6E              LD      L,(HL)              
5695: 69              LD      L,C                 
5696: 63              LD      H,E                 
5697: 65              LD      H,L                 
5698: 20 62           JR      NZ,$56FC            ; {}
569A: 6F              LD      L,A                 
569B: 79              LD      A,C                 
569C: 21 20 20        LD      HL,$2020            
569F: 48              LD      C,B                 
56A0: 6F              LD      L,A                 
56A1: 77              LD      (HL),A              
56A2: 20 20           JR      NZ,$56C4            ; {}
56A4: 63              LD      H,E                 
56A5: 61              LD      H,C                 
56A6: 6E              LD      L,(HL)              
56A7: 20 49           JR      NZ,$56F2            ; {}
56A9: 20 65           JR      NZ,$5710            ; {}
56AB: 76              HALT                        
56AC: 65              LD      H,L                 
56AD: 72              LD      (HL),D              
56AE: 20 72           JR      NZ,$5722            ; {}
56B0: 65              LD      H,L                 
56B1: 70              LD      (HL),B              
56B2: 61              LD      H,C                 
56B3: 79              LD      A,C                 
56B4: 79              LD      A,C                 
56B5: 6F              LD      L,A                 
56B6: 75              LD      (HL),L              
56B7: 3F              CCF                         
56B8: 20 20           JR      NZ,$56DA            ; {}
56BA: 49              LD      C,C                 
56BB: 20 6B           JR      NZ,$5728            ; {}
56BD: 6E              LD      L,(HL)              
56BE: 6F              LD      L,A                 
56BF: 77              LD      (HL),A              
56C0: 2E 2E           LD      L,$2E               
56C2: 2E 20           LD      L,$20               
56C4: 20 20           JR      NZ,$56E6            ; {}
56C6: 53              LD      D,E                 
56C7: 4D              LD      C,L                 
56C8: 4F              LD      C,A                 
56C9: 4F              LD      C,A                 
56CA: 4F              LD      C,A                 
56CB: 4F              LD      C,A                 
56CC: 4F              LD      C,A                 
56CD: 4F              LD      C,A                 
56CE: 4F              LD      C,A                 
56CF: 43              LD      B,E                 
56D0: 48              LD      C,B                 
56D1: 21 20 20        LD      HL,$2020            
56D4: 59              LD      E,C                 
56D5: 6F              LD      L,A                 
56D6: 75              LD      (HL),L              
56D7: 20 67           JR      NZ,$5740            ; {}
56D9: 6F              LD      L,A                 
56DA: 74              LD      (HL),H              
56DB: 20 61           JR      NZ,$573E            ; {}
56DD: 20 72           JR      NZ,$5751            ; {}
56DF: 65              LD      H,L                 
56E0: 77              LD      (HL),A              
56E1: 61              LD      H,C                 
56E2: 72              LD      (HL),D              
56E3: 64              LD      H,H                 
56E4: 66              LD      H,(HL)              
56E5: 72              LD      (HL),D              
56E6: 6F              LD      L,A                 
56E7: 6D              LD      L,L                 
56E8: 20 4D           JR      NZ,$5737            ; {}
56EA: 61              LD      H,C                 
56EB: 64              LD      H,H                 
56EC: 61              LD      H,C                 
56ED: 6D              LD      L,L                 
56EE: 20 4D           JR      NZ,$573D            ; {}
56F0: 65              LD      H,L                 
56F1: 6F              LD      L,A                 
56F2: 77              LD      (HL),A              
56F3: 2D              DEC     L                   
56F4: 4D              LD      C,L                 
56F5: 65              LD      H,L                 
56F6: 6F              LD      L,A                 
56F7: 77              LD      (HL),A              
56F8: 2E 2E           LD      L,$2E               
56FA: 2E 20           LD      L,$20               
56FC: 2E 2E           LD      L,$2E               
56FE: 2E 20           LD      L,$20               
5700: 2E 2E           LD      L,$2E               
5702: 2E 20           LD      L,$20               
5704: 4C              LD      C,H                 
5705: 2D              DEC     L                   
5706: 6C              LD      L,H                 
5707: 2D              DEC     L                   
5708: 6C              LD      L,H                 
5709: 75              LD      (HL),L              
570A: 63              LD      H,E                 
570B: 6B              LD      L,E                 
570C: 79              LD      A,C                 
570D: 21 FF 48        LD      HL,$48FF            
5710: 6F              LD      L,A                 
5711: 20 68           JR      NZ,$577B            ; {}
5713: 6F              LD      L,A                 
5714: 20 68           JR      NZ,$577E            ; {}
5716: 6F              LD      L,A                 
5717: 21 20 20        LD      HL,$2020            
571A: 4D              LD      C,L                 
571B: 79              LD      A,C                 
571C: 20 20           JR      NZ,$573E            ; {}
571E: 20 42           JR      NZ,$5762            ; {}
5720: 6F              LD      L,A                 
5721: 77              LD      (HL),A              
5722: 57              LD      D,A                 
5723: 6F              LD      L,A                 
5724: 77              LD      (HL),A              
5725: 20 69           JR      NZ,$5790            ; {}
5727: 73              LD      (HL),E              
5728: 20 73           JR      NZ,$579D            ; {}
572A: 6F              LD      L,A                 
572B: 20 20           JR      NZ,$574D            ; {}
572D: 20 20           JR      NZ,$574F            ; {}
572F: 70              LD      (HL),B              
5730: 72              LD      (HL),D              
5731: 6F              LD      L,A                 
5732: 75              LD      (HL),L              
5733: 64              LD      H,H                 
5734: 20 6F           JR      NZ,$57A5            ; {}
5736: 66              LD      H,(HL)              
5737: 20 68           JR      NZ,$57A1            ; {}
5739: 69              LD      L,C                 
573A: 73              LD      (HL),E              
573B: 20 20           JR      NZ,$575D            ; {}
573D: 20 20           JR      NZ,$575F            ; {}
573F: 66              LD      H,(HL)              
5740: 69              LD      L,C                 
5741: 6E              LD      L,(HL)              
5742: 65              LD      H,L                 
5743: 20 66           JR      NZ,$57AB            ; {}
5745: 75              LD      (HL),L              
5746: 72              LD      (HL),D              
5747: 20 63           JR      NZ,$57AC            ; {}
5749: 6F              LD      L,A                 
574A: 61              LD      H,C                 
574B: 74              LD      (HL),H              
574C: 21 FF 41        LD      HL,$41FF            
574F: 49              LD      C,C                 
5750: 45              LD      B,L                 
5751: 45              LD      B,L                 
5752: 45              LD      B,L                 
5753: 45              LD      B,L                 
5754: 45              LD      B,L                 
5755: 45              LD      B,L                 
5756: 45              LD      B,L                 
5757: 45              LD      B,L                 
5758: 21 20 20        LD      HL,$2020            
575B: 20 20           JR      NZ,$577D            ; {}
575D: 20 49           JR      NZ,$57A8            ; {}
575F: 74              LD      (HL),H              
5760: 5E              LD      E,(HL)              
5761: 73              LD      (HL),E              
5762: 20 74           JR      NZ,$57D8            ; {}
5764: 65              LD      H,L                 
5765: 72              LD      (HL),D              
5766: 72              LD      (HL),D              
5767: 72              LD      (HL),D              
5768: 72              LD      (HL),D              
5769: 62              LD      H,D                 
576A: 69              LD      L,C                 
576B: 6C              LD      L,H                 
576C: 65              LD      H,L                 
576D: 21 4D 79        LD      HL,$794D            
5770: 20 42           JR      NZ,$57B4            ; {}
5772: 6F              LD      L,A                 
5773: 77              LD      (HL),A              
5774: 57              LD      D,A                 
5775: 6F              LD      L,A                 
5776: 77              LD      (HL),A              
5777: 20 77           JR      NZ,$57F0            ; {}
5779: 61              LD      H,C                 
577A: 73              LD      (HL),E              
577B: 20 20           JR      NZ,$579D            ; {}
577D: 20 64           JR      NZ,$57E3            ; {}
577F: 6F              LD      L,A                 
5780: 67              LD      H,A                 
5781: 6E              LD      L,(HL)              
5782: 61              LD      H,C                 
5783: 70              LD      (HL),B              
5784: 70              LD      (HL),B              
5785: 65              LD      H,L                 
5786: 64              LD      H,H                 
5787: 20 62           JR      NZ,$57EB            ; {}
5789: 79              LD      A,C                 
578A: 2E 2E           LD      L,$2E               
578C: 2E 20           LD      L,$20               
578E: 4D              LD      C,L                 
578F: 6F              LD      L,A                 
5790: 2D              DEC     L                   
5791: 6D              LD      L,L                 
5792: 6F              LD      L,A                 
5793: 2D              DEC     L                   
5794: 4D              LD      C,L                 
5795: 4F              LD      C,A                 
5796: 42              LD      B,D                 
5797: 4C              LD      C,H                 
5798: 49              LD      C,C                 
5799: 4E              LD      C,(HL)              
579A: 53              LD      D,E                 
579B: 21 21 20        LD      HL,$2021            
579E: 4F              LD      C,A                 
579F: 48              LD      C,B                 
57A0: 48              LD      C,B                 
57A1: 48              LD      C,B                 
57A2: 21 20 20        LD      HL,$2020            
57A5: 41              LD      B,C                 
57A6: 48              LD      C,B                 
57A7: 48              LD      C,B                 
57A8: 48              LD      C,B                 
57A9: 48              LD      C,B                 
57AA: 21 20 20        LD      HL,$2020            
57AD: 20 50           JR      NZ,$57FF            ; {}
57AF: 6C              LD      L,H                 
57B0: 65              LD      H,L                 
57B1: 61              LD      H,C                 
57B2: 73              LD      (HL),E              
57B3: 65              LD      H,L                 
57B4: 21 20 53        LD      HL,$5320            
57B7: 6F              LD      L,A                 
57B8: 6D              LD      L,L                 
57B9: 65              LD      H,L                 
57BA: 62              LD      H,D                 
57BB: 6F              LD      L,A                 
57BC: 64              LD      H,H                 
57BD: 79              LD      A,C                 
57BE: 68              LD      L,B                 
57BF: 65              LD      H,L                 
57C0: 6C              LD      L,H                 
57C1: 70              LD      (HL),B              
57C2: 20 6D           JR      NZ,$5831            ; {}
57C4: 79              LD      A,C                 
57C5: 20 70           JR      NZ,$5837            ; {}
57C7: 6F              LD      L,A                 
57C8: 6F              LD      L,A                 
57C9: 72              LD      (HL),D              
57CA: 20 20           JR      NZ,$57EC            ; {}
57CC: 20 20           JR      NZ,$57EE            ; {}
57CE: 42              LD      B,D                 
57CF: 6F              LD      L,A                 
57D0: 77              LD      (HL),A              
57D1: 57              LD      D,A                 
57D2: 6F              LD      L,A                 
57D3: 77              LD      (HL),A              
57D4: 21 21 FF        LD      HL,$FF21            
57D7: 4F              LD      C,A                 
57D8: 68              LD      L,B                 
57D9: 20 74           JR      NZ,$584F            ; {}
57DB: 68              LD      L,B                 
57DC: 61              LD      H,C                 
57DD: 6E              LD      L,(HL)              
57DE: 6B              LD      L,E                 
57DF: 20 79           JR      NZ,$585A            ; {}
57E1: 6F              LD      L,A                 
57E2: 75              LD      (HL),L              
57E3: 21 20 20        LD      HL,$2020            
57E6: 20 49           JR      NZ,$5831            ; {}
57E8: 5E              LD      E,(HL)              
57E9: 6D              LD      L,L                 
57EA: 20 73           JR      NZ,$585F            ; {}
57EC: 6F              LD      L,A                 
57ED: 20 68           JR      NZ,$5857            ; {}
57EF: 61              LD      H,C                 
57F0: 70              LD      (HL),B              
57F1: 70              LD      (HL),B              
57F2: 79              LD      A,C                 
57F3: 20 79           JR      NZ,$586E            ; {}
57F5: 6F              LD      L,A                 
57F6: 75              LD      (HL),L              
57F7: 62              LD      H,D                 
57F8: 72              LD      (HL),D              
57F9: 6F              LD      L,A                 
57FA: 75              LD      (HL),L              
57FB: 67              LD      H,A                 
57FC: 68              LD      L,B                 
57FD: 74              LD      (HL),H              
57FE: 20 6D           JR      NZ,$586D            ; {}
5800: 79              LD      A,C                 
5801: 20 62           JR      NZ,$5865            ; {}
5803: 61              LD      H,C                 
5804: 62              LD      H,D                 
5805: 79              LD      A,C                 
5806: 20 62           JR      NZ,$586A            ; {}
5808: 61              LD      H,C                 
5809: 63              LD      H,E                 
580A: 6B              LD      L,E                 
580B: 21 20 4E        LD      HL,$4E20            
580E: 6F              LD      L,A                 
580F: 77              LD      (HL),A              
5810: 2C              INC     L                   
5811: 20 77           JR      NZ,$588A            ; {}
5813: 6F              LD      L,A                 
5814: 75              LD      (HL),L              
5815: 6C              LD      L,H                 
5816: 64              LD      H,H                 
5817: 79              LD      A,C                 
5818: 6F              LD      L,A                 
5819: 75              LD      (HL),L              
581A: 20 62           JR      NZ,$587E            ; {}
581C: 65              LD      H,L                 
581D: 20 61           JR      NZ,$5880            ; {}
581F: 20 64           JR      NZ,$5885            ; {}
5821: 65              LD      H,L                 
5822: 61              LD      H,C                 
5823: 72              LD      (HL),D              
5824: 20 20           JR      NZ,$5846            ; {}
5826: 20 61           JR      NZ,$5889            ; {}
5828: 6E              LD      L,(HL)              
5829: 64              LD      H,H                 
582A: 20 74           JR      NZ,$58A0            ; {}
582C: 61              LD      H,C                 
582D: 6B              LD      L,E                 
582E: 65              LD      H,L                 
582F: 20 68           JR      NZ,$5899            ; {}
5831: 69              LD      L,C                 
5832: 6D              LD      L,L                 
5833: 20 66           JR      NZ,$589B            ; {}
5835: 6F              LD      L,A                 
5836: 72              LD      (HL),D              
5837: 61              LD      H,C                 
5838: 20 77           JR      NZ,$58B1            ; {}
583A: 61              LD      H,C                 
583B: 6C              LD      L,H                 
583C: 6B              LD      L,E                 
583D: 3F              CCF                         
583E: 20 49           JR      NZ,$5889            ; {}
5840: 74              LD      (HL),H              
5841: 20 77           JR      NZ,$58BA            ; {}
5843: 6F              LD      L,A                 
5844: 75              LD      (HL),L              
5845: 6C              LD      L,H                 
5846: 64              LD      H,H                 
5847: 72              LD      (HL),D              
5848: 65              LD      H,L                 
5849: 61              LD      H,C                 
584A: 6C              LD      L,H                 
584B: 6C              LD      L,H                 
584C: 79              LD      A,C                 
584D: 20 68           JR      NZ,$58B7            ; {}
584F: 65              LD      H,L                 
5850: 6C              LD      L,H                 
5851: 70              LD      (HL),B              
5852: 20 6D           JR      NZ,$58C1            ; {}
5854: 65              LD      H,L                 
5855: 20 20           JR      NZ,$5877            ; {}
5857: 6F              LD      L,A                 
5858: 75              LD      (HL),L              
5859: 74              LD      (HL),H              
585A: 20 61           JR      NZ,$58BD            ; {}
585C: 20 6C           JR      NZ,$58CA            ; {}
585E: 6F              LD      L,A                 
585F: 74              LD      (HL),H              
5860: 21 20 20        LD      HL,$2020            
5863: 59              LD      E,C                 
5864: 6F              LD      L,A                 
5865: 75              LD      (HL),L              
5866: 20 77           JR      NZ,$58DF            ; {}
5868: 69              LD      L,C                 
5869: 6C              LD      L,H                 
586A: 6C              LD      L,H                 
586B: 3F              CCF                         
586C: 21 20 20        LD      HL,$2020            
586F: 54              LD      D,H                 
5870: 68              LD      L,B                 
5871: 61              LD      H,C                 
5872: 6E              LD      L,(HL)              
5873: 6B              LD      L,E                 
5874: 73              LD      (HL),E              
5875: 21 FF 57        LD      HL,$57FF            
5878: 65              LD      H,L                 
5879: 6C              LD      L,H                 
587A: 6C              LD      L,H                 
587B: 2E 2E           LD      L,$2E               
587D: 2E 20           LD      L,$20               
587F: 49              LD      C,C                 
5880: 20 70           JR      NZ,$58F2            ; {}
5882: 72              LD      (HL),D              
5883: 65              LD      H,L                 
5884: 74              LD      (HL),H              
5885: 74              LD      (HL),H              
5886: 79              LD      A,C                 
5887: 6D              LD      L,L                 
5888: 75              LD      (HL),L              
5889: 63              LD      H,E                 
588A: 68              LD      L,B                 
588B: 20 73           JR      NZ,$5900            ; {}
588D: 74              LD      (HL),H              
588E: 69              LD      L,C                 
588F: 63              LD      H,E                 
5890: 6B              LD      L,E                 
5891: 20 74           JR      NZ,$5907            ; {}
5893: 6F              LD      L,A                 
5894: 20 20           JR      NZ,$58B6            ; {}
5896: 20 6D           JR      NZ,$5905            ; {}
5898: 79              LD      A,C                 
5899: 73              LD      (HL),E              
589A: 65              LD      H,L                 
589B: 6C              LD      L,H                 
589C: 66              LD      H,(HL)              
589D: 2C              INC     L                   
589E: 20 6D           JR      NZ,$590D            ; {}
58A0: 65              LD      H,L                 
58A1: 20 61           JR      NZ,$5904            ; {}
58A3: 6E              LD      L,(HL)              
58A4: 64              LD      H,H                 
58A5: 20 20           JR      NZ,$58C7            ; {}
58A7: 6D              LD      L,L                 
58A8: 79              LD      A,C                 
58A9: 20 6C           JR      NZ,$5917            ; {}
58AB: 65              LD      H,L                 
58AC: 74              LD      (HL),H              
58AD: 74              LD      (HL),H              
58AE: 65              LD      H,L                 
58AF: 72              LD      (HL),D              
58B0: 73              LD      (HL),E              
58B1: 2E 2E           LD      L,$2E               
58B3: 2E 20           LD      L,$20               
58B5: 20 20           JR      NZ,$58D7            ; {}
58B7: 4D              LD      C,L                 
58B8: 79              LD      A,C                 
58B9: 20 6E           JR      NZ,$5929            ; {}
58BB: 61              LD      H,C                 
58BC: 6D              LD      L,L                 
58BD: 65              LD      H,L                 
58BE: 5E              LD      E,(HL)              
58BF: 73              LD      (HL),E              
58C0: 20 57           JR      NZ,$5919            ; {}
58C2: 72              LD      (HL),D              
58C3: 69              LD      L,C                 
58C4: 74              LD      (HL),H              
58C5: 65              LD      H,L                 
58C6: 21 54 68        LD      HL,$6854            
58C9: 65              LD      H,L                 
58CA: 20 6F           JR      NZ,$593B            ; {}
58CC: 6E              LD      L,(HL)              
58CD: 6C              LD      L,H                 
58CE: 79              LD      A,C                 
58CF: 20 74           JR      NZ,$5945            ; {}
58D1: 68              LD      L,B                 
58D2: 69              LD      L,C                 
58D3: 6E              LD      L,(HL)              
58D4: 67              LD      H,A                 
58D5: 20 49           JR      NZ,$5920            ; {}
58D7: 64              LD      H,H                 
58D8: 6F              LD      L,A                 
58D9: 6E              LD      L,(HL)              
58DA: 5E              LD      E,(HL)              
58DB: 74              LD      (HL),H              
58DC: 20 6C           JR      NZ,$594A            ; {}
58DE: 69              LD      L,C                 
58DF: 6B              LD      L,E                 
58E0: 65              LD      H,L                 
58E1: 20 61           JR      NZ,$5944            ; {}
58E3: 62              LD      H,D                 
58E4: 6F              LD      L,A                 
58E5: 75              LD      (HL),L              
58E6: 74              LD      (HL),H              
58E7: 6D              LD      L,L                 
58E8: 79              LD      A,C                 
58E9: 20 68           JR      NZ,$5953            ; {}
58EB: 6F              LD      L,A                 
58EC: 62              LD      H,D                 
58ED: 62              LD      H,D                 
58EE: 79              LD      A,C                 
58EF: 20 69           JR      NZ,$595A            ; {}
58F1: 73              LD      (HL),E              
58F2: 20 74           JR      NZ,$5968            ; {}
58F4: 68              LD      L,B                 
58F5: 61              LD      H,C                 
58F6: 74              LD      (HL),H              
58F7: 49              LD      C,C                 
58F8: 20 6E           JR      NZ,$5968            ; {}
58FA: 65              LD      H,L                 
58FB: 76              HALT                        
58FC: 65              LD      H,L                 
58FD: 72              LD      (HL),D              
58FE: 20 72           JR      NZ,$5972            ; {}
5900: 65              LD      H,L                 
5901: 63              LD      H,E                 
5902: 65              LD      H,L                 
5903: 69              LD      L,C                 
5904: 76              HALT                        
5905: 65              LD      H,L                 
5906: 20 61           JR      NZ,$5969            ; {}
5908: 20 72           JR      NZ,$597C            ; {}
590A: 65              LD      H,L                 
590B: 73              LD      (HL),E              
590C: 70              LD      (HL),B              
590D: 6F              LD      L,A                 
590E: 6E              LD      L,(HL)              
590F: 73              LD      (HL),E              
5910: 65              LD      H,L                 
5911: 2E 2E           LD      L,$2E               
5913: 2E FF           LD      L,$FF               
5915: 57              LD      D,A                 
5916: 68              LD      L,B                 
5917: 61              LD      H,C                 
5918: 74              LD      (HL),H              
5919: 5E              LD      E,(HL)              
591A: 73              LD      (HL),E              
591B: 20 74           JR      NZ,$5991            ; {}
591D: 68              LD      L,B                 
591E: 69              LD      L,C                 
591F: 73              LD      (HL),E              
5920: 3F              CCF                         
5921: 21 20 20        LD      HL,$2020            
5924: 41              LD      B,C                 
5925: 6C              LD      L,H                 
5926: 65              LD      H,L                 
5927: 74              LD      (HL),H              
5928: 74              LD      (HL),H              
5929: 65              LD      H,L                 
592A: 72              LD      (HL),D              
592B: 20 66           JR      NZ,$5993            ; {}
592D: 6F              LD      L,A                 
592E: 72              LD      (HL),D              
592F: 20 6D           JR      NZ,$599E            ; {}
5931: 65              LD      H,L                 
5932: 3F              CCF                         
5933: 21 20 49        LD      HL,$4920            
5936: 5E              LD      E,(HL)              
5937: 6D              LD      L,L                 
5938: 20 73           JR      NZ,$59AD            ; {}
593A: 6F              LD      L,A                 
593B: 20 68           JR      NZ,$59A5            ; {}
593D: 61              LD      H,C                 
593E: 70              LD      (HL),B              
593F: 70              LD      (HL),B              
5940: 79              LD      A,C                 
5941: 21 20 20        LD      HL,$2020            
5944: 20 2E           JR      NZ,$5974            ; {}
5946: 2E 2E           LD      L,$2E               
5948: 41              LD      B,C                 
5949: 6E              LD      L,(HL)              
594A: 64              LD      H,H                 
594B: 20 6C           JR      NZ,$59B9            ; {}
594D: 6F              LD      L,A                 
594E: 6F              LD      L,A                 
594F: 6B              LD      L,E                 
5950: 21 20 54        LD      HL,$5420            
5953: 68              LD      L,B                 
5954: 65              LD      H,L                 
5955: 6C              LD      L,H                 
5956: 65              LD      H,L                 
5957: 74              LD      (HL),H              
5958: 74              LD      (HL),H              
5959: 65              LD      H,L                 
595A: 72              LD      (HL),D              
595B: 20 63           JR      NZ,$59C0            ; {}
595D: 61              LD      H,C                 
595E: 6D              LD      L,L                 
595F: 65              LD      H,L                 
5960: 20 77           JR      NZ,$59D9            ; {}
5962: 69              LD      L,C                 
5963: 74              LD      (HL),H              
5964: 68              LD      L,B                 
5965: 61              LD      H,C                 
5966: 20 70           JR      NZ,$59D8            ; {}
5968: 68              LD      L,B                 
5969: 6F              LD      L,A                 
596A: 74              LD      (HL),H              
596B: 6F              LD      L,A                 
596C: 67              LD      H,A                 
596D: 72              LD      (HL),D              
596E: 61              LD      H,C                 
596F: 70              LD      (HL),B              
5970: 68              LD      L,B                 
5971: 21 FF 4D        LD      HL,$4DFF            
5974: 6D              LD      L,L                 
5975: 6D              LD      L,L                 
5976: 2E 2E           LD      L,$2E               
5978: 2E 20           LD      L,$20               
597A: 53              LD      D,E                 
597B: 68              LD      L,B                 
597C: 65              LD      H,L                 
597D: 5E              LD      E,(HL)              
597E: 73              LD      (HL),E              
597F: 20 73           JR      NZ,$59F4            ; {}
5981: 6F              LD      L,A                 
5982: 20 62           JR      NZ,$59E6            ; {}
5984: 65              LD      H,L                 
5985: 61              LD      H,C                 
5986: 75              LD      (HL),L              
5987: 74              LD      (HL),H              
5988: 69              LD      L,C                 
5989: 66              LD      H,(HL)              
598A: 75              LD      (HL),L              
598B: 6C              LD      L,H                 
598C: 2E 2E           LD      L,$2E               
598E: 2E 20           LD      L,$20               
5990: 20 20           JR      NZ,$59B2            ; {}
5992: 20 49           JR      NZ,$59DD            ; {}
5994: 20 6D           JR      NZ,$5A03            ; {}
5996: 75              LD      (HL),L              
5997: 73              LD      (HL),E              
5998: 74              LD      (HL),H              
5999: 20 67           JR      NZ,$5A02            ; {}
599B: 69              LD      L,C                 
599C: 76              HALT                        
599D: 65              LD      H,L                 
599E: 20 79           JR      NZ,$5A19            ; {}
59A0: 6F              LD      L,A                 
59A1: 75              LD      (HL),L              
59A2: 20 73           JR      NZ,$5A17            ; {}
59A4: 6F              LD      L,A                 
59A5: 6D              LD      L,L                 
59A6: 65              LD      H,L                 
59A7: 74              LD      (HL),H              
59A8: 68              LD      L,B                 
59A9: 69              LD      L,C                 
59AA: 6E              LD      L,(HL)              
59AB: 67              LD      H,A                 
59AC: 20 66           JR      NZ,$5A14            ; {}
59AE: 6F              LD      L,A                 
59AF: 72              LD      (HL),D              
59B0: 20 20           JR      NZ,$59D2            ; {}
59B2: 20 79           JR      NZ,$5A2D            ; {}
59B4: 6F              LD      L,A                 
59B5: 75              LD      (HL),L              
59B6: 72              LD      (HL),D              
59B7: 20 74           JR      NZ,$5A2D            ; {}
59B9: 72              LD      (HL),D              
59BA: 6F              LD      L,A                 
59BB: 75              LD      (HL),L              
59BC: 62              LD      H,D                 
59BD: 6C              LD      L,H                 
59BE: 65              LD      H,L                 
59BF: 2E 2E           LD      L,$2E               
59C1: 2E 20           LD      L,$20               
59C3: 48              LD      C,B                 
59C4: 6D              LD      L,L                 
59C5: 6D              LD      L,L                 
59C6: 2E 2E           LD      L,$2E               
59C8: 2E 20           LD      L,$20               
59CA: 20 57           JR      NZ,$5A23            ; {}
59CC: 65              LD      H,L                 
59CD: 6C              LD      L,H                 
59CE: 6C              LD      L,H                 
59CF: 2C              INC     L                   
59D0: 20 69           JR      NZ,$5A3B            ; {}
59D2: 74              LD      (HL),H              
59D3: 6C              LD      L,H                 
59D4: 6F              LD      L,A                 
59D5: 6F              LD      L,A                 
59D6: 6B              LD      L,E                 
59D7: 73              LD      (HL),E              
59D8: 20 6C           JR      NZ,$5A46            ; {}
59DA: 69              LD      L,C                 
59DB: 6B              LD      L,E                 
59DC: 65              LD      H,L                 
59DD: 20 61           JR      NZ,$5A40            ; {}
59DF: 6C              LD      L,H                 
59E0: 6C              LD      L,H                 
59E1: 20 49           JR      NZ,$5A2C            ; {}
59E3: 68              LD      L,B                 
59E4: 61              LD      H,C                 
59E5: 76              HALT                        
59E6: 65              LD      H,L                 
59E7: 20 69           JR      NZ,$5A52            ; {}
59E9: 73              LD      (HL),E              
59EA: 20 74           JR      NZ,$5A60            ; {}
59EC: 68              LD      L,B                 
59ED: 69              LD      L,C                 
59EE: 73              LD      (HL),E              
59EF: 20 20           JR      NZ,$5A11            ; {}
59F1: 20 20           JR      NZ,$5A13            ; {}
59F3: 62              LD      H,D                 
59F4: 72              LD      (HL),D              
59F5: 6F              LD      L,A                 
59F6: 6F              LD      L,A                 
59F7: 6D              LD      L,L                 
59F8: 2E 2E           LD      L,$2E               
59FA: 2E 20           LD      L,$20               
59FC: 68              LD      L,B                 
59FD: 6F              LD      L,A                 
59FE: 77              LD      (HL),A              
59FF: 5E              LD      E,(HL)              
5A00: 6C              LD      L,H                 
5A01: 6C              LD      L,H                 
5A02: 20 74           JR      NZ,$5A78            ; {}
5A04: 68              LD      L,B                 
5A05: 61              LD      H,C                 
5A06: 74              LD      (HL),H              
5A07: 20 62           JR      NZ,$5A6B            ; {}
5A09: 65              LD      H,L                 
5A0A: 3F              CCF                         
5A0B: 20 20           JR      NZ,$5A2D            ; {}
5A0D: 20 20           JR      NZ,$5A2F            ; {}
5A0F: 20 20           JR      NZ,$5A31            ; {}
5A11: 20 20           JR      NZ,$5A33            ; {}
5A13: 20 20           JR      NZ,$5A35            ; {}
5A15: 20 20           JR      NZ,$5A37            ; {}
5A17: 46              LD      B,(HL)              
5A18: 69              LD      L,C                 
5A19: 6E              LD      L,(HL)              
5A1A: 65              LD      H,L                 
5A1B: 20 4E           JR      NZ,$5A6B            ; {}
5A1D: 6F              LD      L,A                 
5A1E: 2E 2E           LD      L,$2E               
5A20: 2E FE           LD      L,$FE               
5A22: 59              LD      E,C                 
5A23: 6F              LD      L,A                 
5A24: 75              LD      (HL),L              
5A25: 20 67           JR      NZ,$5A8E            ; {}
5A27: 6F              LD      L,A                 
5A28: 74              LD      (HL),H              
5A29: 20 61           JR      NZ,$5A8C            ; {}
5A2B: 20 42           JR      NZ,$5A6F            ; {}
5A2D: 72              LD      (HL),D              
5A2E: 6F              LD      L,A                 
5A2F: 6F              LD      L,A                 
5A30: 6D              LD      L,L                 
5A31: 20 61           JR      NZ,$5A94            ; {}
5A33: 73              LD      (HL),E              
5A34: 20 79           JR      NZ,$5AAF            ; {}
5A36: 6F              LD      L,A                 
5A37: 75              LD      (HL),L              
5A38: 72              LD      (HL),D              
5A39: 20 72           JR      NZ,$5AAD            ; {}
5A3B: 65              LD      H,L                 
5A3C: 77              LD      (HL),A              
5A3D: 61              LD      H,C                 
5A3E: 72              LD      (HL),D              
5A3F: 64              LD      H,H                 
5A40: 20 20           JR      NZ,$5A62            ; {}
5A42: 66              LD      H,(HL)              
5A43: 72              LD      (HL),D              
5A44: 6F              LD      L,A                 
5A45: 6D              LD      L,L                 
5A46: 20 4D           JR      NZ,$5A95            ; {}
5A48: 72              LD      (HL),D              
5A49: 2E 20           LD      L,$20               
5A4B: 57              LD      D,A                 
5A4C: 72              LD      (HL),D              
5A4D: 69              LD      L,C                 
5A4E: 74              LD      (HL),H              
5A4F: 65              LD      H,L                 
5A50: 21 20 42        LD      HL,$4220            
5A53: 75              LD      (HL),L              
5A54: 74              LD      (HL),H              
5A55: 20 74           JR      NZ,$5ACB            ; {}
5A57: 68              LD      L,B                 
5A58: 61              LD      H,C                 
5A59: 74              LD      (HL),H              
5A5A: 20 70           JR      NZ,$5ACC            ; {}
5A5C: 68              LD      L,B                 
5A5D: 6F              LD      L,A                 
5A5E: 74              LD      (HL),H              
5A5F: 6F              LD      L,A                 
5A60: 20 20           JR      NZ,$5A82            ; {}
5A62: 77              LD      (HL),A              
5A63: 61              LD      H,C                 
5A64: 73              LD      (HL),E              
5A65: 20 6E           JR      NZ,$5AD5            ; {}
5A67: 6F              LD      L,A                 
5A68: 74              LD      (HL),H              
5A69: 20 6F           JR      NZ,$5ADA            ; {}
5A6B: 66              LD      H,(HL)              
5A6C: 2E 2E           LD      L,$2E               
5A6E: 2E FF           LD      L,$FF               
5A70: 50              LD      D,B                 
5A71: 6C              LD      L,H                 
5A72: 65              LD      H,L                 
5A73: 61              LD      H,C                 
5A74: 73              LD      (HL),E              
5A75: 65              LD      H,L                 
5A76: 21 20 49        LD      HL,$4920            
5A79: 20 72           JR      NZ,$5AED            ; {}
5A7B: 65              LD      H,L                 
5A7C: 61              LD      H,C                 
5A7D: 6C              LD      L,H                 
5A7E: 6C              LD      L,H                 
5A7F: 79              LD      A,C                 
5A80: 6D              LD      L,L                 
5A81: 75              LD      (HL),L              
5A82: 73              LD      (HL),E              
5A83: 74              LD      (HL),H              
5A84: 20 69           JR      NZ,$5AEF            ; {}
5A86: 6E              LD      L,(HL)              
5A87: 73              LD      (HL),E              
5A88: 69              LD      L,C                 
5A89: 73              LD      (HL),E              
5A8A: 74              LD      (HL),H              
5A8B: 20 79           JR      NZ,$5B06            ; {}
5A8D: 6F              LD      L,A                 
5A8E: 75              LD      (HL),L              
5A8F: 20 68           JR      NZ,$5AF9            ; {}
5A91: 61              LD      H,C                 
5A92: 76              HALT                        
5A93: 65              LD      H,L                 
5A94: 20 74           JR      NZ,$5B0A            ; {}
5A96: 68              LD      L,B                 
5A97: 69              LD      L,C                 
5A98: 73              LD      (HL),E              
5A99: 20 E8           JR      NZ,$5A83            ; {}
5A9B: 21 20 20        LD      HL,$2020            
5A9E: 20 20           JR      NZ,$5AC0            ; {}
5AA0: 20 20           JR      NZ,$5AC2            ; {}
5AA2: 20 20           JR      NZ,$5AC4            ; {}
5AA4: 4F              LD      C,A                 
5AA5: 6B              LD      L,E                 
5AA6: 61              LD      H,C                 
5AA7: 79              LD      A,C                 
5AA8: 20 4E           JR      NZ,$5AF8            ; {}
5AAA: 6F              LD      L,A                 
5AAB: 20 57           JR      NZ,$5B04            ; {}
5AAD: 61              LD      H,C                 
5AAE: 79              LD      A,C                 
5AAF: FE 4F           CP      $4F                 
5AB1: 68              LD      L,B                 
5AB2: 20 62           JR      NZ,$5B16            ; {}
5AB4: 6F              LD      L,A                 
5AB5: 79              LD      A,C                 
5AB6: 21 20 20        LD      HL,$2020            
5AB9: 4C              LD      C,H                 
5ABA: 65              LD      H,L                 
5ABB: 74              LD      (HL),H              
5ABC: 74              LD      (HL),H              
5ABD: 65              LD      H,L                 
5ABE: 72              LD      (HL),D              
5ABF: 20 77           JR      NZ,$5B38            ; {}
5AC1: 72              LD      (HL),D              
5AC2: 69              LD      L,C                 
5AC3: 74              LD      (HL),H              
5AC4: 69              LD      L,C                 
5AC5: 6E              LD      L,(HL)              
5AC6: 67              LD      H,A                 
5AC7: 20 69           JR      NZ,$5B32            ; {}
5AC9: 73              LD      (HL),E              
5ACA: 20 73           JR      NZ,$5B3F            ; {}
5ACC: 75              LD      (HL),L              
5ACD: 63              LD      H,E                 
5ACE: 68              LD      L,B                 
5ACF: 20 61           JR      NZ,$5B32            ; {}
5AD1: 20 67           JR      NZ,$5B3A            ; {}
5AD3: 72              LD      (HL),D              
5AD4: 65              LD      H,L                 
5AD5: 61              LD      H,C                 
5AD6: 74              LD      (HL),H              
5AD7: 20 68           JR      NZ,$5B41            ; {}
5AD9: 6F              LD      L,A                 
5ADA: 62              LD      H,D                 
5ADB: 62              LD      H,D                 
5ADC: 79              LD      A,C                 
5ADD: 21 FF 48        LD      HL,$48FF            
5AE0: 65              LD      H,L                 
5AE1: 6C              LD      L,H                 
5AE2: 6C              LD      L,H                 
5AE3: 6F              LD      L,A                 
5AE4: 21 20 20        LD      HL,$2020            
5AE7: 49              LD      C,C                 
5AE8: 5E              LD      E,(HL)              
5AE9: 6D              LD      L,L                 
5AEA: 20 20           JR      NZ,$5B0C            ; {}
5AEC: 20 20           JR      NZ,$5B0E            ; {}
5AEE: 20 77           JR      NZ,$5B67            ; {}
5AF0: 72              LD      (HL),D              
5AF1: 69              LD      L,C                 
5AF2: 74              LD      (HL),H              
5AF3: 69              LD      L,C                 
5AF4: 6E              LD      L,(HL)              
5AF5: 67              LD      H,A                 
5AF6: 20 62           JR      NZ,$5B5A            ; {}
5AF8: 61              LD      H,C                 
5AF9: 63              LD      H,E                 
5AFA: 6B              LD      L,E                 
5AFB: 20 74           JR      NZ,$5B71            ; {}
5AFD: 6F              LD      L,A                 
5AFE: 20 43           JR      NZ,$5B43            ; {}
5B00: 68              LD      L,B                 
5B01: 72              LD      (HL),D              
5B02: 69              LD      L,C                 
5B03: 73              LD      (HL),E              
5B04: 74              LD      (HL),H              
5B05: 69              LD      L,C                 
5B06: 6E              LD      L,(HL)              
5B07: 65              LD      H,L                 
5B08: 20 6E           JR      NZ,$5B78            ; {}
5B0A: 6F              LD      L,A                 
5B0B: 77              LD      (HL),A              
5B0C: 21 FF 53        LD      HL,$53FF            
5B0F: 61              LD      H,C                 
5B10: 6C              LD      L,H                 
5B11: 75              LD      (HL),L              
5B12: 74              LD      (HL),H              
5B13: 61              LD      H,C                 
5B14: 74              LD      (HL),H              
5B15: 69              LD      L,C                 
5B16: 6F              LD      L,A                 
5B17: 6E              LD      L,(HL)              
5B18: 73              LD      (HL),E              
5B19: 21 20 20        LD      HL,$2020            
5B1C: 20 20           JR      NZ,$5B3E            ; {}
5B1E: 59              LD      E,C                 
5B1F: 6F              LD      L,A                 
5B20: 75              LD      (HL),L              
5B21: 20 77           JR      NZ,$5B9A            ; {}
5B23: 6F              LD      L,A                 
5B24: 75              LD      (HL),L              
5B25: 6C              LD      L,H                 
5B26: 64              LD      H,H                 
5B27: 6E              LD      L,(HL)              
5B28: 5E              LD      E,(HL)              
5B29: 74              LD      (HL),H              
5B2A: 20 20           JR      NZ,$5B4C            ; {}
5B2C: 20 20           JR      NZ,$5B4E            ; {}
5B2E: 6B              LD      L,E                 
5B2F: 6E              LD      L,(HL)              
5B30: 6F              LD      L,A                 
5B31: 77              LD      (HL),A              
5B32: 20 62           JR      NZ,$5B96            ; {}
5B34: 79              LD      A,C                 
5B35: 20 74           JR      NZ,$5BAB            ; {}
5B37: 68              LD      L,B                 
5B38: 65              LD      H,L                 
5B39: 20 6C           JR      NZ,$5BA7            ; {}
5B3B: 6F              LD      L,A                 
5B3C: 6F              LD      L,A                 
5B3D: 6B              LD      L,E                 
5B3E: 6F              LD      L,A                 
5B3F: 66              LD      H,(HL)              
5B40: 20 6D           JR      NZ,$5BAF            ; {}
5B42: 65              LD      H,L                 
5B43: 2C              INC     L                   
5B44: 20 62           JR      NZ,$5BA8            ; {}
5B46: 75              LD      (HL),L              
5B47: 74              LD      (HL),H              
5B48: 20 49           JR      NZ,$5B93            ; {}
5B4A: 20 20           JR      NZ,$5B6C            ; {}
5B4C: 20 20           JR      NZ,$5B6E            ; {}
5B4E: 75              LD      (HL),L              
5B4F: 73              LD      (HL),E              
5B50: 65              LD      H,L                 
5B51: 64              LD      H,H                 
5B52: 20 74           JR      NZ,$5BC8            ; {}
5B54: 6F              LD      L,A                 
5B55: 20 6C           JR      NZ,$5BC3            ; {}
5B57: 69              LD      L,C                 
5B58: 76              HALT                        
5B59: 65              LD      H,L                 
5B5A: 20 69           JR      NZ,$5BC5            ; {}
5B5C: 6E              LD      L,(HL)              
5B5D: 20 74           JR      NZ,$5BD3            ; {}
5B5F: 68              LD      L,B                 
5B60: 65              LD      H,L                 
5B61: 20 63           JR      NZ,$5BC6            ; {}
5B63: 61              LD      H,C                 
5B64: 73              LD      (HL),E              
5B65: 74              LD      (HL),H              
5B66: 6C              LD      L,H                 
5B67: 65              LD      H,L                 
5B68: 21 20 4D        LD      HL,$4D20            
5B6B: 79              LD      A,C                 
5B6C: 20 20           JR      NZ,$5B8E            ; {}
5B6E: 73              LD      (HL),E              
5B6F: 65              LD      H,L                 
5B70: 72              LD      (HL),D              
5B71: 76              HALT                        
5B72: 61              LD      H,C                 
5B73: 6E              LD      L,(HL)              
5B74: 74              LD      (HL),H              
5B75: 73              LD      (HL),E              
5B76: 20 77           JR      NZ,$5BEF            ; {}
5B78: 65              LD      H,L                 
5B79: 6E              LD      L,(HL)              
5B7A: 74              LD      (HL),H              
5B7B: 20 20           JR      NZ,$5B9D            ; {}
5B7D: 20 62           JR      NZ,$5BE1            ; {}
5B7F: 65              LD      H,L                 
5B80: 72              LD      (HL),D              
5B81: 73              LD      (HL),E              
5B82: 65              LD      H,L                 
5B83: 72              LD      (HL),D              
5B84: 6B              LD      L,E                 
5B85: 20 61           JR      NZ,$5BE8            ; {}
5B87: 6E              LD      L,(HL)              
5B88: 64              LD      H,H                 
5B89: 20 49           JR      NZ,$5BD4            ; {}
5B8B: 20 20           JR      NZ,$5BAD            ; {}
5B8D: 20 77           JR      NZ,$5C06            ; {}
5B8F: 61              LD      H,C                 
5B90: 73              LD      (HL),E              
5B91: 20 66           JR      NZ,$5BF9            ; {}
5B93: 6F              LD      L,A                 
5B94: 72              LD      (HL),D              
5B95: 63              LD      H,E                 
5B96: 65              LD      H,L                 
5B97: 64              LD      H,H                 
5B98: 20 74           JR      NZ,$5C0E            ; {}
5B9A: 6F              LD      L,A                 
5B9B: 20 20           JR      NZ,$5BBD            ; {}
5B9D: 20 66           JR      NZ,$5C05            ; {}
5B9F: 6C              LD      L,H                 
5BA0: 65              LD      H,L                 
5BA1: 65              LD      H,L                 
5BA2: 20 74           JR      NZ,$5C18            ; {}
5BA4: 6F              LD      L,A                 
5BA5: 20 6D           JR      NZ,$5C14            ; {}
5BA7: 79              LD      A,C                 
5BA8: 20 20           JR      NZ,$5BCA            ; {}
5BAA: 20 20           JR      NZ,$5BCC            ; {}
5BAC: 20 20           JR      NZ,$5BCE            ; {}
5BAE: 76              HALT                        
5BAF: 69              LD      L,C                 
5BB0: 6C              LD      L,H                 
5BB1: 6C              LD      L,H                 
5BB2: 61              LD      H,C                 
5BB3: 2E 2E           LD      L,$2E               
5BB5: 2E 20           LD      L,$20               
5BB7: 53              LD      D,E                 
5BB8: 6F              LD      L,A                 
5BB9: 2C              INC     L                   
5BBA: 20 79           JR      NZ,$5C35            ; {}
5BBC: 6F              LD      L,A                 
5BBD: 75              LD      (HL),L              
5BBE: 77              LD      (HL),A              
5BBF: 61              LD      H,C                 
5BC0: 6E              LD      L,(HL)              
5BC1: 74              LD      (HL),H              
5BC2: 20 74           JR      NZ,$5C38            ; {}
5BC4: 68              LD      L,B                 
5BC5: 65              LD      H,L                 
5BC6: 20 6B           JR      NZ,$5C33            ; {}
5BC8: 65              LD      H,L                 
5BC9: 79              LD      A,C                 
5BCA: 20 74           JR      NZ,$5C40            ; {}
5BCC: 6F              LD      L,A                 
5BCD: 20 55           JR      NZ,$5C24            ; {}
5BCF: 6B              LD      L,E                 
5BD0: 75              LD      (HL),L              
5BD1: 6B              LD      L,E                 
5BD2: 75              LD      (HL),L              
5BD3: 20 50           JR      NZ,$5C25            ; {}
5BD5: 72              LD      (HL),D              
5BD6: 61              LD      H,C                 
5BD7: 69              LD      L,C                 
5BD8: 72              LD      (HL),D              
5BD9: 69              LD      L,C                 
5BDA: 65              LD      H,L                 
5BDB: 2C              INC     L                   
5BDC: 20 20           JR      NZ,$5BFE            ; {}
5BDE: 64              LD      H,H                 
5BDF: 6F              LD      L,A                 
5BE0: 20 79           JR      NZ,$5C5B            ; {}
5BE2: 6F              LD      L,A                 
5BE3: 75              LD      (HL),L              
5BE4: 3F              CCF                         
5BE5: 20 20           JR      NZ,$5C07            ; {}
5BE7: 49              LD      C,C                 
5BE8: 20 6D           JR      NZ,$5C57            ; {}
5BEA: 61              LD      H,C                 
5BEB: 79              LD      A,C                 
5BEC: 20 20           JR      NZ,$5C0E            ; {}
5BEE: 62              LD      H,D                 
5BEF: 65              LD      H,L                 
5BF0: 20 61           JR      NZ,$5C53            ; {}
5BF2: 62              LD      H,D                 
5BF3: 6C              LD      L,H                 
5BF4: 65              LD      H,L                 
5BF5: 20 74           JR      NZ,$5C6B            ; {}
5BF7: 6F              LD      L,A                 
5BF8: 20 68           JR      NZ,$5C62            ; {}
5BFA: 65              LD      H,L                 
5BFB: 6C              LD      L,H                 
5BFC: 70              LD      (HL),B              
5BFD: 20 79           JR      NZ,$5C78            ; {}
5BFF: 6F              LD      L,A                 
5C00: 75              LD      (HL),L              
5C01: 2E 2E           LD      L,$2E               
5C03: 2E 20           LD      L,$20               
5C05: 20 4C           JR      NZ,$5C53            ; {}
5C07: 65              LD      H,L                 
5C08: 74              LD      (HL),H              
5C09: 5E              LD      E,(HL)              
5C0A: 73              LD      (HL),E              
5C0B: 20 20           JR      NZ,$5C2D            ; {}
5C0D: 20 6D           JR      NZ,$5C7C            ; {}
5C0F: 61              LD      H,C                 
5C10: 6B              LD      L,E                 
5C11: 65              LD      H,L                 
5C12: 2E 2E           LD      L,$2E               
5C14: 2E 20           LD      L,$20               
5C16: 61              LD      H,C                 
5C17: 20 64           JR      NZ,$5C7D            ; {}
5C19: 65              LD      H,L                 
5C1A: 61              LD      H,C                 
5C1B: 6C              LD      L,H                 
5C1C: 2C              INC     L                   
5C1D: 20 73           JR      NZ,$5C92            ; {}
5C1F: 68              LD      L,B                 
5C20: 61              LD      H,C                 
5C21: 6C              LD      L,H                 
5C22: 6C              LD      L,H                 
5C23: 20 77           JR      NZ,$5C9C            ; {}
5C25: 65              LD      H,L                 
5C26: 3F              CCF                         
5C27: 20 49           JR      NZ,$5C72            ; {}
5C29: 20 77           JR      NZ,$5CA2            ; {}
5C2B: 61              LD      H,C                 
5C2C: 6E              LD      L,(HL)              
5C2D: 74              LD      (HL),H              
5C2E: 79              LD      A,C                 
5C2F: 6F              LD      L,A                 
5C30: 75              LD      (HL),L              
5C31: 20 74           JR      NZ,$5CA7            ; {}
5C33: 6F              LD      L,A                 
5C34: 20 72           JR      NZ,$5CA8            ; {}
5C36: 65              LD      H,L                 
5C37: 74              LD      (HL),H              
5C38: 72              LD      (HL),D              
5C39: 69              LD      L,C                 
5C3A: 65              LD      H,L                 
5C3B: 76              HALT                        
5C3C: 65              LD      H,L                 
5C3D: 20 74           JR      NZ,$5CB3            ; {}
5C3F: 68              LD      L,B                 
5C40: 65              LD      H,L                 
5C41: 20 47           JR      NZ,$5C8A            ; {}
5C43: 6F              LD      L,A                 
5C44: 6C              LD      L,H                 
5C45: 64              LD      H,H                 
5C46: 65              LD      H,L                 
5C47: 6E              LD      L,(HL)              
5C48: 20 4C           JR      NZ,$5C96            ; {}
5C4A: 65              LD      H,L                 
5C4B: 61              LD      H,C                 
5C4C: 66              LD      H,(HL)              
5C4D: 20 49           JR      NZ,$5C98            ; {}
5C4F: 20 6C           JR      NZ,$5CBD            ; {}
5C51: 65              LD      H,L                 
5C52: 66              LD      H,(HL)              
5C53: 74              LD      (HL),H              
5C54: 20 62           JR      NZ,$5CB8            ; {}
5C56: 65              LD      H,L                 
5C57: 68              LD      L,B                 
5C58: 69              LD      L,C                 
5C59: 6E              LD      L,(HL)              
5C5A: 64              LD      H,H                 
5C5B: 20 69           JR      NZ,$5CC6            ; {}
5C5D: 6E              LD      L,(HL)              
5C5E: 74              LD      (HL),H              
5C5F: 68              LD      L,B                 
5C60: 65              LD      H,L                 
5C61: 20 63           JR      NZ,$5CC6            ; {}
5C63: 61              LD      H,C                 
5C64: 73              LD      (HL),E              
5C65: 74              LD      (HL),H              
5C66: 6C              LD      L,H                 
5C67: 65              LD      H,L                 
5C68: 20 77           JR      NZ,$5CE1            ; {}
5C6A: 68              LD      L,B                 
5C6B: 65              LD      H,L                 
5C6C: 6E              LD      L,(HL)              
5C6D: 20 49           JR      NZ,$5CB8            ; {}
5C6F: 20 66           JR      NZ,$5CD7            ; {}
5C71: 6C              LD      L,H                 
5C72: 65              LD      H,L                 
5C73: 64              LD      H,H                 
5C74: 2E 2E           LD      L,$2E               
5C76: 2E 20           LD      L,$20               
5C78: 20 20           JR      NZ,$5C9A            ; {}
5C7A: 20 20           JR      NZ,$5C9C            ; {}
5C7C: 20 20           JR      NZ,$5C9E            ; {}
5C7E: 20 20           JR      NZ,$5CA0            ; {}
5C80: 20 20           JR      NZ,$5CA2            ; {}
5C82: 4F              LD      C,A                 
5C83: 6B              LD      L,E                 
5C84: 61              LD      H,C                 
5C85: 79              LD      A,C                 
5C86: 20 4E           JR      NZ,$5CD6            ; {}
5C88: 6F              LD      L,A                 
5C89: 20 57           JR      NZ,$5CE2            ; {}
5C8B: 61              LD      H,C                 
5C8C: 79              LD      A,C                 
5C8D: FE 53           CP      $53                 
5C8F: 6D              LD      L,L                 
5C90: 61              LD      H,C                 
5C91: 73              LD      (HL),E              
5C92: 68              LD      L,B                 
5C93: 69              LD      L,C                 
5C94: 6E              LD      L,(HL)              
5C95: 67              LD      H,A                 
5C96: 21 20 20        LD      HL,$2020            
5C99: 54              LD      D,H                 
5C9A: 6F              LD      L,A                 
5C9B: 20 20           JR      NZ,$5CBD            ; {}
5C9D: 20 74           JR      NZ,$5D13            ; {}
5C9F: 65              LD      H,L                 
5CA0: 6C              LD      L,H                 
5CA1: 6C              LD      L,H                 
5CA2: 20 79           JR      NZ,$5D1D            ; {}
5CA4: 6F              LD      L,A                 
5CA5: 75              LD      (HL),L              
5CA6: 20 74           JR      NZ,$5D1C            ; {}
5CA8: 68              LD      L,B                 
5CA9: 65              LD      H,L                 
5CAA: 20 20           JR      NZ,$5CCC            ; {}
5CAC: 20 20           JR      NZ,$5CCE            ; {}
5CAE: 74              LD      (HL),H              
5CAF: 72              LD      (HL),D              
5CB0: 75              LD      (HL),L              
5CB1: 74              LD      (HL),H              
5CB2: 68              LD      L,B                 
5CB3: 2C              INC     L                   
5CB4: 20 74           JR      NZ,$5D2A            ; {}
5CB6: 68              LD      L,B                 
5CB7: 65              LD      H,L                 
5CB8: 72              LD      (HL),D              
5CB9: 65              LD      H,L                 
5CBA: 20 61           JR      NZ,$5D1D            ; {}
5CBC: 72              LD      (HL),D              
5CBD: 65              LD      H,L                 
5CBE: 66              LD      H,(HL)              
5CBF: 69              LD      L,C                 
5CC0: 76              HALT                        
5CC1: 65              LD      H,L                 
5CC2: 20 6C           JR      NZ,$5D30            ; {}
5CC4: 65              LD      H,L                 
5CC5: 61              LD      H,C                 
5CC6: 76              HALT                        
5CC7: 65              LD      H,L                 
5CC8: 73              LD      (HL),E              
5CC9: 2C              INC     L                   
5CCA: 20 61           JR      NZ,$5D2D            ; {}
5CCC: 6E              LD      L,(HL)              
5CCD: 64              LD      H,H                 
5CCE: 49              LD      C,C                 
5CCF: 20 77           JR      NZ,$5D48            ; {}
5CD1: 61              LD      H,C                 
5CD2: 6E              LD      L,(HL)              
5CD3: 74              LD      (HL),H              
5CD4: 20 74           JR      NZ,$5D4A            ; {}
5CD6: 68              LD      L,B                 
5CD7: 65              LD      H,L                 
5CD8: 6D              LD      L,L                 
5CD9: 20 61           JR      NZ,$5D3C            ; {}
5CDB: 6C              LD      L,H                 
5CDC: 6C              LD      L,H                 
5CDD: 21 4F 68        LD      HL,$684F            
5CE0: 2C              INC     L                   
5CE1: 20 79           JR      NZ,$5D5C            ; {}
5CE3: 6F              LD      L,A                 
5CE4: 75              LD      (HL),L              
5CE5: 5E              LD      E,(HL)              
5CE6: 6C              LD      L,H                 
5CE7: 6C              LD      L,H                 
5CE8: 20 6E           JR      NZ,$5D58            ; {}
5CEA: 65              LD      H,L                 
5CEB: 65              LD      H,L                 
5CEC: 64              LD      H,H                 
5CED: 20 74           JR      NZ,$5D63            ; {}
5CEF: 6F              LD      L,A                 
5CF0: 20 64           JR      NZ,$5D56            ; {}
5CF2: 6F              LD      L,A                 
5CF3: 20 73           JR      NZ,$5D68            ; {}
5CF5: 6F              LD      L,A                 
5CF6: 6D              LD      L,L                 
5CF7: 65              LD      H,L                 
5CF8: 20 64           JR      NZ,$5D5E            ; {}
5CFA: 69              LD      L,C                 
5CFB: 67              LD      H,A                 
5CFC: 2D              DEC     L                   
5CFD: 20 67           JR      NZ,$5D66            ; {}
5CFF: 69              LD      L,C                 
5D00: 6E              LD      L,(HL)              
5D01: 67              LD      H,A                 
5D02: 2C              INC     L                   
5D03: 20 73           JR      NZ,$5D78            ; {}
5D05: 6F              LD      L,A                 
5D06: 20 62           JR      NZ,$5D6A            ; {}
5D08: 75              LD      (HL),L              
5D09: 79              LD      A,C                 
5D0A: 20 61           JR      NZ,$5D6D            ; {}
5D0C: 20 20           JR      NZ,$5D2E            ; {}
5D0E: 73              LD      (HL),E              
5D0F: 68              LD      L,B                 
5D10: 6F              LD      L,A                 
5D11: 76              HALT                        
5D12: 65              LD      H,L                 
5D13: 6C              LD      L,H                 
5D14: 21 20 41        LD      HL,$4120            
5D17: 72              LD      (HL),D              
5D18: 65              LD      H,L                 
5D19: 20 79           JR      NZ,$5D94            ; {}
5D1B: 6F              LD      L,A                 
5D1C: 75              LD      (HL),L              
5D1D: 20 6F           JR      NZ,$5D8E            ; {}
5D1F: 66              LD      H,(HL)              
5D20: 66              LD      H,(HL)              
5D21: 2C              INC     L                   
5D22: 20 74           JR      NZ,$5D98            ; {}
5D24: 68              LD      L,B                 
5D25: 65              LD      H,L                 
5D26: 6E              LD      L,(HL)              
5D27: 3F              CCF                         
5D28: 20 20           JR      NZ,$5D4A            ; {}
5D2A: 47              LD      B,A                 
5D2B: 6F              LD      L,A                 
5D2C: 6F              LD      L,A                 
5D2D: 64              LD      H,H                 
5D2E: 6C              LD      L,H                 
5D2F: 75              LD      (HL),L              
5D30: 63              LD      H,E                 
5D31: 6B              LD      L,E                 
5D32: 21 FF 57        LD      HL,$57FF            
5D35: 65              LD      H,L                 
5D36: 6C              LD      L,H                 
5D37: 6C              LD      L,H                 
5D38: 2C              INC     L                   
5D39: 20 49           JR      NZ,$5D84            ; {}
5D3B: 20 6E           JR      NZ,$5DAB            ; {}
5D3D: 65              LD      H,L                 
5D3E: 76              HALT                        
5D3F: 65              LD      H,L                 
5D40: 72              LD      (HL),D              
5D41: 21 20 20        LD      HL,$2020            
5D44: 49              LD      C,C                 
5D45: 20 74           JR      NZ,$5DBB            ; {}
5D47: 68              LD      L,B                 
5D48: 6F              LD      L,A                 
5D49: 75              LD      (HL),L              
5D4A: 67              LD      H,A                 
5D4B: 68              LD      L,B                 
5D4C: 74              LD      (HL),H              
5D4D: 20 79           JR      NZ,$5DC8            ; {}
5D4F: 6F              LD      L,A                 
5D50: 75              LD      (HL),L              
5D51: 20 20           JR      NZ,$5D73            ; {}
5D53: 20 6C           JR      NZ,$5DC1            ; {}
5D55: 6F              LD      L,A                 
5D56: 6F              LD      L,A                 
5D57: 6B              LD      L,E                 
5D58: 65              LD      H,L                 
5D59: 64              LD      H,H                 
5D5A: 20 63           JR      NZ,$5DBF            ; {}
5D5C: 6F              LD      L,A                 
5D5D: 77              LD      (HL),A              
5D5E: 61              LD      H,C                 
5D5F: 72              LD      (HL),D              
5D60: 64              LD      H,H                 
5D61: 6C              LD      L,H                 
5D62: 79              LD      A,C                 
5D63: 2C              INC     L                   
5D64: 62              LD      H,D                 
5D65: 75              LD      (HL),L              
5D66: 74              LD      (HL),H              
5D67: 2E 2E           LD      L,$2E               
5D69: 2E 20           LD      L,$20               
5D6B: 20 50           JR      NZ,$5DBD            ; {}
5D6D: 6C              LD      L,H                 
5D6E: 65              LD      H,L                 
5D6F: 61              LD      H,C                 
5D70: 73              LD      (HL),E              
5D71: 65              LD      H,L                 
5D72: 2C              INC     L                   
5D73: 20 6C           JR      NZ,$5DE1            ; {}
5D75: 65              LD      H,L                 
5D76: 61              LD      H,C                 
5D77: 76              HALT                        
5D78: 65              LD      H,L                 
5D79: 20 6D           JR      NZ,$5DE8            ; {}
5D7B: 65              LD      H,L                 
5D7C: 2E 2E           LD      L,$2E               
5D7E: 2E 20           LD      L,$20               
5D80: 6A              LD      L,D                 
5D81: 75              LD      (HL),L              
5D82: 73              LD      (HL),E              
5D83: 74              LD      (HL),H              
5D84: 67              LD      H,A                 
5D85: 65              LD      H,L                 
5D86: 74              LD      (HL),H              
5D87: 20 6F           JR      NZ,$5DF8            ; {}
5D89: 75              LD      (HL),L              
5D8A: 74              LD      (HL),H              
5D8B: 20 68           JR      NZ,$5DF5            ; {}
5D8D: 65              LD      H,L                 
5D8E: 72              LD      (HL),D              
5D8F: 65              LD      H,L                 
5D90: 21 FF 41        LD      HL,$41FF            
5D93: 68              LD      L,B                 
5D94: 68              LD      L,B                 
5D95: 21 20 20        LD      HL,$2020            
5D98: 54              LD      D,H                 
5D99: 72              LD      (HL),D              
5D9A: 65              LD      H,L                 
5D9B: 73              LD      (HL),E              
5D9C: 20 42           JR      NZ,$5DE0            ; {}
5D9E: 69              LD      L,C                 
5D9F: 65              LD      H,L                 
5DA0: 6E              LD      L,(HL)              
5DA1: 21 49 20        LD      HL,$2049            
5DA4: 73              LD      (HL),E              
5DA5: 65              LD      H,L                 
5DA6: 65              LD      H,L                 
5DA7: 20 79           JR      NZ,$5E22            ; {}
5DA9: 6F              LD      L,A                 
5DAA: 75              LD      (HL),L              
5DAB: 20 68           JR      NZ,$5E15            ; {}
5DAD: 61              LD      H,C                 
5DAE: 76              HALT                        
5DAF: 65              LD      H,L                 
5DB0: 20 20           JR      NZ,$5DD2            ; {}
5DB2: 72              LD      (HL),D              
5DB3: 65              LD      H,L                 
5DB4: 63              LD      H,E                 
5DB5: 6F              LD      L,A                 
5DB6: 76              HALT                        
5DB7: 65              LD      H,L                 
5DB8: 72              LD      (HL),D              
5DB9: 65              LD      H,L                 
5DBA: 64              LD      H,H                 
5DBB: 20 61           JR      NZ,$5E1E            ; {}
5DBD: 6C              LD      L,H                 
5DBE: 6C              LD      L,H                 
5DBF: 20 6F           JR      NZ,$5E30            ; {}
5DC1: 66              LD      H,(HL)              
5DC2: 74              LD      (HL),H              
5DC3: 68              LD      L,B                 
5DC4: 65              LD      H,L                 
5DC5: 20 6C           JR      NZ,$5E33            ; {}
5DC7: 65              LD      H,L                 
5DC8: 61              LD      H,C                 
5DC9: 76              HALT                        
5DCA: 65              LD      H,L                 
5DCB: 73              LD      (HL),E              
5DCC: 21 20 4E        LD      HL,$4E20            
5DCF: 6F              LD      L,A                 
5DD0: 77              LD      (HL),A              
5DD1: 2C              INC     L                   
5DD2: 6D              LD      L,L                 
5DD3: 6F              LD      L,A                 
5DD4: 76              HALT                        
5DD5: 65              LD      H,L                 
5DD6: 20 74           JR      NZ,$5E4C            ; {}
5DD8: 68              LD      L,B                 
5DD9: 69              LD      L,C                 
5DDA: 73              LD      (HL),E              
5DDB: 20 62           JR      NZ,$5E3F            ; {}
5DDD: 6F              LD      L,A                 
5DDE: 78              LD      A,B                 
5DDF: 20 20           JR      NZ,$5E01            ; {}
5DE1: 20 61           JR      NZ,$5E44            ; {}
5DE3: 6E              LD      L,(HL)              
5DE4: 64              LD      H,H                 
5DE5: 20 79           JR      NZ,$5E60            ; {}
5DE7: 6F              LD      L,A                 
5DE8: 75              LD      (HL),L              
5DE9: 20 77           JR      NZ,$5E62            ; {}
5DEB: 69              LD      L,C                 
5DEC: 6C              LD      L,H                 
5DED: 6C              LD      L,H                 
5DEE: 20 20           JR      NZ,$5E10            ; {}
5DF0: 20 20           JR      NZ,$5E12            ; {}
5DF2: 66              LD      H,(HL)              
5DF3: 69              LD      L,C                 
5DF4: 6E              LD      L,(HL)              
5DF5: 64              LD      H,H                 
5DF6: 20 79           JR      NZ,$5E71            ; {}
5DF8: 6F              LD      L,A                 
5DF9: 75              LD      (HL),L              
5DFA: 72              LD      (HL),D              
5DFB: 20 20           JR      NZ,$5E1D            ; {}
5DFD: 20 20           JR      NZ,$5E1F            ; {}
5DFF: 20 20           JR      NZ,$5E21            ; {}
5E01: 20 72           JR      NZ,$5E75            ; {}
5E03: 65              LD      H,L                 
5E04: 77              LD      (HL),A              
5E05: 61              LD      H,C                 
5E06: 72              LD      (HL),D              
5E07: 64              LD      H,H                 
5E08: 21 FF 49        LD      HL,$49FF            
5E0B: 20 61           JR      NZ,$5E6E            ; {}
5E0D: 6D              LD      L,L                 
5E0E: 20 66           JR      NZ,$5E76            ; {}
5E10: 6F              LD      L,A                 
5E11: 72              LD      (HL),D              
5E12: 65              LD      H,L                 
5E13: 76              HALT                        
5E14: 65              LD      H,L                 
5E15: 72              LD      (HL),D              
5E16: 20 69           JR      NZ,$5E81            ; {}
5E18: 6E              LD      L,(HL)              
5E19: 20 79           JR      NZ,$5E94            ; {}
5E1B: 6F              LD      L,A                 
5E1C: 75              LD      (HL),L              
5E1D: 72              LD      (HL),D              
5E1E: 20 64           JR      NZ,$5E84            ; {}
5E20: 65              LD      H,L                 
5E21: 62              LD      H,D                 
5E22: 74              LD      (HL),H              
5E23: 20 66           JR      NZ,$5E8B            ; {}
5E25: 6F              LD      L,A                 
5E26: 72              LD      (HL),D              
5E27: 20 20           JR      NZ,$5E49            ; {}
5E29: 20 67           JR      NZ,$5E92            ; {}
5E2B: 65              LD      H,L                 
5E2C: 74              LD      (HL),H              
5E2D: 74              LD      (HL),H              
5E2E: 69              LD      L,C                 
5E2F: 6E              LD      L,(HL)              
5E30: 67              LD      H,A                 
5E31: 20 6D           JR      NZ,$5EA0            ; {}
5E33: 79              LD      A,C                 
5E34: 20 20           JR      NZ,$5E56            ; {}
5E36: 20 20           JR      NZ,$5E58            ; {}
5E38: 20 20           JR      NZ,$5E5A            ; {}
5E3A: 6C              LD      L,H                 
5E3B: 65              LD      H,L                 
5E3C: 61              LD      H,C                 
5E3D: 76              HALT                        
5E3E: 65              LD      H,L                 
5E3F: 73              LD      (HL),E              
5E40: 20 62           JR      NZ,$5EA4            ; {}
5E42: 61              LD      H,C                 
5E43: 63              LD      H,E                 
5E44: 6B              LD      L,E                 
5E45: 21 FF 41        LD      HL,$41FF            
5E48: 68              LD      L,B                 
5E49: 21 20 20        LD      HL,$2020            
5E4C: 42              LD      B,D                 
5E4D: 6F              LD      L,A                 
5E4E: 6E              LD      L,(HL)              
5E4F: 6A              LD      L,D                 
5E50: 6F              LD      L,A                 
5E51: 75              LD      (HL),L              
5E52: 72              LD      (HL),D              
5E53: 21 20 20        LD      HL,$2020            
5E56: 20 23           JR      NZ,$5E7B            ; {}
5E58: 23              INC     HL                  
5E59: 23              INC     HL                  
5E5A: 23              INC     HL                  
5E5B: 23              INC     HL                  
5E5C: 2C              INC     L                   
5E5D: 20 66           JR      NZ,$5EC5            ; {}
5E5F: 6F              LD      L,A                 
5E60: 72              LD      (HL),D              
5E61: 20 74           JR      NZ,$5ED7            ; {}
5E63: 68              LD      L,B                 
5E64: 65              LD      H,L                 
5E65: 20 20           JR      NZ,$5E87            ; {}
5E67: 6C              LD      L,H                 
5E68: 6F              LD      L,A                 
5E69: 76              HALT                        
5E6A: 65              LD      H,L                 
5E6B: 20 6F           JR      NZ,$5EDC            ; {}
5E6D: 66              LD      H,(HL)              
5E6E: 20 6A           JR      NZ,$5EDA            ; {}
5E70: 75              LD      (HL),L              
5E71: 73              LD      (HL),E              
5E72: 74              LD      (HL),H              
5E73: 69              LD      L,C                 
5E74: 63              LD      H,E                 
5E75: 65              LD      H,L                 
5E76: 2C              INC     L                   
5E77: 61              LD      H,C                 
5E78: 6E              LD      L,(HL)              
5E79: 64              LD      H,H                 
5E7A: 20 6D           JR      NZ,$5EE9            ; {}
5E7C: 79              LD      A,C                 
5E7D: 20 6F           JR      NZ,$5EEE            ; {}
5E7F: 77              LD      (HL),A              
5E80: 6E              LD      L,(HL)              
5E81: 20 73           JR      NZ,$5EF6            ; {}
5E83: 61              LD      H,C                 
5E84: 6B              LD      L,E                 
5E85: 65              LD      H,L                 
5E86: 2C              INC     L                   
5E87: 79              LD      A,C                 
5E88: 6F              LD      L,A                 
5E89: 75              LD      (HL),L              
5E8A: 20 6D           JR      NZ,$5EF9            ; {}
5E8C: 75              LD      (HL),L              
5E8D: 73              LD      (HL),E              
5E8E: 74              LD      (HL),H              
5E8F: 20 66           JR      NZ,$5EF7            ; {}
5E91: 69              LD      L,C                 
5E92: 6E              LD      L,(HL)              
5E93: 64              LD      H,H                 
5E94: 20 20           JR      NZ,$5EB6            ; {}
5E96: 20 61           JR      NZ,$5EF9            ; {}
5E98: 6C              LD      L,H                 
5E99: 6C              LD      L,H                 
5E9A: 20 74           JR      NZ,$5F10            ; {}
5E9C: 68              LD      L,B                 
5E9D: 65              LD      H,L                 
5E9E: 20 6C           JR      NZ,$5F0C            ; {}
5EA0: 65              LD      H,L                 
5EA1: 61              LD      H,C                 
5EA2: 76              HALT                        
5EA3: 65              LD      H,L                 
5EA4: 73              LD      (HL),E              
5EA5: 21 FF 45        LD      HL,$45FF            
5EA8: 72              LD      (HL),D              
5EA9: 2E 2E           LD      L,$2E               
5EAB: 2E 55           LD      L,$55               
5EAD: 68              LD      L,B                 
5EAE: 2E 2E           LD      L,$2E               
5EB0: 2E 48           LD      L,$48               
5EB2: 6D              LD      L,L                 
5EB3: 6D              LD      L,L                 
5EB4: 2E 2E           LD      L,$2E               
5EB6: 2E 48           LD      L,$48               
5EB8: 6F              LD      L,A                 
5EB9: 77              LD      (HL),A              
5EBA: 20 74           JR      NZ,$5F30            ; {}
5EBC: 6F              LD      L,A                 
5EBD: 20 73           JR      NZ,$5F32            ; {}
5EBF: 61              LD      H,C                 
5EC0: 79              LD      A,C                 
5EC1: 2E 2E           LD      L,$2E               
5EC3: 2E 20           LD      L,$20               
5EC5: 20 20           JR      NZ,$5EE7            ; {}
5EC7: 50              LD      D,B                 
5EC8: 6C              LD      L,H                 
5EC9: 65              LD      H,L                 
5ECA: 61              LD      H,C                 
5ECB: 73              LD      (HL),E              
5ECC: 65              LD      H,L                 
5ECD: 20 63           JR      NZ,$5F32            ; {}
5ECF: 61              LD      H,C                 
5ED0: 6C              LD      L,H                 
5ED1: 6C              LD      L,H                 
5ED2: 2E 2E           LD      L,$2E               
5ED4: 2E 20           LD      L,$20               
5ED6: 20 4F           JR      NZ,$5F27            ; {}
5ED8: 75              LD      (HL),L              
5ED9: 74              LD      (HL),H              
5EDA: 73              LD      (HL),E              
5EDB: 69              LD      L,C                 
5EDC: 64              LD      H,H                 
5EDD: 65              LD      H,L                 
5EDE: 2E 2E           LD      L,$2E               
5EE0: 2E 20           LD      L,$20               
5EE2: 20 2E           JR      NZ,$5F12            ; {}
5EE4: 2E 2E           LD      L,$2E               
5EE6: 20 49           JR      NZ,$5F31            ; {}
5EE8: 74              LD      (HL),H              
5EE9: 20 73           JR      NZ,$5F5E            ; {}
5EEB: 65              LD      H,L                 
5EEC: 65              LD      H,L                 
5EED: 6D              LD      L,L                 
5EEE: 73              LD      (HL),E              
5EEF: 20 74           JR      NZ,$5F65            ; {}
5EF1: 68              LD      L,B                 
5EF2: 61              LD      H,C                 
5EF3: 74              LD      (HL),H              
5EF4: 20 20           JR      NZ,$5F16            ; {}
5EF6: 20 6F           JR      NZ,$5F67            ; {}
5EF8: 6C              LD      L,H                 
5EF9: 64              LD      H,H                 
5EFA: 20 6D           JR      NZ,$5F69            ; {}
5EFC: 61              LD      H,C                 
5EFD: 6E              LD      L,(HL)              
5EFE: 20 55           JR      NZ,$5F55            ; {}
5F00: 6C              LD      L,H                 
5F01: 72              LD      (HL),D              
5F02: 69              LD      L,C                 
5F03: 72              LD      (HL),D              
5F04: 61              LD      H,C                 
5F05: 20 20           JR      NZ,$5F27            ; {}
5F07: 69              LD      L,C                 
5F08: 73              LD      (HL),E              
5F09: 20 61           JR      NZ,$5F6C            ; {}
5F0B: 20 73           JR      NZ,$5F80            ; {}
5F0D: 68              LD      L,B                 
5F0E: 79              LD      A,C                 
5F0F: 20 67           JR      NZ,$5F78            ; {}
5F11: 75              LD      (HL),L              
5F12: 79              LD      A,C                 
5F13: 2C              INC     L                   
5F14: 20 20           JR      NZ,$5F36            ; {}
5F16: 20 69           JR      NZ,$5F81            ; {}
5F18: 6E              LD      L,(HL)              
5F19: 20 70           JR      NZ,$5F8B            ; {}
5F1B: 65              LD      H,L                 
5F1C: 72              LD      (HL),D              
5F1D: 73              LD      (HL),E              
5F1E: 6F              LD      L,A                 
5F1F: 6E              LD      L,(HL)              
5F20: 2E 2E           LD      L,$2E               
5F22: 2E FF           LD      L,$FF               
5F24: 5E              LD      E,(HL)              
5F25: 42              LD      B,D                 
5F26: 52              LD      D,D                 
5F27: 52              LD      D,D                 
5F28: 49              LD      C,C                 
5F29: 4E              LD      C,(HL)              
5F2A: 47              LD      B,A                 
5F2B: 21 20 42        LD      HL,$4220            
5F2E: 52              LD      D,D                 
5F2F: 52              LD      D,D                 
5F30: 49              LD      C,C                 
5F31: 4E              LD      C,(HL)              
5F32: 47              LD      B,A                 
5F33: 21 48 65        LD      HL,$6548            
5F36: 6C              LD      L,H                 
5F37: 6C              LD      L,H                 
5F38: 6F              LD      L,A                 
5F39: 21 20 20        LD      HL,$2020            
5F3C: 49              LD      C,C                 
5F3D: 74              LD      (HL),H              
5F3E: 5E              LD      E,(HL)              
5F3F: 73              LD      (HL),E              
5F40: 20 6D           JR      NZ,$5FAF            ; {}
5F42: 65              LD      H,L                 
5F43: 2C              INC     L                   
5F44: 55              LD      D,L                 
5F45: 6C              LD      L,H                 
5F46: 72              LD      (HL),D              
5F47: 69              LD      L,C                 
5F48: 72              LD      (HL),D              
5F49: 61              LD      H,C                 
5F4A: 21 20 20        LD      HL,$2020            
5F4D: 41              LD      B,C                 
5F4E: 73              LD      (HL),E              
5F4F: 6B              LD      L,E                 
5F50: 20 6D           JR      NZ,$5FBF            ; {}
5F52: 65              LD      H,L                 
5F53: 20 61           JR      NZ,$5FB6            ; {}
5F55: 6E              LD      L,(HL)              
5F56: 79              LD      A,C                 
5F57: 74              LD      (HL),H              
5F58: 68              LD      L,B                 
5F59: 69              LD      L,C                 
5F5A: 6E              LD      L,(HL)              
5F5B: 67              LD      H,A                 
5F5C: 20 61           JR      NZ,$5FBF            ; {}
5F5E: 62              LD      H,D                 
5F5F: 6F              LD      L,A                 
5F60: 75              LD      (HL),L              
5F61: 74              LD      (HL),H              
5F62: 20 20           JR      NZ,$5F84            ; {}
5F64: 74              LD      (HL),H              
5F65: 68              LD      L,B                 
5F66: 65              LD      H,L                 
5F67: 20 69           JR      NZ,$5FD2            ; {}
5F69: 73              LD      (HL),E              
5F6A: 6C              LD      L,H                 
5F6B: 61              LD      H,C                 
5F6C: 6E              LD      L,(HL)              
5F6D: 64              LD      H,H                 
5F6E: 21 20 20        LD      HL,$2020            
5F71: 49              LD      C,C                 
5F72: 66              LD      H,(HL)              
5F73: 20 79           JR      NZ,$5FEE            ; {}
5F75: 6F              LD      L,A                 
5F76: 75              LD      (HL),L              
5F77: 20 67           JR      NZ,$5FE0            ; {}
5F79: 65              LD      H,L                 
5F7A: 74              LD      (HL),H              
5F7B: 20 6C           JR      NZ,$5FE9            ; {}
5F7D: 6F              LD      L,A                 
5F7E: 73              LD      (HL),E              
5F7F: 74              LD      (HL),H              
5F80: 2C              INC     L                   
5F81: 20 20           JR      NZ,$5FA3            ; {}
5F83: 20 67           JR      NZ,$5FEC            ; {}
5F85: 69              LD      L,C                 
5F86: 76              HALT                        
5F87: 65              LD      H,L                 
5F88: 20 6D           JR      NZ,$5FF7            ; {}
5F8A: 65              LD      H,L                 
5F8B: 20 61           JR      NZ,$5FEE            ; {}
5F8D: 20 63           JR      NZ,$5FF2            ; {}
5F8F: 61              LD      H,C                 
5F90: 6C              LD      L,H                 
5F91: 6C              LD      L,H                 
5F92: 21 20 42        LD      HL,$4220            
5F95: 79              LD      A,C                 
5F96: 65              LD      H,L                 
5F97: 21 20 43        LD      HL,$4320            
5F9A: 4C              LD      C,H                 
5F9B: 49              LD      C,C                 
5F9C: 43              LD      B,E                 
5F9D: 4B              LD      C,E                 
5F9E: 21 5E FF        LD      HL,$FF5E            
5FA1: 5E              LD      E,(HL)              
5FA2: 42              LD      B,D                 
5FA3: 52              LD      D,D                 
5FA4: 52              LD      D,D                 
5FA5: 49              LD      C,C                 
5FA6: 4E              LD      C,(HL)              
5FA7: 47              LD      B,A                 
5FA8: 21 20 42        LD      HL,$4220            
5FAB: 52              LD      D,D                 
5FAC: 52              LD      D,D                 
5FAD: 49              LD      C,C                 
5FAE: 4E              LD      C,(HL)              
5FAF: 47              LD      B,A                 
5FB0: 21 48 65        LD      HL,$6548            
5FB3: 6C              LD      L,H                 
5FB4: 6C              LD      L,H                 
5FB5: 6F              LD      L,A                 
5FB6: 2C              INC     L                   
5FB7: 20 74           JR      NZ,$602D            ; {}
5FB9: 68              LD      L,B                 
5FBA: 69              LD      L,C                 
5FBB: 73              LD      (HL),E              
5FBC: 20 69           JR      NZ,$6027            ; {}
5FBE: 73              LD      (HL),E              
5FBF: 20 20           JR      NZ,$5FE1            ; {}
5FC1: 55              LD      D,L                 
5FC2: 6C              LD      L,H                 
5FC3: 72              LD      (HL),D              
5FC4: 69              LD      L,C                 
5FC5: 72              LD      (HL),D              
5FC6: 61              LD      H,C                 
5FC7: 21 20 2E        LD      HL,$2E20            
5FCA: 2E 2E           LD      L,$2E               
5FCC: 57              LD      D,A                 
5FCD: 65              LD      H,L                 
5FCE: 6C              LD      L,H                 
5FCF: 6C              LD      L,H                 
5FD0: 2C              INC     L                   
5FD1: 6D              LD      L,L                 
5FD2: 6F              LD      L,A                 
5FD3: 73              LD      (HL),E              
5FD4: 74              LD      (HL),H              
5FD5: 20 4D           JR      NZ,$6024            ; {}
5FD7: 6F              LD      L,A                 
5FD8: 62              LD      H,D                 
5FD9: 6C              LD      L,H                 
5FDA: 69              LD      L,C                 
5FDB: 6E              LD      L,(HL)              
5FDC: 73              LD      (HL),E              
5FDD: 20 20           JR      NZ,$5FFF            ; {}
5FDF: 20 20           JR      NZ,$6001            ; {}
5FE1: 6C              LD      L,H                 
5FE2: 69              LD      L,C                 
5FE3: 76              HALT                        
5FE4: 65              LD      H,L                 
5FE5: 20 69           JR      NZ,$6050            ; {}
5FE7: 6E              LD      L,(HL)              
5FE8: 20 74           JR      NZ,$605E            ; {}
5FEA: 68              LD      L,B                 
5FEB: 65              LD      H,L                 
5FEC: 20 4D           JR      NZ,$603B            ; {}
5FEE: 79              LD      A,C                 
5FEF: 73              LD      (HL),E              
5FF0: 2D              DEC     L                   
5FF1: 74              LD      (HL),H              
5FF2: 65              LD      H,L                 
5FF3: 72              LD      (HL),D              
5FF4: 69              LD      L,C                 
5FF5: 6F              LD      L,A                 
5FF6: 75              LD      (HL),L              
5FF7: 73              LD      (HL),E              
5FF8: 20 46           JR      NZ,$6040            ; {}
5FFA: 6F              LD      L,A                 
5FFB: 72              LD      (HL),D              
5FFC: 65              LD      H,L                 
5FFD: 73              LD      (HL),E              
5FFE: 74              LD      (HL),H              
5FFF: 2C              INC     L                   
6000: 20 62           JR      NZ,$6064            ; {}
6002: 75              LD      (HL),L              
6003: 74              LD      (HL),H              
6004: 20 73           JR      NZ,$6079            ; {}
6006: 6F              LD      L,A                 
6007: 6D              LD      L,L                 
6008: 65              LD      H,L                 
6009: 20 6C           JR      NZ,$6077            ; {}
600B: 69              LD      L,C                 
600C: 76              HALT                        
600D: 65              LD      H,L                 
600E: 20 69           JR      NZ,$6079            ; {}
6010: 6E              LD      L,(HL)              
6011: 74              LD      (HL),H              
6012: 68              LD      L,B                 
6013: 65              LD      H,L                 
6014: 20 63           JR      NZ,$6079            ; {}
6016: 61              LD      H,C                 
6017: 76              HALT                        
6018: 65              LD      H,L                 
6019: 73              LD      (HL),E              
601A: 20 6F           JR      NZ,$608B            ; {}
601C: 66              LD      H,(HL)              
601D: 20 54           JR      NZ,$6073            ; {}
601F: 61              LD      H,C                 
6020: 6C              LD      L,H                 
6021: 54              LD      D,H                 
6022: 61              LD      H,C                 
6023: 6C              LD      L,H                 
6024: 20 48           JR      NZ,$606E            ; {}
6026: 65              LD      H,L                 
6027: 69              LD      L,C                 
6028: 67              LD      H,A                 
6029: 68              LD      L,B                 
602A: 74              LD      (HL),H              
602B: 73              LD      (HL),E              
602C: 2E 2E           LD      L,$2E               
602E: 2E 20           LD      L,$20               
6030: 20 49           JR      NZ,$607B            ; {}
6032: 20 68           JR      NZ,$609C            ; {}
6034: 6F              LD      L,A                 
6035: 70              LD      (HL),B              
6036: 65              LD      H,L                 
6037: 20 74           JR      NZ,$60AD            ; {}
6039: 68              LD      L,B                 
603A: 61              LD      H,C                 
603B: 74              LD      (HL),H              
603C: 20 69           JR      NZ,$60A7            ; {}
603E: 73              LD      (HL),E              
603F: 20 20           JR      NZ,$6061            ; {}
6041: 77              LD      (HL),A              
6042: 68              LD      L,B                 
6043: 61              LD      H,C                 
6044: 74              LD      (HL),H              
6045: 20 79           JR      NZ,$60C0            ; {}
6047: 6F              LD      L,A                 
6048: 75              LD      (HL),L              
6049: 20 77           JR      NZ,$60C2            ; {}
604B: 61              LD      H,C                 
604C: 6E              LD      L,(HL)              
604D: 74              LD      (HL),H              
604E: 65              LD      H,L                 
604F: 64              LD      H,H                 
6050: 20 74           JR      NZ,$60C6            ; {}
6052: 6F              LD      L,A                 
6053: 20 6B           JR      NZ,$60C0            ; {}
6055: 6E              LD      L,(HL)              
6056: 6F              LD      L,A                 
6057: 77              LD      (HL),A              
6058: 21 20 43        LD      HL,$4320            
605B: 4C              LD      C,H                 
605C: 49              LD      C,C                 
605D: 43              LD      B,E                 
605E: 4B              LD      C,E                 
605F: 21 5E FF        LD      HL,$FF5E            
6062: 5E              LD      E,(HL)              
6063: 42              LD      B,D                 
6064: 52              LD      D,D                 
6065: 52              LD      D,D                 
6066: 49              LD      C,C                 
6067: 4E              LD      C,(HL)              
6068: 47              LD      B,A                 
6069: 21 20 42        LD      HL,$4220            
606C: 52              LD      D,D                 
606D: 52              LD      D,D                 
606E: 49              LD      C,C                 
606F: 4E              LD      C,(HL)              
6070: 47              LD      B,A                 
6071: 21 59 65        LD      HL,$6559            
6074: 73              LD      (HL),E              
6075: 2C              INC     L                   
6076: 20 74           JR      NZ,$60EC            ; {}
6078: 68              LD      L,B                 
6079: 69              LD      L,C                 
607A: 73              LD      (HL),E              
607B: 20 69           JR      NZ,$60E6            ; {}
607D: 73              LD      (HL),E              
607E: 20 20           JR      NZ,$60A0            ; {}
6080: 20 20           JR      NZ,$60A2            ; {}
6082: 55              LD      D,L                 
6083: 6C              LD      L,H                 
6084: 72              LD      (HL),D              
6085: 69              LD      L,C                 
6086: 72              LD      (HL),D              
6087: 61              LD      H,C                 
6088: 2E 20           LD      L,$20               
608A: 20 54           JR      NZ,$60E0            ; {}
608C: 68              LD      L,B                 
608D: 65              LD      H,L                 
608E: 20 20           JR      NZ,$60B0            ; {}
6090: 20 20           JR      NZ,$60B2            ; {}
6092: 49              LD      C,C                 
6093: 6E              LD      L,(HL)              
6094: 64              LD      H,H                 
6095: 69              LD      L,C                 
6096: 67              LD      H,A                 
6097: 65              LD      H,L                 
6098: 73              LD      (HL),E              
6099: 74              LD      (HL),H              
609A: 69              LD      L,C                 
609B: 62              LD      H,D                 
609C: 6C              LD      L,H                 
609D: 65              LD      H,L                 
609E: 20 20           JR      NZ,$60C0            ; {}
60A0: 20 20           JR      NZ,$60C2            ; {}
60A2: 46              LD      B,(HL)              
60A3: 6C              LD      L,H                 
60A4: 6F              LD      L,A                 
60A5: 77              LD      (HL),A              
60A6: 65              LD      H,L                 
60A7: 72              LD      (HL),D              
60A8: 73              LD      (HL),E              
60A9: 20 6F           JR      NZ,$611A            ; {}
60AB: 66              LD      H,(HL)              
60AC: 20 20           JR      NZ,$60CE            ; {}
60AE: 20 20           JR      NZ,$60D0            ; {}
60B0: 20 20           JR      NZ,$60D2            ; {}
60B2: 47              LD      B,A                 
60B3: 6F              LD      L,A                 
60B4: 70              LD      (HL),B              
60B5: 6F              LD      L,A                 
60B6: 6E              LD      L,(HL)              
60B7: 67              LD      H,A                 
60B8: 61              LD      H,C                 
60B9: 20 53           JR      NZ,$610E            ; {}
60BB: 77              LD      (HL),A              
60BC: 61              LD      H,C                 
60BD: 6D              LD      L,L                 
60BE: 70              LD      (HL),B              
60BF: 2E 2E           LD      L,$2E               
60C1: 2E 54           LD      L,$54               
60C3: 68              LD      L,B                 
60C4: 6F              LD      L,A                 
60C5: 73              LD      (HL),E              
60C6: 65              LD      H,L                 
60C7: 20 66           JR      NZ,$612F            ; {}
60C9: 6C              LD      L,H                 
60CA: 6F              LD      L,A                 
60CB: 77              LD      (HL),A              
60CC: 65              LD      H,L                 
60CD: 72              LD      (HL),D              
60CE: 73              LD      (HL),E              
60CF: 20 20           JR      NZ,$60F1            ; {}
60D1: 20 61           JR      NZ,$6134            ; {}
60D3: 72              LD      (HL),D              
60D4: 65              LD      H,L                 
60D5: 20 42           JR      NZ,$6119            ; {}
60D7: 6F              LD      L,A                 
60D8: 77              LD      (HL),A              
60D9: 57              LD      D,A                 
60DA: 6F              LD      L,A                 
60DB: 77              LD      (HL),A              
60DC: 5E              LD      E,(HL)              
60DD: 73              LD      (HL),E              
60DE: 20 20           JR      NZ,$6100            ; {}
60E0: 20 20           JR      NZ,$6102            ; {}
60E2: 66              LD      H,(HL)              
60E3: 61              LD      H,C                 
60E4: 76              HALT                        
60E5: 6F              LD      L,A                 
60E6: 72              LD      (HL),D              
60E7: 69              LD      L,C                 
60E8: 74              LD      (HL),H              
60E9: 65              LD      H,L                 
60EA: 2E 20           LD      L,$20               
60EC: 20 57           JR      NZ,$6145            ; {}
60EE: 68              LD      L,B                 
60EF: 79              LD      A,C                 
60F0: 20 20           JR      NZ,$6112            ; {}
60F2: 64              LD      H,H                 
60F3: 6F              LD      L,A                 
60F4: 6E              LD      L,(HL)              
60F5: 5E              LD      E,(HL)              
60F6: 74              LD      (HL),H              
60F7: 20 79           JR      NZ,$6172            ; {}
60F9: 6F              LD      L,A                 
60FA: 75              LD      (HL),L              
60FB: 20 74           JR      NZ,$6171            ; {}
60FD: 61              LD      H,C                 
60FE: 6B              LD      L,E                 
60FF: 65              LD      H,L                 
6100: 20 20           JR      NZ,$6122            ; {}
6102: 68              LD      L,B                 
6103: 69              LD      L,C                 
6104: 6D              LD      L,L                 
6105: 20 66           JR      NZ,$616D            ; {}
6107: 6F              LD      L,A                 
6108: 72              LD      (HL),D              
6109: 20 61           JR      NZ,$616C            ; {}
610B: 20 77           JR      NZ,$6184            ; {}
610D: 61              LD      H,C                 
610E: 6C              LD      L,H                 
610F: 6B              LD      L,E                 
6110: 20 20           JR      NZ,$6132            ; {}
6112: 74              LD      (HL),H              
6113: 68              LD      L,B                 
6114: 65              LD      H,L                 
6115: 72              LD      (HL),D              
6116: 65              LD      H,L                 
6117: 3F              CCF                         
6118: 20 20           JR      NZ,$613A            ; {}
611A: 43              LD      B,E                 
611B: 4C              LD      C,H                 
611C: 49              LD      C,C                 
611D: 43              LD      B,E                 
611E: 4B              LD      C,E                 
611F: 21 5E FF        LD      HL,$FF5E            
6122: 5E              LD      E,(HL)              
6123: 42              LD      B,D                 
6124: 52              LD      D,D                 
6125: 52              LD      D,D                 
6126: 49              LD      C,C                 
6127: 4E              LD      C,(HL)              
6128: 47              LD      B,A                 
6129: 21 20 42        LD      HL,$4220            
612C: 52              LD      D,D                 
612D: 52              LD      D,D                 
612E: 49              LD      C,C                 
612F: 4E              LD      C,(HL)              
6130: 47              LD      B,A                 
6131: 21 48 69        LD      HL,$6948            
6134: 2C              INC     L                   
6135: 20 69           JR      NZ,$61A0            ; {}
6137: 74              LD      (HL),H              
6138: 5E              LD      E,(HL)              
6139: 73              LD      (HL),E              
613A: 20 55           JR      NZ,$6191            ; {}
613C: 6C              LD      L,H                 
613D: 72              LD      (HL),D              
613E: 69              LD      L,C                 
613F: 72              LD      (HL),D              
6140: 61              LD      H,C                 
6141: 21 2E 2E        LD      HL,$2E2E            
6144: 2E 48           LD      L,$48               
6146: 61              LD      H,C                 
6147: 76              HALT                        
6148: 65              LD      H,L                 
6149: 20 79           JR      NZ,$61C4            ; {}
614B: 6F              LD      L,A                 
614C: 75              LD      (HL),L              
614D: 20 6D           JR      NZ,$61BC            ; {}
614F: 65              LD      H,L                 
6150: 74              LD      (HL),H              
6151: 20 65           JR      NZ,$61B8            ; {}
6153: 76              HALT                        
6154: 65              LD      H,L                 
6155: 72              LD      (HL),D              
6156: 79              LD      A,C                 
6157: 6F              LD      L,A                 
6158: 6E              LD      L,(HL)              
6159: 65              LD      H,L                 
615A: 20 6F           JR      NZ,$61CB            ; {}
615C: 6E              LD      L,(HL)              
615D: 20 74           JR      NZ,$61D3            ; {}
615F: 68              LD      L,B                 
6160: 65              LD      H,L                 
6161: 20 69           JR      NZ,$61CC            ; {}
6163: 73              LD      (HL),E              
6164: 6C              LD      L,H                 
6165: 61              LD      H,C                 
6166: 6E              LD      L,(HL)              
6167: 64              LD      H,H                 
6168: 3F              CCF                         
6169: 20 20           JR      NZ,$618B            ; {}
616B: 54              LD      D,H                 
616C: 68              LD      L,B                 
616D: 65              LD      H,L                 
616E: 72              LD      (HL),D              
616F: 65              LD      H,L                 
6170: 5E              LD      E,(HL)              
6171: 73              LD      (HL),E              
6172: 61              LD      H,C                 
6173: 20 6D           JR      NZ,$61E2            ; {}
6175: 61              LD      H,C                 
6176: 6E              LD      L,(HL)              
6177: 20 6E           JR      NZ,$61E7            ; {}
6179: 61              LD      H,C                 
617A: 6D              LD      L,L                 
617B: 65              LD      H,L                 
617C: 64              LD      H,H                 
617D: 20 20           JR      NZ,$619F            ; {}
617F: 20 20           JR      NZ,$61A1            ; {}
6181: 20 52           JR      NZ,$61D5            ; {}
6183: 69              LD      L,C                 
6184: 63              LD      H,E                 
6185: 68              LD      L,B                 
6186: 61              LD      H,C                 
6187: 72              LD      (HL),D              
6188: 64              LD      H,H                 
6189: 20 77           JR      NZ,$6202            ; {}
618B: 68              LD      L,B                 
618C: 6F              LD      L,A                 
618D: 20 20           JR      NZ,$61AF            ; {}
618F: 20 20           JR      NZ,$61B1            ; {}
6191: 20 6C           JR      NZ,$61FF            ; {}
6193: 69              LD      L,C                 
6194: 76              HALT                        
6195: 65              LD      H,L                 
6196: 73              LD      (HL),E              
6197: 20 69           JR      NZ,$6202            ; {}
6199: 6E              LD      L,(HL)              
619A: 20 50           JR      NZ,$61EC            ; {}
619C: 6F              LD      L,A                 
619D: 74              LD      (HL),H              
619E: 68              LD      L,B                 
619F: 6F              LD      L,A                 
61A0: 6C              LD      L,H                 
61A1: 65              LD      H,L                 
61A2: 46              LD      B,(HL)              
61A3: 69              LD      L,C                 
61A4: 65              LD      H,L                 
61A5: 6C              LD      L,H                 
61A6: 64              LD      H,H                 
61A7: 2C              INC     L                   
61A8: 20 73           JR      NZ,$621D            ; {}
61AA: 6F              LD      L,A                 
61AB: 75              LD      (HL),L              
61AC: 74              LD      (HL),H              
61AD: 68              LD      L,B                 
61AE: 65              LD      H,L                 
61AF: 61              LD      H,C                 
61B0: 73              LD      (HL),E              
61B1: 74              LD      (HL),H              
61B2: 6F              LD      L,A                 
61B3: 66              LD      H,(HL)              
61B4: 20 74           JR      NZ,$622A            ; {}
61B6: 68              LD      L,B                 
61B7: 65              LD      H,L                 
61B8: 20 76           JR      NZ,$6230            ; {}
61BA: 69              LD      L,C                 
61BB: 6C              LD      L,H                 
61BC: 6C              LD      L,H                 
61BD: 61              LD      H,C                 
61BE: 67              LD      H,A                 
61BF: 65              LD      H,L                 
61C0: 2E 20           LD      L,$20               
61C2: 57              LD      D,A                 
61C3: 68              LD      L,B                 
61C4: 79              LD      A,C                 
61C5: 20 6E           JR      NZ,$6235            ; {}
61C7: 6F              LD      L,A                 
61C8: 74              LD      (HL),H              
61C9: 20 70           JR      NZ,$623B            ; {}
61CB: 61              LD      H,C                 
61CC: 79              LD      A,C                 
61CD: 20 68           JR      NZ,$6237            ; {}
61CF: 69              LD      L,C                 
61D0: 6D              LD      L,L                 
61D1: 20 61           JR      NZ,$6234            ; {}
61D3: 20 76           JR      NZ,$624B            ; {}
61D5: 69              LD      L,C                 
61D6: 73              LD      (HL),E              
61D7: 69              LD      L,C                 
61D8: 74              LD      (HL),H              
61D9: 3F              CCF                         
61DA: 20 20           JR      NZ,$61FC            ; {}
61DC: 54              LD      D,H                 
61DD: 68              LD      L,B                 
61DE: 61              LD      H,C                 
61DF: 74              LD      (HL),H              
61E0: 5E              LD      E,(HL)              
61E1: 73              LD      (HL),E              
61E2: 61              LD      H,C                 
61E3: 6C              LD      L,H                 
61E4: 6C              LD      L,H                 
61E5: 20 49           JR      NZ,$6230            ; {}
61E7: 20 63           JR      NZ,$624C            ; {}
61E9: 61              LD      H,C                 
61EA: 6E              LD      L,(HL)              
61EB: 20 74           JR      NZ,$6261            ; {}
61ED: 65              LD      H,L                 
61EE: 6C              LD      L,H                 
61EF: 6C              LD      L,H                 
61F0: 20 20           JR      NZ,$6212            ; {}
61F2: 79              LD      A,C                 
61F3: 6F              LD      L,A                 
61F4: 75              LD      (HL),L              
61F5: 20 66           JR      NZ,$625D            ; {}
61F7: 6F              LD      L,A                 
61F8: 72              LD      (HL),D              
61F9: 20 6E           JR      NZ,$6269            ; {}
61FB: 6F              LD      L,A                 
61FC: 77              LD      (HL),A              
61FD: 21 20 20        LD      HL,$2020            
6200: 20 20           JR      NZ,$6222            ; {}
6202: 42              LD      B,D                 
6203: 79              LD      A,C                 
6204: 65              LD      H,L                 
6205: 21 20 20        LD      HL,$2020            
6208: 43              LD      B,E                 
6209: 4C              LD      C,H                 
620A: 49              LD      C,C                 
620B: 43              LD      B,E                 
620C: 4B              LD      C,E                 
620D: 21 5E FF        LD      HL,$FF5E            
6210: 5E              LD      E,(HL)              
6211: 42              LD      B,D                 
6212: 52              LD      D,D                 
6213: 52              LD      D,D                 
6214: 49              LD      C,C                 
6215: 4E              LD      C,(HL)              
6216: 47              LD      B,A                 
6217: 21 20 42        LD      HL,$4220            
621A: 52              LD      D,D                 
621B: 52              LD      D,D                 
621C: 49              LD      C,C                 
621D: 4E              LD      C,(HL)              
621E: 47              LD      B,A                 
621F: 21 4F 6C        LD      HL,$6C4F            
6222: 64              LD      H,H                 
6223: 20 6D           JR      NZ,$6292            ; {}
6225: 61              LD      H,C                 
6226: 6E              LD      L,(HL)              
6227: 20 55           JR      NZ,$627E            ; {}
6229: 6C              LD      L,H                 
622A: 72              LD      (HL),D              
622B: 69              LD      L,C                 
622C: 72              LD      (HL),D              
622D: 61              LD      H,C                 
622E: 20 20           JR      NZ,$6250            ; {}
6230: 68              LD      L,B                 
6231: 65              LD      H,L                 
6232: 72              LD      (HL),D              
6233: 65              LD      H,L                 
6234: 21 20 2E        LD      HL,$2E20            
6237: 2E 2E           LD      L,$2E               
6239: 44              LD      B,H                 
623A: 6F              LD      L,A                 
623B: 20 79           JR      NZ,$62B6            ; {}
623D: 6F              LD      L,A                 
623E: 75              LD      (HL),L              
623F: 20 6C           JR      NZ,$62AD            ; {}
6241: 69              LD      L,C                 
6242: 6B              LD      L,E                 
6243: 65              LD      H,L                 
6244: 20 62           JR      NZ,$62A8            ; {}
6246: 61              LD      H,C                 
6247: 6E              LD      L,(HL)              
6248: 61              LD      H,C                 
6249: 6E              LD      L,(HL)              
624A: 61              LD      H,C                 
624B: 73              LD      (HL),E              
624C: 3F              CCF                         
624D: 20 20           JR      NZ,$626F            ; {}
624F: 20 54           JR      NZ,$62A5            ; {}
6251: 72              LD      (HL),D              
6252: 79              LD      A,C                 
6253: 20 74           JR      NZ,$62C9            ; {}
6255: 61              LD      H,C                 
6256: 6C              LD      L,H                 
6257: 6B              LD      L,E                 
6258: 69              LD      L,C                 
6259: 6E              LD      L,(HL)              
625A: 67              LD      H,A                 
625B: 20 74           JR      NZ,$62D1            ; {}
625D: 6F              LD      L,A                 
625E: 20 20           JR      NZ,$6280            ; {}
6260: 70              LD      (HL),B              
6261: 65              LD      H,L                 
6262: 6F              LD      L,A                 
6263: 70              LD      (HL),B              
6264: 6C              LD      L,H                 
6265: 65              LD      H,L                 
6266: 20 69           JR      NZ,$62D1            ; {}
6268: 6E              LD      L,(HL)              
6269: 20 74           JR      NZ,$62DF            ; {}
626B: 68              LD      L,B                 
626C: 65              LD      H,L                 
626D: 20 20           JR      NZ,$628F            ; {}
626F: 20 76           JR      NZ,$62E7            ; {}
6271: 69              LD      L,C                 
6272: 6C              LD      L,H                 
6273: 6C              LD      L,H                 
6274: 61              LD      H,C                 
6275: 67              LD      H,A                 
6276: 65              LD      H,L                 
6277: 20 61           JR      NZ,$62DA            ; {}
6279: 67              LD      H,A                 
627A: 61              LD      H,C                 
627B: 69              LD      L,C                 
627C: 6E              LD      L,(HL)              
627D: 21 20 20        LD      HL,$2020            
6280: 42              LD      B,D                 
6281: 79              LD      A,C                 
6282: 65              LD      H,L                 
6283: 21 20 20        LD      HL,$2020            
6286: 43              LD      B,E                 
6287: 4C              LD      C,H                 
6288: 49              LD      C,C                 
6289: 43              LD      B,E                 
628A: 4B              LD      C,E                 
628B: 21 5E FF        LD      HL,$FF5E            
628E: 5E              LD      E,(HL)              
628F: 42              LD      B,D                 
6290: 52              LD      D,D                 
6291: 52              LD      D,D                 
6292: 49              LD      C,C                 
6293: 4E              LD      C,(HL)              
6294: 47              LD      B,A                 
6295: 21 20 42        LD      HL,$4220            
6298: 52              LD      D,D                 
6299: 52              LD      D,D                 
629A: 49              LD      C,C                 
629B: 4E              LD      C,(HL)              
629C: 47              LD      B,A                 
629D: 21 55 6C        LD      HL,$6C55            
62A0: 72              LD      (HL),D              
62A1: 69              LD      L,C                 
62A2: 72              LD      (HL),D              
62A3: 61              LD      H,C                 
62A4: 20 73           JR      NZ,$6319            ; {}
62A6: 70              LD      (HL),B              
62A7: 65              LD      H,L                 
62A8: 61              LD      H,C                 
62A9: 6B              LD      L,E                 
62AA: 69              LD      L,C                 
62AB: 6E              LD      L,(HL)              
62AC: 67              LD      H,A                 
62AD: 21 59 6F        LD      HL,$6F59            
62B0: 75              LD      (HL),L              
62B1: 20 6B           JR      NZ,$631E            ; {}
62B3: 6E              LD      L,(HL)              
62B4: 6F              LD      L,A                 
62B5: 77              LD      (HL),A              
62B6: 2C              INC     L                   
62B7: 20 74           JR      NZ,$632D            ; {}
62B9: 68              LD      L,B                 
62BA: 65              LD      H,L                 
62BB: 72              LD      (HL),D              
62BC: 65              LD      H,L                 
62BD: 20 69           JR      NZ,$6328            ; {}
62BF: 73              LD      (HL),E              
62C0: 20 61           JR      NZ,$6323            ; {}
62C2: 20 6C           JR      NZ,$6330            ; {}
62C4: 69              LD      L,C                 
62C5: 62              LD      H,D                 
62C6: 72              LD      (HL),D              
62C7: 61              LD      H,C                 
62C8: 72              LD      (HL),D              
62C9: 79              LD      A,C                 
62CA: 20 69           JR      NZ,$6335            ; {}
62CC: 6E              LD      L,(HL)              
62CD: 20 74           JR      NZ,$6343            ; {}
62CF: 68              LD      L,B                 
62D0: 65              LD      H,L                 
62D1: 20 76           JR      NZ,$6349            ; {}
62D3: 69              LD      L,C                 
62D4: 6C              LD      L,H                 
62D5: 6C              LD      L,H                 
62D6: 61              LD      H,C                 
62D7: 67              LD      H,A                 
62D8: 65              LD      H,L                 
62D9: 20 74           JR      NZ,$634F            ; {}
62DB: 68              LD      L,B                 
62DC: 61              LD      H,C                 
62DD: 74              LD      (HL),H              
62DE: 6D              LD      L,L                 
62DF: 69              LD      L,C                 
62E0: 67              LD      H,A                 
62E1: 68              LD      L,B                 
62E2: 74              LD      (HL),H              
62E3: 20 68           JR      NZ,$634D            ; {}
62E5: 61              LD      H,C                 
62E6: 76              HALT                        
62E7: 65              LD      H,L                 
62E8: 20 73           JR      NZ,$635D            ; {}
62EA: 6F              LD      L,A                 
62EB: 6D              LD      L,L                 
62EC: 65              LD      H,L                 
62ED: 20 67           JR      NZ,$6356            ; {}
62EF: 6F              LD      L,A                 
62F0: 6F              LD      L,A                 
62F1: 64              LD      H,H                 
62F2: 20 69           JR      NZ,$635D            ; {}
62F4: 6E              LD      L,(HL)              
62F5: 66              LD      H,(HL)              
62F6: 6F              LD      L,A                 
62F7: 72              LD      (HL),D              
62F8: 6D              LD      L,L                 
62F9: 61              LD      H,C                 
62FA: 74              LD      (HL),H              
62FB: 69              LD      L,C                 
62FC: 6F              LD      L,A                 
62FD: 6E              LD      L,(HL)              
62FE: 66              LD      H,(HL)              
62FF: 6F              LD      L,A                 
6300: 72              LD      (HL),D              
6301: 20 79           JR      NZ,$637C            ; {}
6303: 6F              LD      L,A                 
6304: 75              LD      (HL),L              
6305: 21 20 20        LD      HL,$2020            
6308: 54              LD      D,H                 
6309: 61              LD      H,C                 
630A: 6C              LD      L,H                 
630B: 6B              LD      L,E                 
630C: 20 20           JR      NZ,$632E            ; {}
630E: 74              LD      (HL),H              
630F: 6F              LD      L,A                 
6310: 20 79           JR      NZ,$638B            ; {}
6312: 6F              LD      L,A                 
6313: 75              LD      (HL),L              
6314: 20 6C           JR      NZ,$6382            ; {}
6316: 61              LD      H,C                 
6317: 74              LD      (HL),H              
6318: 65              LD      H,L                 
6319: 72              LD      (HL),D              
631A: 21 20 20        LD      HL,$2020            
631D: 20 43           JR      NZ,$6362            ; {}
631F: 4C              LD      C,H                 
6320: 49              LD      C,C                 
6321: 43              LD      B,E                 
6322: 4B              LD      C,E                 
6323: 21 5E FF        LD      HL,$FF5E            
6326: 5E              LD      E,(HL)              
6327: 42              LD      B,D                 
6328: 52              LD      D,D                 
6329: 52              LD      D,D                 
632A: 49              LD      C,C                 
632B: 4E              LD      C,(HL)              
632C: 47              LD      B,A                 
632D: 21 20 42        LD      HL,$4220            
6330: 52              LD      D,D                 
6331: 52              LD      D,D                 
6332: 49              LD      C,C                 
6333: 4E              LD      C,(HL)              
6334: 47              LD      B,A                 
6335: 21 59 65        LD      HL,$6559            
6338: 61              LD      H,C                 
6339: 68              LD      L,B                 
633A: 2C              INC     L                   
633B: 20 69           JR      NZ,$63A6            ; {}
633D: 74              LD      (HL),H              
633E: 5E              LD      E,(HL)              
633F: 73              LD      (HL),E              
6340: 20 6D           JR      NZ,$63AF            ; {}
6342: 65              LD      H,L                 
6343: 2C              INC     L                   
6344: 20 20           JR      NZ,$6366            ; {}
6346: 55              LD      D,L                 
6347: 6C              LD      L,H                 
6348: 72              LD      (HL),D              
6349: 69              LD      L,C                 
634A: 72              LD      (HL),D              
634B: 61              LD      H,C                 
634C: 21 20 20        LD      HL,$2020            
634F: 48              LD      C,B                 
6350: 6D              LD      L,L                 
6351: 6D              LD      L,L                 
6352: 6D              LD      L,L                 
6353: 2E 2E           LD      L,$2E               
6355: 2E 59           LD      L,$59               
6357: 6F              LD      L,A                 
6358: 75              LD      (HL),L              
6359: 20 63           JR      NZ,$63BE            ; {}
635B: 61              LD      H,C                 
635C: 6E              LD      L,(HL)              
635D: 5E              LD      E,(HL)              
635E: 74              LD      (HL),H              
635F: 20 66           JR      NZ,$63C7            ; {}
6361: 69              LD      L,C                 
6362: 6E              LD      L,(HL)              
6363: 64              LD      H,H                 
6364: 20 20           JR      NZ,$6386            ; {}
6366: 61              LD      H,C                 
6367: 6C              LD      L,H                 
6368: 6C              LD      L,H                 
6369: 20 74           JR      NZ,$63DF            ; {}
636B: 68              LD      L,B                 
636C: 65              LD      H,L                 
636D: 20 6C           JR      NZ,$63DB            ; {}
636F: 65              LD      H,L                 
6370: 61              LD      H,C                 
6371: 76              HALT                        
6372: 65              LD      H,L                 
6373: 73              LD      (HL),E              
6374: 20 20           JR      NZ,$6396            ; {}
6376: 79              LD      A,C                 
6377: 6F              LD      L,A                 
6378: 75              LD      (HL),L              
6379: 20 73           JR      NZ,$63EE            ; {}
637B: 61              LD      H,C                 
637C: 79              LD      A,C                 
637D: 3F              CCF                         
637E: 20 20           JR      NZ,$63A0            ; {}
6380: 54              LD      D,H                 
6381: 68              LD      L,B                 
6382: 61              LD      H,C                 
6383: 74              LD      (HL),H              
6384: 5E              LD      E,(HL)              
6385: 73              LD      (HL),E              
6386: 61              LD      H,C                 
6387: 20 73           JR      NZ,$63FC            ; {}
6389: 74              LD      (HL),H              
638A: 75              LD      (HL),L              
638B: 6D              LD      L,L                 
638C: 70              LD      (HL),B              
638D: 65              LD      H,L                 
638E: 72              LD      (HL),D              
638F: 21 20 20        LD      HL,$2020            
6392: 41              LD      B,C                 
6393: 68              LD      L,B                 
6394: 68              LD      L,B                 
6395: 2C              INC     L                   
6396: 63              LD      H,E                 
6397: 68              LD      L,B                 
6398: 65              LD      H,L                 
6399: 63              LD      H,E                 
639A: 6B              LD      L,E                 
639B: 20 6F           JR      NZ,$640C            ; {}
639D: 75              LD      (HL),L              
639E: 74              LD      (HL),H              
639F: 20 74           JR      NZ,$6415            ; {}
63A1: 68              LD      L,B                 
63A2: 65              LD      H,L                 
63A3: 20 20           JR      NZ,$63C5            ; {}
63A5: 20 72           JR      NZ,$6419            ; {}
63A7: 61              LD      H,C                 
63A8: 76              HALT                        
63A9: 65              LD      H,L                 
63AA: 6E              LD      L,(HL)              
63AB: 20 62           JR      NZ,$640F            ; {}
63AD: 79              LD      A,C                 
63AE: 20 74           JR      NZ,$6424            ; {}
63B0: 68              LD      L,B                 
63B1: 65              LD      H,L                 
63B2: 20 20           JR      NZ,$63D4            ; {}
63B4: 20 20           JR      NZ,$63D6            ; {}
63B6: 63              LD      H,E                 
63B7: 61              LD      H,C                 
63B8: 73              LD      (HL),E              
63B9: 74              LD      (HL),H              
63BA: 6C              LD      L,H                 
63BB: 65              LD      H,L                 
63BC: 21 20 20        LD      HL,$2020            
63BF: 49              LD      C,C                 
63C0: 6E              LD      L,(HL)              
63C1: 20 61           JR      NZ,$6424            ; {}
63C3: 6E              LD      L,(HL)              
63C4: 79              LD      A,C                 
63C5: 20 63           JR      NZ,$642A            ; {}
63C7: 61              LD      H,C                 
63C8: 73              LD      (HL),E              
63C9: 65              LD      H,L                 
63CA: 2C              INC     L                   
63CB: 20 74           JR      NZ,$6441            ; {}
63CD: 72              LD      (HL),D              
63CE: 79              LD      A,C                 
63CF: 20 6D           JR      NZ,$643E            ; {}
63D1: 61              LD      H,C                 
63D2: 6E              LD      L,(HL)              
63D3: 79              LD      A,C                 
63D4: 20 20           JR      NZ,$63F6            ; {}
63D6: 74              LD      (HL),H              
63D7: 68              LD      L,B                 
63D8: 69              LD      L,C                 
63D9: 6E              LD      L,(HL)              
63DA: 67              LD      H,A                 
63DB: 73              LD      (HL),E              
63DC: 21 20 20        LD      HL,$2020            
63DF: 43              LD      B,E                 
63E0: 4C              LD      C,H                 
63E1: 49              LD      C,C                 
63E2: 43              LD      B,E                 
63E3: 4B              LD      C,E                 
63E4: 21 5E FF        LD      HL,$FF5E            
63E7: 5E              LD      E,(HL)              
63E8: 42              LD      B,D                 
63E9: 52              LD      D,D                 
63EA: 52              LD      D,D                 
63EB: 49              LD      C,C                 
63EC: 4E              LD      C,(HL)              
63ED: 47              LD      B,A                 
63EE: 21 20 42        LD      HL,$4220            
63F1: 52              LD      D,D                 
63F2: 52              LD      D,D                 
63F3: 49              LD      C,C                 
63F4: 4E              LD      C,(HL)              
63F5: 47              LD      B,A                 
63F6: 21 55 6C        LD      HL,$6C55            
63F9: 72              LD      (HL),D              
63FA: 69              LD      L,C                 
63FB: 72              LD      (HL),D              
63FC: 61              LD      H,C                 
63FD: 20 68           JR      NZ,$6467            ; {}
63FF: 65              LD      H,L                 
6400: 72              LD      (HL),D              
6401: 65              LD      H,L                 
6402: 21 20 2E        LD      HL,$2E20            
6405: 2E 2E           LD      L,$2E               
6407: 53              LD      D,E                 
6408: 68              LD      L,B                 
6409: 6F              LD      L,A                 
640A: 76              HALT                        
640B: 65              LD      H,L                 
640C: 6C              LD      L,H                 
640D: 2E 2E           LD      L,$2E               
640F: 2E 20           LD      L,$20               
6411: 20 44           JR      NZ,$6457            ; {}
6413: 69              LD      L,C                 
6414: 64              LD      H,H                 
6415: 20 20           JR      NZ,$6437            ; {}
6417: 79              LD      A,C                 
6418: 6F              LD      L,A                 
6419: 75              LD      (HL),L              
641A: 20 70           JR      NZ,$648C            ; {}
641C: 75              LD      (HL),L              
641D: 72              LD      (HL),D              
641E: 63              LD      H,E                 
641F: 68              LD      L,B                 
6420: 61              LD      H,C                 
6421: 73              LD      (HL),E              
6422: 65              LD      H,L                 
6423: 20 61           JR      NZ,$6486            ; {}
6425: 20 20           JR      NZ,$6447            ; {}
6427: 73              LD      (HL),E              
6428: 68              LD      L,B                 
6429: 6F              LD      L,A                 
642A: 76              HALT                        
642B: 65              LD      H,L                 
642C: 6C              LD      L,H                 
642D: 3F              CCF                         
642E: 20 20           JR      NZ,$6450            ; {}
6430: 59              LD      E,C                 
6431: 6F              LD      L,A                 
6432: 75              LD      (HL),L              
6433: 20 6D           JR      NZ,$64A2            ; {}
6435: 61              LD      H,C                 
6436: 79              LD      A,C                 
6437: 66              LD      H,(HL)              
6438: 69              LD      L,C                 
6439: 6E              LD      L,(HL)              
643A: 64              LD      H,H                 
643B: 20 73           JR      NZ,$64B0            ; {}
643D: 6F              LD      L,A                 
643E: 6D              LD      L,L                 
643F: 65              LD      H,L                 
6440: 74              LD      (HL),H              
6441: 68              LD      L,B                 
6442: 69              LD      L,C                 
6443: 6E              LD      L,(HL)              
6444: 67              LD      H,A                 
6445: 20 20           JR      NZ,$6467            ; {}
6447: 69              LD      L,C                 
6448: 66              LD      H,(HL)              
6449: 20 79           JR      NZ,$64C4            ; {}
644B: 6F              LD      L,A                 
644C: 75              LD      (HL),L              
644D: 20 64           JR      NZ,$64B3            ; {}
644F: 69              LD      L,C                 
6450: 67              LD      H,A                 
6451: 20 68           JR      NZ,$64BB            ; {}
6453: 65              LD      H,L                 
6454: 72              LD      (HL),D              
6455: 65              LD      H,L                 
6456: 20 61           JR      NZ,$64B9            ; {}
6458: 6E              LD      L,(HL)              
6459: 64              LD      H,H                 
645A: 20 74           JR      NZ,$64D0            ; {}
645C: 68              LD      L,B                 
645D: 65              LD      H,L                 
645E: 72              LD      (HL),D              
645F: 65              LD      H,L                 
6460: 21 20 20        LD      HL,$2020            
6463: 42              LD      B,D                 
6464: 79              LD      A,C                 
6465: 65              LD      H,L                 
6466: 21 43 4C        LD      HL,$4C43            
6469: 49              LD      C,C                 
646A: 43              LD      B,E                 
646B: 4B              LD      C,E                 
646C: 21 5E FF        LD      HL,$FF5E            
646F: 5E              LD      E,(HL)              
6470: 42              LD      B,D                 
6471: 52              LD      D,D                 
6472: 52              LD      D,D                 
6473: 49              LD      C,C                 
6474: 4E              LD      C,(HL)              
6475: 47              LD      B,A                 
6476: 21 20 42        LD      HL,$4220            
6479: 52              LD      D,D                 
647A: 52              LD      D,D                 
647B: 49              LD      C,C                 
647C: 4E              LD      C,(HL)              
647D: 47              LD      B,A                 
647E: 21 59 61        LD      HL,$6159            
6481: 2C              INC     L                   
6482: 20 69           JR      NZ,$64ED            ; {}
6484: 74              LD      (HL),H              
6485: 5E              LD      E,(HL)              
6486: 73              LD      (HL),E              
6487: 20 55           JR      NZ,$64DE            ; {}
6489: 6C              LD      L,H                 
648A: 72              LD      (HL),D              
648B: 69              LD      L,C                 
648C: 72              LD      (HL),D              
648D: 61              LD      H,C                 
648E: 21 54 68        LD      HL,$6854            
6491: 65              LD      H,L                 
6492: 20 63           JR      NZ,$64F7            ; {}
6494: 61              LD      H,C                 
6495: 76              HALT                        
6496: 65              LD      H,L                 
6497: 20 69           JR      NZ,$6502            ; {}
6499: 6E              LD      L,(HL)              
649A: 20 74           JR      NZ,$6510            ; {}
649C: 68              LD      L,B                 
649D: 65              LD      H,L                 
649E: 20 55           JR      NZ,$64F5            ; {}
64A0: 6B              LD      L,E                 
64A1: 75              LD      (HL),L              
64A2: 6B              LD      L,E                 
64A3: 75              LD      (HL),L              
64A4: 20 50           JR      NZ,$64F6            ; {}
64A6: 72              LD      (HL),D              
64A7: 61              LD      H,C                 
64A8: 69              LD      L,C                 
64A9: 72              LD      (HL),D              
64AA: 69              LD      L,C                 
64AB: 65              LD      H,L                 
64AC: 20 69           JR      NZ,$6517            ; {}
64AE: 73              LD      (HL),E              
64AF: 74              LD      (HL),H              
64B0: 68              LD      L,B                 
64B1: 65              LD      H,L                 
64B2: 20 6B           JR      NZ,$651F            ; {}
64B4: 65              LD      H,L                 
64B5: 79              LD      A,C                 
64B6: 21 20 20        LD      HL,$2020            
64B9: 59              LD      E,C                 
64BA: 65              LD      H,L                 
64BB: 73              LD      (HL),E              
64BC: 2C              INC     L                   
64BD: 20 49           JR      NZ,$6508            ; {}
64BF: 6D              LD      L,L                 
64C0: 65              LD      H,L                 
64C1: 61              LD      H,C                 
64C2: 6E              LD      L,(HL)              
64C3: 20 74           JR      NZ,$6539            ; {}
64C5: 68              LD      L,B                 
64C6: 65              LD      H,L                 
64C7: 20 6B           JR      NZ,$6534            ; {}
64C9: 65              LD      H,L                 
64CA: 79              LD      A,C                 
64CB: 20 20           JR      NZ,$64ED            ; {}
64CD: 20 20           JR      NZ,$64EF            ; {}
64CF: 63              LD      H,E                 
64D0: 61              LD      H,C                 
64D1: 76              HALT                        
64D2: 65              LD      H,L                 
64D3: 2C              INC     L                   
64D4: 20 6E           JR      NZ,$6544            ; {}
64D6: 6F              LD      L,A                 
64D7: 20 70           JR      NZ,$6549            ; {}
64D9: 75              LD      (HL),L              
64DA: 6E              LD      L,(HL)              
64DB: 20 20           JR      NZ,$64FD            ; {}
64DD: 20 20           JR      NZ,$64FF            ; {}
64DF: 69              LD      L,C                 
64E0: 6E              LD      L,(HL)              
64E1: 74              LD      (HL),H              
64E2: 65              LD      H,L                 
64E3: 6E              LD      L,(HL)              
64E4: 64              LD      H,H                 
64E5: 65              LD      H,L                 
64E6: 64              LD      H,H                 
64E7: 21 20 20        LD      HL,$2020            
64EA: 42              LD      B,D                 
64EB: 79              LD      A,C                 
64EC: 65              LD      H,L                 
64ED: 21 20 43        LD      HL,$4320            
64F0: 4C              LD      C,H                 
64F1: 49              LD      C,C                 
64F2: 43              LD      B,E                 
64F3: 4B              LD      C,E                 
64F4: 21 5E FF        LD      HL,$FF5E            
64F7: 5E              LD      E,(HL)              
64F8: 42              LD      B,D                 
64F9: 52              LD      D,D                 
64FA: 52              LD      D,D                 
64FB: 49              LD      C,C                 
64FC: 4E              LD      C,(HL)              
64FD: 47              LD      B,A                 
64FE: 21 20 42        LD      HL,$4220            
6501: 52              LD      D,D                 
6502: 52              LD      D,D                 
6503: 49              LD      C,C                 
6504: 4E              LD      C,(HL)              
6505: 47              LD      B,A                 
6506: 21 48 69        LD      HL,$6948            
6509: 2C              INC     L                   
650A: 20 74           JR      NZ,$6580            ; {}
650C: 68              LD      L,B                 
650D: 69              LD      L,C                 
650E: 73              LD      (HL),E              
650F: 20 69           JR      NZ,$657A            ; {}
6511: 73              LD      (HL),E              
6512: 20 20           JR      NZ,$6534            ; {}
6514: 20 20           JR      NZ,$6536            ; {}
6516: 20 55           JR      NZ,$656D            ; {}
6518: 6C              LD      L,H                 
6519: 72              LD      (HL),D              
651A: 69              LD      L,C                 
651B: 72              LD      (HL),D              
651C: 61              LD      H,C                 
651D: 21 20 20        LD      HL,$2020            
6520: 49              LD      C,C                 
6521: 6E              LD      L,(HL)              
6522: 20 74           JR      NZ,$6598            ; {}
6524: 68              LD      L,B                 
6525: 65              LD      H,L                 
6526: 20 59           JR      NZ,$6581            ; {}
6528: 61              LD      H,C                 
6529: 72              LD      (HL),D              
652A: 6E              LD      L,(HL)              
652B: 61              LD      H,C                 
652C: 20 44           JR      NZ,$6572            ; {}
652E: 65              LD      H,L                 
652F: 73              LD      (HL),E              
6530: 65              LD      H,L                 
6531: 72              LD      (HL),D              
6532: 74              LD      (HL),H              
6533: 2C              INC     L                   
6534: 20 20           JR      NZ,$6556            ; {}
6536: 20 77           JR      NZ,$65AF            ; {}
6538: 68              LD      L,B                 
6539: 69              LD      L,C                 
653A: 63              LD      H,E                 
653B: 68              LD      L,B                 
653C: 20 69           JR      NZ,$65A7            ; {}
653E: 73              LD      (HL),E              
653F: 20 6C           JR      NZ,$65AD            ; {}
6541: 6F              LD      L,A                 
6542: 63              LD      H,E                 
6543: 61              LD      H,C                 
6544: 74              LD      (HL),H              
6545: 65              LD      H,L                 
6546: 64              LD      H,H                 
6547: 69              LD      L,C                 
6548: 6E              LD      L,(HL)              
6549: 20 74           JR      NZ,$65BF            ; {}
654B: 68              LD      L,B                 
654C: 65              LD      H,L                 
654D: 20 73           JR      NZ,$65C2            ; {}
654F: 6F              LD      L,A                 
6550: 75              LD      (HL),L              
6551: 74              LD      (HL),H              
6552: 68              LD      L,B                 
6553: 65              LD      H,L                 
6554: 61              LD      H,C                 
6555: 73              LD      (HL),E              
6556: 74              LD      (HL),H              
6557: 6F              LD      L,A                 
6558: 66              LD      H,(HL)              
6559: 20 74           JR      NZ,$65CF            ; {}
655B: 68              LD      L,B                 
655C: 65              LD      H,L                 
655D: 20 69           JR      NZ,$65C8            ; {}
655F: 73              LD      (HL),E              
6560: 6C              LD      L,H                 
6561: 61              LD      H,C                 
6562: 6E              LD      L,(HL)              
6563: 64              LD      H,H                 
6564: 2C              INC     L                   
6565: 20 20           JR      NZ,$6587            ; {}
6567: 79              LD      A,C                 
6568: 6F              LD      L,A                 
6569: 75              LD      (HL),L              
656A: 20 77           JR      NZ,$65E3            ; {}
656C: 69              LD      L,C                 
656D: 6C              LD      L,H                 
656E: 6C              LD      L,H                 
656F: 20 66           JR      NZ,$65D7            ; {}
6571: 69              LD      L,C                 
6572: 6E              LD      L,(HL)              
6573: 64              LD      H,H                 
6574: 20 20           JR      NZ,$6596            ; {}
6576: 20 73           JR      NZ,$65EB            ; {}
6578: 6F              LD      L,A                 
6579: 6D              LD      L,L                 
657A: 65              LD      H,L                 
657B: 74              LD      (HL),H              
657C: 68              LD      L,B                 
657D: 69              LD      L,C                 
657E: 6E              LD      L,(HL)              
657F: 67              LD      H,A                 
6580: 20 63           JR      NZ,$65E5            ; {}
6582: 61              LD      H,C                 
6583: 6C              LD      L,H                 
6584: 6C              LD      L,H                 
6585: 65              LD      H,L                 
6586: 64              LD      H,H                 
6587: 74              LD      (HL),H              
6588: 68              LD      L,B                 
6589: 65              LD      H,L                 
658A: 20 41           JR      NZ,$65CD            ; {}
658C: 6E              LD      L,(HL)              
658D: 67              LD      H,A                 
658E: 6C              LD      L,H                 
658F: 65              LD      H,L                 
6590: 72              LD      (HL),D              
6591: 20 4B           JR      NZ,$65DE            ; {}
6593: 65              LD      H,L                 
6594: 79              LD      A,C                 
6595: 2E 20           LD      L,$20               
6597: 48              LD      C,B                 
6598: 6D              LD      L,L                 
6599: 6D              LD      L,L                 
659A: 6D              LD      L,L                 
659B: 2E 2E           LD      L,$2E               
659D: 2E 20           LD      L,$20               
659F: 48              LD      C,B                 
65A0: 6F              LD      L,A                 
65A1: 77              LD      (HL),A              
65A2: 20 6D           JR      NZ,$6611            ; {}
65A4: 75              LD      (HL),L              
65A5: 63              LD      H,E                 
65A6: 68              LD      L,B                 
65A7: 6D              LD      L,L                 
65A8: 6F              LD      L,A                 
65A9: 72              LD      (HL),D              
65AA: 65              LD      H,L                 
65AB: 20 6F           JR      NZ,$661C            ; {}
65AD: 62              LD      H,D                 
65AE: 76              HALT                        
65AF: 69              LD      L,C                 
65B0: 6F              LD      L,A                 
65B1: 75              LD      (HL),L              
65B2: 73              LD      (HL),E              
65B3: 20 64           JR      NZ,$6619            ; {}
65B5: 6F              LD      L,A                 
65B6: 20 49           JR      NZ,$6601            ; {}
65B8: 20 68           JR      NZ,$6622            ; {}
65BA: 61              LD      H,C                 
65BB: 76              HALT                        
65BC: 65              LD      H,L                 
65BD: 20 74           JR      NZ,$6633            ; {}
65BF: 6F              LD      L,A                 
65C0: 20 62           JR      NZ,$6624            ; {}
65C2: 65              LD      H,L                 
65C3: 3F              CCF                         
65C4: 20 20           JR      NZ,$65E6            ; {}
65C6: 20 42           JR      NZ,$660A            ; {}
65C8: 79              LD      A,C                 
65C9: 65              LD      H,L                 
65CA: 21 20 43        LD      HL,$4320            
65CD: 4C              LD      C,H                 
65CE: 49              LD      C,C                 
65CF: 43              LD      B,E                 
65D0: 4B              LD      C,E                 
65D1: 21 5E FF        LD      HL,$FF5E            
65D4: 5E              LD      E,(HL)              
65D5: 42              LD      B,D                 
65D6: 52              LD      D,D                 
65D7: 52              LD      D,D                 
65D8: 49              LD      C,C                 
65D9: 4E              LD      C,(HL)              
65DA: 47              LD      B,A                 
65DB: 21 20 42        LD      HL,$4220            
65DE: 52              LD      D,D                 
65DF: 52              LD      D,D                 
65E0: 49              LD      C,C                 
65E1: 4E              LD      C,(HL)              
65E2: 47              LD      B,A                 
65E3: 21 54 68        LD      HL,$6854            
65E6: 69              LD      L,C                 
65E7: 73              LD      (HL),E              
65E8: 20 69           JR      NZ,$6653            ; {}
65EA: 73              LD      (HL),E              
65EB: 20 55           JR      NZ,$6642            ; {}
65ED: 6C              LD      L,H                 
65EE: 72              LD      (HL),D              
65EF: 69              LD      L,C                 
65F0: 72              LD      (HL),D              
65F1: 61              LD      H,C                 
65F2: 21 20 4E        LD      HL,$4E20            
65F5: 6F              LD      L,A                 
65F6: 77              LD      (HL),A              
65F7: 20 79           JR      NZ,$6672            ; {}
65F9: 6F              LD      L,A                 
65FA: 75              LD      (HL),L              
65FB: 5E              LD      E,(HL)              
65FC: 72              LD      (HL),D              
65FD: 65              LD      H,L                 
65FE: 20 62           JR      NZ,$6662            ; {}
6600: 65              LD      H,L                 
6601: 69              LD      L,C                 
6602: 6E              LD      L,(HL)              
6603: 67              LD      H,A                 
6604: 68              LD      L,B                 
6605: 61              LD      H,C                 
6606: 75              LD      (HL),L              
6607: 6E              LD      L,(HL)              
6608: 74              LD      (HL),H              
6609: 65              LD      H,L                 
660A: 64              LD      H,H                 
660B: 20 62           JR      NZ,$666F            ; {}
660D: 79              LD      A,C                 
660E: 20 61           JR      NZ,$6671            ; {}
6610: 20 20           JR      NZ,$6632            ; {}
6612: 20 20           JR      NZ,$6634            ; {}
6614: 67              LD      H,A                 
6615: 68              LD      L,B                 
6616: 6F              LD      L,A                 
6617: 73              LD      (HL),E              
6618: 74              LD      (HL),H              
6619: 3F              CCF                         
661A: 21 20 57        LD      HL,$5720            
661D: 65              LD      H,L                 
661E: 6C              LD      L,H                 
661F: 6C              LD      L,H                 
6620: 2C              INC     L                   
6621: 20 20           JR      NZ,$6643            ; {}
6623: 20 68           JR      NZ,$668D            ; {}
6625: 6F              LD      L,A                 
6626: 77              LD      (HL),A              
6627: 20 61           JR      NZ,$668A            ; {}
6629: 62              LD      H,D                 
662A: 6F              LD      L,A                 
662B: 75              LD      (HL),L              
662C: 74              LD      (HL),H              
662D: 20 74           JR      NZ,$66A3            ; {}
662F: 61              LD      H,C                 
6630: 6B              LD      L,E                 
6631: 69              LD      L,C                 
6632: 6E              LD      L,(HL)              
6633: 67              LD      H,A                 
6634: 68              LD      L,B                 
6635: 69              LD      L,C                 
6636: 6D              LD      L,L                 
6637: 20 77           JR      NZ,$66B0            ; {}
6639: 68              LD      L,B                 
663A: 65              LD      H,L                 
663B: 72              LD      (HL),D              
663C: 65              LD      H,L                 
663D: 20 68           JR      NZ,$66A7            ; {}
663F: 65              LD      H,L                 
6640: 20 20           JR      NZ,$6662            ; {}
6642: 20 20           JR      NZ,$6664            ; {}
6644: 77              LD      (HL),A              
6645: 61              LD      H,C                 
6646: 6E              LD      L,(HL)              
6647: 74              LD      (HL),H              
6648: 73              LD      (HL),E              
6649: 20 74           JR      NZ,$66BF            ; {}
664B: 6F              LD      L,A                 
664C: 20 67           JR      NZ,$66B5            ; {}
664E: 6F              LD      L,A                 
664F: 3F              CCF                         
6650: 20 20           JR      NZ,$6672            ; {}
6652: 20 20           JR      NZ,$6674            ; {}
6654: 42              LD      B,D                 
6655: 79              LD      A,C                 
6656: 65              LD      H,L                 
6657: 21 20 43        LD      HL,$4320            
665A: 4C              LD      C,H                 
665B: 49              LD      C,C                 
665C: 43              LD      B,E                 
665D: 4B              LD      C,E                 
665E: 21 5E FF        LD      HL,$FF5E            
6661: 5E              LD      E,(HL)              
6662: 42              LD      B,D                 
6663: 52              LD      D,D                 
6664: 52              LD      D,D                 
6665: 49              LD      C,C                 
6666: 4E              LD      C,(HL)              
6667: 47              LD      B,A                 
6668: 21 20 42        LD      HL,$4220            
666B: 52              LD      D,D                 
666C: 52              LD      D,D                 
666D: 49              LD      C,C                 
666E: 4E              LD      C,(HL)              
666F: 47              LD      B,A                 
6670: 21 48 69        LD      HL,$6948            
6673: 2C              INC     L                   
6674: 20 69           JR      NZ,$66DF            ; {}
6676: 74              LD      (HL),H              
6677: 5E              LD      E,(HL)              
6678: 73              LD      (HL),E              
6679: 20 55           JR      NZ,$66D0            ; {}
667B: 6C              LD      L,H                 
667C: 72              LD      (HL),D              
667D: 69              LD      L,C                 
667E: 72              LD      (HL),D              
667F: 61              LD      H,C                 
6680: 21 54 68        LD      HL,$6854            
6683: 65              LD      H,L                 
6684: 20 43           JR      NZ,$66C9            ; {}
6686: 61              LD      H,C                 
6687: 74              LD      (HL),H              
6688: 66              LD      H,(HL)              
6689: 69              LD      L,C                 
668A: 73              LD      (HL),E              
668B: 68              LD      L,B                 
668C: 5E              LD      E,(HL)              
668D: 73              LD      (HL),E              
668E: 20 20           JR      NZ,$66B0            ; {}
6690: 20 6D           JR      NZ,$66FF            ; {}
6692: 6F              LD      L,A                 
6693: 75              LD      (HL),L              
6694: 74              LD      (HL),H              
6695: 68              LD      L,B                 
6696: 20 69           JR      NZ,$6701            ; {}
6698: 73              LD      (HL),E              
6699: 20 77           JR      NZ,$6712            ; {}
669B: 69              LD      L,C                 
669C: 64              LD      H,H                 
669D: 65              LD      H,L                 
669E: 20 20           JR      NZ,$66C0            ; {}
66A0: 20 6F           JR      NZ,$6711            ; {}
66A2: 70              LD      (HL),B              
66A3: 65              LD      H,L                 
66A4: 6E              LD      L,(HL)              
66A5: 3F              CCF                         
66A6: 20 20           JR      NZ,$66C8            ; {}
66A8: 49              LD      C,C                 
66A9: 74              LD      (HL),H              
66AA: 20 73           JR      NZ,$671F            ; {}
66AC: 6F              LD      L,A                 
66AD: 75              LD      (HL),L              
66AE: 6E              LD      L,(HL)              
66AF: 64              LD      H,H                 
66B0: 73              LD      (HL),E              
66B1: 6C              LD      L,H                 
66B2: 69              LD      L,C                 
66B3: 6B              LD      L,E                 
66B4: 65              LD      H,L                 
66B5: 20 61           JR      NZ,$6718            ; {}
66B7: 20 67           JR      NZ,$6720            ; {}
66B9: 72              LD      (HL),D              
66BA: 65              LD      H,L                 
66BB: 61              LD      H,C                 
66BC: 74              LD      (HL),H              
66BD: 20 20           JR      NZ,$66DF            ; {}
66BF: 20 20           JR      NZ,$66E1            ; {}
66C1: 70              LD      (HL),B              
66C2: 6C              LD      L,H                 
66C3: 61              LD      H,C                 
66C4: 63              LD      H,E                 
66C5: 65              LD      H,L                 
66C6: 20 74           JR      NZ,$673C            ; {}
66C8: 6F              LD      L,A                 
66C9: 20 64           JR      NZ,$672F            ; {}
66CB: 69              LD      L,C                 
66CC: 76              HALT                        
66CD: 65              LD      H,L                 
66CE: 21 20 20        LD      HL,$2020            
66D1: 42              LD      B,D                 
66D2: 79              LD      A,C                 
66D3: 65              LD      H,L                 
66D4: 21 20 20        LD      HL,$2020            
66D7: 43              LD      B,E                 
66D8: 4C              LD      C,H                 
66D9: 49              LD      C,C                 
66DA: 43              LD      B,E                 
66DB: 4B              LD      C,E                 
66DC: 21 5E FF        LD      HL,$FF5E            
66DF: 5E              LD      E,(HL)              
66E0: 42              LD      B,D                 
66E1: 52              LD      D,D                 
66E2: 52              LD      D,D                 
66E3: 49              LD      C,C                 
66E4: 4E              LD      C,(HL)              
66E5: 47              LD      B,A                 
66E6: 21 20 42        LD      HL,$4220            
66E9: 52              LD      D,D                 
66EA: 52              LD      D,D                 
66EB: 49              LD      C,C                 
66EC: 4E              LD      C,(HL)              
66ED: 47              LD      B,A                 
66EE: 21 55 6C        LD      HL,$6C55            
66F1: 72              LD      (HL),D              
66F2: 69              LD      L,C                 
66F3: 72              LD      (HL),D              
66F4: 61              LD      H,C                 
66F5: 20 68           JR      NZ,$675F            ; {}
66F7: 65              LD      H,L                 
66F8: 72              LD      (HL),D              
66F9: 65              LD      H,L                 
66FA: 21 20 2E        LD      HL,$2E20            
66FD: 2E 2E           LD      L,$2E               
66FF: 48              LD      C,B                 
6700: 61              LD      H,C                 
6701: 76              HALT                        
6702: 65              LD      H,L                 
6703: 20 79           JR      NZ,$677E            ; {}
6705: 6F              LD      L,A                 
6706: 75              LD      (HL),L              
6707: 20 62           JR      NZ,$676B            ; {}
6709: 65              LD      H,L                 
670A: 65              LD      H,L                 
670B: 6E              LD      L,(HL)              
670C: 20 74           JR      NZ,$6782            ; {}
670E: 6F              LD      L,A                 
670F: 74              LD      (HL),H              
6710: 68              LD      L,B                 
6711: 65              LD      H,L                 
6712: 20 46           JR      NZ,$675A            ; {}
6714: 61              LD      H,C                 
6715: 63              LD      H,E                 
6716: 65              LD      H,L                 
6717: 20 53           JR      NZ,$676C            ; {}
6719: 68              LD      L,B                 
671A: 72              LD      (HL),D              
671B: 69              LD      L,C                 
671C: 6E              LD      L,(HL)              
671D: 65              LD      H,L                 
671E: 3F              CCF                         
671F: 49              LD      C,C                 
6720: 74              LD      (HL),H              
6721: 20 69           JR      NZ,$678C            ; {}
6723: 73              LD      (HL),E              
6724: 20 6E           JR      NZ,$6794            ; {}
6726: 6F              LD      L,A                 
6727: 72              LD      (HL),D              
6728: 74              LD      (HL),H              
6729: 68              LD      L,B                 
672A: 20 6F           JR      NZ,$679B            ; {}
672C: 66              LD      H,(HL)              
672D: 20 20           JR      NZ,$674F            ; {}
672F: 41              LD      B,C                 
6730: 6E              LD      L,(HL)              
6731: 69              LD      L,C                 
6732: 6D              LD      L,L                 
6733: 61              LD      H,C                 
6734: 6C              LD      L,H                 
6735: 20 56           JR      NZ,$678D            ; {}
6737: 69              LD      L,C                 
6738: 6C              LD      L,H                 
6739: 6C              LD      L,H                 
673A: 61              LD      H,C                 
673B: 67              LD      H,A                 
673C: 65              LD      H,L                 
673D: 2E 20           LD      L,$20               
673F: 54              LD      D,H                 
6740: 68              LD      L,B                 
6741: 61              LD      H,C                 
6742: 74              LD      (HL),H              
6743: 20 69           JR      NZ,$67AE            ; {}
6745: 73              LD      (HL),E              
6746: 20 61           JR      NZ,$67A9            ; {}
6748: 20 76           JR      NZ,$67C0            ; {}
674A: 65              LD      H,L                 
674B: 72              LD      (HL),D              
674C: 79              LD      A,C                 
674D: 20 20           JR      NZ,$676F            ; {}
674F: 69              LD      L,C                 
6750: 6E              LD      L,(HL)              
6751: 74              LD      (HL),H              
6752: 65              LD      H,L                 
6753: 72              LD      (HL),D              
6754: 65              LD      H,L                 
6755: 73              LD      (HL),E              
6756: 74              LD      (HL),H              
6757: 69              LD      L,C                 
6758: 6E              LD      L,(HL)              
6759: 67              LD      H,A                 
675A: 20 20           JR      NZ,$677C            ; {}
675C: 20 20           JR      NZ,$677E            ; {}
675E: 20 72           JR      NZ,$67D2            ; {}
6760: 75              LD      (HL),L              
6761: 69              LD      L,C                 
6762: 6E              LD      L,(HL)              
6763: 2E 2E           LD      L,$2E               
6765: 2E 20           LD      L,$20               
6767: 43              LD      B,E                 
6768: 4C              LD      C,H                 
6769: 49              LD      C,C                 
676A: 43              LD      B,E                 
676B: 4B              LD      C,E                 
676C: 21 5E FF        LD      HL,$FF5E            
676F: 5E              LD      E,(HL)              
6770: 42              LD      B,D                 
6771: 52              LD      D,D                 
6772: 52              LD      D,D                 
6773: 49              LD      C,C                 
6774: 4E              LD      C,(HL)              
6775: 47              LD      B,A                 
6776: 21 20 42        LD      HL,$4220            
6779: 52              LD      D,D                 
677A: 52              LD      D,D                 
677B: 49              LD      C,C                 
677C: 4E              LD      C,(HL)              
677D: 47              LD      B,A                 
677E: 21 48 69        LD      HL,$6948            
6781: 2C              INC     L                   
6782: 20 69           JR      NZ,$67ED            ; {}
6784: 74              LD      (HL),H              
6785: 5E              LD      E,(HL)              
6786: 73              LD      (HL),E              
6787: 20 55           JR      NZ,$67DE            ; {}
6789: 6C              LD      L,H                 
678A: 72              LD      (HL),D              
678B: 69              LD      L,C                 
678C: 72              LD      (HL),D              
678D: 61              LD      H,C                 
678E: 21 48 61        LD      HL,$6148            
6791: 76              HALT                        
6792: 65              LD      H,L                 
6793: 20 79           JR      NZ,$680E            ; {}
6795: 6F              LD      L,A                 
6796: 75              LD      (HL),L              
6797: 20 68           JR      NZ,$6801            ; {}
6799: 65              LD      H,L                 
679A: 61              LD      H,C                 
679B: 72              LD      (HL),D              
679C: 64              LD      H,H                 
679D: 20 20           JR      NZ,$67BF            ; {}
679F: 6F              LD      L,A                 
67A0: 66              LD      H,(HL)              
67A1: 20 74           JR      NZ,$6817            ; {}
67A3: 68              LD      L,B                 
67A4: 65              LD      H,L                 
67A5: 20 46           JR      NZ,$67ED            ; {}
67A7: 6C              LD      L,H                 
67A8: 79              LD      A,C                 
67A9: 69              LD      L,C                 
67AA: 6E              LD      L,(HL)              
67AB: 67              LD      H,A                 
67AC: 20 20           JR      NZ,$67CE            ; {}
67AE: 20 52           JR      NZ,$6802            ; {}
67B0: 6F              LD      L,A                 
67B1: 6F              LD      L,A                 
67B2: 73              LD      (HL),E              
67B3: 74              LD      (HL),H              
67B4: 65              LD      H,L                 
67B5: 72              LD      (HL),D              
67B6: 20 6F           JR      NZ,$6827            ; {}
67B8: 66              LD      H,(HL)              
67B9: 20 4D           JR      NZ,$6808            ; {}
67BB: 61              LD      H,C                 
67BC: 62              LD      H,D                 
67BD: 65              LD      H,L                 
67BE: 20 56           JR      NZ,$6816            ; {}
67C0: 69              LD      L,C                 
67C1: 6C              LD      L,H                 
67C2: 6C              LD      L,H                 
67C3: 61              LD      H,C                 
67C4: 67              LD      H,A                 
67C5: 65              LD      H,L                 
67C6: 3F              CCF                         
67C7: 20 20           JR      NZ,$67E9            ; {}
67C9: 49              LD      C,C                 
67CA: 6E              LD      L,(HL)              
67CB: 20 74           JR      NZ,$6841            ; {}
67CD: 68              LD      L,B                 
67CE: 65              LD      H,L                 
67CF: 67              LD      H,A                 
67D0: 6F              LD      L,A                 
67D1: 6F              LD      L,A                 
67D2: 64              LD      H,H                 
67D3: 20 6F           JR      NZ,$6844            ; {}
67D5: 6C              LD      L,H                 
67D6: 64              LD      H,H                 
67D7: 20 64           JR      NZ,$683D            ; {}
67D9: 61              LD      H,C                 
67DA: 79              LD      A,C                 
67DB: 73              LD      (HL),E              
67DC: 2C              INC     L                   
67DD: 20 20           JR      NZ,$67FF            ; {}
67DF: 69              LD      L,C                 
67E0: 74              LD      (HL),H              
67E1: 20 75           JR      NZ,$6858            ; {}
67E3: 73              LD      (HL),E              
67E4: 65              LD      H,L                 
67E5: 64              LD      H,H                 
67E6: 20 74           JR      NZ,$685C            ; {}
67E8: 6F              LD      L,A                 
67E9: 20 67           JR      NZ,$6852            ; {}
67EB: 69              LD      L,C                 
67EC: 76              HALT                        
67ED: 65              LD      H,L                 
67EE: 20 75           JR      NZ,$6865            ; {}
67F0: 73              LD      (HL),E              
67F1: 20 72           JR      NZ,$6865            ; {}
67F3: 69              LD      L,C                 
67F4: 64              LD      H,H                 
67F5: 65              LD      H,L                 
67F6: 73              LD      (HL),E              
67F7: 20 69           JR      NZ,$6862            ; {}
67F9: 66              LD      H,(HL)              
67FA: 20 77           JR      NZ,$6873            ; {}
67FC: 65              LD      H,L                 
67FD: 20 20           JR      NZ,$681F            ; {}
67FF: 68              LD      L,B                 
6800: 65              LD      H,L                 
6801: 6C              LD      L,H                 
6802: 64              LD      H,H                 
6803: 20 69           JR      NZ,$686E            ; {}
6805: 74              LD      (HL),H              
6806: 20 61           JR      NZ,$6869            ; {}
6808: 62              LD      H,D                 
6809: 6F              LD      L,A                 
680A: 76              HALT                        
680B: 65              LD      H,L                 
680C: 20 20           JR      NZ,$682E            ; {}
680E: 20 6F           JR      NZ,$687F            ; {}
6810: 75              LD      (HL),L              
6811: 72              LD      (HL),D              
6812: 20 68           JR      NZ,$687C            ; {}
6814: 65              LD      H,L                 
6815: 61              LD      H,C                 
6816: 64              LD      H,H                 
6817: 73              LD      (HL),E              
6818: 2E 2E           LD      L,$2E               
681A: 2E 20           LD      L,$20               
681C: 4E              LD      C,(HL)              
681D: 6F              LD      L,A                 
681E: 77              LD      (HL),A              
681F: 69              LD      L,C                 
6820: 74              LD      (HL),H              
6821: 20 69           JR      NZ,$688C            ; {}
6823: 73              LD      (HL),E              
6824: 20 6C           JR      NZ,$6892            ; {}
6826: 79              LD      A,C                 
6827: 69              LD      L,C                 
6828: 6E              LD      L,(HL)              
6829: 67              LD      H,A                 
682A: 20 20           JR      NZ,$684C            ; {}
682C: 20 20           JR      NZ,$684E            ; {}
682E: 20 75           JR      NZ,$68A5            ; {}
6830: 6E              LD      L,(HL)              
6831: 64              LD      H,H                 
6832: 65              LD      H,L                 
6833: 72              LD      (HL),D              
6834: 20 74           JR      NZ,$68AA            ; {}
6836: 68              LD      L,B                 
6837: 65              LD      H,L                 
6838: 20 20           JR      NZ,$685A            ; {}
683A: 20 20           JR      NZ,$685C            ; {}
683C: 20 20           JR      NZ,$685E            ; {}
683E: 20 57           JR      NZ,$6897            ; {}
6840: 65              LD      H,L                 
6841: 61              LD      H,C                 
6842: 74              LD      (HL),H              
6843: 68              LD      L,B                 
6844: 65              LD      H,L                 
6845: 72              LD      (HL),D              
6846: 63              LD      H,E                 
6847: 6F              LD      L,A                 
6848: 63              LD      H,E                 
6849: 6B              LD      L,E                 
684A: 2E 2E           LD      L,$2E               
684C: 2E 20           LD      L,$20               
684E: 20 49           JR      NZ,$6899            ; {}
6850: 73              LD      (HL),E              
6851: 20 74           JR      NZ,$68C7            ; {}
6853: 68              LD      L,B                 
6854: 61              LD      H,C                 
6855: 74              LD      (HL),H              
6856: 20 75           JR      NZ,$68CD            ; {}
6858: 73              LD      (HL),E              
6859: 65              LD      H,L                 
685A: 66              LD      H,(HL)              
685B: 75              LD      (HL),L              
685C: 6C              LD      L,H                 
685D: 20 20           JR      NZ,$687F            ; {}
685F: 66              LD      H,(HL)              
6860: 6F              LD      L,A                 
6861: 72              LD      (HL),D              
6862: 20 79           JR      NZ,$68DD            ; {}
6864: 6F              LD      L,A                 
6865: 75              LD      (HL),L              
6866: 3F              CCF                         
6867: 20 20           JR      NZ,$6889            ; {}
6869: 49              LD      C,C                 
686A: 20 68           JR      NZ,$68D4            ; {}
686C: 6F              LD      L,A                 
686D: 70              LD      (HL),B              
686E: 65              LD      H,L                 
686F: 73              LD      (HL),E              
6870: 6F              LD      L,A                 
6871: 21 20 42        LD      HL,$4220            
6874: 79              LD      A,C                 
6875: 65              LD      H,L                 
6876: 21 20 43        LD      HL,$4320            
6879: 4C              LD      C,H                 
687A: 49              LD      C,C                 
687B: 43              LD      B,E                 
687C: 4B              LD      C,E                 
687D: 21 5E FF        LD      HL,$FF5E            
6880: 5E              LD      E,(HL)              
6881: 42              LD      B,D                 
6882: 52              LD      D,D                 
6883: 52              LD      D,D                 
6884: 49              LD      C,C                 
6885: 4E              LD      C,(HL)              
6886: 47              LD      B,A                 
6887: 21 20 42        LD      HL,$4220            
688A: 52              LD      D,D                 
688B: 52              LD      D,D                 
688C: 49              LD      C,C                 
688D: 4E              LD      C,(HL)              
688E: 47              LD      B,A                 
688F: 21 48 69        LD      HL,$6948            
6892: 2C              INC     L                   
6893: 20 69           JR      NZ,$68FE            ; {}
6895: 74              LD      (HL),H              
6896: 5E              LD      E,(HL)              
6897: 73              LD      (HL),E              
6898: 20 55           JR      NZ,$68EF            ; {}
689A: 6C              LD      L,H                 
689B: 72              LD      (HL),D              
689C: 69              LD      L,C                 
689D: 72              LD      (HL),D              
689E: 61              LD      H,C                 
689F: 21 54 68        LD      HL,$6854            
68A2: 65              LD      H,L                 
68A3: 20 68           JR      NZ,$690D            ; {}
68A5: 65              LD      H,L                 
68A6: 61              LD      H,C                 
68A7: 64              LD      H,H                 
68A8: 20 6F           JR      NZ,$6919            ; {}
68AA: 66              LD      H,(HL)              
68AB: 20 74           JR      NZ,$6921            ; {}
68AD: 68              LD      L,B                 
68AE: 65              LD      H,L                 
68AF: 20 74           JR      NZ,$6925            ; {}
68B1: 75              LD      (HL),L              
68B2: 72              LD      (HL),D              
68B3: 74              LD      (HL),H              
68B4: 6C              LD      L,H                 
68B5: 65              LD      H,L                 
68B6: 20 69           JR      NZ,$6921            ; {}
68B8: 73              LD      (HL),E              
68B9: 20 69           JR      NZ,$6924            ; {}
68BB: 6E              LD      L,(HL)              
68BC: 20 20           JR      NZ,$68DE            ; {}
68BE: 20 20           JR      NZ,$68E0            ; {}
68C0: 79              LD      A,C                 
68C1: 6F              LD      L,A                 
68C2: 75              LD      (HL),L              
68C3: 72              LD      (HL),D              
68C4: 20 77           JR      NZ,$693D            ; {}
68C6: 61              LD      H,C                 
68C7: 79              LD      A,C                 
68C8: 3F              CCF                         
68C9: 20 20           JR      NZ,$68EB            ; {}
68CB: 50              LD      D,B                 
68CC: 75              LD      (HL),L              
68CD: 74              LD      (HL),H              
68CE: 20 20           JR      NZ,$68F0            ; {}
68D0: 6C              LD      L,H                 
68D1: 69              LD      L,C                 
68D2: 66              LD      H,(HL)              
68D3: 65              LD      H,L                 
68D4: 20 69           JR      NZ,$693F            ; {}
68D6: 6E              LD      L,(HL)              
68D7: 74              LD      (HL),H              
68D8: 6F              LD      L,A                 
68D9: 20 69           JR      NZ,$6944            ; {}
68DB: 74              LD      (HL),H              
68DC: 20 61           JR      NZ,$693F            ; {}
68DE: 6E              LD      L,(HL)              
68DF: 64              LD      H,H                 
68E0: 69              LD      L,C                 
68E1: 74              LD      (HL),H              
68E2: 20 77           JR      NZ,$695B            ; {}
68E4: 69              LD      L,C                 
68E5: 6C              LD      L,H                 
68E6: 6C              LD      L,H                 
68E7: 20 6D           JR      NZ,$6956            ; {}
68E9: 6F              LD      L,A                 
68EA: 76              HALT                        
68EB: 65              LD      H,L                 
68EC: 21 20 20        LD      HL,$2020            
68EF: 20 49           JR      NZ,$693A            ; {}
68F1: 74              LD      (HL),H              
68F2: 5E              LD      E,(HL)              
68F3: 73              LD      (HL),E              
68F4: 20 74           JR      NZ,$696A            ; {}
68F6: 72              LD      (HL),D              
68F7: 75              LD      (HL),L              
68F8: 65              LD      H,L                 
68F9: 21 20 54        LD      HL,$5420            
68FC: 72              LD      (HL),D              
68FD: 75              LD      (HL),L              
68FE: 65              LD      H,L                 
68FF: 21 42 79        LD      HL,$7942            
6902: 65              LD      H,L                 
6903: 21 20 20        LD      HL,$2020            
6906: 43              LD      B,E                 
6907: 4C              LD      C,H                 
6908: 49              LD      C,C                 
6909: 43              LD      B,E                 
690A: 4B              LD      C,E                 
690B: 21 5E FF        LD      HL,$FF5E            
690E: 20 20           JR      NZ,$6930            ; {}
6910: 20 2E           JR      NZ,$6940            ; {}
6912: 2E 2E           LD      L,$2E               
6914: 53              LD      D,E                 
6915: 57              LD      D,A                 
6916: 41              LD      B,C                 
6917: 4D              LD      C,L                 
6918: 50              LD      D,B                 
6919: 2E 2E           LD      L,$2E               
691B: 2E 20           LD      L,$20               
691D: 20 20           JR      NZ,$693F            ; {}
691F: 41              LD      B,C                 
6920: 20 70           JR      NZ,$6992            ; {}
6922: 61              LD      H,C                 
6923: 74              LD      (HL),H              
6924: 68              LD      L,B                 
6925: 20 6F           JR      NZ,$6996            ; {}
6927: 70              LD      (HL),B              
6928: 65              LD      H,L                 
6929: 6E              LD      L,(HL)              
692A: 73              LD      (HL),E              
692B: 2E 2E           LD      L,$2E               
692D: 2E 69           LD      L,$69               
692F: 6E              LD      L,(HL)              
6930: 20 74           JR      NZ,$69A6            ; {}
6932: 68              LD      L,B                 
6933: 65              LD      H,L                 
6934: 20 62           JR      NZ,$6998            ; {}
6936: 6C              LD      L,H                 
6937: 6F              LD      L,A                 
6938: 6F              LD      L,A                 
6939: 6D              LD      L,L                 
693A: 73              LD      (HL),E              
693B: 2E 2E           LD      L,$2E               
693D: 2E FF           LD      L,$FF               
693F: 20 20           JR      NZ,$6961            ; {}
6941: 2E 2E           LD      L,$2E               
6943: 2E 50           LD      L,$50               
6945: 52              LD      D,D                 
6946: 41              LD      B,C                 
6947: 49              LD      C,C                 
6948: 52              LD      D,D                 
6949: 49              LD      C,C                 
694A: 45              LD      B,L                 
694B: 2E 2E           LD      L,$2E               
694D: 2E 20           LD      L,$20               
694F: 20 20           JR      NZ,$6971            ; {}
6951: 2E 2E           LD      L,$2E               
6953: 2E 50           LD      L,$50               
6955: 52              LD      D,D                 
6956: 41              LD      B,C                 
6957: 49              LD      C,C                 
6958: 52              LD      D,D                 
6959: 49              LD      C,C                 
695A: 45              LD      B,L                 
695B: 2E 2E           LD      L,$2E               
695D: 2E 20           LD      L,$20               
695F: 20 54           JR      NZ,$69B5            ; {}
6961: 68              LD      L,B                 
6962: 65              LD      H,L                 
6963: 20 50           JR      NZ,$69B5            ; {}
6965: 72              LD      (HL),D              
6966: 61              LD      H,C                 
6967: 69              LD      L,C                 
6968: 72              LD      (HL),D              
6969: 69              LD      L,C                 
696A: 65              LD      H,L                 
696B: 20 69           JR      NZ,$69D6            ; {}
696D: 73              LD      (HL),E              
696E: 20 20           JR      NZ,$6990            ; {}
6970: 20 20           JR      NZ,$6992            ; {}
6972: 20 20           JR      NZ,$6994            ; {}
6974: 77              LD      (HL),A              
6975: 61              LD      H,C                 
6976: 69              LD      L,C                 
6977: 74              LD      (HL),H              
6978: 69              LD      L,C                 
6979: 6E              LD      L,(HL)              
697A: 67              LD      H,A                 
697B: 2E 2E           LD      L,$2E               
697D: 2E FF           LD      L,$FF               
697F: 2E 2E           LD      L,$2E               
6981: 2E 57           LD      L,$57               
6983: 41              LD      B,C                 
6984: 54              LD      D,H                 
6985: 45              LD      B,L                 
6986: 52              LD      D,D                 
6987: 46              LD      B,(HL)              
6988: 41              LD      B,C                 
6989: 4C              LD      C,H                 
698A: 4C              LD      C,H                 
698B: 2E 2E           LD      L,$2E               
698D: 2E 20           LD      L,$20               
698F: 49              LD      C,C                 
6990: 74              LD      (HL),H              
6991: 20 69           JR      NZ,$69FC            ; {}
6993: 73              LD      (HL),E              
6994: 20 68           JR      NZ,$69FE            ; {}
6996: 69              LD      L,C                 
6997: 64              LD      H,H                 
6998: 64              LD      H,H                 
6999: 65              LD      H,L                 
699A: 6E              LD      L,(HL)              
699B: 20 69           JR      NZ,$6A06            ; {}
699D: 6E              LD      L,(HL)              
699E: 20 74           JR      NZ,$6A14            ; {}
69A0: 68              LD      L,B                 
69A1: 65              LD      H,L                 
69A2: 20 77           JR      NZ,$6A1B            ; {}
69A4: 61              LD      H,C                 
69A5: 74              LD      (HL),H              
69A6: 65              LD      H,L                 
69A7: 72              LD      (HL),D              
69A8: 66              LD      H,(HL)              
69A9: 61              LD      H,C                 
69AA: 6C              LD      L,H                 
69AB: 6C              LD      L,H                 
69AC: 2E 2E           LD      L,$2E               
69AE: 2E FF           LD      L,$FF               
69B0: 20 20           JR      NZ,$69D2            ; {}
69B2: 20 20           JR      NZ,$69D4            ; {}
69B4: 2E 2E           LD      L,$2E               
69B6: 2E 42           LD      L,$42               
69B8: 41              LD      B,C                 
69B9: 59              LD      E,C                 
69BA: 2E 2E           LD      L,$2E               
69BC: 2E 20           LD      L,$20               
69BE: 20 20           JR      NZ,$69E0            ; {}
69C0: 59              LD      E,C                 
69C1: 6F              LD      L,A                 
69C2: 75              LD      (HL),L              
69C3: 72              LD      (HL),D              
69C4: 20 72           JR      NZ,$6A38            ; {}
69C6: 6F              LD      L,A                 
69C7: 61              LD      H,C                 
69C8: 64              LD      H,H                 
69C9: 20 67           JR      NZ,$6A32            ; {}
69CB: 6F              LD      L,A                 
69CC: 65              LD      H,L                 
69CD: 73              LD      (HL),E              
69CE: 20 20           JR      NZ,$69F0            ; {}
69D0: 69              LD      L,C                 
69D1: 6E              LD      L,(HL)              
69D2: 74              LD      (HL),H              
69D3: 6F              LD      L,A                 
69D4: 20 74           JR      NZ,$6A4A            ; {}
69D6: 68              LD      L,B                 
69D7: 65              LD      H,L                 
69D8: 20 62           JR      NZ,$6A3C            ; {}
69DA: 61              LD      H,C                 
69DB: 79              LD      A,C                 
69DC: 2E 2E           LD      L,$2E               
69DE: 2E 20           LD      L,$20               
69E0: FF              RST     0X38                
69E1: 20 20           JR      NZ,$6A03            ; {}
69E3: 20 2E           JR      NZ,$6A13            ; {}
69E5: 2E 2E           LD      L,$2E               
69E7: 53              LD      D,E                 
69E8: 48              LD      C,B                 
69E9: 52              LD      D,D                 
69EA: 49              LD      C,C                 
69EB: 4E              LD      C,(HL)              
69EC: 45              LD      B,L                 
69ED: 2E 2E           LD      L,$2E               
69EF: 2E 20           LD      L,$20               
69F1: 41              LD      B,C                 
69F2: 6E              LD      L,(HL)              
69F3: 20 69           JR      NZ,$6A5E            ; {}
69F5: 73              LD      (HL),E              
69F6: 6C              LD      L,H                 
69F7: 61              LD      H,C                 
69F8: 6E              LD      L,(HL)              
69F9: 64              LD      H,H                 
69FA: 20 73           JR      NZ,$6A6F            ; {}
69FC: 65              LD      H,L                 
69FD: 63              LD      H,E                 
69FE: 72              LD      (HL),D              
69FF: 65              LD      H,L                 
6A00: 74              LD      (HL),H              
6A01: 69              LD      L,C                 
6A02: 6E              LD      L,(HL)              
6A03: 20 74           JR      NZ,$6A79            ; {}
6A05: 68              LD      L,B                 
6A06: 65              LD      H,L                 
6A07: 20 73           JR      NZ,$6A7C            ; {}
6A09: 68              LD      L,B                 
6A0A: 72              LD      (HL),D              
6A0B: 69              LD      L,C                 
6A0C: 6E              LD      L,(HL)              
6A0D: 65              LD      H,L                 
6A0E: 2E 2E           LD      L,$2E               
6A10: 2E FF           LD      L,$FF               
6A12: 20 2E           JR      NZ,$6A42            ; {}
6A14: 2E 2E           LD      L,$2E               
6A16: 4D              LD      C,L                 
6A17: 4F              LD      C,A                 
6A18: 55              LD      D,L                 
6A19: 4E              LD      C,(HL)              
6A1A: 54              LD      D,H                 
6A1B: 41              LD      B,C                 
6A1C: 49              LD      C,C                 
6A1D: 4E              LD      C,(HL)              
6A1E: 2E 2E           LD      L,$2E               
6A20: 2E 20           LD      L,$20               
6A22: 53              LD      D,E                 
6A23: 6F              LD      L,A                 
6A24: 6D              LD      L,L                 
6A25: 65              LD      H,L                 
6A26: 74              LD      (HL),H              
6A27: 68              LD      L,B                 
6A28: 69              LD      L,C                 
6A29: 6E              LD      L,(HL)              
6A2A: 67              LD      H,A                 
6A2B: 20 63           JR      NZ,$6A90            ; {}
6A2D: 61              LD      H,C                 
6A2E: 6C              LD      L,H                 
6A2F: 6C              LD      L,H                 
6A30: 73              LD      (HL),E              
6A31: 20 20           JR      NZ,$6A53            ; {}
6A33: 20 2E           JR      NZ,$6A63            ; {}
6A35: 2E 2E           LD      L,$2E               
6A37: 66              LD      H,(HL)              
6A38: 72              LD      (HL),D              
6A39: 6F              LD      L,A                 
6A3A: 6D              LD      L,L                 
6A3B: 20 74           JR      NZ,$6AB1            ; {}
6A3D: 68              LD      L,B                 
6A3E: 65              LD      H,L                 
6A3F: 20 20           JR      NZ,$6A61            ; {}
6A41: 20 20           JR      NZ,$6A63            ; {}
6A43: 20 6D           JR      NZ,$6AB2            ; {}
6A45: 6F              LD      L,A                 
6A46: 75              LD      (HL),L              
6A47: 6E              LD      L,(HL)              
6A48: 74              LD      (HL),H              
6A49: 61              LD      H,C                 
6A4A: 69              LD      L,C                 
6A4B: 6E              LD      L,(HL)              
6A4C: 73              LD      (HL),E              
6A4D: 2E 2E           LD      L,$2E               
6A4F: 2E FF           LD      L,$FF               
6A51: 20 20           JR      NZ,$6A73            ; {}
6A53: 2E 2E           LD      L,$2E               
6A55: 2E 4F           LD      L,$4F               
6A57: 43              LD      B,E                 
6A58: 41              LD      B,C                 
6A59: 52              LD      D,D                 
6A5A: 49              LD      C,C                 
6A5B: 4E              LD      C,(HL)              
6A5C: 41              LD      B,C                 
6A5D: 2E 2E           LD      L,$2E               
6A5F: 2E 20           LD      L,$20               
6A61: 54              LD      D,H                 
6A62: 68              LD      L,B                 
6A63: 65              LD      H,L                 
6A64: 20 6D           JR      NZ,$6AD3            ; {}
6A66: 75              LD      (HL),L              
6A67: 73              LD      (HL),E              
6A68: 69              LD      L,C                 
6A69: 63              LD      H,E                 
6A6A: 20 6F           JR      NZ,$6ADB            ; {}
6A6C: 66              LD      H,(HL)              
6A6D: 20 74           JR      NZ,$6AE3            ; {}
6A6F: 68              LD      L,B                 
6A70: 65              LD      H,L                 
6A71: 4F              LD      C,A                 
6A72: 63              LD      H,E                 
6A73: 61              LD      H,C                 
6A74: 72              LD      (HL),D              
6A75: 69              LD      L,C                 
6A76: 6E              LD      L,(HL)              
6A77: 61              LD      H,C                 
6A78: 20 6C           JR      NZ,$6AE6            ; {}
6A7A: 65              LD      H,L                 
6A7B: 61              LD      H,C                 
6A7C: 64              LD      H,H                 
6A7D: 73              LD      (HL),E              
6A7E: 2E 2E           LD      L,$2E               
6A80: 2E FF           LD      L,$FF               
6A82: 20 20           JR      NZ,$6AA4            ; {}
6A84: 20 20           JR      NZ,$6AA6            ; {}
6A86: 2E 2E           LD      L,$2E               
6A88: 2E 45           LD      L,$45               
6A8A: 47              LD      B,A                 
6A8B: 47              LD      B,A                 
6A8C: 2E 2E           LD      L,$2E               
6A8E: 2E 2E           LD      L,$2E               
6A90: 20 20           JR      NZ,$6AB2            ; {}
6A92: 54              LD      D,H                 
6A93: 68              LD      L,B                 
6A94: 65              LD      H,L                 
6A95: 20 45           JR      NZ,$6ADC            ; {}
6A97: 67              LD      H,A                 
6A98: 67              LD      H,A                 
6A99: 20 6F           JR      NZ,$6B0A            ; {}
6A9B: 6E              LD      L,(HL)              
6A9C: 20 74           JR      NZ,$6B12            ; {}
6A9E: 68              LD      L,B                 
6A9F: 65              LD      H,L                 
6AA0: 20 20           JR      NZ,$6AC2            ; {}
6AA2: 6D              LD      L,L                 
6AA3: 6F              LD      L,A                 
6AA4: 75              LD      (HL),L              
6AA5: 6E              LD      L,(HL)              
6AA6: 74              LD      (HL),H              
6AA7: 61              LD      H,C                 
6AA8: 69              LD      L,C                 
6AA9: 6E              LD      L,(HL)              
6AAA: 20 63           JR      NZ,$6B0F            ; {}
6AAC: 61              LD      H,C                 
6AAD: 6C              LD      L,H                 
6AAE: 6C              LD      L,H                 
6AAF: 73              LD      (HL),E              
6AB0: 21 FF 54        LD      HL,$54FF            
6AB3: 68              LD      L,B                 
6AB4: 65              LD      H,L                 
6AB5: 6E              LD      L,(HL)              
6AB6: 20 59           JR      NZ,$6B11            ; {}
6AB8: 4F              LD      C,A                 
6AB9: 55              LD      D,L                 
6ABA: 20 73           JR      NZ,$6B2F            ; {}
6ABC: 77              LD      (HL),A              
6ABD: 65              LD      H,L                 
6ABE: 65              LD      H,L                 
6ABF: 70              LD      (HL),B              
6AC0: 20 20           JR      NZ,$6AE2            ; {}
6AC2: 74              LD      (HL),H              
6AC3: 68              LD      L,B                 
6AC4: 65              LD      H,L                 
6AC5: 20 69           JR      NZ,$6B30            ; {}
6AC7: 73              LD      (HL),E              
6AC8: 6C              LD      L,H                 
6AC9: 61              LD      H,C                 
6ACA: 6E              LD      L,(HL)              
6ACB: 64              LD      H,H                 
6ACC: 21 FF 59        LD      HL,$59FF            
6ACF: 41              LD      B,C                 
6AD0: 48              LD      C,B                 
6AD1: 4F              LD      C,A                 
6AD2: 4F              LD      C,A                 
6AD3: 21 20 20        LD      HL,$2020            
6AD6: 20 49           JR      NZ,$6B21            ; {}
6AD8: 5E              LD      E,(HL)              
6AD9: 6D              LD      L,L                 
6ADA: 20 20           JR      NZ,$6AFC            ; {}
6ADC: 20 20           JR      NZ,$6AFE            ; {}
6ADE: 66              LD      H,(HL)              
6ADF: 69              LD      L,C                 
6AE0: 6E              LD      L,(HL)              
6AE1: 65              LD      H,L                 
6AE2: 2C              INC     L                   
6AE3: 20 61           JR      NZ,$6B46            ; {}
6AE5: 6E              LD      L,(HL)              
6AE6: 64              LD      H,H                 
6AE7: 20 79           JR      NZ,$6B62            ; {}
6AE9: 6F              LD      L,A                 
6AEA: 75              LD      (HL),L              
6AEB: 3F              CCF                         
6AEC: 21 FF 59        LD      HL,$59FF            
6AEF: 41              LD      B,C                 
6AF0: 48              LD      C,B                 
6AF1: 4F              LD      C,A                 
6AF2: 4F              LD      C,A                 
6AF3: 21 20 20        LD      HL,$2020            
6AF6: 49              LD      C,C                 
6AF7: 20 77           JR      NZ,$6B70            ; {}
6AF9: 6F              LD      L,A                 
6AFA: 72              LD      (HL),D              
6AFB: 6B              LD      L,E                 
6AFC: 65              LD      H,L                 
6AFD: 64              LD      H,H                 
6AFE: 74              LD      (HL),H              
6AFF: 6F              LD      L,A                 
6B00: 6F              LD      L,A                 
6B01: 20 68           JR      NZ,$6B6B            ; {}
6B03: 61              LD      H,C                 
6B04: 72              LD      (HL),D              
6B05: 64              LD      H,H                 
6B06: 20 61           JR      NZ,$6B69            ; {}
6B08: 6E              LD      L,(HL)              
6B09: 64              LD      H,H                 
6B0A: 20 6E           JR      NZ,$6B7A            ; {}
6B0C: 6F              LD      L,A                 
6B0D: 77              LD      (HL),A              
6B0E: 6D              LD      L,L                 
6B0F: 79              LD      A,C                 
6B10: 20 62           JR      NZ,$6B74            ; {}
6B12: 72              LD      (HL),D              
6B13: 6F              LD      L,A                 
6B14: 6F              LD      L,A                 
6B15: 6D              LD      L,L                 
6B16: 20 69           JR      NZ,$6B81            ; {}
6B18: 73              LD      (HL),E              
6B19: 20 77           JR      NZ,$6B92            ; {}
6B1B: 6F              LD      L,A                 
6B1C: 72              LD      (HL),D              
6B1D: 6E              LD      L,(HL)              
6B1E: 74              LD      (HL),H              
6B1F: 6F              LD      L,A                 
6B20: 20 74           JR      NZ,$6B96            ; {}
6B22: 68              LD      L,B                 
6B23: 65              LD      H,L                 
6B24: 20 68           JR      NZ,$6B8E            ; {}
6B26: 61              LD      H,C                 
6B27: 6E              LD      L,(HL)              
6B28: 64              LD      H,H                 
6B29: 6C              LD      L,H                 
6B2A: 65              LD      H,L                 
6B2B: 21 FF 59        LD      HL,$59FF            
6B2E: 41              LD      B,C                 
6B2F: 48              LD      C,B                 
6B30: 4F              LD      C,A                 
6B31: 4F              LD      C,A                 
6B32: 21 20 20        LD      HL,$2020            
6B35: 59              LD      E,C                 
6B36: 41              LD      B,C                 
6B37: 48              LD      C,B                 
6B38: 4F              LD      C,A                 
6B39: 4F              LD      C,A                 
6B3A: 21 20 20        LD      HL,$2020            
6B3D: 41              LD      B,C                 
6B3E: 20 6E           JR      NZ,$6BAE            ; {}
6B40: 65              LD      H,L                 
6B41: 77              LD      (HL),A              
6B42: 20 62           JR      NZ,$6BA6            ; {}
6B44: 72              LD      (HL),D              
6B45: 6F              LD      L,A                 
6B46: 6F              LD      L,A                 
6B47: 6D              LD      L,L                 
6B48: 3F              CCF                         
6B49: 21 20 20        LD      HL,$2020            
6B4C: 20 46           JR      NZ,$6B94            ; {}
6B4E: 6F              LD      L,A                 
6B4F: 72              LD      (HL),D              
6B50: 20 6D           JR      NZ,$6BBF            ; {}
6B52: 65              LD      H,L                 
6B53: 3F              CCF                         
6B54: 20 20           JR      NZ,$6B76            ; {}
6B56: 49              LD      C,C                 
6B57: 74              LD      (HL),H              
6B58: 20 69           JR      NZ,$6BC3            ; {}
6B5A: 73              LD      (HL),E              
6B5B: 2C              INC     L                   
6B5C: 20 69           JR      NZ,$6BC7            ; {}
6B5E: 73              LD      (HL),E              
6B5F: 6E              LD      L,(HL)              
6B60: 5E              LD      E,(HL)              
6B61: 74              LD      (HL),H              
6B62: 20 69           JR      NZ,$6BCD            ; {}
6B64: 74              LD      (HL),H              
6B65: 3F              CCF                         
6B66: 21 20 20        LD      HL,$2020            
6B69: 20 20           JR      NZ,$6B8B            ; {}
6B6B: 20 20           JR      NZ,$6B8D            ; {}
6B6D: 20 20           JR      NZ,$6B8F            ; {}
6B6F: 20 20           JR      NZ,$6B91            ; {}
6B71: 59              LD      E,C                 
6B72: 65              LD      H,L                 
6B73: 73              LD      (HL),E              
6B74: 20 20           JR      NZ,$6B96            ; {}
6B76: 4E              LD      C,(HL)              
6B77: 6F              LD      L,A                 
6B78: FE 4F           CP      $4F                 
6B7A: 6B              LD      L,E                 
6B7B: 61              LD      H,C                 
6B7C: 79              LD      A,C                 
6B7D: 21 20 20        LD      HL,$2020            
6B80: 49              LD      C,C                 
6B81: 6E              LD      L,(HL)              
6B82: 20 72           JR      NZ,$6BF6            ; {}
6B84: 65              LD      H,L                 
6B85: 74              LD      (HL),H              
6B86: 75              LD      (HL),L              
6B87: 72              LD      (HL),D              
6B88: 6E              LD      L,(HL)              
6B89: 79              LD      A,C                 
6B8A: 6F              LD      L,A                 
6B8B: 75              LD      (HL),L              
6B8C: 20 63           JR      NZ,$6BF1            ; {}
6B8E: 61              LD      H,C                 
6B8F: 6E              LD      L,(HL)              
6B90: 20 68           JR      NZ,$6BFA            ; {}
6B92: 61              LD      H,C                 
6B93: 76              HALT                        
6B94: 65              LD      H,L                 
6B95: 20 20           JR      NZ,$6BB7            ; {}
6B97: 20 20           JR      NZ,$6BB9            ; {}
6B99: 74              LD      (HL),H              
6B9A: 68              LD      L,B                 
6B9B: 69              LD      L,C                 
6B9C: 73              LD      (HL),E              
6B9D: 20 66           JR      NZ,$6C05            ; {}
6B9F: 69              LD      L,C                 
6BA0: 73              LD      (HL),E              
6BA1: 68              LD      L,B                 
6BA2: 69              LD      L,C                 
6BA3: 6E              LD      L,(HL)              
6BA4: 67              LD      H,A                 
6BA5: 20 20           JR      NZ,$6BC7            ; {}
6BA7: 20 20           JR      NZ,$6BC9            ; {}
6BA9: 68              LD      L,B                 
6BAA: 6F              LD      L,A                 
6BAB: 6F              LD      L,A                 
6BAC: 6B              LD      L,E                 
6BAD: 20 49           JR      NZ,$6BF8            ; {}
6BAF: 20 66           JR      NZ,$6C17            ; {}
6BB1: 6F              LD      L,A                 
6BB2: 75              LD      (HL),L              
6BB3: 6E              LD      L,(HL)              
6BB4: 64              LD      H,H                 
6BB5: 20 20           JR      NZ,$6BD7            ; {}
6BB7: 20 20           JR      NZ,$6BD9            ; {}
6BB9: 77              LD      (HL),A              
6BBA: 68              LD      L,B                 
6BBB: 65              LD      H,L                 
6BBC: 6E              LD      L,(HL)              
6BBD: 20 49           JR      NZ,$6C08            ; {}
6BBF: 20 73           JR      NZ,$6C34            ; {}
6BC1: 77              LD      (HL),A              
6BC2: 65              LD      H,L                 
6BC3: 70              LD      (HL),B              
6BC4: 74              LD      (HL),H              
6BC5: 20 62           JR      NZ,$6C29            ; {}
6BC7: 79              LD      A,C                 
6BC8: 20 74           JR      NZ,$6C3E            ; {}
6BCA: 68              LD      L,B                 
6BCB: 65              LD      H,L                 
6BCC: 20 72           JR      NZ,$6C40            ; {}
6BCE: 69              LD      L,C                 
6BCF: 76              HALT                        
6BD0: 65              LD      H,L                 
6BD1: 72              LD      (HL),D              
6BD2: 20 62           JR      NZ,$6C36            ; {}
6BD4: 61              LD      H,C                 
6BD5: 6E              LD      L,(HL)              
6BD6: 6B              LD      L,E                 
6BD7: 21 FF 59        LD      HL,$59FF            
6BDA: 6F              LD      L,A                 
6BDB: 75              LD      (HL),L              
6BDC: 20 65           JR      NZ,$6C43            ; {}
6BDE: 78              LD      A,B                 
6BDF: 63              LD      H,E                 
6BE0: 68              LD      L,B                 
6BE1: 61              LD      H,C                 
6BE2: 6E              LD      L,(HL)              
6BE3: 67              LD      H,A                 
6BE4: 65              LD      H,L                 
6BE5: 64              LD      H,H                 
6BE6: 20 E8           JR      NZ,$6BD0            ; {}
6BE8: 20 66           JR      NZ,$6C50            ; {}
6BEA: 6F              LD      L,A                 
6BEB: 72              LD      (HL),D              
6BEC: 20 74           JR      NZ,$6C62            ; {}
6BEE: 68              LD      L,B                 
6BEF: 65              LD      H,L                 
6BF0: 20 66           JR      NZ,$6C58            ; {}
6BF2: 69              LD      L,C                 
6BF3: 73              LD      (HL),E              
6BF4: 68              LD      L,B                 
6BF5: 69              LD      L,C                 
6BF6: 6E              LD      L,(HL)              
6BF7: 67              LD      H,A                 
6BF8: 20 68           JR      NZ,$6C62            ; {}
6BFA: 6F              LD      L,A                 
6BFB: 6F              LD      L,A                 
6BFC: 6B              LD      L,E                 
6BFD: 20 E9           JR      NZ,$6BE8            ; {}
6BFF: 21 20 20        LD      HL,$2020            
6C02: 57              LD      D,A                 
6C03: 68              LD      L,B                 
6C04: 61              LD      H,C                 
6C05: 74              LD      (HL),H              
6C06: 20 20           JR      NZ,$6C28            ; {}
6C08: 20 77           JR      NZ,$6C81            ; {}
6C0A: 69              LD      L,C                 
6C0B: 6C              LD      L,H                 
6C0C: 6C              LD      L,H                 
6C0D: 20 74           JR      NZ,$6C83            ; {}
6C0F: 68              LD      L,B                 
6C10: 65              LD      H,L                 
6C11: 20 66           JR      NZ,$6C79            ; {}
6C13: 69              LD      L,C                 
6C14: 73              LD      (HL),E              
6C15: 68              LD      L,B                 
6C16: 69              LD      L,C                 
6C17: 6E              LD      L,(HL)              
6C18: 67              LD      H,A                 
6C19: 68              LD      L,B                 
6C1A: 6F              LD      L,A                 
6C1B: 6F              LD      L,A                 
6C1C: 6B              LD      L,E                 
6C1D: 20 62           JR      NZ,$6C81            ; {}
6C1F: 65              LD      H,L                 
6C20: 63              LD      H,E                 
6C21: 6F              LD      L,A                 
6C22: 6D              LD      L,L                 
6C23: 65              LD      H,L                 
6C24: 3F              CCF                         
6C25: FF              RST     0X38                
6C26: 59              LD      E,C                 
6C27: 41              LD      B,C                 
6C28: 48              LD      C,B                 
6C29: 4F              LD      C,A                 
6C2A: 4F              LD      C,A                 
6C2B: 21 20 20        LD      HL,$2020            
6C2E: 41              LD      B,C                 
6C2F: 20 6E           JR      NZ,$6C9F            ; {}
6C31: 65              LD      H,L                 
6C32: 77              LD      (HL),A              
6C33: 20 20           JR      NZ,$6C55            ; {}
6C35: 20 62           JR      NZ,$6C99            ; {}
6C37: 72              LD      (HL),D              
6C38: 6F              LD      L,A                 
6C39: 6F              LD      L,A                 
6C3A: 6D              LD      L,L                 
6C3B: 21 20 20        LD      HL,$2020            
6C3E: 53              LD      D,E                 
6C3F: 75              LD      (HL),L              
6C40: 70              LD      (HL),B              
6C41: 65              LD      H,L                 
6C42: 72              LD      (HL),D              
6C43: 62              LD      H,D                 
6C44: 21 FF 4B        LD      HL,$4BFF            
6C47: 69              LD      L,C                 
6C48: 69              LD      L,C                 
6C49: 69              LD      L,C                 
6C4A: 6B              LD      L,E                 
6C4B: 69              LD      L,C                 
6C4C: 21 20 20        LD      HL,$2020            
6C4F: 57              LD      D,A                 
6C50: 68              LD      L,B                 
6C51: 61              LD      H,C                 
6C52: 74              LD      (HL),H              
6C53: 3F              CCF                         
6C54: 21 20 41        LD      HL,$4120            
6C57: 6C              LD      L,H                 
6C58: 6C              LD      L,H                 
6C59: 20 72           JR      NZ,$6CCD            ; {}
6C5B: 69              LD      L,C                 
6C5C: 67              LD      H,A                 
6C5D: 68              LD      L,B                 
6C5E: 74              LD      (HL),H              
6C5F: 2C              INC     L                   
6C60: 20 6D           JR      NZ,$6CCF            ; {}
6C62: 75              LD      (HL),L              
6C63: 74              LD      (HL),H              
6C64: 74              LD      (HL),H              
6C65: 21 4C 65        LD      HL,$654C            
6C68: 74              LD      (HL),H              
6C69: 5E              LD      E,(HL)              
6C6A: 73              LD      (HL),E              
6C6B: 20 62           JR      NZ,$6CCF            ; {}
6C6D: 61              LD      H,C                 
6C6E: 74              LD      (HL),H              
6C6F: 74              LD      (HL),H              
6C70: 6C              LD      L,H                 
6C71: 65              LD      H,L                 
6C72: 21 21 FF        LD      HL,$FF21            
6C75: 43              LD      B,E                 
6C76: 68              LD      L,B                 
6C77: 69              LD      L,C                 
6C78: 2D              DEC     L                   
6C79: 6B              LD      L,E                 
6C7A: 69              LD      L,C                 
6C7B: 69              LD      L,C                 
6C7C: 74              LD      (HL),H              
6C7D: 61              LD      H,C                 
6C7E: 21 20 43        LD      HL,$4320            
6C81: 68              LD      L,B                 
6C82: 69              LD      L,C                 
6C83: 2D              DEC     L                   
6C84: 20 6B           JR      NZ,$6CF1            ; {}
6C86: 69              LD      L,C                 
6C87: 69              LD      L,C                 
6C88: 74              LD      (HL),H              
6C89: 61              LD      H,C                 
6C8A: 21 20 20        LD      HL,$2020            
6C8D: 4B              LD      C,E                 
6C8E: 69              LD      L,C                 
6C8F: 6B              LD      L,E                 
6C90: 69              LD      L,C                 
6C91: 20 74           JR      NZ,$6D07            ; {}
6C93: 68              LD      L,B                 
6C94: 65              LD      H,L                 
6C95: 6D              LD      L,L                 
6C96: 6F              LD      L,A                 
6C97: 6E              LD      L,(HL)              
6C98: 6B              LD      L,E                 
6C99: 65              LD      H,L                 
6C9A: 79              LD      A,C                 
6C9B: 21 20 20        LD      HL,$2020            
6C9E: 48              LD      C,B                 
6C9F: 75              LD      (HL),L              
6CA0: 6E              LD      L,(HL)              
6CA1: 67              LD      H,A                 
6CA2: 72              LD      (HL),D              
6CA3: 79              LD      A,C                 
6CA4: 21 4B 69        LD      HL,$694B            
6CA7: 6B              LD      L,E                 
6CA8: 69              LD      L,C                 
6CA9: 20 74           JR      NZ,$6D1F            ; {}
6CAB: 68              LD      L,B                 
6CAC: 65              LD      H,L                 
6CAD: 20 6D           JR      NZ,$6D1C            ; {}
6CAF: 6F              LD      L,A                 
6CB0: 6E              LD      L,(HL)              
6CB1: 6B              LD      L,E                 
6CB2: 65              LD      H,L                 
6CB3: 79              LD      A,C                 
6CB4: 21 FF 20        LD      HL,$20FF            
6CB7: 20 20           JR      NZ,$6CD9            ; {}
6CB9: 20 E3           JR      NZ,$6C9E            ; {}
6CBB: 21 20 20        LD      HL,$2020            
6CBE: 20 20           JR      NZ,$6CE0            ; {}
6CC0: E3                              
6CC1: 21 20 20        LD      HL,$2020            
6CC4: 20 20           JR      NZ,$6CE6            ; {}
6CC6: 4F              LD      C,A                 
6CC7: 6F              LD      L,A                 
6CC8: 6F              LD      L,A                 
6CC9: 68              LD      L,B                 
6CCA: 21 20 4F        LD      HL,$4F20            
6CCD: 6F              LD      L,A                 
6CCE: 68              LD      L,B                 
6CCF: 21 20 4B        LD      HL,$4B20            
6CD2: 69              LD      L,C                 
6CD3: 6B              LD      L,E                 
6CD4: 69              LD      L,C                 
6CD5: 21 4D 6F        LD      HL,$6F4D            
6CD8: 6E              LD      L,(HL)              
6CD9: 6B              LD      L,E                 
6CDA: 65              LD      H,L                 
6CDB: 65              LD      H,L                 
6CDC: 73              LD      (HL),E              
6CDD: 21 20 20        LD      HL,$2020            
6CE0: 43              LD      B,E                 
6CE1: 6F              LD      L,A                 
6CE2: 6D              LD      L,L                 
6CE3: 65              LD      H,L                 
6CE4: 21 20 52        LD      HL,$5220            
6CE7: 65              LD      H,L                 
6CE8: 70              LD      (HL),B              
6CE9: 61              LD      H,C                 
6CEA: 79              LD      A,C                 
6CEB: 20 68           JR      NZ,$6D55            ; {}
6CED: 69              LD      L,C                 
6CEE: 6D              LD      L,L                 
6CEF: 21 20 4B        LD      HL,$4B20            
6CF2: 69              LD      L,C                 
6CF3: 6B              LD      L,E                 
6CF4: 69              LD      L,C                 
6CF5: 21 FF 4D        LD      HL,$4DFF            
6CF8: 6F              LD      L,A                 
6CF9: 6E              LD      L,(HL)              
6CFA: 6B              LD      L,E                 
6CFB: 65              LD      H,L                 
6CFC: 79              LD      A,C                 
6CFD: 20 62           JR      NZ,$6D61            ; {}
6CFF: 75              LD      (HL),L              
6D00: 73              LD      (HL),E              
6D01: 69              LD      L,C                 
6D02: 6E              LD      L,(HL)              
6D03: 65              LD      H,L                 
6D04: 73              LD      (HL),E              
6D05: 73              LD      (HL),E              
6D06: 21 44 6F        LD      HL,$6F44            
6D09: 6E              LD      L,(HL)              
6D0A: 65              LD      H,L                 
6D0B: 21 20 20        LD      HL,$2020            
6D0E: 42              LD      B,D                 
6D0F: 79              LD      A,C                 
6D10: 65              LD      H,L                 
6D11: 20 62           JR      NZ,$6D75            ; {}
6D13: 79              LD      A,C                 
6D14: 65              LD      H,L                 
6D15: 21 20 4F        LD      HL,$4F20            
6D18: 6F              LD      L,A                 
6D19: 6F              LD      L,A                 
6D1A: 68              LD      L,B                 
6D1B: 21 20 20        LD      HL,$2020            
6D1E: 4B              LD      C,E                 
6D1F: 69              LD      L,C                 
6D20: 6B              LD      L,E                 
6D21: 69              LD      L,C                 
6D22: 21 FF 59        LD      HL,$59FF            
6D25: 6F              LD      L,A                 
6D26: 75              LD      (HL),L              
6D27: 20 66           JR      NZ,$6D8F            ; {}
6D29: 6F              LD      L,A                 
6D2A: 75              LD      (HL),L              
6D2B: 6E              LD      L,(HL)              
6D2C: 64              LD      H,H                 
6D2D: 20 61           JR      NZ,$6D90            ; {}
6D2F: 20 20           JR      NZ,$6D51            ; {}
6D31: 20 20           JR      NZ,$6D53            ; {}
6D33: 20 73           JR      NZ,$6DA8            ; {}
6D35: 74              LD      (HL),H              
6D36: 69              LD      L,C                 
6D37: 63              LD      H,E                 
6D38: 6B              LD      L,E                 
6D39: 20 61           JR      NZ,$6D9C            ; {}
6D3B: 20 6D           JR      NZ,$6DAA            ; {}
6D3D: 6F              LD      L,A                 
6D3E: 6E              LD      L,(HL)              
6D3F: 6B              LD      L,E                 
6D40: 65              LD      H,L                 
6D41: 79              LD      A,C                 
6D42: 20 20           JR      NZ,$6D64            ; {}
6D44: 6C              LD      L,H                 
6D45: 65              LD      H,L                 
6D46: 66              LD      H,(HL)              
6D47: 74              LD      (HL),H              
6D48: 20 62           JR      NZ,$6DAC            ; {}
6D4A: 65              LD      H,L                 
6D4B: 68              LD      L,B                 
6D4C: 69              LD      L,C                 
6D4D: 6E              LD      L,(HL)              
6D4E: 64              LD      H,H                 
6D4F: 2E 2E           LD      L,$2E               
6D51: 2E 20           LD      L,$20               
6D53: 20 59           JR      NZ,$6DAE            ; {}
6D55: 6F              LD      L,A                 
6D56: 75              LD      (HL),L              
6D57: 20 74           JR      NZ,$6DCD            ; {}
6D59: 61              LD      H,C                 
6D5A: 6B              LD      L,E                 
6D5B: 65              LD      H,L                 
6D5C: 20 69           JR      NZ,$6DC7            ; {}
6D5E: 74              LD      (HL),H              
6D5F: 21 FF 20        LD      HL,$20FF            
6D62: 20 20           JR      NZ,$6D84            ; {}
6D64: 20 E3           JR      NZ,$6D49            ; {}
6D66: 21 20 20        LD      HL,$2020            
6D69: 20 20           JR      NZ,$6D8B            ; {}
6D6B: E3                              
6D6C: 21 20 20        LD      HL,$2020            
6D6F: 20 20           JR      NZ,$6D91            ; {}
6D71: 20 20           JR      NZ,$6D93            ; {}
6D73: 4F              LD      C,A                 
6D74: 6F              LD      L,A                 
6D75: 6F              LD      L,A                 
6D76: 68              LD      L,B                 
6D77: 21 20 20        LD      HL,$2020            
6D7A: 4F              LD      C,A                 
6D7B: 6F              LD      L,A                 
6D7C: 6F              LD      L,A                 
6D7D: 68              LD      L,B                 
6D7E: 21 20 20        LD      HL,$2020            
6D81: 20 47           JR      NZ,$6DCA            ; {}
6D83: 69              LD      L,C                 
6D84: 76              HALT                        
6D85: 65              LD      H,L                 
6D86: 20 74           JR      NZ,$6DFC            ; {}
6D88: 6F              LD      L,A                 
6D89: 20 4B           JR      NZ,$6DD6            ; {}
6D8B: 69              LD      L,C                 
6D8C: 6B              LD      L,E                 
6D8D: 69              LD      L,C                 
6D8E: 21 3F 20        LD      HL,$203F            
6D91: 20 20           JR      NZ,$6DB3            ; {}
6D93: 20 20           JR      NZ,$6DB5            ; {}
6D95: 59              LD      E,C                 
6D96: 65              LD      H,L                 
6D97: 73              LD      (HL),E              
6D98: 20 20           JR      NZ,$6DBA            ; {}
6D9A: 4E              LD      C,(HL)              
6D9B: 6F              LD      L,A                 
6D9C: 21 FE 59        LD      HL,$59FE            
6D9F: 6F              LD      L,A                 
6DA0: 75              LD      (HL),L              
6DA1: 20 64           JR      NZ,$6E07            ; {}
6DA3: 6F              LD      L,A                 
6DA4: 6E              LD      L,(HL)              
6DA5: 5E              LD      E,(HL)              
6DA6: 74              LD      (HL),H              
6DA7: 20 6B           JR      NZ,$6E14            ; {}
6DA9: 6E              LD      L,(HL)              
6DAA: 6F              LD      L,A                 
6DAB: 77              LD      (HL),A              
6DAC: 20 20           JR      NZ,$6DCE            ; {}
6DAE: 74              LD      (HL),H              
6DAF: 68              LD      L,B                 
6DB0: 65              LD      H,L                 
6DB1: 20 70           JR      NZ,$6E23            ; {}
6DB3: 72              LD      (HL),D              
6DB4: 6F              LD      L,A                 
6DB5: 70              LD      (HL),B              
6DB6: 65              LD      H,L                 
6DB7: 72              LD      (HL),D              
6DB8: 20 20           JR      NZ,$6DDA            ; {}
6DBA: 20 20           JR      NZ,$6DDC            ; {}
6DBC: 20 20           JR      NZ,$6DDE            ; {}
6DBE: 65              LD      H,L                 
6DBF: 74              LD      (HL),H              
6DC0: 69              LD      L,C                 
6DC1: 71              LD      (HL),C              
6DC2: 75              LD      (HL),L              
6DC3: 65              LD      H,L                 
6DC4: 74              LD      (HL),H              
6DC5: 74              LD      (HL),H              
6DC6: 65              LD      H,L                 
6DC7: 20 77           JR      NZ,$6E40            ; {}
6DC9: 68              LD      L,B                 
6DCA: 65              LD      H,L                 
6DCB: 6E              LD      L,(HL)              
6DCC: 20 20           JR      NZ,$6DEE            ; {}
6DCE: 64              LD      H,H                 
6DCF: 65              LD      H,L                 
6DD0: 61              LD      H,C                 
6DD1: 6C              LD      L,H                 
6DD2: 69              LD      L,C                 
6DD3: 6E              LD      L,(HL)              
6DD4: 67              LD      H,A                 
6DD5: 20 77           JR      NZ,$6E4E            ; {}
6DD7: 69              LD      L,C                 
6DD8: 74              LD      (HL),H              
6DD9: 68              LD      L,B                 
6DDA: 20 61           JR      NZ,$6E3D            ; {}
6DDC: 20 20           JR      NZ,$6DFE            ; {}
6DDE: 6C              LD      L,H                 
6DDF: 61              LD      H,C                 
6DE0: 64              LD      H,H                 
6DE1: 79              LD      A,C                 
6DE2: 2C              INC     L                   
6DE3: 20 64           JR      NZ,$6E49            ; {}
6DE5: 6F              LD      L,A                 
6DE6: 20 79           JR      NZ,$6E61            ; {}
6DE8: 6F              LD      L,A                 
6DE9: 75              LD      (HL),L              
6DEA: 3F              CCF                         
6DEB: 20 20           JR      NZ,$6E0D            ; {}
6DED: 20 59           JR      NZ,$6E48            ; {}
6DEF: 6F              LD      L,A                 
6DF0: 75              LD      (HL),L              
6DF1: 20 73           JR      NZ,$6E66            ; {}
6DF3: 68              LD      L,B                 
6DF4: 6F              LD      L,A                 
6DF5: 75              LD      (HL),L              
6DF6: 6C              LD      L,H                 
6DF7: 64              LD      H,H                 
6DF8: 20 68           JR      NZ,$6E62            ; {}
6DFA: 61              LD      H,C                 
6DFB: 76              HALT                        
6DFC: 65              LD      H,L                 
6DFD: 20 62           JR      NZ,$6E61            ; {}
6DFF: 72              LD      (HL),D              
6E00: 6F              LD      L,A                 
6E01: 75              LD      (HL),L              
6E02: 67              LD      H,A                 
6E03: 68              LD      L,B                 
6E04: 74              LD      (HL),H              
6E05: 20 66           JR      NZ,$6E6D            ; {}
6E07: 6C              LD      L,H                 
6E08: 6F              LD      L,A                 
6E09: 77              LD      (HL),A              
6E0A: 65              LD      H,L                 
6E0B: 72              LD      (HL),D              
6E0C: 73              LD      (HL),E              
6E0D: 20 6F           JR      NZ,$6E7E            ; {}
6E0F: 72              LD      (HL),D              
6E10: 20 73           JR      NZ,$6E85            ; {}
6E12: 6F              LD      L,A                 
6E13: 6D              LD      L,L                 
6E14: 65              LD      H,L                 
6E15: 74              LD      (HL),H              
6E16: 68              LD      L,B                 
6E17: 69              LD      L,C                 
6E18: 6E              LD      L,(HL)              
6E19: 67              LD      H,A                 
6E1A: 2C              INC     L                   
6E1B: 20 20           JR      NZ,$6E3D            ; {}
6E1D: 20 74           JR      NZ,$6E93            ; {}
6E1F: 68              LD      L,B                 
6E20: 65              LD      H,L                 
6E21: 6E              LD      L,(HL)              
6E22: 20 49           JR      NZ,$6E6D            ; {}
6E24: 20 6D           JR      NZ,$6E93            ; {}
6E26: 69              LD      L,C                 
6E27: 67              LD      H,A                 
6E28: 68              LD      L,B                 
6E29: 74              LD      (HL),H              
6E2A: 20 62           JR      NZ,$6E8E            ; {}
6E2C: 65              LD      H,L                 
6E2D: 20 6D           JR      NZ,$6E9C            ; {}
6E2F: 6F              LD      L,A                 
6E30: 72              LD      (HL),D              
6E31: 65              LD      H,L                 
6E32: 20 69           JR      NZ,$6E9D            ; {}
6E34: 6E              LD      L,(HL)              
6E35: 63              LD      H,E                 
6E36: 6C              LD      L,H                 
6E37: 69              LD      L,C                 
6E38: 6E              LD      L,(HL)              
6E39: 65              LD      H,L                 
6E3A: 64              LD      H,H                 
6E3B: 20 74           JR      NZ,$6EB1            ; {}
6E3D: 6F              LD      L,A                 
6E3E: 74              LD      (HL),H              
6E3F: 61              LD      H,C                 
6E40: 6C              LD      L,H                 
6E41: 6B              LD      L,E                 
6E42: 20 77           JR      NZ,$6EBB            ; {}
6E44: 69              LD      L,C                 
6E45: 74              LD      (HL),H              
6E46: 68              LD      L,B                 
6E47: 20 79           JR      NZ,$6EC2            ; {}
6E49: 6F              LD      L,A                 
6E4A: 75              LD      (HL),L              
6E4B: 2E 2E           LD      L,$2E               
6E4D: 2E 4F           LD      L,$4F               
6E4F: 68              LD      L,B                 
6E50: 20 79           JR      NZ,$6ECB            ; {}
6E52: 65              LD      H,L                 
6E53: 73              LD      (HL),E              
6E54: 2C              INC     L                   
6E55: 20 69           JR      NZ,$6EC0            ; {}
6E57: 6E              LD      L,(HL)              
6E58: 20 6D           JR      NZ,$6EC7            ; {}
6E5A: 79              LD      A,C                 
6E5B: 20 20           JR      NZ,$6E7D            ; {}
6E5D: 20 63           JR      NZ,$6EC2            ; {}
6E5F: 61              LD      H,C                 
6E60: 73              LD      (HL),E              
6E61: 65              LD      H,L                 
6E62: 2C              INC     L                   
6E63: 20 68           JR      NZ,$6ECD            ; {}
6E65: 69              LD      L,C                 
6E66: 62              LD      H,D                 
6E67: 69              LD      L,C                 
6E68: 73              LD      (HL),E              
6E69: 63              LD      H,E                 
6E6A: 75              LD      (HL),L              
6E6B: 73              LD      (HL),E              
6E6C: 20 20           JR      NZ,$6E8E            ; {}
6E6E: 61              LD      H,C                 
6E6F: 72              LD      (HL),D              
6E70: 65              LD      H,L                 
6E71: 20 62           JR      NZ,$6ED5            ; {}
6E73: 65              LD      H,L                 
6E74: 73              LD      (HL),E              
6E75: 74              LD      (HL),H              
6E76: 2E 2E           LD      L,$2E               
6E78: 2E FF           LD      L,$FF               
6E7A: 4F              LD      C,A                 
6E7B: 68              LD      L,B                 
6E7C: 2C              INC     L                   
6E7D: 20 79           JR      NZ,$6EF8            ; {}
6E7F: 6F              LD      L,A                 
6E80: 75              LD      (HL),L              
6E81: 20 62           JR      NZ,$6EE5            ; {}
6E83: 72              LD      (HL),D              
6E84: 6F              LD      L,A                 
6E85: 75              LD      (HL),L              
6E86: 67              LD      H,A                 
6E87: 68              LD      L,B                 
6E88: 74              LD      (HL),H              
6E89: 20 6D           JR      NZ,$6EF8            ; {}
6E8B: 65              LD      H,L                 
6E8C: 20 61           JR      NZ,$6EEF            ; {}
6E8E: 20 68           JR      NZ,$6EF8            ; {}
6E90: 69              LD      L,C                 
6E91: 62              LD      H,D                 
6E92: 69              LD      L,C                 
6E93: 73              LD      (HL),E              
6E94: 63              LD      H,E                 
6E95: 75              LD      (HL),L              
6E96: 73              LD      (HL),E              
6E97: 21 20 20        LD      HL,$2020            
6E9A: 48              LD      C,B                 
6E9B: 6F              LD      L,A                 
6E9C: 77              LD      (HL),A              
6E9D: 20 73           JR      NZ,$6F12            ; {}
6E9F: 77              LD      (HL),A              
6EA0: 65              LD      H,L                 
6EA1: 65              LD      H,L                 
6EA2: 74              LD      (HL),H              
6EA3: 21 20 57        LD      HL,$5720            
6EA6: 65              LD      H,L                 
6EA7: 6C              LD      L,H                 
6EA8: 6C              LD      L,H                 
6EA9: 2C              INC     L                   
6EAA: 73              LD      (HL),E              
6EAB: 69              LD      L,C                 
6EAC: 6E              LD      L,(HL)              
6EAD: 63              LD      H,E                 
6EAE: 65              LD      H,L                 
6EAF: 20 79           JR      NZ,$6F2A            ; {}
6EB1: 6F              LD      L,A                 
6EB2: 75              LD      (HL),L              
6EB3: 20 61           JR      NZ,$6F16            ; {}
6EB5: 72              LD      (HL),D              
6EB6: 65              LD      H,L                 
6EB7: 20 20           JR      NZ,$6ED9            ; {}
6EB9: 20 73           JR      NZ,$6F2E            ; {}
6EBB: 75              LD      (HL),L              
6EBC: 63              LD      H,E                 
6EBD: 68              LD      L,B                 
6EBE: 20 61           JR      NZ,$6F21            ; {}
6EC0: 20 67           JR      NZ,$6F29            ; {}
6EC2: 65              LD      H,L                 
6EC3: 6E              LD      L,(HL)              
6EC4: 74              LD      (HL),H              
6EC5: 6C              LD      L,H                 
6EC6: 65              LD      H,L                 
6EC7: 6D              LD      L,L                 
6EC8: 61              LD      H,C                 
6EC9: 6E              LD      L,(HL)              
6ECA: 49              LD      C,C                 
6ECB: 20 68           JR      NZ,$6F35            ; {}
6ECD: 61              LD      H,C                 
6ECE: 76              HALT                        
6ECF: 65              LD      H,L                 
6ED0: 20 61           JR      NZ,$6F33            ; {}
6ED2: 20 72           JR      NZ,$6F46            ; {}
6ED4: 65              LD      H,L                 
6ED5: 71              LD      (HL),C              
6ED6: 75              LD      (HL),L              
6ED7: 65              LD      H,L                 
6ED8: 73              LD      (HL),E              
6ED9: 74              LD      (HL),H              
6EDA: 74              LD      (HL),H              
6EDB: 6F              LD      L,A                 
6EDC: 20 6D           JR      NZ,$6F4B            ; {}
6EDE: 61              LD      H,C                 
6EDF: 6B              LD      L,E                 
6EE0: 65              LD      H,L                 
6EE1: 20 6F           JR      NZ,$6F52            ; {}
6EE3: 66              LD      H,(HL)              
6EE4: 20 79           JR      NZ,$6F5F            ; {}
6EE6: 6F              LD      L,A                 
6EE7: 75              LD      (HL),L              
6EE8: 2E 20           LD      L,$20               
6EEA: 57              LD      D,A                 
6EEB: 69              LD      L,C                 
6EEC: 6C              LD      L,H                 
6EED: 6C              LD      L,H                 
6EEE: 20 79           JR      NZ,$6F69            ; {}
6EF0: 6F              LD      L,A                 
6EF1: 75              LD      (HL),L              
6EF2: 20 6C           JR      NZ,$6F60            ; {}
6EF4: 69              LD      L,C                 
6EF5: 73              LD      (HL),E              
6EF6: 74              LD      (HL),H              
6EF7: 65              LD      H,L                 
6EF8: 6E              LD      L,(HL)              
6EF9: 3F              CCF                         
6EFA: 20 20           JR      NZ,$6F1C            ; {}
6EFC: 20 20           JR      NZ,$6F1E            ; {}
6EFE: 59              LD      E,C                 
6EFF: 65              LD      H,L                 
6F00: 73              LD      (HL),E              
6F01: 20 20           JR      NZ,$6F23            ; {}
6F03: 4E              LD      C,(HL)              
6F04: 6F              LD      L,A                 
6F05: FE 49           CP      $49                 
6F07: 20 77           JR      NZ,$6F80            ; {}
6F09: 6F              LD      L,A                 
6F0A: 75              LD      (HL),L              
6F0B: 6C              LD      L,H                 
6F0C: 64              LD      H,H                 
6F0D: 20 6C           JR      NZ,$6F7B            ; {}
6F0F: 69              LD      L,C                 
6F10: 6B              LD      L,E                 
6F11: 65              LD      H,L                 
6F12: 20 79           JR      NZ,$6F8D            ; {}
6F14: 6F              LD      L,A                 
6F15: 75              LD      (HL),L              
6F16: 74              LD      (HL),H              
6F17: 6F              LD      L,A                 
6F18: 20 74           JR      NZ,$6F8E            ; {}
6F1A: 61              LD      H,C                 
6F1B: 6B              LD      L,E                 
6F1C: 65              LD      H,L                 
6F1D: 20 74           JR      NZ,$6F93            ; {}
6F1F: 68              LD      L,B                 
6F20: 69              LD      L,C                 
6F21: 73              LD      (HL),E              
6F22: 20 20           JR      NZ,$6F44            ; {}
6F24: 20 20           JR      NZ,$6F46            ; {}
6F26: 6C              LD      L,H                 
6F27: 65              LD      H,L                 
6F28: 74              LD      (HL),H              
6F29: 74              LD      (HL),H              
6F2A: 65              LD      H,L                 
6F2B: 72              LD      (HL),D              
6F2C: 20 74           JR      NZ,$6FA2            ; {}
6F2E: 6F              LD      L,A                 
6F2F: 20 61           JR      NZ,$6F92            ; {}
6F31: 20 4D           JR      NZ,$6F80            ; {}
6F33: 72              LD      (HL),D              
6F34: 2E 20           LD      L,$20               
6F36: 57              LD      D,A                 
6F37: 72              LD      (HL),D              
6F38: 69              LD      L,C                 
6F39: 74              LD      (HL),H              
6F3A: 65              LD      H,L                 
6F3B: 20 77           JR      NZ,$6FB4            ; {}
6F3D: 68              LD      L,B                 
6F3E: 6F              LD      L,A                 
6F3F: 20 6C           JR      NZ,$6FAD            ; {}
6F41: 69              LD      L,C                 
6F42: 76              HALT                        
6F43: 65              LD      H,L                 
6F44: 73              LD      (HL),E              
6F45: 20 6F           JR      NZ,$6FB6            ; {}
6F47: 6E              LD      L,(HL)              
6F48: 20 74           JR      NZ,$6FBE            ; {}
6F4A: 68              LD      L,B                 
6F4B: 65              LD      H,L                 
6F4C: 20 62           JR      NZ,$6FB0            ; {}
6F4E: 6F              LD      L,A                 
6F4F: 72              LD      (HL),D              
6F50: 64              LD      H,H                 
6F51: 65              LD      H,L                 
6F52: 72              LD      (HL),D              
6F53: 20 6F           JR      NZ,$6FC4            ; {}
6F55: 66              LD      H,(HL)              
6F56: 74              LD      (HL),H              
6F57: 68              LD      L,B                 
6F58: 65              LD      H,L                 
6F59: 20 4D           JR      NZ,$6FA8            ; {}
6F5B: 79              LD      A,C                 
6F5C: 73              LD      (HL),E              
6F5D: 74              LD      (HL),H              
6F5E: 65              LD      H,L                 
6F5F: 72              LD      (HL),D              
6F60: 69              LD      L,C                 
6F61: 6F              LD      L,A                 
6F62: 75              LD      (HL),L              
6F63: 73              LD      (HL),E              
6F64: 20 20           JR      NZ,$6F86            ; {}
6F66: 46              LD      B,(HL)              
6F67: 6F              LD      L,A                 
6F68: 72              LD      (HL),D              
6F69: 65              LD      H,L                 
6F6A: 73              LD      (HL),E              
6F6B: 74              LD      (HL),H              
6F6C: 2C              INC     L                   
6F6D: 20 70           JR      NZ,$6FDF            ; {}
6F6F: 6C              LD      L,H                 
6F70: 65              LD      H,L                 
6F71: 61              LD      H,C                 
6F72: 73              LD      (HL),E              
6F73: 65              LD      H,L                 
6F74: 21 FF 2E        LD      HL,$2EFF            
6F77: 2E 2E           LD      L,$2E               
6F79: 49              LD      C,C                 
6F7A: 73              LD      (HL),E              
6F7B: 20 74           JR      NZ,$6FF1            ; {}
6F7D: 68              LD      L,B                 
6F7E: 61              LD      H,C                 
6F7F: 74              LD      (HL),H              
6F80: 20 73           JR      NZ,$6FF5            ; {}
6F82: 6F              LD      L,A                 
6F83: 3F              CCF                         
6F84: 20 20           JR      NZ,$6FA6            ; {}
6F86: 41              LD      B,C                 
6F87: 6E              LD      L,(HL)              
6F88: 64              LD      H,H                 
6F89: 20 49           JR      NZ,$6FD4            ; {}
6F8B: 20 74           JR      NZ,$7001            ; {}
6F8D: 68              LD      L,B                 
6F8E: 6F              LD      L,A                 
6F8F: 75              LD      (HL),L              
6F90: 67              LD      H,A                 
6F91: 68              LD      L,B                 
6F92: 74              LD      (HL),H              
6F93: 20 20           JR      NZ,$6FB5            ; {}
6F95: 20 79           JR      NZ,$7010            ; {}
6F97: 6F              LD      L,A                 
6F98: 75              LD      (HL),L              
6F99: 20 77           JR      NZ,$7012            ; {}
6F9B: 65              LD      H,L                 
6F9C: 72              LD      (HL),D              
6F9D: 65              LD      H,L                 
6F9E: 20 61           JR      NZ,$7001            ; {}
6FA0: 20 20           JR      NZ,$6FC2            ; {}
6FA2: 20 20           JR      NZ,$6FC4            ; {}
6FA4: 20 20           JR      NZ,$6FC6            ; {}
6FA6: 67              LD      H,A                 
6FA7: 65              LD      H,L                 
6FA8: 6E              LD      L,(HL)              
6FA9: 74              LD      (HL),H              
6FAA: 6C              LD      L,H                 
6FAB: 65              LD      H,L                 
6FAC: 6D              LD      L,L                 
6FAD: 61              LD      H,C                 
6FAE: 6E              LD      L,(HL)              
6FAF: 2E 2E           LD      L,$2E               
6FB1: 2E FF           LD      L,$FF               
6FB3: 59              LD      E,C                 
6FB4: 6F              LD      L,A                 
6FB5: 75              LD      (HL),L              
6FB6: 20 74           JR      NZ,$702C            ; {}
6FB8: 72              LD      (HL),D              
6FB9: 61              LD      H,C                 
6FBA: 64              LD      H,H                 
6FBB: 65              LD      H,L                 
6FBC: 64              LD      H,H                 
6FBD: 20 E7           JR      NZ,$6FA6            ; {}
6FBF: 20 66           JR      NZ,$7027            ; {}
6FC1: 6F              LD      L,A                 
6FC2: 72              LD      (HL),D              
6FC3: 61              LD      H,C                 
6FC4: 20 67           JR      NZ,$702D            ; {}
6FC6: 6F              LD      L,A                 
6FC7: 61              LD      H,C                 
6FC8: 74              LD      (HL),H              
6FC9: 5E              LD      E,(HL)              
6FCA: 73              LD      (HL),E              
6FCB: 20 6C           JR      NZ,$7039            ; {}
6FCD: 65              LD      H,L                 
6FCE: 74              LD      (HL),H              
6FCF: 74              LD      (HL),H              
6FD0: 65              LD      H,L                 
6FD1: 72              LD      (HL),D              
6FD2: 20 ED           JR      NZ,$6FC1            ; {}
6FD4: 21 20 20        LD      HL,$2020            
6FD7: 2E 2E           LD      L,$2E               
6FD9: 2E 47           LD      L,$47               
6FDB: 72              LD      (HL),D              
6FDC: 65              LD      H,L                 
6FDD: 61              LD      H,C                 
6FDE: 74              LD      (HL),H              
6FDF: 21 3F FF        LD      HL,$FF3F            
6FE2: 59              LD      E,C                 
6FE3: 6F              LD      L,A                 
6FE4: 75              LD      (HL),L              
6FE5: 20 6B           JR      NZ,$7052            ; {}
6FE7: 6E              LD      L,(HL)              
6FE8: 6F              LD      L,A                 
6FE9: 77              LD      (HL),A              
6FEA: 2C              INC     L                   
6FEB: 20 73           JR      NZ,$7060            ; {}
6FED: 6F              LD      L,A                 
6FEE: 6D              LD      L,L                 
6FEF: 65              LD      H,L                 
6FF0: 2D              DEC     L                   
6FF1: 20 74           JR      NZ,$7067            ; {}
6FF3: 69              LD      L,C                 
6FF4: 6D              LD      L,L                 
6FF5: 65              LD      H,L                 
6FF6: 73              LD      (HL),E              
6FF7: 20 49           JR      NZ,$7042            ; {}
6FF9: 20 63           JR      NZ,$705E            ; {}
6FFB: 61              LD      H,C                 
6FFC: 6E              LD      L,(HL)              
6FFD: 5E              LD      E,(HL)              
6FFE: 74              LD      (HL),H              
6FFF: 20 20           JR      NZ,$7021            ; {}
7001: 20 68           JR      NZ,$706B            ; {}
7003: 65              LD      H,L                 
7004: 6C              LD      L,H                 
7005: 70              LD      (HL),B              
7006: 20 65           JR      NZ,$706D            ; {}
7008: 61              LD      H,C                 
7009: 74              LD      (HL),H              
700A: 69              LD      L,C                 
700B: 6E              LD      L,(HL)              
700C: 67              LD      H,A                 
700D: 20 61           JR      NZ,$7070            ; {}
700F: 20 20           JR      NZ,$7031            ; {}
7011: 20 64           JR      NZ,$7077            ; {}
7013: 65              LD      H,L                 
7014: 6C              LD      L,H                 
7015: 69              LD      L,C                 
7016: 63              LD      H,E                 
7017: 69              LD      L,C                 
7018: 6F              LD      L,A                 
7019: 75              LD      (HL),L              
701A: 73              LD      (HL),E              
701B: 20 70           JR      NZ,$708D            ; {}
701D: 69              LD      L,C                 
701E: 65              LD      H,L                 
701F: 63              LD      H,E                 
7020: 65              LD      H,L                 
7021: 20 6F           JR      NZ,$7092            ; {}
7023: 66              LD      H,(HL)              
7024: 20 70           JR      NZ,$7096            ; {}
7026: 61              LD      H,C                 
7027: 70              LD      (HL),B              
7028: 65              LD      H,L                 
7029: 72              LD      (HL),D              
702A: 2C              INC     L                   
702B: 20 65           JR      NZ,$7092            ; {}
702D: 76              HALT                        
702E: 65              LD      H,L                 
702F: 6E              LD      L,(HL)              
7030: 20 20           JR      NZ,$7052            ; {}
7032: 69              LD      L,C                 
7033: 66              LD      H,(HL)              
7034: 20 69           JR      NZ,$709F            ; {}
7036: 74              LD      (HL),H              
7037: 5E              LD      E,(HL)              
7038: 73              LD      (HL),E              
7039: 20 61           JR      NZ,$709C            ; {}
703B: 20 6C           JR      NZ,$70A9            ; {}
703D: 65              LD      H,L                 
703E: 74              LD      (HL),H              
703F: 74              LD      (HL),H              
7040: 65              LD      H,L                 
7041: 72              LD      (HL),D              
7042: 74              LD      (HL),H              
7043: 6F              LD      L,A                 
7044: 20 6D           JR      NZ,$70B3            ; {}
7046: 79              LD      A,C                 
7047: 20 64           JR      NZ,$70AD            ; {}
7049: 61              LD      H,C                 
704A: 72              LD      (HL),D              
704B: 6C              LD      L,H                 
704C: 69              LD      L,C                 
704D: 6E              LD      L,(HL)              
704E: 67              LD      H,A                 
704F: 20 20           JR      NZ,$7071            ; {}
7051: 20 4D           JR      NZ,$70A0            ; {}
7053: 72              LD      (HL),D              
7054: 2E 20           LD      L,$20               
7056: 57              LD      D,A                 
7057: 72              LD      (HL),D              
7058: 69              LD      L,C                 
7059: 74              LD      (HL),H              
705A: 65              LD      H,L                 
705B: 2E 2E           LD      L,$2E               
705D: 2E 20           LD      L,$20               
705F: 48              LD      C,B                 
7060: 6F              LD      L,A                 
7061: 77              LD      (HL),A              
7062: 65              LD      H,L                 
7063: 6D              LD      L,L                 
7064: 62              LD      H,D                 
7065: 61              LD      H,C                 
7066: 72              LD      (HL),D              
7067: 72              LD      (HL),D              
7068: 61              LD      H,C                 
7069: 73              LD      (HL),E              
706A: 73              LD      (HL),E              
706B: 69              LD      L,C                 
706C: 6E              LD      L,(HL)              
706D: 67              LD      H,A                 
706E: 21 FF 59        LD      HL,$59FF            
7071: 6F              LD      L,A                 
7072: 75              LD      (HL),L              
7073: 5E              LD      E,(HL)              
7074: 76              HALT                        
7075: 65              LD      H,L                 
7076: 20 73           JR      NZ,$70EB            ; {}
7078: 61              LD      H,C                 
7079: 76              HALT                        
707A: 65              LD      H,L                 
707B: 64              LD      H,H                 
707C: 20 20           JR      NZ,$709E            ; {}
707E: 20 20           JR      NZ,$70A0            ; {}
7080: 42              LD      B,D                 
7081: 6F              LD      L,A                 
7082: 77              LD      (HL),A              
7083: 57              LD      D,A                 
7084: 6F              LD      L,A                 
7085: 77              LD      (HL),A              
7086: 21 20 20        LD      HL,$2020            
7089: 57              LD      D,A                 
708A: 68              LD      L,B                 
708B: 61              LD      H,C                 
708C: 74              LD      (HL),H              
708D: 20 61           JR      NZ,$70F0            ; {}
708F: 20 66           JR      NZ,$70F7            ; {}
7091: 65              LD      H,L                 
7092: 61              LD      H,C                 
7093: 72              LD      (HL),D              
7094: 73              LD      (HL),E              
7095: 6F              LD      L,A                 
7096: 6D              LD      L,L                 
7097: 65              LD      H,L                 
7098: 20 62           JR      NZ,$70FC            ; {}
709A: 65              LD      H,L                 
709B: 61              LD      H,C                 
709C: 73              LD      (HL),E              
709D: 74              LD      (HL),H              
709E: 21 FF 57        LD      HL,$57FF            
70A1: 6F              LD      L,A                 
70A2: 77              LD      (HL),A              
70A3: 21 20 54        LD      HL,$5420            
70A6: 68              LD      L,B                 
70A7: 65              LD      H,L                 
70A8: 20 52           JR      NZ,$70FC            ; {}
70AA: 6F              LD      L,A                 
70AB: 6F              LD      L,A                 
70AC: 73              LD      (HL),E              
70AD: 74              LD      (HL),H              
70AE: 65              LD      H,L                 
70AF: 72              LD      (HL),D              
70B0: 68              LD      L,B                 
70B1: 61              LD      H,C                 
70B2: 73              LD      (HL),E              
70B3: 20 72           JR      NZ,$7127            ; {}
70B5: 65              LD      H,L                 
70B6: 63              LD      H,E                 
70B7: 6F              LD      L,A                 
70B8: 76              HALT                        
70B9: 65              LD      H,L                 
70BA: 72              LD      (HL),D              
70BB: 65              LD      H,L                 
70BC: 64              LD      H,H                 
70BD: 21 20 20        LD      HL,$2020            
70C0: 48              LD      C,B                 
70C1: 65              LD      H,L                 
70C2: 20 73           JR      NZ,$7137            ; {}
70C4: 65              LD      H,L                 
70C5: 65              LD      H,L                 
70C6: 6D              LD      L,L                 
70C7: 73              LD      (HL),E              
70C8: 20 76           JR      NZ,$7140            ; {}
70CA: 65              LD      H,L                 
70CB: 72              LD      (HL),D              
70CC: 79              LD      A,C                 
70CD: 20 20           JR      NZ,$70EF            ; {}
70CF: 20 66           JR      NZ,$7137            ; {}
70D1: 72              LD      (HL),D              
70D2: 69              LD      L,C                 
70D3: 65              LD      H,L                 
70D4: 6E              LD      L,(HL)              
70D5: 64              LD      H,H                 
70D6: 6C              LD      L,H                 
70D7: 79              LD      A,C                 
70D8: 21 FF 59        LD      HL,$59FF            
70DB: 65              LD      H,L                 
70DC: 70              LD      (HL),B              
70DD: 2C              INC     L                   
70DE: 20 50           JR      NZ,$7130            ; {}
70E0: 61              LD      H,C                 
70E1: 70              LD      (HL),B              
70E2: 61              LD      H,C                 
70E3: 68              LD      L,B                 
70E4: 6C              LD      L,H                 
70E5: 20 67           JR      NZ,$714E            ; {}
70E7: 6F              LD      L,A                 
70E8: 74              LD      (HL),H              
70E9: 20 6C           JR      NZ,$7157            ; {}
70EB: 6F              LD      L,A                 
70EC: 73              LD      (HL),E              
70ED: 74              LD      (HL),H              
70EE: 2C              INC     L                   
70EF: 20 6A           JR      NZ,$715B            ; {}
70F1: 75              LD      (HL),L              
70F2: 73              LD      (HL),E              
70F3: 74              LD      (HL),H              
70F4: 20 6C           JR      NZ,$7162            ; {}
70F6: 69              LD      L,C                 
70F7: 6B              LD      L,E                 
70F8: 65              LD      H,L                 
70F9: 20 68           JR      NZ,$7163            ; {}
70FB: 65              LD      H,L                 
70FC: 20 73           JR      NZ,$7171            ; {}
70FE: 61              LD      H,C                 
70FF: 69              LD      L,C                 
7100: 64              LD      H,H                 
7101: 21 20 20        LD      HL,$2020            
7104: 4E              LD      C,(HL)              
7105: 6F              LD      L,A                 
7106: 77              LD      (HL),A              
7107: 2C              INC     L                   
7108: 20 49           JR      NZ,$7153            ; {}
710A: 61              LD      H,C                 
710B: 6D              LD      L,L                 
710C: 20 73           JR      NZ,$7181            ; {}
710E: 6F              LD      L,A                 
710F: 20 66           JR      NZ,$7177            ; {}
7111: 61              LD      H,C                 
7112: 6D              LD      L,L                 
7113: 69              LD      L,C                 
7114: 73              LD      (HL),E              
7115: 68              LD      L,B                 
7116: 65              LD      H,L                 
7117: 64              LD      H,H                 
7118: 20 49           JR      NZ,$7163            ; {}
711A: 63              LD      H,E                 
711B: 61              LD      H,C                 
711C: 6E              LD      L,(HL)              
711D: 5E              LD      E,(HL)              
711E: 74              LD      (HL),H              
711F: 20 6D           JR      NZ,$718E            ; {}
7121: 6F              LD      L,A                 
7122: 76              HALT                        
7123: 65              LD      H,L                 
7124: 21 20 20        LD      HL,$2020            
7127: 43              LD      B,E                 
7128: 61              LD      H,C                 
7129: 6E              LD      L,(HL)              
712A: 79              LD      A,C                 
712B: 6F              LD      L,A                 
712C: 75              LD      (HL),L              
712D: 20 67           JR      NZ,$7196            ; {}
712F: 69              LD      L,C                 
7130: 76              HALT                        
7131: 65              LD      H,L                 
7132: 20 6D           JR      NZ,$71A1            ; {}
7134: 65              LD      H,L                 
7135: 20 73           JR      NZ,$71AA            ; {}
7137: 6F              LD      L,A                 
7138: 6D              LD      L,L                 
7139: 65              LD      H,L                 
713A: 76              HALT                        
713B: 69              LD      L,C                 
713C: 74              LD      (HL),H              
713D: 74              LD      (HL),H              
713E: 6C              LD      L,H                 
713F: 65              LD      H,L                 
7140: 73              LD      (HL),E              
7141: 3F              CCF                         
7142: 20 20           JR      NZ,$7164            ; {}
7144: 20 20           JR      NZ,$7166            ; {}
7146: 20 20           JR      NZ,$7168            ; {}
7148: 20 20           JR      NZ,$716A            ; {}
714A: 20 20           JR      NZ,$716C            ; {}
714C: 20 20           JR      NZ,$716E            ; {}
714E: 59              LD      E,C                 
714F: 65              LD      H,L                 
7150: 73              LD      (HL),E              
7151: 20 20           JR      NZ,$7173            ; {}
7153: 4E              LD      C,(HL)              
7154: 6F              LD      L,A                 
7155: 70              LD      (HL),B              
7156: 65              LD      H,L                 
7157: FE 59           CP      $59                 
7159: 6F              LD      L,A                 
715A: 75              LD      (HL),L              
715B: 5E              LD      E,(HL)              
715C: 72              LD      (HL),D              
715D: 65              LD      H,L                 
715E: 20 6F           JR      NZ,$71CF            ; {}
7160: 6E              LD      L,(HL)              
7161: 65              LD      H,L                 
7162: 20 63           JR      NZ,$71C7            ; {}
7164: 6F              LD      L,A                 
7165: 6C              LD      L,H                 
7166: 64              LD      H,H                 
7167: 20 68           JR      NZ,$71D1            ; {}
7169: 6F              LD      L,A                 
716A: 6D              LD      L,L                 
716B: 62              LD      H,D                 
716C: 72              LD      (HL),D              
716D: 65              LD      H,L                 
716E: 2E 2E           LD      L,$2E               
7170: 2E FF           LD      L,$FF               
7172: 54              LD      D,H                 
7173: 68              LD      L,B                 
7174: 69              LD      L,C                 
7175: 73              LD      (HL),E              
7176: 20 E6           JR      NZ,$715E            ; {}
7178: 20 69           JR      NZ,$71E3            ; {}
717A: 73              LD      (HL),E              
717B: 20 73           JR      NZ,$71F0            ; {}
717D: 6F              LD      L,A                 
717E: 20 20           JR      NZ,$71A0            ; {}
7180: 20 20           JR      NZ,$71A2            ; {}
7182: 64              LD      H,H                 
7183: 65              LD      H,L                 
7184: 6C              LD      L,H                 
7185: 69              LD      L,C                 
7186: 63              LD      H,E                 
7187: 69              LD      L,C                 
7188: 6F              LD      L,A                 
7189: 75              LD      (HL),L              
718A: 73              LD      (HL),E              
718B: 21 20 20        LD      HL,$2020            
718E: 49              LD      C,C                 
718F: 5E              LD      E,(HL)              
7190: 6D              LD      L,L                 
7191: 20 67           JR      NZ,$71FA            ; {}
7193: 6F              LD      L,A                 
7194: 69              LD      L,C                 
7195: 6E              LD      L,(HL)              
7196: 67              LD      H,A                 
7197: 20 74           JR      NZ,$720D            ; {}
7199: 6F              LD      L,A                 
719A: 20 65           JR      NZ,$7201            ; {}
719C: 61              LD      H,C                 
719D: 74              LD      (HL),H              
719E: 20 74           JR      NZ,$7214            ; {}
71A0: 68              LD      L,B                 
71A1: 65              LD      H,L                 
71A2: E6 20           AND     $20                 
71A4: 72              LD      (HL),D              
71A5: 69              LD      L,C                 
71A6: 67              LD      H,A                 
71A7: 68              LD      L,B                 
71A8: 74              LD      (HL),H              
71A9: 20 6E           JR      NZ,$7219            ; {}
71AB: 6F              LD      L,A                 
71AC: 77              LD      (HL),A              
71AD: 21 20 20        LD      HL,$2020            
71B0: 20 20           JR      NZ,$71D2            ; {}
71B2: 20 42           JR      NZ,$71F6            ; {}
71B4: 6F              LD      L,A                 
71B5: 6E              LD      L,(HL)              
71B6: 20 41           JR      NZ,$71F9            ; {}
71B8: 70              LD      (HL),B              
71B9: 70              LD      (HL),B              
71BA: 65              LD      H,L                 
71BB: 74              LD      (HL),H              
71BC: 69              LD      L,C                 
71BD: 74              LD      (HL),H              
71BE: 21 FF 41        LD      HL,$41FF            
71C1: 48              LD      C,B                 
71C2: 21 20 20        LD      HL,$2020            
71C5: 54              LD      D,H                 
71C6: 68              LD      L,B                 
71C7: 69              LD      L,C                 
71C8: 73              LD      (HL),E              
71C9: 20 69           JR      NZ,$7234            ; {}
71CB: 73              LD      (HL),E              
71CC: 6E              LD      L,(HL)              
71CD: 5E              LD      E,(HL)              
71CE: 74              LD      (HL),H              
71CF: 20 6D           JR      NZ,$723E            ; {}
71D1: 65              LD      H,L                 
71D2: 61              LD      H,C                 
71D3: 6E              LD      L,(HL)              
71D4: 74              LD      (HL),H              
71D5: 20 74           JR      NZ,$724B            ; {}
71D7: 6F              LD      L,A                 
71D8: 20 62           JR      NZ,$723C            ; {}
71DA: 65              LD      H,L                 
71DB: 20 61           JR      NZ,$723E            ; {}
71DD: 20 20           JR      NZ,$71FF            ; {}
71DF: 20 72           JR      NZ,$7253            ; {}
71E1: 65              LD      H,L                 
71E2: 77              LD      (HL),A              
71E3: 61              LD      H,C                 
71E4: 72              LD      (HL),D              
71E5: 64              LD      H,H                 
71E6: 2E 2E           LD      L,$2E               
71E8: 2E 20           LD      L,$20               
71EA: 20 48           JR      NZ,$7234            ; {}
71EC: 65              LD      H,L                 
71ED: 72              LD      (HL),D              
71EE: 65              LD      H,L                 
71EF: 2C              INC     L                   
71F0: 74              LD      (HL),H              
71F1: 61              LD      H,C                 
71F2: 6B              LD      L,E                 
71F3: 65              LD      H,L                 
71F4: 20 74           JR      NZ,$726A            ; {}
71F6: 68              LD      L,B                 
71F7: 69              LD      L,C                 
71F8: 73              LD      (HL),E              
71F9: 20 E7           JR      NZ,$71E2            ; {}
71FB: 21 20 20        LD      HL,$2020            
71FE: 20 20           JR      NZ,$7220            ; {}
7200: 49              LD      C,C                 
7201: 74              LD      (HL),H              
7202: 5E              LD      E,(HL)              
7203: 73              LD      (HL),E              
7204: 20 61           JR      NZ,$7267            ; {}
7206: 20 68           JR      NZ,$7270            ; {}
7208: 69              LD      L,C                 
7209: 62              LD      H,D                 
720A: 69              LD      L,C                 
720B: 73              LD      (HL),E              
720C: 63              LD      H,E                 
720D: 75              LD      (HL),L              
720E: 73              LD      (HL),E              
720F: 21 FF 59        LD      HL,$59FF            
7212: 6F              LD      L,A                 
7213: 75              LD      (HL),L              
7214: 20 74           JR      NZ,$728A            ; {}
7216: 72              LD      (HL),D              
7217: 61              LD      H,C                 
7218: 64              LD      H,H                 
7219: 65              LD      H,L                 
721A: 64              LD      H,H                 
721B: 20 74           JR      NZ,$7291            ; {}
721D: 68              LD      L,B                 
721E: 65              LD      H,L                 
721F: 20 E6           JR      NZ,$7207            ; {}
7221: 66              LD      H,(HL)              
7222: 6F              LD      L,A                 
7223: 72              LD      (HL),D              
7224: 20 74           JR      NZ,$729A            ; {}
7226: 68              LD      L,B                 
7227: 65              LD      H,L                 
7228: 20 E7           JR      NZ,$7211            ; {}
722A: 21 FF 44        LD      HL,$44FF            
722D: 65              LD      H,L                 
722E: 6C              LD      L,H                 
722F: 69              LD      L,C                 
7230: 63              LD      H,E                 
7231: 69              LD      L,C                 
7232: 6F              LD      L,A                 
7233: 75              LD      (HL),L              
7234: 73              LD      (HL),E              
7235: 21 20 20        LD      HL,$2020            
7238: 59              LD      E,C                 
7239: 75              LD      (HL),L              
723A: 6D              LD      L,L                 
723B: 21 49 5E        LD      HL,$5E49            
723E: 6D              LD      L,L                 
723F: 20 66           JR      NZ,$72A7            ; {}
7241: 69              LD      L,C                 
7242: 6C              LD      L,H                 
7243: 6C              LD      L,H                 
7244: 65              LD      H,L                 
7245: 64              LD      H,H                 
7246: 20 77           JR      NZ,$72BF            ; {}
7248: 69              LD      L,C                 
7249: 74              LD      (HL),H              
724A: 68              LD      L,B                 
724B: 20 65           JR      NZ,$72B2            ; {}
724D: 6E              LD      L,(HL)              
724E: 65              LD      H,L                 
724F: 72              LD      (HL),D              
7250: 67              LD      H,A                 
7251: 79              LD      A,C                 
7252: 2C              INC     L                   
7253: 20 6E           JR      NZ,$72C3            ; {}
7255: 6F              LD      L,A                 
7256: 77              LD      (HL),A              
7257: 21 FF 49        LD      HL,$49FF            
725A: 5E              LD      E,(HL)              
725B: 76              HALT                        
725C: 65              LD      H,L                 
725D: 20 67           JR      NZ,$72C6            ; {}
725F: 6F              LD      L,A                 
7260: 74              LD      (HL),H              
7261: 20 74           JR      NZ,$72D7            ; {}
7263: 6F              LD      L,A                 
7264: 20 73           JR      NZ,$72D9            ; {}
7266: 61              LD      H,C                 
7267: 79              LD      A,C                 
7268: 2C              INC     L                   
7269: 74              LD      (HL),H              
726A: 68              LD      L,B                 
726B: 61              LD      H,C                 
726C: 6E              LD      L,(HL)              
726D: 6B              LD      L,E                 
726E: 73              LD      (HL),E              
726F: 20 61           JR      NZ,$72D2            ; {}
7271: 67              LD      H,A                 
7272: 61              LD      H,C                 
7273: 69              LD      L,C                 
7274: 6E              LD      L,(HL)              
7275: 21 FF 59        LD      HL,$59FF            
7278: 65              LD      H,L                 
7279: 70              LD      (HL),B              
727A: 2C              INC     L                   
727B: 20 50           JR      NZ,$72CD            ; {}
727D: 61              LD      H,C                 
727E: 70              LD      (HL),B              
727F: 61              LD      H,C                 
7280: 68              LD      L,B                 
7281: 6C              LD      L,H                 
7282: 20 67           JR      NZ,$72EB            ; {}
7284: 6F              LD      L,A                 
7285: 74              LD      (HL),H              
7286: 20 6C           JR      NZ,$72F4            ; {}
7288: 6F              LD      L,A                 
7289: 73              LD      (HL),E              
728A: 74              LD      (HL),H              
728B: 2C              INC     L                   
728C: 20 6A           JR      NZ,$72F8            ; {}
728E: 75              LD      (HL),L              
728F: 73              LD      (HL),E              
7290: 74              LD      (HL),H              
7291: 20 6C           JR      NZ,$72FF            ; {}
7293: 69              LD      L,C                 
7294: 6B              LD      L,E                 
7295: 65              LD      H,L                 
7296: 20 68           JR      NZ,$7300            ; {}
7298: 65              LD      H,L                 
7299: 20 73           JR      NZ,$730E            ; {}
729B: 61              LD      H,C                 
729C: 69              LD      L,C                 
729D: 64              LD      H,H                 
729E: 21 20 20        LD      HL,$2020            
72A1: 4E              LD      C,(HL)              
72A2: 6F              LD      L,A                 
72A3: 77              LD      (HL),A              
72A4: 2C              INC     L                   
72A5: 20 49           JR      NZ,$72F0            ; {}
72A7: 61              LD      H,C                 
72A8: 6D              LD      L,L                 
72A9: 20 73           JR      NZ,$731E            ; {}
72AB: 6F              LD      L,A                 
72AC: 20 66           JR      NZ,$7314            ; {}
72AE: 61              LD      H,C                 
72AF: 6D              LD      L,L                 
72B0: 69              LD      L,C                 
72B1: 73              LD      (HL),E              
72B2: 68              LD      L,B                 
72B3: 65              LD      H,L                 
72B4: 64              LD      H,H                 
72B5: 20 49           JR      NZ,$7300            ; {}
72B7: 63              LD      H,E                 
72B8: 61              LD      H,C                 
72B9: 6E              LD      L,(HL)              
72BA: 5E              LD      E,(HL)              
72BB: 74              LD      (HL),H              
72BC: 20 6D           JR      NZ,$732B            ; {}
72BE: 6F              LD      L,A                 
72BF: 76              HALT                        
72C0: 65              LD      H,L                 
72C1: 21 20 20        LD      HL,$2020            
72C4: 43              LD      B,E                 
72C5: 61              LD      H,C                 
72C6: 6E              LD      L,(HL)              
72C7: 79              LD      A,C                 
72C8: 6F              LD      L,A                 
72C9: 75              LD      (HL),L              
72CA: 20 67           JR      NZ,$7333            ; {}
72CC: 69              LD      L,C                 
72CD: 76              HALT                        
72CE: 65              LD      H,L                 
72CF: 20 6D           JR      NZ,$733E            ; {}
72D1: 65              LD      H,L                 
72D2: 20 73           JR      NZ,$7347            ; {}
72D4: 6F              LD      L,A                 
72D5: 6D              LD      L,L                 
72D6: 65              LD      H,L                 
72D7: 76              HALT                        
72D8: 69              LD      L,C                 
72D9: 74              LD      (HL),H              
72DA: 74              LD      (HL),H              
72DB: 6C              LD      L,H                 
72DC: 65              LD      H,L                 
72DD: 73              LD      (HL),E              
72DE: 3F              CCF                         
72DF: 20 20           JR      NZ,$7301            ; {}
72E1: 20 20           JR      NZ,$7303            ; {}
72E3: 20 20           JR      NZ,$7305            ; {}
72E5: 20 20           JR      NZ,$7307            ; {}
72E7: 20 20           JR      NZ,$7309            ; {}
72E9: 20 20           JR      NZ,$730B            ; {}
72EB: 4E              LD      C,(HL)              
72EC: 6F              LD      L,A                 
72ED: 70              LD      (HL),B              
72EE: 65              LD      H,L                 
72EF: 20 43           JR      NZ,$7334            ; {}
72F1: 61              LD      H,C                 
72F2: 6E              LD      L,(HL)              
72F3: 5E              LD      E,(HL)              
72F4: 74              LD      (HL),H              
72F5: FE 53           CP      $53                 
72F7: 68              LD      L,B                 
72F8: 65              LD      H,L                 
72F9: 5E              LD      E,(HL)              
72FA: 73              LD      (HL),E              
72FB: 20 68           JR      NZ,$7365            ; {}
72FD: 61              LD      H,C                 
72FE: 64              LD      H,H                 
72FF: 20 61           JR      NZ,$7362            ; {}
7301: 6E              LD      L,(HL)              
7302: 20 20           JR      NZ,$7324            ; {}
7304: 20 20           JR      NZ,$7326            ; {}
7306: 61              LD      H,C                 
7307: 77              LD      (HL),A              
7308: 66              LD      H,(HL)              
7309: 75              LD      (HL),L              
730A: 6C              LD      L,H                 
730B: 20 74           JR      NZ,$7381            ; {}
730D: 72              LD      (HL),D              
730E: 61              LD      H,C                 
730F: 64              LD      H,H                 
7310: 67              LD      H,A                 
7311: 65              LD      H,L                 
7312: 64              LD      H,H                 
7313: 79              LD      A,C                 
7314: 20 20           JR      NZ,$7336            ; {}
7316: 69              LD      L,C                 
7317: 6E              LD      L,(HL)              
7318: 20 74           JR      NZ,$738E            ; {}
731A: 68              LD      L,B                 
731B: 65              LD      H,L                 
731C: 20 68           JR      NZ,$7386            ; {}
731E: 6F              LD      L,A                 
731F: 75              LD      (HL),L              
7320: 73              LD      (HL),E              
7321: 65              LD      H,L                 
7322: 20 20           JR      NZ,$7344            ; {}
7324: 20 20           JR      NZ,$7346            ; {}
7326: 61              LD      H,C                 
7327: 63              LD      H,E                 
7328: 72              LD      (HL),D              
7329: 6F              LD      L,A                 
732A: 73              LD      (HL),E              
732B: 73              LD      (HL),E              
732C: 20 74           JR      NZ,$73A2            ; {}
732E: 68              LD      L,B                 
732F: 65              LD      H,L                 
7330: 20 77           JR      NZ,$73A9            ; {}
7332: 61              LD      H,C                 
7333: 79              LD      A,C                 
7334: 21 20 49        LD      HL,$4920            
7337: 74              LD      (HL),H              
7338: 5E              LD      E,(HL)              
7339: 73              LD      (HL),E              
733A: 20 6A           JR      NZ,$73A6            ; {}
733C: 75              LD      (HL),L              
733D: 73              LD      (HL),E              
733E: 74              LD      (HL),H              
733F: 20 61           JR      NZ,$73A2            ; {}
7341: 77              LD      (HL),A              
7342: 66              LD      H,(HL)              
7343: 75              LD      (HL),L              
7344: 6C              LD      L,H                 
7345: 2C              INC     L                   
7346: 61              LD      H,C                 
7347: 6E              LD      L,(HL)              
7348: 64              LD      H,H                 
7349: 20 61           JR      NZ,$73AC            ; {}
734B: 6C              LD      L,H                 
734C: 6C              LD      L,H                 
734D: 20 49           JR      NZ,$7398            ; {}
734F: 20 63           JR      NZ,$73B4            ; {}
7351: 61              LD      H,C                 
7352: 6E              LD      L,(HL)              
7353: 20 64           JR      NZ,$73B9            ; {}
7355: 6F              LD      L,A                 
7356: 69              LD      L,C                 
7357: 73              LD      (HL),E              
7358: 20 73           JR      NZ,$73CD            ; {}
735A: 77              LD      (HL),A              
735B: 65              LD      H,L                 
735C: 65              LD      H,L                 
735D: 70              LD      (HL),B              
735E: 21 FF FF        LD      HL,$FFFF            
7361: FF              RST     0X38                
7362: FF              RST     0X38                
7363: FF              RST     0X38                
7364: FF              RST     0X38                
7365: FF              RST     0X38                
7366: FF              RST     0X38                
7367: FF              RST     0X38                
7368: FF              RST     0X38                
7369: FF              RST     0X38                
736A: FF              RST     0X38                
736B: FF              RST     0X38                
736C: FF              RST     0X38                
736D: FF              RST     0X38                
736E: FF              RST     0X38                
736F: FF              RST     0X38                
7370: FF              RST     0X38                
7371: FF              RST     0X38                
7372: FF              RST     0X38                
7373: FF              RST     0X38                
7374: FF              RST     0X38                
7375: FF              RST     0X38                
7376: FF              RST     0X38                
7377: FF              RST     0X38                
7378: FF              RST     0X38                
7379: FF              RST     0X38                
737A: FF              RST     0X38                
737B: FF              RST     0X38                
737C: FF              RST     0X38                
737D: FF              RST     0X38                
737E: FF              RST     0X38                
737F: FF              RST     0X38                
7380: FF              RST     0X38                
7381: FF              RST     0X38                
7382: FF              RST     0X38                
7383: FF              RST     0X38                
7384: FF              RST     0X38                
7385: FF              RST     0X38                
7386: FF              RST     0X38                
7387: FF              RST     0X38                
7388: FF              RST     0X38                
7389: FF              RST     0X38                
738A: FF              RST     0X38                
738B: FF              RST     0X38                
738C: FF              RST     0X38                
738D: FF              RST     0X38                
738E: FF              RST     0X38                
738F: FF              RST     0X38                
7390: FF              RST     0X38                
7391: FF              RST     0X38                
7392: FF              RST     0X38                
7393: FF              RST     0X38                
7394: FF              RST     0X38                
7395: FF              RST     0X38                
7396: FF              RST     0X38                
7397: FF              RST     0X38                
7398: FF              RST     0X38                
7399: FF              RST     0X38                
739A: FF              RST     0X38                
739B: FF              RST     0X38                
739C: FF              RST     0X38                
739D: FF              RST     0X38                
739E: FF              RST     0X38                
739F: FF              RST     0X38                
73A0: FF              RST     0X38                
73A1: FF              RST     0X38                
73A2: FF              RST     0X38                
73A3: FF              RST     0X38                
73A4: FF              RST     0X38                
73A5: FF              RST     0X38                
73A6: FF              RST     0X38                
73A7: FF              RST     0X38                
73A8: FF              RST     0X38                
73A9: FF              RST     0X38                
73AA: FF              RST     0X38                
73AB: FF              RST     0X38                
73AC: FF              RST     0X38                
73AD: FF              RST     0X38                
73AE: FF              RST     0X38                
73AF: FF              RST     0X38                
73B0: FF              RST     0X38                
73B1: FF              RST     0X38                
73B2: FF              RST     0X38                
73B3: FF              RST     0X38                
73B4: FF              RST     0X38                
73B5: FF              RST     0X38                
73B6: FF              RST     0X38                
73B7: FF              RST     0X38                
73B8: FF              RST     0X38                
73B9: FF              RST     0X38                
73BA: FF              RST     0X38                
73BB: FF              RST     0X38                
73BC: FF              RST     0X38                
73BD: FF              RST     0X38                
73BE: FF              RST     0X38                
73BF: FF              RST     0X38                
73C0: FF              RST     0X38                
73C1: FF              RST     0X38                
73C2: FF              RST     0X38                
73C3: FF              RST     0X38                
73C4: FF              RST     0X38                
73C5: FF              RST     0X38                
73C6: FF              RST     0X38                
73C7: FF              RST     0X38                
73C8: FF              RST     0X38                
73C9: FF              RST     0X38                
73CA: FF              RST     0X38                
73CB: FF              RST     0X38                
73CC: FF              RST     0X38                
73CD: FF              RST     0X38                
73CE: FF              RST     0X38                
73CF: FF              RST     0X38                
73D0: FF              RST     0X38                
73D1: FF              RST     0X38                
73D2: FF              RST     0X38                
73D3: FF              RST     0X38                
73D4: FF              RST     0X38                
73D5: FF              RST     0X38                
73D6: FF              RST     0X38                
73D7: FF              RST     0X38                
73D8: FF              RST     0X38                
73D9: FF              RST     0X38                
73DA: FF              RST     0X38                
73DB: FF              RST     0X38                
73DC: FF              RST     0X38                
73DD: FF              RST     0X38                
73DE: FF              RST     0X38                
73DF: FF              RST     0X38                
73E0: FF              RST     0X38                
73E1: FF              RST     0X38                
73E2: FF              RST     0X38                
73E3: FF              RST     0X38                
73E4: FF              RST     0X38                
73E5: FF              RST     0X38                
73E6: FF              RST     0X38                
73E7: FF              RST     0X38                
73E8: FF              RST     0X38                
73E9: FF              RST     0X38                
73EA: FF              RST     0X38                
73EB: FF              RST     0X38                
73EC: FF              RST     0X38                
73ED: FF              RST     0X38                
73EE: FF              RST     0X38                
73EF: FF              RST     0X38                
73F0: FF              RST     0X38                
73F1: FF              RST     0X38                
73F2: FF              RST     0X38                
73F3: FF              RST     0X38                
73F4: FF              RST     0X38                
73F5: FF              RST     0X38                
73F6: FF              RST     0X38                
73F7: FF              RST     0X38                
73F8: FF              RST     0X38                
73F9: FF              RST     0X38                
73FA: FF              RST     0X38                
73FB: FF              RST     0X38                
73FC: FF              RST     0X38                
73FD: FF              RST     0X38                
73FE: FF              RST     0X38                
73FF: FF              RST     0X38                
7400: FF              RST     0X38                
7401: FF              RST     0X38                
7402: FF              RST     0X38                
7403: FF              RST     0X38                
7404: FF              RST     0X38                
7405: FF              RST     0X38                
7406: FF              RST     0X38                
7407: FF              RST     0X38                
7408: FF              RST     0X38                
7409: FF              RST     0X38                
740A: FF              RST     0X38                
740B: FF              RST     0X38                
740C: FF              RST     0X38                
740D: FF              RST     0X38                
740E: FF              RST     0X38                
740F: FF              RST     0X38                
7410: FF              RST     0X38                
7411: FF              RST     0X38                
7412: FF              RST     0X38                
7413: FF              RST     0X38                
7414: FF              RST     0X38                
7415: FF              RST     0X38                
7416: FF              RST     0X38                
7417: FF              RST     0X38                
7418: FF              RST     0X38                
7419: FF              RST     0X38                
741A: FF              RST     0X38                
741B: FF              RST     0X38                
741C: FF              RST     0X38                
741D: FF              RST     0X38                
741E: FF              RST     0X38                
741F: FF              RST     0X38                
7420: FF              RST     0X38                
7421: FF              RST     0X38                
7422: FF              RST     0X38                
7423: FF              RST     0X38                
7424: FF              RST     0X38                
7425: FF              RST     0X38                
7426: FF              RST     0X38                
7427: FF              RST     0X38                
7428: FF              RST     0X38                
7429: FF              RST     0X38                
742A: FF              RST     0X38                
742B: FF              RST     0X38                
742C: FF              RST     0X38                
742D: FF              RST     0X38                
742E: FF              RST     0X38                
742F: FF              RST     0X38                
7430: FF              RST     0X38                
7431: FF              RST     0X38                
7432: FF              RST     0X38                
7433: FF              RST     0X38                
7434: FF              RST     0X38                
7435: FF              RST     0X38                
7436: FF              RST     0X38                
7437: FF              RST     0X38                
7438: FF              RST     0X38                
7439: FF              RST     0X38                
743A: FF              RST     0X38                
743B: FF              RST     0X38                
743C: FF              RST     0X38                
743D: FF              RST     0X38                
743E: FF              RST     0X38                
743F: FF              RST     0X38                
7440: FF              RST     0X38                
7441: FF              RST     0X38                
7442: FF              RST     0X38                
7443: FF              RST     0X38                
7444: FF              RST     0X38                
7445: FF              RST     0X38                
7446: FF              RST     0X38                
7447: FF              RST     0X38                
7448: FF              RST     0X38                
7449: FF              RST     0X38                
744A: FF              RST     0X38                
744B: FF              RST     0X38                
744C: FF              RST     0X38                
744D: FF              RST     0X38                
744E: FF              RST     0X38                
744F: FF              RST     0X38                
7450: FF              RST     0X38                
7451: FF              RST     0X38                
7452: FF              RST     0X38                
7453: FF              RST     0X38                
7454: FF              RST     0X38                
7455: FF              RST     0X38                
7456: FF              RST     0X38                
7457: FF              RST     0X38                
7458: FF              RST     0X38                
7459: FF              RST     0X38                
745A: FF              RST     0X38                
745B: FF              RST     0X38                
745C: FF              RST     0X38                
745D: FF              RST     0X38                
745E: FF              RST     0X38                
745F: FF              RST     0X38                
7460: FF              RST     0X38                
7461: FF              RST     0X38                
7462: FF              RST     0X38                
7463: FF              RST     0X38                
7464: FF              RST     0X38                
7465: FF              RST     0X38                
7466: FF              RST     0X38                
7467: FF              RST     0X38                
7468: FF              RST     0X38                
7469: FF              RST     0X38                
746A: FF              RST     0X38                
746B: FF              RST     0X38                
746C: FF              RST     0X38                
746D: FF              RST     0X38                
746E: FF              RST     0X38                
746F: FF              RST     0X38                
7470: FF              RST     0X38                
7471: FF              RST     0X38                
7472: FF              RST     0X38                
7473: FF              RST     0X38                
7474: FF              RST     0X38                
7475: FF              RST     0X38                
7476: FF              RST     0X38                
7477: FF              RST     0X38                
7478: FF              RST     0X38                
7479: FF              RST     0X38                
747A: FF              RST     0X38                
747B: FF              RST     0X38                
747C: FF              RST     0X38                
747D: FF              RST     0X38                
747E: FF              RST     0X38                
747F: FF              RST     0X38                
7480: FF              RST     0X38                
7481: FF              RST     0X38                
7482: FF              RST     0X38                
7483: FF              RST     0X38                
7484: FF              RST     0X38                
7485: FF              RST     0X38                
7486: FF              RST     0X38                
7487: FF              RST     0X38                
7488: FF              RST     0X38                
7489: FF              RST     0X38                
748A: FF              RST     0X38                
748B: FF              RST     0X38                
748C: FF              RST     0X38                
748D: FF              RST     0X38                
748E: FF              RST     0X38                
748F: FF              RST     0X38                
7490: FF              RST     0X38                
7491: FF              RST     0X38                
7492: FF              RST     0X38                
7493: FF              RST     0X38                
7494: FF              RST     0X38                
7495: FF              RST     0X38                
7496: FF              RST     0X38                
7497: FF              RST     0X38                
7498: FF              RST     0X38                
7499: FF              RST     0X38                
749A: FF              RST     0X38                
749B: FF              RST     0X38                
749C: FF              RST     0X38                
749D: FF              RST     0X38                
749E: FF              RST     0X38                
749F: FF              RST     0X38                
74A0: FF              RST     0X38                
74A1: FF              RST     0X38                
74A2: FF              RST     0X38                
74A3: FF              RST     0X38                
74A4: FF              RST     0X38                
74A5: FF              RST     0X38                
74A6: FF              RST     0X38                
74A7: FF              RST     0X38                
74A8: FF              RST     0X38                
74A9: FF              RST     0X38                
74AA: FF              RST     0X38                
74AB: FF              RST     0X38                
74AC: FF              RST     0X38                
74AD: FF              RST     0X38                
74AE: FF              RST     0X38                
74AF: FF              RST     0X38                
74B0: FF              RST     0X38                
74B1: FF              RST     0X38                
74B2: FF              RST     0X38                
74B3: FF              RST     0X38                
74B4: FF              RST     0X38                
74B5: FF              RST     0X38                
74B6: FF              RST     0X38                
74B7: FF              RST     0X38                
74B8: FF              RST     0X38                
74B9: FF              RST     0X38                
74BA: FF              RST     0X38                
74BB: FF              RST     0X38                
74BC: FF              RST     0X38                
74BD: FF              RST     0X38                
74BE: FF              RST     0X38                
74BF: FF              RST     0X38                
74C0: FF              RST     0X38                
74C1: FF              RST     0X38                
74C2: FF              RST     0X38                
74C3: FF              RST     0X38                
74C4: FF              RST     0X38                
74C5: FF              RST     0X38                
74C6: FF              RST     0X38                
74C7: FF              RST     0X38                
74C8: FF              RST     0X38                
74C9: FF              RST     0X38                
74CA: FF              RST     0X38                
74CB: FF              RST     0X38                
74CC: FF              RST     0X38                
74CD: FF              RST     0X38                
74CE: FF              RST     0X38                
74CF: FF              RST     0X38                
74D0: FF              RST     0X38                
74D1: FF              RST     0X38                
74D2: FF              RST     0X38                
74D3: FF              RST     0X38                
74D4: FF              RST     0X38                
74D5: FF              RST     0X38                
74D6: FF              RST     0X38                
74D7: FF              RST     0X38                
74D8: FF              RST     0X38                
74D9: FF              RST     0X38                
74DA: FF              RST     0X38                
74DB: FF              RST     0X38                
74DC: FF              RST     0X38                
74DD: FF              RST     0X38                
74DE: FF              RST     0X38                
74DF: FF              RST     0X38                
74E0: FF              RST     0X38                
74E1: FF              RST     0X38                
74E2: FF              RST     0X38                
74E3: FF              RST     0X38                
74E4: FF              RST     0X38                
74E5: FF              RST     0X38                
74E6: FF              RST     0X38                
74E7: FF              RST     0X38                
74E8: FF              RST     0X38                
74E9: FF              RST     0X38                
74EA: FF              RST     0X38                
74EB: FF              RST     0X38                
74EC: FF              RST     0X38                
74ED: FF              RST     0X38                
74EE: FF              RST     0X38                
74EF: FF              RST     0X38                
74F0: FF              RST     0X38                
74F1: FF              RST     0X38                
74F2: FF              RST     0X38                
74F3: FF              RST     0X38                
74F4: FF              RST     0X38                
74F5: FF              RST     0X38                
74F6: FF              RST     0X38                
74F7: FF              RST     0X38                
74F8: FF              RST     0X38                
74F9: FF              RST     0X38                
74FA: FF              RST     0X38                
74FB: FF              RST     0X38                
74FC: FF              RST     0X38                
74FD: FF              RST     0X38                
74FE: FF              RST     0X38                
74FF: FF              RST     0X38                
7500: FF              RST     0X38                
7501: FF              RST     0X38                
7502: FF              RST     0X38                
7503: FF              RST     0X38                
7504: FF              RST     0X38                
7505: FF              RST     0X38                
7506: FF              RST     0X38                
7507: FF              RST     0X38                
7508: FF              RST     0X38                
7509: FF              RST     0X38                
750A: FF              RST     0X38                
750B: FF              RST     0X38                
750C: FF              RST     0X38                
750D: FF              RST     0X38                
750E: FF              RST     0X38                
750F: FF              RST     0X38                
7510: FF              RST     0X38                
7511: FF              RST     0X38                
7512: FF              RST     0X38                
7513: FF              RST     0X38                
7514: FF              RST     0X38                
7515: FF              RST     0X38                
7516: FF              RST     0X38                
7517: FF              RST     0X38                
7518: FF              RST     0X38                
7519: FF              RST     0X38                
751A: FF              RST     0X38                
751B: FF              RST     0X38                
751C: FF              RST     0X38                
751D: FF              RST     0X38                
751E: FF              RST     0X38                
751F: FF              RST     0X38                
7520: FF              RST     0X38                
7521: FF              RST     0X38                
7522: FF              RST     0X38                
7523: FF              RST     0X38                
7524: FF              RST     0X38                
7525: FF              RST     0X38                
7526: FF              RST     0X38                
7527: FF              RST     0X38                
7528: FF              RST     0X38                
7529: FF              RST     0X38                
752A: FF              RST     0X38                
752B: FF              RST     0X38                
752C: FF              RST     0X38                
752D: FF              RST     0X38                
752E: FF              RST     0X38                
752F: FF              RST     0X38                
7530: FF              RST     0X38                
7531: FF              RST     0X38                
7532: FF              RST     0X38                
7533: FF              RST     0X38                
7534: FF              RST     0X38                
7535: FF              RST     0X38                
7536: FF              RST     0X38                
7537: FF              RST     0X38                
7538: FF              RST     0X38                
7539: FF              RST     0X38                
753A: FF              RST     0X38                
753B: FF              RST     0X38                
753C: FF              RST     0X38                
753D: FF              RST     0X38                
753E: FF              RST     0X38                
753F: FF              RST     0X38                
7540: FF              RST     0X38                
7541: FF              RST     0X38                
7542: FF              RST     0X38                
7543: FF              RST     0X38                
7544: FF              RST     0X38                
7545: FF              RST     0X38                
7546: FF              RST     0X38                
7547: FF              RST     0X38                
7548: FF              RST     0X38                
7549: FF              RST     0X38                
754A: FF              RST     0X38                
754B: FF              RST     0X38                
754C: FF              RST     0X38                
754D: FF              RST     0X38                
754E: FF              RST     0X38                
754F: FF              RST     0X38                
7550: FF              RST     0X38                
7551: FF              RST     0X38                
7552: FF              RST     0X38                
7553: FF              RST     0X38                
7554: FF              RST     0X38                
7555: FF              RST     0X38                
7556: FF              RST     0X38                
7557: FF              RST     0X38                
7558: FF              RST     0X38                
7559: FF              RST     0X38                
755A: FF              RST     0X38                
755B: FF              RST     0X38                
755C: FF              RST     0X38                
755D: FF              RST     0X38                
755E: FF              RST     0X38                
755F: FF              RST     0X38                
7560: FF              RST     0X38                
7561: FF              RST     0X38                
7562: FF              RST     0X38                
7563: FF              RST     0X38                
7564: FF              RST     0X38                
7565: FF              RST     0X38                
7566: FF              RST     0X38                
7567: FF              RST     0X38                
7568: FF              RST     0X38                
7569: FF              RST     0X38                
756A: FF              RST     0X38                
756B: FF              RST     0X38                
756C: FF              RST     0X38                
756D: FF              RST     0X38                
756E: FF              RST     0X38                
756F: FF              RST     0X38                
7570: FF              RST     0X38                
7571: FF              RST     0X38                
7572: FF              RST     0X38                
7573: FF              RST     0X38                
7574: FF              RST     0X38                
7575: FF              RST     0X38                
7576: FF              RST     0X38                
7577: FF              RST     0X38                
7578: FF              RST     0X38                
7579: FF              RST     0X38                
757A: FF              RST     0X38                
757B: FF              RST     0X38                
757C: FF              RST     0X38                
757D: FF              RST     0X38                
757E: FF              RST     0X38                
757F: FF              RST     0X38                
7580: FF              RST     0X38                
7581: FF              RST     0X38                
7582: FF              RST     0X38                
7583: FF              RST     0X38                
7584: FF              RST     0X38                
7585: FF              RST     0X38                
7586: FF              RST     0X38                
7587: FF              RST     0X38                
7588: FF              RST     0X38                
7589: FF              RST     0X38                
758A: FF              RST     0X38                
758B: FF              RST     0X38                
758C: FF              RST     0X38                
758D: FF              RST     0X38                
758E: FF              RST     0X38                
758F: FF              RST     0X38                
7590: FF              RST     0X38                
7591: FF              RST     0X38                
7592: FF              RST     0X38                
7593: FF              RST     0X38                
7594: FF              RST     0X38                
7595: FF              RST     0X38                
7596: FF              RST     0X38                
7597: FF              RST     0X38                
7598: FF              RST     0X38                
7599: FF              RST     0X38                
759A: FF              RST     0X38                
759B: FF              RST     0X38                
759C: FF              RST     0X38                
759D: FF              RST     0X38                
759E: FF              RST     0X38                
759F: FF              RST     0X38                
75A0: FF              RST     0X38                
75A1: FF              RST     0X38                
75A2: FF              RST     0X38                
75A3: FF              RST     0X38                
75A4: FF              RST     0X38                
75A5: FF              RST     0X38                
75A6: FF              RST     0X38                
75A7: FF              RST     0X38                
75A8: FF              RST     0X38                
75A9: FF              RST     0X38                
75AA: FF              RST     0X38                
75AB: FF              RST     0X38                
75AC: FF              RST     0X38                
75AD: FF              RST     0X38                
75AE: FF              RST     0X38                
75AF: FF              RST     0X38                
75B0: FF              RST     0X38                
75B1: FF              RST     0X38                
75B2: FF              RST     0X38                
75B3: FF              RST     0X38                
75B4: FF              RST     0X38                
75B5: FF              RST     0X38                
75B6: FF              RST     0X38                
75B7: FF              RST     0X38                
75B8: FF              RST     0X38                
75B9: FF              RST     0X38                
75BA: FF              RST     0X38                
75BB: FF              RST     0X38                
75BC: FF              RST     0X38                
75BD: FF              RST     0X38                
75BE: FF              RST     0X38                
75BF: FF              RST     0X38                
75C0: FF              RST     0X38                
75C1: FF              RST     0X38                
75C2: FF              RST     0X38                
75C3: FF              RST     0X38                
75C4: FF              RST     0X38                
75C5: FF              RST     0X38                
75C6: FF              RST     0X38                
75C7: FF              RST     0X38                
75C8: FF              RST     0X38                
75C9: FF              RST     0X38                
75CA: FF              RST     0X38                
75CB: FF              RST     0X38                
75CC: FF              RST     0X38                
75CD: FF              RST     0X38                
75CE: FF              RST     0X38                
75CF: FF              RST     0X38                
75D0: FF              RST     0X38                
75D1: FF              RST     0X38                
75D2: FF              RST     0X38                
75D3: FF              RST     0X38                
75D4: FF              RST     0X38                
75D5: FF              RST     0X38                
75D6: FF              RST     0X38                
75D7: FF              RST     0X38                
75D8: FF              RST     0X38                
75D9: FF              RST     0X38                
75DA: FF              RST     0X38                
75DB: FF              RST     0X38                
75DC: FF              RST     0X38                
75DD: FF              RST     0X38                
75DE: FF              RST     0X38                
75DF: FF              RST     0X38                
75E0: FF              RST     0X38                
75E1: FF              RST     0X38                
75E2: FF              RST     0X38                
75E3: FF              RST     0X38                
75E4: FF              RST     0X38                
75E5: FF              RST     0X38                
75E6: FF              RST     0X38                
75E7: FF              RST     0X38                
75E8: FF              RST     0X38                
75E9: FF              RST     0X38                
75EA: FF              RST     0X38                
75EB: FF              RST     0X38                
75EC: FF              RST     0X38                
75ED: FF              RST     0X38                
75EE: FF              RST     0X38                
75EF: FF              RST     0X38                
75F0: FF              RST     0X38                
75F1: FF              RST     0X38                
75F2: FF              RST     0X38                
75F3: FF              RST     0X38                
75F4: FF              RST     0X38                
75F5: FF              RST     0X38                
75F6: FF              RST     0X38                
75F7: FF              RST     0X38                
75F8: FF              RST     0X38                
75F9: FF              RST     0X38                
75FA: FF              RST     0X38                
75FB: FF              RST     0X38                
75FC: FF              RST     0X38                
75FD: FF              RST     0X38                
75FE: FF              RST     0X38                
75FF: FF              RST     0X38                
7600: FF              RST     0X38                
7601: FF              RST     0X38                
7602: FF              RST     0X38                
7603: FF              RST     0X38                
7604: FF              RST     0X38                
7605: FF              RST     0X38                
7606: FF              RST     0X38                
7607: FF              RST     0X38                
7608: FF              RST     0X38                
7609: FF              RST     0X38                
760A: FF              RST     0X38                
760B: FF              RST     0X38                
760C: FF              RST     0X38                
760D: FF              RST     0X38                
760E: FF              RST     0X38                
760F: FF              RST     0X38                
7610: FF              RST     0X38                
7611: FF              RST     0X38                
7612: FF              RST     0X38                
7613: FF              RST     0X38                
7614: FF              RST     0X38                
7615: FF              RST     0X38                
7616: FF              RST     0X38                
7617: FF              RST     0X38                
7618: FF              RST     0X38                
7619: FF              RST     0X38                
761A: FF              RST     0X38                
761B: FF              RST     0X38                
761C: FF              RST     0X38                
761D: FF              RST     0X38                
761E: FF              RST     0X38                
761F: FF              RST     0X38                
7620: FF              RST     0X38                
7621: FF              RST     0X38                
7622: FF              RST     0X38                
7623: FF              RST     0X38                
7624: FF              RST     0X38                
7625: FF              RST     0X38                
7626: FF              RST     0X38                
7627: FF              RST     0X38                
7628: FF              RST     0X38                
7629: FF              RST     0X38                
762A: FF              RST     0X38                
762B: FF              RST     0X38                
762C: FF              RST     0X38                
762D: FF              RST     0X38                
762E: FF              RST     0X38                
762F: FF              RST     0X38                
7630: FF              RST     0X38                
7631: FF              RST     0X38                
7632: FF              RST     0X38                
7633: FF              RST     0X38                
7634: FF              RST     0X38                
7635: FF              RST     0X38                
7636: FF              RST     0X38                
7637: FF              RST     0X38                
7638: FF              RST     0X38                
7639: FF              RST     0X38                
763A: FF              RST     0X38                
763B: FF              RST     0X38                
763C: FF              RST     0X38                
763D: FF              RST     0X38                
763E: FF              RST     0X38                
763F: FF              RST     0X38                
7640: FF              RST     0X38                
7641: FF              RST     0X38                
7642: FF              RST     0X38                
7643: FF              RST     0X38                
7644: FF              RST     0X38                
7645: FF              RST     0X38                
7646: FF              RST     0X38                
7647: FF              RST     0X38                
7648: FF              RST     0X38                
7649: FF              RST     0X38                
764A: FF              RST     0X38                
764B: FF              RST     0X38                
764C: FF              RST     0X38                
764D: FF              RST     0X38                
764E: FF              RST     0X38                
764F: FF              RST     0X38                
7650: FF              RST     0X38                
7651: FF              RST     0X38                
7652: FF              RST     0X38                
7653: FF              RST     0X38                
7654: FF              RST     0X38                
7655: FF              RST     0X38                
7656: FF              RST     0X38                
7657: FF              RST     0X38                
7658: FF              RST     0X38                
7659: FF              RST     0X38                
765A: FF              RST     0X38                
765B: FF              RST     0X38                
765C: FF              RST     0X38                
765D: FF              RST     0X38                
765E: FF              RST     0X38                
765F: FF              RST     0X38                
7660: FF              RST     0X38                
7661: FF              RST     0X38                
7662: FF              RST     0X38                
7663: FF              RST     0X38                
7664: FF              RST     0X38                
7665: FF              RST     0X38                
7666: FF              RST     0X38                
7667: FF              RST     0X38                
7668: FF              RST     0X38                
7669: FF              RST     0X38                
766A: FF              RST     0X38                
766B: FF              RST     0X38                
766C: FF              RST     0X38                
766D: FF              RST     0X38                
766E: FF              RST     0X38                
766F: FF              RST     0X38                
7670: FF              RST     0X38                
7671: FF              RST     0X38                
7672: FF              RST     0X38                
7673: FF              RST     0X38                
7674: FF              RST     0X38                
7675: FF              RST     0X38                
7676: FF              RST     0X38                
7677: FF              RST     0X38                
7678: FF              RST     0X38                
7679: FF              RST     0X38                
767A: FF              RST     0X38                
767B: FF              RST     0X38                
767C: FF              RST     0X38                
767D: FF              RST     0X38                
767E: FF              RST     0X38                
767F: FF              RST     0X38                
7680: FF              RST     0X38                
7681: FF              RST     0X38                
7682: FF              RST     0X38                
7683: FF              RST     0X38                
7684: FF              RST     0X38                
7685: FF              RST     0X38                
7686: FF              RST     0X38                
7687: FF              RST     0X38                
7688: FF              RST     0X38                
7689: FF              RST     0X38                
768A: FF              RST     0X38                
768B: FF              RST     0X38                
768C: FF              RST     0X38                
768D: FF              RST     0X38                
768E: FF              RST     0X38                
768F: FF              RST     0X38                
7690: FF              RST     0X38                
7691: FF              RST     0X38                
7692: FF              RST     0X38                
7693: FF              RST     0X38                
7694: FF              RST     0X38                
7695: FF              RST     0X38                
7696: FF              RST     0X38                
7697: FF              RST     0X38                
7698: FF              RST     0X38                
7699: FF              RST     0X38                
769A: FF              RST     0X38                
769B: FF              RST     0X38                
769C: FF              RST     0X38                
769D: FF              RST     0X38                
769E: FF              RST     0X38                
769F: FF              RST     0X38                
76A0: FF              RST     0X38                
76A1: FF              RST     0X38                
76A2: FF              RST     0X38                
76A3: FF              RST     0X38                
76A4: FF              RST     0X38                
76A5: FF              RST     0X38                
76A6: FF              RST     0X38                
76A7: FF              RST     0X38                
76A8: FF              RST     0X38                
76A9: FF              RST     0X38                
76AA: FF              RST     0X38                
76AB: FF              RST     0X38                
76AC: FF              RST     0X38                
76AD: FF              RST     0X38                
76AE: FF              RST     0X38                
76AF: FF              RST     0X38                
76B0: FF              RST     0X38                
76B1: FF              RST     0X38                
76B2: FF              RST     0X38                
76B3: FF              RST     0X38                
76B4: FF              RST     0X38                
76B5: FF              RST     0X38                
76B6: FF              RST     0X38                
76B7: FF              RST     0X38                
76B8: FF              RST     0X38                
76B9: FF              RST     0X38                
76BA: FF              RST     0X38                
76BB: FF              RST     0X38                
76BC: FF              RST     0X38                
76BD: FF              RST     0X38                
76BE: FF              RST     0X38                
76BF: FF              RST     0X38                
76C0: FF              RST     0X38                
76C1: FF              RST     0X38                
76C2: FF              RST     0X38                
76C3: FF              RST     0X38                
76C4: FF              RST     0X38                
76C5: FF              RST     0X38                
76C6: FF              RST     0X38                
76C7: FF              RST     0X38                
76C8: FF              RST     0X38                
76C9: FF              RST     0X38                
76CA: FF              RST     0X38                
76CB: FF              RST     0X38                
76CC: FF              RST     0X38                
76CD: FF              RST     0X38                
76CE: FF              RST     0X38                
76CF: FF              RST     0X38                
76D0: FF              RST     0X38                
76D1: FF              RST     0X38                
76D2: FF              RST     0X38                
76D3: FF              RST     0X38                
76D4: FF              RST     0X38                
76D5: FF              RST     0X38                
76D6: FF              RST     0X38                
76D7: FF              RST     0X38                
76D8: FF              RST     0X38                
76D9: FF              RST     0X38                
76DA: FF              RST     0X38                
76DB: FF              RST     0X38                
76DC: FF              RST     0X38                
76DD: FF              RST     0X38                
76DE: FF              RST     0X38                
76DF: FF              RST     0X38                
76E0: FF              RST     0X38                
76E1: FF              RST     0X38                
76E2: FF              RST     0X38                
76E3: FF              RST     0X38                
76E4: FF              RST     0X38                
76E5: FF              RST     0X38                
76E6: FF              RST     0X38                
76E7: FF              RST     0X38                
76E8: FF              RST     0X38                
76E9: FF              RST     0X38                
76EA: FF              RST     0X38                
76EB: FF              RST     0X38                
76EC: FF              RST     0X38                
76ED: FF              RST     0X38                
76EE: FF              RST     0X38                
76EF: FF              RST     0X38                
76F0: FF              RST     0X38                
76F1: FF              RST     0X38                
76F2: FF              RST     0X38                
76F3: FF              RST     0X38                
76F4: FF              RST     0X38                
76F5: FF              RST     0X38                
76F6: FF              RST     0X38                
76F7: FF              RST     0X38                
76F8: FF              RST     0X38                
76F9: FF              RST     0X38                
76FA: FF              RST     0X38                
76FB: FF              RST     0X38                
76FC: FF              RST     0X38                
76FD: FF              RST     0X38                
76FE: FF              RST     0X38                
76FF: FF              RST     0X38                
7700: FF              RST     0X38                
7701: FF              RST     0X38                
7702: FF              RST     0X38                
7703: FF              RST     0X38                
7704: FF              RST     0X38                
7705: FF              RST     0X38                
7706: FF              RST     0X38                
7707: FF              RST     0X38                
7708: FF              RST     0X38                
7709: FF              RST     0X38                
770A: FF              RST     0X38                
770B: FF              RST     0X38                
770C: FF              RST     0X38                
770D: FF              RST     0X38                
770E: FF              RST     0X38                
770F: FF              RST     0X38                
7710: FF              RST     0X38                
7711: FF              RST     0X38                
7712: FF              RST     0X38                
7713: FF              RST     0X38                
7714: FF              RST     0X38                
7715: FF              RST     0X38                
7716: FF              RST     0X38                
7717: FF              RST     0X38                
7718: FF              RST     0X38                
7719: FF              RST     0X38                
771A: FF              RST     0X38                
771B: FF              RST     0X38                
771C: FF              RST     0X38                
771D: FF              RST     0X38                
771E: FF              RST     0X38                
771F: FF              RST     0X38                
7720: FF              RST     0X38                
7721: FF              RST     0X38                
7722: FF              RST     0X38                
7723: FF              RST     0X38                
7724: FF              RST     0X38                
7725: FF              RST     0X38                
7726: FF              RST     0X38                
7727: FF              RST     0X38                
7728: FF              RST     0X38                
7729: FF              RST     0X38                
772A: FF              RST     0X38                
772B: FF              RST     0X38                
772C: FF              RST     0X38                
772D: FF              RST     0X38                
772E: FF              RST     0X38                
772F: FF              RST     0X38                
7730: FF              RST     0X38                
7731: FF              RST     0X38                
7732: FF              RST     0X38                
7733: FF              RST     0X38                
7734: FF              RST     0X38                
7735: FF              RST     0X38                
7736: FF              RST     0X38                
7737: FF              RST     0X38                
7738: FF              RST     0X38                
7739: FF              RST     0X38                
773A: FF              RST     0X38                
773B: FF              RST     0X38                
773C: FF              RST     0X38                
773D: FF              RST     0X38                
773E: FF              RST     0X38                
773F: FF              RST     0X38                
7740: FF              RST     0X38                
7741: FF              RST     0X38                
7742: FF              RST     0X38                
7743: FF              RST     0X38                
7744: FF              RST     0X38                
7745: FF              RST     0X38                
7746: FF              RST     0X38                
7747: FF              RST     0X38                
7748: FF              RST     0X38                
7749: FF              RST     0X38                
774A: FF              RST     0X38                
774B: FF              RST     0X38                
774C: FF              RST     0X38                
774D: FF              RST     0X38                
774E: FF              RST     0X38                
774F: FF              RST     0X38                
7750: FF              RST     0X38                
7751: FF              RST     0X38                
7752: FF              RST     0X38                
7753: FF              RST     0X38                
7754: FF              RST     0X38                
7755: FF              RST     0X38                
7756: FF              RST     0X38                
7757: FF              RST     0X38                
7758: FF              RST     0X38                
7759: FF              RST     0X38                
775A: FF              RST     0X38                
775B: FF              RST     0X38                
775C: FF              RST     0X38                
775D: FF              RST     0X38                
775E: FF              RST     0X38                
775F: FF              RST     0X38                
7760: FF              RST     0X38                
7761: FF              RST     0X38                
7762: FF              RST     0X38                
7763: FF              RST     0X38                
7764: FF              RST     0X38                
7765: FF              RST     0X38                
7766: FF              RST     0X38                
7767: FF              RST     0X38                
7768: FF              RST     0X38                
7769: FF              RST     0X38                
776A: FF              RST     0X38                
776B: FF              RST     0X38                
776C: FF              RST     0X38                
776D: FF              RST     0X38                
776E: FF              RST     0X38                
776F: FF              RST     0X38                
7770: FF              RST     0X38                
7771: FF              RST     0X38                
7772: FF              RST     0X38                
7773: FF              RST     0X38                
7774: FF              RST     0X38                
7775: FF              RST     0X38                
7776: FF              RST     0X38                
7777: FF              RST     0X38                
7778: FF              RST     0X38                
7779: FF              RST     0X38                
777A: FF              RST     0X38                
777B: FF              RST     0X38                
777C: FF              RST     0X38                
777D: FF              RST     0X38                
777E: FF              RST     0X38                
777F: FF              RST     0X38                
7780: FF              RST     0X38                
7781: FF              RST     0X38                
7782: FF              RST     0X38                
7783: FF              RST     0X38                
7784: FF              RST     0X38                
7785: FF              RST     0X38                
7786: FF              RST     0X38                
7787: FF              RST     0X38                
7788: FF              RST     0X38                
7789: FF              RST     0X38                
778A: FF              RST     0X38                
778B: FF              RST     0X38                
778C: FF              RST     0X38                
778D: FF              RST     0X38                
778E: FF              RST     0X38                
778F: FF              RST     0X38                
7790: FF              RST     0X38                
7791: FF              RST     0X38                
7792: FF              RST     0X38                
7793: FF              RST     0X38                
7794: FF              RST     0X38                
7795: FF              RST     0X38                
7796: FF              RST     0X38                
7797: FF              RST     0X38                
7798: FF              RST     0X38                
7799: FF              RST     0X38                
779A: FF              RST     0X38                
779B: FF              RST     0X38                
779C: FF              RST     0X38                
779D: FF              RST     0X38                
779E: FF              RST     0X38                
779F: FF              RST     0X38                
77A0: FF              RST     0X38                
77A1: FF              RST     0X38                
77A2: FF              RST     0X38                
77A3: FF              RST     0X38                
77A4: FF              RST     0X38                
77A5: FF              RST     0X38                
77A6: FF              RST     0X38                
77A7: FF              RST     0X38                
77A8: FF              RST     0X38                
77A9: FF              RST     0X38                
77AA: FF              RST     0X38                
77AB: FF              RST     0X38                
77AC: FF              RST     0X38                
77AD: FF              RST     0X38                
77AE: FF              RST     0X38                
77AF: FF              RST     0X38                
77B0: FF              RST     0X38                
77B1: FF              RST     0X38                
77B2: FF              RST     0X38                
77B3: FF              RST     0X38                
77B4: FF              RST     0X38                
77B5: FF              RST     0X38                
77B6: FF              RST     0X38                
77B7: FF              RST     0X38                
77B8: FF              RST     0X38                
77B9: FF              RST     0X38                
77BA: FF              RST     0X38                
77BB: FF              RST     0X38                
77BC: FF              RST     0X38                
77BD: FF              RST     0X38                
77BE: FF              RST     0X38                
77BF: FF              RST     0X38                
77C0: FF              RST     0X38                
77C1: FF              RST     0X38                
77C2: FF              RST     0X38                
77C3: FF              RST     0X38                
77C4: FF              RST     0X38                
77C5: FF              RST     0X38                
77C6: FF              RST     0X38                
77C7: FF              RST     0X38                
77C8: FF              RST     0X38                
77C9: FF              RST     0X38                
77CA: FF              RST     0X38                
77CB: FF              RST     0X38                
77CC: FF              RST     0X38                
77CD: FF              RST     0X38                
77CE: FF              RST     0X38                
77CF: FF              RST     0X38                
77D0: FF              RST     0X38                
77D1: FF              RST     0X38                
77D2: FF              RST     0X38                
77D3: FF              RST     0X38                
77D4: FF              RST     0X38                
77D5: FF              RST     0X38                
77D6: FF              RST     0X38                
77D7: FF              RST     0X38                
77D8: FF              RST     0X38                
77D9: FF              RST     0X38                
77DA: FF              RST     0X38                
77DB: FF              RST     0X38                
77DC: FF              RST     0X38                
77DD: FF              RST     0X38                
77DE: FF              RST     0X38                
77DF: FF              RST     0X38                
77E0: FF              RST     0X38                
77E1: FF              RST     0X38                
77E2: FF              RST     0X38                
77E3: FF              RST     0X38                
77E4: FF              RST     0X38                
77E5: FF              RST     0X38                
77E6: FF              RST     0X38                
77E7: FF              RST     0X38                
77E8: FF              RST     0X38                
77E9: FF              RST     0X38                
77EA: FF              RST     0X38                
77EB: FF              RST     0X38                
77EC: FF              RST     0X38                
77ED: FF              RST     0X38                
77EE: FF              RST     0X38                
77EF: FF              RST     0X38                
77F0: FF              RST     0X38                
77F1: FF              RST     0X38                
77F2: FF              RST     0X38                
77F3: FF              RST     0X38                
77F4: FF              RST     0X38                
77F5: FF              RST     0X38                
77F6: FF              RST     0X38                
77F7: FF              RST     0X38                
77F8: FF              RST     0X38                
77F9: FF              RST     0X38                
77FA: FF              RST     0X38                
77FB: FF              RST     0X38                
77FC: FF              RST     0X38                
77FD: FF              RST     0X38                
77FE: FF              RST     0X38                
77FF: FF              RST     0X38                
7800: FF              RST     0X38                
7801: FF              RST     0X38                
7802: FF              RST     0X38                
7803: FF              RST     0X38                
7804: FF              RST     0X38                
7805: FF              RST     0X38                
7806: FF              RST     0X38                
7807: FF              RST     0X38                
7808: FF              RST     0X38                
7809: FF              RST     0X38                
780A: FF              RST     0X38                
780B: FF              RST     0X38                
780C: FF              RST     0X38                
780D: FF              RST     0X38                
780E: FF              RST     0X38                
780F: FF              RST     0X38                
7810: FF              RST     0X38                
7811: FF              RST     0X38                
7812: FF              RST     0X38                
7813: FF              RST     0X38                
7814: FF              RST     0X38                
7815: FF              RST     0X38                
7816: FF              RST     0X38                
7817: FF              RST     0X38                
7818: FF              RST     0X38                
7819: FF              RST     0X38                
781A: FF              RST     0X38                
781B: FF              RST     0X38                
781C: FF              RST     0X38                
781D: FF              RST     0X38                
781E: FF              RST     0X38                
781F: FF              RST     0X38                
7820: FF              RST     0X38                
7821: FF              RST     0X38                
7822: FF              RST     0X38                
7823: FF              RST     0X38                
7824: FF              RST     0X38                
7825: FF              RST     0X38                
7826: FF              RST     0X38                
7827: FF              RST     0X38                
7828: FF              RST     0X38                
7829: FF              RST     0X38                
782A: FF              RST     0X38                
782B: FF              RST     0X38                
782C: FF              RST     0X38                
782D: FF              RST     0X38                
782E: FF              RST     0X38                
782F: FF              RST     0X38                
7830: FF              RST     0X38                
7831: FF              RST     0X38                
7832: FF              RST     0X38                
7833: FF              RST     0X38                
7834: FF              RST     0X38                
7835: FF              RST     0X38                
7836: FF              RST     0X38                
7837: FF              RST     0X38                
7838: FF              RST     0X38                
7839: FF              RST     0X38                
783A: FF              RST     0X38                
783B: FF              RST     0X38                
783C: FF              RST     0X38                
783D: FF              RST     0X38                
783E: FF              RST     0X38                
783F: FF              RST     0X38                
7840: FF              RST     0X38                
7841: FF              RST     0X38                
7842: FF              RST     0X38                
7843: FF              RST     0X38                
7844: FF              RST     0X38                
7845: FF              RST     0X38                
7846: FF              RST     0X38                
7847: FF              RST     0X38                
7848: FF              RST     0X38                
7849: FF              RST     0X38                
784A: FF              RST     0X38                
784B: FF              RST     0X38                
784C: FF              RST     0X38                
784D: FF              RST     0X38                
784E: FF              RST     0X38                
784F: FF              RST     0X38                
7850: FF              RST     0X38                
7851: FF              RST     0X38                
7852: FF              RST     0X38                
7853: FF              RST     0X38                
7854: FF              RST     0X38                
7855: FF              RST     0X38                
7856: FF              RST     0X38                
7857: FF              RST     0X38                
7858: FF              RST     0X38                
7859: FF              RST     0X38                
785A: FF              RST     0X38                
785B: FF              RST     0X38                
785C: FF              RST     0X38                
785D: FF              RST     0X38                
785E: FF              RST     0X38                
785F: FF              RST     0X38                
7860: FF              RST     0X38                
7861: FF              RST     0X38                
7862: FF              RST     0X38                
7863: FF              RST     0X38                
7864: FF              RST     0X38                
7865: FF              RST     0X38                
7866: FF              RST     0X38                
7867: FF              RST     0X38                
7868: FF              RST     0X38                
7869: FF              RST     0X38                
786A: FF              RST     0X38                
786B: FF              RST     0X38                
786C: FF              RST     0X38                
786D: FF              RST     0X38                
786E: FF              RST     0X38                
786F: FF              RST     0X38                
7870: FF              RST     0X38                
7871: FF              RST     0X38                
7872: FF              RST     0X38                
7873: FF              RST     0X38                
7874: FF              RST     0X38                
7875: FF              RST     0X38                
7876: FF              RST     0X38                
7877: FF              RST     0X38                
7878: FF              RST     0X38                
7879: FF              RST     0X38                
787A: FF              RST     0X38                
787B: FF              RST     0X38                
787C: FF              RST     0X38                
787D: FF              RST     0X38                
787E: FF              RST     0X38                
787F: FF              RST     0X38                
7880: FF              RST     0X38                
7881: FF              RST     0X38                
7882: FF              RST     0X38                
7883: FF              RST     0X38                
7884: FF              RST     0X38                
7885: FF              RST     0X38                
7886: FF              RST     0X38                
7887: FF              RST     0X38                
7888: FF              RST     0X38                
7889: FF              RST     0X38                
788A: FF              RST     0X38                
788B: FF              RST     0X38                
788C: FF              RST     0X38                
788D: FF              RST     0X38                
788E: FF              RST     0X38                
788F: FF              RST     0X38                
7890: FF              RST     0X38                
7891: FF              RST     0X38                
7892: FF              RST     0X38                
7893: FF              RST     0X38                
7894: FF              RST     0X38                
7895: FF              RST     0X38                
7896: FF              RST     0X38                
7897: FF              RST     0X38                
7898: FF              RST     0X38                
7899: FF              RST     0X38                
789A: FF              RST     0X38                
789B: FF              RST     0X38                
789C: FF              RST     0X38                
789D: FF              RST     0X38                
789E: FF              RST     0X38                
789F: FF              RST     0X38                
78A0: FF              RST     0X38                
78A1: FF              RST     0X38                
78A2: FF              RST     0X38                
78A3: FF              RST     0X38                
78A4: FF              RST     0X38                
78A5: FF              RST     0X38                
78A6: FF              RST     0X38                
78A7: FF              RST     0X38                
78A8: FF              RST     0X38                
78A9: FF              RST     0X38                
78AA: FF              RST     0X38                
78AB: FF              RST     0X38                
78AC: FF              RST     0X38                
78AD: FF              RST     0X38                
78AE: FF              RST     0X38                
78AF: FF              RST     0X38                
78B0: FF              RST     0X38                
78B1: FF              RST     0X38                
78B2: FF              RST     0X38                
78B3: FF              RST     0X38                
78B4: FF              RST     0X38                
78B5: FF              RST     0X38                
78B6: FF              RST     0X38                
78B7: FF              RST     0X38                
78B8: FF              RST     0X38                
78B9: FF              RST     0X38                
78BA: FF              RST     0X38                
78BB: FF              RST     0X38                
78BC: FF              RST     0X38                
78BD: FF              RST     0X38                
78BE: FF              RST     0X38                
78BF: FF              RST     0X38                
78C0: FF              RST     0X38                
78C1: FF              RST     0X38                
78C2: FF              RST     0X38                
78C3: FF              RST     0X38                
78C4: FF              RST     0X38                
78C5: FF              RST     0X38                
78C6: FF              RST     0X38                
78C7: FF              RST     0X38                
78C8: FF              RST     0X38                
78C9: FF              RST     0X38                
78CA: FF              RST     0X38                
78CB: FF              RST     0X38                
78CC: FF              RST     0X38                
78CD: FF              RST     0X38                
78CE: FF              RST     0X38                
78CF: FF              RST     0X38                
78D0: FF              RST     0X38                
78D1: FF              RST     0X38                
78D2: FF              RST     0X38                
78D3: FF              RST     0X38                
78D4: FF              RST     0X38                
78D5: FF              RST     0X38                
78D6: FF              RST     0X38                
78D7: FF              RST     0X38                
78D8: FF              RST     0X38                
78D9: FF              RST     0X38                
78DA: FF              RST     0X38                
78DB: FF              RST     0X38                
78DC: FF              RST     0X38                
78DD: FF              RST     0X38                
78DE: FF              RST     0X38                
78DF: FF              RST     0X38                
78E0: FF              RST     0X38                
78E1: FF              RST     0X38                
78E2: FF              RST     0X38                
78E3: FF              RST     0X38                
78E4: FF              RST     0X38                
78E5: FF              RST     0X38                
78E6: FF              RST     0X38                
78E7: FF              RST     0X38                
78E8: FF              RST     0X38                
78E9: FF              RST     0X38                
78EA: FF              RST     0X38                
78EB: FF              RST     0X38                
78EC: FF              RST     0X38                
78ED: FF              RST     0X38                
78EE: FF              RST     0X38                
78EF: FF              RST     0X38                
78F0: FF              RST     0X38                
78F1: FF              RST     0X38                
78F2: FF              RST     0X38                
78F3: FF              RST     0X38                
78F4: FF              RST     0X38                
78F5: FF              RST     0X38                
78F6: FF              RST     0X38                
78F7: FF              RST     0X38                
78F8: FF              RST     0X38                
78F9: FF              RST     0X38                
78FA: FF              RST     0X38                
78FB: FF              RST     0X38                
78FC: FF              RST     0X38                
78FD: FF              RST     0X38                
78FE: FF              RST     0X38                
78FF: FF              RST     0X38                
7900: FF              RST     0X38                
7901: FF              RST     0X38                
7902: FF              RST     0X38                
7903: FF              RST     0X38                
7904: FF              RST     0X38                
7905: FF              RST     0X38                
7906: FF              RST     0X38                
7907: FF              RST     0X38                
7908: FF              RST     0X38                
7909: FF              RST     0X38                
790A: FF              RST     0X38                
790B: FF              RST     0X38                
790C: FF              RST     0X38                
790D: FF              RST     0X38                
790E: FF              RST     0X38                
790F: FF              RST     0X38                
7910: FF              RST     0X38                
7911: FF              RST     0X38                
7912: FF              RST     0X38                
7913: FF              RST     0X38                
7914: FF              RST     0X38                
7915: FF              RST     0X38                
7916: FF              RST     0X38                
7917: FF              RST     0X38                
7918: FF              RST     0X38                
7919: FF              RST     0X38                
791A: FF              RST     0X38                
791B: FF              RST     0X38                
791C: FF              RST     0X38                
791D: FF              RST     0X38                
791E: FF              RST     0X38                
791F: FF              RST     0X38                
7920: FF              RST     0X38                
7921: FF              RST     0X38                
7922: FF              RST     0X38                
7923: FF              RST     0X38                
7924: FF              RST     0X38                
7925: FF              RST     0X38                
7926: FF              RST     0X38                
7927: FF              RST     0X38                
7928: FF              RST     0X38                
7929: FF              RST     0X38                
792A: FF              RST     0X38                
792B: FF              RST     0X38                
792C: FF              RST     0X38                
792D: FF              RST     0X38                
792E: FF              RST     0X38                
792F: FF              RST     0X38                
7930: FF              RST     0X38                
7931: FF              RST     0X38                
7932: FF              RST     0X38                
7933: FF              RST     0X38                
7934: FF              RST     0X38                
7935: FF              RST     0X38                
7936: FF              RST     0X38                
7937: FF              RST     0X38                
7938: FF              RST     0X38                
7939: FF              RST     0X38                
793A: FF              RST     0X38                
793B: FF              RST     0X38                
793C: FF              RST     0X38                
793D: FF              RST     0X38                
793E: FF              RST     0X38                
793F: FF              RST     0X38                
7940: FF              RST     0X38                
7941: FF              RST     0X38                
7942: FF              RST     0X38                
7943: FF              RST     0X38                
7944: FF              RST     0X38                
7945: FF              RST     0X38                
7946: FF              RST     0X38                
7947: FF              RST     0X38                
7948: FF              RST     0X38                
7949: FF              RST     0X38                
794A: FF              RST     0X38                
794B: FF              RST     0X38                
794C: FF              RST     0X38                
794D: FF              RST     0X38                
794E: FF              RST     0X38                
794F: FF              RST     0X38                
7950: FF              RST     0X38                
7951: FF              RST     0X38                
7952: FF              RST     0X38                
7953: FF              RST     0X38                
7954: FF              RST     0X38                
7955: FF              RST     0X38                
7956: FF              RST     0X38                
7957: FF              RST     0X38                
7958: FF              RST     0X38                
7959: FF              RST     0X38                
795A: FF              RST     0X38                
795B: FF              RST     0X38                
795C: FF              RST     0X38                
795D: FF              RST     0X38                
795E: FF              RST     0X38                
795F: FF              RST     0X38                
7960: FF              RST     0X38                
7961: FF              RST     0X38                
7962: FF              RST     0X38                
7963: FF              RST     0X38                
7964: FF              RST     0X38                
7965: FF              RST     0X38                
7966: FF              RST     0X38                
7967: FF              RST     0X38                
7968: FF              RST     0X38                
7969: FF              RST     0X38                
796A: FF              RST     0X38                
796B: FF              RST     0X38                
796C: FF              RST     0X38                
796D: FF              RST     0X38                
796E: FF              RST     0X38                
796F: FF              RST     0X38                
7970: FF              RST     0X38                
7971: FF              RST     0X38                
7972: FF              RST     0X38                
7973: FF              RST     0X38                
7974: FF              RST     0X38                
7975: FF              RST     0X38                
7976: FF              RST     0X38                
7977: FF              RST     0X38                
7978: FF              RST     0X38                
7979: FF              RST     0X38                
797A: FF              RST     0X38                
797B: FF              RST     0X38                
797C: FF              RST     0X38                
797D: FF              RST     0X38                
797E: FF              RST     0X38                
797F: FF              RST     0X38                
7980: FF              RST     0X38                
7981: FF              RST     0X38                
7982: FF              RST     0X38                
7983: FF              RST     0X38                
7984: FF              RST     0X38                
7985: FF              RST     0X38                
7986: FF              RST     0X38                
7987: FF              RST     0X38                
7988: FF              RST     0X38                
7989: FF              RST     0X38                
798A: FF              RST     0X38                
798B: FF              RST     0X38                
798C: FF              RST     0X38                
798D: FF              RST     0X38                
798E: FF              RST     0X38                
798F: FF              RST     0X38                
7990: FF              RST     0X38                
7991: FF              RST     0X38                
7992: FF              RST     0X38                
7993: FF              RST     0X38                
7994: FF              RST     0X38                
7995: FF              RST     0X38                
7996: FF              RST     0X38                
7997: FF              RST     0X38                
7998: FF              RST     0X38                
7999: FF              RST     0X38                
799A: FF              RST     0X38                
799B: FF              RST     0X38                
799C: FF              RST     0X38                
799D: FF              RST     0X38                
799E: FF              RST     0X38                
799F: FF              RST     0X38                
79A0: FF              RST     0X38                
79A1: FF              RST     0X38                
79A2: FF              RST     0X38                
79A3: FF              RST     0X38                
79A4: FF              RST     0X38                
79A5: FF              RST     0X38                
79A6: FF              RST     0X38                
79A7: FF              RST     0X38                
79A8: FF              RST     0X38                
79A9: FF              RST     0X38                
79AA: FF              RST     0X38                
79AB: FF              RST     0X38                
79AC: FF              RST     0X38                
79AD: FF              RST     0X38                
79AE: FF              RST     0X38                
79AF: FF              RST     0X38                
79B0: FF              RST     0X38                
79B1: FF              RST     0X38                
79B2: FF              RST     0X38                
79B3: FF              RST     0X38                
79B4: FF              RST     0X38                
79B5: FF              RST     0X38                
79B6: FF              RST     0X38                
79B7: FF              RST     0X38                
79B8: FF              RST     0X38                
79B9: FF              RST     0X38                
79BA: FF              RST     0X38                
79BB: FF              RST     0X38                
79BC: FF              RST     0X38                
79BD: FF              RST     0X38                
79BE: FF              RST     0X38                
79BF: FF              RST     0X38                
79C0: FF              RST     0X38                
79C1: FF              RST     0X38                
79C2: FF              RST     0X38                
79C3: FF              RST     0X38                
79C4: FF              RST     0X38                
79C5: FF              RST     0X38                
79C6: FF              RST     0X38                
79C7: FF              RST     0X38                
79C8: FF              RST     0X38                
79C9: FF              RST     0X38                
79CA: FF              RST     0X38                
79CB: FF              RST     0X38                
79CC: FF              RST     0X38                
79CD: FF              RST     0X38                
79CE: FF              RST     0X38                
79CF: FF              RST     0X38                
79D0: FF              RST     0X38                
79D1: FF              RST     0X38                
79D2: FF              RST     0X38                
79D3: FF              RST     0X38                
79D4: FF              RST     0X38                
79D5: FF              RST     0X38                
79D6: FF              RST     0X38                
79D7: FF              RST     0X38                
79D8: FF              RST     0X38                
79D9: FF              RST     0X38                
79DA: FF              RST     0X38                
79DB: FF              RST     0X38                
79DC: FF              RST     0X38                
79DD: FF              RST     0X38                
79DE: FF              RST     0X38                
79DF: FF              RST     0X38                
79E0: FF              RST     0X38                
79E1: FF              RST     0X38                
79E2: FF              RST     0X38                
79E3: FF              RST     0X38                
79E4: FF              RST     0X38                
79E5: FF              RST     0X38                
79E6: FF              RST     0X38                
79E7: FF              RST     0X38                
79E8: FF              RST     0X38                
79E9: FF              RST     0X38                
79EA: FF              RST     0X38                
79EB: FF              RST     0X38                
79EC: FF              RST     0X38                
79ED: FF              RST     0X38                
79EE: FF              RST     0X38                
79EF: FF              RST     0X38                
79F0: FF              RST     0X38                
79F1: FF              RST     0X38                
79F2: FF              RST     0X38                
79F3: FF              RST     0X38                
79F4: FF              RST     0X38                
79F5: FF              RST     0X38                
79F6: FF              RST     0X38                
79F7: FF              RST     0X38                
79F8: FF              RST     0X38                
79F9: FF              RST     0X38                
79FA: FF              RST     0X38                
79FB: FF              RST     0X38                
79FC: FF              RST     0X38                
79FD: FF              RST     0X38                
79FE: FF              RST     0X38                
79FF: FF              RST     0X38                
7A00: FF              RST     0X38                
7A01: FF              RST     0X38                
7A02: FF              RST     0X38                
7A03: FF              RST     0X38                
7A04: FF              RST     0X38                
7A05: FF              RST     0X38                
7A06: FF              RST     0X38                
7A07: FF              RST     0X38                
7A08: FF              RST     0X38                
7A09: FF              RST     0X38                
7A0A: FF              RST     0X38                
7A0B: FF              RST     0X38                
7A0C: FF              RST     0X38                
7A0D: FF              RST     0X38                
7A0E: FF              RST     0X38                
7A0F: FF              RST     0X38                
7A10: FF              RST     0X38                
7A11: FF              RST     0X38                
7A12: FF              RST     0X38                
7A13: FF              RST     0X38                
7A14: FF              RST     0X38                
7A15: FF              RST     0X38                
7A16: FF              RST     0X38                
7A17: FF              RST     0X38                
7A18: FF              RST     0X38                
7A19: FF              RST     0X38                
7A1A: FF              RST     0X38                
7A1B: FF              RST     0X38                
7A1C: FF              RST     0X38                
7A1D: FF              RST     0X38                
7A1E: FF              RST     0X38                
7A1F: FF              RST     0X38                
7A20: FF              RST     0X38                
7A21: FF              RST     0X38                
7A22: FF              RST     0X38                
7A23: FF              RST     0X38                
7A24: FF              RST     0X38                
7A25: FF              RST     0X38                
7A26: FF              RST     0X38                
7A27: FF              RST     0X38                
7A28: FF              RST     0X38                
7A29: FF              RST     0X38                
7A2A: FF              RST     0X38                
7A2B: FF              RST     0X38                
7A2C: FF              RST     0X38                
7A2D: FF              RST     0X38                
7A2E: FF              RST     0X38                
7A2F: FF              RST     0X38                
7A30: FF              RST     0X38                
7A31: FF              RST     0X38                
7A32: FF              RST     0X38                
7A33: FF              RST     0X38                
7A34: FF              RST     0X38                
7A35: FF              RST     0X38                
7A36: FF              RST     0X38                
7A37: FF              RST     0X38                
7A38: FF              RST     0X38                
7A39: FF              RST     0X38                
7A3A: FF              RST     0X38                
7A3B: FF              RST     0X38                
7A3C: FF              RST     0X38                
7A3D: FF              RST     0X38                
7A3E: FF              RST     0X38                
7A3F: FF              RST     0X38                
7A40: FF              RST     0X38                
7A41: FF              RST     0X38                
7A42: FF              RST     0X38                
7A43: FF              RST     0X38                
7A44: FF              RST     0X38                
7A45: FF              RST     0X38                
7A46: FF              RST     0X38                
7A47: FF              RST     0X38                
7A48: FF              RST     0X38                
7A49: FF              RST     0X38                
7A4A: FF              RST     0X38                
7A4B: FF              RST     0X38                
7A4C: FF              RST     0X38                
7A4D: FF              RST     0X38                
7A4E: FF              RST     0X38                
7A4F: FF              RST     0X38                
7A50: FF              RST     0X38                
7A51: FF              RST     0X38                
7A52: FF              RST     0X38                
7A53: FF              RST     0X38                
7A54: FF              RST     0X38                
7A55: FF              RST     0X38                
7A56: FF              RST     0X38                
7A57: FF              RST     0X38                
7A58: FF              RST     0X38                
7A59: FF              RST     0X38                
7A5A: FF              RST     0X38                
7A5B: FF              RST     0X38                
7A5C: FF              RST     0X38                
7A5D: FF              RST     0X38                
7A5E: FF              RST     0X38                
7A5F: FF              RST     0X38                
7A60: FF              RST     0X38                
7A61: FF              RST     0X38                
7A62: FF              RST     0X38                
7A63: FF              RST     0X38                
7A64: FF              RST     0X38                
7A65: FF              RST     0X38                
7A66: FF              RST     0X38                
7A67: FF              RST     0X38                
7A68: FF              RST     0X38                
7A69: FF              RST     0X38                
7A6A: FF              RST     0X38                
7A6B: FF              RST     0X38                
7A6C: FF              RST     0X38                
7A6D: FF              RST     0X38                
7A6E: FF              RST     0X38                
7A6F: FF              RST     0X38                
7A70: FF              RST     0X38                
7A71: FF              RST     0X38                
7A72: FF              RST     0X38                
7A73: FF              RST     0X38                
7A74: FF              RST     0X38                
7A75: FF              RST     0X38                
7A76: FF              RST     0X38                
7A77: FF              RST     0X38                
7A78: FF              RST     0X38                
7A79: FF              RST     0X38                
7A7A: FF              RST     0X38                
7A7B: FF              RST     0X38                
7A7C: FF              RST     0X38                
7A7D: FF              RST     0X38                
7A7E: FF              RST     0X38                
7A7F: FF              RST     0X38                
7A80: FF              RST     0X38                
7A81: FF              RST     0X38                
7A82: FF              RST     0X38                
7A83: FF              RST     0X38                
7A84: FF              RST     0X38                
7A85: FF              RST     0X38                
7A86: FF              RST     0X38                
7A87: FF              RST     0X38                
7A88: FF              RST     0X38                
7A89: FF              RST     0X38                
7A8A: FF              RST     0X38                
7A8B: FF              RST     0X38                
7A8C: FF              RST     0X38                
7A8D: FF              RST     0X38                
7A8E: FF              RST     0X38                
7A8F: FF              RST     0X38                
7A90: FF              RST     0X38                
7A91: FF              RST     0X38                
7A92: FF              RST     0X38                
7A93: FF              RST     0X38                
7A94: FF              RST     0X38                
7A95: FF              RST     0X38                
7A96: FF              RST     0X38                
7A97: FF              RST     0X38                
7A98: FF              RST     0X38                
7A99: FF              RST     0X38                
7A9A: FF              RST     0X38                
7A9B: FF              RST     0X38                
7A9C: FF              RST     0X38                
7A9D: FF              RST     0X38                
7A9E: FF              RST     0X38                
7A9F: FF              RST     0X38                
7AA0: FF              RST     0X38                
7AA1: FF              RST     0X38                
7AA2: FF              RST     0X38                
7AA3: FF              RST     0X38                
7AA4: FF              RST     0X38                
7AA5: FF              RST     0X38                
7AA6: FF              RST     0X38                
7AA7: FF              RST     0X38                
7AA8: FF              RST     0X38                
7AA9: FF              RST     0X38                
7AAA: FF              RST     0X38                
7AAB: FF              RST     0X38                
7AAC: FF              RST     0X38                
7AAD: FF              RST     0X38                
7AAE: FF              RST     0X38                
7AAF: FF              RST     0X38                
7AB0: FF              RST     0X38                
7AB1: FF              RST     0X38                
7AB2: FF              RST     0X38                
7AB3: FF              RST     0X38                
7AB4: FF              RST     0X38                
7AB5: FF              RST     0X38                
7AB6: FF              RST     0X38                
7AB7: FF              RST     0X38                
7AB8: FF              RST     0X38                
7AB9: FF              RST     0X38                
7ABA: FF              RST     0X38                
7ABB: FF              RST     0X38                
7ABC: FF              RST     0X38                
7ABD: FF              RST     0X38                
7ABE: FF              RST     0X38                
7ABF: FF              RST     0X38                
7AC0: FF              RST     0X38                
7AC1: FF              RST     0X38                
7AC2: FF              RST     0X38                
7AC3: FF              RST     0X38                
7AC4: FF              RST     0X38                
7AC5: FF              RST     0X38                
7AC6: FF              RST     0X38                
7AC7: FF              RST     0X38                
7AC8: FF              RST     0X38                
7AC9: FF              RST     0X38                
7ACA: FF              RST     0X38                
7ACB: FF              RST     0X38                
7ACC: FF              RST     0X38                
7ACD: FF              RST     0X38                
7ACE: FF              RST     0X38                
7ACF: FF              RST     0X38                
7AD0: FF              RST     0X38                
7AD1: FF              RST     0X38                
7AD2: FF              RST     0X38                
7AD3: FF              RST     0X38                
7AD4: FF              RST     0X38                
7AD5: FF              RST     0X38                
7AD6: FF              RST     0X38                
7AD7: FF              RST     0X38                
7AD8: FF              RST     0X38                
7AD9: FF              RST     0X38                
7ADA: FF              RST     0X38                
7ADB: FF              RST     0X38                
7ADC: FF              RST     0X38                
7ADD: FF              RST     0X38                
7ADE: FF              RST     0X38                
7ADF: FF              RST     0X38                
7AE0: FF              RST     0X38                
7AE1: FF              RST     0X38                
7AE2: FF              RST     0X38                
7AE3: FF              RST     0X38                
7AE4: FF              RST     0X38                
7AE5: FF              RST     0X38                
7AE6: FF              RST     0X38                
7AE7: FF              RST     0X38                
7AE8: FF              RST     0X38                
7AE9: FF              RST     0X38                
7AEA: FF              RST     0X38                
7AEB: FF              RST     0X38                
7AEC: FF              RST     0X38                
7AED: FF              RST     0X38                
7AEE: FF              RST     0X38                
7AEF: FF              RST     0X38                
7AF0: FF              RST     0X38                
7AF1: FF              RST     0X38                
7AF2: FF              RST     0X38                
7AF3: FF              RST     0X38                
7AF4: FF              RST     0X38                
7AF5: FF              RST     0X38                
7AF6: FF              RST     0X38                
7AF7: FF              RST     0X38                
7AF8: FF              RST     0X38                
7AF9: FF              RST     0X38                
7AFA: FF              RST     0X38                
7AFB: FF              RST     0X38                
7AFC: FF              RST     0X38                
7AFD: FF              RST     0X38                
7AFE: FF              RST     0X38                
7AFF: FF              RST     0X38                
7B00: FF              RST     0X38                
7B01: FF              RST     0X38                
7B02: FF              RST     0X38                
7B03: FF              RST     0X38                
7B04: FF              RST     0X38                
7B05: FF              RST     0X38                
7B06: FF              RST     0X38                
7B07: FF              RST     0X38                
7B08: FF              RST     0X38                
7B09: FF              RST     0X38                
7B0A: FF              RST     0X38                
7B0B: FF              RST     0X38                
7B0C: FF              RST     0X38                
7B0D: FF              RST     0X38                
7B0E: FF              RST     0X38                
7B0F: FF              RST     0X38                
7B10: FF              RST     0X38                
7B11: FF              RST     0X38                
7B12: FF              RST     0X38                
7B13: FF              RST     0X38                
7B14: FF              RST     0X38                
7B15: FF              RST     0X38                
7B16: FF              RST     0X38                
7B17: FF              RST     0X38                
7B18: FF              RST     0X38                
7B19: FF              RST     0X38                
7B1A: FF              RST     0X38                
7B1B: FF              RST     0X38                
7B1C: FF              RST     0X38                
7B1D: FF              RST     0X38                
7B1E: FF              RST     0X38                
7B1F: FF              RST     0X38                
7B20: FF              RST     0X38                
7B21: FF              RST     0X38                
7B22: FF              RST     0X38                
7B23: FF              RST     0X38                
7B24: FF              RST     0X38                
7B25: FF              RST     0X38                
7B26: FF              RST     0X38                
7B27: FF              RST     0X38                
7B28: FF              RST     0X38                
7B29: FF              RST     0X38                
7B2A: FF              RST     0X38                
7B2B: FF              RST     0X38                
7B2C: FF              RST     0X38                
7B2D: FF              RST     0X38                
7B2E: FF              RST     0X38                
7B2F: FF              RST     0X38                
7B30: FF              RST     0X38                
7B31: FF              RST     0X38                
7B32: FF              RST     0X38                
7B33: FF              RST     0X38                
7B34: FF              RST     0X38                
7B35: FF              RST     0X38                
7B36: FF              RST     0X38                
7B37: FF              RST     0X38                
7B38: FF              RST     0X38                
7B39: FF              RST     0X38                
7B3A: FF              RST     0X38                
7B3B: FF              RST     0X38                
7B3C: FF              RST     0X38                
7B3D: FF              RST     0X38                
7B3E: FF              RST     0X38                
7B3F: FF              RST     0X38                
7B40: FF              RST     0X38                
7B41: FF              RST     0X38                
7B42: FF              RST     0X38                
7B43: FF              RST     0X38                
7B44: FF              RST     0X38                
7B45: FF              RST     0X38                
7B46: FF              RST     0X38                
7B47: FF              RST     0X38                
7B48: FF              RST     0X38                
7B49: FF              RST     0X38                
7B4A: FF              RST     0X38                
7B4B: FF              RST     0X38                
7B4C: FF              RST     0X38                
7B4D: FF              RST     0X38                
7B4E: FF              RST     0X38                
7B4F: FF              RST     0X38                
7B50: FF              RST     0X38                
7B51: FF              RST     0X38                
7B52: FF              RST     0X38                
7B53: FF              RST     0X38                
7B54: FF              RST     0X38                
7B55: FF              RST     0X38                
7B56: FF              RST     0X38                
7B57: FF              RST     0X38                
7B58: FF              RST     0X38                
7B59: FF              RST     0X38                
7B5A: FF              RST     0X38                
7B5B: FF              RST     0X38                
7B5C: FF              RST     0X38                
7B5D: FF              RST     0X38                
7B5E: FF              RST     0X38                
7B5F: FF              RST     0X38                
7B60: FF              RST     0X38                
7B61: FF              RST     0X38                
7B62: FF              RST     0X38                
7B63: FF              RST     0X38                
7B64: FF              RST     0X38                
7B65: FF              RST     0X38                
7B66: FF              RST     0X38                
7B67: FF              RST     0X38                
7B68: FF              RST     0X38                
7B69: FF              RST     0X38                
7B6A: FF              RST     0X38                
7B6B: FF              RST     0X38                
7B6C: FF              RST     0X38                
7B6D: FF              RST     0X38                
7B6E: FF              RST     0X38                
7B6F: FF              RST     0X38                
7B70: FF              RST     0X38                
7B71: FF              RST     0X38                
7B72: FF              RST     0X38                
7B73: FF              RST     0X38                
7B74: FF              RST     0X38                
7B75: FF              RST     0X38                
7B76: FF              RST     0X38                
7B77: FF              RST     0X38                
7B78: FF              RST     0X38                
7B79: FF              RST     0X38                
7B7A: FF              RST     0X38                
7B7B: FF              RST     0X38                
7B7C: FF              RST     0X38                
7B7D: FF              RST     0X38                
7B7E: FF              RST     0X38                
7B7F: FF              RST     0X38                
7B80: FF              RST     0X38                
7B81: FF              RST     0X38                
7B82: FF              RST     0X38                
7B83: FF              RST     0X38                
7B84: FF              RST     0X38                
7B85: FF              RST     0X38                
7B86: FF              RST     0X38                
7B87: FF              RST     0X38                
7B88: FF              RST     0X38                
7B89: FF              RST     0X38                
7B8A: FF              RST     0X38                
7B8B: FF              RST     0X38                
7B8C: FF              RST     0X38                
7B8D: FF              RST     0X38                
7B8E: FF              RST     0X38                
7B8F: FF              RST     0X38                
7B90: FF              RST     0X38                
7B91: FF              RST     0X38                
7B92: FF              RST     0X38                
7B93: FF              RST     0X38                
7B94: FF              RST     0X38                
7B95: FF              RST     0X38                
7B96: FF              RST     0X38                
7B97: FF              RST     0X38                
7B98: FF              RST     0X38                
7B99: FF              RST     0X38                
7B9A: FF              RST     0X38                
7B9B: FF              RST     0X38                
7B9C: FF              RST     0X38                
7B9D: FF              RST     0X38                
7B9E: FF              RST     0X38                
7B9F: FF              RST     0X38                
7BA0: FF              RST     0X38                
7BA1: FF              RST     0X38                
7BA2: FF              RST     0X38                
7BA3: FF              RST     0X38                
7BA4: FF              RST     0X38                
7BA5: FF              RST     0X38                
7BA6: FF              RST     0X38                
7BA7: FF              RST     0X38                
7BA8: FF              RST     0X38                
7BA9: FF              RST     0X38                
7BAA: FF              RST     0X38                
7BAB: FF              RST     0X38                
7BAC: FF              RST     0X38                
7BAD: FF              RST     0X38                
7BAE: FF              RST     0X38                
7BAF: FF              RST     0X38                
7BB0: FF              RST     0X38                
7BB1: FF              RST     0X38                
7BB2: FF              RST     0X38                
7BB3: FF              RST     0X38                
7BB4: FF              RST     0X38                
7BB5: FF              RST     0X38                
7BB6: FF              RST     0X38                
7BB7: FF              RST     0X38                
7BB8: FF              RST     0X38                
7BB9: FF              RST     0X38                
7BBA: FF              RST     0X38                
7BBB: FF              RST     0X38                
7BBC: FF              RST     0X38                
7BBD: FF              RST     0X38                
7BBE: FF              RST     0X38                
7BBF: FF              RST     0X38                
7BC0: FF              RST     0X38                
7BC1: FF              RST     0X38                
7BC2: FF              RST     0X38                
7BC3: FF              RST     0X38                
7BC4: FF              RST     0X38                
7BC5: FF              RST     0X38                
7BC6: FF              RST     0X38                
7BC7: FF              RST     0X38                
7BC8: FF              RST     0X38                
7BC9: FF              RST     0X38                
7BCA: FF              RST     0X38                
7BCB: FF              RST     0X38                
7BCC: FF              RST     0X38                
7BCD: FF              RST     0X38                
7BCE: FF              RST     0X38                
7BCF: FF              RST     0X38                
7BD0: FF              RST     0X38                
7BD1: FF              RST     0X38                
7BD2: FF              RST     0X38                
7BD3: FF              RST     0X38                
7BD4: FF              RST     0X38                
7BD5: FF              RST     0X38                
7BD6: FF              RST     0X38                
7BD7: FF              RST     0X38                
7BD8: FF              RST     0X38                
7BD9: FF              RST     0X38                
7BDA: FF              RST     0X38                
7BDB: FF              RST     0X38                
7BDC: FF              RST     0X38                
7BDD: FF              RST     0X38                
7BDE: FF              RST     0X38                
7BDF: FF              RST     0X38                
7BE0: FF              RST     0X38                
7BE1: FF              RST     0X38                
7BE2: FF              RST     0X38                
7BE3: FF              RST     0X38                
7BE4: FF              RST     0X38                
7BE5: FF              RST     0X38                
7BE6: FF              RST     0X38                
7BE7: FF              RST     0X38                
7BE8: FF              RST     0X38                
7BE9: FF              RST     0X38                
7BEA: FF              RST     0X38                
7BEB: FF              RST     0X38                
7BEC: FF              RST     0X38                
7BED: FF              RST     0X38                
7BEE: FF              RST     0X38                
7BEF: FF              RST     0X38                
7BF0: FF              RST     0X38                
7BF1: FF              RST     0X38                
7BF2: FF              RST     0X38                
7BF3: FF              RST     0X38                
7BF4: FF              RST     0X38                
7BF5: FF              RST     0X38                
7BF6: FF              RST     0X38                
7BF7: FF              RST     0X38                
7BF8: FF              RST     0X38                
7BF9: FF              RST     0X38                
7BFA: FF              RST     0X38                
7BFB: FF              RST     0X38                
7BFC: FF              RST     0X38                
7BFD: FF              RST     0X38                
7BFE: FF              RST     0X38                
7BFF: FF              RST     0X38                
7C00: FF              RST     0X38                
7C01: FF              RST     0X38                
7C02: FF              RST     0X38                
7C03: FF              RST     0X38                
7C04: FF              RST     0X38                
7C05: FF              RST     0X38                
7C06: FF              RST     0X38                
7C07: FF              RST     0X38                
7C08: FF              RST     0X38                
7C09: FF              RST     0X38                
7C0A: FF              RST     0X38                
7C0B: FF              RST     0X38                
7C0C: FF              RST     0X38                
7C0D: FF              RST     0X38                
7C0E: FF              RST     0X38                
7C0F: FF              RST     0X38                
7C10: FF              RST     0X38                
7C11: FF              RST     0X38                
7C12: FF              RST     0X38                
7C13: FF              RST     0X38                
7C14: FF              RST     0X38                
7C15: FF              RST     0X38                
7C16: FF              RST     0X38                
7C17: FF              RST     0X38                
7C18: FF              RST     0X38                
7C19: FF              RST     0X38                
7C1A: FF              RST     0X38                
7C1B: FF              RST     0X38                
7C1C: FF              RST     0X38                
7C1D: FF              RST     0X38                
7C1E: FF              RST     0X38                
7C1F: FF              RST     0X38                
7C20: FF              RST     0X38                
7C21: FF              RST     0X38                
7C22: FF              RST     0X38                
7C23: FF              RST     0X38                
7C24: FF              RST     0X38                
7C25: FF              RST     0X38                
7C26: FF              RST     0X38                
7C27: FF              RST     0X38                
7C28: FF              RST     0X38                
7C29: FF              RST     0X38                
7C2A: FF              RST     0X38                
7C2B: FF              RST     0X38                
7C2C: FF              RST     0X38                
7C2D: FF              RST     0X38                
7C2E: FF              RST     0X38                
7C2F: FF              RST     0X38                
7C30: FF              RST     0X38                
7C31: FF              RST     0X38                
7C32: FF              RST     0X38                
7C33: FF              RST     0X38                
7C34: FF              RST     0X38                
7C35: FF              RST     0X38                
7C36: FF              RST     0X38                
7C37: FF              RST     0X38                
7C38: FF              RST     0X38                
7C39: FF              RST     0X38                
7C3A: FF              RST     0X38                
7C3B: FF              RST     0X38                
7C3C: FF              RST     0X38                
7C3D: FF              RST     0X38                
7C3E: FF              RST     0X38                
7C3F: FF              RST     0X38                
7C40: FF              RST     0X38                
7C41: FF              RST     0X38                
7C42: FF              RST     0X38                
7C43: FF              RST     0X38                
7C44: FF              RST     0X38                
7C45: FF              RST     0X38                
7C46: FF              RST     0X38                
7C47: FF              RST     0X38                
7C48: FF              RST     0X38                
7C49: FF              RST     0X38                
7C4A: FF              RST     0X38                
7C4B: FF              RST     0X38                
7C4C: FF              RST     0X38                
7C4D: FF              RST     0X38                
7C4E: FF              RST     0X38                
7C4F: FF              RST     0X38                
7C50: FF              RST     0X38                
7C51: FF              RST     0X38                
7C52: FF              RST     0X38                
7C53: FF              RST     0X38                
7C54: FF              RST     0X38                
7C55: FF              RST     0X38                
7C56: FF              RST     0X38                
7C57: FF              RST     0X38                
7C58: FF              RST     0X38                
7C59: FF              RST     0X38                
7C5A: FF              RST     0X38                
7C5B: FF              RST     0X38                
7C5C: FF              RST     0X38                
7C5D: FF              RST     0X38                
7C5E: FF              RST     0X38                
7C5F: FF              RST     0X38                
7C60: FF              RST     0X38                
7C61: FF              RST     0X38                
7C62: FF              RST     0X38                
7C63: FF              RST     0X38                
7C64: FF              RST     0X38                
7C65: FF              RST     0X38                
7C66: FF              RST     0X38                
7C67: FF              RST     0X38                
7C68: FF              RST     0X38                
7C69: FF              RST     0X38                
7C6A: FF              RST     0X38                
7C6B: FF              RST     0X38                
7C6C: FF              RST     0X38                
7C6D: FF              RST     0X38                
7C6E: FF              RST     0X38                
7C6F: FF              RST     0X38                
7C70: FF              RST     0X38                
7C71: FF              RST     0X38                
7C72: FF              RST     0X38                
7C73: FF              RST     0X38                
7C74: FF              RST     0X38                
7C75: FF              RST     0X38                
7C76: FF              RST     0X38                
7C77: FF              RST     0X38                
7C78: FF              RST     0X38                
7C79: FF              RST     0X38                
7C7A: FF              RST     0X38                
7C7B: FF              RST     0X38                
7C7C: FF              RST     0X38                
7C7D: FF              RST     0X38                
7C7E: FF              RST     0X38                
7C7F: FF              RST     0X38                
7C80: FF              RST     0X38                
7C81: FF              RST     0X38                
7C82: FF              RST     0X38                
7C83: FF              RST     0X38                
7C84: FF              RST     0X38                
7C85: FF              RST     0X38                
7C86: FF              RST     0X38                
7C87: FF              RST     0X38                
7C88: FF              RST     0X38                
7C89: FF              RST     0X38                
7C8A: FF              RST     0X38                
7C8B: FF              RST     0X38                
7C8C: FF              RST     0X38                
7C8D: FF              RST     0X38                
7C8E: FF              RST     0X38                
7C8F: FF              RST     0X38                
7C90: FF              RST     0X38                
7C91: FF              RST     0X38                
7C92: FF              RST     0X38                
7C93: FF              RST     0X38                
7C94: FF              RST     0X38                
7C95: FF              RST     0X38                
7C96: FF              RST     0X38                
7C97: FF              RST     0X38                
7C98: FF              RST     0X38                
7C99: FF              RST     0X38                
7C9A: FF              RST     0X38                
7C9B: FF              RST     0X38                
7C9C: FF              RST     0X38                
7C9D: FF              RST     0X38                
7C9E: FF              RST     0X38                
7C9F: FF              RST     0X38                
7CA0: FF              RST     0X38                
7CA1: FF              RST     0X38                
7CA2: FF              RST     0X38                
7CA3: FF              RST     0X38                
7CA4: FF              RST     0X38                
7CA5: FF              RST     0X38                
7CA6: FF              RST     0X38                
7CA7: FF              RST     0X38                
7CA8: FF              RST     0X38                
7CA9: FF              RST     0X38                
7CAA: FF              RST     0X38                
7CAB: FF              RST     0X38                
7CAC: FF              RST     0X38                
7CAD: FF              RST     0X38                
7CAE: FF              RST     0X38                
7CAF: FF              RST     0X38                
7CB0: FF              RST     0X38                
7CB1: FF              RST     0X38                
7CB2: FF              RST     0X38                
7CB3: FF              RST     0X38                
7CB4: FF              RST     0X38                
7CB5: FF              RST     0X38                
7CB6: FF              RST     0X38                
7CB7: FF              RST     0X38                
7CB8: FF              RST     0X38                
7CB9: FF              RST     0X38                
7CBA: FF              RST     0X38                
7CBB: FF              RST     0X38                
7CBC: FF              RST     0X38                
7CBD: FF              RST     0X38                
7CBE: FF              RST     0X38                
7CBF: FF              RST     0X38                
7CC0: FF              RST     0X38                
7CC1: FF              RST     0X38                
7CC2: FF              RST     0X38                
7CC3: FF              RST     0X38                
7CC4: FF              RST     0X38                
7CC5: FF              RST     0X38                
7CC6: FF              RST     0X38                
7CC7: FF              RST     0X38                
7CC8: FF              RST     0X38                
7CC9: FF              RST     0X38                
7CCA: FF              RST     0X38                
7CCB: FF              RST     0X38                
7CCC: FF              RST     0X38                
7CCD: FF              RST     0X38                
7CCE: FF              RST     0X38                
7CCF: FF              RST     0X38                
7CD0: FF              RST     0X38                
7CD1: FF              RST     0X38                
7CD2: FF              RST     0X38                
7CD3: FF              RST     0X38                
7CD4: FF              RST     0X38                
7CD5: FF              RST     0X38                
7CD6: FF              RST     0X38                
7CD7: FF              RST     0X38                
7CD8: FF              RST     0X38                
7CD9: FF              RST     0X38                
7CDA: FF              RST     0X38                
7CDB: FF              RST     0X38                
7CDC: FF              RST     0X38                
7CDD: FF              RST     0X38                
7CDE: FF              RST     0X38                
7CDF: FF              RST     0X38                
7CE0: FF              RST     0X38                
7CE1: FF              RST     0X38                
7CE2: FF              RST     0X38                
7CE3: FF              RST     0X38                
7CE4: FF              RST     0X38                
7CE5: FF              RST     0X38                
7CE6: FF              RST     0X38                
7CE7: FF              RST     0X38                
7CE8: FF              RST     0X38                
7CE9: FF              RST     0X38                
7CEA: FF              RST     0X38                
7CEB: FF              RST     0X38                
7CEC: FF              RST     0X38                
7CED: FF              RST     0X38                
7CEE: FF              RST     0X38                
7CEF: FF              RST     0X38                
7CF0: FF              RST     0X38                
7CF1: FF              RST     0X38                
7CF2: FF              RST     0X38                
7CF3: FF              RST     0X38                
7CF4: FF              RST     0X38                
7CF5: FF              RST     0X38                
7CF6: FF              RST     0X38                
7CF7: FF              RST     0X38                
7CF8: FF              RST     0X38                
7CF9: FF              RST     0X38                
7CFA: FF              RST     0X38                
7CFB: FF              RST     0X38                
7CFC: FF              RST     0X38                
7CFD: FF              RST     0X38                
7CFE: FF              RST     0X38                
7CFF: FF              RST     0X38                
7D00: FF              RST     0X38                
7D01: FF              RST     0X38                
7D02: FF              RST     0X38                
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

