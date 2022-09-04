![Bank 0E](GBZelda.jpg)

# Bank 0E

>>> cpu Z80GB

>>> binary 4000:roms/zelda.gb[38000:3C000]

>>> memoryTable ram 

[RAM Usage](RAMUse.md)

>>> memoryTable hard 

[Hardware Info](../Hardware.md)

```code
4000: 02              LD      (BC),A              
4001: 00              NOP                         
4002: 07              RLCA                        
4003: 02              LD      (BC),A              
4004: 0F              RRCA                        
4005: 06 0A           LD      B,$0A               
4007: 07              RLCA                        
4008: 05              DEC     B                   
4009: 02              LD      (BC),A              
400A: 03              INC     BC                  
400B: 01 03 01        LD      BC,$0103            
400E: 07              RLCA                        
400F: 00              NOP                         
4010: 07              RLCA                        
4011: 02              LD      (BC),A              
4012: 0F              RRCA                        
4013: 05              DEC     B                   
4014: 0B              DEC     BC                  
4015: 04              INC     B                   
4016: 0F              RRCA                        
4017: 02              LD      (BC),A              
4018: 07              RLCA                        
4019: 02              LD      (BC),A              
401A: 07              RLCA                        
401B: 00              NOP                         
401C: 05              DEC     B                   
401D: 03              INC     BC                  
401E: 02              LD      (BC),A              
401F: 01 00 00        LD      BC,$0000            
4022: 00              NOP                         
4023: 00              NOP                         
4024: 3C              INC     A                   
4025: 00              NOP                         
4026: FF              RST     0X38                
4027: 00              NOP                         
4028: FD                              
4029: 8E              ADC     A,(HL)              
402A: FE DF           CP      $DF                 
402C: FE 57           CP      $57                 
402E: FD                              
402F: 0E FF           LD      C,$FF               
4031: 30 FF           JR      NC,$4032            ; {}
4033: FD                              
4034: FF              RST     0X38                
4035: 02              LD      (BC),A              
4036: FF              RST     0X38                
4037: 06 FF           LD      B,$FF               
4039: 06 FF           LD      B,$FF               
403B: F1              POP     AF                  
403C: FE FF           CP      $FF                 
403E: 77              LD      (HL),A              
403F: F8 40           LD      HL,SP+$40           
4041: 00              NOP                         
4042: E0 40           LD      ($FF00+$40),A       
4044: F0 60           LD      A,($60)             
4046: D0              RET     NC                  
4047: E0 A0           LD      ($FF00+$A0),A       
4049: 40              LD      B,B                 
404A: C0              RET     NZ                  
404B: 00              NOP                         
404C: E0 00           LD      ($FF00+$00),A       
404E: F0 20           LD      A,($20)             
4050: D0              RET     NC                  
4051: 60              LD      H,B                 
4052: E0 00           LD      ($FF00+$00),A       
4054: E0 80           LD      ($FF00+$80),A       
4056: E0 80           LD      ($FF00+$80),A       
4058: C0              RET     NZ                  
4059: 80              ADD     A,B                 
405A: 40              LD      B,B                 
405B: 80              ADD     A,B                 
405C: 80              ADD     A,B                 
405D: 00              NOP                         
405E: 00              NOP                         
405F: 00              NOP                         
4060: 00              NOP                         
4061: 00              NOP                         
4062: 01 00 03        LD      BC,$0300            
4065: 00              NOP                         
4066: 07              RLCA                        
4067: 00              NOP                         
4068: 0F              RRCA                        
4069: 00              NOP                         
406A: 17              RLA                         
406B: 08 27 18        LD      ($1827),SP          
406E: 2F              CPL                         
406F: 10 27           ;;STOP    $27                 
4071: 1C              INC     E                   
4072: 23              INC     HL                  
4073: 1C              INC     E                   
4074: 17              RLA                         
4075: 08 0F 00        LD      ($000F),SP          
4078: 04              INC     B                   
4079: 03              INC     BC                  
407A: 07              RLCA                        
407B: 00              NOP                         
407C: 0F              RRCA                        
407D: 05              DEC     B                   
407E: 0F              RRCA                        
407F: 00              NOP                         
4080: 7E              LD      A,(HL)              
4081: 00              NOP                         
4082: FF              RST     0X38                
4083: 00              NOP                         
4084: FF              RST     0X38                
4085: 00              NOP                         
4086: FF              RST     0X38                
4087: 00              NOP                         
4088: FF              RST     0X38                
4089: 00              NOP                         
408A: FF              RST     0X38                
408B: 00              NOP                         
408C: FF              RST     0X38                
408D: 00              NOP                         
408E: FF              RST     0X38                
408F: 00              NOP                         
4090: FF              RST     0X38                
4091: 00              NOP                         
4092: AF              XOR     A                   
4093: 70              LD      (HL),B              
4094: 8F              ADC     A,A                 
4095: 70              LD      (HL),B              
4096: FF              RST     0X38                
4097: 00              NOP                         
4098: 00              NOP                         
4099: FF              RST     0X38                
409A: 9E              SBC     (HL)                
409B: 61              LD      H,C                 
409C: CA B1 FB        JP      Z,$FBB1             
409F: 00              NOP                         
40A0: 00              NOP                         
40A1: 00              NOP                         
40A2: 80              ADD     A,B                 
40A3: 00              NOP                         
40A4: F8 00           LD      HL,SP+$00           
40A6: C4 38 C2        CALL    NZ,$C238            
40A9: 3C              INC     A                   
40AA: E2              LD      (C),A               
40AB: 1C              INC     E                   
40AC: D2 6C D2        JP      NC,$D26C            
40AF: 2C              INC     L                   
40B0: 82              ADD     A,D                 
40B1: FC                              
40B2: 06 F8           LD      B,$F8               
40B4: 8E              ADC     A,(HL)              
40B5: 70              LD      (HL),B              
40B6: FC                              
40B7: 00              NOP                         
40B8: 08 F0 3C        LD      ($3CF0),SP          
40BB: C0              RET     NZ                  
40BC: 7E              LD      A,(HL)              
40BD: B4              OR      H                   
40BE: FE 00           CP      $00                 
40C0: 70              LD      (HL),B              
40C1: 00              NOP                         
40C2: 98              SBC     B                   
40C3: 70              LD      (HL),B              
40C4: 89              ADC     A,C                 
40C5: 70              LD      (HL),B              
40C6: 9F              SBC     A                   
40C7: 60              LD      H,B                 
40C8: 8F              ADC     A,A                 
40C9: 70              LD      (HL),B              
40CA: 4F              LD      C,A                 
40CB: 30 47           JR      NC,$4114            ; {}
40CD: 38 27           JR      C,$40F6             ; {}
40CF: 18 1F           JR      $40F0               ; {}
40D1: 00              NOP                         
40D2: 0F              RRCA                        
40D3: 00              NOP                         
40D4: 0F              RRCA                        
40D5: 00              NOP                         
40D6: 0F              RRCA                        
40D7: 00              NOP                         
40D8: 04              INC     B                   
40D9: 03              INC     BC                  
40DA: 07              RLCA                        
40DB: 00              NOP                         
40DC: 0F              RRCA                        
40DD: 05              DEC     B                   
40DE: 0F              RRCA                        
40DF: 00              NOP                         
40E0: 0E 00           LD      C,$00               
40E2: 9D              SBC     L                   
40E3: 0E F5           LD      C,$F5               
40E5: 0E E9           LD      C,$E9               
40E7: 16 E7           LD      D,$E7               
40E9: 18 E2           JR      $40CD               ; {}
40EB: 1C              INC     E                   
40EC: F2                              
40ED: 0C              INC     C                   
40EE: FC                              
40EF: 00              NOP                         
40F0: FE 00           CP      $00                 
40F2: FE 00           CP      $00                 
40F4: FE 00           CP      $00                 
40F6: FC                              
40F7: 00              NOP                         
40F8: 08 F0 3C        LD      ($3CF0),SP          
40FB: C0              RET     NZ                  
40FC: 7E              LD      A,(HL)              
40FD: B4              OR      H                   
40FE: FE 00           CP      $00                 
4100: 0C              INC     C                   
4101: 00              NOP                         
4102: 1E 0C           LD      E,$0C               
4104: 3E 0C           LD      A,$0C               
4106: 3F              CCF                         
4107: 14              INC     D                   
4108: 3E 11           LD      A,$11               
410A: 3F              CCF                         
410B: 18 2F           JR      $413C               ; {}
410D: 1C              INC     E                   
410E: 1F              RRA                         
410F: 0C              INC     C                   
4110: 3F              CCF                         
4111: 04              INC     B                   
4112: 5F              LD      E,A                 
4113: 20 5F           JR      NZ,$4174            ; {}
4115: 20 E7           JR      NZ,$40FE            ; {}
4117: 18 F9           JR      $4112               ; {}
4119: 87              ADD     A,A                 
411A: FF              RST     0X38                
411B: 80              ADD     A,B                 
411C: 7F              LD      A,A                 
411D: 70              LD      (HL),B              
411E: 1F              RRA                         
411F: 19              ADD     HL,DE               
4120: 01 00 63        LD      BC,$6300            
4123: 01 73 21        LD      BC,$2173            
4126: 7B              LD      A,E                 
4127: 20 7F           JR      NZ,$41A8            ; {}
4129: 31 7F 31        LD      SP,$317F            
412C: 5F              LD      E,A                 
412D: 31 2F 11        LD      SP,$112F            
4130: 3E 01           LD      A,$01               
4132: DF              RST     0X18                
4133: 20 DF           JR      NZ,$4114            ; {}
4135: A0              AND     B                   
4136: E7              RST     0X20                
4137: 98              SBC     B                   
4138: F9              LD      SP,HL               
4139: 07              RLCA                        
413A: FF              RST     0X38                
413B: C0              RET     NZ                  
413C: 7F              LD      A,A                 
413D: 60              LD      H,B                 
413E: 3F              CCF                         
413F: 36 00           LD      (HL),$00            
4141: 00              NOP                         
4142: 00              NOP                         
4143: 00              NOP                         
4144: 00              NOP                         
4145: 00              NOP                         
4146: 00              NOP                         
4147: 00              NOP                         
4148: 00              NOP                         
4149: 00              NOP                         
414A: 06 00           LD      B,$00               
414C: 0E 04           LD      C,$04               
414E: 3E 04           LD      A,$04               
4150: 3F              CCF                         
4151: 14              INC     D                   
4152: 3E 11           LD      A,$11               
4154: 3F              CCF                         
4155: 18 6F           JR      $41C6               ; {}
4157: 1C              INC     E                   
4158: F7              RST     0X30                
4159: 6C              LD      L,H                 
415A: FB              EI                          
415B: E4                              
415C: FF              RST     0X38                
415D: D0              RET     NC                  
415E: 7F              LD      A,A                 
415F: 78              LD      A,B                 
4160: 00              NOP                         
4161: 00              NOP                         
4162: 00              NOP                         
4163: 00              NOP                         
4164: 00              NOP                         
4165: 00              NOP                         
4166: 00              NOP                         
4167: 00              NOP                         
4168: 00              NOP                         
4169: 00              NOP                         
416A: 00              NOP                         
416B: 00              NOP                         
416C: 00              NOP                         
416D: 00              NOP                         
416E: 00              NOP                         
416F: 00              NOP                         
4170: 0E 00           LD      C,$00               
4172: 3F              CCF                         
4173: 2E 3F           LD      L,$3F               
4175: 2D              DEC     L                   
4176: 7F              LD      A,A                 
4177: 31 7F 36        LD      SP,$367F            
417A: 7F              LD      A,A                 
417B: 4D              LD      C,L                 
417C: 3F              CCF                         
417D: 39              ADD     HL,SP               
417E: 0F              RRCA                        
417F: 0E 00           LD      C,$00               
4181: 00              NOP                         
4182: 38 00           JR      C,$4184             ; {}
4184: 7C              LD      A,H                 
4185: 38 FC           JR      C,$4183             ; {}
4187: 70              LD      (HL),B              
4188: FE 74           CP      $74                 
418A: FE 74           CP      $74                 
418C: FE 74           CP      $74                 
418E: BA              CP      D                   
418F: 6C              LD      L,H                 
4190: 57              LD      D,A                 
4191: 38 2F           JR      C,$41C2             ; {}
4193: 12              LD      (DE),A              
4194: 1F              RRA                         
4195: 02              LD      (BC),A              
4196: 35              DEC     (HL)                
4197: 0A              LD      A,(BC)              
4198: 76              HALT                        
4199: 2D              DEC     L                   
419A: F3              DI                          
419B: 6F              LD      L,A                 
419C: F8 47           LD      HL,SP+$47           
419E: FF              RST     0X38                
419F: 00              NOP                         
41A0: 1C              INC     E                   
41A1: 00              NOP                         
41A2: 3E 1C           LD      A,$1C               
41A4: 7E              LD      A,(HL)              
41A5: 38 7F           JR      C,$4226             ; {}
41A7: 3A              LD      A,(HLD)             
41A8: 7F              LD      A,A                 
41A9: 3A              LD      A,(HLD)             
41AA: 7F              LD      A,A                 
41AB: 3A              LD      A,(HLD)             
41AC: 5D              LD      E,L                 
41AD: 36 2B           LD      (HL),$2B            
41AF: 1C              INC     E                   
41B0: 2F              CPL                         
41B1: 12              LD      (DE),A              
41B2: 1F              RRA                         
41B3: 02              LD      (BC),A              
41B4: 15              DEC     D                   
41B5: 0A              LD      A,(BC)              
41B6: 36 0D           LD      (HL),$0D            
41B8: 73              LD      (HL),E              
41B9: 2F              CPL                         
41BA: 78              LD      A,B                 
41BB: 37              SCF                         
41BC: 7F              LD      A,A                 
41BD: 20 7F           JR      NZ,$423E            ; {}
41BF: 00              NOP                         
41C0: 00              NOP                         
41C1: 00              NOP                         
41C2: 61              LD      H,C                 
41C3: 00              NOP                         
41C4: 71              LD      (HL),C              
41C5: 20 3F           JR      NZ,$4206            ; {}
41C7: 10 1F           ;;STOP    $1F                 
41C9: 00              NOP                         
41CA: 14              INC     D                   
41CB: 0F              RRCA                        
41CC: 6F              LD      L,A                 
41CD: 1B              DEC     DE                  
41CE: EF              RST     0X28                
41CF: 5B              LD      E,E                 
41D0: 6F              LD      L,A                 
41D1: 1B              DEC     DE                  
41D2: 14              INC     D                   
41D3: 0F              RRCA                        
41D4: 1F              RRA                         
41D5: 00              NOP                         
41D6: 3F              CCF                         
41D7: 10 6F           ;;STOP    $6F                 
41D9: 30 F3           JR      NC,$41CE            ; {}
41DB: 41              LD      B,C                 
41DC: C3 01 01        JP      $0101               
41DF: 00              NOP                         
41E0: 80              ADD     A,B                 
41E1: 00              NOP                         
41E2: C3 80 CF        JP      $CF80               
41E5: 82              ADD     A,D                 
41E6: FE 0C           CP      $0C                 
41E8: F4                              
41E9: 18 B8           JR      $41A3               ; {}
41EB: C0              RET     NZ                  
41EC: D8              RET     C                   
41ED: 60              LD      H,B                 
41EE: DE 60           SBC     $60                 
41F0: DF              RST     0X18                
41F1: 6E              LD      L,(HL)              
41F2: BE              CP      (HL)                
41F3: C0              RET     NZ                  
41F4: F8 00           LD      HL,SP+$00           
41F6: F8 10           LD      HL,SP+$10           
41F8: EC                              
41F9: 18 9E           JR      $4199               ; {}
41FB: 04              INC     B                   
41FC: 86              ADD     A,(HL)              
41FD: 00              NOP                         
41FE: 00              NOP                         
41FF: 00              NOP                         
4200: E7              RST     0X20                
4201: 00              NOP                         
4202: 3C              INC     A                   
4203: 03              INC     BC                  
4204: 3E 1D           LD      A,$1D               
4206: FE 15           CP      $15                 
4208: BE              CP      (HL)                
4209: 1D              DEC     E                   
420A: 3C              INC     A                   
420B: 03              INC     BC                  
420C: 3F              CCF                         
420D: 18 3F           JR      $424E               ; {}
420F: 01 77 38        LD      BC,$3877            
4212: 82              ADD     A,D                 
4213: 7D              LD      A,L                 
4214: AB              XOR     E                   
4215: 54              LD      D,H                 
4216: 7E              LD      A,(HL)              
4217: 01 20 1F        LD      BC,$1F20            
421A: 23              INC     HL                  
421B: 1C              INC     E                   
421C: 1F              RRA                         
421D: 00              NOP                         
421E: 07              RLCA                        
421F: 00              NOP                         
4220: DC 00 30        CALL    C,$3000             
4223: C0              RET     NZ                  
4224: 1E E0           LD      E,$E0               
4226: CA 30 88        JP      Z,$8830             
4229: 70              LD      (HL),B              
422A: 3C              INC     A                   
422B: C0              RET     NZ                  
422C: EE 1C           XOR     $1C                 
422E: C1              POP     BC                  
422F: BE              CP      (HL)                
4230: D5              PUSH    DE                  
4231: 2A              LD      A,(HLI)             
4232: 7E              LD      A,(HL)              
4233: 80              ADD     A,B                 
4234: C4 38 04        CALL    NZ,$0438            
4237: F8 08           LD      HL,SP+$08           
4239: F0 84           LD      A,($84)             
423B: 78              LD      A,B                 
423C: C4 38 FC        CALL    NZ,$FC38            
423F: 00              NOP                         
4240: 73              LD      (HL),E              
4241: 00              NOP                         
4242: 1E 01           LD      E,$01               
4244: 1F              RRA                         
4245: 0E 7F           LD      C,$7F               
4247: 0A              LD      A,(BC)              
4248: 5F              LD      E,A                 
4249: 0E 3E           LD      C,$3E               
424B: 01 77 38        LD      BC,$3877            
424E: 83              ADD     A,E                 
424F: 7C              LD      A,H                 
4250: AB              XOR     E                   
4251: 54              LD      D,H                 
4252: 7E              LD      A,(HL)              
4253: 01 23 1C        LD      BC,$1C23            
4256: 20 1F           JR      NZ,$4277            ; {}
4258: 10 0F           ;;STOP    $0F                 
425A: 21 1E 23        LD      HL,$231E            
425D: 1C              INC     E                   
425E: 3F              CCF                         
425F: 00              NOP                         
4260: EE 00           XOR     $00                 
4262: 18 E0           JR      $4244               ; {}
4264: 0F              RRCA                        
4265: F0 65           LD      A,($65)             
4267: 98              SBC     B                   
4268: 44              LD      B,H                 
4269: B8              CP      B                   
426A: 1C              INC     E                   
426B: E0 FC           LD      ($FF00+$FC),A       
426D: 08 FC D8        LD      ($D8FC),SP          
4270: FC                              
4271: 00              NOP                         
4272: 2E DC           LD      L,$DC               
4274: C1              POP     BC                  
4275: 3E 55           LD      A,$55               
4277: AA              XOR     D                   
4278: 3E C0           LD      A,$C0               
427A: 84              ADD     A,H                 
427B: 78              LD      A,B                 
427C: F8 00           LD      HL,SP+$00           
427E: E0 00           LD      ($FF00+$00),A       
4280: 00              NOP                         
4281: 00              NOP                         
4282: 00              NOP                         
4283: 00              NOP                         
4284: 00              NOP                         
4285: 00              NOP                         
4286: 00              NOP                         
4287: 00              NOP                         
4288: 00              NOP                         
4289: 00              NOP                         
428A: E7              RST     0X20                
428B: 00              NOP                         
428C: 38 07           JR      C,$4295             ; {}
428E: 20 1F           JR      NZ,$42AF            ; {}
4290: 3C              INC     A                   
4291: 03              INC     BC                  
4292: FE 1D           CP      $1D                 
4294: BE              CP      (HL)                
4295: 15              DEC     D                   
4296: 3E 05           LD      A,$05               
4298: 75              LD      (HL),L              
4299: 3A              LD      A,(HLD)             
429A: 83              ADD     A,E                 
429B: 7C              LD      A,H                 
429C: AB              XOR     E                   
429D: 54              LD      D,H                 
429E: 7C              LD      A,H                 
429F: 00              NOP                         
42A0: 00              NOP                         
42A1: 00              NOP                         
42A2: 00              NOP                         
42A3: 00              NOP                         
42A4: 00              NOP                         
42A5: 00              NOP                         
42A6: 00              NOP                         
42A7: 00              NOP                         
42A8: 00              NOP                         
42A9: 00              NOP                         
42AA: 9C              SBC     H                   
42AB: 00              NOP                         
42AC: 70              LD      (HL),B              
42AD: 80              ADD     A,B                 
42AE: 1E E0           LD      E,$E0               
42B0: 0A              LD      A,(BC)              
42B1: F0 C8           LD      A,($C8)             
42B3: 30 88           JR      NC,$423D            ; {}
42B5: 70              LD      (HL),B              
42B6: 38 C0           JR      C,$4278             ; {}
42B8: DC 38 82        CALL    C,$8238             
42BB: 7C              LD      A,H                 
42BC: AA              XOR     D                   
42BD: 54              LD      D,H                 
42BE: 7C              LD      A,H                 
42BF: 00              NOP                         
42C0: 00              NOP                         
42C1: 00              NOP                         
42C2: 00              NOP                         
42C3: 00              NOP                         
42C4: 00              NOP                         
42C5: 00              NOP                         
42C6: 00              NOP                         
42C7: 00              NOP                         
42C8: 00              NOP                         
42C9: 00              NOP                         
42CA: 00              NOP                         
42CB: 00              NOP                         
42CC: 00              NOP                         
42CD: 00              NOP                         
42CE: 00              NOP                         
42CF: 00              NOP                         
42D0: 00              NOP                         
42D1: 00              NOP                         
42D2: 14              INC     D                   
42D3: 00              NOP                         
42D4: 6A              LD      L,D                 
42D5: 14              INC     D                   
42D6: AA              XOR     D                   
42D7: 54              LD      D,H                 
42D8: C2 3C 96        JP      NZ,$963C            
42DB: 68              LD      L,B                 
42DC: 69              LD      L,C                 
42DD: 00              NOP                         
42DE: 00              NOP                         
42DF: 00              NOP                         
42E0: 0F              RRCA                        
42E1: 00              NOP                         
42E2: 1F              RRA                         
42E3: 0F              RRCA                        
42E4: 3F              CCF                         
42E5: 1F              RRA                         
42E6: 30 1F           JR      NC,$4307            ; {}
42E8: 27              DAA                         
42E9: 18 2F           JR      $431A               ; {}
42EB: 13              INC     DE                  
42EC: 2F              CPL                         
42ED: 10 6F           ;;STOP    $6F                 
42EF: 16 EF           LD      D,$EF               
42F1: 50              LD      D,B                 
42F2: EF              RST     0X28                
42F3: 55              LD      D,L                 
42F4: EF              RST     0X28                
42F5: 50              LD      D,B                 
42F6: E0 5F           LD      ($FF00+$5F),A       
42F8: FF              RST     0X38                
42F9: 40              LD      B,B                 
42FA: FF              RST     0X38                
42FB: 7F              LD      A,A                 
42FC: 98              SBC     B                   
42FD: 67              LD      H,A                 
42FE: FF              RST     0X38                
42FF: 98              SBC     B                   
4300: 73              LD      (HL),E              
4301: 00              NOP                         
4302: FF              RST     0X38                
4303: 73              LD      (HL),E              
4304: 7F              LD      A,A                 
4305: 3F              CCF                         
4306: 3F              CCF                         
4307: 07              RLCA                        
4308: 1F              RRA                         
4309: 0B              DEC     BC                  
430A: 3F              CCF                         
430B: 08 7F 27        LD      ($277F),SP          
430E: FF              RST     0X38                
430F: 6F              LD      L,A                 
4310: FF              RST     0X38                
4311: 6D              LD      L,L                 
4312: 9F              SBC     A                   
4313: 67              LD      H,A                 
4314: 7F              LD      A,A                 
4315: 00              NOP                         
4316: 3B              DEC     SP                  
4317: 07              RLCA                        
4318: 3F              CCF                         
4319: 00              NOP                         
431A: 3F              CCF                         
431B: 1C              INC     E                   
431C: 7F              LD      A,A                 
431D: 2C              INC     L                   
431E: 7E              LD      A,(HL)              
431F: 00              NOP                         
4320: CC 00 FE        CALL    Z,$FE00             
4323: CC FF FE        CALL    Z,$FEFF             
4326: DF              RST     0X18                
4327: E0 B8           LD      ($FF00+$B8),A       
4329: D0              RET     NC                  
432A: FC                              
432B: 10 EE           ;;STOP    $EE                 
432D: B4              OR      H                   
432E: FF              RST     0X38                
432F: C6 DF           ADD     $DF                 
4331: 62              LD      H,D                 
4332: FF              RST     0X38                
4333: CE FD           ADC     $FD                 
4335: 0E B2           LD      C,$B2               
4337: CC FC 00        CALL    Z,$00FC             
433A: A4              AND     H                   
433B: 58              LD      E,B                 
433C: FC                              
433D: 00              NOP                         
433E: 00              NOP                         
433F: 00              NOP                         
4340: 03              INC     BC                  
4341: 00              NOP                         
4342: 7F              LD      A,A                 
4343: 03              INC     BC                  
4344: FF              RST     0X38                
4345: 7F              LD      A,A                 
4346: 5F              LD      E,A                 
4347: 2F              CPL                         
4348: 3F              CCF                         
4349: 00              NOP                         
434A: 17              RLA                         
434B: 0F              RRCA                        
434C: 27              DAA                         
434D: 18 7F           JR      $43CE               ; {}
434F: 00              NOP                         
4350: FF              RST     0X38                
4351: 40              LD      B,B                 
4352: FF              RST     0X38                
4353: 40              LD      B,B                 
4354: A7              AND     A                   
4355: 58              LD      E,B                 
4356: 70              LD      (HL),B              
4357: 0F              RRCA                        
4358: 3F              CCF                         
4359: 00              NOP                         
435A: 27              DAA                         
435B: 18 3F           JR      $439C               ; {}
435D: 00              NOP                         
435E: 00              NOP                         
435F: 00              NOP                         
4360: C0              RET     NZ                  
4361: 00              NOP                         
4362: EC                              
4363: C0              RET     NZ                  
4364: FE EC           CP      $EC                 
4366: FF              RST     0X38                
4367: FE EE           CP      $EE                 
4369: 10 DC           ;;STOP    $DC                 
436B: E0 CC           LD      ($FF00+$CC),A       
436D: 30 FE           JR      NC,$436D            ; {}
436F: 04              INC     B                   
4370: FB              EI                          
4371: 06 FD           LD      B,$FD               
4373: 02              LD      (BC),A              
4374: CE 30           ADC     $30                 
4376: 1C              INC     E                   
4377: E0 FC           LD      ($FF00+$FC),A       
4379: 00              NOP                         
437A: FC                              
437B: 18 FE           JR      $437B               ; {}
437D: 3C              INC     A                   
437E: 7E              LD      A,(HL)              
437F: 00              NOP                         
4380: 03              INC     BC                  
4381: 00              NOP                         
4382: 07              RLCA                        
4383: 03              INC     BC                  
4384: 6F              LD      L,A                 
4385: 07              RLCA                        
4386: FF              RST     0X38                
4387: 64              LD      H,H                 
4388: FF              RST     0X38                
4389: 71              LD      (HL),C              
438A: FF              RST     0X38                
438B: 5B              LD      E,E                 
438C: BF              CP      A                   
438D: 7C              LD      A,H                 
438E: 7F              LD      A,A                 
438F: 0F              RRCA                        
4390: 5E              LD      E,(HL)              
4391: 3F              CCF                         
4392: 37              SCF                         
4393: 08 0F 07        LD      ($070F),SP          
4396: 0F              RRCA                        
4397: 07              RLCA                        
4398: 0A              LD      A,(BC)              
4399: 07              RLCA                        
439A: 07              RLCA                        
439B: 00              NOP                         
439C: 03              INC     BC                  
439D: 01 07 00        LD      BC,$0007            
43A0: DC 00 FE        CALL    C,$FE00             
43A3: DC FF FE        CALL    C,$FEFF             
43A6: 7F              LD      A,A                 
43A7: D8              RET     C                   
43A8: DC 60 DE        CALL    C,$DE60             
43AB: 68              LD      L,B                 
43AC: BE              CP      (HL)                
43AD: D0              RET     NC                  
43AE: 7F              LD      A,A                 
43AF: 80              ADD     A,B                 
43B0: FF              RST     0X38                
43B1: 70              LD      (HL),B              
43B2: FD                              
43B3: FA FD 7A        LD      A,($7AFD)           ; {}
43B6: F7              RST     0X30                
43B7: F8 8F           LD      HL,SP+$8F           
43B9: 70              LD      (HL),B              
43BA: FC                              
43BB: 00              NOP                         
43BC: 86              ADD     A,(HL)              
43BD: F8 FE           LD      HL,SP+$FE           
43BF: 00              NOP                         
43C0: 00              NOP                         
43C1: 00              NOP                         
43C2: 03              INC     BC                  
43C3: 00              NOP                         
43C4: 07              RLCA                        
43C5: 03              INC     BC                  
43C6: 6F              LD      L,A                 
43C7: 07              RLCA                        
43C8: FF              RST     0X38                
43C9: 64              LD      H,H                 
43CA: FF              RST     0X38                
43CB: 71              LD      (HL),C              
43CC: FF              RST     0X38                
43CD: 5B              LD      E,E                 
43CE: BF              CP      A                   
43CF: 7C              LD      A,H                 
43D0: 7F              LD      A,A                 
43D1: 0F              RRCA                        
43D2: 5F              LD      E,A                 
43D3: 3C              INC     A                   
43D4: 37              SCF                         
43D5: 0B              DEC     BC                  
43D6: 1F              RRA                         
43D7: 03              INC     BC                  
43D8: 1D              DEC     E                   
43D9: 03              INC     BC                  
43DA: 0F              RRCA                        
43DB: 00              NOP                         
43DC: 1C              INC     E                   
43DD: 0F              RRCA                        
43DE: 1F              RRA                         
43DF: 00              NOP                         
43E0: 00              NOP                         
43E1: 00              NOP                         
43E2: CF              RST     0X08                
43E3: 00              NOP                         
43E4: FF              RST     0X38                
43E5: CE FE           ADC     $FE                 
43E7: FC                              
43E8: 7C              LD      A,H                 
43E9: D8              RET     C                   
43EA: DC 60 DE        CALL    C,$DE60             
43ED: 68              LD      L,B                 
43EE: BE              CP      (HL)                
43EF: D0              RET     NC                  
43F0: 7F              LD      A,A                 
43F1: 80              ADD     A,B                 
43F2: FF              RST     0X38                
43F3: 70              LD      (HL),B              
43F4: FD                              
43F5: BA              CP      D                   
43F6: F5              PUSH    AF                  
43F7: FA 4F B0        LD      A,($B04F)           
43FA: F9              LD      SP,HL               
43FB: 06 79           LD      B,$79               
43FD: 9E              SBC     (HL)                
43FE: FE 00           CP      $00                 
4400: 0F              RRCA                        
4401: 00              NOP                         
4402: 3F              CCF                         
4403: 01 7F 03        LD      BC,$037F            
4406: 73              LD      (HL),E              
4407: 0F              RRCA                        
4408: FE 01           CP      $01                 
440A: FF              RST     0X38                
440B: 2E 7F           LD      L,$7F               
440D: 36 7F           LD      (HL),$7F            
440F: 3D              DEC     A                   
4410: 3F              CCF                         
4411: 03              INC     BC                  
4412: 7F              LD      A,A                 
4413: 0C              INC     C                   
4414: FF              RST     0X38                
4415: 47              LD      B,A                 
4416: E7              RST     0X20                
4417: 58              LD      E,B                 
4418: 60              LD      H,B                 
4419: 1F              RRA                         
441A: 1E 01           LD      E,$01               
441C: 1F              RRA                         
441D: 0C              INC     C                   
441E: 1F              RRA                         
441F: 00              NOP                         
4420: F0 00           LD      A,($00)             
4422: FC                              
4423: 80              ADD     A,B                 
4424: FE C0           CP      $C0                 
4426: CE F0           ADC     $F0                 
4428: 7F              LD      A,A                 
4429: 80              ADD     A,B                 
442A: FF              RST     0X38                
442B: 74              LD      (HL),H              
442C: FE 6C           CP      $6C                 
442E: FE BC           CP      $BC                 
4430: FE C0           CP      $C0                 
4432: FC                              
4433: 38 FC           JR      C,$4431             ; {}
4435: E0 FE           LD      ($FF00+$FE),A       
4437: 0C              INC     C                   
4438: 1E EC           LD      E,$EC               
443A: 1C              INC     E                   
443B: E0 F0           LD      ($FF00+$F0),A       
443D: 00              NOP                         
443E: F0 00           LD      A,($00)             
4440: 07              RLCA                        
4441: 00              NOP                         
4442: 1F              RRA                         
4443: 00              NOP                         
4444: 3F              CCF                         
4445: 00              NOP                         
4446: 7F              LD      A,A                 
4447: 00              NOP                         
4448: 7F              LD      A,A                 
4449: 00              NOP                         
444A: FF              RST     0X38                
444B: 40              LD      B,B                 
444C: FF              RST     0X38                
444D: 40              LD      B,B                 
444E: F3              DI                          
444F: 5C              LD      E,H                 
4450: 78              LD      A,B                 
4451: 1F              RRA                         
4452: 1F              RRA                         
4453: 0F              RRCA                        
4454: 3F              CCF                         
4455: 00              NOP                         
4456: 70              LD      (HL),B              
4457: 2F              CPL                         
4458: 70              LD      (HL),B              
4459: 2F              CPL                         
445A: 38 07           JR      C,$4463             ; {}
445C: 0F              RRCA                        
445D: 00              NOP                         
445E: 3F              CCF                         
445F: 00              NOP                         
4460: E0 00           LD      ($FF00+$00),A       
4462: F8 00           LD      HL,SP+$00           
4464: FC                              
4465: 00              NOP                         
4466: FE 00           CP      $00                 
4468: FE 00           CP      $00                 
446A: FF              RST     0X38                
446B: 02              LD      (BC),A              
446C: FF              RST     0X38                
446D: 02              LD      (BC),A              
446E: CF              RST     0X08                
446F: 3A              LD      A,(HLD)             
4470: 1E F8           LD      E,$F8               
4472: FE F0           CP      $F0                 
4474: FE 04           CP      $04                 
4476: 0E F4           LD      C,$F4               
4478: 0C              INC     C                   
4479: F0 F8           LD      A,($F8)             
447B: 00              NOP                         
447C: F8 70           LD      HL,SP+$70           
447E: FC                              
447F: 00              NOP                         
4480: 07              RLCA                        
4481: 00              NOP                         
4482: 0F              RRCA                        
4483: 02              LD      (BC),A              
4484: 0F              RRCA                        
4485: 07              RLCA                        
4486: 3F              CCF                         
4487: 04              INC     B                   
4488: 3F              CCF                         
4489: 13              INC     DE                  
448A: 3F              CCF                         
448B: 13              INC     DE                  
448C: 3F              CCF                         
448D: 0A              LD      A,(BC)              
448E: 3F              CCF                         
448F: 1B              DEC     DE                  
4490: 7F              LD      A,A                 
4491: 3C              INC     A                   
4492: 7F              LD      A,A                 
4493: 07              RLCA                        
4494: 1F              RRA                         
4495: 0F              RRCA                        
4496: 1F              RRA                         
4497: 00              NOP                         
4498: 05              DEC     B                   
4499: 02              LD      (BC),A              
449A: 05              DEC     B                   
449B: 02              LD      (BC),A              
449C: 03              INC     BC                  
449D: 01 07 00        LD      BC,$0007            
44A0: F0 00           LD      A,($00)             
44A2: FC                              
44A3: 00              NOP                         
44A4: FE C0           CP      $C0                 
44A6: FF              RST     0X38                
44A7: 40              LD      B,B                 
44A8: FF              RST     0X38                
44A9: 4C              LD      C,H                 
44AA: FF              RST     0X38                
44AB: 3E FF           LD      A,$FF               
44AD: 7E              LD      A,(HL)              
44AE: FE 70           CP      $70                 
44B0: FC                              
44B1: F8 F8           LD      HL,SP+$F8           
44B3: F0 F0           LD      A,($F0)             
44B5: 00              NOP                         
44B6: E8 D0           ADD     SP,$D0              
44B8: E8 D0           ADD     SP,$D0              
44BA: F8 00           LD      HL,SP+$00           
44BC: F8 E0           LD      HL,SP+$E0           
44BE: F8 00           LD      HL,SP+$00           
44C0: 00              NOP                         
44C1: 00              NOP                         
44C2: 07              RLCA                        
44C3: 00              NOP                         
44C4: 0F              RRCA                        
44C5: 02              LD      (BC),A              
44C6: 0F              RRCA                        
44C7: 07              RLCA                        
44C8: 3F              CCF                         
44C9: 04              INC     B                   
44CA: 3F              CCF                         
44CB: 13              INC     DE                  
44CC: 3F              CCF                         
44CD: 13              INC     DE                  
44CE: 3F              CCF                         
44CF: 0A              LD      A,(BC)              
44D0: 3F              CCF                         
44D1: 1B              DEC     DE                  
44D2: 7F              LD      A,A                 
44D3: 3C              INC     A                   
44D4: 7F              LD      A,A                 
44D5: 07              RLCA                        
44D6: 1F              RRA                         
44D7: 0E 0F           LD      C,$0F               
44D9: 01 0F 01        LD      BC,$010F            
44DC: 1F              RRA                         
44DD: 0E 1F           LD      C,$1F               
44DF: 00              NOP                         
44E0: 00              NOP                         
44E1: 00              NOP                         
44E2: F0 00           LD      A,($00)             
44E4: FC                              
44E5: 00              NOP                         
44E6: FE C0           CP      $C0                 
44E8: FF              RST     0X38                
44E9: 40              LD      B,B                 
44EA: FF              RST     0X38                
44EB: 4C              LD      C,H                 
44EC: FF              RST     0X38                
44ED: 3E FF           LD      A,$FF               
44EF: 7E              LD      A,(HL)              
44F0: FE 70           CP      $70                 
44F2: FC                              
44F3: F8 F8           LD      HL,SP+$F8           
44F5: F0 F0           LD      A,($F0)             
44F7: 00              NOP                         
44F8: D8              RET     C                   
44F9: A0              AND     B                   
44FA: FC                              
44FB: 88              ADC     A,B                 
44FC: FC                              
44FD: 38 FC           JR      C,$44FB             ; {}
44FF: 00              NOP                         
4500: 03              INC     BC                  
4501: 00              NOP                         
4502: 04              INC     B                   
4503: 03              INC     BC                  
4504: 09              ADD     HL,BC               
4505: 07              RLCA                        
4506: 11 0F 11        LD      DE,$110F            
4509: 0E 23           LD      C,$23               
450B: 1C              INC     E                   
450C: 26 19           LD      H,$19               
450E: 65              LD      H,L                 
450F: 1B              DEC     DE                  
4510: AF              XOR     A                   
4511: 51              LD      D,C                 
4512: BF              CP      A                   
4513: 46              LD      B,(HL)              
4514: 9F              SBC     A                   
4515: 6F              LD      L,A                 
4516: 4B              LD      C,E                 
4517: 37              SCF                         
4518: 3F              CCF                         
4519: 07              RLCA                        
451A: 27              DAA                         
451B: 1B              DEC     DE                  
451C: 67              LD      H,A                 
451D: 1D              DEC     E                   
451E: 7F              LD      A,A                 
451F: 00              NOP                         
4520: C0              RET     NZ                  
4521: 00              NOP                         
4522: 20 C0           JR      NZ,$44E4            ; {}
4524: 90              SUB     B                   
4525: E0 88           LD      ($FF00+$88),A       
4527: F0 88           LD      A,($88)             
4529: 70              LD      (HL),B              
452A: C4 38 66        CALL    NZ,$6638            ; {}
452D: 98              SBC     B                   
452E: A5              AND     L                   
452F: DA F5 8A        JP      C,$8AF5             
4532: F9              LD      SP,HL               
4533: 66              LD      H,(HL)              
4534: FA F4 DC        LD      A,($DCF4)           
4537: E0 F4           LD      ($FF00+$F4),A       
4539: E8 E2           ADD     SP,$E2              
453B: DC F2 BC        CALL    C,$BCF2             
453E: FE 00           CP      $00                 
4540: 03              INC     BC                  
4541: 00              NOP                         
4542: 05              DEC     B                   
4543: 03              INC     BC                  
4544: 09              ADD     HL,BC               
4545: 07              RLCA                        
4546: 11 0F 10        LD      DE,$100F            
4549: 0F              RRCA                        
454A: 28 17           JR      Z,$4563             ; {}
454C: 28 17           JR      Z,$4565             ; {}
454E: 24              INC     H                   
454F: 1B              DEC     DE                  
4550: 50              LD      D,B                 
4551: 2F              CPL                         
4552: 88              ADC     A,B                 
4553: 77              LD      (HL),A              
4554: 8C              ADC     A,H                 
4555: 7B              LD      A,E                 
4556: 9F              SBC     A                   
4557: 6C              LD      L,H                 
4558: 57              LD      D,A                 
4559: 2F              CPL                         
455A: 30 0F           JR      NC,$456B            ; {}
455C: 60              LD      H,B                 
455D: 1F              RRA                         
455E: 7F              LD      A,A                 
455F: 00              NOP                         
4560: C0              RET     NZ                  
4561: 00              NOP                         
4562: A0              AND     B                   
4563: C0              RET     NZ                  
4564: 90              SUB     B                   
4565: E0 08           LD      ($FF00+$08),A       
4567: F0 08           LD      A,($08)             
4569: F0 14           LD      A,($14)             
456B: E8 34           ADD     SP,$34              
456D: C8              RET     Z                   
456E: 4A              LD      C,D                 
456F: B4              OR      H                   
4570: 11 EE 29        LD      DE,$29EE            
4573: D6 59           SUB     $59                 
4575: B6              OR      (HL)                
4576: FA 74 EC        LD      A,($EC74)           
4579: F0 04           LD      A,($04)             
457B: F8 02           LD      HL,SP+$02           
457D: FC                              
457E: FE 00           CP      $00                 
4580: 7E              LD      A,(HL)              
4581: 00              NOP                         
4582: FF              RST     0X38                
4583: 7E              LD      A,(HL)              
4584: E0 3F           LD      ($FF00+$3F),A       
4586: E0 1F           LD      ($FF00+$1F),A       
4588: 70              LD      (HL),B              
4589: 0F              RRCA                        
458A: 70              LD      (HL),B              
458B: 0F              RRCA                        
458C: 78              LD      A,B                 
458D: 27              DAA                         
458E: F8 67           LD      HL,SP+$67           
4590: FF              RST     0X38                
4591: 18 F8           JR      $458B               ; {}
4593: 77              LD      (HL),A              
4594: F8 77           LD      HL,SP+$77           
4596: FC                              
4597: 73              LD      (HL),E              
4598: 7B              LD      A,E                 
4599: 34              INC     (HL)                
459A: 78              LD      A,B                 
459B: 27              DAA                         
459C: 38 07           JR      C,$45A5             ; {}
459E: 1F              RRA                         
459F: 00              NOP                         
45A0: 00              NOP                         
45A1: 00              NOP                         
45A2: 80              ADD     A,B                 
45A3: 00              NOP                         
45A4: 40              LD      B,B                 
45A5: 80              ADD     A,B                 
45A6: 20 C0           JR      NZ,$4568            ; {}
45A8: 10 E0           ;;STOP    $E0                 
45AA: 70              LD      (HL),B              
45AB: 80              ADD     A,B                 
45AC: 08 F0 C8        LD      ($C8F0),SP          
45AF: 30 24           JR      NC,$45D5            ; {}
45B1: D8              RET     C                   
45B2: 14              INC     D                   
45B3: E8 1C           ADD     SP,$1C              
45B5: F0 78           LD      A,($78)             
45B7: B0              OR      B                   
45B8: 88              ADC     A,B                 
45B9: 70              LD      (HL),B              
45BA: 08 F0 04        LD      ($04F0),SP          
45BD: F8 FC           LD      HL,SP+$FC           
45BF: 00              NOP                         
45C0: 00              NOP                         
45C1: 00              NOP                         
45C2: 7E              LD      A,(HL)              
45C3: 00              NOP                         
45C4: FF              RST     0X38                
45C5: 7E              LD      A,(HL)              
45C6: E0 3F           LD      ($FF00+$3F),A       
45C8: E0 1F           LD      ($FF00+$1F),A       
45CA: 70              LD      (HL),B              
45CB: 0F              RRCA                        
45CC: 70              LD      (HL),B              
45CD: 0F              RRCA                        
45CE: 78              LD      A,B                 
45CF: 27              DAA                         
45D0: F9              LD      SP,HL               
45D1: 66              LD      H,(HL)              
45D2: FE 11           CP      $11                 
45D4: F0 6F           LD      A,($6F)             
45D6: F0 6F           LD      A,($6F)             
45D8: F8 77           LD      HL,SP+$77           
45DA: 7F              LD      A,A                 
45DB: 30 70           JR      NC,$464D            ; {}
45DD: 2F              CPL                         
45DE: 3F              CCF                         
45DF: 00              NOP                         
45E0: 00              NOP                         
45E1: 00              NOP                         
45E2: 00              NOP                         
45E3: 00              NOP                         
45E4: 80              ADD     A,B                 
45E5: 00              NOP                         
45E6: 40              LD      B,B                 
45E7: 80              ADD     A,B                 
45E8: 20 C0           JR      NZ,$45AA            ; {}
45EA: 10 E0           ;;STOP    $E0                 
45EC: 70              LD      (HL),B              
45ED: 80              ADD     A,B                 
45EE: 08 F0 C8        LD      ($C8F0),SP          
45F1: 30 24           JR      NC,$4617            ; {}
45F3: D8              RET     C                   
45F4: 14              INC     D                   
45F5: E8 1C           ADD     SP,$1C              
45F7: F0 B8           LD      A,($B8)             
45F9: 70              LD      (HL),B              
45FA: 04              INC     B                   
45FB: F8 02           LD      HL,SP+$02           
45FD: FC                              
45FE: FE 00           CP      $00                 
4600: 73              LD      (HL),E              
4601: 00              NOP                         
4602: 6F              LD      L,A                 
4603: 32              LD      (HLD),A             
4604: 3F              CCF                         
4605: 17              RLA                         
4606: 1F              RRA                         
4607: 05              DEC     B                   
4608: 0F              RRCA                        
4609: 00              NOP                         
460A: 1F              RRA                         
460B: 04              INC     B                   
460C: 3F              CCF                         
460D: 0F              RRCA                        
460E: 5F              LD      E,A                 
460F: 2C              INC     L                   
4610: FF              RST     0X38                
4611: 6B              LD      L,E                 
4612: FB              EI                          
4613: 67              LD      H,A                 
4614: 99              SBC     C                   
4615: 67              LD      H,A                 
4616: 7F              LD      A,A                 
4617: 00              NOP                         
4618: 3B              DEC     SP                  
4619: 07              RLCA                        
461A: 4F              LD      C,A                 
461B: 30 F3           JR      NC,$4610            ; {}
461D: 7C              LD      A,H                 
461E: FF              RST     0X38                
461F: 00              NOP                         
4620: CF              RST     0X08                
4621: 00              NOP                         
4622: F7              RST     0X30                
4623: CE FE           ADC     $FE                 
4625: E4                              
4626: FC                              
4627: 60              LD      H,B                 
4628: F8 00           LD      HL,SP+$00           
462A: DC E0 EA        CALL    C,$EAE0             
462D: F4                              
462E: FF              RST     0X38                
462F: 76              HALT                        
4630: FF              RST     0X38                
4631: B6              OR      (HL)                
4632: A9              XOR     C                   
4633: D6 3E           SUB     $3E                 
4635: C0              RET     NZ                  
4636: FC                              
4637: 00              NOP                         
4638: DE E0           SBC     $E0                 
463A: F2                              
463B: 0C              INC     C                   
463C: CF              RST     0X08                
463D: 3E FF           LD      A,$FF               
463F: 00              NOP                         
4640: 73              LD      (HL),E              
4641: 00              NOP                         
4642: 5F              LD      E,A                 
4643: 20 2F           JR      NZ,$4674            ; {}
4645: 10 1F           ;;STOP    $1F                 
4647: 00              NOP                         
4648: 3F              CCF                         
4649: 00              NOP                         
464A: 7F              LD      A,A                 
464B: 20 FF           JR      NZ,$464C            ; {}
464D: 60              LD      H,B                 
464E: DF              RST     0X18                
464F: 60              LD      H,B                 
4650: BF              CP      A                   
4651: 44              LD      B,H                 
4652: 7F              LD      A,A                 
4653: 06 7B           LD      B,$7B               
4655: 07              RLCA                        
4656: 75              LD      (HL),L              
4657: 0B              DEC     BC                  
4658: 23              INC     HL                  
4659: 1C              INC     E                   
465A: 58              LD      E,B                 
465B: 27              DAA                         
465C: C7              RST     0X00                
465D: 78              LD      A,B                 
465E: FF              RST     0X38                
465F: 00              NOP                         
4660: EF              RST     0X28                
4661: 00              NOP                         
4662: FD                              
4663: 02              LD      (BC),A              
4664: FA 04 FC        LD      A,($FC04)           
4667: 00              NOP                         
4668: F8 00           LD      HL,SP+$00           
466A: FC                              
466B: 00              NOP                         
466C: FE 04           CP      $04                 
466E: FF              RST     0X38                
466F: 06 FB           LD      B,$FB               
4671: 06 FD           LD      B,$FD               
4673: 02              LD      (BC),A              
4674: FE 00           CP      $00                 
4676: BC              CP      H                   
4677: 40              LD      B,B                 
4678: 0C              INC     C                   
4679: F0 1A           LD      A,($1A)             
467B: E4                              
467C: E3                              
467D: 1E FF           LD      E,$FF               
467F: 00              NOP                         
4680: 0F              RRCA                        
4681: 00              NOP                         
4682: 1F              RRA                         
4683: 0C              INC     C                   
4684: 1F              RRA                         
4685: 04              INC     B                   
4686: FF              RST     0X38                
4687: 04              INC     B                   
4688: FF              RST     0X38                
4689: 38 FF           JR      C,$468A             ; {}
468B: 7C              LD      A,H                 
468C: FD                              
468D: 3E FD           LD      A,$FD               
468F: 5E              LD      E,(HL)              
4690: BB              CP      E                   
4691: 6C              LD      L,H                 
4692: 5F              LD      E,A                 
4693: 2B              DEC     HL                  
4694: 3F              CCF                         
4695: 03              INC     BC                  
4696: 25              DEC     H                   
4697: 1B              DEC     DE                  
4698: 3F              CCF                         
4699: 00              NOP                         
469A: 1F              RRA                         
469B: 01 0E 07        LD      BC,$070E            
469E: 0F              RRCA                        
469F: 00              NOP                         
46A0: 70              LD      (HL),B              
46A1: 00              NOP                         
46A2: F0 60           LD      A,($60)             
46A4: E0 C0           LD      ($FF00+$C0),A       
46A6: F0 00           LD      A,($00)             
46A8: F8 00           LD      HL,SP+$00           
46AA: F8 00           LD      HL,SP+$00           
46AC: FC                              
46AD: 00              NOP                         
46AE: 5C              LD      E,H                 
46AF: E0 FE           LD      ($FF00+$FE),A       
46B1: E0 FF           LD      ($FF00+$FF),A       
46B3: E2              LD      (C),A               
46B4: DF              RST     0X18                
46B5: E2              LD      (C),A               
46B6: B9              CP      C                   
46B7: C6 E2           ADD     $E2                 
46B9: 1C              INC     E                   
46BA: 3C              INC     A                   
46BB: C0              RET     NZ                  
46BC: 08 F0 F8        LD      ($F8F0),SP          
46BF: 00              NOP                         
46C0: 1F              RRA                         
46C1: 00              NOP                         
46C2: 3F              CCF                         
46C3: 16 3F           LD      D,$3F               
46C5: 0B              DEC     BC                  
46C6: 7F              LD      A,A                 
46C7: 03              INC     BC                  
46C8: FF              RST     0X38                
46C9: 4C              LD      C,H                 
46CA: FF              RST     0X38                
46CB: 7E              LD      A,(HL)              
46CC: FE 5F           CP      $5F                 
46CE: FE 2F           CP      $2F                 
46D0: FF              RST     0X38                
46D1: 76              HALT                        
46D2: 7B              LD      A,E                 
46D3: 34              INC     (HL)                
46D4: 3F              CCF                         
46D5: 01 23 1D        LD      BC,$1D23            
46D8: 3E 01           LD      A,$01               
46DA: 1F              RRA                         
46DB: 00              NOP                         
46DC: 0E 07           LD      C,$07               
46DE: 0F              RRCA                        
46DF: 00              NOP                         
46E0: 78              LD      A,B                 
46E1: 00              NOP                         
46E2: F8 30           LD      HL,SP+$30           
46E4: F0 60           LD      A,($60)             
46E6: F0 00           LD      A,($00)             
46E8: F8 00           LD      HL,SP+$00           
46EA: F8 00           LD      HL,SP+$00           
46EC: FC                              
46ED: 00              NOP                         
46EE: AC              XOR     H                   
46EF: 70              LD      (HL),B              
46F0: FE 70           CP      $70                 
46F2: FF              RST     0X38                
46F3: 72              LD      (HL),D              
46F4: FF              RST     0X38                
46F5: F2                              
46F6: E9              JP      (HL)                
46F7: F6 D2           OR      $D2                 
46F9: EC                              
46FA: FC                              
46FB: 00              NOP                         
46FC: 08 F0 F8        LD      ($F8F0),SP          
46FF: 00              NOP                         
4700: 00              NOP                         
4701: FF              RST     0X38                
4702: 00              NOP                         
4703: FF              RST     0X38                
4704: 22              LD      (HLI),A             
4705: DD                              
4706: 14              INC     D                   
4707: EB                              
4708: 08 F7 14        LD      ($14F7),SP          
470B: EB                              
470C: 22              LD      (HLI),A             
470D: DD                              
470E: 00              NOP                         
470F: FF              RST     0X38                
4710: 00              NOP                         
4711: FF              RST     0X38                
4712: 00              NOP                         
4713: FF              RST     0X38                
4714: 22              LD      (HLI),A             
4715: DD                              
4716: 14              INC     D                   
4717: EB                              
4718: 08 F7 14        LD      ($14F7),SP          
471B: EB                              
471C: 22              LD      (HLI),A             
471D: DD                              
471E: 00              NOP                         
471F: FF              RST     0X38                
4720: 00              NOP                         
4721: 00              NOP                         
4722: 01 00 03        LD      BC,$0300            
4725: 01 E3 01        LD      BC,$01E3            
4728: F7              RST     0X30                
4729: 60              LD      H,B                 
472A: FF              RST     0X38                
472B: 74              LD      (HL),H              
472C: 7D              LD      A,L                 
472D: 2B              DEC     HL                  
472E: 78              LD      A,B                 
472F: 27              DAA                         
4730: F3              DI                          
4731: 6C              LD      L,H                 
4732: F7              RST     0X30                
4733: 69              LD      L,C                 
4734: 77              LD      (HL),A              
4735: 28 F7           JR      Z,$472E             ; {}
4737: 68              LD      L,B                 
4738: F3              DI                          
4739: 8C              ADC     A,H                 
473A: F8 E7           LD      HL,SP+$E7           
473C: 77              LD      (HL),A              
473D: 78              LD      A,B                 
473E: 0F              RRCA                        
473F: 0F              RRCA                        
4740: 00              NOP                         
4741: 00              NOP                         
4742: 07              RLCA                        
4743: 07              RLCA                        
4744: 1F              RRA                         
4745: 1C              INC     E                   
4746: 3F              CCF                         
4747: 31 7F 67        LD      SP,$677F            
474A: 7F              LD      A,A                 
474B: 6E              LD      L,(HL)              
474C: FF              RST     0X38                
474D: CC FF CD        CALL    Z,$CDFF             
4750: FF              RST     0X38                
4751: 67              LD      H,A                 
4752: FF              RST     0X38                
4753: 73              LD      (HL),E              
4754: FF              RST     0X38                
4755: B8              CP      B                   
4756: FF              RST     0X38                
4757: 9F              SBC     A                   
4758: 7F              LD      A,A                 
4759: 47              LD      B,A                 
475A: 3F              CCF                         
475B: 30 0F           JR      NC,$476C            ; {}
475D: 0F              RRCA                        
475E: 00              NOP                         
475F: 00              NOP                         
4760: 01 00 03        LD      BC,$0300            
4763: 01 E3 01        LD      BC,$01E3            
4766: F7              RST     0X30                
4767: 60              LD      H,B                 
4768: FF              RST     0X38                
4769: 70              LD      (HL),B              
476A: 7F              LD      A,A                 
476B: 2C              INC     L                   
476C: 7F              LD      A,A                 
476D: 2E FF           LD      L,$FF               
476F: 6B              LD      L,E                 
4770: FF              RST     0X38                
4771: 68              LD      L,B                 
4772: 79              LD      A,C                 
4773: 27              DAA                         
4774: F3              DI                          
4775: 6C              LD      L,H                 
4776: F4                              
4777: 4B              LD      C,E                 
4778: F1              POP     AF                  
4779: 8E              ADC     A,(HL)              
477A: FF              RST     0X38                
477B: F1              POP     AF                  
477C: 3F              CCF                         
477D: 3F              CCF                         
477E: 07              RLCA                        
477F: 07              RLCA                        
4780: 03              INC     BC                  
4781: 00              NOP                         
4782: 3C              INC     A                   
4783: 03              INC     BC                  
4784: 79              LD      A,C                 
4785: 37              SCF                         
4786: DB                              
4787: 75              LD      (HL),L              
4788: BB              CP      E                   
4789: 54              LD      D,H                 
478A: F9              LD      SP,HL               
478B: 46              LD      B,(HL)              
478C: AC              XOR     H                   
478D: 43              LD      B,E                 
478E: E7              RST     0X20                
478F: 40              LD      B,B                 
4790: A7              AND     A                   
4791: 42              LD      B,D                 
4792: E7              RST     0X20                
4793: 42              LD      B,D                 
4794: A2              AND     D                   
4795: 40              LD      B,B                 
4796: E0 40           LD      ($FF00+$40),A       
4798: A0              AND     B                   
4799: 40              LD      B,B                 
479A: E0 40           LD      ($FF00+$40),A       
479C: 90              SUB     B                   
479D: 60              LD      H,B                 
479E: 70              LD      (HL),B              
479F: 00              NOP                         
47A0: 00              NOP                         
47A1: 00              NOP                         
47A2: 00              NOP                         
47A3: 00              NOP                         
47A4: 00              NOP                         
47A5: 00              NOP                         
47A6: 00              NOP                         
47A7: 00              NOP                         
47A8: 00              NOP                         
47A9: 00              NOP                         
47AA: 30 00           JR      NC,$47AC            ; {}
47AC: 7B              LD      A,E                 
47AD: 30 DC           JR      NC,$478B            ; {}
47AF: 73              LD      (HL),E              
47B0: B9              CP      C                   
47B1: 57              LD      D,A                 
47B2: EB                              
47B3: 55              LD      D,L                 
47B4: AB              XOR     E                   
47B5: 54              LD      D,H                 
47B6: E9              JP      (HL)                
47B7: 56              LD      D,(HL)              
47B8: BC              CP      H                   
47B9: 43              LD      B,E                 
47BA: E7              RST     0X20                
47BB: 40              LD      B,B                 
47BC: 97              SUB     A                   
47BD: 62              LD      H,D                 
47BE: 73              LD      (HL),E              
47BF: 00              NOP                         
47C0: 00              NOP                         
47C1: 00              NOP                         
47C2: 3F              CCF                         
47C3: 00              NOP                         
47C4: 7F              LD      A,A                 
47C5: 2B              DEC     HL                  
47C6: FF              RST     0X38                
47C7: AB              XOR     E                   
47C8: D4 AB FF        CALL    NC,$FFAB            
47CB: 80              ADD     A,B                 
47CC: FF              RST     0X38                
47CD: AB              XOR     E                   
47CE: FF              RST     0X38                
47CF: AB              XOR     E                   
47D0: D4 AB FF        CALL    NC,$FFAB            
47D3: 80              ADD     A,B                 
47D4: FF              RST     0X38                
47D5: AB              XOR     E                   
47D6: FF              RST     0X38                
47D7: AB              XOR     E                   
47D8: D4 AB D4        CALL    NC,$D4AB            
47DB: AB              XOR     E                   
47DC: BF              CP      A                   
47DD: C0              RET     NZ                  
47DE: 7F              LD      A,A                 
47DF: 7F              LD      A,A                 
47E0: 00              NOP                         
47E1: 00              NOP                         
47E2: 3F              CCF                         
47E3: 3F              CCF                         
47E4: 7F              LD      A,A                 
47E5: 40              LD      B,B                 
47E6: FF              RST     0X38                
47E7: AB              XOR     E                   
47E8: FF              RST     0X38                
47E9: AB              XOR     E                   
47EA: D4 AB FF        CALL    NC,$FFAB            
47ED: C0              RET     NZ                  
47EE: FF              RST     0X38                
47EF: AB              XOR     E                   
47F0: FF              RST     0X38                
47F1: AB              XOR     E                   
47F2: D4 AB FF        CALL    NC,$FFAB            
47F5: C0              RET     NZ                  
47F6: FF              RST     0X38                
47F7: AB              XOR     E                   
47F8: FF              RST     0X38                
47F9: AB              XOR     E                   
47FA: D4 AB FF        CALL    NC,$FFAB            
47FD: C0              RET     NZ                  
47FE: 7F              LD      A,A                 
47FF: 7F              LD      A,A                 
4800: 03              INC     BC                  
4801: 00              NOP                         
4802: 07              RLCA                        
4803: 03              INC     BC                  
4804: 0F              RRCA                        
4805: 07              RLCA                        
4806: 3F              CCF                         
4807: 0F              RRCA                        
4808: 7F              LD      A,A                 
4809: 2B              DEC     HL                  
480A: 6F              LD      L,A                 
480B: 3D              DEC     A                   
480C: 7F              LD      A,A                 
480D: 3F              CCF                         
480E: 3F              CCF                         
480F: 1B              DEC     DE                  
4810: 2F              CPL                         
4811: 1C              INC     E                   
4812: 17              RLA                         
4813: 0F              RRCA                        
4814: 2F              CPL                         
4815: 10 2F           ;;STOP    $2F                 
4817: 17              RLA                         
4818: 1F              RRA                         
4819: 06 1F           LD      B,$1F               
481B: 00              NOP                         
481C: 3F              CCF                         
481D: 1C              INC     E                   
481E: 3F              CCF                         
481F: 00              NOP                         
4820: C0              RET     NZ                  
4821: 00              NOP                         
4822: E0 C0           LD      ($FF00+$C0),A       
4824: F0 E0           LD      A,($E0)             
4826: FE F0           CP      $F0                 
4828: FF              RST     0X38                
4829: B6              OR      (HL)                
482A: F7              RST     0X30                
482B: 7E              LD      A,(HL)              
482C: FD                              
482D: FE FE           CP      $FE                 
482F: B8              CP      B                   
4830: F4                              
4831: 78              LD      A,B                 
4832: E8 F0           ADD     SP,$F0              
4834: F8 00           LD      HL,SP+$00           
4836: F4                              
4837: 68              LD      L,B                 
4838: F4                              
4839: 68              LD      L,B                 
483A: F8 C0           LD      HL,SP+$C0           
483C: FC                              
483D: 38 FC           JR      C,$483B             ; {}
483F: 00              NOP                         
4840: 03              INC     BC                  
4841: 00              NOP                         
4842: 07              RLCA                        
4843: 03              INC     BC                  
4844: 0F              RRCA                        
4845: 07              RLCA                        
4846: 3F              CCF                         
4847: 0F              RRCA                        
4848: 7F              LD      A,A                 
4849: 37              SCF                         
484A: 77              LD      (HL),A              
484B: 3F              CCF                         
484C: 5F              LD      E,A                 
484D: 3F              CCF                         
484E: 3F              CCF                         
484F: 0F              RRCA                        
4850: 5E              LD      E,(HL)              
4851: 2F              CPL                         
4852: 4F              LD      C,A                 
4853: 33              INC     SP                  
4854: 43              LD      B,E                 
4855: 3C              INC     A                   
4856: 20 1F           JR      NZ,$4877            ; {}
4858: 1F              RRA                         
4859: 0F              RRCA                        
485A: 1F              RRA                         
485B: 00              NOP                         
485C: 3F              CCF                         
485D: 1C              INC     E                   
485E: 3F              CCF                         
485F: 00              NOP                         
4860: C0              RET     NZ                  
4861: 00              NOP                         
4862: E0 C0           LD      ($FF00+$C0),A       
4864: F0 E0           LD      A,($E0)             
4866: FC                              
4867: F0 FE           LD      A,($FE)             
4869: F4                              
486A: FE FC           CP      $FC                 
486C: FA FC FC        LD      A,($FCFC)           
486F: F8 38           LD      HL,SP+$38           
4871: F0 FC           LD      A,($FC)             
4873: C0              RET     NZ                  
4874: C2 3C 02        JP      NZ,$023C            
4877: FC                              
4878: FC                              
4879: F8 F8           LD      HL,SP+$F8           
487B: 00              NOP                         
487C: FC                              
487D: 38 FC           JR      C,$487B             ; {}
487F: 00              NOP                         
4880: 03              INC     BC                  
4881: 00              NOP                         
4882: 07              RLCA                        
4883: 03              INC     BC                  
4884: 0F              RRCA                        
4885: 07              RLCA                        
4886: 1F              RRA                         
4887: 0F              RRCA                        
4888: 1F              RRA                         
4889: 0B              DEC     BC                  
488A: 3F              CCF                         
488B: 17              RLA                         
488C: 3F              CCF                         
488D: 1F              RRA                         
488E: 3F              CCF                         
488F: 1B              DEC     DE                  
4890: 3F              CCF                         
4891: 07              RLCA                        
4892: 1F              RRA                         
4893: 0F              RRCA                        
4894: 1F              RRA                         
4895: 00              NOP                         
4896: 3F              CCF                         
4897: 1A              LD      A,(DE)              
4898: 3F              CCF                         
4899: 16 1F           LD      D,$1F               
489B: 0E 0F           LD      C,$0F               
489D: 01 0F 00        LD      BC,$000F            
48A0: C0              RET     NZ                  
48A1: 00              NOP                         
48A2: F0 C0           LD      A,($C0)             
48A4: F8 F0           LD      HL,SP+$F0           
48A6: FC                              
48A7: C0              RET     NZ                  
48A8: FC                              
48A9: B8              CP      B                   
48AA: BC              CP      H                   
48AB: F8 FC           LD      HL,SP+$FC           
48AD: F8 F8           LD      HL,SP+$F8           
48AF: E0 F0           LD      ($FF00+$F0),A       
48B1: E0 F0           LD      ($FF00+$F0),A       
48B3: 00              NOP                         
48B4: 10 E0           ;;STOP    $E0                 
48B6: 10 E0           ;;STOP    $E0                 
48B8: 20 C0           JR      NZ,$487A            ; {}
48BA: E0 00           LD      ($FF00+$00),A       
48BC: F0 E0           LD      A,($E0)             
48BE: F0 00           LD      A,($00)             
48C0: 03              INC     BC                  
48C1: 00              NOP                         
48C2: 07              RLCA                        
48C3: 03              INC     BC                  
48C4: 1F              RRA                         
48C5: 07              RLCA                        
48C6: 1F              RRA                         
48C7: 0F              RRCA                        
48C8: 3F              CCF                         
48C9: 16 3F           LD      D,$3F               
48CB: 15              DEC     D                   
48CC: 3F              CCF                         
48CD: 1F              RRA                         
48CE: 3F              CCF                         
48CF: 1E 1F           LD      E,$1F               
48D1: 01 1F 0F        LD      BC,$0F1F            
48D4: 3F              CCF                         
48D5: 00              NOP                         
48D6: 7E              LD      A,(HL)              
48D7: 2D              DEC     L                   
48D8: 7E              LD      A,(HL)              
48D9: 2D              DEC     L                   
48DA: 7F              LD      A,A                 
48DB: 34              INC     (HL)                
48DC: 3F              CCF                         
48DD: 01 0F 00        LD      BC,$000F            
48E0: C0              RET     NZ                  
48E1: 00              NOP                         
48E2: F0 C0           LD      A,($C0)             
48E4: F8 F0           LD      HL,SP+$F0           
48E6: FC                              
48E7: E0 FE           LD      ($FF00+$FE),A       
48E9: DC DE FC        CALL    C,$FCDE             
48EC: FE FC           CP      $FC                 
48EE: FC                              
48EF: F0 F8           LD      A,($F8)             
48F1: F0 F0           LD      A,($F0)             
48F3: 80              ADD     A,B                 
48F4: 90              SUB     B                   
48F5: 60              LD      H,B                 
48F6: 10 E0           ;;STOP    $E0                 
48F8: 20 C0           JR      NZ,$48BA            ; {}
48FA: E0 00           LD      ($FF00+$00),A       
48FC: F0 E0           LD      A,($E0)             
48FE: F0 00           LD      A,($00)             
4900: 03              INC     BC                  
4901: 00              NOP                         
4902: 07              RLCA                        
4903: 03              INC     BC                  
4904: 07              RLCA                        
4905: 00              NOP                         
4906: FF              RST     0X38                
4907: 03              INC     BC                  
4908: FF              RST     0X38                
4909: 7A              LD      A,D                 
490A: FF              RST     0X38                
490B: 02              LD      (BC),A              
490C: FF              RST     0X38                
490D: 7B              LD      A,E                 
490E: FF              RST     0X38                
490F: 40              LD      B,B                 
4910: E0 40           LD      ($FF00+$40),A       
4912: E0 40           LD      ($FF00+$40),A       
4914: E0 40           LD      ($FF00+$40),A       
4916: E0 40           LD      ($FF00+$40),A       
4918: E0 00           LD      ($FF00+$00),A       
491A: 00              NOP                         
491B: 00              NOP                         
491C: 00              NOP                         
491D: 00              NOP                         
491E: 00              NOP                         
491F: 00              NOP                         
4920: 03              INC     BC                  
4921: 00              NOP                         
4922: 07              RLCA                        
4923: 03              INC     BC                  
4924: 07              RLCA                        
4925: 00              NOP                         
4926: 0F              RRCA                        
4927: 03              INC     BC                  
4928: 1F              RRA                         
4929: 0A              LD      A,(BC)              
492A: 3F              CCF                         
492B: 1A              LD      A,(DE)              
492C: 7F              LD      A,A                 
492D: 33              INC     SP                  
492E: FF              RST     0X38                
492F: 68              LD      L,B                 
4930: F8 50           LD      HL,SP+$50           
4932: F0 20           LD      A,($20)             
4934: F0 40           LD      A,($40)             
4936: 78              LD      A,B                 
4937: 20 3C           JR      NZ,$4975            ; {}
4939: 10 1C           ;;STOP    $1C                 
493B: 08 08 00        LD      ($0008),SP          
493E: 00              NOP                         
493F: 00              NOP                         
4940: 00              NOP                         
4941: 00              NOP                         
4942: 00              NOP                         
4943: 00              NOP                         
4944: FF              RST     0X38                
4945: 00              NOP                         
4946: FF              RST     0X38                
4947: 7E              LD      A,(HL)              
4948: FF              RST     0X38                
4949: 7E              LD      A,(HL)              
494A: 81              ADD     A,C                 
494B: 7E              LD      A,(HL)              
494C: BD              CP      L                   
494D: 42              LD      B,D                 
494E: A5              AND     L                   
494F: 5A              LD      E,D                 
4950: 85              ADD     A,L                 
4951: 7A              LD      A,D                 
4952: 9D              SBC     L                   
4953: 62              LD      H,D                 
4954: 99              SBC     C                   
4955: 66              LD      H,(HL)              
4956: 81              ADD     A,C                 
4957: 7E              LD      A,(HL)              
4958: 99              SBC     C                   
4959: 66              LD      H,(HL)              
495A: 81              ADD     A,C                 
495B: 7E              LD      A,(HL)              
495C: FF              RST     0X38                
495D: 00              NOP                         
495E: 00              NOP                         
495F: 00              NOP                         
4960: FF              RST     0X38                
4961: 00              NOP                         
4962: FF              RST     0X38                
4963: 7F              LD      A,A                 
4964: FF              RST     0X38                
4965: 00              NOP                         
4966: FF              RST     0X38                
4967: 6B              LD      L,E                 
4968: FF              RST     0X38                
4969: 5D              LD      E,L                 
496A: FF              RST     0X38                
496B: 5D              LD      E,L                 
496C: FF              RST     0X38                
496D: 6B              LD      L,E                 
496E: FF              RST     0X38                
496F: 00              NOP                         
4970: 02              LD      (BC),A              
4971: 01 02 01        LD      BC,$0102            
4974: 02              LD      (BC),A              
4975: 01 02 01        LD      BC,$0102            
4978: 02              LD      (BC),A              
4979: 01 02 01        LD      BC,$0102            
497C: 02              LD      (BC),A              
497D: 01 02 01        LD      BC,$0102            
4980: FF              RST     0X38                
4981: 00              NOP                         
4982: FF              RST     0X38                
4983: FE FF           CP      $FF                 
4985: 00              NOP                         
4986: FF              RST     0X38                
4987: C6 FF           ADD     $FF                 
4989: 82              ADD     A,D                 
498A: FF              RST     0X38                
498B: 82              ADD     A,D                 
498C: FF              RST     0X38                
498D: C6 FF           ADD     $FF                 
498F: 00              NOP                         
4990: 40              LD      B,B                 
4991: 80              ADD     A,B                 
4992: 40              LD      B,B                 
4993: 80              ADD     A,B                 
4994: 40              LD      B,B                 
4995: 80              ADD     A,B                 
4996: 40              LD      B,B                 
4997: 80              ADD     A,B                 
4998: 40              LD      B,B                 
4999: 80              ADD     A,B                 
499A: 40              LD      B,B                 
499B: 80              ADD     A,B                 
499C: 40              LD      B,B                 
499D: 80              ADD     A,B                 
499E: 40              LD      B,B                 
499F: 80              ADD     A,B                 
49A0: 78              LD      A,B                 
49A1: 00              NOP                         
49A2: 6C              LD      L,H                 
49A3: 00              NOP                         
49A4: 6C              LD      L,H                 
49A5: 00              NOP                         
49A6: 7C              LD      A,H                 
49A7: 00              NOP                         
49A8: 66              LD      H,(HL)              
49A9: 00              NOP                         
49AA: 66              LD      H,(HL)              
49AB: 00              NOP                         
49AC: 7E              LD      A,(HL)              
49AD: 00              NOP                         
49AE: 00              NOP                         
49AF: 00              NOP                         
49B0: 00              NOP                         
49B1: 00              NOP                         
49B2: 08 00 7C        LD      ($7C00),SP          ; {}
49B5: 00              NOP                         
49B6: 7E              LD      A,(HL)              
49B7: 00              NOP                         
49B8: 7E              LD      A,(HL)              
49B9: 00              NOP                         
49BA: 7C              LD      A,H                 
49BB: 00              NOP                         
49BC: 08 00 00        LD      ($0000),SP          
49BF: 00              NOP                         
49C0: 3C              INC     A                   
49C1: 00              NOP                         
49C2: 66              LD      H,(HL)              
49C3: 00              NOP                         
49C4: 66              LD      H,(HL)              
49C5: 00              NOP                         
49C6: 7E              LD      A,(HL)              
49C7: 00              NOP                         
49C8: 66              LD      H,(HL)              
49C9: 00              NOP                         
49CA: 66              LD      H,(HL)              
49CB: 00              NOP                         
49CC: 66              LD      H,(HL)              
49CD: 00              NOP                         
49CE: 00              NOP                         
49CF: 00              NOP                         
49D0: 00              NOP                         
49D1: 00              NOP                         
49D2: 3C              INC     A                   
49D3: 00              NOP                         
49D4: 3C              INC     A                   
49D5: 00              NOP                         
49D6: 3C              INC     A                   
49D7: 00              NOP                         
49D8: 7E              LD      A,(HL)              
49D9: 00              NOP                         
49DA: 3C              INC     A                   
49DB: 00              NOP                         
49DC: 18 00           JR      $49DE               ; {}
49DE: 00              NOP                         
49DF: 00              NOP                         
49E0: 02              LD      (BC),A              
49E1: 01 02 01        LD      BC,$0102            
49E4: 02              LD      (BC),A              
49E5: 01 02 01        LD      BC,$0102            
49E8: 02              LD      (BC),A              
49E9: 01 02 01        LD      BC,$0102            
49EC: 02              LD      (BC),A              
49ED: 01 02 01        LD      BC,$0102            
49F0: 00              NOP                         
49F1: 00              NOP                         
49F2: 00              NOP                         
49F3: 00              NOP                         
49F4: 00              NOP                         
49F5: 00              NOP                         
49F6: 00              NOP                         
49F7: 00              NOP                         
49F8: 00              NOP                         
49F9: 00              NOP                         
49FA: 00              NOP                         
49FB: 00              NOP                         
49FC: 00              NOP                         
49FD: 00              NOP                         
49FE: 00              NOP                         
49FF: 00              NOP                         
4A00: 00              NOP                         
4A01: 00              NOP                         
4A02: 00              NOP                         
4A03: 00              NOP                         
4A04: 00              NOP                         
4A05: 00              NOP                         
4A06: 00              NOP                         
4A07: 00              NOP                         
4A08: 30 00           JR      NC,$4A0A            ; {}
4A0A: 78              LD      A,B                 
4A0B: 30 7D           JR      NC,$4A8A            ; {}
4A0D: 38 5F           JR      C,$4A6E             ; {}
4A0F: 3D              DEC     A                   
4A10: 4F              LD      C,A                 
4A11: 3F              CCF                         
4A12: 2F              CPL                         
4A13: 1F              RRA                         
4A14: 27              DAA                         
4A15: 1B              DEC     DE                  
4A16: 17              RLA                         
4A17: 0B              DEC     BC                  
4A18: 0F              RRCA                        
4A19: 01 0F 07        LD      BC,$070F            
4A1C: 1F              RRA                         
4A1D: 0F              RRCA                        
4A1E: 1F              RRA                         
4A1F: 0F              RRCA                        
4A20: 00              NOP                         
4A21: 00              NOP                         
4A22: 00              NOP                         
4A23: 00              NOP                         
4A24: 03              INC     BC                  
4A25: 00              NOP                         
4A26: 1F              RRA                         
4A27: 03              INC     BC                  
4A28: 7F              LD      A,A                 
4A29: 1F              RRA                         
4A2A: FF              RST     0X38                
4A2B: 7F              LD      A,A                 
4A2C: FF              RST     0X38                
4A2D: F8 F8           LD      HL,SP+$F8           
4A2F: F7              RST     0X30                
4A30: F1              POP     AF                  
4A31: EF              RST     0X28                
4A32: E1              POP     HL                  
4A33: DE E3           SBC     $E3                 
4A35: DC A3 DC        CALL    C,$DCA3             
4A38: 1F              RRA                         
4A39: E3                              
4A3A: FF              RST     0X38                
4A3B: FF              RST     0X38                
4A3C: FF              RST     0X38                
4A3D: FF              RST     0X38                
4A3E: FF              RST     0X38                
4A3F: FF              RST     0X38                
4A40: 1F              RRA                         
4A41: 0F              RRCA                        
4A42: 1F              RRA                         
4A43: 0F              RRCA                        
4A44: 1F              RRA                         
4A45: 0F              RRCA                        
4A46: 17              RLA                         
4A47: 0F              RRCA                        
4A48: 17              RLA                         
4A49: 0F              RRCA                        
4A4A: 13              INC     DE                  
4A4B: 0F              RRCA                        
4A4C: 0B              DEC     BC                  
4A4D: 07              RLCA                        
4A4E: 09              ADD     HL,BC               
4A4F: 07              RLCA                        
4A50: 09              ADD     HL,BC               
4A51: 07              RLCA                        
4A52: 04              INC     B                   
4A53: 03              INC     BC                  
4A54: 02              LD      (BC),A              
4A55: 01 01 00        LD      BC,$0001            
4A58: 00              NOP                         
4A59: 00              NOP                         
4A5A: 00              NOP                         
4A5B: 00              NOP                         
4A5C: 00              NOP                         
4A5D: 00              NOP                         
4A5E: 00              NOP                         
4A5F: 00              NOP                         
4A60: FF              RST     0X38                
4A61: 3F              CCF                         
4A62: FF              RST     0X38                
4A63: 0F              RRCA                        
4A64: FF              RST     0X38                
4A65: 00              NOP                         
4A66: FF              RST     0X38                
4A67: 80              ADD     A,B                 
4A68: FF              RST     0X38                
4A69: C0              RET     NZ                  
4A6A: F1              POP     AF                  
4A6B: CE E2           ADC     $E2                 
4A6D: DD                              
4A6E: E2              LD      (C),A               
4A6F: DD                              
4A70: E2              LD      (C),A               
4A71: DD                              
4A72: E2              LD      (C),A               
4A73: DD                              
4A74: 70              LD      (HL),B              
4A75: EF              RST     0X28                
4A76: 33              INC     SP                  
4A77: EF              RST     0X28                
4A78: 88              ADC     A,B                 
4A79: 77              LD      (HL),A              
4A7A: 67              LD      H,A                 
4A7B: 18 18           JR      $4A95               ; {}
4A7D: 07              RLCA                        
4A7E: 07              RLCA                        
4A7F: 00              NOP                         
4A80: FF              RST     0X38                
4A81: FC                              
4A82: FF              RST     0X38                
4A83: F0 FF           LD      A,($FF)             
4A85: 00              NOP                         
4A86: FF              RST     0X38                
4A87: 00              NOP                         
4A88: FF              RST     0X38                
4A89: 01 0F F7        LD      BC,$F70F            
4A8C: 1F              RRA                         
4A8D: EF              RST     0X28                
4A8E: 1F              RRA                         
4A8F: EF              RST     0X28                
4A90: 1F              RRA                         
4A91: EF              RST     0X28                
4A92: 1E EF           LD      E,$EF               
4A94: 1F              RRA                         
4A95: EF              RST     0X28                
4A96: 3F              CCF                         
4A97: DF              RST     0X18                
4A98: 7F              LD      A,A                 
4A99: BF              CP      A                   
4A9A: 80              ADD     A,B                 
4A9B: 7F              LD      A,A                 
4A9C: 01 FE FE        LD      BC,$FEFE            
4A9F: 00              NOP                         
4AA0: F8 F0           LD      HL,SP+$F0           
4AA2: F8 F0           LD      HL,SP+$F0           
4AA4: FB              EI                          
4AA5: F0 EF           LD      A,($EF)             
4AA7: F2                              
4AA8: EF              RST     0X28                
4AA9: F6 CF           OR      $CF                 
4AAB: F6 DD           OR      $DD                 
4AAD: EE 9D           XOR     $9D                 
4AAF: EE 39           XOR     $39                 
4AB1: DE 7A           SBC     $7A                 
4AB3: BC              CP      H                   
4AB4: F2                              
4AB5: FC                              
4AB6: E4                              
4AB7: F8 08           LD      HL,SP+$08           
4AB9: F0 30           LD      A,($30)             
4ABB: C0              RET     NZ                  
4ABC: C0              RET     NZ                  
4ABD: 00              NOP                         
4ABE: 00              NOP                         
4ABF: 00              NOP                         
4AC0: FF              RST     0X38                
4AC1: 7F              LD      A,A                 
4AC2: FF              RST     0X38                
4AC3: 1F              RRA                         
4AC4: FF              RST     0X38                
4AC5: 80              ADD     A,B                 
4AC6: F1              POP     AF                  
4AC7: CE E2           ADC     $E2                 
4AC9: DD                              
4ACA: E2              LD      (C),A               
4ACB: DD                              
4ACC: F0 EF           LD      A,($EF)             
4ACE: F3              DI                          
4ACF: EF              RST     0X28                
4AD0: F8 F7           LD      HL,SP+$F7           
4AD2: FF              RST     0X38                
4AD3: F8 7F           LD      HL,SP+$7F           
4AD5: FF              RST     0X38                
4AD6: 3F              CCF                         
4AD7: FF              RST     0X38                
4AD8: 87              ADD     A,A                 
4AD9: 7F              LD      A,A                 
4ADA: 60              LD      H,B                 
4ADB: 1F              RRA                         
4ADC: 18 07           JR      $4AE5               ; {}
4ADE: 07              RLCA                        
4ADF: 00              NOP                         
4AE0: FF              RST     0X38                
4AE1: FE FF           CP      $FF                 
4AE3: F8 FF           LD      HL,SP+$FF           
4AE5: 01 1F E7        LD      BC,$E71F            
4AE8: 0F              RRCA                        
4AE9: F7              RST     0X30                
4AEA: 0F              RRCA                        
4AEB: F7              RST     0X30                
4AEC: 1F              RRA                         
4AED: EF              RST     0X28                
4AEE: 1F              RRA                         
4AEF: EF              RST     0X28                
4AF0: 3F              CCF                         
4AF1: DF              RST     0X18                
4AF2: FE 3F           CP      $3F                 
4AF4: FF              RST     0X38                
4AF5: FF              RST     0X38                
4AF6: FF              RST     0X38                
4AF7: FF              RST     0X38                
4AF8: FF              RST     0X38                
4AF9: FF              RST     0X38                
4AFA: 00              NOP                         
4AFB: FF              RST     0X38                
4AFC: 01 FE FE        LD      BC,$FEFE            
4AFF: 00              NOP                         
4B00: 0F              RRCA                        
4B01: 00              NOP                         
4B02: 10 0F           ;;STOP    $0F                 
4B04: 1C              INC     E                   
4B05: 03              INC     BC                  
4B06: 3E 1D           LD      A,$1D               
4B08: 7F              LD      A,A                 
4B09: 3E 7F           LD      A,$7F               
4B0B: 36 7F           LD      (HL),$7F            
4B0D: 36 7F           LD      (HL),$7F            
4B0F: 1C              INC     E                   
4B10: 9C              SBC     H                   
4B11: 60              LD      H,B                 
4B12: 98              SBC     B                   
4B13: 70              LD      (HL),B              
4B14: B8              CP      B                   
4B15: 70              LD      (HL),B              
4B16: B8              CP      B                   
4B17: 70              LD      (HL),B              
4B18: B8              CP      B                   
4B19: 70              LD      (HL),B              
4B1A: 7C              LD      A,H                 
4B1B: 38 3E           JR      C,$4B5B             ; {}
4B1D: 1C              INC     E                   
4B1E: 1E 00           LD      E,$00               
4B20: 3E 00           LD      A,$00               
4B22: 7F              LD      A,A                 
4B23: 3E E3           LD      A,$E3               
4B25: 7E              LD      A,(HL)              
4B26: DD                              
4B27: 62              LD      H,D                 
4B28: E3                              
4B29: 40              LD      B,B                 
4B2A: C1              POP     BC                  
4B2B: 00              NOP                         
4B2C: 01 00 01        LD      BC,$0100            
4B2F: 00              NOP                         
4B30: C1              POP     BC                  
4B31: 00              NOP                         
4B32: E3                              
4B33: 40              LD      B,B                 
4B34: FF              RST     0X38                
4B35: 63              LD      H,E                 
4B36: BF              CP      A                   
4B37: 7F              LD      A,A                 
4B38: 5E              LD      E,(HL)              
4B39: 3F              CCF                         
4B3A: 21 1E 1E        LD      HL,$1E1E            
4B3D: 00              NOP                         
4B3E: 00              NOP                         
4B3F: 00              NOP                         
4B40: 70              LD      (HL),B              
4B41: 00              NOP                         
4B42: F8 70           LD      HL,SP+$70           
4B44: FC                              
4B45: 98              SBC     B                   
4B46: FA F4 71        LD      A,($71F4)           ; {}
4B49: 8E              ADC     A,(HL)              
4B4A: F9              LD      SP,HL               
4B4B: 76              HALT                        
4B4C: FD                              
4B4D: FA FD 9A        LD      A,($9AFD)           
4B50: F5              PUSH    AF                  
4B51: FA 69 F6        LD      A,($F669)           
4B54: F1              POP     AF                  
4B55: 0E 43           LD      C,$43               
4B57: BC              CP      H                   
4B58: 86              ADD     A,(HL)              
4B59: 78              LD      A,B                 
4B5A: FC                              
4B5B: 00              NOP                         
4B5C: 00              NOP                         
4B5D: 00              NOP                         
4B5E: 00              NOP                         
4B5F: 00              NOP                         
4B60: 01 00 0F        LD      BC,$0F00            
4B63: 01 37 0B        LD      BC,$0B37            
4B66: 47              LD      B,A                 
4B67: 3A              LD      A,(HLD)             
4B68: 5F              LD      E,A                 
4B69: 3A              LD      A,(HLD)             
4B6A: BF              CP      A                   
4B6B: 79              LD      A,C                 
4B6C: B9              CP      C                   
4B6D: 70              LD      (HL),B              
4B6E: F0 60           LD      A,($60)             
4B70: F0 60           LD      A,($60)             
4B72: F0 60           LD      A,($60)             
4B74: E0 40           LD      ($FF00+$40),A       
4B76: 60              LD      H,B                 
4B77: 00              NOP                         
4B78: 03              INC     BC                  
4B79: 00              NOP                         
4B7A: 0F              RRCA                        
4B7B: 03              INC     BC                  
4B7C: 0F              RRCA                        
4B7D: 07              RLCA                        
4B7E: 07              RLCA                        
4B7F: 00              NOP                         
4B80: F8 00           LD      HL,SP+$00           
4B82: E4                              
4B83: D8              RET     C                   
4B84: F2                              
4B85: EC                              
4B86: F1              POP     AF                  
4B87: 6E              LD      L,(HL)              
4B88: FD                              
4B89: E2              LD      (C),A               
4B8A: FF              RST     0X38                
4B8B: DC FF 3E        CALL    C,$3EFF             
4B8E: 7F              LD      A,A                 
4B8F: 36 7F           LD      (HL),$7F            
4B91: 26 7E           LD      H,$7E               
4B93: 1C              INC     E                   
4B94: 3E 00           LD      A,$00               
4B96: 72              LD      (HL),D              
4B97: 3C              INC     A                   
4B98: F4                              
4B99: 78              LD      A,B                 
4B9A: E4                              
4B9B: F8 98           LD      HL,SP+$98           
4B9D: E0 E0           LD      ($FF00+$E0),A       
4B9F: 00              NOP                         
4BA0: 00              NOP                         
4BA1: 00              NOP                         
4BA2: 00              NOP                         
4BA3: 00              NOP                         
4BA4: 00              NOP                         
4BA5: 00              NOP                         
4BA6: 00              NOP                         
4BA7: 00              NOP                         
4BA8: 3C              INC     A                   
4BA9: 00              NOP                         
4BAA: 5A              LD      E,D                 
4BAB: 3C              INC     A                   
4BAC: A5              AND     L                   
4BAD: 7E              LD      A,(HL)              
4BAE: A5              AND     L                   
4BAF: 7E              LD      A,(HL)              
4BB0: 99              SBC     C                   
4BB1: 7E              LD      A,(HL)              
4BB2: 81              ADD     A,C                 
4BB3: 7E              LD      A,(HL)              
4BB4: 42              LD      B,D                 
4BB5: 3C              INC     A                   
4BB6: 3C              INC     A                   
4BB7: 00              NOP                         
4BB8: 00              NOP                         
4BB9: 00              NOP                         
4BBA: 00              NOP                         
4BBB: 00              NOP                         
4BBC: 00              NOP                         
4BBD: 00              NOP                         
4BBE: 00              NOP                         
4BBF: 00              NOP                         
4BC0: 00              NOP                         
4BC1: 00              NOP                         
4BC2: 00              NOP                         
4BC3: 00              NOP                         
4BC4: 00              NOP                         
4BC5: 00              NOP                         
4BC6: 00              NOP                         
4BC7: 00              NOP                         
4BC8: 0F              RRCA                        
4BC9: 00              NOP                         
4BCA: 13              INC     DE                  
4BCB: 0C              INC     C                   
4BCC: 2D              DEC     L                   
4BCD: 1E 3F           LD      E,$3F               
4BCF: 1A              LD      A,(DE)              
4BD0: 3F              CCF                         
4BD1: 1A              LD      A,(DE)              
4BD2: 2D              DEC     L                   
4BD3: 1E 33           LD      E,$33               
4BD5: 0C              INC     C                   
4BD6: 1F              RRA                         
4BD7: 00              NOP                         
4BD8: 07              RLCA                        
4BD9: 00              NOP                         
4BDA: 00              NOP                         
4BDB: 00              NOP                         
4BDC: 00              NOP                         
4BDD: 00              NOP                         
4BDE: 00              NOP                         
4BDF: 00              NOP                         
4BE0: 00              NOP                         
4BE1: 00              NOP                         
4BE2: 00              NOP                         
4BE3: 00              NOP                         
4BE4: 00              NOP                         
4BE5: 00              NOP                         
4BE6: 00              NOP                         
4BE7: 00              NOP                         
4BE8: 0F              RRCA                        
4BE9: 00              NOP                         
4BEA: 1F              RRA                         
4BEB: 00              NOP                         
4BEC: 3F              CCF                         
4BED: 00              NOP                         
4BEE: 3F              CCF                         
4BEF: 00              NOP                         
4BF0: 3F              CCF                         
4BF1: 00              NOP                         
4BF2: 3F              CCF                         
4BF3: 00              NOP                         
4BF4: 3F              CCF                         
4BF5: 00              NOP                         
4BF6: 1F              RRA                         
4BF7: 00              NOP                         
4BF8: 0F              RRCA                        
4BF9: 00              NOP                         
4BFA: 00              NOP                         
4BFB: 00              NOP                         
4BFC: 00              NOP                         
4BFD: 00              NOP                         
4BFE: 00              NOP                         
4BFF: 00              NOP                         
4C00: 00              NOP                         
4C01: 00              NOP                         
4C02: 00              NOP                         
4C03: 00              NOP                         
4C04: 00              NOP                         
4C05: 00              NOP                         
4C06: 06 00           LD      B,$00               
4C08: 0F              RRCA                        
4C09: 06 1F           LD      B,$1F               
4C0B: 0A              LD      A,(BC)              
4C0C: 1F              RRA                         
4C0D: 08 1F 01        LD      ($011F),SP          
4C10: 07              RLCA                        
4C11: 01 1F 00        LD      BC,$001F            
4C14: 3F              CCF                         
4C15: 1C              INC     E                   
4C16: 7F              LD      A,A                 
4C17: 20 F0           JR      NZ,$4C09            ; {}
4C19: 40              LD      B,B                 
4C1A: E0 00           LD      ($FF00+$00),A       
4C1C: 00              NOP                         
4C1D: 00              NOP                         
4C1E: 00              NOP                         
4C1F: 00              NOP                         
4C20: 00              NOP                         
4C21: 00              NOP                         
4C22: 00              NOP                         
4C23: 00              NOP                         
4C24: 00              NOP                         
4C25: 00              NOP                         
4C26: 00              NOP                         
4C27: 00              NOP                         
4C28: 3C              INC     A                   
4C29: 00              NOP                         
4C2A: 7E              LD      A,(HL)              
4C2B: 3C              INC     A                   
4C2C: FF              RST     0X38                
4C2D: 02              LD      (BC),A              
4C2E: 63              LD      H,E                 
4C2F: 80              ADD     A,B                 
4C30: E0 00           LD      ($FF00+$00),A       
4C32: F0 60           LD      A,($60)             
4C34: F8 50           LD      HL,SP+$50           
4C36: F8 10           LD      HL,SP+$10           
4C38: 38 10           JR      C,$4C4A             ; {}
4C3A: 18 00           JR      $4C3C               ; {}
4C3C: 00              NOP                         
4C3D: 00              NOP                         
4C3E: 00              NOP                         
4C3F: 00              NOP                         
4C40: 06 00           LD      B,$00               
4C42: 0F              RRCA                        
4C43: 04              INC     B                   
4C44: 1C              INC     E                   
4C45: 03              INC     BC                  
4C46: 30 0F           JR      NC,$4C57            ; {}
4C48: 67              LD      H,A                 
4C49: 18 E7           JR      $4C32               ; {}
4C4B: 5A              LD      E,D                 
4C4C: C7              RST     0X00                
4C4D: 38 40           JR      C,$4C8F             ; {}
4C4F: 3F              CCF                         
4C50: 49              LD      C,C                 
4C51: 36 EF           LD      (HL),$EF            
4C53: 10 E6           ;;STOP    $E6                 
4C55: 59              LD      E,C                 
4C56: 70              LD      (HL),B              
4C57: 0F              RRCA                        
4C58: 1C              INC     E                   
4C59: 03              INC     BC                  
4C5A: 1F              RRA                         
4C5B: 08 0C 00        LD      ($000C),SP          
4C5E: 00              NOP                         
4C5F: 00              NOP                         
4C60: 00              NOP                         
4C61: 00              NOP                         
4C62: 06 00           LD      B,$00               
4C64: 0F              RRCA                        
4C65: 04              INC     B                   
4C66: 0E 01           LD      C,$01               
4C68: 38 07           JR      C,$4C71             ; {}
4C6A: 72              LD      (HL),D              
4C6B: 2D              DEC     L                   
4C6C: 77              LD      (HL),A              
4C6D: 0A              LD      A,(BC)              
4C6E: 22              LD      (HLI),A             
4C6F: 1D              DEC     E                   
4C70: 22              LD      (HLI),A             
4C71: 1D              DEC     E                   
4C72: 77              LD      (HL),A              
4C73: 0A              LD      A,(BC)              
4C74: 72              LD      (HL),D              
4C75: 2D              DEC     L                   
4C76: 38 07           JR      C,$4C7F             ; {}
4C78: 0E 01           LD      C,$01               
4C7A: 0F              RRCA                        
4C7B: 04              INC     B                   
4C7C: 06 00           LD      B,$00               
4C7E: 00              NOP                         
4C7F: 00              NOP                         
4C80: 1C              INC     E                   
4C81: 00              NOP                         
4C82: 13              INC     DE                  
4C83: 0C              INC     C                   
4C84: 18 07           JR      $4C8D               ; {}
4C86: 1C              INC     E                   
4C87: 0B              DEC     BC                  
4C88: 3E 1D           LD      A,$1D               
4C8A: 3F              CCF                         
4C8B: 18 3E           JR      $4CCB               ; {}
4C8D: 19              ADD     HL,DE               
4C8E: 2F              CPL                         
4C8F: 1E 37           LD      E,$37               
4C91: 0D              DEC     C                   
4C92: 5F              LD      E,A                 
4C93: 21 56 2D        LD      HL,$2D56            
4C96: 57              LD      D,A                 
4C97: 2E 4B           LD      L,$4B               
4C99: 37              SCF                         
4C9A: 3C              INC     A                   
4C9B: 03              INC     BC                  
4C9C: 37              SCF                         
4C9D: 1C              INC     E                   
4C9E: 3F              CCF                         
4C9F: 00              NOP                         
4CA0: 1C              INC     E                   
4CA1: 00              NOP                         
4CA2: 13              INC     DE                  
4CA3: 0C              INC     C                   
4CA4: 18 07           JR      $4CAD               ; {}
4CA6: 14              INC     D                   
4CA7: 0B              DEC     BC                  
4CA8: 22              LD      (HLI),A             
4CA9: 1D              DEC     E                   
4CAA: 21 1E 3E        LD      HL,$3E1E            
4CAD: 01 21 1E        LD      BC,$1E21            
4CB0: 33              INC     SP                  
4CB1: 0D              DEC     C                   
4CB2: 5F              LD      E,A                 
4CB3: 21 56 2D        LD      HL,$2D56            
4CB6: 57              LD      D,A                 
4CB7: 2E 4B           LD      L,$4B               
4CB9: 37              SCF                         
4CBA: 3C              INC     A                   
4CBB: 03              INC     BC                  
4CBC: 37              SCF                         
4CBD: 1C              INC     E                   
4CBE: 3F              CCF                         
4CBF: 00              NOP                         
4CC0: 00              NOP                         
4CC1: 00              NOP                         
4CC2: 00              NOP                         
4CC3: 00              NOP                         
4CC4: 00              NOP                         
4CC5: 00              NOP                         
4CC6: 07              RLCA                        
4CC7: 00              NOP                         
4CC8: 08 07 08        LD      ($0807),SP          
4CCB: 07              RLCA                        
4CCC: 07              RLCA                        
4CCD: 00              NOP                         
4CCE: 03              INC     BC                  
4CCF: 01 01 00        LD      BC,$0001            
4CD2: 00              NOP                         
4CD3: 00              NOP                         
4CD4: 00              NOP                         
4CD5: 00              NOP                         
4CD6: 00              NOP                         
4CD7: 00              NOP                         
4CD8: 00              NOP                         
4CD9: 00              NOP                         
4CDA: 00              NOP                         
4CDB: 00              NOP                         
4CDC: 00              NOP                         
4CDD: 00              NOP                         
4CDE: 00              NOP                         
4CDF: 00              NOP                         
4CE0: 1C              INC     E                   
4CE1: 00              NOP                         
4CE2: 13              INC     DE                  
4CE3: 0C              INC     C                   
4CE4: 18 07           JR      $4CED               ; {}
4CE6: 9C              SBC     H                   
4CE7: 0B              DEC     BC                  
4CE8: 7E              LD      A,(HL)              
4CE9: 9D              SBC     L                   
4CEA: 3F              CCF                         
4CEB: D8              RET     C                   
4CEC: BE              CP      (HL)                
4CED: D9              RETI                        
4CEE: EF              RST     0X28                
4CEF: DE F7           SBC     $F7                 
4CF1: 6D              LD      L,L                 
4CF2: 5F              LD      E,A                 
4CF3: 31 3E 1D        LD      SP,$1D3E            
4CF6: 2F              CPL                         
4CF7: 1E 17           LD      E,$17               
4CF9: 0F              RRCA                        
4CFA: 1C              INC     E                   
4CFB: 03              INC     BC                  
4CFC: 37              SCF                         
4CFD: 1C              INC     E                   
4CFE: 3F              CCF                         
4CFF: 00              NOP                         
4D00: 03              INC     BC                  
4D01: 00              NOP                         
4D02: 0D              DEC     C                   
4D03: 02              LD      (BC),A              
4D04: 1F              RRA                         
4D05: 09              ADD     HL,BC               
4D06: 1F              RRA                         
4D07: 0C              INC     C                   
4D08: 37              SCF                         
4D09: 0D              DEC     C                   
4D0A: 2D              DEC     L                   
4D0B: 17              RLA                         
4D0C: 25              DEC     H                   
4D0D: 1B              DEC     DE                  
4D0E: 3F              CCF                         
4D0F: 00              NOP                         
4D10: 47              LD      B,A                 
4D11: 3F              CCF                         
4D12: A7              AND     A                   
4D13: 7F              LD      A,A                 
4D14: A7              AND     A                   
4D15: 7F              LD      A,A                 
4D16: A7              AND     A                   
4D17: 7F              LD      A,A                 
4D18: A7              AND     A                   
4D19: 7F              LD      A,A                 
4D1A: A7              AND     A                   
4D1B: 7F              LD      A,A                 
4D1C: A3              AND     E                   
4D1D: 7F              LD      A,A                 
4D1E: B1              OR      C                   
4D1F: 7F              LD      A,A                 
4D20: F0 00           LD      A,($00)             
4D22: FC                              
4D23: F4                              
4D24: FF              RST     0X38                
4D25: 00              NOP                         
4D26: FF              RST     0X38                
4D27: E1              POP     HL                  
4D28: FF              RST     0X38                
4D29: 30 FF           JR      NC,$4D2A            ; {}
4D2B: E8 F6           ADD     SP,$F6              
4D2D: BA              CP      D                   
4D2E: FC                              
4D2F: 00              NOP                         
4D30: FA FC ED        LD      A,($EDFC)           
4D33: FE F5           CP      $F5                 
4D35: FE F5           CP      $F5                 
4D37: FE F5           CP      $F5                 
4D39: FE F5           CP      $F5                 
4D3B: FE F5           CP      $F5                 
4D3D: FE CD           CP      $CD                 
4D3F: FE 00           CP      $00                 
4D41: 00              NOP                         
4D42: 07              RLCA                        
4D43: 00              NOP                         
4D44: 0B              DEC     BC                  
4D45: 07              RLCA                        
4D46: 1B              DEC     DE                  
4D47: 04              INC     B                   
4D48: 3F              CCF                         
4D49: 13              INC     DE                  
4D4A: 3F              CCF                         
4D4B: 14              INC     D                   
4D4C: 3F              CCF                         
4D4D: 10 27           ;;STOP    $27                 
4D4F: 18 3F           JR      $4D90               ; {}
4D51: 0D              DEC     C                   
4D52: 37              SCF                         
4D53: 0D              DEC     C                   
4D54: 6B              LD      L,E                 
4D55: 17              RLA                         
4D56: EF              RST     0X28                
4D57: 58              LD      E,B                 
4D58: DF              RST     0X18                
4D59: 6C              LD      L,H                 
4D5A: ED                              
4D5B: 73              LD      (HL),E              
4D5C: 7F              LD      A,A                 
4D5D: 3F              CCF                         
4D5E: 3F              CCF                         
4D5F: 40              LD      B,B                 
4D60: 00              NOP                         
4D61: 00              NOP                         
4D62: C0              RET     NZ                  
4D63: 00              NOP                         
4D64: 20 C0           JR      NZ,$4D26            ; {}
4D66: 18 E0           JR      $4D48               ; {}
4D68: DC E8 FC        CALL    C,$FCE8             
4D6B: 28 FC           JR      Z,$4D69             ; {}
4D6D: 08 E4 18        LD      ($18E4),SP          
4D70: F8 B0           LD      HL,SP+$B0           
4D72: EC                              
4D73: B0              OR      B                   
4D74: D6 E8           SUB     $E8                 
4D76: F7              RST     0X30                
4D77: 1A              LD      A,(DE)              
4D78: FB              EI                          
4D79: 36 B7           LD      (HL),$B7            
4D7B: CE FE           ADC     $FE                 
4D7D: FC                              
4D7E: FC                              
4D7F: 02              LD      (BC),A              
4D80: 00              NOP                         
4D81: 00              NOP                         
4D82: 07              RLCA                        
4D83: 00              NOP                         
4D84: 08 07 13        LD      ($1307),SP          
4D87: 0F              RRCA                        
4D88: 24              INC     H                   
4D89: 1B              DEC     DE                  
4D8A: 4F              LD      C,A                 
4D8B: 34              INC     (HL)                
4D8C: 4D              LD      C,L                 
4D8D: 36 2F           LD      (HL),$2F            
4D8F: 16 1F           LD      D,$1F               
4D91: 06 2B           LD      B,$2B               
4D93: 16 6D           LD      D,$6D               
4D95: 12              LD      (DE),A              
4D96: EF              RST     0X28                
4D97: 5C              LD      E,H                 
4D98: DF              RST     0X18                
4D99: 6C              LD      L,H                 
4D9A: ED                              
4D9B: 73              LD      (HL),E              
4D9C: 7F              LD      A,A                 
4D9D: 3F              CCF                         
4D9E: 3F              CCF                         
4D9F: 40              LD      B,B                 
4DA0: 00              NOP                         
4DA1: 00              NOP                         
4DA2: C0              RET     NZ                  
4DA3: 00              NOP                         
4DA4: B0              OR      B                   
4DA5: C0              RET     NZ                  
4DA6: 78              LD      A,B                 
4DA7: B0              OR      B                   
4DA8: EE 70           XOR     $70                 
4DAA: DC E0 70        CALL    C,$70E0             ; {}
4DAD: 80              ADD     A,B                 
4DAE: FC                              
4DAF: 50              LD      D,B                 
4DB0: FC                              
4DB1: D8              RET     C                   
4DB2: E8 F0           ADD     SP,$F0              
4DB4: 16 E8           LD      D,$E8               
4DB6: F7              RST     0X30                
4DB7: 1A              LD      A,(DE)              
4DB8: FB              EI                          
4DB9: 36 B7           LD      (HL),$B7            
4DBB: CE FE           ADC     $FE                 
4DBD: FC                              
4DBE: FC                              
4DBF: 02              LD      (BC),A              
4DC0: 00              NOP                         
4DC1: 00              NOP                         
4DC2: C0              RET     NZ                  
4DC3: 00              NOP                         
4DC4: B0              OR      B                   
4DC5: C0              RET     NZ                  
4DC6: 78              LD      A,B                 
4DC7: B0              OR      B                   
4DC8: EE 70           XOR     $70                 
4DCA: DC E0 70        CALL    C,$70E0             ; {}
4DCD: 80              ADD     A,B                 
4DCE: FC                              
4DCF: 70              LD      (HL),B              
4DD0: FC                              
4DD1: D8              RET     C                   
4DD2: E8 F0           ADD     SP,$F0              
4DD4: 16 E8           LD      D,$E8               
4DD6: F7              RST     0X30                
4DD7: 1A              LD      A,(DE)              
4DD8: FB              EI                          
4DD9: 36 B7           LD      (HL),$B7            
4DDB: CE FE           ADC     $FE                 
4DDD: FC                              
4DDE: FC                              
4DDF: 02              LD      (BC),A              
4DE0: 00              NOP                         
4DE1: 00              NOP                         
4DE2: 00              NOP                         
4DE3: 00              NOP                         
4DE4: 22              LD      (HLI),A             
4DE5: 00              NOP                         
4DE6: 14              INC     D                   
4DE7: 00              NOP                         
4DE8: 08 00 14        LD      ($1400),SP          
4DEB: 00              NOP                         
4DEC: 22              LD      (HLI),A             
4DED: 00              NOP                         
4DEE: 00              NOP                         
4DEF: 00              NOP                         
4DF0: 00              NOP                         
4DF1: 00              NOP                         
4DF2: 00              NOP                         
4DF3: 00              NOP                         
4DF4: 22              LD      (HLI),A             
4DF5: 00              NOP                         
4DF6: 14              INC     D                   
4DF7: 00              NOP                         
4DF8: 08 00 14        LD      ($1400),SP          
4DFB: 00              NOP                         
4DFC: 22              LD      (HLI),A             
4DFD: 00              NOP                         
4DFE: 00              NOP                         
4DFF: 00              NOP                         
4E00: 15              DEC     D                   
4E01: 00              NOP                         
4E02: 1F              RRA                         
4E03: 00              NOP                         
4E04: 1F              RRA                         
4E05: 00              NOP                         
4E06: 3F              CCF                         
4E07: 07              RLCA                        
4E08: 7F              LD      A,A                 
4E09: 2D              DEC     L                   
4E0A: 7F              LD      A,A                 
4E0B: 28 5B           JR      Z,$4E68             ; {}
4E0D: 37              SCF                         
4E0E: 38 17           JR      C,$4E27             ; {}
4E10: 3F              CCF                         
4E11: 10 3F           ;;STOP    $3F                 
4E13: 08 7F 27        LD      ($277F),SP          
4E16: 77              LD      (HL),A              
4E17: 28 33           JR      Z,$4E4C             ; {}
4E19: 0F              RRCA                        
4E1A: 1E 01           LD      E,$01               
4E1C: 3D              DEC     A                   
4E1D: 1E 1F           LD      E,$1F               
4E1F: 00              NOP                         
4E20: E0 00           LD      ($FF00+$00),A       
4E22: F8 00           LD      HL,SP+$00           
4E24: FC                              
4E25: 00              NOP                         
4E26: FC                              
4E27: E0 FE           LD      ($FF00+$FE),A       
4E29: B4              OR      H                   
4E2A: FE B4           CP      $B4                 
4E2C: 3A              LD      A,(HLD)             
4E2D: FC                              
4E2E: 3C              INC     A                   
4E2F: C8              RET     Z                   
4E30: FC                              
4E31: 18 FA           JR      $4E2D               ; {}
4E33: 34              INC     (HL)                
4E34: F2                              
4E35: CC FA 34        CALL    Z,$34FA             
4E38: FC                              
4E39: B0              OR      B                   
4E3A: 78              LD      A,B                 
4E3B: 80              ADD     A,B                 
4E3C: BC              CP      H                   
4E3D: 78              LD      A,B                 
4E3E: F8 00           LD      HL,SP+$00           
4E40: 2B              DEC     HL                  
4E41: 2B              DEC     HL                  
4E42: 7F              LD      A,A                 
4E43: 54              LD      D,H                 
4E44: 7F              LD      A,A                 
4E45: 40              LD      B,B                 
4E46: 7F              LD      A,A                 
4E47: 40              LD      B,B                 
4E48: 3F              CCF                         
4E49: 2F              CPL                         
4E4A: 7F              LD      A,A                 
4E4B: 5F              LD      E,A                 
4E4C: 7F              LD      A,A                 
4E4D: 44              LD      B,H                 
4E4E: 5B              LD      E,E                 
4E4F: 3F              CCF                         
4E50: 43              LD      B,E                 
4E51: 3C              INC     A                   
4E52: 7F              LD      A,A                 
4E53: 00              NOP                         
4E54: 37              SCF                         
4E55: 0F              RRCA                        
4E56: 6F              LD      L,A                 
4E57: 3F              CCF                         
4E58: DF              RST     0X18                
4E59: 7F              LD      A,A                 
4E5A: C7              RST     0X00                
4E5B: 7F              LD      A,A                 
4E5C: CF              RST     0X08                
4E5D: 7F              LD      A,A                 
4E5E: DF              RST     0X18                
4E5F: 7F              LD      A,A                 
4E60: C0              RET     NZ                  
4E61: C0              RET     NZ                  
4E62: F0 30           LD      A,($30)             
4E64: F8 08           LD      HL,SP+$08           
4E66: FC                              
4E67: 04              INC     B                   
4E68: FE 02           CP      $02                 
4E6A: FE DA           CP      $DA                 
4E6C: FE DA           CP      $DA                 
4E6E: F6 FA           OR      $FA                 
4E70: FC                              
4E71: 74              LD      (HL),H              
4E72: FC                              
4E73: 04              INC     B                   
4E74: DC E4 E4        CALL    C,$E4E4             
4E77: F8 F2           LD      HL,SP+$F2           
4E79: FC                              
4E7A: F2                              
4E7B: FC                              
4E7C: E6 FC           AND     $FC                 
4E7E: 8E              ADC     A,(HL)              
4E7F: FC                              
4E80: 2B              DEC     HL                  
4E81: 00              NOP                         
4E82: 3F              CCF                         
4E83: 00              NOP                         
4E84: 3F              CCF                         
4E85: 00              NOP                         
4E86: 1F              RRA                         
4E87: 0F              RRCA                        
4E88: 3F              CCF                         
4E89: 15              DEC     D                   
4E8A: 3F              CCF                         
4E8B: 05              DEC     B                   
4E8C: 5B              LD      E,E                 
4E8D: 3F              CCF                         
4E8E: 43              LD      B,E                 
4E8F: 3C              INC     A                   
4E90: 7F              LD      A,A                 
4E91: 00              NOP                         
4E92: 3F              CCF                         
4E93: 01 17 0F        LD      BC,$0F17            
4E96: 0F              RRCA                        
4E97: 00              NOP                         
4E98: 11 0E 1F        LD      DE,$1F0E            
4E9B: 00              NOP                         
4E9C: 0B              DEC     BC                  
4E9D: 07              RLCA                        
4E9E: 1F              RRA                         
4E9F: 00              NOP                         
4EA0: C0              RET     NZ                  
4EA1: 00              NOP                         
4EA2: F0 00           LD      A,($00)             
4EA4: F8 00           LD      HL,SP+$00           
4EA6: FC                              
4EA7: 00              NOP                         
4EA8: FC                              
4EA9: D8              RET     C                   
4EAA: FC                              
4EAB: D8              RET     C                   
4EAC: F4                              
4EAD: F8 F8           LD      HL,SP+$F8           
4EAF: 70              LD      (HL),B              
4EB0: F8 F0           LD      HL,SP+$F0           
4EB2: F8 E0           LD      HL,SP+$E0           
4EB4: E4                              
4EB5: 18 E4           JR      $4E9B               ; {}
4EB7: D8              RET     C                   
4EB8: E4                              
4EB9: D8              RET     C                   
4EBA: F8 00           LD      HL,SP+$00           
4EBC: D0              RET     NC                  
4EBD: E0 F8           LD      ($FF00+$F8),A       
4EBF: 00              NOP                         
4EC0: 7F              LD      A,A                 
4EC1: 00              NOP                         
4EC2: 7F              LD      A,A                 
4EC3: 3F              CCF                         
4EC4: 7F              LD      A,A                 
4EC5: 22              LD      (HLI),A             
4EC6: 7F              LD      A,A                 
4EC7: 3F              CCF                         
4EC8: 7F              LD      A,A                 
4EC9: 29              ADD     HL,HL               
4ECA: 7F              LD      A,A                 
4ECB: 3F              CCF                         
4ECC: 7F              LD      A,A                 
4ECD: 22              LD      (HLI),A             
4ECE: 7F              LD      A,A                 
4ECF: 3F              CCF                         
4ED0: 7F              LD      A,A                 
4ED1: 25              DEC     H                   
4ED2: 7F              LD      A,A                 
4ED3: 3F              CCF                         
4ED4: 7F              LD      A,A                 
4ED5: 00              NOP                         
4ED6: 00              NOP                         
4ED7: 00              NOP                         
4ED8: 00              NOP                         
4ED9: 00              NOP                         
4EDA: 00              NOP                         
4EDB: 00              NOP                         
4EDC: 00              NOP                         
4EDD: 00              NOP                         
4EDE: 00              NOP                         
4EDF: 00              NOP                         
4EE0: 00              NOP                         
4EE1: 00              NOP                         
4EE2: 00              NOP                         
4EE3: 00              NOP                         
4EE4: 00              NOP                         
4EE5: 00              NOP                         
4EE6: 00              NOP                         
4EE7: 00              NOP                         
4EE8: 03              INC     BC                  
4EE9: 00              NOP                         
4EEA: 05              DEC     B                   
4EEB: 03              INC     BC                  
4EEC: 09              ADD     HL,BC               
4EED: 07              RLCA                        
4EEE: 10 0F           ;;STOP    $0F                 
4EF0: 10 0F           ;;STOP    $0F                 
4EF2: 10 0F           ;;STOP    $0F                 
4EF4: 0C              INC     C                   
4EF5: 03              INC     BC                  
4EF6: 03              INC     BC                  
4EF7: 00              NOP                         
4EF8: 03              INC     BC                  
4EF9: 01 03 01        LD      BC,$0103            
4EFC: 01 00 00        LD      BC,$0000            
4EFF: 00              NOP                         
4F00: 07              RLCA                        
4F01: 00              NOP                         
4F02: 38 07           JR      C,$4F0B             ; {}
4F04: 50              LD      D,B                 
4F05: 2F              CPL                         
4F06: 41              LD      B,C                 
4F07: 3E 51           LD      A,$51               
4F09: 2E 3F           LD      L,$3F               
4F0B: 10 3F           ;;STOP    $3F                 
4F0D: 15              DEC     D                   
4F0E: 5F              LD      E,A                 
4F0F: 2D              DEC     L                   
4F10: 9F              SBC     A                   
4F11: 67              LD      H,A                 
4F12: 9F              SBC     A                   
4F13: 63              LD      H,E                 
4F14: B7              OR      A                   
4F15: 48              LD      C,B                 
4F16: 7C              LD      A,H                 
4F17: 17              RLA                         
4F18: 3B              DEC     SP                  
4F19: 17              RLA                         
4F1A: 30 0F           JR      NC,$4F2B            ; {}
4F1C: 1F              RRA                         
4F1D: 0F              RRCA                        
4F1E: 1F              RRA                         
4F1F: 00              NOP                         
4F20: E0 00           LD      ($FF00+$00),A       
4F22: 1C              INC     E                   
4F23: E0 8A           LD      ($FF00+$8A),A       
4F25: 74              LD      (HL),H              
4F26: C2 BC CA        JP      NZ,$CABC            
4F29: B4              OR      H                   
4F2A: FC                              
4F2B: 88              ADC     A,B                 
4F2C: FE A8           CP      $A8                 
4F2E: F9              LD      SP,HL               
4F2F: B6              OR      (HL)                
4F30: F9              LD      SP,HL               
4F31: E6 F9           AND     $F9                 
4F33: C6 EE           ADD     $EE                 
4F35: 10 7C           ;;STOP    $7C                 
4F37: D8              RET     C                   
4F38: BC              CP      H                   
4F39: D8              RET     C                   
4F3A: 1C              INC     E                   
4F3B: E0 08           LD      ($FF00+$08),A       
4F3D: F0 F8           LD      A,($F8)             
4F3F: 00              NOP                         
4F40: 03              INC     BC                  
4F41: 00              NOP                         
4F42: 04              INC     B                   
4F43: 03              INC     BC                  
4F44: 39              ADD     HL,SP               
4F45: 07              RLCA                        
4F46: 40              LD      B,B                 
4F47: 3F              CCF                         
4F48: 40              LD      B,B                 
4F49: 3F              CCF                         
4F4A: 20 1F           JR      NZ,$4F6B            ; {}
4F4C: 30 0F           JR      NC,$4F5D            ; {}
4F4E: 20 1F           JR      NZ,$4F6F            ; {}
4F50: 10 0F           ;;STOP    $0F                 
4F52: 20 1F           JR      NZ,$4F73            ; {}
4F54: 20 1F           JR      NZ,$4F75            ; {}
4F56: 30 0F           JR      NC,$4F67            ; {}
4F58: 1C              INC     E                   
4F59: 03              INC     BC                  
4F5A: 23              INC     HL                  
4F5B: 1C              INC     E                   
4F5C: 20 1F           JR      NZ,$4F7D            ; {}
4F5E: 3F              CCF                         
4F5F: 00              NOP                         
4F60: C0              RET     NZ                  
4F61: 00              NOP                         
4F62: 20 C0           JR      NZ,$4F24            ; {}
4F64: 9C              SBC     H                   
4F65: E0 02           LD      ($FF00+$02),A       
4F67: FC                              
4F68: 02              LD      (BC),A              
4F69: FC                              
4F6A: 04              INC     B                   
4F6B: F8 0C           LD      HL,SP+$0C           
4F6D: F0 04           LD      A,($04)             
4F6F: F8 08           LD      HL,SP+$08           
4F71: F0 08           LD      A,($08)             
4F73: F0 1C           LD      A,($1C)             
4F75: E0 1C           LD      ($FF00+$1C),A       
4F77: E8 74           ADD     SP,$74              
4F79: 88              ADC     A,B                 
4F7A: 88              ADC     A,B                 
4F7B: 70              LD      (HL),B              
4F7C: 04              INC     B                   
4F7D: F8 FC           LD      HL,SP+$FC           
4F7F: 00              NOP                         
4F80: 0F              RRCA                        
4F81: 00              NOP                         
4F82: 36 0F           LD      (HL),$0F            
4F84: 60              LD      H,B                 
4F85: 3F              CCF                         
4F86: 58              LD      E,B                 
4F87: 27              DAA                         
4F88: 7C              LD      A,H                 
4F89: 0B              DEC     BC                  
4F8A: 1F              RRA                         
4F8B: 08 1F 0A        LD      ($0A1F),SP          
4F8E: 3F              CCF                         
4F8F: 1A              LD      A,(DE)              
4F90: 3F              CCF                         
4F91: 1F              RRA                         
4F92: 1E 0F           LD      E,$0F               
4F94: 0F              RRCA                        
4F95: 00              NOP                         
4F96: 07              RLCA                        
4F97: 03              INC     BC                  
4F98: 07              RLCA                        
4F99: 03              INC     BC                  
4F9A: 07              RLCA                        
4F9B: 00              NOP                         
4F9C: 08 07 0F        LD      ($0F07),SP          
4F9F: 00              NOP                         
4FA0: 80              ADD     A,B                 
4FA1: 00              NOP                         
4FA2: 60              LD      H,B                 
4FA3: 80              ADD     A,B                 
4FA4: 10 E0           ;;STOP    $E0                 
4FA6: 1C              INC     E                   
4FA7: E0 04           LD      ($FF00+$04),A       
4FA9: F8 74           LD      HL,SP+$74           
4FAB: 88              ADC     A,B                 
4FAC: 78              LD      A,B                 
4FAD: A0              AND     B                   
4FAE: D8              RET     C                   
4FAF: 60              LD      H,B                 
4FB0: A4              AND     H                   
4FB1: D8              RET     C                   
4FB2: 44              LD      B,H                 
4FB3: B8              CP      B                   
4FB4: C2 3C E2        JP      NZ,$E23C            
4FB7: 1C              INC     E                   
4FB8: BC              CP      H                   
4FB9: 40              LD      B,B                 
4FBA: 10 E0           ;;STOP    $E0                 
4FBC: 08 F0 F8        LD      ($F8F0),SP          
4FBF: 00              NOP                         
4FC0: 00              NOP                         
4FC1: 00              NOP                         
4FC2: 0F              RRCA                        
4FC3: 00              NOP                         
4FC4: 76              HALT                        
4FC5: 0F              RRCA                        
4FC6: A0              AND     B                   
4FC7: 7F              LD      A,A                 
4FC8: B8              CP      B                   
4FC9: 47              LD      B,A                 
4FCA: 7C              LD      A,H                 
4FCB: 0B              DEC     BC                  
4FCC: 1F              RRA                         
4FCD: 08 1F 0A        LD      ($0A1F),SP          
4FD0: 3F              CCF                         
4FD1: 1A              LD      A,(DE)              
4FD2: 3F              CCF                         
4FD3: 1F              RRA                         
4FD4: 1E 0F           LD      E,$0F               
4FD6: 0F              RRCA                        
4FD7: 00              NOP                         
4FD8: 07              RLCA                        
4FD9: 03              INC     BC                  
4FDA: 0F              RRCA                        
4FDB: 03              INC     BC                  
4FDC: 13              INC     DE                  
4FDD: 0C              INC     C                   
4FDE: 1F              RRA                         
4FDF: 00              NOP                         
4FE0: 00              NOP                         
4FE1: 00              NOP                         
4FE2: 80              ADD     A,B                 
4FE3: 00              NOP                         
4FE4: 60              LD      H,B                 
4FE5: 80              ADD     A,B                 
4FE6: 10 E0           ;;STOP    $E0                 
4FE8: 1C              INC     E                   
4FE9: E0 04           LD      ($FF00+$04),A       
4FEB: F8 74           LD      HL,SP+$74           
4FED: 88              ADC     A,B                 
4FEE: 78              LD      A,B                 
4FEF: A0              AND     B                   
4FF0: D4 68 A2        CALL    NC,$A268            
4FF3: DC 41 BE        CALL    C,$BE41             
4FF6: E1              POP     HL                  
4FF7: 1E 9E           LD      E,$9E               
4FF9: 60              LD      H,B                 
4FFA: 88              ADC     A,B                 
4FFB: 70              LD      (HL),B              
4FFC: 04              INC     B                   
4FFD: F8 FC           LD      HL,SP+$FC           
4FFF: 00              NOP                         
5000: 00              NOP                         
5001: 00              NOP                         
5002: 00              NOP                         
5003: 00              NOP                         
5004: 00              NOP                         
5005: 00              NOP                         
5006: 00              NOP                         
5007: 00              NOP                         
5008: 10 00           ;;STOP    $00                 
500A: 32              LD      (HLD),A             
500B: 00              NOP                         
500C: 3A              LD      A,(HLD)             
500D: 00              NOP                         
500E: 7F              LD      A,A                 
500F: 00              NOP                         
5010: 7F              LD      A,A                 
5011: 06 FF           LD      B,$FF               
5013: 02              LD      (BC),A              
5014: E7              RST     0X20                
5015: 00              NOP                         
5016: 81              ADD     A,C                 
5017: 00              NOP                         
5018: 00              NOP                         
5019: 00              NOP                         
501A: 00              NOP                         
501B: 00              NOP                         
501C: 00              NOP                         
501D: 00              NOP                         
501E: 00              NOP                         
501F: 00              NOP                         
5020: 00              NOP                         
5021: 00              NOP                         
5022: 00              NOP                         
5023: 00              NOP                         
5024: 00              NOP                         
5025: 00              NOP                         
5026: 02              LD      (BC),A              
5027: 00              NOP                         
5028: 02              LD      (BC),A              
5029: 00              NOP                         
502A: 06 00           LD      B,$00               
502C: 07              RLCA                        
502D: 00              NOP                         
502E: 0F              RRCA                        
502F: 02              LD      (BC),A              
5030: 0F              RRCA                        
5031: 02              LD      (BC),A              
5032: 0F              RRCA                        
5033: 00              NOP                         
5034: 0D              DEC     C                   
5035: 00              NOP                         
5036: 0C              INC     C                   
5037: 00              NOP                         
5038: 08 00 00        LD      ($0000),SP          
503B: 00              NOP                         
503C: 00              NOP                         
503D: 00              NOP                         
503E: 00              NOP                         
503F: 00              NOP                         
5040: 03              INC     BC                  
5041: 00              NOP                         
5042: 0E 01           LD      C,$01               
5044: 1D              DEC     E                   
5045: 03              INC     BC                  
5046: 3E 01           LD      A,$01               
5048: 3F              CCF                         
5049: 00              NOP                         
504A: 7B              LD      A,E                 
504B: 07              RLCA                        
504C: FF              RST     0X38                
504D: 4F              LD      C,A                 
504E: D7              RST     0X10                
504F: 78              LD      A,B                 
5050: AF              XOR     A                   
5051: 76              HALT                        
5052: DF              RST     0X18                
5053: 2A              LD      A,(HLI)             
5054: 7F              LD      A,A                 
5055: 0A              LD      A,(BC)              
5056: 7F              LD      A,A                 
5057: 2E 6E           LD      L,$6E               
5059: 31 6F 36        LD      SP,$366F            
505C: 7F              LD      A,A                 
505D: 06 1F           LD      B,$1F               
505F: 00              NOP                         
5060: 00              NOP                         
5061: 00              NOP                         
5062: 00              NOP                         
5063: 00              NOP                         
5064: 03              INC     BC                  
5065: 00              NOP                         
5066: 0E 01           LD      C,$01               
5068: 1D              DEC     E                   
5069: 03              INC     BC                  
506A: 3E 01           LD      A,$01               
506C: 3F              CCF                         
506D: 00              NOP                         
506E: 7B              LD      A,E                 
506F: 07              RLCA                        
5070: FF              RST     0X38                
5071: 4F              LD      C,A                 
5072: D7              RST     0X10                
5073: 78              LD      A,B                 
5074: AF              XOR     A                   
5075: 72              LD      (HL),D              
5076: 7F              LD      A,A                 
5077: 0E EE           LD      C,$EE               
5079: 71              LD      (HL),C              
507A: DF              RST     0X18                
507B: 66              LD      H,(HL)              
507C: FD                              
507D: 0E 3F           LD      C,$3F               
507F: 00              NOP                         
5080: 00              NOP                         
5081: 00              NOP                         
5082: 00              NOP                         
5083: 00              NOP                         
5084: 00              NOP                         
5085: 00              NOP                         
5086: 0E 00           LD      C,$00               
5088: 1E 04           LD      E,$04               
508A: 1D              DEC     E                   
508B: 0E 1A           LD      C,$1A               
508D: 07              RLCA                        
508E: 05              DEC     B                   
508F: 03              INC     BC                  
5090: 02              LD      (BC),A              
5091: 01 01 00        LD      BC,$0001            
5094: 00              NOP                         
5095: 00              NOP                         
5096: 00              NOP                         
5097: 00              NOP                         
5098: 00              NOP                         
5099: 00              NOP                         
509A: 00              NOP                         
509B: 00              NOP                         
509C: 00              NOP                         
509D: 00              NOP                         
509E: 00              NOP                         
509F: 00              NOP                         
50A0: 03              INC     BC                  
50A1: 00              NOP                         
50A2: 07              RLCA                        
50A3: 03              INC     BC                  
50A4: 0F              RRCA                        
50A5: 07              RLCA                        
50A6: 0F              RRCA                        
50A7: 04              INC     B                   
50A8: 7F              LD      A,A                 
50A9: 05              DEC     B                   
50AA: 7B              LD      A,E                 
50AB: 37              SCF                         
50AC: 7F              LD      A,A                 
50AD: 31 3F 1D        LD      SP,$1D3F            
50B0: 5F              LD      E,A                 
50B1: 2C              INC     L                   
50B2: 7C              LD      A,H                 
50B3: 03              INC     BC                  
50B4: 7B              LD      A,E                 
50B5: 34              INC     (HL)                
50B6: 7C              LD      A,H                 
50B7: 33              INC     SP                  
50B8: 3F              CCF                         
50B9: 00              NOP                         
50BA: 0F              RRCA                        
50BB: 06 1F           LD      B,$1F               
50BD: 0E 1F           LD      C,$1F               
50BF: 00              NOP                         
50C0: F0 00           LD      A,($00)             
50C2: F8 F0           LD      HL,SP+$F0           
50C4: 7C              LD      A,H                 
50C5: F8 3C           LD      HL,SP+$3C           
50C7: C8              RET     Z                   
50C8: FF              RST     0X38                
50C9: E8 F7           ADD     SP,$F7              
50CB: 3A              LD      A,(HLD)             
50CC: FF              RST     0X38                
50CD: E6 FE           AND     $FE                 
50CF: 2C              INC     L                   
50D0: FD                              
50D1: 0A              LD      A,(BC)              
50D2: CD 32 37        CALL    $3732               
50D5: C8              RET     Z                   
50D6: CF              RST     0X08                
50D7: 36 FF           LD      (HL),$FF            
50D9: 06 CE           LD      B,$CE               
50DB: 30 F8           JR      NC,$50D5            ; {}
50DD: 00              NOP                         
50DE: 00              NOP                         
50DF: 00              NOP                         
50E0: E7              RST     0X20                
50E1: 00              NOP                         
50E2: FF              RST     0X38                
50E3: 67              LD      H,A                 
50E4: FE 6F           CP      $6F                 
50E6: 7E              LD      A,(HL)              
50E7: 29              ADD     HL,HL               
50E8: FF              RST     0X38                
50E9: 0B              DEC     BC                  
50EA: FF              RST     0X38                
50EB: 66              LD      H,(HL)              
50EC: FF              RST     0X38                
50ED: 6B              LD      L,E                 
50EE: FF              RST     0X38                
50EF: 02              LD      (BC),A              
50F0: 27              DAA                         
50F1: 18 7F           JR      $5172               ; {}
50F3: 20 F8           JR      NZ,$50ED            ; {}
50F5: 70              LD      (HL),B              
50F6: 78              LD      A,B                 
50F7: 30 70           JR      NC,$5169            ; {}
50F9: 20 20           JR      NZ,$511B            ; {}
50FB: 00              NOP                         
50FC: 00              NOP                         
50FD: 00              NOP                         
50FE: 00              NOP                         
50FF: 00              NOP                         
5100: 06 00           LD      B,$00               
5102: 0E 04           LD      C,$04               
5104: 1E 0C           LD      E,$0C               
5106: 3B              DEC     SP                  
5107: 1C              INC     E                   
5108: 74              LD      (HL),H              
5109: 3B              DEC     SP                  
510A: E8 77           ADD     SP,$77              
510C: FA 05 1A        LD      A,($1A05)           
510F: 05              DEC     B                   
5110: 18 07           JR      $5119               ; {}
5112: FC                              
5113: 03              INC     BC                  
5114: EF              RST     0X28                
5115: 70              LD      (HL),B              
5116: 77              LD      (HL),A              
5117: 38 3B           JR      C,$5154             ; {}
5119: 1C              INC     E                   
511A: 1E 0C           LD      E,$0C               
511C: 0E 04           LD      C,$04               
511E: 06 00           LD      B,$00               
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
512A: 07              RLCA                        
512B: 00              NOP                         
512C: 08 07 11        LD      ($1107),SP          
512F: 0F              RRCA                        
5130: 23              INC     HL                  
5131: 1F              RRA                         
5132: 21 1F 20        LD      HL,$201F            
5135: 1F              RRA                         
5136: 22              LD      (HLI),A             
5137: 1D              DEC     E                   
5138: 22              LD      (HLI),A             
5139: 1D              DEC     E                   
513A: 30 0F           JR      NC,$514B            ; {}
513C: 18 07           JR      $5145               ; {}
513E: 0F              RRCA                        
513F: 00              NOP                         
5140: 03              INC     BC                  
5141: 00              NOP                         
5142: 04              INC     B                   
5143: 03              INC     BC                  
5144: 09              ADD     HL,BC               
5145: 07              RLCA                        
5146: 09              ADD     HL,BC               
5147: 07              RLCA                        
5148: 08 07 0A        LD      ($0A07),SP          
514B: 05              DEC     B                   
514C: 0A              LD      A,(BC)              
514D: 05              DEC     B                   
514E: 0A              LD      A,(BC)              
514F: 05              DEC     B                   
5150: 0A              LD      A,(BC)              
5151: 05              DEC     B                   
5152: 0A              LD      A,(BC)              
5153: 05              DEC     B                   
5154: 08 07 08        LD      ($0807),SP          
5157: 07              RLCA                        
5158: 18 07           JR      $5161               ; {}
515A: 18 07           JR      $5163               ; {}
515C: 1C              INC     E                   
515D: 03              INC     BC                  
515E: 0F              RRCA                        
515F: 00              NOP                         
5160: 00              NOP                         
5161: 00              NOP                         
5162: 00              NOP                         
5163: 00              NOP                         
5164: 00              NOP                         
5165: 00              NOP                         
5166: 00              NOP                         
5167: 00              NOP                         
5168: 00              NOP                         
5169: 00              NOP                         
516A: 00              NOP                         
516B: 00              NOP                         
516C: 00              NOP                         
516D: 00              NOP                         
516E: 00              NOP                         
516F: 00              NOP                         
5170: 00              NOP                         
5171: 00              NOP                         
5172: 38 00           JR      C,$5174             ; {}
5174: 74              LD      (HL),H              
5175: 38 A2           JR      C,$5119             ; {}
5177: 7C              LD      A,H                 
5178: CA 34 CA        JP      Z,$CA34             
517B: 34              INC     (HL)                
517C: 82              ADD     A,D                 
517D: 7C              LD      A,H                 
517E: 7C              LD      A,H                 
517F: 00              NOP                         
5180: 00              NOP                         
5181: 00              NOP                         
5182: 03              INC     BC                  
5183: 00              NOP                         
5184: 0C              INC     C                   
5185: 03              INC     BC                  
5186: 11 0F 13        LD      DE,$130F            
5189: 0F              RRCA                        
518A: 23              INC     HL                  
518B: 1D              DEC     E                   
518C: 27              DAA                         
518D: 18 27           JR      $51B6               ; {}
518F: 18 77           JR      $5208               ; {}
5191: 28 73           JR      Z,$5206             ; {}
5193: 2C              INC     L                   
5194: 5C              LD      E,H                 
5195: 33              INC     SP                  
5196: 2F              CPL                         
5197: 1C              INC     E                   
5198: 7B              LD      A,E                 
5199: 07              RLCA                        
519A: 77              LD      (HL),A              
519B: 18 3F           JR      $51DC               ; {}
519D: 10 1F           ;;STOP    $1F                 
519F: 00              NOP                         
51A0: 03              INC     BC                  
51A1: 00              NOP                         
51A2: 77              LD      (HL),A              
51A3: 70              LD      (HL),B              
51A4: 7F              LD      A,A                 
51A5: 78              LD      A,B                 
51A6: 7F              LD      A,A                 
51A7: 78              LD      A,B                 
51A8: 3F              CCF                         
51A9: 33              INC     SP                  
51AA: 7F              LD      A,A                 
51AB: 07              RLCA                        
51AC: FF              RST     0X38                
51AD: 09              ADD     HL,BC               
51AE: FF              RST     0X38                
51AF: 09              ADD     HL,BC               
51B0: FF              RST     0X38                
51B1: 0D              DEC     C                   
51B2: FF              RST     0X38                
51B3: 0F              RRCA                        
51B4: 7F              LD      A,A                 
51B5: 03              INC     BC                  
51B6: 3F              CCF                         
51B7: 32              LD      (HLD),A             
51B8: 7F              LD      A,A                 
51B9: 7A              LD      A,D                 
51BA: 7F              LD      A,A                 
51BB: 78              LD      A,B                 
51BC: 77              LD      (HL),A              
51BD: 70              LD      (HL),B              
51BE: 03              INC     BC                  
51BF: 00              NOP                         
51C0: 0F              RRCA                        
51C1: 09              ADD     HL,BC               
51C2: 3F              CCF                         
51C3: 18 7F           JR      $5244               ; {}
51C5: 03              INC     BC                  
51C6: 7F              LD      A,A                 
51C7: 4F              LD      C,A                 
51C8: FF              RST     0X38                
51C9: D3                              
51CA: FF              RST     0X38                
51CB: 19              ADD     HL,DE               
51CC: FF              RST     0X38                
51CD: 3D              DEC     A                   
51CE: FF              RST     0X38                
51CF: AF              XOR     A                   
51D0: FF              RST     0X38                
51D1: A7              AND     A                   
51D2: FF              RST     0X38                
51D3: 39              ADD     HL,SP               
51D4: FF              RST     0X38                
51D5: 1C              INC     E                   
51D6: FF              RST     0X38                
51D7: DE 7F           SBC     $7F                 
51D9: 4F              LD      C,A                 
51DA: 7F              LD      A,A                 
51DB: 03              INC     BC                  
51DC: 3F              CCF                         
51DD: 18 0F           JR      $51EE               ; {}
51DF: 09              ADD     HL,BC               
51E0: 1F              RRA                         
51E1: 00              NOP                         
51E2: 3F              CCF                         
51E3: 1F              RRA                         
51E4: 5F              LD      E,A                 
51E5: 3F              CCF                         
51E6: 9F              SBC     A                   
51E7: 60              LD      H,B                 
51E8: A0              AND     B                   
51E9: 5F              LD      E,A                 
51EA: C0              RET     NZ                  
51EB: 3F              CCF                         
51EC: 9B              SBC     E                   
51ED: 64              LD      H,H                 
51EE: 9F              SBC     A                   
51EF: 78              LD      A,B                 
51F0: 87              ADD     A,A                 
51F1: 78              LD      A,B                 
51F2: B7              OR      A                   
51F3: 48              LD      C,B                 
51F4: B7              OR      A                   
51F5: 78              LD      A,B                 
51F6: 87              ADD     A,A                 
51F7: 7C              LD      A,H                 
51F8: BB              CP      E                   
51F9: 46              LD      B,(HL)              
51FA: B9              CP      C                   
51FB: 7F              LD      A,A                 
51FC: 80              ADD     A,B                 
51FD: 7F              LD      A,A                 
51FE: FF              RST     0X38                
51FF: 00              NOP                         
5200: 30 00           JR      NC,$5202            ; {}
5202: 3F              CCF                         
5203: 10 3B           ;;STOP    $3B                 
5205: 17              RLA                         
5206: 15              DEC     D                   
5207: 0B              DEC     BC                  
5208: 17              RLA                         
5209: 08 77 0A        LD      ($0A77),SP          
520C: F3              DI                          
520D: 6C              LD      L,H                 
520E: D1              POP     DE                  
520F: 6E              LD      L,(HL)              
5210: 91              SUB     C                   
5211: 6E              LD      L,(HL)              
5212: F9              LD      SP,HL               
5213: 06 9F           LD      B,$9F               
5215: 60              LD      H,B                 
5216: FF              RST     0X38                
5217: 03              INC     BC                  
5218: EC                              
5219: 73              LD      (HL),E              
521A: FF              RST     0X38                
521B: 70              LD      (HL),B              
521C: FF              RST     0X38                
521D: 70              LD      (HL),B              
521E: 7F              LD      A,A                 
521F: 00              NOP                         
5220: 0E 00           LD      C,$00               
5222: FE 0C           CP      $0C                 
5224: BC              CP      H                   
5225: D8              RET     C                   
5226: 78              LD      A,B                 
5227: 90              SUB     B                   
5228: DE 20           SBC     $20                 
522A: CF              RST     0X08                
522B: B6              OR      (HL)                
522C: 8B              ADC     A,E                 
522D: 76              HALT                        
522E: 09              ADD     HL,BC               
522F: F6 0F           OR      $0F                 
5231: F0 39           LD      A,($39)             
5233: C6 F9           ADD     $F9                 
5235: 06 9F           LD      B,$9F               
5237: E0 37           LD      ($FF00+$37),A       
5239: CE FF           ADC     $FF                 
523B: 0E FF           LD      C,$FF               
523D: 6E              LD      L,(HL)              
523E: FE 00           CP      $00                 
5240: 03              INC     BC                  
5241: 00              NOP                         
5242: 07              RLCA                        
5243: 03              INC     BC                  
5244: 09              ADD     HL,BC               
5245: 07              RLCA                        
5246: 1C              INC     E                   
5247: 03              INC     BC                  
5248: 3C              INC     A                   
5249: 0B              DEC     BC                  
524A: 3C              INC     A                   
524B: 1B              DEC     DE                  
524C: 7C              LD      A,H                 
524D: 1B              DEC     DE                  
524E: FD                              
524F: 52              LD      D,D                 
5250: BE              CP      (HL)                
5251: 41              LD      B,C                 
5252: BB              CP      E                   
5253: 5E              LD      E,(HL)              
5254: 7B              LD      A,E                 
5255: 1F              RRA                         
5256: 3B              DEC     SP                  
5257: 1F              RRA                         
5258: 39              ADD     HL,SP               
5259: 1F              RRA                         
525A: 6C              LD      L,H                 
525B: 1F              RRA                         
525C: 77              LD      (HL),A              
525D: 0F              RRCA                        
525E: 3F              CCF                         
525F: 00              NOP                         
5260: C0              RET     NZ                  
5261: 00              NOP                         
5262: A0              AND     B                   
5263: C0              RET     NZ                  
5264: D8              RET     C                   
5265: E0 DC           LD      ($FF00+$DC),A       
5267: E8 1E           ADD     SP,$1E              
5269: EC                              
526A: 1E EC           LD      E,$EC               
526C: 1E E4           LD      E,$E4               
526E: DF              RST     0X18                
526F: 20 3F           JR      NZ,$52B0            ; {}
5271: CA ED 3A        JP      Z,$3AED             
5274: FD                              
5275: FA FE F8        LD      A,($F8FE)           
5278: FE F8           CP      $F8                 
527A: 7E              LD      A,(HL)              
527B: F8 FE           LD      HL,SP+$FE           
527D: F0 FC           LD      A,($FC)             
527F: 00              NOP                         
5280: 00              NOP                         
5281: 00              NOP                         
5282: 1F              RRA                         
5283: 00              NOP                         
5284: 3F              CCF                         
5285: 1E 6D           LD      E,$6D               
5287: 32              LD      (HLD),A             
5288: 5D              LD      E,L                 
5289: 22              LD      (HLI),A             
528A: 78              LD      A,B                 
528B: 17              RLA                         
528C: 70              LD      (HL),B              
528D: 0F              RRCA                        
528E: 47              LD      B,A                 
528F: 38 4F           JR      C,$52E0             ; {}
5291: 37              SCF                         
5292: CC 37 BC        CALL    Z,$BC37             
5295: 43              LD      B,E                 
5296: FB              EI                          
5297: 34              INC     (HL)                
5298: 78              LD      A,B                 
5299: 37              SCF                         
529A: 7F              LD      A,A                 
529B: 00              NOP                         
529C: FF              RST     0X38                
529D: 1F              RRA                         
529E: FF              RST     0X38                
529F: 00              NOP                         
52A0: FC                              
52A1: 00              NOP                         
52A2: FC                              
52A3: F8 B8           LD      HL,SP+$B8           
52A5: C0              RET     NZ                  
52A6: F0 E0           LD      A,($E0)             
52A8: E0 00           LD      ($FF00+$00),A       
52AA: 20 C0           JR      NZ,$526C            ; {}
52AC: 70              LD      (HL),B              
52AD: A0              AND     B                   
52AE: F0 60           LD      A,($60)             
52B0: F0 60           LD      A,($60)             
52B2: 78              LD      A,B                 
52B3: B0              OR      B                   
52B4: 78              LD      A,B                 
52B5: B0              OR      B                   
52B6: FC                              
52B7: 18 FC           JR      $52B5               ; {}
52B9: 18 FC           JR      $52B7               ; {}
52BB: 08 FC 80        LD      ($80FC),SP          
52BE: F0 00           LD      A,($00)             
52C0: 00              NOP                         
52C1: 00              NOP                         
52C2: 00              NOP                         
52C3: 00              NOP                         
52C4: 1F              RRA                         
52C5: 00              NOP                         
52C6: 3F              CCF                         
52C7: 1E 6D           LD      E,$6D               
52C9: 32              LD      (HLD),A             
52CA: 5D              LD      E,L                 
52CB: 22              LD      (HLI),A             
52CC: 78              LD      A,B                 
52CD: 17              RLA                         
52CE: 70              LD      (HL),B              
52CF: 0F              RRCA                        
52D0: 47              LD      B,A                 
52D1: 38 4F           JR      C,$5322             ; {}
52D3: 37              SCF                         
52D4: FC                              
52D5: 07              RLCA                        
52D6: FC                              
52D7: 33              INC     SP                  
52D8: FB              EI                          
52D9: 34              INC     (HL)                
52DA: 78              LD      A,B                 
52DB: 07              RLCA                        
52DC: FF              RST     0X38                
52DD: 70              LD      (HL),B              
52DE: FF              RST     0X38                
52DF: 00              NOP                         
52E0: 00              NOP                         
52E1: 00              NOP                         
52E2: FC                              
52E3: 00              NOP                         
52E4: FC                              
52E5: F8 B8           LD      HL,SP+$B8           
52E7: C0              RET     NZ                  
52E8: F0 E0           LD      A,($E0)             
52EA: E0 00           LD      ($FF00+$00),A       
52EC: 20 C0           JR      NZ,$52AE            ; {}
52EE: 70              LD      (HL),B              
52EF: A0              AND     B                   
52F0: F0 60           LD      A,($60)             
52F2: FF              RST     0X38                
52F3: 70              LD      (HL),B              
52F4: 7F              LD      A,A                 
52F5: BE              CP      (HL)                
52F6: 7F              LD      A,A                 
52F7: 9E              SBC     (HL)                
52F8: FF              RST     0X38                
52F9: 0E FF           LD      C,$FF               
52FB: 20 F8           JR      NZ,$52F5            ; {}
52FD: E0 F0           LD      ($FF00+$F0),A       
52FF: 00              NOP                         
5300: 70              LD      (HL),B              
5301: 00              NOP                         
5302: F8 70           LD      HL,SP+$70           
5304: FC                              
5305: 58              LD      E,B                 
5306: DE 6C           SBC     $6C                 
5308: CE 74           ADC     $74                 
530A: CF              RST     0X08                
530B: 76              HALT                        
530C: 67              LD      H,A                 
530D: 3B              DEC     SP                  
530E: 67              LD      H,A                 
530F: 3B              DEC     SP                  
5310: 37              SCF                         
5311: 1F              RRA                         
5312: 1F              RRA                         
5313: 0D              DEC     C                   
5314: FF              RST     0X38                
5315: 0D              DEC     C                   
5316: 2F              CPL                         
5317: 15              DEC     D                   
5318: FF              RST     0X38                
5319: 0F              RRCA                        
531A: 27              DAA                         
531B: 1F              RRA                         
531C: 43              LD      B,E                 
531D: 3C              INC     A                   
531E: 7C              LD      A,H                 
531F: 00              NOP                         
5320: 00              NOP                         
5321: 00              NOP                         
5322: 00              NOP                         
5323: 00              NOP                         
5324: 00              NOP                         
5325: 00              NOP                         
5326: 00              NOP                         
5327: 00              NOP                         
5328: 00              NOP                         
5329: 00              NOP                         
532A: 3C              INC     A                   
532B: 00              NOP                         
532C: 7E              LD      A,(HL)              
532D: 3C              INC     A                   
532E: FF              RST     0X38                
532F: 7E              LD      A,(HL)              
5330: 7F              LD      A,A                 
5331: 03              INC     BC                  
5332: 23              INC     HL                  
5333: 1D              DEC     E                   
5334: 17              RLA                         
5335: 0F              RRCA                        
5336: 1F              RRA                         
5337: 0F              RRCA                        
5338: 7F              LD      A,A                 
5339: 0B              DEC     BC                  
533A: AF              XOR     A                   
533B: 1D              DEC     E                   
533C: 47              LD      B,A                 
533D: 3F              CCF                         
533E: 7F              LD      A,A                 
533F: 00              NOP                         
5340: 0F              RRCA                        
5341: 00              NOP                         
5342: 73              LD      (HL),E              
5343: 0F              RRCA                        
5344: F7              RST     0X30                
5345: 6F              LD      L,A                 
5346: 9F              SBC     A                   
5347: 64              LD      H,H                 
5348: FF              RST     0X38                
5349: 60              LD      H,B                 
534A: 9F              SBC     A                   
534B: 6F              LD      L,A                 
534C: F3              DI                          
534D: 6F              LD      L,A                 
534E: 96              SUB     (HL)                
534F: 6F              LD      L,A                 
5350: BB              CP      E                   
5351: 77              LD      (HL),A              
5352: 57              LD      D,A                 
5353: 38 20           JR      C,$5375             ; {}
5355: 1F              RRA                         
5356: 7F              LD      A,A                 
5357: 3F              CCF                         
5358: 43              LD      B,E                 
5359: 3C              INC     A                   
535A: FF              RST     0X38                
535B: 78              LD      A,B                 
535C: FF              RST     0X38                
535D: 00              NOP                         
535E: 7F              LD      A,A                 
535F: 00              NOP                         
5360: E0 00           LD      ($FF00+$00),A       
5362: 90              SUB     B                   
5363: E0 E8           LD      ($FF00+$E8),A       
5365: F0 EC           LD      A,($EC)             
5367: B0              OR      B                   
5368: EE 34           XOR     $34                 
536A: 0F              RRCA                        
536B: F6 EB           OR      $EB                 
536D: F6 7D           OR      $7D                 
536F: 8E              ADC     A,(HL)              
5370: ED                              
5371: 7E              LD      A,(HL)              
5372: EA 7C 7E        LD      ($7E7C),A           ; {}
5375: 80              ADD     A,B                 
5376: 82              ADD     A,D                 
5377: FC                              
5378: BE              CP      (HL)                
5379: 7C              LD      A,H                 
537A: C3 3C FF        JP      $FF3C               
537D: 3E FF           LD      A,$FF               
537F: 00              NOP                         
5380: 00              NOP                         
5381: FF              RST     0X38                
5382: 00              NOP                         
5383: FF              RST     0X38                
5384: 22              LD      (HLI),A             
5385: DD                              
5386: 14              INC     D                   
5387: EB                              
5388: 08 F7 14        LD      ($14F7),SP          
538B: EB                              
538C: 22              LD      (HLI),A             
538D: DD                              
538E: 00              NOP                         
538F: FF              RST     0X38                
5390: 00              NOP                         
5391: FF              RST     0X38                
5392: 00              NOP                         
5393: FF              RST     0X38                
5394: 22              LD      (HLI),A             
5395: DD                              
5396: 14              INC     D                   
5397: EB                              
5398: 08 F7 14        LD      ($14F7),SP          
539B: EB                              
539C: 22              LD      (HLI),A             
539D: DD                              
539E: 00              NOP                         
539F: FF              RST     0X38                
53A0: 00              NOP                         
53A1: FF              RST     0X38                
53A2: 00              NOP                         
53A3: FF              RST     0X38                
53A4: 22              LD      (HLI),A             
53A5: DD                              
53A6: 14              INC     D                   
53A7: EB                              
53A8: 08 F7 14        LD      ($14F7),SP          
53AB: EB                              
53AC: 22              LD      (HLI),A             
53AD: DD                              
53AE: 00              NOP                         
53AF: FF              RST     0X38                
53B0: 00              NOP                         
53B1: FF              RST     0X38                
53B2: 00              NOP                         
53B3: FF              RST     0X38                
53B4: 22              LD      (HLI),A             
53B5: DD                              
53B6: 14              INC     D                   
53B7: EB                              
53B8: 08 F7 14        LD      ($14F7),SP          
53BB: EB                              
53BC: 22              LD      (HLI),A             
53BD: DD                              
53BE: 00              NOP                         
53BF: FF              RST     0X38                
53C0: 00              NOP                         
53C1: 00              NOP                         
53C2: 0F              RRCA                        
53C3: 00              NOP                         
53C4: 3F              CCF                         
53C5: 0F              RRCA                        
53C6: 5B              LD      E,E                 
53C7: 3C              INC     A                   
53C8: BF              CP      A                   
53C9: 78              LD      A,B                 
53CA: BB              CP      E                   
53CB: 7C              LD      A,H                 
53CC: 9F              SBC     A                   
53CD: 7F              LD      A,A                 
53CE: 8B              ADC     A,E                 
53CF: 77              LD      (HL),A              
53D0: C8              RET     Z                   
53D1: 37              SCF                         
53D2: FC                              
53D3: 43              LD      B,E                 
53D4: F7              RST     0X30                
53D5: 78              LD      A,B                 
53D6: BF              CP      A                   
53D7: 7F              LD      A,A                 
53D8: 8B              ADC     A,E                 
53D9: 77              LD      (HL),A              
53DA: C8              RET     Z                   
53DB: 37              SCF                         
53DC: 7C              LD      A,H                 
53DD: 03              INC     BC                  
53DE: 1F              RRA                         
53DF: 00              NOP                         
53E0: 07              RLCA                        
53E1: 00              NOP                         
53E2: 1F              RRA                         
53E3: 07              RLCA                        
53E4: 2D              DEC     L                   
53E5: 1E 3D           LD      E,$3D               
53E7: 1E 5F           LD      E,$5F               
53E9: 3F              CCF                         
53EA: 4F              LD      C,A                 
53EB: 3F              CCF                         
53EC: 45              LD      B,L                 
53ED: 3B              DEC     SP                  
53EE: 44              LD      B,H                 
53EF: 3B              DEC     SP                  
53F0: 64              LD      H,H                 
53F1: 1B              DEC     DE                  
53F2: 7E              LD      A,(HL)              
53F3: 21 7B 3C        LD      HL,$3C7B            
53F6: 5F              LD      E,A                 
53F7: 3F              CCF                         
53F8: 45              LD      B,L                 
53F9: 3B              DEC     SP                  
53FA: 64              LD      H,H                 
53FB: 1B              DEC     DE                  
53FC: 3E 01           LD      A,$01               
53FE: 0F              RRCA                        
53FF: 00              NOP                         
5400: 3F              CCF                         
5401: 00              NOP                         
5402: 7F              LD      A,A                 
5403: 3F              CCF                         
5404: 7F              LD      A,A                 
5405: 1F              RRA                         
5406: 3E 0F           LD      A,$0F               
5408: 1F              RRA                         
5409: 07              RLCA                        
540A: 3F              CCF                         
540B: 0B              DEC     BC                  
540C: 3F              CCF                         
540D: 09              ADD     HL,BC               
540E: 3F              CCF                         
540F: 0D              DEC     C                   
5410: 2F              CPL                         
5411: 13              INC     DE                  
5412: 2F              CPL                         
5413: 17              RLA                         
5414: 68              LD      L,B                 
5415: 17              RLA                         
5416: D8              RET     C                   
5417: 67              LD      H,A                 
5418: F8 77           LD      HL,SP+$77           
541A: FF              RST     0X38                
541B: 00              NOP                         
541C: 00              NOP                         
541D: 00              NOP                         
541E: 00              NOP                         
541F: 00              NOP                         
5420: FC                              
5421: 00              NOP                         
5422: FE FC           CP      $FC                 
5424: FE FC           CP      $FC                 
5426: 4E              LD      C,(HL)              
5427: FC                              
5428: 1C              INC     E                   
5429: F8 9C           LD      HL,SP+$9C           
542B: F8 FC           LD      HL,SP+$FC           
542D: F0 FC           LD      A,($FC)             
542F: F0 FC           LD      A,($FC)             
5431: F8 FE           LD      HL,SP+$FE           
5433: F8 F7           LD      HL,SP+$F7           
5435: FA 77 FA        LD      A,($FA77)           
5438: 3F              CCF                         
5439: F0 F8           LD      A,($F8)             
543B: 00              NOP                         
543C: 00              NOP                         
543D: 00              NOP                         
543E: 00              NOP                         
543F: 00              NOP                         
5440: 00              NOP                         
5441: 00              NOP                         
5442: 01 00 07        LD      BC,$0700            
5445: 01 1F 07        LD      BC,$071F            
5448: 3F              CCF                         
5449: 1F              RRA                         
544A: 7F              LD      A,A                 
544B: 20 FF           JR      NZ,$544C            ; {}
544D: 40              LD      B,B                 
544E: F8 47           LD      HL,SP+$47           
5450: F0 0F           LD      A,($0F)             
5452: 23              INC     HL                  
5453: 1D              DEC     E                   
5454: 63              LD      H,E                 
5455: 1D              DEC     E                   
5456: A1              AND     C                   
5457: 5E              LD      E,(HL)              
5458: E0 5F           LD      ($FF00+$5F),A       
545A: F0 6F           LD      A,($6F)             
545C: FC                              
545D: 03              INC     BC                  
545E: 0F              RRCA                        
545F: 00              NOP                         
5460: 00              NOP                         
5461: 00              NOP                         
5462: C0              RET     NZ                  
5463: 00              NOP                         
5464: E0 C0           LD      ($FF00+$C0),A       
5466: F0 E0           LD      A,($E0)             
5468: F8 F0           LD      HL,SP+$F0           
546A: FC                              
546B: 08 FE 04        LD      ($04FE),SP          
546E: 1E E4           LD      E,$E4               
5470: 0E F0           LD      C,$F0               
5472: 84              ADD     A,H                 
5473: 78              LD      A,B                 
5474: 84              ADD     A,H                 
5475: 78              LD      A,B                 
5476: 06 F8           LD      B,$F8               
5478: 0D              DEC     C                   
5479: F2                              
547A: 1B              DEC     DE                  
547B: E6 7F           AND     $7F                 
547D: 8E              ADC     A,(HL)              
547E: FF              RST     0X38                
547F: 00              NOP                         
5480: 00              NOP                         
5481: 00              NOP                         
5482: 00              NOP                         
5483: 00              NOP                         
5484: 01 00 06        LD      BC,$0600            
5487: 01 18 07        LD      BC,$0718            
548A: 7F              LD      A,A                 
548B: 1F              RRA                         
548C: FF              RST     0X38                
548D: 7F              LD      A,A                 
548E: 41              LD      B,C                 
548F: 3F              CCF                         
5490: 20 1F           JR      NZ,$54B1            ; {}
5492: 10 0F           ;;STOP    $0F                 
5494: 10 0F           ;;STOP    $0F                 
5496: 10 0F           ;;STOP    $0F                 
5498: 31 0E 7F        LD      SP,$7F0E            
549B: 01 3F 00        LD      BC,$003F            
549E: 00              NOP                         
549F: 00              NOP                         
54A0: 1F              RRA                         
54A1: 00              NOP                         
54A2: 7F              LD      A,A                 
54A3: 1E FF           LD      E,$FF               
54A5: 7E              LD      A,(HL)              
54A6: 3E FC           LD      A,$FC               
54A8: 3C              INC     A                   
54A9: E0 FA           LD      ($FF00+$FA),A       
54AB: D4 F9 96        CALL    NC,$96F9            
54AE: F9              LD      SP,HL               
54AF: B6              OR      (HL)                
54B0: F1              POP     AF                  
54B1: 8E              ADC     A,(HL)              
54B2: 41              LD      B,C                 
54B3: BE              CP      (HL)                
54B4: 42              LD      B,D                 
54B5: BC              CP      H                   
54B6: FC                              
54B7: 00              NOP                         
54B8: FE F8           CP      $F8                 
54BA: C7              RST     0X00                
54BB: F8 FE           LD      HL,SP+$FE           
54BD: 00              NOP                         
54BE: 00              NOP                         
54BF: 00              NOP                         
54C0: 00              NOP                         
54C1: 00              NOP                         
54C2: 00              NOP                         
54C3: 00              NOP                         
54C4: 00              NOP                         
54C5: 00              NOP                         
54C6: 03              INC     BC                  
54C7: 00              NOP                         
54C8: 0C              INC     C                   
54C9: 03              INC     BC                  
54CA: 3F              CCF                         
54CB: 0F              RRCA                        
54CC: 7F              LD      A,A                 
54CD: 3F              CCF                         
54CE: 23              INC     HL                  
54CF: 1F              RRA                         
54D0: 11 0F 08        LD      DE,$080F            
54D3: 07              RLCA                        
54D4: 08 07 0F        LD      ($0F07),SP          
54D7: 00              NOP                         
54D8: 3F              CCF                         
54D9: 07              RLCA                        
54DA: 7E              LD      A,(HL)              
54DB: 0F              RRCA                        
54DC: 3F              CCF                         
54DD: 00              NOP                         
54DE: 00              NOP                         
54DF: 00              NOP                         
54E0: 0F              RRCA                        
54E1: 00              NOP                         
54E2: 3F              CCF                         
54E3: 0E FF           LD      C,$FF               
54E5: 3C              INC     A                   
54E6: 7E              LD      A,(HL)              
54E7: F0 7C           LD      A,($7C)             
54E9: C0              RET     NZ                  
54EA: F2                              
54EB: AC              XOR     H                   
54EC: F1              POP     AF                  
54ED: 2E F1           LD      L,$F1               
54EF: 6E              LD      L,(HL)              
54F0: E1              POP     HL                  
54F1: 1E 81           LD      E,$81               
54F3: 7E              LD      A,(HL)              
54F4: 82              ADD     A,D                 
54F5: 7C              LD      A,H                 
54F6: C6 38           ADD     $38                 
54F8: FA C4 23        LD      A,($23C4)           
54FB: DC FE 00        CALL    C,$00FE             
54FE: 00              NOP                         
54FF: 00              NOP                         
5500: 01 00 03        LD      BC,$0300            
5503: 01 05 03        LD      BC,$0305            
5506: 1F              RRA                         
5507: 00              NOP                         
5508: 20 1F           JR      NZ,$5529            ; {}
550A: 40              LD      B,B                 
550B: 3F              CCF                         
550C: E7              RST     0X20                
550D: 18 FF           JR      $550E               ; {}
550F: 62              LD      H,D                 
5510: FF              RST     0X38                
5511: 72              LD      (HL),D              
5512: BF              CP      A                   
5513: 70              LD      (HL),B              
5514: 5F              LD      E,A                 
5515: 38 3F           JR      C,$5556             ; {}
5517: 1F              RRA                         
5518: 3C              INC     A                   
5519: 1F              RRA                         
551A: 7E              LD      A,(HL)              
551B: 3F              CCF                         
551C: FF              RST     0X38                
551D: 7F              LD      A,A                 
551E: FF              RST     0X38                
551F: 00              NOP                         
5520: 01 00 03        LD      BC,$0300            
5523: 01 05 03        LD      BC,$0305            
5526: 1D              DEC     E                   
5527: 03              INC     BC                  
5528: 25              DEC     H                   
5529: 1B              DEC     DE                  
552A: 45              LD      B,L                 
552B: 3B              DEC     SP                  
552C: 45              LD      B,L                 
552D: 3B              DEC     SP                  
552E: C3 3C E0        JP      $E03C               
5531: 5F              LD      E,A                 
5532: F0 6F           LD      A,($6F)             
5534: 7F              LD      A,A                 
5535: 30 38           JR      NC,$556F            ; {}
5537: 1F              RRA                         
5538: 3F              CCF                         
5539: 1F              RRA                         
553A: 7F              LD      A,A                 
553B: 3F              CCF                         
553C: FF              RST     0X38                
553D: 7F              LD      A,A                 
553E: FF              RST     0X38                
553F: 00              NOP                         
5540: 0F              RRCA                        
5541: 00              NOP                         
5542: 10 0F           ;;STOP    $0F                 
5544: 20 1F           JR      NZ,$5565            ; {}
5546: 20 1F           JR      NZ,$5567            ; {}
5548: 37              SCF                         
5549: 08 7F 30        LD      ($307F),SP          
554C: 7F              LD      A,A                 
554D: 35              DEC     (HL)                
554E: 5F              LD      E,A                 
554F: 35              DEC     (HL)                
5550: 3F              CCF                         
5551: 10 3F           ;;STOP    $3F                 
5553: 18 2F           JR      $5584               ; {}
5555: 1F              RRA                         
5556: 18 0F           JR      $5567               ; {}
5558: 1D              DEC     E                   
5559: 0F              RRCA                        
555A: 1F              RRA                         
555B: 0F              RRCA                        
555C: 3F              CCF                         
555D: 1F              RRA                         
555E: 3F              CCF                         
555F: 00              NOP                         
5560: 00              NOP                         
5561: 00              NOP                         
5562: FC                              
5563: 00              NOP                         
5564: 7E              LD      A,(HL)              
5565: BC              CP      H                   
5566: 22              LD      (HLI),A             
5567: DC 1E E0        CALL    C,$E01E             
556A: 9F              SBC     A                   
556B: 6E              LD      L,(HL)              
556C: FF              RST     0X38                
556D: 1E FD           LD      E,$FD               
556F: 3E FA           LD      A,$FA               
5571: 7C              LD      A,H                 
5572: F4                              
5573: F8 F4           LD      HL,SP+$F4           
5575: F8 F4           LD      HL,SP+$F4           
5577: F8 F4           LD      HL,SP+$F4           
5579: F8 FE           LD      HL,SP+$FE           
557B: FC                              
557C: FF              RST     0X38                
557D: FE FF           CP      $FF                 
557F: 00              NOP                         
5580: 00              NOP                         
5581: 00              NOP                         
5582: 00              NOP                         
5583: 00              NOP                         
5584: 03              INC     BC                  
5585: 00              NOP                         
5586: 07              RLCA                        
5587: 03              INC     BC                  
5588: 0E 07           LD      C,$07               
558A: 1F              RRA                         
558B: 0F              RRCA                        
558C: 1C              INC     E                   
558D: 0F              RRCA                        
558E: 3F              CCF                         
558F: 1F              RRA                         
5590: 3F              CCF                         
5591: 1F              RRA                         
5592: 1C              INC     E                   
5593: 0F              RRCA                        
5594: 1F              RRA                         
5595: 0F              RRCA                        
5596: 0E 07           LD      C,$07               
5598: 07              RLCA                        
5599: 03              INC     BC                  
559A: 03              INC     BC                  
559B: 00              NOP                         
559C: 00              NOP                         
559D: 00              NOP                         
559E: 00              NOP                         
559F: 00              NOP                         
55A0: 00              NOP                         
55A1: 00              NOP                         
55A2: 00              NOP                         
55A3: 00              NOP                         
55A4: FC                              
55A5: 00              NOP                         
55A6: F0 E0           LD      A,($E0)             
55A8: 60              LD      H,B                 
55A9: 80              ADD     A,B                 
55AA: F8 C0           LD      HL,SP+$C0           
55AC: C0              RET     NZ                  
55AD: 00              NOP                         
55AE: F8 C0           LD      HL,SP+$C0           
55B0: F8 C0           LD      HL,SP+$C0           
55B2: C0              RET     NZ                  
55B3: 00              NOP                         
55B4: F8 C0           LD      HL,SP+$C0           
55B6: 60              LD      H,B                 
55B7: 80              ADD     A,B                 
55B8: F0 E0           LD      A,($E0)             
55BA: FC                              
55BB: 00              NOP                         
55BC: 00              NOP                         
55BD: 00              NOP                         
55BE: 00              NOP                         
55BF: 00              NOP                         
55C0: 00              NOP                         
55C1: 00              NOP                         
55C2: 00              NOP                         
55C3: 00              NOP                         
55C4: 20 00           JR      NZ,$55C6            ; {}
55C6: 25              DEC     H                   
55C7: 00              NOP                         
55C8: 35              DEC     (HL)                
55C9: 00              NOP                         
55CA: 3D              DEC     A                   
55CB: 10 3F           ;;STOP    $3F                 
55CD: 15              DEC     D                   
55CE: 37              SCF                         
55CF: 1D              DEC     E                   
55D0: 35              DEC     (HL)                
55D1: 1F              RRA                         
55D2: 3D              DEC     A                   
55D3: 1F              RRA                         
55D4: 1F              RRA                         
55D5: 0F              RRCA                        
55D6: 0F              RRCA                        
55D7: 07              RLCA                        
55D8: 07              RLCA                        
55D9: 01 01 00        LD      BC,$0001            
55DC: 00              NOP                         
55DD: 00              NOP                         
55DE: 00              NOP                         
55DF: 00              NOP                         
55E0: 00              NOP                         
55E1: 00              NOP                         
55E2: 00              NOP                         
55E3: 00              NOP                         
55E4: 00              NOP                         
55E5: 00              NOP                         
55E6: 00              NOP                         
55E7: 00              NOP                         
55E8: 00              NOP                         
55E9: 00              NOP                         
55EA: 00              NOP                         
55EB: 00              NOP                         
55EC: 01 00 03        LD      BC,$0300            
55EF: 01 05 03        LD      BC,$0305            
55F2: 1D              DEC     E                   
55F3: 03              INC     BC                  
55F4: 25              DEC     H                   
55F5: 1B              DEC     DE                  
55F6: 45              LD      B,L                 
55F7: 3B              DEC     SP                  
55F8: 43              LD      B,E                 
55F9: 3C              INC     A                   
55FA: 40              LD      B,B                 
55FB: 3F              CCF                         
55FC: 20 1F           JR      NZ,$561D            ; {}
55FE: 1F              RRA                         
55FF: 00              NOP                         
5600: 03              INC     BC                  
5601: 00              NOP                         
5602: 05              DEC     B                   
5603: 03              INC     BC                  
5604: 69              LD      L,C                 
5605: 07              RLCA                        
5606: 98              SBC     B                   
5607: 67              LD      H,A                 
5608: 88              ADC     A,B                 
5609: 77              LD      (HL),A              
560A: E2              LD      (C),A               
560B: 1D              DEC     E                   
560C: F2                              
560D: 6D              LD      L,L                 
560E: FA 75 78        LD      A,($7875)           ; {}
5611: 37              SCF                         
5612: 39              ADD     HL,SP               
5613: 16 11           LD      D,$11               
5615: 0E 11           LD      C,$11               
5617: 0E 1C           LD      C,$1C               
5619: 03              INC     BC                  
561A: 1F              RRA                         
561B: 0C              INC     C                   
561C: 3F              CCF                         
561D: 1E 3F           LD      E,$3F               
561F: 00              NOP                         
5620: C0              RET     NZ                  
5621: 00              NOP                         
5622: A0              AND     B                   
5623: C0              RET     NZ                  
5624: 90              SUB     B                   
5625: E0 10           LD      ($FF00+$10),A       
5627: E0 10           LD      ($FF00+$10),A       
5629: E0 4C           LD      ($FF00+$4C),A       
562B: B0              OR      B                   
562C: 42              LD      B,D                 
562D: BC              CP      H                   
562E: 41              LD      B,C                 
562F: BE              CP      (HL)                
5630: 1D              DEC     E                   
5631: E2              LD      (C),A               
5632: 9F              SBC     A                   
5633: 6C              LD      L,H                 
5634: 8F              ADC     A,A                 
5635: 76              HALT                        
5636: 8E              ADC     A,(HL)              
5637: 70              LD      (HL),B              
5638: 18 E0           JR      $561A               ; {}
563A: F8 00           LD      HL,SP+$00           
563C: F0 00           LD      A,($00)             
563E: 00              NOP                         
563F: 00              NOP                         
5640: 03              INC     BC                  
5641: 00              NOP                         
5642: 05              DEC     B                   
5643: 03              INC     BC                  
5644: 69              LD      L,C                 
5645: 07              RLCA                        
5646: 98              SBC     B                   
5647: 67              LD      H,A                 
5648: 88              ADC     A,B                 
5649: 77              LD      (HL),A              
564A: 80              ADD     A,B                 
564B: 7F              LD      A,A                 
564C: 80              ADD     A,B                 
564D: 7F              LD      A,A                 
564E: 80              ADD     A,B                 
564F: 7F              LD      A,A                 
5650: 48              LD      C,B                 
5651: 37              SCF                         
5652: 30 0F           JR      NC,$5663            ; {}
5654: 10 0F           ;;STOP    $0F                 
5656: 10 0F           ;;STOP    $0F                 
5658: 1C              INC     E                   
5659: 03              INC     BC                  
565A: 1F              RRA                         
565B: 0C              INC     C                   
565C: 3F              CCF                         
565D: 1E 3F           LD      E,$3F               
565F: 00              NOP                         
5660: C0              RET     NZ                  
5661: 00              NOP                         
5662: A0              AND     B                   
5663: C0              RET     NZ                  
5664: 90              SUB     B                   
5665: E0 10           LD      ($FF00+$10),A       
5667: E0 10           LD      ($FF00+$10),A       
5669: E0 0C           LD      ($FF00+$0C),A       
566B: F0 02           LD      A,($02)             
566D: FC                              
566E: 01 FE 01        LD      BC,$01FE            
5671: FE 11           CP      $11                 
5673: EE 09           XOR     $09                 
5675: F6 0E           OR      $0E                 
5677: F0 18           LD      A,($18)             
5679: E0 F8           LD      ($FF00+$F8),A       
567B: 00              NOP                         
567C: F0 00           LD      A,($00)             
567E: 00              NOP                         
567F: 00              NOP                         
5680: 03              INC     BC                  
5681: 00              NOP                         
5682: 05              DEC     B                   
5683: 03              INC     BC                  
5684: 09              ADD     HL,BC               
5685: 07              RLCA                        
5686: 08 07 08        LD      ($0807),SP          
5689: 07              RLCA                        
568A: 0A              LD      A,(BC)              
568B: 05              DEC     B                   
568C: 12              LD      (DE),A              
568D: 0D              DEC     C                   
568E: 22              LD      (HLI),A             
568F: 1D              DEC     E                   
5690: 28 17           JR      Z,$56A9             ; {}
5692: 2C              INC     L                   
5693: 13              INC     DE                  
5694: 2C              INC     L                   
5695: 13              INC     DE                  
5696: 2C              INC     L                   
5697: 13              INC     DE                  
5698: 10 0F           ;;STOP    $0F                 
569A: 0F              RRCA                        
569B: 00              NOP                         
569C: 0F              RRCA                        
569D: 07              RLCA                        
569E: 1F              RRA                         
569F: 00              NOP                         
56A0: C0              RET     NZ                  
56A1: 00              NOP                         
56A2: A0              AND     B                   
56A3: C0              RET     NZ                  
56A4: 90              SUB     B                   
56A5: E0 08           LD      ($FF00+$08),A       
56A7: F0 08           LD      A,($08)             
56A9: F0 38           LD      A,($38)             
56AB: C0              RET     NZ                  
56AC: 0C              INC     C                   
56AD: F0 02           LD      A,($02)             
56AF: FC                              
56B0: 41              LD      B,C                 
56B1: BE              CP      (HL)                
56B2: 21 DE 1F        LD      HL,$1FDE            
56B5: E0 08           LD      ($FF00+$08),A       
56B7: F0 10           LD      A,($10)             
56B9: E0 E0           LD      ($FF00+$E0),A       
56BB: 00              NOP                         
56BC: E0 C0           LD      ($FF00+$C0),A       
56BE: E0 00           LD      ($FF00+$00),A       
56C0: 00              NOP                         
56C1: 00              NOP                         
56C2: 03              INC     BC                  
56C3: 00              NOP                         
56C4: 05              DEC     B                   
56C5: 03              INC     BC                  
56C6: 09              ADD     HL,BC               
56C7: 07              RLCA                        
56C8: 08 07 08        LD      ($0807),SP          
56CB: 07              RLCA                        
56CC: 0A              LD      A,(BC)              
56CD: 05              DEC     B                   
56CE: 12              LD      (DE),A              
56CF: 0D              DEC     C                   
56D0: 22              LD      (HLI),A             
56D1: 1D              DEC     E                   
56D2: 28 17           JR      Z,$56EB             ; {}
56D4: 2C              INC     L                   
56D5: 13              INC     DE                  
56D6: 2C              INC     L                   
56D7: 13              INC     DE                  
56D8: 2C              INC     L                   
56D9: 13              INC     DE                  
56DA: 38 07           JR      C,$56E3             ; {}
56DC: 7F              LD      A,A                 
56DD: 38 7F           JR      C,$575E             ; {}
56DF: 00              NOP                         
56E0: 00              NOP                         
56E1: 00              NOP                         
56E2: C0              RET     NZ                  
56E3: 00              NOP                         
56E4: A0              AND     B                   
56E5: C0              RET     NZ                  
56E6: 9E              SBC     (HL)                
56E7: E0 11           LD      ($FF00+$11),A       
56E9: EE 27           XOR     $27                 
56EB: D8              RET     C                   
56EC: 4F              LD      C,A                 
56ED: B6              OR      (HL)                
56EE: 1F              RRA                         
56EF: EE 3E           XOR     $3E                 
56F1: DC 7C B8        CALL    C,$B87C             
56F4: 3C              INC     A                   
56F5: C0              RET     NZ                  
56F6: 04              INC     B                   
56F7: F8 0C           LD      HL,SP+$0C           
56F9: F0 3E           LD      A,($3E)             
56FB: C4 FE 3C        CALL    NZ,$3CFE            
56FE: FC                              
56FF: 00              NOP                         
5700: 07              RLCA                        
5701: 00              NOP                         
5702: 1F              RRA                         
5703: 07              RLCA                        
5704: FF              RST     0X38                
5705: 1F              RRA                         
5706: FF              RST     0X38                
5707: 7F              LD      A,A                 
5708: FF              RST     0X38                
5709: 6F              LD      L,A                 
570A: 7F              LD      A,A                 
570B: 30 FF           JR      NC,$570C            ; {}
570D: 76              HALT                        
570E: FF              RST     0X38                
570F: 76              HALT                        
5710: FF              RST     0X38                
5711: 7F              LD      A,A                 
5712: FF              RST     0X38                
5713: 6F              LD      L,A                 
5714: FF              RST     0X38                
5715: 70              LD      (HL),B              
5716: 7F              LD      A,A                 
5717: 3F              CCF                         
5718: 78              LD      A,B                 
5719: 3F              CCF                         
571A: 3F              CCF                         
571B: 1F              RRA                         
571C: 1F              RRA                         
571D: 07              RLCA                        
571E: 07              RLCA                        
571F: 00              NOP                         
5720: 80              ADD     A,B                 
5721: 00              NOP                         
5722: E0 80           LD      ($FF00+$80),A       
5724: FE E0           CP      $E0                 
5726: FE FC           CP      $FC                 
5728: FE 7C           CP      $7C                 
572A: FC                              
572B: F8 FC           LD      HL,SP+$FC           
572D: F0 FC           LD      A,($FC)             
572F: F8 FC           LD      HL,SP+$FC           
5731: F8 FC           LD      HL,SP+$FC           
5733: B8              CP      B                   
5734: FE 78           CP      $78                 
5736: FF              RST     0X38                
5737: F6 F9           OR      $F9                 
5739: FE E2           CP      $E2                 
573B: FC                              
573C: 9C              SBC     H                   
573D: E0 E0           LD      ($FF00+$E0),A       
573F: 00              NOP                         
5740: 07              RLCA                        
5741: 00              NOP                         
5742: 1F              RRA                         
5743: 07              RLCA                        
5744: FF              RST     0X38                
5745: 1F              RRA                         
5746: FF              RST     0X38                
5747: 6F              LD      L,A                 
5748: FF              RST     0X38                
5749: 76              HALT                        
574A: 7F              LD      A,A                 
574B: 36 FF           LD      (HL),$FF            
574D: 70              LD      (HL),B              
574E: FF              RST     0X38                
574F: 76              HALT                        
5750: FF              RST     0X38                
5751: 5F              LD      E,A                 
5752: FF              RST     0X38                
5753: 40              LD      B,B                 
5754: FF              RST     0X38                
5755: 49              LD      C,C                 
5756: 7F              LD      A,A                 
5757: 20 7F           JR      NZ,$57D8            ; {}
5759: 30 3F           JR      NC,$579A            ; {}
575B: 1F              RRA                         
575C: 1F              RRA                         
575D: 07              RLCA                        
575E: 07              RLCA                        
575F: 00              NOP                         
5760: 80              ADD     A,B                 
5761: 00              NOP                         
5762: E0 80           LD      ($FF00+$80),A       
5764: FE E0           CP      $E0                 
5766: FE 7C           CP      $7C                 
5768: FE FC           CP      $FC                 
576A: FC                              
576B: F8 FC           LD      HL,SP+$FC           
576D: F0 FC           LD      A,($FC)             
576F: F8 FF           LD      HL,SP+$FF           
5771: D8              RET     C                   
5772: FF              RST     0X38                
5773: 1A              LD      A,(DE)              
5774: FF              RST     0X38                
5775: 9A              SBC     D                   
5776: FD                              
5777: 36 FA           LD      (HL),$FA            
5779: 7C              LD      A,H                 
577A: E4                              
577B: F8 98           LD      HL,SP+$98           
577D: E0 E0           LD      ($FF00+$E0),A       
577F: 00              NOP                         
5780: 06 02           LD      B,$02               
5782: 46              LD      B,(HL)              
5783: 02              LD      (BC),A              
5784: 60              LD      H,B                 
5785: 00              NOP                         
5786: 63              LD      H,E                 
5787: 40              LD      B,B                 
5788: 2F              CPL                         
5789: 20 1F           JR      NZ,$57AA            ; {}
578B: 00              NOP                         
578C: 1F              RRA                         
578D: 00              NOP                         
578E: 3F              CCF                         
578F: 02              LD      (BC),A              
5790: 3F              CCF                         
5791: 02              LD      (BC),A              
5792: 7F              LD      A,A                 
5793: 06 7F           LD      B,$7F               
5795: 00              NOP                         
5796: 7F              LD      A,A                 
5797: 00              NOP                         
5798: 1C              INC     E                   
5799: 03              INC     BC                  
579A: 1F              RRA                         
579B: 00              NOP                         
579C: 0F              RRCA                        
579D: 00              NOP                         
579E: 03              INC     BC                  
579F: 00              NOP                         
57A0: 00              NOP                         
57A1: 00              NOP                         
57A2: 00              NOP                         
57A3: 00              NOP                         
57A4: 00              NOP                         
57A5: 00              NOP                         
57A6: 03              INC     BC                  
57A7: 00              NOP                         
57A8: 7F              LD      A,A                 
57A9: 00              NOP                         
57AA: FF              RST     0X38                
57AB: 02              LD      (BC),A              
57AC: FF              RST     0X38                
57AD: 02              LD      (BC),A              
57AE: 7F              LD      A,A                 
57AF: 06 3F           LD      B,$3F               
57B1: 00              NOP                         
57B2: 3F              CCF                         
57B3: 00              NOP                         
57B4: 3F              CCF                         
57B5: 03              INC     BC                  
57B6: 3F              CCF                         
57B7: 07              RLCA                        
57B8: 1F              RRA                         
57B9: 00              NOP                         
57BA: 1F              RRA                         
57BB: 00              NOP                         
57BC: 0F              RRCA                        
57BD: 00              NOP                         
57BE: 03              INC     BC                  
57BF: 00              NOP                         
57C0: 07              RLCA                        
57C1: 00              NOP                         
57C2: 1F              RRA                         
57C3: 07              RLCA                        
57C4: FF              RST     0X38                
57C5: 1F              RRA                         
57C6: FF              RST     0X38                
57C7: 7F              LD      A,A                 
57C8: FF              RST     0X38                
57C9: 76              HALT                        
57CA: 7F              LD      A,A                 
57CB: 36 FF           LD      (HL),$FF            
57CD: 7F              LD      A,A                 
57CE: FF              RST     0X38                
57CF: 7F              LD      A,A                 
57D0: FF              RST     0X38                
57D1: 7F              LD      A,A                 
57D2: FF              RST     0X38                
57D3: 4F              LD      C,A                 
57D4: FF              RST     0X38                
57D5: 76              HALT                        
57D6: 7F              LD      A,A                 
57D7: 39              ADD     HL,SP               
57D8: 7F              LD      A,A                 
57D9: 3F              CCF                         
57DA: 39              ADD     HL,SP               
57DB: 1F              RRA                         
57DC: 1F              RRA                         
57DD: 07              RLCA                        
57DE: 07              RLCA                        
57DF: 00              NOP                         
57E0: 80              ADD     A,B                 
57E1: 00              NOP                         
57E2: E0 80           LD      ($FF00+$80),A       
57E4: FE E0           CP      $E0                 
57E6: FE FC           CP      $FC                 
57E8: FE FC           CP      $FC                 
57EA: FC                              
57EB: F8 FC           LD      HL,SP+$FC           
57ED: F0 FC           LD      A,($FC)             
57EF: F8 FC           LD      HL,SP+$FC           
57F1: F8 FC           LD      HL,SP+$FC           
57F3: 18 FE           JR      $57F3               ; {}
57F5: F8 FF           LD      HL,SP+$FF           
57F7: F6 F9           OR      $F9                 
57F9: FE E2           CP      $E2                 
57FB: FC                              
57FC: 9C              SBC     H                   
57FD: E0 E0           LD      ($FF00+$E0),A       
57FF: 00              NOP                         
5800: 00              NOP                         
5801: 00              NOP                         
5802: 03              INC     BC                  
5803: 00              NOP                         
5804: 0C              INC     C                   
5805: 03              INC     BC                  
5806: 13              INC     DE                  
5807: 0C              INC     C                   
5808: 2F              CPL                         
5809: 10 2F           ;;STOP    $2F                 
580B: 10 5E           ;;STOP    $5E                 
580D: 21 5D 23        LD      HL,$235D            
5810: 5D              LD      E,L                 
5811: 23              INC     HL                  
5812: 5E              LD      E,(HL)              
5813: 21 2F 10        LD      HL,$102F            
5816: 3F              CCF                         
5817: 0E 3F           LD      C,$3F               
5819: 19              ADD     HL,DE               
581A: 3F              CCF                         
581B: 19              ADD     HL,DE               
581C: 1F              RRA                         
581D: 0E 0E           LD      C,$0E               
581F: 00              NOP                         
5820: 00              NOP                         
5821: 00              NOP                         
5822: 03              INC     BC                  
5823: 00              NOP                         
5824: 3C              INC     A                   
5825: 03              INC     BC                  
5826: 7B              LD      A,E                 
5827: 34              INC     (HL)                
5828: FF              RST     0X38                
5829: 78              LD      A,B                 
582A: FF              RST     0X38                
582B: 48              LD      C,B                 
582C: FE 49           CP      $49                 
582E: 7D              LD      A,L                 
582F: 33              INC     SP                  
5830: 7D              LD      A,L                 
5831: 33              INC     SP                  
5832: FE 49           CP      $49                 
5834: FF              RST     0X38                
5835: 48              LD      C,B                 
5836: FF              RST     0X38                
5837: 78              LD      A,B                 
5838: 7B              LD      A,E                 
5839: 34              INC     (HL)                
583A: 3C              INC     A                   
583B: 03              INC     BC                  
583C: 03              INC     BC                  
583D: 00              NOP                         
583E: 00              NOP                         
583F: 00              NOP                         
5840: 00              NOP                         
5841: 00              NOP                         
5842: C0              RET     NZ                  
5843: 00              NOP                         
5844: 30 C0           JR      NC,$5806            ; {}
5846: C8              RET     Z                   
5847: 30 F4           JR      NC,$583D            ; {}
5849: 08 F4 08        LD      ($08F4),SP          
584C: 7A              LD      A,D                 
584D: 84              ADD     A,H                 
584E: BA              CP      D                   
584F: C4 BA C4        CALL    NZ,$C4BA            
5852: 7A              LD      A,D                 
5853: 84              ADD     A,H                 
5854: F4                              
5855: 08 F4 08        LD      ($08F4),SP          
5858: C8              RET     Z                   
5859: 30 30           JR      NC,$588B            ; {}
585B: C0              RET     NZ                  
585C: C0              RET     NZ                  
585D: 00              NOP                         
585E: 00              NOP                         
585F: 00              NOP                         
5860: 00              NOP                         
5861: 00              NOP                         
5862: 03              INC     BC                  
5863: 00              NOP                         
5864: 0C              INC     C                   
5865: 03              INC     BC                  
5866: 13              INC     DE                  
5867: 0C              INC     C                   
5868: 2F              CPL                         
5869: 10 2F           ;;STOP    $2F                 
586B: 10 7E           ;;STOP    $7E                 
586D: 01 7D 33        LD      BC,$337D            
5870: FD                              
5871: 7B              LD      A,E                 
5872: FE 49           CP      $49                 
5874: FF              RST     0X38                
5875: 48              LD      C,B                 
5876: 7F              LD      A,A                 
5877: 3F              CCF                         
5878: 3F              CCF                         
5879: 09              ADD     HL,BC               
587A: 1F              RRA                         
587B: 09              ADD     HL,BC               
587C: 0F              RRCA                        
587D: 07              RLCA                        
587E: 07              RLCA                        
587F: 00              NOP                         
5880: 00              NOP                         
5881: 00              NOP                         
5882: C0              RET     NZ                  
5883: 00              NOP                         
5884: 30 C0           JR      NC,$5846            ; {}
5886: C8              RET     Z                   
5887: 30 F4           JR      NC,$587D            ; {}
5889: 08 F4 08        LD      ($08F4),SP          
588C: 7A              LD      A,D                 
588D: 84              ADD     A,H                 
588E: BA              CP      D                   
588F: C4 BA C4        CALL    NZ,$C4BA            
5892: 7A              LD      A,D                 
5893: 84              ADD     A,H                 
5894: F4                              
5895: 08 F4 08        LD      ($08F4),SP          
5898: C8              RET     Z                   
5899: B0              OR      B                   
589A: F0 80           LD      A,($80)             
589C: C0              RET     NZ                  
589D: 00              NOP                         
589E: 00              NOP                         
589F: 00              NOP                         
58A0: 00              NOP                         
58A1: 00              NOP                         
58A2: 00              NOP                         
58A3: 00              NOP                         
58A4: 00              NOP                         
58A5: 00              NOP                         
58A6: 03              INC     BC                  
58A7: 00              NOP                         
58A8: 04              INC     B                   
58A9: 03              INC     BC                  
58AA: 0B              DEC     BC                  
58AB: 04              INC     B                   
58AC: 16 09           LD      D,$09               
58AE: 16 09           LD      D,$09               
58B0: 17              RLA                         
58B1: 08 17 08        LD      ($0817),SP          
58B4: 0B              DEC     BC                  
58B5: 04              INC     B                   
58B6: 04              INC     B                   
58B7: 03              INC     BC                  
58B8: 03              INC     BC                  
58B9: 00              NOP                         
58BA: 00              NOP                         
58BB: 00              NOP                         
58BC: 00              NOP                         
58BD: 00              NOP                         
58BE: 00              NOP                         
58BF: 00              NOP                         
58C0: 00              NOP                         
58C1: 00              NOP                         
58C2: 00              NOP                         
58C3: 00              NOP                         
58C4: 00              NOP                         
58C5: 00              NOP                         
58C6: 00              NOP                         
58C7: 00              NOP                         
58C8: 03              INC     BC                  
58C9: 00              NOP                         
58CA: 04              INC     B                   
58CB: 03              INC     BC                  
58CC: 0B              DEC     BC                  
58CD: 04              INC     B                   
58CE: 0A              LD      A,(BC)              
58CF: 05              DEC     B                   
58D0: 0B              DEC     BC                  
58D1: 04              INC     B                   
58D2: 0B              DEC     BC                  
58D3: 04              INC     B                   
58D4: 04              INC     B                   
58D5: 03              INC     BC                  
58D6: 03              INC     BC                  
58D7: 00              NOP                         
58D8: 00              NOP                         
58D9: 00              NOP                         
58DA: 00              NOP                         
58DB: 00              NOP                         
58DC: 00              NOP                         
58DD: 00              NOP                         
58DE: 00              NOP                         
58DF: 00              NOP                         
58E0: 00              NOP                         
58E1: FF              RST     0X38                
58E2: 00              NOP                         
58E3: FF              RST     0X38                
58E4: 22              LD      (HLI),A             
58E5: DD                              
58E6: 14              INC     D                   
58E7: EB                              
58E8: 08 F7 14        LD      ($14F7),SP          
58EB: EB                              
58EC: 22              LD      (HLI),A             
58ED: DD                              
58EE: 00              NOP                         
58EF: FF              RST     0X38                
58F0: 00              NOP                         
58F1: FF              RST     0X38                
58F2: 00              NOP                         
58F3: FF              RST     0X38                
58F4: 22              LD      (HLI),A             
58F5: DD                              
58F6: 14              INC     D                   
58F7: EB                              
58F8: 08 F7 14        LD      ($14F7),SP          
58FB: EB                              
58FC: 22              LD      (HLI),A             
58FD: DD                              
58FE: 00              NOP                         
58FF: FF              RST     0X38                
5900: 00              NOP                         
5901: 00              NOP                         
5902: 00              NOP                         
5903: 00              NOP                         
5904: 03              INC     BC                  
5905: 00              NOP                         
5906: 0F              RRCA                        
5907: 00              NOP                         
5908: 1E 01           LD      E,$01               
590A: 1E 01           LD      E,$01               
590C: 1F              RRA                         
590D: 00              NOP                         
590E: 3F              CCF                         
590F: 00              NOP                         
5910: 5F              LD      E,A                 
5911: 23              INC     HL                  
5912: 5F              LD      E,A                 
5913: 27              DAA                         
5914: 5F              LD      E,A                 
5915: 26 5B           LD      H,$5B               
5917: 26 4D           LD      H,$4D               
5919: 33              INC     SP                  
591A: 67              LD      H,A                 
591B: 18 33           JR      $5950               ; {}
591D: 0F              RRCA                        
591E: 1F              RRA                         
591F: 00              NOP                         
5920: 07              RLCA                        
5921: 00              NOP                         
5922: 0B              DEC     BC                  
5923: 06 0B           LD      B,$0B               
5925: 07              RLCA                        
5926: 1B              DEC     DE                  
5927: 04              INC     B                   
5928: 1E 01           LD      E,$01               
592A: 1E 01           LD      E,$01               
592C: 1F              RRA                         
592D: 00              NOP                         
592E: 3F              CCF                         
592F: 00              NOP                         
5930: 5F              LD      E,A                 
5931: 20 5F           JR      NZ,$5992            ; {}
5933: 20 5F           JR      NZ,$5994            ; {}
5935: 20 5F           JR      NZ,$5996            ; {}
5937: 20 4F           JR      NZ,$5988            ; {}
5939: 30 67           JR      NC,$59A2            ; {}
593B: 18 33           JR      $5970               ; {}
593D: 0F              RRCA                        
593E: 1F              RRA                         
593F: 00              NOP                         
5940: 00              NOP                         
5941: 00              NOP                         
5942: 00              NOP                         
5943: 00              NOP                         
5944: 03              INC     BC                  
5945: 00              NOP                         
5946: 3F              CCF                         
5947: 00              NOP                         
5948: 7E              LD      A,(HL)              
5949: 39              ADD     HL,SP               
594A: FE 19           CP      $19                 
594C: FF              RST     0X38                
594D: 18 FB           JR      $594A               ; {}
594F: 3C              INC     A                   
5950: B3              OR      E                   
5951: 7C              LD      A,H                 
5952: 47              LD      B,A                 
5953: 38 7F           JR      C,$59D4             ; {}
5955: 00              NOP                         
5956: 5F              LD      E,A                 
5957: 20 4F           JR      NZ,$59A8            ; {}
5959: 30 67           JR      NC,$59C2            ; {}
595B: 18 33           JR      $5990               ; {}
595D: 0F              RRCA                        
595E: 1F              RRA                         
595F: 00              NOP                         
5960: 00              NOP                         
5961: 00              NOP                         
5962: 00              NOP                         
5963: 00              NOP                         
5964: C0              RET     NZ                  
5965: 00              NOP                         
5966: F0 00           LD      A,($00)             
5968: 78              LD      A,B                 
5969: 80              ADD     A,B                 
596A: 78              LD      A,B                 
596B: 80              ADD     A,B                 
596C: F8 00           LD      HL,SP+$00           
596E: FC                              
596F: 00              NOP                         
5970: FA 04 FA        LD      A,($FA04)           
5973: 04              INC     B                   
5974: FA 04 FA        LD      A,($FA04)           
5977: 04              INC     B                   
5978: F2                              
5979: 0C              INC     C                   
597A: E6 18           AND     $18                 
597C: CC F0 F8        CALL    Z,$F8F0             
597F: 00              NOP                         
5980: 00              NOP                         
5981: 00              NOP                         
5982: 00              NOP                         
5983: 00              NOP                         
5984: 03              INC     BC                  
5985: 00              NOP                         
5986: 0F              RRCA                        
5987: 00              NOP                         
5988: 1E 01           LD      E,$01               
598A: 1E 01           LD      E,$01               
598C: 1F              RRA                         
598D: 00              NOP                         
598E: 3F              CCF                         
598F: 0E 7F           LD      C,$7F               
5991: 1F              RRA                         
5992: 7F              LD      A,A                 
5993: 13              INC     DE                  
5994: 7F              LD      A,A                 
5995: 13              INC     DE                  
5996: 6E              LD      L,(HL)              
5997: 1F              RRA                         
5998: 50              LD      D,B                 
5999: 2F              CPL                         
599A: 6F              LD      L,A                 
599B: 10 33           ;;STOP    $33                 
599D: 0F              RRCA                        
599E: 1F              RRA                         
599F: 00              NOP                         
59A0: 00              NOP                         
59A1: 00              NOP                         
59A2: 00              NOP                         
59A3: 00              NOP                         
59A4: C0              RET     NZ                  
59A5: 00              NOP                         
59A6: F0 00           LD      A,($00)             
59A8: 78              LD      A,B                 
59A9: 80              ADD     A,B                 
59AA: 78              LD      A,B                 
59AB: 80              ADD     A,B                 
59AC: F8 00           LD      HL,SP+$00           
59AE: FC                              
59AF: 00              NOP                         
59B0: FA 04 7A        LD      A,($7A04)           ; {}
59B3: 84              ADD     A,H                 
59B4: 7A              LD      A,D                 
59B5: 84              ADD     A,H                 
59B6: 7A              LD      A,D                 
59B7: 84              ADD     A,H                 
59B8: F2                              
59B9: 0C              INC     C                   
59BA: E6 18           AND     $18                 
59BC: CC F0 F8        CALL    Z,$F8F0             
59BF: 00              NOP                         
59C0: 0E 00           LD      C,$00               
59C2: 1D              DEC     E                   
59C3: 0E 3F           LD      C,$3F               
59C5: 0C              INC     C                   
59C6: 7F              LD      A,A                 
59C7: 38 7E           JR      C,$5A47             ; {}
59C9: 31 4E 31        LD      SP,$314E            
59CC: 4F              LD      C,A                 
59CD: 30 3F           JR      NC,$5A0E            ; {}
59CF: 00              NOP                         
59D0: 5F              LD      E,A                 
59D1: 20 5F           JR      NZ,$5A32            ; {}
59D3: 20 5F           JR      NZ,$5A34            ; {}
59D5: 20 5F           JR      NZ,$5A36            ; {}
59D7: 20 4F           JR      NZ,$5A28            ; {}
59D9: 30 67           JR      NC,$5A42            ; {}
59DB: 18 33           JR      $5A10               ; {}
59DD: 0F              RRCA                        
59DE: 1F              RRA                         
59DF: 00              NOP                         
59E0: 00              NOP                         
59E1: 00              NOP                         
59E2: 00              NOP                         
59E3: 00              NOP                         
59E4: C0              RET     NZ                  
59E5: 00              NOP                         
59E6: F0 00           LD      A,($00)             
59E8: 78              LD      A,B                 
59E9: 80              ADD     A,B                 
59EA: 78              LD      A,B                 
59EB: 80              ADD     A,B                 
59EC: F8 00           LD      HL,SP+$00           
59EE: FC                              
59EF: 00              NOP                         
59F0: FA 04 FA        LD      A,($FA04)           
59F3: 04              INC     B                   
59F4: FA 04 FA        LD      A,($FA04)           
59F7: 04              INC     B                   
59F8: F2                              
59F9: 0C              INC     C                   
59FA: E6 18           AND     $18                 
59FC: CC F0 F8        CALL    Z,$F8F0             
59FF: 00              NOP                         
5A00: 07              RLCA                        
5A01: 00              NOP                         
5A02: 3B              DEC     SP                  
5A03: 07              RLCA                        
5A04: 7B              LD      A,E                 
5A05: 37              SCF                         
5A06: 78              LD      A,B                 
5A07: 37              SCF                         
5A08: 7F              LD      A,A                 
5A09: 30 7F           JR      NC,$5A8A            ; {}
5A0B: 04              INC     B                   
5A0C: 4F              LD      C,A                 
5A0D: 30 48           JR      NC,$5A57            ; {}
5A0F: 37              SCF                         
5A10: 78              LD      A,B                 
5A11: 07              RLCA                        
5A12: 48              LD      C,B                 
5A13: 37              SCF                         
5A14: 37              SCF                         
5A15: 08 20 1F        LD      ($1F20),SP          
5A18: 23              INC     HL                  
5A19: 1C              INC     E                   
5A1A: 3C              INC     A                   
5A1B: 03              INC     BC                  
5A1C: 1F              RRA                         
5A1D: 00              NOP                         
5A1E: 07              RLCA                        
5A1F: 00              NOP                         
5A20: C0              RET     NZ                  
5A21: 00              NOP                         
5A22: 20 C0           JR      NZ,$59E4            ; {}
5A24: 10 E0           ;;STOP    $E0                 
5A26: 10 E0           ;;STOP    $E0                 
5A28: DC 20 FE        CALL    C,$FE20             
5A2B: 8C              ADC     A,H                 
5A2C: F2                              
5A2D: 0C              INC     C                   
5A2E: 52              LD      D,D                 
5A2F: AC              XOR     H                   
5A30: 3E C0           LD      A,$C0               
5A32: 7E              LD      A,(HL)              
5A33: BC              CP      H                   
5A34: FF              RST     0X38                
5A35: 66              LD      H,(HL)              
5A36: FF              RST     0X38                
5A37: 42              LD      B,D                 
5A38: FF              RST     0X38                
5A39: 42              LD      B,D                 
5A3A: FF              RST     0X38                
5A3B: 66              LD      H,(HL)              
5A3C: FE 3C           CP      $3C                 
5A3E: FC                              
5A3F: 00              NOP                         
5A40: 67              LD      H,A                 
5A41: 00              NOP                         
5A42: F9              LD      SP,HL               
5A43: 67              LD      H,A                 
5A44: F1              POP     AF                  
5A45: 6F              LD      L,A                 
5A46: F0 6F           LD      A,($6F)             
5A48: F7              RST     0X30                
5A49: 08 9F 62        LD      ($629F),SP          ; {}
5A4C: 9F              SBC     A                   
5A4D: 60              LD      H,B                 
5A4E: F4                              
5A4F: 0B              DEC     BC                  
5A50: 90              SUB     B                   
5A51: 6F              LD      L,A                 
5A52: 78              LD      A,B                 
5A53: 07              RLCA                        
5A54: 27              DAA                         
5A55: 18 20           JR      $5A77               ; {}
5A57: 1F              RRA                         
5A58: 23              INC     HL                  
5A59: 1C              INC     E                   
5A5A: 3E 01           LD      A,$01               
5A5C: 3F              CCF                         
5A5D: 1E 1F           LD      E,$1F               
5A5F: 00              NOP                         
5A60: E0 00           LD      ($FF00+$00),A       
5A62: 90              SUB     B                   
5A63: E0 88           LD      ($FF00+$88),A       
5A65: F0 08           LD      A,($08)             
5A67: F0 E8           LD      A,($E8)             
5A69: 10 FE           ;;STOP    $FE                 
5A6B: 40              LD      B,B                 
5A6C: FF              RST     0X38                
5A6D: 06 3D           LD      B,$3D               
5A6F: C2 7F BC        JP      NZ,$BC7F            
5A72: FF              RST     0X38                
5A73: 66              LD      H,(HL)              
5A74: FF              RST     0X38                
5A75: 42              LD      B,D                 
5A76: FF              RST     0X38                
5A77: 42              LD      B,D                 
5A78: FF              RST     0X38                
5A79: 66              LD      H,(HL)              
5A7A: FE 3C           CP      $3C                 
5A7C: FE 00           CP      $00                 
5A7E: FC                              
5A7F: 00              NOP                         
5A80: 01 01 03        LD      BC,$0301            
5A83: 02              LD      (BC),A              
5A84: 3F              CCF                         
5A85: 3D              DEC     A                   
5A86: 3F              CCF                         
5A87: 21 3F 28        LD      HL,$283F            
5A8A: 3F              CCF                         
5A8B: 26 7B           LD      H,$7B               
5A8D: 46              LD      B,(HL)              
5A8E: FF              RST     0X38                
5A8F: B0              OR      B                   
5A90: CF              RST     0X08                
5A91: B0              OR      B                   
5A92: 7F              LD      A,A                 
5A93: 46              LD      B,(HL)              
5A94: 3D              DEC     A                   
5A95: 26 3F           LD      H,$3F               
5A97: 28 3E           JR      Z,$5AD7             ; {}
5A99: 21 3E 3D        LD      HL,$3D3E            
5A9C: 03              INC     BC                  
5A9D: 02              LD      (BC),A              
5A9E: 01 01 00        LD      BC,$0001            
5AA1: FF              RST     0X38                
5AA2: 00              NOP                         
5AA3: FF              RST     0X38                
5AA4: 22              LD      (HLI),A             
5AA5: DD                              
5AA6: 14              INC     D                   
5AA7: EB                              
5AA8: 08 F7 14        LD      ($14F7),SP          
5AAB: EB                              
5AAC: 22              LD      (HLI),A             
5AAD: DD                              
5AAE: 00              NOP                         
5AAF: FF              RST     0X38                
5AB0: 00              NOP                         
5AB1: FF              RST     0X38                
5AB2: 00              NOP                         
5AB3: FF              RST     0X38                
5AB4: 22              LD      (HLI),A             
5AB5: DD                              
5AB6: 14              INC     D                   
5AB7: EB                              
5AB8: 08 F7 14        LD      ($14F7),SP          
5ABB: EB                              
5ABC: 22              LD      (HLI),A             
5ABD: DD                              
5ABE: 00              NOP                         
5ABF: FF              RST     0X38                
5AC0: 00              NOP                         
5AC1: FF              RST     0X38                
5AC2: 00              NOP                         
5AC3: FF              RST     0X38                
5AC4: 22              LD      (HLI),A             
5AC5: DD                              
5AC6: 14              INC     D                   
5AC7: EB                              
5AC8: 08 F7 14        LD      ($14F7),SP          
5ACB: EB                              
5ACC: 22              LD      (HLI),A             
5ACD: DD                              
5ACE: 00              NOP                         
5ACF: FF              RST     0X38                
5AD0: 00              NOP                         
5AD1: FF              RST     0X38                
5AD2: 00              NOP                         
5AD3: FF              RST     0X38                
5AD4: 22              LD      (HLI),A             
5AD5: DD                              
5AD6: 14              INC     D                   
5AD7: EB                              
5AD8: 08 F7 14        LD      ($14F7),SP          
5ADB: EB                              
5ADC: 22              LD      (HLI),A             
5ADD: DD                              
5ADE: 00              NOP                         
5ADF: FF              RST     0X38                
5AE0: 00              NOP                         
5AE1: FF              RST     0X38                
5AE2: 00              NOP                         
5AE3: FF              RST     0X38                
5AE4: 22              LD      (HLI),A             
5AE5: DD                              
5AE6: 14              INC     D                   
5AE7: EB                              
5AE8: 08 F7 14        LD      ($14F7),SP          
5AEB: EB                              
5AEC: 22              LD      (HLI),A             
5AED: DD                              
5AEE: 00              NOP                         
5AEF: FF              RST     0X38                
5AF0: 00              NOP                         
5AF1: FF              RST     0X38                
5AF2: 00              NOP                         
5AF3: FF              RST     0X38                
5AF4: 22              LD      (HLI),A             
5AF5: DD                              
5AF6: 14              INC     D                   
5AF7: EB                              
5AF8: 08 F7 14        LD      ($14F7),SP          
5AFB: EB                              
5AFC: 22              LD      (HLI),A             
5AFD: DD                              
5AFE: 00              NOP                         
5AFF: FF              RST     0X38                
5B00: 18 00           JR      $5B02               ; {}
5B02: 1C              INC     E                   
5B03: 08 1E 0C        LD      ($0C1E),SP          
5B06: 1B              DEC     DE                  
5B07: 0C              INC     C                   
5B08: D6 09           SUB     $09                 
5B0A: FF              RST     0X38                
5B0B: 40              LD      B,B                 
5B0C: FF              RST     0X38                
5B0D: 60              LD      H,B                 
5B0E: 7F              LD      A,A                 
5B0F: 30 5F           JR      NC,$5B70            ; {}
5B11: 38 27           JR      C,$5B3A             ; {}
5B13: 18 5F           JR      $5B74               ; {}
5B15: 20 47           JR      NZ,$5B5E            ; {}
5B17: 38 63           JR      C,$5B7C             ; {}
5B19: 1F              RRA                         
5B1A: 78              LD      A,B                 
5B1B: 27              DAA                         
5B1C: 7F              LD      A,A                 
5B1D: 38 3F           JR      C,$5B5E             ; {}
5B1F: 00              NOP                         
5B20: 00              NOP                         
5B21: 00              NOP                         
5B22: 18 00           JR      $5B24               ; {}
5B24: 1C              INC     E                   
5B25: 08 1E 0C        LD      ($0C1E),SP          
5B28: 1B              DEC     DE                  
5B29: 0C              INC     C                   
5B2A: D6 09           SUB     $09                 
5B2C: FF              RST     0X38                
5B2D: 40              LD      B,B                 
5B2E: FF              RST     0X38                
5B2F: 60              LD      H,B                 
5B30: 7F              LD      A,A                 
5B31: 30 5F           JR      NC,$5B92            ; {}
5B33: 38 27           JR      C,$5B5C             ; {}
5B35: 18 5F           JR      $5B96               ; {}
5B37: 20 47           JR      NZ,$5B80            ; {}
5B39: 38 E3           JR      C,$5B1E             ; {}
5B3B: 5F              LD      E,A                 
5B3C: F8 67           LD      HL,SP+$67           
5B3E: FF              RST     0X38                
5B3F: 00              NOP                         
5B40: 00              NOP                         
5B41: 00              NOP                         
5B42: 07              RLCA                        
5B43: 00              NOP                         
5B44: 18 07           JR      $5B4D               ; {}
5B46: 23              INC     HL                  
5B47: 1C              INC     E                   
5B48: 45              LD      B,L                 
5B49: 3B              DEC     SP                  
5B4A: 4E              LD      C,(HL)              
5B4B: 37              SCF                         
5B4C: 4E              LD      C,(HL)              
5B4D: 37              SCF                         
5B4E: 4D              LD      C,L                 
5B4F: 37              SCF                         
5B50: 47              LD      B,A                 
5B51: 3B              DEC     SP                  
5B52: C3 3C E0        JP      $E03C               
5B55: 5F              LD      E,A                 
5B56: F1              POP     AF                  
5B57: 0F              RRCA                        
5B58: 1C              INC     E                   
5B59: 03              INC     BC                  
5B5A: 0F              RRCA                        
5B5B: 00              NOP                         
5B5C: 05              DEC     B                   
5B5D: 03              INC     BC                  
5B5E: 03              INC     BC                  
5B5F: 00              NOP                         
5B60: 00              NOP                         
5B61: 00              NOP                         
5B62: 07              RLCA                        
5B63: 00              NOP                         
5B64: 1B              DEC     DE                  
5B65: 05              DEC     B                   
5B66: 23              INC     HL                  
5B67: 1D              DEC     E                   
5B68: 5F              LD      E,A                 
5B69: 23              INC     HL                  
5B6A: 5F              LD      E,A                 
5B6B: 2D              DEC     L                   
5B6C: 5F              LD      E,A                 
5B6D: 2E 4F           LD      L,$4F               
5B6F: 35              DEC     (HL)                
5B70: 47              LD      B,A                 
5B71: 39              ADD     HL,SP               
5B72: C3 3C E0        JP      $E03C               
5B75: 5F              LD      E,A                 
5B76: F1              POP     AF                  
5B77: 0F              RRCA                        
5B78: 1C              INC     E                   
5B79: 03              INC     BC                  
5B7A: 0F              RRCA                        
5B7B: 00              NOP                         
5B7C: 05              DEC     B                   
5B7D: 03              INC     BC                  
5B7E: 03              INC     BC                  
5B7F: 00              NOP                         
5B80: 00              NOP                         
5B81: FF              RST     0X38                
5B82: 00              NOP                         
5B83: FF              RST     0X38                
5B84: 22              LD      (HLI),A             
5B85: DD                              
5B86: 14              INC     D                   
5B87: EB                              
5B88: 08 F7 14        LD      ($14F7),SP          
5B8B: EB                              
5B8C: 22              LD      (HLI),A             
5B8D: DD                              
5B8E: 00              NOP                         
5B8F: FF              RST     0X38                
5B90: 00              NOP                         
5B91: FF              RST     0X38                
5B92: 00              NOP                         
5B93: FF              RST     0X38                
5B94: 22              LD      (HLI),A             
5B95: DD                              
5B96: 14              INC     D                   
5B97: EB                              
5B98: 08 F7 14        LD      ($14F7),SP          
5B9B: EB                              
5B9C: 22              LD      (HLI),A             
5B9D: DD                              
5B9E: 00              NOP                         
5B9F: FF              RST     0X38                
5BA0: 00              NOP                         
5BA1: FF              RST     0X38                
5BA2: 00              NOP                         
5BA3: FF              RST     0X38                
5BA4: 22              LD      (HLI),A             
5BA5: DD                              
5BA6: 14              INC     D                   
5BA7: EB                              
5BA8: 08 F7 14        LD      ($14F7),SP          
5BAB: EB                              
5BAC: 22              LD      (HLI),A             
5BAD: DD                              
5BAE: 00              NOP                         
5BAF: FF              RST     0X38                
5BB0: 00              NOP                         
5BB1: FF              RST     0X38                
5BB2: 00              NOP                         
5BB3: FF              RST     0X38                
5BB4: 22              LD      (HLI),A             
5BB5: DD                              
5BB6: 14              INC     D                   
5BB7: EB                              
5BB8: 08 F7 14        LD      ($14F7),SP          
5BBB: EB                              
5BBC: 22              LD      (HLI),A             
5BBD: DD                              
5BBE: 00              NOP                         
5BBF: FF              RST     0X38                
5BC0: 00              NOP                         
5BC1: FF              RST     0X38                
5BC2: 00              NOP                         
5BC3: FF              RST     0X38                
5BC4: 22              LD      (HLI),A             
5BC5: DD                              
5BC6: 14              INC     D                   
5BC7: EB                              
5BC8: 08 F7 14        LD      ($14F7),SP          
5BCB: EB                              
5BCC: 22              LD      (HLI),A             
5BCD: DD                              
5BCE: 00              NOP                         
5BCF: FF              RST     0X38                
5BD0: 00              NOP                         
5BD1: FF              RST     0X38                
5BD2: 00              NOP                         
5BD3: FF              RST     0X38                
5BD4: 22              LD      (HLI),A             
5BD5: DD                              
5BD6: 14              INC     D                   
5BD7: EB                              
5BD8: 08 F7 14        LD      ($14F7),SP          
5BDB: EB                              
5BDC: 22              LD      (HLI),A             
5BDD: DD                              
5BDE: 00              NOP                         
5BDF: FF              RST     0X38                
5BE0: 00              NOP                         
5BE1: FF              RST     0X38                
5BE2: 00              NOP                         
5BE3: FF              RST     0X38                
5BE4: 22              LD      (HLI),A             
5BE5: DD                              
5BE6: 14              INC     D                   
5BE7: EB                              
5BE8: 08 F7 14        LD      ($14F7),SP          
5BEB: EB                              
5BEC: 22              LD      (HLI),A             
5BED: DD                              
5BEE: 00              NOP                         
5BEF: FF              RST     0X38                
5BF0: 00              NOP                         
5BF1: FF              RST     0X38                
5BF2: 00              NOP                         
5BF3: FF              RST     0X38                
5BF4: 22              LD      (HLI),A             
5BF5: DD                              
5BF6: 14              INC     D                   
5BF7: EB                              
5BF8: 08 F7 14        LD      ($14F7),SP          
5BFB: EB                              
5BFC: 22              LD      (HLI),A             
5BFD: DD                              
5BFE: 00              NOP                         
5BFF: FF              RST     0X38                
5C00: 03              INC     BC                  
5C01: 00              NOP                         
5C02: 05              DEC     B                   
5C03: 03              INC     BC                  
5C04: 0B              DEC     BC                  
5C05: 07              RLCA                        
5C06: 17              RLA                         
5C07: 08 28 17        LD      ($1728),SP          
5C0A: 37              SCF                         
5C0B: 0F              RRCA                        
5C0C: 3F              CCF                         
5C0D: 0B              DEC     BC                  
5C0E: 5F              LD      E,A                 
5C0F: 2B              DEC     HL                  
5C10: 9F              SBC     A                   
5C11: 6B              LD      L,E                 
5C12: 97              SUB     A                   
5C13: 6F              LD      L,A                 
5C14: BC              CP      H                   
5C15: 67              LD      H,A                 
5C16: BF              CP      A                   
5C17: 67              LD      H,A                 
5C18: BF              CP      A                   
5C19: 64              LD      H,H                 
5C1A: 67              LD      H,A                 
5C1B: 18 C0           JR      $5BDD               ; {}
5C1D: 3F              CCF                         
5C1E: FF              RST     0X38                
5C1F: 00              NOP                         
5C20: E0 00           LD      ($FF00+$00),A       
5C22: 90              SUB     B                   
5C23: E0 08           LD      ($FF00+$08),A       
5C25: F0 C4           LD      A,($C4)             
5C27: 38 44           JR      C,$5C6D             ; {}
5C29: B8              CP      B                   
5C2A: A2              AND     D                   
5C2B: DC D2 6C        CALL    C,$6CD2             ; {}
5C2E: F5              PUSH    AF                  
5C2F: 2A              LD      A,(HLI)             
5C30: F5              PUSH    AF                  
5C31: 2A              LD      A,(HLI)             
5C32: DD                              
5C33: E2              LD      (C),A               
5C34: B1              OR      C                   
5C35: CE F9           ADC     $F9                 
5C37: 8E              ADC     A,(HL)              
5C38: FA 8C CD        LD      A,($CD8C)           
5C3B: 32              LD      (HLD),A             
5C3C: 01 FE FF        LD      BC,$FFFE            
5C3F: 00              NOP                         
5C40: 03              INC     BC                  
5C41: 00              NOP                         
5C42: 05              DEC     B                   
5C43: 03              INC     BC                  
5C44: 09              ADD     HL,BC               
5C45: 07              RLCA                        
5C46: 11 0F 10        LD      DE,$100F            
5C49: 0F              RRCA                        
5C4A: 28 17           JR      Z,$5C63             ; {}
5C4C: 28 17           JR      Z,$5C65             ; {}
5C4E: 64              LD      H,H                 
5C4F: 1B              DEC     DE                  
5C50: A0              AND     B                   
5C51: 5F              LD      E,A                 
5C52: 90              SUB     B                   
5C53: 6F              LD      L,A                 
5C54: 88              ADC     A,B                 
5C55: 77              LD      (HL),A              
5C56: B7              OR      A                   
5C57: 58              LD      E,B                 
5C58: 4C              LD      C,H                 
5C59: 3F              CCF                         
5C5A: 83              ADD     A,E                 
5C5B: 7F              LD      A,A                 
5C5C: 80              ADD     A,B                 
5C5D: 7F              LD      A,A                 
5C5E: FF              RST     0X38                
5C5F: 00              NOP                         
5C60: E0 00           LD      ($FF00+$00),A       
5C62: 90              SUB     B                   
5C63: E0 88           LD      ($FF00+$88),A       
5C65: F0 08           LD      A,($08)             
5C67: F0 08           LD      A,($08)             
5C69: F0 14           LD      A,($14)             
5C6B: E8 34           ADD     SP,$34              
5C6D: C8              RET     Z                   
5C6E: 4A              LD      C,D                 
5C6F: B4              OR      H                   
5C70: 11 EE 21        LD      DE,$21EE            
5C73: DE 45           SBC     $45                 
5C75: BA              CP      D                   
5C76: 8D              ADC     A,L                 
5C77: 7A              LD      A,D                 
5C78: 12              LD      (DE),A              
5C79: FC                              
5C7A: E2              LD      (C),A               
5C7B: FC                              
5C7C: 01 FE FF        LD      BC,$FFFE            
5C7F: 00              NOP                         
5C80: 00              NOP                         
5C81: 00              NOP                         
5C82: 7F              LD      A,A                 
5C83: 00              NOP                         
5C84: 7F              LD      A,A                 
5C85: 3F              CCF                         
5C86: 7C              LD      A,H                 
5C87: 0F              RRCA                        
5C88: 2C              INC     L                   
5C89: 17              RLA                         
5C8A: 78              LD      A,B                 
5C8B: 37              SCF                         
5C8C: 7C              LD      A,H                 
5C8D: 23              INC     HL                  
5C8E: 7E              LD      A,(HL)              
5C8F: 21 FA 65        LD      HL,$65FA            
5C92: BB              CP      E                   
5C93: 7C              LD      A,H                 
5C94: A7              AND     A                   
5C95: 7B              LD      A,E                 
5C96: FF              RST     0X38                
5C97: 63              LD      H,E                 
5C98: BF              CP      A                   
5C99: 6B              LD      L,E                 
5C9A: 7F              LD      A,A                 
5C9B: 00              NOP                         
5C9C: 10 0F           ;;STOP    $0F                 
5C9E: 1F              RRA                         
5C9F: 00              NOP                         
5CA0: 00              NOP                         
5CA1: 00              NOP                         
5CA2: C0              RET     NZ                  
5CA3: 00              NOP                         
5CA4: A0              AND     B                   
5CA5: C0              RET     NZ                  
5CA6: 10 E0           ;;STOP    $E0                 
5CA8: 08 F0 38        LD      ($38F0),SP          
5CAB: C0              RET     NZ                  
5CAC: 04              INC     B                   
5CAD: F8 E4           LD      HL,SP+$E4           
5CAF: 18 92           JR      $5C43               ; {}
5CB1: 6C              LD      L,H                 
5CB2: 0E F0           LD      C,$F0               
5CB4: 04              INC     B                   
5CB5: F8 04           LD      HL,SP+$04           
5CB7: F8 2A           LD      HL,SP+$2A           
5CB9: DC F1 3E        CALL    C,$3EF1             
5CBC: 01 FE FF        LD      BC,$FFFE            
5CBF: 00              NOP                         
5CC0: 7F              LD      A,A                 
5CC1: 00              NOP                         
5CC2: 7F              LD      A,A                 
5CC3: 3F              CCF                         
5CC4: 7C              LD      A,H                 
5CC5: 0F              RRCA                        
5CC6: 2C              INC     L                   
5CC7: 17              RLA                         
5CC8: 78              LD      A,B                 
5CC9: 37              SCF                         
5CCA: 7C              LD      A,H                 
5CCB: 23              INC     HL                  
5CCC: 7E              LD      A,(HL)              
5CCD: 21 FA 65        LD      HL,$65FA            
5CD0: BB              CP      E                   
5CD1: 7C              LD      A,H                 
5CD2: A7              AND     A                   
5CD3: 79              LD      A,C                 
5CD4: FF              RST     0X38                
5CD5: 65              LD      H,L                 
5CD6: BF              CP      A                   
5CD7: 6D              LD      L,L                 
5CD8: 7F              LD      A,A                 
5CD9: 00              NOP                         
5CDA: 06 01           LD      B,$01               
5CDC: 08 07 0F        LD      ($0F07),SP          
5CDF: 00              NOP                         
5CE0: C0              RET     NZ                  
5CE1: 00              NOP                         
5CE2: A0              AND     B                   
5CE3: C0              RET     NZ                  
5CE4: 10 E0           ;;STOP    $E0                 
5CE6: 08 F0 38        LD      ($38F0),SP          
5CE9: C0              RET     NZ                  
5CEA: 04              INC     B                   
5CEB: F8 64           LD      HL,SP+$64           
5CED: 98              SBC     B                   
5CEE: 92              SUB     D                   
5CEF: 6C              LD      L,H                 
5CF0: 8E              ADC     A,(HL)              
5CF1: 70              LD      (HL),B              
5CF2: 84              ADD     A,H                 
5CF3: F8 84           LD      HL,SP+$84           
5CF5: F8 AC           LD      HL,SP+$AC           
5CF7: D8              RET     C                   
5CF8: F4                              
5CF9: 38 02           JR      C,$5CFD             ; {}
5CFB: FC                              
5CFC: 02              LD      (BC),A              
5CFD: FC                              
5CFE: FE 00           CP      $00                 
5D00: 01 00 03        LD      BC,$0300            
5D03: 01 03 01        LD      BC,$0103            
5D06: 07              RLCA                        
5D07: 01 1F 00        LD      BC,$001F            
5D0A: 3F              CCF                         
5D0B: 03              INC     BC                  
5D0C: 3F              CCF                         
5D0D: 06 7F           LD      B,$7F               
5D0F: 00              NOP                         
5D10: 7F              LD      A,A                 
5D11: 01 7F 00        LD      BC,$007F            
5D14: 7F              LD      A,A                 
5D15: 06 3F           LD      B,$3F               
5D17: 03              INC     BC                  
5D18: 3F              CCF                         
5D19: 00              NOP                         
5D1A: 1F              RRA                         
5D1B: 00              NOP                         
5D1C: 29              ADD     HL,HL               
5D1D: 1E 1E           LD      E,$1E               
5D1F: 00              NOP                         
5D20: 80              ADD     A,B                 
5D21: 00              NOP                         
5D22: C0              RET     NZ                  
5D23: 80              ADD     A,B                 
5D24: C0              RET     NZ                  
5D25: 80              ADD     A,B                 
5D26: E0 80           LD      ($FF00+$80),A       
5D28: F8 00           LD      HL,SP+$00           
5D2A: FC                              
5D2B: C0              RET     NZ                  
5D2C: FC                              
5D2D: 60              LD      H,B                 
5D2E: FE 60           CP      $60                 
5D30: FE C0           CP      $C0                 
5D32: FE 60           CP      $60                 
5D34: FE 60           CP      $60                 
5D36: FC                              
5D37: C0              RET     NZ                  
5D38: FC                              
5D39: 00              NOP                         
5D3A: F8 00           LD      HL,SP+$00           
5D3C: 94              SUB     H                   
5D3D: 78              LD      A,B                 
5D3E: 78              LD      A,B                 
5D3F: 00              NOP                         
5D40: 00              NOP                         
5D41: 00              NOP                         
5D42: 00              NOP                         
5D43: 00              NOP                         
5D44: 01 00 07        LD      BC,$0700            
5D47: 01 1F 00        LD      BC,$001F            
5D4A: 3F              CCF                         
5D4B: 03              INC     BC                  
5D4C: 3F              CCF                         
5D4D: 06 7F           LD      B,$7F               
5D4F: 00              NOP                         
5D50: 7F              LD      A,A                 
5D51: 01 7F 03        LD      BC,$037F            
5D54: 7F              LD      A,A                 
5D55: 06 3F           LD      B,$3F               
5D57: 07              RLCA                        
5D58: 3F              CCF                         
5D59: 00              NOP                         
5D5A: 1F              RRA                         
5D5B: 00              NOP                         
5D5C: 29              ADD     HL,HL               
5D5D: 1E 1E           LD      E,$1E               
5D5F: 00              NOP                         
5D60: 00              NOP                         
5D61: 00              NOP                         
5D62: 00              NOP                         
5D63: 00              NOP                         
5D64: 80              ADD     A,B                 
5D65: 00              NOP                         
5D66: E0 80           LD      ($FF00+$80),A       
5D68: F8 00           LD      HL,SP+$00           
5D6A: FC                              
5D6B: C0              RET     NZ                  
5D6C: FC                              
5D6D: 60              LD      H,B                 
5D6E: FE 60           CP      $60                 
5D70: FE C0           CP      $C0                 
5D72: FE 00           CP      $00                 
5D74: FE 00           CP      $00                 
5D76: FC                              
5D77: E0 FC           LD      ($FF00+$FC),A       
5D79: 00              NOP                         
5D7A: F8 00           LD      HL,SP+$00           
5D7C: 94              SUB     H                   
5D7D: 78              LD      A,B                 
5D7E: 78              LD      A,B                 
5D7F: 00              NOP                         
5D80: 00              NOP                         
5D81: 00              NOP                         
5D82: 00              NOP                         
5D83: 00              NOP                         
5D84: 00              NOP                         
5D85: 00              NOP                         
5D86: 07              RLCA                        
5D87: 00              NOP                         
5D88: 1F              RRA                         
5D89: 02              LD      (BC),A              
5D8A: 3D              DEC     A                   
5D8B: 03              INC     BC                  
5D8C: 3F              CCF                         
5D8D: 00              NOP                         
5D8E: 7F              LD      A,A                 
5D8F: 00              NOP                         
5D90: 7F              LD      A,A                 
5D91: 10 7F           ;;STOP    $7F                 
5D93: 10 7F           ;;STOP    $7F                 
5D95: 18 3F           JR      $5DD6               ; {}
5D97: 08 3F 00        LD      ($003F),SP          
5D9A: 57              LD      D,A                 
5D9B: 38 43           JR      C,$5DE0             ; {}
5D9D: 3C              INC     A                   
5D9E: 3C              INC     A                   
5D9F: 00              NOP                         
5DA0: 38 00           JR      C,$5DA2             ; {}
5DA2: 68              LD      L,B                 
5DA3: 30 D0           JR      NC,$5D75            ; {}
5DA5: 60              LD      H,B                 
5DA6: A0              AND     B                   
5DA7: C0              RET     NZ                  
5DA8: F0 00           LD      A,($00)             
5DAA: B8              CP      B                   
5DAB: C0              RET     NZ                  
5DAC: F8 00           LD      HL,SP+$00           
5DAE: FC                              
5DAF: 00              NOP                         
5DB0: FC                              
5DB1: 20 FC           JR      NZ,$5DAF            ; {}
5DB3: 60              LD      H,B                 
5DB4: FC                              
5DB5: C0              RET     NZ                  
5DB6: F8 80           LD      HL,SP+$80           
5DB8: F4                              
5DB9: 08 E4 18        LD      ($18E4),SP          
5DBC: F8 00           LD      HL,SP+$00           
5DBE: 00              NOP                         
5DBF: 00              NOP                         
5DC0: 00              NOP                         
5DC1: 00              NOP                         
5DC2: 00              NOP                         
5DC3: 00              NOP                         
5DC4: 00              NOP                         
5DC5: 00              NOP                         
5DC6: 07              RLCA                        
5DC7: 00              NOP                         
5DC8: 1F              RRA                         
5DC9: 00              NOP                         
5DCA: 3F              CCF                         
5DCB: 01 3F 01        LD      BC,$013F            
5DCE: 7F              LD      A,A                 
5DCF: 01 7F 01        LD      BC,$017F            
5DD2: 7F              LD      A,A                 
5DD3: 01 7F 01        LD      BC,$017F            
5DD6: 3F              CCF                         
5DD7: 01 3F 00        LD      BC,$003F            
5DDA: 1F              RRA                         
5DDB: 00              NOP                         
5DDC: 29              ADD     HL,HL               
5DDD: 1E 1E           LD      E,$1E               
5DDF: 00              NOP                         
5DE0: 01 00 03        LD      BC,$0300            
5DE3: 01 03 01        LD      BC,$0103            
5DE6: 07              RLCA                        
5DE7: 01 1F 00        LD      BC,$001F            
5DEA: 3F              CCF                         
5DEB: 04              INC     B                   
5DEC: 3F              CCF                         
5DED: 06 7F           LD      B,$7F               
5DEF: 02              LD      (BC),A              
5DF0: 7F              LD      A,A                 
5DF1: 00              NOP                         
5DF2: 7F              LD      A,A                 
5DF3: 18 7B           JR      $5E70               ; {}
5DF5: 1F              RRA                         
5DF6: 3B              DEC     SP                  
5DF7: 0F              RRCA                        
5DF8: 3B              DEC     SP                  
5DF9: 07              RLCA                        
5DFA: 1F              RRA                         
5DFB: 00              NOP                         
5DFC: 29              ADD     HL,HL               
5DFD: 1E 1E           LD      E,$1E               
5DFF: 00              NOP                         
5E00: 1C              INC     E                   
5E01: 00              NOP                         
5E02: 3F              CCF                         
5E03: 1C              INC     E                   
5E04: 3F              CCF                         
5E05: 17              RLA                         
5E06: 3F              CCF                         
5E07: 18 7F           JR      $5E88               ; {}
5E09: 07              RLCA                        
5E0A: 5F              LD      E,A                 
5E0B: 2F              CPL                         
5E0C: AF              XOR     A                   
5E0D: 5F              LD      E,A                 
5E0E: AF              XOR     A                   
5E0F: 5F              LD      E,A                 
5E10: EF              RST     0X28                
5E11: 5F              LD      E,A                 
5E12: F6 6F           OR      $6F                 
5E14: BF              CP      A                   
5E15: 60              LD      H,B                 
5E16: 56              LD      D,(HL)              
5E17: 2F              CPL                         
5E18: 38 07           JR      C,$5E21             ; {}
5E1A: 7F              LD      A,A                 
5E1B: 38 FD           JR      C,$5E1A             ; {}
5E1D: 56              LD      D,(HL)              
5E1E: FF              RST     0X38                
5E1F: 00              NOP                         
5E20: E0 00           LD      ($FF00+$00),A       
5E22: F0 E0           LD      A,($E0)             
5E24: F8 A0           LD      HL,SP+$A0           
5E26: FC                              
5E27: E0 FE           LD      ($FF00+$FE),A       
5E29: 00              NOP                         
5E2A: C6 B8           ADD     $B8                 
5E2C: BB              CP      E                   
5E2D: DC BB DC        CALL    C,$DCBB             
5E30: 7D              LD      A,L                 
5E31: 9E              SBC     (HL)                
5E32: BD              CP      L                   
5E33: 5E              LD      E,(HL)              
5E34: 3D              DEC     A                   
5E35: DE 5A           SBC     $5A                 
5E37: BC              CP      H                   
5E38: FC                              
5E39: 00              NOP                         
5E3A: DE 3C           SBC     $3C                 
5E3C: BF              CP      A                   
5E3D: 6A              LD      L,D                 
5E3E: FF              RST     0X38                
5E3F: 00              NOP                         
5E40: 01 00 03        LD      BC,$0300            
5E43: 01 03 01        LD      BC,$0103            
5E46: 03              INC     BC                  
5E47: 01 03 01        LD      BC,$0103            
5E4A: 05              DEC     B                   
5E4B: 03              INC     BC                  
5E4C: 0B              DEC     BC                  
5E4D: 07              RLCA                        
5E4E: 17              RLA                         
5E4F: 0F              RRCA                        
5E50: 17              RLA                         
5E51: 0F              RRCA                        
5E52: 0B              DEC     BC                  
5E53: 07              RLCA                        
5E54: 05              DEC     B                   
5E55: 03              INC     BC                  
5E56: 03              INC     BC                  
5E57: 01 03 01        LD      BC,$0103            
5E5A: 03              INC     BC                  
5E5B: 01 03 01        LD      BC,$0103            
5E5E: 01 00 00        LD      BC,$0000            
5E61: 00              NOP                         
5E62: 00              NOP                         
5E63: 00              NOP                         
5E64: 00              NOP                         
5E65: 00              NOP                         
5E66: 00              NOP                         
5E67: 00              NOP                         
5E68: 00              NOP                         
5E69: 00              NOP                         
5E6A: 00              NOP                         
5E6B: 00              NOP                         
5E6C: 3F              CCF                         
5E6D: 00              NOP                         
5E6E: 7F              LD      A,A                 
5E6F: 3F              CCF                         
5E70: 7F              LD      A,A                 
5E71: 3F              CCF                         
5E72: 3F              CCF                         
5E73: 00              NOP                         
5E74: 00              NOP                         
5E75: 00              NOP                         
5E76: 00              NOP                         
5E77: 00              NOP                         
5E78: 00              NOP                         
5E79: 00              NOP                         
5E7A: 00              NOP                         
5E7B: 00              NOP                         
5E7C: 00              NOP                         
5E7D: 00              NOP                         
5E7E: 00              NOP                         
5E7F: 00              NOP                         
5E80: 00              NOP                         
5E81: 00              NOP                         
5E82: 00              NOP                         
5E83: 00              NOP                         
5E84: 00              NOP                         
5E85: 00              NOP                         
5E86: 01 00 03        LD      BC,$0300            
5E89: 01 03 01        LD      BC,$0103            
5E8C: FF              RST     0X38                
5E8D: 03              INC     BC                  
5E8E: FF              RST     0X38                
5E8F: FF              RST     0X38                
5E90: FF              RST     0X38                
5E91: FF              RST     0X38                
5E92: FF              RST     0X38                
5E93: 03              INC     BC                  
5E94: 03              INC     BC                  
5E95: 01 03 01        LD      BC,$0103            
5E98: 01 00 00        LD      BC,$0000            
5E9B: 00              NOP                         
5E9C: 00              NOP                         
5E9D: 00              NOP                         
5E9E: 00              NOP                         
5E9F: 00              NOP                         
5EA0: 00              NOP                         
5EA1: 00              NOP                         
5EA2: 00              NOP                         
5EA3: 00              NOP                         
5EA4: 00              NOP                         
5EA5: 00              NOP                         
5EA6: 00              NOP                         
5EA7: 00              NOP                         
5EA8: 00              NOP                         
5EA9: 00              NOP                         
5EAA: 00              NOP                         
5EAB: 00              NOP                         
5EAC: 01 00 02        LD      BC,$0200            
5EAF: 01 FC 03        LD      BC,$03FC            
5EB2: 02              LD      (BC),A              
5EB3: 01 01 00        LD      BC,$0001            
5EB6: 00              NOP                         
5EB7: 00              NOP                         
5EB8: 00              NOP                         
5EB9: 00              NOP                         
5EBA: 00              NOP                         
5EBB: 00              NOP                         
5EBC: 00              NOP                         
5EBD: 00              NOP                         
5EBE: 00              NOP                         
5EBF: 00              NOP                         
5EC0: 00              NOP                         
5EC1: 00              NOP                         
5EC2: 00              NOP                         
5EC3: 00              NOP                         
5EC4: 1C              INC     E                   
5EC5: 00              NOP                         
5EC6: 3F              CCF                         
5EC7: 08 3F 1C        LD      ($1C3F),SP          
5ECA: 3F              CCF                         
5ECB: 0F              RRCA                        
5ECC: 1E 07           LD      E,$07               
5ECE: 1D              DEC     E                   
5ECF: 06 1D           LD      B,$1D               
5ED1: 06 1E           LD      B,$1E               
5ED3: 07              RLCA                        
5ED4: 3F              CCF                         
5ED5: 0F              RRCA                        
5ED6: 3F              CCF                         
5ED7: 1C              INC     E                   
5ED8: 3F              CCF                         
5ED9: 08 1C 00        LD      ($001C),SP          
5EDC: 00              NOP                         
5EDD: 00              NOP                         
5EDE: 00              NOP                         
5EDF: 00              NOP                         
5EE0: 00              NOP                         
5EE1: 00              NOP                         
5EE2: 01 00 03        LD      BC,$0300            
5EE5: 00              NOP                         
5EE6: 03              INC     BC                  
5EE7: 01 07 01        LD      BC,$0107            
5EEA: 0F              RRCA                        
5EEB: 03              INC     BC                  
5EEC: 3E 07           LD      A,$07               
5EEE: 7D              LD      A,L                 
5EEF: 1E 7D           LD      E,$7D               
5EF1: 1E 3E           LD      E,$3E               
5EF3: 07              RLCA                        
5EF4: 0F              RRCA                        
5EF5: 03              INC     BC                  
5EF6: 07              RLCA                        
5EF7: 01 03 01        LD      BC,$0103            
5EFA: 03              INC     BC                  
5EFB: 00              NOP                         
5EFC: 01 00 00        LD      BC,$0000            
5EFF: 00              NOP                         
5F00: 00              NOP                         
5F01: 00              NOP                         
5F02: 00              NOP                         
5F03: 00              NOP                         
5F04: 03              INC     BC                  
5F05: 00              NOP                         
5F06: 0C              INC     C                   
5F07: 03              INC     BC                  
5F08: 1F              RRA                         
5F09: 01 1F 0E        LD      BC,$0E1F            
5F0C: 3F              CCF                         
5F0D: 0A              LD      A,(BC)              
5F0E: 3F              CCF                         
5F0F: 0E 2E           LD      C,$2E               
5F11: 11 20 1F        LD      DE,$1F20            
5F14: 60              LD      H,B                 
5F15: 1F              RRA                         
5F16: F0 6F           LD      A,($6F)             
5F18: F8 77           LD      HL,SP+$77           
5F1A: FF              RST     0X38                
5F1B: 00              NOP                         
5F1C: 00              NOP                         
5F1D: 00              NOP                         
5F1E: 00              NOP                         
5F1F: 00              NOP                         
5F20: 00              NOP                         
5F21: 00              NOP                         
5F22: 00              NOP                         
5F23: 00              NOP                         
5F24: E0 00           LD      ($FF00+$00),A       
5F26: 90              SUB     B                   
5F27: E0 F8           LD      ($FF00+$F8),A       
5F29: C0              RET     NZ                  
5F2A: FC                              
5F2B: B8              CP      B                   
5F2C: 7C              LD      A,H                 
5F2D: A8              XOR     B                   
5F2E: 7C              LD      A,H                 
5F2F: B8              CP      B                   
5F30: 3C              INC     A                   
5F31: C0              RET     NZ                  
5F32: 06 F8           LD      B,$F8               
5F34: 07              RLCA                        
5F35: FA 07 FA        LD      A,($FA07)           
5F38: 0F              RRCA                        
5F39: F0 F0           LD      A,($F0)             
5F3B: 00              NOP                         
5F3C: 00              NOP                         
5F3D: 00              NOP                         
5F3E: 00              NOP                         
5F3F: 00              NOP                         
5F40: 07              RLCA                        
5F41: 00              NOP                         
5F42: 07              RLCA                        
5F43: 03              INC     BC                  
5F44: 07              RLCA                        
5F45: 03              INC     BC                  
5F46: 0C              INC     C                   
5F47: 07              RLCA                        
5F48: 19              ADD     HL,DE               
5F49: 0F              RRCA                        
5F4A: 7F              LD      A,A                 
5F4B: 1F              RRA                         
5F4C: FF              RST     0X38                
5F4D: 7F              LD      A,A                 
5F4E: 41              LD      B,C                 
5F4F: 3F              CCF                         
5F50: 20 1F           JR      NZ,$5F71            ; {}
5F52: 10 0F           ;;STOP    $0F                 
5F54: 10 0F           ;;STOP    $0F                 
5F56: 10 0F           ;;STOP    $0F                 
5F58: 10 0F           ;;STOP    $0F                 
5F5A: 0F              RRCA                        
5F5B: 00              NOP                         
5F5C: 00              NOP                         
5F5D: 00              NOP                         
5F5E: 00              NOP                         
5F5F: 00              NOP                         
5F60: FF              RST     0X38                
5F61: 00              NOP                         
5F62: FF              RST     0X38                
5F63: FE FF           CP      $FF                 
5F65: FE 7E           CP      $7E                 
5F67: FC                              
5F68: FC                              
5F69: F0 F0           LD      A,($F0)             
5F6B: E0 E0           LD      ($FF00+$E0),A       
5F6D: C0              RET     NZ                  
5F6E: C0              RET     NZ                  
5F6F: 80              ADD     A,B                 
5F70: C0              RET     NZ                  
5F71: 80              ADD     A,B                 
5F72: 40              LD      B,B                 
5F73: 80              ADD     A,B                 
5F74: 40              LD      B,B                 
5F75: 80              ADD     A,B                 
5F76: 40              LD      B,B                 
5F77: 80              ADD     A,B                 
5F78: 80              ADD     A,B                 
5F79: 00              NOP                         
5F7A: 00              NOP                         
5F7B: 00              NOP                         
5F7C: 00              NOP                         
5F7D: 00              NOP                         
5F7E: 00              NOP                         
5F7F: 00              NOP                         
5F80: 00              NOP                         
5F81: FF              RST     0X38                
5F82: 00              NOP                         
5F83: FF              RST     0X38                
5F84: 22              LD      (HLI),A             
5F85: DD                              
5F86: 14              INC     D                   
5F87: EB                              
5F88: 08 F7 14        LD      ($14F7),SP          
5F8B: EB                              
5F8C: 22              LD      (HLI),A             
5F8D: DD                              
5F8E: 00              NOP                         
5F8F: FF              RST     0X38                
5F90: 00              NOP                         
5F91: FF              RST     0X38                
5F92: 00              NOP                         
5F93: FF              RST     0X38                
5F94: 22              LD      (HLI),A             
5F95: DD                              
5F96: 14              INC     D                   
5F97: EB                              
5F98: 08 F7 14        LD      ($14F7),SP          
5F9B: EB                              
5F9C: 22              LD      (HLI),A             
5F9D: DD                              
5F9E: 00              NOP                         
5F9F: FF              RST     0X38                
5FA0: 00              NOP                         
5FA1: FF              RST     0X38                
5FA2: 00              NOP                         
5FA3: FF              RST     0X38                
5FA4: 22              LD      (HLI),A             
5FA5: DD                              
5FA6: 14              INC     D                   
5FA7: EB                              
5FA8: 08 F7 14        LD      ($14F7),SP          
5FAB: EB                              
5FAC: 22              LD      (HLI),A             
5FAD: DD                              
5FAE: 00              NOP                         
5FAF: FF              RST     0X38                
5FB0: 00              NOP                         
5FB1: FF              RST     0X38                
5FB2: 00              NOP                         
5FB3: FF              RST     0X38                
5FB4: 22              LD      (HLI),A             
5FB5: DD                              
5FB6: 14              INC     D                   
5FB7: EB                              
5FB8: 08 F7 14        LD      ($14F7),SP          
5FBB: EB                              
5FBC: 22              LD      (HLI),A             
5FBD: DD                              
5FBE: 00              NOP                         
5FBF: FF              RST     0X38                
5FC0: 00              NOP                         
5FC1: FF              RST     0X38                
5FC2: 00              NOP                         
5FC3: FF              RST     0X38                
5FC4: 22              LD      (HLI),A             
5FC5: DD                              
5FC6: 14              INC     D                   
5FC7: EB                              
5FC8: 08 F7 14        LD      ($14F7),SP          
5FCB: EB                              
5FCC: 22              LD      (HLI),A             
5FCD: DD                              
5FCE: 00              NOP                         
5FCF: FF              RST     0X38                
5FD0: 00              NOP                         
5FD1: FF              RST     0X38                
5FD2: 00              NOP                         
5FD3: FF              RST     0X38                
5FD4: 22              LD      (HLI),A             
5FD5: DD                              
5FD6: 14              INC     D                   
5FD7: EB                              
5FD8: 08 F7 14        LD      ($14F7),SP          
5FDB: EB                              
5FDC: 22              LD      (HLI),A             
5FDD: DD                              
5FDE: 00              NOP                         
5FDF: FF              RST     0X38                
5FE0: 00              NOP                         
5FE1: FF              RST     0X38                
5FE2: 00              NOP                         
5FE3: FF              RST     0X38                
5FE4: 22              LD      (HLI),A             
5FE5: DD                              
5FE6: 14              INC     D                   
5FE7: EB                              
5FE8: 08 F7 14        LD      ($14F7),SP          
5FEB: EB                              
5FEC: 22              LD      (HLI),A             
5FED: DD                              
5FEE: 00              NOP                         
5FEF: FF              RST     0X38                
5FF0: 00              NOP                         
5FF1: FF              RST     0X38                
5FF2: 00              NOP                         
5FF3: FF              RST     0X38                
5FF4: 22              LD      (HLI),A             
5FF5: DD                              
5FF6: 14              INC     D                   
5FF7: EB                              
5FF8: 08 F7 14        LD      ($14F7),SP          
5FFB: EB                              
5FFC: 22              LD      (HLI),A             
5FFD: DD                              
5FFE: 00              NOP                         
5FFF: FF              RST     0X38                
6000: 03              INC     BC                  
6001: 00              NOP                         
6002: 03              INC     BC                  
6003: 01 1F 00        LD      BC,$001F            
6006: 67              LD      H,A                 
6007: 1F              RRA                         
6008: CE 71           ADC     $71                 
600A: FE 65           CP      $65                 
600C: FE 6D           CP      $6D                 
600E: 6D              LD      L,L                 
600F: 32              LD      (HLD),A             
6010: 74              LD      (HL),H              
6011: 3B              DEC     SP                  
6012: 36 19           LD      (HL),$19            
6014: 30 1F           JR      NC,$6035            ; {}
6016: 39              ADD     HL,SP               
6017: 06 7F           LD      B,$7F               
6019: 3D              DEC     A                   
601A: F7              RST     0X30                
601B: 78              LD      A,B                 
601C: FF              RST     0X38                
601D: 07              RLCA                        
601E: 07              RLCA                        
601F: 00              NOP                         
6020: 60              LD      H,B                 
6021: 00              NOP                         
6022: F0 60           LD      A,($60)             
6024: F8 10           LD      HL,SP+$10           
6026: BC              CP      H                   
6027: C8              RET     Z                   
6028: 5C              LD      E,H                 
6029: E0 A8           LD      ($FF00+$A8),A       
602B: 70              LD      (HL),B              
602C: 9E              SBC     (HL)                
602D: 70              LD      (HL),B              
602E: E7              RST     0X20                
602F: 1A              LD      A,(DE)              
6030: FF              RST     0X38                
6031: 02              LD      (BC),A              
6032: 87              ADD     A,A                 
6033: 7A              LD      A,D                 
6034: F7              RST     0X30                
6035: 1A              LD      A,(DE)              
6036: F7              RST     0X30                
6037: DA EE B0        JP      C,$B0EE             
603A: DC 68 B8        CALL    C,$B868             
603D: D0              RET     NC                  
603E: F0 00           LD      A,($00)             
6040: 03              INC     BC                  
6041: 00              NOP                         
6042: 03              INC     BC                  
6043: 01 1F 00        LD      BC,$001F            
6046: 67              LD      H,A                 
6047: 1F              RRA                         
6048: CE 71           ADC     $71                 
604A: FE 6D           CP      $6D                 
604C: FE 65           CP      $65                 
604E: 6D              LD      L,L                 
604F: 32              LD      (HLD),A             
6050: 74              LD      (HL),H              
6051: 3B              DEC     SP                  
6052: F6 59           OR      $59                 
6054: F0 5F           LD      A,($5F)             
6056: 79              LD      A,C                 
6057: 26 3F           LD      H,$3F               
6059: 1D              DEC     E                   
605A: 1F              RRA                         
605B: 08 0F 07        LD      ($070F),SP          
605E: 07              RLCA                        
605F: 00              NOP                         
6060: C0              RET     NZ                  
6061: 00              NOP                         
6062: E0 40           LD      ($FF00+$40),A       
6064: F0 20           LD      A,($20)             
6066: B0              OR      B                   
6067: C0              RET     NZ                  
6068: 50              LD      D,B                 
6069: E0 A8           LD      ($FF00+$A8),A       
606B: 70              LD      (HL),B              
606C: 4C              LD      C,H                 
606D: B0              OR      B                   
606E: 6A              LD      L,D                 
606F: 94              SUB     H                   
6070: FA 04 4A        LD      A,($4A04)           ; {}
6073: B4              OR      H                   
6074: FA 04 FA        LD      A,($FA04)           
6077: 64              LD      H,H                 
6078: EC                              
6079: D0              RET     NC                  
607A: D8              RET     C                   
607B: 20 F0           JR      NZ,$606D            ; {}
607D: C0              RET     NZ                  
607E: E0 00           LD      ($FF00+$00),A       
6080: 00              NOP                         
6081: 00              NOP                         
6082: 01 00 1B        LD      BC,$1B00            
6085: 01 7F 18        LD      BC,$187F            
6088: FC                              
6089: 4B              LD      C,E                 
608A: BD              CP      L                   
608B: 5A              LD      E,D                 
608C: D9              RETI                        
608D: 26 61           LD      H,$61               
608F: 1E 39           LD      E,$39               
6091: 06 FF           LD      B,$FF               
6093: 1C              INC     E                   
6094: FF              RST     0X38                
6095: 7B              LD      A,E                 
6096: 7F              LD      A,A                 
6097: 00              NOP                         
6098: 00              NOP                         
6099: 00              NOP                         
609A: 00              NOP                         
609B: 00              NOP                         
609C: 00              NOP                         
609D: 00              NOP                         
609E: 00              NOP                         
609F: 00              NOP                         
60A0: 00              NOP                         
60A1: 00              NOP                         
60A2: C0              RET     NZ                  
60A3: 00              NOP                         
60A4: E0 C0           LD      ($FF00+$C0),A       
60A6: F0 00           LD      A,($00)             
60A8: 0B              DEC     BC                  
60A9: F0 57           LD      A,($57)             
60AB: FA 57 FA        LD      A,($FA57)           
60AE: D7              RST     0X10                
60AF: 3A              LD      A,(HLD)             
60B0: DF              RST     0X18                
60B1: BA              CP      D                   
60B2: FB              EI                          
60B3: 70              LD      (HL),B              
60B4: F0 C0           LD      A,($C0)             
60B6: C0              RET     NZ                  
60B7: 00              NOP                         
60B8: 00              NOP                         
60B9: 00              NOP                         
60BA: 00              NOP                         
60BB: 00              NOP                         
60BC: 00              NOP                         
60BD: 00              NOP                         
60BE: 00              NOP                         
60BF: 00              NOP                         
60C0: 00              NOP                         
60C1: 00              NOP                         
60C2: 01 00 1B        LD      BC,$1B00            
60C5: 01 7F 18        LD      BC,$187F            
60C8: FC                              
60C9: 4B              LD      C,E                 
60CA: BD              CP      L                   
60CB: 5A              LD      E,D                 
60CC: 59              LD      E,C                 
60CD: 26 E1           LD      H,$E1               
60CF: 5E              LD      E,(HL)              
60D0: F9              LD      SP,HL               
60D1: 66              LD      H,(HL)              
60D2: 7F              LD      A,A                 
60D3: 3C              INC     A                   
60D4: 3F              CCF                         
60D5: 0B              DEC     BC                  
60D6: 0F              RRCA                        
60D7: 00              NOP                         
60D8: 00              NOP                         
60D9: 00              NOP                         
60DA: 00              NOP                         
60DB: 00              NOP                         
60DC: 00              NOP                         
60DD: 00              NOP                         
60DE: 00              NOP                         
60DF: 00              NOP                         
60E0: 00              NOP                         
60E1: 00              NOP                         
60E2: C0              RET     NZ                  
60E3: 00              NOP                         
60E4: A0              AND     B                   
60E5: C0              RET     NZ                  
60E6: E0 00           LD      ($FF00+$00),A       
60E8: 16 E0           LD      D,$E0               
60EA: 4A              LD      C,D                 
60EB: F4                              
60EC: 5A              LD      E,D                 
60ED: F4                              
60EE: FA 14 FA        LD      A,($FA14)           
60F1: D4 F6 20        CALL    NC,$20F6            
60F4: E0 80           LD      ($FF00+$80),A       
60F6: 80              ADD     A,B                 
60F7: 00              NOP                         
60F8: 00              NOP                         
60F9: 00              NOP                         
60FA: 00              NOP                         
60FB: 00              NOP                         
60FC: 00              NOP                         
60FD: 00              NOP                         
60FE: 00              NOP                         
60FF: 00              NOP                         
6100: 00              NOP                         
6101: 00              NOP                         
6102: 00              NOP                         
6103: 00              NOP                         
6104: 00              NOP                         
6105: 00              NOP                         
6106: 00              NOP                         
6107: 00              NOP                         
6108: 00              NOP                         
6109: 00              NOP                         
610A: 00              NOP                         
610B: 00              NOP                         
610C: 00              NOP                         
610D: 00              NOP                         
610E: 00              NOP                         
610F: 00              NOP                         
6110: 00              NOP                         
6111: 00              NOP                         
6112: 10 10           ;;STOP    $10                 
6114: 12              LD      (DE),A              
6115: 12              LD      (DE),A              
6116: 1C              INC     E                   
6117: 1C              INC     E                   
6118: 04              INC     B                   
6119: 04              INC     B                   
611A: 07              RLCA                        
611B: 07              RLCA                        
611C: 00              NOP                         
611D: 00              NOP                         
611E: 00              NOP                         
611F: 00              NOP                         
6120: 00              NOP                         
6121: 00              NOP                         
6122: 00              NOP                         
6123: 00              NOP                         
6124: 10 00           ;;STOP    $00                 
6126: 18 00           JR      $6128               ; {}
6128: 1E 00           LD      E,$00               
612A: 2F              CPL                         
612B: 1E 5F           LD      E,$5F               
612D: 2A              LD      A,(HLI)             
612E: BF              CP      A                   
612F: 4E              LD      C,(HL)              
6130: FE 00           CP      $00                 
6132: 7C              LD      A,H                 
6133: 00              NOP                         
6134: 00              NOP                         
6135: 00              NOP                         
6136: 00              NOP                         
6137: 00              NOP                         
6138: 00              NOP                         
6139: 00              NOP                         
613A: 00              NOP                         
613B: 00              NOP                         
613C: 00              NOP                         
613D: 00              NOP                         
613E: 00              NOP                         
613F: 00              NOP                         
6140: 00              NOP                         
6141: 00              NOP                         
6142: 00              NOP                         
6143: 00              NOP                         
6144: 00              NOP                         
6145: 00              NOP                         
6146: 10 00           ;;STOP    $00                 
6148: 18 00           JR      $614A               ; {}
614A: 16 08           LD      D,$08               
614C: 3F              CCF                         
614D: 1E 7F           LD      E,$7F               
614F: 3A              LD      A,(HLD)             
6150: EF              RST     0X28                
6151: 7E              LD      A,(HL)              
6152: 82              ADD     A,D                 
6153: 7C              LD      A,H                 
6154: 7C              LD      A,H                 
6155: 00              NOP                         
6156: 00              NOP                         
6157: 00              NOP                         
6158: 00              NOP                         
6159: 00              NOP                         
615A: 00              NOP                         
615B: 00              NOP                         
615C: 00              NOP                         
615D: 00              NOP                         
615E: 00              NOP                         
615F: 00              NOP                         
6160: 80              ADD     A,B                 
6161: 00              NOP                         
6162: 80              ADD     A,B                 
6163: 00              NOP                         
6164: 40              LD      B,B                 
6165: 00              NOP                         
6166: 40              LD      B,B                 
6167: 00              NOP                         
6168: 60              LD      H,B                 
6169: 00              NOP                         
616A: 60              LD      H,B                 
616B: 00              NOP                         
616C: 60              LD      H,B                 
616D: 00              NOP                         
616E: 60              LD      H,B                 
616F: 00              NOP                         
6170: 30 00           JR      NC,$6172            ; {}
6172: 30 00           JR      NC,$6174            ; {}
6174: 30 00           JR      NC,$6176            ; {}
6176: 3C              INC     A                   
6177: 00              NOP                         
6178: 3E 0C           LD      A,$0C               
617A: 3E 0C           LD      A,$0C               
617C: 3C              INC     A                   
617D: 00              NOP                         
617E: 30 00           JR      NC,$6180            ; {}
6180: 00              NOP                         
6181: 00              NOP                         
6182: 00              NOP                         
6183: 00              NOP                         
6184: 00              NOP                         
6185: 00              NOP                         
6186: 00              NOP                         
6187: 00              NOP                         
6188: 00              NOP                         
6189: 00              NOP                         
618A: 00              NOP                         
618B: 00              NOP                         
618C: 00              NOP                         
618D: 00              NOP                         
618E: 00              NOP                         
618F: 00              NOP                         
6190: 00              NOP                         
6191: 00              NOP                         
6192: 00              NOP                         
6193: 00              NOP                         
6194: 00              NOP                         
6195: 00              NOP                         
6196: 0F              RRCA                        
6197: 00              NOP                         
6198: 3F              CCF                         
6199: 00              NOP                         
619A: C0              RET     NZ                  
619B: 00              NOP                         
619C: 00              NOP                         
619D: 00              NOP                         
619E: 00              NOP                         
619F: 00              NOP                         
61A0: 00              NOP                         
61A1: 00              NOP                         
61A2: 00              NOP                         
61A3: 00              NOP                         
61A4: 00              NOP                         
61A5: 00              NOP                         
61A6: 00              NOP                         
61A7: 00              NOP                         
61A8: 00              NOP                         
61A9: 00              NOP                         
61AA: 00              NOP                         
61AB: 00              NOP                         
61AC: 00              NOP                         
61AD: 00              NOP                         
61AE: 0C              INC     C                   
61AF: 00              NOP                         
61B0: 1E 0C           LD      E,$0C               
61B2: 1E 0C           LD      E,$0C               
61B4: FF              RST     0X38                
61B5: 00              NOP                         
61B6: FF              RST     0X38                
61B7: 00              NOP                         
61B8: 00              NOP                         
61B9: 00              NOP                         
61BA: 00              NOP                         
61BB: 00              NOP                         
61BC: 00              NOP                         
61BD: 00              NOP                         
61BE: 00              NOP                         
61BF: 00              NOP                         
61C0: 00              NOP                         
61C1: 00              NOP                         
61C2: 00              NOP                         
61C3: 00              NOP                         
61C4: 00              NOP                         
61C5: 00              NOP                         
61C6: 00              NOP                         
61C7: 00              NOP                         
61C8: 00              NOP                         
61C9: 00              NOP                         
61CA: 00              NOP                         
61CB: 00              NOP                         
61CC: 1C              INC     E                   
61CD: 00              NOP                         
61CE: 07              RLCA                        
61CF: 00              NOP                         
61D0: 01 00 00        LD      BC,$0000            
61D3: 00              NOP                         
61D4: 00              NOP                         
61D5: 00              NOP                         
61D6: 00              NOP                         
61D7: 00              NOP                         
61D8: 00              NOP                         
61D9: 00              NOP                         
61DA: 00              NOP                         
61DB: 00              NOP                         
61DC: 00              NOP                         
61DD: 00              NOP                         
61DE: 00              NOP                         
61DF: 00              NOP                         
61E0: 00              NOP                         
61E1: 00              NOP                         
61E2: 00              NOP                         
61E3: 00              NOP                         
61E4: 00              NOP                         
61E5: 00              NOP                         
61E6: 00              NOP                         
61E7: 00              NOP                         
61E8: 00              NOP                         
61E9: 00              NOP                         
61EA: 00              NOP                         
61EB: 00              NOP                         
61EC: 00              NOP                         
61ED: 00              NOP                         
61EE: 00              NOP                         
61EF: 00              NOP                         
61F0: C0              RET     NZ                  
61F1: 00              NOP                         
61F2: E0 00           LD      ($FF00+$00),A       
61F4: 76              HALT                        
61F5: 00              NOP                         
61F6: 3F              CCF                         
61F7: 06 1F           LD      B,$1F               
61F9: 06 0E           LD      B,$0E               
61FB: 00              NOP                         
61FC: 07              RLCA                        
61FD: 00              NOP                         
61FE: 03              INC     BC                  
61FF: 00              NOP                         
6200: 1C              INC     E                   
6201: 00              NOP                         
6202: 3A              LD      A,(HLD)             
6203: 1C              INC     E                   
6204: 29              ADD     HL,HL               
6205: 1E 11           LD      E,$11               
6207: 0E 39           LD      C,$39               
6209: 1E 1B           LD      E,$1B               
620B: 0C              INC     C                   
620C: 17              RLA                         
620D: 08 1F 00        LD      ($001F),SP          
6210: 0B              DEC     BC                  
6211: 04              INC     B                   
6212: 08 07 04        LD      ($0407),SP          
6215: 03              INC     BC                  
6216: 07              RLCA                        
6217: 00              NOP                         
6218: 07              RLCA                        
6219: 00              NOP                         
621A: 0D              DEC     C                   
621B: 06 0B           LD      B,$0B               
621D: 04              INC     B                   
621E: 0F              RRCA                        
621F: 00              NOP                         
6220: 3C              INC     A                   
6221: 00              NOP                         
6222: 42              LD      B,D                 
6223: 3C              INC     A                   
6224: 99              SBC     C                   
6225: 66              LD      H,(HL)              
6226: BD              CP      L                   
6227: 42              LD      B,D                 
6228: 3C              INC     A                   
6229: C3 18 E7        JP      $E718               
622C: 81              ADD     A,C                 
622D: 7E              LD      A,(HL)              
622E: 81              ADD     A,C                 
622F: 7E              LD      A,(HL)              
6230: 00              NOP                         
6231: FF              RST     0X38                
6232: 42              LD      B,D                 
6233: BD              CP      L                   
6234: FF              RST     0X38                
6235: 42              LD      B,D                 
6236: FF              RST     0X38                
6237: 3C              INC     A                   
6238: BD              CP      L                   
6239: 7E              LD      A,(HL)              
623A: DB                              
623B: 3C              INC     A                   
623C: BD              CP      L                   
623D: 00              NOP                         
623E: 00              NOP                         
623F: 00              NOP                         
6240: 00              NOP                         
6241: 00              NOP                         
6242: 30 00           JR      NC,$6244            ; {}
6244: 78              LD      A,B                 
6245: 30 5C           JR      NC,$62A3            ; {}
6247: 38 EB           JR      C,$6234             ; {}
6249: 5C              LD      E,H                 
624A: BB              CP      E                   
624B: 7C              LD      A,H                 
624C: 57              LD      D,A                 
624D: 38 EF           JR      C,$623E             ; {}
624F: 50              LD      D,B                 
6250: BB              CP      E                   
6251: 74              LD      (HL),H              
6252: 48              LD      C,B                 
6253: 37              SCF                         
6254: 24              INC     H                   
6255: 1B              DEC     DE                  
6256: 1F              RRA                         
6257: 00              NOP                         
6258: 07              RLCA                        
6259: 00              NOP                         
625A: 0D              DEC     C                   
625B: 06 0B           LD      B,$0B               
625D: 04              INC     B                   
625E: 0F              RRCA                        
625F: 00              NOP                         
6260: 00              NOP                         
6261: 00              NOP                         
6262: 00              NOP                         
6263: 00              NOP                         
6264: 00              NOP                         
6265: 00              NOP                         
6266: 00              NOP                         
6267: 00              NOP                         
6268: 0D              DEC     C                   
6269: 00              NOP                         
626A: 1F              RRA                         
626B: 0C              INC     C                   
626C: 3F              CCF                         
626D: 18 37           JR      $62A6               ; {}
626F: 18 73           JR      $62E4               ; {}
6271: 1C              INC     E                   
6272: 72              LD      (HL),D              
6273: 2D              DEC     L                   
6274: 72              LD      (HL),D              
6275: 1D              DEC     E                   
6276: 57              LD      D,A                 
6277: 28 25           JR      Z,$629E             ; {}
6279: 1A              LD      A,(DE)              
627A: 17              RLA                         
627B: 08 0F 00        LD      ($000F),SP          
627E: 00              NOP                         
627F: 00              NOP                         
6280: 1C              INC     E                   
6281: 00              NOP                         
6282: 13              INC     DE                  
6283: 0C              INC     C                   
6284: 18 07           JR      $628D               ; {}
6286: 1C              INC     E                   
6287: 0B              DEC     BC                  
6288: 3E 1D           LD      A,$1D               
628A: 3F              CCF                         
628B: 18 3E           JR      $62CB               ; {}
628D: 19              ADD     HL,DE               
628E: 2F              CPL                         
628F: 1E 37           LD      E,$37               
6291: 0D              DEC     C                   
6292: 5F              LD      E,A                 
6293: 21 56 2D        LD      HL,$2D56            
6296: 57              LD      D,A                 
6297: 2E 4B           LD      L,$4B               
6299: 37              SCF                         
629A: 3C              INC     A                   
629B: 03              INC     BC                  
629C: 37              SCF                         
629D: 1C              INC     E                   
629E: 3F              CCF                         
629F: 00              NOP                         
62A0: 1C              INC     E                   
62A1: 00              NOP                         
62A2: 13              INC     DE                  
62A3: 0C              INC     C                   
62A4: 18 07           JR      $62AD               ; {}
62A6: 14              INC     D                   
62A7: 0B              DEC     BC                  
62A8: 22              LD      (HLI),A             
62A9: 1D              DEC     E                   
62AA: 21 1E 3E        LD      HL,$3E1E            
62AD: 01 21 1E        LD      BC,$1E21            
62B0: 33              INC     SP                  
62B1: 0D              DEC     C                   
62B2: 5F              LD      E,A                 
62B3: 21 56 2D        LD      HL,$2D56            
62B6: 57              LD      D,A                 
62B7: 2E 4B           LD      L,$4B               
62B9: 37              SCF                         
62BA: 3C              INC     A                   
62BB: 03              INC     BC                  
62BC: 37              SCF                         
62BD: 1C              INC     E                   
62BE: 3F              CCF                         
62BF: 00              NOP                         
62C0: 00              NOP                         
62C1: 00              NOP                         
62C2: 00              NOP                         
62C3: 00              NOP                         
62C4: 00              NOP                         
62C5: 00              NOP                         
62C6: 07              RLCA                        
62C7: 00              NOP                         
62C8: 08 07 08        LD      ($0807),SP          
62CB: 07              RLCA                        
62CC: 07              RLCA                        
62CD: 00              NOP                         
62CE: 03              INC     BC                  
62CF: 01 01 00        LD      BC,$0001            
62D2: 00              NOP                         
62D3: 00              NOP                         
62D4: 00              NOP                         
62D5: 00              NOP                         
62D6: 00              NOP                         
62D7: 00              NOP                         
62D8: 00              NOP                         
62D9: 00              NOP                         
62DA: 00              NOP                         
62DB: 00              NOP                         
62DC: 00              NOP                         
62DD: 00              NOP                         
62DE: 00              NOP                         
62DF: 00              NOP                         
62E0: 1C              INC     E                   
62E1: 00              NOP                         
62E2: 13              INC     DE                  
62E3: 0C              INC     C                   
62E4: 18 07           JR      $62ED               ; {}
62E6: 9C              SBC     H                   
62E7: 0B              DEC     BC                  
62E8: 7E              LD      A,(HL)              
62E9: 9D              SBC     L                   
62EA: 3F              CCF                         
62EB: D8              RET     C                   
62EC: BE              CP      (HL)                
62ED: D9              RETI                        
62EE: EF              RST     0X28                
62EF: DE F7           SBC     $F7                 
62F1: 6D              LD      L,L                 
62F2: 5F              LD      E,A                 
62F3: 31 3E 1D        LD      SP,$1D3E            
62F6: 2F              CPL                         
62F7: 1E 17           LD      E,$17               
62F9: 0F              RRCA                        
62FA: 1C              INC     E                   
62FB: 03              INC     BC                  
62FC: 37              SCF                         
62FD: 1C              INC     E                   
62FE: 3F              CCF                         
62FF: 00              NOP                         
6300: 00              NOP                         
6301: 00              NOP                         
6302: 00              NOP                         
6303: 00              NOP                         
6304: 00              NOP                         
6305: 00              NOP                         
6306: 01 00 1F        LD      BC,$1F00            
6309: 00              NOP                         
630A: 7F              LD      A,A                 
630B: 00              NOP                         
630C: FF              RST     0X38                
630D: 00              NOP                         
630E: FF              RST     0X38                
630F: 00              NOP                         
6310: F0 0F           LD      A,($0F)             
6312: 7F              LD      A,A                 
6313: 05              DEC     B                   
6314: 3F              CCF                         
6315: 0D              DEC     C                   
6316: 3F              CCF                         
6317: 1F              RRA                         
6318: 7F              LD      A,A                 
6319: 3F              CCF                         
631A: 7F              LD      A,A                 
631B: 37              SCF                         
631C: 70              LD      (HL),B              
631D: 0F              RRCA                        
631E: BF              CP      A                   
631F: 70              LD      (HL),B              
6320: 00              NOP                         
6321: 00              NOP                         
6322: 00              NOP                         
6323: 00              NOP                         
6324: F8 00           LD      HL,SP+$00           
6326: 8C              ADC     A,H                 
6327: 70              LD      (HL),B              
6328: 7E              LD      A,(HL)              
6329: 80              ADD     A,B                 
632A: FE 00           CP      $00                 
632C: F0 00           LD      A,($00)             
632E: F8 00           LD      HL,SP+$00           
6330: FC                              
6331: 00              NOP                         
6332: 7C              LD      A,H                 
6333: 80              ADD     A,B                 
6334: DC A0 C8        CALL    C,$C8A0             
6337: B0              OR      B                   
6338: 44              LD      B,H                 
6339: B8              CP      B                   
633A: 44              LD      B,H                 
633B: B8              CP      B                   
633C: C4 38 E8        CALL    NZ,$E838            
633F: 10 BF           ;;STOP    $BF                 
6341: 60              LD      H,B                 
6342: 7F              LD      A,A                 
6343: 18 5F           JR      $63A4               ; {}
6345: 30 F3           JR      NC,$633A            ; {}
6347: 0C              INC     C                   
6348: F7              RST     0X30                
6349: 4E              LD      C,(HL)              
634A: EB                              
634B: 17              RLA                         
634C: 3D              DEC     A                   
634D: 13              INC     DE                  
634E: 2F              CPL                         
634F: 18 57           JR      $63A8               ; {}
6351: 2F              CPL                         
6352: 4F              LD      C,A                 
6353: 30 43           JR      NC,$6398            ; {}
6355: 3F              CCF                         
6356: 60              LD      H,B                 
6357: 1F              RRA                         
6358: 6C              LD      L,H                 
6359: 13              INC     DE                  
635A: 3E 01           LD      A,$01               
635C: 0F              RRCA                        
635D: 10 00           ;;STOP    $00                 
635F: 00              NOP                         
6360: FE 00           CP      $00                 
6362: FF              RST     0X38                
6363: 02              LD      (BC),A              
6364: FF              RST     0X38                
6365: 02              LD      (BC),A              
6366: 7F              LD      A,A                 
6367: F6 EF           OR      $EF                 
6369: 18 FE           JR      $6369               ; {}
636B: 08 FC 08        LD      ($08FC),SP          
636E: F4                              
636F: 18 EA           JR      $635B               ; {}
6371: F4                              
6372: F2                              
6373: 0C              INC     C                   
6374: C2 FC 06        JP      NZ,$06FC            
6377: F8 36           LD      HL,SP+$36           
6379: C8              RET     Z                   
637A: 7C              LD      A,H                 
637B: 80              ADD     A,B                 
637C: F0 08           LD      A,($08)             
637E: 00              NOP                         
637F: 00              NOP                         
6380: 00              NOP                         
6381: 00              NOP                         
6382: 01 00 03        LD      BC,$0300            
6385: 00              NOP                         
6386: 03              INC     BC                  
6387: 00              NOP                         
6388: 03              INC     BC                  
6389: 00              NOP                         
638A: 1F              RRA                         
638B: 00              NOP                         
638C: 7F              LD      A,A                 
638D: 00              NOP                         
638E: FF              RST     0X38                
638F: 00              NOP                         
6390: F7              RST     0X30                
6391: 0B              DEC     BC                  
6392: EF              RST     0X28                
6393: 15              DEC     D                   
6394: 6F              LD      L,A                 
6395: 15              DEC     D                   
6396: 4F              LD      C,A                 
6397: 37              SCF                         
6398: 4B              LD      C,E                 
6399: 37              SCF                         
639A: 4F              LD      C,A                 
639B: 33              INC     SP                  
639C: 4D              LD      C,L                 
639D: 33              INC     SP                  
639E: 3F              CCF                         
639F: 00              NOP                         
63A0: 00              NOP                         
63A1: 00              NOP                         
63A2: E0 00           LD      ($FF00+$00),A       
63A4: 70              LD      (HL),B              
63A5: 80              ADD     A,B                 
63A6: 70              LD      (HL),B              
63A7: 80              ADD     A,B                 
63A8: 60              LD      H,B                 
63A9: 80              ADD     A,B                 
63AA: F8 00           LD      HL,SP+$00           
63AC: FE 00           CP      $00                 
63AE: FF              RST     0X38                
63AF: 00              NOP                         
63B0: AF              XOR     A                   
63B1: D0              RET     NC                  
63B2: F7              RST     0X30                
63B3: A8              XOR     B                   
63B4: F2                              
63B5: AC              XOR     H                   
63B6: F3              DI                          
63B7: EC                              
63B8: 91              SUB     C                   
63B9: EE E1           XOR     $E1                 
63BB: 9E              SBC     (HL)                
63BC: 61              LD      H,C                 
63BD: 9E              SBC     (HL)                
63BE: F2                              
63BF: 0C              INC     C                   
63C0: 3F              CCF                         
63C1: 07              RLCA                        
63C2: 3F              CCF                         
63C3: 0E 7F           LD      C,$7F               
63C5: 0D              DEC     C                   
63C6: FF              RST     0X38                
63C7: 40              LD      B,B                 
63C8: F5              PUSH    AF                  
63C9: 5B              LD      E,E                 
63CA: FD                              
63CB: 13              INC     DE                  
63CC: 3E 11           LD      A,$11               
63CE: 2F              CPL                         
63CF: 18 57           JR      $6428               ; {}
63D1: 2F              CPL                         
63D2: 4F              LD      C,A                 
63D3: 30 43           JR      NC,$6418            ; {}
63D5: 3F              CCF                         
63D6: 60              LD      H,B                 
63D7: 1F              RRA                         
63D8: 6C              LD      L,H                 
63D9: 13              INC     DE                  
63DA: 3E 01           LD      A,$01               
63DC: 0F              RRCA                        
63DD: 10 00           ;;STOP    $00                 
63DF: 00              NOP                         
63E0: FC                              
63E1: 00              NOP                         
63E2: FC                              
63E3: C0              RET     NZ                  
63E4: BE              CP      (HL)                
63E5: C0              RET     NZ                  
63E6: DF              RST     0X18                
63E7: 32              LD      (HLD),A             
63E8: 6F              LD      L,A                 
63E9: 9A              SBC     D                   
63EA: 7F              LD      A,A                 
63EB: 88              ADC     A,B                 
63EC: FC                              
63ED: 08 F4 18        LD      ($18F4),SP          
63F0: EA F4 F2        LD      ($F2F4),A           
63F3: 0C              INC     C                   
63F4: C2 FC 06        JP      NZ,$06FC            
63F7: F8 36           LD      HL,SP+$36           
63F9: C8              RET     Z                   
63FA: 7C              LD      A,H                 
63FB: 80              ADD     A,B                 
63FC: F0 08           LD      A,($08)             
63FE: 00              NOP                         
63FF: 00              NOP                         
6400: 07              RLCA                        
6401: 00              NOP                         
6402: 1E 01           LD      E,$01               
6404: 3F              CCF                         
6405: 00              NOP                         
6406: 7F              LD      A,A                 
6407: 00              NOP                         
6408: 7F              LD      A,A                 
6409: 20 FF           JR      NZ,$640A            ; {}
640B: 50              LD      D,B                 
640C: FF              RST     0X38                
640D: 50              LD      D,B                 
640E: FF              RST     0X38                
640F: 20 FF           JR      NZ,$6410            ; {}
6411: 00              NOP                         
6412: BF              CP      A                   
6413: 40              LD      B,B                 
6414: FF              RST     0X38                
6415: 30 77           JR      NC,$648E            ; {}
6417: 3E 7E           LD      A,$7E               
6419: 17              RLA                         
641A: 3F              CCF                         
641B: 02              LD      (BC),A              
641C: 1F              RRA                         
641D: 00              NOP                         
641E: 07              RLCA                        
641F: 00              NOP                         
6420: 07              RLCA                        
6421: 00              NOP                         
6422: 1E 01           LD      E,$01               
6424: 3F              CCF                         
6425: 00              NOP                         
6426: 7F              LD      A,A                 
6427: 20 7F           JR      NZ,$64A8            ; {}
6429: 10 FF           ;;STOP    $FF                 
642B: 50              LD      D,B                 
642C: FF              RST     0X38                
642D: 20 FE           JR      NZ,$642D            ; {}
642F: 07              RLCA                        
6430: F7              RST     0X30                
6431: 1E FF           LD      E,$FF               
6433: 32              LD      (HLD),A             
6434: BF              CP      A                   
6435: 50              LD      D,B                 
6436: 5F              LD      E,A                 
6437: 20 5F           JR      NZ,$6498            ; {}
6439: 20 27           JR      NZ,$6462            ; {}
643B: 18 19           JR      $6456               ; {}
643D: 07              RLCA                        
643E: 07              RLCA                        
643F: 00              NOP                         
6440: 07              RLCA                        
6441: 00              NOP                         
6442: 1E 01           LD      E,$01               
6444: 3F              CCF                         
6445: 00              NOP                         
6446: 7F              LD      A,A                 
6447: 00              NOP                         
6448: 7F              LD      A,A                 
6449: 00              NOP                         
644A: FF              RST     0X38                
644B: 01 FF 01        LD      BC,$01FF            
644E: FF              RST     0X38                
644F: 40              LD      B,B                 
6450: FF              RST     0X38                
6451: 60              LD      H,B                 
6452: FF              RST     0X38                
6453: 58              LD      E,B                 
6454: FF              RST     0X38                
6455: 13              INC     DE                  
6456: 7F              LD      A,A                 
6457: 02              LD      (BC),A              
6458: 7F              LD      A,A                 
6459: 00              NOP                         
645A: 3F              CCF                         
645B: 00              NOP                         
645C: 1F              RRA                         
645D: 00              NOP                         
645E: 07              RLCA                        
645F: 00              NOP                         
6460: E0 00           LD      ($FF00+$00),A       
6462: 78              LD      A,B                 
6463: 80              ADD     A,B                 
6464: FC                              
6465: 00              NOP                         
6466: FE 00           CP      $00                 
6468: FE C0           CP      $C0                 
646A: FF              RST     0X38                
646B: 20 FF           JR      NZ,$646C            ; {}
646D: 20 FF           JR      NZ,$646E            ; {}
646F: C0              RET     NZ                  
6470: FF              RST     0X38                
6471: 00              NOP                         
6472: FF              RST     0X38                
6473: 00              NOP                         
6474: BF              CP      A                   
6475: 40              LD      B,B                 
6476: FE 00           CP      $00                 
6478: FE 00           CP      $00                 
647A: FC                              
647B: 00              NOP                         
647C: F8 00           LD      HL,SP+$00           
647E: E0 00           LD      ($FF00+$00),A       
6480: 07              RLCA                        
6481: 00              NOP                         
6482: 1E 01           LD      E,$01               
6484: 3F              CCF                         
6485: 00              NOP                         
6486: 7F              LD      A,A                 
6487: 00              NOP                         
6488: FF              RST     0X38                
6489: 60              LD      H,B                 
648A: FF              RST     0X38                
648B: 50              LD      D,B                 
648C: FF              RST     0X38                
648D: 58              LD      E,B                 
648E: 7F              LD      A,A                 
648F: 1C              INC     E                   
6490: 3F              CCF                         
6491: 02              LD      (BC),A              
6492: 5F              LD      E,A                 
6493: 23              INC     HL                  
6494: FF              RST     0X38                
6495: 40              LD      B,B                 
6496: FC                              
6497: 43              LD      B,E                 
6498: 7B              LD      A,E                 
6499: 3C              INC     A                   
649A: 3F              CCF                         
649B: 00              NOP                         
649C: 1F              RRA                         
649D: 00              NOP                         
649E: 07              RLCA                        
649F: 00              NOP                         
64A0: E0 00           LD      ($FF00+$00),A       
64A2: 78              LD      A,B                 
64A3: 80              ADD     A,B                 
64A4: FC                              
64A5: 00              NOP                         
64A6: FE 60           CP      $60                 
64A8: FE 90           CP      $90                 
64AA: FF              RST     0X38                
64AB: 90              SUB     B                   
64AC: FF              RST     0X38                
64AD: 60              LD      H,B                 
64AE: FF              RST     0X38                
64AF: 00              NOP                         
64B0: FF              RST     0X38                
64B1: 00              NOP                         
64B2: FF              RST     0X38                
64B3: 00              NOP                         
64B4: 3F              CCF                         
64B5: C0              RET     NZ                  
64B6: FE 00           CP      $00                 
64B8: FE 00           CP      $00                 
64BA: FC                              
64BB: 00              NOP                         
64BC: F8 00           LD      HL,SP+$00           
64BE: E0 00           LD      ($FF00+$00),A       
64C0: 07              RLCA                        
64C1: 00              NOP                         
64C2: 1E 01           LD      E,$01               
64C4: 3F              CCF                         
64C5: 00              NOP                         
64C6: 7F              LD      A,A                 
64C7: 00              NOP                         
64C8: 7F              LD      A,A                 
64C9: 00              NOP                         
64CA: FF              RST     0X38                
64CB: 00              NOP                         
64CC: FF              RST     0X38                
64CD: 00              NOP                         
64CE: FF              RST     0X38                
64CF: 00              NOP                         
64D0: FF              RST     0X38                
64D1: 00              NOP                         
64D2: FF              RST     0X38                
64D3: 00              NOP                         
64D4: FF              RST     0X38                
64D5: 00              NOP                         
64D6: 7F              LD      A,A                 
64D7: 00              NOP                         
64D8: 7F              LD      A,A                 
64D9: 00              NOP                         
64DA: 3F              CCF                         
64DB: 00              NOP                         
64DC: 1F              RRA                         
64DD: 00              NOP                         
64DE: 07              RLCA                        
64DF: 00              NOP                         
64E0: 00              NOP                         
64E1: 00              NOP                         
64E2: 00              NOP                         
64E3: 00              NOP                         
64E4: 00              NOP                         
64E5: 00              NOP                         
64E6: 00              NOP                         
64E7: 00              NOP                         
64E8: 00              NOP                         
64E9: 00              NOP                         
64EA: 3C              INC     A                   
64EB: 00              NOP                         
64EC: 5A              LD      E,D                 
64ED: 3C              INC     A                   
64EE: 7E              LD      A,(HL)              
64EF: 24              INC     H                   
64F0: 7E              LD      A,(HL)              
64F1: 24              INC     H                   
64F2: 5A              LD      E,D                 
64F3: 3C              INC     A                   
64F4: 3C              INC     A                   
64F5: 00              NOP                         
64F6: 00              NOP                         
64F7: 00              NOP                         
64F8: 00              NOP                         
64F9: 00              NOP                         
64FA: 00              NOP                         
64FB: 00              NOP                         
64FC: 00              NOP                         
64FD: 00              NOP                         
64FE: 00              NOP                         
64FF: 00              NOP                         
6500: 07              RLCA                        
6501: 00              NOP                         
6502: 0E 03           LD      C,$03               
6504: 3F              CCF                         
6505: 01 5F 21        LD      BC,$215F            
6508: FF              RST     0X38                
6509: 41              LD      B,C                 
650A: FE 01           CP      $01                 
650C: 3E 01           LD      A,$01               
650E: 77              LD      (HL),A              
650F: 38 FF           JR      C,$6510             ; {}
6511: 78              LD      A,B                 
6512: F7              RST     0X30                
6513: 08 1F 06        LD      ($061F),SP          
6516: 0F              RRCA                        
6517: 05              DEC     B                   
6518: 0F              RRCA                        
6519: 03              INC     BC                  
651A: 07              RLCA                        
651B: 00              NOP                         
651C: 03              INC     BC                  
651D: 00              NOP                         
651E: 00              NOP                         
651F: 00              NOP                         
6520: 3F              CCF                         
6521: 00              NOP                         
6522: FF              RST     0X38                
6523: 00              NOP                         
6524: BF              CP      A                   
6525: 40              LD      B,B                 
6526: BF              CP      A                   
6527: 40              LD      B,B                 
6528: B9              CP      C                   
6529: 46              LD      B,(HL)              
652A: 94              SUB     H                   
652B: 6F              LD      L,A                 
652C: 90              SUB     B                   
652D: 6F              LD      L,A                 
652E: F1              POP     AF                  
652F: 0E FA           LD      C,$FA               
6531: 65              LD      H,L                 
6532: F4                              
6533: DB                              
6534: E4                              
6535: DB                              
6536: E4                              
6537: 5B              LD      E,E                 
6538: F8 47           LD      HL,SP+$47           
653A: FE E1           CP      $E1                 
653C: FE 0D           CP      $0D                 
653E: 1F              RRA                         
653F: 00              NOP                         
6540: 18 00           JR      $6542               ; {}
6542: A4              AND     H                   
6543: 18 F4           JR      $6539               ; {}
6545: 08 9A 64        LD      ($649A),SP          ; {}
6548: 8F              ADC     A,A                 
6549: 70              LD      (HL),B              
654A: 8F              ADC     A,A                 
654B: 76              HALT                        
654C: 8E              ADC     A,(HL)              
654D: 70              LD      (HL),B              
654E: C8              RET     Z                   
654F: 30 08           JR      NC,$6559            ; {}
6551: F0 08           LD      A,($08)             
6553: F0 08           LD      A,($08)             
6555: F0 30           LD      A,($30)             
6557: C0              RET     NZ                  
6558: 40              LD      B,B                 
6559: 80              ADD     A,B                 
655A: 40              LD      B,B                 
655B: 80              ADD     A,B                 
655C: 40              LD      B,B                 
655D: 80              ADD     A,B                 
655E: 80              ADD     A,B                 
655F: 00              NOP                         
6560: 00              NOP                         
6561: 00              NOP                         
6562: 3F              CCF                         
6563: 00              NOP                         
6564: FF              RST     0X38                
6565: 00              NOP                         
6566: BF              CP      A                   
6567: 40              LD      B,B                 
6568: BF              CP      A                   
6569: 40              LD      B,B                 
656A: B9              CP      C                   
656B: 46              LD      B,(HL)              
656C: 94              SUB     H                   
656D: 6F              LD      L,A                 
656E: 90              SUB     B                   
656F: 6F              LD      L,A                 
6570: F1              POP     AF                  
6571: 0E F9           LD      C,$F9               
6573: 66              LD      H,(HL)              
6574: F5              PUSH    AF                  
6575: EA E9 DE        LD      ($DEE9),A           
6578: E1              POP     HL                  
6579: 5E              LD      E,(HL)              
657A: F3              DI                          
657B: 6C              LD      L,H                 
657C: FC                              
657D: E0 E0           LD      ($FF00+$E0),A       
657F: 00              NOP                         
6580: 00              NOP                         
6581: 00              NOP                         
6582: 00              NOP                         
6583: 00              NOP                         
6584: F0 00           LD      A,($00)             
6586: C8              RET     Z                   
6587: 30 C8           JR      NC,$6551            ; {}
6589: 30 C4           JR      NC,$654F            ; {}
658B: 38 E4           JR      C,$6571             ; {}
658D: 18 84           JR      $6513               ; {}
658F: 78              LD      A,B                 
6590: 06 F8           LD      B,$F8               
6592: 0A              LD      A,(BC)              
6593: F4                              
6594: 1A              LD      A,(DE)              
6595: E4                              
6596: 0A              LD      A,(BC)              
6597: F4                              
6598: 84              ADD     A,H                 
6599: 78              LD      A,B                 
659A: F2                              
659B: 0C              INC     C                   
659C: F2                              
659D: 6C              LD      L,H                 
659E: FC                              
659F: 00              NOP                         
65A0: 08 00 1C        LD      ($1C00),SP          
65A3: 08 1F 0C        LD      ($0C1F),SP          
65A6: 17              RLA                         
65A7: 0E 0B           LD      C,$0B               
65A9: 05              DEC     B                   
65AA: 07              RLCA                        
65AB: 01 67 00        LD      BC,$0067            
65AE: F4                              
65AF: 43              LD      B,E                 
65B0: AB              XOR     E                   
65B1: 56              LD      D,(HL)              
65B2: 8F              ADC     A,A                 
65B3: 75              LD      (HL),L              
65B4: 6F              LD      L,A                 
65B5: 15              DEC     D                   
65B6: FB              EI                          
65B7: 66              LD      H,(HL)              
65B8: ED                              
65B9: 53              LD      D,E                 
65BA: C7              RST     0X00                
65BB: 38 64           JR      C,$6621             ; {}
65BD: 1B              DEC     DE                  
65BE: 3F              CCF                         
65BF: 00              NOP                         
65C0: 00              NOP                         
65C1: 00              NOP                         
65C2: 7C              LD      A,H                 
65C3: 00              NOP                         
65C4: EF              RST     0X28                
65C5: 10 FF           ;;STOP    $FF                 
65C7: C3 FF A7        JP      $A7FF               
65CA: FF              RST     0X38                
65CB: E5              PUSH    HL                  
65CC: FF              RST     0X38                
65CD: D3                              
65CE: DB                              
65CF: 24              INC     H                   
65D0: 00              NOP                         
65D1: FF              RST     0X38                
65D2: FF              RST     0X38                
65D3: 00              NOP                         
65D4: FF              RST     0X38                
65D5: 82              ADD     A,D                 
65D6: FF              RST     0X38                
65D7: 76              HALT                        
65D8: FF              RST     0X38                
65D9: F9              LD      SP,HL               
65DA: BE              CP      (HL)                
65DB: 7F              LD      A,A                 
65DC: FF              RST     0X38                
65DD: 00              NOP                         
65DE: FF              RST     0X38                
65DF: 00              NOP                         
65E0: 00              NOP                         
65E1: 00              NOP                         
65E2: 10 00           ;;STOP    $00                 
65E4: 38 10           JR      C,$65F6             ; {}
65E6: F8 30           LD      HL,SP+$30           
65E8: E8 B0           ADD     SP,$B0              
65EA: D0              RET     NC                  
65EB: A0              AND     B                   
65EC: EC                              
65ED: 00              NOP                         
65EE: 7E              LD      A,(HL)              
65EF: 84              ADD     A,H                 
65F0: AA              XOR     D                   
65F1: D4 E2 DC        CALL    NC,$DCE2            
65F4: E6 D8           AND     $D8                 
65F6: BF              CP      A                   
65F7: C6 77           ADD     $77                 
65F9: 8A              ADC     A,D                 
65FA: E3                              
65FB: 1C              INC     E                   
65FC: 26 D8           LD      H,$D8               
65FE: FC                              
65FF: 00              NOP                         
6600: 00              NOP                         
6601: 00              NOP                         
6602: 3F              CCF                         
6603: 00              NOP                         
6604: 21 1F 21        LD      HL,$211F            
6607: 1F              RRA                         
6608: 21 1F 21        LD      HL,$211F            
660B: 1F              RRA                         
660C: 3F              CCF                         
660D: 1F              RRA                         
660E: 3F              CCF                         
660F: 1F              RRA                         
6610: 21 1F 21        LD      HL,$211F            
6613: 1F              RRA                         
6614: 21 1F 21        LD      HL,$211F            
6617: 1F              RRA                         
6618: 3F              CCF                         
6619: 00              NOP                         
661A: 3F              CCF                         
661B: 00              NOP                         
661C: 00              NOP                         
661D: 00              NOP                         
661E: 00              NOP                         
661F: 00              NOP                         
6620: 01 00 02        LD      BC,$0200            
6623: 01 04 03        LD      BC,$0304            
6626: 08 07 1C        LD      ($1C07),SP          
6629: 0F              RRCA                        
662A: 26 1F           LD      H,$1F               
662C: 43              LD      B,E                 
662D: 3F              CCF                         
662E: 81              ADD     A,C                 
662F: 7F              LD      A,A                 
6630: C3 3F 66        JP      $663F               ; {}
6633: 1F              RRA                         
6634: 3C              INC     A                   
6635: 0F              RRCA                        
6636: 1C              INC     E                   
6637: 07              RLCA                        
6638: 0C              INC     C                   
6639: 03              INC     BC                  
663A: 06 01           LD      B,$01               
663C: 03              INC     BC                  
663D: 00              NOP                         
663E: 01 00 03        LD      BC,$0300            
6641: 00              NOP                         
6642: 02              LD      (BC),A              
6643: 01 03 00        LD      BC,$0003            
6646: 02              LD      (BC),A              
6647: 01 0F 01        LD      BC,$010F            
664A: 1B              DEC     DE                  
664B: 0D              DEC     C                   
664C: 2E 11           LD      L,$11               
664E: 5A              LD      E,D                 
664F: 21 B2 41        LD      HL,$41B2            
6652: A2              AND     D                   
6653: 41              LD      B,C                 
6654: A2              AND     D                   
6655: 41              LD      B,C                 
6656: A2              AND     D                   
6657: 41              LD      B,C                 
6658: BE              CP      (HL)                
6659: 41              LD      B,C                 
665A: 87              ADD     A,A                 
665B: 7D              LD      A,L                 
665C: FE 01           CP      $01                 
665E: 7F              LD      A,A                 
665F: 00              NOP                         
6660: 02              LD      (BC),A              
6661: 01 02 01        LD      BC,$0102            
6664: 02              LD      (BC),A              
6665: 01 02 01        LD      BC,$0102            
6668: 02              LD      (BC),A              
6669: 01 02 01        LD      BC,$0102            
666C: 02              LD      (BC),A              
666D: 01 02 01        LD      BC,$0102            
6670: 02              LD      (BC),A              
6671: 01 02 01        LD      BC,$0102            
6674: 02              LD      (BC),A              
6675: 01 02 01        LD      BC,$0102            
6678: 02              LD      (BC),A              
6679: 01 02 01        LD      BC,$0102            
667C: 02              LD      (BC),A              
667D: 01 02 01        LD      BC,$0102            
6680: 00              NOP                         
6681: 00              NOP                         
6682: E7              RST     0X20                
6683: 00              NOP                         
6684: FB              EI                          
6685: 67              LD      H,A                 
6686: 97              SUB     A                   
6687: 7F              LD      A,A                 
6688: 9F              SBC     A                   
6689: 6E              LD      L,(HL)              
668A: AF              XOR     A                   
668B: 5D              LD      E,L                 
668C: AE              XOR     (HL)                
668D: 5D              LD      E,L                 
668E: AF              XOR     A                   
668F: 5E              LD      E,(HL)              
6690: B7              OR      A                   
6691: 4F              LD      C,A                 
6692: BB              CP      E                   
6693: 57              LD      D,A                 
6694: BD              CP      L                   
6695: 53              LD      D,E                 
6696: 6C              LD      L,H                 
6697: 1B              DEC     DE                  
6698: F5              PUSH    AF                  
6699: 4B              LD      C,E                 
669A: FD                              
669B: 63              LD      H,E                 
669C: BC              CP      H                   
669D: 7B              LD      A,E                 
669E: 7D              LD      A,L                 
669F: 3B              DEC     SP                  
66A0: DD                              
66A1: 3B              DEC     SP                  
66A2: A4              AND     H                   
66A3: 5B              LD      E,E                 
66A4: BD              CP      L                   
66A5: 43              LD      B,E                 
66A6: A5              AND     L                   
66A7: 5B              LD      E,E                 
66A8: A4              AND     H                   
66A9: 5B              LD      E,E                 
66AA: A5              AND     L                   
66AB: 5B              LD      E,E                 
66AC: A5              AND     L                   
66AD: 5B              LD      E,E                 
66AE: C4 3B C5        CALL    NZ,$C53B            
66B1: 3B              DEC     SP                  
66B2: C5              PUSH    BC                  
66B3: 3B              DEC     SP                  
66B4: FC                              
66B5: 43              LD      B,E                 
66B6: BD              CP      L                   
66B7: 5B              LD      E,E                 
66B8: EC                              
66B9: 1B              DEC     DE                  
66BA: FE 41           CP      $41                 
66BC: FD                              
66BD: 7E              LD      A,(HL)              
66BE: 7F              LD      A,A                 
66BF: 00              NOP                         
66C0: 03              INC     BC                  
66C1: 03              INC     BC                  
66C2: 0C              INC     C                   
66C3: 0F              RRCA                        
66C4: 13              INC     DE                  
66C5: 1C              INC     E                   
66C6: 2F              CPL                         
66C7: 30 2F           JR      NC,$66F8            ; {}
66C9: 30 5C           JR      NC,$6727            ; {}
66CB: 63              LD      H,E                 
66CC: 59              LD      E,C                 
66CD: 67              LD      H,A                 
66CE: 59              LD      E,C                 
66CF: 67              LD      H,A                 
66D0: 59              LD      E,C                 
66D1: 66              LD      H,(HL)              
66D2: 59              LD      E,C                 
66D3: 66              LD      H,(HL)              
66D4: 2C              INC     L                   
66D5: 33              INC     SP                  
66D6: 2F              CPL                         
66D7: 30 13           JR      NC,$66EC            ; {}
66D9: 1C              INC     E                   
66DA: 0C              INC     C                   
66DB: 0F              RRCA                        
66DC: 03              INC     BC                  
66DD: 03              INC     BC                  
66DE: 00              NOP                         
66DF: 00              NOP                         
66E0: 00              NOP                         
66E1: 0C              INC     C                   
66E2: 45              LD      B,L                 
66E3: 0B              DEC     BC                  
66E4: 16 19           LD      D,$19               
66E6: 37              SCF                         
66E7: 38 0F           JR      C,$66F8             ; {}
66E9: F0 7C           LD      A,($7C)             
66EB: 83              ADD     A,E                 
66EC: 39              ADD     HL,SP               
66ED: 47              LD      B,A                 
66EE: 59              LD      E,C                 
66EF: 67              LD      H,A                 
66F0: D9              RETI                        
66F1: 66              LD      H,(HL)              
66F2: 59              LD      E,C                 
66F3: 66              LD      H,(HL)              
66F4: 3C              INC     A                   
66F5: 43              LD      B,E                 
66F6: 7F              LD      A,A                 
66F7: 80              ADD     A,B                 
66F8: 0F              RRCA                        
66F9: F0 36           LD      A,($36)             
66FB: 39              ADD     HL,SP               
66FC: 55              LD      D,L                 
66FD: 1B              DEC     DE                  
66FE: 00              NOP                         
66FF: 0C              INC     C                   
6700: 07              RLCA                        
6701: 00              NOP                         
6702: 1F              RRA                         
6703: 00              NOP                         
6704: 3F              CCF                         
6705: 1C              INC     E                   
6706: 7F              LD      A,A                 
6707: 3E 7F           LD      A,$7F               
6709: 26 DD           LD      H,$DD               
670B: 2E E3           LD      L,$E3               
670D: 1C              INC     E                   
670E: FF              RST     0X38                
670F: 03              INC     BC                  
6710: CF              RST     0X08                
6711: 3F              CCF                         
6712: BE              CP      (HL)                
6713: 7F              LD      A,A                 
6714: BD              CP      L                   
6715: 7E              LD      A,(HL)              
6716: C2 3D 7C        JP      NZ,$7C3D            ; {}
6719: 03              INC     BC                  
671A: 7F              LD      A,A                 
671B: 00              NOP                         
671C: BD              CP      L                   
671D: 7E              LD      A,(HL)              
671E: FF              RST     0X38                
671F: 00              NOP                         
6720: C0              RET     NZ                  
6721: 00              NOP                         
6722: F0 00           LD      A,($00)             
6724: F8 00           LD      HL,SP+$00           
6726: F8 00           LD      HL,SP+$00           
6728: F4                              
6729: 08 6C F0        LD      ($F06C),SP          
672C: F2                              
672D: 0C              INC     C                   
672E: 6A              LD      L,D                 
672F: 9C              SBC     H                   
6730: FA FC FA        LD      A,($FAFC)           
6733: FC                              
6734: F2                              
6735: FC                              
6736: E7              RST     0X20                
6737: F8 0F           LD      HL,SP+$0F           
6739: F6 FD           OR      $FD                 
673B: 0E FB           LD      C,$FB               
673D: 3C              INC     A                   
673E: FE 00           CP      $00                 
6740: 07              RLCA                        
6741: 00              NOP                         
6742: 1F              RRA                         
6743: 00              NOP                         
6744: 3F              CCF                         
6745: 0E 7F           LD      C,$7F               
6747: 1F              RRA                         
6748: 7F              LD      A,A                 
6749: 13              INC     DE                  
674A: EE 17           XOR     $17                 
674C: F1              POP     AF                  
674D: 0E FF           LD      C,$FF               
674F: 31 F7 6F        LD      SP,$6FF7            
6752: F7              RST     0X30                
6753: 6F              LD      L,A                 
6754: F6 6F           OR      $6F                 
6756: B9              CP      C                   
6757: 76              HALT                        
6758: 46              LD      B,(HL)              
6759: 39              ADD     HL,SP               
675A: 7F              LD      A,A                 
675B: 00              NOP                         
675C: 0B              DEC     BC                  
675D: 07              RLCA                        
675E: 0F              RRCA                        
675F: 00              NOP                         
6760: C0              RET     NZ                  
6761: 00              NOP                         
6762: F0 00           LD      A,($00)             
6764: F8 00           LD      HL,SP+$00           
6766: F8 00           LD      HL,SP+$00           
6768: F4                              
6769: 08 EC 70        LD      ($70EC),SP          ; {}
676C: FA 04 B2        LD      A,($B204)           
676F: CC FA FC        CALL    Z,$FCFA             
6772: 7A              LD      A,D                 
6773: FC                              
6774: F2                              
6775: 7C              LD      A,H                 
6776: E4                              
6777: F8 08           LD      HL,SP+$08           
6779: F0 F8           LD      A,($F8)             
677B: 00              NOP                         
677C: E8 F0           ADD     SP,$F0              
677E: F8 00           LD      HL,SP+$00           
6780: 0F              RRCA                        
6781: 00              NOP                         
6782: 3F              CCF                         
6783: 00              NOP                         
6784: 7F              LD      A,A                 
6785: 11 7F 3B        LD      DE,$3B7F            
6788: FF              RST     0X38                
6789: 2A              LD      A,(HLI)             
678A: D5              PUSH    DE                  
678B: 2A              LD      A,(HLI)             
678C: EE 11           XOR     $11                 
678E: BF              CP      A                   
678F: 40              LD      B,B                 
6790: FF              RST     0X38                
6791: 51              LD      D,C                 
6792: FF              RST     0X38                
6793: 5F              LD      E,A                 
6794: BF              CP      A                   
6795: 5F              LD      E,A                 
6796: 5F              LD      E,A                 
6797: 3F              CCF                         
6798: 2F              CPL                         
6799: 1F              RRA                         
679A: 7C              LD      A,H                 
679B: 03              INC     BC                  
679C: BB              CP      E                   
679D: 7C              LD      A,H                 
679E: FF              RST     0X38                
679F: 00              NOP                         
67A0: E0 00           LD      ($FF00+$00),A       
67A2: F8 00           LD      HL,SP+$00           
67A4: FC                              
67A5: C0              RET     NZ                  
67A6: FE E0           CP      $E0                 
67A8: FE 60           CP      $60                 
67AA: DB                              
67AB: EC                              
67AC: 3F              CCF                         
67AD: C0              RET     NZ                  
67AE: EF              RST     0X28                
67AF: 1C              INC     E                   
67B0: FD                              
67B1: FE FD           CP      $FD                 
67B3: EE F1           XOR     $F1                 
67B5: EE EE           XOR     $EE                 
67B7: F0 84           LD      A,($84)             
67B9: F8 0E           LD      HL,SP+$0E           
67BB: F0 F3           LD      A,($F3)             
67BD: 0C              INC     C                   
67BE: FE 00           CP      $00                 
67C0: 00              NOP                         
67C1: 00              NOP                         
67C2: 00              NOP                         
67C3: 00              NOP                         
67C4: 00              NOP                         
67C5: 00              NOP                         
67C6: 00              NOP                         
67C7: 00              NOP                         
67C8: 00              NOP                         
67C9: 00              NOP                         
67CA: 1F              RRA                         
67CB: 00              NOP                         
67CC: 27              DAA                         
67CD: 1F              RRA                         
67CE: 47              LD      B,A                 
67CF: 3F              CCF                         
67D0: 40              LD      B,B                 
67D1: 3F              CCF                         
67D2: 40              LD      B,B                 
67D3: 3F              CCF                         
67D4: 40              LD      B,B                 
67D5: 3F              CCF                         
67D6: 40              LD      B,B                 
67D7: 3F              CCF                         
67D8: 60              LD      H,B                 
67D9: 1F              RRA                         
67DA: 70              LD      (HL),B              
67DB: 0F              RRCA                        
67DC: 3F              CCF                         
67DD: 00              NOP                         
67DE: 1F              RRA                         
67DF: 00              NOP                         
67E0: 00              NOP                         
67E1: 00              NOP                         
67E2: 00              NOP                         
67E3: 00              NOP                         
67E4: 00              NOP                         
67E5: 00              NOP                         
67E6: 00              NOP                         
67E7: 00              NOP                         
67E8: 00              NOP                         
67E9: 00              NOP                         
67EA: C0              RET     NZ                  
67EB: 00              NOP                         
67EC: 20 C0           JR      NZ,$67AE            ; {}
67EE: 10 E0           ;;STOP    $E0                 
67F0: 10 E0           ;;STOP    $E0                 
67F2: 10 E0           ;;STOP    $E0                 
67F4: 10 E0           ;;STOP    $E0                 
67F6: 10 E0           ;;STOP    $E0                 
67F8: 30 C0           JR      NC,$67BA            ; {}
67FA: 70              LD      (HL),B              
67FB: 80              ADD     A,B                 
67FC: E0 00           LD      ($FF00+$00),A       
67FE: C0              RET     NZ                  
67FF: 00              NOP                         
6800: 00              NOP                         
6801: 00              NOP                         
6802: E3                              
6803: 00              NOP                         
6804: FE 61           CP      $61                 
6806: 5F              LD      E,A                 
6807: 30 5F           JR      NC,$6868            ; {}
6809: 20 FF           JR      NZ,$680A            ; {}
680B: 00              NOP                         
680C: FD                              
680D: 03              INC     BC                  
680E: F3              DI                          
680F: 0C              INC     C                   
6810: EF              RST     0X28                
6811: 10 FF           ;;STOP    $FF                 
6813: 00              NOP                         
6814: FF              RST     0X38                
6815: 80              ADD     A,B                 
6816: FF              RST     0X38                
6817: 00              NOP                         
6818: FF              RST     0X38                
6819: 60              LD      H,B                 
681A: FF              RST     0X38                
681B: 70              LD      (HL),B              
681C: 7E              LD      A,(HL)              
681D: BD              CP      L                   
681E: 3E C0           LD      A,$C0               
6820: E3                              
6821: 00              NOP                         
6822: FF              RST     0X38                
6823: 60              LD      H,B                 
6824: 5D              LD      E,L                 
6825: 33              INC     SP                  
6826: 53              LD      D,E                 
6827: 2C              INC     L                   
6828: EF              RST     0X28                
6829: 13              INC     DE                  
682A: FF              RST     0X38                
682B: 0F              RRCA                        
682C: FF              RST     0X38                
682D: 1D              DEC     E                   
682E: DE 39           SBC     $39                 
6830: CF              RST     0X08                
6831: 38 E5           JR      C,$6818             ; {}
6833: 9A              SBC     D                   
6834: F2                              
6835: 0D              DEC     C                   
6836: FF              RST     0X38                
6837: C0              RET     NZ                  
6838: EF              RST     0X28                
6839: D0              RET     NC                  
683A: E0 DF           LD      ($FF00+$DF),A       
683C: F0 6F           LD      A,($6F)             
683E: 70              LD      (HL),B              
683F: 00              NOP                         
6840: 00              NOP                         
6841: 00              NOP                         
6842: 00              NOP                         
6843: 00              NOP                         
6844: 00              NOP                         
6845: 00              NOP                         
6846: 00              NOP                         
6847: 00              NOP                         
6848: 00              NOP                         
6849: 00              NOP                         
684A: 00              NOP                         
684B: 00              NOP                         
684C: 00              NOP                         
684D: 00              NOP                         
684E: 00              NOP                         
684F: 00              NOP                         
6850: 03              INC     BC                  
6851: 00              NOP                         
6852: 05              DEC     B                   
6853: 03              INC     BC                  
6854: 0E 05           LD      C,$05               
6856: 1B              DEC     DE                  
6857: 0C              INC     C                   
6858: 34              INC     (HL)                
6859: 18 68           JR      $68C3               ; {}
685B: 30 D0           JR      NC,$682D            ; {}
685D: 60              LD      H,B                 
685E: E0 1F           LD      ($FF00+$1F),A       
6860: 70              LD      (HL),B              
6861: 00              NOP                         
6862: F8 30           LD      HL,SP+$30           
6864: DC 78 EE        CALL    C,$EE78             
6867: 5C              LD      E,H                 
6868: F7              RST     0X30                
6869: 4E              LD      C,(HL)              
686A: EB                              
686B: 47              LD      B,A                 
686C: E5              PUSH    HL                  
686D: 42              LD      B,D                 
686E: E3                              
686F: 40              LD      B,B                 
6870: FF              RST     0X38                
6871: 00              NOP                         
6872: FF              RST     0X38                
6873: FD                              
6874: 05              DEC     B                   
6875: FB              EI                          
6876: FC                              
6877: 03              INC     BC                  
6878: 75              LD      (HL),L              
6879: 22              LD      (HLI),A             
687A: 63              LD      H,E                 
687B: 1C              INC     E                   
687C: 00              NOP                         
687D: 07              RLCA                        
687E: 00              NOP                         
687F: FF              RST     0X38                
6880: 00              NOP                         
6881: 00              NOP                         
6882: 00              NOP                         
6883: 00              NOP                         
6884: 00              NOP                         
6885: 00              NOP                         
6886: 01 00 01        LD      BC,$0100            
6889: 00              NOP                         
688A: 01 00 03        LD      BC,$0300            
688D: 00              NOP                         
688E: 07              RLCA                        
688F: 02              LD      (BC),A              
6890: 0D              DEC     C                   
6891: 06 1B           LD      B,$1B               
6893: 0C              INC     C                   
6894: 35              DEC     (HL)                
6895: 18 69           JR      $6900               ; {}
6897: 30 D1           JR      NC,$686A            ; {}
6899: 60              LD      H,B                 
689A: E1              POP     HL                  
689B: 1E 01           LD      E,$01               
689D: 00              NOP                         
689E: 00              NOP                         
689F: 00              NOP                         
68A0: 00              NOP                         
68A1: 00              NOP                         
68A2: 00              NOP                         
68A3: 00              NOP                         
68A4: 00              NOP                         
68A5: 00              NOP                         
68A6: C0              RET     NZ                  
68A7: 00              NOP                         
68A8: E0 C0           LD      ($FF00+$C0),A       
68AA: 30 E0           JR      NC,$688C            ; {}
68AC: FF              RST     0X38                
68AD: B0              OR      B                   
68AE: DD                              
68AF: BA              CP      D                   
68B0: EF              RST     0X28                
68B1: 9C              SBC     H                   
68B2: F7              RST     0X30                
68B3: 8D              ADC     A,L                 
68B4: CD 83 C4        CALL    $C483               
68B7: 83              ADD     A,E                 
68B8: C5              PUSH    BC                  
68B9: 82              ADD     A,D                 
68BA: C3 BC C0        JP      $C0BC               
68BD: 87              ADD     A,A                 
68BE: C0              RET     NZ                  
68BF: 3F              CCF                         
68C0: 00              NOP                         
68C1: 00              NOP                         
68C2: 00              NOP                         
68C3: 00              NOP                         
68C4: 00              NOP                         
68C5: 00              NOP                         
68C6: 00              NOP                         
68C7: 00              NOP                         
68C8: 00              NOP                         
68C9: 00              NOP                         
68CA: 00              NOP                         
68CB: 00              NOP                         
68CC: 01 00 01        LD      BC,$0100            
68CF: 00              NOP                         
68D0: 01 00 03        LD      BC,$0300            
68D3: 01 03 01        LD      BC,$0103            
68D6: 06 03           LD      B,$03               
68D8: 07              RLCA                        
68D9: 02              LD      (BC),A              
68DA: 0D              DEC     C                   
68DB: 06 0E           LD      B,$0E               
68DD: 04              INC     B                   
68DE: 0C              INC     C                   
68DF: 03              INC     BC                  
68E0: 00              NOP                         
68E1: 00              NOP                         
68E2: 00              NOP                         
68E3: 00              NOP                         
68E4: 00              NOP                         
68E5: 00              NOP                         
68E6: 00              NOP                         
68E7: 00              NOP                         
68E8: 00              NOP                         
68E9: 00              NOP                         
68EA: 38 00           JR      C,$68EC             ; {}
68EC: DF              RST     0X18                
68ED: 38 F7           JR      C,$68E6             ; {}
68EF: CE FF           ADC     $FF                 
68F1: B0              OR      B                   
68F2: 4F              LD      C,A                 
68F3: BD              CP      L                   
68F4: F3              DI                          
68F5: 0D              DEC     C                   
68F6: 8C              ADC     A,H                 
68F7: 03              INC     BC                  
68F8: 05              DEC     B                   
68F9: 0A              LD      A,(BC)              
68FA: 03              INC     BC                  
68FB: FC                              
68FC: 00              NOP                         
68FD: 07              RLCA                        
68FE: 00              NOP                         
68FF: FF              RST     0X38                
6900: 00              NOP                         
6901: 00              NOP                         
6902: 00              NOP                         
6903: 00              NOP                         
6904: 00              NOP                         
6905: 00              NOP                         
6906: 00              NOP                         
6907: 00              NOP                         
6908: 00              NOP                         
6909: 00              NOP                         
690A: 10 00           ;;STOP    $00                 
690C: 3C              INC     A                   
690D: 10 3E           ;;STOP    $3E                 
690F: 1C              INC     E                   
6910: FF              RST     0X38                
6911: 0E FF           LD      C,$FF               
6913: 6A              LD      L,D                 
6914: 9E              SBC     (HL)                
6915: 61              LD      H,C                 
6916: FF              RST     0X38                
6917: 00              NOP                         
6918: 01 00 03        LD      BC,$0300            
691B: 00              NOP                         
691C: 07              RLCA                        
691D: 03              INC     BC                  
691E: 07              RLCA                        
691F: 00              NOP                         
6920: 0F              RRCA                        
6921: 00              NOP                         
6922: 3F              CCF                         
6923: 0F              RRCA                        
6924: 7F              LD      A,A                 
6925: 3F              CCF                         
6926: FF              RST     0X38                
6927: 4E              LD      C,(HL)              
6928: FF              RST     0X38                
6929: 5C              LD      E,H                 
692A: FF              RST     0X38                
692B: 4C              LD      C,H                 
692C: FF              RST     0X38                
692D: 4C              LD      C,H                 
692E: FF              RST     0X38                
692F: 6C              LD      L,H                 
6930: FF              RST     0X38                
6931: 3F              CCF                         
6932: FF              RST     0X38                
6933: D3                              
6934: 7F              LD      A,A                 
6935: 82              ADD     A,D                 
6936: FF              RST     0X38                
6937: 70              LD      (HL),B              
6938: BF              CP      A                   
6939: 78              LD      A,B                 
693A: 5C              LD      E,H                 
693B: BB              CP      E                   
693C: BF              CP      A                   
693D: C0              RET     NZ                  
693E: F8 00           LD      HL,SP+$00           
6940: C0              RET     NZ                  
6941: 00              NOP                         
6942: F0 C0           LD      A,($C0)             
6944: F8 F0           LD      HL,SP+$F0           
6946: FC                              
6947: 38 FC           JR      C,$6945             ; {}
6949: 98              SBC     B                   
694A: FC                              
694B: 18 FC           JR      $6949               ; {}
694D: 38 FE           JR      C,$694D             ; {}
694F: F0 FF           LD      A,($FF)             
6951: 80              ADD     A,B                 
6952: FF              RST     0X38                
6953: 00              NOP                         
6954: FF              RST     0X38                
6955: 00              NOP                         
6956: E7              RST     0X20                
6957: 18 9E           JR      $68F7               ; {}
6959: 60              LD      H,B                 
695A: 7E              LD      A,(HL)              
695B: 98              SBC     B                   
695C: BF              CP      A                   
695D: 7E              LD      A,(HL)              
695E: FF              RST     0X38                
695F: 00              NOP                         
6960: 00              NOP                         
6961: 00              NOP                         
6962: 00              NOP                         
6963: 00              NOP                         
6964: 00              NOP                         
6965: 00              NOP                         
6966: 00              NOP                         
6967: 00              NOP                         
6968: 00              NOP                         
6969: 00              NOP                         
696A: 0C              INC     C                   
696B: 00              NOP                         
696C: 3E 04           LD      A,$04               
696E: 7E              LD      A,(HL)              
696F: 34              INC     (HL)                
6970: FF              RST     0X38                
6971: 3C              INC     A                   
6972: FF              RST     0X38                
6973: 53              LD      D,E                 
6974: 98              SBC     B                   
6975: 67              LD      H,A                 
6976: FF              RST     0X38                
6977: 00              NOP                         
6978: 07              RLCA                        
6979: 00              NOP                         
697A: 06 03           LD      B,$03               
697C: 03              INC     BC                  
697D: 01 03 00        LD      BC,$0003            
6980: FF              RST     0X38                
6981: 6E              LD      L,(HL)              
6982: F7              RST     0X30                
6983: 6E              LD      L,(HL)              
6984: 69              LD      L,C                 
6985: 06 0F           LD      B,$0F               
6987: 00              NOP                         
6988: 0D              DEC     C                   
6989: 06 0D           LD      B,$0D               
698B: 06 0D           LD      B,$0D               
698D: 06 0D           LD      B,$0D               
698F: 06 0D           LD      B,$0D               
6991: 06 0D           LD      B,$0D               
6993: 06 0D           LD      B,$0D               
6995: 06 0F           LD      B,$0F               
6997: 00              NOP                         
6998: 00              NOP                         
6999: 00              NOP                         
699A: 00              NOP                         
699B: 00              NOP                         
699C: 00              NOP                         
699D: 00              NOP                         
699E: 00              NOP                         
699F: 00              NOP                         
69A0: 00              NOP                         
69A1: 00              NOP                         
69A2: 00              NOP                         
69A3: 00              NOP                         
69A4: 0F              RRCA                        
69A5: 00              NOP                         
69A6: 3F              CCF                         
69A7: 0F              RRCA                        
69A8: 7F              LD      A,A                 
69A9: 3F              CCF                         
69AA: FF              RST     0X38                
69AB: 63              LD      H,E                 
69AC: FF              RST     0X38                
69AD: 61              LD      H,C                 
69AE: FF              RST     0X38                
69AF: 61              LD      H,C                 
69B0: FF              RST     0X38                
69B1: 65              LD      H,L                 
69B2: 7F              LD      A,A                 
69B3: 39              ADD     HL,SP               
69B4: FF              RST     0X38                
69B5: 0F              RRCA                        
69B6: FF              RST     0X38                
69B7: 06 BF           LD      B,$BF               
69B9: 42              LD      B,D                 
69BA: BF              CP      A                   
69BB: 40              LD      B,B                 
69BC: 5F              LD      E,A                 
69BD: 20 FF           JR      NZ,$69BE            ; {}
69BF: 4C              LD      C,H                 
69C0: 00              NOP                         
69C1: 00              NOP                         
69C2: 00              NOP                         
69C3: 00              NOP                         
69C4: C0              RET     NZ                  
69C5: 00              NOP                         
69C6: F0 C0           LD      A,($C0)             
69C8: F8 F0           LD      HL,SP+$F0           
69CA: FC                              
69CB: C8              RET     Z                   
69CC: FC                              
69CD: 88              ADC     A,B                 
69CE: FC                              
69CF: 88              ADC     A,B                 
69D0: FE D8           CP      $D8                 
69D2: FF              RST     0X38                
69D3: B6              OR      (HL)                
69D4: FF              RST     0X38                
69D5: EE FF           XOR     $FF                 
69D7: 6C              LD      L,H                 
69D8: FF              RST     0X38                
69D9: 40              LD      B,B                 
69DA: D6 28           SUB     $28                 
69DC: 2F              CPL                         
69DD: DE FF           SBC     $FF                 
69DF: 00              NOP                         
69E0: C0              RET     NZ                  
69E1: 00              NOP                         
69E2: E0 00           LD      ($FF00+$00),A       
69E4: F0 00           LD      A,($00)             
69E6: 88              ADC     A,B                 
69E7: 70              LD      (HL),B              
69E8: B8              CP      B                   
69E9: 70              LD      (HL),B              
69EA: BB              CP      E                   
69EB: 70              LD      (HL),B              
69EC: 7F              LD      A,A                 
69ED: 30 3F           JR      NC,$6A2E            ; {}
69EF: 06 1F           LD      B,$1F               
69F1: 0F              RRCA                        
69F2: 1F              RRA                         
69F3: 0D              DEC     C                   
69F4: 1F              RRA                         
69F5: 0D              DEC     C                   
69F6: 1F              RRA                         
69F7: 06 0F           LD      B,$0F               
69F9: 00              NOP                         
69FA: 07              RLCA                        
69FB: 00              NOP                         
69FC: 00              NOP                         
69FD: 00              NOP                         
69FE: 00              NOP                         
69FF: 00              NOP                         
6A00: 0E 01           LD      C,$01               
6A02: 1D              DEC     E                   
6A03: 03              INC     BC                  
6A04: 3E 01           LD      A,$01               
6A06: 7F              LD      A,A                 
6A07: 00              NOP                         
6A08: 7E              LD      A,(HL)              
6A09: 01 FE 61        LD      BC,$61FE            
6A0C: FF              RST     0X38                
6A0D: 70              LD      (HL),B              
6A0E: FF              RST     0X38                
6A0F: 5F              LD      E,A                 
6A10: E7              RST     0X20                
6A11: 5F              LD      E,A                 
6A12: B8              CP      B                   
6A13: 67              LD      H,A                 
6A14: 7F              LD      A,A                 
6A15: 20 5F           JR      NZ,$6A76            ; {}
6A17: 30 2F           JR      NC,$6A48            ; {}
6A19: 18 27           JR      $6A42               ; {}
6A1B: 1F              RRA                         
6A1C: 18 07           JR      $6A25               ; {}
6A1E: 07              RLCA                        
6A1F: 00              NOP                         
6A20: 00              NOP                         
6A21: 00              NOP                         
6A22: 07              RLCA                        
6A23: 00              NOP                         
6A24: 0B              DEC     BC                  
6A25: 07              RLCA                        
6A26: 17              RLA                         
6A27: 0F              RRCA                        
6A28: 17              RLA                         
6A29: 0C              INC     C                   
6A2A: 2E 19           LD      L,$19               
6A2C: 5F              LD      E,A                 
6A2D: 30 FE           JR      NC,$6A2D            ; {}
6A2F: 61              LD      H,C                 
6A30: FD                              
6A31: 63              LD      H,E                 
6A32: BE              CP      (HL)                
6A33: 61              LD      H,C                 
6A34: 5F              LD      E,A                 
6A35: 20 7F           JR      NZ,$6AB6            ; {}
6A37: 00              NOP                         
6A38: 3F              CCF                         
6A39: 00              NOP                         
6A3A: 1F              RRA                         
6A3B: 00              NOP                         
6A3C: 0F              RRCA                        
6A3D: 00              NOP                         
6A3E: 03              INC     BC                  
6A3F: 00              NOP                         
6A40: 38 00           JR      C,$6A42             ; {}
6A42: 57              LD      D,A                 
6A43: 38 AC           JR      C,$69F1             ; {}
6A45: 73              LD      (HL),E              
6A46: FF              RST     0X38                
6A47: 60              LD      H,B                 
6A48: FF              RST     0X38                
6A49: 60              LD      H,B                 
6A4A: AF              XOR     A                   
6A4B: 70              LD      (HL),B              
6A4C: 5B              LD      E,E                 
6A4D: 3C              INC     A                   
6A4E: 27              DAA                         
6A4F: 1F              RRA                         
6A50: 18 07           JR      $6A59               ; {}
6A52: 27              DAA                         
6A53: 18 4F           JR      $6AA4               ; {}
6A55: 30 BF           JR      NC,$6A16            ; {}
6A57: 60              LD      H,B                 
6A58: AE              XOR     (HL)                
6A59: 71              LD      (HL),C              
6A5A: 9F              SBC     A                   
6A5B: 7F              LD      A,A                 
6A5C: 40              LD      B,B                 
6A5D: 3F              CCF                         
6A5E: 3F              CCF                         
6A5F: 00              NOP                         
6A60: 70              LD      (HL),B              
6A61: 00              NOP                         
6A62: AC              XOR     H                   
6A63: 70              LD      (HL),B              
6A64: AE              XOR     (HL)                
6A65: 70              LD      (HL),B              
6A66: DF              RST     0X18                
6A67: 20 FF           JR      NZ,$6A68            ; {}
6A69: 00              NOP                         
6A6A: FF              RST     0X38                
6A6B: 00              NOP                         
6A6C: FF              RST     0X38                
6A6D: 00              NOP                         
6A6E: 7F              LD      A,A                 
6A6F: 80              ADD     A,B                 
6A70: DF              RST     0X18                
6A71: E0 EF           LD      ($FF00+$EF),A       
6A73: 70              LD      (HL),B              
6A74: EF              RST     0X28                
6A75: 70              LD      (HL),B              
6A76: EF              RST     0X28                
6A77: 70              LD      (HL),B              
6A78: DE E0           SBC     $E0                 
6A7A: BE              CP      (HL)                
6A7B: C0              RET     NZ                  
6A7C: F8 00           LD      HL,SP+$00           
6A7E: C0              RET     NZ                  
6A7F: 00              NOP                         
6A80: 03              INC     BC                  
6A81: 00              NOP                         
6A82: 0E 01           LD      C,$01               
6A84: 1D              DEC     E                   
6A85: 03              INC     BC                  
6A86: 3D              DEC     A                   
6A87: 03              INC     BC                  
6A88: 7E              LD      A,(HL)              
6A89: 01 7F 00        LD      BC,$007F            
6A8C: FF              RST     0X38                
6A8D: 00              NOP                         
6A8E: FF              RST     0X38                
6A8F: 00              NOP                         
6A90: FF              RST     0X38                
6A91: 00              NOP                         
6A92: FF              RST     0X38                
6A93: 00              NOP                         
6A94: FF              RST     0X38                
6A95: 00              NOP                         
6A96: FF              RST     0X38                
6A97: 00              NOP                         
6A98: 7F              LD      A,A                 
6A99: 00              NOP                         
6A9A: 7F              LD      A,A                 
6A9B: 00              NOP                         
6A9C: 3F              CCF                         
6A9D: 00              NOP                         
6A9E: 0F              RRCA                        
6A9F: 00              NOP                         
6AA0: 07              RLCA                        
6AA1: 00              NOP                         
6AA2: 3F              CCF                         
6AA3: 00              NOP                         
6AA4: FE 01           CP      $01                 
6AA6: FD                              
6AA7: 03              INC     BC                  
6AA8: FD                              
6AA9: 03              INC     BC                  
6AAA: FE 01           CP      $01                 
6AAC: FF              RST     0X38                
6AAD: 00              NOP                         
6AAE: FF              RST     0X38                
6AAF: 00              NOP                         
6AB0: FF              RST     0X38                
6AB1: 00              NOP                         
6AB2: FF              RST     0X38                
6AB3: 00              NOP                         
6AB4: FF              RST     0X38                
6AB5: 00              NOP                         
6AB6: FF              RST     0X38                
6AB7: 00              NOP                         
6AB8: FF              RST     0X38                
6AB9: 00              NOP                         
6ABA: FF              RST     0X38                
6ABB: 00              NOP                         
6ABC: FF              RST     0X38                
6ABD: 00              NOP                         
6ABE: FF              RST     0X38                
6ABF: 00              NOP                         
6AC0: 00              NOP                         
6AC1: 00              NOP                         
6AC2: 00              NOP                         
6AC3: 00              NOP                         
6AC4: 00              NOP                         
6AC5: 00              NOP                         
6AC6: 03              INC     BC                  
6AC7: 00              NOP                         
6AC8: 07              RLCA                        
6AC9: 00              NOP                         
6ACA: 0F              RRCA                        
6ACB: 00              NOP                         
6ACC: 1F              RRA                         
6ACD: 00              NOP                         
6ACE: 1F              RRA                         
6ACF: 00              NOP                         
6AD0: 3F              CCF                         
6AD1: 00              NOP                         
6AD2: 3F              CCF                         
6AD3: 00              NOP                         
6AD4: 7F              LD      A,A                 
6AD5: 00              NOP                         
6AD6: 7F              LD      A,A                 
6AD7: 00              NOP                         
6AD8: 7F              LD      A,A                 
6AD9: 00              NOP                         
6ADA: FF              RST     0X38                
6ADB: 00              NOP                         
6ADC: FF              RST     0X38                
6ADD: 00              NOP                         
6ADE: FF              RST     0X38                
6ADF: 00              NOP                         
6AE0: 07              RLCA                        
6AE1: 00              NOP                         
6AE2: 3F              CCF                         
6AE3: 00              NOP                         
6AE4: FF              RST     0X38                
6AE5: 00              NOP                         
6AE6: FF              RST     0X38                
6AE7: 00              NOP                         
6AE8: FF              RST     0X38                
6AE9: 00              NOP                         
6AEA: FF              RST     0X38                
6AEB: 00              NOP                         
6AEC: FF              RST     0X38                
6AED: 00              NOP                         
6AEE: FF              RST     0X38                
6AEF: 00              NOP                         
6AF0: FF              RST     0X38                
6AF1: 00              NOP                         
6AF2: FF              RST     0X38                
6AF3: 00              NOP                         
6AF4: FF              RST     0X38                
6AF5: 00              NOP                         
6AF6: FF              RST     0X38                
6AF7: 00              NOP                         
6AF8: FF              RST     0X38                
6AF9: 00              NOP                         
6AFA: FF              RST     0X38                
6AFB: 00              NOP                         
6AFC: FF              RST     0X38                
6AFD: 00              NOP                         
6AFE: FF              RST     0X38                
6AFF: 00              NOP                         
6B00: 01 00 0F        LD      BC,$0F00            
6B03: 01 1F 0C        LD      BC,$0C1F            
6B06: 1F              RRA                         
6B07: 0B              DEC     BC                  
6B08: 3F              CCF                         
6B09: 02              LD      (BC),A              
6B0A: 4F              LD      C,A                 
6B0B: 3B              DEC     SP                  
6B0C: 43              LD      B,E                 
6B0D: 3C              INC     A                   
6B0E: 42              LD      B,D                 
6B0F: 3D              DEC     A                   
6B10: 70              LD      (HL),B              
6B11: 0F              RRCA                        
6B12: BF              CP      A                   
6B13: 70              LD      (HL),B              
6B14: BF              CP      A                   
6B15: 7F              LD      A,A                 
6B16: 5F              LD      E,A                 
6B17: 3F              CCF                         
6B18: 30 0F           JR      NC,$6B29            ; {}
6B1A: 0F              RRCA                        
6B1B: 00              NOP                         
6B1C: 04              INC     B                   
6B1D: 03              INC     BC                  
6B1E: 03              INC     BC                  
6B1F: 00              NOP                         
6B20: F0 00           LD      A,($00)             
6B22: FC                              
6B23: F0 FF           LD      A,($FF)             
6B25: 3C              INC     A                   
6B26: FF              RST     0X38                
6B27: DF              RST     0X18                
6B28: FF              RST     0X38                
6B29: DF              RST     0X18                
6B2A: FF              RST     0X38                
6B2B: 8F              ADC     A,A                 
6B2C: BF              CP      A                   
6B2D: 77              LD      (HL),A              
6B2E: 0F              RRCA                        
6B2F: F7              RST     0X30                
6B30: 4F              LD      C,A                 
6B31: B7              OR      A                   
6B32: FF              RST     0X38                
6B33: 0F              RRCA                        
6B34: FF              RST     0X38                
6B35: FF              RST     0X38                
6B36: FF              RST     0X38                
6B37: FF              RST     0X38                
6B38: 3F              CCF                         
6B39: FF              RST     0X38                
6B3A: FF              RST     0X38                
6B3B: 7F              LD      A,A                 
6B3C: 00              NOP                         
6B3D: FF              RST     0X38                
6B3E: FF              RST     0X38                
6B3F: 00              NOP                         
6B40: 00              NOP                         
6B41: 00              NOP                         
6B42: 00              NOP                         
6B43: 00              NOP                         
6B44: 00              NOP                         
6B45: 00              NOP                         
6B46: C0              RET     NZ                  
6B47: 00              NOP                         
6B48: E0 C0           LD      ($FF00+$C0),A       
6B4A: F0 E0           LD      A,($E0)             
6B4C: F8 F0           LD      HL,SP+$F0           
6B4E: F8 F0           LD      HL,SP+$F0           
6B50: FC                              
6B51: F8 FC           LD      HL,SP+$FC           
6B53: F8 FE           LD      HL,SP+$FE           
6B55: FC                              
6B56: FE FC           CP      $FC                 
6B58: FA FC F2        LD      A,($F2FC)           
6B5B: FC                              
6B5C: 04              INC     B                   
6B5D: F8 F8           LD      HL,SP+$F8           
6B5F: 00              NOP                         
6B60: 00              NOP                         
6B61: 00              NOP                         
6B62: 01 00 03        LD      BC,$0300            
6B65: 01 03 01        LD      BC,$0103            
6B68: 07              RLCA                        
6B69: 00              NOP                         
6B6A: 09              ADD     HL,BC               
6B6B: 07              RLCA                        
6B6C: 08 07 0C        LD      ($0C07),SP          
6B6F: 03              INC     BC                  
6B70: 0A              LD      A,(BC)              
6B71: 05              DEC     B                   
6B72: 09              ADD     HL,BC               
6B73: 06 04           LD      B,$04               
6B75: 03              INC     BC                  
6B76: 03              INC     BC                  
6B77: 00              NOP                         
6B78: 05              DEC     B                   
6B79: 03              INC     BC                  
6B7A: 04              INC     B                   
6B7B: 03              INC     BC                  
6B7C: 04              INC     B                   
6B7D: 03              INC     BC                  
6B7E: 03              INC     BC                  
6B7F: 00              NOP                         
6B80: 3E 00           LD      A,$00               
6B82: FF              RST     0X38                
6B83: 3E FF           LD      A,$FF               
6B85: 87              ADD     A,A                 
6B86: FF              RST     0X38                
6B87: 7B              LD      A,E                 
6B88: FF              RST     0X38                
6B89: 5B              LD      E,E                 
6B8A: FF              RST     0X38                
6B8B: 71              LD      (HL),C              
6B8C: 77              LD      (HL),A              
6B8D: 8E              ADC     A,(HL)              
6B8E: 41              LD      B,C                 
6B8F: BE              CP      (HL)                
6B90: 09              ADD     HL,BC               
6B91: F6 F3           OR      $F3                 
6B93: 0C              INC     C                   
6B94: 07              RLCA                        
6B95: FB              EI                          
6B96: FF              RST     0X38                
6B97: 07              RLCA                        
6B98: F8 F7           LD      HL,SP+$F7           
6B9A: FF              RST     0X38                
6B9B: F8 00           LD      HL,SP+$00           
6B9D: FF              RST     0X38                
6B9E: FF              RST     0X38                
6B9F: 00              NOP                         
6BA0: 00              NOP                         
6BA1: 00              NOP                         
6BA2: C0              RET     NZ                  
6BA3: 00              NOP                         
6BA4: F0 C0           LD      A,($C0)             
6BA6: F8 F0           LD      HL,SP+$F0           
6BA8: FC                              
6BA9: F8 FE           LD      HL,SP+$FE           
6BAB: FC                              
6BAC: FE FC           CP      $FC                 
6BAE: FF              RST     0X38                
6BAF: FE FF           CP      $FF                 
6BB1: 3E EF           LD      A,$EF               
6BB3: FE FF           CP      $FF                 
6BB5: EE DF           XOR     $DF                 
6BB7: EE 3D           XOR     $3D                 
6BB9: DE F9           SBC     $F9                 
6BBB: 3E 02           LD      A,$02               
6BBD: FC                              
6BBE: FC                              
6BBF: 00              NOP                         
6BC0: 39              ADD     HL,SP               
6BC1: 07              RLCA                        
6BC2: 39              ADD     HL,SP               
6BC3: 07              RLCA                        
6BC4: 7D              LD      A,L                 
6BC5: 03              INC     BC                  
6BC6: BF              CP      A                   
6BC7: 4D              LD      C,L                 
6BC8: BF              CP      A                   
6BC9: 4D              LD      C,L                 
6BCA: 7D              LD      A,L                 
6BCB: 03              INC     BC                  
6BCC: 39              ADD     HL,SP               
6BCD: 07              RLCA                        
6BCE: 39              ADD     HL,SP               
6BCF: 07              RLCA                        
6BD0: 39              ADD     HL,SP               
6BD1: 07              RLCA                        
6BD2: 39              ADD     HL,SP               
6BD3: 07              RLCA                        
6BD4: 39              ADD     HL,SP               
6BD5: 06 7B           LD      B,$7B               
6BD7: 35              DEC     (HL)                
6BD8: 7B              LD      A,E                 
6BD9: 35              DEC     (HL)                
6BDA: 39              ADD     HL,SP               
6BDB: 06 39           LD      B,$39               
6BDD: 07              RLCA                        
6BDE: 39              ADD     HL,SP               
6BDF: 07              RLCA                        
6BE0: 00              NOP                         
6BE1: 00              NOP                         
6BE2: 00              NOP                         
6BE3: 00              NOP                         
6BE4: 00              NOP                         
6BE5: 00              NOP                         
6BE6: 00              NOP                         
6BE7: 00              NOP                         
6BE8: 00              NOP                         
6BE9: 00              NOP                         
6BEA: 00              NOP                         
6BEB: 00              NOP                         
6BEC: 00              NOP                         
6BED: 00              NOP                         
6BEE: 00              NOP                         
6BEF: 00              NOP                         
6BF0: 70              LD      (HL),B              
6BF1: 00              NOP                         
6BF2: D8              RET     C                   
6BF3: 20 F8           JR      NZ,$6BED            ; {}
6BF5: 00              NOP                         
6BF6: F8 00           LD      HL,SP+$00           
6BF8: 74              LD      (HL),H              
6BF9: 00              NOP                         
6BFA: 02              LD      (BC),A              
6BFB: 00              NOP                         
6BFC: 02              LD      (BC),A              
6BFD: 00              NOP                         
6BFE: 02              LD      (BC),A              
6BFF: 00              NOP                         
6C00: 00              NOP                         
6C01: 3C              INC     A                   
6C02: 3C              INC     A                   
6C03: 7E              LD      A,(HL)              
6C04: 7E              LD      A,(HL)              
6C05: FF              RST     0X38                
6C06: 7E              LD      A,(HL)              
6C07: FF              RST     0X38                
6C08: 7E              LD      A,(HL)              
6C09: FF              RST     0X38                
6C0A: 7E              LD      A,(HL)              
6C0B: FF              RST     0X38                
6C0C: 3C              INC     A                   
6C0D: 7E              LD      A,(HL)              
6C0E: 00              NOP                         
6C0F: 3C              INC     A                   
6C10: 00              NOP                         
6C11: 00              NOP                         
6C12: 00              NOP                         
6C13: 00              NOP                         
6C14: 00              NOP                         
6C15: 00              NOP                         
6C16: 00              NOP                         
6C17: 00              NOP                         
6C18: 00              NOP                         
6C19: 00              NOP                         
6C1A: 07              RLCA                        
6C1B: 00              NOP                         
6C1C: 0F              RRCA                        
6C1D: 07              RLCA                        
6C1E: 1F              RRA                         
6C1F: 0F              RRCA                        
6C20: 00              NOP                         
6C21: 00              NOP                         
6C22: 00              NOP                         
6C23: 00              NOP                         
6C24: 00              NOP                         
6C25: 00              NOP                         
6C26: E0 00           LD      ($FF00+$00),A       
6C28: F0 60           LD      A,($60)             
6C2A: 78              LD      A,B                 
6C2B: 10 1C           ;;STOP    $1C                 
6C2D: 08 0E 04        LD      ($040E),SP          
6C30: 0E 04           LD      C,$04               
6C32: 0F              RRCA                        
6C33: 04              INC     B                   
6C34: 0E 05           LD      C,$05               
6C36: 3F              CCF                         
6C37: 06 7F           LD      B,$7F               
6C39: 21 FF 5E        LD      HL,$5EFF            
6C3C: FF              RST     0X38                
6C3D: 33              INC     SP                  
6C3E: F7              RST     0X30                
6C3F: A9              XOR     C                   
6C40: 00              NOP                         
6C41: 00              NOP                         
6C42: 00              NOP                         
6C43: 00              NOP                         
6C44: 00              NOP                         
6C45: 00              NOP                         
6C46: 00              NOP                         
6C47: 00              NOP                         
6C48: 00              NOP                         
6C49: 00              NOP                         
6C4A: 03              INC     BC                  
6C4B: 00              NOP                         
6C4C: 0C              INC     C                   
6C4D: 03              INC     BC                  
6C4E: 13              INC     DE                  
6C4F: 0F              RRCA                        
6C50: 26 1F           LD      H,$1F               
6C52: E0 3F           LD      ($FF00+$3F),A       
6C54: 70              LD      (HL),B              
6C55: BF              CP      A                   
6C56: F0 7F           LD      A,($7F)             
6C58: F0 FF           LD      A,($FF)             
6C5A: 70              LD      (HL),B              
6C5B: FF              RST     0X38                
6C5C: B1              OR      C                   
6C5D: 7E              LD      A,(HL)              
6C5E: E0 BF           LD      ($FF00+$BF),A       
6C60: 0F              RRCA                        
6C61: 0F              RRCA                        
6C62: 10 1F           ;;STOP    $1F                 
6C64: 28 3F           JR      Z,$6CA5             ; {}
6C66: 53              LD      D,E                 
6C67: 7F              LD      A,A                 
6C68: 54              LD      D,H                 
6C69: 7F              LD      A,A                 
6C6A: A4              AND     H                   
6C6B: FF              RST     0X38                
6C6C: 29              ADD     HL,HL               
6C6D: FF              RST     0X38                
6C6E: A9              XOR     C                   
6C6F: 7F              LD      A,A                 
6C70: 92              SUB     D                   
6C71: 7E              LD      A,(HL)              
6C72: CF              RST     0X08                
6C73: 3F              CCF                         
6C74: E0 1F           LD      ($FF00+$1F),A       
6C76: 20 DF           JR      NZ,$6C57            ; {}
6C78: 00              NOP                         
6C79: FF              RST     0X38                
6C7A: 80              ADD     A,B                 
6C7B: 7F              LD      A,A                 
6C7C: 60              LD      H,B                 
6C7D: 9F              SBC     A                   
6C7E: E1              POP     HL                  
6C7F: 9F              SBC     A                   
6C80: 00              NOP                         
6C81: 00              NOP                         
6C82: 80              ADD     A,B                 
6C83: 80              ADD     A,B                 
6C84: 80              ADD     A,B                 
6C85: 80              ADD     A,B                 
6C86: 00              NOP                         
6C87: 00              NOP                         
6C88: 80              ADD     A,B                 
6C89: 80              ADD     A,B                 
6C8A: 81              ADD     A,C                 
6C8B: 81              ADD     A,C                 
6C8C: 06 07           LD      B,$07               
6C8E: 09              ADD     HL,BC               
6C8F: 0F              RRCA                        
6C90: 32              LD      (HLD),A             
6C91: 3F              CCF                         
6C92: C4 FF 09        CALL    NZ,$09FF            
6C95: FF              RST     0X38                
6C96: 0A              LD      A,(BC)              
6C97: FF              RST     0X38                
6C98: 04              INC     B                   
6C99: FF              RST     0X38                
6C9A: 02              LD      (BC),A              
6C9B: FF              RST     0X38                
6C9C: 03              INC     BC                  
6C9D: FF              RST     0X38                
6C9E: 81              ADD     A,C                 
6C9F: FF              RST     0X38                
6CA0: 00              NOP                         
6CA1: 00              NOP                         
6CA2: 00              NOP                         
6CA3: 00              NOP                         
6CA4: 00              NOP                         
6CA5: 00              NOP                         
6CA6: 00              NOP                         
6CA7: 00              NOP                         
6CA8: 00              NOP                         
6CA9: 00              NOP                         
6CAA: F8 F8           LD      HL,SP+$F8           
6CAC: 06 FE           LD      B,$FE               
6CAE: 81              ADD     A,C                 
6CAF: FF              RST     0X38                
6CB0: 03              INC     BC                  
6CB1: FF              RST     0X38                
6CB2: 7D              LD      A,L                 
6CB3: FF              RST     0X38                
6CB4: 81              ADD     A,C                 
6CB5: FF              RST     0X38                
6CB6: 1E FE           LD      E,$FE               
6CB8: 61              LD      H,C                 
6CB9: FF              RST     0X38                
6CBA: 82              ADD     A,D                 
6CBB: FE 0C           CP      $0C                 
6CBD: FC                              
6CBE: F0 F0           LD      A,($F0)             
6CC0: 13              INC     DE                  
6CC1: 0F              RRCA                        
6CC2: 1D              DEC     E                   
6CC3: 03              INC     BC                  
6CC4: 1A              LD      A,(DE)              
6CC5: 0D              DEC     C                   
6CC6: 17              RLA                         
6CC7: 0A              LD      A,(BC)              
6CC8: 3D              DEC     A                   
6CC9: 02              LD      (BC),A              
6CCA: 57              LD      D,A                 
6CCB: 38 BB           JR      C,$6C88             ; {}
6CCD: 7C              LD      A,H                 
6CCE: 99              SBC     C                   
6CCF: 7E              LD      A,(HL)              
6CD0: 80              ADD     A,B                 
6CD1: 7F              LD      A,A                 
6CD2: 60              LD      H,B                 
6CD3: 1F              RRA                         
6CD4: 18 07           JR      $6CDD               ; {}
6CD6: 0C              INC     C                   
6CD7: 03              INC     BC                  
6CD8: 06 01           LD      B,$01               
6CDA: 03              INC     BC                  
6CDB: 00              NOP                         
6CDC: 01 00 00        LD      BC,$0000            
6CDF: 00              NOP                         
6CE0: FF              RST     0X38                
6CE1: A1              AND     C                   
6CE2: FF              RST     0X38                
6CE3: B3              OR      E                   
6CE4: FE DF           CP      $DF                 
6CE6: 71              LD      (HL),C              
6CE7: EE 0E           XOR     $0E                 
6CE9: F1              POP     AF                  
6CEA: 87              ADD     A,A                 
6CEB: 78              LD      A,B                 
6CEC: C4 BB 44        CALL    NZ,$44BB            ; {}
6CEF: BB              CP      E                   
6CF0: E2              LD      (C),A               
6CF1: 1D              DEC     E                   
6CF2: E1              POP     HL                  
6CF3: 1E 60           LD      E,$60               
6CF5: 9F              SBC     A                   
6CF6: 30 CF           JR      NC,$6CC7            ; {}
6CF8: 10 EF           ;;STOP    $EF                 
6CFA: 10 EF           ;;STOP    $EF                 
6CFC: 99              SBC     C                   
6CFD: 66              LD      H,(HL)              
6CFE: FF              RST     0X38                
6CFF: 00              NOP                         
6D00: FF              RST     0X38                
6D01: 48              LD      C,B                 
6D02: FF              RST     0X38                
6D03: 4A              LD      C,D                 
6D04: FF              RST     0X38                
6D05: D2 FF 94        JP      NC,$94FF            
6D08: FF              RST     0X38                
6D09: 24              INC     H                   
6D0A: FF              RST     0X38                
6D0B: C4 FF 08        CALL    NZ,$08FF            
6D0E: FF              RST     0X38                
6D0F: 08 FF 08        LD      ($08FF),SP          
6D12: FB              EI                          
6D13: 0C              INC     C                   
6D14: FD                              
6D15: 86              ADD     A,(HL)              
6D16: FA 87 FA        LD      A,($FA87)           
6D19: 87              ADD     A,A                 
6D1A: B2              OR      D                   
6D1B: CF              RST     0X08                
6D1C: 86              ADD     A,(HL)              
6D1D: FF              RST     0X38                
6D1E: 0C              INC     C                   
6D1F: FF              RST     0X38                
6D20: F1              POP     AF                  
6D21: 8F              ADC     A,A                 
6D22: BC              CP      H                   
6D23: CF              RST     0X08                
6D24: BE              CP      (HL)                
6D25: DF              RST     0X18                
6D26: BE              CP      (HL)                
6D27: DF              RST     0X18                
6D28: BE              CP      (HL)                
6D29: DF              RST     0X18                
6D2A: AC              XOR     H                   
6D2B: DF              RST     0X18                
6D2C: C0              RET     NZ                  
6D2D: FF              RST     0X38                
6D2E: 46              LD      B,(HL)              
6D2F: FF              RST     0X38                
6D30: A6              AND     (HL)                
6D31: 7F              LD      A,A                 
6D32: 9F              SBC     A                   
6D33: 7F              LD      A,A                 
6D34: 1F              RRA                         
6D35: FF              RST     0X38                
6D36: 1C              INC     E                   
6D37: FF              RST     0X38                
6D38: 18 FF           JR      $6D39               ; {}
6D3A: 18 FF           JR      $6D3B               ; {}
6D3C: 18 FF           JR      $6D3D               ; {}
6D3E: 18 FF           JR      $6D3F               ; {}
6D40: 80              ADD     A,B                 
6D41: FF              RST     0X38                
6D42: 00              NOP                         
6D43: FF              RST     0X38                
6D44: 38 FF           JR      C,$6D45             ; {}
6D46: 78              LD      A,B                 
6D47: FF              RST     0X38                
6D48: 38 FF           JR      C,$6D49             ; {}
6D4A: 19              ADD     HL,DE               
6D4B: FF              RST     0X38                
6D4C: 81              ADD     A,C                 
6D4D: FF              RST     0X38                
6D4E: 18 FF           JR      $6D4F               ; {}
6D50: 1C              INC     E                   
6D51: FF              RST     0X38                
6D52: 3E FF           LD      A,$FF               
6D54: FF              RST     0X38                
6D55: FF              RST     0X38                
6D56: 81              ADD     A,C                 
6D57: FF              RST     0X38                
6D58: 00              NOP                         
6D59: FF              RST     0X38                
6D5A: 3F              CCF                         
6D5B: FF              RST     0X38                
6D5C: C0              RET     NZ                  
6D5D: FF              RST     0X38                
6D5E: 8C              ADC     A,H                 
6D5F: FF              RST     0X38                
6D60: 20 E0           JR      NZ,$6D42            ; {}
6D62: 10 F0           ;;STOP    $F0                 
6D64: 08 F8 09        LD      ($09F8),SP          
6D67: F9              LD      SP,HL               
6D68: 06 FF           LD      B,$FF               
6D6A: 84              ADD     A,H                 
6D6B: FF              RST     0X38                
6D6C: 82              ADD     A,D                 
6D6D: FF              RST     0X38                
6D6E: 01 FF 61        LD      BC,$61FF            
6D71: FF              RST     0X38                
6D72: E0 FF           LD      ($FF00+$FF),A       
6D74: F0 FF           LD      A,($FF)             
6D76: FE FF           CP      $FF                 
6D78: FF              RST     0X38                
6D79: FF              RST     0X38                
6D7A: CF              RST     0X08                
6D7B: FF              RST     0X38                
6D7C: 80              ADD     A,B                 
6D7D: FF              RST     0X38                
6D7E: 81              ADD     A,C                 
6D7F: FF              RST     0X38                
6D80: 00              NOP                         
6D81: 00              NOP                         
6D82: 3C              INC     A                   
6D83: 3C              INC     A                   
6D84: C2 FE 3A        JP      NZ,$3AFE            
6D87: FE 41           CP      $41                 
6D89: FF              RST     0X38                
6D8A: 9A              SBC     D                   
6D8B: FE 61           CP      $61                 
6D8D: FF              RST     0X38                
6D8E: 02              LD      (BC),A              
6D8F: FE 1C           CP      $1C                 
6D91: FC                              
6D92: A8              XOR     B                   
6D93: F8 86           LD      HL,SP+$86           
6D95: FE BC           CP      $BC                 
6D97: FC                              
6D98: 82              ADD     A,D                 
6D99: FE 82           CP      $82                 
6D9B: FE BC           CP      $BC                 
6D9D: FC                              
6D9E: 88              ADC     A,B                 
6D9F: F8 8E           LD      HL,SP+$8E           
6DA1: FF              RST     0X38                
6DA2: 80              ADD     A,B                 
6DA3: FF              RST     0X38                
6DA4: 83              ADD     A,E                 
6DA5: FF              RST     0X38                
6DA6: 98              SBC     B                   
6DA7: FF              RST     0X38                
6DA8: 44              LD      B,H                 
6DA9: 7F              LD      A,A                 
6DAA: 46              LD      B,(HL)              
6DAB: 7F              LD      A,A                 
6DAC: 23              INC     HL                  
6DAD: 3F              CCF                         
6DAE: 11 1F 08        LD      DE,$081F            
6DB1: 0F              RRCA                        
6DB2: 06 07           LD      B,$07               
6DB4: 01 01 00        LD      BC,$0001            
6DB7: 00              NOP                         
6DB8: 00              NOP                         
6DB9: 00              NOP                         
6DBA: 00              NOP                         
6DBB: 00              NOP                         
6DBC: 00              NOP                         
6DBD: 00              NOP                         
6DBE: 00              NOP                         
6DBF: 00              NOP                         
6DC0: 10 FF           ;;STOP    $FF                 
6DC2: 20 FF           JR      NZ,$6DC3            ; {}
6DC4: C0              RET     NZ                  
6DC5: FF              RST     0X38                
6DC6: 00              NOP                         
6DC7: FF              RST     0X38                
6DC8: 01 FF 03        LD      BC,$03FF            
6DCB: FF              RST     0X38                
6DCC: FE FF           CP      $FF                 
6DCE: FC                              
6DCF: FF              RST     0X38                
6DD0: 00              NOP                         
6DD1: FF              RST     0X38                
6DD2: 00              NOP                         
6DD3: FF              RST     0X38                
6DD4: 83              ADD     A,E                 
6DD5: FF              RST     0X38                
6DD6: 7C              LD      A,H                 
6DD7: 7F              LD      A,A                 
6DD8: 26 3F           LD      H,$3F               
6DDA: 13              INC     DE                  
6DDB: 1F              RRA                         
6DDC: 0F              RRCA                        
6DDD: 0F              RRCA                        
6DDE: 00              NOP                         
6DDF: 00              NOP                         
6DE0: 30 FF           JR      NC,$6DE1            ; {}
6DE2: 30 FF           JR      NC,$6DE3            ; {}
6DE4: 61              LD      H,C                 
6DE5: FF              RST     0X38                
6DE6: C1              POP     BC                  
6DE7: FF              RST     0X38                
6DE8: 86              ADD     A,(HL)              
6DE9: FF              RST     0X38                
6DEA: 00              NOP                         
6DEB: FF              RST     0X38                
6DEC: 00              NOP                         
6DED: FF              RST     0X38                
6DEE: 00              NOP                         
6DEF: FF              RST     0X38                
6DF0: 00              NOP                         
6DF1: FF              RST     0X38                
6DF2: 00              NOP                         
6DF3: FF              RST     0X38                
6DF4: F0 FF           LD      A,($FF)             
6DF6: 4F              LD      C,A                 
6DF7: FF              RST     0X38                
6DF8: 22              LD      (HLI),A             
6DF9: FE 11           CP      $11                 
6DFB: FF              RST     0X38                
6DFC: 89              ADC     A,C                 
6DFD: FF              RST     0X38                
6DFE: 7E              LD      A,(HL)              
6DFF: 7E              LD      A,(HL)              
6E00: F3              DI                          
6E01: FF              RST     0X38                
6E02: 8C              ADC     A,H                 
6E03: FF              RST     0X38                
6E04: F0 FF           LD      A,($FF)             
6E06: 00              NOP                         
6E07: FF              RST     0X38                
6E08: 00              NOP                         
6E09: FF              RST     0X38                
6E0A: 00              NOP                         
6E0B: FF              RST     0X38                
6E0C: 01 FF 01        LD      BC,$01FF            
6E0F: FF              RST     0X38                
6E10: 01 FF 03        LD      BC,$03FF            
6E13: FF              RST     0X38                
6E14: 0C              INC     C                   
6E15: FF              RST     0X38                
6E16: FC                              
6E17: FF              RST     0X38                
6E18: 02              LD      (BC),A              
6E19: 03              INC     BC                  
6E1A: 01 01 00        LD      BC,$0001            
6E1D: 00              NOP                         
6E1E: 00              NOP                         
6E1F: 00              NOP                         
6E20: 03              INC     BC                  
6E21: FF              RST     0X38                
6E22: 0E FF           LD      C,$FF               
6E24: 12              LD      (DE),A              
6E25: F3              DI                          
6E26: 22              LD      (HLI),A             
6E27: E3                              
6E28: 79              LD      A,C                 
6E29: F9              LD      SP,HL               
6E2A: C4 FC C3        CALL    NZ,$C3FC            
6E2D: FF              RST     0X38                
6E2E: 20 FF           JR      NZ,$6E2F            ; {}
6E30: 18 FF           JR      $6E31               ; {}
6E32: 87              ADD     A,A                 
6E33: FF              RST     0X38                
6E34: 60              LD      H,B                 
6E35: FF              RST     0X38                
6E36: 1F              RRA                         
6E37: FF              RST     0X38                
6E38: 00              NOP                         
6E39: FF              RST     0X38                
6E3A: 81              ADD     A,C                 
6E3B: FF              RST     0X38                
6E3C: 7E              LD      A,(HL)              
6E3D: 7E              LD      A,(HL)              
6E3E: 00              NOP                         
6E3F: 00              NOP                         
6E40: 24              INC     H                   
6E41: FC                              
6E42: 9C              SBC     H                   
6E43: FC                              
6E44: 42              LD      B,D                 
6E45: FE 21           CP      $21                 
6E47: FF              RST     0X38                
6E48: 1D              DEC     E                   
6E49: FF              RST     0X38                
6E4A: 83              ADD     A,E                 
6E4B: FF              RST     0X38                
6E4C: 62              LD      H,D                 
6E4D: 7E              LD      A,(HL)              
6E4E: 9C              SBC     H                   
6E4F: 9C              SBC     H                   
6E50: 80              ADD     A,B                 
6E51: 80              ADD     A,B                 
6E52: 80              ADD     A,B                 
6E53: 80              ADD     A,B                 
6E54: 40              LD      B,B                 
6E55: C0              RET     NZ                  
6E56: 80              ADD     A,B                 
6E57: 80              ADD     A,B                 
6E58: 40              LD      B,B                 
6E59: C0              RET     NZ                  
6E5A: 80              ADD     A,B                 
6E5B: 80              ADD     A,B                 
6E5C: 00              NOP                         
6E5D: 00              NOP                         
6E5E: 00              NOP                         
6E5F: 00              NOP                         
6E60: 00              NOP                         
6E61: 00              NOP                         
6E62: 00              NOP                         
6E63: 00              NOP                         
6E64: 00              NOP                         
6E65: 18 18           JR      $6E7F               ; {}
6E67: 3C              INC     A                   
6E68: 18 3C           JR      $6EA6               ; {}
6E6A: 00              NOP                         
6E6B: 18 00           JR      $6E6D               ; {}
6E6D: 00              NOP                         
6E6E: 00              NOP                         
6E6F: 00              NOP                         
6E70: 00              NOP                         
6E71: 00              NOP                         
6E72: 00              NOP                         
6E73: 00              NOP                         
6E74: 00              NOP                         
6E75: 00              NOP                         
6E76: 00              NOP                         
6E77: 00              NOP                         
6E78: 00              NOP                         
6E79: 00              NOP                         
6E7A: 07              RLCA                        
6E7B: 00              NOP                         
6E7C: 0F              RRCA                        
6E7D: 07              RLCA                        
6E7E: 1F              RRA                         
6E7F: 0F              RRCA                        
6E80: 13              INC     DE                  
6E81: 0F              RRCA                        
6E82: 1D              DEC     E                   
6E83: 03              INC     BC                  
6E84: 1A              LD      A,(DE)              
6E85: 0D              DEC     C                   
6E86: 17              RLA                         
6E87: 0A              LD      A,(BC)              
6E88: 1D              DEC     E                   
6E89: 02              LD      (BC),A              
6E8A: 1F              RRA                         
6E8B: 00              NOP                         
6E8C: 3F              CCF                         
6E8D: 08 4F 32        LD      ($324F),SP          
6E90: 9B              SBC     E                   
6E91: 7C              LD      A,H                 
6E92: BD              CP      L                   
6E93: 7E              LD      A,(HL)              
6E94: 98              SBC     B                   
6E95: 7F              LD      A,A                 
6E96: 60              LD      H,B                 
6E97: 1F              RRA                         
6E98: 18 07           JR      $6EA1               ; {}
6E9A: 0E 01           LD      C,$01               
6E9C: 03              INC     BC                  
6E9D: 00              NOP                         
6E9E: 01 00 30        LD      BC,$3000            
6EA1: 30 48           JR      NC,$6EEB            ; {}
6EA3: 78              LD      A,B                 
6EA4: BC              CP      H                   
6EA5: FC                              
6EA6: 44              LD      B,H                 
6EA7: FC                              
6EA8: 84              ADD     A,H                 
6EA9: FC                              
6EAA: 3C              INC     A                   
6EAB: FC                              
6EAC: 44              LD      B,H                 
6EAD: FC                              
6EAE: 18 F8           JR      $6EA8               ; {}
6EB0: 28 F8           JR      Z,$6EAA             ; {}
6EB2: 86              ADD     A,(HL)              
6EB3: FE 81           CP      $81                 
6EB5: FF              RST     0X38                
6EB6: AF              XOR     A                   
6EB7: FF              RST     0X38                
6EB8: 81              ADD     A,C                 
6EB9: FF              RST     0X38                
6EBA: 9E              SBC     (HL)                
6EBB: FE 81           CP      $81                 
6EBD: FF              RST     0X38                
6EBE: 02              LD      (BC),A              
6EBF: FE 4C           CP      $4C                 
6EC1: FC                              
6EC2: 38 F8           JR      C,$6EBC             ; {}
6EC4: 84              ADD     A,H                 
6EC5: FC                              
6EC6: 44              LD      B,H                 
6EC7: FC                              
6EC8: 38 F8           JR      C,$6EC2             ; {}
6ECA: 84              ADD     A,H                 
6ECB: FC                              
6ECC: 44              LD      B,H                 
6ECD: 7C              LD      A,H                 
6ECE: B8              CP      B                   
6ECF: B8              CP      B                   
6ED0: 80              ADD     A,B                 
6ED1: 80              ADD     A,B                 
6ED2: 80              ADD     A,B                 
6ED3: 80              ADD     A,B                 
6ED4: 40              LD      B,B                 
6ED5: C0              RET     NZ                  
6ED6: 80              ADD     A,B                 
6ED7: 80              ADD     A,B                 
6ED8: 40              LD      B,B                 
6ED9: C0              RET     NZ                  
6EDA: 80              ADD     A,B                 
6EDB: 80              ADD     A,B                 
6EDC: 00              NOP                         
6EDD: 00              NOP                         
6EDE: 00              NOP                         
6EDF: 00              NOP                         
6EE0: 00              NOP                         
6EE1: 00              NOP                         
6EE2: 00              NOP                         
6EE3: 00              NOP                         
6EE4: 22              LD      (HLI),A             
6EE5: 22              LD      (HLI),A             
6EE6: 14              INC     D                   
6EE7: 14              INC     D                   
6EE8: 08 08 14        LD      ($1408),SP          
6EEB: 14              INC     D                   
6EEC: 22              LD      (HLI),A             
6EED: 22              LD      (HLI),A             
6EEE: 00              NOP                         
6EEF: 00              NOP                         
6EF0: 00              NOP                         
6EF1: 00              NOP                         
6EF2: 00              NOP                         
6EF3: 00              NOP                         
6EF4: 22              LD      (HLI),A             
6EF5: 22              LD      (HLI),A             
6EF6: 14              INC     D                   
6EF7: 14              INC     D                   
6EF8: 08 08 14        LD      ($1408),SP          
6EFB: 14              INC     D                   
6EFC: 22              LD      (HLI),A             
6EFD: 22              LD      (HLI),A             
6EFE: 00              NOP                         
6EFF: 00              NOP                         
6F00: 00              NOP                         
6F01: 00              NOP                         
6F02: 00              NOP                         
6F03: 00              NOP                         
6F04: 22              LD      (HLI),A             
6F05: 22              LD      (HLI),A             
6F06: 14              INC     D                   
6F07: 14              INC     D                   
6F08: 08 08 14        LD      ($1408),SP          
6F0B: 14              INC     D                   
6F0C: 22              LD      (HLI),A             
6F0D: 22              LD      (HLI),A             
6F0E: 00              NOP                         
6F0F: 00              NOP                         
6F10: 00              NOP                         
6F11: 00              NOP                         
6F12: 00              NOP                         
6F13: 00              NOP                         
6F14: 22              LD      (HLI),A             
6F15: 22              LD      (HLI),A             
6F16: 14              INC     D                   
6F17: 14              INC     D                   
6F18: 08 08 14        LD      ($1408),SP          
6F1B: 14              INC     D                   
6F1C: 22              LD      (HLI),A             
6F1D: 22              LD      (HLI),A             
6F1E: 00              NOP                         
6F1F: 00              NOP                         
6F20: 00              NOP                         
6F21: 00              NOP                         
6F22: 00              NOP                         
6F23: 00              NOP                         
6F24: 1C              INC     E                   
6F25: 1C              INC     E                   
6F26: 22              LD      (HLI),A             
6F27: 22              LD      (HLI),A             
6F28: 22              LD      (HLI),A             
6F29: 22              LD      (HLI),A             
6F2A: 22              LD      (HLI),A             
6F2B: 22              LD      (HLI),A             
6F2C: 1C              INC     E                   
6F2D: 1C              INC     E                   
6F2E: 00              NOP                         
6F2F: 00              NOP                         
6F30: 00              NOP                         
6F31: 00              NOP                         
6F32: 00              NOP                         
6F33: 00              NOP                         
6F34: 00              NOP                         
6F35: 00              NOP                         
6F36: 00              NOP                         
6F37: 00              NOP                         
6F38: 00              NOP                         
6F39: 00              NOP                         
6F3A: 00              NOP                         
6F3B: 00              NOP                         
6F3C: 00              NOP                         
6F3D: 00              NOP                         
6F3E: 00              NOP                         
6F3F: 00              NOP                         
6F40: 07              RLCA                        
6F41: 00              NOP                         
6F42: 08 07 17        LD      ($1707),SP          
6F45: 0F              RRCA                        
6F46: 2F              CPL                         
6F47: 1F              RRA                         
6F48: 4F              LD      C,A                 
6F49: 3F              CCF                         
6F4A: E3                              
6F4B: 1F              RRA                         
6F4C: 9B              SBC     E                   
6F4D: 67              LD      H,A                 
6F4E: 8E              ADC     A,(HL)              
6F4F: 71              LD      (HL),C              
6F50: 83              ADD     A,E                 
6F51: 7C              LD      A,H                 
6F52: 80              ADD     A,B                 
6F53: 7F              LD      A,A                 
6F54: 60              LD      H,B                 
6F55: 1F              RRA                         
6F56: 1C              INC     E                   
6F57: 03              INC     BC                  
6F58: 06 01           LD      B,$01               
6F5A: 01 00 00        LD      BC,$0000            
6F5D: 00              NOP                         
6F5E: 00              NOP                         
6F5F: 00              NOP                         
6F60: 00              NOP                         
6F61: 00              NOP                         
6F62: C0              RET     NZ                  
6F63: 00              NOP                         
6F64: B0              OR      B                   
6F65: C0              RET     NZ                  
6F66: CC F0 FA        CALL    Z,$FAF0             
6F69: FC                              
6F6A: F5              PUSH    AF                  
6F6B: FA C9 F6        LD      A,($F6C9)           
6F6E: D1              POP     DE                  
6F6F: EE B1           XOR     $B1                 
6F71: 4E              LD      C,(HL)              
6F72: 42              LD      B,D                 
6F73: BC              CP      H                   
6F74: 44              LD      B,H                 
6F75: B8              CP      B                   
6F76: 48              LD      C,B                 
6F77: B0              OR      B                   
6F78: 50              LD      D,B                 
6F79: A0              AND     B                   
6F7A: E0 00           LD      ($FF00+$00),A       
6F7C: 00              NOP                         
6F7D: 00              NOP                         
6F7E: 00              NOP                         
6F7F: 00              NOP                         
6F80: C0              RET     NZ                  
6F81: D0              RET     NC                  
6F82: C0              RET     NZ                  
6F83: C8              RET     Z                   
6F84: 00              NOP                         
6F85: 08 39 00        LD      ($0039),SP          
6F88: 77              LD      (HL),A              
6F89: 38 FD           JR      C,$6F88             ; {}
6F8B: 1B              DEC     DE                  
6F8C: F4                              
6F8D: BB              CP      E                   
6F8E: 7E              LD      A,(HL)              
6F8F: C1              POP     BC                  
6F90: B7              OR      A                   
6F91: 68              LD      L,B                 
6F92: 7F              LD      A,A                 
6F93: 26 DF           LD      H,$DF               
6F95: 6E              LD      L,(HL)              
6F96: AF              XOR     A                   
6F97: DD                              
6F98: CF              RST     0X08                
6F99: 33              INC     SP                  
6F9A: 4F              LD      C,A                 
6F9B: 3F              CCF                         
6F9C: 30 0F           JR      NC,$6FAD            ; {}
6F9E: 0F              RRCA                        
6F9F: 00              NOP                         
6FA0: 00              NOP                         
6FA1: 00              NOP                         
6FA2: 70              LD      (HL),B              
6FA3: 00              NOP                         
6FA4: D0              RET     NC                  
6FA5: 60              LD      H,B                 
6FA6: D0              RET     NC                  
6FA7: E0 C8           LD      ($FF00+$C8),A       
6FA9: 30 AB           JR      NC,$6F56            ; {}
6FAB: D0              RET     NC                  
6FAC: 1F              RRA                         
6FAD: E3                              
6FAE: CC 37 FB        CALL    Z,$FB37             
6FB1: 07              RLCA                        
6FB2: FB              EI                          
6FB3: 07              RLCA                        
6FB4: EC                              
6FB5: 57              LD      D,A                 
6FB6: EF              RST     0X28                
6FB7: F3              DI                          
6FB8: DB                              
6FB9: E0 38           LD      ($FF00+$38),A       
6FBB: C0              RET     NZ                  
6FBC: 74              LD      (HL),H              
6FBD: B8              CP      B                   
6FBE: B2              OR      D                   
6FBF: 1C              INC     E                   
6FC0: 00              NOP                         
6FC1: D0              RET     NC                  
6FC2: 00              NOP                         
6FC3: C8              RET     Z                   
6FC4: 00              NOP                         
6FC5: 08 39 00        LD      ($0039),SP          
6FC8: 77              LD      (HL),A              
6FC9: 38 FD           JR      C,$6FC8             ; {}
6FCB: 1B              DEC     DE                  
6FCC: F4                              
6FCD: BB              CP      E                   
6FCE: 7E              LD      A,(HL)              
6FCF: C1              POP     BC                  
6FD0: B7              OR      A                   
6FD1: 68              LD      L,B                 
6FD2: FF              RST     0X38                
6FD3: A7              AND     A                   
6FD4: DF              RST     0X18                
6FD5: EF              RST     0X28                
6FD6: AF              XOR     A                   
6FD7: 5E              LD      E,(HL)              
6FD8: 4F              LD      C,A                 
6FD9: 31 4F 3F        LD      SP,$3F4F            
6FDC: 30 0F           JR      NC,$6FED            ; {}
6FDE: 0F              RRCA                        
6FDF: 00              NOP                         
6FE0: 00              NOP                         
6FE1: 00              NOP                         
6FE2: 70              LD      (HL),B              
6FE3: 00              NOP                         
6FE4: F0 60           LD      A,($60)             
6FE6: F0 E0           LD      A,($E0)             
6FE8: F8 30           LD      HL,SP+$30           
6FEA: BB              CP      E                   
6FEB: D0              RET     NC                  
6FEC: 1F              RRA                         
6FED: E2              LD      (C),A               
6FEE: CD 36 FB        CALL    $FB36               
6FF1: 06 FB           LD      B,$FB               
6FF3: 06 ED           LD      B,$ED               
6FF5: 56              LD      D,(HL)              
6FF6: EF              RST     0X28                
6FF7: F2                              
6FF8: DB                              
6FF9: E0 38           LD      ($FF00+$38),A       
6FFB: C0              RET     NZ                  
6FFC: 7C              LD      A,H                 
6FFD: B8              CP      B                   
6FFE: BE              CP      (HL)                
6FFF: 1C              INC     E                   
7000: 00              NOP                         
7001: 00              NOP                         
7002: 00              NOP                         
7003: 00              NOP                         
7004: 00              NOP                         
7005: 00              NOP                         
7006: 00              NOP                         
7007: 00              NOP                         
7008: 00              NOP                         
7009: 00              NOP                         
700A: 00              NOP                         
700B: 00              NOP                         
700C: 00              NOP                         
700D: 00              NOP                         
700E: 00              NOP                         
700F: 00              NOP                         
7010: 01 00 01        LD      BC,$0100            
7013: 00              NOP                         
7014: 00              NOP                         
7015: 00              NOP                         
7016: 00              NOP                         
7017: 00              NOP                         
7018: 01 00 01        LD      BC,$0100            
701B: 00              NOP                         
701C: 06 01           LD      B,$01               
701E: 0A              LD      A,(BC)              
701F: 05              DEC     B                   
7020: 00              NOP                         
7021: 00              NOP                         
7022: 00              NOP                         
7023: 00              NOP                         
7024: 00              NOP                         
7025: 00              NOP                         
7026: 00              NOP                         
7027: 00              NOP                         
7028: 01 00 02        LD      BC,$0200            
702B: 01 03 00        LD      BC,$0003            
702E: CC 03 33        CALL    Z,$3303             
7031: CF              RST     0X08                
7032: 4F              LD      C,A                 
7033: BC              CP      H                   
7034: 9F              SBC     A                   
7035: 70              LD      (HL),B              
7036: BF              CP      A                   
7037: 60              LD      H,B                 
7038: 7F              LD      A,A                 
7039: C0              RET     NZ                  
703A: 7F              LD      A,A                 
703B: C0              RET     NZ                  
703C: FE 81           CP      $81                 
703E: FD                              
703F: 83              ADD     A,E                 
7040: 0A              LD      A,(BC)              
7041: 05              DEC     B                   
7042: 06 01           LD      B,$01               
7044: 01 00 01        LD      BC,$0100            
7047: 00              NOP                         
7048: 02              LD      (BC),A              
7049: 01 02 01        LD      BC,$0102            
704C: 01 00 00        LD      BC,$0000            
704F: 00              NOP                         
7050: 00              NOP                         
7051: 00              NOP                         
7052: 00              NOP                         
7053: 00              NOP                         
7054: 00              NOP                         
7055: 00              NOP                         
7056: 00              NOP                         
7057: 00              NOP                         
7058: 00              NOP                         
7059: 00              NOP                         
705A: 00              NOP                         
705B: 00              NOP                         
705C: 00              NOP                         
705D: 00              NOP                         
705E: 00              NOP                         
705F: 00              NOP                         
7060: FD                              
7061: 83              ADD     A,E                 
7062: FE 81           CP      $81                 
7064: 7F              LD      A,A                 
7065: C0              RET     NZ                  
7066: 7F              LD      A,A                 
7067: C0              RET     NZ                  
7068: DD                              
7069: 3E BE           LD      A,$BE               
706B: 7F              LD      A,A                 
706C: FF              RST     0X38                
706D: 67              LD      H,A                 
706E: FF              RST     0X38                
706F: 63              LD      H,E                 
7070: BE              CP      (HL)                
7071: 73              LD      (HL),E              
7072: 5D              LD      E,L                 
7073: 3E 3E           LD      A,$3E               
7075: 00              NOP                         
7076: 48              LD      C,B                 
7077: 30 90           JR      NC,$7009            ; {}
7079: 60              LD      H,B                 
707A: B0              OR      B                   
707B: 60              LD      H,B                 
707C: B0              OR      B                   
707D: 60              LD      H,B                 
707E: 60              LD      H,B                 
707F: 00              NOP                         
7080: 00              NOP                         
7081: 00              NOP                         
7082: 00              NOP                         
7083: 00              NOP                         
7084: 00              NOP                         
7085: 00              NOP                         
7086: 00              NOP                         
7087: 00              NOP                         
7088: 00              NOP                         
7089: 00              NOP                         
708A: 00              NOP                         
708B: 00              NOP                         
708C: 00              NOP                         
708D: 00              NOP                         
708E: 00              NOP                         
708F: 00              NOP                         
7090: 71              LD      (HL),C              
7091: 00              NOP                         
7092: 8A              ADC     A,D                 
7093: 71              LD      (HL),C              
7094: E5              PUSH    HL                  
7095: 7B              LD      A,E                 
7096: 77              LD      (HL),A              
7097: 0B              DEC     BC                  
7098: 0F              RRCA                        
7099: 02              LD      (BC),A              
709A: 07              RLCA                        
709B: 02              LD      (BC),A              
709C: 05              DEC     B                   
709D: 03              INC     BC                  
709E: 02              LD      (BC),A              
709F: 01 00 00        LD      BC,$0000            
70A2: 00              NOP                         
70A3: 00              NOP                         
70A4: 00              NOP                         
70A5: 00              NOP                         
70A6: 00              NOP                         
70A7: 00              NOP                         
70A8: 01 00 02        LD      BC,$0200            
70AB: 01 33 00        LD      BC,$0033            
70AE: 4C              LD      C,H                 
70AF: 33              INC     SP                  
70B0: F3              DI                          
70B1: 0F              RRCA                        
70B2: DF              RST     0X18                
70B3: EC                              
70B4: EF              RST     0X28                
70B5: F0 FF           LD      A,($FF)             
70B7: 30 FF           JR      NC,$70B8            ; {}
70B9: 30 FF           JR      NC,$70BA            ; {}
70BB: 70              LD      (HL),B              
70BC: EE F1           XOR     $F1                 
70BE: DD                              
70BF: E3                              
70C0: 0A              LD      A,(BC)              
70C1: 05              DEC     B                   
70C2: 05              DEC     B                   
70C3: 03              INC     BC                  
70C4: 3F              CCF                         
70C5: 03              INC     BC                  
70C6: 47              LD      B,A                 
70C7: 3B              DEC     SP                  
70C8: 8F              ADC     A,A                 
70C9: 73              LD      (HL),E              
70CA: D5              PUSH    DE                  
70CB: 63              LD      H,E                 
70CC: 63              LD      H,E                 
70CD: 00              NOP                         
70CE: 00              NOP                         
70CF: 00              NOP                         
70D0: 00              NOP                         
70D1: 00              NOP                         
70D2: 00              NOP                         
70D3: 00              NOP                         
70D4: 00              NOP                         
70D5: 00              NOP                         
70D6: 00              NOP                         
70D7: 00              NOP                         
70D8: 00              NOP                         
70D9: 00              NOP                         
70DA: 00              NOP                         
70DB: 00              NOP                         
70DC: 00              NOP                         
70DD: 00              NOP                         
70DE: 00              NOP                         
70DF: 00              NOP                         
70E0: DD                              
70E1: E3                              
70E2: EE F1           XOR     $F1                 
70E4: FF              RST     0X38                
70E5: 30 FF           JR      NC,$70E6            ; {}
70E7: 30 ED           JR      NC,$70D6            ; {}
70E9: 3E FE           LD      A,$FE               
70EB: FF              RST     0X38                
70EC: 3F              CCF                         
70ED: E3                              
70EE: BF              CP      A                   
70EF: 63              LD      H,E                 
70F0: 7E              LD      A,(HL)              
70F1: 3F              CCF                         
70F2: 5D              LD      E,L                 
70F3: 3E 3E           LD      A,$3E               
70F5: 01 15 08        LD      BC,$0815            
70F8: 24              INC     H                   
70F9: 18 64           JR      $715F               ; {}
70FB: 38 48           JR      C,$7145             ; {}
70FD: 30 30           JR      NC,$712F            ; {}
70FF: 00              NOP                         
7100: E7              RST     0X20                
7101: 00              NOP                         
7102: B8              CP      B                   
7103: 47              LD      B,A                 
7104: E7              RST     0X20                
7105: 1F              RRA                         
7106: 4F              LD      C,A                 
7107: 38 5F           JR      C,$7168             ; {}
7109: 30 BF           JR      NC,$70CA            ; {}
710B: 60              LD      H,B                 
710C: BE              CP      (HL)                
710D: 61              LD      H,C                 
710E: BD              CP      L                   
710F: 63              LD      H,E                 
7110: BD              CP      L                   
7111: 63              LD      H,E                 
7112: BE              CP      (HL)                
7113: 61              LD      H,C                 
7114: BF              CP      A                   
7115: 60              LD      H,B                 
7116: 5F              LD      E,A                 
7117: 30 4F           JR      NC,$7168            ; {}
7119: 38 E7           JR      C,$7102             ; {}
711B: 1F              RRA                         
711C: B8              CP      B                   
711D: 47              LD      B,A                 
711E: E7              RST     0X20                
711F: 00              NOP                         
7120: 00              NOP                         
7121: 00              NOP                         
7122: 73              LD      (HL),E              
7123: 00              NOP                         
7124: 5C              LD      E,H                 
7125: 23              INC     HL                  
7126: 73              LD      (HL),E              
7127: 0F              RRCA                        
7128: 27              DAA                         
7129: 1C              INC     E                   
712A: 2F              CPL                         
712B: 18 5F           JR      $718C               ; {}
712D: 30 5E           JR      NC,$718D            ; {}
712F: 31 5E 31        LD      SP,$315E            
7132: 5F              LD      E,A                 
7133: 30 2F           JR      NC,$7164            ; {}
7135: 18 27           JR      $715E               ; {}
7137: 1C              INC     E                   
7138: 73              LD      (HL),E              
7139: 0F              RRCA                        
713A: 5C              LD      E,H                 
713B: 23              INC     HL                  
713C: 73              LD      (HL),E              
713D: 00              NOP                         
713E: 00              NOP                         
713F: 00              NOP                         
7140: 01 00 03        LD      BC,$0300            
7143: 01 03 01        LD      BC,$0103            
7146: 0F              RRCA                        
7147: 01 12 0D        LD      BC,$0D12            
714A: 17              RLA                         
714B: 08 7F 00        LD      ($007F),SP          
714E: F7              RST     0X30                
714F: 79              LD      A,C                 
7150: F7              RST     0X30                
7151: 79              LD      A,C                 
7152: 7F              LD      A,A                 
7153: 00              NOP                         
7154: 17              RLA                         
7155: 08 12 0D        LD      ($0D12),SP          
7158: 0F              RRCA                        
7159: 01 03 01        LD      BC,$0103            
715C: 03              INC     BC                  
715D: 01 01 00        LD      BC,$0001            
7160: 00              NOP                         
7161: 00              NOP                         
7162: 30 00           JR      NC,$7164            ; {}
7164: 79              LD      A,C                 
7165: 30 77           JR      NC,$71DE            ; {}
7167: 39              ADD     HL,SP               
7168: 23              INC     HL                  
7169: 1D              DEC     E                   
716A: 13              INC     DE                  
716B: 0C              INC     C                   
716C: 1F              RRA                         
716D: 00              NOP                         
716E: 3F              CCF                         
716F: 19              ADD     HL,DE               
7170: 3F              CCF                         
7171: 19              ADD     HL,DE               
7172: 1F              RRA                         
7173: 00              NOP                         
7174: 13              INC     DE                  
7175: 0C              INC     C                   
7176: 23              INC     HL                  
7177: 1D              DEC     E                   
7178: 77              LD      (HL),A              
7179: 39              ADD     HL,SP               
717A: 79              LD      A,C                 
717B: 30 30           JR      NC,$71AD            ; {}
717D: 00              NOP                         
717E: 00              NOP                         
717F: 00              NOP                         
7180: 00              NOP                         
7181: FF              RST     0X38                
7182: 00              NOP                         
7183: FF              RST     0X38                
7184: 22              LD      (HLI),A             
7185: DD                              
7186: 14              INC     D                   
7187: EB                              
7188: 08 F7 14        LD      ($14F7),SP          
718B: EB                              
718C: 22              LD      (HLI),A             
718D: DD                              
718E: 00              NOP                         
718F: FF              RST     0X38                
7190: 00              NOP                         
7191: FF              RST     0X38                
7192: 00              NOP                         
7193: FF              RST     0X38                
7194: 22              LD      (HLI),A             
7195: DD                              
7196: 14              INC     D                   
7197: EB                              
7198: 08 F7 14        LD      ($14F7),SP          
719B: EB                              
719C: 22              LD      (HLI),A             
719D: DD                              
719E: 00              NOP                         
719F: FF              RST     0X38                
71A0: 00              NOP                         
71A1: FF              RST     0X38                
71A2: 00              NOP                         
71A3: FF              RST     0X38                
71A4: 22              LD      (HLI),A             
71A5: DD                              
71A6: 14              INC     D                   
71A7: EB                              
71A8: 08 F7 14        LD      ($14F7),SP          
71AB: EB                              
71AC: 22              LD      (HLI),A             
71AD: DD                              
71AE: 00              NOP                         
71AF: FF              RST     0X38                
71B0: 00              NOP                         
71B1: FF              RST     0X38                
71B2: 00              NOP                         
71B3: FF              RST     0X38                
71B4: 22              LD      (HLI),A             
71B5: DD                              
71B6: 14              INC     D                   
71B7: EB                              
71B8: 08 F7 14        LD      ($14F7),SP          
71BB: EB                              
71BC: 22              LD      (HLI),A             
71BD: DD                              
71BE: 00              NOP                         
71BF: FF              RST     0X38                
71C0: 00              NOP                         
71C1: FF              RST     0X38                
71C2: 00              NOP                         
71C3: FF              RST     0X38                
71C4: 22              LD      (HLI),A             
71C5: DD                              
71C6: 14              INC     D                   
71C7: EB                              
71C8: 08 F7 14        LD      ($14F7),SP          
71CB: EB                              
71CC: 22              LD      (HLI),A             
71CD: DD                              
71CE: 00              NOP                         
71CF: FF              RST     0X38                
71D0: 00              NOP                         
71D1: FF              RST     0X38                
71D2: 00              NOP                         
71D3: FF              RST     0X38                
71D4: 22              LD      (HLI),A             
71D5: DD                              
71D6: 14              INC     D                   
71D7: EB                              
71D8: 08 F7 14        LD      ($14F7),SP          
71DB: EB                              
71DC: 22              LD      (HLI),A             
71DD: DD                              
71DE: 00              NOP                         
71DF: FF              RST     0X38                
71E0: 00              NOP                         
71E1: FF              RST     0X38                
71E2: 00              NOP                         
71E3: FF              RST     0X38                
71E4: 22              LD      (HLI),A             
71E5: DD                              
71E6: 14              INC     D                   
71E7: EB                              
71E8: 08 F7 14        LD      ($14F7),SP          
71EB: EB                              
71EC: 22              LD      (HLI),A             
71ED: DD                              
71EE: 00              NOP                         
71EF: FF              RST     0X38                
71F0: 00              NOP                         
71F1: FF              RST     0X38                
71F2: 00              NOP                         
71F3: FF              RST     0X38                
71F4: 22              LD      (HLI),A             
71F5: DD                              
71F6: 14              INC     D                   
71F7: EB                              
71F8: 08 F7 14        LD      ($14F7),SP          
71FB: EB                              
71FC: 22              LD      (HLI),A             
71FD: DD                              
71FE: 00              NOP                         
71FF: FF              RST     0X38                
7200: 00              NOP                         
7201: 00              NOP                         
7202: 00              NOP                         
7203: 00              NOP                         
7204: 00              NOP                         
7205: 30 30           JR      NC,$7237            ; {}
7207: 48              LD      C,B                 
7208: 40              LD      B,B                 
7209: 80              ADD     A,B                 
720A: 00              NOP                         
720B: 80              ADD     A,B                 
720C: 1E 01           LD      E,$01               
720E: 3F              CCF                         
720F: 00              NOP                         
7210: 27              DAA                         
7211: 18 03           JR      $7216               ; {}
7213: 24              INC     H                   
7214: 01 02 00        LD      BC,$0002            
7217: 01 00 00        LD      BC,$0000            
721A: 00              NOP                         
721B: 00              NOP                         
721C: 00              NOP                         
721D: 00              NOP                         
721E: 00              NOP                         
721F: 00              NOP                         
7220: 00              NOP                         
7221: 00              NOP                         
7222: 00              NOP                         
7223: 00              NOP                         
7224: 00              NOP                         
7225: 00              NOP                         
7226: 00              NOP                         
7227: 00              NOP                         
7228: 00              NOP                         
7229: 00              NOP                         
722A: 00              NOP                         
722B: 10 00           ;;STOP    $00                 
722D: 08 03 84        LD      ($8403),SP          
7230: C0              RET     NZ                  
7231: 20 F0           JR      NZ,$7223            ; {}
7233: 08 FF 00        LD      ($00FF),SP          
7236: FF              RST     0X38                
7237: 00              NOP                         
7238: 3F              CCF                         
7239: C0              RET     NZ                  
723A: 0F              RRCA                        
723B: 30 00           JR      NC,$723D            ; {}
723D: 0F              RRCA                        
723E: 00              NOP                         
723F: 00              NOP                         
7240: 00              NOP                         
7241: 3C              INC     A                   
7242: 0C              INC     C                   
7243: 72              LD      (HL),D              
7244: 1A              LD      A,(DE)              
7245: FD                              
7246: 3D              DEC     A                   
7247: FE 1C           CP      $1C                 
7249: FF              RST     0X38                
724A: 0C              INC     C                   
724B: FF              RST     0X38                
724C: 00              NOP                         
724D: FF              RST     0X38                
724E: 00              NOP                         
724F: FF              RST     0X38                
7250: 00              NOP                         
7251: FF              RST     0X38                
7252: 00              NOP                         
7253: 7F              LD      A,A                 
7254: 00              NOP                         
7255: 7F              LD      A,A                 
7256: 00              NOP                         
7257: 3F              CCF                         
7258: 01 1E 02        LD      BC,$021E            
725B: 0D              DEC     C                   
725C: 00              NOP                         
725D: 00              NOP                         
725E: 00              NOP                         
725F: 00              NOP                         
7260: 07              RLCA                        
7261: 00              NOP                         
7262: 0A              LD      A,(BC)              
7263: 07              RLCA                        
7264: 0E 07           LD      C,$07               
7266: 0F              RRCA                        
7267: 90              SUB     B                   
7268: 9F              SBC     A                   
7269: 40              LD      B,B                 
726A: 9F              SBC     A                   
726B: 40              LD      B,B                 
726C: 5F              LD      E,A                 
726D: 80              ADD     A,B                 
726E: 4F              LD      C,A                 
726F: 90              SUB     B                   
7270: 47              LD      B,A                 
7271: 88              ADC     A,B                 
7272: 40              LD      B,B                 
7273: 83              ADD     A,E                 
7274: 83              ADD     A,E                 
7275: 53              LD      D,E                 
7276: 88              ADC     A,B                 
7277: 14              INC     D                   
7278: 04              INC     B                   
7279: 9B              SBC     E                   
727A: 03              INC     BC                  
727B: 0C              INC     C                   
727C: 00              NOP                         
727D: 07              RLCA                        
727E: 00              NOP                         
727F: 00              NOP                         
7280: 00              NOP                         
7281: 00              NOP                         
7282: 00              NOP                         
7283: 00              NOP                         
7284: 00              NOP                         
7285: 00              NOP                         
7286: 00              NOP                         
7287: 00              NOP                         
7288: 00              NOP                         
7289: 00              NOP                         
728A: 00              NOP                         
728B: 00              NOP                         
728C: 01 00 02        LD      BC,$0200            
728F: 01 03 00        LD      BC,$0003            
7292: 01 00 00        LD      BC,$0000            
7295: 00              NOP                         
7296: 00              NOP                         
7297: 00              NOP                         
7298: 00              NOP                         
7299: 00              NOP                         
729A: 00              NOP                         
729B: 00              NOP                         
729C: 00              NOP                         
729D: 00              NOP                         
729E: 00              NOP                         
729F: 00              NOP                         
72A0: 00              NOP                         
72A1: 00              NOP                         
72A2: 00              NOP                         
72A3: 00              NOP                         
72A4: 00              NOP                         
72A5: 00              NOP                         
72A6: 00              NOP                         
72A7: 00              NOP                         
72A8: 03              INC     BC                  
72A9: 00              NOP                         
72AA: 04              INC     B                   
72AB: 03              INC     BC                  
72AC: 08 07 0B        LD      ($0B07),SP          
72AF: 04              INC     B                   
72B0: 0F              RRCA                        
72B1: 00              NOP                         
72B2: 0F              RRCA                        
72B3: 00              NOP                         
72B4: 07              RLCA                        
72B5: 00              NOP                         
72B6: 03              INC     BC                  
72B7: 00              NOP                         
72B8: 00              NOP                         
72B9: 00              NOP                         
72BA: 00              NOP                         
72BB: 00              NOP                         
72BC: 00              NOP                         
72BD: 00              NOP                         
72BE: 00              NOP                         
72BF: 00              NOP                         
72C0: 00              NOP                         
72C1: 00              NOP                         
72C2: 00              NOP                         
72C3: 00              NOP                         
72C4: 0F              RRCA                        
72C5: 00              NOP                         
72C6: 10 0F           ;;STOP    $0F                 
72C8: 20 1F           JR      NZ,$72E9            ; {}
72CA: 27              DAA                         
72CB: 18 2F           JR      $72FC               ; {}
72CD: 10 3F           ;;STOP    $3F                 
72CF: 00              NOP                         
72D0: 3F              CCF                         
72D1: 00              NOP                         
72D2: 3F              CCF                         
72D3: 00              NOP                         
72D4: 3F              CCF                         
72D5: 00              NOP                         
72D6: 3F              CCF                         
72D7: 00              NOP                         
72D8: 1F              RRA                         
72D9: 00              NOP                         
72DA: 0F              RRCA                        
72DB: 00              NOP                         
72DC: 00              NOP                         
72DD: 00              NOP                         
72DE: 00              NOP                         
72DF: 00              NOP                         
72E0: 1F              RRA                         
72E1: 00              NOP                         
72E2: 20 1F           JR      NZ,$7303            ; {}
72E4: 40              LD      B,B                 
72E5: 3F              CCF                         
72E6: 9F              SBC     A                   
72E7: 60              LD      H,B                 
72E8: BF              CP      A                   
72E9: 40              LD      B,B                 
72EA: FF              RST     0X38                
72EB: 00              NOP                         
72EC: FF              RST     0X38                
72ED: 00              NOP                         
72EE: FF              RST     0X38                
72EF: 00              NOP                         
72F0: FF              RST     0X38                
72F1: 00              NOP                         
72F2: FF              RST     0X38                
72F3: 00              NOP                         
72F4: FF              RST     0X38                
72F5: 00              NOP                         
72F6: FF              RST     0X38                
72F7: 00              NOP                         
72F8: FF              RST     0X38                
72F9: 00              NOP                         
72FA: 7F              LD      A,A                 
72FB: 00              NOP                         
72FC: 3F              CCF                         
72FD: 00              NOP                         
72FE: 1F              RRA                         
72FF: 00              NOP                         
7300: 00              NOP                         
7301: 00              NOP                         
7302: 00              NOP                         
7303: 00              NOP                         
7304: 60              LD      H,B                 
7305: 00              NOP                         
7306: 18 00           JR      $7308               ; {}
7308: 0E 00           LD      C,$00               
730A: 03              INC     BC                  
730B: 00              NOP                         
730C: 01 00 00        LD      BC,$0000            
730F: 00              NOP                         
7310: 00              NOP                         
7311: 02              LD      (BC),A              
7312: 00              NOP                         
7313: 01 00 00        LD      BC,$0000            
7316: 00              NOP                         
7317: 00              NOP                         
7318: 00              NOP                         
7319: 00              NOP                         
731A: 00              NOP                         
731B: 00              NOP                         
731C: 00              NOP                         
731D: 00              NOP                         
731E: 00              NOP                         
731F: 00              NOP                         
7320: 00              NOP                         
7321: 00              NOP                         
7322: 00              NOP                         
7323: 00              NOP                         
7324: 00              NOP                         
7325: 00              NOP                         
7326: 00              NOP                         
7327: 00              NOP                         
7328: 00              NOP                         
7329: 00              NOP                         
732A: 00              NOP                         
732B: 00              NOP                         
732C: 80              ADD     A,B                 
732D: 00              NOP                         
732E: C0              RET     NZ                  
732F: 00              NOP                         
7330: 60              LD      H,B                 
7331: 00              NOP                         
7332: 30 00           JR      NC,$7334            ; {}
7334: 98              SBC     B                   
7335: 40              LD      B,B                 
7336: 4C              LD      C,H                 
7337: 20 26           JR      NZ,$735F            ; {}
7339: 10 13           ;;STOP    $13                 
733B: 08 00 00        LD      ($0000),SP          
733E: 00              NOP                         
733F: 00              NOP                         
7340: 00              NOP                         
7341: 00              NOP                         
7342: 00              NOP                         
7343: 00              NOP                         
7344: 70              LD      (HL),B              
7345: 00              NOP                         
7346: 3C              INC     A                   
7347: 00              NOP                         
7348: 1F              RRA                         
7349: 00              NOP                         
734A: 0F              RRCA                        
734B: 00              NOP                         
734C: 07              RLCA                        
734D: 00              NOP                         
734E: 03              INC     BC                  
734F: 10 01           ;;STOP    $01                 
7351: 08 04 02        LD      ($0204),SP          
7354: 02              LD      (BC),A              
7355: 01 01 00        LD      BC,$0001            
7358: 00              NOP                         
7359: 00              NOP                         
735A: 00              NOP                         
735B: 00              NOP                         
735C: 00              NOP                         
735D: 00              NOP                         
735E: 00              NOP                         
735F: 00              NOP                         
7360: 00              NOP                         
7361: 00              NOP                         
7362: 00              NOP                         
7363: 00              NOP                         
7364: 00              NOP                         
7365: 08 00 04        LD      ($0400),SP          
7368: 00              NOP                         
7369: 02              LD      (BC),A              
736A: 80              ADD     A,B                 
736B: 02              LD      (BC),A              
736C: C0              RET     NZ                  
736D: 01 A0 41        LD      BC,$41A0            
7370: D0              RET     NC                  
7371: 21 F8 00        LD      HL,$00F8            
7374: 7C              LD      A,H                 
7375: 00              NOP                         
7376: 1E 80           LD      E,$80               
7378: C7              RST     0X00                
7379: 20 31           JR      NZ,$73AC            ; {}
737B: 02              LD      (BC),A              
737C: 00              NOP                         
737D: 01 00 00        LD      BC,$0000            
7380: 1F              RRA                         
7381: 00              NOP                         
7382: 3F              CCF                         
7383: 00              NOP                         
7384: 5F              LD      E,A                 
7385: 20 7F           JR      NZ,$7406            ; {}
7387: 00              NOP                         
7388: 3F              CCF                         
7389: 00              NOP                         
738A: 3F              CCF                         
738B: 00              NOP                         
738C: 1F              RRA                         
738D: 00              NOP                         
738E: 0F              RRCA                        
738F: 40              LD      B,B                 
7390: 07              RLCA                        
7391: 20 13           JR      NZ,$73A6            ; {}
7393: 08 09 04        LD      ($0409),SP          
7396: 04              INC     B                   
7397: 02              LD      (BC),A              
7398: 03              INC     BC                  
7399: 00              NOP                         
739A: 00              NOP                         
739B: 00              NOP                         
739C: 00              NOP                         
739D: 00              NOP                         
739E: 00              NOP                         
739F: 00              NOP                         
73A0: 00              NOP                         
73A1: 08 C0 04        LD      ($04C0),SP          
73A4: E2              LD      (C),A               
73A5: 00              NOP                         
73A6: F1              POP     AF                  
73A7: 00              NOP                         
73A8: F9              LD      SP,HL               
73A9: 00              NOP                         
73AA: 7C              LD      A,H                 
73AB: C1              POP     BC                  
73AC: BC              CP      H                   
73AD: 60              LD      H,B                 
73AE: DE 20           SBC     $20                 
73B0: FE 00           CP      $00                 
73B2: FF              RST     0X38                
73B3: 00              NOP                         
73B4: FF              RST     0X38                
73B5: 00              NOP                         
73B6: 7F              LD      A,A                 
73B7: 00              NOP                         
73B8: 1D              DEC     E                   
73B9: 82              ADD     A,D                 
73BA: C7              RST     0X00                
73BB: 00              NOP                         
73BC: 00              NOP                         
73BD: 00              NOP                         
73BE: 00              NOP                         
73BF: 00              NOP                         
73C0: 00              NOP                         
73C1: 00              NOP                         
73C2: 00              NOP                         
73C3: 00              NOP                         
73C4: 00              NOP                         
73C5: 00              NOP                         
73C6: 00              NOP                         
73C7: 00              NOP                         
73C8: 00              NOP                         
73C9: 00              NOP                         
73CA: 00              NOP                         
73CB: 00              NOP                         
73CC: 00              NOP                         
73CD: 00              NOP                         
73CE: 00              NOP                         
73CF: 0C              INC     C                   
73D0: 00              NOP                         
73D1: 10 07           ;;STOP    $07                 
73D3: 00              NOP                         
73D4: 08 07 00        LD      ($0007),SP          
73D7: 08 00 00        LD      ($0000),SP          
73DA: 00              NOP                         
73DB: 00              NOP                         
73DC: 00              NOP                         
73DD: 00              NOP                         
73DE: 00              NOP                         
73DF: 00              NOP                         
73E0: 00              NOP                         
73E1: 00              NOP                         
73E2: 00              NOP                         
73E3: 00              NOP                         
73E4: 00              NOP                         
73E5: 00              NOP                         
73E6: 00              NOP                         
73E7: 00              NOP                         
73E8: 00              NOP                         
73E9: 00              NOP                         
73EA: 00              NOP                         
73EB: 00              NOP                         
73EC: 00              NOP                         
73ED: 00              NOP                         
73EE: 00              NOP                         
73EF: 00              NOP                         
73F0: 00              NOP                         
73F1: 00              NOP                         
73F2: 00              NOP                         
73F3: 03              INC     BC                  
73F4: 80              ADD     A,B                 
73F5: 00              NOP                         
73F6: 60              LD      H,B                 
73F7: 80              ADD     A,B                 
73F8: 1F              RRA                         
73F9: 60              LD      H,B                 
73FA: 00              NOP                         
73FB: 1F              RRA                         
73FC: 00              NOP                         
73FD: 00              NOP                         
73FE: 00              NOP                         
73FF: 00              NOP                         
7400: 00              NOP                         
7401: 00              NOP                         
7402: 00              NOP                         
7403: 00              NOP                         
7404: 00              NOP                         
7405: 00              NOP                         
7406: 00              NOP                         
7407: 00              NOP                         
7408: 00              NOP                         
7409: 00              NOP                         
740A: 00              NOP                         
740B: 00              NOP                         
740C: 01 00 02        LD      BC,$0200            
740F: 01 04 03        LD      BC,$0304            
7412: 08 06 10        LD      ($1006),SP          
7415: 0C              INC     C                   
7416: 10 0B           ;;STOP    $0B                 
7418: 21 16 23        LD      HL,$2316            
741B: 14              INC     D                   
741C: 47              LD      B,A                 
741D: 38 4C           JR      C,$746B             ; {}
741F: 33              INC     SP                  
7420: 00              NOP                         
7421: 00              NOP                         
7422: 00              NOP                         
7423: 00              NOP                         
7424: 00              NOP                         
7425: 00              NOP                         
7426: 03              INC     BC                  
7427: 00              NOP                         
7428: 1C              INC     E                   
7429: 03              INC     BC                  
742A: 60              LD      H,B                 
742B: 1C              INC     E                   
742C: 80              ADD     A,B                 
742D: 60              LD      H,B                 
742E: 00              NOP                         
742F: 80              ADD     A,B                 
7430: 00              NOP                         
7431: 1F              RRA                         
7432: 00              NOP                         
7433: 7F              LD      A,A                 
7434: 0F              RRCA                        
7435: F0 7F           LD      A,($7F)             
7437: 80              ADD     A,B                 
7438: F0 0F           LD      A,($0F)             
743A: C0              RET     NZ                  
743B: 3F              CCF                         
743C: 00              NOP                         
743D: F0 00           LD      A,($00)             
743F: 80              ADD     A,B                 
7440: C8              RET     Z                   
7441: 36 D0           LD      (HL),$D0            
7443: 2C              INC     L                   
7444: D0              RET     NC                  
7445: 28 C0           JR      Z,$7407             ; {}
7447: 38 C0           JR      C,$7409             ; {}
7449: 38 60           JR      C,$74AB             ; {}
744B: 1C              INC     E                   
744C: 60              LD      H,B                 
744D: 1E 30           LD      E,$30               
744F: 0F              RRCA                        
7450: 38 07           JR      C,$7459             ; {}
7452: 1C              INC     E                   
7453: 03              INC     BC                  
7454: 0E 01           LD      C,$01               
7456: 07              RLCA                        
7457: 00              NOP                         
7458: 03              INC     BC                  
7459: 00              NOP                         
745A: 00              NOP                         
745B: 00              NOP                         
745C: 00              NOP                         
745D: 00              NOP                         
745E: 00              NOP                         
745F: 00              NOP                         
7460: 00              NOP                         
7461: 00              NOP                         
7462: 00              NOP                         
7463: 00              NOP                         
7464: 00              NOP                         
7465: 00              NOP                         
7466: 03              INC     BC                  
7467: 00              NOP                         
7468: 0C              INC     C                   
7469: 03              INC     BC                  
746A: 11 0F 23        LD      DE,$230F            
746D: 1D              DEC     E                   
746E: 27              DAA                         
746F: 18 27           JR      $7498               ; {}
7471: D8              RET     C                   
7472: 27              DAA                         
7473: D8              RET     C                   
7474: 2B              DEC     HL                  
7475: DC 94 6F        CALL    C,$6F94             ; {}
7478: EF              RST     0X28                
7479: 13              INC     DE                  
747A: FF              RST     0X38                
747B: 00              NOP                         
747C: 3F              CCF                         
747D: 00              NOP                         
747E: 03              INC     BC                  
747F: 00              NOP                         
7480: 00              NOP                         
7481: 00              NOP                         
7482: 00              NOP                         
7483: 00              NOP                         
7484: 00              NOP                         
7485: 00              NOP                         
7486: 00              NOP                         
7487: 00              NOP                         
7488: 00              NOP                         
7489: 00              NOP                         
748A: 01 00 02        LD      BC,$0200            
748D: 01 04 03        LD      BC,$0304            
7490: 04              INC     B                   
7491: 02              LD      (BC),A              
7492: 08 06 08        LD      ($0806),SP          
7495: 04              INC     B                   
7496: 10 0C           ;;STOP    $0C                 
7498: 10 09           ;;STOP    $09                 
749A: 30 0B           JR      NC,$74A7            ; {}
749C: 31 0E 33        LD      SP,$330E            
749F: 0C              INC     C                   
74A0: 00              NOP                         
74A1: 00              NOP                         
74A2: 0F              RRCA                        
74A3: 00              NOP                         
74A4: 30 0F           JR      NC,$74B5            ; {}
74A6: 40              LD      B,B                 
74A7: 3C              INC     A                   
74A8: 80              ADD     A,B                 
74A9: 70              LD      (HL),B              
74AA: 00              NOP                         
74AB: C0              RET     NZ                  
74AC: 00              NOP                         
74AD: 80              ADD     A,B                 
74AE: 00              NOP                         
74AF: 00              NOP                         
74B0: 00              NOP                         
74B1: 00              NOP                         
74B2: 00              NOP                         
74B3: 07              RLCA                        
74B4: 00              NOP                         
74B5: 3F              CCF                         
74B6: 00              NOP                         
74B7: FF              RST     0X38                
74B8: 1F              RRA                         
74B9: E0 7F           LD      ($FF00+$7F),A       
74BB: 80              ADD     A,B                 
74BC: E0 18           LD      ($FF00+$18),A       
74BE: 80              ADD     A,B                 
74BF: 60              LD      H,B                 
74C0: 33              INC     SP                  
74C1: 0C              INC     C                   
74C2: 36 09           LD      (HL),$09            
74C4: 34              INC     (HL)                
74C5: 0A              LD      A,(BC)              
74C6: 34              INC     (HL)                
74C7: 0A              LD      A,(BC)              
74C8: 30 0E           JR      NC,$74D8            ; {}
74CA: 38 06           JR      C,$74D2             ; {}
74CC: 18 07           JR      $74D5               ; {}
74CE: 1C              INC     E                   
74CF: 03              INC     BC                  
74D0: 0C              INC     C                   
74D1: 03              INC     BC                  
74D2: 0E 01           LD      C,$01               
74D4: 07              RLCA                        
74D5: 00              NOP                         
74D6: 03              INC     BC                  
74D7: 00              NOP                         
74D8: 01 00 00        LD      BC,$0000            
74DB: 00              NOP                         
74DC: 00              NOP                         
74DD: 00              NOP                         
74DE: 00              NOP                         
74DF: 00              NOP                         
74E0: 00              NOP                         
74E1: 00              NOP                         
74E2: 00              NOP                         
74E3: 00              NOP                         
74E4: 00              NOP                         
74E5: 00              NOP                         
74E6: 00              NOP                         
74E7: 00              NOP                         
74E8: 00              NOP                         
74E9: 00              NOP                         
74EA: 00              NOP                         
74EB: 00              NOP                         
74EC: 00              NOP                         
74ED: 00              NOP                         
74EE: 00              NOP                         
74EF: 00              NOP                         
74F0: 00              NOP                         
74F1: C0              RET     NZ                  
74F2: 00              NOP                         
74F3: F0 00           LD      A,($00)             
74F5: FF              RST     0X38                
74F6: 80              ADD     A,B                 
74F7: 7F              LD      A,A                 
74F8: E0 1F           LD      ($FF00+$1F),A       
74FA: FF              RST     0X38                
74FB: 00              NOP                         
74FC: 3F              CCF                         
74FD: 00              NOP                         
74FE: 03              INC     BC                  
74FF: 00              NOP                         
7500: 00              NOP                         
7501: 00              NOP                         
7502: 00              NOP                         
7503: 00              NOP                         
7504: 1F              RRA                         
7505: 00              NOP                         
7506: E0 1F           LD      ($FF00+$1F),A       
7508: 00              NOP                         
7509: E0 00           LD      ($FF00+$00),A       
750B: 00              NOP                         
750C: 00              NOP                         
750D: 00              NOP                         
750E: 00              NOP                         
750F: FF              RST     0X38                
7510: 00              NOP                         
7511: FF              RST     0X38                
7512: FF              RST     0X38                
7513: 00              NOP                         
7514: FF              RST     0X38                
7515: 00              NOP                         
7516: 00              NOP                         
7517: FF              RST     0X38                
7518: 00              NOP                         
7519: FF              RST     0X38                
751A: 00              NOP                         
751B: 00              NOP                         
751C: 00              NOP                         
751D: 00              NOP                         
751E: 00              NOP                         
751F: 00              NOP                         
7520: 07              RLCA                        
7521: 00              NOP                         
7522: 18 07           JR      $752B               ; {}
7524: 20 1F           JR      NZ,$7545            ; {}
7526: 41              LD      B,C                 
7527: 3F              CCF                         
7528: 43              LD      B,E                 
7529: 3F              CCF                         
752A: 87              ADD     A,A                 
752B: 79              LD      A,C                 
752C: 8F              ADC     A,A                 
752D: 70              LD      (HL),B              
752E: 8F              ADC     A,A                 
752F: 70              LD      (HL),B              
7530: 8F              ADC     A,A                 
7531: 70              LD      (HL),B              
7532: 8F              ADC     A,A                 
7533: 70              LD      (HL),B              
7534: 57              LD      D,A                 
7535: B8              CP      B                   
7536: 5B              LD      E,E                 
7537: 3C              INC     A                   
7538: 2F              CPL                         
7539: 5F              LD      E,A                 
753A: 1B              DEC     DE                  
753B: E7              RST     0X20                
753C: FF              RST     0X38                
753D: 00              NOP                         
753E: FF              RST     0X38                
753F: 00              NOP                         
7540: 00              NOP                         
7541: 00              NOP                         
7542: 00              NOP                         
7543: 00              NOP                         
7544: 00              NOP                         
7545: 00              NOP                         
7546: 00              NOP                         
7547: 00              NOP                         
7548: 00              NOP                         
7549: 00              NOP                         
754A: 00              NOP                         
754B: 00              NOP                         
754C: C3 00 3C        JP      $3C00               
754F: C3 00 7E        JP      $7E00               ; {}
7552: 00              NOP                         
7553: 00              NOP                         
7554: 00              NOP                         
7555: 00              NOP                         
7556: 00              NOP                         
7557: C3 81 7E        JP      $7E81               ; {}
755A: FF              RST     0X38                
755B: 00              NOP                         
755C: 7C              LD      A,H                 
755D: 83              ADD     A,E                 
755E: 00              NOP                         
755F: FF              RST     0X38                
7560: 00              NOP                         
7561: 3C              INC     A                   
7562: 00              NOP                         
7563: 00              NOP                         
7564: 00              NOP                         
7565: 00              NOP                         
7566: 00              NOP                         
7567: 00              NOP                         
7568: 00              NOP                         
7569: 00              NOP                         
756A: 00              NOP                         
756B: 00              NOP                         
756C: 00              NOP                         
756D: 00              NOP                         
756E: 00              NOP                         
756F: 7E              LD      A,(HL)              
7570: 00              NOP                         
7571: FF              RST     0X38                
7572: 00              NOP                         
7573: FF              RST     0X38                
7574: 7E              LD      A,(HL)              
7575: 81              ADD     A,C                 
7576: FF              RST     0X38                
7577: 00              NOP                         
7578: C3 00 00        JP      $0000               
757B: 00              NOP                         
757C: 00              NOP                         
757D: 00              NOP                         
757E: 00              NOP                         
757F: 00              NOP                         
7580: 00              NOP                         
7581: 00              NOP                         
7582: 00              NOP                         
7583: 00              NOP                         
7584: 00              NOP                         
7585: 00              NOP                         
7586: 00              NOP                         
7587: 00              NOP                         
7588: 00              NOP                         
7589: 00              NOP                         
758A: 00              NOP                         
758B: 00              NOP                         
758C: 00              NOP                         
758D: 00              NOP                         
758E: 80              ADD     A,B                 
758F: 00              NOP                         
7590: 60              LD      H,B                 
7591: 80              ADD     A,B                 
7592: 18 60           JR      $75F4               ; {}
7594: 07              RLCA                        
7595: 18 00           JR      $7597               ; {}
7597: CF              RST     0X08                
7598: 80              ADD     A,B                 
7599: 60              LD      H,B                 
759A: C0              RET     NZ                  
759B: 38 F8           JR      C,$7595             ; {}
759D: 07              RLCA                        
759E: 3F              CCF                         
759F: C0              RET     NZ                  
75A0: 07              RLCA                        
75A1: 78              LD      A,B                 
75A2: 00              NOP                         
75A3: 1F              RRA                         
75A4: 00              NOP                         
75A5: 07              RLCA                        
75A6: 00              NOP                         
75A7: 00              NOP                         
75A8: 00              NOP                         
75A9: 03              INC     BC                  
75AA: 00              NOP                         
75AB: 0F              RRCA                        
75AC: 03              INC     BC                  
75AD: 3C              INC     A                   
75AE: 0E 70           LD      C,$70               
75B0: 18 E0           JR      $7592               ; {}
75B2: 30 C0           JR      NC,$7574            ; {}
75B4: 60              LD      H,B                 
75B5: 80              ADD     A,B                 
75B6: C0              RET     NZ                  
75B7: 00              NOP                         
75B8: 80              ADD     A,B                 
75B9: 00              NOP                         
75BA: 00              NOP                         
75BB: 00              NOP                         
75BC: 00              NOP                         
75BD: 00              NOP                         
75BE: 00              NOP                         
75BF: 00              NOP                         
75C0: 07              RLCA                        
75C1: 78              LD      A,B                 
75C2: 00              NOP                         
75C3: 1F              RRA                         
75C4: 03              INC     BC                  
75C5: 04              INC     B                   
75C6: 0F              RRCA                        
75C7: 10 18           ;;STOP    $18                 
75C9: 24              INC     H                   
75CA: 30 48           JR      NC,$7614            ; {}
75CC: 20 D0           JR      NZ,$759E            ; {}
75CE: 60              LD      H,B                 
75CF: 90              SUB     B                   
75D0: 60              LD      H,B                 
75D1: 90              SUB     B                   
75D2: C0              RET     NZ                  
75D3: 20 C0           JR      NZ,$7595            ; {}
75D5: 00              NOP                         
75D6: 80              ADD     A,B                 
75D7: 00              NOP                         
75D8: 00              NOP                         
75D9: 00              NOP                         
75DA: 00              NOP                         
75DB: 00              NOP                         
75DC: 00              NOP                         
75DD: 00              NOP                         
75DE: 00              NOP                         
75DF: 00              NOP                         
75E0: FF              RST     0X38                
75E1: 00              NOP                         
75E2: 00              NOP                         
75E3: FF              RST     0X38                
75E4: 00              NOP                         
75E5: 80              ADD     A,B                 
75E6: 00              NOP                         
75E7: 00              NOP                         
75E8: 00              NOP                         
75E9: 00              NOP                         
75EA: 00              NOP                         
75EB: 00              NOP                         
75EC: 00              NOP                         
75ED: 00              NOP                         
75EE: 00              NOP                         
75EF: 00              NOP                         
75F0: 00              NOP                         
75F1: FF              RST     0X38                
75F2: 00              NOP                         
75F3: FF              RST     0X38                
75F4: 00              NOP                         
75F5: FF              RST     0X38                
75F6: FF              RST     0X38                
75F7: 00              NOP                         
75F8: FF              RST     0X38                
75F9: 00              NOP                         
75FA: 00              NOP                         
75FB: 00              NOP                         
75FC: 00              NOP                         
75FD: 00              NOP                         
75FE: 00              NOP                         
75FF: 00              NOP                         
7600: 01 00 03        LD      BC,$0300            
7603: 01 03 01        LD      BC,$0103            
7606: 63              LD      H,E                 
7607: 01 F3 61        LD      BC,$61F3            
760A: FB              EI                          
760B: 71              LD      (HL),C              
760C: 7F              LD      A,A                 
760D: 39              ADD     HL,SP               
760E: 3F              CCF                         
760F: 0F              RRCA                        
7610: 0F              RRCA                        
7611: 07              RLCA                        
7612: 0F              RRCA                        
7613: 03              INC     BC                  
7614: 7F              LD      A,A                 
7615: 0F              RRCA                        
7616: FF              RST     0X38                
7617: 7F              LD      A,A                 
7618: FF              RST     0X38                
7619: 78              LD      A,B                 
761A: 7F              LD      A,A                 
761B: 07              RLCA                        
761C: 7F              LD      A,A                 
761D: 1D              DEC     E                   
761E: BF              CP      A                   
761F: 58              LD      E,B                 
7620: 80              ADD     A,B                 
7621: 00              NOP                         
7622: C0              RET     NZ                  
7623: 80              ADD     A,B                 
7624: C0              RET     NZ                  
7625: 80              ADD     A,B                 
7626: CC 80 DE        CALL    Z,$DE80             
7629: 8C              ADC     A,H                 
762A: FE 9C           CP      $9C                 
762C: FC                              
762D: B8              CP      B                   
762E: F8 70           LD      HL,SP+$70           
7630: FE 60           CP      $60                 
7632: FF              RST     0X38                
7633: EE FF           XOR     $FF                 
7635: DC FF B0        CALL    C,$B0FF             
7638: FF              RST     0X38                
7639: 7B              LD      A,E                 
763A: FF              RST     0X38                
763B: DB                              
763C: FF              RST     0X38                
763D: C3 F3 CD        JP      $CDF3               
7640: 0E 00           LD      C,$00               
7642: 1D              DEC     E                   
7643: 0E 1D           LD      C,$1D               
7645: 0E 11           LD      C,$11               
7647: 0E 0E           LD      C,$0E               
7649: 00              NOP                         
764A: 06 00           LD      B,$00               
764C: 03              INC     BC                  
764D: 00              NOP                         
764E: 1F              RRA                         
764F: 00              NOP                         
7650: 3F              CCF                         
7651: 00              NOP                         
7652: 6B              LD      L,E                 
7653: 1C              INC     E                   
7654: FF              RST     0X38                
7655: 00              NOP                         
7656: DF              RST     0X18                
7657: 67              LD      H,A                 
7658: FF              RST     0X38                
7659: AE              XOR     (HL)                
765A: FF              RST     0X38                
765B: 3D              DEC     A                   
765C: BF              CP      A                   
765D: 5B              LD      E,E                 
765E: FF              RST     0X38                
765F: 1B              DEC     DE                  
7660: 9D              SBC     L                   
7661: 62              LD      H,D                 
7662: 80              ADD     A,B                 
7663: 7F              LD      A,A                 
7664: 80              ADD     A,B                 
7665: 7F              LD      A,A                 
7666: 82              ADD     A,D                 
7667: 7D              LD      A,L                 
7668: 85              ADD     A,L                 
7669: 7A              LD      A,D                 
766A: 45              LD      B,L                 
766B: 3A              LD      A,(HLD)             
766C: 45              LD      B,L                 
766D: 3A              LD      A,(HLD)             
766E: 24              INC     H                   
766F: 1B              DEC     DE                  
7670: 1C              INC     E                   
7671: 03              INC     BC                  
7672: 04              INC     B                   
7673: 03              INC     BC                  
7674: 02              LD      (BC),A              
7675: 01 02 01        LD      BC,$0102            
7678: 01 00 00        LD      BC,$0000            
767B: 00              NOP                         
767C: 00              NOP                         
767D: 00              NOP                         
767E: 00              NOP                         
767F: 00              NOP                         
7680: E7              RST     0X20                
7681: 1D              DEC     E                   
7682: 69              LD      L,C                 
7683: 96              SUB     (HL)                
7684: E4                              
7685: 5B              LD      E,E                 
7686: F4                              
7687: 4B              LD      C,E                 
7688: F2                              
7689: ED                              
768A: F1              POP     AF                  
768B: EE F8           XOR     $F8                 
768D: 17              RLA                         
768E: 3C              INC     A                   
768F: DB                              
7690: 3F              CCF                         
7691: DC 7F BF        CALL    C,$BF7F             
7694: 7F              LD      A,A                 
7695: B1              OR      C                   
7696: 73              LD      (HL),E              
7697: 8D              ADC     A,L                 
7698: 03              INC     BC                  
7699: FC                              
769A: C0              RET     NZ                  
769B: 3F              CCF                         
769C: 30 0F           JR      NC,$76AD            ; {}
769E: 0F              RRCA                        
769F: 00              NOP                         
76A0: FF              RST     0X38                
76A1: D1              POP     DE                  
76A2: FB              EI                          
76A3: D5              PUSH    DE                  
76A4: FF              RST     0X38                
76A5: 02              LD      (BC),A              
76A6: 76              HALT                        
76A7: B9              CP      C                   
76A8: 80              ADD     A,B                 
76A9: FF              RST     0X38                
76AA: FF              RST     0X38                
76AB: 00              NOP                         
76AC: D3                              
76AD: 2C              INC     L                   
76AE: 92              SUB     D                   
76AF: 6D              LD      L,L                 
76B0: 92              SUB     D                   
76B1: 6D              LD      L,L                 
76B2: D7              RST     0X10                
76B3: 6C              LD      L,H                 
76B4: EF              RST     0X28                
76B5: 7D              LD      A,L                 
76B6: BB              CP      E                   
76B7: 7D              LD      A,L                 
76B8: C5              PUSH    BC                  
76B9: 3A              LD      A,(HLD)             
76BA: 38 C7           JR      C,$7683             ; {}
76BC: 00              NOP                         
76BD: FF              RST     0X38                
76BE: C3 3C 00        JP      $003C               
76C1: 00              NOP                         
76C2: 00              NOP                         
76C3: 00              NOP                         
76C4: 00              NOP                         
76C5: 00              NOP                         
76C6: 00              NOP                         
76C7: 00              NOP                         
76C8: 00              NOP                         
76C9: 00              NOP                         
76CA: 00              NOP                         
76CB: 00              NOP                         
76CC: 00              NOP                         
76CD: 00              NOP                         
76CE: 00              NOP                         
76CF: 00              NOP                         
76D0: 00              NOP                         
76D1: 00              NOP                         
76D2: 87              ADD     A,A                 
76D3: 00              NOP                         
76D4: D8              RET     C                   
76D5: 07              RLCA                        
76D6: E0 1F           LD      ($FF00+$1F),A       
76D8: E0 DF           LD      ($FF00+$DF),A       
76DA: EC                              
76DB: D3                              
76DC: FF              RST     0X38                
76DD: CC FF CF        CALL    Z,$CFFF             
76E0: 00              NOP                         
76E1: 00              NOP                         
76E2: 00              NOP                         
76E3: 00              NOP                         
76E4: 00              NOP                         
76E5: 00              NOP                         
76E6: 00              NOP                         
76E7: 00              NOP                         
76E8: 00              NOP                         
76E9: 00              NOP                         
76EA: 00              NOP                         
76EB: 00              NOP                         
76EC: 00              NOP                         
76ED: 00              NOP                         
76EE: 00              NOP                         
76EF: 00              NOP                         
76F0: 00              NOP                         
76F1: 00              NOP                         
76F2: E0 00           LD      ($FF00+$00),A       
76F4: 18 E0           JR      $76D6               ; {}
76F6: 04              INC     B                   
76F7: F8 04           LD      HL,SP+$04           
76F9: F8 C2           LD      HL,SP+$C2           
76FB: 3C              INC     A                   
76FC: E2              LD      (C),A               
76FD: DC E1 DE        CALL    C,$DEE1             
7700: FF              RST     0X38                
7701: 81              ADD     A,C                 
7702: FF              RST     0X38                
7703: 7E              LD      A,(HL)              
7704: FF              RST     0X38                
7705: 7F              LD      A,A                 
7706: 7F              LD      A,A                 
7707: 87              ADD     A,A                 
7708: 5F              LD      E,A                 
7709: AF              XOR     A                   
770A: BF              CP      A                   
770B: 5F              LD      E,A                 
770C: 7F              LD      A,A                 
770D: B9              CP      C                   
770E: FF              RST     0X38                
770F: 71              LD      (HL),C              
7710: FB              EI                          
7711: 75              LD      (HL),L              
7712: FF              RST     0X38                
7713: 09              ADD     HL,BC               
7714: FF              RST     0X38                
7715: 99              SBC     C                   
7716: DF              RST     0X18                
7717: A1              AND     C                   
7718: C3 3D 01        JP      $013D               
771B: FE 06           CP      $06                 
771D: F8 F8           LD      HL,SP+$F8           
771F: 00              NOP                         
7720: FD                              
7721: C2 FD 7A        JP      NZ,$7AFD            ; {}
7724: FD                              
7725: BA              CP      D                   
7726: FE D8           CP      $D8                 
7728: FF              RST     0X38                
7729: EE FF           XOR     $FF                 
772B: EE FF           XOR     $FF                 
772D: F4                              
772E: FE B8           CP      $B8                 
7730: FE 9C           CP      $9C                 
7732: FE 8C           CP      $8C                 
7734: EC                              
7735: 80              ADD     A,B                 
7736: C0              RET     NZ                  
7737: 80              ADD     A,B                 
7738: C0              RET     NZ                  
7739: 80              ADD     A,B                 
773A: 80              ADD     A,B                 
773B: 00              NOP                         
773C: 00              NOP                         
773D: 00              NOP                         
773E: 00              NOP                         
773F: 00              NOP                         
7740: A5              AND     L                   
7741: 5A              LD      E,D                 
7742: 82              ADD     A,D                 
7743: 7C              LD      A,H                 
7744: A4              AND     H                   
7745: 78              LD      A,B                 
7746: A8              XOR     B                   
7747: 70              LD      (HL),B              
7748: 74              LD      (HL),H              
7749: 38 5A           JR      C,$77A5             ; {}
774B: 3C              INC     A                   
774C: 2D              DEC     L                   
774D: 1E 1F           LD      E,$1F               
774F: 0E 1F           LD      C,$1F               
7751: 0E 3E           LD      C,$3E               
7753: 1C              INC     E                   
7754: 7C              LD      A,H                 
7755: 38 78           JR      C,$77CF             ; {}
7757: 00              NOP                         
7758: 00              NOP                         
7759: 00              NOP                         
775A: 00              NOP                         
775B: 00              NOP                         
775C: 00              NOP                         
775D: 00              NOP                         
775E: 00              NOP                         
775F: 00              NOP                         
7760: 00              NOP                         
7761: 00              NOP                         
7762: 00              NOP                         
7763: 00              NOP                         
7764: 00              NOP                         
7765: 00              NOP                         
7766: 00              NOP                         
7767: 00              NOP                         
7768: 00              NOP                         
7769: 00              NOP                         
776A: 00              NOP                         
776B: 00              NOP                         
776C: 00              NOP                         
776D: 00              NOP                         
776E: 00              NOP                         
776F: 00              NOP                         
7770: 07              RLCA                        
7771: 00              NOP                         
7772: 0B              DEC     BC                  
7773: 07              RLCA                        
7774: 17              RLA                         
7775: 0C              INC     C                   
7776: 17              RLA                         
7777: 0C              INC     C                   
7778: 13              INC     DE                  
7779: 0F              RRCA                        
777A: 08 07 07        LD      ($0707),SP          
777D: 00              NOP                         
777E: 02              LD      (BC),A              
777F: 01 06 01        LD      BC,$0106            
7782: 0A              LD      A,(BC)              
7783: 05              DEC     B                   
7784: 16 0D           LD      D,$0D               
7786: 35              DEC     (HL)                
7787: 0E 53           LD      C,$53               
7789: 2F              CPL                         
778A: 68              LD      L,B                 
778B: 37              SCF                         
778C: B7              OR      A                   
778D: 78              LD      A,B                 
778E: 98              SBC     B                   
778F: 67              LD      H,A                 
7790: BF              CP      A                   
7791: 5B              LD      E,E                 
7792: FE 3D           CP      $3D                 
7794: FE 35           CP      $35                 
7796: BE              CP      (HL)                
7797: 5D              LD      E,L                 
7798: 9C              SBC     H                   
7799: 63              LD      H,E                 
779A: 40              LD      B,B                 
779B: 3F              CCF                         
779C: 30 0F           JR      NC,$77AD            ; {}
779E: 0F              RRCA                        
779F: 00              NOP                         
77A0: 00              NOP                         
77A1: 00              NOP                         
77A2: 00              NOP                         
77A3: 00              NOP                         
77A4: 00              NOP                         
77A5: 00              NOP                         
77A6: 00              NOP                         
77A7: 00              NOP                         
77A8: 01 00 02        LD      BC,$0200            
77AB: 01 02 01        LD      BC,$0102            
77AE: 02              LD      (BC),A              
77AF: 01 01 00        LD      BC,$0001            
77B2: 00              NOP                         
77B3: 00              NOP                         
77B4: 00              NOP                         
77B5: 00              NOP                         
77B6: 01 00 01        LD      BC,$0100            
77B9: 00              NOP                         
77BA: 02              LD      (BC),A              
77BB: 01 06 01        LD      BC,$0106            
77BE: 0A              LD      A,(BC)              
77BF: 05              DEC     B                   
77C0: 00              NOP                         
77C1: 00              NOP                         
77C2: 00              NOP                         
77C3: 00              NOP                         
77C4: 00              NOP                         
77C5: 00              NOP                         
77C6: F0 00           LD      A,($00)             
77C8: 7C              LD      A,H                 
77C9: F0 FE           LD      A,($FE)             
77CB: 8C              ADC     A,H                 
77CC: FD                              
77CD: 86              ADD     A,(HL)              
77CE: 7D              LD      A,L                 
77CF: C6 3D           ADD     $3D                 
77D1: FE 82           CP      $82                 
77D3: 7C              LD      A,H                 
77D4: FC                              
77D5: 00              NOP                         
77D6: 10 E0           ;;STOP    $E0                 
77D8: 20 C0           JR      NZ,$779A            ; {}
77DA: 40              LD      B,B                 
77DB: 80              ADD     A,B                 
77DC: 60              LD      H,B                 
77DD: 80              ADD     A,B                 
77DE: 50              LD      D,B                 
77DF: A0              AND     B                   
77E0: 0E 05           LD      C,$05               
77E2: 1B              DEC     DE                  
77E3: 06 29           LD      B,$29               
77E5: 17              RLA                         
77E6: 34              INC     (HL)                
77E7: 1B              DEC     DE                  
77E8: 7B              LD      A,E                 
77E9: 2C              INC     L                   
77EA: 7C              LD      A,H                 
77EB: 2F              CPL                         
77EC: 77              LD      (HL),A              
77ED: 2F              CPL                         
77EE: 71              LD      (HL),C              
77EF: 2E 73           LD      L,$73               
77F1: 2D              DEC     L                   
77F2: 67              LD      H,A                 
77F3: 1B              DEC     DE                  
77F4: 47              LD      B,A                 
77F5: 3A              LD      A,(HLD)             
77F6: 47              LD      B,A                 
77F7: 3B              DEC     SP                  
77F8: 23              INC     HL                  
77F9: 1D              DEC     E                   
77FA: 21 1E 18        LD      HL,$181E            
77FD: 07              RLCA                        
77FE: 07              RLCA                        
77FF: 00              NOP                         
7800: 00              NOP                         
7801: 00              NOP                         
7802: 00              NOP                         
7803: 00              NOP                         
7804: 00              NOP                         
7805: 00              NOP                         
7806: 00              NOP                         
7807: 00              NOP                         
7808: 00              NOP                         
7809: 00              NOP                         
780A: 00              NOP                         
780B: 00              NOP                         
780C: 00              NOP                         
780D: 00              NOP                         
780E: 00              NOP                         
780F: 00              NOP                         
7810: 00              NOP                         
7811: 00              NOP                         
7812: 01 00 01        LD      BC,$0100            
7815: 00              NOP                         
7816: 02              LD      (BC),A              
7817: 01 02 01        LD      BC,$0102            
781A: 05              DEC     B                   
781B: 03              INC     BC                  
781C: 05              DEC     B                   
781D: 03              INC     BC                  
781E: 05              DEC     B                   
781F: 03              INC     BC                  
7820: 00              NOP                         
7821: 00              NOP                         
7822: 00              NOP                         
7823: 00              NOP                         
7824: 00              NOP                         
7825: 00              NOP                         
7826: 00              NOP                         
7827: 00              NOP                         
7828: 00              NOP                         
7829: 00              NOP                         
782A: 07              RLCA                        
782B: 00              NOP                         
782C: 18 07           JR      $7835               ; {}
782E: 67              LD      H,A                 
782F: 1F              RRA                         
7830: 9F              SBC     A                   
7831: 78              LD      A,B                 
7832: 3F              CCF                         
7833: E0 7F           LD      ($FF00+$7F),A       
7835: C0              RET     NZ                  
7836: FF              RST     0X38                
7837: 80              ADD     A,B                 
7838: FF              RST     0X38                
7839: 80              ADD     A,B                 
783A: FF              RST     0X38                
783B: 00              NOP                         
783C: FE 01           CP      $01                 
783E: FD                              
783F: 03              INC     BC                  
7840: 05              DEC     B                   
7841: 03              INC     BC                  
7842: 05              DEC     B                   
7843: 03              INC     BC                  
7844: 04              INC     B                   
7845: 03              INC     BC                  
7846: 02              LD      (BC),A              
7847: 01 02 01        LD      BC,$0102            
784A: 01 00 01        LD      BC,$0100            
784D: 00              NOP                         
784E: 00              NOP                         
784F: 00              NOP                         
7850: 01 00 01        LD      BC,$0100            
7853: 00              NOP                         
7854: 01 00 00        LD      BC,$0000            
7857: 00              NOP                         
7858: 00              NOP                         
7859: 00              NOP                         
785A: 00              NOP                         
785B: 00              NOP                         
785C: 00              NOP                         
785D: 00              NOP                         
785E: 00              NOP                         
785F: 00              NOP                         
7860: FF              RST     0X38                
7861: 00              NOP                         
7862: FF              RST     0X38                
7863: 07              RLCA                        
7864: FE 8F           CP      $8F                 
7866: FD                              
7867: 8E              ADC     A,(HL)              
7868: 7D              LD      A,L                 
7869: CE 7F           ADC     $7F                 
786B: C6 FF           ADD     $FF                 
786D: 06 FF           LD      B,$FF               
786F: 72              LD      (HL),D              
7870: FF              RST     0X38                
7871: FA FF CA        LD      A,($CAFF)           
7874: FF              RST     0X38                
7875: CA FF 76        JP      Z,$76FF             ; {}
7878: 77              LD      (HL),A              
7879: 0E 13           LD      C,$13               
787B: 0E 09           LD      C,$09               
787D: 06 06           LD      B,$06               
787F: 00              NOP                         
7880: 00              NOP                         
7881: 00              NOP                         
7882: 00              NOP                         
7883: 00              NOP                         
7884: 00              NOP                         
7885: 00              NOP                         
7886: 00              NOP                         
7887: 00              NOP                         
7888: 00              NOP                         
7889: 00              NOP                         
788A: 00              NOP                         
788B: 00              NOP                         
788C: 00              NOP                         
788D: 00              NOP                         
788E: 07              RLCA                        
788F: 00              NOP                         
7890: 0F              RRCA                        
7891: 07              RLCA                        
7892: 1F              RRA                         
7893: 0F              RRCA                        
7894: 1F              RRA                         
7895: 09              ADD     HL,BC               
7896: 3F              CCF                         
7897: 09              ADD     HL,BC               
7898: 4F              LD      C,A                 
7899: 37              SCF                         
789A: 9F              SBC     A                   
789B: 78              LD      A,B                 
789C: BF              CP      A                   
789D: 7F              LD      A,A                 
789E: 7F              LD      A,A                 
789F: 00              NOP                         
78A0: 00              NOP                         
78A1: 00              NOP                         
78A2: 00              NOP                         
78A3: 00              NOP                         
78A4: 00              NOP                         
78A5: 00              NOP                         
78A6: 00              NOP                         
78A7: 00              NOP                         
78A8: 00              NOP                         
78A9: 00              NOP                         
78AA: 07              RLCA                        
78AB: 00              NOP                         
78AC: 18 07           JR      $78B5               ; {}
78AE: 63              LD      H,E                 
78AF: 1F              RRA                         
78B0: CF              RST     0X08                
78B1: 3C              INC     A                   
78B2: FF              RST     0X38                
78B3: B0              OR      B                   
78B4: FF              RST     0X38                
78B5: 80              ADD     A,B                 
78B6: FF              RST     0X38                
78B7: 80              ADD     A,B                 
78B8: FF              RST     0X38                
78B9: 1C              INC     E                   
78BA: FF              RST     0X38                
78BB: 7E              LD      A,(HL)              
78BC: E7              RST     0X20                
78BD: FE FB           CP      $FB                 
78BF: 06 0F           LD      B,$0F               
78C1: 01 1F 0E        LD      BC,$0E1F            
78C4: 3F              CCF                         
78C5: 1F              RRA                         
78C6: 3F              CCF                         
78C7: 13              INC     DE                  
78C8: 3F              CCF                         
78C9: 13              INC     DE                  
78CA: 1F              RRA                         
78CB: 0E 1F           LD      C,$1F               
78CD: 01 17 0F        LD      BC,$0F17            
78D0: 17              RLA                         
78D1: 0E 13           LD      C,$13               
78D3: 0D              DEC     C                   
78D4: 0D              DEC     C                   
78D5: 03              INC     BC                  
78D6: 04              INC     B                   
78D7: 03              INC     BC                  
78D8: 03              INC     BC                  
78D9: 00              NOP                         
78DA: 00              NOP                         
78DB: 00              NOP                         
78DC: 00              NOP                         
78DD: 00              NOP                         
78DE: 00              NOP                         
78DF: 00              NOP                         
78E0: FF              RST     0X38                
78E1: 1D              DEC     E                   
78E2: FF              RST     0X38                
78E3: 3E F3           LD      A,$F3               
78E5: 3F              CCF                         
78E6: EB                              
78E7: 77              LD      (HL),A              
78E8: F7              RST     0X30                
78E9: 6F              LD      L,A                 
78EA: FF              RST     0X38                
78EB: DE FF           SBC     $FF                 
78ED: B8              CP      B                   
78EE: FF              RST     0X38                
78EF: 60              LD      H,B                 
78F0: FF              RST     0X38                
78F1: DD                              
78F2: FF              RST     0X38                
78F3: BE              CP      (HL)                
78F4: FF              RST     0X38                
78F5: A6              AND     (HL)                
78F6: 7F              LD      A,A                 
78F7: A6              AND     (HL)                
78F8: FE 1C           CP      $1C                 
78FA: 1C              INC     E                   
78FB: 00              NOP                         
78FC: 00              NOP                         
78FD: 00              NOP                         
78FE: 00              NOP                         
78FF: 00              NOP                         
7900: 07              RLCA                        
7901: 00              NOP                         
7902: 18 07           JR      $790B               ; {}
7904: 27              DAA                         
7905: 1F              RRA                         
7906: 4F              LD      C,A                 
7907: 38 5F           JR      C,$7968             ; {}
7909: 30 BF           JR      NC,$78CA            ; {}
790B: 60              LD      H,B                 
790C: BE              CP      (HL)                
790D: 61              LD      H,C                 
790E: BD              CP      L                   
790F: 63              LD      H,E                 
7910: BD              CP      L                   
7911: 63              LD      H,E                 
7912: BE              CP      (HL)                
7913: 61              LD      H,C                 
7914: BF              CP      A                   
7915: 60              LD      H,B                 
7916: 5F              LD      E,A                 
7917: 30 4F           JR      NC,$7968            ; {}
7919: 38 27           JR      C,$7942             ; {}
791B: 1F              RRA                         
791C: 18 07           JR      $7925               ; {}
791E: 07              RLCA                        
791F: 00              NOP                         
7920: 00              NOP                         
7921: 00              NOP                         
7922: 03              INC     BC                  
7923: 00              NOP                         
7924: 0C              INC     C                   
7925: 03              INC     BC                  
7926: 13              INC     DE                  
7927: 0F              RRCA                        
7928: 27              DAA                         
7929: 1C              INC     E                   
792A: 2F              CPL                         
792B: 18 5F           JR      $798C               ; {}
792D: 30 5E           JR      NC,$798D            ; {}
792F: 31 5E 31        LD      SP,$315E            
7932: 5F              LD      E,A                 
7933: 30 2F           JR      NC,$7964            ; {}
7935: 18 27           JR      $795E               ; {}
7937: 1C              INC     E                   
7938: 13              INC     DE                  
7939: 0F              RRCA                        
793A: 0C              INC     C                   
793B: 03              INC     BC                  
793C: 03              INC     BC                  
793D: 00              NOP                         
793E: 00              NOP                         
793F: 00              NOP                         
7940: 01 01 03        LD      BC,$0301            
7943: 02              LD      (BC),A              
7944: 3F              CCF                         
7945: 3D              DEC     A                   
7946: 3F              CCF                         
7947: 21 3F 28        LD      HL,$283F            
794A: 3F              CCF                         
794B: 26 7B           LD      H,$7B               
794D: 46              LD      B,(HL)              
794E: FF              RST     0X38                
794F: B0              OR      B                   
7950: CF              RST     0X08                
7951: B0              OR      B                   
7952: 7F              LD      A,A                 
7953: 46              LD      B,(HL)              
7954: 3D              DEC     A                   
7955: 26 3F           LD      H,$3F               
7957: 28 3E           JR      Z,$7997             ; {}
7959: 21 3E 3D        LD      HL,$3D3E            
795C: 03              INC     BC                  
795D: 02              LD      (BC),A              
795E: 01 01 7F        LD      BC,$7F01            
7961: 38 FF           JR      C,$7962             ; {}
7963: 7C              LD      A,H                 
7964: FF              RST     0X38                
7965: 64              LD      H,H                 
7966: FF              RST     0X38                
7967: 64              LD      H,H                 
7968: 7F              LD      A,A                 
7969: 38 39           JR      C,$79A4             ; {}
796B: 06 17           LD      B,$17               
796D: 0E 17           LD      C,$17               
796F: 0E 09           LD      C,$09               
7971: 06 07           LD      B,$07               
7973: 00              NOP                         
7974: 00              NOP                         
7975: 00              NOP                         
7976: 00              NOP                         
7977: 00              NOP                         
7978: 00              NOP                         
7979: 00              NOP                         
797A: 00              NOP                         
797B: 00              NOP                         
797C: 00              NOP                         
797D: 00              NOP                         
797E: 00              NOP                         
797F: 00              NOP                         
7980: 05              DEC     B                   
7981: 03              INC     BC                  
7982: 05              DEC     B                   
7983: 03              INC     BC                  
7984: 07              RLCA                        
7985: 00              NOP                         
7986: 0F              RRCA                        
7987: 07              RLCA                        
7988: 1F              RRA                         
7989: 0F              RRCA                        
798A: 1F              RRA                         
798B: 09              ADD     HL,BC               
798C: 1F              RRA                         
798D: 09              ADD     HL,BC               
798E: 0F              RRCA                        
798F: 07              RLCA                        
7990: 0F              RRCA                        
7991: 00              NOP                         
7992: 0B              DEC     BC                  
7993: 07              RLCA                        
7994: 0B              DEC     BC                  
7995: 07              RLCA                        
7996: 07              RLCA                        
7997: 03              INC     BC                  
7998: 03              INC     BC                  
7999: 00              NOP                         
799A: 00              NOP                         
799B: 00              NOP                         
799C: 00              NOP                         
799D: 00              NOP                         
799E: 00              NOP                         
799F: 00              NOP                         
79A0: FF              RST     0X38                
79A1: 00              NOP                         
79A2: FF              RST     0X38                
79A3: 07              RLCA                        
79A4: FC                              
79A5: 0F              RRCA                        
79A6: FB              EI                          
79A7: 1C              INC     E                   
79A8: FC                              
79A9: 98              SBC     B                   
79AA: FC                              
79AB: B8              CP      B                   
79AC: FE B4           CP      $B4                 
79AE: FE 60           CP      $60                 
79B0: E0 C0           LD      ($FF00+$C0),A       
79B2: E0 80           LD      ($FF00+$80),A       
79B4: F0 60           LD      A,($60)             
79B6: E0 00           LD      ($FF00+$00),A       
79B8: 00              NOP                         
79B9: 00              NOP                         
79BA: 00              NOP                         
79BB: 00              NOP                         
79BC: 00              NOP                         
79BD: 00              NOP                         
79BE: 00              NOP                         
79BF: 00              NOP                         
79C0: 07              RLCA                        
79C1: 00              NOP                         
79C2: 18 07           JR      $79CB               ; {}
79C4: 23              INC     HL                  
79C5: 1F              RRA                         
79C6: 4F              LD      C,A                 
79C7: 3F              CCF                         
79C8: 5F              LD      E,A                 
79C9: 33              INC     SP                  
79CA: 93              SUB     E                   
79CB: 6D              LD      L,L                 
79CC: BF              CP      A                   
79CD: 60              LD      H,B                 
79CE: BF              CP      A                   
79CF: 60              LD      H,B                 
79D0: BF              CP      A                   
79D1: 60              LD      H,B                 
79D2: BF              CP      A                   
79D3: 70              LD      (HL),B              
79D4: 9F              SBC     A                   
79D5: 78              LD      A,B                 
79D6: 5F              LD      E,A                 
79D7: 3C              INC     A                   
79D8: 4F              LD      C,A                 
79D9: 3E 23           LD      A,$23               
79DB: 1F              RRA                         
79DC: 18 07           JR      $79E5               ; {}
79DE: 07              RLCA                        
79DF: 00              NOP                         
79E0: 07              RLCA                        
79E1: 00              NOP                         
79E2: 18 07           JR      $79EB               ; {}
79E4: 23              INC     HL                  
79E5: 1F              RRA                         
79E6: 4F              LD      C,A                 
79E7: 3F              CCF                         
79E8: 5F              LD      E,A                 
79E9: 3F              CCF                         
79EA: 9F              SBC     A                   
79EB: 7F              LD      A,A                 
79EC: BF              CP      A                   
79ED: 79              LD      A,C                 
79EE: BD              CP      L                   
79EF: 7A              LD      A,D                 
79F0: BF              CP      A                   
79F1: 78              LD      A,B                 
79F2: BF              CP      A                   
79F3: 7C              LD      A,H                 
79F4: 9F              SBC     A                   
79F5: 7E              LD      A,(HL)              
79F6: 5F              LD      E,A                 
79F7: 3F              CCF                         
79F8: 4F              LD      C,A                 
79F9: 3F              CCF                         
79FA: 23              INC     HL                  
79FB: 1F              RRA                         
79FC: 18 07           JR      $7A05               ; {}
79FE: 07              RLCA                        
79FF: 00              NOP                         
7A00: 00              NOP                         
7A01: 00              NOP                         
7A02: 00              NOP                         
7A03: 00              NOP                         
7A04: 02              LD      (BC),A              
7A05: 00              NOP                         
7A06: 07              RLCA                        
7A07: 02              LD      (BC),A              
7A08: 07              RLCA                        
7A09: 03              INC     BC                  
7A0A: 07              RLCA                        
7A0B: 03              INC     BC                  
7A0C: 2F              CPL                         
7A0D: 07              RLCA                        
7A0E: 7F              LD      A,A                 
7A0F: 27              DAA                         
7A10: 7E              LD      A,(HL)              
7A11: 27              DAA                         
7A12: 2E 07           LD      L,$07               
7A14: 0E 07           LD      C,$07               
7A16: 0F              RRCA                        
7A17: 07              RLCA                        
7A18: 2F              CPL                         
7A19: 07              RLCA                        
7A1A: 7E              LD      A,(HL)              
7A1B: 2F              CPL                         
7A1C: 7C              LD      A,H                 
7A1D: 3F              CCF                         
7A1E: 7C              LD      A,H                 
7A1F: 3F              CCF                         
7A20: 10 00           ;;STOP    $00                 
7A22: 38 10           JR      C,$7A34             ; {}
7A24: 39              ADD     HL,SP               
7A25: 10 3B           ;;STOP    $3B                 
7A27: 11 93 01        LD      DE,$0193            
7A2A: 87              ADD     A,A                 
7A2B: 03              INC     BC                  
7A2C: C7              RST     0X00                
7A2D: 83              ADD     A,E                 
7A2E: EF              RST     0X28                
7A2F: C7              RST     0X00                
7A30: FD                              
7A31: EF              RST     0X28                
7A32: 7B              LD      A,E                 
7A33: FF              RST     0X38                
7A34: FF              RST     0X38                
7A35: FF              RST     0X38                
7A36: FC                              
7A37: FF              RST     0X38                
7A38: 78              LD      A,B                 
7A39: FF              RST     0X38                
7A3A: 30 FF           JR      NC,$7A3B            ; {}
7A3C: 30 FF           JR      NC,$7A3D            ; {}
7A3E: 20 FF           JR      NZ,$7A3F            ; {}
7A40: 40              LD      B,B                 
7A41: 00              NOP                         
7A42: E1              POP     HL                  
7A43: 40              LD      B,B                 
7A44: F3              DI                          
7A45: E1              POP     HL                  
7A46: B7              OR      A                   
7A47: E3                              
7A48: B6              OR      (HL)                
7A49: E3                              
7A4A: 3E F7           LD      A,$F7               
7A4C: 1C              INC     E                   
7A4D: FF              RST     0X38                
7A4E: 1C              INC     E                   
7A4F: FF              RST     0X38                
7A50: 1C              INC     E                   
7A51: FF              RST     0X38                
7A52: BE              CP      (HL)                
7A53: FF              RST     0X38                
7A54: BF              CP      A                   
7A55: FF              RST     0X38                
7A56: FF              RST     0X38                
7A57: FF              RST     0X38                
7A58: FB              EI                          
7A59: FF              RST     0X38                
7A5A: F3              DI                          
7A5B: FF              RST     0X38                
7A5C: 33              INC     SP                  
7A5D: FF              RST     0X38                
7A5E: 21 FF 04        LD      HL,$04FF            
7A61: 00              NOP                         
7A62: 0E 04           LD      C,$04               
7A64: 9E              SBC     (HL)                
7A65: 0C              INC     C                   
7A66: D6 8C           SUB     $8C                 
7A68: CC 80 C0        CALL    Z,$C080             
7A6B: 80              ADD     A,B                 
7A6C: E0 C0           LD      ($FF00+$C0),A       
7A6E: E4                              
7A6F: C0              RET     NZ                  
7A70: EE C4           XOR     $C4                 
7A72: FE E4           CP      $E4                 
7A74: FF              RST     0X38                
7A75: EE FF           XOR     $FF                 
7A77: FE FB           CP      $FB                 
7A79: FE BB           CP      $BB                 
7A7B: FE 3B           CP      $3B                 
7A7D: FE 1F           CP      $1F                 
7A7F: FE F9           CP      $F9                 
7A81: 7F              LD      A,A                 
7A82: FA 7F D1        LD      A,($D17F)           
7A85: 7E              LD      A,(HL)              
7A86: D1              POP     DE                  
7A87: 7E              LD      A,(HL)              
7A88: F1              POP     AF                  
7A89: 7E              LD      A,(HL)              
7A8A: EC                              
7A8B: 73              LD      (HL),E              
7A8C: EE 71           XOR     $71                 
7A8E: E6 79           AND     $79                 
7A90: 67              LD      H,A                 
7A91: 38 77           JR      C,$7B0A             ; {}
7A93: 38 33           JR      C,$7AC8             ; {}
7A95: 1C              INC     E                   
7A96: 39              ADD     HL,SP               
7A97: 1E 1C           LD      E,$1C               
7A99: 0F              RRCA                        
7A9A: 0F              RRCA                        
7A9B: 07              RLCA                        
7A9C: 07              RLCA                        
7A9D: 01 01 00        LD      BC,$0001            
7AA0: E0 FF           LD      ($FF00+$FF),A       
7AA2: F0 1F           LD      A,($1F)             
7AA4: FC                              
7AA5: 0F              RRCA                        
7AA6: FE 07           CP      $07                 
7AA8: FB              EI                          
7AA9: 27              DAA                         
7AAA: FB              EI                          
7AAB: 07              RLCA                        
7AAC: 77              LD      (HL),A              
7AAD: 8F              ADC     A,A                 
7AAE: 1F              RRA                         
7AAF: FF              RST     0X38                
7AB0: F7              RST     0X30                
7AB1: F8 6F           LD      HL,SP+$6F           
7AB3: F0 9F           LD      A,($9F)             
7AB5: 60              LD      H,B                 
7AB6: FC                              
7AB7: 03              INC     BC                  
7AB8: F0 0F           LD      A,($0F)             
7ABA: 07              RLCA                        
7ABB: FF              RST     0X38                
7ABC: FF              RST     0X38                
7ABD: FC                              
7ABE: FC                              
7ABF: 00              NOP                         
7AC0: 01 00 07        LD      BC,$0700            
7AC3: 00              NOP                         
7AC4: 0F              RRCA                        
7AC5: 00              NOP                         
7AC6: 1E 01           LD      E,$01               
7AC8: 15              DEC     D                   
7AC9: 0B              DEC     BC                  
7ACA: 25              DEC     H                   
7ACB: 1A              LD      A,(DE)              
7ACC: 21 1E 2D        LD      HL,$2D1E            
7ACF: 1E 3E           LD      E,$3E               
7AD1: 13              INC     DE                  
7AD2: 3F              CCF                         
7AD3: 11 3F 10        LD      DE,$103F            
7AD6: 1F              RRA                         
7AD7: 08 1D 0E        LD      ($0E1D),SP          
7ADA: 0F              RRCA                        
7ADB: 07              RLCA                        
7ADC: 07              RLCA                        
7ADD: 01 01 00        LD      BC,$0001            
7AE0: FE 00           CP      $00                 
7AE2: FF              RST     0X38                
7AE3: 00              NOP                         
7AE4: 0F              RRCA                        
7AE5: F0 F7           LD      A,($F7)             
7AE7: F8 FB           LD      HL,SP+$FB           
7AE9: 0C              INC     C                   
7AEA: FB              EI                          
7AEB: 04              INC     B                   
7AEC: FA 25 F9        LD      A,($F925)           
7AEF: 07              RLCA                        
7AF0: F3              DI                          
7AF1: 0F              RRCA                        
7AF2: 8F              ADC     A,A                 
7AF3: FC                              
7AF4: FF              RST     0X38                
7AF5: F8 FF           LD      HL,SP+$FF           
7AF7: 00              NOP                         
7AF8: FC                              
7AF9: 03              INC     BC                  
7AFA: 03              INC     BC                  
7AFB: FF              RST     0X38                
7AFC: FF              RST     0X38                
7AFD: FF              RST     0X38                
7AFE: FF              RST     0X38                
7AFF: 00              NOP                         
7B00: 00              NOP                         
7B01: 00              NOP                         
7B02: 00              NOP                         
7B03: 00              NOP                         
7B04: 18 00           JR      $7B06               ; {}
7B06: 1C              INC     E                   
7B07: 08 1E 0C        LD      ($0C1E),SP          
7B0A: 0F              RRCA                        
7B0B: 06 0A           LD      B,$0A               
7B0D: 07              RLCA                        
7B0E: 04              INC     B                   
7B0F: 03              INC     BC                  
7B10: 04              INC     B                   
7B11: 03              INC     BC                  
7B12: 04              INC     B                   
7B13: 03              INC     BC                  
7B14: 08 07 01        LD      ($0107),SP          
7B17: 2E 00           LD      L,$00               
7B19: 27              DAA                         
7B1A: 00              NOP                         
7B1B: 30 00           JR      NC,$7B1D            ; {}
7B1D: 1C              INC     E                   
7B1E: 00              NOP                         
7B1F: 00              NOP                         
7B20: 00              NOP                         
7B21: 00              NOP                         
7B22: 40              LD      B,B                 
7B23: 00              NOP                         
7B24: E1              POP     HL                  
7B25: 40              LD      B,B                 
7B26: E3                              
7B27: 41              LD      B,C                 
7B28: D5              PUSH    DE                  
7B29: 63              LD      H,E                 
7B2A: F4                              
7B2B: 63              LD      H,E                 
7B2C: A8              XOR     B                   
7B2D: 77              LD      (HL),A              
7B2E: BB              CP      E                   
7B2F: 74              LD      (HL),H              
7B30: 8F              ADC     A,A                 
7B31: 70              LD      (HL),B              
7B32: 8E              ADC     A,(HL)              
7B33: 71              LD      (HL),C              
7B34: 8E              ADC     A,(HL)              
7B35: 71              LD      (HL),C              
7B36: 06 F9           LD      B,$F9               
7B38: 04              INC     B                   
7B39: FB              EI                          
7B3A: 00              NOP                         
7B3B: 0F              RRCA                        
7B3C: 00              NOP                         
7B3D: E3                              
7B3E: 00              NOP                         
7B3F: 18 00           JR      $7B41               ; {}
7B41: 00              NOP                         
7B42: 00              NOP                         
7B43: 00              NOP                         
7B44: 00              NOP                         
7B45: 00              NOP                         
7B46: 00              NOP                         
7B47: 00              NOP                         
7B48: 00              NOP                         
7B49: 00              NOP                         
7B4A: 01 00 01        LD      BC,$0100            
7B4D: 00              NOP                         
7B4E: 1E 01           LD      E,$01               
7B50: 3E 1F           LD      A,$1F               
7B52: 01 3F 00        LD      BC,$003F            
7B55: 1F              RRA                         
7B56: 06 09           LD      B,$09               
7B58: 0A              LD      A,(BC)              
7B59: 07              RLCA                        
7B5A: 14              INC     D                   
7B5B: 0F              RRCA                        
7B5C: 10 0F           ;;STOP    $0F                 
7B5E: 00              NOP                         
7B5F: 00              NOP                         
7B60: 00              NOP                         
7B61: 00              NOP                         
7B62: 00              NOP                         
7B63: 00              NOP                         
7B64: 00              NOP                         
7B65: 00              NOP                         
7B66: 00              NOP                         
7B67: 00              NOP                         
7B68: 03              INC     BC                  
7B69: 00              NOP                         
7B6A: C4 03 A5        CALL    NZ,$A503            
7B6D: C3 58 E7        JP      $E758               
7B70: 00              NOP                         
7B71: FF              RST     0X38                
7B72: 0F              RRCA                        
7B73: F0 3F           LD      A,($3F)             
7B75: C0              RET     NZ                  
7B76: CC F3 20        CALL    Z,$20F3             
7B79: FF              RST     0X38                
7B7A: 01 DF 00        LD      BC,$00DF            
7B7D: 07              RLCA                        
7B7E: 00              NOP                         
7B7F: 03              INC     BC                  
7B80: 00              NOP                         
7B81: 00              NOP                         
7B82: 00              NOP                         
7B83: 00              NOP                         
7B84: 01 00 33        LD      BC,$3300            
7B87: 01 7B 31        LD      BC,$317B            
7B8A: 4E              LD      C,(HL)              
7B8B: 39              ADD     HL,SP               
7B8C: 26 1D           LD      H,$1D               
7B8E: 10 0F           ;;STOP    $0F                 
7B90: 3C              INC     A                   
7B91: 03              INC     BC                  
7B92: 7F              LD      A,A                 
7B93: 3C              INC     A                   
7B94: 40              LD      B,B                 
7B95: 3F              CCF                         
7B96: 3D              DEC     A                   
7B97: 03              INC     BC                  
7B98: 04              INC     B                   
7B99: 03              INC     BC                  
7B9A: 02              LD      (BC),A              
7B9B: 01 01 00        LD      BC,$0001            
7B9E: 00              NOP                         
7B9F: 00              NOP                         
7BA0: 00              NOP                         
7BA1: 00              NOP                         
7BA2: 00              NOP                         
7BA3: 00              NOP                         
7BA4: 01 00 03        LD      BC,$0300            
7BA7: 01 02 01        LD      BC,$0102            
7BAA: 61              LD      H,C                 
7BAB: 00              NOP                         
7BAC: F0 60           LD      A,($60)             
7BAE: 88              ADC     A,B                 
7BAF: 70              LD      (HL),B              
7BB0: 70              LD      (HL),B              
7BB1: 00              NOP                         
7BB2: 00              NOP                         
7BB3: 00              NOP                         
7BB4: 38 00           JR      C,$7BB6             ; {}
7BB6: 68              LD      L,B                 
7BB7: 30 D1           JR      NC,$7B8A            ; {}
7BB9: 60              LD      H,B                 
7BBA: 93              SUB     E                   
7BBB: 61              LD      H,C                 
7BBC: 62              LD      H,D                 
7BBD: 01 01 00        LD      BC,$0001            
7BC0: 03              INC     BC                  
7BC1: 00              NOP                         
7BC2: F4                              
7BC3: 03              INC     BC                  
7BC4: DB                              
7BC5: 64              LD      H,H                 
7BC6: 6C              LD      L,H                 
7BC7: 33              INC     SP                  
7BC8: 39              ADD     HL,SP               
7BC9: 07              RLCA                        
7BCA: 7B              LD      A,E                 
7BCB: 07              RLCA                        
7BCC: E7              RST     0X20                
7BCD: 1B              DEC     DE                  
7BCE: DB                              
7BCF: 3D              DEC     A                   
7BD0: DD                              
7BD1: 26 6E           LD      H,$6E               
7BD3: 1B              DEC     DE                  
7BD4: 5F              LD      E,A                 
7BD5: 3B              DEC     SP                  
7BD6: BB              CP      E                   
7BD7: 75              LD      (HL),L              
7BD8: FD                              
7BD9: 66              LD      H,(HL)              
7BDA: E6 43           AND     $43                 
7BDC: 43              LD      B,E                 
7BDD: 00              NOP                         
7BDE: 00              NOP                         
7BDF: 00              NOP                         
7BE0: 87              ADD     A,A                 
7BE1: 00              NOP                         
7BE2: CC 03 7B        CALL    Z,$7B03             ; {}
7BE5: 84              ADD     A,H                 
7BE6: B4              OR      H                   
7BE7: 4B              LD      C,E                 
7BE8: CB B4           RES     1,E                 
7BEA: FF              RST     0X38                
7BEB: C4 FF 27        CALL    NZ,$27FF            
7BEE: FF              RST     0X38                
7BEF: 27              DAA                         
7BF0: FF              RST     0X38                
7BF1: E0 EE           LD      ($FF00+$EE),A       
7BF3: 1F              RRA                         
7BF4: 7F              LD      A,A                 
7BF5: FF              RST     0X38                
7BF6: FF              RST     0X38                
7BF7: F3              DI                          
7BF8: FF              RST     0X38                
7BF9: 00              NOP                         
7BFA: FE 65           CP      $65                 
7BFC: FF              RST     0X38                
7BFD: 20 30           JR      NZ,$7C2F            ; {}
7BFF: 00              NOP                         
7C00: 00              NOP                         
7C01: 00              NOP                         
7C02: 00              NOP                         
7C03: 00              NOP                         
7C04: 0E 00           LD      C,$00               
7C06: 17              RLA                         
7C07: 0E 2C           LD      C,$2C               
7C09: 1B              DEC     DE                  
7C0A: 3C              INC     A                   
7C0B: 13              INC     DE                  
7C0C: 4C              LD      C,H                 
7C0D: 37              SCF                         
7C0E: 48              LD      C,B                 
7C0F: 3F              CCF                         
7C10: 80              ADD     A,B                 
7C11: 7F              LD      A,A                 
7C12: 81              ADD     A,C                 
7C13: 7F              LD      A,A                 
7C14: 83              ADD     A,E                 
7C15: 7F              LD      A,A                 
7C16: CF              RST     0X08                
7C17: 7E              LD      A,(HL)              
7C18: FF              RST     0X38                
7C19: 78              LD      A,B                 
7C1A: FC                              
7C1B: 63              LD      H,E                 
7C1C: F2                              
7C1D: 41              LD      B,C                 
7C1E: E1              POP     HL                  
7C1F: 00              NOP                         
7C20: 03              INC     BC                  
7C21: 00              NOP                         
7C22: 04              INC     B                   
7C23: 03              INC     BC                  
7C24: 0B              DEC     BC                  
7C25: 04              INC     B                   
7C26: 1F              RRA                         
7C27: 00              NOP                         
7C28: FF              RST     0X38                
7C29: 18 FF           JR      $7C2A               ; {}
7C2B: D0              RET     NC                  
7C2C: 1F              RRA                         
7C2D: F6 0F           OR      $0F                 
7C2F: F2                              
7C30: 1F              RRA                         
7C31: E4                              
7C32: 9F              SBC     A                   
7C33: F3              DI                          
7C34: CD FE C2        CALL    $C2FE               
7C37: 7D              LD      A,L                 
7C38: FC                              
7C39: 73              LD      (HL),E              
7C3A: 70              LD      (HL),B              
7C3B: 8F              ADC     A,A                 
7C3C: 04              INC     B                   
7C3D: FB              EI                          
7C3E: FB              EI                          
7C3F: 00              NOP                         
7C40: E0 00           LD      ($FF00+$00),A       
7C42: C0              RET     NZ                  
7C43: 00              NOP                         
7C44: F0 00           LD      A,($00)             
7C46: F8 70           LD      HL,SP+$70           
7C48: F8 20           LD      HL,SP+$20           
7C4A: FC                              
7C4B: 70              LD      (HL),B              
7C4C: FF              RST     0X38                
7C4D: F8 FF           LD      HL,SP+$FF           
7C4F: FF              RST     0X38                
7C50: DB                              
7C51: 37              SCF                         
7C52: E4                              
7C53: DB                              
7C54: E6 59           AND     $59                 
7C56: 45              LD      B,L                 
7C57: B8              CP      B                   
7C58: 48              LD      C,B                 
7C59: B0              OR      B                   
7C5A: 70              LD      (HL),B              
7C5B: 80              ADD     A,B                 
7C5C: 40              LD      B,B                 
7C5D: 80              ADD     A,B                 
7C5E: 80              ADD     A,B                 
7C5F: 00              NOP                         
7C60: 07              RLCA                        
7C61: 00              NOP                         
7C62: 0F              RRCA                        
7C63: 07              RLCA                        
7C64: 1F              RRA                         
7C65: 0F              RRCA                        
7C66: 3F              CCF                         
7C67: 18 3F           JR      $7CA8               ; {}
7C69: 10 3F           ;;STOP    $3F                 
7C6B: 14              INC     D                   
7C6C: 3F              CCF                         
7C6D: 10 3F           ;;STOP    $3F                 
7C6F: 1B              DEC     DE                  
7C70: 1E 07           LD      E,$07               
7C72: 3F              CCF                         
7C73: 1F              RRA                         
7C74: 77              LD      (HL),A              
7C75: 39              ADD     HL,SP               
7C76: 4F              LD      C,A                 
7C77: 3E 27           LD      A,$27               
7C79: 1F              RRA                         
7C7A: 73              LD      (HL),E              
7C7B: 0F              RRCA                        
7C7C: F9              LD      SP,HL               
7C7D: 07              RLCA                        
7C7E: DF              RST     0X18                
7C7F: E0 E0           LD      ($FF00+$E0),A       
7C81: 00              NOP                         
7C82: F0 E0           LD      A,($E0)             
7C84: F8 F0           LD      HL,SP+$F0           
7C86: FC                              
7C87: 78              LD      A,B                 
7C88: FC                              
7C89: 70              LD      (HL),B              
7C8A: FF              RST     0X38                
7C8B: C0              RET     NZ                  
7C8C: FF              RST     0X38                
7C8D: 3E EF           LD      A,$EF               
7C8F: F1              POP     AF                  
7C90: FF              RST     0X38                
7C91: 3E FF           LD      A,$FF               
7C93: CF              RST     0X08                
7C94: FF              RST     0X38                
7C95: F0 FF           LD      A,($FF)             
7C97: 70              LD      (HL),B              
7C98: FF              RST     0X38                
7C99: 80              ADD     A,B                 
7C9A: FF              RST     0X38                
7C9B: 80              ADD     A,B                 
7C9C: E7              RST     0X20                
7C9D: 98              SBC     B                   
7C9E: F3              DI                          
7C9F: 0C              INC     C                   
7CA0: 00              NOP                         
7CA1: 00              NOP                         
7CA2: 00              NOP                         
7CA3: 00              NOP                         
7CA4: 00              NOP                         
7CA5: 00              NOP                         
7CA6: 00              NOP                         
7CA7: 00              NOP                         
7CA8: 00              NOP                         
7CA9: 00              NOP                         
7CAA: E0 00           LD      ($FF00+$00),A       
7CAC: FC                              
7CAD: 00              NOP                         
7CAE: FE 00           CP      $00                 
7CB0: FF              RST     0X38                
7CB1: 00              NOP                         
7CB2: E7              RST     0X20                
7CB3: 00              NOP                         
7CB4: F3              DI                          
7CB5: 00              NOP                         
7CB6: FF              RST     0X38                
7CB7: 03              INC     BC                  
7CB8: 7F              LD      A,A                 
7CB9: 83              ADD     A,E                 
7CBA: 3F              CCF                         
7CBB: C1              POP     BC                  
7CBC: BF              CP      A                   
7CBD: 51              LD      D,C                 
7CBE: BF              CP      A                   
7CBF: 5E              LD      E,(HL)              
7CC0: FF              RST     0X38                
7CC1: E0 7F           LD      ($FF00+$7F),A       
7CC3: E0 1E           LD      ($FF00+$1E),A       
7CC5: E1              POP     HL                  
7CC6: BF              CP      A                   
7CC7: 40              LD      B,B                 
7CC8: FF              RST     0X38                
7CC9: 00              NOP                         
7CCA: 7F              LD      A,A                 
7CCB: 00              NOP                         
7CCC: 3F              CCF                         
7CCD: 00              NOP                         
7CCE: 3F              CCF                         
7CCF: 00              NOP                         
7CD0: 1A              LD      A,(DE)              
7CD1: 01 01 00        LD      BC,$0001            
7CD4: 01 00 00        LD      BC,$0000            
7CD7: 00              NOP                         
7CD8: 00              NOP                         
7CD9: 00              NOP                         
7CDA: 00              NOP                         
7CDB: 00              NOP                         
7CDC: 00              NOP                         
7CDD: 00              NOP                         
7CDE: 00              NOP                         
7CDF: 00              NOP                         
7CE0: F8 07           LD      HL,SP+$07           
7CE2: 78              LD      A,B                 
7CE3: 87              ADD     A,A                 
7CE4: 39              ADD     HL,SP               
7CE5: C6 01           ADD     $01                 
7CE7: FE 07           CP      $07                 
7CE9: F8 00           LD      HL,SP+$00           
7CEB: FF              RST     0X38                
7CEC: 80              ADD     A,B                 
7CED: 7F              LD      A,A                 
7CEE: 80              ADD     A,B                 
7CEF: 7F              LD      A,A                 
7CF0: 00              NOP                         
7CF1: FF              RST     0X38                
7CF2: 00              NOP                         
7CF3: FF              RST     0X38                
7CF4: 18 FF           JR      $7CF5               ; {}
7CF6: E7              RST     0X20                
7CF7: 1F              RRA                         
7CF8: 18 07           JR      $7D01               ; {}
7CFA: 07              RLCA                        
7CFB: 00              NOP                         
7CFC: 00              NOP                         
7CFD: 00              NOP                         
7CFE: 00              NOP                         
7CFF: 00              NOP                         
7D00: 0C              INC     C                   
7D01: FF              RST     0X38                
7D02: 18 EF           JR      $7CF3               ; {}
7D04: 23              INC     HL                  
7D05: DC C4 3B        CALL    C,$3BC4             
7D08: 0E FF           LD      C,$FF               
7D0A: 1E FF           LD      E,$FF               
7D0C: 0E FF           LD      C,$FF               
7D0E: 00              NOP                         
7D0F: FF              RST     0X38                
7D10: 11 EE 3F        LD      DE,$3FEE            
7D13: C0              RET     NZ                  
7D14: 08 F0 90        LD      ($90F0),SP          
7D17: E0 60           LD      ($FF00+$60),A       
7D19: 80              ADD     A,B                 
7D1A: 80              ADD     A,B                 
7D1B: 00              NOP                         
7D1C: 00              NOP                         
7D1D: 00              NOP                         
7D1E: 00              NOP                         
7D1F: 00              NOP                         
7D20: 78              LD      A,B                 
7D21: 00              NOP                         
7D22: FF              RST     0X38                
7D23: 00              NOP                         
7D24: FF              RST     0X38                
7D25: 80              ADD     A,B                 
7D26: FE 98           CP      $98                 
7D28: FC                              
7D29: 70              LD      (HL),B              
7D2A: F8 C0           LD      HL,SP+$C0           
7D2C: 7E              LD      A,(HL)              
7D2D: 80              ADD     A,B                 
7D2E: FD                              
7D2F: 0E F9           LD      C,$F9               
7D31: 26 FD           LD      H,$FD               
7D33: 26 F1           LD      H,$F1               
7D35: 1E F6           LD      E,$F6               
7D37: 78              LD      A,B                 
7D38: C8              RET     Z                   
7D39: 30 70           JR      NC,$7DAB            ; {}
7D3B: 80              ADD     A,B                 
7D3C: C0              RET     NZ                  
7D3D: 00              NOP                         
7D3E: 80              ADD     A,B                 
7D3F: 00              NOP                         
7D40: 06 00           LD      B,$00               
7D42: 0E 00           LD      C,$00               
7D44: 1E 00           LD      E,$00               
7D46: 3F              CCF                         
7D47: 00              NOP                         
7D48: 7F              LD      A,A                 
7D49: 00              NOP                         
7D4A: 7F              LD      A,A                 
7D4B: 01 FF 0F        LD      BC,$0FFF            
7D4E: FF              RST     0X38                
7D4F: 5F              LD      E,A                 
7D50: FF              RST     0X38                
7D51: 5F              LD      E,A                 
7D52: EF              RST     0X28                
7D53: 5F              LD      E,A                 
7D54: FF              RST     0X38                
7D55: 6F              LD      L,A                 
7D56: BF              CP      A                   
7D57: 6F              LD      L,A                 
7D58: 77              LD      (HL),A              
7D59: 2F              CPL                         
7D5A: 7F              LD      A,A                 
7D5B: 37              SCF                         
7D5C: 7F              LD      A,A                 
7D5D: 37              SCF                         
7D5E: 5F              LD      E,A                 
7D5F: 37              SCF                         
7D60: 00              NOP                         
7D61: 00              NOP                         
7D62: 03              INC     BC                  
7D63: 00              NOP                         
7D64: 1F              RRA                         
7D65: 00              NOP                         
7D66: FF              RST     0X38                
7D67: 00              NOP                         
7D68: FF              RST     0X38                
7D69: 7C              LD      A,H                 
7D6A: FF              RST     0X38                
7D6B: FC                              
7D6C: FF              RST     0X38                
7D6D: F8 FF           LD      HL,SP+$FF           
7D6F: F0 CF           LD      A,($CF)             
7D71: FC                              
7D72: FF              RST     0X38                
7D73: FC                              
7D74: FF              RST     0X38                
7D75: F8 F7           LD      HL,SP+$F7           
7D77: FE EF           CP      $EF                 
7D79: FE FF           CP      $FF                 
7D7B: FC                              
7D7C: FF              RST     0X38                
7D7D: FA F7 FE        LD      A,($FEF7)           
7D80: 7E              LD      A,(HL)              
7D81: 00              NOP                         
7D82: FE 00           CP      $00                 
7D84: FC                              
7D85: 00              NOP                         
7D86: F0 00           LD      A,($00)             
7D88: FF              RST     0X38                
7D89: 00              NOP                         
7D8A: FF              RST     0X38                
7D8B: 00              NOP                         
7D8C: FE 00           CP      $00                 
7D8E: F0 00           LD      A,($00)             
7D90: C0              RET     NZ                  
7D91: 00              NOP                         
7D92: FC                              
7D93: 00              NOP                         
7D94: FE 00           CP      $00                 
7D96: FC                              
7D97: 00              NOP                         
7D98: F0 00           LD      A,($00)             
7D9A: C0              RET     NZ                  
7D9B: 00              NOP                         
7D9C: F0 00           LD      A,($00)             
7D9E: E0 00           LD      ($FF00+$00),A       
7DA0: C0              RET     NZ                  
7DA1: 00              NOP                         
7DA2: F8 00           LD      HL,SP+$00           
7DA4: FC                              
7DA5: 78              LD      A,B                 
7DA6: FF              RST     0X38                
7DA7: F0 FF           LD      A,($FF)             
7DA9: 3F              CCF                         
7DAA: FB              EI                          
7DAB: 7F              LD      A,A                 
7DAC: F3              DI                          
7DAD: FF              RST     0X38                
7DAE: E5              PUSH    HL                  
7DAF: FB              EI                          
7DB0: 04              INC     B                   
7DB1: FB              EI                          
7DB2: C4 3B 44        CALL    NZ,$443B            ; {}
7DB5: BB              CP      E                   
7DB6: 4C              LD      C,H                 
7DB7: B3              OR      E                   
7DB8: 72              LD      (HL),D              
7DB9: 81              ADD     A,C                 
7DBA: 47              LD      B,A                 
7DBB: 80              ADD     A,B                 
7DBC: 8F              ADC     A,A                 
7DBD: 00              NOP                         
7DBE: 0F              RRCA                        
7DBF: 00              NOP                         
7DC0: 3F              CCF                         
7DC1: 17              RLA                         
7DC2: 3B              DEC     SP                  
7DC3: 17              RLA                         
7DC4: 3F              CCF                         
7DC5: 1B              DEC     DE                  
7DC6: BF              CP      A                   
7DC7: 1B              DEC     DE                  
7DC8: BF              CP      A                   
7DC9: 1B              DEC     DE                  
7DCA: BF              CP      A                   
7DCB: 1B              DEC     DE                  
7DCC: FF              RST     0X38                
7DCD: 9B              SBC     E                   
7DCE: FF              RST     0X38                
7DCF: DB                              
7DD0: FF              RST     0X38                
7DD1: DB                              
7DD2: 7B              LD      A,E                 
7DD3: D7              RST     0X10                
7DD4: 6F              LD      L,A                 
7DD5: D7              RST     0X10                
7DD6: 7F              LD      A,A                 
7DD7: 87              ADD     A,A                 
7DD8: FF              RST     0X38                
7DD9: 0F              RRCA                        
7DDA: FF              RST     0X38                
7DDB: 0F              RRCA                        
7DDC: FF              RST     0X38                
7DDD: 1F              RRA                         
7DDE: FF              RST     0X38                
7DDF: 1E FF           LD      E,$FF               
7DE1: FC                              
7DE2: FE F8           CP      $F8                 
7DE4: FF              RST     0X38                
7DE5: F0 EF           LD      A,($EF)             
7DE7: F8 FF           LD      HL,SP+$FF           
7DE9: F8 FE           LD      HL,SP+$FE           
7DEB: F0 FF           LD      A,($FF)             
7DED: F8 FF           LD      HL,SP+$FF           
7DEF: F8 FF           LD      HL,SP+$FF           
7DF1: C0              RET     NZ                  
7DF2: FC                              
7DF3: E0 F8           LD      ($FF00+$F8),A       
7DF5: E0 F8           LD      ($FF00+$F8),A       
7DF7: 00              NOP                         
7DF8: E0 80           LD      ($FF00+$80),A       
7DFA: EC                              
7DFB: 80              ADD     A,B                 
7DFC: FC                              
7DFD: 00              NOP                         
7DFE: FF              RST     0X38                
7DFF: 00              NOP                         
7E00: 00              NOP                         
7E01: 00              NOP                         
7E02: 00              NOP                         
7E03: 00              NOP                         
7E04: 00              NOP                         
7E05: 00              NOP                         
7E06: 36 00           LD      (HL),$00            
7E08: 4F              LD      C,A                 
7E09: 36 D9           LD      (HL),$D9            
7E0B: 6E              LD      L,(HL)              
7E0C: FD                              
7E0D: 02              LD      (BC),A              
7E0E: FF              RST     0X38                
7E0F: 6C              LD      L,H                 
7E10: 7E              LD      A,(HL)              
7E11: 24              INC     H                   
7E12: 24              INC     H                   
7E13: 00              NOP                         
7E14: 00              NOP                         
7E15: 00              NOP                         
7E16: 0E 00           LD      C,$00               
7E18: 0F              RRCA                        
7E19: 06 07           LD      B,$07               
7E1B: 02              LD      (BC),A              
7E1C: 03              INC     BC                  
7E1D: 00              NOP                         
7E1E: 00              NOP                         
7E1F: 00              NOP                         
7E20: 0F              RRCA                        
7E21: 00              NOP                         
7E22: 0F              RRCA                        
7E23: 04              INC     B                   
7E24: 1F              RRA                         
7E25: 0F              RRCA                        
7E26: 7F              LD      A,A                 
7E27: 03              INC     BC                  
7E28: DF              RST     0X18                
7E29: 6D              LD      L,L                 
7E2A: B3              OR      E                   
7E2B: DE F9           SBC     $F9                 
7E2D: 06 FD           LD      B,$FD               
7E2F: DA FD 4B        JP      C,$4BFD             ; {}
7E32: FD                              
7E33: 03              INC     BC                  
7E34: A7              AND     A                   
7E35: 59              LD      E,C                 
7E36: 9E              SBC     (HL)                
7E37: 61              LD      H,C                 
7E38: FC                              
7E39: 1B              DEC     DE                  
7E3A: 7E              LD      A,(HL)              
7E3B: 8D              ADC     A,L                 
7E3C: 2F              CPL                         
7E3D: C0              RET     NZ                  
7E3E: C0              RET     NZ                  
7E3F: 00              NOP                         
7E40: FF              RST     0X38                
7E41: 7F              LD      A,A                 
7E42: FF              RST     0X38                
7E43: 7F              LD      A,A                 
7E44: FF              RST     0X38                
7E45: FF              RST     0X38                
7E46: FF              RST     0X38                
7E47: FF              RST     0X38                
7E48: FF              RST     0X38                
7E49: FF              RST     0X38                
7E4A: FF              RST     0X38                
7E4B: FF              RST     0X38                
7E4C: 3D              DEC     A                   
7E4D: DF              RST     0X18                
7E4E: F2                              
7E4F: 3D              DEC     A                   
7E50: F2                              
7E51: 7D              LD      A,L                 
7E52: E3                              
7E53: 7C              LD      A,H                 
7E54: 82              ADD     A,D                 
7E55: 7C              LD      A,H                 
7E56: C4 B8 64        CALL    NZ,$64B8            ; {}
7E59: D8              RET     C                   
7E5A: 98              SBC     B                   
7E5B: 60              LD      H,B                 
7E5C: 90              SUB     B                   
7E5D: 60              LD      H,B                 
7E5E: 60              LD      H,B                 
7E5F: 00              NOP                         
7E60: FF              RST     0X38                
7E61: 90              SUB     B                   
7E62: EF              RST     0X28                
7E63: B0              OR      B                   
7E64: EE F0           XOR     $F0                 
7E66: DC E0 BC        CALL    C,$BCE0             
7E69: C0              RET     NZ                  
7E6A: 0E F0           LD      C,$F0               
7E6C: 0E F0           LD      C,$F0               
7E6E: 1E E0           LD      E,$E0               
7E70: 78              LD      A,B                 
7E71: 80              ADD     A,B                 
7E72: 80              ADD     A,B                 
7E73: 00              NOP                         
7E74: 00              NOP                         
7E75: 00              NOP                         
7E76: 00              NOP                         
7E77: 00              NOP                         
7E78: 00              NOP                         
7E79: 00              NOP                         
7E7A: 00              NOP                         
7E7B: 00              NOP                         
7E7C: 00              NOP                         
7E7D: 00              NOP                         
7E7E: 00              NOP                         
7E7F: 00              NOP                         
7E80: 0E 00           LD      C,$00               
7E82: 3F              CCF                         
7E83: 00              NOP                         
7E84: 7F              LD      A,A                 
7E85: 00              NOP                         
7E86: FF              RST     0X38                
7E87: 00              NOP                         
7E88: FF              RST     0X38                
7E89: 00              NOP                         
7E8A: F7              RST     0X30                
7E8B: 08 E7 18        LD      ($18E7),SP          
7E8E: F6 E9           OR      $E9                 
7E90: F6 E9           OR      $E9                 
7E92: 70              LD      (HL),B              
7E93: EF              RST     0X28                
7E94: 70              LD      (HL),B              
7E95: CF              RST     0X08                
7E96: 70              LD      (HL),B              
7E97: 8F              ADC     A,A                 
7E98: F0 0F           LD      A,($0F)             
7E9A: F0 0F           LD      A,($0F)             
7E9C: FC                              
7E9D: 1F              RRA                         
7E9E: FF              RST     0X38                
7E9F: 1E 00           LD      E,$00               
7EA1: 00              NOP                         
7EA2: C0              RET     NZ                  
7EA3: 00              NOP                         
7EA4: F0 00           LD      A,($00)             
7EA6: F8 00           LD      HL,SP+$00           
7EA8: FC                              
7EA9: 00              NOP                         
7EAA: FE 00           CP      $00                 
7EAC: 7E              LD      A,(HL)              
7EAD: 80              ADD     A,B                 
7EAE: 77              LD      (HL),A              
7EAF: 88              ADC     A,B                 
7EB0: 77              LD      (HL),A              
7EB1: 88              ADC     A,B                 
7EB2: 66              LD      H,(HL)              
7EB3: 98              SBC     B                   
7EB4: 0F              RRCA                        
7EB5: F0 0E           LD      A,($0E)             
7EB7: F0 78           LD      A,($78)             
7EB9: 80              ADD     A,B                 
7EBA: 3C              INC     A                   
7EBB: C0              RET     NZ                  
7EBC: 7C              LD      A,H                 
7EBD: 80              ADD     A,B                 
7EBE: FF              RST     0X38                
7EBF: 00              NOP                         
7EC0: C0              RET     NZ                  
7EC1: 00              NOP                         
7EC2: F8 00           LD      HL,SP+$00           
7EC4: FC                              
7EC5: 78              LD      A,B                 
7EC6: FF              RST     0X38                
7EC7: F0 FF           LD      A,($FF)             
7EC9: 3F              CCF                         
7ECA: FB              EI                          
7ECB: 7F              LD      A,A                 
7ECC: F3              DI                          
7ECD: FF              RST     0X38                
7ECE: E5              PUSH    HL                  
7ECF: FB              EI                          
7ED0: 05              DEC     B                   
7ED1: FA C5 3A        LD      A,($3AC5)           
7ED4: 47              LD      B,A                 
7ED5: B8              CP      B                   
7ED6: 4F              LD      C,A                 
7ED7: B0              OR      B                   
7ED8: 7F              LD      A,A                 
7ED9: 80              ADD     A,B                 
7EDA: 5F              LD      E,A                 
7EDB: 81              ADD     A,C                 
7EDC: 9F              SBC     A                   
7EDD: 01 3F 03        LD      BC,$033F            
7EE0: 03              INC     BC                  
7EE1: 00              NOP                         
7EE2: 07              RLCA                        
7EE3: 03              INC     BC                  
7EE4: 0F              RRCA                        
7EE5: 07              RLCA                        
7EE6: 1F              RRA                         
7EE7: 0C              INC     C                   
7EE8: FF              RST     0X38                
7EE9: 08 FF 72        LD      ($72FF),SP          ; {}
7EEC: FF              RST     0X38                
7EED: 7C              LD      A,H                 
7EEE: FF              RST     0X38                
7EEF: 7E              LD      A,(HL)              
7EF0: FF              RST     0X38                
7EF1: 7F              LD      A,A                 
7EF2: FF              RST     0X38                
7EF3: FF              RST     0X38                
7EF4: FF              RST     0X38                
7EF5: FF              RST     0X38                
7EF6: FF              RST     0X38                
7EF7: FF              RST     0X38                
7EF8: FF              RST     0X38                
7EF9: FF              RST     0X38                
7EFA: FD                              
7EFB: FE FF           CP      $FF                 
7EFD: FF              RST     0X38                
7EFE: FF              RST     0X38                
7EFF: FF              RST     0X38                
7F00: E0 00           LD      ($FF00+$00),A       
7F02: F8 E0           LD      HL,SP+$E0           
7F04: FC                              
7F05: F8 FC           LD      HL,SP+$FC           
7F07: 38 FE           JR      C,$7F07             ; {}
7F09: 3C              INC     A                   
7F0A: FE 7C           CP      $7C                 
7F0C: FE E0           CP      $E0                 
7F0E: FC                              
7F0F: 80              ADD     A,B                 
7F10: FE 00           CP      $00                 
7F12: FE 80           CP      $80                 
7F14: FE 80           CP      $80                 
7F16: FC                              
7F17: 00              NOP                         
7F18: F0 00           LD      A,($00)             
7F1A: EC                              
7F1B: 00              NOP                         
7F1C: FC                              
7F1D: 00              NOP                         
7F1E: FF              RST     0X38                
7F1F: 00              NOP                         
7F20: 3F              CCF                         
7F21: 07              RLCA                        
7F22: 5F              LD      E,A                 
7F23: 2F              CPL                         
7F24: 5F              LD      E,A                 
7F25: 2F              CPL                         
7F26: FF              RST     0X38                
7F27: 1F              RRA                         
7F28: FF              RST     0X38                
7F29: 5F              LD      E,A                 
7F2A: FB              EI                          
7F2B: BF              CP      A                   
7F2C: FF              RST     0X38                
7F2D: 3B              DEC     SP                  
7F2E: FF              RST     0X38                
7F2F: B3              OR      E                   
7F30: FF              RST     0X38                
7F31: 22              LD      (HLI),A             
7F32: FF              RST     0X38                
7F33: 00              NOP                         
7F34: FF              RST     0X38                
7F35: 00              NOP                         
7F36: FF              RST     0X38                
7F37: 00              NOP                         
7F38: FF              RST     0X38                
7F39: 00              NOP                         
7F3A: EF              RST     0X28                
7F3B: 00              NOP                         
7F3C: 2E C0           LD      L,$C0               
7F3E: CC 00 FD        CALL    Z,$FD00             
7F41: FE FF           CP      $FF                 
7F43: FE FF           CP      $FF                 
7F45: FF              RST     0X38                
7F46: FB              EI                          
7F47: FD                              
7F48: FF              RST     0X38                
7F49: FC                              
7F4A: 7F              LD      A,A                 
7F4B: FE EF           CP      $EF                 
7F4D: 7E              LD      A,(HL)              
7F4E: FF              RST     0X38                
7F4F: 6E              LD      L,(HL)              
7F50: FF              RST     0X38                
7F51: 4E              LD      C,(HL)              
7F52: FF              RST     0X38                
7F53: 04              INC     B                   
7F54: FF              RST     0X38                
7F55: 00              NOP                         
7F56: FF              RST     0X38                
7F57: 00              NOP                         
7F58: 7F              LD      A,A                 
7F59: 00              NOP                         
7F5A: 77              LD      (HL),A              
7F5B: 00              NOP                         
7F5C: 76              HALT                        
7F5D: 00              NOP                         
7F5E: 60              LD      H,B                 
7F5F: 00              NOP                         
7F60: FF              RST     0X38                
7F61: 10 EF           ;;STOP    $EF                 
7F63: 30 EE           JR      NC,$7F53            ; {}
7F65: 30 DC           JR      NC,$7F43            ; {}
7F67: 20 FC           JR      NZ,$7F65            ; {}
7F69: 00              NOP                         
7F6A: CE 30           ADC     $30                 
7F6C: CE 30           ADC     $30                 
7F6E: 9E              SBC     (HL)                
7F6F: 60              LD      H,B                 
7F70: F8 00           LD      HL,SP+$00           
7F72: 80              ADD     A,B                 
7F73: 00              NOP                         
7F74: 00              NOP                         
7F75: 00              NOP                         
7F76: 00              NOP                         
7F77: 00              NOP                         
7F78: 00              NOP                         
7F79: 00              NOP                         
7F7A: 00              NOP                         
7F7B: 00              NOP                         
7F7C: 00              NOP                         
7F7D: 00              NOP                         
7F7E: 00              NOP                         
7F7F: 00              NOP                         
7F80: 00              NOP                         
7F81: 00              NOP                         
7F82: 00              NOP                         
7F83: 00              NOP                         
7F84: 00              NOP                         
7F85: 00              NOP                         
7F86: 00              NOP                         
7F87: 00              NOP                         
7F88: 00              NOP                         
7F89: 00              NOP                         
7F8A: 01 00 07        LD      BC,$0700            
7F8D: 00              NOP                         
7F8E: 0B              DEC     BC                  
7F8F: 07              RLCA                        
7F90: 17              RLA                         
7F91: 0F              RRCA                        
7F92: 1F              RRA                         
7F93: 0F              RRCA                        
7F94: 7F              LD      A,A                 
7F95: 1F              RRA                         
7F96: FF              RST     0X38                
7F97: 60              LD      H,B                 
7F98: E0 00           LD      ($FF00+$00),A       
7F9A: 00              NOP                         
7F9B: 00              NOP                         
7F9C: 00              NOP                         
7F9D: 00              NOP                         
7F9E: 00              NOP                         
7F9F: 00              NOP                         
7FA0: 00              NOP                         
7FA1: 00              NOP                         
7FA2: 00              NOP                         
7FA3: 00              NOP                         
7FA4: 00              NOP                         
7FA5: 00              NOP                         
7FA6: 00              NOP                         
7FA7: 00              NOP                         
7FA8: 00              NOP                         
7FA9: 00              NOP                         
7FAA: FE 00           CP      $00                 
7FAC: FE 00           CP      $00                 
7FAE: 7C              LD      A,H                 
7FAF: 80              ADD     A,B                 
7FB0: B8              CP      B                   
7FB1: C0              RET     NZ                  
7FB2: B0              OR      B                   
7FB3: C0              RET     NZ                  
7FB4: C0              RET     NZ                  
7FB5: 00              NOP                         
7FB6: 00              NOP                         
7FB7: 00              NOP                         
7FB8: 00              NOP                         
7FB9: 00              NOP                         
7FBA: 00              NOP                         
7FBB: 00              NOP                         
7FBC: 00              NOP                         
7FBD: 00              NOP                         
7FBE: 00              NOP                         
7FBF: 00              NOP                         
7FC0: C0              RET     NZ                  
7FC1: 00              NOP                         
7FC2: E0 00           LD      ($FF00+$00),A       
7FC4: F0 00           LD      A,($00)             
7FC6: 88              ADC     A,B                 
7FC7: 70              LD      (HL),B              
7FC8: B8              CP      B                   
7FC9: 70              LD      (HL),B              
7FCA: BB              CP      E                   
7FCB: 70              LD      (HL),B              
7FCC: 7F              LD      A,A                 
7FCD: 30 3F           JR      NC,$800E            
7FCF: 06 1F           LD      B,$1F               
7FD1: 0F              RRCA                        
7FD2: 1F              RRA                         
7FD3: 0D              DEC     C                   
7FD4: 1F              RRA                         
7FD5: 0D              DEC     C                   
7FD6: 1F              RRA                         
7FD7: 06 0F           LD      B,$0F               
7FD9: 00              NOP                         
7FDA: 07              RLCA                        
7FDB: 00              NOP                         
7FDC: 00              NOP                         
7FDD: 00              NOP                         
7FDE: 00              NOP                         
7FDF: 00              NOP                         
7FE0: 07              RLCA                        
7FE1: 00              NOP                         
7FE2: 1F              RRA                         
7FE3: 07              RLCA                        
7FE4: 3F              CCF                         
7FE5: 1F              RRA                         
7FE6: 7F              LD      A,A                 
7FE7: 23              INC     HL                  
7FE8: 7F              LD      A,A                 
7FE9: 21 7F 25        LD      HL,$257F            
7FEC: 5F              LD      E,A                 
7FED: 31 7F 0D        LD      SP,$0D7F            
7FF0: FF              RST     0X38                
7FF1: 07              RLCA                        
7FF2: FF              RST     0X38                
7FF3: 46              LD      B,(HL)              
7FF4: FF              RST     0X38                
7FF5: 62              LD      H,D                 
7FF6: F7              RST     0X30                
7FF7: 68              LD      L,B                 
7FF8: 7B              LD      A,E                 
7FF9: 04              INC     B                   
7FFA: 74              LD      (HL),H              
7FFB: 1B              DEC     DE                  
7FFC: FB              EI                          
7FFD: 7C              LD      A,H                 
7FFE: FE 00           CP      $00                 
```

