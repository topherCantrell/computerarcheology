![Bank 1B](GBZelda.jpg)

# Bank 1B

>>> cpu Z80GB

>>> binary 4000:roms/zelda.gb[6C000:70000]

>>> memoryTable ram 

[RAM Usage](RAMUse.md)

>>> memoryTable hard 

[Hardware Info](../Hardware.md)

```code
4000: C3 09 40        JP      $4009               ; {}
4003: C3 9E 4D        JP      $4D9E               ; {}
4006: C3 1E 40        JP      $401E               ; {}
4009: 21 00 D3        LD      HL,$D300            
400C: 36 00           LD      (HL),$00            
400E: 2C              INC     L                   
400F: 20 FB           JR      NZ,$400C            ; {}
4011: 3E 80           LD      A,$80               
4013: E0 26           LD      ($FF00+$26),A       
4015: 3E 77           LD      A,$77               
4017: E0 24           LD      ($FF00+$24),A       
4019: 3E FF           LD      A,$FF               
401B: E0 25           LD      ($FF00+$25),A       
401D: C9              RET                         
401E: 21 68 D3        LD      HL,$D368            
4021: 2A              LD      A,(HLI)             
4022: A7              AND     A                   
4023: 20 0C           JR      NZ,$4031            ; {}
4025: CD 37 40        CALL    $4037               ; {}
4028: CD 81 44        CALL    $4481               ; {}
402B: C9              RET                         
402C: AF              XOR     A                   
402D: EA CE D3        LD      ($D3CE),A           
4030: C9              RET                         
4031: 77              LD      (HL),A              
4032: CD 1B 41        CALL    $411B               ; {}
4035: 18 F1           JR      $4028               ; {}
4037: 11 93 D3        LD      DE,$D393            
403A: 21 78 D3        LD      HL,$D378            
403D: 2A              LD      A,(HLI)             
403E: FE 01           CP      $01                 
4040: 28 06           JR      Z,$4048             ; {}
4042: 7E              LD      A,(HL)              
4043: FE 01           CP      $01                 
4045: 28 0C           JR      Z,$4053             ; {}
4047: C9              RET                         
4048: 3E 01           LD      A,$01               
404A: EA 79 D3        LD      ($D379),A           
404D: 21 60 40        LD      HL,$4060            
4050: C3 6A 40        JP      $406A               ; {}
4053: 1A              LD      A,(DE)              
4054: 3D              DEC     A                   
4055: 12              LD      (DE),A              
4056: C0              RET     NZ                  
4057: AF              XOR     A                   
4058: EA 79 D3        LD      ($D379),A           
405B: 21 65 40        LD      HL,$4065            
405E: 18 0A           JR      $406A               ; {}
4060: 3B              DEC     SP                  
4061: 80              ADD     A,B                 
4062: 07              RLCA                        
4063: C0              RET     NZ                  
4064: 02              LD      (BC),A              
4065: 00              NOP                         
4066: 42              LD      B,D                 
4067: 02              LD      (BC),A              
4068: C0              RET     NZ                  
4069: 04              INC     B                   
406A: 06 04           LD      B,$04               
406C: 0E 20           LD      C,$20               
406E: 2A              LD      A,(HLI)             
406F: E2              LD      (C),A               
4070: 0C              INC     C                   
4071: 05              DEC     B                   
4072: 20 FA           JR      NZ,$406E            ; {}
4074: 7E              LD      A,(HL)              
4075: 12              LD      (DE),A              
4076: C9              RET                         
4077: 34              INC     (HL)                
4078: 50              LD      D,B                 
4079: E2              LD      (C),A               
407A: 51              LD      D,C                 
407B: 93              SUB     E                   
407C: 52              LD      D,D                 
407D: 2C              INC     L                   
407E: 53              LD      D,E                 
407F: 05              DEC     B                   
4080: 54              LD      D,H                 
4081: 58              LD      E,B                 
4082: 57              LD      D,A                 
4083: F0 59           LD      A,($59)             
4085: 8D              ADC     A,L                 
4086: 5A              LD      E,D                 
4087: 7D              LD      A,L                 
4088: 5B              LD      E,E                 
4089: 71              LD      (HL),C              
408A: 5C              LD      E,H                 
408B: 09              ADD     HL,BC               
408C: 5D              LD      E,L                 
408D: B8              CP      B                   
408E: 5D              LD      E,L                 
408F: 08 5E 27        LD      ($275E),SP          
4092: 5E              LD      E,(HL)              
4093: A7              AND     A                   
4094: 5E              LD      E,(HL)              
4095: A8              XOR     B                   
4096: 4A              LD      C,D                 
4097: 0A              LD      A,(BC)              
4098: 5F              LD      E,A                 
4099: C1              POP     BC                  
409A: 5F              LD      E,A                 
409B: 17              RLA                         
409C: 60              LD      H,B                 
409D: 96              SUB     (HL)                
409E: 60              LD      H,B                 
409F: 5F              LD      E,A                 
40A0: 61              LD      H,C                 
40A1: 41              LD      B,C                 
40A2: 62              LD      H,D                 
40A3: 1E 4D           LD      E,$4D               
40A5: 00              NOP                         
40A6: 50              LD      D,B                 
40A7: 15              DEC     D                   
40A8: 63              LD      H,E                 
40A9: 3E 64           LD      A,$64               
40AB: DF              RST     0X18                
40AC: 64              LD      H,H                 
40AD: EC                              
40AE: 4B              LD      C,E                 
40AF: 13              INC     DE                  
40B0: 65              LD      H,L                 
40B1: 9C              SBC     H                   
40B2: 6B              LD      L,E                 
40B3: EA 6B 01        LD      ($016B),A           
40B6: 4B              LD      C,E                 
40B7: 1C              INC     E                   
40B8: 3D              DEC     A                   
40B9: CB 27           SLA     1,E                 
40BB: 4F              LD      C,A                 
40BC: 06 00           LD      B,$00               
40BE: 09              ADD     HL,BC               
40BF: 4E              LD      C,(HL)              
40C0: 23              INC     HL                  
40C1: 46              LD      B,(HL)              
40C2: 69              LD      L,C                 
40C3: 60              LD      H,B                 
40C4: 7C              LD      A,H                 
40C5: C9              RET                         
40C6: C5              PUSH    BC                  
40C7: 0E 30           LD      C,$30               
40C9: 2A              LD      A,(HLI)             
40CA: E2              LD      (C),A               
40CB: 0C              INC     C                   
40CC: 79              LD      A,C                 
40CD: FE 40           CP      $40                 
40CF: 20 F8           JR      NZ,$40C9            ; {}
40D1: C1              POP     BC                  
40D2: C9              RET                         
40D3: AF              XOR     A                   
40D4: EA 79 D3        LD      ($D379),A           
40D7: EA 4F D3        LD      ($D34F),A           
40DA: EA 98 D3        LD      ($D398),A           
40DD: EA 93 D3        LD      ($D393),A           
40E0: EA C9 D3        LD      ($D3C9),A           
40E3: EA A3 D3        LD      ($D3A3),A           
40E6: 3E 08           LD      A,$08               
40E8: E0 21           LD      ($FF00+$21),A       
40EA: 3E 80           LD      A,$80               
40EC: E0 23           LD      ($FF00+$23),A       
40EE: C9              RET                         
40EF: FA 79 D3        LD      A,($D379)           
40F2: FE 0C           CP      $0C                 
40F4: CA BC 4D        JP      Z,$4DBC             ; {}
40F7: FE 05           CP      $05                 
40F9: CA BC 4D        JP      Z,$4DBC             ; {}
40FC: FE 1A           CP      $1A                 
40FE: CA BC 4D        JP      Z,$4DBC             ; {}
4101: FE 24           CP      $24                 
4103: CA BC 4D        JP      Z,$4DBC             ; {}
4106: FE 2A           CP      $2A                 
4108: CA BC 4D        JP      Z,$4DBC             ; {}
410B: FE 2E           CP      $2E                 
410D: CA BC 4D        JP      Z,$4DBC             ; {}
4110: FE 3F           CP      $3F                 
4112: CA BC 4D        JP      Z,$4DBC             ; {}
4115: CD D3 40        CALL    $40D3               ; {}
4118: C3 BC 4D        JP      $4DBC               ; {}
411B: FE FF           CP      $FF                 
411D: 28 D0           JR      Z,$40EF             ; {}
411F: FA CA D3        LD      A,($D3CA)           
4122: EA CB D3        LD      ($D3CB),A           
4125: 7E              LD      A,(HL)              
4126: EA CA D3        LD      ($D3CA),A           
4129: FE 11           CP      $11                 
412B: 30 02           JR      NC,$412F            ; {}
412D: 18 15           JR      $4144               ; {}
412F: FE 21           CP      $21                 
4131: 30 03           JR      NC,$4136            ; {}
4133: C3 2C 40        JP      $402C               ; {}
4136: FE 31           CP      $31                 
4138: 30 03           JR      NC,$413D            ; {}
413A: C3 2C 40        JP      $402C               ; {}
413D: FE 41           CP      $41                 
413F: D2 2C 40        JP      NC,$402C            ; {}
4142: C6 E0           ADD     $E0                 
4144: 2B              DEC     HL                  
4145: 22              LD      (HLI),A             
4146: 47              LD      B,A                 
4147: 3E 01           LD      A,$01               
4149: EA CE D3        LD      ($D3CE),A           
414C: 78              LD      A,B                 
414D: 77              LD      (HL),A              
414E: 47              LD      B,A                 
414F: 21 77 40        LD      HL,$4077            
4152: E6 7F           AND     $7F                 
4154: CD B7 40        CALL    $40B7               ; {}
4157: CD AE 42        CALL    $42AE               ; {}
415A: C3 47 42        JP      $4247               ; {}
415D: 01 00 FF        LD      BC,$FF00            
4160: FF              RST     0X38                
4161: 00              NOP                         
4162: 00              NOP                         
4163: 01 00 FF        LD      BC,$FF00            
4166: FF              RST     0X38                
4167: 00              NOP                         
4168: 00              NOP                         
4169: 01 00 FF        LD      BC,$FF00            
416C: FF              RST     0X38                
416D: 00              NOP                         
416E: 00              NOP                         
416F: 01 00 FF        LD      BC,$FF00            
4172: FF              RST     0X38                
4173: 00              NOP                         
4174: 00              NOP                         
4175: 01 00 FF        LD      BC,$FF00            
4178: FF              RST     0X38                
4179: 00              NOP                         
417A: 00              NOP                         
417B: 01 00 FF        LD      BC,$FF00            
417E: FF              RST     0X38                
417F: 00              NOP                         
4180: 00              NOP                         
4181: 01 00 FF        LD      BC,$FF00            
4184: FF              RST     0X38                
4185: 00              NOP                         
4186: 00              NOP                         
4187: 01 00 FF        LD      BC,$FF00            
418A: FF              RST     0X38                
418B: 00              NOP                         
418C: 00              NOP                         
418D: 01 00 FF        LD      BC,$FF00            
4190: FF              RST     0X38                
4191: 00              NOP                         
4192: 00              NOP                         
4193: 01 00 FF        LD      BC,$FF00            
4196: FF              RST     0X38                
4197: 00              NOP                         
4198: 00              NOP                         
4199: 01 00 FF        LD      BC,$FF00            
419C: FF              RST     0X38                
419D: 00              NOP                         
419E: 00              NOP                         
419F: 01 00 FF        LD      BC,$FF00            
41A2: FF              RST     0X38                
41A3: 00              NOP                         
41A4: 00              NOP                         
41A5: 01 00 FF        LD      BC,$FF00            
41A8: FF              RST     0X38                
41A9: 00              NOP                         
41AA: 00              NOP                         
41AB: 01 00 FF        LD      BC,$FF00            
41AE: FF              RST     0X38                
41AF: 00              NOP                         
41B0: 00              NOP                         
41B1: 01 00 FF        LD      BC,$FF00            
41B4: FF              RST     0X38                
41B5: 00              NOP                         
41B6: 00              NOP                         
41B7: 01 00 FF        LD      BC,$FF00            
41BA: FF              RST     0X38                
41BB: 00              NOP                         
41BC: 00              NOP                         
41BD: 01 00 FF        LD      BC,$FF00            
41C0: FF              RST     0X38                
41C1: 00              NOP                         
41C2: 00              NOP                         
41C3: 01 00 FF        LD      BC,$FF00            
41C6: FF              RST     0X38                
41C7: 00              NOP                         
41C8: 00              NOP                         
41C9: 01 00 FF        LD      BC,$FF00            
41CC: FF              RST     0X38                
41CD: 00              NOP                         
41CE: 00              NOP                         
41CF: 01 00 FF        LD      BC,$FF00            
41D2: FF              RST     0X38                
41D3: 00              NOP                         
41D4: 00              NOP                         
41D5: 01 00 FF        LD      BC,$FF00            
41D8: FF              RST     0X38                
41D9: 00              NOP                         
41DA: 00              NOP                         
41DB: 01 00 FF        LD      BC,$FF00            
41DE: FF              RST     0X38                
41DF: 00              NOP                         
41E0: 00              NOP                         
41E1: 01 00 FF        LD      BC,$FF00            
41E4: FF              RST     0X38                
41E5: 00              NOP                         
41E6: 00              NOP                         
41E7: 01 00 FF        LD      BC,$FF00            
41EA: FF              RST     0X38                
41EB: 00              NOP                         
41EC: 00              NOP                         
41ED: 01 00 FF        LD      BC,$FF00            
41F0: FF              RST     0X38                
41F1: 00              NOP                         
41F2: 00              NOP                         
41F3: 01 00 FF        LD      BC,$FF00            
41F6: FF              RST     0X38                
41F7: 00              NOP                         
41F8: 00              NOP                         
41F9: 01 00 FF        LD      BC,$FF00            
41FC: FF              RST     0X38                
41FD: 00              NOP                         
41FE: 00              NOP                         
41FF: 01 00 FF        LD      BC,$FF00            
4202: FF              RST     0X38                
4203: 00              NOP                         
4204: 00              NOP                         
4205: 01 00 FF        LD      BC,$FF00            
4208: FF              RST     0X38                
4209: 00              NOP                         
420A: 00              NOP                         
420B: 01 00 FF        LD      BC,$FF00            
420E: FF              RST     0X38                
420F: 00              NOP                         
4210: 00              NOP                         
4211: 01 00 FF        LD      BC,$FF00            
4214: FF              RST     0X38                
4215: 00              NOP                         
4216: 00              NOP                         
4217: 01 00 FF        LD      BC,$FF00            
421A: FF              RST     0X38                
421B: 00              NOP                         
421C: 00              NOP                         
421D: FA E7 D3        LD      A,($D3E7)           
4220: A7              AND     A                   
4221: CA 3D 46        JP      Z,$463D             ; {}
4224: AF              XOR     A                   
4225: E0 1A           LD      ($FF00+$1A),A       
4227: EA E7 D3        LD      ($D3E7),A           
422A: E5              PUSH    HL                  
422B: FA 36 D3        LD      A,($D336)           
422E: 6F              LD      L,A                 
422F: FA 37 D3        LD      A,($D337)           
4232: 67              LD      H,A                 
4233: C5              PUSH    BC                  
4234: 0E 30           LD      C,$30               
4236: 2A              LD      A,(HLI)             
4237: E2              LD      (C),A               
4238: 0C              INC     C                   
4239: 79              LD      A,C                 
423A: FE 40           CP      $40                 
423C: 20 F8           JR      NZ,$4236            ; {}
423E: 3E 80           LD      A,$80               
4240: E0 1A           LD      ($FF00+$1A),A       
4242: C1              POP     BC                  
4243: E1              POP     HL                  
4244: C3 3D 46        JP      $463D               ; {}
4247: FA 69 D3        LD      A,($D369)           
424A: 21 5D 41        LD      HL,$415D            
424D: 3D              DEC     A                   
424E: 28 08           JR      Z,$4258             ; {}
4250: 23              INC     HL                  
4251: 23              INC     HL                  
4252: 23              INC     HL                  
4253: 23              INC     HL                  
4254: 23              INC     HL                  
4255: 23              INC     HL                  
4256: 18 F5           JR      $424D               ; {}
4258: 01 55 D3        LD      BC,$D355            
425B: 2A              LD      A,(HLI)             
425C: 02              LD      (BC),A              
425D: 0C              INC     C                   
425E: AF              XOR     A                   
425F: 02              LD      (BC),A              
4260: 0C              INC     C                   
4261: 2A              LD      A,(HLI)             
4262: 02              LD      (BC),A              
4263: 0C              INC     C                   
4264: AF              XOR     A                   
4265: 02              LD      (BC),A              
4266: 0C              INC     C                   
4267: 2A              LD      A,(HLI)             
4268: 02              LD      (BC),A              
4269: E0 25           LD      ($FF00+$25),A       
426B: 0C              INC     C                   
426C: 2A              LD      A,(HLI)             
426D: 02              LD      (BC),A              
426E: 0C              INC     C                   
426F: 2A              LD      A,(HLI)             
4270: 02              LD      (BC),A              
4271: 0C              INC     C                   
4272: 2A              LD      A,(HLI)             
4273: 02              LD      (BC),A              
4274: C9              RET                         
4275: 21 55 D3        LD      HL,$D355            
4278: 2A              LD      A,(HLI)             
4279: FE 01           CP      $01                 
427B: C8              RET     Z                   
427C: 34              INC     (HL)                
427D: 2A              LD      A,(HLI)             
427E: BE              CP      (HL)                
427F: C0              RET     NZ                  
4280: 2D              DEC     L                   
4281: 36 00           LD      (HL),$00            
4283: 2C              INC     L                   
4284: 2C              INC     L                   
4285: 34              INC     (HL)                
4286: 2A              LD      A,(HLI)             
4287: E6 03           AND     $03                 
4289: 4D              LD      C,L                 
428A: 44              LD      B,H                 
428B: A7              AND     A                   
428C: 28 0B           JR      Z,$4299             ; {}
428E: 0C              INC     C                   
428F: FE 01           CP      $01                 
4291: 28 06           JR      Z,$4299             ; {}
4293: 0C              INC     C                   
4294: FE 02           CP      $02                 
4296: 28 01           JR      Z,$4299             ; {}
4298: 0C              INC     C                   
4299: 0A              LD      A,(BC)              
429A: E0 25           LD      ($FF00+$25),A       
429C: C9              RET                         
429D: 2A              LD      A,(HLI)             
429E: 4F              LD      C,A                 
429F: 7E              LD      A,(HL)              
42A0: 47              LD      B,A                 
42A1: 0A              LD      A,(BC)              
42A2: 12              LD      (DE),A              
42A3: 1C              INC     E                   
42A4: 03              INC     BC                  
42A5: 0A              LD      A,(BC)              
42A6: 12              LD      (DE),A              
42A7: C9              RET                         
42A8: 2A              LD      A,(HLI)             
42A9: 12              LD      (DE),A              
42AA: 1C              INC     E                   
42AB: 2A              LD      A,(HLI)             
42AC: 12              LD      (DE),A              
42AD: C9              RET                         
42AE: FA 79 D3        LD      A,($D379)           
42B1: FE 05           CP      $05                 
42B3: 28 1B           JR      Z,$42D0             ; {}
42B5: FE 0C           CP      $0C                 
42B7: 28 17           JR      Z,$42D0             ; {}
42B9: FE 1A           CP      $1A                 
42BB: 28 13           JR      Z,$42D0             ; {}
42BD: FE 24           CP      $24                 
42BF: 28 0F           JR      Z,$42D0             ; {}
42C1: FE 2A           CP      $2A                 
42C3: 28 0B           JR      Z,$42D0             ; {}
42C5: FE 2E           CP      $2E                 
42C7: 28 07           JR      Z,$42D0             ; {}
42C9: FE 3F           CP      $3F                 
42CB: 28 03           JR      Z,$42D0             ; {}
42CD: CD D3 40        CALL    $40D3               ; {}
42D0: CD C9 4D        CALL    $4DC9               ; {}
42D3: 11 00 D3        LD      DE,$D300            
42D6: 06 00           LD      B,$00               
42D8: 2A              LD      A,(HLI)             
42D9: 12              LD      (DE),A              
42DA: 1C              INC     E                   
42DB: CD A8 42        CALL    $42A8               ; {}
42DE: 11 10 D3        LD      DE,$D310            
42E1: CD A8 42        CALL    $42A8               ; {}
42E4: 11 20 D3        LD      DE,$D320            
42E7: CD A8 42        CALL    $42A8               ; {}
42EA: 11 30 D3        LD      DE,$D330            
42ED: CD A8 42        CALL    $42A8               ; {}
42F0: 11 40 D3        LD      DE,$D340            
42F3: CD A8 42        CALL    $42A8               ; {}
42F6: 21 10 D3        LD      HL,$D310            
42F9: 11 14 D3        LD      DE,$D314            
42FC: CD 9D 42        CALL    $429D               ; {}
42FF: 21 20 D3        LD      HL,$D320            
4302: 11 24 D3        LD      DE,$D324            
4305: CD 9D 42        CALL    $429D               ; {}
4308: 21 30 D3        LD      HL,$D330            
430B: 11 34 D3        LD      DE,$D334            
430E: CD 9D 42        CALL    $429D               ; {}
4311: 21 40 D3        LD      HL,$D340            
4314: 11 44 D3        LD      DE,$D344            
4317: CD 9D 42        CALL    $429D               ; {}
431A: 01 10 04        LD      BC,$0410            
431D: 21 12 D3        LD      HL,$D312            
4320: 36 01           LD      (HL),$01            
4322: 79              LD      A,C                 
4323: 85              ADD     A,L                 
4324: 6F              LD      L,A                 
4325: 05              DEC     B                   
4326: 20 F8           JR      NZ,$4320            ; {}
4328: AF              XOR     A                   
4329: EA 1E D3        LD      ($D31E),A           
432C: EA 2E D3        LD      ($D32E),A           
432F: EA 3E D3        LD      ($D33E),A           
4332: C9              RET                         
4333: E5              PUSH    HL                  
4334: 7B              LD      A,E                 
4335: EA 36 D3        LD      ($D336),A           
4338: 7A              LD      A,D                 
4339: EA 37 D3        LD      ($D337),A           
433C: FA 71 D3        LD      A,($D371)           
433F: A7              AND     A                   
4340: 20 08           JR      NZ,$434A            ; {}
4342: AF              XOR     A                   
4343: E0 1A           LD      ($FF00+$1A),A       
4345: 6B              LD      L,E                 
4346: 62              LD      H,D                 
4347: CD C6 40        CALL    $40C6               ; {}
434A: E1              POP     HL                  
434B: 18 2A           JR      $4377               ; {}
434D: CD 7D 43        CALL    $437D               ; {}
4350: CD 92 43        CALL    $4392               ; {}
4353: 5F              LD      E,A                 
4354: CD 7D 43        CALL    $437D               ; {}
4357: CD 92 43        CALL    $4392               ; {}
435A: 57              LD      D,A                 
435B: CD 7D 43        CALL    $437D               ; {}
435E: CD 92 43        CALL    $4392               ; {}
4361: 4F              LD      C,A                 
4362: 2C              INC     L                   
4363: 2C              INC     L                   
4364: 73              LD      (HL),E              
4365: 2C              INC     L                   
4366: 72              LD      (HL),D              
4367: 2C              INC     L                   
4368: 71              LD      (HL),C              
4369: 2D              DEC     L                   
436A: 2D              DEC     L                   
436B: 2D              DEC     L                   
436C: 2D              DEC     L                   
436D: E5              PUSH    HL                  
436E: 21 50 D3        LD      HL,$D350            
4371: 7E              LD      A,(HL)              
4372: E1              POP     HL                  
4373: FE 03           CP      $03                 
4375: 28 BC           JR      Z,$4333             ; {}
4377: CD 7D 43        CALL    $437D               ; {}
437A: C3 A3 44        JP      $44A3               ; {}
437D: D5              PUSH    DE                  
437E: 2A              LD      A,(HLI)             
437F: 5F              LD      E,A                 
4380: 3A              LD      A,(HLD)             
4381: 57              LD      D,A                 
4382: 13              INC     DE                  
4383: 7B              LD      A,E                 
4384: 22              LD      (HLI),A             
4385: 7A              LD      A,D                 
4386: 32              LD      (HLD),A             
4387: D1              POP     DE                  
4388: C9              RET                         
4389: D5              PUSH    DE                  
438A: 2A              LD      A,(HLI)             
438B: 5F              LD      E,A                 
438C: 3A              LD      A,(HLD)             
438D: 57              LD      D,A                 
438E: 13              INC     DE                  
438F: 13              INC     DE                  
4390: 18 F1           JR      $4383               ; {}
4392: 2A              LD      A,(HLI)             
4393: 4F              LD      C,A                 
4394: 3A              LD      A,(HLD)             
4395: 47              LD      B,A                 
4396: 0A              LD      A,(BC)              
4397: 47              LD      B,A                 
4398: C9              RET                         
4399: E1              POP     HL                  
439A: 18 31           JR      $43CD               ; {}
439C: FA 50 D3        LD      A,($D350)           
439F: FE 03           CP      $03                 
43A1: 20 10           JR      NZ,$43B3            ; {}
43A3: FA 38 D3        LD      A,($D338)           
43A6: CB 7F           BIT     1,E                 
43A8: 28 09           JR      Z,$43B3             ; {}
43AA: 7E              LD      A,(HL)              
43AB: FE 06           CP      $06                 
43AD: 20 04           JR      NZ,$43B3            ; {}
43AF: 3E 40           LD      A,$40               
43B1: E0 1C           LD      ($FF00+$1C),A       
43B3: E5              PUSH    HL                  
43B4: 7D              LD      A,L                 
43B5: C6 09           ADD     $09                 
43B7: 6F              LD      L,A                 
43B8: 7E              LD      A,(HL)              
43B9: A7              AND     A                   
43BA: 20 DD           JR      NZ,$4399            ; {}
43BC: 7D              LD      A,L                 
43BD: C6 04           ADD     $04                 
43BF: 6F              LD      L,A                 
43C0: CB 7E           BIT     1,E                 
43C2: 20 D5           JR      NZ,$4399            ; {}
43C4: E1              POP     HL                  
43C5: CD 70 46        CALL    $4670               ; {}
43C8: E5              PUSH    HL                  
43C9: CD F9 46        CALL    $46F9               ; {}
43CC: E1              POP     HL                  
43CD: 2D              DEC     L                   
43CE: 2D              DEC     L                   
43CF: C3 50 46        JP      $4650               ; {}
43D2: 2D              DEC     L                   
43D3: 2D              DEC     L                   
43D4: 2D              DEC     L                   
43D5: 2D              DEC     L                   
43D6: CD 89 43        CALL    $4389               ; {}
43D9: 7D              LD      A,L                 
43DA: C6 04           ADD     $04                 
43DC: 5F              LD      E,A                 
43DD: 54              LD      D,H                 
43DE: CD 9D 42        CALL    $429D               ; {}
43E1: FE 00           CP      $00                 
43E3: 28 1F           JR      Z,$4404             ; {}
43E5: FE FF           CP      $FF                 
43E7: 28 04           JR      Z,$43ED             ; {}
43E9: 2C              INC     L                   
43EA: C3 A1 44        JP      $44A1               ; {}
43ED: 2D              DEC     L                   
43EE: E5              PUSH    HL                  
43EF: CD 89 43        CALL    $4389               ; {}
43F2: CD 92 43        CALL    $4392               ; {}
43F5: 5F              LD      E,A                 
43F6: CD 7D 43        CALL    $437D               ; {}
43F9: CD 92 43        CALL    $4392               ; {}
43FC: 57              LD      D,A                 
43FD: E1              POP     HL                  
43FE: 7B              LD      A,E                 
43FF: 22              LD      (HLI),A             
4400: 7A              LD      A,D                 
4401: 32              LD      (HLD),A             
4402: 18 D5           JR      $43D9               ; {}
4404: FA CA D3        LD      A,($D3CA)           
4407: FE 0F           CP      $0F                 
4409: CA 57 47        JP      Z,$4757             ; {}
440C: FE 10           CP      $10                 
440E: CA 57 47        JP      Z,$4757             ; {}
4411: FE 25           CP      $25                 
4413: CA 57 47        JP      Z,$4757             ; {}
4416: 21 69 D3        LD      HL,$D369            
4419: 36 00           LD      (HL),$00            
441B: CD EF 40        CALL    $40EF               ; {}
441E: C9              RET                         
441F: CD 7D 43        CALL    $437D               ; {}
4422: CD 92 43        CALL    $4392               ; {}
4425: EA 01 D3        LD      ($D301),A           
4428: CD 7D 43        CALL    $437D               ; {}
442B: CD 92 43        CALL    $4392               ; {}
442E: EA 02 D3        LD      ($D302),A           
4431: 18 09           JR      $443C               ; {}
4433: CD 7D 43        CALL    $437D               ; {}
4436: CD 92 43        CALL    $4392               ; {}
4439: EA 00 D3        LD      ($D300),A           
443C: CD 7D 43        CALL    $437D               ; {}
443F: 18 62           JR      $44A3               ; {}
4441: CD 7D 43        CALL    $437D               ; {}
4444: CD 92 43        CALL    $4392               ; {}
4447: E5              PUSH    HL                  
4448: 7D              LD      A,L                 
4449: C6 0B           ADD     $0B                 
444B: 6F              LD      L,A                 
444C: 4E              LD      C,(HL)              
444D: 78              LD      A,B                 
444E: B1              OR      C                   
444F: 77              LD      (HL),A              
4450: 44              LD      B,H                 
4451: 4D              LD      C,L                 
4452: 0D              DEC     C                   
4453: 0D              DEC     C                   
4454: E1              POP     HL                  
4455: 2A              LD      A,(HLI)             
4456: 5F              LD      E,A                 
4457: 3A              LD      A,(HLD)             
4458: 57              LD      D,A                 
4459: 13              INC     DE                  
445A: 7B              LD      A,E                 
445B: 22              LD      (HLI),A             
445C: 7A              LD      A,D                 
445D: 32              LD      (HLD),A             
445E: 7A              LD      A,D                 
445F: 02              LD      (BC),A              
4460: 0D              DEC     C                   
4461: 7B              LD      A,E                 
4462: 02              LD      (BC),A              
4463: 18 3E           JR      $44A3               ; {}
4465: E5              PUSH    HL                  
4466: 7D              LD      A,L                 
4467: C6 0B           ADD     $0B                 
4469: 6F              LD      L,A                 
446A: 7E              LD      A,(HL)              
446B: 35              DEC     (HL)                
446C: 7E              LD      A,(HL)              
446D: E6 7F           AND     $7F                 
446F: 28 0D           JR      Z,$447E             ; {}
4471: 44              LD      B,H                 
4472: 4D              LD      C,L                 
4473: 0D              DEC     C                   
4474: 0D              DEC     C                   
4475: 0D              DEC     C                   
4476: E1              POP     HL                  
4477: 0A              LD      A,(BC)              
4478: 22              LD      (HLI),A             
4479: 0C              INC     C                   
447A: 0A              LD      A,(BC)              
447B: 32              LD      (HLD),A             
447C: 18 25           JR      $44A3               ; {}
447E: E1              POP     HL                  
447F: 18 BB           JR      $443C               ; {}
4481: 21 69 D3        LD      HL,$D369            
4484: 7E              LD      A,(HL)              
4485: A7              AND     A                   
4486: C8              RET     Z                   
4487: FA CE D3        LD      A,($D3CE)           
448A: A7              AND     A                   
448B: C8              RET     Z                   
448C: CD 75 42        CALL    $4275               ; {}
448F: 3E 01           LD      A,$01               
4491: EA 50 D3        LD      ($D350),A           
4494: 21 10 D3        LD      HL,$D310            
4497: 2C              INC     L                   
4498: 2A              LD      A,(HLI)             
4499: A7              AND     A                   
449A: CA CD 43        JP      Z,$43CD             ; {}
449D: 35              DEC     (HL)                
449E: C2 9C 43        JP      NZ,$439C            ; {}
44A1: 2C              INC     L                   
44A2: 2C              INC     L                   
44A3: CD 92 43        CALL    $4392               ; {}
44A6: FE 00           CP      $00                 
44A8: CA D2 43        JP      Z,$43D2             ; {}
44AB: FE 9D           CP      $9D                 
44AD: CA 4D 43        JP      Z,$434D             ; {}
44B0: FE 9E           CP      $9E                 
44B2: CA 1F 44        JP      Z,$441F             ; {}
44B5: FE 9F           CP      $9F                 
44B7: CA 33 44        JP      Z,$4433             ; {}
44BA: FE 9B           CP      $9B                 
44BC: CA 41 44        JP      Z,$4441             ; {}
44BF: FE 9C           CP      $9C                 
44C1: CA 65 44        JP      Z,$4465             ; {}
44C4: FE 99           CP      $99                 
44C6: CA 71 47        JP      Z,$4771             ; {}
44C9: FE 9A           CP      $9A                 
44CB: CA 7C 47        JP      Z,$477C             ; {}
44CE: FE 94           CP      $94                 
44D0: CA FF 48        JP      Z,$48FF             ; {}
44D3: FE 97           CP      $97                 
44D5: CA B8 47        JP      Z,$47B8             ; {}
44D8: FE 98           CP      $98                 
44DA: CA C7 47        JP      Z,$47C7             ; {}
44DD: FE 96           CP      $96                 
44DF: CA 63 47        JP      Z,$4763             ; {}
44E2: FE 95           CP      $95                 
44E4: CA 6E 47        JP      Z,$476E             ; {}
44E7: E6 F0           AND     $F0                 
44E9: FE A0           CP      $A0                 
44EB: 20 4D           JR      NZ,$453A            ; {}
44ED: 78              LD      A,B                 
44EE: E6 0F           AND     $0F                 
44F0: 4F              LD      C,A                 
44F1: 06 00           LD      B,$00               
44F3: E5              PUSH    HL                  
44F4: 11 01 D3        LD      DE,$D301            
44F7: 1A              LD      A,(DE)              
44F8: 6F              LD      L,A                 
44F9: 1C              INC     E                   
44FA: 1A              LD      A,(DE)              
44FB: 67              LD      H,A                 
44FC: 09              ADD     HL,BC               
44FD: 7E              LD      A,(HL)              
44FE: E1              POP     HL                  
44FF: E5              PUSH    HL                  
4500: 57              LD      D,A                 
4501: 2C              INC     L                   
4502: 2C              INC     L                   
4503: 2C              INC     L                   
4504: 7E              LD      A,(HL)              
4505: E6 F0           AND     $F0                 
4507: 20 03           JR      NZ,$450C            ; {}
4509: 7A              LD      A,D                 
450A: 18 25           JR      $4531               ; {}
450C: 5F              LD      E,A                 
450D: 7A              LD      A,D                 
450E: F5              PUSH    AF                  
450F: CB 3F           SRL     1,E                 
4511: CB 23           SLA     1,E                 
4513: 38 08           JR      C,$451D             ; {}
4515: 57              LD      D,A                 
4516: CB 3F           SRL     1,E                 
4518: CB 23           SLA     1,E                 
451A: 38 01           JR      C,$451D             ; {}
451C: 82              ADD     A,D                 
451D: 4F              LD      C,A                 
451E: A7              AND     A                   
451F: 20 02           JR      NZ,$4523            ; {}
4521: 0E 02           LD      C,$02               
4523: 11 50 D3        LD      DE,$D350            
4526: 1A              LD      A,(DE)              
4527: 3D              DEC     A                   
4528: 5F              LD      E,A                 
4529: 16 00           LD      D,$00               
452B: 21 07 D3        LD      HL,$D307            
452E: 19              ADD     HL,DE               
452F: 71              LD      (HL),C              
4530: F1              POP     AF                  
4531: E1              POP     HL                  
4532: 2D              DEC     L                   
4533: 22              LD      (HLI),A             
4534: CD 7D 43        CALL    $437D               ; {}
4537: CD 92 43        CALL    $4392               ; {}
453A: FA 50 D3        LD      A,($D350)           
453D: FE 04           CP      $04                 
453F: 28 38           JR      Z,$4579             ; {}
4541: D5              PUSH    DE                  
4542: 11 B0 D3        LD      DE,$D3B0            
4545: CD 07 48        CALL    $4807               ; {}
4548: AF              XOR     A                   
4549: 12              LD      (DE),A              
454A: 1C              INC     E                   
454B: 12              LD      (DE),A              
454C: 11 B6 D3        LD      DE,$D3B6            
454F: CD 07 48        CALL    $4807               ; {}
4552: 1C              INC     E                   
4553: AF              XOR     A                   
4554: 12              LD      (DE),A              
4555: FA 50 D3        LD      A,($D350)           
4558: FE 03           CP      $03                 
455A: 20 1C           JR      NZ,$4578            ; {}
455C: 11 9E D3        LD      DE,$D39E            
455F: 1A              LD      A,(DE)              
4560: A7              AND     A                   
4561: 28 07           JR      Z,$456A             ; {}
4563: 3E 01           LD      A,$01               
4565: 12              LD      (DE),A              
4566: AF              XOR     A                   
4567: EA 9F D3        LD      ($D39F),A           
456A: 11 D9 D3        LD      DE,$D3D9            
456D: 1A              LD      A,(DE)              
456E: A7              AND     A                   
456F: 28 07           JR      Z,$4578             ; {}
4571: 3E 01           LD      A,$01               
4573: 12              LD      (DE),A              
4574: AF              XOR     A                   
4575: EA DA D3        LD      ($D3DA),A           
4578: D1              POP     DE                  
4579: 48              LD      C,B                 
457A: 06 00           LD      B,$00               
457C: CD 7D 43        CALL    $437D               ; {}
457F: FA 50 D3        LD      A,($D350)           
4582: FE 04           CP      $04                 
4584: CA BB 45        JP      Z,$45BB             ; {}
4587: E5              PUSH    HL                  
4588: 7D              LD      A,L                 
4589: C6 05           ADD     $05                 
458B: 6F              LD      L,A                 
458C: 5D              LD      E,L                 
458D: 54              LD      D,H                 
458E: 2C              INC     L                   
458F: 2C              INC     L                   
4590: 79              LD      A,C                 
4591: FE 01           CP      $01                 
4593: 28 21           JR      Z,$45B6             ; {}
4595: 36 00           LD      (HL),$00            
4597: FA 00 D3        LD      A,($D300)           
459A: A7              AND     A                   
459B: 28 0C           JR      Z,$45A9             ; {}
459D: 6F              LD      L,A                 
459E: 26 00           LD      H,$00               
45A0: CB 7D           BIT     1,E                 
45A2: 28 02           JR      Z,$45A6             ; {}
45A4: 26 FF           LD      H,$FF               
45A6: 09              ADD     HL,BC               
45A7: 44              LD      B,H                 
45A8: 4D              LD      C,L                 
45A9: 21 34 49        LD      HL,$4934            
45AC: 09              ADD     HL,BC               
45AD: 2A              LD      A,(HLI)             
45AE: 12              LD      (DE),A              
45AF: 1C              INC     E                   
45B0: 7E              LD      A,(HL)              
45B1: 12              LD      (DE),A              
45B2: E1              POP     HL                  
45B3: C3 EC 45        JP      $45EC               ; {}
45B6: 36 01           LD      (HL),$01            
45B8: E1              POP     HL                  
45B9: 18 31           JR      $45EC               ; {}
45BB: E5              PUSH    HL                  
45BC: 79              LD      A,C                 
45BD: FE FF           CP      $FF                 
45BF: 28 18           JR      Z,$45D9             ; {}
45C1: 11 46 D3        LD      DE,$D346            
45C4: 21 C6 49        LD      HL,$49C6            
45C7: 09              ADD     HL,BC               
45C8: 2A              LD      A,(HLI)             
45C9: 12              LD      (DE),A              
45CA: 1C              INC     E                   
45CB: 7B              LD      A,E                 
45CC: FE 4B           CP      $4B                 
45CE: 20 F8           JR      NZ,$45C8            ; {}
45D0: 0E 20           LD      C,$20               
45D2: 21 44 D3        LD      HL,$D344            
45D5: 06 00           LD      B,$00               
45D7: 18 41           JR      $461A               ; {}
45D9: FA 4F D3        LD      A,($D34F)           
45DC: CB 7F           BIT     1,E                 
45DE: C2 4B 46        JP      NZ,$464B            ; {}
45E1: 3E 01           LD      A,$01               
45E3: EA 78 D3        LD      ($D378),A           
45E6: CD 37 40        CALL    $4037               ; {}
45E9: C3 4B 46        JP      $464B               ; {}
45EC: E5              PUSH    HL                  
45ED: 06 00           LD      B,$00               
45EF: FA 50 D3        LD      A,($D350)           
45F2: FE 01           CP      $01                 
45F4: 28 21           JR      Z,$4617             ; {}
45F6: FE 02           CP      $02                 
45F8: 28 19           JR      Z,$4613             ; {}
45FA: 0E 1A           LD      C,$1A               
45FC: FA 3F D3        LD      A,($D33F)           
45FF: CB 7F           BIT     1,E                 
4601: 20 05           JR      NZ,$4608            ; {}
4603: AF              XOR     A                   
4604: E2              LD      (C),A               
4605: 3E 80           LD      A,$80               
4607: E2              LD      (C),A               
4608: 0C              INC     C                   
4609: 2C              INC     L                   
460A: 2C              INC     L                   
460B: 2C              INC     L                   
460C: 2C              INC     L                   
460D: 2A              LD      A,(HLI)             
460E: 5F              LD      E,A                 
460F: 16 00           LD      D,$00               
4611: 18 0E           JR      $4621               ; {}
4613: 0E 16           LD      C,$16               
4615: 18 03           JR      $461A               ; {}
4617: 0E 10           LD      C,$10               
4619: 0C              INC     C                   
461A: 2C              INC     L                   
461B: 2C              INC     L                   
461C: 2A              LD      A,(HLI)             
461D: 5F              LD      E,A                 
461E: 2C              INC     L                   
461F: 2A              LD      A,(HLI)             
4620: 57              LD      D,A                 
4621: E5              PUSH    HL                  
4622: 2C              INC     L                   
4623: 2C              INC     L                   
4624: 2A              LD      A,(HLI)             
4625: A7              AND     A                   
4626: 28 02           JR      Z,$462A             ; {}
4628: 1E 08           LD      E,$08               
462A: 2C              INC     L                   
462B: 2C              INC     L                   
462C: 36 00           LD      (HL),$00            
462E: 2C              INC     L                   
462F: 7E              LD      A,(HL)              
4630: E1              POP     HL                  
4631: CB 7F           BIT     1,E                 
4633: 20 16           JR      NZ,$464B            ; {}
4635: FA 50 D3        LD      A,($D350)           
4638: FE 03           CP      $03                 
463A: CA 1D 42        JP      Z,$421D             ; {}
463D: 7A              LD      A,D                 
463E: B0              OR      B                   
463F: E2              LD      (C),A               
4640: 0C              INC     C                   
4641: 7B              LD      A,E                 
4642: E2              LD      (C),A               
4643: 0C              INC     C                   
4644: 2A              LD      A,(HLI)             
4645: E2              LD      (C),A               
4646: 0C              INC     C                   
4647: 7E              LD      A,(HL)              
4648: F6 80           OR      $80                 
464A: E2              LD      (C),A               
464B: E1              POP     HL                  
464C: 2D              DEC     L                   
464D: 3A              LD      A,(HLD)             
464E: 32              LD      (HLD),A             
464F: 2D              DEC     L                   
4650: 11 50 D3        LD      DE,$D350            
4653: 1A              LD      A,(DE)              
4654: FE 04           CP      $04                 
4656: 28 09           JR      Z,$4661             ; {}
4658: 3C              INC     A                   
4659: 12              LD      (DE),A              
465A: 3E 10           LD      A,$10               
465C: 85              ADD     A,L                 
465D: 6F              LD      L,A                 
465E: C3 97 44        JP      $4497               ; {}
4661: 21 1E D3        LD      HL,$D31E            
4664: 34              INC     (HL)                
4665: 21 2E D3        LD      HL,$D32E            
4668: 34              INC     (HL)                
4669: 21 3E D3        LD      HL,$D33E            
466C: 34              INC     (HL)                
466D: C9              RET                         
466E: E1              POP     HL                  
466F: C9              RET                         
4670: E5              PUSH    HL                  
4671: 7D              LD      A,L                 
4672: C6 06           ADD     $06                 
4674: 6F              LD      L,A                 
4675: 7E              LD      A,(HL)              
4676: E6 0F           AND     $0F                 
4678: 28 18           JR      Z,$4692             ; {}
467A: EA 51 D3        LD      ($D351),A           
467D: FA 50 D3        LD      A,($D350)           
4680: 0E 13           LD      C,$13               
4682: FE 01           CP      $01                 
4684: 28 4E           JR      Z,$46D4             ; {}
4686: 0E 18           LD      C,$18               
4688: FE 02           CP      $02                 
468A: 28 48           JR      Z,$46D4             ; {}
468C: 0E 1D           LD      C,$1D               
468E: FE 03           CP      $03                 
4690: 28 42           JR      Z,$46D4             ; {}
4692: FA 50 D3        LD      A,($D350)           
4695: FE 04           CP      $04                 
4697: CA 6E 46        JP      Z,$466E             ; {}
469A: 11 B6 D3        LD      DE,$D3B6            
469D: CD 07 48        CALL    $4807               ; {}
46A0: 1A              LD      A,(DE)              
46A1: A7              AND     A                   
46A2: CA BB 46        JP      Z,$46BB             ; {}
46A5: FA 50 D3        LD      A,($D350)           
46A8: 0E 13           LD      C,$13               
46AA: FE 01           CP      $01                 
46AC: CA D0 47        JP      Z,$47D0             ; {}
46AF: 0E 18           LD      C,$18               
46B1: FE 02           CP      $02                 
46B3: CA D0 47        JP      Z,$47D0             ; {}
46B6: 0E 1D           LD      C,$1D               
46B8: C3 D0 47        JP      $47D0               ; {}
46BB: FA 50 D3        LD      A,($D350)           
46BE: FE 03           CP      $03                 
46C0: C2 6E 46        JP      NZ,$466E            ; {}
46C3: FA 9E D3        LD      A,($D39E)           
46C6: A7              AND     A                   
46C7: C2 82 47        JP      NZ,$4782            ; {}
46CA: FA D9 D3        LD      A,($D3D9)           
46CD: A7              AND     A                   
46CE: C2 0A 49        JP      NZ,$490A            ; {}
46D1: C3 6E 46        JP      $466E               ; {}
46D4: 2C              INC     L                   
46D5: 2A              LD      A,(HLI)             
46D6: 5F              LD      E,A                 
46D7: 7E              LD      A,(HL)              
46D8: E6 0F           AND     $0F                 
46DA: 57              LD      D,A                 
46DB: D5              PUSH    DE                  
46DC: 7D              LD      A,L                 
46DD: C6 04           ADD     $04                 
46DF: 6F              LD      L,A                 
46E0: 46              LD      B,(HL)              
46E1: FA 51 D3        LD      A,($D351)           
46E4: FE 01           CP      $01                 
46E6: CA 1D 48        JP      Z,$481D             ; {}
46E9: FE 05           CP      $05                 
46EB: CA 8A 48        JP      Z,$488A             ; {}
46EE: 21 FF FF        LD      HL,$FFFF            
46F1: D1              POP     DE                  
46F2: 19              ADD     HL,DE               
46F3: CD F6 47        CALL    $47F6               ; {}
46F6: C3 92 46        JP      $4692               ; {}
46F9: FA 1B D3        LD      A,($D31B)           
46FC: A7              AND     A                   
46FD: 20 21           JR      NZ,$4720            ; {}
46FF: FA 17 D3        LD      A,($D317)           
4702: A7              AND     A                   
4703: 28 1B           JR      Z,$4720             ; {}
4705: E6 0F           AND     $0F                 
4707: 47              LD      B,A                 
4708: 21 07 D3        LD      HL,$D307            
470B: FA 1E D3        LD      A,($D31E)           
470E: BE              CP      (HL)                
470F: 20 0F           JR      NZ,$4720            ; {}
4711: 0E 12           LD      C,$12               
4713: 11 1A D3        LD      DE,$D31A            
4716: FA 1F D3        LD      A,($D31F)           
4719: CB 7F           BIT     1,E                 
471B: 20 03           JR      NZ,$4720            ; {}
471D: CD 44 47        CALL    $4744               ; {}
4720: FA 2B D3        LD      A,($D32B)           
4723: A7              AND     A                   
4724: C0              RET     NZ                  
4725: FA 27 D3        LD      A,($D327)           
4728: A7              AND     A                   
4729: C8              RET     Z                   
472A: E6 0F           AND     $0F                 
472C: 47              LD      B,A                 
472D: 21 08 D3        LD      HL,$D308            
4730: FA 2E D3        LD      A,($D32E)           
4733: BE              CP      (HL)                
4734: C0              RET     NZ                  
4735: FA 2F D3        LD      A,($D32F)           
4738: CB 7F           BIT     1,E                 
473A: C0              RET     NZ                  
473B: 0E 17           LD      C,$17               
473D: 11 2A D3        LD      DE,$D32A            
4740: CD 44 47        CALL    $4744               ; {}
4743: C9              RET                         
4744: C5              PUSH    BC                  
4745: 05              DEC     B                   
4746: 48              LD      C,B                 
4747: 06 00           LD      B,$00               
4749: 21 85 4A        LD      HL,$4A85            
474C: 09              ADD     HL,BC               
474D: 7E              LD      A,(HL)              
474E: C1              POP     BC                  
474F: E2              LD      (C),A               
4750: 0C              INC     C                   
4751: 0C              INC     C                   
4752: 1A              LD      A,(DE)              
4753: F6 80           OR      $80                 
4755: E2              LD      (C),A               
4756: C9              RET                         
4757: AF              XOR     A                   
4758: EA CE D3        LD      ($D3CE),A           
475B: F0 BF           LD      A,($BF)             
475D: EA 68 D3        LD      ($D368),A           
4760: C3 1E 40        JP      $401E               ; {}
4763: 3E 01           LD      A,$01               
4765: EA CD D3        LD      ($D3CD),A           
4768: CD 7D 43        CALL    $437D               ; {}
476B: C3 A3 44        JP      $44A3               ; {}
476E: AF              XOR     A                   
476F: 18 F4           JR      $4765               ; {}
4771: 3E 01           LD      A,$01               
4773: EA 9E D3        LD      ($D39E),A           
4776: CD 7D 43        CALL    $437D               ; {}
4779: C3 A3 44        JP      $44A3               ; {}
477C: AF              XOR     A                   
477D: EA 9E D3        LD      ($D39E),A           
4780: 18 F1           JR      $4773               ; {}
4782: FE 02           CP      $02                 
4784: CA 6E 46        JP      Z,$466E             ; {}
4787: 01 9F D3        LD      BC,$D39F            
478A: CD B4 47        CALL    $47B4               ; {}
478D: 0E 1C           LD      C,$1C               
478F: 06 40           LD      B,$40               
4791: FE 03           CP      $03                 
4793: 28 1A           JR      Z,$47AF             ; {}
4795: 06 60           LD      B,$60               
4797: FE 05           CP      $05                 
4799: 28 14           JR      Z,$47AF             ; {}
479B: FE 0A           CP      $0A                 
479D: 28 10           JR      Z,$47AF             ; {}
479F: 06 00           LD      B,$00               
47A1: FE 07           CP      $07                 
47A3: 28 0A           JR      Z,$47AF             ; {}
47A5: FE 0D           CP      $0D                 
47A7: C2 6E 46        JP      NZ,$466E            ; {}
47AA: 3E 02           LD      A,$02               
47AC: EA 9E D3        LD      ($D39E),A           
47AF: 78              LD      A,B                 
47B0: E2              LD      (C),A               
47B1: C3 6E 46        JP      $466E               ; {}
47B4: 0A              LD      A,(BC)              
47B5: 3C              INC     A                   
47B6: 02              LD      (BC),A              
47B7: C9              RET                         
47B8: 11 B6 D3        LD      DE,$D3B6            
47BB: CD 07 48        CALL    $4807               ; {}
47BE: 3E 01           LD      A,$01               
47C0: 12              LD      (DE),A              
47C1: CD 7D 43        CALL    $437D               ; {}
47C4: C3 A3 44        JP      $44A3               ; {}
47C7: 11 B6 D3        LD      DE,$D3B6            
47CA: CD 07 48        CALL    $4807               ; {}
47CD: AF              XOR     A                   
47CE: 18 F0           JR      $47C0               ; {}
47D0: 1C              INC     E                   
47D1: 1A              LD      A,(DE)              
47D2: A7              AND     A                   
47D3: 20 11           JR      NZ,$47E6            ; {}
47D5: 3C              INC     A                   
47D6: 12              LD      (DE),A              
47D7: E1              POP     HL                  
47D8: E5              PUSH    HL                  
47D9: CD EB 47        CALL    $47EB               ; {}
47DC: 21 9C FF        LD      HL,$FF9C            
47DF: 19              ADD     HL,DE               
47E0: CD F6 47        CALL    $47F6               ; {}
47E3: C3 6E 46        JP      $466E               ; {}
47E6: CD 10 48        CALL    $4810               ; {}
47E9: 18 F1           JR      $47DC               ; {}
47EB: 3E 07           LD      A,$07               
47ED: 85              ADD     A,L                 
47EE: 6F              LD      L,A                 
47EF: 2A              LD      A,(HLI)             
47F0: 5F              LD      E,A                 
47F1: 7E              LD      A,(HL)              
47F2: E6 0F           AND     $0F                 
47F4: 57              LD      D,A                 
47F5: C9              RET                         
47F6: 11 A4 D3        LD      DE,$D3A4            
47F9: CD 07 48        CALL    $4807               ; {}
47FC: 7D              LD      A,L                 
47FD: E2              LD      (C),A               
47FE: 12              LD      (DE),A              
47FF: 0C              INC     C                   
4800: 1C              INC     E                   
4801: 7C              LD      A,H                 
4802: E6 0F           AND     $0F                 
4804: E2              LD      (C),A               
4805: 12              LD      (DE),A              
4806: C9              RET                         
4807: FA 50 D3        LD      A,($D350)           
480A: 3D              DEC     A                   
480B: CB 27           SLA     1,E                 
480D: 83              ADD     A,E                 
480E: 5F              LD      E,A                 
480F: C9              RET                         
4810: 11 A4 D3        LD      DE,$D3A4            
4813: CD 07 48        CALL    $4807               ; {}
4816: 1A              LD      A,(DE)              
4817: 6F              LD      L,A                 
4818: 1C              INC     E                   
4819: 1A              LD      A,(DE)              
481A: 57              LD      D,A                 
481B: 5D              LD      E,L                 
481C: C9              RET                         
481D: D1              POP     DE                  
481E: 11 B0 D3        LD      DE,$D3B0            
4821: CD 07 48        CALL    $4807               ; {}
4824: 1A              LD      A,(DE)              
4825: 3C              INC     A                   
4826: 12              LD      (DE),A              
4827: 1C              INC     E                   
4828: FE 19           CP      $19                 
482A: 28 31           JR      Z,$485D             ; {}
482C: FE 2D           CP      $2D                 
482E: 28 26           JR      Z,$4856             ; {}
4830: 1A              LD      A,(DE)              
4831: A7              AND     A                   
4832: CA 92 46        JP      Z,$4692             ; {}
4835: 1D              DEC     E                   
4836: 1A              LD      A,(DE)              
4837: D6 19           SUB     $19                 
4839: CB 27           SLA     1,E                 
483B: 6F              LD      L,A                 
483C: 26 00           LD      H,$00               
483E: 11 62 48        LD      DE,$4862            
4841: 19              ADD     HL,DE               
4842: 2A              LD      A,(HLI)             
4843: 57              LD      D,A                 
4844: 7E              LD      A,(HL)              
4845: 5F              LD      E,A                 
4846: E1              POP     HL                  
4847: E5              PUSH    HL                  
4848: D5              PUSH    DE                  
4849: CD EB 47        CALL    $47EB               ; {}
484C: 62              LD      H,D                 
484D: 6B              LD      L,E                 
484E: D1              POP     DE                  
484F: 19              ADD     HL,DE               
4850: CD F6 47        CALL    $47F6               ; {}
4853: C3 92 46        JP      $4692               ; {}
4856: 1D              DEC     E                   
4857: 3E 19           LD      A,$19               
4859: 12              LD      (DE),A              
485A: 1C              INC     E                   
485B: 18 D8           JR      $4835               ; {}
485D: 3E 01           LD      A,$01               
485F: 12              LD      (DE),A              
4860: 18 D3           JR      $4835               ; {}
4862: 00              NOP                         
4863: 00              NOP                         
4864: 00              NOP                         
4865: 00              NOP                         
4866: 00              NOP                         
4867: 01 00 01        LD      BC,$0100            
486A: 00              NOP                         
486B: 02              LD      (BC),A              
486C: 00              NOP                         
486D: 02              LD      (BC),A              
486E: 00              NOP                         
486F: 00              NOP                         
4870: 00              NOP                         
4871: 00              NOP                         
4872: FF              RST     0X38                
4873: FF              RST     0X38                
4874: FF              RST     0X38                
4875: FF              RST     0X38                
4876: FF              RST     0X38                
4877: FE FF           CP      $FF                 
4879: FE 00           CP      $00                 
487B: 00              NOP                         
487C: 00              NOP                         
487D: 01 00 02        LD      BC,$0200            
4880: 00              NOP                         
4881: 01 00 00        LD      BC,$0000            
4884: FF              RST     0X38                
4885: FF              RST     0X38                
4886: FF              RST     0X38                
4887: FE FF           CP      $FF                 
4889: FF              RST     0X38                
488A: D1              POP     DE                  
488B: 11 D0 D3        LD      DE,$D3D0            
488E: CD 07 48        CALL    $4807               ; {}
4891: 1A              LD      A,(DE)              
4892: 3C              INC     A                   
4893: 12              LD      (DE),A              
4894: 1C              INC     E                   
4895: FE 21           CP      $21                 
4897: 28 1F           JR      Z,$48B8             ; {}
4899: 1D              DEC     E                   
489A: 1A              LD      A,(DE)              
489B: CB 27           SLA     1,E                 
489D: 6F              LD      L,A                 
489E: 26 00           LD      H,$00               
48A0: 11 BF 48        LD      DE,$48BF            
48A3: 19              ADD     HL,DE               
48A4: 2A              LD      A,(HLI)             
48A5: 57              LD      D,A                 
48A6: 7E              LD      A,(HL)              
48A7: 5F              LD      E,A                 
48A8: E1              POP     HL                  
48A9: E5              PUSH    HL                  
48AA: D5              PUSH    DE                  
48AB: CD EB 47        CALL    $47EB               ; {}
48AE: 62              LD      H,D                 
48AF: 6B              LD      L,E                 
48B0: D1              POP     DE                  
48B1: 19              ADD     HL,DE               
48B2: CD F6 47        CALL    $47F6               ; {}
48B5: C3 92 46        JP      $4692               ; {}
48B8: 1D              DEC     E                   
48B9: 3E 01           LD      A,$01               
48BB: 12              LD      (DE),A              
48BC: 1C              INC     E                   
48BD: 18 DA           JR      $4899               ; {}
48BF: 00              NOP                         
48C0: 08 00 00        LD      ($0000),SP          
48C3: FF              RST     0X38                
48C4: F8 00           LD      HL,SP+$00           
48C6: 00              NOP                         
48C7: 00              NOP                         
48C8: 0A              LD      A,(BC)              
48C9: 00              NOP                         
48CA: 02              LD      (BC),A              
48CB: FF              RST     0X38                
48CC: FA 00 02        LD      A,($0200)           
48CF: 00              NOP                         
48D0: 0C              INC     C                   
48D1: 00              NOP                         
48D2: 04              INC     B                   
48D3: FF              RST     0X38                
48D4: FC                              
48D5: 00              NOP                         
48D6: 04              INC     B                   
48D7: 00              NOP                         
48D8: 0A              LD      A,(BC)              
48D9: 00              NOP                         
48DA: 02              LD      (BC),A              
48DB: FF              RST     0X38                
48DC: FA 00 02        LD      A,($0200)           
48DF: 00              NOP                         
48E0: 08 00 00        LD      ($0000),SP          
48E3: FF              RST     0X38                
48E4: F8 00           LD      HL,SP+$00           
48E6: 00              NOP                         
48E7: 00              NOP                         
48E8: 06 FF           LD      B,$FF               
48EA: FE FF           CP      $FF                 
48EC: F6 FF           OR      $FF                 
48EE: FE 00           CP      $00                 
48F0: 04              INC     B                   
48F1: FF              RST     0X38                
48F2: FC                              
48F3: FF              RST     0X38                
48F4: F4                              
48F5: FF              RST     0X38                
48F6: FC                              
48F7: 00              NOP                         
48F8: 06 FF           LD      B,$FF               
48FA: FE FF           CP      $FF                 
48FC: F6 FF           OR      $FF                 
48FE: FE 3E           CP      $3E                 
4900: 01 EA D9        LD      BC,$D9EA            
4903: D3                              
4904: CD 7D 43        CALL    $437D               ; {}
4907: C3 A3 44        JP      $44A3               ; {}
490A: FE 02           CP      $02                 
490C: CA 6E 46        JP      Z,$466E             ; {}
490F: 01 DA D3        LD      BC,$D3DA            
4912: CD B4 47        CALL    $47B4               ; {}
4915: 0E 1C           LD      C,$1C               
4917: 06 60           LD      B,$60               
4919: FE 03           CP      $03                 
491B: CA AF 47        JP      Z,$47AF             ; {}
491E: 06 40           LD      B,$40               
4920: FE 05           CP      $05                 
4922: CA AF 47        JP      Z,$47AF             ; {}
4925: 06 20           LD      B,$20               
4927: FE 06           CP      $06                 
4929: C2 6E 46        JP      NZ,$466E            ; {}
492C: 3E 02           LD      A,$02               
492E: EA D9 D3        LD      ($D3D9),A           
4931: C3 AF 47        JP      $47AF               ; {}
4934: 00              NOP                         
4935: 0F              RRCA                        
4936: 2C              INC     L                   
4937: 00              NOP                         
4938: 9C              SBC     H                   
4939: 00              NOP                         
493A: 06 01           LD      B,$01               
493C: 6B              LD      L,E                 
493D: 01 C9 01        LD      BC,$01C9            
4940: 23              INC     HL                  
4941: 02              LD      (BC),A              
4942: 77              LD      (HL),A              
4943: 02              LD      (BC),A              
4944: C6 02           ADD     $02                 
4946: 12              LD      (DE),A              
4947: 03              INC     BC                  
4948: 56              LD      D,(HL)              
4949: 03              INC     BC                  
494A: 9B              SBC     E                   
494B: 03              INC     BC                  
494C: DA 03 16        JP      C,$1603             
494F: 04              INC     B                   
4950: 4E              LD      C,(HL)              
4951: 04              INC     B                   
4952: 83              ADD     A,E                 
4953: 04              INC     B                   
4954: B5              OR      L                   
4955: 04              INC     B                   
4956: E5              PUSH    HL                  
4957: 04              INC     B                   
4958: 11 05 3B        LD      DE,$3B05            
495B: 05              DEC     B                   
495C: 63              LD      H,E                 
495D: 05              DEC     B                   
495E: 89              ADC     A,C                 
495F: 05              DEC     B                   
4960: AC              XOR     H                   
4961: 05              DEC     B                   
4962: CE 05           ADC     $05                 
4964: ED                              
4965: 05              DEC     B                   
4966: 0A              LD      A,(BC)              
4967: 06 27           LD      B,$27               
4969: 06 42           LD      B,$42               
496B: 06 5B           LD      B,$5B               
496D: 06 72           LD      B,$72               
496F: 06 89           LD      B,$89               
4971: 06 9E           LD      B,$9E               
4973: 06 B2           LD      B,$B2               
4975: 06 C4           LD      B,$C4               
4977: 06 D6           LD      B,$D6               
4979: 06 E7           LD      B,$E7               
497B: 06 F7           LD      B,$F7               
497D: 06 06           LD      B,$06               
497F: 07              RLCA                        
4980: 14              INC     D                   
4981: 07              RLCA                        
4982: 21 07 2D        LD      HL,$2D07            
4985: 07              RLCA                        
4986: 39              ADD     HL,SP               
4987: 07              RLCA                        
4988: 44              LD      B,H                 
4989: 07              RLCA                        
498A: 4F              LD      C,A                 
498B: 07              RLCA                        
498C: 59              LD      E,C                 
498D: 07              RLCA                        
498E: 62              LD      H,D                 
498F: 07              RLCA                        
4990: 6B              LD      L,E                 
4991: 07              RLCA                        
4992: 74              LD      (HL),H              
4993: 07              RLCA                        
4994: 7B              LD      A,E                 
4995: 07              RLCA                        
4996: 83              ADD     A,E                 
4997: 07              RLCA                        
4998: 8A              ADC     A,D                 
4999: 07              RLCA                        
499A: 90              SUB     B                   
499B: 07              RLCA                        
499C: 97              SUB     A                   
499D: 07              RLCA                        
499E: 9D              SBC     L                   
499F: 07              RLCA                        
49A0: A2              AND     D                   
49A1: 07              RLCA                        
49A2: A7              AND     A                   
49A3: 07              RLCA                        
49A4: AC              XOR     H                   
49A5: 07              RLCA                        
49A6: B1              OR      C                   
49A7: 07              RLCA                        
49A8: B6              OR      (HL)                
49A9: 07              RLCA                        
49AA: BA              CP      D                   
49AB: 07              RLCA                        
49AC: BE              CP      (HL)                
49AD: 07              RLCA                        
49AE: C1              POP     BC                  
49AF: 07              RLCA                        
49B0: C5              PUSH    BC                  
49B1: 07              RLCA                        
49B2: C8              RET     Z                   
49B3: 07              RLCA                        
49B4: CB 07           RLC     1,E                 
49B6: CE 07           ADC     $07                 
49B8: D1              POP     DE                  
49B9: 07              RLCA                        
49BA: D4 07 D6        CALL    NC,$D607            
49BD: 07              RLCA                        
49BE: D9              RETI                        
49BF: 07              RLCA                        
49C0: DB                              
49C1: 07              RLCA                        
49C2: DD                              
49C3: 07              RLCA                        
49C4: DF              RST     0X18                
49C5: 07              RLCA                        
49C6: 00              NOP                         
49C7: 00              NOP                         
49C8: 00              NOP                         
49C9: 00              NOP                         
49CA: 00              NOP                         
49CB: C0              RET     NZ                  
49CC: 09              ADD     HL,BC               
49CD: 00              NOP                         
49CE: 38 34           JR      C,$4A04             ; {}
49D0: C0              RET     NZ                  
49D1: 19              ADD     HL,DE               
49D2: 00              NOP                         
49D3: 38 33           JR      C,$4A08             ; {}
49D5: C0              RET     NZ                  
49D6: 46              LD      B,(HL)              
49D7: 00              NOP                         
49D8: 13              INC     DE                  
49D9: 10 C0           ;;STOP    $C0                 
49DB: 23              INC     HL                  
49DC: 00              NOP                         
49DD: 20 40           JR      NZ,$4A1F            ; {}
49DF: 80              ADD     A,B                 
49E0: 51              LD      D,C                 
49E1: 00              NOP                         
49E2: 20 07           JR      NZ,$49EB            ; {}
49E4: 80              ADD     A,B                 
49E5: A1              AND     C                   
49E6: 00              NOP                         
49E7: 00              NOP                         
49E8: 18 80           JR      $496A               ; {}
49EA: F2                              
49EB: 00              NOP                         
49EC: 00              NOP                         
49ED: 18 80           JR      $496F               ; {}
49EF: 81              ADD     A,C                 
49F0: 00              NOP                         
49F1: 3A              LD      A,(HLD)             
49F2: 10 C0           ;;STOP    $C0                 
49F4: 80              ADD     A,B                 
49F5: 00              NOP                         
49F6: 00              NOP                         
49F7: 10 C0           ;;STOP    $C0                 
49F9: 57              LD      D,A                 
49FA: 00              NOP                         
49FB: 00              NOP                         
49FC: 60              LD      H,B                 
49FD: 80              ADD     A,B                 
49FE: 01 02 04        LD      BC,$0402            
4A01: 08 10 20        LD      ($2010),SP          
4A04: 06 0C           LD      B,$0C               
4A06: 18 01           JR      $4A09               ; {}
4A08: 01 01 01        LD      BC,$0101            
4A0B: 01 30 01        LD      BC,$0130            
4A0E: 03              INC     BC                  
4A0F: 06 0C           LD      B,$0C               
4A11: 18 30           JR      $4A43               ; {}
4A13: 09              ADD     HL,BC               
4A14: 12              LD      (DE),A              
4A15: 24              INC     H                   
4A16: 02              LD      (BC),A              
4A17: 04              INC     B                   
4A18: 08 01 01        LD      ($0101),SP          
4A1B: 48              LD      C,B                 
4A1C: 02              LD      (BC),A              
4A1D: 04              INC     B                   
4A1E: 08 10 20        LD      ($2010),SP          
4A21: 40              LD      B,B                 
4A22: 0C              INC     C                   
4A23: 18 30           JR      $4A55               ; {}
4A25: 02              LD      (BC),A              
4A26: 05              DEC     B                   
4A27: 03              INC     BC                  
4A28: 01 01 60        LD      BC,$6001            
4A2B: 03              INC     BC                  
4A2C: 05              DEC     B                   
4A2D: 0A              LD      A,(BC)              
4A2E: 14              INC     D                   
4A2F: 28 50           JR      Z,$4A81             ; {}
4A31: 0F              RRCA                        
4A32: 1E 3C           LD      E,$3C               
4A34: 02              LD      (BC),A              
4A35: 08 10 02        LD      ($0210),SP          
4A38: 01 78 03        LD      BC,$0378            
4A3B: 06 0C           LD      B,$0C               
4A3D: 18 30           JR      $4A6F               ; {}
4A3F: 60              LD      H,B                 
4A40: 12              LD      (DE),A              
4A41: 24              INC     H                   
4A42: 48              LD      C,B                 
4A43: 03              INC     BC                  
4A44: 08 10 02        LD      ($0210),SP          
4A47: 04              INC     B                   
4A48: 90              SUB     B                   
4A49: 03              INC     BC                  
4A4A: 07              RLCA                        
4A4B: 0E 1C           LD      C,$1C               
4A4D: 38 70           JR      C,$4ABF             ; {}
4A4F: 15              DEC     D                   
4A50: 2A              LD      A,(HLI)             
4A51: 54              LD      D,H                 
4A52: 04              INC     B                   
4A53: 09              ADD     HL,BC               
4A54: 12              LD      (DE),A              
4A55: 02              LD      (BC),A              
4A56: 01 A8 04        LD      BC,$04A8            
4A59: 08 10 20        LD      ($2010),SP          
4A5C: 40              LD      B,B                 
4A5D: 80              ADD     A,B                 
4A5E: 18 30           JR      $4A90               ; {}
4A60: 60              LD      H,B                 
4A61: 04              INC     B                   
4A62: 02              LD      (BC),A              
4A63: 01 01 00        LD      BC,$0001            
4A66: C0              RET     NZ                  
4A67: 04              INC     B                   
4A68: 09              ADD     HL,BC               
4A69: 12              LD      (DE),A              
4A6A: 24              INC     H                   
4A6B: 48              LD      C,B                 
4A6C: 90              SUB     B                   
4A6D: 1B              DEC     DE                  
4A6E: 36 6C           LD      (HL),$6C            
4A70: 05              DEC     B                   
4A71: 0C              INC     C                   
4A72: 18 18           JR      $4A8C               ; {}
4A74: 06 D8           LD      B,$D8               
4A76: 05              DEC     B                   
4A77: 0A              LD      A,(BC)              
4A78: 14              INC     D                   
4A79: 28 50           JR      Z,$4ACB             ; {}
4A7B: A0              AND     B                   
4A7C: 1E 3C           LD      E,$3C               
4A7E: 78              LD      A,B                 
4A7F: 05              DEC     B                   
4A80: 01 01 01        LD      BC,$0101            
4A83: 01 F0 10        LD      BC,$10F0            
4A86: 32              LD      (HLD),A             
4A87: 22              LD      (HLI),A             
4A88: 47              LD      B,A                 
4A89: 81              ADD     A,C                 
4A8A: 20 00           JR      NZ,$4A8C            ; {}
4A8C: 92              SUB     D                   
4A8D: 4A              LD      C,D                 
4A8E: FF              RST     0X38                
4A8F: FF              RST     0X38                
4A90: 8C              ADC     A,H                 
4A91: 4A              LD      C,D                 
4A92: 9B              SBC     E                   
4A93: 20 AE           JR      NZ,$4A43            ; {}
4A95: 01 9C 00        LD      BC,$009C            
4A98: 00              NOP                         
4A99: 22              LD      (HLI),A             
4A9A: 44              LD      B,H                 
4A9B: 55              LD      D,L                 
4A9C: 66              LD      H,(HL)              
4A9D: 66              LD      H,(HL)              
4A9E: 88              ADC     A,B                 
4A9F: 88              ADC     A,B                 
4AA0: AA              XOR     D                   
4AA1: AA              XOR     D                   
4AA2: CC CC 04        CALL    Z,$04CC             
4AA5: 84              ADD     A,H                 
4AA6: 04              INC     B                   
4AA7: 84              ADD     A,H                 
4AA8: 00              NOP                         
4AA9: 2B              DEC     HL                  
4AAA: 4A              LD      C,D                 
4AAB: B3              OR      E                   
4AAC: 4A              LD      C,D                 
4AAD: B7              OR      A                   
4AAE: 4A              LD      C,D                 
4AAF: BB              CP      E                   
4AB0: 4A              LD      C,D                 
4AB1: BF              CP      A                   
4AB2: 4A              LD      C,D                 
4AB3: C3 4A 00        JP      $004A               
4AB6: 00              NOP                         
4AB7: D3                              
4AB8: 4A              LD      C,D                 
4AB9: 00              NOP                         
4ABA: 00              NOP                         
4ABB: E1              POP     HL                  
4ABC: 4A              LD      C,D                 
4ABD: 00              NOP                         
4ABE: 00              NOP                         
4ABF: F3              DI                          
4AC0: 4A              LD      C,D                 
4AC1: 00              NOP                         
4AC2: 00              NOP                         
4AC3: 9D              SBC     L                   
4AC4: 60              LD      H,B                 
4AC5: 21 00 96        LD      HL,$9600            
4AC8: A2              AND     D                   
4AC9: 5C              LD      E,H                 
4ACA: 5E              LD      E,(HL)              
4ACB: AA              XOR     D                   
4ACC: 60              LD      H,B                 
4ACD: 62              LD      H,D                 
4ACE: 64              LD      H,H                 
4ACF: AE              XOR     (HL)                
4AD0: 66              LD      H,(HL)              
4AD1: 95              SUB     L                   
4AD2: 00              NOP                         
4AD3: 9D              SBC     L                   
4AD4: 80              ADD     A,B                 
4AD5: 21 41 A2        LD      HL,$A241            
4AD8: 4A              LD      C,D                 
4AD9: 4C              LD      C,H                 
4ADA: AA              XOR     D                   
4ADB: 4E              LD      C,(HL)              
4ADC: 50              LD      D,B                 
4ADD: 52              LD      D,D                 
4ADE: AE              XOR     (HL)                
4ADF: 54              LD      D,H                 
4AE0: 00              NOP                         
4AE1: 9D              SBC     L                   
4AE2: 42              LD      B,D                 
4AE3: 6E              LD      L,(HL)              
4AE4: 20 99           JR      NZ,$4A7F            ; {}
4AE6: A2              AND     D                   
4AE7: 3C              INC     A                   
4AE8: 3E AA           LD      A,$AA               
4AEA: 40              LD      B,B                 
4AEB: 42              LD      B,D                 
4AEC: 44              LD      B,H                 
4AED: 9A              SBC     D                   
4AEE: A5              AND     L                   
4AEF: 46              LD      B,(HL)              
4AF0: A4              AND     H                   
4AF1: 01 00 A3        LD      BC,$A300            
4AF4: 01 AA 15        LD      BC,$15AA            
4AF7: 1A              LD      A,(DE)              
4AF8: 1A              LD      A,(DE)              
4AF9: 9B              SBC     E                   
4AFA: 1E A0           LD      E,$A0               
4AFC: 15              DEC     D                   
4AFD: 9C              SBC     H                   
4AFE: A7              AND     A                   
4AFF: 01 00 04        LD      BC,$0400            
4B02: 67              LD      H,A                 
4B03: 4A              LD      C,D                 
4B04: 0C              INC     C                   
4B05: 4B              LD      C,E                 
4B06: 24              INC     H                   
4B07: 4B              LD      C,E                 
4B08: 2C              INC     L                   
4B09: 4B              LD      C,E                 
4B0A: 00              NOP                         
4B0B: 00              NOP                         
4B0C: 42              LD      B,D                 
4B0D: 4B              LD      C,E                 
4B0E: 7C              LD      A,H                 
4B0F: 4B              LD      C,E                 
4B10: 7C              LD      A,H                 
4B11: 4B              LD      C,E                 
4B12: 7C              LD      A,H                 
4B13: 4B              LD      C,E                 
4B14: 7C              LD      A,H                 
4B15: 4B              LD      C,E                 
4B16: 7C              LD      A,H                 
4B17: 4B              LD      C,E                 
4B18: 7C              LD      A,H                 
4B19: 4B              LD      C,E                 
4B1A: 7C              LD      A,H                 
4B1B: 4B              LD      C,E                 
4B1C: 7C              LD      A,H                 
4B1D: 4B              LD      C,E                 
4B1E: E6 4B           AND     $4B                 
4B20: FF              RST     0X38                
4B21: FF              RST     0X38                
4B22: 0C              INC     C                   
4B23: 4B              LD      C,E                 
4B24: 47              LD      B,A                 
4B25: 4B              LD      C,E                 
4B26: B1              OR      C                   
4B27: 4B              LD      C,E                 
4B28: FF              RST     0X38                
4B29: FF              RST     0X38                
4B2A: 24              INC     H                   
4B2B: 4B              LD      C,E                 
4B2C: 77              LD      (HL),A              
4B2D: 4B              LD      C,E                 
4B2E: 77              LD      (HL),A              
4B2F: 4B              LD      C,E                 
4B30: 77              LD      (HL),A              
4B31: 4B              LD      C,E                 
4B32: 77              LD      (HL),A              
4B33: 4B              LD      C,E                 
4B34: 77              LD      (HL),A              
4B35: 4B              LD      C,E                 
4B36: 77              LD      (HL),A              
4B37: 4B              LD      C,E                 
4B38: 77              LD      (HL),A              
4B39: 4B              LD      C,E                 
4B3A: 77              LD      (HL),A              
4B3B: 4B              LD      C,E                 
4B3C: E6 4B           AND     $4B                 
4B3E: FF              RST     0X38                
4B3F: FF              RST     0X38                
4B40: 2C              INC     L                   
4B41: 4B              LD      C,E                 
4B42: 9D              SBC     L                   
4B43: 31 00 40        LD      SP,$4000            
4B46: 00              NOP                         
4B47: 9D              SBC     L                   
4B48: 30 81           JR      NC,$4ACB            ; {}
4B4A: 80              ADD     A,B                 
4B4B: 9B              SBC     E                   
4B4C: 08 A3 01        LD      ($01A3),SP          
4B4F: A2              AND     D                   
4B50: 44              LD      B,H                 
4B51: 46              LD      B,(HL)              
4B52: A3              AND     E                   
4B53: 4A              LD      C,D                 
4B54: A2              AND     D                   
4B55: 54              LD      D,H                 
4B56: 5C              LD      E,H                 
4B57: A7              AND     A                   
4B58: 5C              LD      E,H                 
4B59: A1              AND     C                   
4B5A: 58              LD      E,B                 
4B5B: 56              LD      D,(HL)              
4B5C: A4              AND     H                   
4B5D: 58              LD      E,B                 
4B5E: A2              AND     D                   
4B5F: 01 58 5C        LD      BC,$5C58            
4B62: 5E              LD      E,(HL)              
4B63: A3              AND     E                   
4B64: 5C              LD      E,H                 
4B65: 58              LD      E,B                 
4B66: A5              AND     L                   
4B67: 4A              LD      C,D                 
4B68: A4              AND     H                   
4B69: 7A              LD      A,D                 
4B6A: A7              AND     A                   
4B6B: 6C              LD      L,H                 
4B6C: A1              AND     C                   
4B6D: 6A              LD      L,D                 
4B6E: 6C              LD      L,H                 
4B6F: A4              AND     H                   
4B70: 70              LD      (HL),B              
4B71: 62              LD      H,D                 
4B72: 66              LD      H,(HL)              
4B73: AE              XOR     (HL)                
4B74: 74              LD      (HL),H              
4B75: 9C              SBC     H                   
4B76: 00              NOP                         
4B77: 9D              SBC     L                   
4B78: 52              LD      D,D                 
4B79: 6E              LD      L,(HL)              
4B7A: 40              LD      B,B                 
4B7B: 99              SBC     C                   
4B7C: 9B              SBC     E                   
4B7D: 02              LD      (BC),A              
4B7E: A2              AND     D                   
4B7F: 24              INC     H                   
4B80: 2C              INC     L                   
4B81: 32              LD      (HLD),A             
4B82: 2C              INC     L                   
4B83: 9C              SBC     H                   
4B84: 9B              SBC     E                   
4B85: 02              LD      (BC),A              
4B86: 24              INC     H                   
4B87: 30 36           JR      NC,$4BBF            ; {}
4B89: 30 9C           JR      NC,$4B27            ; {}
4B8B: 24              INC     H                   
4B8C: 2E 36           LD      L,$36               
4B8E: 2E 22           LD      L,$22               
4B90: 2E 34           LD      L,$34               
4B92: 2E 2C           LD      L,$2C               
4B94: 32              LD      (HLD),A             
4B95: 40              LD      B,B                 
4B96: 3A              LD      A,(HLD)             
4B97: 3C              INC     A                   
4B98: 36 32           LD      (HL),$32            
4B9A: 2C              INC     L                   
4B9B: 9B              SBC     E                   
4B9C: 02              LD      (BC),A              
4B9D: 28 2E           JR      Z,$4BCD             ; {}
4B9F: 36 2E           LD      (HL),$2E            
4BA1: 9C              SBC     H                   
4BA2: 9B              SBC     E                   
4BA3: 02              LD      (BC),A              
4BA4: 28 2E           JR      Z,$4BD4             ; {}
4BA6: 34              INC     (HL)                
4BA7: 2E 9C           LD      L,$9C               
4BA9: 9B              SBC     E                   
4BAA: 04              INC     B                   
4BAB: 24              INC     H                   
4BAC: 2C              INC     L                   
4BAD: 32              LD      (HLD),A             
4BAE: 2C              INC     L                   
4BAF: 9C              SBC     H                   
4BB0: 00              NOP                         
4BB1: 9D              SBC     L                   
4BB2: 61              LD      H,C                 
4BB3: 00              NOP                         
4BB4: 80              ADD     A,B                 
4BB5: A4              AND     H                   
4BB6: 01 97 AC        LD      BC,$AC97            
4BB9: 01 AD 2C        LD      BC,$2CAD            
4BBC: 2C              INC     L                   
4BBD: AC              XOR     H                   
4BBE: 2C              INC     L                   
4BBF: AA              XOR     D                   
4BC0: 2C              INC     L                   
4BC1: 98              SBC     B                   
4BC2: AC              XOR     H                   
4BC3: 32              LD      (HLD),A             
4BC4: AD              XOR     L                   
4BC5: 32              LD      (HLD),A             
4BC6: 36 AC           LD      (HL),$AC            
4BC8: 3A              LD      A,(HLD)             
4BC9: AA              XOR     D                   
4BCA: 36 A3           LD      (HL),$A3            
4BCC: 32              LD      (HLD),A             
4BCD: 40              LD      B,B                 
4BCE: 3A              LD      A,(HLD)             
4BCF: 4A              LD      C,D                 
4BD0: A4              AND     H                   
4BD1: 40              LD      B,B                 
4BD2: AC              XOR     H                   
4BD3: 40              LD      B,B                 
4BD4: AD              XOR     L                   
4BD5: 40              LD      B,B                 
4BD6: 42              LD      B,D                 
4BD7: AC              XOR     H                   
4BD8: 40              LD      B,B                 
4BD9: AA              XOR     D                   
4BDA: 3E A4           LD      A,$A4               
4BDC: 38 A3           JR      C,$4B81             ; {}
4BDE: 36 A7           LD      (HL),$A7            
4BE0: 40              LD      B,B                 
4BE1: A4              AND     H                   
4BE2: 40              LD      B,B                 
4BE3: A7              AND     A                   
4BE4: 01 00 9B        LD      BC,$9B00            
4BE7: 0B              DEC     BC                  
4BE8: A4              AND     H                   
4BE9: 01 9C 00        LD      BC,$009C            
4BEC: 00              NOP                         
4BED: 58              LD      E,B                 
4BEE: 4A              LD      C,D                 
4BEF: F7              RST     0X30                
4BF0: 4B              LD      C,E                 
4BF1: FF              RST     0X38                
4BF2: 4B              LD      C,E                 
4BF3: 07              RLCA                        
4BF4: 4C              LD      C,H                 
4BF5: 0F              RRCA                        
4BF6: 4C              LD      C,H                 
4BF7: 17              RLA                         
4BF8: 4C              LD      C,H                 
4BF9: 50              LD      D,B                 
4BFA: 4C              LD      C,H                 
4BFB: FF              RST     0X38                
4BFC: FF              RST     0X38                
4BFD: F9              LD      SP,HL               
4BFE: 4B              LD      C,E                 
4BFF: 24              INC     H                   
4C00: 4C              LD      C,H                 
4C01: 61              LD      H,C                 
4C02: 4C              LD      C,H                 
4C03: FF              RST     0X38                
4C04: FF              RST     0X38                
4C05: 01 4C 31        LD      BC,$314C            
4C08: 4C              LD      C,H                 
4C09: B1              OR      C                   
4C0A: 4C              LD      C,H                 
4C0B: FF              RST     0X38                
4C0C: FF              RST     0X38                
4C0D: 09              ADD     HL,BC               
4C0E: 4C              LD      C,H                 
4C0F: 3E 4C           LD      A,$4C               
4C11: FA 4C FF        LD      A,($FF4C)           
4C14: FF              RST     0X38                
4C15: 11 4C 9D        LD      DE,$9D4C            
4C18: 60              LD      H,B                 
4C19: 00              NOP                         
4C1A: 41              LD      B,C                 
4C1B: A7              AND     A                   
4C1C: 01 A1 4E        LD      BC,$4EA1            
4C1F: AA              XOR     D                   
4C20: 01 AE 50        LD      BC,$50AE            
4C23: 00              NOP                         
4C24: 9D              SBC     L                   
4C25: 40              LD      B,B                 
4C26: 00              NOP                         
4C27: 01 A7 01        LD      BC,$01A7            
4C2A: A1              AND     C                   
4C2B: 64              LD      H,H                 
4C2C: AA              XOR     D                   
4C2D: 01 AE 66        LD      BC,$66AE            
4C30: 00              NOP                         
4C31: 9D              SBC     L                   
4C32: A1              AND     C                   
4C33: 4C              LD      C,H                 
4C34: 20 A7           JR      NZ,$4BDD            ; {}
4C36: 01 A1 5A        LD      BC,$5AA1            
4C39: AA              XOR     D                   
4C3A: 01 AE 5C        LD      BC,$5CAE            
4C3D: 00              NOP                         
4C3E: A7              AND     A                   
4C3F: 01 A1 01        LD      BC,$01A1            
4C42: AA              XOR     D                   
4C43: 01 A5 01        LD      BC,$01A5            
4C46: A1              AND     C                   
4C47: FF              RST     0X38                
4C48: A2              AND     D                   
4C49: FF              RST     0X38                
4C4A: FF              RST     0X38                
4C4B: A1              AND     C                   
4C4C: FF              RST     0X38                
4C4D: A2              AND     D                   
4C4E: FF              RST     0X38                
4C4F: 00              NOP                         
4C50: 9D              SBC     L                   
4C51: 22              LD      (HLI),A             
4C52: 00              NOP                         
4C53: 80              ADD     A,B                 
4C54: 97              SUB     A                   
4C55: 9B              SBC     E                   
4C56: 20 A1           JR      NZ,$4BF9            ; {}
4C58: 54              LD      D,H                 
4C59: 6A              LD      L,D                 
4C5A: 62              LD      H,D                 
4C5B: 5C              LD      E,H                 
4C5C: 78              LD      A,B                 
4C5D: 70              LD      (HL),B              
4C5E: 6A              LD      L,D                 
4C5F: 9C              SBC     H                   
4C60: 00              NOP                         
4C61: 9D              SBC     L                   
4C62: 81              ADD     A,C                 
4C63: 00              NOP                         
4C64: 40              LD      B,B                 
4C65: A6              AND     (HL)                
4C66: 46              LD      B,(HL)              
4C67: A0              AND     B                   
4C68: 46              LD      B,(HL)              
4C69: 4A              LD      C,D                 
4C6A: A6              AND     (HL)                
4C6B: 4E              LD      C,(HL)              
4C6C: A1              AND     C                   
4C6D: 4A              LD      C,D                 
4C6E: A3              AND     E                   
4C6F: 46              LD      B,(HL)              
4C70: 54              LD      D,H                 
4C71: 4E              LD      C,(HL)              
4C72: 5E              LD      E,(HL)              
4C73: A4              AND     H                   
4C74: 54              LD      D,H                 
4C75: A6              AND     (HL)                
4C76: 54              LD      D,H                 
4C77: A0              AND     B                   
4C78: 54              LD      D,H                 
4C79: 56              LD      D,(HL)              
4C7A: A6              AND     (HL)                
4C7B: 54              LD      D,H                 
4C7C: A1              AND     C                   
4C7D: 52              LD      D,D                 
4C7E: A4              AND     H                   
4C7F: 4C              LD      C,H                 
4C80: A3              AND     E                   
4C81: 4A              LD      C,D                 
4C82: 54              LD      D,H                 
4C83: A4              AND     H                   
4C84: 46              LD      B,(HL)              
4C85: A5              AND     L                   
4C86: 01 01 01        LD      BC,$0101            
4C89: 9D              SBC     L                   
4C8A: 61              LD      H,C                 
4C8B: 00              NOP                         
4C8C: 80              ADD     A,B                 
4C8D: 97              SUB     A                   
4C8E: A1              AND     C                   
4C8F: 36 A6           LD      (HL),$A6            
4C91: 36 A1           LD      (HL),$A1            
4C93: 36 A6           LD      (HL),$A6            
4C95: 36 A1           LD      (HL),$A1            
4C97: 36 A2           LD      (HL),$A2            
4C99: 36 36           LD      (HL),$36            
4C9B: A1              AND     C                   
4C9C: 36 A2           LD      (HL),$A2            
4C9E: 36 98           LD      (HL),$98            
4CA0: 00              NOP                         
4CA1: 8A              ADC     A,D                 
4CA2: DF              RST     0X18                
4CA3: DA 86 31        JP      C,$3186             
4CA6: 01 36 86        LD      BC,$8636            
4CA9: 8A              ADC     A,D                 
4CAA: DF              RST     0X18                
4CAB: DA 86 31        JP      C,$3186             
4CAE: 01 36 86        LD      BC,$8636            
4CB1: 9D              SBC     L                   
4CB2: A1              AND     C                   
4CB3: 4C              LD      C,H                 
4CB4: 20 97           JR      NZ,$4C4D            ; {}
4CB6: 9B              SBC     E                   
4CB7: 02              LD      (BC),A              
4CB8: AA              XOR     D                   
4CB9: 30 01           JR      NC,$4CBC            ; {}
4CBB: A0              AND     B                   
4CBC: 01 A1 01        LD      BC,$01A1            
4CBF: 9C              SBC     H                   
4CC0: A6              AND     (HL)                
4CC1: 01 AA 30        LD      BC,$30AA            
4CC4: 01 A0 01        LD      BC,$01A0            
4CC7: A1              AND     C                   
4CC8: 01 9B 02        LD      BC,$029B            
4CCB: AA              XOR     D                   
4CCC: 30 01           JR      NC,$4CCF            ; {}
4CCE: A0              AND     B                   
4CCF: 01 9C A1        LD      BC,$A19C            
4CD2: 01 A3 01        LD      BC,$01A3            
4CD5: 9B              SBC     E                   
4CD6: 02              LD      (BC),A              
4CD7: AA              XOR     D                   
4CD8: 30 01           JR      NC,$4CDB            ; {}
4CDA: A0              AND     B                   
4CDB: 01 A1 01        LD      BC,$01A1            
4CDE: 9C              SBC     H                   
4CDF: A6              AND     (HL)                
4CE0: 01 AA 30        LD      BC,$30AA            
4CE3: 01 A0 01        LD      BC,$01A0            
4CE6: A1              AND     C                   
4CE7: 01 9B 02        LD      BC,$029B            
4CEA: AA              XOR     D                   
4CEB: 30 01           JR      NC,$4CEE            ; {}
4CED: A0              AND     B                   
4CEE: 01 9C A1        LD      BC,$A19C            
4CF1: 01 A6 01        LD      BC,$01A6            
4CF4: AA              XOR     D                   
4CF5: 30 01           JR      NC,$4CF8            ; {}
4CF7: A0              AND     B                   
4CF8: 01 00 9B        LD      BC,$9B00            
4CFB: 07              RLCA                        
4CFC: A1              AND     C                   
4CFD: 15              DEC     D                   
4CFE: 15              DEC     D                   
4CFF: 15              DEC     D                   
4D00: 15              DEC     D                   
4D01: FF              RST     0X38                
4D02: 15              DEC     D                   
4D03: 15              DEC     D                   
4D04: 15              DEC     D                   
4D05: 15              DEC     D                   
4D06: 15              DEC     D                   
4D07: 15              DEC     D                   
4D08: 15              DEC     D                   
4D09: FF              RST     0X38                
4D0A: 15              DEC     D                   
4D0B: 15              DEC     D                   
4D0C: 1A              LD      A,(DE)              
4D0D: 9C              SBC     H                   
4D0E: 9B              SBC     E                   
4D0F: 02              LD      (BC),A              
4D10: FF              RST     0X38                
4D11: FF              RST     0X38                
4D12: 15              DEC     D                   
4D13: 15              DEC     D                   
4D14: 9C              SBC     H                   
4D15: FF              RST     0X38                
4D16: FF              RST     0X38                
4D17: 15              DEC     D                   
4D18: FF              RST     0X38                
4D19: 15              DEC     D                   
4D1A: FF              RST     0X38                
4D1B: FF              RST     0X38                
4D1C: 15              DEC     D                   
4D1D: 00              NOP                         
4D1E: 00              NOP                         
4D1F: 2B              DEC     HL                  
4D20: 4A              LD      C,D                 
4D21: 29              ADD     HL,HL               
4D22: 4D              LD      C,L                 
4D23: 2F              CPL                         
4D24: 4D              LD      C,L                 
4D25: 35              DEC     (HL)                
4D26: 4D              LD      C,L                 
4D27: 00              NOP                         
4D28: 00              NOP                         
4D29: 3B              DEC     SP                  
4D2A: 4D              LD      C,L                 
4D2B: FF              RST     0X38                
4D2C: FF              RST     0X38                
4D2D: 29              ADD     HL,HL               
4D2E: 4D              LD      C,L                 
4D2F: 51              LD      D,C                 
4D30: 4D              LD      C,L                 
4D31: FF              RST     0X38                
4D32: FF              RST     0X38                
4D33: 2F              CPL                         
4D34: 4D              LD      C,L                 
4D35: 87              ADD     A,A                 
4D36: 4D              LD      C,L                 
4D37: FF              RST     0X38                
4D38: FF              RST     0X38                
4D39: 35              DEC     (HL)                
4D3A: 4D              LD      C,L                 
4D3B: 9D              SBC     L                   
4D3C: 43              LD      B,E                 
4D3D: 00              NOP                         
4D3E: 80              ADD     A,B                 
4D3F: A7              AND     A                   
4D40: 4C              LD      C,H                 
4D41: 4C              LD      C,H                 
4D42: 4C              LD      C,H                 
4D43: 4C              LD      C,H                 
4D44: 4A              LD      C,D                 
4D45: 4A              LD      C,D                 
4D46: 4A              LD      C,D                 
4D47: 4A              LD      C,D                 
4D48: 46              LD      B,(HL)              
4D49: 46              LD      B,(HL)              
4D4A: 46              LD      B,(HL)              
4D4B: 46              LD      B,(HL)              
4D4C: 42              LD      B,D                 
4D4D: 46              LD      B,(HL)              
4D4E: 4A              LD      C,D                 
4D4F: 50              LD      D,B                 
4D50: 00              NOP                         
4D51: 9D              SBC     L                   
4D52: 40              LD      B,B                 
4D53: 21 80 A8        LD      HL,$A880            
4D56: 5A              LD      E,D                 
4D57: A3              AND     E                   
4D58: 01 A2 58        LD      BC,$58A2            
4D5B: A3              AND     E                   
4D5C: 5E              LD      E,(HL)              
4D5D: A8              XOR     B                   
4D5E: 50              LD      D,B                 
4D5F: A2              AND     D                   
4D60: 01 A3 5A        LD      BC,$5AA3            
4D63: A2              AND     D                   
4D64: 42              LD      B,D                 
4D65: A3              AND     E                   
4D66: 46              LD      B,(HL)              
4D67: A2              AND     D                   
4D68: 4A              LD      C,D                 
4D69: A3              AND     E                   
4D6A: 4C              LD      C,H                 
4D6B: A2              AND     D                   
4D6C: 4A              LD      C,D                 
4D6D: A3              AND     E                   
4D6E: 4C              LD      C,H                 
4D6F: A7              AND     A                   
4D70: 40              LD      B,B                 
4D71: 54              LD      D,H                 
4D72: AE              XOR     (HL)                
4D73: 50              LD      D,B                 
4D74: A2              AND     D                   
4D75: 01 00 44        LD      BC,$4400            
4D78: 44              LD      B,H                 
4D79: 44              LD      B,H                 
4D7A: 42              LD      B,D                 
4D7B: 00              NOP                         
4D7C: 00              NOP                         
4D7D: 00              NOP                         
4D7E: 00              NOP                         
4D7F: 44              LD      B,H                 
4D80: 44              LD      B,H                 
4D81: 44              LD      B,H                 
4D82: 42              LD      B,D                 
4D83: 00              NOP                         
4D84: 00              NOP                         
4D85: 00              NOP                         
4D86: 00              NOP                         
4D87: 9D              SBC     L                   
4D88: 77              LD      (HL),A              
4D89: 4D              LD      C,L                 
4D8A: 20 99           JR      NZ,$4D25            ; {}
4D8C: A7              AND     A                   
4D8D: 4A              LD      C,D                 
4D8E: 4A              LD      C,D                 
4D8F: 46              LD      B,(HL)              
4D90: 46              LD      B,(HL)              
4D91: 46              LD      B,(HL)              
4D92: 46              LD      B,(HL)              
4D93: 42              LD      B,D                 
4D94: 42              LD      B,D                 
4D95: 42              LD      B,D                 
4D96: 42              LD      B,D                 
4D97: 40              LD      B,B                 
4D98: 40              LD      B,B                 
4D99: 3E 3E           LD      A,$3E               
4D9B: 44              LD      B,H                 
4D9C: 4A              LD      C,D                 
4D9D: 00              NOP                         
4D9E: AF              XOR     A                   
4D9F: EA 79 D3        LD      ($D379),A           
4DA2: EA 4F D3        LD      ($D34F),A           
4DA5: EA 98 D3        LD      ($D398),A           
4DA8: EA 93 D3        LD      ($D393),A           
4DAB: EA C9 D3        LD      ($D3C9),A           
4DAE: EA A3 D3        LD      ($D3A3),A           
4DB1: EA E5 D3        LD      ($D3E5),A           
4DB4: 3E 08           LD      A,$08               
4DB6: E0 21           LD      ($FF00+$21),A       
4DB8: 3E 80           LD      A,$80               
4DBA: E0 23           LD      ($FF00+$23),A       
4DBC: 3E FF           LD      A,$FF               
4DBE: E0 25           LD      ($FF00+$25),A       
4DC0: 3E 03           LD      A,$03               
4DC2: EA 55 D3        LD      ($D355),A           
4DC5: AF              XOR     A                   
4DC6: EA 69 D3        LD      ($D369),A           
4DC9: AF              XOR     A                   
4DCA: EA 61 D3        LD      ($D361),A           
4DCD: EA 71 D3        LD      ($D371),A           
4DD0: EA 1F D3        LD      ($D31F),A           
4DD3: EA 2F D3        LD      ($D32F),A           
4DD6: EA 3F D3        LD      ($D33F),A           
4DD9: EA 9E D3        LD      ($D39E),A           
4DDC: EA 9F D3        LD      ($D39F),A           
4DDF: EA D9 D3        LD      ($D3D9),A           
4DE2: EA DA D3        LD      ($D3DA),A           
4DE5: EA B6 D3        LD      ($D3B6),A           
4DE8: EA B7 D3        LD      ($D3B7),A           
4DEB: EA B8 D3        LD      ($D3B8),A           
4DEE: EA B9 D3        LD      ($D3B9),A           
4DF1: EA BA D3        LD      ($D3BA),A           
4DF4: EA BB D3        LD      ($D3BB),A           
4DF7: EA 94 D3        LD      ($D394),A           
4DFA: EA 95 D3        LD      ($D395),A           
4DFD: EA 96 D3        LD      ($D396),A           
4E00: EA 90 D3        LD      ($D390),A           
4E03: EA 91 D3        LD      ($D391),A           
4E06: EA 92 D3        LD      ($D392),A           
4E09: EA C6 D3        LD      ($D3C6),A           
4E0C: EA C7 D3        LD      ($D3C7),A           
4E0F: EA C8 D3        LD      ($D3C8),A           
4E12: EA A0 D3        LD      ($D3A0),A           
4E15: EA A1 D3        LD      ($D3A1),A           
4E18: EA A2 D3        LD      ($D3A2),A           
4E1B: EA CD D3        LD      ($D3CD),A           
4E1E: EA D6 D3        LD      ($D3D6),A           
4E21: EA D7 D3        LD      ($D3D7),A           
4E24: EA D8 D3        LD      ($D3D8),A           
4E27: EA DC D3        LD      ($D3DC),A           
4E2A: EA E7 D3        LD      ($D3E7),A           
4E2D: EA E2 D3        LD      ($D3E2),A           
4E30: EA E3 D3        LD      ($D3E3),A           
4E33: EA E4 D3        LD      ($D3E4),A           
4E36: 3E 08           LD      A,$08               
4E38: E0 12           LD      ($FF00+$12),A       
4E3A: E0 17           LD      ($FF00+$17),A       
4E3C: 3E 80           LD      A,$80               
4E3E: E0 14           LD      ($FF00+$14),A       
4E40: E0 19           LD      ($FF00+$19),A       
4E42: AF              XOR     A                   
4E43: E0 10           LD      ($FF00+$10),A       
4E45: E0 1A           LD      ($FF00+$1A),A       
4E47: C9              RET                         
4E48: FF              RST     0X38                
4E49: FF              RST     0X38                
4E4A: FF              RST     0X38                
4E4B: FF              RST     0X38                
4E4C: FF              RST     0X38                
4E4D: FF              RST     0X38                
4E4E: FF              RST     0X38                
4E4F: FF              RST     0X38                
4E50: FF              RST     0X38                
4E51: FF              RST     0X38                
4E52: FF              RST     0X38                
4E53: FF              RST     0X38                
4E54: FF              RST     0X38                
4E55: FF              RST     0X38                
4E56: FF              RST     0X38                
4E57: FF              RST     0X38                
4E58: FF              RST     0X38                
4E59: FF              RST     0X38                
4E5A: FF              RST     0X38                
4E5B: FF              RST     0X38                
4E5C: FF              RST     0X38                
4E5D: FF              RST     0X38                
4E5E: FF              RST     0X38                
4E5F: FF              RST     0X38                
4E60: FF              RST     0X38                
4E61: FF              RST     0X38                
4E62: FF              RST     0X38                
4E63: FF              RST     0X38                
4E64: FF              RST     0X38                
4E65: FF              RST     0X38                
4E66: FF              RST     0X38                
4E67: FF              RST     0X38                
4E68: FF              RST     0X38                
4E69: FF              RST     0X38                
4E6A: FF              RST     0X38                
4E6B: FF              RST     0X38                
4E6C: FF              RST     0X38                
4E6D: FF              RST     0X38                
4E6E: FF              RST     0X38                
4E6F: FF              RST     0X38                
4E70: FF              RST     0X38                
4E71: FF              RST     0X38                
4E72: FF              RST     0X38                
4E73: FF              RST     0X38                
4E74: FF              RST     0X38                
4E75: FF              RST     0X38                
4E76: FF              RST     0X38                
4E77: FF              RST     0X38                
4E78: FF              RST     0X38                
4E79: FF              RST     0X38                
4E7A: FF              RST     0X38                
4E7B: FF              RST     0X38                
4E7C: FF              RST     0X38                
4E7D: FF              RST     0X38                
4E7E: FF              RST     0X38                
4E7F: FF              RST     0X38                
4E80: FF              RST     0X38                
4E81: FF              RST     0X38                
4E82: FF              RST     0X38                
4E83: FF              RST     0X38                
4E84: FF              RST     0X38                
4E85: FF              RST     0X38                
4E86: FF              RST     0X38                
4E87: FF              RST     0X38                
4E88: FF              RST     0X38                
4E89: FF              RST     0X38                
4E8A: FF              RST     0X38                
4E8B: FF              RST     0X38                
4E8C: FF              RST     0X38                
4E8D: FF              RST     0X38                
4E8E: FF              RST     0X38                
4E8F: FF              RST     0X38                
4E90: FF              RST     0X38                
4E91: FF              RST     0X38                
4E92: FF              RST     0X38                
4E93: FF              RST     0X38                
4E94: FF              RST     0X38                
4E95: FF              RST     0X38                
4E96: FF              RST     0X38                
4E97: FF              RST     0X38                
4E98: FF              RST     0X38                
4E99: FF              RST     0X38                
4E9A: FF              RST     0X38                
4E9B: FF              RST     0X38                
4E9C: FF              RST     0X38                
4E9D: FF              RST     0X38                
4E9E: FF              RST     0X38                
4E9F: FF              RST     0X38                
4EA0: FF              RST     0X38                
4EA1: FF              RST     0X38                
4EA2: FF              RST     0X38                
4EA3: FF              RST     0X38                
4EA4: FF              RST     0X38                
4EA5: FF              RST     0X38                
4EA6: FF              RST     0X38                
4EA7: FF              RST     0X38                
4EA8: FF              RST     0X38                
4EA9: FF              RST     0X38                
4EAA: FF              RST     0X38                
4EAB: FF              RST     0X38                
4EAC: FF              RST     0X38                
4EAD: FF              RST     0X38                
4EAE: FF              RST     0X38                
4EAF: FF              RST     0X38                
4EB0: FF              RST     0X38                
4EB1: FF              RST     0X38                
4EB2: FF              RST     0X38                
4EB3: FF              RST     0X38                
4EB4: FF              RST     0X38                
4EB5: FF              RST     0X38                
4EB6: FF              RST     0X38                
4EB7: FF              RST     0X38                
4EB8: FF              RST     0X38                
4EB9: FF              RST     0X38                
4EBA: FF              RST     0X38                
4EBB: FF              RST     0X38                
4EBC: FF              RST     0X38                
4EBD: FF              RST     0X38                
4EBE: FF              RST     0X38                
4EBF: FF              RST     0X38                
4EC0: FF              RST     0X38                
4EC1: FF              RST     0X38                
4EC2: FF              RST     0X38                
4EC3: FF              RST     0X38                
4EC4: FF              RST     0X38                
4EC5: FF              RST     0X38                
4EC6: FF              RST     0X38                
4EC7: FF              RST     0X38                
4EC8: FF              RST     0X38                
4EC9: FF              RST     0X38                
4ECA: FF              RST     0X38                
4ECB: FF              RST     0X38                
4ECC: FF              RST     0X38                
4ECD: FF              RST     0X38                
4ECE: FF              RST     0X38                
4ECF: FF              RST     0X38                
4ED0: FF              RST     0X38                
4ED1: FF              RST     0X38                
4ED2: FF              RST     0X38                
4ED3: FF              RST     0X38                
4ED4: FF              RST     0X38                
4ED5: FF              RST     0X38                
4ED6: FF              RST     0X38                
4ED7: FF              RST     0X38                
4ED8: FF              RST     0X38                
4ED9: FF              RST     0X38                
4EDA: FF              RST     0X38                
4EDB: FF              RST     0X38                
4EDC: FF              RST     0X38                
4EDD: FF              RST     0X38                
4EDE: FF              RST     0X38                
4EDF: FF              RST     0X38                
4EE0: FF              RST     0X38                
4EE1: FF              RST     0X38                
4EE2: FF              RST     0X38                
4EE3: FF              RST     0X38                
4EE4: FF              RST     0X38                
4EE5: FF              RST     0X38                
4EE6: FF              RST     0X38                
4EE7: FF              RST     0X38                
4EE8: FF              RST     0X38                
4EE9: FF              RST     0X38                
4EEA: FF              RST     0X38                
4EEB: FF              RST     0X38                
4EEC: FF              RST     0X38                
4EED: FF              RST     0X38                
4EEE: FF              RST     0X38                
4EEF: FF              RST     0X38                
4EF0: FF              RST     0X38                
4EF1: FF              RST     0X38                
4EF2: FF              RST     0X38                
4EF3: FF              RST     0X38                
4EF4: FF              RST     0X38                
4EF5: FF              RST     0X38                
4EF6: FF              RST     0X38                
4EF7: FF              RST     0X38                
4EF8: FF              RST     0X38                
4EF9: FF              RST     0X38                
4EFA: FF              RST     0X38                
4EFB: FF              RST     0X38                
4EFC: FF              RST     0X38                
4EFD: FF              RST     0X38                
4EFE: FF              RST     0X38                
4EFF: FF              RST     0X38                
4F00: FF              RST     0X38                
4F01: FF              RST     0X38                
4F02: FF              RST     0X38                
4F03: FF              RST     0X38                
4F04: FF              RST     0X38                
4F05: FF              RST     0X38                
4F06: FF              RST     0X38                
4F07: FF              RST     0X38                
4F08: FF              RST     0X38                
4F09: FF              RST     0X38                
4F0A: FF              RST     0X38                
4F0B: FF              RST     0X38                
4F0C: FF              RST     0X38                
4F0D: FF              RST     0X38                
4F0E: FF              RST     0X38                
4F0F: FF              RST     0X38                
4F10: FF              RST     0X38                
4F11: FF              RST     0X38                
4F12: FF              RST     0X38                
4F13: FF              RST     0X38                
4F14: FF              RST     0X38                
4F15: FF              RST     0X38                
4F16: FF              RST     0X38                
4F17: FF              RST     0X38                
4F18: FF              RST     0X38                
4F19: FF              RST     0X38                
4F1A: FF              RST     0X38                
4F1B: FF              RST     0X38                
4F1C: FF              RST     0X38                
4F1D: FF              RST     0X38                
4F1E: FF              RST     0X38                
4F1F: FF              RST     0X38                
4F20: FF              RST     0X38                
4F21: FF              RST     0X38                
4F22: FF              RST     0X38                
4F23: FF              RST     0X38                
4F24: FF              RST     0X38                
4F25: FF              RST     0X38                
4F26: FF              RST     0X38                
4F27: FF              RST     0X38                
4F28: FF              RST     0X38                
4F29: FF              RST     0X38                
4F2A: FF              RST     0X38                
4F2B: FF              RST     0X38                
4F2C: FF              RST     0X38                
4F2D: FF              RST     0X38                
4F2E: FF              RST     0X38                
4F2F: FF              RST     0X38                
4F30: FF              RST     0X38                
4F31: FF              RST     0X38                
4F32: FF              RST     0X38                
4F33: FF              RST     0X38                
4F34: FF              RST     0X38                
4F35: FF              RST     0X38                
4F36: FF              RST     0X38                
4F37: FF              RST     0X38                
4F38: FF              RST     0X38                
4F39: FF              RST     0X38                
4F3A: FF              RST     0X38                
4F3B: FF              RST     0X38                
4F3C: FF              RST     0X38                
4F3D: FF              RST     0X38                
4F3E: FF              RST     0X38                
4F3F: FF              RST     0X38                
4F40: FF              RST     0X38                
4F41: FF              RST     0X38                
4F42: FF              RST     0X38                
4F43: FF              RST     0X38                
4F44: FF              RST     0X38                
4F45: FF              RST     0X38                
4F46: FF              RST     0X38                
4F47: FF              RST     0X38                
4F48: FF              RST     0X38                
4F49: FF              RST     0X38                
4F4A: FF              RST     0X38                
4F4B: FF              RST     0X38                
4F4C: FF              RST     0X38                
4F4D: FF              RST     0X38                
4F4E: FF              RST     0X38                
4F4F: FF              RST     0X38                
4F50: FF              RST     0X38                
4F51: FF              RST     0X38                
4F52: FF              RST     0X38                
4F53: FF              RST     0X38                
4F54: FF              RST     0X38                
4F55: FF              RST     0X38                
4F56: FF              RST     0X38                
4F57: FF              RST     0X38                
4F58: FF              RST     0X38                
4F59: FF              RST     0X38                
4F5A: FF              RST     0X38                
4F5B: FF              RST     0X38                
4F5C: FF              RST     0X38                
4F5D: FF              RST     0X38                
4F5E: FF              RST     0X38                
4F5F: FF              RST     0X38                
4F60: FF              RST     0X38                
4F61: FF              RST     0X38                
4F62: FF              RST     0X38                
4F63: FF              RST     0X38                
4F64: FF              RST     0X38                
4F65: FF              RST     0X38                
4F66: FF              RST     0X38                
4F67: FF              RST     0X38                
4F68: FF              RST     0X38                
4F69: FF              RST     0X38                
4F6A: FF              RST     0X38                
4F6B: FF              RST     0X38                
4F6C: FF              RST     0X38                
4F6D: FF              RST     0X38                
4F6E: FF              RST     0X38                
4F6F: FF              RST     0X38                
4F70: FF              RST     0X38                
4F71: FF              RST     0X38                
4F72: FF              RST     0X38                
4F73: FF              RST     0X38                
4F74: FF              RST     0X38                
4F75: FF              RST     0X38                
4F76: FF              RST     0X38                
4F77: FF              RST     0X38                
4F78: FF              RST     0X38                
4F79: FF              RST     0X38                
4F7A: FF              RST     0X38                
4F7B: FF              RST     0X38                
4F7C: FF              RST     0X38                
4F7D: FF              RST     0X38                
4F7E: FF              RST     0X38                
4F7F: FF              RST     0X38                
4F80: FF              RST     0X38                
4F81: FF              RST     0X38                
4F82: FF              RST     0X38                
4F83: FF              RST     0X38                
4F84: FF              RST     0X38                
4F85: FF              RST     0X38                
4F86: FF              RST     0X38                
4F87: FF              RST     0X38                
4F88: FF              RST     0X38                
4F89: FF              RST     0X38                
4F8A: FF              RST     0X38                
4F8B: FF              RST     0X38                
4F8C: FF              RST     0X38                
4F8D: FF              RST     0X38                
4F8E: FF              RST     0X38                
4F8F: FF              RST     0X38                
4F90: FF              RST     0X38                
4F91: FF              RST     0X38                
4F92: FF              RST     0X38                
4F93: FF              RST     0X38                
4F94: FF              RST     0X38                
4F95: FF              RST     0X38                
4F96: FF              RST     0X38                
4F97: FF              RST     0X38                
4F98: FF              RST     0X38                
4F99: FF              RST     0X38                
4F9A: FF              RST     0X38                
4F9B: FF              RST     0X38                
4F9C: FF              RST     0X38                
4F9D: FF              RST     0X38                
4F9E: FF              RST     0X38                
4F9F: FF              RST     0X38                
4FA0: FF              RST     0X38                
4FA1: FF              RST     0X38                
4FA2: FF              RST     0X38                
4FA3: FF              RST     0X38                
4FA4: FF              RST     0X38                
4FA5: FF              RST     0X38                
4FA6: FF              RST     0X38                
4FA7: FF              RST     0X38                
4FA8: FF              RST     0X38                
4FA9: FF              RST     0X38                
4FAA: FF              RST     0X38                
4FAB: FF              RST     0X38                
4FAC: FF              RST     0X38                
4FAD: FF              RST     0X38                
4FAE: FF              RST     0X38                
4FAF: FF              RST     0X38                
4FB0: FF              RST     0X38                
4FB1: FF              RST     0X38                
4FB2: FF              RST     0X38                
4FB3: FF              RST     0X38                
4FB4: FF              RST     0X38                
4FB5: FF              RST     0X38                
4FB6: FF              RST     0X38                
4FB7: FF              RST     0X38                
4FB8: FF              RST     0X38                
4FB9: FF              RST     0X38                
4FBA: FF              RST     0X38                
4FBB: FF              RST     0X38                
4FBC: FF              RST     0X38                
4FBD: FF              RST     0X38                
4FBE: FF              RST     0X38                
4FBF: FF              RST     0X38                
4FC0: FF              RST     0X38                
4FC1: FF              RST     0X38                
4FC2: FF              RST     0X38                
4FC3: FF              RST     0X38                
4FC4: FF              RST     0X38                
4FC5: FF              RST     0X38                
4FC6: FF              RST     0X38                
4FC7: FF              RST     0X38                
4FC8: FF              RST     0X38                
4FC9: FF              RST     0X38                
4FCA: FF              RST     0X38                
4FCB: FF              RST     0X38                
4FCC: FF              RST     0X38                
4FCD: FF              RST     0X38                
4FCE: FF              RST     0X38                
4FCF: FF              RST     0X38                
4FD0: FF              RST     0X38                
4FD1: FF              RST     0X38                
4FD2: FF              RST     0X38                
4FD3: FF              RST     0X38                
4FD4: FF              RST     0X38                
4FD5: FF              RST     0X38                
4FD6: FF              RST     0X38                
4FD7: FF              RST     0X38                
4FD8: FF              RST     0X38                
4FD9: FF              RST     0X38                
4FDA: FF              RST     0X38                
4FDB: FF              RST     0X38                
4FDC: FF              RST     0X38                
4FDD: FF              RST     0X38                
4FDE: FF              RST     0X38                
4FDF: FF              RST     0X38                
4FE0: FF              RST     0X38                
4FE1: FF              RST     0X38                
4FE2: FF              RST     0X38                
4FE3: FF              RST     0X38                
4FE4: FF              RST     0X38                
4FE5: FF              RST     0X38                
4FE6: FF              RST     0X38                
4FE7: FF              RST     0X38                
4FE8: FF              RST     0X38                
4FE9: FF              RST     0X38                
4FEA: FF              RST     0X38                
4FEB: FF              RST     0X38                
4FEC: FF              RST     0X38                
4FED: FF              RST     0X38                
4FEE: FF              RST     0X38                
4FEF: FF              RST     0X38                
4FF0: FF              RST     0X38                
4FF1: FF              RST     0X38                
4FF2: FF              RST     0X38                
4FF3: FF              RST     0X38                
4FF4: FF              RST     0X38                
4FF5: FF              RST     0X38                
4FF6: FF              RST     0X38                
4FF7: FF              RST     0X38                
4FF8: FF              RST     0X38                
4FF9: FF              RST     0X38                
4FFA: FF              RST     0X38                
4FFB: FF              RST     0X38                
4FFC: FF              RST     0X38                
4FFD: FF              RST     0X38                
4FFE: FF              RST     0X38                
4FFF: FF              RST     0X38                
5000: 00              NOP                         
5001: 58              LD      E,B                 
5002: 4A              LD      C,D                 
5003: 8C              ADC     A,H                 
5004: 4A              LD      C,D                 
5005: 8C              ADC     A,H                 
5006: 4A              LD      C,D                 
5007: 0B              DEC     BC                  
5008: 50              LD      D,B                 
5009: 00              NOP                         
500A: 00              NOP                         
500B: 0F              RRCA                        
500C: 50              LD      D,B                 
500D: 00              NOP                         
500E: 00              NOP                         
500F: 9D              SBC     L                   
5010: 82              ADD     A,D                 
5011: 6E              LD      L,(HL)              
5012: 01 94 A3        LD      BC,$A394            
5015: 4A              LD      C,D                 
5016: A2              AND     D                   
5017: 4E              LD      C,(HL)              
5018: A3              AND     E                   
5019: 52              LD      D,D                 
501A: A2              AND     D                   
501B: 4E              LD      C,(HL)              
501C: A7              AND     A                   
501D: 4A              LD      C,D                 
501E: 58              LD      E,B                 
501F: 52              LD      D,D                 
5020: 62              LD      H,D                 
5021: A8              XOR     B                   
5022: 58              LD      E,B                 
5023: A3              AND     E                   
5024: 58              LD      E,B                 
5025: A2              AND     D                   
5026: 5A              LD      E,D                 
5027: A3              AND     E                   
5028: 58              LD      E,B                 
5029: A2              AND     D                   
502A: 56              LD      D,(HL)              
502B: A8              XOR     B                   
502C: 50              LD      D,B                 
502D: A7              AND     A                   
502E: 4E              LD      C,(HL)              
502F: 58              LD      E,B                 
5030: A8              XOR     B                   
5031: 4A              LD      C,D                 
5032: 9A              SBC     D                   
5033: 00              NOP                         
5034: 00              NOP                         
5035: 3A              LD      A,(HLD)             
5036: 4A              LD      C,D                 
5037: 3F              CCF                         
5038: 50              LD      D,B                 
5039: 47              LD      B,A                 
503A: 50              LD      D,B                 
503B: 4F              LD      C,A                 
503C: 50              LD      D,B                 
503D: 00              NOP                         
503E: 00              NOP                         
503F: EC                              
5040: 6F              LD      L,A                 
5041: 5B              LD      E,E                 
5042: 50              LD      D,B                 
5043: FF              RST     0X38                
5044: FF              RST     0X38                
5045: 41              LD      B,C                 
5046: 50              LD      D,B                 
5047: AB              XOR     E                   
5048: 50              LD      D,B                 
5049: D9              RETI                        
504A: 50              LD      D,B                 
504B: FF              RST     0X38                
504C: FF              RST     0X38                
504D: 49              LD      C,C                 
504E: 50              LD      D,B                 
504F: E1              POP     HL                  
5050: 6E              LD      L,(HL)              
5051: 3C              INC     A                   
5052: 51              LD      D,C                 
5053: C2 6E 7E        JP      NZ,$7E6E            ; {}
5056: 51              LD      D,C                 
5057: FF              RST     0X38                
5058: FF              RST     0X38                
5059: 53              LD      D,E                 
505A: 50              LD      D,B                 
505B: 9D              SBC     L                   
505C: 66              LD      H,(HL)              
505D: 81              ADD     A,C                 
505E: 80              ADD     A,B                 
505F: A5              AND     L                   
5060: 01 A2 01        LD      BC,$01A2            
5063: 5E              LD      E,(HL)              
5064: A1              AND     C                   
5065: 5E              LD      E,(HL)              
5066: 62              LD      H,D                 
5067: 66              LD      H,(HL)              
5068: 68              LD      L,B                 
5069: A3              AND     E                   
506A: 6C              LD      L,H                 
506B: 01 01 A1        LD      BC,$A101            
506E: 64              LD      H,H                 
506F: 6E              LD      L,(HL)              
5070: 72              LD      (HL),D              
5071: 76              HALT                        
5072: A3              AND     E                   
5073: 7C              LD      A,H                 
5074: 01 A7 01        LD      BC,$01A7            
5077: A1              AND     C                   
5078: 64              LD      H,H                 
5079: 68              LD      L,B                 
507A: A2              AND     D                   
507B: 6C              LD      L,H                 
507C: 64              LD      H,H                 
507D: A3              AND     E                   
507E: 5A              LD      E,D                 
507F: A7              AND     A                   
5080: 01 9B 02        LD      BC,$029B            
5083: A1              AND     C                   
5084: 68              LD      L,B                 
5085: 6C              LD      L,H                 
5086: A2              AND     D                   
5087: 6E              LD      L,(HL)              
5088: 9C              SBC     H                   
5089: 01 A7 01        LD      BC,$01A7            
508C: 9B              SBC     E                   
508D: 02              LD      (BC),A              
508E: A1              AND     C                   
508F: 64              LD      H,H                 
5090: 68              LD      L,B                 
5091: A2              AND     D                   
5092: 6C              LD      L,H                 
5093: 9C              SBC     H                   
5094: 01 A7 01        LD      BC,$01A7            
5097: A1              AND     C                   
5098: 62              LD      H,D                 
5099: 66              LD      H,(HL)              
509A: A2              AND     D                   
509B: 6A              LD      L,D                 
509C: A1              AND     C                   
509D: 6A              LD      L,D                 
509E: 6C              LD      L,H                 
509F: 70              LD      (HL),B              
50A0: 74              LD      (HL),H              
50A1: 76              HALT                        
50A2: 7A              LD      A,D                 
50A3: A2              AND     D                   
50A4: 74              LD      (HL),H              
50A5: 01 A8 01        LD      BC,$01A8            
50A8: A5              AND     L                   
50A9: 01 00 9D        LD      BC,$9D00            
50AC: A0              AND     B                   
50AD: 84              ADD     A,H                 
50AE: 80              ADD     A,B                 
50AF: A4              AND     H                   
50B0: 46              LD      B,(HL)              
50B1: A2              AND     D                   
50B2: 01 46 46        LD      BC,$4646            
50B5: A1              AND     C                   
50B6: 46              LD      B,(HL)              
50B7: 46              LD      B,(HL)              
50B8: 9B              SBC     E                   
50B9: 02              LD      (BC),A              
50BA: A6              AND     (HL)                
50BB: 46              LD      B,(HL)              
50BC: A1              AND     C                   
50BD: 42              LD      B,D                 
50BE: A3              AND     E                   
50BF: 46              LD      B,(HL)              
50C0: A2              AND     D                   
50C1: 01 46 46        LD      BC,$4646            
50C4: A1              AND     C                   
50C5: 46              LD      B,(HL)              
50C6: 46              LD      B,(HL)              
50C7: 9C              SBC     H                   
50C8: A2              AND     D                   
50C9: 46              LD      B,(HL)              
50CA: A1              AND     C                   
50CB: 3C              INC     A                   
50CC: 3C              INC     A                   
50CD: 9B              SBC     E                   
50CE: 02              LD      (BC),A              
50CF: A2              AND     D                   
50D0: 3C              INC     A                   
50D1: A1              AND     C                   
50D2: 3C              INC     A                   
50D3: 3C              INC     A                   
50D4: 9C              SBC     H                   
50D5: A2              AND     D                   
50D6: 3C              INC     A                   
50D7: 3C              INC     A                   
50D8: 00              NOP                         
50D9: 9D              SBC     L                   
50DA: 80              ADD     A,B                 
50DB: 21 40 A2        LD      HL,$A240            
50DE: 46              LD      B,(HL)              
50DF: 01 A7 3C        LD      BC,$3CA7            
50E2: A1              AND     C                   
50E3: 01 46 46        LD      BC,$4646            
50E6: 4A              LD      C,D                 
50E7: 4E              LD      C,(HL)              
50E8: 50              LD      D,B                 
50E9: A4              AND     H                   
50EA: 54              LD      D,H                 
50EB: A2              AND     D                   
50EC: 01 54 54        LD      BC,$5454            
50EF: A1              AND     C                   
50F0: 56              LD      D,(HL)              
50F1: 5A              LD      E,D                 
50F2: A4              AND     H                   
50F3: 5E              LD      E,(HL)              
50F4: A2              AND     D                   
50F5: 01 5E 5E        LD      BC,$5E5E            
50F8: A1              AND     C                   
50F9: 5A              LD      E,D                 
50FA: 56              LD      D,(HL)              
50FB: A6              AND     (HL)                
50FC: 5A              LD      E,D                 
50FD: A1              AND     C                   
50FE: 56              LD      D,(HL)              
50FF: A4              AND     H                   
5100: 54              LD      D,H                 
5101: A3              AND     E                   
5102: 54              LD      D,H                 
5103: A6              AND     (HL)                
5104: 50              LD      D,B                 
5105: A1              AND     C                   
5106: 54              LD      D,H                 
5107: A4              AND     H                   
5108: 56              LD      D,(HL)              
5109: A2              AND     D                   
510A: 54              LD      D,H                 
510B: 50              LD      D,B                 
510C: A6              AND     (HL)                
510D: 4C              LD      C,H                 
510E: A1              AND     C                   
510F: 50              LD      D,B                 
5110: A4              AND     H                   
5111: 54              LD      D,H                 
5112: A2              AND     D                   
5113: 50              LD      D,B                 
5114: 4C              LD      C,H                 
5115: A6              AND     (HL)                
5116: 4A              LD      C,D                 
5117: A1              AND     C                   
5118: 4E              LD      C,(HL)              
5119: A4              AND     H                   
511A: 52              LD      D,D                 
511B: A3              AND     E                   
511C: 58              LD      E,B                 
511D: 9D              SBC     L                   
511E: 60              LD      H,B                 
511F: 81              ADD     A,C                 
5120: 80              ADD     A,B                 
5121: A2              AND     D                   
5122: 54              LD      D,H                 
5123: A1              AND     C                   
5124: 46              LD      B,(HL)              
5125: 46              LD      B,(HL)              
5126: A2              AND     D                   
5127: 46              LD      B,(HL)              
5128: A1              AND     C                   
5129: 46              LD      B,(HL)              
512A: 46              LD      B,(HL)              
512B: A3              AND     E                   
512C: 46              LD      B,(HL)              
512D: 01 A2 01        LD      BC,$01A2            
5130: A1              AND     C                   
5131: 44              LD      B,H                 
5132: 44              LD      B,H                 
5133: A2              AND     D                   
5134: 44              LD      B,H                 
5135: A1              AND     C                   
5136: 44              LD      B,H                 
5137: 44              LD      B,H                 
5138: A3              AND     E                   
5139: 44              LD      B,H                 
513A: 01 00 99        LD      BC,$9900            
513D: A3              AND     E                   
513E: 4E              LD      C,(HL)              
513F: A2              AND     D                   
5140: 01 A1 2E        LD      BC,$2EA1            
5143: 2E A2           LD      L,$A2               
5145: 2E 4E           LD      L,$4E               
5147: 4E              LD      C,(HL)              
5148: A1              AND     C                   
5149: 4E              LD      C,(HL)              
514A: 4E              LD      C,(HL)              
514B: A6              AND     (HL)                
514C: 4A              LD      C,D                 
514D: A1              AND     C                   
514E: 4A              LD      C,D                 
514F: A2              AND     D                   
5150: 4A              LD      C,D                 
5151: A1              AND     C                   
5152: 2A              LD      A,(HLI)             
5153: 2A              LD      A,(HLI)             
5154: A2              AND     D                   
5155: 2A              LD      A,(HLI)             
5156: 4A              LD      C,D                 
5157: 4A              LD      C,D                 
5158: A1              AND     C                   
5159: 4A              LD      C,D                 
515A: 4A              LD      C,D                 
515B: A6              AND     (HL)                
515C: 4C              LD      C,H                 
515D: A1              AND     C                   
515E: 4C              LD      C,H                 
515F: A2              AND     D                   
5160: 4C              LD      C,H                 
5161: A1              AND     C                   
5162: 26 26           LD      H,$26               
5164: A2              AND     D                   
5165: 26 4C           LD      H,$4C               
5167: 4C              LD      C,H                 
5168: A1              AND     C                   
5169: 4C              LD      C,H                 
516A: 4C              LD      C,H                 
516B: A2              AND     D                   
516C: 4C              LD      C,H                 
516D: A1              AND     C                   
516E: 44              LD      B,H                 
516F: 44              LD      B,H                 
5170: 9B              SBC     E                   
5171: 02              LD      (BC),A              
5172: A2              AND     D                   
5173: 44              LD      B,H                 
5174: A1              AND     C                   
5175: 44              LD      B,H                 
5176: 44              LD      B,H                 
5177: 9C              SBC     H                   
5178: A2              AND     D                   
5179: 24              INC     H                   
517A: A1              AND     C                   
517B: 28 2C           JR      Z,$51A9             ; {}
517D: 00              NOP                         
517E: 99              SBC     C                   
517F: 9B              SBC     E                   
5180: 02              LD      (BC),A              
5181: A2              AND     D                   
5182: 2E A3           LD      L,$A3               
5184: 46              LD      B,(HL)              
5185: A2              AND     D                   
5186: 46              LD      B,(HL)              
5187: 9C              SBC     H                   
5188: 9B              SBC     E                   
5189: 02              LD      (BC),A              
518A: A2              AND     D                   
518B: 2A              LD      A,(HLI)             
518C: A3              AND     E                   
518D: 42              LD      B,D                 
518E: A2              AND     D                   
518F: 42              LD      B,D                 
5190: 9C              SBC     H                   
5191: 9B              SBC     E                   
5192: 02              LD      (BC),A              
5193: A2              AND     D                   
5194: 26 A3           LD      H,$A3               
5196: 3E A2           LD      A,$A2               
5198: 3E 9C           LD      A,$9C               
519A: 9B              SBC     E                   
519B: 02              LD      (BC),A              
519C: A2              AND     D                   
519D: 34              INC     (HL)                
519E: A3              AND     E                   
519F: 4C              LD      C,H                 
51A0: A2              AND     D                   
51A1: 4C              LD      C,H                 
51A2: 9C              SBC     H                   
51A3: 9B              SBC     E                   
51A4: 02              LD      (BC),A              
51A5: A2              AND     D                   
51A6: 30 A3           JR      NC,$514B            ; {}
51A8: 48              LD      C,B                 
51A9: A2              AND     D                   
51AA: 48              LD      C,B                 
51AB: 9C              SBC     H                   
51AC: 9B              SBC     E                   
51AD: 02              LD      (BC),A              
51AE: A2              AND     D                   
51AF: 2E A3           LD      L,$A3               
51B1: 46              LD      B,(HL)              
51B2: A2              AND     D                   
51B3: 46              LD      B,(HL)              
51B4: 9C              SBC     H                   
51B5: A2              AND     D                   
51B6: 32              LD      (HLD),A             
51B7: A3              AND     E                   
51B8: 4A              LD      C,D                 
51B9: A2              AND     D                   
51BA: 4A              LD      C,D                 
51BB: 32              LD      (HLD),A             
51BC: 4A              LD      C,D                 
51BD: 5E              LD      E,(HL)              
51BE: 32              LD      (HLD),A             
51BF: 3C              INC     A                   
51C0: 9B              SBC     E                   
51C1: 02              LD      (BC),A              
51C2: A1              AND     C                   
51C3: 50              LD      D,B                 
51C4: 50              LD      D,B                 
51C5: A2              AND     D                   
51C6: 50              LD      D,B                 
51C7: 9C              SBC     H                   
51C8: A1              AND     C                   
51C9: 32              LD      (HLD),A             
51CA: 32              LD      (HLD),A             
51CB: A2              AND     D                   
51CC: 32              LD      (HLD),A             
51CD: A1              AND     C                   
51CE: 32              LD      (HLD),A             
51CF: 32              LD      (HLD),A             
51D0: A2              AND     D                   
51D1: 3C              INC     A                   
51D2: 9B              SBC     E                   
51D3: 02              LD      (BC),A              
51D4: A1              AND     C                   
51D5: 50              LD      D,B                 
51D6: 50              LD      D,B                 
51D7: A2              AND     D                   
51D8: 50              LD      D,B                 
51D9: 9C              SBC     H                   
51DA: A1              AND     C                   
51DB: 24              INC     H                   
51DC: 24              INC     H                   
51DD: 24              INC     H                   
51DE: 26 28           LD      H,$28               
51E0: 2C              INC     L                   
51E1: 00              NOP                         
51E2: 00              NOP                         
51E3: 1C              INC     E                   
51E4: 4A              LD      C,D                 
51E5: ED                              
51E6: 51              LD      D,C                 
51E7: 0D              DEC     C                   
51E8: 52              LD      D,D                 
51E9: 21 52 00        LD      HL,$0052            
51EC: 00              NOP                         
51ED: FB              EI                          
51EE: 6E              LD      L,(HL)              
51EF: A5              AND     L                   
51F0: 6F              LD      L,A                 
51F1: 41              LD      B,C                 
51F2: 52              LD      D,D                 
51F3: 41              LD      B,C                 
51F4: 52              LD      D,D                 
51F5: 41              LD      B,C                 
51F6: 52              LD      D,D                 
51F7: 41              LD      B,C                 
51F8: 52              LD      D,D                 
51F9: 41              LD      B,C                 
51FA: 52              LD      D,D                 
51FB: 41              LD      B,C                 
51FC: 52              LD      D,D                 
51FD: 00              NOP                         
51FE: 6F              LD      L,A                 
51FF: AB              XOR     E                   
5200: 6F              LD      L,A                 
5201: 41              LD      B,C                 
5202: 52              LD      D,D                 
5203: 41              LD      B,C                 
5204: 52              LD      D,D                 
5205: 41              LD      B,C                 
5206: 52              LD      D,D                 
5207: 4B              LD      C,E                 
5208: 52              LD      D,D                 
5209: FF              RST     0X38                
520A: FF              RST     0X38                
520B: ED                              
520C: 51              LD      D,C                 
520D: 05              DEC     B                   
520E: 6F              LD      L,A                 
520F: A5              AND     L                   
5210: 6F              LD      L,A                 
5211: 55              LD      D,L                 
5212: 52              LD      D,D                 
5213: 5D              LD      E,L                 
5214: 52              LD      D,D                 
5215: 0A              LD      A,(BC)              
5216: 6F              LD      L,A                 
5217: AB              XOR     E                   
5218: 6F              LD      L,A                 
5219: 5D              LD      E,L                 
521A: 52              LD      D,D                 
521B: 7A              LD      A,D                 
521C: 52              LD      D,D                 
521D: FF              RST     0X38                
521E: FF              RST     0X38                
521F: 0D              DEC     C                   
5220: 52              LD      D,D                 
5221: DC 6E A5        CALL    C,$A56E             
5224: 6F              LD      L,A                 
5225: 7D              LD      A,L                 
5226: 52              LD      D,D                 
5227: 7D              LD      A,L                 
5228: 52              LD      D,D                 
5229: 7D              LD      A,L                 
522A: 52              LD      D,D                 
522B: 7D              LD      A,L                 
522C: 52              LD      D,D                 
522D: 7D              LD      A,L                 
522E: 52              LD      D,D                 
522F: 7D              LD      A,L                 
5230: 52              LD      D,D                 
5231: C2 6E AB        JP      NZ,$AB6E            
5234: 6F              LD      L,A                 
5235: 7D              LD      A,L                 
5236: 52              LD      D,D                 
5237: 7D              LD      A,L                 
5238: 52              LD      D,D                 
5239: 7D              LD      A,L                 
523A: 52              LD      D,D                 
523B: 88              ADC     A,B                 
523C: 52              LD      D,D                 
523D: FF              RST     0X38                
523E: FF              RST     0X38                
523F: 21 52 A7        LD      HL,$A752            
5242: 22              LD      (HLI),A             
5243: A2              AND     D                   
5244: 22              LD      (HLI),A             
5245: A3              AND     E                   
5246: 24              INC     H                   
5247: 22              LD      (HLI),A             
5248: 1E 18           LD      E,$18               
524A: 00              NOP                         
524B: A7              AND     A                   
524C: 22              LD      (HLI),A             
524D: A2              AND     D                   
524E: 22              LD      (HLI),A             
524F: A3              AND     E                   
5250: 24              INC     H                   
5251: 22              LD      (HLI),A             
5252: 1E 01           LD      E,$01               
5254: 00              NOP                         
5255: 9B              SBC     E                   
5256: 03              INC     BC                  
5257: A8              XOR     B                   
5258: 01 9C A4        LD      BC,$A49C            
525B: 01 00 9B        LD      BC,$9B00            
525E: 02              LD      (BC),A              
525F: A1              AND     C                   
5260: 01 40 42        LD      BC,$4240            
5263: 44              LD      B,H                 
5264: A7              AND     A                   
5265: 46              LD      B,(HL)              
5266: A2              AND     D                   
5267: 3A              LD      A,(HLD)             
5268: A4              AND     H                   
5269: 46              LD      B,(HL)              
526A: A1              AND     C                   
526B: 01 44 46        LD      BC,$4644            
526E: 44              LD      B,H                 
526F: A2              AND     D                   
5270: 40              LD      B,B                 
5271: 3C              INC     A                   
5272: A7              AND     A                   
5273: 40              LD      B,B                 
5274: A2              AND     D                   
5275: 32              LD      (HLD),A             
5276: A8              XOR     B                   
5277: 40              LD      B,B                 
5278: 9C              SBC     H                   
5279: 00              NOP                         
527A: A3              AND     E                   
527B: 01 00 99        LD      BC,$9900            
527E: A7              AND     A                   
527F: 32              LD      (HLD),A             
5280: A2              AND     D                   
5281: 32              LD      (HLD),A             
5282: A3              AND     E                   
5283: 34              INC     (HL)                
5284: 32              LD      (HLD),A             
5285: 2E 28           LD      L,$28               
5287: 00              NOP                         
5288: 99              SBC     C                   
5289: A7              AND     A                   
528A: 32              LD      (HLD),A             
528B: A2              AND     D                   
528C: 32              LD      (HLD),A             
528D: A3              AND     E                   
528E: 34              INC     (HL)                
528F: 32              LD      (HLD),A             
5290: 2E 01           LD      L,$01               
5292: 00              NOP                         
5293: 00              NOP                         
5294: 58              LD      E,B                 
5295: 4A              LD      C,D                 
5296: 9E              SBC     (HL)                
5297: 52              LD      D,D                 
5298: A4              AND     H                   
5299: 52              LD      D,D                 
529A: AC              XOR     H                   
529B: 52              LD      D,D                 
529C: 00              NOP                         
529D: 00              NOP                         
529E: EB                              
529F: 52              LD      D,D                 
52A0: FF              RST     0X38                
52A1: FF              RST     0X38                
52A2: 9E              SBC     (HL)                
52A3: 52              LD      D,D                 
52A4: B6              OR      (HL)                
52A5: 52              LD      D,D                 
52A6: BB              CP      E                   
52A7: 52              LD      D,D                 
52A8: FF              RST     0X38                
52A9: FF              RST     0X38                
52AA: A4              AND     H                   
52AB: 52              LD      D,D                 
52AC: FB              EI                          
52AD: 6F              LD      L,A                 
52AE: 27              DAA                         
52AF: 53              LD      D,E                 
52B0: BB              CP      E                   
52B1: 52              LD      D,D                 
52B2: FF              RST     0X38                
52B3: FF              RST     0X38                
52B4: AE              XOR     (HL)                
52B5: 52              LD      D,D                 
52B6: 9D              SBC     L                   
52B7: 57              LD      D,A                 
52B8: 00              NOP                         
52B9: 80              ADD     A,B                 
52BA: 00              NOP                         
52BB: A2              AND     D                   
52BC: 78              LD      A,B                 
52BD: 7C              LD      A,H                 
52BE: A3              AND     E                   
52BF: 7E              LD      A,(HL)              
52C0: 01 01 A2        LD      BC,$A201            
52C3: 78              LD      A,B                 
52C4: 7C              LD      A,H                 
52C5: A3              AND     E                   
52C6: 7E              LD      A,(HL)              
52C7: 01 01 A2        LD      BC,$A201            
52CA: 7C              LD      A,H                 
52CB: 78              LD      A,B                 
52CC: 6E              LD      L,(HL)              
52CD: A7              AND     A                   
52CE: 74              LD      (HL),H              
52CF: A3              AND     E                   
52D0: 78              LD      A,B                 
52D1: 01 A8 01        LD      BC,$01A8            
52D4: A2              AND     D                   
52D5: 78              LD      A,B                 
52D6: 7C              LD      A,H                 
52D7: A3              AND     E                   
52D8: 7E              LD      A,(HL)              
52D9: 01 01 A2        LD      BC,$A201            
52DC: 78              LD      A,B                 
52DD: 7E              LD      A,(HL)              
52DE: A3              AND     E                   
52DF: 88              ADC     A,B                 
52E0: 01 01 A2        LD      BC,$A201            
52E3: 86              ADD     A,(HL)              
52E4: 82              ADD     A,D                 
52E5: A4              AND     H                   
52E6: 86              ADD     A,(HL)              
52E7: 01 A8 01        LD      BC,$01A8            
52EA: 00              NOP                         
52EB: 9D              SBC     L                   
52EC: 37              SCF                         
52ED: 00              NOP                         
52EE: 80              ADD     A,B                 
52EF: A7              AND     A                   
52F0: 01 9B 02        LD      BC,$029B            
52F3: A2              AND     D                   
52F4: 40              LD      B,B                 
52F5: 4E              LD      C,(HL)              
52F6: 58              LD      E,B                 
52F7: 5C              LD      E,H                 
52F8: A3              AND     E                   
52F9: 60              LD      H,B                 
52FA: 01 9C A2        LD      BC,$A29C            
52FD: 48              LD      C,B                 
52FE: 56              LD      D,(HL)              
52FF: 5C              LD      E,H                 
5300: 6A              LD      L,D                 
5301: A3              AND     E                   
5302: 6E              LD      L,(HL)              
5303: 01 A2 48        LD      BC,$48A2            
5306: 56              LD      D,(HL)              
5307: 5C              LD      E,H                 
5308: 56              LD      D,(HL)              
5309: 44              LD      B,H                 
530A: 56              LD      D,(HL)              
530B: 5C              LD      E,H                 
530C: 56              LD      D,(HL)              
530D: 9B              SBC     E                   
530E: 02              LD      (BC),A              
530F: A2              AND     D                   
5310: 40              LD      B,B                 
5311: 4E              LD      C,(HL)              
5312: 58              LD      E,B                 
5313: 5C              LD      E,H                 
5314: A3              AND     E                   
5315: 60              LD      H,B                 
5316: 01 9C A2        LD      BC,$A29C            
5319: 36 44           LD      (HL),$44            
531B: 4C              LD      C,H                 
531C: 52              LD      D,D                 
531D: 56              LD      D,(HL)              
531E: 5C              LD      E,H                 
531F: 64              LD      H,H                 
5320: 6A              LD      L,D                 
5321: 6E              LD      L,(HL)              
5322: 6A              LD      L,D                 
5323: 6E              LD      L,(HL)              
5324: 74              LD      (HL),H              
5325: 8C              ADC     A,H                 
5326: 00              NOP                         
5327: 9D              SBC     L                   
5328: A2              AND     D                   
5329: 6E              LD      L,(HL)              
532A: 20 00           JR      NZ,$532C            ; {}
532C: 00              NOP                         
532D: 67              LD      H,A                 
532E: 4A              LD      C,D                 
532F: 37              SCF                         
5330: 53              LD      D,E                 
5331: 3D              DEC     A                   
5332: 53              LD      D,E                 
5333: 8C              ADC     A,H                 
5334: 4A              LD      C,D                 
5335: 00              NOP                         
5336: 00              NOP                         
5337: 43              LD      B,E                 
5338: 53              LD      D,E                 
5339: FF              RST     0X38                
533A: FF              RST     0X38                
533B: 37              SCF                         
533C: 53              LD      D,E                 
533D: A5              AND     L                   
533E: 53              LD      D,E                 
533F: FF              RST     0X38                
5340: FF              RST     0X38                
5341: 3D              DEC     A                   
5342: 53              LD      D,E                 
5343: 9D              SBC     L                   
5344: 52              LD      D,D                 
5345: 00              NOP                         
5346: 80              ADD     A,B                 
5347: 99              SBC     C                   
5348: 9B              SBC     E                   
5349: 02              LD      (BC),A              
534A: A2              AND     D                   
534B: 40              LD      B,B                 
534C: 4E              LD      C,(HL)              
534D: 9C              SBC     H                   
534E: 9B              SBC     E                   
534F: 02              LD      (BC),A              
5350: 40              LD      B,B                 
5351: 52              LD      D,D                 
5352: 9C              SBC     H                   
5353: 9B              SBC     E                   
5354: 02              LD      (BC),A              
5355: 40              LD      B,B                 
5356: 56              LD      D,(HL)              
5357: 9C              SBC     H                   
5358: 9B              SBC     E                   
5359: 02              LD      (BC),A              
535A: 40              LD      B,B                 
535B: 52              LD      D,D                 
535C: 9C              SBC     H                   
535D: 9B              SBC     E                   
535E: 02              LD      (BC),A              
535F: 40              LD      B,B                 
5360: 4E              LD      C,(HL)              
5361: 9C              SBC     H                   
5362: 9B              SBC     E                   
5363: 02              LD      (BC),A              
5364: 40              LD      B,B                 
5365: 50              LD      D,B                 
5366: 9C              SBC     H                   
5367: 9B              SBC     E                   
5368: 02              LD      (BC),A              
5369: 44              LD      B,H                 
536A: 52              LD      D,D                 
536B: 9C              SBC     H                   
536C: 4E              LD      C,(HL)              
536D: 36 3A           LD      (HL),$3A            
536F: 36 9B           LD      (HL),$9B            
5371: 02              LD      (BC),A              
5372: 32              LD      (HLD),A             
5373: 40              LD      B,B                 
5374: 9C              SBC     H                   
5375: 9B              SBC     E                   
5376: 02              LD      (BC),A              
5377: 32              LD      (HLD),A             
5378: 44              LD      B,H                 
5379: 9C              SBC     H                   
537A: 9B              SBC     E                   
537B: 02              LD      (BC),A              
537C: 30 44           JR      NC,$53C2            ; {}
537E: 9C              SBC     H                   
537F: 9B              SBC     E                   
5380: 02              LD      (BC),A              
5381: 3A              LD      A,(HLD)             
5382: 48              LD      C,B                 
5383: 9C              SBC     H                   
5384: 9B              SBC     E                   
5385: 02              LD      (BC),A              
5386: 2C              INC     L                   
5387: 3A              LD      A,(HLD)             
5388: 9C              SBC     H                   
5389: 2C              INC     L                   
538A: 38 36           JR      C,$53C2             ; {}
538C: 32              LD      (HLD),A             
538D: 9D              SBC     L                   
538E: 40              LD      B,B                 
538F: 00              NOP                         
5390: 80              ADD     A,B                 
5391: A4              AND     H                   
5392: 36 32           LD      (HL),$32            
5394: 9E              SBC     (HL)                
5395: 76              HALT                        
5396: 4A              LD      C,D                 
5397: A4              AND     H                   
5398: 30 A7           JR      NC,$5341            ; {}
539A: 2C              INC     L                   
539B: 9D              SBC     L                   
539C: 52              LD      D,D                 
539D: 00              NOP                         
539E: 80              ADD     A,B                 
539F: A2              AND     D                   
53A0: 36 9E           LD      (HL),$9E            
53A2: 67              LD      H,A                 
53A3: 4A              LD      C,D                 
53A4: 00              NOP                         
53A5: 9D              SBC     L                   
53A6: 56              LD      D,(HL)              
53A7: 00              NOP                         
53A8: 80              ADD     A,B                 
53A9: A3              AND     E                   
53AA: 66              LD      H,(HL)              
53AB: 58              LD      E,B                 
53AC: A7              AND     A                   
53AD: 5C              LD      E,H                 
53AE: A1              AND     C                   
53AF: 60              LD      H,B                 
53B0: 62              LD      H,D                 
53B1: A2              AND     D                   
53B2: 66              LD      H,(HL)              
53B3: 66              LD      H,(HL)              
53B4: 58              LD      E,B                 
53B5: 58              LD      E,B                 
53B6: A7              AND     A                   
53B7: 5C              LD      E,H                 
53B8: A1              AND     C                   
53B9: 60              LD      H,B                 
53BA: 62              LD      H,D                 
53BB: A2              AND     D                   
53BC: 60              LD      H,B                 
53BD: 66              LD      H,(HL)              
53BE: A7              AND     A                   
53BF: 74              LD      (HL),H              
53C0: A2              AND     D                   
53C1: 70              LD      (HL),B              
53C2: 74              LD      (HL),H              
53C3: 70              LD      (HL),B              
53C4: 66              LD      H,(HL)              
53C5: A1              AND     C                   
53C6: 62              LD      H,D                 
53C7: 60              LD      H,B                 
53C8: A3              AND     E                   
53C9: 5C              LD      E,H                 
53CA: 9D              SBC     L                   
53CB: 42              LD      B,D                 
53CC: 00              NOP                         
53CD: 80              ADD     A,B                 
53CE: 56              LD      D,(HL)              
53CF: 9D              SBC     L                   
53D0: 56              LD      D,(HL)              
53D1: 00              NOP                         
53D2: 80              ADD     A,B                 
53D3: A1              AND     C                   
53D4: 01 60 62        LD      BC,$6260            
53D7: 66              LD      H,(HL)              
53D8: A3              AND     E                   
53D9: 6A              LD      L,D                 
53DA: 58              LD      E,B                 
53DB: A7              AND     A                   
53DC: 56              LD      D,(HL)              
53DD: A1              AND     C                   
53DE: 5C              LD      E,H                 
53DF: 6A              LD      L,D                 
53E0: A2              AND     D                   
53E1: 66              LD      H,(HL)              
53E2: 66              LD      H,(HL)              
53E3: 56              LD      D,(HL)              
53E4: 56              LD      D,(HL)              
53E5: A7              AND     A                   
53E6: 58              LD      E,B                 
53E7: A1              AND     C                   
53E8: 58              LD      E,B                 
53E9: 56              LD      D,(HL)              
53EA: A2              AND     D                   
53EB: 52              LD      D,D                 
53EC: 58              LD      E,B                 
53ED: A7              AND     A                   
53EE: 60              LD      H,B                 
53EF: A2              AND     D                   
53F0: 5C              LD      E,H                 
53F1: 58              LD      E,B                 
53F2: 50              LD      D,B                 
53F3: 9B              SBC     E                   
53F4: 04              INC     B                   
53F5: 4E              LD      C,(HL)              
53F6: 66              LD      H,(HL)              
53F7: 9C              SBC     H                   
53F8: 9E              SBC     (HL)                
53F9: 76              HALT                        
53FA: 4A              LD      C,D                 
53FB: 9B              SBC     E                   
53FC: 04              INC     B                   
53FD: A2              AND     D                   
53FE: 66              LD      H,(HL)              
53FF: 7E              LD      A,(HL)              
5400: 9C              SBC     H                   
5401: 9E              SBC     (HL)                
5402: 67              LD      H,A                 
5403: 4A              LD      C,D                 
5404: 00              NOP                         
5405: 00              NOP                         
5406: 3A              LD      A,(HLD)             
5407: 4A              LD      C,D                 
5408: 10 54           ;;STOP    $54                 
540A: 1E 54           LD      E,$54               
540C: 2C              INC     L                   
540D: 54              LD      D,H                 
540E: 00              NOP                         
540F: 00              NOP                         
5410: 46              LD      B,(HL)              
5411: 54              LD      D,H                 
5412: 71              LD      (HL),C              
5413: 54              LD      D,H                 
5414: BC              CP      H                   
5415: 54              LD      D,H                 
5416: 71              LD      (HL),C              
5417: 54              LD      D,H                 
5418: E9              JP      (HL)                
5419: 54              LD      D,H                 
541A: FF              RST     0X38                
541B: FF              RST     0X38                
541C: 12              LD      (DE),A              
541D: 54              LD      D,H                 
541E: 62              LD      H,D                 
541F: 55              LD      D,L                 
5420: 8F              ADC     A,A                 
5421: 55              LD      D,L                 
5422: C4 55 8F        CALL    NZ,$8F55            
5425: 55              LD      D,L                 
5426: E8 55           ADD     SP,$55              
5428: FF              RST     0X38                
5429: FF              RST     0X38                
542A: 20 54           JR      NZ,$5480            ; {}
542C: C2 6E 64        JP      NZ,$646E            ; {}
542F: 56              LD      D,(HL)              
5430: C2 6E 8D        JP      NZ,$8D6E            
5433: 56              LD      D,(HL)              
5434: AF              XOR     A                   
5435: 56              LD      D,(HL)              
5436: 8D              ADC     A,L                 
5437: 56              LD      D,(HL)              
5438: DD                              
5439: 56              LD      D,(HL)              
543A: C7              RST     0X00                
543B: 6E              LD      L,(HL)              
543C: EA 56 C2        LD      ($C256),A           
543F: 6E              LD      L,(HL)              
5440: F7              RST     0X30                
5441: 56              LD      D,(HL)              
5442: FF              RST     0X38                
5443: FF              RST     0X38                
5444: 30 54           JR      NC,$549A            ; {}
5446: 9D              SBC     L                   
5447: 45              LD      B,L                 
5448: 00              NOP                         
5449: 80              ADD     A,B                 
544A: A3              AND     E                   
544B: 30 AA           JR      NC,$53F7            ; {}
544D: 30 30           JR      NC,$547F            ; {}
544F: 30 A3           JR      NC,$53F4            ; {}
5451: 2C              INC     L                   
5452: AA              XOR     D                   
5453: 2C              INC     L                   
5454: 30 32           JR      NC,$5488            ; {}
5456: A3              AND     E                   
5457: 38 AA           JR      C,$5403             ; {}
5459: 38 38           JR      C,$5493             ; {}
545B: 38 A3           JR      C,$5400             ; {}
545D: 3C              INC     A                   
545E: AA              XOR     D                   
545F: 3C              INC     A                   
5460: 3C              INC     A                   
5461: 3C              INC     A                   
5462: 9D              SBC     L                   
5463: 40              LD      B,B                 
5464: 21 81 A8        LD      HL,$A881            
5467: 40              LD      B,B                 
5468: AA              XOR     D                   
5469: 3C              INC     A                   
546A: 3C              INC     A                   
546B: 3C              INC     A                   
546C: A8              XOR     B                   
546D: 40              LD      B,B                 
546E: A3              AND     E                   
546F: 01 00 9D        LD      BC,$9D00            
5472: 45              LD      B,L                 
5473: 00              NOP                         
5474: 80              ADD     A,B                 
5475: A3              AND     E                   
5476: 30 AA           JR      NC,$5422            ; {}
5478: 32              LD      (HLD),A             
5479: 30 2C           JR      NC,$54A7            ; {}
547B: A6              AND     (HL)                
547C: 30 A1           JR      NC,$541F            ; {}
547E: 30 30           JR      NC,$54B0            ; {}
5480: 32              LD      (HLD),A             
5481: 36 3A           LD      (HL),$3A            
5483: A6              AND     (HL)                
5484: 3C              INC     A                   
5485: A1              AND     C                   
5486: 40              LD      B,B                 
5487: 40              LD      B,B                 
5488: 44              LD      B,H                 
5489: 48              LD      C,B                 
548A: 4A              LD      C,D                 
548B: A3              AND     E                   
548C: 4E              LD      C,(HL)              
548D: AA              XOR     D                   
548E: 3C              INC     A                   
548F: 40              LD      B,B                 
5490: 44              LD      B,H                 
5491: A6              AND     (HL)                
5492: 46              LD      B,(HL)              
5493: A1              AND     C                   
5494: 38 38           JR      C,$54CE             ; {}
5496: 3C              INC     A                   
5497: 40              LD      B,B                 
5498: 44              LD      B,H                 
5499: AA              XOR     D                   
549A: 46              LD      B,(HL)              
549B: 01 46 46        LD      BC,$4646            
549E: 44              LD      B,H                 
549F: 40              LD      B,B                 
54A0: 46              LD      B,(HL)              
54A1: 01 3C 3C        LD      BC,$3C3C            
54A4: 3C              INC     A                   
54A5: 38 3C           JR      C,$54E3             ; {}
54A7: 01 3C 3C        LD      BC,$3C3C            
54AA: 38 3C           JR      C,$54E8             ; {}
54AC: A2              AND     D                   
54AD: 38 A1           JR      C,$5450             ; {}
54AF: 38 36           JR      C,$54E7             ; {}
54B1: A2              AND     D                   
54B2: 38 A1           JR      C,$5455             ; {}
54B4: 38 3C           JR      C,$54F2             ; {}
54B6: A3              AND     E                   
54B7: 40              LD      B,B                 
54B8: A2              AND     D                   
54B9: 3C              INC     A                   
54BA: 38 00           JR      C,$54BC             ; {}
54BC: A2              AND     D                   
54BD: 36 A1           LD      (HL),$A1            
54BF: 36 32           LD      (HL),$32            
54C1: A2              AND     D                   
54C2: 36 A1           LD      (HL),$A1            
54C4: 36 38           LD      (HL),$38            
54C6: A3              AND     E                   
54C7: 3C              INC     A                   
54C8: A2              AND     D                   
54C9: 38 36           JR      C,$5501             ; {}
54CB: A3              AND     E                   
54CC: 34              INC     (HL)                
54CD: A2              AND     D                   
54CE: 34              INC     (HL)                
54CF: A1              AND     C                   
54D0: 34              INC     (HL)                
54D1: 36 A2           LD      (HL),$A2            
54D3: 3A              LD      A,(HLD)             
54D4: A1              AND     C                   
54D5: 3A              LD      A,(HLD)             
54D6: 3C              INC     A                   
54D7: 40              LD      B,B                 
54D8: 44              LD      B,H                 
54D9: 46              LD      B,(HL)              
54DA: 4A              LD      C,D                 
54DB: A3              AND     E                   
54DC: 44              LD      B,H                 
54DD: 9D              SBC     L                   
54DE: 40              LD      B,B                 
54DF: 21 41 AA        LD      HL,$AA41            
54E2: 32              LD      (HLD),A             
54E3: 32              LD      (HLD),A             
54E4: 32              LD      (HLD),A             
54E5: A3              AND     E                   
54E6: 36 01           LD      (HL),$01            
54E8: 00              NOP                         
54E9: 9D              SBC     L                   
54EA: 45              LD      B,L                 
54EB: 00              NOP                         
54EC: 80              ADD     A,B                 
54ED: AA              XOR     D                   
54EE: 36 34           LD      (HL),$34            
54F0: 36 3E           LD      (HL),$3E            
54F2: 40              LD      B,B                 
54F3: 44              LD      B,H                 
54F4: 46              LD      B,(HL)              
54F5: 01 46 46        LD      BC,$4646            
54F8: 44              LD      B,H                 
54F9: 40              LD      B,B                 
54FA: 9D              SBC     L                   
54FB: 70              LD      (HL),B              
54FC: 21 80 A6        LD      HL,$A680            
54FF: 4E              LD      C,(HL)              
5500: 46              LD      B,(HL)              
5501: A2              AND     D                   
5502: 40              LD      B,B                 
5503: A3              AND     E                   
5504: 3E AA           LD      A,$AA               
5506: 3E 3A           LD      A,$3A               
5508: 3E AA           LD      A,$AA               
550A: 40              LD      B,B                 
550B: 44              LD      B,H                 
550C: 46              LD      B,(HL)              
550D: 4A              LD      C,D                 
550E: 46              LD      B,(HL)              
550F: 44              LD      B,H                 
5510: A3              AND     E                   
5511: 46              LD      B,(HL)              
5512: 01 9D 50        LD      BC,$509D            
5515: 21 81 A3        LD      HL,$A381            
5518: 46              LD      B,(HL)              
5519: A7              AND     A                   
551A: 40              LD      B,B                 
551B: A1              AND     C                   
551C: 01 46 46        LD      BC,$4646            
551F: 4A              LD      C,D                 
5520: 4E              LD      C,(HL)              
5521: 50              LD      D,B                 
5522: AA              XOR     D                   
5523: 4A              LD      C,D                 
5524: 01 46 A4        LD      BC,$A446            
5527: 44              LD      B,H                 
5528: A3              AND     E                   
5529: 3C              INC     A                   
552A: AA              XOR     D                   
552B: 40              LD      B,B                 
552C: 01 36 A3        LD      BC,$A336            
552F: 36 32           LD      (HL),$32            
5531: 3A              LD      A,(HLD)             
5532: A2              AND     D                   
5533: 40              LD      B,B                 
5534: A1              AND     C                   
5535: 40              LD      B,B                 
5536: 3E 40           LD      A,$40               
5538: 44              LD      B,H                 
5539: 46              LD      B,(HL)              
553A: 4A              LD      C,D                 
553B: A4              AND     H                   
553C: 4E              LD      C,(HL)              
553D: AA              XOR     D                   
553E: 4E              LD      C,(HL)              
553F: 01 4A A4        LD      BC,$A44A            
5542: 46              LD      B,(HL)              
5543: A3              AND     E                   
5544: 01 AA 4A        LD      BC,$4AAA            
5547: 01 50 A4        LD      BC,$A450            
554A: 5A              LD      E,D                 
554B: A3              AND     E                   
554C: 01 01 AA        LD      BC,$AA01            
554F: 40              LD      B,B                 
5550: 40              LD      B,B                 
5551: 40              LD      B,B                 
5552: A3              AND     E                   
5553: 40              LD      B,B                 
5554: 01 9D 40        LD      BC,$409D            
5557: 21 40 01        LD      HL,$0140            
555A: AA              XOR     D                   
555B: 4A              LD      C,D                 
555C: 4A              LD      C,D                 
555D: 4A              LD      C,D                 
555E: A3              AND     E                   
555F: 4E              LD      C,(HL)              
5560: 01 00 9D        LD      BC,$9D00            
5563: 55              LD      D,L                 
5564: 00              NOP                         
5565: 80              ADD     A,B                 
5566: A3              AND     E                   
5567: 40              LD      B,B                 
5568: AA              XOR     D                   
5569: 40              LD      B,B                 
556A: 36 40           LD      (HL),$40            
556C: A3              AND     E                   
556D: 3C              INC     A                   
556E: AA              XOR     D                   
556F: 3C              INC     A                   
5570: 40              LD      B,B                 
5571: 44              LD      B,H                 
5572: A3              AND     E                   
5573: 46              LD      B,(HL)              
5574: AA              XOR     D                   
5575: 46              LD      B,(HL)              
5576: 40              LD      B,B                 
5577: 46              LD      B,(HL)              
5578: A3              AND     E                   
5579: 44              LD      B,H                 
557A: AA              XOR     D                   
557B: 44              LD      B,H                 
557C: 46              LD      B,(HL)              
557D: 4A              LD      C,D                 
557E: 9D              SBC     L                   
557F: 50              LD      D,B                 
5580: 21 81 A8        LD      HL,$A881            
5583: 4E              LD      C,(HL)              
5584: AA              XOR     D                   
5585: 4A              LD      C,D                 
5586: 4A              LD      C,D                 
5587: 4A              LD      C,D                 
5588: A8              XOR     B                   
5589: 4E              LD      C,(HL)              
558A: AA              XOR     D                   
558B: 4A              LD      C,D                 
558C: 48              LD      C,B                 
558D: 44              LD      B,H                 
558E: 00              NOP                         
558F: 9D              SBC     L                   
5590: 65              LD      H,L                 
5591: 00              NOP                         
5592: 80              ADD     A,B                 
5593: A3              AND     E                   
5594: 40              LD      B,B                 
5595: A7              AND     A                   
5596: 36 A1           LD      (HL),$A1            
5598: 01 40 40        LD      BC,$4040            
559B: 44              LD      B,H                 
559C: 48              LD      C,B                 
559D: 4A              LD      C,D                 
559E: A4              AND     H                   
559F: 4E              LD      C,(HL)              
55A0: AA              XOR     D                   
55A1: 01 01 4E        LD      BC,$4E01            
55A4: 4E              LD      C,(HL)              
55A5: 50              LD      D,B                 
55A6: 54              LD      D,H                 
55A7: A4              AND     H                   
55A8: 58              LD      E,B                 
55A9: AA              XOR     D                   
55AA: 01 01 58        LD      BC,$5801            
55AD: 58              LD      E,B                 
55AE: 54              LD      D,H                 
55AF: 50              LD      D,B                 
55B0: 54              LD      D,H                 
55B1: 01 50 A4        LD      BC,$A450            
55B4: 4E              LD      C,(HL)              
55B5: AA              XOR     D                   
55B6: 4E              LD      C,(HL)              
55B7: 50              LD      D,B                 
55B8: 4E              LD      C,(HL)              
55B9: A2              AND     D                   
55BA: 4A              LD      C,D                 
55BB: A1              AND     C                   
55BC: 4A              LD      C,D                 
55BD: 4E              LD      C,(HL)              
55BE: A4              AND     H                   
55BF: 50              LD      D,B                 
55C0: A2              AND     D                   
55C1: 4E              LD      C,(HL)              
55C2: 4A              LD      C,D                 
55C3: 00              NOP                         
55C4: A2              AND     D                   
55C5: 46              LD      B,(HL)              
55C6: A1              AND     C                   
55C7: 46              LD      B,(HL)              
55C8: 4A              LD      C,D                 
55C9: A4              AND     H                   
55CA: 4E              LD      C,(HL)              
55CB: A2              AND     D                   
55CC: 4A              LD      C,D                 
55CD: 46              LD      B,(HL)              
55CE: 44              LD      B,H                 
55CF: A1              AND     C                   
55D0: 44              LD      B,H                 
55D1: 48              LD      C,B                 
55D2: A4              AND     H                   
55D3: 4C              LD      C,H                 
55D4: A3              AND     E                   
55D5: 52              LD      D,D                 
55D6: A2              AND     D                   
55D7: 4E              LD      C,(HL)              
55D8: 9D              SBC     L                   
55D9: 60              LD      H,B                 
55DA: 21 01 AD        LD      HL,$AD01            
55DD: 36 36           LD      (HL),$36            
55DF: 36 AA           LD      (HL),$AA            
55E1: 3A              LD      A,(HLD)             
55E2: 3A              LD      A,(HLD)             
55E3: 3A              LD      A,(HLD)             
55E4: A3              AND     E                   
55E5: 3E 01           LD      A,$01               
55E7: 00              NOP                         
55E8: 9D              SBC     L                   
55E9: 45              LD      B,L                 
55EA: 00              NOP                         
55EB: 80              ADD     A,B                 
55EC: AA              XOR     D                   
55ED: 46              LD      B,(HL)              
55EE: 44              LD      B,H                 
55EF: 46              LD      B,(HL)              
55F0: 4A              LD      C,D                 
55F1: 46              LD      B,(HL)              
55F2: 4A              LD      C,D                 
55F3: 4E              LD      C,(HL)              
55F4: 01 4E 4E        LD      BC,$4E4E            
55F7: 4A              LD      C,D                 
55F8: 46              LD      B,(HL)              
55F9: 9D              SBC     L                   
55FA: 40              LD      B,B                 
55FB: 00              NOP                         
55FC: 81              ADD     A,C                 
55FD: A4              AND     H                   
55FE: 4E              LD      C,(HL)              
55FF: 66              LD      H,(HL)              
5600: A8              XOR     B                   
5601: 58              LD      E,B                 
5602: 9D              SBC     L                   
5603: 70              LD      (HL),B              
5604: 21 41 AA        LD      HL,$AA41            
5607: 4E              LD      C,(HL)              
5608: 50              LD      D,B                 
5609: 54              LD      D,H                 
560A: A3              AND     E                   
560B: 58              LD      E,B                 
560C: A7              AND     A                   
560D: 4E              LD      C,(HL)              
560E: A1              AND     C                   
560F: 01 58 58        LD      BC,$5858            
5612: 5C              LD      E,H                 
5613: 5E              LD      E,(HL)              
5614: 62              LD      H,D                 
5615: AA              XOR     D                   
5616: 5C              LD      E,H                 
5617: 01 54 A7        LD      BC,$A754            
561A: 4A              LD      C,D                 
561B: A1              AND     C                   
561C: 4A              LD      C,D                 
561D: 4E              LD      C,(HL)              
561E: 54              LD      D,H                 
561F: 50              LD      D,B                 
5620: 4E              LD      C,(HL)              
5621: 4A              LD      C,D                 
5622: AA              XOR     D                   
5623: 4E              LD      C,(HL)              
5624: 01 40 A7        LD      BC,$A740            
5627: 40              LD      B,B                 
5628: A1              AND     C                   
5629: 40              LD      B,B                 
562A: 3E 40           LD      A,$40               
562C: 44              LD      B,H                 
562D: 46              LD      B,(HL)              
562E: 4A              LD      C,D                 
562F: A4              AND     H                   
5630: 4E              LD      C,(HL)              
5631: A3              AND     E                   
5632: 01 AA 4E        LD      BC,$4EAA            
5635: 4A              LD      C,D                 
5636: 4E              LD      C,(HL)              
5637: AA              XOR     D                   
5638: 5E              LD      E,(HL)              
5639: 01 5C A3        LD      BC,$A35C            
563C: 58              LD      E,B                 
563D: AA              XOR     D                   
563E: 01 4E 4E        LD      BC,$4E4E            
5641: 4E              LD      C,(HL)              
5642: 46              LD      B,(HL)              
5643: 58              LD      E,B                 
5644: 5A              LD      E,D                 
5645: 01 5E A3        LD      BC,$A35E            
5648: 62              LD      H,D                 
5649: AA              XOR     D                   
564A: 01 62 66        LD      BC,$6662            
564D: 68              LD      L,B                 
564E: 6C              LD      L,H                 
564F: 68              LD      L,B                 
5650: A5              AND     L                   
5651: 66              LD      H,(HL)              
5652: 9D              SBC     L                   
5653: 40              LD      B,B                 
5654: 21 40 A2        LD      HL,$A240            
5657: 01 AD 4E        LD      BC,$4EAD            
565A: 4E              LD      C,(HL)              
565B: 4E              LD      C,(HL)              
565C: AA              XOR     D                   
565D: 52              LD      D,D                 
565E: 52              LD      D,D                 
565F: 52              LD      D,D                 
5660: A3              AND     E                   
5661: 56              LD      D,(HL)              
5662: 01 00 99        LD      BC,$9900            
5665: A3              AND     E                   
5666: 40              LD      B,B                 
5667: AA              XOR     D                   
5668: 40              LD      B,B                 
5669: 40              LD      B,B                 
566A: 40              LD      B,B                 
566B: A3              AND     E                   
566C: 3C              INC     A                   
566D: AA              XOR     D                   
566E: 3C              INC     A                   
566F: 3C              INC     A                   
5670: 3C              INC     A                   
5671: A3              AND     E                   
5672: 38 AA           JR      C,$561E             ; {}
5674: 38 38           JR      C,$56AE             ; {}
5676: 38 3C           JR      C,$56B4             ; {}
5678: 3C              INC     A                   
5679: 3C              INC     A                   
567A: 3C              INC     A                   
567B: 38 3C           JR      C,$56B9             ; {}
567D: 9B              SBC     E                   
567E: 02              LD      (BC),A              
567F: A3              AND     E                   
5680: 40              LD      B,B                 
5681: AA              XOR     D                   
5682: 40              LD      B,B                 
5683: 40              LD      B,B                 
5684: 40              LD      B,B                 
5685: A3              AND     E                   
5686: 40              LD      B,B                 
5687: AA              XOR     D                   
5688: 36 36           LD      (HL),$36            
568A: 36 9C           LD      (HL),$9C            
568C: 00              NOP                         
568D: A3              AND     E                   
568E: 28 AA           JR      Z,$563A             ; {}
5690: 28 28           JR      Z,$56BA             ; {}
5692: 24              INC     H                   
5693: A3              AND     E                   
5694: 28 28           JR      Z,$56BE             ; {}
5696: 24              INC     H                   
5697: AA              XOR     D                   
5698: 24              INC     H                   
5699: 24              INC     H                   
569A: 20 A3           JR      NZ,$563F            ; {}
569C: 24              INC     H                   
569D: 24              INC     H                   
569E: 20 AA           JR      NZ,$564A            ; {}
56A0: 20 20           JR      NZ,$56C2            ; {}
56A2: 1E A3           LD      E,$A3               
56A4: 20 20           JR      NZ,$56C6            ; {}
56A6: 2E AA           LD      L,$AA               
56A8: 2E 2E           LD      L,$2E               
56AA: 2A              LD      A,(HLI)             
56AB: A3              AND     E                   
56AC: 2E 2E           LD      L,$2E               
56AE: 00              NOP                         
56AF: 2A              LD      A,(HLI)             
56B0: AA              XOR     D                   
56B1: 2A              LD      A,(HLI)             
56B2: 2A              LD      A,(HLI)             
56B3: 28 A3           JR      Z,$5658             ; {}
56B5: 2A              LD      A,(HLI)             
56B6: AA              XOR     D                   
56B7: 2A              LD      A,(HLI)             
56B8: 2A              LD      A,(HLI)             
56B9: 2A              LD      A,(HLI)             
56BA: A3              AND     E                   
56BB: 28 AA           JR      Z,$5667             ; {}
56BD: 28 28           JR      Z,$56E7             ; {}
56BF: 24              INC     H                   
56C0: A3              AND     E                   
56C1: 28 AA           JR      Z,$566D             ; {}
56C3: 28 28           JR      Z,$56ED             ; {}
56C5: 28 9B           JR      Z,$5662             ; {}
56C7: 02              LD      (BC),A              
56C8: A3              AND     E                   
56C9: 2C              INC     L                   
56CA: AA              XOR     D                   
56CB: 2C              INC     L                   
56CC: 2C              INC     L                   
56CD: 2C              INC     L                   
56CE: 9C              SBC     H                   
56CF: A3              AND     E                   
56D0: 36 AA           LD      (HL),$AA            
56D2: 40              LD      B,B                 
56D3: 40              LD      B,B                 
56D4: 40              LD      B,B                 
56D5: 9A              SBC     D                   
56D6: A3              AND     E                   
56D7: 44              LD      B,H                 
56D8: 99              SBC     C                   
56D9: A2              AND     D                   
56DA: 22              LD      (HLI),A             
56DB: 26 00           LD      H,$00               
56DD: A3              AND     E                   
56DE: 2A              LD      A,(HLI)             
56DF: AA              XOR     D                   
56E0: 42              LD      B,D                 
56E1: 42              LD      B,D                 
56E2: 40              LD      B,B                 
56E3: A3              AND     E                   
56E4: 42              LD      B,D                 
56E5: AA              XOR     D                   
56E6: 42              LD      B,D                 
56E7: 42              LD      B,D                 
56E8: 42              LD      B,D                 
56E9: 00              NOP                         
56EA: 9A              SBC     D                   
56EB: A3              AND     E                   
56EC: 40              LD      B,B                 
56ED: 3E A4           LD      A,$A4               
56EF: 3C              INC     A                   
56F0: A3              AND     E                   
56F1: 3A              LD      A,(HLD)             
56F2: 32              LD      (HLD),A             
56F3: 99              SBC     C                   
56F4: A3              AND     E                   
56F5: 36 00           LD      (HL),$00            
56F7: AA              XOR     D                   
56F8: 36 4E           LD      (HL),$4E            
56FA: 4A              LD      C,D                 
56FB: 46              LD      B,(HL)              
56FC: 44              LD      B,H                 
56FD: 40              LD      B,B                 
56FE: A3              AND     E                   
56FF: 44              LD      B,H                 
5700: 40              LD      B,B                 
5701: 01 20 AA        LD      BC,$AA20            
5704: 38 40           JR      C,$5746             ; {}
5706: 46              LD      B,(HL)              
5707: A3              AND     E                   
5708: 50              LD      D,B                 
5709: AA              XOR     D                   
570A: 20 20           JR      NZ,$572C            ; {}
570C: 20 A3           JR      NZ,$56B1            ; {}
570E: 1E AA           LD      E,$AA               
5710: 36 3C           LD      (HL),$3C            
5712: 44              LD      B,H                 
5713: A3              AND     E                   
5714: 4E              LD      C,(HL)              
5715: AA              XOR     D                   
5716: 36 36           LD      (HL),$36            
5718: 36 9B           LD      (HL),$9B            
571A: 03              INC     BC                  
571B: A3              AND     E                   
571C: 28 AA           JR      Z,$56C8             ; {}
571E: 28 28           JR      Z,$5748             ; {}
5720: 28 9C           JR      Z,$56BE             ; {}
5722: A6              AND     (HL)                
5723: 28 28           JR      Z,$574D             ; {}
5725: A2              AND     D                   
5726: 24              INC     H                   
5727: A3              AND     E                   
5728: 20 AA           JR      NZ,$56D4            ; {}
572A: 20 28           JR      NZ,$5754            ; {}
572C: 2E A3           LD      L,$A3               
572E: 38 AA           JR      C,$56DA             ; {}
5730: 20 20           JR      NZ,$5752            ; {}
5732: 20 A3           JR      NZ,$56D7            ; {}
5734: 2A              LD      A,(HLI)             
5735: AA              XOR     D                   
5736: 2A              LD      A,(HLI)             
5737: 32              LD      (HLD),A             
5738: 38 A3           JR      C,$56DD             ; {}
573A: 42              LD      B,D                 
573B: AA              XOR     D                   
573C: 2A              LD      A,(HLI)             
573D: 2A              LD      A,(HLI)             
573E: 2A              LD      A,(HLI)             
573F: A3              AND     E                   
5740: 1E AA           LD      E,$AA               
5742: 4A              LD      C,D                 
5743: 4A              LD      C,D                 
5744: 4A              LD      C,D                 
5745: A3              AND     E                   
5746: 4A              LD      C,D                 
5747: AA              XOR     D                   
5748: 1E 1E           LD      E,$1E               
574A: 1E A3           LD      E,$A3               
574C: 1E AA           LD      E,$AA               
574E: 58              LD      E,B                 
574F: 58              LD      E,B                 
5750: 58              LD      E,B                 
5751: 5C              LD      E,H                 
5752: 38 36           JR      C,$578A             ; {}
5754: 32              LD      (HLD),A             
5755: 2E 2C           LD      L,$2C               
5757: 00              NOP                         
5758: 00              NOP                         
5759: 3A              LD      A,(HLD)             
575A: 4A              LD      C,D                 
575B: 63              LD      H,E                 
575C: 57              LD      D,A                 
575D: 8D              ADC     A,L                 
575E: 57              LD      D,A                 
575F: A7              AND     A                   
5760: 57              LD      D,A                 
5761: C3 57 19        JP      $1957               
5764: 6F              LD      L,A                 
5765: D3                              
5766: 57              LD      D,A                 
5767: D3                              
5768: 57              LD      D,A                 
5769: 19              ADD     HL,DE               
576A: 6F              LD      L,A                 
576B: F8 57           LD      HL,SP+$57           
576D: 16 58           LD      D,$58               
576F: 19              ADD     HL,DE               
5770: 6F              LD      L,A                 
5771: F8 57           LD      HL,SP+$57           
5773: A8              XOR     B                   
5774: 6F              LD      L,A                 
5775: FB              EI                          
5776: 6E              LD      L,(HL)              
5777: F8 57           LD      HL,SP+$57           
5779: 1E 6F           LD      E,$6F               
577B: F8 57           LD      HL,SP+$57           
577D: 16 58           LD      D,$58               
577F: A5              AND     L                   
5780: 6F              LD      L,A                 
5781: E2              LD      (C),A               
5782: 6F              LD      L,A                 
5783: 19              ADD     HL,DE               
5784: 6F              LD      L,A                 
5785: F8 57           LD      HL,SP+$57           
5787: F8 57           LD      HL,SP+$57           
5789: FF              RST     0X38                
578A: FF              RST     0X38                
578B: 69              LD      L,C                 
578C: 57              LD      D,A                 
578D: EC                              
578E: 6F              LD      L,A                 
578F: 6F              LD      L,A                 
5790: 58              LD      E,B                 
5791: 23              INC     HL                  
5792: 6F              LD      L,A                 
5793: 8E              ADC     A,(HL)              
5794: 58              LD      E,B                 
5795: EC                              
5796: 6F              LD      L,A                 
5797: EC                              
5798: 6F              LD      L,A                 
5799: 28 6F           JR      Z,$580A             ; {}
579B: 8E              ADC     A,(HL)              
579C: 58              LD      E,B                 
579D: E2              LD      (C),A               
579E: 6F              LD      L,A                 
579F: EC                              
57A0: 6F              LD      L,A                 
57A1: 1B              DEC     DE                  
57A2: 59              LD      E,C                 
57A3: FF              RST     0X38                
57A4: FF              RST     0X38                
57A5: 91              SUB     C                   
57A6: 57              LD      D,A                 
57A7: D6 6E           SUB     $6E                 
57A9: 26 59           LD      H,$59               
57AB: EC                              
57AC: 6E              LD      L,(HL)              
57AD: 33              INC     SP                  
57AE: 59              LD      E,C                 
57AF: 7F              LD      A,A                 
57B0: 59              LD      E,C                 
57B1: EC                              
57B2: 6F              LD      L,A                 
57B3: F2                              
57B4: 6F              LD      L,A                 
57B5: E2              LD      (C),A               
57B6: 6F              LD      L,A                 
57B7: 7F              LD      A,A                 
57B8: 59              LD      E,C                 
57B9: E2              LD      (C),A               
57BA: 6F              LD      L,A                 
57BB: EC                              
57BC: 6F              LD      L,A                 
57BD: EC                              
57BE: 6F              LD      L,A                 
57BF: FF              RST     0X38                
57C0: FF              RST     0X38                
57C1: AB              XOR     E                   
57C2: 57              LD      D,A                 
57C3: 94              SUB     H                   
57C4: 59              LD      E,C                 
57C5: A1              AND     C                   
57C6: 59              LD      E,C                 
57C7: B8              CP      B                   
57C8: 59              LD      E,C                 
57C9: C2 59 B8        JP      NZ,$B859            
57CC: 59              LD      E,C                 
57CD: D9              RETI                        
57CE: 59              LD      E,C                 
57CF: FF              RST     0X38                
57D0: FF              RST     0X38                
57D1: C5              PUSH    BC                  
57D2: 57              LD      D,A                 
57D3: 9D              SBC     L                   
57D4: 33              INC     SP                  
57D5: 00              NOP                         
57D6: 80              ADD     A,B                 
57D7: 9B              SBC     E                   
57D8: 04              INC     B                   
57D9: A2              AND     D                   
57DA: 4E              LD      C,(HL)              
57DB: A1              AND     C                   
57DC: 4E              LD      C,(HL)              
57DD: 4E              LD      C,(HL)              
57DE: 9C              SBC     H                   
57DF: 9B              SBC     E                   
57E0: 04              INC     B                   
57E1: A2              AND     D                   
57E2: 52              LD      D,D                 
57E3: A1              AND     C                   
57E4: 52              LD      D,D                 
57E5: 52              LD      D,D                 
57E6: 9C              SBC     H                   
57E7: 9B              SBC     E                   
57E8: 04              INC     B                   
57E9: A2              AND     D                   
57EA: 54              LD      D,H                 
57EB: A1              AND     C                   
57EC: 54              LD      D,H                 
57ED: 54              LD      D,H                 
57EE: 9C              SBC     H                   
57EF: 9B              SBC     E                   
57F0: 04              INC     B                   
57F1: A2              AND     D                   
57F2: 52              LD      D,D                 
57F3: A1              AND     C                   
57F4: 52              LD      D,D                 
57F5: 52              LD      D,D                 
57F6: 9C              SBC     H                   
57F7: 00              NOP                         
57F8: 9B              SBC     E                   
57F9: 04              INC     B                   
57FA: A1              AND     C                   
57FB: 28 36           JR      Z,$5833             ; {}
57FD: 2E 36           LD      L,$36               
57FF: 9C              SBC     H                   
5800: 9B              SBC     E                   
5801: 04              INC     B                   
5802: 28 3A           JR      Z,$583E             ; {}
5804: 32              LD      (HLD),A             
5805: 3A              LD      A,(HLD)             
5806: 9C              SBC     H                   
5807: 9B              SBC     E                   
5808: 04              INC     B                   
5809: 28 3C           JR      Z,$5847             ; {}
580B: 36 3C           LD      (HL),$3C            
580D: 9C              SBC     H                   
580E: 9B              SBC     E                   
580F: 04              INC     B                   
5810: 28 3A           JR      Z,$584C             ; {}
5812: 32              LD      (HLD),A             
5813: 3A              LD      A,(HLD)             
5814: 9C              SBC     H                   
5815: 00              NOP                         
5816: 9B              SBC     E                   
5817: 04              INC     B                   
5818: 20 36           JR      NZ,$5850            ; {}
581A: 2E 36           LD      L,$36               
581C: 9C              SBC     H                   
581D: 9B              SBC     E                   
581E: 04              INC     B                   
581F: 24              INC     H                   
5820: 32              LD      (HLD),A             
5821: 2C              INC     L                   
5822: 32              LD      (HLD),A             
5823: 9C              SBC     H                   
5824: 9B              SBC     E                   
5825: 02              LD      (BC),A              
5826: 24              INC     H                   
5827: 36 2E           LD      (HL),$2E            
5829: 36 9C           LD      (HL),$9C            
582B: 9B              SBC     E                   
582C: 02              LD      (BC),A              
582D: 28 3A           JR      Z,$5869             ; {}
582F: 32              LD      (HLD),A             
5830: 3A              LD      A,(HLD)             
5831: 9C              SBC     H                   
5832: 9B              SBC     E                   
5833: 04              INC     B                   
5834: 2C              INC     L                   
5835: 3E 36           LD      A,$36               
5837: 3E 9C           LD      A,$9C               
5839: 9B              SBC     E                   
583A: 04              INC     B                   
583B: 28 36           JR      Z,$5873             ; {}
583D: 2E 36           LD      L,$36               
583F: 9C              SBC     H                   
5840: 9B              SBC     E                   
5841: 04              INC     B                   
5842: 2A              LD      A,(HLI)             
5843: 38 32           JR      C,$5877             ; {}
5845: 38 9C           JR      C,$57E3             ; {}
5847: 9B              SBC     E                   
5848: 04              INC     B                   
5849: 28 36           JR      Z,$5881             ; {}
584B: 2E 36           LD      L,$36               
584D: 9C              SBC     H                   
584E: 9B              SBC     E                   
584F: 04              INC     B                   
5850: 22              LD      (HLI),A             
5851: 36 2E           LD      (HL),$2E            
5853: 36 9C           LD      (HL),$9C            
5855: 9B              SBC     E                   
5856: 04              INC     B                   
5857: 2A              LD      A,(HLI)             
5858: 38 32           JR      C,$588C             ; {}
585A: 38 9C           JR      C,$57F8             ; {}
585C: A1              AND     C                   
585D: 36 40           LD      (HL),$40            
585F: 44              LD      B,H                 
5860: 4A              LD      C,D                 
5861: A3              AND     E                   
5862: 4E              LD      C,(HL)              
5863: A4              AND     H                   
5864: 01 9D 50        LD      BC,$509D            
5867: 26 01           LD      H,$01               
5869: A4              AND     H                   
586A: 4E              LD      C,(HL)              
586B: 4A              LD      C,D                 
586C: 46              LD      B,(HL)              
586D: 4A              LD      C,D                 
586E: 00              NOP                         
586F: 9D              SBC     L                   
5870: 40              LD      B,B                 
5871: 26 41           LD      H,$41               
5873: A3              AND     E                   
5874: 40              LD      B,B                 
5875: A7              AND     A                   
5876: 36 A2           LD      (HL),$A2            
5878: 40              LD      B,B                 
5879: A1              AND     C                   
587A: 40              LD      B,B                 
587B: 44              LD      B,H                 
587C: 46              LD      B,(HL)              
587D: 4A              LD      C,D                 
587E: A5              AND     L                   
587F: 4E              LD      C,(HL)              
5880: A3              AND     E                   
5881: 58              LD      E,B                 
5882: A7              AND     A                   
5883: 4E              LD      C,(HL)              
5884: A2              AND     D                   
5885: 58              LD      E,B                 
5886: A1              AND     C                   
5887: 58              LD      E,B                 
5888: 5C              LD      E,H                 
5889: 5E              LD      E,(HL)              
588A: 62              LD      H,D                 
588B: A5              AND     L                   
588C: 66              LD      H,(HL)              
588D: 00              NOP                         
588E: A6              AND     (HL)                
588F: 40              LD      B,B                 
5890: A1              AND     C                   
5891: 36 A7           LD      (HL),$A7            
5893: 36 A2           LD      (HL),$A2            
5895: 40              LD      B,B                 
5896: A1              AND     C                   
5897: 40              LD      B,B                 
5898: 44              LD      B,H                 
5899: 46              LD      B,(HL)              
589A: 4A              LD      C,D                 
589B: A7              AND     A                   
589C: 4E              LD      C,(HL)              
589D: A1              AND     C                   
589E: 52              LD      D,D                 
589F: 54              LD      D,H                 
58A0: A6              AND     (HL)                
58A1: 52              LD      D,D                 
58A2: 4E              LD      C,(HL)              
58A3: A2              AND     D                   
58A4: 4A              LD      C,D                 
58A5: A6              AND     (HL)                
58A6: 4E              LD      C,(HL)              
58A7: A1              AND     C                   
58A8: 40              LD      B,B                 
58A9: A5              AND     L                   
58AA: 58              LD      E,B                 
58AB: A2              AND     D                   
58AC: 01 4E 5E        LD      BC,$5E4E            
58AF: 5C              LD      E,H                 
58B0: 5E              LD      E,(HL)              
58B1: 62              LD      H,D                 
58B2: 66              LD      H,(HL)              
58B3: A1              AND     C                   
58B4: 58              LD      E,B                 
58B5: 66              LD      H,(HL)              
58B6: A3              AND     E                   
58B7: 70              LD      (HL),B              
58B8: A2              AND     D                   
58B9: 01 66 62        LD      BC,$6266            
58BC: 5E              LD      E,(HL)              
58BD: 62              LD      H,D                 
58BE: A1              AND     C                   
58BF: 54              LD      D,H                 
58C0: 62              LD      H,D                 
58C1: A3              AND     E                   
58C2: 6C              LD      L,H                 
58C3: A2              AND     D                   
58C4: 01 62 5E        LD      BC,$5E62            
58C7: 5C              LD      E,H                 
58C8: A6              AND     (HL)                
58C9: 5E              LD      E,(HL)              
58CA: A1              AND     C                   
58CB: 4E              LD      C,(HL)              
58CC: A3              AND     E                   
58CD: 4E              LD      C,(HL)              
58CE: A2              AND     D                   
58CF: 01 AD 4A        LD      BC,$4AAD            
58D2: 4E              LD      C,(HL)              
58D3: 4A              LD      C,D                 
58D4: A2              AND     D                   
58D5: 46              LD      B,(HL)              
58D6: 4A              LD      C,D                 
58D7: A5              AND     L                   
58D8: 4E              LD      C,(HL)              
58D9: A6              AND     (HL)                
58DA: 40              LD      B,B                 
58DB: A1              AND     C                   
58DC: 36 A7           LD      (HL),$A7            
58DE: 36 A2           LD      (HL),$A2            
58E0: 40              LD      B,B                 
58E1: A1              AND     C                   
58E2: 40              LD      B,B                 
58E3: 44              LD      B,H                 
58E4: 46              LD      B,(HL)              
58E5: 4A              LD      C,D                 
58E6: A7              AND     A                   
58E7: 4E              LD      C,(HL)              
58E8: A1              AND     C                   
58E9: 50              LD      D,B                 
58EA: 54              LD      D,H                 
58EB: A6              AND     (HL)                
58EC: 50              LD      D,B                 
58ED: 4E              LD      C,(HL)              
58EE: A2              AND     D                   
58EF: 4A              LD      C,D                 
58F0: A6              AND     (HL)                
58F1: 46              LD      B,(HL)              
58F2: A1              AND     C                   
58F3: 40              LD      B,B                 
58F4: A7              AND     A                   
58F5: 4E              LD      C,(HL)              
58F6: A2              AND     D                   
58F7: 46              LD      B,(HL)              
58F8: 58              LD      E,B                 
58F9: 4E              LD      C,(HL)              
58FA: A7              AND     A                   
58FB: 5E              LD      E,(HL)              
58FC: A2              AND     D                   
58FD: 5C              LD      E,H                 
58FE: 58              LD      E,B                 
58FF: 5C              LD      E,H                 
5900: 5E              LD      E,(HL)              
5901: 62              LD      H,D                 
5902: A2              AND     D                   
5903: 66              LD      H,(HL)              
5904: A1              AND     C                   
5905: 62              LD      H,D                 
5906: 66              LD      H,(HL)              
5907: A3              AND     E                   
5908: 68              LD      L,B                 
5909: A2              AND     D                   
590A: 01 A6 6C        LD      BC,$6CA6            
590D: 68              LD      L,B                 
590E: 66              LD      H,(HL)              
590F: 5C              LD      E,H                 
5910: A2              AND     D                   
5911: 5E              LD      E,(HL)              
5912: A6              AND     (HL)                
5913: 62              LD      H,D                 
5914: 5E              LD      E,(HL)              
5915: A2              AND     D                   
5916: 5C              LD      E,H                 
5917: A5              AND     L                   
5918: 58              LD      E,B                 
5919: 70              LD      (HL),B              
591A: 00              NOP                         
591B: 9D              SBC     L                   
591C: 56              LD      D,(HL)              
591D: 00              NOP                         
591E: 80              ADD     A,B                 
591F: 9B              SBC     E                   
5920: 04              INC     B                   
5921: A4              AND     H                   
5922: 01 8C 9C        LD      BC,$9C8C            
5925: 00              NOP                         
5926: 9B              SBC     E                   
5927: 1F              RRA                         
5928: A2              AND     D                   
5929: 40              LD      B,B                 
592A: A1              AND     C                   
592B: 40              LD      B,B                 
592C: 40              LD      B,B                 
592D: 9C              SBC     H                   
592E: 01 1A 16        LD      BC,$161A            
5931: 14              INC     D                   
5932: 00              NOP                         
5933: 99              SBC     C                   
5934: 9B              SBC     E                   
5935: 02              LD      (BC),A              
5936: A3              AND     E                   
5937: 28 A4           JR      Z,$58DD             ; {}
5939: 28 A3           JR      Z,$58DE             ; {}
593B: 28 9C           JR      Z,$58D9             ; {}
593D: 28 A4           JR      Z,$58E3             ; {}
593F: 28 A3           JR      Z,$58E4             ; {}
5941: 36 32           LD      (HL),$32            
5943: A4              AND     H                   
5944: 32              LD      (HLD),A             
5945: A2              AND     D                   
5946: 32              LD      (HLD),A             
5947: 36 A3           LD      (HL),$A3            
5949: 38 A4           JR      C,$58EF             ; {}
594B: 38 A3           JR      C,$58F0             ; {}
594D: 38 3C           JR      C,$598B             ; {}
594F: A4              AND     H                   
5950: 3C              INC     A                   
5951: A3              AND     E                   
5952: 3C              INC     A                   
5953: 2E 2E           LD      L,$2E               
5955: 32              LD      (HLD),A             
5956: 32              LD      (HLD),A             
5957: 36 A4           LD      (HL),$A4            
5959: 36 A1           LD      (HL),$A1            
595B: 36 32           LD      (HL),$32            
595D: 2E 2C           LD      L,$2C               
595F: A3              AND     E                   
5960: 28 A4           JR      Z,$5906             ; {}
5962: 28 A3           JR      Z,$5907             ; {}
5964: 28 2A           JR      Z,$5990             ; {}
5966: A4              AND     H                   
5967: 2A              LD      A,(HLI)             
5968: A3              AND     E                   
5969: 2A              LD      A,(HLI)             
596A: 28 A4           JR      Z,$5910             ; {}
596C: 28 A3           JR      Z,$5911             ; {}
596E: 24              INC     H                   
596F: 22              LD      (HLI),A             
5970: A4              AND     H                   
5971: 22              LD      (HLI),A             
5972: A3              AND     E                   
5973: 22              LD      (HLI),A             
5974: 2A              LD      A,(HLI)             
5975: A4              AND     H                   
5976: 2A              LD      A,(HLI)             
5977: A3              AND     E                   
5978: 2A              LD      A,(HLI)             
5979: 36 01           LD      (HL),$01            
597B: 01 9A 1E        LD      BC,$1E9A            
597E: 00              NOP                         
597F: A6              AND     (HL)                
5980: 28 36           JR      Z,$59B8             ; {}
5982: A2              AND     D                   
5983: 28 A6           JR      Z,$592B             ; {}
5985: 24              INC     H                   
5986: 32              LD      (HLD),A             
5987: A2              AND     D                   
5988: 24              INC     H                   
5989: A6              AND     (HL)                
598A: 20 2E           JR      NZ,$59BA            ; {}
598C: A2              AND     D                   
598D: 20 A6           JR      NZ,$5935            ; {}
598F: 24              INC     H                   
5990: 32              LD      (HLD),A             
5991: A2              AND     D                   
5992: 24              INC     H                   
5993: 00              NOP                         
5994: 9B              SBC     E                   
5995: 1F              RRA                         
5996: A2              AND     D                   
5997: 0B              DEC     BC                  
5998: A1              AND     C                   
5999: 0B              DEC     BC                  
599A: 0B              DEC     BC                  
599B: 9C              SBC     H                   
599C: 15              DEC     D                   
599D: 15              DEC     D                   
599E: 15              DEC     D                   
599F: 15              DEC     D                   
59A0: 00              NOP                         
59A1: 9B              SBC     E                   
59A2: 0D              DEC     C                   
59A3: A2              AND     D                   
59A4: 15              DEC     D                   
59A5: A1              AND     C                   
59A6: 15              DEC     D                   
59A7: 15              DEC     D                   
59A8: A2              AND     D                   
59A9: 15              DEC     D                   
59AA: A1              AND     C                   
59AB: 15              DEC     D                   
59AC: 15              DEC     D                   
59AD: A2              AND     D                   
59AE: 15              DEC     D                   
59AF: A1              AND     C                   
59B0: 15              DEC     D                   
59B1: 15              DEC     D                   
59B2: 15              DEC     D                   
59B3: 15              DEC     D                   
59B4: 15              DEC     D                   
59B5: 15              DEC     D                   
59B6: 9C              SBC     H                   
59B7: 00              NOP                         
59B8: A1              AND     C                   
59B9: 15              DEC     D                   
59BA: 15              DEC     D                   
59BB: 15              DEC     D                   
59BC: 15              DEC     D                   
59BD: A3              AND     E                   
59BE: 15              DEC     D                   
59BF: A4              AND     H                   
59C0: 01 00 9B        LD      BC,$9B00            
59C3: 17              RLA                         
59C4: A2              AND     D                   
59C5: 15              DEC     D                   
59C6: A1              AND     C                   
59C7: 15              DEC     D                   
59C8: 15              DEC     D                   
59C9: A2              AND     D                   
59CA: 15              DEC     D                   
59CB: A1              AND     C                   
59CC: 15              DEC     D                   
59CD: 15              DEC     D                   
59CE: A2              AND     D                   
59CF: 15              DEC     D                   
59D0: A1              AND     C                   
59D1: 15              DEC     D                   
59D2: 15              DEC     D                   
59D3: 15              DEC     D                   
59D4: 15              DEC     D                   
59D5: 15              DEC     D                   
59D6: 15              DEC     D                   
59D7: 9C              SBC     H                   
59D8: 00              NOP                         
59D9: 9B              SBC     E                   
59DA: 0C              INC     C                   
59DB: A2              AND     D                   
59DC: 15              DEC     D                   
59DD: A1              AND     C                   
59DE: 15              DEC     D                   
59DF: 15              DEC     D                   
59E0: A2              AND     D                   
59E1: 15              DEC     D                   
59E2: A1              AND     C                   
59E3: 15              DEC     D                   
59E4: 15              DEC     D                   
59E5: A2              AND     D                   
59E6: 15              DEC     D                   
59E7: A1              AND     C                   
59E8: 15              DEC     D                   
59E9: 15              DEC     D                   
59EA: 15              DEC     D                   
59EB: 15              DEC     D                   
59EC: 15              DEC     D                   
59ED: 15              DEC     D                   
59EE: 9C              SBC     H                   
59EF: 00              NOP                         
59F0: 00              NOP                         
59F1: 76              HALT                        
59F2: 4A              LD      C,D                 
59F3: FB              EI                          
59F4: 59              LD      E,C                 
59F5: 01 5A 07        LD      BC,$075A            
59F8: 5A              LD      E,D                 
59F9: 00              NOP                         
59FA: 00              NOP                         
59FB: 0F              RRCA                        
59FC: 5A              LD      E,D                 
59FD: FF              RST     0X38                
59FE: FF              RST     0X38                
59FF: FB              EI                          
5A00: 59              LD      E,C                 
5A01: 3F              CCF                         
5A02: 5A              LD      E,D                 
5A03: FF              RST     0X38                
5A04: FF              RST     0X38                
5A05: 01 5A C7        LD      BC,$C75A            
5A08: 6E              LD      L,(HL)              
5A09: 7A              LD      A,D                 
5A0A: 5A              LD      E,D                 
5A0B: FF              RST     0X38                
5A0C: FF              RST     0X38                
5A0D: 07              RLCA                        
5A0E: 5A              LD      E,D                 
5A0F: 9D              SBC     L                   
5A10: 44              LD      B,H                 
5A11: 00              NOP                         
5A12: 80              ADD     A,B                 
5A13: 98              SBC     B                   
5A14: 9B              SBC     E                   
5A15: 02              LD      (BC),A              
5A16: A3              AND     E                   
5A17: 01 A2 46        LD      BC,$46A2            
5A1A: A1              AND     C                   
5A1B: 88              ADC     A,B                 
5A1C: 88              ADC     A,B                 
5A1D: A3              AND     E                   
5A1E: 01 A2 44        LD      BC,$44A2            
5A21: A1              AND     C                   
5A22: 88              ADC     A,B                 
5A23: 88              ADC     A,B                 
5A24: 9C              SBC     H                   
5A25: 9D              SBC     L                   
5A26: 24              INC     H                   
5A27: 00              NOP                         
5A28: 80              ADD     A,B                 
5A29: A3              AND     E                   
5A2A: 01 A2 64        LD      BC,$64A2            
5A2D: 62              LD      H,D                 
5A2E: 60              LD      H,B                 
5A2F: 64              LD      H,H                 
5A30: 5E              LD      E,(HL)              
5A31: 60              LD      H,B                 
5A32: 5C              LD      E,H                 
5A33: 60              LD      H,B                 
5A34: 5A              LD      E,D                 
5A35: 5C              LD      E,H                 
5A36: 58              LD      E,B                 
5A37: 56              LD      D,(HL)              
5A38: A4              AND     H                   
5A39: 01 97 A1        LD      BC,$A197            
5A3C: 88              ADC     A,B                 
5A3D: 88              ADC     A,B                 
5A3E: 00              NOP                         
5A3F: 9D              SBC     L                   
5A40: 50              LD      D,B                 
5A41: 84              ADD     A,H                 
5A42: 00              NOP                         
5A43: A6              AND     (HL)                
5A44: 70              LD      (HL),B              
5A45: A1              AND     C                   
5A46: 66              LD      H,(HL)              
5A47: A2              AND     D                   
5A48: 60              LD      H,B                 
5A49: 58              LD      E,B                 
5A4A: A3              AND     E                   
5A4B: 5A              LD      E,D                 
5A4C: A1              AND     C                   
5A4D: 68              LD      L,B                 
5A4E: 62              LD      H,D                 
5A4F: 5A              LD      E,D                 
5A50: 50              LD      D,B                 
5A51: A2              AND     D                   
5A52: 4E              LD      C,(HL)              
5A53: A1              AND     C                   
5A54: 66              LD      H,(HL)              
5A55: 60              LD      H,B                 
5A56: A2              AND     D                   
5A57: 58              LD      E,B                 
5A58: 4E              LD      C,(HL)              
5A59: 54              LD      D,H                 
5A5A: A1              AND     C                   
5A5B: 50              LD      D,B                 
5A5C: 54              LD      D,H                 
5A5D: A3              AND     E                   
5A5E: 4E              LD      C,(HL)              
5A5F: 9D              SBC     L                   
5A60: 24              INC     H                   
5A61: 00              NOP                         
5A62: 00              NOP                         
5A63: A2              AND     D                   
5A64: 4C              LD      C,H                 
5A65: 4E              LD      C,(HL)              
5A66: 68              LD      L,B                 
5A67: 66              LD      H,(HL)              
5A68: 64              LD      H,H                 
5A69: 66              LD      H,(HL)              
5A6A: 62              LD      H,D                 
5A6B: 64              LD      H,H                 
5A6C: 60              LD      H,B                 
5A6D: 62              LD      H,D                 
5A6E: 5E              LD      E,(HL)              
5A6F: 60              LD      H,B                 
5A70: A1              AND     C                   
5A71: 5C              LD      E,H                 
5A72: 5E              LD      E,(HL)              
5A73: 5A              LD      E,D                 
5A74: 5C              LD      E,H                 
5A75: A3              AND     E                   
5A76: 01 A7 01        LD      BC,$01A7            
5A79: 00              NOP                         
5A7A: 9B              SBC     E                   
5A7B: 02              LD      (BC),A              
5A7C: 99              SBC     C                   
5A7D: A2              AND     D                   
5A7E: 40              LD      B,B                 
5A7F: 4C              LD      C,H                 
5A80: 56              LD      D,(HL)              
5A81: 4C              LD      C,H                 
5A82: 36 4A           LD      (HL),$4A            
5A84: 54              LD      D,H                 
5A85: 4A              LD      C,D                 
5A86: 9C              SBC     H                   
5A87: A5              AND     L                   
5A88: 01 01 A7        LD      BC,$A701            
5A8B: 01 00 00        LD      BC,$0000            
5A8E: 49              LD      C,C                 
5A8F: 4A              LD      C,D                 
5A90: 98              SBC     B                   
5A91: 5A              LD      E,D                 
5A92: B2              OR      D                   
5A93: 5A              LD      E,D                 
5A94: C4 5A D6        CALL    NZ,$D65A            
5A97: 5A              LD      E,D                 
5A98: AB              XOR     E                   
5A99: 6F              LD      L,A                 
5A9A: DF              RST     0X18                
5A9B: 6F              LD      L,A                 
5A9C: 32              LD      (HLD),A             
5A9D: 6F              LD      L,A                 
5A9E: F9              LD      SP,HL               
5A9F: 5A              LD      E,D                 
5AA0: 2D              DEC     L                   
5AA1: 6F              LD      L,A                 
5AA2: F9              LD      SP,HL               
5AA3: 5A              LD      E,D                 
5AA4: A5              AND     L                   
5AA5: 6F              LD      L,A                 
5AA6: E0 5A           LD      ($FF00+$5A),A       
5AA8: AB              XOR     E                   
5AA9: 6F              LD      L,A                 
5AAA: E0 5A           LD      ($FF00+$5A),A       
5AAC: E2              LD      (C),A               
5AAD: 6F              LD      L,A                 
5AAE: FF              RST     0X38                
5AAF: FF              RST     0X38                
5AB0: 98              SBC     B                   
5AB1: 5A              LD      E,D                 
5AB2: 32              LD      (HLD),A             
5AB3: 6F              LD      L,A                 
5AB4: 21 5B 2D        LD      HL,$2D5B            
5AB7: 6F              LD      L,A                 
5AB8: 28 5B           JR      Z,$5B15             ; {}
5ABA: 00              NOP                         
5ABB: 5B              LD      E,E                 
5ABC: 00              NOP                         
5ABD: 5B              LD      E,E                 
5ABE: E2              LD      (C),A               
5ABF: 6F              LD      L,A                 
5AC0: FF              RST     0X38                
5AC1: FF              RST     0X38                
5AC2: B2              OR      D                   
5AC3: 5A              LD      E,D                 
5AC4: C2 6E E2        JP      NZ,$E26E            
5AC7: 6F              LD      L,A                 
5AC8: 2F              CPL                         
5AC9: 5B              LD      E,E                 
5ACA: 45              LD      B,L                 
5ACB: 5B              LD      E,E                 
5ACC: 2F              CPL                         
5ACD: 5B              LD      E,E                 
5ACE: 45              LD      B,L                 
5ACF: 5B              LD      E,E                 
5AD0: E2              LD      (C),A               
5AD1: 6F              LD      L,A                 
5AD2: FF              RST     0X38                
5AD3: FF              RST     0X38                
5AD4: C4 5A 68        CALL    NZ,$685A            ; {}
5AD7: 5B              LD      E,E                 
5AD8: 5A              LD      E,D                 
5AD9: 5B              LD      E,E                 
5ADA: 68              LD      L,B                 
5ADB: 5B              LD      E,E                 
5ADC: FF              RST     0X38                
5ADD: FF              RST     0X38                
5ADE: D6 5A           SUB     $5A                 
5AE0: 9D              SBC     L                   
5AE1: 33              INC     SP                  
5AE2: 00              NOP                         
5AE3: 80              ADD     A,B                 
5AE4: 9B              SBC     E                   
5AE5: 04              INC     B                   
5AE6: A1              AND     C                   
5AE7: 58              LD      E,B                 
5AE8: 56              LD      D,(HL)              
5AE9: 54              LD      D,H                 
5AEA: 52              LD      D,D                 
5AEB: 50              LD      D,B                 
5AEC: 4E              LD      C,(HL)              
5AED: 4C              LD      C,H                 
5AEE: 4A              LD      C,D                 
5AEF: 48              LD      C,B                 
5AF0: 4A              LD      C,D                 
5AF1: 4C              LD      C,H                 
5AF2: 4E              LD      C,(HL)              
5AF3: 50              LD      D,B                 
5AF4: 52              LD      D,D                 
5AF5: 54              LD      D,H                 
5AF6: 56              LD      D,(HL)              
5AF7: 9C              SBC     H                   
5AF8: 00              NOP                         
5AF9: 9B              SBC     E                   
5AFA: 04              INC     B                   
5AFB: A1              AND     C                   
5AFC: 46              LD      B,(HL)              
5AFD: 44              LD      B,H                 
5AFE: 9C              SBC     H                   
5AFF: 00              NOP                         
5B00: 9D              SBC     L                   
5B01: 40              LD      B,B                 
5B02: 81              ADD     A,C                 
5B03: 80              ADD     A,B                 
5B04: A7              AND     A                   
5B05: 58              LD      E,B                 
5B06: A2              AND     D                   
5B07: 4E              LD      C,(HL)              
5B08: 58              LD      E,B                 
5B09: 5C              LD      E,H                 
5B0A: 60              LD      H,B                 
5B0B: 66              LD      H,(HL)              
5B0C: A7              AND     A                   
5B0D: 64              LD      H,H                 
5B0E: A2              AND     D                   
5B0F: 66              LD      H,(HL)              
5B10: A4              AND     H                   
5B11: 68              LD      L,B                 
5B12: A7              AND     A                   
5B13: 58              LD      E,B                 
5B14: A2              AND     D                   
5B15: 4E              LD      C,(HL)              
5B16: 58              LD      E,B                 
5B17: 5C              LD      E,H                 
5B18: 60              LD      H,B                 
5B19: 66              LD      H,(HL)              
5B1A: A7              AND     A                   
5B1B: 64              LD      H,H                 
5B1C: A2              AND     D                   
5B1D: 66              LD      H,(HL)              
5B1E: A4              AND     H                   
5B1F: 80              ADD     A,B                 
5B20: 00              NOP                         
5B21: 9B              SBC     E                   
5B22: 0C              INC     C                   
5B23: A1              AND     C                   
5B24: 58              LD      E,B                 
5B25: 56              LD      D,(HL)              
5B26: 9C              SBC     H                   
5B27: 00              NOP                         
5B28: 9B              SBC     E                   
5B29: 04              INC     B                   
5B2A: A1              AND     C                   
5B2B: 58              LD      E,B                 
5B2C: 56              LD      D,(HL)              
5B2D: 9C              SBC     H                   
5B2E: 00              NOP                         
5B2F: 99              SBC     C                   
5B30: A3              AND     E                   
5B31: 28 A2           JR      Z,$5AD5             ; {}
5B33: 36 A3           LD      (HL),$A3            
5B35: 28 A2           JR      Z,$5AD9             ; {}
5B37: 28 2A           JR      Z,$5B63             ; {}
5B39: 38 A3           JR      C,$5ADE             ; {}
5B3B: 28 A2           JR      Z,$5ADF             ; {}
5B3D: 36 A3           LD      (HL),$A3            
5B3F: 28 A2           JR      Z,$5AE3             ; {}
5B41: 28 24           JR      Z,$5B67             ; {}
5B43: 26 00           LD      H,$00               
5B45: A3              AND     E                   
5B46: 28 A2           JR      Z,$5AEA             ; {}
5B48: 36 A3           LD      (HL),$A3            
5B4A: 28 A2           JR      Z,$5AEE             ; {}
5B4C: 28 2A           JR      Z,$5B78             ; {}
5B4E: 38 A3           JR      C,$5AF3             ; {}
5B50: 28 A2           JR      Z,$5AF4             ; {}
5B52: 36 A3           LD      (HL),$A3            
5B54: 28 A2           JR      Z,$5AF8             ; {}
5B56: 28 36           JR      Z,$5B8E             ; {}
5B58: 40              LD      B,B                 
5B59: 00              NOP                         
5B5A: 9B              SBC     E                   
5B5B: 08 A2 29        LD      ($29A2),SP          
5B5E: 29              ADD     HL,HL               
5B5F: 29              ADD     HL,HL               
5B60: 29              ADD     HL,HL               
5B61: A3              AND     E                   
5B62: FF              RST     0X38                
5B63: A2              AND     D                   
5B64: 29              ADD     HL,HL               
5B65: 29              ADD     HL,HL               
5B66: 9C              SBC     H                   
5B67: 00              NOP                         
5B68: A3              AND     E                   
5B69: 29              ADD     HL,HL               
5B6A: A2              AND     D                   
5B6B: 29              ADD     HL,HL               
5B6C: 29              ADD     HL,HL               
5B6D: A3              AND     E                   
5B6E: FF              RST     0X38                
5B6F: A2              AND     D                   
5B70: 29              ADD     HL,HL               
5B71: 29              ADD     HL,HL               
5B72: A2              AND     D                   
5B73: 29              ADD     HL,HL               
5B74: 29              ADD     HL,HL               
5B75: 29              ADD     HL,HL               
5B76: 29              ADD     HL,HL               
5B77: A3              AND     E                   
5B78: FF              RST     0X38                
5B79: A2              AND     D                   
5B7A: 29              ADD     HL,HL               
5B7B: 29              ADD     HL,HL               
5B7C: 00              NOP                         
5B7D: 00              NOP                         
5B7E: 76              HALT                        
5B7F: 4A              LD      C,D                 
5B80: 88              ADC     A,B                 
5B81: 5B              LD      E,E                 
5B82: 94              SUB     H                   
5B83: 5B              LD      E,E                 
5B84: 9C              SBC     H                   
5B85: 5B              LD      E,E                 
5B86: A8              XOR     B                   
5B87: 5B              LD      E,E                 
5B88: E2              LD      (C),A               
5B89: 6F              LD      L,A                 
5B8A: AE              XOR     (HL)                
5B8B: 5B              LD      E,E                 
5B8C: AE              XOR     (HL)                
5B8D: 5B              LD      E,E                 
5B8E: BE              CP      (HL)                
5B8F: 5B              LD      E,E                 
5B90: FF              RST     0X38                
5B91: FF              RST     0X38                
5B92: 8A              ADC     A,D                 
5B93: 5B              LD      E,E                 
5B94: D3                              
5B95: 5B              LD      E,E                 
5B96: F4                              
5B97: 5B              LD      E,E                 
5B98: FF              RST     0X38                
5B99: FF              RST     0X38                
5B9A: 96              SUB     (HL)                
5B9B: 5B              LD      E,E                 
5B9C: E2              LD      (C),A               
5B9D: 6F              LD      L,A                 
5B9E: EC                              
5B9F: 6E              LD      L,(HL)              
5BA0: 26 5C           LD      H,$5C               
5BA2: 44              LD      B,H                 
5BA3: 5C              LD      E,H                 
5BA4: FF              RST     0X38                
5BA5: FF              RST     0X38                
5BA6: 9E              SBC     (HL)                
5BA7: 5B              LD      E,E                 
5BA8: 61              LD      H,C                 
5BA9: 5C              LD      E,H                 
5BAA: FF              RST     0X38                
5BAB: FF              RST     0X38                
5BAC: A8              XOR     B                   
5BAD: 5B              LD      E,E                 
5BAE: 9D              SBC     L                   
5BAF: 23              INC     HL                  
5BB0: 00              NOP                         
5BB1: 80              ADD     A,B                 
5BB2: 9B              SBC     E                   
5BB3: 20 A0           JR      NZ,$5B55            ; {}
5BB5: 5E              LD      E,(HL)              
5BB6: 62              LD      H,D                 
5BB7: 9C              SBC     H                   
5BB8: 9B              SBC     E                   
5BB9: 20 62           JR      NZ,$5C1D            ; {}
5BBB: 64              LD      H,H                 
5BBC: 9C              SBC     H                   
5BBD: 00              NOP                         
5BBE: 9B              SBC     E                   
5BBF: 20 5E           JR      NZ,$5C1F            ; {}
5BC1: 54              LD      D,H                 
5BC2: 9C              SBC     H                   
5BC3: 9B              SBC     E                   
5BC4: 20 5C           JR      NZ,$5C22            ; {}
5BC6: 52              LD      D,D                 
5BC7: 9C              SBC     H                   
5BC8: 9B              SBC     E                   
5BC9: 20 5E           JR      NZ,$5C29            ; {}
5BCB: 50              LD      D,B                 
5BCC: 9C              SBC     H                   
5BCD: 9B              SBC     E                   
5BCE: 20 5C           JR      NZ,$5C2C            ; {}
5BD0: 52              LD      D,D                 
5BD1: 9C              SBC     H                   
5BD2: 00              NOP                         
5BD3: 9D              SBC     L                   
5BD4: 81              ADD     A,C                 
5BD5: 82              ADD     A,D                 
5BD6: 00              NOP                         
5BD7: A2              AND     D                   
5BD8: 10 1E           ;;STOP    $1E                 
5BDA: A1              AND     C                   
5BDB: 24              INC     H                   
5BDC: A2              AND     D                   
5BDD: 26 A1           LD      H,$A1               
5BDF: 28 A7           JR      Z,$5B88             ; {}
5BE1: 01 A1 0C        LD      BC,$0CA1            
5BE4: 0E A2           LD      C,$A2               
5BE6: 10 A1           ;;STOP    $A1                 
5BE8: 1E A2           LD      E,$A2               
5BEA: 24              INC     H                   
5BEB: 26 A1           LD      H,$A1               
5BED: 28 A7           JR      Z,$5B96             ; {}
5BEF: 01 A1 0C        LD      BC,$0CA1            
5BF2: 0E 00           LD      C,$00               
5BF4: 9D              SBC     L                   
5BF5: 40              LD      B,B                 
5BF6: 00              NOP                         
5BF7: 81              ADD     A,C                 
5BF8: 9B              SBC     E                   
5BF9: 02              LD      (BC),A              
5BFA: A4              AND     H                   
5BFB: 58              LD      E,B                 
5BFC: 4E              LD      C,(HL)              
5BFD: A8              XOR     B                   
5BFE: 4E              LD      C,(HL)              
5BFF: A0              AND     B                   
5C00: 58              LD      E,B                 
5C01: 56              LD      D,(HL)              
5C02: 58              LD      E,B                 
5C03: 5C              LD      E,H                 
5C04: 5E              LD      E,(HL)              
5C05: 5C              LD      E,H                 
5C06: 5E              LD      E,(HL)              
5C07: 62              LD      H,D                 
5C08: A6              AND     (HL)                
5C09: 66              LD      H,(HL)              
5C0A: 68              LD      L,B                 
5C0B: A2              AND     D                   
5C0C: 6C              LD      L,H                 
5C0D: A8              XOR     B                   
5C0E: 70              LD      (HL),B              
5C0F: A2              AND     D                   
5C10: 70              LD      (HL),B              
5C11: 6C              LD      L,H                 
5C12: A6              AND     (HL)                
5C13: 68              LD      L,B                 
5C14: 62              LD      H,D                 
5C15: A2              AND     D                   
5C16: 5A              LD      E,D                 
5C17: 9C              SBC     H                   
5C18: 9D              SBC     L                   
5C19: 30 00           JR      NC,$5C1B            ; {}
5C1B: 01 A5 58        LD      BC,$58A5            
5C1E: 4E              LD      C,(HL)              
5C1F: 50              LD      D,B                 
5C20: 52              LD      D,D                 
5C21: 54              LD      D,H                 
5C22: 54              LD      D,H                 
5C23: 56              LD      D,(HL)              
5C24: 56              LD      D,(HL)              
5C25: 00              NOP                         
5C26: 99              SBC     C                   
5C27: A2              AND     D                   
5C28: 28 36           JR      Z,$5C60             ; {}
5C2A: A1              AND     C                   
5C2B: 3C              INC     A                   
5C2C: A2              AND     D                   
5C2D: 3E A1           LD      A,$A1               
5C2F: 40              LD      B,B                 
5C30: A7              AND     A                   
5C31: 01 A1 24        LD      BC,$24A1            
5C34: 26 A2           LD      H,$A2               
5C36: 28 A1           JR      Z,$5BD9             ; {}
5C38: 36 A2           LD      (HL),$A2            
5C3A: 3C              INC     A                   
5C3B: 3E A1           LD      A,$A1               
5C3D: 40              LD      B,B                 
5C3E: A7              AND     A                   
5C3F: 01 A1 26        LD      BC,$26A1            
5C42: 28 00           JR      Z,$5C44             ; {}
5C44: A2              AND     D                   
5C45: 2A              LD      A,(HLI)             
5C46: 38 A1           JR      C,$5BE9             ; {}
5C48: 3E A2           LD      A,$A2               
5C4A: 40              LD      B,B                 
5C4B: A1              AND     C                   
5C4C: 42              LD      B,D                 
5C4D: A7              AND     A                   
5C4E: 01 A1 26        LD      BC,$26A1            
5C51: 28 A2           JR      Z,$5BF5             ; {}
5C53: 2A              LD      A,(HLI)             
5C54: A1              AND     C                   
5C55: 38 A2           JR      C,$5BF9             ; {}
5C57: 3E 40           LD      A,$40               
5C59: A1              AND     C                   
5C5A: 42              LD      B,D                 
5C5B: A7              AND     A                   
5C5C: 01 A1 24        LD      BC,$24A1            
5C5F: 26 00           LD      H,$00               
5C61: 9B              SBC     E                   
5C62: 04              INC     B                   
5C63: A1              AND     C                   
5C64: 29              ADD     HL,HL               
5C65: 9C              SBC     H                   
5C66: FF              RST     0X38                
5C67: 9B              SBC     E                   
5C68: 05              DEC     B                   
5C69: 29              ADD     HL,HL               
5C6A: 9C              SBC     H                   
5C6B: FF              RST     0X38                
5C6C: 9B              SBC     E                   
5C6D: 05              DEC     B                   
5C6E: 29              ADD     HL,HL               
5C6F: 9C              SBC     H                   
5C70: 00              NOP                         
5C71: 04              INC     B                   
5C72: 58              LD      E,B                 
5C73: 4A              LD      C,D                 
5C74: 7C              LD      A,H                 
5C75: 5C              LD      E,H                 
5C76: 86              ADD     A,(HL)              
5C77: 5C              LD      E,H                 
5C78: 8C              ADC     A,H                 
5C79: 4A              LD      C,D                 
5C7A: 00              NOP                         
5C7B: 00              NOP                         
5C7C: AE              XOR     (HL)                
5C7D: 6F              LD      L,A                 
5C7E: FB              EI                          
5C7F: 6F              LD      L,A                 
5C80: 8E              ADC     A,(HL)              
5C81: 5C              LD      E,H                 
5C82: FF              RST     0X38                
5C83: FF              RST     0X38                
5C84: 80              ADD     A,B                 
5C85: 5C              LD      E,H                 
5C86: B3              OR      E                   
5C87: 6F              LD      L,A                 
5C88: 8E              ADC     A,(HL)              
5C89: 5C              LD      E,H                 
5C8A: FF              RST     0X38                
5C8B: FF              RST     0X38                
5C8C: 86              ADD     A,(HL)              
5C8D: 5C              LD      E,H                 
5C8E: A2              AND     D                   
5C8F: 5C              LD      E,H                 
5C90: 3C              INC     A                   
5C91: 4A              LD      C,D                 
5C92: 52              LD      D,D                 
5C93: 58              LD      E,B                 
5C94: 5C              LD      E,H                 
5C95: 5E              LD      E,(HL)              
5C96: 40              LD      B,B                 
5C97: 4E              LD      C,(HL)              
5C98: 54              LD      D,H                 
5C99: 5C              LD      E,H                 
5C9A: 5E              LD      E,(HL)              
5C9B: 62              LD      H,D                 
5C9C: 44              LD      B,H                 
5C9D: 52              LD      D,D                 
5C9E: 58              LD      E,B                 
5C9F: 70              LD      (HL),B              
5CA0: 6C              LD      L,H                 
5CA1: 62              LD      H,D                 
5CA2: 36 44           LD      (HL),$44            
5CA4: 4A              LD      C,D                 
5CA5: 5E              LD      E,(HL)              
5CA6: 5C              LD      E,H                 
5CA7: 5C              LD      E,H                 
5CA8: 40              LD      B,B                 
5CA9: 4E              LD      C,(HL)              
5CAA: 54              LD      D,H                 
5CAB: 58              LD      E,B                 
5CAC: 5C              LD      E,H                 
5CAD: 5E              LD      E,(HL)              
5CAE: 40              LD      B,B                 
5CAF: 4C              LD      C,H                 
5CB0: 54              LD      D,H                 
5CB1: 5C              LD      E,H                 
5CB2: 5E              LD      E,(HL)              
5CB3: 58              LD      E,B                 
5CB4: 32              LD      (HLD),A             
5CB5: 40              LD      B,B                 
5CB6: 46              LD      B,(HL)              
5CB7: 4C              LD      C,H                 
5CB8: 54              LD      D,H                 
5CB9: 52              LD      D,D                 
5CBA: 4A              LD      C,D                 
5CBB: 4E              LD      C,(HL)              
5CBC: 52              LD      D,D                 
5CBD: 54              LD      D,H                 
5CBE: 58              LD      E,B                 
5CBF: 5C              LD      E,H                 
5CC0: 3C              INC     A                   
5CC1: 4A              LD      C,D                 
5CC2: 52              LD      D,D                 
5CC3: 58              LD      E,B                 
5CC4: 5C              LD      E,H                 
5CC5: 5E              LD      E,(HL)              
5CC6: 40              LD      B,B                 
5CC7: 4E              LD      C,(HL)              
5CC8: 54              LD      D,H                 
5CC9: 5C              LD      E,H                 
5CCA: 5E              LD      E,(HL)              
5CCB: 62              LD      H,D                 
5CCC: 44              LD      B,H                 
5CCD: 52              LD      D,D                 
5CCE: 58              LD      E,B                 
5CCF: 74              LD      (HL),H              
5CD0: 70              LD      (HL),B              
5CD1: 70              LD      (HL),B              
5CD2: 36 44           LD      (HL),$44            
5CD4: 6E              LD      L,(HL)              
5CD5: 68              LD      L,B                 
5CD6: 66              LD      H,(HL)              
5CD7: 62              LD      H,D                 
5CD8: 40              LD      B,B                 
5CD9: 4E              LD      C,(HL)              
5CDA: 54              LD      D,H                 
5CDB: 5E              LD      E,(HL)              
5CDC: 5C              LD      E,H                 
5CDD: 5C              LD      E,H                 
5CDE: 32              LD      (HLD),A             
5CDF: 40              LD      B,B                 
5CE0: 46              LD      B,(HL)              
5CE1: 58              LD      E,B                 
5CE2: 5C              LD      E,H                 
5CE3: 54              LD      D,H                 
5CE4: 46              LD      B,(HL)              
5CE5: 54              LD      D,H                 
5CE6: 5C              LD      E,H                 
5CE7: 5E              LD      E,(HL)              
5CE8: 74              LD      (HL),H              
5CE9: 70              LD      (HL),B              
5CEA: 44              LD      B,H                 
5CEB: 52              LD      D,D                 
5CEC: 58              LD      E,B                 
5CED: 5C              LD      E,H                 
5CEE: 6A              LD      L,D                 
5CEF: 66              LD      H,(HL)              
5CF0: 40              LD      B,B                 
5CF1: 4E              LD      C,(HL)              
5CF2: 54              LD      D,H                 
5CF3: 58              LD      E,B                 
5CF4: 66              LD      H,(HL)              
5CF5: 64              LD      H,H                 
5CF6: 32              LD      (HLD),A             
5CF7: 40              LD      B,B                 
5CF8: 46              LD      B,(HL)              
5CF9: 4C              LD      C,H                 
5CFA: 54              LD      D,H                 
5CFB: 62              LD      H,D                 
5CFC: 32              LD      (HLD),A             
5CFD: 3A              LD      A,(HLD)             
5CFE: 40              LD      B,B                 
5CFF: 4A              LD      C,D                 
5D00: 52              LD      D,D                 
5D01: A3              AND     E                   
5D02: 62              LD      H,D                 
5D03: A2              AND     D                   
5D04: 62              LD      H,D                 
5D05: A7              AND     A                   
5D06: 7A              LD      A,D                 
5D07: 32              LD      (HLD),A             
5D08: 00              NOP                         
5D09: 00              NOP                         
5D0A: 76              HALT                        
5D0B: 4A              LD      C,D                 
5D0C: 14              INC     D                   
5D0D: 5D              LD      E,L                 
5D0E: 22              LD      (HLI),A             
5D0F: 5D              LD      E,L                 
5D10: 2C              INC     L                   
5D11: 5D              LD      E,L                 
5D12: 38 5D           JR      C,$5D71             ; {}
5D14: DF              RST     0X18                
5D15: 6F              LD      L,A                 
5D16: A5              AND     L                   
5D17: 6F              LD      L,A                 
5D18: 3E 5D           LD      A,$5D               
5D1A: AB              XOR     E                   
5D1B: 6F              LD      L,A                 
5D1C: 3E 5D           LD      A,$5D               
5D1E: FF              RST     0X38                
5D1F: FF              RST     0X38                
5D20: 16 5D           LD      D,$5D               
5D22: DF              RST     0X18                
5D23: 6F              LD      L,A                 
5D24: 60              LD      H,B                 
5D25: 5D              LD      E,L                 
5D26: 60              LD      H,B                 
5D27: 5D              LD      E,L                 
5D28: FF              RST     0X38                
5D29: FF              RST     0X38                
5D2A: 24              INC     H                   
5D2B: 5D              LD      E,L                 
5D2C: DF              RST     0X18                
5D2D: 6F              LD      L,A                 
5D2E: C2 6E 7B        JP      NZ,$7B6E            ; {}
5D31: 5D              LD      E,L                 
5D32: 7B              LD      A,E                 
5D33: 5D              LD      E,L                 
5D34: FF              RST     0X38                
5D35: FF              RST     0X38                
5D36: 2E 5D           LD      L,$5D               
5D38: A5              AND     L                   
5D39: 5D              LD      E,L                 
5D3A: FF              RST     0X38                
5D3B: FF              RST     0X38                
5D3C: 38 5D           JR      C,$5D9B             ; {}
5D3E: 9D              SBC     L                   
5D3F: 44              LD      B,H                 
5D40: 00              NOP                         
5D41: 80              ADD     A,B                 
5D42: A2              AND     D                   
5D43: 01 A1 36        LD      BC,$36A1            
5D46: 36 A2           LD      (HL),$A2            
5D48: 34              INC     (HL)                
5D49: A3              AND     E                   
5D4A: 01 A1 36        LD      BC,$36A1            
5D4D: 36 A2           LD      (HL),$A2            
5D4F: 38 A3           JR      C,$5CF4             ; {}
5D51: 01 A1 36        LD      BC,$36A1            
5D54: 36 A2           LD      (HL),$A2            
5D56: 34              INC     (HL)                
5D57: A3              AND     E                   
5D58: 01 A1 36        LD      BC,$36A1            
5D5B: 34              INC     (HL)                
5D5C: A2              AND     D                   
5D5D: 36 01           LD      (HL),$01            
5D5F: 00              NOP                         
5D60: 9D              SBC     L                   
5D61: 64              LD      H,H                 
5D62: 00              NOP                         
5D63: 00              NOP                         
5D64: 9B              SBC     E                   
5D65: 02              LD      (BC),A              
5D66: A2              AND     D                   
5D67: 40              LD      B,B                 
5D68: 36 A1           LD      (HL),$A1            
5D6A: 40              LD      B,B                 
5D6B: 44              LD      B,H                 
5D6C: 48              LD      C,B                 
5D6D: 4A              LD      C,D                 
5D6E: A2              AND     D                   
5D6F: 4E              LD      C,(HL)              
5D70: A0              AND     B                   
5D71: 56              LD      D,(HL)              
5D72: A1              AND     C                   
5D73: 58              LD      E,B                 
5D74: A0              AND     B                   
5D75: 01 A2 4E        LD      BC,$4EA2            
5D78: 01 9C 00        LD      BC,$009C            
5D7B: 99              SBC     C                   
5D7C: A2              AND     D                   
5D7D: 28 A1           JR      Z,$5D20             ; {}
5D7F: 40              LD      B,B                 
5D80: 40              LD      B,B                 
5D81: A2              AND     D                   
5D82: 3E A1           LD      A,$A1               
5D84: 36 36           LD      (HL),$36            
5D86: A2              AND     D                   
5D87: 28 A1           JR      Z,$5D2A             ; {}
5D89: 40              LD      B,B                 
5D8A: 40              LD      B,B                 
5D8B: A2              AND     D                   
5D8C: 42              LD      B,D                 
5D8D: A1              AND     C                   
5D8E: 2A              LD      A,(HLI)             
5D8F: 2A              LD      A,(HLI)             
5D90: A2              AND     D                   
5D91: 28 A1           JR      Z,$5D34             ; {}
5D93: 40              LD      B,B                 
5D94: 40              LD      B,B                 
5D95: A2              AND     D                   
5D96: 3E A1           LD      A,$A1               
5D98: 36 36           LD      (HL),$36            
5D9A: A2              AND     D                   
5D9B: 28 A1           JR      Z,$5D3E             ; {}
5D9D: 40              LD      B,B                 
5D9E: 3E A2           LD      A,$A2               
5DA0: 40              LD      B,B                 
5DA1: A1              AND     C                   
5DA2: 28 28           JR      Z,$5DCC             ; {}
5DA4: 00              NOP                         
5DA5: A2              AND     D                   
5DA6: 29              ADD     HL,HL               
5DA7: A1              AND     C                   
5DA8: 29              ADD     HL,HL               
5DA9: 29              ADD     HL,HL               
5DAA: A2              AND     D                   
5DAB: FF              RST     0X38                
5DAC: A1              AND     C                   
5DAD: 29              ADD     HL,HL               
5DAE: 29              ADD     HL,HL               
5DAF: A1              AND     C                   
5DB0: 29              ADD     HL,HL               
5DB1: 29              ADD     HL,HL               
5DB2: 29              ADD     HL,HL               
5DB3: 29              ADD     HL,HL               
5DB4: A2              AND     D                   
5DB5: FF              RST     0X38                
5DB6: 1A              LD      A,(DE)              
5DB7: 00              NOP                         
5DB8: 00              NOP                         
5DB9: 3A              LD      A,(HLD)             
5DBA: 4A              LD      C,D                 
5DBB: C3 5D D3        JP      $D35D               
5DBE: 5D              LD      E,L                 
5DBF: E1              POP     HL                  
5DC0: 5D              LD      E,L                 
5DC1: 00              NOP                         
5DC2: 00              NOP                         
5DC3: F1              POP     AF                  
5DC4: 5D              LD      E,L                 
5DC5: 01 70 A5        LD      BC,$A570            
5DC8: 6F              LD      L,A                 
5DC9: F6 5D           OR      $5D                 
5DCB: A2              AND     D                   
5DCC: 6F              LD      L,A                 
5DCD: F6 5D           OR      $5D                 
5DCF: FF              RST     0X38                
5DD0: FF              RST     0X38                
5DD1: C7              RST     0X00                
5DD2: 5D              LD      E,L                 
5DD3: B8              CP      B                   
5DD4: 6F              LD      L,A                 
5DD5: A5              AND     L                   
5DD6: 6F              LD      L,A                 
5DD7: F6 5D           OR      $5D                 
5DD9: A2              AND     D                   
5DDA: 6F              LD      L,A                 
5DDB: F6 5D           OR      $5D                 
5DDD: FF              RST     0X38                
5DDE: FF              RST     0X38                
5DDF: D3                              
5DE0: 5D              LD      E,L                 
5DE1: FB              EI                          
5DE2: 6F              LD      L,A                 
5DE3: E6 6E           AND     $6E                 
5DE5: A5              AND     L                   
5DE6: 6F              LD      L,A                 
5DE7: F6 5D           OR      $5D                 
5DE9: A2              AND     D                   
5DEA: 6F              LD      L,A                 
5DEB: F6 5D           OR      $5D                 
5DED: FF              RST     0X38                
5DEE: FF              RST     0X38                
5DEF: E3                              
5DF0: 5D              LD      E,L                 
5DF1: 9D              SBC     L                   
5DF2: 44              LD      B,H                 
5DF3: 00              NOP                         
5DF4: 80              ADD     A,B                 
5DF5: 00              NOP                         
5DF6: A2              AND     D                   
5DF7: 30 34           JR      NC,$5E2D            ; {}
5DF9: 3A              LD      A,(HLD)             
5DFA: 40              LD      B,B                 
5DFB: 48              LD      C,B                 
5DFC: 4C              LD      C,H                 
5DFD: 52              LD      D,D                 
5DFE: 58              LD      E,B                 
5DFF: 60              LD      H,B                 
5E00: 64              LD      H,H                 
5E01: 6A              LD      L,D                 
5E02: 70              LD      (HL),B              
5E03: 78              LD      A,B                 
5E04: 7C              LD      A,H                 
5E05: 82              ADD     A,D                 
5E06: 88              ADC     A,B                 
5E07: 00              NOP                         
5E08: 00              NOP                         
5E09: 3A              LD      A,(HLD)             
5E0A: 4A              LD      C,D                 
5E0B: 13              INC     DE                  
5E0C: 5E              LD      E,(HL)              
5E0D: 19              ADD     HL,DE               
5E0E: 5E              LD      E,(HL)              
5E0F: 1F              RRA                         
5E10: 5E              LD      E,(HL)              
5E11: 00              NOP                         
5E12: 00              NOP                         
5E13: 5B              LD      E,E                 
5E14: 50              LD      D,B                 
5E15: FF              RST     0X38                
5E16: FF              RST     0X38                
5E17: 13              INC     DE                  
5E18: 5E              LD      E,(HL)              
5E19: D9              RETI                        
5E1A: 50              LD      D,B                 
5E1B: FF              RST     0X38                
5E1C: FF              RST     0X38                
5E1D: 19              ADD     HL,DE               
5E1E: 5E              LD      E,(HL)              
5E1F: C2 6E 7E        JP      NZ,$7E6E            ; {}
5E22: 51              LD      D,C                 
5E23: FF              RST     0X38                
5E24: FF              RST     0X38                
5E25: 1F              RRA                         
5E26: 5E              LD      E,(HL)              
5E27: 00              NOP                         
5E28: 2B              DEC     HL                  
5E29: 4A              LD      C,D                 
5E2A: 32              LD      (HLD),A             
5E2B: 5E              LD      E,(HL)              
5E2C: 52              LD      D,D                 
5E2D: 5E              LD      E,(HL)              
5E2E: 5E              LD      E,(HL)              
5E2F: 5E              LD      E,(HL)              
5E30: 00              NOP                         
5E31: 00              NOP                         
5E32: A5              AND     L                   
5E33: 6F              LD      L,A                 
5E34: 0F              RRCA                        
5E35: 6F              LD      L,A                 
5E36: 6E              LD      L,(HL)              
5E37: 5E              LD      E,(HL)              
5E38: 6E              LD      L,(HL)              
5E39: 5E              LD      E,(HL)              
5E3A: 14              INC     D                   
5E3B: 6F              LD      L,A                 
5E3C: 6E              LD      L,(HL)              
5E3D: 5E              LD      E,(HL)              
5E3E: 6E              LD      L,(HL)              
5E3F: 5E              LD      E,(HL)              
5E40: A2              AND     D                   
5E41: 6F              LD      L,A                 
5E42: 0F              RRCA                        
5E43: 6F              LD      L,A                 
5E44: 6E              LD      L,(HL)              
5E45: 5E              LD      E,(HL)              
5E46: 6E              LD      L,(HL)              
5E47: 5E              LD      E,(HL)              
5E48: 14              INC     D                   
5E49: 6F              LD      L,A                 
5E4A: 6E              LD      L,(HL)              
5E4B: 5E              LD      E,(HL)              
5E4C: 6E              LD      L,(HL)              
5E4D: 5E              LD      E,(HL)              
5E4E: FF              RST     0X38                
5E4F: FF              RST     0X38                
5E50: 32              LD      (HLD),A             
5E51: 5E              LD      E,(HL)              
5E52: 78              LD      A,B                 
5E53: 5E              LD      E,(HL)              
5E54: 91              SUB     C                   
5E55: 5E              LD      E,(HL)              
5E56: 78              LD      A,B                 
5E57: 5E              LD      E,(HL)              
5E58: 91              SUB     C                   
5E59: 5E              LD      E,(HL)              
5E5A: FF              RST     0X38                
5E5B: FF              RST     0X38                
5E5C: 52              LD      D,D                 
5E5D: 5E              LD      E,(HL)              
5E5E: EC                              
5E5F: 6E              LD      L,(HL)              
5E60: A0              AND     B                   
5E61: 5E              LD      E,(HL)              
5E62: A0              AND     B                   
5E63: 5E              LD      E,(HL)              
5E64: F6 6E           OR      $6E                 
5E66: A0              AND     B                   
5E67: 5E              LD      E,(HL)              
5E68: A0              AND     B                   
5E69: 5E              LD      E,(HL)              
5E6A: FF              RST     0X38                
5E6B: FF              RST     0X38                
5E6C: 5E              LD      E,(HL)              
5E6D: 5E              LD      E,(HL)              
5E6E: 9B              SBC     E                   
5E6F: 02              LD      (BC),A              
5E70: A2              AND     D                   
5E71: 1C              INC     E                   
5E72: 20 20           JR      NZ,$5E94            ; {}
5E74: 9C              SBC     H                   
5E75: 1C              INC     E                   
5E76: 20 00           JR      NZ,$5E78            ; {}
5E78: 9D              SBC     L                   
5E79: 70              LD      (HL),B              
5E7A: 21 40 A7        LD      HL,$A740            
5E7D: 48              LD      C,B                 
5E7E: A1              AND     C                   
5E7F: 44              LD      B,H                 
5E80: 48              LD      C,B                 
5E81: A7              AND     A                   
5E82: 4A              LD      C,D                 
5E83: A1              AND     C                   
5E84: 48              LD      C,B                 
5E85: 4A              LD      C,D                 
5E86: A7              AND     A                   
5E87: 4C              LD      C,H                 
5E88: A1              AND     C                   
5E89: 5C              LD      E,H                 
5E8A: 58              LD      E,B                 
5E8B: A2              AND     D                   
5E8C: 4C              LD      C,H                 
5E8D: 64              LD      H,H                 
5E8E: A3              AND     E                   
5E8F: 64              LD      H,H                 
5E90: 00              NOP                         
5E91: 9D              SBC     L                   
5E92: 20 21           JR      NZ,$5EB5            ; {}
5E94: 81              ADD     A,C                 
5E95: A2              AND     D                   
5E96: 4C              LD      C,H                 
5E97: 64              LD      H,H                 
5E98: A8              XOR     B                   
5E99: 64              LD      H,H                 
5E9A: A2              AND     D                   
5E9B: 64              LD      H,H                 
5E9C: 7C              LD      A,H                 
5E9D: A8              XOR     B                   
5E9E: 7C              LD      A,H                 
5E9F: 00              NOP                         
5EA0: 99              SBC     C                   
5EA1: A7              AND     A                   
5EA2: 28 28           JR      Z,$5ECC             ; {}
5EA4: A3              AND     E                   
5EA5: 28 00           JR      Z,$5EA7             ; {}
5EA7: 00              NOP                         
5EA8: 2B              DEC     HL                  
5EA9: 4A              LD      C,D                 
5EAA: B2              OR      D                   
5EAB: 5E              LD      E,(HL)              
5EAC: BA              CP      D                   
5EAD: 5E              LD      E,(HL)              
5EAE: C2 5E 00        JP      NZ,$005E            
5EB1: 00              NOP                         
5EB2: CC 5E D1        CALL    Z,$D15E             
5EB5: 5E              LD      E,(HL)              
5EB6: DB                              
5EB7: 5E              LD      E,(HL)              
5EB8: 00              NOP                         
5EB9: 00              NOP                         
5EBA: D6 5E           SUB     $5E                 
5EBC: DB                              
5EBD: 5E              LD      E,(HL)              
5EBE: D1              POP     DE                  
5EBF: 5E              LD      E,(HL)              
5EC0: 00              NOP                         
5EC1: 00              NOP                         
5EC2: D6 6E           SUB     $6E                 
5EC4: 04              INC     B                   
5EC5: 70              LD      (HL),B              
5EC6: DB                              
5EC7: 5E              LD      E,(HL)              
5EC8: FB              EI                          
5EC9: 6F              LD      L,A                 
5ECA: 00              NOP                         
5ECB: 00              NOP                         
5ECC: 9D              SBC     L                   
5ECD: 26 00           LD      H,$00               
5ECF: 80              ADD     A,B                 
5ED0: 00              NOP                         
5ED1: A3              AND     E                   
5ED2: 01 A1 01        LD      BC,$01A1            
5ED5: 00              NOP                         
5ED6: 9D              SBC     L                   
5ED7: 67              LD      H,A                 
5ED8: 00              NOP                         
5ED9: 81              ADD     A,C                 
5EDA: 00              NOP                         
5EDB: 96              SUB     (HL)                
5EDC: A1              AND     C                   
5EDD: 70              LD      (HL),B              
5EDE: 6E              LD      L,(HL)              
5EDF: 66              LD      H,(HL)              
5EE0: 60              LD      H,B                 
5EE1: 58              LD      E,B                 
5EE2: 56              LD      D,(HL)              
5EE3: 4E              LD      C,(HL)              
5EE4: 48              LD      C,B                 
5EE5: 74              LD      (HL),H              
5EE6: 70              LD      (HL),B              
5EE7: 6A              LD      L,D                 
5EE8: 62              LD      H,D                 
5EE9: 5C              LD      E,H                 
5EEA: 58              LD      E,B                 
5EEB: 52              LD      D,D                 
5EEC: 4A              LD      C,D                 
5EED: 78              LD      A,B                 
5EEE: 74              LD      (HL),H              
5EEF: 6E              LD      L,(HL)              
5EF0: 66              LD      H,(HL)              
5EF1: 60              LD      H,B                 
5EF2: 5C              LD      E,H                 
5EF3: 56              LD      D,(HL)              
5EF4: 4E              LD      C,(HL)              
5EF5: 7A              LD      A,D                 
5EF6: 78              LD      A,B                 
5EF7: 70              LD      (HL),B              
5EF8: 6A              LD      L,D                 
5EF9: 62              LD      H,D                 
5EFA: 60              LD      H,B                 
5EFB: 58              LD      E,B                 
5EFC: 52              LD      D,D                 
5EFD: A2              AND     D                   
5EFE: 36 44           LD      (HL),$44            
5F00: 4A              LD      C,D                 
5F01: 4E              LD      C,(HL)              
5F02: 56              LD      D,(HL)              
5F03: 5C              LD      E,H                 
5F04: 62              LD      H,D                 
5F05: 66              LD      H,(HL)              
5F06: A8              XOR     B                   
5F07: 7E              LD      A,(HL)              
5F08: 95              SUB     L                   
5F09: 00              NOP                         
5F0A: 00              NOP                         
5F0B: 3A              LD      A,(HLD)             
5F0C: 4A              LD      C,D                 
5F0D: 15              DEC     D                   
5F0E: 5F              LD      E,A                 
5F0F: 1B              DEC     DE                  
5F10: 5F              LD      E,A                 
5F11: 21 5F 00        LD      HL,$005F            
5F14: 00              NOP                         
5F15: 29              ADD     HL,HL               
5F16: 5F              LD      E,A                 
5F17: FF              RST     0X38                
5F18: FF              RST     0X38                
5F19: 12              LD      (DE),A              
5F1A: 54              LD      D,H                 
5F1B: 5C              LD      E,H                 
5F1C: 5F              LD      E,A                 
5F1D: FF              RST     0X38                
5F1E: FF              RST     0X38                
5F1F: 20 54           JR      NZ,$5F75            ; {}
5F21: C2 6E 85        JP      NZ,$856E            
5F24: 5F              LD      E,A                 
5F25: FF              RST     0X38                
5F26: FF              RST     0X38                
5F27: 30 54           JR      NC,$5F7D            ; {}
5F29: 9D              SBC     L                   
5F2A: 70              LD      (HL),B              
5F2B: 21 81 AA        LD      HL,$AA81            
5F2E: 01 36 40        LD      BC,$4036            
5F31: A3              AND     E                   
5F32: 48              LD      C,B                 
5F33: AA              XOR     D                   
5F34: 48              LD      C,B                 
5F35: 48              LD      C,B                 
5F36: 44              LD      B,H                 
5F37: A3              AND     E                   
5F38: 48              LD      C,B                 
5F39: AA              XOR     D                   
5F3A: 01 3C 46        LD      BC,$463C            
5F3D: A3              AND     E                   
5F3E: 4E              LD      C,(HL)              
5F3F: AA              XOR     D                   
5F40: 4E              LD      C,(HL)              
5F41: 4E              LD      C,(HL)              
5F42: 4A              LD      C,D                 
5F43: A3              AND     E                   
5F44: 4E              LD      C,(HL)              
5F45: A3              AND     E                   
5F46: 01 9B 02        LD      BC,$029B            
5F49: A3              AND     E                   
5F4A: 4C              LD      C,H                 
5F4B: A2              AND     D                   
5F4C: 01 A1 4C        LD      BC,$4CA1            
5F4F: 4C              LD      C,H                 
5F50: 9C              SBC     H                   
5F51: A8              XOR     B                   
5F52: 4A              LD      C,D                 
5F53: 9D              SBC     L                   
5F54: 40              LD      B,B                 
5F55: 21 80 AA        LD      HL,$AA80            
5F58: 32              LD      (HLD),A             
5F59: 30 2C           JR      NC,$5F87            ; {}
5F5B: 00              NOP                         
5F5C: 9D              SBC     L                   
5F5D: 90              SUB     B                   
5F5E: 21 81 AA        LD      HL,$AA81            
5F61: 36 40           LD      (HL),$40            
5F63: 48              LD      C,B                 
5F64: A8              XOR     B                   
5F65: 4E              LD      C,(HL)              
5F66: AA              XOR     D                   
5F67: 3C              INC     A                   
5F68: 46              LD      B,(HL)              
5F69: 4E              LD      C,(HL)              
5F6A: A8              XOR     B                   
5F6B: 54              LD      D,H                 
5F6C: AA              XOR     D                   
5F6D: 4E              LD      C,(HL)              
5F6E: 54              LD      D,H                 
5F6F: 5E              LD      E,(HL)              
5F70: 9B              SBC     E                   
5F71: 02              LD      (BC),A              
5F72: A3              AND     E                   
5F73: 5A              LD      E,D                 
5F74: A2              AND     D                   
5F75: 01 A1 5A        LD      BC,$5AA1            
5F78: 5A              LD      E,D                 
5F79: 9C              SBC     H                   
5F7A: A8              XOR     B                   
5F7B: 5C              LD      E,H                 
5F7C: 9D              SBC     L                   
5F7D: 60              LD      H,B                 
5F7E: 21 80 AA        LD      HL,$AA80            
5F81: 44              LD      B,H                 
5F82: 40              LD      B,B                 
5F83: 3E 00           LD      A,$00               
5F85: 99              SBC     C                   
5F86: AA              XOR     D                   
5F87: 01 01 4E        LD      BC,$4E01            
5F8A: 9A              SBC     D                   
5F8B: A3              AND     E                   
5F8C: 58              LD      E,B                 
5F8D: 99              SBC     C                   
5F8E: AA              XOR     D                   
5F8F: 40              LD      B,B                 
5F90: 40              LD      B,B                 
5F91: 3C              INC     A                   
5F92: 9A              SBC     D                   
5F93: A3              AND     E                   
5F94: 40              LD      B,B                 
5F95: 99              SBC     C                   
5F96: AA              XOR     D                   
5F97: 01 01 54        LD      BC,$5401            
5F9A: 9A              SBC     D                   
5F9B: A3              AND     E                   
5F9C: 5E              LD      E,(HL)              
5F9D: 99              SBC     C                   
5F9E: AA              XOR     D                   
5F9F: 46              LD      B,(HL)              
5FA0: 46              LD      B,(HL)              
5FA1: 42              LD      B,D                 
5FA2: 9A              SBC     D                   
5FA3: A3              AND     E                   
5FA4: 46              LD      B,(HL)              
5FA5: 01 99 AA        LD      BC,$AA99            
5FA8: 2A              LD      A,(HLI)             
5FA9: 28 2A           JR      Z,$5FD5             ; {}
5FAB: 34              INC     (HL)                
5FAC: 32              LD      (HLD),A             
5FAD: 34              INC     (HL)                
5FAE: 3C              INC     A                   
5FAF: 3A              LD      A,(HLD)             
5FB0: 3C              INC     A                   
5FB1: 42              LD      B,D                 
5FB2: 4C              LD      C,H                 
5FB3: 54              LD      D,H                 
5FB4: 56              LD      D,(HL)              
5FB5: 52              LD      D,D                 
5FB6: 56              LD      D,(HL)              
5FB7: 58              LD      E,B                 
5FB8: 56              LD      D,(HL)              
5FB9: 52              LD      D,D                 
5FBA: A3              AND     E                   
5FBB: 4E              LD      C,(HL)              
5FBC: AA              XOR     D                   
5FBD: 1E 1E           LD      E,$1E               
5FBF: 1E 00           LD      E,$00               
5FC1: 00              NOP                         
5FC2: 58              LD      E,B                 
5FC3: 4A              LD      C,D                 
5FC4: CC 5F D4        CALL    Z,$D45F             
5FC7: 5F              LD      E,A                 
5FC8: 8C              ADC     A,H                 
5FC9: 4A              LD      C,D                 
5FCA: 00              NOP                         
5FCB: 00              NOP                         
5FCC: 37              SCF                         
5FCD: 6F              LD      L,A                 
5FCE: DC 5F FF        CALL    C,$FF5F             
5FD1: FF              RST     0X38                
5FD2: CC 5F 3C        CALL    Z,$3C5F             
5FD5: 6F              LD      L,A                 
5FD6: FE 5F           CP      $5F                 
5FD8: FF              RST     0X38                
5FD9: FF              RST     0X38                
5FDA: D4 5F A2        CALL    NC,$A25F            
5FDD: 32              LD      (HLD),A             
5FDE: 3A              LD      A,(HLD)             
5FDF: 40              LD      B,B                 
5FE0: 3A              LD      A,(HLD)             
5FE1: 32              LD      (HLD),A             
5FE2: 36 3E           LD      (HL),$3E            
5FE4: 44              LD      B,H                 
5FE5: 30 36           JR      NC,$601D            ; {}
5FE7: 3E 44           LD      A,$44               
5FE9: 22              LD      (HLI),A             
5FEA: 28 30           JR      Z,$601C             ; {}
5FEC: 28 2C           JR      Z,$601A             ; {}
5FEE: 32              LD      (HLD),A             
5FEF: 3A              LD      A,(HLD)             
5FF0: 32              LD      (HLD),A             
5FF1: 1E 26           LD      E,$26               
5FF3: 2C              INC     L                   
5FF4: 26 28           LD      H,$28               
5FF6: 2C              INC     L                   
5FF7: 32              LD      (HLD),A             
5FF8: 36 28           LD      (HL),$28            
5FFA: 30 36           JR      NC,$6032            ; {}
5FFC: 3C              INC     A                   
5FFD: 00              NOP                         
5FFE: A4              AND     H                   
5FFF: 70              LD      (HL),B              
6000: A2              AND     D                   
6001: 01 6E 74        LD      BC,$746E            
6004: A4              AND     H                   
6005: 66              LD      H,(HL)              
6006: A2              AND     D                   
6007: 01 70 58        LD      BC,$5870            
600A: 5C              LD      E,H                 
600B: 60              LD      H,B                 
600C: 62              LD      H,D                 
600D: 60              LD      H,B                 
600E: 62              LD      H,D                 
600F: A3              AND     E                   
6010: 56              LD      D,(HL)              
6011: 6A              LD      L,D                 
6012: A5              AND     L                   
6013: 66              LD      H,(HL)              
6014: A2              AND     D                   
6015: 01 00 00        LD      BC,$0000            
6018: 2B              DEC     HL                  
6019: 4A              LD      C,D                 
601A: 22              LD      (HLI),A             
601B: 60              LD      H,B                 
601C: 38 60           JR      C,$607E             ; {}
601E: 8C              ADC     A,H                 
601F: 4A              LD      C,D                 
6020: 00              NOP                         
6021: 00              NOP                         
6022: 59              LD      E,C                 
6023: 60              LD      H,B                 
6024: 65              LD      H,L                 
6025: 60              LD      H,B                 
6026: 4E              LD      C,(HL)              
6027: 60              LD      H,B                 
6028: 4E              LD      C,(HL)              
6029: 60              LD      H,B                 
602A: 59              LD      E,C                 
602B: 60              LD      H,B                 
602C: 6A              LD      L,D                 
602D: 60              LD      H,B                 
602E: 4E              LD      C,(HL)              
602F: 60              LD      H,B                 
6030: 4E              LD      C,(HL)              
6031: 60              LD      H,B                 
6032: 4E              LD      C,(HL)              
6033: 60              LD      H,B                 
6034: FF              RST     0X38                
6035: FF              RST     0X38                
6036: 22              LD      (HLI),A             
6037: 60              LD      H,B                 
6038: 7E              LD      A,(HL)              
6039: 60              LD      H,B                 
603A: 8A              ADC     A,D                 
603B: 60              LD      H,B                 
603C: 6F              LD      L,A                 
603D: 60              LD      H,B                 
603E: 6F              LD      L,A                 
603F: 60              LD      H,B                 
6040: 7E              LD      A,(HL)              
6041: 60              LD      H,B                 
6042: 90              SUB     B                   
6043: 60              LD      H,B                 
6044: 6F              LD      L,A                 
6045: 60              LD      H,B                 
6046: 6F              LD      L,A                 
6047: 60              LD      H,B                 
6048: 6F              LD      L,A                 
6049: 60              LD      H,B                 
604A: FF              RST     0X38                
604B: FF              RST     0X38                
604C: 38 60           JR      C,$60AE             ; {}
604E: 9B              SBC     E                   
604F: 0C              INC     C                   
6050: AD              XOR     L                   
6051: 01 01 01        LD      BC,$0101            
6054: 01 9C A5        LD      BC,$A59C            
6057: 01 00 9D        LD      BC,$9D00            
605A: 40              LD      B,B                 
605B: 41              LD      B,C                 
605C: 80              ADD     A,B                 
605D: 9B              SBC     E                   
605E: 02              LD      (BC),A              
605F: A3              AND     E                   
6060: 28 32           JR      Z,$6094             ; {}
6062: 32              LD      (HLD),A             
6063: 9C              SBC     H                   
6064: 00              NOP                         
6065: A3              AND     E                   
6066: 30 26           JR      NC,$608E            ; {}
6068: 01 00 A3        LD      BC,$A300            
606B: 34              INC     (HL)                
606C: 2A              LD      A,(HLI)             
606D: 01 00 9D        LD      BC,$9D00            
6070: 42              LD      B,D                 
6071: 00              NOP                         
6072: 80              ADD     A,B                 
6073: 9B              SBC     E                   
6074: 0C              INC     C                   
6075: AD              XOR     L                   
6076: 46              LD      B,(HL)              
6077: 44              LD      B,H                 
6078: 46              LD      B,(HL)              
6079: 01 9C A5        LD      BC,$A59C            
607C: 01 00 9D        LD      BC,$9D00            
607F: 40              LD      B,B                 
6080: 41              LD      B,C                 
6081: 80              ADD     A,B                 
6082: 9B              SBC     E                   
6083: 02              LD      (BC),A              
6084: A3              AND     E                   
6085: 30 3A           JR      NC,$60C1            ; {}
6087: 3A              LD      A,(HLD)             
6088: 9C              SBC     H                   
6089: 00              NOP                         
608A: A3              AND     E                   
608B: 38 2E           JR      C,$60BB             ; {}
608D: A3              AND     E                   
608E: 01 00 A3        LD      BC,$A300            
6091: 3C              INC     A                   
6092: 32              LD      (HLD),A             
6093: A3              AND     E                   
6094: 01 00 00        LD      BC,$0000            
6097: 49              LD      C,C                 
6098: 4A              LD      C,D                 
6099: 8C              ADC     A,H                 
609A: 4A              LD      C,D                 
609B: A1              AND     C                   
609C: 60              LD      H,B                 
609D: B1              OR      C                   
609E: 60              LD      H,B                 
609F: 00              NOP                         
60A0: 00              NOP                         
60A1: C1              POP     BC                  
60A2: 60              LD      H,B                 
60A3: D9              RETI                        
60A4: 60              LD      H,B                 
60A5: D9              RETI                        
60A6: 60              LD      H,B                 
60A7: FA 60 B3        LD      A,($B360)           
60AA: 6F              LD      L,A                 
60AB: 0F              RRCA                        
60AC: 61              LD      H,C                 
60AD: 01 70 00        LD      BC,$0070            
60B0: 00              NOP                         
60B1: CC 6E 1D        CALL    Z,$1D6E             
60B4: 61              LD      H,C                 
60B5: 29              ADD     HL,HL               
60B6: 61              LD      H,C                 
60B7: D6 6E           SUB     $6E                 
60B9: 4C              LD      C,H                 
60BA: 61              LD      H,C                 
60BB: 59              LD      E,C                 
60BC: 61              LD      H,C                 
60BD: 0F              RRCA                        
60BE: 61              LD      H,C                 
60BF: 00              NOP                         
60C0: 00              NOP                         
60C1: 9D              SBC     L                   
60C2: 43              LD      B,E                 
60C3: 00              NOP                         
60C4: 80              ADD     A,B                 
60C5: A4              AND     H                   
60C6: 01 A2 01        LD      BC,$01A2            
60C9: A1              AND     C                   
60CA: 78              LD      A,B                 
60CB: 74              LD      (HL),H              
60CC: A2              AND     D                   
60CD: 78              LD      A,B                 
60CE: A3              AND     E                   
60CF: 01 A1 7A        LD      BC,$7AA1            
60D2: 78              LD      A,B                 
60D3: A2              AND     D                   
60D4: 7A              LD      A,D                 
60D5: A3              AND     E                   
60D6: 01 01 00        LD      BC,$0001            
60D9: 9D              SBC     L                   
60DA: 55              LD      D,L                 
60DB: 00              NOP                         
60DC: 00              NOP                         
60DD: 9E              SBC     (HL)                
60DE: 2B              DEC     HL                  
60DF: 4A              LD      C,D                 
60E0: 9B              SBC     E                   
60E1: 02              LD      (BC),A              
60E2: A1              AND     C                   
60E3: 66              LD      H,(HL)              
60E4: 68              LD      L,B                 
60E5: 66              LD      H,(HL)              
60E6: 64              LD      H,H                 
60E7: 62              LD      H,D                 
60E8: 64              LD      H,H                 
60E9: 62              LD      H,D                 
60EA: 64              LD      H,H                 
60EB: 9C              SBC     H                   
60EC: A2              AND     D                   
60ED: 66              LD      H,(HL)              
60EE: 7E              LD      A,(HL)              
60EF: 66              LD      H,(HL)              
60F0: A1              AND     C                   
60F1: 66              LD      H,(HL)              
60F2: 68              LD      L,B                 
60F3: 6A              LD      L,D                 
60F4: 6C              LD      L,H                 
60F5: 6A              LD      L,D                 
60F6: 68              LD      L,B                 
60F7: A3              AND     E                   
60F8: 66              LD      H,(HL)              
60F9: 00              NOP                         
60FA: 9D              SBC     L                   
60FB: 35              DEC     (HL)                
60FC: 00              NOP                         
60FD: 40              LD      B,B                 
60FE: 9B              SBC     E                   
60FF: 02              LD      (BC),A              
6100: A1              AND     C                   
6101: 66              LD      H,(HL)              
6102: 68              LD      L,B                 
6103: 66              LD      H,(HL)              
6104: 64              LD      H,H                 
6105: 62              LD      H,D                 
6106: 64              LD      H,H                 
6107: 62              LD      H,D                 
6108: 64              LD      H,H                 
6109: 9C              SBC     H                   
610A: A5              AND     L                   
610B: 01 A3 01        LD      BC,$01A3            
610E: 00              NOP                         
610F: 9E              SBC     (HL)                
6110: 3A              LD      A,(HLD)             
6111: 4A              LD      C,D                 
6112: A0              AND     B                   
6113: 7E              LD      A,(HL)              
6114: 7A              LD      A,D                 
6115: 76              HALT                        
6116: 72              LD      (HL),D              
6117: 6E              LD      L,(HL)              
6118: 6A              LD      L,D                 
6119: A3              AND     E                   
611A: 66              LD      H,(HL)              
611B: 01 00 A4        LD      BC,$A400            
611E: 01 A2 01        LD      BC,$01A2            
6121: 99              SBC     C                   
6122: A3              AND     E                   
6123: 6C              LD      L,H                 
6124: 01 6E 01        LD      BC,$016E            
6127: 01 00 9E        LD      BC,$9E00            
612A: 2B              DEC     HL                  
612B: 4A              LD      C,D                 
612C: 99              SBC     C                   
612D: 9B              SBC     E                   
612E: 02              LD      (BC),A              
612F: A2              AND     D                   
6130: 40              LD      B,B                 
6131: 4E              LD      C,(HL)              
6132: 36 4E           LD      (HL),$4E            
6134: 9C              SBC     H                   
6135: 9B              SBC     E                   
6136: 02              LD      (BC),A              
6137: 42              LD      B,D                 
6138: 50              LD      D,B                 
6139: 38 50           JR      C,$618B             ; {}
613B: 9C              SBC     H                   
613C: 9B              SBC     E                   
613D: 02              LD      (BC),A              
613E: 46              LD      B,(HL)              
613F: 54              LD      D,H                 
6140: 3C              INC     A                   
6141: 54              LD      D,H                 
6142: 9C              SBC     H                   
6143: 4A              LD      C,D                 
6144: 58              LD      E,B                 
6145: 40              LD      B,B                 
6146: 58              LD      E,B                 
6147: 4A              LD      C,D                 
6148: 58              LD      E,B                 
6149: 48              LD      C,B                 
614A: 44              LD      B,H                 
614B: 00              NOP                         
614C: 9B              SBC     E                   
614D: 02              LD      (BC),A              
614E: A2              AND     D                   
614F: 40              LD      B,B                 
6150: 4E              LD      C,(HL)              
6151: 36 4E           LD      (HL),$4E            
6153: 9C              SBC     H                   
6154: A5              AND     L                   
6155: 01 A3 01        LD      BC,$01A3            
6158: 00              NOP                         
6159: 9E              SBC     (HL)                
615A: 3A              LD      A,(HLD)             
615B: 4A              LD      C,D                 
615C: A1              AND     C                   
615D: 01 00 00        LD      BC,$0000            
6160: 49              LD      C,C                 
6161: 4A              LD      C,D                 
6162: 6A              LD      L,D                 
6163: 61              LD      H,C                 
6164: 76              HALT                        
6165: 61              LD      H,C                 
6166: 82              ADD     A,D                 
6167: 61              LD      H,C                 
6168: 00              NOP                         
6169: 00              NOP                         
616A: 41              LD      B,C                 
616B: 6F              LD      L,A                 
616C: 8C              ADC     A,H                 
616D: 61              LD      H,C                 
616E: 46              LD      B,(HL)              
616F: 6F              LD      L,A                 
6170: 9A              SBC     D                   
6171: 61              LD      H,C                 
6172: 9A              SBC     D                   
6173: 61              LD      H,C                 
6174: 00              NOP                         
6175: 00              NOP                         
6176: 41              LD      B,C                 
6177: 6F              LD      L,A                 
6178: C8              RET     Z                   
6179: 61              LD      H,C                 
617A: 46              LD      B,(HL)              
617B: 6F              LD      L,A                 
617C: D6 61           SUB     $61                 
617E: D6 61           SUB     $61                 
6180: 00              NOP                         
6181: 00              NOP                         
6182: F1              POP     AF                  
6183: 6E              LD      L,(HL)              
6184: 04              INC     B                   
6185: 62              LD      H,D                 
6186: 11 62 11        LD      DE,$1162            
6189: 62              LD      H,D                 
618A: 00              NOP                         
618B: 00              NOP                         
618C: A4              AND     H                   
618D: 01 A1 26        LD      BC,$26A1            
6190: 2A              LD      A,(HLI)             
6191: 2E 30           LD      L,$30               
6193: 34              INC     (HL)                
6194: 01 34 01        LD      BC,$0134            
6197: A5              AND     L                   
6198: 36 00           LD      (HL),$00            
619A: A4              AND     H                   
619B: 01 A2 34        LD      BC,$34A2            
619E: 38 3C           JR      C,$61DC             ; {}
61A0: 3E A7           LD      A,$A7               
61A2: 42              LD      B,D                 
61A3: A2              AND     D                   
61A4: 46              LD      B,(HL)              
61A5: 42              LD      B,D                 
61A6: 3E 3C           LD      A,$3C               
61A8: 38 A4           JR      C,$614E             ; {}
61AA: 34              INC     (HL)                
61AB: A2              AND     D                   
61AC: 3C              INC     A                   
61AD: 3E 42           LD      A,$42               
61AF: 4C              LD      C,H                 
61B0: A7              AND     A                   
61B1: 54              LD      D,H                 
61B2: A2              AND     D                   
61B3: 56              LD      D,(HL)              
61B4: 54              LD      D,H                 
61B5: 50              LD      D,B                 
61B6: 4C              LD      C,H                 
61B7: 4A              LD      C,D                 
61B8: A7              AND     A                   
61B9: 4C              LD      C,H                 
61BA: A1              AND     C                   
61BB: 42              LD      B,D                 
61BC: 42              LD      B,D                 
61BD: 9B              SBC     E                   
61BE: 02              LD      (BC),A              
61BF: A2              AND     D                   
61C0: 4C              LD      C,H                 
61C1: A1              AND     C                   
61C2: 42              LD      B,D                 
61C3: 42              LD      B,D                 
61C4: 9C              SBC     H                   
61C5: A5              AND     L                   
61C6: 4C              LD      C,H                 
61C7: 00              NOP                         
61C8: A5              AND     L                   
61C9: 01 A1 40        LD      BC,$40A1            
61CC: 44              LD      B,H                 
61CD: 48              LD      C,B                 
61CE: 4A              LD      C,D                 
61CF: 4E              LD      C,(HL)              
61D0: 01 4E 01        LD      BC,$014E            
61D3: A4              AND     H                   
61D4: 50              LD      D,B                 
61D5: 00              NOP                         
61D6: A5              AND     L                   
61D7: 01 A2 4E        LD      BC,$4EA2            
61DA: 52              LD      D,D                 
61DB: 56              LD      D,(HL)              
61DC: 58              LD      E,B                 
61DD: A7              AND     A                   
61DE: 5C              LD      E,H                 
61DF: A2              AND     D                   
61E0: 60              LD      H,B                 
61E1: 5C              LD      E,H                 
61E2: 58              LD      E,B                 
61E3: 56              LD      D,(HL)              
61E4: 52              LD      D,D                 
61E5: A4              AND     H                   
61E6: 4E              LD      C,(HL)              
61E7: A2              AND     D                   
61E8: 56              LD      D,(HL)              
61E9: 58              LD      E,B                 
61EA: 5C              LD      E,H                 
61EB: 66              LD      H,(HL)              
61EC: A7              AND     A                   
61ED: 6E              LD      L,(HL)              
61EE: A2              AND     D                   
61EF: 70              LD      (HL),B              
61F0: 6E              LD      L,(HL)              
61F1: 6A              LD      L,D                 
61F2: 66              LD      H,(HL)              
61F3: 64              LD      H,H                 
61F4: A7              AND     A                   
61F5: 66              LD      H,(HL)              
61F6: A1              AND     C                   
61F7: 5C              LD      E,H                 
61F8: 5C              LD      E,H                 
61F9: 9B              SBC     E                   
61FA: 02              LD      (BC),A              
61FB: A2              AND     D                   
61FC: 66              LD      H,(HL)              
61FD: A1              AND     C                   
61FE: 5C              LD      E,H                 
61FF: 5C              LD      E,H                 
6200: 9C              SBC     H                   
6201: A4              AND     H                   
6202: 66              LD      H,(HL)              
6203: 00              NOP                         
6204: 9A              SBC     D                   
6205: A1              AND     C                   
6206: 24              INC     H                   
6207: 28 2C           JR      Z,$6235             ; {}
6209: 2E 32           LD      L,$32               
620B: 01 32 01        LD      BC,$0132            
620E: AE              XOR     (HL)                
620F: 34              INC     (HL)                
6210: 00              NOP                         
6211: A2              AND     D                   
6212: 32              LD      (HLD),A             
6213: 36 3A           LD      (HL),$3A            
6215: 3C              INC     A                   
6216: A7              AND     A                   
6217: 40              LD      B,B                 
6218: A2              AND     D                   
6219: 44              LD      B,H                 
621A: 40              LD      B,B                 
621B: 3C              INC     A                   
621C: 3A              LD      A,(HLD)             
621D: 36 A4           LD      (HL),$A4            
621F: 32              LD      (HLD),A             
6220: A2              AND     D                   
6221: 3A              LD      A,(HLD)             
6222: 3C              INC     A                   
6223: 40              LD      B,B                 
6224: 4A              LD      C,D                 
6225: A7              AND     A                   
6226: 52              LD      D,D                 
6227: A2              AND     D                   
6228: 54              LD      D,H                 
6229: 52              LD      D,D                 
622A: 4E              LD      C,(HL)              
622B: 4A              LD      C,D                 
622C: 48              LD      C,B                 
622D: A3              AND     E                   
622E: 4A              LD      C,D                 
622F: A2              AND     D                   
6230: 01 99 A1        LD      BC,$A199            
6233: 40              LD      B,B                 
6234: 40              LD      B,B                 
6235: 9B              SBC     E                   
6236: 02              LD      (BC),A              
6237: A2              AND     D                   
6238: 4A              LD      C,D                 
6239: A1              AND     C                   
623A: 40              LD      B,B                 
623B: 40              LD      B,B                 
623C: 9C              SBC     H                   
623D: 9A              SBC     D                   
623E: AE              XOR     (HL)                
623F: 4A              LD      C,D                 
6240: 00              NOP                         
6241: 00              NOP                         
6242: 49              LD      C,C                 
6243: 4A              LD      C,D                 
6244: 8C              ADC     A,H                 
6245: 4A              LD      C,D                 
6246: 4C              LD      C,H                 
6247: 62              LD      H,D                 
6248: 5C              LD      E,H                 
6249: 62              LD      H,D                 
624A: 00              NOP                         
624B: 00              NOP                         
624C: 6C              LD      L,H                 
624D: 62              LD      H,D                 
624E: 71              LD      (HL),C              
624F: 62              LD      H,D                 
6250: 23              INC     HL                  
6251: 6F              LD      L,A                 
6252: 71              LD      (HL),C              
6253: 62              LD      H,D                 
6254: 82              ADD     A,D                 
6255: 62              LD      H,D                 
6256: 37              SCF                         
6257: 6F              LD      L,A                 
6258: BA              CP      D                   
6259: 62              LD      H,D                 
625A: 00              NOP                         
625B: 00              NOP                         
625C: D6 6E           SUB     $6E                 
625E: C7              RST     0X00                
625F: 62              LD      H,D                 
6260: CC 6E C7        CALL    Z,$C76E             
6263: 62              LD      H,D                 
6264: D9              RETI                        
6265: 62              LD      H,D                 
6266: D6 6E           SUB     $6E                 
6268: 00              NOP                         
6269: 63              LD      H,E                 
626A: 00              NOP                         
626B: 00              NOP                         
626C: 9D              SBC     L                   
626D: 40              LD      B,B                 
626E: 26 01           LD      H,$01               
6270: 00              NOP                         
6271: A1              AND     C                   
6272: 90              SUB     B                   
6273: A6              AND     (HL)                
6274: 90              SUB     B                   
6275: A1              AND     C                   
6276: 88              ADC     A,B                 
6277: A6              AND     (HL)                
6278: 88              ADC     A,B                 
6279: A1              AND     C                   
627A: 7E              LD      A,(HL)              
627B: A6              AND     (HL)                
627C: 7E              LD      A,(HL)              
627D: A1              AND     C                   
627E: 88              ADC     A,B                 
627F: A6              AND     (HL)                
6280: 88              ADC     A,B                 
6281: 00              NOP                         
6282: A6              AND     (HL)                
6283: 4E              LD      C,(HL)              
6284: A1              AND     C                   
6285: 4E              LD      C,(HL)              
6286: A3              AND     E                   
6287: 48              LD      C,B                 
6288: A6              AND     (HL)                
6289: 4A              LD      C,D                 
628A: A1              AND     C                   
628B: 4A              LD      C,D                 
628C: A3              AND     E                   
628D: 42              LD      B,D                 
628E: A1              AND     C                   
628F: 4E              LD      C,(HL)              
6290: A2              AND     D                   
6291: 4E              LD      C,(HL)              
6292: A1              AND     C                   
6293: 52              LD      D,D                 
6294: 4E              LD      C,(HL)              
6295: 48              LD      C,B                 
6296: 40              LD      B,B                 
6297: 48              LD      C,B                 
6298: A2              AND     D                   
6299: 4A              LD      C,D                 
629A: 90              SUB     B                   
629B: A3              AND     E                   
629C: 90              SUB     B                   
629D: A6              AND     (HL)                
629E: 4E              LD      C,(HL)              
629F: A1              AND     C                   
62A0: 4E              LD      C,(HL)              
62A1: A3              AND     E                   
62A2: 48              LD      C,B                 
62A3: A6              AND     (HL)                
62A4: 58              LD      E,B                 
62A5: A1              AND     C                   
62A6: 58              LD      E,B                 
62A7: A3              AND     E                   
62A8: 50              LD      D,B                 
62A9: A1              AND     C                   
62AA: 4E              LD      C,(HL)              
62AB: A2              AND     D                   
62AC: 4E              LD      C,(HL)              
62AD: A1              AND     C                   
62AE: 52              LD      D,D                 
62AF: A2              AND     D                   
62B0: 4E              LD      C,(HL)              
62B1: A1              AND     C                   
62B2: 58              LD      E,B                 
62B3: 60              LD      H,B                 
62B4: A2              AND     D                   
62B5: 62              LD      H,D                 
62B6: 90              SUB     B                   
62B7: A3              AND     E                   
62B8: 90              SUB     B                   
62B9: 00              NOP                         
62BA: A6              AND     (HL)                
62BB: 4E              LD      C,(HL)              
62BC: A1              AND     C                   
62BD: 4E              LD      C,(HL)              
62BE: A3              AND     E                   
62BF: 48              LD      C,B                 
62C0: A6              AND     (HL)                
62C1: 4A              LD      C,D                 
62C2: A1              AND     C                   
62C3: 4A              LD      C,D                 
62C4: A3              AND     E                   
62C5: 42              LD      B,D                 
62C6: 00              NOP                         
62C7: 99              SBC     C                   
62C8: A1              AND     C                   
62C9: 8E              ADC     A,(HL)              
62CA: A6              AND     (HL)                
62CB: 8E              ADC     A,(HL)              
62CC: A1              AND     C                   
62CD: 86              ADD     A,(HL)              
62CE: A6              AND     (HL)                
62CF: 86              ADD     A,(HL)              
62D0: A1              AND     C                   
62D1: 7C              LD      A,H                 
62D2: A6              AND     (HL)                
62D3: 7C              LD      A,H                 
62D4: A1              AND     C                   
62D5: 86              ADD     A,(HL)              
62D6: A6              AND     (HL)                
62D7: 86              ADD     A,(HL)              
62D8: 00              NOP                         
62D9: 9B              SBC     E                   
62DA: 02              LD      (BC),A              
62DB: A2              AND     D                   
62DC: 28 A1           JR      Z,$627F             ; {}
62DE: 30 36           JR      NC,$6316            ; {}
62E0: A2              AND     D                   
62E1: 1E A1           LD      E,$A1               
62E3: 30 36           JR      NC,$631B            ; {}
62E5: A2              AND     D                   
62E6: 2A              LD      A,(HLI)             
62E7: A1              AND     C                   
62E8: 32              LD      (HLD),A             
62E9: 38 A2           JR      C,$628D             ; {}
62EB: 20 A1           JR      NZ,$628E            ; {}
62ED: 32              LD      (HLD),A             
62EE: 38 A2           JR      C,$6292             ; {}
62F0: 28 A1           JR      Z,$6293             ; {}
62F2: 30 36           JR      NC,$632A            ; {}
62F4: A2              AND     D                   
62F5: 1E A1           LD      E,$A1               
62F7: 30 36           JR      NC,$632F            ; {}
62F9: A2              AND     D                   
62FA: 2A              LD      A,(HLI)             
62FB: 8E              ADC     A,(HL)              
62FC: 8E              ADC     A,(HL)              
62FD: 1E 9C           LD      E,$9C               
62FF: 00              NOP                         
6300: A2              AND     D                   
6301: 28 A1           JR      Z,$62A4             ; {}
6303: 30 36           JR      NC,$633B            ; {}
6305: A2              AND     D                   
6306: 1E A1           LD      E,$A1               
6308: 30 36           JR      NC,$6340            ; {}
630A: A2              AND     D                   
630B: 2A              LD      A,(HLI)             
630C: A1              AND     C                   
630D: 32              LD      (HLD),A             
630E: 38 A2           JR      C,$62B2             ; {}
6310: 20 A1           JR      NZ,$62B3            ; {}
6312: 32              LD      (HLD),A             
6313: 38 00           JR      C,$6315             ; {}
6315: 00              NOP                         
6316: 2B              DEC     HL                  
6317: 4A              LD      C,D                 
6318: 20 63           JR      NZ,$637D            ; {}
631A: 3A              LD      A,(HLD)             
631B: 63              LD      H,E                 
631C: 50              LD      D,B                 
631D: 63              LD      H,E                 
631E: 64              LD      H,H                 
631F: 63              LD      H,E                 
6320: EC                              
6321: 6F              LD      L,A                 
6322: 2D              DEC     L                   
6323: 6F              LD      L,A                 
6324: 6E              LD      L,(HL)              
6325: 63              LD      H,E                 
6326: 4B              LD      C,E                 
6327: 6F              LD      L,A                 
6328: 7F              LD      A,A                 
6329: 63              LD      H,E                 
632A: 0F              RRCA                        
632B: 6F              LD      L,A                 
632C: A5              AND     L                   
632D: 6F              LD      L,A                 
632E: 94              SUB     H                   
632F: 63              LD      H,E                 
6330: 5A              LD      E,D                 
6331: 6F              LD      L,A                 
6332: A8              XOR     B                   
6333: 6F              LD      L,A                 
6334: 94              SUB     H                   
6335: 63              LD      H,E                 
6336: FF              RST     0X38                
6337: FF              RST     0X38                
6338: 2A              LD      A,(HLI)             
6339: 63              LD      H,E                 
633A: 2D              DEC     L                   
633B: 6F              LD      L,A                 
633C: A3              AND     E                   
633D: 63              LD      H,E                 
633E: B2              OR      D                   
633F: 63              LD      H,E                 
6340: 4B              LD      C,E                 
6341: 6F              LD      L,A                 
6342: C1              POP     BC                  
6343: 63              LD      H,E                 
6344: 50              LD      D,B                 
6345: 6F              LD      L,A                 
6346: D6 63           SUB     $63                 
6348: 55              LD      D,L                 
6349: 6F              LD      L,A                 
634A: D6 63           SUB     $63                 
634C: FF              RST     0X38                
634D: FF              RST     0X38                
634E: 44              LD      B,H                 
634F: 63              LD      H,E                 
6350: C7              RST     0X00                
6351: 6E              LD      L,(HL)              
6352: E5              PUSH    HL                  
6353: 63              LD      H,E                 
6354: E2              LD      (C),A               
6355: 6F              LD      L,A                 
6356: C2 6E F4        JP      NZ,$F46E            
6359: 63              LD      H,E                 
635A: C2 6E 04        JP      NZ,$046E            
635D: 64              LD      H,H                 
635E: 04              INC     B                   
635F: 64              LD      H,H                 
6360: FF              RST     0X38                
6361: FF              RST     0X38                
6362: 5A              LD      E,D                 
6363: 63              LD      H,E                 
6364: 20 64           JR      NZ,$63CA            ; {}
6366: 28 64           JR      Z,$63CC             ; {}
6368: 2E 64           LD      L,$64               
636A: FF              RST     0X38                
636B: FF              RST     0X38                
636C: 68              LD      L,B                 
636D: 63              LD      H,E                 
636E: A8              XOR     B                   
636F: 01 A1 46        LD      BC,$46A1            
6372: 48              LD      C,B                 
6373: 5E              LD      E,(HL)              
6374: 60              LD      H,B                 
6375: A8              XOR     B                   
6376: 01 A1 48        LD      BC,$48A1            
6379: 4A              LD      C,D                 
637A: 60              LD      H,B                 
637B: 62              LD      H,D                 
637C: A8              XOR     B                   
637D: 01 00 9B        LD      BC,$9B00            
6380: 05              DEC     B                   
6381: A1              AND     C                   
6382: 70              LD      (HL),B              
6383: 72              LD      (HL),D              
6384: 70              LD      (HL),B              
6385: 6E              LD      L,(HL)              
6386: 9C              SBC     H                   
6387: 70              LD      (HL),B              
6388: 6E              LD      L,(HL)              
6389: 6C              LD      L,H                 
638A: 6A              LD      L,D                 
638B: 68              LD      L,B                 
638C: 66              LD      H,(HL)              
638D: 64              LD      H,H                 
638E: 62              LD      H,D                 
638F: 60              LD      H,B                 
6390: 5E              LD      E,(HL)              
6391: 5C              LD      E,H                 
6392: 5A              LD      E,D                 
6393: 00              NOP                         
6394: 9B              SBC     E                   
6395: 04              INC     B                   
6396: A2              AND     D                   
6397: 50              LD      D,B                 
6398: 4A              LD      C,D                 
6399: 4A              LD      C,D                 
639A: 50              LD      D,B                 
639B: 4A              LD      C,D                 
639C: 4A              LD      C,D                 
639D: 50              LD      D,B                 
639E: 4A              LD      C,D                 
639F: 50              LD      D,B                 
63A0: 4A              LD      C,D                 
63A1: 9C              SBC     H                   
63A2: 00              NOP                         
63A3: A5              AND     L                   
63A4: 01 9B 08        LD      BC,$089B            
63A7: A1              AND     C                   
63A8: 1E 20           LD      E,$20               
63AA: 9C              SBC     H                   
63AB: A3              AND     E                   
63AC: 1E AE           LD      E,$AE               
63AE: 01 A5 01        LD      BC,$01A5            
63B1: 00              NOP                         
63B2: A1              AND     C                   
63B3: 52              LD      D,D                 
63B4: 54              LD      D,H                 
63B5: 6A              LD      L,D                 
63B6: 6C              LD      L,H                 
63B7: A8              XOR     B                   
63B8: 01 A1 54        LD      BC,$54A1            
63BB: 56              LD      D,(HL)              
63BC: 6C              LD      L,H                 
63BD: 6E              LD      L,(HL)              
63BE: A8              XOR     B                   
63BF: 01 00 9B        LD      BC,$9B00            
63C2: 05              DEC     B                   
63C3: A1              AND     C                   
63C4: 58              LD      E,B                 
63C5: 5A              LD      E,D                 
63C6: 58              LD      E,B                 
63C7: 56              LD      D,(HL)              
63C8: 9C              SBC     H                   
63C9: 58              LD      E,B                 
63CA: 56              LD      D,(HL)              
63CB: 54              LD      D,H                 
63CC: 52              LD      D,D                 
63CD: 50              LD      D,B                 
63CE: 4E              LD      C,(HL)              
63CF: 4C              LD      C,H                 
63D0: 4A              LD      C,D                 
63D1: 48              LD      C,B                 
63D2: 46              LD      B,(HL)              
63D3: 44              LD      B,H                 
63D4: 42              LD      B,D                 
63D5: 00              NOP                         
63D6: 9B              SBC     E                   
63D7: 04              INC     B                   
63D8: A2              AND     D                   
63D9: 58              LD      E,B                 
63DA: 01 01 56        LD      BC,$5601            
63DD: 01 01 58        LD      BC,$5801            
63E0: 01 5A 01        LD      BC,$015A            
63E3: 9C              SBC     H                   
63E4: 00              NOP                         
63E5: 9A              SBC     D                   
63E6: 9B              SBC     E                   
63E7: 10 A1           ;;STOP    $A1                 
63E9: 28 2A           JR      Z,$6415             ; {}
63EB: 9C              SBC     H                   
63EC: 99              SBC     C                   
63ED: A3              AND     E                   
63EE: 2C              INC     L                   
63EF: AE              XOR     (HL)                
63F0: 01 A5 01        LD      BC,$01A5            
63F3: 00              NOP                         
63F4: A5              AND     L                   
63F5: 01 99 9B        LD      BC,$9B99            
63F8: 04              INC     B                   
63F9: A2              AND     D                   
63FA: 40              LD      B,B                 
63FB: 9C              SBC     H                   
63FC: 28 28           JR      Z,$6426             ; {}
63FE: A1              AND     C                   
63FF: 28 28           JR      Z,$6429             ; {}
6401: 2A              LD      A,(HLI)             
6402: 28 00           JR      Z,$6404             ; {}
6404: 99              SBC     C                   
6405: 9B              SBC     E                   
6406: 04              INC     B                   
6407: A1              AND     C                   
6408: 4A              LD      C,D                 
6409: 4A              LD      C,D                 
640A: 32              LD      (HLD),A             
640B: 32              LD      (HLD),A             
640C: A2              AND     D                   
640D: 32              LD      (HLD),A             
640E: A1              AND     C                   
640F: 4A              LD      C,D                 
6410: 4A              LD      C,D                 
6411: 32              LD      (HLD),A             
6412: 32              LD      (HLD),A             
6413: A2              AND     D                   
6414: 32              LD      (HLD),A             
6415: A1              AND     C                   
6416: 4A              LD      C,D                 
6417: 4A              LD      C,D                 
6418: 32              LD      (HLD),A             
6419: 32              LD      (HLD),A             
641A: 4A              LD      C,D                 
641B: 4A              LD      C,D                 
641C: 32              LD      (HLD),A             
641D: 32              LD      (HLD),A             
641E: 9C              SBC     H                   
641F: 00              NOP                         
6420: 9B              SBC     E                   
6421: 04              INC     B                   
6422: A5              AND     L                   
6423: 01 9C A8        LD      BC,$A89C            
6426: 01 00 9B        LD      BC,$9B00            
6429: 04              INC     B                   
642A: A5              AND     L                   
642B: 01 9C 00        LD      BC,$009C            
642E: 9B              SBC     E                   
642F: 02              LD      (BC),A              
6430: A1              AND     C                   
6431: 15              DEC     D                   
6432: 15              DEC     D                   
6433: 15              DEC     D                   
6434: 15              DEC     D                   
6435: A2              AND     D                   
6436: 01 9C 9B        LD      BC,$9B9C            
6439: 08 A1 15        LD      ($15A1),SP          
643C: 9C              SBC     H                   
643D: 00              NOP                         
643E: 00              NOP                         
643F: 67              LD      H,A                 
6440: 4A              LD      C,D                 
6441: 8C              ADC     A,H                 
6442: 4A              LD      C,D                 
6443: 49              LD      C,C                 
6444: 64              LD      H,H                 
6445: 53              LD      D,E                 
6446: 64              LD      H,H                 
6447: 5B              LD      E,E                 
6448: 64              LD      H,H                 
6449: 37              SCF                         
644A: 6F              LD      L,A                 
644B: 61              LD      H,C                 
644C: 64              LD      H,H                 
644D: 80              ADD     A,B                 
644E: 64              LD      H,H                 
644F: FF              RST     0X38                
6450: FF              RST     0X38                
6451: 49              LD      C,C                 
6452: 64              LD      H,H                 
6453: EC                              
6454: 6E              LD      L,(HL)              
6455: B5              OR      L                   
6456: 64              LD      H,H                 
6457: FF              RST     0X38                
6458: FF              RST     0X38                
6459: 53              LD      D,E                 
645A: 64              LD      H,H                 
645B: D0              RET     NC                  
645C: 64              LD      H,H                 
645D: FF              RST     0X38                
645E: FF              RST     0X38                
645F: 5B              LD      E,E                 
6460: 64              LD      H,H                 
6461: A4              AND     H                   
6462: 01 A7 01        LD      BC,$01A7            
6465: AD              XOR     L                   
6466: 5A              LD      E,D                 
6467: 5E              LD      E,(HL)              
6468: 5A              LD      E,D                 
6469: A3              AND     E                   
646A: 58              LD      E,B                 
646B: 01 A7 01        LD      BC,$01A7            
646E: A1              AND     C                   
646F: 4A              LD      C,D                 
6470: 54              LD      D,H                 
6471: A3              AND     E                   
6472: 4E              LD      C,(HL)              
6473: 01 A7 01        LD      BC,$01A7            
6476: AD              XOR     L                   
6477: 42              LD      B,D                 
6478: 46              LD      B,(HL)              
6479: 42              LD      B,D                 
647A: A3              AND     E                   
647B: 40              LD      B,B                 
647C: 01 A7 01        LD      BC,$01A7            
647F: 00              NOP                         
6480: 9D              SBC     L                   
6481: 40              LD      B,B                 
6482: 21 01 AD        LD      HL,$AD01            
6485: 4E              LD      C,(HL)              
6486: 50              LD      D,B                 
6487: 52              LD      D,D                 
6488: A6              AND     (HL)                
6489: 54              LD      D,H                 
648A: A1              AND     C                   
648B: 48              LD      C,B                 
648C: A7              AND     A                   
648D: 54              LD      D,H                 
648E: AD              XOR     L                   
648F: 52              LD      D,D                 
6490: 54              LD      D,H                 
6491: 52              LD      D,D                 
6492: A2              AND     D                   
6493: 4E              LD      C,(HL)              
6494: 4A              LD      C,D                 
6495: A6              AND     (HL)                
6496: 4E              LD      C,(HL)              
6497: A1              AND     C                   
6498: 40              LD      B,B                 
6499: A4              AND     H                   
649A: 4E              LD      C,(HL)              
649B: A2              AND     D                   
649C: 01 AD 4E        LD      BC,$4EAD            
649F: 50              LD      D,B                 
64A0: 52              LD      D,D                 
64A1: A6              AND     (HL)                
64A2: 54              LD      D,H                 
64A3: A1              AND     C                   
64A4: 48              LD      C,B                 
64A5: A7              AND     A                   
64A6: 54              LD      D,H                 
64A7: AD              XOR     L                   
64A8: 52              LD      D,D                 
64A9: 54              LD      D,H                 
64AA: 52              LD      D,D                 
64AB: A2              AND     D                   
64AC: 4E              LD      C,(HL)              
64AD: 4A              LD      C,D                 
64AE: A6              AND     (HL)                
64AF: 4E              LD      C,(HL)              
64B0: A1              AND     C                   
64B1: 40              LD      B,B                 
64B2: A8              XOR     B                   
64B3: 4E              LD      C,(HL)              
64B4: 00              NOP                         
64B5: 99              SBC     C                   
64B6: 9B              SBC     E                   
64B7: 04              INC     B                   
64B8: A6              AND     (HL)                
64B9: 28 A1           JR      Z,$645C             ; {}
64BB: 30 A2           JR      NC,$645F            ; {}
64BD: 36 28           LD      (HL),$28            
64BF: 2A              LD      A,(HLI)             
64C0: 32              LD      (HLD),A             
64C1: A3              AND     E                   
64C2: 38 A6           JR      C,$646A             ; {}
64C4: 28 A1           JR      Z,$6467             ; {}
64C6: 30 A2           JR      NC,$646A            ; {}
64C8: 36 28           LD      (HL),$28            
64CA: 1E 2A           LD      E,$2A               
64CC: A3              AND     E                   
64CD: 32              LD      (HLD),A             
64CE: 9C              SBC     H                   
64CF: 00              NOP                         
64D0: 9B              SBC     E                   
64D1: 03              INC     BC                  
64D2: A2              AND     D                   
64D3: 15              DEC     D                   
64D4: AD              XOR     L                   
64D5: 15              DEC     D                   
64D6: 15              DEC     D                   
64D7: 15              DEC     D                   
64D8: 9C              SBC     H                   
64D9: 9B              SBC     E                   
64DA: 04              INC     B                   
64DB: A1              AND     C                   
64DC: 15              DEC     D                   
64DD: 9C              SBC     H                   
64DE: 00              NOP                         
64DF: 00              NOP                         
64E0: 2B              DEC     HL                  
64E1: 4A              LD      C,D                 
64E2: EA 64 F0        LD      ($F064),A           
64E5: 64              LD      H,H                 
64E6: F6 64           OR      $64                 
64E8: 00              NOP                         
64E9: 00              NOP                         
64EA: 50              LD      D,B                 
64EB: 6F              LD      L,A                 
64EC: FC                              
64ED: 64              LD      H,H                 
64EE: 00              NOP                         
64EF: 00              NOP                         
64F0: 50              LD      D,B                 
64F1: 6F              LD      L,A                 
64F2: 03              INC     BC                  
64F3: 65              LD      H,L                 
64F4: 00              NOP                         
64F5: 00              NOP                         
64F6: EC                              
64F7: 6E              LD      L,(HL)              
64F8: 0A              LD      A,(BC)              
64F9: 65              LD      H,L                 
64FA: 00              NOP                         
64FB: 00              NOP                         
64FC: A2              AND     D                   
64FD: 52              LD      D,D                 
64FE: 54              LD      D,H                 
64FF: 56              LD      D,(HL)              
6500: A8              XOR     B                   
6501: 58              LD      E,B                 
6502: 00              NOP                         
6503: A2              AND     D                   
6504: 5C              LD      E,H                 
6505: 5E              LD      E,(HL)              
6506: 60              LD      H,B                 
6507: A8              XOR     B                   
6508: 62              LD      H,D                 
6509: 00              NOP                         
650A: 99              SBC     C                   
650B: A2              AND     D                   
650C: 30 32           JR      NC,$6540            ; {}
650E: 34              INC     (HL)                
650F: 9A              SBC     D                   
6510: A8              XOR     B                   
6511: 36 00           LD      (HL),$00            
6513: 00              NOP                         
6514: 58              LD      E,B                 
6515: 4A              LD      C,D                 
6516: 1E 65           LD      E,$65               
6518: 5A              LD      E,D                 
6519: 65              LD      H,L                 
651A: A2              AND     D                   
651B: 65              LD      H,L                 
651C: EC                              
651D: 65              LD      H,L                 
651E: CB 6F           BIT     1,E                 
6520: BD              CP      L                   
6521: 6F              LD      L,A                 
6522: 44              LD      B,H                 
6523: 66              LD      H,(HL)              
6524: 49              LD      C,C                 
6525: 66              LD      H,(HL)              
6526: 5B              LD      E,E                 
6527: 66              LD      H,(HL)              
6528: 78              LD      A,B                 
6529: 66              LD      H,(HL)              
652A: A8              XOR     B                   
652B: 66              LD      H,(HL)              
652C: 20 70           JR      NZ,$659E            ; {}
652E: C6 66           ADD     $66                 
6530: 04              INC     B                   
6531: 67              LD      H,A                 
6532: 09              ADD     HL,BC               
6533: 67              LD      H,A                 
6534: 07              RLCA                        
6535: 70              LD      (HL),B              
6536: 1C              INC     E                   
6537: 70              LD      (HL),B              
6538: E2              LD      (C),A               
6539: 6F              LD      L,A                 
653A: 1D              DEC     E                   
653B: 67              LD      H,A                 
653C: 58              LD      E,B                 
653D: 67              LD      H,A                 
653E: 58              LD      E,B                 
653F: 67              LD      H,A                 
6540: BF              CP      A                   
6541: 67              LD      H,A                 
6542: 58              LD      E,B                 
6543: 67              LD      H,A                 
6544: 58              LD      E,B                 
6545: 67              LD      H,A                 
6546: BF              CP      A                   
6547: 67              LD      H,A                 
6548: 58              LD      E,B                 
6549: 67              LD      H,A                 
654A: 58              LD      E,B                 
654B: 67              LD      H,A                 
654C: FF              RST     0X38                
654D: 67              LD      H,A                 
654E: 1F              RRA                         
654F: 68              LD      L,B                 
6550: 20 70           JR      NZ,$65C2            ; {}
6552: 30 68           JR      NC,$65BC            ; {}
6554: 24              INC     H                   
6555: 70              LD      (HL),B              
6556: 4D              LD      C,L                 
6557: 68              LD      L,B                 
6558: 00              NOP                         
6559: 00              NOP                         
655A: CB 6F           BIT     1,E                 
655C: 69              LD      L,C                 
655D: 6F              LD      L,A                 
655E: 5C              LD      E,H                 
655F: 68              LD      L,B                 
6560: 64              LD      H,H                 
6561: 6F              LD      L,A                 
6562: 72              LD      (HL),D              
6563: 68              LD      L,B                 
6564: 73              LD      (HL),E              
6565: 6F              LD      L,A                 
6566: 5C              LD      E,H                 
6567: 68              LD      L,B                 
6568: 5F              LD      E,A                 
6569: 6F              LD      L,A                 
656A: 86              ADD     A,(HL)              
656B: 68              LD      L,B                 
656C: 99              SBC     C                   
656D: 68              LD      L,B                 
656E: 6E              LD      L,(HL)              
656F: 6F              LD      L,A                 
6570: 9E              SBC     (HL)                
6571: 68              LD      L,B                 
6572: 20 70           JR      NZ,$65E4            ; {}
6574: B5              OR      L                   
6575: 68              LD      L,B                 
6576: CC 5E 01        CALL    Z,$015E             
6579: 70              LD      (HL),B              
657A: 09              ADD     HL,BC               
657B: 67              LD      H,A                 
657C: FB              EI                          
657D: 6F              LD      L,A                 
657E: 1C              INC     E                   
657F: 70              LD      (HL),B              
6580: E2              LD      (C),A               
6581: 6F              LD      L,A                 
6582: D1              POP     DE                  
6583: 68              LD      L,B                 
6584: 0A              LD      A,(BC)              
6585: 69              LD      L,C                 
6586: 0A              LD      A,(BC)              
6587: 69              LD      L,C                 
6588: 5C              LD      E,H                 
6589: 69              LD      L,C                 
658A: 0A              LD      A,(BC)              
658B: 69              LD      L,C                 
658C: 0A              LD      A,(BC)              
658D: 69              LD      L,C                 
658E: 5C              LD      E,H                 
658F: 69              LD      L,C                 
6590: 0A              LD      A,(BC)              
6591: 69              LD      L,C                 
6592: 0A              LD      A,(BC)              
6593: 69              LD      L,C                 
6594: 9C              SBC     H                   
6595: 69              LD      L,C                 
6596: B5              OR      L                   
6597: 69              LD      L,C                 
6598: 20 70           JR      NZ,$660A            ; {}
659A: C6 69           ADD     $69                 
659C: 24              INC     H                   
659D: 70              LD      (HL),B              
659E: DB                              
659F: 69              LD      L,C                 
65A0: 00              NOP                         
65A1: 00              NOP                         
65A2: CB 6F           BIT     1,E                 
65A4: FB              EI                          
65A5: 6F              LD      L,A                 
65A6: EA 69 5C        LD      ($5C69),A           ; {}
65A9: 68              LD      L,B                 
65AA: EF              RST     0X28                
65AB: 69              LD      L,C                 
65AC: 72              LD      (HL),D              
65AD: 68              LD      L,B                 
65AE: F4                              
65AF: 69              LD      L,C                 
65B0: D6 6E           SUB     $6E                 
65B2: 49              LD      C,C                 
65B3: 66              LD      H,(HL)              
65B4: 5B              LD      E,E                 
65B5: 66              LD      H,(HL)              
65B6: DF              RST     0X18                
65B7: 6F              LD      L,A                 
65B8: FE 69           CP      $69                 
65BA: 03              INC     BC                  
65BB: 6A              LD      L,D                 
65BC: 20 70           JR      NZ,$662E            ; {}
65BE: 2A              LD      A,(HLI)             
65BF: 6A              LD      L,D                 
65C0: D6 6E           SUB     $6E                 
65C2: 04              INC     B                   
65C3: 70              LD      (HL),B              
65C4: 09              ADD     HL,BC               
65C5: 67              LD      H,A                 
65C6: FE 6F           CP      $6F                 
65C8: 1C              INC     E                   
65C9: 70              LD      (HL),B              
65CA: E2              LD      (C),A               
65CB: 6F              LD      L,A                 
65CC: 51              LD      D,C                 
65CD: 6A              LD      L,D                 
65CE: 65              LD      H,L                 
65CF: 6A              LD      L,D                 
65D0: 65              LD      H,L                 
65D1: 6A              LD      L,D                 
65D2: C3 6A 65        JP      $656A               ; {}
65D5: 6A              LD      L,D                 
65D6: 65              LD      H,L                 
65D7: 6A              LD      L,D                 
65D8: C3 6A 65        JP      $656A               ; {}
65DB: 6A              LD      L,D                 
65DC: 65              LD      H,L                 
65DD: 6A              LD      L,D                 
65DE: 0D              DEC     C                   
65DF: 6B              LD      L,E                 
65E0: 2A              LD      A,(HLI)             
65E1: 6B              LD      L,E                 
65E2: 20 70           JR      NZ,$6654            ; {}
65E4: 36 6B           LD      (HL),$6B            
65E6: 24              INC     H                   
65E7: 70              LD      (HL),B              
65E8: 4C              LD      C,H                 
65E9: 6B              LD      L,E                 
65EA: 00              NOP                         
65EB: 00              NOP                         
65EC: D3                              
65ED: 6F              LD      L,A                 
65EE: 57              LD      D,A                 
65EF: 6B              LD      L,E                 
65F0: 20 70           JR      NZ,$6662            ; {}
65F2: 5F              LD      E,A                 
65F3: 6B              LD      L,E                 
65F4: 1C              INC     E                   
65F5: 70              LD      (HL),B              
65F6: 67              LD      H,A                 
65F7: 6B              LD      L,E                 
65F8: 67              LD      H,A                 
65F9: 6B              LD      L,E                 
65FA: 67              LD      H,A                 
65FB: 6B              LD      L,E                 
65FC: 67              LD      H,A                 
65FD: 6B              LD      L,E                 
65FE: 67              LD      H,A                 
65FF: 6B              LD      L,E                 
6600: 67              LD      H,A                 
6601: 6B              LD      L,E                 
6602: 67              LD      H,A                 
6603: 6B              LD      L,E                 
6604: 67              LD      H,A                 
6605: 6B              LD      L,E                 
6606: 67              LD      H,A                 
6607: 6B              LD      L,E                 
6608: 67              LD      H,A                 
6609: 6B              LD      L,E                 
660A: 67              LD      H,A                 
660B: 6B              LD      L,E                 
660C: 78              LD      A,B                 
660D: 6B              LD      L,E                 
660E: 78              LD      A,B                 
660F: 6B              LD      L,E                 
6610: 67              LD      H,A                 
6611: 6B              LD      L,E                 
6612: 67              LD      H,A                 
6613: 6B              LD      L,E                 
6614: 67              LD      H,A                 
6615: 6B              LD      L,E                 
6616: 67              LD      H,A                 
6617: 6B              LD      L,E                 
6618: 67              LD      H,A                 
6619: 6B              LD      L,E                 
661A: 67              LD      H,A                 
661B: 6B              LD      L,E                 
661C: 67              LD      H,A                 
661D: 6B              LD      L,E                 
661E: 67              LD      H,A                 
661F: 6B              LD      L,E                 
6620: 78              LD      A,B                 
6621: 6B              LD      L,E                 
6622: 78              LD      A,B                 
6623: 6B              LD      L,E                 
6624: 67              LD      H,A                 
6625: 6B              LD      L,E                 
6626: 67              LD      H,A                 
6627: 6B              LD      L,E                 
6628: 67              LD      H,A                 
6629: 6B              LD      L,E                 
662A: 67              LD      H,A                 
662B: 6B              LD      L,E                 
662C: 67              LD      H,A                 
662D: 6B              LD      L,E                 
662E: 67              LD      H,A                 
662F: 6B              LD      L,E                 
6630: 67              LD      H,A                 
6631: 6B              LD      L,E                 
6632: 67              LD      H,A                 
6633: 6B              LD      L,E                 
6634: 67              LD      H,A                 
6635: 6B              LD      L,E                 
6636: 83              ADD     A,E                 
6637: 6B              LD      L,E                 
6638: 20 70           JR      NZ,$66AA            ; {}
663A: 83              ADD     A,E                 
663B: 6B              LD      L,E                 
663C: 83              ADD     A,E                 
663D: 6B              LD      L,E                 
663E: 24              INC     H                   
663F: 70              LD      (HL),B              
6640: 91              SUB     C                   
6641: 6B              LD      L,E                 
6642: 00              NOP                         
6643: 00              NOP                         
6644: 9D              SBC     L                   
6645: 56              LD      D,(HL)              
6646: 00              NOP                         
6647: 80              ADD     A,B                 
6648: 00              NOP                         
6649: A1              AND     C                   
664A: 30 3E           JR      NC,$668A            ; {}
664C: 44              LD      B,H                 
664D: 4C              LD      C,H                 
664E: 4E              LD      C,(HL)              
664F: 56              LD      D,(HL)              
6650: 5C              LD      E,H                 
6651: 64              LD      H,H                 
6652: 66              LD      H,(HL)              
6653: 64              LD      H,H                 
6654: 5C              LD      E,H                 
6655: 56              LD      D,(HL)              
6656: 4E              LD      C,(HL)              
6657: 4C              LD      C,H                 
6658: 44              LD      B,H                 
6659: 3E 00           LD      A,$00               
665B: A1              AND     C                   
665C: 40              LD      B,B                 
665D: 44              LD      B,H                 
665E: 48              LD      C,B                 
665F: 4E              LD      C,(HL)              
6660: 58              LD      E,B                 
6661: 5C              LD      E,H                 
6662: 60              LD      H,B                 
6663: 66              LD      H,(HL)              
6664: 70              LD      (HL),B              
6665: 66              LD      H,(HL)              
6666: 60              LD      H,B                 
6667: 5C              LD      E,H                 
6668: 58              LD      E,B                 
6669: 4E              LD      C,(HL)              
666A: 48              LD      C,B                 
666B: 44              LD      B,H                 
666C: 40              LD      B,B                 
666D: 44              LD      B,H                 
666E: 48              LD      C,B                 
666F: 4E              LD      C,(HL)              
6670: 58              LD      E,B                 
6671: 5C              LD      E,H                 
6672: 60              LD      H,B                 
6673: 66              LD      H,(HL)              
6674: A3              AND     E                   
6675: 70              LD      (HL),B              
6676: 01 00 9D        LD      BC,$9D00            
6679: 42              LD      B,D                 
667A: 00              NOP                         
667B: 80              ADD     A,B                 
667C: A1              AND     C                   
667D: 36 34           LD      (HL),$34            
667F: 36 2C           LD      (HL),$2C            
6681: 30 34           JR      NC,$66B7            ; {}
6683: 36 3A           LD      (HL),$3A            
6685: 3E 3A           LD      A,$3A               
6687: 3E 36           LD      A,$36               
6689: 3A              LD      A,(HLD)             
668A: 3E 40           LD      A,$40               
668C: 44              LD      B,H                 
668D: 9D              SBC     L                   
668E: 52              LD      D,D                 
668F: 00              NOP                         
6690: 80              ADD     A,B                 
6691: 4E              LD      C,(HL)              
6692: 4C              LD      C,H                 
6693: 4E              LD      C,(HL)              
6694: 44              LD      B,H                 
6695: 56              LD      D,(HL)              
6696: 52              LD      D,D                 
6697: 56              LD      D,(HL)              
6698: 4E              LD      C,(HL)              
6699: 9D              SBC     L                   
669A: 62              LD      H,D                 
669B: 00              NOP                         
669C: 80              ADD     A,B                 
669D: 5C              LD      E,H                 
669E: 56              LD      D,(HL)              
669F: 4E              LD      C,(HL)              
66A0: 66              LD      H,(HL)              
66A1: 64              LD      H,H                 
66A2: 5E              LD      E,(HL)              
66A3: 56              LD      D,(HL)              
66A4: 52              LD      D,D                 
66A5: A3              AND     E                   
66A6: 4E              LD      C,(HL)              
66A7: 00              NOP                         
66A8: 9D              SBC     L                   
66A9: 60              LD      H,B                 
66AA: 21 80 A3        LD      HL,$A380            
66AD: 52              LD      D,D                 
66AE: 4E              LD      C,(HL)              
66AF: 5C              LD      E,H                 
66B0: A7              AND     A                   
66B1: 5C              LD      E,H                 
66B2: A3              AND     E                   
66B3: 60              LD      H,B                 
66B4: A2              AND     D                   
66B5: 5C              LD      E,H                 
66B6: 58              LD      E,B                 
66B7: 52              LD      D,D                 
66B8: A3              AND     E                   
66B9: 56              LD      D,(HL)              
66BA: A2              AND     D                   
66BB: 01 58 56        LD      BC,$5658            
66BE: 52              LD      D,D                 
66BF: 4E              LD      C,(HL)              
66C0: 5C              LD      E,H                 
66C1: A3              AND     E                   
66C2: 58              LD      E,B                 
66C3: A4              AND     H                   
66C4: 01 00 9D        LD      BC,$9D00            
66C7: 52              LD      D,D                 
66C8: 00              NOP                         
66C9: 80              ADD     A,B                 
66CA: A3              AND     E                   
66CB: 01 9B 02        LD      BC,$029B            
66CE: A1              AND     C                   
66CF: 44              LD      B,H                 
66D0: 4A              LD      C,D                 
66D1: 52              LD      D,D                 
66D2: 58              LD      E,B                 
66D3: 60              LD      H,B                 
66D4: 58              LD      E,B                 
66D5: 52              LD      D,D                 
66D6: 4A              LD      C,D                 
66D7: 9C              SBC     H                   
66D8: 9B              SBC     E                   
66D9: 02              LD      (BC),A              
66DA: 36 3E           LD      (HL),$3E            
66DC: 44              LD      B,H                 
66DD: 4A              LD      C,D                 
66DE: 52              LD      D,D                 
66DF: 4A              LD      C,D                 
66E0: 44              LD      B,H                 
66E1: 3E 9C           LD      A,$9C               
66E3: 40              LD      B,B                 
66E4: 44              LD      B,H                 
66E5: 48              LD      C,B                 
66E6: 4E              LD      C,(HL)              
66E7: 58              LD      E,B                 
66E8: 4E              LD      C,(HL)              
66E9: 48              LD      C,B                 
66EA: 44              LD      B,H                 
66EB: 40              LD      B,B                 
66EC: 44              LD      B,H                 
66ED: 48              LD      C,B                 
66EE: 4E              LD      C,(HL)              
66EF: 58              LD      E,B                 
66F0: 4E              LD      C,(HL)              
66F1: 48              LD      C,B                 
66F2: 40              LD      B,B                 
66F3: 3E 42           LD      A,$42               
66F5: 46              LD      B,(HL)              
66F6: 4C              LD      C,H                 
66F7: 56              LD      D,(HL)              
66F8: 5A              LD      E,D                 
66F9: 5E              LD      E,(HL)              
66FA: 64              LD      H,H                 
66FB: 6E              LD      L,(HL)              
66FC: 64              LD      H,H                 
66FD: 5E              LD      E,(HL)              
66FE: 5A              LD      E,D                 
66FF: 56              LD      D,(HL)              
6700: 4C              LD      C,H                 
6701: 46              LD      B,(HL)              
6702: 3E 00           LD      A,$00               
6704: 9D              SBC     L                   
6705: 47              LD      B,A                 
6706: 00              NOP                         
6707: 80              ADD     A,B                 
6708: 00              NOP                         
6709: A1              AND     C                   
670A: 1E 22           LD      E,$22               
670C: 26 2C           LD      H,$2C               
670E: 32              LD      (HLD),A             
670F: 3A              LD      A,(HLD)             
6710: 3E 44           LD      A,$44               
6712: 4A              LD      C,D                 
6713: 52              LD      D,D                 
6714: 56              LD      D,(HL)              
6715: 5C              LD      E,H                 
6716: 62              LD      H,D                 
6717: 6A              LD      L,D                 
6718: 6E              LD      L,(HL)              
6719: 74              LD      (HL),H              
671A: A4              AND     H                   
671B: 7E              LD      A,(HL)              
671C: 00              NOP                         
671D: 9D              SBC     L                   
671E: 52              LD      D,D                 
671F: 00              NOP                         
6720: 80              ADD     A,B                 
6721: A4              AND     H                   
6722: 01 A3 1E        LD      BC,$1EA3            
6725: AA              XOR     D                   
6726: 1E 1E           LD      E,$1E               
6728: 1E 9D           LD      E,$9D               
672A: 72              LD      (HL),D              
672B: 00              NOP                         
672C: 80              ADD     A,B                 
672D: A3              AND     E                   
672E: 22              LD      (HLI),A             
672F: 9B              SBC     E                   
6730: 06 AA           LD      B,$AA               
6732: 22              LD      (HLI),A             
6733: 9C              SBC     H                   
6734: 28 28           JR      Z,$675E             ; {}
6736: 28 9D           JR      Z,$66D5             ; {}
6738: 92              SUB     D                   
6739: 00              NOP                         
673A: 80              ADD     A,B                 
673B: A3              AND     E                   
673C: 2C              INC     L                   
673D: AA              XOR     D                   
673E: 2C              INC     L                   
673F: 2C              INC     L                   
6740: 2C              INC     L                   
6741: A3              AND     E                   
6742: 32              LD      (HLD),A             
6743: AA              XOR     D                   
6744: 32              LD      (HLD),A             
6745: 32              LD      (HLD),A             
6746: 3A              LD      A,(HLD)             
6747: A3              AND     E                   
6748: 3E AA           LD      A,$AA               
674A: 36 36           LD      (HL),$36            
674C: 36 A3           LD      (HL),$A3            
674E: 36 9D           LD      (HL),$9D            
6750: 92              SUB     D                   
6751: 00              NOP                         
6752: 40              LD      B,B                 
6753: AA              XOR     D                   
6754: 36 3A           LD      (HL),$3A            
6756: 3E 00           LD      A,$00               
6758: 9D              SBC     L                   
6759: 90              SUB     B                   
675A: 21 41 A3        LD      HL,$A341            
675D: 30 AA           JR      NC,$6709            ; {}
675F: 32              LD      (HLD),A             
6760: 30 2C           JR      NC,$678E            ; {}
6762: 30 01           JR      NC,$6765            ; {}
6764: 30 32           JR      NC,$6798            ; {}
6766: 36 3A           LD      (HL),$3A            
6768: A3              AND     E                   
6769: 3C              INC     A                   
676A: AA              XOR     D                   
676B: 44              LD      B,H                 
676C: 48              LD      C,B                 
676D: 44              LD      B,H                 
676E: A3              AND     E                   
676F: 42              LD      B,D                 
6770: AA              XOR     D                   
6771: 3A              LD      A,(HLD)             
6772: 3E 42           LD      A,$42               
6774: A3              AND     E                   
6775: 44              LD      B,H                 
6776: AA              XOR     D                   
6777: 5C              LD      E,H                 
6778: 62              LD      H,D                 
6779: 6A              LD      L,D                 
677A: 70              LD      (HL),B              
677B: 38 3C           JR      C,$67B9             ; {}
677D: 40              LD      B,B                 
677E: 3C              INC     A                   
677F: 38 A3           JR      C,$6724             ; {}
6781: 36 AA           LD      (HL),$AA            
6783: 36 3A           LD      (HL),$3A            
6785: 36 A3           LD      (HL),$A3            
6787: 32              LD      (HLD),A             
6788: 01 9D 77        LD      BC,$779D            
678B: 00              NOP                         
678C: 80              ADD     A,B                 
678D: 9B              SBC     E                   
678E: 02              LD      (BC),A              
678F: AA              XOR     D                   
6790: 52              LD      D,D                 
6791: 56              LD      D,(HL)              
6792: 58              LD      E,B                 
6793: 9C              SBC     H                   
6794: 56              LD      D,(HL)              
6795: 4E              LD      C,(HL)              
6796: 48              LD      C,B                 
6797: A3              AND     E                   
6798: 4E              LD      C,(HL)              
6799: AA              XOR     D                   
679A: 52              LD      D,D                 
679B: 56              LD      D,(HL)              
679C: 58              LD      E,B                 
679D: 58              LD      E,B                 
679E: 5C              LD      E,H                 
679F: 58              LD      E,B                 
67A0: 56              LD      D,(HL)              
67A1: 4E              LD      C,(HL)              
67A2: 48              LD      C,B                 
67A3: A3              AND     E                   
67A4: 4E              LD      C,(HL)              
67A5: 9D              SBC     L                   
67A6: 70              LD      (HL),B              
67A7: 21 41 AA        LD      HL,$AA41            
67AA: 4A              LD      C,D                 
67AB: 4E              LD      C,(HL)              
67AC: 52              LD      D,D                 
67AD: 52              LD      D,D                 
67AE: 52              LD      D,D                 
67AF: 52              LD      D,D                 
67B0: A3              AND     E                   
67B1: 50              LD      D,B                 
67B2: AA              XOR     D                   
67B3: 50              LD      D,B                 
67B4: 54              LD      D,H                 
67B5: 50              LD      D,B                 
67B6: A3              AND     E                   
67B7: 4E              LD      C,(HL)              
67B8: AA              XOR     D                   
67B9: 4E              LD      C,(HL)              
67BA: 52              LD      D,D                 
67BB: 4E              LD      C,(HL)              
67BC: A4              AND     H                   
67BD: 4A              LD      C,D                 
67BE: 00              NOP                         
67BF: 9D              SBC     L                   
67C0: 70              LD      (HL),B              
67C1: 00              NOP                         
67C2: 81              ADD     A,C                 
67C3: A5              AND     L                   
67C4: 01 01 A8        LD      BC,$A801            
67C7: 4A              LD      C,D                 
67C8: AA              XOR     D                   
67C9: 4A              LD      C,D                 
67CA: 4E              LD      C,(HL)              
67CB: 4A              LD      C,D                 
67CC: A4              AND     H                   
67CD: 48              LD      C,B                 
67CE: A3              AND     E                   
67CF: 4A              LD      C,D                 
67D0: 4E              LD      C,(HL)              
67D1: 9D              SBC     L                   
67D2: 90              SUB     B                   
67D3: 26 80           LD      H,$80               
67D5: AA              XOR     D                   
67D6: 50              LD      D,B                 
67D7: 01 54 A4        LD      BC,$A454            
67DA: 58              LD      E,B                 
67DB: AA              XOR     D                   
67DC: 50              LD      D,B                 
67DD: 54              LD      D,H                 
67DE: 58              LD      E,B                 
67DF: A8              XOR     B                   
67E0: 58              LD      E,B                 
67E1: AA              XOR     D                   
67E2: 58              LD      E,B                 
67E3: 58              LD      E,B                 
67E4: 58              LD      E,B                 
67E5: 9B              SBC     E                   
67E6: 02              LD      (BC),A              
67E7: 01 50 50        LD      BC,$5050            
67EA: 50              LD      D,B                 
67EB: 4E              LD      C,(HL)              
67EC: 50              LD      D,B                 
67ED: 9C              SBC     H                   
67EE: A3              AND     E                   
67EF: 4E              LD      C,(HL)              
67F0: 9D              SBC     L                   
67F1: 70              LD      (HL),B              
67F2: 21 40 AA        LD      HL,$AA40            
67F5: 3A              LD      A,(HLD)             
67F6: 01 3A 36        LD      BC,$363A            
67F9: 01 36 32        LD      BC,$3236            
67FC: 01 32 00        LD      BC,$0032            
67FF: 9D              SBC     L                   
6800: 80              ADD     A,B                 
6801: 21 41 AA        LD      HL,$AA41            
6804: 46              LD      B,(HL)              
6805: 44              LD      B,H                 
6806: 46              LD      B,(HL)              
6807: 4A              LD      C,D                 
6808: 46              LD      B,(HL)              
6809: 44              LD      B,H                 
680A: 9B              SBC     E                   
680B: 04              INC     B                   
680C: 46              LD      B,(HL)              
680D: 9C              SBC     H                   
680E: 44              LD      B,H                 
680F: 46              LD      B,(HL)              
6810: 4A              LD      C,D                 
6811: 46              LD      B,(HL)              
6812: 4A              LD      C,D                 
6813: 50              LD      D,B                 
6814: 5A              LD      E,D                 
6815: 62              LD      H,D                 
6816: 68              LD      L,B                 
6817: 5A              LD      E,D                 
6818: 5A              LD      E,D                 
6819: 62              LD      H,D                 
681A: 62              LD      H,D                 
681B: 62              LD      H,D                 
681C: A3              AND     E                   
681D: 60              LD      H,B                 
681E: 00              NOP                         
681F: 9D              SBC     L                   
6820: 70              LD      (HL),B              
6821: 21 41 A2        LD      HL,$A241            
6824: 48              LD      C,B                 
6825: A1              AND     C                   
6826: 48              LD      C,B                 
6827: 48              LD      C,B                 
6828: A3              AND     E                   
6829: 44              LD      B,H                 
682A: A2              AND     D                   
682B: 44              LD      B,H                 
682C: A1              AND     C                   
682D: 46              LD      B,(HL)              
682E: 4A              LD      C,D                 
682F: 00              NOP                         
6830: 9D              SBC     L                   
6831: 70              LD      (HL),B              
6832: 21 41 A3        LD      HL,$A341            
6835: 50              LD      D,B                 
6836: A2              AND     D                   
6837: 50              LD      D,B                 
6838: A1              AND     C                   
6839: 50              LD      D,B                 
683A: 50              LD      D,B                 
683B: A2              AND     D                   
683C: 5C              LD      E,H                 
683D: 58              LD      E,B                 
683E: A3              AND     E                   
683F: 54              LD      D,H                 
6840: A3              AND     E                   
6841: 60              LD      H,B                 
6842: A2              AND     D                   
6843: 60              LD      H,B                 
6844: A1              AND     C                   
6845: 5C              LD      E,H                 
6846: 60              LD      H,B                 
6847: A2              AND     D                   
6848: 62              LD      H,D                 
6849: 66              LD      H,(HL)              
684A: 68              LD      L,B                 
684B: 62              LD      H,D                 
684C: 00              NOP                         
684D: A3              AND     E                   
684E: 66              LD      H,(HL)              
684F: 9D              SBC     L                   
6850: A0              AND     B                   
6851: 21 40 A2        LD      HL,$A240            
6854: 28 A1           JR      Z,$67F7             ; {}
6856: 28 28           JR      Z,$6880             ; {}
6858: A3              AND     E                   
6859: 28 01           JR      Z,$685C             ; {}
685B: 00              NOP                         
685C: A2              AND     D                   
685D: 01 60 64        LD      BC,$6460            
6860: A8              XOR     B                   
6861: 66              LD      H,(HL)              
6862: A2              AND     D                   
6863: 60              LD      H,B                 
6864: 64              LD      H,H                 
6865: A8              XOR     B                   
6866: 66              LD      H,(HL)              
6867: A2              AND     D                   
6868: 64              LD      H,H                 
6869: 60              LD      H,B                 
686A: 56              LD      D,(HL)              
686B: A7              AND     A                   
686C: 5C              LD      E,H                 
686D: A5              AND     L                   
686E: 60              LD      H,B                 
686F: A3              AND     E                   
6870: 01 00 A2        LD      BC,$A200            
6873: 60              LD      H,B                 
6874: 64              LD      H,H                 
6875: A8              XOR     B                   
6876: 66              LD      H,(HL)              
6877: A2              AND     D                   
6878: 5C              LD      E,H                 
6879: 66              LD      H,(HL)              
687A: A8              XOR     B                   
687B: 70              LD      (HL),B              
687C: A2              AND     D                   
687D: 6E              LD      L,(HL)              
687E: 6A              LD      L,D                 
687F: A5              AND     L                   
6880: 6E              LD      L,(HL)              
6881: A4              AND     H                   
6882: 01 A2 01        LD      BC,$01A2            
6885: 00              NOP                         
6886: A2              AND     D                   
6887: 60              LD      H,B                 
6888: 64              LD      H,H                 
6889: A8              XOR     B                   
688A: 66              LD      H,(HL)              
688B: A2              AND     D                   
688C: 5C              LD      E,H                 
688D: 66              LD      H,(HL)              
688E: A8              XOR     B                   
688F: 70              LD      (HL),B              
6890: A2              AND     D                   
6891: 6E              LD      L,(HL)              
6892: 6A              LD      L,D                 
6893: 9D              SBC     L                   
6894: 50              LD      D,B                 
6895: 00              NOP                         
6896: 80              ADD     A,B                 
6897: 6E              LD      L,(HL)              
6898: 00              NOP                         
6899: A5              AND     L                   
689A: 6E              LD      L,(HL)              
689B: A4              AND     H                   
689C: 01 00 A8        LD      BC,$A800            
689F: 01 A3 7C        LD      BC,$7CA3            
68A2: 78              LD      A,B                 
68A3: 6E              LD      L,(HL)              
68A4: A7              AND     A                   
68A5: 6E              LD      L,(HL)              
68A6: A5              AND     L                   
68A7: 70              LD      (HL),B              
68A8: A2              AND     D                   
68A9: 82              ADD     A,D                 
68AA: 7E              LD      A,(HL)              
68AB: 7C              LD      A,H                 
68AC: 78              LD      A,B                 
68AD: 6E              LD      L,(HL)              
68AE: 6A              LD      L,D                 
68AF: 6E              LD      L,(HL)              
68B0: 78              LD      A,B                 
68B1: 70              LD      (HL),B              
68B2: A3              AND     E                   
68B3: 01 00 A2        LD      BC,$A200            
68B6: 70              LD      (HL),B              
68B7: A4              AND     H                   
68B8: 74              LD      (HL),H              
68B9: A2              AND     D                   
68BA: 01 62 6A        LD      BC,$6A62            
68BD: 74              LD      (HL),H              
68BE: A8              XOR     B                   
68BF: 6E              LD      L,(HL)              
68C0: A2              AND     D                   
68C1: 01 66 A5        LD      BC,$A566            
68C4: 78              LD      A,B                 
68C5: A2              AND     D                   
68C6: 01 A7 76        LD      BC,$76A7            
68C9: 88              ADC     A,B                 
68CA: 9D              SBC     L                   
68CB: 60              LD      H,B                 
68CC: 00              NOP                         
68CD: 80              ADD     A,B                 
68CE: A4              AND     H                   
68CF: 86              ADD     A,(HL)              
68D0: 00              NOP                         
68D1: 9D              SBC     L                   
68D2: 62              LD      H,D                 
68D3: 21 80 A3        LD      HL,$A380            
68D6: 01 01 26        LD      BC,$2601            
68D9: AA              XOR     D                   
68DA: 26 26           LD      H,$26               
68DC: 26 9D           LD      H,$9D               
68DE: 82              ADD     A,D                 
68DF: 21 80 A3        LD      HL,$A380            
68E2: 28 AA           JR      Z,$688E             ; {}
68E4: 28 28           JR      Z,$690E             ; {}
68E6: 28 32           JR      Z,$691A             ; {}
68E8: 32              LD      (HLD),A             
68E9: 32              LD      (HLD),A             
68EA: 3A              LD      A,(HLD)             
68EB: 3A              LD      A,(HLD)             
68EC: 3A              LD      A,(HLD)             
68ED: 9D              SBC     L                   
68EE: A2              AND     D                   
68EF: 21 80 A3        LD      HL,$A380            
68F2: 3E AA           LD      A,$AA               
68F4: 3E 3E           LD      A,$3E               
68F6: 3E A3           LD      A,$A3               
68F8: 40              LD      B,B                 
68F9: AA              XOR     D                   
68FA: 40              LD      B,B                 
68FB: 40              LD      B,B                 
68FC: 40              LD      B,B                 
68FD: A3              AND     E                   
68FE: 44              LD      B,H                 
68FF: AA              XOR     D                   
6900: 4E              LD      C,(HL)              
6901: 4E              LD      C,(HL)              
6902: 4E              LD      C,(HL)              
6903: A3              AND     E                   
6904: 4E              LD      C,(HL)              
6905: AA              XOR     D                   
6906: 4E              LD      C,(HL)              
6907: 4E              LD      C,(HL)              
6908: 4E              LD      C,(HL)              
6909: 00              NOP                         
690A: 9D              SBC     L                   
690B: A0              AND     B                   
690C: 21 41 A3        LD      HL,$A341            
690F: 40              LD      B,B                 
6910: 36 AA           LD      (HL),$AA            
6912: 36 01           LD      (HL),$01            
6914: 40              LD      B,B                 
6915: 44              LD      B,H                 
6916: 48              LD      C,B                 
6917: 4A              LD      C,D                 
6918: A4              AND     H                   
6919: 4E              LD      C,(HL)              
691A: AA              XOR     D                   
691B: 01 4E 52        LD      BC,$524E            
691E: 54              LD      D,H                 
691F: 52              LD      D,D                 
6920: 4E              LD      C,(HL)              
6921: A4              AND     H                   
6922: 4A              LD      C,D                 
6923: AA              XOR     D                   
6924: 01 4A 4E        LD      BC,$4E4A            
6927: 50              LD      D,B                 
6928: 4E              LD      C,(HL)              
6929: 4A              LD      C,D                 
692A: A3              AND     E                   
692B: 48              LD      C,B                 
692C: AA              XOR     D                   
692D: 48              LD      C,B                 
692E: 4A              LD      C,D                 
692F: 48              LD      C,B                 
6930: A3              AND     E                   
6931: 44              LD      B,H                 
6932: 9D              SBC     L                   
6933: 57              LD      D,A                 
6934: 00              NOP                         
6935: 80              ADD     A,B                 
6936: AA              XOR     D                   
6937: 01 70 74        LD      BC,$7470            
693A: 9B              SBC     E                   
693B: 02              LD      (BC),A              
693C: A3              AND     E                   
693D: 78              LD      A,B                 
693E: 70              LD      (HL),B              
693F: A4              AND     H                   
6940: 7E              LD      A,(HL)              
6941: 9C              SBC     H                   
6942: 9D              SBC     L                   
6943: A0              AND     B                   
6944: 21 41 AA        LD      HL,$AA41            
6947: 52              LD      D,D                 
6948: 56              LD      D,(HL)              
6949: 58              LD      E,B                 
694A: 58              LD      E,B                 
694B: 5C              LD      E,H                 
694C: 60              LD      H,B                 
694D: A3              AND     E                   
694E: 62              LD      H,D                 
694F: AA              XOR     D                   
6950: 62              LD      H,D                 
6951: 66              LD      H,(HL)              
6952: 62              LD      H,D                 
6953: A3              AND     E                   
6954: 60              LD      H,B                 
6955: AA              XOR     D                   
6956: 60              LD      H,B                 
6957: 62              LD      H,D                 
6958: 60              LD      H,B                 
6959: A4              AND     H                   
695A: 5C              LD      E,H                 
695B: 00              NOP                         
695C: 9D              SBC     L                   
695D: A0              AND     B                   
695E: 26 81           LD      H,$81               
6960: AA              XOR     D                   
6961: 58              LD      E,B                 
6962: 01 5C A4        LD      BC,$A45C            
6965: 5E              LD      E,(HL)              
6966: AA              XOR     D                   
6967: 58              LD      E,B                 
6968: 01 5C A3        LD      BC,$A35C            
696B: 5E              LD      E,(HL)              
696C: AA              XOR     D                   
696D: 01 01 5E        LD      BC,$5E01            
6970: A6              AND     (HL)                
6971: 5C              LD      E,H                 
6972: 58              LD      E,B                 
6973: A2              AND     D                   
6974: 4E              LD      C,(HL)              
6975: A4              AND     H                   
6976: 54              LD      D,H                 
6977: AE              XOR     (HL)                
6978: 58              LD      E,B                 
6979: AA              XOR     D                   
697A: 58              LD      E,B                 
697B: 01 5C A4        LD      BC,$A45C            
697E: 5E              LD      E,(HL)              
697F: AA              XOR     D                   
6980: 58              LD      E,B                 
6981: 5C              LD      E,H                 
6982: 5E              LD      E,(HL)              
6983: A8              XOR     B                   
6984: 68              LD      L,B                 
6985: AA              XOR     D                   
6986: 68              LD      L,B                 
6987: 66              LD      H,(HL)              
6988: 5E              LD      E,(HL)              
6989: A5              AND     L                   
698A: 62              LD      H,D                 
698B: A3              AND     E                   
698C: 62              LD      H,D                 
698D: 9D              SBC     L                   
698E: A0              AND     B                   
698F: 21 40 AA        LD      HL,$AA40            
6992: 4A              LD      C,D                 
6993: 4E              LD      C,(HL)              
6994: 4A              LD      C,D                 
6995: 48              LD      C,B                 
6996: 4A              LD      C,D                 
6997: 48              LD      C,B                 
6998: 44              LD      B,H                 
6999: 48              LD      C,B                 
699A: 44              LD      B,H                 
699B: 00              NOP                         
699C: 9D              SBC     L                   
699D: A0              AND     B                   
699E: 21 41 A4        LD      HL,$A441            
69A1: 58              LD      E,B                 
69A2: AA              XOR     D                   
69A3: 01 58 58        LD      BC,$5858            
69A6: 58              LD      E,B                 
69A7: 54              LD      D,H                 
69A8: 58              LD      E,B                 
69A9: A4              AND     H                   
69AA: 5A              LD      E,D                 
69AB: AA              XOR     D                   
69AC: 01 5E 62        LD      BC,$625E            
69AF: 66              LD      H,(HL)              
69B0: 68              LD      L,B                 
69B1: 6C              LD      L,H                 
69B2: A3              AND     E                   
69B3: 70              LD      (HL),B              
69B4: 00              NOP                         
69B5: 9D              SBC     L                   
69B6: A0              AND     B                   
69B7: 21 00 A2        LD      HL,$A200            
69BA: 58              LD      E,B                 
69BB: A1              AND     C                   
69BC: 4E              LD      C,(HL)              
69BD: 58              LD      E,B                 
69BE: A3              AND     E                   
69BF: 54              LD      D,H                 
69C0: A2              AND     D                   
69C1: 54              LD      D,H                 
69C2: A1              AND     C                   
69C3: 58              LD      E,B                 
69C4: 5C              LD      E,H                 
69C5: 00              NOP                         
69C6: A3              AND     E                   
69C7: 5E              LD      E,(HL)              
69C8: A2              AND     D                   
69C9: 5E              LD      E,(HL)              
69CA: A1              AND     C                   
69CB: 58              LD      E,B                 
69CC: 5E              LD      E,(HL)              
69CD: A3              AND     E                   
69CE: 62              LD      H,D                 
69CF: A1              AND     C                   
69D0: 62              LD      H,D                 
69D1: 66              LD      H,(HL)              
69D2: 68              LD      L,B                 
69D3: 6C              LD      L,H                 
69D4: 9D              SBC     L                   
69D5: A0              AND     B                   
69D6: 00              NOP                         
69D7: 01 A5 70        LD      BC,$70A5            
69DA: 00              NOP                         
69DB: 9D              SBC     L                   
69DC: A0              AND     B                   
69DD: 21 00 A3        LD      HL,$A300            
69E0: 78              LD      A,B                 
69E1: A2              AND     D                   
69E2: 40              LD      B,B                 
69E3: A1              AND     C                   
69E4: 40              LD      B,B                 
69E5: 40              LD      B,B                 
69E6: A3              AND     E                   
69E7: 40              LD      B,B                 
69E8: 01 00 9D        LD      BC,$9D00            
69EB: A2              AND     D                   
69EC: 6E              LD      L,(HL)              
69ED: 20 00           JR      NZ,$69EF            ; {}
69EF: 9D              SBC     L                   
69F0: 92              SUB     D                   
69F1: 6E              LD      L,(HL)              
69F2: 40              LD      B,B                 
69F3: 00              NOP                         
69F4: 9B              SBC     E                   
69F5: 03              INC     BC                  
69F6: A5              AND     L                   
69F7: 01 9C A3        LD      BC,$A39C            
69FA: 01 A6 01        LD      BC,$01A6            
69FD: 00              NOP                         
69FE: A8              XOR     B                   
69FF: 01 A2 01        LD      BC,$01A2            
6A02: 00              NOP                         
6A03: 9D              SBC     L                   
6A04: 42              LD      B,D                 
6A05: 6E              LD      L,(HL)              
6A06: 20 99           JR      NZ,$69A1            ; {}
6A08: A2              AND     D                   
6A09: 48              LD      C,B                 
6A0A: 56              LD      D,(HL)              
6A0B: 5C              LD      E,H                 
6A0C: 66              LD      H,(HL)              
6A0D: A4              AND     H                   
6A0E: 01 A2 3A        LD      BC,$3AA2            
6A11: 48              LD      C,B                 
6A12: 4E              LD      C,(HL)              
6A13: 58              LD      E,B                 
6A14: 01 56 A1        LD      BC,$A156            
6A17: 52              LD      D,D                 
6A18: 4E              LD      C,(HL)              
6A19: 4C              LD      C,H                 
6A1A: 3E A2           LD      A,$A2               
6A1C: 48              LD      C,B                 
6A1D: 56              LD      D,(HL)              
6A1E: 5C              LD      E,H                 
6A1F: 66              LD      H,(HL)              
6A20: A4              AND     H                   
6A21: 01 A2 3A        LD      BC,$3AA2            
6A24: 48              LD      C,B                 
6A25: 4E              LD      C,(HL)              
6A26: 58              LD      E,B                 
6A27: A3              AND     E                   
6A28: 01 00 A3        LD      BC,$A300            
6A2B: 01 9B 02        LD      BC,$029B            
6A2E: A2              AND     D                   
6A2F: 2C              INC     L                   
6A30: A3              AND     E                   
6A31: 2C              INC     L                   
6A32: A2              AND     D                   
6A33: 2C              INC     L                   
6A34: 9C              SBC     H                   
6A35: 9B              SBC     E                   
6A36: 02              LD      (BC),A              
6A37: A2              AND     D                   
6A38: 1E A3           LD      E,$A3               
6A3A: 1E A2           LD      E,$A2               
6A3C: 1E 9C           LD      E,$9C               
6A3E: 9B              SBC     E                   
6A3F: 02              LD      (BC),A              
6A40: A2              AND     D                   
6A41: 28 A3           JR      Z,$69E6             ; {}
6A43: 28 A2           JR      Z,$69E7             ; {}
6A45: 28 9C           JR      Z,$69E3             ; {}
6A47: 9B              SBC     E                   
6A48: 02              LD      (BC),A              
6A49: A2              AND     D                   
6A4A: 26 A3           LD      H,$A3               
6A4C: 26 A2           LD      H,$A2               
6A4E: 26 9C           LD      H,$9C               
6A50: 00              NOP                         
6A51: 9D              SBC     L                   
6A52: 42              LD      B,D                 
6A53: 6E              LD      L,(HL)              
6A54: 20 99           JR      NZ,$69EF            ; {}
6A56: 9B              SBC     E                   
6A57: 06 A3           LD      B,$A3               
6A59: 1E AA           LD      E,$AA               
6A5B: 1E 1E           LD      E,$1E               
6A5D: 1E 9C           LD      E,$9C               
6A5F: A3              AND     E                   
6A60: 1E 1E           LD      E,$1E               
6A62: 22              LD      (HLI),A             
6A63: 26 00           LD      H,$00               
6A65: 99              SBC     C                   
6A66: A3              AND     E                   
6A67: 28 AA           JR      Z,$6A13             ; {}
6A69: 28 28           JR      Z,$6A93             ; {}
6A6B: 24              INC     H                   
6A6C: A3              AND     E                   
6A6D: 28 AA           JR      Z,$6A19             ; {}
6A6F: 28 28           JR      Z,$6A99             ; {}
6A71: 28 A3           JR      Z,$6A16             ; {}
6A73: 24              INC     H                   
6A74: AA              XOR     D                   
6A75: 3C              INC     A                   
6A76: 3C              INC     A                   
6A77: 3C              INC     A                   
6A78: 9A              SBC     D                   
6A79: A3              AND     E                   
6A7A: 3A              LD      A,(HLD)             
6A7B: 22              LD      (HLI),A             
6A7C: 99              SBC     C                   
6A7D: 9B              SBC     E                   
6A7E: 02              LD      (BC),A              
6A7F: A3              AND     E                   
6A80: 2C              INC     L                   
6A81: AA              XOR     D                   
6A82: 2C              INC     L                   
6A83: 2C              INC     L                   
6A84: 2C              INC     L                   
6A85: 9C              SBC     H                   
6A86: A3              AND     E                   
6A87: 1E AA           LD      E,$AA               
6A89: 1E 1E           LD      E,$1E               
6A8B: 1E 9A           LD      E,$9A               
6A8D: A3              AND     E                   
6A8E: 1E 20           LD      E,$20               
6A90: 99              SBC     C                   
6A91: AA              XOR     D                   
6A92: 22              LD      (HLI),A             
6A93: 40              LD      B,B                 
6A94: 48              LD      C,B                 
6A95: 52              LD      D,D                 
6A96: 48              LD      C,B                 
6A97: 40              LD      B,B                 
6A98: 30 3E           JR      NC,$6AD8            ; {}
6A9A: 44              LD      B,H                 
6A9B: 4E              LD      C,(HL)              
6A9C: 44              LD      B,H                 
6A9D: 3E 3A           LD      A,$3A               
6A9F: 40              LD      B,B                 
6AA0: 48              LD      C,B                 
6AA1: 52              LD      D,D                 
6AA2: 48              LD      C,B                 
6AA3: 40              LD      B,B                 
6AA4: 30 3E           JR      NC,$6AE4            ; {}
6AA6: 44              LD      B,H                 
6AA7: 4E              LD      C,(HL)              
6AA8: 44              LD      B,H                 
6AA9: 30 A3           JR      NC,$6A4E            ; {}
6AAB: 32              LD      (HLD),A             
6AAC: AA              XOR     D                   
6AAD: 32              LD      (HLD),A             
6AAE: 32              LD      (HLD),A             
6AAF: 32              LD      (HLD),A             
6AB0: A3              AND     E                   
6AB1: 2A              LD      A,(HLI)             
6AB2: AA              XOR     D                   
6AB3: 2A              LD      A,(HLI)             
6AB4: 2A              LD      A,(HLI)             
6AB5: 2A              LD      A,(HLI)             
6AB6: 1E 28           LD      E,$28               
6AB8: 2C              INC     L                   
6AB9: 36 40           LD      (HL),$40            
6ABB: 44              LD      B,H                 
6ABC: 4E              LD      C,(HL)              
6ABD: 36 3A           LD      (HL),$3A            
6ABF: 3E 3A           LD      A,$3A               
6AC1: 36 00           LD      (HL),$00            
6AC3: 38 58           JR      C,$6B1D             ; {}
6AC5: 5E              LD      E,(HL)              
6AC6: 68              LD      L,B                 
6AC7: 5E              LD      E,(HL)              
6AC8: 58              LD      E,B                 
6AC9: 50              LD      D,B                 
6ACA: 58              LD      E,B                 
6ACB: 5E              LD      E,(HL)              
6ACC: 68              LD      L,B                 
6ACD: 5E              LD      E,(HL)              
6ACE: 58              LD      E,B                 
6ACF: 9B              SBC     E                   
6AD0: 02              LD      (BC),A              
6AD1: 50              LD      D,B                 
6AD2: 54              LD      D,H                 
6AD3: 5C              LD      E,H                 
6AD4: 62              LD      H,D                 
6AD5: 5C              LD      E,H                 
6AD6: 54              LD      D,H                 
6AD7: 9C              SBC     H                   
6AD8: 9B              SBC     E                   
6AD9: 02              LD      (BC),A              
6ADA: 4E              LD      C,(HL)              
6ADB: 54              LD      D,H                 
6ADC: 5C              LD      E,H                 
6ADD: 62              LD      H,D                 
6ADE: 5C              LD      E,H                 
6ADF: 54              LD      D,H                 
6AE0: 9C              SBC     H                   
6AE1: 40              LD      B,B                 
6AE2: 48              LD      C,B                 
6AE3: 4E              LD      C,(HL)              
6AE4: 54              LD      D,H                 
6AE5: 4E              LD      C,(HL)              
6AE6: 48              LD      C,B                 
6AE7: 40              LD      B,B                 
6AE8: 48              LD      C,B                 
6AE9: 4E              LD      C,(HL)              
6AEA: 54              LD      D,H                 
6AEB: 4E              LD      C,(HL)              
6AEC: 40              LD      B,B                 
6AED: 9B              SBC     E                   
6AEE: 02              LD      (BC),A              
6AEF: 99              SBC     C                   
6AF0: AA              XOR     D                   
6AF1: 32              LD      (HLD),A             
6AF2: 40              LD      B,B                 
6AF3: 46              LD      B,(HL)              
6AF4: 50              LD      D,B                 
6AF5: 58              LD      E,B                 
6AF6: 5E              LD      E,(HL)              
6AF7: 9A              SBC     D                   
6AF8: A3              AND     E                   
6AF9: 68              LD      L,B                 
6AFA: 01 9C 99        LD      BC,$999C            
6AFD: 9B              SBC     E                   
6AFE: 02              LD      (BC),A              
6AFF: AA              XOR     D                   
6B00: 2A              LD      A,(HLI)             
6B01: 42              LD      B,D                 
6B02: 42              LD      B,D                 
6B03: 42              LD      B,D                 
6B04: 46              LD      B,(HL)              
6B05: 4A              LD      C,D                 
6B06: 9C              SBC     H                   
6B07: A3              AND     E                   
6B08: 4E              LD      C,(HL)              
6B09: 1E 22           LD      E,$22               
6B0B: 26 00           LD      H,$00               
6B0D: 38 40           JR      C,$6B4F             ; {}
6B0F: 46              LD      B,(HL)              
6B10: 50              LD      D,B                 
6B11: 58              LD      E,B                 
6B12: 5E              LD      E,(HL)              
6B13: 9A              SBC     D                   
6B14: A3              AND     E                   
6B15: 68              LD      L,B                 
6B16: 99              SBC     C                   
6B17: AA              XOR     D                   
6B18: 38 38           JR      C,$6B52             ; {}
6B1A: 38 2A           JR      C,$6B46             ; {}
6B1C: 32              LD      (HLD),A             
6B1D: 38 42           JR      C,$6B61             ; {}
6B1F: 4A              LD      C,D                 
6B20: 50              LD      D,B                 
6B21: 9A              SBC     D                   
6B22: A3              AND     E                   
6B23: 72              LD      (HL),D              
6B24: 99              SBC     C                   
6B25: AA              XOR     D                   
6B26: 2A              LD      A,(HLI)             
6B27: 2A              LD      A,(HLI)             
6B28: 2A              LD      A,(HLI)             
6B29: 00              NOP                         
6B2A: 9B              SBC     E                   
6B2B: 02              LD      (BC),A              
6B2C: A2              AND     D                   
6B2D: 28 1E           JR      Z,$6B4D             ; {}
6B2F: 9C              SBC     H                   
6B30: 9B              SBC     E                   
6B31: 02              LD      (BC),A              
6B32: 24              INC     H                   
6B33: 1A              LD      A,(DE)              
6B34: 9C              SBC     H                   
6B35: 00              NOP                         
6B36: 9B              SBC     E                   
6B37: 02              LD      (BC),A              
6B38: A2              AND     D                   
6B39: 20 2E           JR      NZ,$6B69            ; {}
6B3B: 9C              SBC     H                   
6B3C: 9B              SBC     E                   
6B3D: 02              LD      (BC),A              
6B3E: 24              INC     H                   
6B3F: 32              LD      (HLD),A             
6B40: 9C              SBC     H                   
6B41: 9B              SBC     E                   
6B42: 02              LD      (BC),A              
6B43: 28 1E           JR      Z,$6B63             ; {}
6B45: 9C              SBC     H                   
6B46: 9B              SBC     E                   
6B47: 02              LD      (BC),A              
6B48: 2A              LD      A,(HLI)             
6B49: 20 9C           JR      NZ,$6AE7            ; {}
6B4B: 00              NOP                         
6B4C: A3              AND     E                   
6B4D: 28 A2           JR      Z,$6AF1             ; {}
6B4F: 28 A1           JR      Z,$6AF2             ; {}
6B51: 28 28           JR      Z,$6B7B             ; {}
6B53: A3              AND     E                   
6B54: 28 01           JR      Z,$6B57             ; {}
6B56: 00              NOP                         
6B57: 9B              SBC     E                   
6B58: 14              INC     D                   
6B59: A5              AND     L                   
6B5A: 01 9C A3        LD      BC,$A39C            
6B5D: 01 00 9B        LD      BC,$9B00            
6B60: 06 A5           LD      B,$A5               
6B62: 01 9C A3        LD      BC,$A39C            
6B65: 01 00 9B        LD      BC,$9B00            
6B68: 03              INC     BC                  
6B69: A3              AND     E                   
6B6A: 15              DEC     D                   
6B6B: AA              XOR     D                   
6B6C: 1A              LD      A,(DE)              
6B6D: 1A              LD      A,(DE)              
6B6E: 1A              LD      A,(DE)              
6B6F: 9C              SBC     H                   
6B70: AA              XOR     D                   
6B71: 15              DEC     D                   
6B72: 15              DEC     D                   
6B73: 15              DEC     D                   
6B74: 1A              LD      A,(DE)              
6B75: 15              DEC     D                   
6B76: 15              DEC     D                   
6B77: 00              NOP                         
6B78: 9B              SBC     E                   
6B79: 08 AA 29        LD      ($29AA),SP          
6B7C: 29              ADD     HL,HL               
6B7D: 29              ADD     HL,HL               
6B7E: 1A              LD      A,(DE)              
6B7F: 29              ADD     HL,HL               
6B80: 29              ADD     HL,HL               
6B81: 9C              SBC     H                   
6B82: 00              NOP                         
6B83: 9B              SBC     E                   
6B84: 02              LD      (BC),A              
6B85: A1              AND     C                   
6B86: 1A              LD      A,(DE)              
6B87: 1A              LD      A,(DE)              
6B88: A3              AND     E                   
6B89: 1A              LD      A,(DE)              
6B8A: 9C              SBC     H                   
6B8B: 9B              SBC     E                   
6B8C: 04              INC     B                   
6B8D: A1              AND     C                   
6B8E: 1A              LD      A,(DE)              
6B8F: 9C              SBC     H                   
6B90: 00              NOP                         
6B91: A3              AND     E                   
6B92: 1A              LD      A,(DE)              
6B93: A2              AND     D                   
6B94: 1A              LD      A,(DE)              
6B95: A1              AND     C                   
6B96: 1A              LD      A,(DE)              
6B97: 1A              LD      A,(DE)              
6B98: A3              AND     E                   
6B99: 1A              LD      A,(DE)              
6B9A: 01 00 00        LD      BC,$0000            
6B9D: 2B              DEC     HL                  
6B9E: 4A              LD      C,D                 
6B9F: A7              AND     A                   
6BA0: 6B              LD      L,E                 
6BA1: B9              CP      C                   
6BA2: 6B              LD      L,E                 
6BA3: CB 6B           BIT     1,E                 
6BA5: 00              NOP                         
6BA6: 00              NOP                         
6BA7: D1              POP     DE                  
6BA8: 6B              LD      L,E                 
6BA9: D6 6B           SUB     $6B                 
6BAB: D6 6B           SUB     $6B                 
6BAD: 41              LD      B,C                 
6BAE: 6F              LD      L,A                 
6BAF: D6 6B           SUB     $6B                 
6BB1: 78              LD      A,B                 
6BB2: 6F              LD      L,A                 
6BB3: D6 6B           SUB     $6B                 
6BB5: FF              RST     0X38                
6BB6: FF              RST     0X38                
6BB7: 32              LD      (HLD),A             
6BB8: 5E              LD      E,(HL)              
6BB9: D1              POP     DE                  
6BBA: 6B              LD      L,E                 
6BBB: E0 6B           LD      ($FF00+$6B),A       
6BBD: E0 6B           LD      ($FF00+$6B),A       
6BBF: 41              LD      B,C                 
6BC0: 6F              LD      L,A                 
6BC1: E0 6B           LD      ($FF00+$6B),A       
6BC3: 78              LD      A,B                 
6BC4: 6F              LD      L,A                 
6BC5: E0 6B           LD      ($FF00+$6B),A       
6BC7: FF              RST     0X38                
6BC8: FF              RST     0X38                
6BC9: 52              LD      D,D                 
6BCA: 5E              LD      E,(HL)              
6BCB: E2              LD      (C),A               
6BCC: 6F              LD      L,A                 
6BCD: FF              RST     0X38                
6BCE: FF              RST     0X38                
6BCF: 5E              LD      E,(HL)              
6BD0: 5E              LD      E,(HL)              
6BD1: 9D              SBC     L                   
6BD2: 40              LD      B,B                 
6BD3: 00              NOP                         
6BD4: 40              LD      B,B                 
6BD5: 00              NOP                         
6BD6: A1              AND     C                   
6BD7: 34              INC     (HL)                
6BD8: 36 34           LD      (HL),$34            
6BDA: 32              LD      (HLD),A             
6BDB: 30 2E           JR      NC,$6C0B            ; {}
6BDD: 30 32           JR      NC,$6C11            ; {}
6BDF: 00              NOP                         
6BE0: A1              AND     C                   
6BE1: 48              LD      C,B                 
6BE2: 4A              LD      C,D                 
6BE3: 48              LD      C,B                 
6BE4: 46              LD      B,(HL)              
6BE5: 44              LD      B,H                 
6BE6: 42              LD      B,D                 
6BE7: 44              LD      B,H                 
6BE8: 46              LD      B,(HL)              
6BE9: 00              NOP                         
6BEA: 00              NOP                         
6BEB: 49              LD      C,C                 
6BEC: 4A              LD      C,D                 
6BED: F5              PUSH    AF                  
6BEE: 6B              LD      L,E                 
6BEF: 15              DEC     D                   
6BF0: 6C              LD      L,H                 
6BF1: 39              ADD     HL,SP               
6BF2: 6C              LD      L,H                 
6BF3: 59              LD      E,C                 
6BF4: 6C              LD      L,H                 
6BF5: E2              LD      (C),A               
6BF6: 6F              LD      L,A                 
6BF7: 77              LD      (HL),A              
6BF8: 6C              LD      L,H                 
6BF9: 81              ADD     A,C                 
6BFA: 6D              LD      L,L                 
6BFB: 0A              LD      A,(BC)              
6BFC: 70              LD      (HL),B              
6BFD: 87              ADD     A,A                 
6BFE: 6F              LD      L,A                 
6BFF: 7E              LD      A,(HL)              
6C00: 6C              LD      L,H                 
6C01: 8C              ADC     A,H                 
6C02: 6F              LD      L,A                 
6C03: 84              ADD     A,H                 
6C04: 6C              LD      L,H                 
6C05: 82              ADD     A,D                 
6C06: 6F              LD      L,A                 
6C07: 8A              ADC     A,D                 
6C08: 6C              LD      L,H                 
6C09: FB              EI                          
6C0A: 6C              LD      L,H                 
6C0B: 61              LD      H,C                 
6C0C: 6D              LD      L,L                 
6C0D: 74              LD      (HL),H              
6C0E: 6D              LD      L,L                 
6C0F: 79              LD      A,C                 
6C10: 6D              LD      L,L                 
6C11: FF              RST     0X38                
6C12: FF              RST     0X38                
6C13: 10 70           ;;STOP    $70                 
6C15: E2              LD      (C),A               
6C16: 6F              LD      L,A                 
6C17: 02              LD      (BC),A              
6C18: 6D              LD      L,L                 
6C19: 81              ADD     A,C                 
6C1A: 6D              LD      L,L                 
6C1B: 0A              LD      A,(BC)              
6C1C: 70              LD      (HL),B              
6C1D: 7D              LD      A,L                 
6C1E: 6F              LD      L,A                 
6C1F: 09              ADD     HL,BC               
6C20: 6D              LD      L,L                 
6C21: 91              SUB     C                   
6C22: 6F              LD      L,A                 
6C23: 28 6D           JR      Z,$6C92             ; {}
6C25: 04              INC     B                   
6C26: 70              LD      (HL),B              
6C27: 7C              LD      A,H                 
6C28: 6D              LD      L,L                 
6C29: 48              LD      C,B                 
6C2A: 6D              LD      L,L                 
6C2B: 55              LD      D,L                 
6C2C: 6D              LD      L,L                 
6C2D: 61              LD      H,C                 
6C2E: 6D              LD      L,L                 
6C2F: 04              INC     B                   
6C30: 70              LD      (HL),B              
6C31: 74              LD      (HL),H              
6C32: 6D              LD      L,L                 
6C33: 79              LD      A,C                 
6C34: 6D              LD      L,L                 
6C35: FF              RST     0X38                
6C36: FF              RST     0X38                
6C37: 10 70           ;;STOP    $70                 
6C39: E2              LD      (C),A               
6C3A: 6F              LD      L,A                 
6C3B: 96              SUB     (HL)                
6C3C: 6F              LD      L,A                 
6C3D: 81              ADD     A,C                 
6C3E: 6D              LD      L,L                 
6C3F: 04              INC     B                   
6C40: 70              LD      (HL),B              
6C41: 0A              LD      A,(BC)              
6C42: 70              LD      (HL),B              
6C43: 9C              SBC     H                   
6C44: 6F              LD      L,A                 
6C45: 93              SUB     E                   
6C46: 6D              LD      L,L                 
6C47: B5              OR      L                   
6C48: 6D              LD      L,L                 
6C49: D6 6E           SUB     $6E                 
6C4B: 48              LD      C,B                 
6C4C: 6D              LD      L,L                 
6C4D: 55              LD      D,L                 
6C4E: 6D              LD      L,L                 
6C4F: 61              LD      H,C                 
6C50: 6D              LD      L,L                 
6C51: 0A              LD      A,(BC)              
6C52: 70              LD      (HL),B              
6C53: 79              LD      A,C                 
6C54: 6D              LD      L,L                 
6C55: FF              RST     0X38                
6C56: FF              RST     0X38                
6C57: 10 70           ;;STOP    $70                 
6C59: CB 6D           BIT     1,E                 
6C5B: D7              RST     0X10                
6C5C: 6D              LD      L,L                 
6C5D: D7              RST     0X10                
6C5E: 6D              LD      L,L                 
6C5F: D7              RST     0X10                
6C60: 6D              LD      L,L                 
6C61: D7              RST     0X10                
6C62: 6D              LD      L,L                 
6C63: EC                              
6C64: 6D              LD      L,L                 
6C65: EC                              
6C66: 6D              LD      L,L                 
6C67: EC                              
6C68: 6D              LD      L,L                 
6C69: EC                              
6C6A: 6D              LD      L,L                 
6C6B: EC                              
6C6C: 6D              LD      L,L                 
6C6D: EC                              
6C6E: 6D              LD      L,L                 
6C6F: 16 6E           LD      D,$6E               
6C71: 1A              LD      A,(DE)              
6C72: 6E              LD      L,(HL)              
6C73: FF              RST     0X38                
6C74: FF              RST     0X38                
6C75: 16 70           LD      D,$70               
6C77: 9D              SBC     L                   
6C78: 10 00           ;;STOP    $00                 
6C7A: 81              ADD     A,C                 
6C7B: A2              AND     D                   
6C7C: 01 00 A4        LD      BC,$A400            
6C7F: 90              SUB     B                   
6C80: 82              ADD     A,D                 
6C81: 86              ADD     A,(HL)              
6C82: 78              LD      A,B                 
6C83: 00              NOP                         
6C84: A4              AND     H                   
6C85: 90              SUB     B                   
6C86: 82              ADD     A,D                 
6C87: 86              ADD     A,(HL)              
6C88: 01 00 9D        LD      BC,$9D00            
6C8B: B1              OR      C                   
6C8C: 82              ADD     A,D                 
6C8D: 00              NOP                         
6C8E: A2              AND     D                   
6C8F: 10 10           ;;STOP    $10                 
6C91: 9D              SBC     L                   
6C92: 71              LD      (HL),C              
6C93: 82              ADD     A,D                 
6C94: 80              ADD     A,B                 
6C95: A1              AND     C                   
6C96: 6E              LD      L,(HL)              
6C97: 60              LD      H,B                 
6C98: 6E              LD      L,(HL)              
6C99: 78              LD      A,B                 
6C9A: A3              AND     E                   
6C9B: 01 9D B1        LD      BC,$B19D            
6C9E: 82              ADD     A,D                 
6C9F: 00              NOP                         
6CA0: A2              AND     D                   
6CA1: 01 06 10        LD      BC,$1006            
6CA4: 10 9D           ;;STOP    $9D                 
6CA6: 71              LD      (HL),C              
6CA7: 82              ADD     A,D                 
6CA8: 80              ADD     A,B                 
6CA9: A1              AND     C                   
6CAA: 6E              LD      L,(HL)              
6CAB: 60              LD      H,B                 
6CAC: 6E              LD      L,(HL)              
6CAD: 78              LD      A,B                 
6CAE: A3              AND     E                   
6CAF: 01 9D B1        LD      BC,$B19D            
6CB2: 82              ADD     A,D                 
6CB3: 00              NOP                         
6CB4: A2              AND     D                   
6CB5: 01 10 18        LD      BC,$1810            
6CB8: 18 9D           JR      $6C57               ; {}
6CBA: 71              LD      (HL),C              
6CBB: 82              ADD     A,D                 
6CBC: 80              ADD     A,B                 
6CBD: A1              AND     C                   
6CBE: 6A              LD      L,D                 
6CBF: 5C              LD      E,H                 
6CC0: 6A              LD      L,D                 
6CC1: 6E              LD      L,(HL)              
6CC2: A3              AND     E                   
6CC3: 01 9D B1        LD      BC,$B19D            
6CC6: 82              ADD     A,D                 
6CC7: 00              NOP                         
6CC8: A2              AND     D                   
6CC9: 01 0E 18        LD      BC,$180E            
6CCC: 18 9D           JR      $6C6B               ; {}
6CCE: 71              LD      (HL),C              
6CCF: 82              ADD     A,D                 
6CD0: 80              ADD     A,B                 
6CD1: A1              AND     C                   
6CD2: 6A              LD      L,D                 
6CD3: 5C              LD      E,H                 
6CD4: 6A              LD      L,D                 
6CD5: 6E              LD      L,(HL)              
6CD6: 9D              SBC     L                   
6CD7: 80              ADD     A,B                 
6CD8: 00              NOP                         
6CD9: 00              NOP                         
6CDA: A3              AND     E                   
6CDB: 18 14           JR      $6CF1               ; {}
6CDD: 9D              SBC     L                   
6CDE: A1              AND     C                   
6CDF: 82              ADD     A,D                 
6CE0: 00              NOP                         
6CE1: A2              AND     D                   
6CE2: 10 10           ;;STOP    $10                 
6CE4: A4              AND     H                   
6CE5: 01 A2 01        LD      BC,$01A2            
6CE8: 06 10           LD      B,$10               
6CEA: 10 A4           ;;STOP    $A4                 
6CEC: 01 A3 10        LD      BC,$10A3            
6CEF: 9B              SBC     E                   
6CF0: 03              INC     BC                  
6CF1: A2              AND     D                   
6CF2: 06 06           LD      B,$06               
6CF4: A4              AND     H                   
6CF5: 01 A2 01        LD      BC,$01A2            
6CF8: 14              INC     D                   
6CF9: 9C              SBC     H                   
6CFA: 00              NOP                         
6CFB: 9D              SBC     L                   
6CFC: 26 00           LD      H,$00               
6CFE: 00              NOP                         
6CFF: A3              AND     E                   
6D00: 01 00 9D        LD      BC,$9D00            
6D03: 40              LD      B,B                 
6D04: 00              NOP                         
6D05: 41              LD      B,C                 
6D06: A2              AND     D                   
6D07: 01 00 9B        LD      BC,$9B00            
6D0A: 03              INC     BC                  
6D0B: A5              AND     L                   
6D0C: 01 9C A4        LD      BC,$A49C            
6D0F: 01 A2 01        LD      BC,$01A2            
6D12: 48              LD      C,B                 
6D13: 4C              LD      C,H                 
6D14: A8              XOR     B                   
6D15: 4E              LD      C,(HL)              
6D16: A2              AND     D                   
6D17: 48              LD      C,B                 
6D18: 4C              LD      C,H                 
6D19: A8              XOR     B                   
6D1A: 4E              LD      C,(HL)              
6D1B: A2              AND     D                   
6D1C: 4C              LD      C,H                 
6D1D: 48              LD      C,B                 
6D1E: 3E A7           LD      A,$A7               
6D20: 44              LD      B,H                 
6D21: A8              XOR     B                   
6D22: 48              LD      C,B                 
6D23: A2              AND     D                   
6D24: 01 A8 01        LD      BC,$01A8            
6D27: 00              NOP                         
6D28: 9B              SBC     E                   
6D29: 03              INC     BC                  
6D2A: A1              AND     C                   
6D2B: 60              LD      H,B                 
6D2C: 5C              LD      E,H                 
6D2D: 58              LD      E,B                 
6D2E: 4E              LD      C,(HL)              
6D2F: 48              LD      C,B                 
6D30: 4E              LD      C,(HL)              
6D31: 58              LD      E,B                 
6D32: 5C              LD      E,H                 
6D33: 9C              SBC     H                   
6D34: 60              LD      H,B                 
6D35: 5C              LD      E,H                 
6D36: 58              LD      E,B                 
6D37: 4E              LD      C,(HL)              
6D38: 48              LD      C,B                 
6D39: 4E              LD      C,(HL)              
6D3A: 58              LD      E,B                 
6D3B: 60              LD      H,B                 
6D3C: 9B              SBC     E                   
6D3D: 02              LD      (BC),A              
6D3E: 5C              LD      E,H                 
6D3F: 56              LD      D,(HL)              
6D40: 52              LD      D,D                 
6D41: 4E              LD      C,(HL)              
6D42: 44              LD      B,H                 
6D43: 4E              LD      C,(HL)              
6D44: 52              LD      D,D                 
6D45: 56              LD      D,(HL)              
6D46: 9C              SBC     H                   
6D47: 00              NOP                         
6D48: 9B              SBC     E                   
6D49: 02              LD      (BC),A              
6D4A: A1              AND     C                   
6D4B: 64              LD      H,H                 
6D4C: 5C              LD      E,H                 
6D4D: 56              LD      D,(HL)              
6D4E: 4E              LD      C,(HL)              
6D4F: 4C              LD      C,H                 
6D50: 4E              LD      C,(HL)              
6D51: 56              LD      D,(HL)              
6D52: 5C              LD      E,H                 
6D53: 9C              SBC     H                   
6D54: 00              NOP                         
6D55: 9B              SBC     E                   
6D56: 02              LD      (BC),A              
6D57: 6A              LD      L,D                 
6D58: 64              LD      H,H                 
6D59: 5C              LD      E,H                 
6D5A: 56              LD      D,(HL)              
6D5B: 52              LD      D,D                 
6D5C: 56              LD      D,(HL)              
6D5D: 5C              LD      E,H                 
6D5E: 64              LD      H,H                 
6D5F: 9C              SBC     H                   
6D60: 00              NOP                         
6D61: A1              AND     C                   
6D62: 06 14           LD      B,$14               
6D64: 1C              INC     E                   
6D65: 1E 26           LD      E,$26               
6D67: 2C              INC     L                   
6D68: 34              INC     (HL)                
6D69: 36 3E           LD      (HL),$3E            
6D6B: 44              LD      B,H                 
6D6C: 4C              LD      C,H                 
6D6D: 4E              LD      C,(HL)              
6D6E: 56              LD      D,(HL)              
6D6F: 5C              LD      E,H                 
6D70: A2              AND     D                   
6D71: 64              LD      H,H                 
6D72: 66              LD      H,(HL)              
6D73: 00              NOP                         
6D74: 9D              SBC     L                   
6D75: 77              LD      (HL),A              
6D76: 00              NOP                         
6D77: 80              ADD     A,B                 
6D78: 00              NOP                         
6D79: A5              AND     L                   
6D7A: 8C              ADC     A,H                 
6D7B: 00              NOP                         
6D7C: 9D              SBC     L                   
6D7D: 40              LD      B,B                 
6D7E: 00              NOP                         
6D7F: 80              ADD     A,B                 
6D80: 00              NOP                         
6D81: A2              AND     D                   
6D82: 48              LD      C,B                 
6D83: 4C              LD      C,H                 
6D84: A8              XOR     B                   
6D85: 4E              LD      C,(HL)              
6D86: A2              AND     D                   
6D87: 48              LD      C,B                 
6D88: 4C              LD      C,H                 
6D89: A8              XOR     B                   
6D8A: 4E              LD      C,(HL)              
6D8B: A2              AND     D                   
6D8C: 4C              LD      C,H                 
6D8D: 48              LD      C,B                 
6D8E: A6              AND     (HL)                
6D8F: 3E A5           LD      A,$A5               
6D91: 56              LD      D,(HL)              
6D92: 00              NOP                         
6D93: 9B              SBC     E                   
6D94: 03              INC     BC                  
6D95: A5              AND     L                   
6D96: 01 9C A4        LD      BC,$A49C            
6D99: 01 A2 01        LD      BC,$01A2            
6D9C: A2              AND     D                   
6D9D: 36 3A           LD      (HL),$3A            
6D9F: A4              AND     H                   
6DA0: 3E A3           LD      A,$A3               
6DA2: 01 A2 36        LD      BC,$36A2            
6DA5: 3A              LD      A,(HLD)             
6DA6: A4              AND     H                   
6DA7: 3E A3           LD      A,$A3               
6DA9: 01 A2 3A        LD      BC,$3AA2            
6DAC: A3              AND     E                   
6DAD: 36 A7           LD      (HL),$A7            
6DAF: 34              INC     (HL)                
6DB0: A4              AND     H                   
6DB1: 36 A8           LD      (HL),$A8            
6DB3: 01 00 A2        LD      BC,$A200            
6DB6: 48              LD      C,B                 
6DB7: 4C              LD      C,H                 
6DB8: A4              AND     H                   
6DB9: 4E              LD      C,(HL)              
6DBA: A3              AND     E                   
6DBB: 01 A2 48        LD      BC,$48A2            
6DBE: 4E              LD      C,(HL)              
6DBF: A4              AND     H                   
6DC0: 58              LD      E,B                 
6DC1: A3              AND     E                   
6DC2: 01 A2 56        LD      BC,$56A2            
6DC5: 52              LD      D,D                 
6DC6: A5              AND     L                   
6DC7: 56              LD      D,(HL)              
6DC8: A2              AND     D                   
6DC9: 01 00 9B        LD      BC,$9B00            
6DCC: 05              DEC     B                   
6DCD: A5              AND     L                   
6DCE: 01 9C A4        LD      BC,$A49C            
6DD1: 01 A2 01        LD      BC,$01A2            
6DD4: A6              AND     (HL)                
6DD5: 01 00 9B        LD      BC,$9B00            
6DD8: 03              INC     BC                  
6DD9: A2              AND     D                   
6DDA: 15              DEC     D                   
6DDB: A9              XOR     C                   
6DDC: 15              DEC     D                   
6DDD: AD              XOR     L                   
6DDE: 01 A9 15        LD      BC,$15A9            
6DE1: AD              XOR     L                   
6DE2: 01 A9 15        LD      BC,$15A9            
6DE5: 9C              SBC     H                   
6DE6: 9B              SBC     E                   
6DE7: 04              INC     B                   
6DE8: A1              AND     C                   
6DE9: 15              DEC     D                   
6DEA: 9C              SBC     H                   
6DEB: 00              NOP                         
6DEC: A2              AND     D                   
6DED: 24              INC     H                   
6DEE: A9              XOR     C                   
6DEF: 1A              LD      A,(DE)              
6DF0: AD              XOR     L                   
6DF1: 01 A9 1A        LD      BC,$1AA9            
6DF4: AD              XOR     L                   
6DF5: 01 A9 1A        LD      BC,$1AA9            
6DF8: A2              AND     D                   
6DF9: 1A              LD      A,(DE)              
6DFA: A9              XOR     C                   
6DFB: 1A              LD      A,(DE)              
6DFC: AD              XOR     L                   
6DFD: 01 A9 1A        LD      BC,$1AA9            
6E00: AD              XOR     L                   
6E01: 01 A9 1A        LD      BC,$1AA9            
6E04: A2              AND     D                   
6E05: 24              INC     H                   
6E06: A9              XOR     C                   
6E07: 15              DEC     D                   
6E08: AD              XOR     L                   
6E09: 01 A9 1A        LD      BC,$1AA9            
6E0C: AD              XOR     L                   
6E0D: 01 A9 1A        LD      BC,$1AA9            
6E10: 9B              SBC     E                   
6E11: 04              INC     B                   
6E12: A1              AND     C                   
6E13: 1A              LD      A,(DE)              
6E14: 9C              SBC     H                   
6E15: 00              NOP                         
6E16: A4              AND     H                   
6E17: 24              INC     H                   
6E18: 01 00 9B        LD      BC,$9B00            
6E1B: 04              INC     B                   
6E1C: A5              AND     L                   
6E1D: 01 9C A7        LD      BC,$A79C            
6E20: 01 00 66        LD      BC,$6600            
6E23: 66              LD      H,(HL)              
6E24: 66              LD      H,(HL)              
6E25: 66              LD      H,(HL)              
6E26: 66              LD      H,(HL)              
6E27: 66              LD      H,(HL)              
6E28: 66              LD      H,(HL)              
6E29: 66              LD      H,(HL)              
6E2A: 00              NOP                         
6E2B: 00              NOP                         
6E2C: 00              NOP                         
6E2D: 00              NOP                         
6E2E: 00              NOP                         
6E2F: 00              NOP                         
6E30: 00              NOP                         
6E31: 00              NOP                         
6E32: 88              ADC     A,B                 
6E33: 88              ADC     A,B                 
6E34: 00              NOP                         
6E35: 00              NOP                         
6E36: 00              NOP                         
6E37: 00              NOP                         
6E38: 00              NOP                         
6E39: 00              NOP                         
6E3A: 00              NOP                         
6E3B: 00              NOP                         
6E3C: 00              NOP                         
6E3D: 00              NOP                         
6E3E: 00              NOP                         
6E3F: 00              NOP                         
6E40: 00              NOP                         
6E41: 00              NOP                         
6E42: 88              ADC     A,B                 
6E43: 88              ADC     A,B                 
6E44: 88              ADC     A,B                 
6E45: 88              ADC     A,B                 
6E46: 88              ADC     A,B                 
6E47: 88              ADC     A,B                 
6E48: 88              ADC     A,B                 
6E49: 88              ADC     A,B                 
6E4A: 00              NOP                         
6E4B: 00              NOP                         
6E4C: 00              NOP                         
6E4D: 00              NOP                         
6E4E: 00              NOP                         
6E4F: 00              NOP                         
6E50: 00              NOP                         
6E51: 00              NOP                         
6E52: 88              ADC     A,B                 
6E53: 88              ADC     A,B                 
6E54: 88              ADC     A,B                 
6E55: 88              ADC     A,B                 
6E56: 00              NOP                         
6E57: 00              NOP                         
6E58: 00              NOP                         
6E59: 00              NOP                         
6E5A: 88              ADC     A,B                 
6E5B: 88              ADC     A,B                 
6E5C: 88              ADC     A,B                 
6E5D: 88              ADC     A,B                 
6E5E: 00              NOP                         
6E5F: 00              NOP                         
6E60: 00              NOP                         
6E61: 00              NOP                         
6E62: AA              XOR     D                   
6E63: AA              XOR     D                   
6E64: AA              XOR     D                   
6E65: AA              XOR     D                   
6E66: AA              XOR     D                   
6E67: AA              XOR     D                   
6E68: AA              XOR     D                   
6E69: AA              XOR     D                   
6E6A: 00              NOP                         
6E6B: 00              NOP                         
6E6C: 00              NOP                         
6E6D: 00              NOP                         
6E6E: 00              NOP                         
6E6F: 00              NOP                         
6E70: 00              NOP                         
6E71: 00              NOP                         
6E72: 06 9B           LD      B,$9B               
6E74: CD DE EE        CALL    $EEDE               
6E77: FF              RST     0X38                
6E78: FF              RST     0X38                
6E79: FE 06           CP      $06                 
6E7B: 9B              SBC     E                   
6E7C: CD DE EE        CALL    $EEDE               
6E7F: FF              RST     0X38                
6E80: FF              RST     0X38                
6E81: FE 7F           CP      $7F                 
6E83: FF              RST     0X38                
6E84: 57              LD      D,A                 
6E85: 73              LD      (HL),E              
6E86: 55              LD      D,L                 
6E87: 34              INC     (HL)                
6E88: 42              LD      B,D                 
6E89: 21 7F FF        LD      HL,$FF7F            
6E8C: 57              LD      D,A                 
6E8D: 73              LD      (HL),E              
6E8E: 55              LD      D,L                 
6E8F: 34              INC     (HL)                
6E90: 42              LD      B,D                 
6E91: 21 33 33        LD      HL,$3333            
6E94: 33              INC     SP                  
6E95: 33              INC     SP                  
6E96: 00              NOP                         
6E97: 00              NOP                         
6E98: 00              NOP                         
6E99: 00              NOP                         
6E9A: 33              INC     SP                  
6E9B: 33              INC     SP                  
6E9C: 33              INC     SP                  
6E9D: 33              INC     SP                  
6E9E: 00              NOP                         
6E9F: 00              NOP                         
6EA0: 00              NOP                         
6EA1: 00              NOP                         
6EA2: 11 11 11        LD      DE,$1111            
6EA5: 11 00 00        LD      DE,$0000            
6EA8: 00              NOP                         
6EA9: 00              NOP                         
6EAA: 11 11 11        LD      DE,$1111            
6EAD: 11 00 00        LD      DE,$0000            
6EB0: 00              NOP                         
6EB1: 00              NOP                         
6EB2: 44              LD      B,H                 
6EB3: 44              LD      B,H                 
6EB4: 44              LD      B,H                 
6EB5: 44              LD      B,H                 
6EB6: 00              NOP                         
6EB7: 00              NOP                         
6EB8: 00              NOP                         
6EB9: 00              NOP                         
6EBA: 44              LD      B,H                 
6EBB: 44              LD      B,H                 
6EBC: 44              LD      B,H                 
6EBD: 44              LD      B,H                 
6EBE: 00              NOP                         
6EBF: 00              NOP                         
6EC0: 00              NOP                         
6EC1: 00              NOP                         
6EC2: 9D              SBC     L                   
6EC3: 42              LD      B,D                 
6EC4: 6E              LD      L,(HL)              
6EC5: 20 00           JR      NZ,$6EC7            ; {}
6EC7: 9D              SBC     L                   
6EC8: 42              LD      B,D                 
6EC9: 6E              LD      L,(HL)              
6ECA: 40              LD      B,B                 
6ECB: 00              NOP                         
6ECC: 9D              SBC     L                   
6ECD: 52              LD      D,D                 
6ECE: 6E              LD      L,(HL)              
6ECF: 21 00 9D        LD      HL,$9D00            
6ED2: 52              LD      D,D                 
6ED3: 6E              LD      L,(HL)              
6ED4: 40              LD      B,B                 
6ED5: 00              NOP                         
6ED6: 9D              SBC     L                   
6ED7: 52              LD      D,D                 
6ED8: 6E              LD      L,(HL)              
6ED9: 40              LD      B,B                 
6EDA: 99              SBC     C                   
6EDB: 00              NOP                         
6EDC: 9D              SBC     L                   
6EDD: 22              LD      (HLI),A             
6EDE: 6E              LD      L,(HL)              
6EDF: 20 00           JR      NZ,$6EE1            ; {}
6EE1: 9D              SBC     L                   
6EE2: 62              LD      H,D                 
6EE3: 6E              LD      L,(HL)              
6EE4: 20 00           JR      NZ,$6EE6            ; {}
6EE6: 9D              SBC     L                   
6EE7: B2              OR      D                   
6EE8: 6E              LD      L,(HL)              
6EE9: 40              LD      B,B                 
6EEA: 99              SBC     C                   
6EEB: 00              NOP                         
6EEC: 9D              SBC     L                   
6EED: 32              LD      (HLD),A             
6EEE: 6E              LD      L,(HL)              
6EEF: 21 00 9D        LD      HL,$9D00            
6EF2: 32              LD      (HLD),A             
6EF3: 6E              LD      L,(HL)              
6EF4: 25              DEC     H                   
6EF5: 00              NOP                         
6EF6: 9D              SBC     L                   
6EF7: 32              LD      (HLD),A             
6EF8: 6E              LD      L,(HL)              
6EF9: 40              LD      B,B                 
6EFA: 00              NOP                         
6EFB: 9D              SBC     L                   
6EFC: 42              LD      B,D                 
6EFD: 00              NOP                         
6EFE: 80              ADD     A,B                 
6EFF: 00              NOP                         
6F00: 9D              SBC     L                   
6F01: 53              LD      D,E                 
6F02: 00              NOP                         
6F03: 80              ADD     A,B                 
6F04: 00              NOP                         
6F05: 9D              SBC     L                   
6F06: 50              LD      D,B                 
6F07: 83              ADD     A,E                 
6F08: 40              LD      B,B                 
6F09: 00              NOP                         
6F0A: 9D              SBC     L                   
6F0B: 60              LD      H,B                 
6F0C: 81              ADD     A,C                 
6F0D: 80              ADD     A,B                 
6F0E: 00              NOP                         
6F0F: 9D              SBC     L                   
6F10: 71              LD      (HL),C              
6F11: 00              NOP                         
6F12: 40              LD      B,B                 
6F13: 00              NOP                         
6F14: 9D              SBC     L                   
6F15: 42              LD      B,D                 
6F16: 00              NOP                         
6F17: 40              LD      B,B                 
6F18: 00              NOP                         
6F19: 9D              SBC     L                   
6F1A: 33              INC     SP                  
6F1B: 00              NOP                         
6F1C: 40              LD      B,B                 
6F1D: 00              NOP                         
6F1E: 9D              SBC     L                   
6F1F: 62              LD      H,D                 
6F20: 00              NOP                         
6F21: 80              ADD     A,B                 
6F22: 00              NOP                         
6F23: 9D              SBC     L                   
6F24: 60              LD      H,B                 
6F25: 26 01           LD      H,$01               
6F27: 00              NOP                         
6F28: 9D              SBC     L                   
6F29: 60              LD      H,B                 
6F2A: 26 81           LD      H,$81               
6F2C: 00              NOP                         
6F2D: 9D              SBC     L                   
6F2E: 40              LD      B,B                 
6F2F: 00              NOP                         
6F30: 80              ADD     A,B                 
6F31: 00              NOP                         
6F32: 9D              SBC     L                   
6F33: 20 00           JR      NZ,$6F35            ; {}
6F35: 80              ADD     A,B                 
6F36: 00              NOP                         
6F37: 9D              SBC     L                   
6F38: 43              LD      B,E                 
6F39: 00              NOP                         
6F3A: 80              ADD     A,B                 
6F3B: 00              NOP                         
6F3C: 9D              SBC     L                   
6F3D: 40              LD      B,B                 
6F3E: 21 80 00        LD      HL,$0080            
6F41: 9D              SBC     L                   
6F42: 50              LD      D,B                 
6F43: 00              NOP                         
6F44: 41              LD      B,C                 
6F45: 00              NOP                         
6F46: 9D              SBC     L                   
6F47: 60              LD      H,B                 
6F48: 21 41 00        LD      HL,$0041            
6F4B: 9D              SBC     L                   
6F4C: 60              LD      H,B                 
6F4D: 00              NOP                         
6F4E: 81              ADD     A,C                 
6F4F: 00              NOP                         
6F50: 9D              SBC     L                   
6F51: 90              SUB     B                   
6F52: 21 41 00        LD      HL,$0041            
6F55: 9D              SBC     L                   
6F56: B0              OR      B                   
6F57: 21 41 00        LD      HL,$0041            
6F5A: 9D              SBC     L                   
6F5B: 91              SUB     C                   
6F5C: 00              NOP                         
6F5D: 40              LD      B,B                 
6F5E: 00              NOP                         
6F5F: 9D              SBC     L                   
6F60: 50              LD      D,B                 
6F61: 26 80           LD      H,$80               
6F63: 00              NOP                         
6F64: 9D              SBC     L                   
6F65: 30 21           JR      NC,$6F88            ; {}
6F67: 80              ADD     A,B                 
6F68: 00              NOP                         
6F69: 9D              SBC     L                   
6F6A: 20 21           JR      NZ,$6F8D            ; {}
6F6C: 80              ADD     A,B                 
6F6D: 00              NOP                         
6F6E: 9D              SBC     L                   
6F6F: 60              LD      H,B                 
6F70: 26 80           LD      H,$80               
6F72: 00              NOP                         
6F73: 9D              SBC     L                   
6F74: 40              LD      B,B                 
6F75: 26 80           LD      H,$80               
6F77: 00              NOP                         
6F78: 9D              SBC     L                   
6F79: 60              LD      H,B                 
6F7A: 00              NOP                         
6F7B: 40              LD      B,B                 
6F7C: 00              NOP                         
6F7D: 9D              SBC     L                   
6F7E: A0              AND     B                   
6F7F: 21 41 00        LD      HL,$0041            
6F82: 9D              SBC     L                   
6F83: 82              ADD     A,D                 
6F84: 82              ADD     A,D                 
6F85: 80              ADD     A,B                 
6F86: 00              NOP                         
6F87: 9D              SBC     L                   
6F88: 77              LD      (HL),A              
6F89: 00              NOP                         
6F8A: 80              ADD     A,B                 
6F8B: 00              NOP                         
6F8C: 9D              SBC     L                   
6F8D: 97              SUB     A                   
6F8E: 00              NOP                         
6F8F: 80              ADD     A,B                 
6F90: 00              NOP                         
6F91: 9D              SBC     L                   
6F92: 51              LD      D,C                 
6F93: 82              ADD     A,D                 
6F94: 80              ADD     A,B                 
6F95: 00              NOP                         
6F96: 9D              SBC     L                   
6F97: 82              ADD     A,D                 
6F98: 6E              LD      L,(HL)              
6F99: 01 94 00        LD      BC,$0094            
6F9C: 9D              SBC     L                   
6F9D: 72              LD      (HL),D              
6F9E: 6E              LD      L,(HL)              
6F9F: 01 94 00        LD      BC,$0094            
6FA2: 9F              SBC     A                   
6FA3: FE 00           CP      $00                 
6FA5: 9F              SBC     A                   
6FA6: 00              NOP                         
6FA7: 00              NOP                         
6FA8: 9F              SBC     A                   
6FA9: 02              LD      (BC),A              
6FAA: 00              NOP                         
6FAB: 9F              SBC     A                   
6FAC: 0A              LD      A,(BC)              
6FAD: 00              NOP                         
6FAE: 9D              SBC     L                   
6FAF: 10 00           ;;STOP    $00                 
6FB1: 80              ADD     A,B                 
6FB2: 00              NOP                         
6FB3: 9D              SBC     L                   
6FB4: 37              SCF                         
6FB5: 00              NOP                         
6FB6: 80              ADD     A,B                 
6FB7: 00              NOP                         
6FB8: 9D              SBC     L                   
6FB9: 43              LD      B,E                 
6FBA: 83              ADD     A,E                 
6FBB: 80              ADD     A,B                 
6FBC: 00              NOP                         
6FBD: 9B              SBC     E                   
6FBE: 0B              DEC     BC                  
6FBF: A5              AND     L                   
6FC0: 01 9C A4        LD      BC,$A49C            
6FC3: 01 00 9B        LD      BC,$9B00            
6FC6: 11 A5 01        LD      DE,$01A5            
6FC9: 9C              SBC     H                   
6FCA: 00              NOP                         
6FCB: 9B              SBC     E                   
6FCC: 09              ADD     HL,BC               
6FCD: A5              AND     L                   
6FCE: 01 9C A4        LD      BC,$A49C            
6FD1: 01 00 9B        LD      BC,$9B00            
6FD4: 09              ADD     HL,BC               
6FD5: A5              AND     L                   
6FD6: 01 9C A4        LD      BC,$A49C            
6FD9: 01 00 A5        LD      BC,$A500            
6FDC: 01 01 00        LD      BC,$0001            
6FDF: A5              AND     L                   
6FE0: 01 00 A5        LD      BC,$A500            
6FE3: 01 01 00        LD      BC,$0001            
6FE6: 9B              SBC     E                   
6FE7: 03              INC     BC                  
6FE8: A5              AND     L                   
6FE9: 01 9C 00        LD      BC,$009C            
6FEC: 9B              SBC     E                   
6FED: 04              INC     B                   
6FEE: A5              AND     L                   
6FEF: 01 9C 00        LD      BC,$009C            
6FF2: 9B              SBC     E                   
6FF3: 10 A5           ;;STOP    $A5                 
6FF5: 01 9C 00        LD      BC,$009C            
6FF8: A8              XOR     B                   
6FF9: 01 00 A6        LD      BC,$A600            
6FFC: 01 00 A7        LD      BC,$A700            
6FFF: 01 00 A1        LD      BC,$A100            
7002: 01 00 A2        LD      BC,$A200            
7005: 01 00 A4        LD      BC,$A400            
7008: 01 00 A3        LD      BC,$A300            
700B: 01 00 A5        LD      BC,$A500            
700E: 01 00 DF        LD      BC,$DF00            
7011: 6F              LD      L,A                 
7012: FF              RST     0X38                
7013: FF              RST     0X38                
7014: 10 70           ;;STOP    $70                 
7016: 0D              DEC     C                   
7017: 70              LD      (HL),B              
7018: FF              RST     0X38                
7019: FF              RST     0X38                
701A: 16 70           LD      D,$70               
701C: 9E              SBC     (HL)                
701D: 3A              LD      A,(HLD)             
701E: 4A              LD      C,D                 
701F: 00              NOP                         
7020: 9E              SBC     (HL)                
7021: 49              LD      C,C                 
7022: 4A              LD      C,D                 
7023: 00              NOP                         
7024: 9E              SBC     (HL)                
7025: 67              LD      H,A                 
7026: 4A              LD      C,D                 
7027: 00              NOP                         
7028: FF              RST     0X38                
7029: FF              RST     0X38                
702A: FF              RST     0X38                
702B: FF              RST     0X38                
702C: FF              RST     0X38                
702D: FF              RST     0X38                
702E: FF              RST     0X38                
702F: FF              RST     0X38                
7030: FF              RST     0X38                
7031: FF              RST     0X38                
7032: FF              RST     0X38                
7033: FF              RST     0X38                
7034: FF              RST     0X38                
7035: FF              RST     0X38                
7036: FF              RST     0X38                
7037: FF              RST     0X38                
7038: FF              RST     0X38                
7039: FF              RST     0X38                
703A: FF              RST     0X38                
703B: FF              RST     0X38                
703C: FF              RST     0X38                
703D: FF              RST     0X38                
703E: FF              RST     0X38                
703F: FF              RST     0X38                
7040: FF              RST     0X38                
7041: FF              RST     0X38                
7042: FF              RST     0X38                
7043: FF              RST     0X38                
7044: FF              RST     0X38                
7045: FF              RST     0X38                
7046: FF              RST     0X38                
7047: FF              RST     0X38                
7048: FF              RST     0X38                
7049: FF              RST     0X38                
704A: FF              RST     0X38                
704B: FF              RST     0X38                
704C: FF              RST     0X38                
704D: FF              RST     0X38                
704E: FF              RST     0X38                
704F: FF              RST     0X38                
7050: FF              RST     0X38                
7051: FF              RST     0X38                
7052: FF              RST     0X38                
7053: FF              RST     0X38                
7054: FF              RST     0X38                
7055: FF              RST     0X38                
7056: FF              RST     0X38                
7057: FF              RST     0X38                
7058: FF              RST     0X38                
7059: FF              RST     0X38                
705A: FF              RST     0X38                
705B: FF              RST     0X38                
705C: FF              RST     0X38                
705D: FF              RST     0X38                
705E: FF              RST     0X38                
705F: FF              RST     0X38                
7060: FF              RST     0X38                
7061: FF              RST     0X38                
7062: FF              RST     0X38                
7063: FF              RST     0X38                
7064: FF              RST     0X38                
7065: FF              RST     0X38                
7066: FF              RST     0X38                
7067: FF              RST     0X38                
7068: FF              RST     0X38                
7069: FF              RST     0X38                
706A: FF              RST     0X38                
706B: FF              RST     0X38                
706C: FF              RST     0X38                
706D: FF              RST     0X38                
706E: FF              RST     0X38                
706F: FF              RST     0X38                
7070: FF              RST     0X38                
7071: FF              RST     0X38                
7072: FF              RST     0X38                
7073: FF              RST     0X38                
7074: FF              RST     0X38                
7075: FF              RST     0X38                
7076: FF              RST     0X38                
7077: FF              RST     0X38                
7078: FF              RST     0X38                
7079: FF              RST     0X38                
707A: FF              RST     0X38                
707B: FF              RST     0X38                
707C: FF              RST     0X38                
707D: FF              RST     0X38                
707E: FF              RST     0X38                
707F: FF              RST     0X38                
7080: FF              RST     0X38                
7081: FF              RST     0X38                
7082: FF              RST     0X38                
7083: FF              RST     0X38                
7084: FF              RST     0X38                
7085: FF              RST     0X38                
7086: FF              RST     0X38                
7087: FF              RST     0X38                
7088: FF              RST     0X38                
7089: FF              RST     0X38                
708A: FF              RST     0X38                
708B: FF              RST     0X38                
708C: FF              RST     0X38                
708D: FF              RST     0X38                
708E: FF              RST     0X38                
708F: FF              RST     0X38                
7090: FF              RST     0X38                
7091: FF              RST     0X38                
7092: FF              RST     0X38                
7093: FF              RST     0X38                
7094: FF              RST     0X38                
7095: FF              RST     0X38                
7096: FF              RST     0X38                
7097: FF              RST     0X38                
7098: FF              RST     0X38                
7099: FF              RST     0X38                
709A: FF              RST     0X38                
709B: FF              RST     0X38                
709C: FF              RST     0X38                
709D: FF              RST     0X38                
709E: FF              RST     0X38                
709F: FF              RST     0X38                
70A0: FF              RST     0X38                
70A1: FF              RST     0X38                
70A2: FF              RST     0X38                
70A3: FF              RST     0X38                
70A4: FF              RST     0X38                
70A5: FF              RST     0X38                
70A6: FF              RST     0X38                
70A7: FF              RST     0X38                
70A8: FF              RST     0X38                
70A9: FF              RST     0X38                
70AA: FF              RST     0X38                
70AB: FF              RST     0X38                
70AC: FF              RST     0X38                
70AD: FF              RST     0X38                
70AE: FF              RST     0X38                
70AF: FF              RST     0X38                
70B0: FF              RST     0X38                
70B1: FF              RST     0X38                
70B2: FF              RST     0X38                
70B3: FF              RST     0X38                
70B4: FF              RST     0X38                
70B5: FF              RST     0X38                
70B6: FF              RST     0X38                
70B7: FF              RST     0X38                
70B8: FF              RST     0X38                
70B9: FF              RST     0X38                
70BA: FF              RST     0X38                
70BB: FF              RST     0X38                
70BC: FF              RST     0X38                
70BD: FF              RST     0X38                
70BE: FF              RST     0X38                
70BF: FF              RST     0X38                
70C0: FF              RST     0X38                
70C1: FF              RST     0X38                
70C2: FF              RST     0X38                
70C3: FF              RST     0X38                
70C4: FF              RST     0X38                
70C5: FF              RST     0X38                
70C6: FF              RST     0X38                
70C7: FF              RST     0X38                
70C8: FF              RST     0X38                
70C9: FF              RST     0X38                
70CA: FF              RST     0X38                
70CB: FF              RST     0X38                
70CC: FF              RST     0X38                
70CD: FF              RST     0X38                
70CE: FF              RST     0X38                
70CF: FF              RST     0X38                
70D0: FF              RST     0X38                
70D1: FF              RST     0X38                
70D2: FF              RST     0X38                
70D3: FF              RST     0X38                
70D4: FF              RST     0X38                
70D5: FF              RST     0X38                
70D6: FF              RST     0X38                
70D7: FF              RST     0X38                
70D8: FF              RST     0X38                
70D9: FF              RST     0X38                
70DA: FF              RST     0X38                
70DB: FF              RST     0X38                
70DC: FF              RST     0X38                
70DD: FF              RST     0X38                
70DE: FF              RST     0X38                
70DF: FF              RST     0X38                
70E0: FF              RST     0X38                
70E1: FF              RST     0X38                
70E2: FF              RST     0X38                
70E3: FF              RST     0X38                
70E4: FF              RST     0X38                
70E5: FF              RST     0X38                
70E6: FF              RST     0X38                
70E7: FF              RST     0X38                
70E8: FF              RST     0X38                
70E9: FF              RST     0X38                
70EA: FF              RST     0X38                
70EB: FF              RST     0X38                
70EC: FF              RST     0X38                
70ED: FF              RST     0X38                
70EE: FF              RST     0X38                
70EF: FF              RST     0X38                
70F0: FF              RST     0X38                
70F1: FF              RST     0X38                
70F2: FF              RST     0X38                
70F3: FF              RST     0X38                
70F4: FF              RST     0X38                
70F5: FF              RST     0X38                
70F6: FF              RST     0X38                
70F7: FF              RST     0X38                
70F8: FF              RST     0X38                
70F9: FF              RST     0X38                
70FA: FF              RST     0X38                
70FB: FF              RST     0X38                
70FC: FF              RST     0X38                
70FD: FF              RST     0X38                
70FE: FF              RST     0X38                
70FF: FF              RST     0X38                
7100: FF              RST     0X38                
7101: FF              RST     0X38                
7102: FF              RST     0X38                
7103: FF              RST     0X38                
7104: FF              RST     0X38                
7105: FF              RST     0X38                
7106: FF              RST     0X38                
7107: FF              RST     0X38                
7108: FF              RST     0X38                
7109: FF              RST     0X38                
710A: FF              RST     0X38                
710B: FF              RST     0X38                
710C: FF              RST     0X38                
710D: FF              RST     0X38                
710E: FF              RST     0X38                
710F: FF              RST     0X38                
7110: FF              RST     0X38                
7111: FF              RST     0X38                
7112: FF              RST     0X38                
7113: FF              RST     0X38                
7114: FF              RST     0X38                
7115: FF              RST     0X38                
7116: FF              RST     0X38                
7117: FF              RST     0X38                
7118: FF              RST     0X38                
7119: FF              RST     0X38                
711A: FF              RST     0X38                
711B: FF              RST     0X38                
711C: FF              RST     0X38                
711D: FF              RST     0X38                
711E: FF              RST     0X38                
711F: FF              RST     0X38                
7120: FF              RST     0X38                
7121: FF              RST     0X38                
7122: FF              RST     0X38                
7123: FF              RST     0X38                
7124: FF              RST     0X38                
7125: FF              RST     0X38                
7126: FF              RST     0X38                
7127: FF              RST     0X38                
7128: FF              RST     0X38                
7129: FF              RST     0X38                
712A: FF              RST     0X38                
712B: FF              RST     0X38                
712C: FF              RST     0X38                
712D: FF              RST     0X38                
712E: FF              RST     0X38                
712F: FF              RST     0X38                
7130: FF              RST     0X38                
7131: FF              RST     0X38                
7132: FF              RST     0X38                
7133: FF              RST     0X38                
7134: FF              RST     0X38                
7135: FF              RST     0X38                
7136: FF              RST     0X38                
7137: FF              RST     0X38                
7138: FF              RST     0X38                
7139: FF              RST     0X38                
713A: FF              RST     0X38                
713B: FF              RST     0X38                
713C: FF              RST     0X38                
713D: FF              RST     0X38                
713E: FF              RST     0X38                
713F: FF              RST     0X38                
7140: FF              RST     0X38                
7141: FF              RST     0X38                
7142: FF              RST     0X38                
7143: FF              RST     0X38                
7144: FF              RST     0X38                
7145: FF              RST     0X38                
7146: FF              RST     0X38                
7147: FF              RST     0X38                
7148: FF              RST     0X38                
7149: FF              RST     0X38                
714A: FF              RST     0X38                
714B: FF              RST     0X38                
714C: FF              RST     0X38                
714D: FF              RST     0X38                
714E: FF              RST     0X38                
714F: FF              RST     0X38                
7150: FF              RST     0X38                
7151: FF              RST     0X38                
7152: FF              RST     0X38                
7153: FF              RST     0X38                
7154: FF              RST     0X38                
7155: FF              RST     0X38                
7156: FF              RST     0X38                
7157: FF              RST     0X38                
7158: FF              RST     0X38                
7159: FF              RST     0X38                
715A: FF              RST     0X38                
715B: FF              RST     0X38                
715C: FF              RST     0X38                
715D: FF              RST     0X38                
715E: FF              RST     0X38                
715F: FF              RST     0X38                
7160: FF              RST     0X38                
7161: FF              RST     0X38                
7162: FF              RST     0X38                
7163: FF              RST     0X38                
7164: FF              RST     0X38                
7165: FF              RST     0X38                
7166: FF              RST     0X38                
7167: FF              RST     0X38                
7168: FF              RST     0X38                
7169: FF              RST     0X38                
716A: FF              RST     0X38                
716B: FF              RST     0X38                
716C: FF              RST     0X38                
716D: FF              RST     0X38                
716E: FF              RST     0X38                
716F: FF              RST     0X38                
7170: FF              RST     0X38                
7171: FF              RST     0X38                
7172: FF              RST     0X38                
7173: FF              RST     0X38                
7174: FF              RST     0X38                
7175: FF              RST     0X38                
7176: FF              RST     0X38                
7177: FF              RST     0X38                
7178: FF              RST     0X38                
7179: FF              RST     0X38                
717A: FF              RST     0X38                
717B: FF              RST     0X38                
717C: FF              RST     0X38                
717D: FF              RST     0X38                
717E: FF              RST     0X38                
717F: FF              RST     0X38                
7180: FF              RST     0X38                
7181: FF              RST     0X38                
7182: FF              RST     0X38                
7183: FF              RST     0X38                
7184: FF              RST     0X38                
7185: FF              RST     0X38                
7186: FF              RST     0X38                
7187: FF              RST     0X38                
7188: FF              RST     0X38                
7189: FF              RST     0X38                
718A: FF              RST     0X38                
718B: FF              RST     0X38                
718C: FF              RST     0X38                
718D: FF              RST     0X38                
718E: FF              RST     0X38                
718F: FF              RST     0X38                
7190: FF              RST     0X38                
7191: FF              RST     0X38                
7192: FF              RST     0X38                
7193: FF              RST     0X38                
7194: FF              RST     0X38                
7195: FF              RST     0X38                
7196: FF              RST     0X38                
7197: FF              RST     0X38                
7198: FF              RST     0X38                
7199: FF              RST     0X38                
719A: FF              RST     0X38                
719B: FF              RST     0X38                
719C: FF              RST     0X38                
719D: FF              RST     0X38                
719E: FF              RST     0X38                
719F: FF              RST     0X38                
71A0: FF              RST     0X38                
71A1: FF              RST     0X38                
71A2: FF              RST     0X38                
71A3: FF              RST     0X38                
71A4: FF              RST     0X38                
71A5: FF              RST     0X38                
71A6: FF              RST     0X38                
71A7: FF              RST     0X38                
71A8: FF              RST     0X38                
71A9: FF              RST     0X38                
71AA: FF              RST     0X38                
71AB: FF              RST     0X38                
71AC: FF              RST     0X38                
71AD: FF              RST     0X38                
71AE: FF              RST     0X38                
71AF: FF              RST     0X38                
71B0: FF              RST     0X38                
71B1: FF              RST     0X38                
71B2: FF              RST     0X38                
71B3: FF              RST     0X38                
71B4: FF              RST     0X38                
71B5: FF              RST     0X38                
71B6: FF              RST     0X38                
71B7: FF              RST     0X38                
71B8: FF              RST     0X38                
71B9: FF              RST     0X38                
71BA: FF              RST     0X38                
71BB: FF              RST     0X38                
71BC: FF              RST     0X38                
71BD: FF              RST     0X38                
71BE: FF              RST     0X38                
71BF: FF              RST     0X38                
71C0: FF              RST     0X38                
71C1: FF              RST     0X38                
71C2: FF              RST     0X38                
71C3: FF              RST     0X38                
71C4: FF              RST     0X38                
71C5: FF              RST     0X38                
71C6: FF              RST     0X38                
71C7: FF              RST     0X38                
71C8: FF              RST     0X38                
71C9: FF              RST     0X38                
71CA: FF              RST     0X38                
71CB: FF              RST     0X38                
71CC: FF              RST     0X38                
71CD: FF              RST     0X38                
71CE: FF              RST     0X38                
71CF: FF              RST     0X38                
71D0: FF              RST     0X38                
71D1: FF              RST     0X38                
71D2: FF              RST     0X38                
71D3: FF              RST     0X38                
71D4: FF              RST     0X38                
71D5: FF              RST     0X38                
71D6: FF              RST     0X38                
71D7: FF              RST     0X38                
71D8: FF              RST     0X38                
71D9: FF              RST     0X38                
71DA: FF              RST     0X38                
71DB: FF              RST     0X38                
71DC: FF              RST     0X38                
71DD: FF              RST     0X38                
71DE: FF              RST     0X38                
71DF: FF              RST     0X38                
71E0: FF              RST     0X38                
71E1: FF              RST     0X38                
71E2: FF              RST     0X38                
71E3: FF              RST     0X38                
71E4: FF              RST     0X38                
71E5: FF              RST     0X38                
71E6: FF              RST     0X38                
71E7: FF              RST     0X38                
71E8: FF              RST     0X38                
71E9: FF              RST     0X38                
71EA: FF              RST     0X38                
71EB: FF              RST     0X38                
71EC: FF              RST     0X38                
71ED: FF              RST     0X38                
71EE: FF              RST     0X38                
71EF: FF              RST     0X38                
71F0: FF              RST     0X38                
71F1: FF              RST     0X38                
71F2: FF              RST     0X38                
71F3: FF              RST     0X38                
71F4: FF              RST     0X38                
71F5: FF              RST     0X38                
71F6: FF              RST     0X38                
71F7: FF              RST     0X38                
71F8: FF              RST     0X38                
71F9: FF              RST     0X38                
71FA: FF              RST     0X38                
71FB: FF              RST     0X38                
71FC: FF              RST     0X38                
71FD: FF              RST     0X38                
71FE: FF              RST     0X38                
71FF: FF              RST     0X38                
7200: FF              RST     0X38                
7201: FF              RST     0X38                
7202: FF              RST     0X38                
7203: FF              RST     0X38                
7204: FF              RST     0X38                
7205: FF              RST     0X38                
7206: FF              RST     0X38                
7207: FF              RST     0X38                
7208: FF              RST     0X38                
7209: FF              RST     0X38                
720A: FF              RST     0X38                
720B: FF              RST     0X38                
720C: FF              RST     0X38                
720D: FF              RST     0X38                
720E: FF              RST     0X38                
720F: FF              RST     0X38                
7210: FF              RST     0X38                
7211: FF              RST     0X38                
7212: FF              RST     0X38                
7213: FF              RST     0X38                
7214: FF              RST     0X38                
7215: FF              RST     0X38                
7216: FF              RST     0X38                
7217: FF              RST     0X38                
7218: FF              RST     0X38                
7219: FF              RST     0X38                
721A: FF              RST     0X38                
721B: FF              RST     0X38                
721C: FF              RST     0X38                
721D: FF              RST     0X38                
721E: FF              RST     0X38                
721F: FF              RST     0X38                
7220: FF              RST     0X38                
7221: FF              RST     0X38                
7222: FF              RST     0X38                
7223: FF              RST     0X38                
7224: FF              RST     0X38                
7225: FF              RST     0X38                
7226: FF              RST     0X38                
7227: FF              RST     0X38                
7228: FF              RST     0X38                
7229: FF              RST     0X38                
722A: FF              RST     0X38                
722B: FF              RST     0X38                
722C: FF              RST     0X38                
722D: FF              RST     0X38                
722E: FF              RST     0X38                
722F: FF              RST     0X38                
7230: FF              RST     0X38                
7231: FF              RST     0X38                
7232: FF              RST     0X38                
7233: FF              RST     0X38                
7234: FF              RST     0X38                
7235: FF              RST     0X38                
7236: FF              RST     0X38                
7237: FF              RST     0X38                
7238: FF              RST     0X38                
7239: FF              RST     0X38                
723A: FF              RST     0X38                
723B: FF              RST     0X38                
723C: FF              RST     0X38                
723D: FF              RST     0X38                
723E: FF              RST     0X38                
723F: FF              RST     0X38                
7240: FF              RST     0X38                
7241: FF              RST     0X38                
7242: FF              RST     0X38                
7243: FF              RST     0X38                
7244: FF              RST     0X38                
7245: FF              RST     0X38                
7246: FF              RST     0X38                
7247: FF              RST     0X38                
7248: FF              RST     0X38                
7249: FF              RST     0X38                
724A: FF              RST     0X38                
724B: FF              RST     0X38                
724C: FF              RST     0X38                
724D: FF              RST     0X38                
724E: FF              RST     0X38                
724F: FF              RST     0X38                
7250: FF              RST     0X38                
7251: FF              RST     0X38                
7252: FF              RST     0X38                
7253: FF              RST     0X38                
7254: FF              RST     0X38                
7255: FF              RST     0X38                
7256: FF              RST     0X38                
7257: FF              RST     0X38                
7258: FF              RST     0X38                
7259: FF              RST     0X38                
725A: FF              RST     0X38                
725B: FF              RST     0X38                
725C: FF              RST     0X38                
725D: FF              RST     0X38                
725E: FF              RST     0X38                
725F: FF              RST     0X38                
7260: FF              RST     0X38                
7261: FF              RST     0X38                
7262: FF              RST     0X38                
7263: FF              RST     0X38                
7264: FF              RST     0X38                
7265: FF              RST     0X38                
7266: FF              RST     0X38                
7267: FF              RST     0X38                
7268: FF              RST     0X38                
7269: FF              RST     0X38                
726A: FF              RST     0X38                
726B: FF              RST     0X38                
726C: FF              RST     0X38                
726D: FF              RST     0X38                
726E: FF              RST     0X38                
726F: FF              RST     0X38                
7270: FF              RST     0X38                
7271: FF              RST     0X38                
7272: FF              RST     0X38                
7273: FF              RST     0X38                
7274: FF              RST     0X38                
7275: FF              RST     0X38                
7276: FF              RST     0X38                
7277: FF              RST     0X38                
7278: FF              RST     0X38                
7279: FF              RST     0X38                
727A: FF              RST     0X38                
727B: FF              RST     0X38                
727C: FF              RST     0X38                
727D: FF              RST     0X38                
727E: FF              RST     0X38                
727F: FF              RST     0X38                
7280: FF              RST     0X38                
7281: FF              RST     0X38                
7282: FF              RST     0X38                
7283: FF              RST     0X38                
7284: FF              RST     0X38                
7285: FF              RST     0X38                
7286: FF              RST     0X38                
7287: FF              RST     0X38                
7288: FF              RST     0X38                
7289: FF              RST     0X38                
728A: FF              RST     0X38                
728B: FF              RST     0X38                
728C: FF              RST     0X38                
728D: FF              RST     0X38                
728E: FF              RST     0X38                
728F: FF              RST     0X38                
7290: FF              RST     0X38                
7291: FF              RST     0X38                
7292: FF              RST     0X38                
7293: FF              RST     0X38                
7294: FF              RST     0X38                
7295: FF              RST     0X38                
7296: FF              RST     0X38                
7297: FF              RST     0X38                
7298: FF              RST     0X38                
7299: FF              RST     0X38                
729A: FF              RST     0X38                
729B: FF              RST     0X38                
729C: FF              RST     0X38                
729D: FF              RST     0X38                
729E: FF              RST     0X38                
729F: FF              RST     0X38                
72A0: FF              RST     0X38                
72A1: FF              RST     0X38                
72A2: FF              RST     0X38                
72A3: FF              RST     0X38                
72A4: FF              RST     0X38                
72A5: FF              RST     0X38                
72A6: FF              RST     0X38                
72A7: FF              RST     0X38                
72A8: FF              RST     0X38                
72A9: FF              RST     0X38                
72AA: FF              RST     0X38                
72AB: FF              RST     0X38                
72AC: FF              RST     0X38                
72AD: FF              RST     0X38                
72AE: FF              RST     0X38                
72AF: FF              RST     0X38                
72B0: FF              RST     0X38                
72B1: FF              RST     0X38                
72B2: FF              RST     0X38                
72B3: FF              RST     0X38                
72B4: FF              RST     0X38                
72B5: FF              RST     0X38                
72B6: FF              RST     0X38                
72B7: FF              RST     0X38                
72B8: FF              RST     0X38                
72B9: FF              RST     0X38                
72BA: FF              RST     0X38                
72BB: FF              RST     0X38                
72BC: FF              RST     0X38                
72BD: FF              RST     0X38                
72BE: FF              RST     0X38                
72BF: FF              RST     0X38                
72C0: FF              RST     0X38                
72C1: FF              RST     0X38                
72C2: FF              RST     0X38                
72C3: FF              RST     0X38                
72C4: FF              RST     0X38                
72C5: FF              RST     0X38                
72C6: FF              RST     0X38                
72C7: FF              RST     0X38                
72C8: FF              RST     0X38                
72C9: FF              RST     0X38                
72CA: FF              RST     0X38                
72CB: FF              RST     0X38                
72CC: FF              RST     0X38                
72CD: FF              RST     0X38                
72CE: FF              RST     0X38                
72CF: FF              RST     0X38                
72D0: FF              RST     0X38                
72D1: FF              RST     0X38                
72D2: FF              RST     0X38                
72D3: FF              RST     0X38                
72D4: FF              RST     0X38                
72D5: FF              RST     0X38                
72D6: FF              RST     0X38                
72D7: FF              RST     0X38                
72D8: FF              RST     0X38                
72D9: FF              RST     0X38                
72DA: FF              RST     0X38                
72DB: FF              RST     0X38                
72DC: FF              RST     0X38                
72DD: FF              RST     0X38                
72DE: FF              RST     0X38                
72DF: FF              RST     0X38                
72E0: FF              RST     0X38                
72E1: FF              RST     0X38                
72E2: FF              RST     0X38                
72E3: FF              RST     0X38                
72E4: FF              RST     0X38                
72E5: FF              RST     0X38                
72E6: FF              RST     0X38                
72E7: FF              RST     0X38                
72E8: FF              RST     0X38                
72E9: FF              RST     0X38                
72EA: FF              RST     0X38                
72EB: FF              RST     0X38                
72EC: FF              RST     0X38                
72ED: FF              RST     0X38                
72EE: FF              RST     0X38                
72EF: FF              RST     0X38                
72F0: FF              RST     0X38                
72F1: FF              RST     0X38                
72F2: FF              RST     0X38                
72F3: FF              RST     0X38                
72F4: FF              RST     0X38                
72F5: FF              RST     0X38                
72F6: FF              RST     0X38                
72F7: FF              RST     0X38                
72F8: FF              RST     0X38                
72F9: FF              RST     0X38                
72FA: FF              RST     0X38                
72FB: FF              RST     0X38                
72FC: FF              RST     0X38                
72FD: FF              RST     0X38                
72FE: FF              RST     0X38                
72FF: FF              RST     0X38                
7300: FF              RST     0X38                
7301: FF              RST     0X38                
7302: FF              RST     0X38                
7303: FF              RST     0X38                
7304: FF              RST     0X38                
7305: FF              RST     0X38                
7306: FF              RST     0X38                
7307: FF              RST     0X38                
7308: FF              RST     0X38                
7309: FF              RST     0X38                
730A: FF              RST     0X38                
730B: FF              RST     0X38                
730C: FF              RST     0X38                
730D: FF              RST     0X38                
730E: FF              RST     0X38                
730F: FF              RST     0X38                
7310: FF              RST     0X38                
7311: FF              RST     0X38                
7312: FF              RST     0X38                
7313: FF              RST     0X38                
7314: FF              RST     0X38                
7315: FF              RST     0X38                
7316: FF              RST     0X38                
7317: FF              RST     0X38                
7318: FF              RST     0X38                
7319: FF              RST     0X38                
731A: FF              RST     0X38                
731B: FF              RST     0X38                
731C: FF              RST     0X38                
731D: FF              RST     0X38                
731E: FF              RST     0X38                
731F: FF              RST     0X38                
7320: FF              RST     0X38                
7321: FF              RST     0X38                
7322: FF              RST     0X38                
7323: FF              RST     0X38                
7324: FF              RST     0X38                
7325: FF              RST     0X38                
7326: FF              RST     0X38                
7327: FF              RST     0X38                
7328: FF              RST     0X38                
7329: FF              RST     0X38                
732A: FF              RST     0X38                
732B: FF              RST     0X38                
732C: FF              RST     0X38                
732D: FF              RST     0X38                
732E: FF              RST     0X38                
732F: FF              RST     0X38                
7330: FF              RST     0X38                
7331: FF              RST     0X38                
7332: FF              RST     0X38                
7333: FF              RST     0X38                
7334: FF              RST     0X38                
7335: FF              RST     0X38                
7336: FF              RST     0X38                
7337: FF              RST     0X38                
7338: FF              RST     0X38                
7339: FF              RST     0X38                
733A: FF              RST     0X38                
733B: FF              RST     0X38                
733C: FF              RST     0X38                
733D: FF              RST     0X38                
733E: FF              RST     0X38                
733F: FF              RST     0X38                
7340: FF              RST     0X38                
7341: FF              RST     0X38                
7342: FF              RST     0X38                
7343: FF              RST     0X38                
7344: FF              RST     0X38                
7345: FF              RST     0X38                
7346: FF              RST     0X38                
7347: FF              RST     0X38                
7348: FF              RST     0X38                
7349: FF              RST     0X38                
734A: FF              RST     0X38                
734B: FF              RST     0X38                
734C: FF              RST     0X38                
734D: FF              RST     0X38                
734E: FF              RST     0X38                
734F: FF              RST     0X38                
7350: FF              RST     0X38                
7351: FF              RST     0X38                
7352: FF              RST     0X38                
7353: FF              RST     0X38                
7354: FF              RST     0X38                
7355: FF              RST     0X38                
7356: FF              RST     0X38                
7357: FF              RST     0X38                
7358: FF              RST     0X38                
7359: FF              RST     0X38                
735A: FF              RST     0X38                
735B: FF              RST     0X38                
735C: FF              RST     0X38                
735D: FF              RST     0X38                
735E: FF              RST     0X38                
735F: FF              RST     0X38                
7360: FF              RST     0X38                
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

