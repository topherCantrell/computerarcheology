![Bank 0A](GBZelda.jpg)

# Bank 0A

>>> cpu Z80GB

>>> binary 4000:roms/zelda.gb[28000:2C000]

>>> memoryTable ram 
[RAM Usage](RAMUse.md)

>>> memoryTable hard 
[Hardware Info](../Hardware.md)

```code
4000: 00         NOP
4001: 42         LD           B,D
4002: 03         INC         BC
4003: 42         LD           B,D
4004: 42         LD           B,D
4005: 42         LD           B,D
4006: 87         ADD         A,A
4007: 42         LD           B,D
4008: B3         OR           E
4009: 42         LD           B,D
400A: E8 42      ADD         SP,$42
400C: 1A         LD           A,(DE)
400D: 43         LD           B,E
400E: 38 43      JR           C,$4053
4010: 8B         ADC         A,E
4011: 43         LD           B,E
4012: E2         LDFF00   (C),A
4013: 43         LD           B,E
4014: 1F         RRA
4015: 44         LD           B,H
4016: 4F         LD           C,A
4017: 44         LD           B,H
4018: 68         LD           L,B
4019: 44         LD           B,H
401A: A4         AND         H
401B: 44         LD           B,H
401C: D7         RST         0X10
401D: 44         LD           B,H
401E: 0E 45      LD           C,$45
4020: 2E 45      LD           L,$45
4022: 59         LD           E,C
4023: 45         LD           B,L
4024: 68         LD           L,B
4025: 45         LD           B,L
4026: AE         XOR         (HL)
4027: 45         LD           B,L
4028: DC 45 0C   CALL       C,$0C45
402B: 46         LD           B,(HL)
402C: 4A         LD           C,D
402D: 46         LD           B,(HL)
402E: 8C         ADC         A,H
402F: 46         LD           B,(HL)
4030: C7         RST         0X00
4031: 46         LD           B,(HL)
4032: FC                              
4033: 46         LD           B,(HL)
4034: 35         DEC         (HL)
4035: 47         LD           B,A
4036: 6D         LD           L,L
4037: 47         LD           B,A
4038: 99         SBC         C
4039: 47         LD           B,A
403A: A9         XOR         C
403B: 47         LD           B,A
403C: DA 47 10   JP           C,$1047
403F: 48         LD           C,B
4040: 3D         DEC         A
4041: 48         LD           C,B
4042: 78         LD           A,B
4043: 48         LD           C,B
4044: CD 48 18   CALL       $1848
4047: 49         LD           C,C
4048: 5E         LD           E,(HL)
4049: 49         LD           C,C
404A: 92         SUB         D
404B: 49         LD           C,C
404C: BB         CP           E
404D: 49         LD           C,C
404E: FD                              
404F: 49         LD           C,C
4050: 29         ADD         HL,HL
4051: 4A         LD           C,D
4052: 57         LD           D,A
4053: 4A         LD           C,D
4054: 8D         ADC         A,L
4055: 4A         LD           C,D
4056: CC 4A F1   CALL       Z,$F14A
4059: 4A         LD           C,D
405A: 3C         INC         A
405B: 4B         LD           C,E
405C: 86         ADD         A,(HL)
405D: 4B         LD           C,E
405E: C6 4B      ADD         $4B
4060: F3         DI
4061: 4B         LD           C,E
4062: FE 4B      CP           $4B
4064: 55         LD           D,L
4065: 4C         LD           C,H
4066: AE         XOR         (HL)
4067: 4C         LD           C,H
4068: F5         PUSH       AF
4069: 4C         LD           C,H
406A: 44         LD           B,H
406B: 4D         LD           C,L
406C: 7C         LD           A,H
406D: 4D         LD           C,L
406E: D1         POP         DE
406F: 4D         LD           C,L
4070: 05         DEC         B
4071: 4E         LD           C,(HL)
4072: 49         LD           C,C
4073: 4E         LD           C,(HL)
4074: A0         AND         B
4075: 4E         LD           C,(HL)
4076: DD                              
4077: 4E         LD           C,(HL)
4078: 12         LD           (DE),A
4079: 4F         LD           C,A
407A: 56         LD           D,(HL)
407B: 4F         LD           C,A
407C: 9D         SBC         L
407D: 4F         LD           C,A
407E: DB                              
407F: 4F         LD           C,A
4080: 0F         RRCA
4081: 50         LD           D,B
4082: 59         LD           E,C
4083: 50         LD           D,B
4084: 7C         LD           A,H
4085: 50         LD           D,B
4086: 9F         SBC         A
4087: 50         LD           D,B
4088: D9         RETI
4089: 50         LD           D,B
408A: 07         RLCA
408B: 51         LD           D,C
408C: 42         LD           B,D
408D: 51         LD           D,C
408E: 96         SUB         (HL)
408F: 51         LD           D,C
4090: C9         RET
4091: 51         LD           D,C
4092: 04         INC         B
4093: 52         LD           D,D
4094: 52         LD           D,D
4095: 52         LD           D,D
4096: A2         AND         D
4097: 52         LD           D,D
4098: D8         RET         C
4099: 52         LD           D,D
409A: 39         ADD         HL,SP
409B: 53         LD           D,E
409C: 7A         LD           A,D
409D: 53         LD           D,E
409E: A5         AND         L
409F: 53         LD           D,E
40A0: CB 53      BIT         1,E
40A2: F9         LD           SP,HL
40A3: 53         LD           D,E
40A4: 33         INC         SP
40A5: 54         LD           D,H
40A6: 83         ADD         A,E
40A7: 54         LD           D,H
40A8: A6         AND         (HL)
40A9: 54         LD           D,H
40AA: E2         LDFF00   (C),A
40AB: 54         LD           D,H
40AC: 1B         DEC         DE
40AD: 55         LD           D,L
40AE: 63         LD           H,E
40AF: 55         LD           D,L
40B0: A1         AND         C
40B1: 55         LD           D,L
40B2: 00         NOP
40B3: 56         LD           D,(HL)
40B4: 46         LD           B,(HL)
40B5: 56         LD           D,(HL)
40B6: 59         LD           E,C
40B7: 56         LD           D,(HL)
40B8: B5         OR           L
40B9: 56         LD           D,(HL)
40BA: E2         LDFF00   (C),A
40BB: 56         LD           D,(HL)
40BC: E5         PUSH       HL
40BD: 56         LD           D,(HL)
40BE: 17         RLA
40BF: 57         LD           D,A
40C0: 4A         LD           C,D
40C1: 57         LD           D,A
40C2: 92         SUB         D
40C3: 57         LD           D,A
40C4: AE         XOR         (HL)
40C5: 57         LD           D,A
40C6: F3         DI
40C7: 57         LD           D,A
40C8: 25         DEC         H
40C9: 58         LD           E,B
40CA: 4C         LD           C,H
40CB: 58         LD           E,B
40CC: 75         LD           (HL),L
40CD: 58         LD           E,B
40CE: C8         RET         Z
40CF: 58         LD           E,B
40D0: 06 59      LD           B,$59
40D2: 4B         LD           C,E
40D3: 59         LD           E,C
40D4: 95         SUB         L
40D5: 59         LD           E,C
40D6: D9         RETI
40D7: 59         LD           E,C
40D8: 14         INC         D
40D9: 5A         LD           E,D
40DA: 4B         LD           C,E
40DB: 5A         LD           E,D
40DC: A4         AND         H
40DD: 5A         LD           E,D
40DE: FB         EI
40DF: 5A         LD           E,D
40E0: 44         LD           B,H
40E1: 5B         LD           E,E
40E2: 91         SUB         C
40E3: 5B         LD           E,E
40E4: CE 5B      ADC         $5B
40E6: 3D         DEC         A
40E7: 5C         LD           E,H
40E8: 8B         ADC         A,E
40E9: 5C         LD           E,H
40EA: C4 5C 0F   CALL       NZ,$0F5C
40ED: 5D         LD           E,L
40EE: 63         LD           H,E
40EF: 5D         LD           E,L
40F0: AC         XOR         H
40F1: 5D         LD           E,L
40F2: E2         LDFF00   (C),A
40F3: 5D         LD           E,L
40F4: 2D         DEC         L
40F5: 5E         LD           E,(HL)
40F6: 68         LD           L,B
40F7: 5E         LD           E,(HL)
40F8: A2         AND         D
40F9: 5E         LD           E,(HL)
40FA: DE 5E      SBC         $5E
40FC: 12         LD           (DE),A
40FD: 5F         LD           E,A
40FE: 12         LD           (DE),A
40FF: 5F         LD           E,A
4100: 15         DEC         D
4101: 5F         LD           E,A
4102: 33         INC         SP
4103: 5F         LD           E,A
4104: 57         LD           D,A
4105: 5F         LD           E,A
4106: 90         SUB         B
4107: 5F         LD           E,A
4108: CB 5F      BIT         1,E
410A: E9         JP           (HL)
410B: 5F         LD           E,A
410C: FC                              
410D: 5F         LD           E,A
410E: 39         ADD         HL,SP
410F: 60         LD           H,B
4110: 6A         LD           L,D
4111: 60         LD           H,B
4112: A5         AND         L
4113: 60         LD           H,B
4114: C3 60 E7   JP           $E760
4117: 60         LD           H,B
4118: 12         LD           (DE),A
4119: 61         LD           H,C
411A: 47         LD           B,A
411B: 61         LD           H,C
411C: 82         ADD         A,D
411D: 61         LD           H,C
411E: CE 61      ADC         $61
4120: 03         INC         BC
4121: 62         LD           H,D
4122: 29         ADD         HL,HL
4123: 62         LD           H,D
4124: 7E         LD           A,(HL)
4125: 62         LD           H,D
4126: 98         SBC         B
4127: 62         LD           H,D
4128: B6         OR           (HL)
4129: 62         LD           H,D
412A: F3         DI
412B: 62         LD           H,D
412C: 0D         DEC         C
412D: 63         LD           H,E
412E: 66         LD           H,(HL)
412F: 63         LD           H,E
4130: 8B         ADC         A,E
4131: 63         LD           H,E
4132: D2 63 0C   JP           NC,$0C63
4135: 64         LD           H,H
4136: 3D         DEC         A
4137: 64         LD           H,H
4138: 56         LD           D,(HL)
4139: 64         LD           H,H
413A: 6E         LD           L,(HL)
413B: 64         LD           H,H
413C: A6         AND         (HL)
413D: 64         LD           H,H
413E: DC 64 0C   CALL       C,$0C64
4141: 65         LD           H,L
4142: 3D         DEC         A
4143: 65         LD           H,L
4144: 6B         LD           L,E
4145: 65         LD           H,L
4146: B2         OR           D
4147: 65         LD           H,L
4148: FF         RST         0X38
4149: 65         LD           H,L
414A: 39         ADD         HL,SP
414B: 66         LD           H,(HL)
414C: 73         LD           (HL),E
414D: 66         LD           H,(HL)
414E: B7         OR           A
414F: 66         LD           H,(HL)
4150: F7         RST         0X30
4151: 66         LD           H,(HL)
4152: 20 67      JR           NZ,$41BB
4154: 4E         LD           C,(HL)
4155: 67         LD           H,A
4156: 8E         ADC         A,(HL)
4157: 67         LD           H,A
4158: CF         RST         0X08
4159: 67         LD           H,A
415A: 1F         RRA
415B: 68         LD           L,B
415C: 22         LD           (HLI),A
415D: 68         LD           L,B
415E: 25         DEC         H
415F: 68         LD           L,B
4160: 28 68      JR           Z,$41CA
4162: 5D         LD           E,L
4163: 68         LD           L,B
4164: 8D         ADC         A,L
4165: 68         LD           L,B
4166: C9         RET
4167: 68         LD           L,B
4168: 0D         DEC         C
4169: 69         LD           L,C
416A: 3D         DEC         A
416B: 69         LD           L,C
416C: 8B         ADC         A,E
416D: 69         LD           L,C
416E: C5         PUSH       BC
416F: 69         LD           L,C
4170: F8 69      LDHL       SP,$69
4172: 29         ADD         HL,HL
4173: 6A         LD           L,D
4174: 7C         LD           A,H
4175: 6A         LD           L,D
4176: AF         XOR         A
4177: 6A         LD           L,D
4178: F3         DI
4179: 6A         LD           L,D
417A: 12         LD           (DE),A
417B: 6B         LD           L,E
417C: 33         INC         SP
417D: 6B         LD           L,E
417E: 8F         ADC         A,A
417F: 6B         LD           L,E
4180: C5         PUSH       BC
4181: 6B         LD           L,E
4182: E7         RST         0X20
4183: 6B         LD           L,E
4184: 35         DEC         (HL)
4185: 6C         LD           L,H
4186: 54         LD           D,H
4187: 6C         LD           L,H
4188: 8E         ADC         A,(HL)
4189: 6C         LD           L,H
418A: A9         XOR         C
418B: 6C         LD           L,H
418C: CC 6C 2C   CALL       Z,$2C6C
418F: 6D         LD           L,L
4190: 53         LD           D,E
4191: 6D         LD           L,L
4192: 8D         ADC         A,L
4193: 6D         LD           L,L
4194: D4 6D 0C   CALL       NC,$0C6D
4197: 6E         LD           L,(HL)
4198: 2D         DEC         L
4199: 6E         LD           L,(HL)
419A: 44         LD           B,H
419B: 6E         LD           L,(HL)
419C: 81         ADD         A,C
419D: 6E         LD           L,(HL)
419E: C6 6E      ADD         $6E
41A0: FA 6E 1D   LD           A,($1D6E)
41A3: 6F         LD           L,A
41A4: 51         LD           D,C
41A5: 6F         LD           L,A
41A6: 76         HALT
41A7: 6F         LD           L,A
41A8: A1         AND         C
41A9: 6F         LD           L,A
41AA: CD 6F 35   CALL       $356F
41AD: 70         LD           (HL),B
41AE: 61         LD           H,C
41AF: 70         LD           (HL),B
41B0: AA         XOR         D
41B1: 70         LD           (HL),B
41B2: E2         LDFF00   (C),A
41B3: 70         LD           (HL),B
41B4: 25         DEC         H
41B5: 71         LD           (HL),C
41B6: 61         LD           H,C
41B7: 71         LD           (HL),C
41B8: 99         SBC         C
41B9: 71         LD           (HL),C
41BA: D1         POP         DE
41BB: 71         LD           (HL),C
41BC: 0D         DEC         C
41BD: 72         LD           (HL),D
41BE: 10 72      STOP       $72
41C0: 13         INC         DE
41C1: 72         LD           (HL),D
41C2: 6C         LD           L,H
41C3: 72         LD           (HL),D
41C4: BF         CP           A
41C5: 72         LD           (HL),D
41C6: 12         LD           (DE),A
41C7: 73         LD           (HL),E
41C8: 44         LD           B,H
41C9: 73         LD           (HL),E
41CA: 94         SUB         H
41CB: 73         LD           (HL),E
41CC: FF         RST         0X38
41CD: 73         LD           (HL),E
41CE: 53         LD           D,E
41CF: 74         LD           (HL),H
41D0: B7         OR           A
41D1: 74         LD           (HL),H
41D2: E9         JP           (HL)
41D3: 74         LD           (HL),H
41D4: 36 75      LD           (HL),$75
41D6: 82         ADD         A,D
41D7: 75         LD           (HL),L
41D8: C4 75 22   CALL       NZ,$2275
41DB: 76         HALT
41DC: 22         LD           (HLI),A
41DD: 76         HALT
41DE: 6D         LD           L,L
41DF: 76         HALT
41E0: B2         OR           D
41E1: 76         HALT
41E2: 0A         LD           A,(BC)
41E3: 77         LD           (HL),A
41E4: 51         LD           D,C
41E5: 77         LD           (HL),A
41E6: 7F         LD           A,A
41E7: 77         LD           (HL),A
41E8: CF         RST         0X08
41E9: 77         LD           (HL),A
41EA: 19         ADD         HL,DE
41EB: 78         LD           A,B
41EC: 95         SUB         L
41ED: 78         LD           A,B
41EE: 0C         INC         C
41EF: 79         LD           A,C
41F0: 86         ADD         A,(HL)
41F1: 79         LD           A,C
41F2: C4 79 01   CALL       NZ,$0179
41F5: 7A         LD           A,D
41F6: 21 7A 71   LD           HL,$717A
41F9: 7A         LD           A,D
41FA: 96         SUB         (HL)
41FB: 7A         LD           A,D
41FC: EB                              
41FD: 7A         LD           A,D
41FE: 35         DEC         (HL)
41FF: 7B         LD           A,E
4200: 00         NOP
4201: 0D         DEC         C
4202: FE 04      CP           $04
4204: 93         SUB         E
4205: 03         INC         BC
4206: F4                              
4207: C4 04 0D   CALL       NZ,$0D04
420A: 85         ADD         A,L
420B: 43         LD           B,E
420C: 0D         DEC         C
420D: 86         ADD         A,(HL)
420E: 52         LD           D,D
420F: 0D         DEC         C
4210: 85         ADD         A,L
4211: 63         LD           H,E
4212: 0D         DEC         C
4213: C3 03 23   JP           $2303
4216: 31 25 32   LD           SP,$3225
4219: 21 33 29   LD           HL,$2933
421C: C3 41 23   JP           $2341
421F: 71         LD           (HL),C
4220: 27         DAA
4221: 86         ADD         A,(HL)
4222: 72         LD           (HL),D
4223: 22         LD           (HLI),A
4224: 77         LD           (HL),A
4225: 28 C3      JR           Z,$41EA
4227: 47         LD           B,A
4228: 24         INC         H
4229: 37         SCF
422A: 26 35      LD           H,$35
422C: 2A         LD           A,(HLI)
422D: 36 21      LD           (HL),$21
422F: C3 05 24   JP           $2405
4232: 42         LD           B,D
4233: AC         XOR         H
4234: 46         LD           B,(HL)
4235: AC         XOR         H
4236: 62         LD           H,D
4237: AC         XOR         H
4238: 66         LD           H,(HL)
4239: AC         XOR         H
423A: 54         LD           D,H
423B: BE         CP           (HL)
423C: E2         LDFF00   (C),A
423D: 00         NOP
423E: 18 28      JR           $4268
4240: 10 FE      STOP       $FE
4242: 04         INC         B
4243: 0D         DEC         C
4244: 74         LD           (HL),H
4245: F1         POP         AF
4246: 84         ADD         A,H
4247: 13         INC         DE
4248: 0F         RRCA
4249: 84         ADD         A,H
424A: 23         INC         HL
424B: 0F         RRCA
424C: 84         ADD         A,H
424D: 33         INC         SP
424E: 0F         RRCA
424F: 82         ADD         A,D
4250: 54         LD           D,H
4251: 0F         RRCA
4252: 82         ADD         A,D
4253: 64         LD           H,H
4254: 0F         RRCA
4255: 02         LD           (BC),A
4256: 26 03      LD           H,$03
4258: 2A         LD           A,(HLI)
4259: 06 29      LD           B,$29
425B: 07         RLCA
425C: 25         DEC         H
425D: C3 12 24   JP           $2412
4260: 42         LD           B,D
4261: 2A         LD           A,(HLI)
4262: 84         ADD         A,H
4263: 43         LD           B,E
4264: 21 82 44   LD           HL,$4482
4267: 97         SUB         A
4268: 47         LD           B,A
4269: 29         ADD         HL,HL
426A: C3 17 23   JP           $2317
426D: 13         INC         DE
426E: C0         RET         NZ
426F: 16 C0      LD           D,$C0
4271: 33         INC         SP
4272: C0         RET         NZ
4273: 36 C0      LD           (HL),$C0
4275: 11 AC 18   LD           DE,$18AC
4278: AC         XOR         H
4279: 61         LD           H,C
427A: AC         XOR         H
427B: 68         LD           L,B
427C: AC         XOR         H
427D: 73         LD           (HL),E
427E: C8         RET         Z
427F: 76         HALT
4280: C8         RET         Z
4281: E0 00      LDFF00   ($00),A
4283: D3                              
4284: 68         LD           L,B
4285: 22         LD           (HLI),A
4286: FE 04      CP           $04
4288: 0D         DEC         C
4289: 29         ADD         HL,HL
428A: F7         RST         0X30
428B: 13         INC         DE
428C: AE         XOR         (HL)
428D: 16 AE      LD           D,$AE
428F: 22         LD           (HLI),A
4290: AE         XOR         (HL)
4291: 27         DAA
4292: AE         XOR         (HL)
4293: 51         LD           D,C
4294: AC         XOR         H
4295: 62         LD           H,D
4296: AC         XOR         H
4297: 58         LD           E,B
4298: AC         XOR         H
4299: 67         LD           H,A
429A: AC         XOR         H
429B: 60         LD           H,B
429C: 27         DAA
429D: 61         LD           H,C
429E: 2B         DEC         HL
429F: 70         LD           (HL),B
42A0: 03         INC         BC
42A1: 71         LD           (HL),C
42A2: 27         DAA
42A3: 68         LD           L,B
42A4: 2C         INC         L
42A5: 69         LD           L,C
42A6: 28 78      JR           Z,$4320
42A8: 28 79      JR           Z,$4323
42AA: 03         INC         BC
42AB: 18 BF      JR           $426C
42AD: E2         LDFF00   (C),A
42AE: 00         NOP
42AF: 19         ADD         HL,DE
42B0: 78         LD           A,B
42B1: 10 FE      STOP       $FE
42B3: 04         INC         B
42B4: 0D         DEC         C
42B5: 20 F2      JR           NZ,$42A9
42B7: 39         ADD         HL,SP
42B8: F7         RST         0X30
42B9: 74         LD           (HL),H
42BA: ED                              
42BB: 10 C9      STOP       $C9
42BD: 40         LD           B,B
42BE: C9         RET
42BF: 73         LD           (HL),E
42C0: C8         RET         Z
42C1: 76         HALT
42C2: C8         RET         Z
42C3: 09         ADD         HL,BC
42C4: 21 79 22   LD           HL,$2279
42C7: C6 19      ADD         $19
42C9: 0D         DEC         C
42CA: 89         ADC         A,C
42CB: 21 0F 89   LD           HL,$890F
42CE: 31 0F 86   LD           SP,$860F
42D1: 64         LD           H,H
42D2: 0F         RRCA
42D3: 89         ADC         A,C
42D4: 51         LD           D,C
42D5: 12         LD           (DE),A
42D6: 11 AC 61   LD           DE,$61AC
42D9: AC         XOR         H
42DA: 24         INC         H
42DB: A6         AND         (HL)
42DC: 26 A6      LD           H,$A6
42DE: 35         DEC         (HL)
42DF: A6         AND         (HL)
42E0: 37         SCF
42E1: A6         AND         (HL)
42E2: 32         LD           (HLD),A
42E3: A7         AND         A
42E4: 82         ADD         A,D
42E5: 52         LD           D,D
42E6: AE         XOR         (HL)
42E7: FE 04      CP           $04
42E9: 0D         DEC         C
42EA: 30 F6      JR           NC,$42E2
42EC: C6 10      ADD         $10
42EE: 0D         DEC         C
42EF: 88         ADC         A,B
42F0: 20 0F      JR           NZ,$4301
42F2: 88         ADC         A,B
42F3: 30 0F      JR           NC,$4304
42F5: 88         ADC         A,B
42F6: 60         LD           H,B
42F7: 0F         RRCA
42F8: 82         ADD         A,D
42F9: 46         LD           B,(HL)
42FA: 0F         RRCA
42FB: 82         ADD         A,D
42FC: 56         LD           D,(HL)
42FD: 0F         RRCA
42FE: 23         INC         HL
42FF: A6         AND         (HL)
4300: 26 A6      LD           H,$A6
4302: 32         LD           (HLD),A
4303: A6         AND         (HL)
4304: 35         DEC         (HL)
4305: A6         AND         (HL)
4306: 44         LD           B,H
4307: A6         AND         (HL)
4308: 47         LD           B,A
4309: A6         AND         (HL)
430A: 53         LD           D,E
430B: A6         AND         (HL)
430C: 56         LD           D,(HL)
430D: A6         AND         (HL)
430E: 00         NOP
430F: 21 70 22   LD           HL,$2270
4312: 18 AC      JR           $42C0
4314: 68         LD           L,B
4315: AC         XOR         H
4316: 83         ADD         A,E
4317: 50         LD           D,B
4318: 12         LD           (DE),A
4319: FE 04      CP           $04
431B: 0F         RRCA
431C: 03         INC         BC
431D: C7         RST         0X00
431E: 06 C7      LD           B,$C7
4320: 04         INC         B
4321: F0 74      LD           A,($74)
4323: F1         POP         AF
4324: C6 11      ADD         $11
4326: 1C         INC         E
4327: C6 18      ADD         $18
4329: 1C         INC         E
432A: 12         LD           (DE),A
432B: 1F         RRA
432C: 17         RLA
432D: 1F         RRA
432E: 62         LD           H,D
432F: 1E 67      LD           E,$67
4331: 1E E2      LD           E,$E2
4333: 00         NOP
4334: 1A         LD           A,(DE)
4335: 28 13      JR           Z,$434A
4337: FE 04      CP           $04
4339: 8D         ADC         A,L
433A: 04         INC         B
433B: EC                              
433C: 74         LD           (HL),H
433D: F5         PUSH       AF
433E: 39         ADD         HL,SP
433F: F7         RST         0X30
4340: 82         ADD         A,D
4341: 74         LD           (HL),H
4342: 0D         DEC         C
4343: C2 39 0D   JP           NZ,$0D39
4346: 82         ADD         A,D
4347: 00         NOP
4348: 03         INC         BC
4349: 10 03      STOP       $03
434B: 02         LD           (BC),A
434C: 25         DEC         H
434D: 07         RLCA
434E: 26 C3      LD           H,$C3
4350: 17         RLA
4351: 24         INC         H
4352: 47         LD           B,A
4353: 2A         LD           A,(HLI)
4354: 82         ADD         A,D
4355: 48         LD           C,B
4356: 21 08 17   LD           HL,$1708
4359: 09         ADD         HL,BC
435A: 12         LD           (DE),A
435B: C2 18 11   JP           NZ,$1118
435E: 38 15      JR           C,$4375
4360: 39         ADD         HL,SP
4361: 13         INC         DE
4362: 16 AF      LD           D,$AF
4364: 56         LD           D,(HL)
4365: B0         OR           B
4366: C3 26 01   JP           $0126
4369: 83         ADD         A,E
436A: 57         LD           D,A
436B: B0         OR           B
436C: 68         LD           L,B
436D: 2C         INC         L
436E: 69         LD           L,C
436F: 22         LD           (HLI),A
4370: 78         LD           A,B
4371: 24         INC         H
4372: 79         LD           A,C
4373: 03         INC         BC
4374: 63         LD           H,E
4375: C0         RET         NZ
4376: 66         LD           H,(HL)
4377: C0         RET         NZ
4378: 20 25      JR           NZ,$439F
437A: 21 29 11   LD           HL,$1129
437D: 25         DEC         H
437E: 12         LD           (DE),A
437F: 29         ADD         HL,HL
4380: 02         LD           (BC),A
4381: 25         DEC         H
4382: 22         LD           (HLI),A
4383: AE         XOR         (HL)
4384: 35         DEC         (HL)
4385: AE         XOR         (HL)
4386: 42         LD           B,D
4387: A7         AND         A
4388: 61         LD           H,C
4389: AC         XOR         H
438A: FE 04      CP           $04
438C: 7D         LD           A,L
438D: 69         LD           L,C
438E: F7         RST         0X30
438F: 30 F6      JR           NC,$4387
4391: 74         LD           (HL),H
4392: F5         PUSH       AF
4393: 82         ADD         A,D
4394: 74         LD           (HL),H
4395: 0D         DEC         C
4396: C2 30 0D   JP           NZ,$0D30
4399: 8A         ADC         A,D
439A: 00         NOP
439B: 12         LD           (DE),A
439C: 82         ADD         A,D
439D: 01 AC 82   LD           BC,$82AC
43A0: 06 AC      LD           B,$AC
43A2: 14         INC         D
43A3: A0         AND         B
43A4: 21 96 85   LD           HL,$8596
43A7: 22         LD           (HLI),A
43A8: 13         INC         DE
43A9: 27         DAA
43AA: 95         SUB         L
43AB: 30 13      JR           NC,$43C0
43AD: 31 14 32   LD           SP,$3214
43B0: 25         DEC         H
43B1: 83         ADD         A,E
43B2: 33         INC         SP
43B3: 21 36 26   LD           HL,$2636
43B6: 37         SCF
43B7: 15         DEC         D
43B8: 82         ADD         A,D
43B9: 38 13      JR           C,$43CE
43BB: 82         ADD         A,D
43BC: 40         LD           B,B
43BD: 21 42 29   LD           HL,$2942
43C0: 83         ADD         A,E
43C1: 43         LD           B,E
43C2: 01 44 B0   LD           BC,$B044
43C5: 46         LD           B,(HL)
43C6: 2A         LD           A,(HLI)
43C7: 82         ADD         A,D
43C8: 47         LD           B,A
43C9: 21 49 26   LD           HL,$2649
43CC: 89         ADC         A,C
43CD: 50         LD           D,B
43CE: B0         OR           B
43CF: 54         LD           D,H
43D0: 0D         DEC         C
43D1: 59         LD           E,C
43D2: 24         INC         H
43D3: 60         LD           H,B
43D4: 22         LD           (HLI),A
43D5: 61         LD           H,C
43D6: 2B         DEC         HL
43D7: 70         LD           (HL),B
43D8: 03         INC         BC
43D9: 71         LD           (HL),C
43DA: 23         INC         HL
43DB: C2 19 0D   JP           NZ,$0D19
43DE: C3 59 24   JP           $2459
43E1: FE 00      CP           $00
43E3: 0D         DEC         C
43E4: 30 F6      JR           NC,$43DC
43E6: 76         HALT
43E7: F5         PUSH       AF
43E8: 76         HALT
43E9: 2B         DEC         HL
43EA: 77         LD           (HL),A
43EB: 0D         DEC         C
43EC: 78         LD           A,B
43ED: 2C         INC         L
43EE: 04         INC         B
43EF: 25         DEC         H
43F0: 08 26 09   LD           ($0926),SP
43F3: 03         INC         BC
43F4: 83         ADD         A,E
43F5: 00         NOP
43F6: 12         LD           (DE),A
43F7: 03         INC         BC
43F8: 16 C3      LD           D,$C3
43FA: 14         INC         D
43FB: 23         INC         HL
43FC: 18 2A      JR           $4428
43FE: 19         ADD         HL,DE
43FF: 26 0A      LD           H,$0A
4401: 26 C2      LD           H,$C2
4403: 13         INC         DE
4404: 10 82      STOP       $82
4406: 30 13      JR           NC,$441B
4408: 33         INC         SP
4409: 14         INC         D
440A: 40         LD           B,B
440B: 25         DEC         H
440C: 83         ADD         A,E
440D: 41         LD           B,C
440E: 21 44 29   LD           HL,$2944
4411: 42         LD           B,D
4412: 98         SBC         B
4413: 52         LD           D,D
4414: DE 45      SBC         $45
4416: AF         XOR         A
4417: 55         LD           D,L
4418: 01 65 B0   LD           BC,$B065
441B: C2 10 0D   JP           NZ,$0D10
441E: FE 04      CP           $04
4420: 07         RLCA
4421: 74         LD           (HL),H
4422: F5         PUSH       AF
4423: 73         LD           (HL),E
4424: 2B         DEC         HL
4425: 82         ADD         A,D
4426: 74         LD           (HL),H
4427: 0D         DEC         C
4428: 76         HALT
4429: 2C         INC         L
442A: 21 AC 60   LD           HL,$60AC
442D: 27         DAA
442E: 61         LD           H,C
442F: 2B         DEC         HL
4430: 70         LD           (HL),B
4431: 03         INC         BC
4432: 71         LD           (HL),C
4433: 27         DAA
4434: 68         LD           L,B
4435: 2C         INC         L
4436: 69         LD           L,C
4437: 28 78      JR           Z,$44B1
4439: 28 79      JR           Z,$44B4
443B: 03         INC         BC
443C: 28 A1      JR           Z,$43DF
443E: 00         NOP
443F: 03         INC         BC
4440: 01 25 10   LD           BC,$1025
4443: 25         DEC         H
4444: 11 29 08   LD           DE,$0829
4447: 26 09      LD           H,$09
4449: 03         INC         BC
444A: 18 2A      JR           $4476
444C: 19         ADD         HL,DE
444D: 26 FE      LD           H,$FE
444F: 04         INC         B
4450: 0D         DEC         C
4451: 04         INC         B
4452: F8 74      LDHL       SP,$74
4454: F5         PUSH       AF
4455: 33         INC         SP
4456: AC         XOR         H
4457: 36 AC      LD           (HL),$AC
4459: 03         INC         BC
445A: C7         RST         0X00
445B: 06 C7      LD           B,$C7
445D: 84         ADD         A,H
445E: 43         LD           B,E
445F: C0         RET         NZ
4460: 35         DEC         (HL)
4461: BE         CP           (HL)
4462: E2         LDFF00   (C),A
4463: 00         NOP
4464: 1B         DEC         DE
4465: 78         LD           A,B
4466: 10 FE      STOP       $FE
4468: 04         INC         B
4469: 0F         RRCA
446A: 39         ADD         HL,SP
446B: 42         LD           B,D
446C: 82         ADD         A,D
446D: 00         NOP
446E: 03         INC         BC
446F: C6 10      ADD         $10
4471: 03         INC         BC
4472: 82         ADD         A,D
4473: 70         LD           (HL),B
4474: 03         INC         BC
4475: 02         LD           (BC),A
4476: 25         DEC         H
4477: 11 25 12   LD           DE,$1225
447A: 29         ADD         HL,HL
447B: 13         INC         DE
447C: 01 83 14   LD           BC,$1483
447F: B0         OR           B
4480: 82         ADD         A,D
4481: 17         RLA
4482: 01 C4 22   LD           BC,$22C4
4485: 01 23 B0   LD           BC,$B023
4488: 82         ADD         A,D
4489: 27         DAA
448A: B0         OR           B
448B: 53         LD           D,E
448C: AF         XOR         A
448D: 82         ADD         A,D
448E: 57         LD           D,A
448F: AF         XOR         A
4490: 63         LD           H,E
4491: 01 83 64   LD           BC,$6483
4494: AF         XOR         A
4495: 82         ADD         A,D
4496: 67         LD           H,A
4497: 01 C4 21   LD           BC,$21C4
449A: 23         INC         HL
449B: 61         LD           H,C
449C: 27         DAA
449D: 62         LD           H,D
449E: 2B         DEC         HL
449F: 72         LD           (HL),D
44A0: 27         DAA
44A1: 34         INC         (HL)
44A2: A0         AND         B
44A3: FE 04      CP           $04
44A5: 5D         LD           E,L
44A6: 30 41      JR           NC,$44E9
44A8: 74         LD           (HL),H
44A9: F5         PUSH       AF
44AA: 04         INC         B
44AB: F4                              
44AC: 39         ADD         HL,SP
44AD: F7         RST         0X30
44AE: 82         ADD         A,D
44AF: 04         INC         B
44B0: 0D         DEC         C
44B1: C2 39 0D   JP           NZ,$0D39
44B4: 08 24 09   LD           ($0924),SP
44B7: 03         INC         BC
44B8: C2 13 C0   JP           NZ,$C013
44BB: C2 16 C0   JP           NZ,$C016
44BE: 18 2A      JR           $44EA
44C0: 19         ADD         HL,DE
44C1: 21 32 AF   LD           HL,$AF32
44C4: 37         SCF
44C5: AF         XOR         A
44C6: 42         LD           B,D
44C7: B0         OR           B
44C8: 47         LD           B,A
44C9: B0         OR           B
44CA: 51         LD           D,C
44CB: AF         XOR         A
44CC: 61         LD           H,C
44CD: 01 87 62   LD           BC,$6287
44D0: AF         XOR         A
44D1: 82         ADD         A,D
44D2: 64         LD           H,H
44D3: DD                              
44D4: 28 A1      JR           Z,$4477
44D6: FE 04      CP           $04
44D8: 6D         LD           L,L
44D9: 04         INC         B
44DA: F4                              
44DB: 30 F6      JR           NC,$44D3
44DD: 82         ADD         A,D
44DE: 04         INC         B
44DF: 0D         DEC         C
44E0: C2 30 0D   JP           NZ,$0D30
44E3: 00         NOP
44E4: 03         INC         BC
44E5: 01 23 10   LD           BC,$1023
44E8: 21 11 29   LD           HL,$2911
44EB: 83         ADD         A,E
44EC: 13         INC         DE
44ED: 0F         RRCA
44EE: 19         ADD         HL,DE
44EF: F7         RST         0X30
44F0: 19         ADD         HL,DE
44F1: 24         INC         H
44F2: 28 0D      JR           Z,$4501
44F4: 39         ADD         HL,SP
44F5: A6         AND         (HL)
44F6: C2 49 0D   JP           NZ,$0D49
44F9: 83         ADD         A,E
44FA: 23         INC         HL
44FB: 0F         RRCA
44FC: 83         ADD         A,E
44FD: 33         INC         SP
44FE: 0F         RRCA
44FF: 24         INC         H
4500: A0         AND         B
4501: 27         DAA
4502: A6         AND         (HL)
4503: 54         LD           D,H
4504: A6         AND         (HL)
4505: 57         LD           D,A
4506: A6         AND         (HL)
4507: 29         ADD         HL,HL
4508: 0D         DEC         C
4509: 19         ADD         HL,DE
450A: 2A         LD           A,(HLI)
450B: 69         LD           L,C
450C: 2C         INC         L
450D: FE 04      CP           $04
450F: 0D         DEC         C
4510: 06 F4      LD           B,$F4
4512: 30 F6      JR           NC,$450A
4514: 39         ADD         HL,SP
4515: EF         RST         0X28
4516: 74         LD           (HL),H
4517: FB         EI
4518: 06 29      LD           B,$29
451A: 07         RLCA
451B: 0D         DEC         C
451C: 08 2A 20   LD           ($202A),SP
451F: 0D         DEC         C
4520: 84         ADD         A,H
4521: 30 A6      JR           NC,$44C9
4523: 86         ADD         A,(HL)
4524: 23         INC         HL
4525: A6         AND         (HL)
4526: C2 40 0D   JP           NZ,$0D40
4529: 10 29      STOP       $29
452B: 60         LD           H,B
452C: 2B         DEC         HL
452D: FE 04      CP           $04
452F: 0D         DEC         C
4530: 04         INC         B
4531: F4                              
4532: 30 EE      JR           NC,$4522
4534: 39         ADD         HL,SP
4535: F7         RST         0X30
4536: 29         ADD         HL,HL
4537: CA 59 CA   JP           Z,$CA59
453A: 03         INC         BC
453B: 29         ADD         HL,HL
453C: 82         ADD         A,D
453D: 04         INC         B
453E: 0D         DEC         C
453F: 06 2A      LD           B,$2A
4541: 33         INC         SP
4542: 2C         INC         L
4543: 34         INC         (HL)
4544: 22         LD           (HLI),A
4545: 35         DEC         (HL)
4546: 2B         DEC         HL
4547: 43         LD           B,E
4548: 2A         LD           A,(HLI)
4549: 44         LD           B,H
454A: 21 45 29   LD           HL,$2945
454D: 28 AE      JR           Z,$44FD
454F: 58         LD           E,B
4550: AE         XOR         (HL)
4551: 27         DAA
4552: AF         XOR         A
4553: 57         LD           D,A
4554: B0         OR           B
4555: C2 37 01   JP           NZ,$0137
4558: FE 04      CP           $04
455A: 0F         RRCA
455B: 30 F2      JR           NC,$454F
455D: 04         INC         B
455E: F0 03      LD           A,($03)
4560: C7         RST         0X00
4561: 06 C7      LD           B,$C7
4563: 20 C9      JR           NZ,$452E
4565: 50         LD           D,B
4566: C9         RET
4567: FE 04      CP           $04
4569: 0D         DEC         C
456A: 04         INC         B
456B: F0 39      LD           A,($39)
456D: F3         DI
456E: 29         ADD         HL,HL
456F: CA 59 CA   JP           Z,$CA59
4572: 00         NOP
4573: 03         INC         BC
4574: 09         ADD         HL,BC
4575: 03         INC         BC
4576: 70         LD           (HL),B
4577: 03         INC         BC
4578: 79         LD           A,C
4579: 03         INC         BC
457A: 01 25 08   LD           BC,$0825
457D: 26 10      LD           H,$10
457F: 25         DEC         H
4580: 11 29 18   LD           DE,$1829
4583: 2A         LD           A,(HLI)
4584: 19         ADD         HL,DE
4585: 26 60      LD           H,$60
4587: 27         DAA
4588: 61         LD           H,C
4589: 2B         DEC         HL
458A: 71         LD           (HL),C
458B: 27         DAA
458C: 68         LD           L,B
458D: 2C         INC         L
458E: 69         LD           L,C
458F: 28 78      JR           Z,$4609
4591: 28 86      JR           Z,$4519
4593: 12         LD           (DE),A
4594: DF         RST         0X18
4595: 82         ADD         A,D
4596: 14         INC         D
4597: 0D         DEC         C
4598: C4 21 DF   CALL       NZ,$DF21
459B: 86         ADD         A,(HL)
459C: 62         LD           H,D
459D: DF         RST         0X18
459E: 82         ADD         A,D
459F: 64         LD           H,H
45A0: 0D         DEC         C
45A1: 28 DF      JR           Z,$4582
45A3: 58         LD           E,B
45A4: DF         RST         0X18
45A5: 33         INC         SP
45A6: C0         RET         NZ
45A7: 36 C0      LD           (HL),$C0
45A9: 43         LD           B,E
45AA: C0         RET         NZ
45AB: 46         LD           B,(HL)
45AC: C0         RET         NZ
45AD: FE 04      CP           $04
45AF: 0D         DEC         C
45B0: 30 F6      JR           NC,$45A8
45B2: 29         ADD         HL,HL
45B3: F7         RST         0X30
45B4: 74         LD           (HL),H
45B5: F5         PUSH       AF
45B6: 29         ADD         HL,HL
45B7: 2A         LD           A,(HLI)
45B8: C2 39 0D   JP           NZ,$0D39
45BB: 59         LD           E,C
45BC: 2C         INC         L
45BD: 73         LD           (HL),E
45BE: 2B         DEC         HL
45BF: 82         ADD         A,D
45C0: 74         LD           (HL),H
45C1: 0D         DEC         C
45C2: 76         HALT
45C3: 2C         INC         L
45C4: 23         INC         HL
45C5: AF         XOR         A
45C6: 26 AF      LD           H,$AF
45C8: 33         INC         SP
45C9: 01 36 01   LD           BC,$0136
45CC: 43         LD           B,E
45CD: B0         OR           B
45CE: 83         ADD         A,E
45CF: 44         LD           B,H
45D0: AE         XOR         (HL)
45D1: 46         LD           B,(HL)
45D2: B0         OR           B
45D3: 61         LD           H,C
45D4: AC         XOR         H
45D5: 68         LD           L,B
45D6: AC         XOR         H
45D7: 35         DEC         (HL)
45D8: AA         XOR         D
45D9: 28 A1      JR           Z,$457C
45DB: FE 04      CP           $04
45DD: 0D         DEC         C
45DE: 04         INC         B
45DF: F4                              
45E0: 04         INC         B
45E1: FA 20 F6   LD           A,($F620)
45E4: 34         INC         (HL)
45E5: A0         AND         B
45E6: 20 29      JR           NZ,$4611
45E8: C2 30 0D   JP           NZ,$0D30
45EB: 50         LD           D,B
45EC: 2B         DEC         HL
45ED: 11 01 61   LD           DE,$6101
45F0: 01 21 B0   LD           BC,$B021
45F3: 51         LD           D,C
45F4: AF         XOR         A
45F5: 53         LD           D,E
45F6: C0         RET         NZ
45F7: 56         LD           D,(HL)
45F8: C0         RET         NZ
45F9: 84         ADD         A,H
45FA: 13         INC         DE
45FB: 0F         RRCA
45FC: 84         ADD         A,H
45FD: 23         INC         HL
45FE: 0F         RRCA
45FF: 84         ADD         A,H
4600: 33         INC         SP
4601: 0F         RRCA
4602: 84         ADD         A,H
4603: 43         LD           B,E
4604: 0F         RRCA
4605: 13         INC         DE
4606: AC         XOR         H
4607: 16 AC      LD           D,$AC
4609: 28 A1      JR           Z,$45AC
460B: FE 04      CP           $04
460D: 0D         DEC         C
460E: 39         ADD         HL,SP
460F: F3         DI
4610: 83         ADD         A,E
4611: 22         LD           (HLI),A
4612: 0F         RRCA
4613: 83         ADD         A,E
4614: 32         LD           (HLD),A
4615: 0F         RRCA
4616: 83         ADD         A,E
4617: 42         LD           B,D
4618: 0F         RRCA
4619: 22         LD           (HLI),A
461A: C0         RET         NZ
461B: 24         INC         H
461C: C0         RET         NZ
461D: 33         INC         SP
461E: A0         AND         B
461F: 06 26      LD           B,$26
4621: 16 24      LD           D,$24
4623: 26 2A      LD           H,$2A
4625: 82         ADD         A,D
4626: 27         DAA
4627: 21 29 26   LD           HL,$2629
462A: 83         ADD         A,E
462B: 07         RLCA
462C: 03         INC         BC
462D: 83         ADD         A,E
462E: 17         RLA
462F: 03         INC         BC
4630: 83         ADD         A,E
4631: 67         LD           H,A
4632: 03         INC         BC
4633: 83         ADD         A,E
4634: 77         LD           (HL),A
4635: 03         INC         BC
4636: 56         LD           D,(HL)
4637: 2C         INC         L
4638: 82         ADD         A,D
4639: 57         LD           D,A
463A: 22         LD           (HLI),A
463B: 59         LD           E,C
463C: 28 66      JR           Z,$46A4
463E: 24         INC         H
463F: 76         HALT
4640: 28 11      JR           Z,$4653
4642: AC         XOR         H
4643: 15         DEC         D
4644: AC         XOR         H
4645: 61         LD           H,C
4646: AC         XOR         H
4647: 65         LD           H,L
4648: AC         XOR         H
4649: FE 04      CP           $04
464B: 0D         DEC         C
464C: 30 F6      JR           NC,$4644
464E: 39         ADD         HL,SP
464F: F7         RST         0X30
4650: 20 C9      JR           NZ,$461B
4652: 50         LD           D,B
4653: C9         RET
4654: 21 B0 86   LD           HL,$86B0
4657: 12         LD           (DE),A
4658: B0         OR           B
4659: 28 B0      JR           Z,$460B
465B: 51         LD           D,C
465C: AF         XOR         A
465D: 86         ADD         A,(HL)
465E: 62         LD           H,D
465F: AF         XOR         A
4660: 58         LD           E,B
4661: AF         XOR         A
4662: 29         ADD         HL,HL
4663: 2A         LD           A,(HLI)
4664: C2 39 0D   JP           NZ,$0D39
4667: 59         LD           E,C
4668: 2C         INC         L
4669: 00         NOP
466A: 03         INC         BC
466B: 09         ADD         HL,BC
466C: 03         INC         BC
466D: 70         LD           (HL),B
466E: 03         INC         BC
466F: 79         LD           A,C
4670: 03         INC         BC
4671: 01 25 08   LD           BC,$0825
4674: 26 10      LD           H,$10
4676: 25         DEC         H
4677: 11 29 18   LD           DE,$1829
467A: 2A         LD           A,(HLI)
467B: 19         ADD         HL,DE
467C: 26 60      LD           H,$60
467E: 27         DAA
467F: 61         LD           H,C
4680: 2B         DEC         HL
4681: 71         LD           (HL),C
4682: 27         DAA
4683: 68         LD           L,B
4684: 2C         INC         L
4685: 69         LD           L,C
4686: 28 78      JR           Z,$4700
4688: 28 32      JR           Z,$46BC
468A: 0F         RRCA
468B: FE 04      CP           $04
468D: 0D         DEC         C
468E: 04         INC         B
468F: F4                              
4690: 30 F6      JR           NC,$4688
4692: 03         INC         BC
4693: 29         ADD         HL,HL
4694: 82         ADD         A,D
4695: 04         INC         B
4696: 0D         DEC         C
4697: 06 2A      LD           B,$2A
4699: 20 29      JR           NZ,$46C4
469B: C2 30 0D   JP           NZ,$0D30
469E: 50         LD           D,B
469F: 2B         DEC         HL
46A0: C6 11      ADD         $11
46A2: 0F         RRCA
46A3: C6 18      ADD         $18
46A5: 0F         RRCA
46A6: 88         ADC         A,B
46A7: 11 0F 62   LD           DE,$620F
46AA: 0F         RRCA
46AB: 67         LD           H,A
46AC: 0F         RRCA
46AD: C3 22 C0   JP           $C022
46B0: C3 27 C0   JP           $C027
46B3: 23         INC         HL
46B4: C0         RET         NZ
46B5: 26 C0      LD           H,$C0
46B7: 11 AC 18   LD           DE,$18AC
46BA: AC         XOR         H
46BB: 61         LD           H,C
46BC: AC         XOR         H
46BD: 68         LD           L,B
46BE: AC         XOR         H
46BF: 53         LD           D,E
46C0: FC                              
46C1: E0 00      LDFF00   ($00),A
46C3: D3                              
46C4: 68         LD           L,B
46C5: 22         LD           (HLI),A
46C6: FE 05      CP           $05
46C8: 94         SUB         H
46C9: 8A         ADC         A,D
46CA: 00         NOP
46CB: 6D         LD           L,L
46CC: C7         RST         0X00
46CD: 02         LD           (BC),A
46CE: 63         LD           H,E
46CF: C3 10 6C   JP           $6C10
46D2: 83         ADD         A,E
46D3: 16 6B      LD           D,$6B
46D5: 17         RLA
46D6: 69         LD           L,C
46D7: 83         ADD         A,E
46D8: 26 69      LD           H,$69
46DA: 27         DAA
46DB: 82         ADD         A,D
46DC: 8A         ADC         A,D
46DD: 40         LD           B,B
46DE: 6D         LD           L,L
46DF: 42         LD           B,D
46E0: 62         LD           H,D
46E1: 45         LD           B,L
46E2: 04         INC         B
46E3: 48         LD           C,B
46E4: 62         LD           H,D
46E5: C3 50 54   JP           $5450
46E8: C2 51 57   JP           NZ,$5751
46EB: C2 58 63   JP           NZ,$6358
46EE: C2 59 6C   JP           NZ,$6C59
46F1: 71         LD           (HL),C
46F2: 54         LD           D,H
46F3: 88         ADC         A,B
46F4: 72         LD           (HL),D
46F5: 5B         LD           E,E
46F6: E1         POP         HL
46F7: 00         NOP
46F8: 01 48 60   LD           BC,$6048
46FB: FE 05      CP           $05
46FD: 94         SUB         H
46FE: 8A         ADC         A,D
46FF: 00         NOP
4700: 6D         LD           L,L
4701: C7         RST         0X00
4702: 07         RLCA
4703: 63         LD           H,E
4704: 83         ADD         A,E
4705: 11 6B 12   LD           DE,$126B
4708: 69         LD           L,C
4709: 83         ADD         A,E
470A: 21 69 22   LD           HL,$2269
470D: 82         ADD         A,D
470E: C2 19 6C   JP           NZ,$6C19
4711: 84         ADD         A,H
4712: 36 6D      LD           (HL),$6D
4714: 37         SCF
4715: 62         LD           H,D
4716: 40         LD           B,B
4717: 6D         LD           L,L
4718: 41         LD           B,C
4719: 62         LD           H,D
471A: 82         ADD         A,D
471B: 43         LD           B,E
471C: 6D         LD           L,L
471D: C3 48 51   JP           $5148
4720: C3 49 54   JP           $5449
4723: C2 50 6C   JP           NZ,$6C50
4726: C2 51 63   JP           NZ,$6351
4729: 88         ADC         A,B
472A: 70         LD           (HL),B
472B: 5B         LD           E,E
472C: 82         ADD         A,D
472D: 78         LD           A,B
472E: 54         LD           D,H
472F: E1         POP         HL
4730: 00         NOP
4731: 03         INC         BC
4732: 88         ADC         A,B
4733: 20 FE      JR           NZ,$4733
4735: 05         DEC         B
4736: 94         SUB         H
4737: C7         RST         0X00
4738: 00         NOP
4739: 6C         LD           L,H
473A: 82         ADD         A,D
473B: 30 6D      JR           NC,$47AA
473D: 8A         ADC         A,D
473E: 70         LD           (HL),B
473F: 6D         LD           L,L
4740: 82         ADD         A,D
4741: 61         LD           H,C
4742: 75         LD           (HL),L
4743: 64         LD           H,H
4744: 75         LD           (HL),L
4745: 83         ADD         A,E
4746: 32         LD           (HLD),A
4747: 6B         LD           L,E
4748: 33         INC         SP
4749: 69         LD           L,C
474A: 83         ADD         A,E
474B: 42         LD           B,D
474C: 69         LD           L,C
474D: 43         LD           B,E
474E: 82         ADD         A,D
474F: 83         ADD         A,E
4750: 36 6B      LD           (HL),$6B
4752: 37         SCF
4753: 69         LD           L,C
4754: 83         ADD         A,E
4755: 46         LD           B,(HL)
4756: 69         LD           L,C
4757: 47         LD           B,A
4758: 82         ADD         A,D
4759: 02         LD           (BC),A
475A: 4D         LD           C,L
475B: 08 4D C2   LD           ($C24D),SP
475E: 05         DEC         B
475F: 4D         LD           C,L
4760: 12         LD           (DE),A
4761: 78         LD           A,B
4762: 18 78      JR           $47DC
4764: 25         DEC         H
4765: 78         LD           A,B
4766: 22         LD           (HLI),A
4767: 79         LD           A,C
4768: 28 79      JR           Z,$47E3
476A: 35         DEC         (HL)
476B: 79         LD           A,C
476C: FE 05      CP           $05
476E: 94         SUB         H
476F: 83         ADD         A,E
4770: 31 6B 32   LD           SP,$326B
4773: 69         LD           L,C
4774: 83         ADD         A,E
4775: 41         LD           B,C
4776: 69         LD           L,C
4777: 42         LD           B,D
4778: 82         ADD         A,D
4779: 85         ADD         A,L
477A: 05         DEC         B
477B: 6D         LD           L,L
477C: C2 15 6C   JP           NZ,$6C15
477F: C6 19      ADD         $19
4781: 6C         LD           L,H
4782: 85         ADD         A,L
4783: 35         DEC         (HL)
4784: 6D         LD           L,L
4785: 8A         ADC         A,D
4786: 70         LD           (HL),B
4787: 6D         LD           L,L
4788: C7         RST         0X00
4789: 07         RLCA
478A: 63         LD           H,E
478B: 64         LD           H,H
478C: 75         LD           (HL),L
478D: 66         LD           H,(HL)
478E: 75         LD           (HL),L
478F: 68         LD           L,B
4790: 75         LD           (HL),L
4791: 37         SCF
4792: 62         LD           H,D
4793: E1         POP         HL
4794: 00         NOP
4795: 0B         DEC         BC
4796: 58         LD           E,B
4797: 40         LD           B,B
4798: FE 04      CP           $04
479A: 93         SUB         E
479B: 03         INC         BC
479C: F4                              
479D: 73         LD           (HL),E
479E: F5         PUSH       AF
479F: C8         RET         Z
47A0: 03         INC         BC
47A1: 23         INC         HL
47A2: C8         RET         Z
47A3: 04         INC         B
47A4: 0D         DEC         C
47A5: C8         RET         Z
47A6: 05         DEC         B
47A7: 24         INC         H
47A8: FE 04      CP           $04
47AA: 0D         DEC         C
47AB: 73         LD           (HL),E
47AC: F5         PUSH       AF
47AD: 73         LD           (HL),E
47AE: 2B         DEC         HL
47AF: 74         LD           (HL),H
47B0: 0D         DEC         C
47B1: 75         LD           (HL),L
47B2: 2C         INC         L
47B3: 83         ADD         A,E
47B4: 13         INC         DE
47B5: 0F         RRCA
47B6: 83         ADD         A,E
47B7: 23         INC         HL
47B8: 0F         RRCA
47B9: 83         ADD         A,E
47BA: 33         INC         SP
47BB: 0F         RRCA
47BC: 12         LD           (DE),A
47BD: AC         XOR         H
47BE: 16 AC      LD           D,$AC
47C0: 61         LD           H,C
47C1: AC         XOR         H
47C2: 68         LD           L,B
47C3: AC         XOR         H
47C4: 24         INC         H
47C5: A0         AND         B
47C6: C3 11 01   JP           $0111
47C9: C3 17 01   JP           $0117
47CC: C3 18 01   JP           $0118
47CF: 41         LD           B,C
47D0: B0         OR           B
47D1: 82         ADD         A,D
47D2: 47         LD           B,A
47D3: B0         OR           B
47D4: 85         ADD         A,L
47D5: 42         LD           B,D
47D6: AE         XOR         (HL)
47D7: 44         LD           B,H
47D8: 0D         DEC         C
47D9: FE 05      CP           $05
47DB: 94         SUB         H
47DC: 8A         ADC         A,D
47DD: 00         NOP
47DE: 6D         LD           L,L
47DF: C3 01 62   JP           $6201
47E2: C2 10 6C   JP           NZ,$6C10
47E5: 82         ADD         A,D
47E6: 15         DEC         D
47E7: 71         LD           (HL),C
47E8: 83         ADD         A,E
47E9: 17         RLA
47EA: 6B         LD           L,E
47EB: 18 69      JR           $4856
47ED: 83         ADD         A,E
47EE: 27         DAA
47EF: 69         LD           L,C
47F0: 28 82      JR           Z,$4774
47F2: 83         ADD         A,E
47F3: 30 6D      JR           NC,$4862
47F5: C3 40 54   JP           $5440
47F8: C3 41 57   JP           $5741
47FB: 43         LD           B,E
47FC: 64         LD           H,H
47FD: 53         LD           D,E
47FE: 65         LD           H,L
47FF: 82         ADD         A,D
4800: 48         LD           C,B
4801: 6D         LD           L,L
4802: 82         ADD         A,D
4803: 70         LD           (HL),B
4804: 54         LD           D,H
4805: 88         ADC         A,B
4806: 72         LD           (HL),D
4807: 5B         LD           E,E
4808: 23         INC         HL
4809: 6D         LD           L,L
480A: E1         POP         HL
480B: 03         INC         BC
480C: 72         LD           (HL),D
480D: 28 70      JR           Z,$487F
480F: FE 05      CP           $05
4811: 94         SUB         H
4812: 8A         ADC         A,D
4813: 00         NOP
4814: 6D         LD           L,L
4815: C7         RST         0X00
4816: 08 63 83   LD           ($8363),SP
4819: 11 6B 12   LD           DE,$126B
481C: 69         LD           L,C
481D: 83         ADD         A,E
481E: 21 69 22   LD           HL,$2269
4821: 82         ADD         A,D
4822: C3 13 6C   JP           $6C13
4825: C3 16 6C   JP           $6C16
4828: C6 19      ADD         $19
482A: 51         LD           D,C
482B: 82         ADD         A,D
482C: 40         LD           B,B
482D: 6D         LD           L,L
482E: 43         LD           B,E
482F: 6D         LD           L,L
4830: 46         LD           B,(HL)
4831: 6D         LD           L,L
4832: 89         ADC         A,C
4833: 70         LD           (HL),B
4834: 5B         LD           E,E
4835: 79         LD           A,C
4836: 54         LD           D,H
4837: E1         POP         HL
4838: 03         INC         BC
4839: 67         LD           H,A
483A: 88         ADC         A,B
483B: 20 FE      JR           NZ,$483B
483D: 04         INC         B
483E: 07         RLCA
483F: 39         ADD         HL,SP
4840: EF         RST         0X28
4841: C8         RET         Z
4842: 00         NOP
4843: 03         INC         BC
4844: 08 21 09   LD           ($0921),SP
4847: 26 61      LD           H,$61
4849: 03         INC         BC
484A: 19         ADD         HL,DE
484B: 24         INC         H
484C: 82         ADD         A,D
484D: 71         LD           (HL),C
484E: 03         INC         BC
484F: 69         LD           L,C
4850: 03         INC         BC
4851: 82         ADD         A,D
4852: 78         LD           A,B
4853: 03         INC         BC
4854: 01 25 11   LD           BC,$1125
4857: 23         INC         HL
4858: 02         LD           (BC),A
4859: 21 51 27   LD           HL,$2751
485C: 52         LD           D,D
485D: 2B         DEC         HL
485E: 62         LD           H,D
485F: 27         DAA
4860: 63         LD           H,E
4861: 2B         DEC         HL
4862: 73         LD           (HL),E
4863: 27         DAA
4864: 58         LD           E,B
4865: 2C         INC         L
4866: 59         LD           E,C
4867: 28 67      JR           Z,$48D0
4869: 2C         INC         L
486A: 68         LD           L,B
486B: 28 77      JR           Z,$48E4
486D: 28 22      JR           Z,$4891
486F: AB         XOR         E
4870: 65         LD           H,L
4871: AB         XOR         E
4872: C3 21 23   JP           $2321
4875: 28 A1      JR           Z,$4818
4877: FE 04      CP           $04
4879: 2D         DEC         L
487A: 30 EE      JR           NC,$486A
487C: 39         ADD         HL,SP
487D: F7         RST         0X30
487E: 74         LD           (HL),H
487F: F5         PUSH       AF
4880: 00         NOP
4881: 03         INC         BC
4882: 49         LD           C,C
4883: 03         INC         BC
4884: 70         LD           (HL),B
4885: 03         INC         BC
4886: 01 25 05   LD           BC,$0525
4889: C7         RST         0X00
488A: 10 25      STOP       $25
488C: 11 29 20   LD           DE,$2029
488F: C9         RET
4890: 50         LD           D,B
4891: C9         RET
4892: 60         LD           H,B
4893: 27         DAA
4894: 61         LD           H,C
4895: 2B         DEC         HL
4896: 71         LD           (HL),C
4897: 27         DAA
4898: 12         LD           (DE),A
4899: 01 13 B0   LD           BC,$B013
489C: 21 B0 22   LD           HL,$22B0
489F: B0         OR           B
48A0: 83         ADD         A,E
48A1: 16 20      LD           D,$20
48A3: 83         ADD         A,E
48A4: 26 20      LD           H,$20
48A6: 27         DAA
48A7: A0         AND         B
48A8: 82         ADD         A,D
48A9: 23         INC         HL
48AA: 20 82      JR           NZ,$482E
48AC: 56         LD           D,(HL)
48AD: 20 82      JR           NZ,$4831
48AF: 66         LD           H,(HL)
48B0: 20 82      JR           NZ,$4834
48B2: 46         LD           B,(HL)
48B3: AE         XOR         (HL)
48B4: 51         LD           D,C
48B5: AF         XOR         A
48B6: 52         LD           D,D
48B7: AF         XOR         A
48B8: 62         LD           H,D
48B9: 01 63 AF   LD           BC,$AF63
48BC: 38 2C      JR           C,$48EA
48BE: 39         ADD         HL,SP
48BF: C8         RET         Z
48C0: 48         LD           C,B
48C1: 24         INC         H
48C2: 58         LD           E,B
48C3: 2A         LD           A,(HLI)
48C4: 59         LD           E,C
48C5: C7         RST         0X00
48C6: 73         LD           (HL),E
48C7: 2B         DEC         HL
48C8: 74         LD           (HL),H
48C9: 0D         DEC         C
48CA: 75         LD           (HL),L
48CB: 2C         INC         L
48CC: FE 04      CP           $04
48CE: 2D         DEC         L
48CF: 30 F6      JR           NC,$48C7
48D1: 39         ADD         HL,SP
48D2: F7         RST         0X30
48D3: C6 10      ADD         $10
48D5: 0D         DEC         C
48D6: 88         ADC         A,B
48D7: 11 DB 88   LD           DE,$88DB
48DA: 21 DB 88   LD           HL,$88DB
48DD: 31 DB 00   LD           SP,$00DB
48E0: 21 70 22   LD           HL,$2270
48E3: 04         INC         B
48E4: 03         INC         BC
48E5: 03         INC         BC
48E6: 26 05      LD           H,$05
48E8: 25         DEC         H
48E9: 13         INC         DE
48EA: 2A         LD           A,(HLI)
48EB: 15         DEC         D
48EC: 29         ADD         HL,HL
48ED: 14         INC         D
48EE: C7         RST         0X00
48EF: 07         RLCA
48F0: C7         RST         0X00
48F1: 23         INC         HL
48F2: A6         AND         (HL)
48F3: 25         DEC         H
48F4: A6         AND         (HL)
48F5: 27         DAA
48F6: A0         AND         B
48F7: 34         INC         (HL)
48F8: DC 30 2B   CALL       C,$2B30
48FB: 40         LD           B,B
48FC: 23         INC         HL
48FD: 50         LD           D,B
48FE: 29         ADD         HL,HL
48FF: 88         ADC         A,B
4900: 41         LD           B,C
4901: AE         XOR         (HL)
4902: 39         ADD         HL,SP
4903: 2C         INC         L
4904: 49         LD           C,C
4905: 24         INC         H
4906: 59         LD           E,C
4907: 2A         LD           A,(HLI)
4908: 88         ADC         A,B
4909: 51         LD           D,C
490A: DC 84 53   CALL       C,$5384
490D: 20 84      JR           NZ,$4893
490F: 63         LD           H,E
4910: DC 72 C8   CALL       C,$C872
4913: 77         LD           (HL),A
4914: C8         RET         Z
4915: 24         INC         H
4916: 0D         DEC         C
4917: FE 04      CP           $04
4919: 4D         LD           C,L
491A: 30 F6      JR           NC,$4912
491C: 59         LD           E,C
491D: F7         RST         0X30
491E: C6 19      ADD         $19
4920: 0D         DEC         C
4921: 09         ADD         HL,BC
4922: 21 03 C7   LD           HL,$C703
4925: 06 C7      LD           B,$C7
4927: 73         LD           (HL),E
4928: C8         RET         Z
4929: 76         HALT
492A: C8         RET         Z
492B: C2 11 DC   JP           NZ,$DC11
492E: 15         DEC         D
492F: AE         XOR         (HL)
4930: 32         LD           (HLD),A
4931: AF         XOR         A
4932: 87         ADD         A,A
4933: 33         INC         SP
4934: AF         XOR         A
4935: 34         INC         (HL)
4936: 0D         DEC         C
4937: 37         SCF
4938: 0D         DEC         C
4939: 87         ADD         A,A
493A: 42         LD           B,D
493B: B0         OR           B
493C: 44         LD           B,H
493D: AE         XOR         (HL)
493E: 47         LD           B,A
493F: AE         XOR         (HL)
4940: 30 C8      JR           NC,$490A
4942: 31 2B 40   LD           SP,$402B
4945: 03         INC         BC
4946: 41         LD           B,C
4947: 23         INC         HL
4948: 50         LD           D,B
4949: C7         RST         0X00
494A: 51         LD           D,C
494B: 29         ADD         HL,HL
494C: 84         ADD         A,H
494D: 52         LD           D,D
494E: DC 82 56   CALL       C,$5682
4951: DB                              
4952: 82         ADD         A,D
4953: 66         LD           H,(HL)
4954: DB                              
4955: 49         LD           C,C
4956: 2C         INC         L
4957: 59         LD           E,C
4958: 2A         LD           A,(HLI)
4959: 69         LD           L,C
495A: 0D         DEC         C
495B: 79         LD           A,C
495C: 22         LD           (HLI),A
495D: FE 04      CP           $04
495F: 4D         LD           C,L
4960: 39         ADD         HL,SP
4961: EF         RST         0X28
4962: 50         LD           D,B
4963: F6 77      OR           $77
4965: F5         PUSH       AF
4966: 04         INC         B
4967: C7         RST         0X00
4968: 29         ADD         HL,HL
4969: CA 59 CA   JP           Z,$CA59
496C: 74         LD           (HL),H
496D: C8         RET         Z
496E: 83         ADD         A,E
496F: 30 AF      JR           NC,$4920
4971: 83         ADD         A,E
4972: 23         INC         HL
4973: 0F         RRCA
4974: 83         ADD         A,E
4975: 33         INC         SP
4976: 0F         RRCA
4977: 83         ADD         A,E
4978: 43         LD           B,E
4979: 0F         RRCA
497A: 40         LD           B,B
497B: 2B         DEC         HL
497C: 82         ADD         A,D
497D: 41         LD           B,C
497E: A6         AND         (HL)
497F: 83         ADD         A,E
4980: 53         LD           D,E
4981: A6         AND         (HL)
4982: C4 26 A6   CALL       NZ,$A626
4985: 50         LD           D,B
4986: 29         ADD         HL,HL
4987: 60         LD           H,B
4988: 0D         DEC         C
4989: 70         LD           (HL),B
498A: 22         LD           (HLI),A
498B: 76         HALT
498C: 2B         DEC         HL
498D: 77         LD           (HL),A
498E: 0D         DEC         C
498F: 78         LD           A,B
4990: 2C         INC         L
4991: FE 04      CP           $04
4993: 0D         DEC         C
4994: 30 EE      JR           NC,$4984
4996: 03         INC         BC
4997: C7         RST         0X00
4998: 06 C7      LD           B,$C7
499A: 73         LD           (HL),E
499B: C8         RET         Z
499C: 76         HALT
499D: C8         RET         Z
499E: 83         ADD         A,E
499F: 11 20 83   LD           DE,$8320
49A2: 21 20 83   LD           HL,$8320
49A5: 51         LD           D,C
49A6: 20 83      JR           NZ,$492B
49A8: 61         LD           H,C
49A9: 20 C2      JR           NZ,$496D
49AB: 14         INC         D
49AC: 20 C2      JR           NZ,$4970
49AE: 54         LD           D,H
49AF: 20 C4      JR           NZ,$4975
49B1: 25         DEC         H
49B2: 20 18      JR           NZ,$49CC
49B4: BF         CP           A
49B5: E2         LDFF00   (C),A
49B6: 01 3B 88   LD           BC,$883B
49B9: 10 FE      STOP       $FE
49BB: 04         INC         B
49BC: 0D         DEC         C
49BD: 04         INC         B
49BE: F4                              
49BF: 77         LD           (HL),A
49C0: F5         PUSH       AF
49C1: 11 AC 16   LD           DE,$16AC
49C4: AC         XOR         H
49C5: 38 AC      JR           C,$4973
49C7: 07         RLCA
49C8: 26 82      LD           H,$82
49CA: 08 03 82   LD           ($8203),SP
49CD: 18 03      JR           $49D2
49CF: 17         RLA
49D0: 24         INC         H
49D1: 27         DAA
49D2: 2A         LD           A,(HLI)
49D3: 28 21      JR           Z,$49F6
49D5: 29         ADD         HL,HL
49D6: 26 22      LD           H,$22
49D8: A0         AND         B
49D9: 23         INC         HL
49DA: AE         XOR         (HL)
49DB: 34         INC         (HL)
49DC: AE         XOR         (HL)
49DD: 45         LD           B,L
49DE: AE         XOR         (HL)
49DF: 56         LD           D,(HL)
49E0: AE         XOR         (HL)
49E1: 41         LD           B,C
49E2: AF         XOR         A
49E3: 52         LD           D,D
49E4: AF         XOR         A
49E5: 51         LD           D,C
49E6: B0         OR           B
49E7: 62         LD           H,D
49E8: 01 63 AF   LD           BC,$AF63
49EB: 03         INC         BC
49EC: 29         ADD         HL,HL
49ED: 04         INC         B
49EE: 0D         DEC         C
49EF: 05         DEC         B
49F0: 2A         LD           A,(HLI)
49F1: 76         HALT
49F2: 2B         DEC         HL
49F3: 77         LD           (HL),A
49F4: 0D         DEC         C
49F5: 78         LD           A,B
49F6: 2C         INC         L
49F7: E1         POP         HL
49F8: 01 36 50   LD           BC,$5036
49FB: 7C         LD           A,H
49FC: FE 04      CP           $04
49FE: 0D         DEC         C
49FF: 07         RLCA
4A00: F4                              
4A01: 06 29      LD           B,$29
4A03: 07         RLCA
4A04: 0D         DEC         C
4A05: 08 2A 82   LD           ($822A),SP
4A08: 12         LD           (DE),A
4A09: 20 22      JR           NZ,$4A2D
4A0B: 20 82      JR           NZ,$498F
4A0D: 44         LD           B,H
4A0E: A7         AND         A
4A0F: C2 53 A6   JP           NZ,$A653
4A12: C2 56 A6   JP           NZ,$A656
4A15: 61         LD           H,C
4A16: AC         XOR         H
4A17: 68         LD           L,B
4A18: AC         XOR         H
4A19: 82         ADD         A,D
4A1A: 54         LD           D,H
4A1B: 07         RLCA
4A1C: 82         ADD         A,D
4A1D: 64         LD           H,H
4A1E: 07         RLCA
4A1F: 28 A1      JR           Z,$49C2
4A21: 11 CB E2   LD           DE,$E2CB
4A24: 01 3D 88   LD           BC,$883D
4A27: 80         ADD         A,B
4A28: FE 04      CP           $04
4A2A: 0F         RRCA
4A2B: 59         LD           E,C
4A2C: F3         DI
4A2D: 74         LD           (HL),H
4A2E: FB         EI
4A2F: 00         NOP
4A30: 03         INC         BC
4A31: 09         ADD         HL,BC
4A32: 03         INC         BC
4A33: 01 25 10   LD           BC,$1025
4A36: 25         DEC         H
4A37: 11 29 08   LD           DE,$0829
4A3A: 26 18      LD           H,$18
4A3C: 2A         LD           A,(HLI)
4A3D: 19         ADD         HL,DE
4A3E: 26 86      LD           H,$86
4A40: 12         LD           (DE),A
4A41: DF         RST         0X18
4A42: 12         LD           (DE),A
4A43: DF         RST         0X18
4A44: 17         RLA
4A45: DF         RST         0X18
4A46: 41         LD           B,C
4A47: DF         RST         0X18
4A48: 48         LD           C,B
4A49: DF         RST         0X18
4A4A: 86         ADD         A,(HL)
4A4B: 62         LD           H,D
4A4C: DF         RST         0X18
4A4D: 82         ADD         A,D
4A4E: 64         LD           H,H
4A4F: 0F         RRCA
4A50: C2 21 DF   JP           NZ,$DF21
4A53: C2 28 DF   JP           NZ,$DF28
4A56: FE 04      CP           $04
4A58: 0D         DEC         C
4A59: 07         RLCA
4A5A: F4                              
4A5B: 50         LD           D,B
4A5C: F6 73      OR           $73
4A5E: C8         RET         Z
4A5F: 76         HALT
4A60: C8         RET         Z
4A61: 63         LD           H,E
4A62: AF         XOR         A
4A63: 66         LD           H,(HL)
4A64: AF         XOR         A
4A65: 38 AE      JR           C,$4A15
4A67: 13         INC         DE
4A68: B0         OR           B
4A69: 16 B0      LD           D,$B0
4A6B: 22         LD           (HLI),A
4A6C: C0         RET         NZ
4A6D: 84         ADD         A,H
4A6E: 23         INC         HL
4A6F: 20 27      JR           NZ,$4A98
4A71: C0         RET         NZ
4A72: C2 32 20   JP           NZ,$2032
4A75: C2 37 A6   JP           NZ,$A637
4A78: 52         LD           D,D
4A79: C0         RET         NZ
4A7A: 84         ADD         A,H
4A7B: 53         LD           D,E
4A7C: A6         AND         (HL)
4A7D: 57         LD           D,A
4A7E: C0         RET         NZ
4A7F: 06 29      LD           B,$29
4A81: 44         LD           B,H
4A82: CB E2      SET         1,E
4A84: 01 3C 18   LD           BC,$183C
4A87: 80         ADD         A,B
4A88: 07         RLCA
4A89: 0D         DEC         C
4A8A: 08 2A FE   LD           ($FE2A),SP
4A8D: 04         INC         B
4A8E: 0D         DEC         C
4A8F: 49         LD           C,C
4A90: F3         DI
4A91: 84         ADD         A,H
4A92: 13         INC         DE
4A93: 0F         RRCA
4A94: 84         ADD         A,H
4A95: 23         INC         HL
4A96: 0F         RRCA
4A97: 84         ADD         A,H
4A98: 33         INC         SP
4A99: 0F         RRCA
4A9A: 02         LD           (BC),A
4A9B: 26 03      LD           H,$03
4A9D: 2A         LD           A,(HLI)
4A9E: 06 29      LD           B,$29
4AA0: 07         RLCA
4AA1: 25         DEC         H
4AA2: C3 12 24   JP           $2412
4AA5: 42         LD           B,D
4AA6: 2A         LD           A,(HLI)
4AA7: 84         ADD         A,H
4AA8: 43         LD           B,E
4AA9: 21 82 44   LD           HL,$4482
4AAC: 97         SUB         A
4AAD: 47         LD           B,A
4AAE: 29         ADD         HL,HL
4AAF: C3 17 23   JP           $2317
4AB2: 13         INC         DE
4AB3: C0         RET         NZ
4AB4: 16 C0      LD           D,$C0
4AB6: 33         INC         SP
4AB7: C0         RET         NZ
4AB8: 36 C0      LD           (HL),$C0
4ABA: 11 AC 18   LD           DE,$18AC
4ABD: AC         XOR         H
4ABE: 61         LD           H,C
4ABF: AC         XOR         H
4AC0: 68         LD           L,B
4AC1: AC         XOR         H
4AC2: 73         LD           (HL),E
4AC3: C8         RET         Z
4AC4: 76         HALT
4AC5: C8         RET         Z
4AC6: E0 00      LDFF00   ($00),A
4AC8: 24         INC         H
4AC9: 38 22      JR           C,$4AED
4ACB: FE 04      CP           $04
4ACD: 0F         RRCA
4ACE: 40         LD           B,B
4ACF: F2                              
4AD0: 74         LD           (HL),H
4AD1: F1         POP         AF
4AD2: 82         ADD         A,D
4AD3: 00         NOP
4AD4: 03         INC         BC
4AD5: 82         ADD         A,D
4AD6: 08 03 10   LD           ($1003),SP
4AD9: 25         DEC         H
4ADA: 02         LD           (BC),A
4ADB: 25         DEC         H
4ADC: 07         RLCA
4ADD: 26 19      LD           H,$19
4ADF: 26 11      LD           H,$11
4AE1: C7         RST         0X00
4AE2: 18 C7      JR           $4AAB
4AE4: 72         LD           (HL),D
4AE5: C8         RET         Z
4AE6: 77         LD           (HL),A
4AE7: C8         RET         Z
4AE8: 12         LD           (DE),A
4AE9: 29         ADD         HL,HL
4AEA: 17         RLA
4AEB: 2A         LD           A,(HLI)
4AEC: 33         INC         SP
4AED: AC         XOR         H
4AEE: 36 AC      LD           (HL),$AC
4AF0: FE 04      CP           $04
4AF2: 07         RLCA
4AF3: 04         INC         B
4AF4: F4                              
4AF5: 04         INC         B
4AF6: FA 09 03   LD           A,($0309)
4AF9: 79         LD           A,C
4AFA: 03         INC         BC
4AFB: 18 2A      JR           $4B27
4AFD: 08 26 19   LD           ($1926),SP
4B00: 26 68      LD           H,$68
4B02: 2C         INC         L
4B03: 69         LD           L,C
4B04: 28 78      JR           Z,$4B7E
4B06: 28 09      JR           Z,$4B11
4B08: 03         INC         BC
4B09: 32         LD           (HLD),A
4B0A: AF         XOR         A
4B0B: 85         ADD         A,L
4B0C: 23         INC         HL
4B0D: AF         XOR         A
4B0E: 82         ADD         A,D
4B0F: 28 AF      JR           Z,$4AC0
4B11: 42         LD           B,D
4B12: B0         OR           B
4B13: 53         LD           D,E
4B14: B0         OR           B
4B15: 84         ADD         A,H
4B16: 56         LD           D,(HL)
4B17: B0         OR           B
4B18: 82         ADD         A,D
4B19: 54         LD           D,H
4B1A: AE         XOR         (HL)
4B1B: C2 33 01   JP           NZ,$0133
4B1E: C2 36 01   JP           NZ,$0136
4B21: C2 37 01   JP           NZ,$0137
4B24: 82         ADD         A,D
4B25: 38 01      JR           C,$4B28
4B27: 82         ADD         A,D
4B28: 48         LD           C,B
4B29: 01 C4 29   LD           BC,$29C4
4B2C: 24         INC         H
4B2D: 11 AB 61   LD           DE,$61AB
4B30: AB         XOR         E
4B31: 82         ADD         A,D
4B32: 24         INC         H
4B33: AE         XOR         (HL)
4B34: 67         LD           H,A
4B35: BE         CP           (HL)
4B36: E2         LDFF00   (C),A
4B37: 01 3E 18   LD           BC,$183E
4B3A: 10 FE      STOP       $FE
4B3C: 04         INC         B
4B3D: 0D         DEC         C
4B3E: 03         INC         BC
4B3F: C7         RST         0X00
4B40: 04         INC         B
4B41: F8 06      LDHL       SP,$06
4B43: C7         RST         0X00
4B44: 73         LD           (HL),E
4B45: C8         RET         Z
4B46: 76         HALT
4B47: C8         RET         Z
4B48: 13         INC         DE
4B49: AF         XOR         A
4B4A: 16 AF      LD           D,$AF
4B4C: 53         LD           D,E
4B4D: B0         OR           B
4B4E: 56         LD           D,(HL)
4B4F: B0         OR           B
4B50: C3 23 01   JP           $0123
4B53: C3 26 01   JP           $0126
4B56: C4 14 11   CALL       NZ,$1114
4B59: C4 15 10   CALL       NZ,$1015
4B5C: 82         ADD         A,D
4B5D: 24         INC         H
4B5E: AE         XOR         (HL)
4B5F: 82         ADD         A,D
4B60: 54         LD           D,H
4B61: AE         XOR         (HL)
4B62: 28 2C      JR           Z,$4B90
4B64: 29         ADD         HL,HL
4B65: 28 C4      JR           Z,$4B2B
4B67: 38 24      JR           C,$4B8D
4B69: 78         LD           A,B
4B6A: 28 C5      JR           Z,$4B31
4B6C: 39         ADD         HL,SP
4B6D: 03         INC         BC
4B6E: 00         NOP
4B6F: 25         DEC         H
4B70: 10 23      STOP       $23
4B72: 20 27      JR           NZ,$4B9B
4B74: 21 2B C4   LD           HL,$C42B
4B77: 31 23 C5   LD           SP,$C523
4B7A: 30 03      JR           NC,$4B7F
4B7C: 71         LD           (HL),C
4B7D: 27         DAA
4B7E: 18 BE      JR           $4B3E
4B80: E2         LDFF00   (C),A
4B81: 01 3A 18   LD           BC,$183A
4B84: 10 FE      STOP       $FE
4B86: 04         INC         B
4B87: 07         RLCA
4B88: 74         LD           (HL),H
4B89: F1         POP         AF
4B8A: 8A         ADC         A,D
4B8B: 00         NOP
4B8C: 03         INC         BC
4B8D: 8A         ADC         A,D
4B8E: 10 03      STOP       $03
4B90: 02         LD           (BC),A
4B91: 25         DEC         H
4B92: 12         LD           (DE),A
4B93: 23         INC         HL
4B94: 84         ADD         A,H
4B95: 03         INC         BC
4B96: 21 07 26   LD           HL,$2607
4B99: 17         RLA
4B9A: 24         INC         H
4B9B: 84         ADD         A,H
4B9C: 13         INC         DE
4B9D: 0F         RRCA
4B9E: 84         ADD         A,H
4B9F: 23         INC         HL
4BA0: 0F         RRCA
4BA1: 84         ADD         A,H
4BA2: 33         INC         SP
4BA3: 0F         RRCA
4BA4: 20 25      JR           NZ,$4BCB
4BA6: 21 21 22   LD           HL,$2221
4BA9: 29         ADD         HL,HL
4BAA: 24         INC         H
4BAB: A0         AND         B
4BAC: 27         DAA
4BAD: 2A         LD           A,(HLI)
4BAE: 28 21      JR           Z,$4BD1
4BB0: 29         ADD         HL,HL
4BB1: 26 82      LD           H,$82
4BB3: 41         LD           B,C
4BB4: AF         XOR         A
4BB5: 84         ADD         A,H
4BB6: 43         LD           B,E
4BB7: AE         XOR         (HL)
4BB8: 82         ADD         A,D
4BB9: 47         LD           B,A
4BBA: AF         XOR         A
4BBB: 82         ADD         A,D
4BBC: 51         LD           D,C
4BBD: B0         OR           B
4BBE: 82         ADD         A,D
4BBF: 57         LD           D,A
4BC0: B0         OR           B
4BC1: 53         LD           D,E
4BC2: AB         XOR         E
4BC3: 56         LD           D,(HL)
4BC4: AB         XOR         E
4BC5: FE 04      CP           $04
4BC7: 0D         DEC         C
4BC8: 77         LD           (HL),A
4BC9: ED                              
4BCA: 03         INC         BC
4BCB: C7         RST         0X00
4BCC: 06 C7      LD           B,$C7
4BCE: 73         LD           (HL),E
4BCF: C8         RET         Z
4BD0: 76         HALT
4BD1: C8         RET         Z
4BD2: 84         ADD         A,H
4BD3: 13         INC         DE
4BD4: 20 82      JR           NZ,$4B58
4BD6: 24         INC         H
4BD7: 20 C2      JR           NZ,$4B9B
4BD9: 31 20 C2   LD           SP,$C220
4BDC: 38 20      JR           C,$4BFE
4BDE: 82         ADD         A,D
4BDF: 54         LD           D,H
4BE0: 20 84      JR           NZ,$4B66
4BE2: 63         LD           H,E
4BE3: 20 82      JR           NZ,$4B67
4BE5: 34         INC         (HL)
4BE6: 0F         RRCA
4BE7: 33         INC         SP
4BE8: A7         AND         A
4BE9: 36 A7      LD           (HL),$A7
4BEB: 18 BF      JR           $4BAC
4BED: E2         LDFF00   (C),A
4BEE: 01 3F 88   LD           BC,$883F
4BF1: 10 FE      STOP       $FE
4BF3: 04         INC         B
4BF4: 07         RLCA
4BF5: 04         INC         B
4BF6: F0 39      LD           A,($39)
4BF8: EF         RST         0X28
4BF9: 53         LD           D,E
4BFA: AB         XOR         E
4BFB: 56         LD           D,(HL)
4BFC: AB         XOR         E
4BFD: FE 04      CP           $04
4BFF: 07         RLCA
4C00: 30 EE      JR           NC,$4BF0
4C02: 39         ADD         HL,SP
4C03: F3         DI
4C04: 74         LD           (HL),H
4C05: F5         PUSH       AF
4C06: C2 00 03   JP           NZ,$0300
4C09: C2 09 03   JP           NZ,$0309
4C0C: C2 60 03   JP           NZ,$0360
4C0F: C2 69 03   JP           NZ,$0369
4C12: 01 25 11   LD           BC,$1125
4C15: 23         INC         HL
4C16: 21 29 20   LD           HL,$2029
4C19: 25         DEC         H
4C1A: 08 26 18   LD           ($1826),SP
4C1D: 24         INC         H
4C1E: 28 2A      JR           Z,$4C4A
4C20: 29         ADD         HL,HL
4C21: 26 50      LD           H,$50
4C23: 27         DAA
4C24: 51         LD           D,C
4C25: 2B         DEC         HL
4C26: 61         LD           H,C
4C27: 23         INC         HL
4C28: 71         LD           (HL),C
4C29: 27         DAA
4C2A: 58         LD           E,B
4C2B: 2C         INC         L
4C2C: 59         LD           E,C
4C2D: 28 68      JR           Z,$4C97
4C2F: 24         INC         H
4C30: 78         LD           A,B
4C31: 28 23      JR           Z,$4C56
4C33: 2C         INC         L
4C34: 82         ADD         A,D
4C35: 24         INC         H
4C36: 22         LD           (HLI),A
4C37: 26 2B      LD           H,$2B
4C39: C2 33 24   JP           NZ,$2433
4C3C: C2 36 23   JP           NZ,$2336
4C3F: 53         LD           D,E
4C40: 2A         LD           A,(HLI)
4C41: 56         LD           D,(HL)
4C42: 29         ADD         HL,HL
4C43: 82         ADD         A,D
4C44: 54         LD           D,H
4C45: 97         SUB         A
4C46: 34         INC         (HL)
4C47: AB         XOR         E
4C48: 35         DEC         (HL)
4C49: AB         XOR         E
4C4A: 82         ADD         A,D
4C4B: 44         LD           B,H
4C4C: 0F         RRCA
4C4D: 73         LD           (HL),E
4C4E: 2B         DEC         HL
4C4F: 76         HALT
4C50: 2C         INC         L
4C51: 82         ADD         A,D
4C52: 74         LD           (HL),H
4C53: 0D         DEC         C
4C54: FE 04      CP           $04
4C56: 0D         DEC         C
4C57: 30 F6      JR           NC,$4C4F
4C59: 39         ADD         HL,SP
4C5A: F7         RST         0X30
4C5B: 74         LD           (HL),H
4C5C: ED                              
4C5D: C2 39 0D   JP           NZ,$0D39
4C60: 82         ADD         A,D
4C61: 00         NOP
4C62: 03         INC         BC
4C63: 82         ADD         A,D
4C64: 10 03      STOP       $03
4C66: 82         ADD         A,D
4C67: 08 03 82   LD           ($8203),SP
4C6A: 18 03      JR           $4C6F
4C6C: 82         ADD         A,D
4C6D: 60         LD           H,B
4C6E: 03         INC         BC
4C6F: 82         ADD         A,D
4C70: 70         LD           (HL),B
4C71: 03         INC         BC
4C72: 82         ADD         A,D
4C73: 68         LD           L,B
4C74: 03         INC         BC
4C75: 82         ADD         A,D
4C76: 78         LD           A,B
4C77: 03         INC         BC
4C78: C2 37 DB   JP           NZ,$DB37
4C7B: 02         LD           (BC),A
4C7C: 25         DEC         H
4C7D: 12         LD           (DE),A
4C7E: 23         INC         HL
4C7F: 22         LD           (HLI),A
4C80: 29         ADD         HL,HL
4C81: 21 21 20   LD           HL,$2021
4C84: 25         DEC         H
4C85: 50         LD           D,B
4C86: 27         DAA
4C87: 51         LD           D,C
4C88: 22         LD           (HLI),A
4C89: 52         LD           D,D
4C8A: 2B         DEC         HL
4C8B: 62         LD           H,D
4C8C: 23         INC         HL
4C8D: 72         LD           (HL),D
4C8E: 27         DAA
4C8F: 07         RLCA
4C90: 26 17      LD           H,$17
4C92: 24         INC         H
4C93: 27         DAA
4C94: 2A         LD           A,(HLI)
4C95: 28 21      JR           Z,$4CB8
4C97: 29         ADD         HL,HL
4C98: 21 59 22   LD           HL,$2259
4C9B: 58         LD           E,B
4C9C: 22         LD           (HLI),A
4C9D: 57         LD           D,A
4C9E: 2C         INC         L
4C9F: 67         LD           H,A
4CA0: 24         INC         H
4CA1: 77         LD           (HL),A
4CA2: 28 03      JR           Z,$4CA7
4CA4: C7         RST         0X00
4CA5: 06 C7      LD           B,$C7
4CA7: 73         LD           (HL),E
4CA8: C8         RET         Z
4CA9: 76         HALT
4CAA: C8         RET         Z
4CAB: 32         LD           (HLD),A
4CAC: 0F         RRCA
4CAD: FE 04      CP           $04
4CAF: 3D         DEC         A
4CB0: 30 F6      JR           NC,$4CA8
4CB2: 39         ADD         HL,SP
4CB3: F7         RST         0X30
4CB4: 74         LD           (HL),H
4CB5: F5         PUSH       AF
4CB6: C2 30 0D   JP           NZ,$0D30
4CB9: C2 39 0D   JP           NZ,$0D39
4CBC: 82         ADD         A,D
4CBD: 74         LD           (HL),H
4CBE: 0D         DEC         C
4CBF: C2 60 03   JP           NZ,$0360
4CC2: C2 69 03   JP           NZ,$0369
4CC5: C2 00 03   JP           NZ,$0300
4CC8: C2 09 03   JP           NZ,$0309
4CCB: 01 25 08   LD           BC,$0825
4CCE: 26 11      LD           H,$11
4CD0: 23         INC         HL
4CD1: 18 24      JR           $4CF7
4CD3: 20 21      JR           NZ,$4CF6
4CD5: 21 29 28   LD           HL,$2829
4CD8: 2A         LD           A,(HLI)
4CD9: 29         ADD         HL,HL
4CDA: 21 50 22   LD           HL,$2250
4CDD: 51         LD           D,C
4CDE: 2B         DEC         HL
4CDF: C2 61 23   JP           NZ,$2361
4CE2: 58         LD           E,B
4CE3: 2C         INC         L
4CE4: 59         LD           E,C
4CE5: 22         LD           (HLI),A
4CE6: C2 68 24   JP           NZ,$2468
4CE9: 86         ADD         A,(HL)
4CEA: 62         LD           H,D
4CEB: DC 03 C7   CALL       C,$C703
4CEE: 06 C7      LD           B,$C7
4CF0: 23         INC         HL
4CF1: C0         RET         NZ
4CF2: 26 C0      LD           H,$C0
4CF4: FE 04      CP           $04
4CF6: 4D         LD           C,L
4CF7: 76         HALT
4CF8: C8         RET         Z
4CF9: 74         LD           (HL),H
4CFA: DB                              
4CFB: 74         LD           (HL),H
4CFC: DC 39 F7   CALL       C,$F739
4CFF: 74         LD           (HL),H
4D00: F5         PUSH       AF
4D01: 30 F6      JR           NC,$4CF9
4D03: C2 30 0D   JP           NZ,$0D30
4D06: 19         ADD         HL,DE
4D07: 2A         LD           A,(HLI)
4D08: 69         LD           L,C
4D09: 2C         INC         L
4D0A: C4 29 0D   CALL       NZ,$0D29
4D0D: 83         ADD         A,E
4D0E: 00         NOP
4D0F: 03         INC         BC
4D10: 83         ADD         A,E
4D11: 10 03      STOP       $03
4D13: 83         ADD         A,E
4D14: 60         LD           H,B
4D15: 03         INC         BC
4D16: 83         ADD         A,E
4D17: 70         LD           (HL),B
4D18: 03         INC         BC
4D19: 03         INC         BC
4D1A: 25         DEC         H
4D1B: 13         INC         DE
4D1C: 23         INC         HL
4D1D: 83         ADD         A,E
4D1E: 20 21      JR           NZ,$4D41
4D20: 23         INC         HL
4D21: 29         ADD         HL,HL
4D22: 83         ADD         A,E
4D23: 50         LD           D,B
4D24: 22         LD           (HLI),A
4D25: 53         LD           D,E
4D26: 2B         DEC         HL
4D27: 63         LD           H,E
4D28: 23         INC         HL
4D29: 73         LD           (HL),E
4D2A: 27         DAA
4D2B: 32         LD           (HLD),A
4D2C: 0F         RRCA
4D2D: C2 33 A6   JP           NZ,$A633
4D30: 82         ADD         A,D
4D31: 14         INC         D
4D32: 20 82      JR           NZ,$4CB6
4D34: 67         LD           H,A
4D35: 20 24      JR           NZ,$4D5B
4D37: 20 58      JR           NZ,$4D91
4D39: 20 67      JR           NZ,$4DA2
4D3B: 20 73      JR           NZ,$4DB0
4D3D: 23         INC         HL
4D3E: 82         ADD         A,D
4D3F: 74         LD           (HL),H
4D40: 0D         DEC         C
4D41: 76         HALT
4D42: 2C         INC         L
4D43: FE 04      CP           $04
4D45: 4D         LD           C,L
4D46: 07         RLCA
4D47: EC                              
4D48: 30 F6      JR           NC,$4D40
4D4A: C2 30 0D   JP           NZ,$0D30
4D4D: 03         INC         BC
4D4E: C7         RST         0X00
4D4F: 06 C7      LD           B,$C7
4D51: 73         LD           (HL),E
4D52: C8         RET         Z
4D53: 76         HALT
4D54: C8         RET         Z
4D55: 29         ADD         HL,HL
4D56: CA 59 CA   JP           Z,$CA59
4D59: 00         NOP
4D5A: 03         INC         BC
4D5B: 01 25 10   LD           BC,$1025
4D5E: 21 11 29   LD           HL,$2911
4D61: 60         LD           H,B
4D62: 22         LD           (HLI),A
4D63: 70         LD           (HL),B
4D64: 03         INC         BC
4D65: 61         LD           H,C
4D66: 2B         DEC         HL
4D67: 71         LD           (HL),C
4D68: 27         DAA
4D69: 84         ADD         A,H
4D6A: 23         INC         HL
4D6B: 0F         RRCA
4D6C: 84         ADD         A,H
4D6D: 33         INC         SP
4D6E: 0F         RRCA
4D6F: 84         ADD         A,H
4D70: 43         LD           B,E
4D71: 0F         RRCA
4D72: 84         ADD         A,H
4D73: 53         LD           D,E
4D74: 0F         RRCA
4D75: 82         ADD         A,D
4D76: 34         INC         (HL)
4D77: A6         AND         (HL)
4D78: 82         ADD         A,D
4D79: 44         LD           B,H
4D7A: A6         AND         (HL)
4D7B: FE 04      CP           $04
4D7D: 0D         DEC         C
4D7E: 04         INC         B
4D7F: F4                              
4D80: 82         ADD         A,D
4D81: 60         LD           H,B
4D82: 03         INC         BC
4D83: 82         ADD         A,D
4D84: 70         LD           (HL),B
4D85: 03         INC         BC
4D86: 82         ADD         A,D
4D87: 68         LD           L,B
4D88: 03         INC         BC
4D89: 82         ADD         A,D
4D8A: 78         LD           A,B
4D8B: 03         INC         BC
4D8C: 02         LD           (BC),A
4D8D: C7         RST         0X00
4D8E: 07         RLCA
4D8F: C7         RST         0X00
4D90: 30 C9      JR           NC,$4D5B
4D92: 39         ADD         HL,SP
4D93: CA 50 27   JP           Z,$2750
4D96: 72         LD           (HL),D
4D97: 27         DAA
4D98: 51         LD           D,C
4D99: 22         LD           (HLI),A
4D9A: 52         LD           D,D
4D9B: 2B         DEC         HL
4D9C: 62         LD           H,D
4D9D: 23         INC         HL
4D9E: 57         LD           D,A
4D9F: 2C         INC         L
4DA0: 58         LD           E,B
4DA1: 22         LD           (HLI),A
4DA2: 59         LD           E,C
4DA3: 28 67      JR           Z,$4E0C
4DA5: 24         INC         H
4DA6: 77         LD           (HL),A
4DA7: 28 03      JR           Z,$4DAC
4DA9: 29         ADD         HL,HL
4DAA: 06 2A      LD           B,$2A
4DAC: 82         ADD         A,D
4DAD: 04         INC         B
4DAE: 0D         DEC         C
4DAF: 53         LD           D,E
4DB0: FC                              
4DB1: E0 00      LDFF00   ($00),A
4DB3: 24         INC         H
4DB4: 38 22      JR           C,$4DD8
4DB6: C4 11 20   CALL       NZ,$2011
4DB9: C4 12 20   CALL       NZ,$2012
4DBC: 84         ADD         A,H
4DBD: 13         INC         DE
4DBE: 0F         RRCA
4DBF: C4 17 20   CALL       NZ,$2017
4DC2: C4 18 20   CALL       NZ,$2018
4DC5: 84         ADD         A,H
4DC6: 23         INC         HL
4DC7: 0F         RRCA
4DC8: 84         ADD         A,H
4DC9: 33         INC         SP
4DCA: 0F         RRCA
4DCB: 82         ADD         A,D
4DCC: 24         INC         H
4DCD: AC         XOR         H
4DCE: 21 A0 FE   LD           HL,$FEA0
4DD1: 04         INC         B
4DD2: 0D         DEC         C
4DD3: 04         INC         B
4DD4: EC                              
4DD5: 03         INC         BC
4DD6: C7         RST         0X00
4DD7: 06 C7      LD           B,$C7
4DD9: 50         LD           D,B
4DDA: 27         DAA
4DDB: 51         LD           D,C
4DDC: 2B         DEC         HL
4DDD: 61         LD           H,C
4DDE: 27         DAA
4DDF: 62         LD           H,D
4DE0: 2B         DEC         HL
4DE1: 72         LD           (HL),D
4DE2: 27         DAA
4DE3: 58         LD           E,B
4DE4: 2C         INC         L
4DE5: 59         LD           E,C
4DE6: 28 67      JR           Z,$4E4F
4DE8: 2C         INC         L
4DE9: 68         LD           L,B
4DEA: 28 77      JR           Z,$4E63
4DEC: 28 60      JR           Z,$4E4E
4DEE: 03         INC         BC
4DEF: 69         LD           L,C
4DF0: 03         INC         BC
4DF1: 82         ADD         A,D
4DF2: 70         LD           (HL),B
4DF3: 03         INC         BC
4DF4: 82         ADD         A,D
4DF5: 78         LD           A,B
4DF6: 03         INC         BC
4DF7: 28 A1      JR           Z,$4D9A
4DF9: 82         ADD         A,D
4DFA: 17         RLA
4DFB: 0F         RRCA
4DFC: 27         DAA
4DFD: 0F         RRCA
4DFE: 82         ADD         A,D
4DFF: 37         SCF
4E00: 0F         RRCA
4E01: 84         ADD         A,H
4E02: 43         LD           B,E
4E03: 20 FE      JR           NZ,$4E03
4E05: 04         INC         B
4E06: 1D         DEC         E
4E07: 04         INC         B
4E08: F4                              
4E09: 19         ADD         HL,DE
4E0A: F7         RST         0X30
4E0B: 82         ADD         A,D
4E0C: 04         INC         B
4E0D: 0D         DEC         C
4E0E: C2 49 0D   JP           NZ,$0D49
4E11: 30 C9      JR           NC,$4DDC
4E13: 73         LD           (HL),E
4E14: C8         RET         Z
4E15: 76         HALT
4E16: C8         RET         Z
4E17: 00         NOP
4E18: 03         INC         BC
4E19: C3 09 03   JP           $0309
4E1C: 79         LD           A,C
4E1D: 03         INC         BC
4E1E: 01 23 10   LD           BC,$1023
4E21: 25         DEC         H
4E22: 11 29 C3   LD           DE,$C329
4E25: 08 24 38   LD           ($3824),SP
4E28: 2A         LD           A,(HLI)
4E29: 39         ADD         HL,SP
4E2A: 21 78 28   LD           HL,$2878
4E2D: 68         LD           L,B
4E2E: 2C         INC         L
4E2F: 69         LD           L,C
4E30: 22         LD           (HLI),A
4E31: C2 48 DB   JP           NZ,$DB48
4E34: 83         ADD         A,E
4E35: 33         INC         SP
4E36: DB                              
4E37: 83         ADD         A,E
4E38: 53         LD           D,E
4E39: DB                              
4E3A: 42         LD           B,D
4E3B: DB                              
4E3C: 46         LD           B,(HL)
4E3D: DB                              
4E3E: 43         LD           B,E
4E3F: A0         AND         B
4E40: 60         LD           H,B
4E41: 27         DAA
4E42: 61         LD           H,C
4E43: 2B         DEC         HL
4E44: 70         LD           (HL),B
4E45: 03         INC         BC
4E46: 71         LD           (HL),C
4E47: 27         DAA
4E48: FE 04      CP           $04
4E4A: 0D         DEC         C
4E4B: 58         LD           E,B
4E4C: AA         XOR         D
4E4D: 04         INC         B
4E4E: F4                              
4E4F: 40         LD           B,B
4E50: F6 02      OR           $02
4E52: C7         RST         0X00
4E53: 07         RLCA
4E54: C7         RST         0X00
4E55: 72         LD           (HL),D
4E56: C8         RET         Z
4E57: 77         LD           (HL),A
4E58: C8         RET         Z
4E59: C2 40 0D   JP           NZ,$0D40
4E5C: C2 11 20   JP           NZ,$2011
4E5F: 28 A1      JR           Z,$4E02
4E61: 60         LD           H,B
4E62: 2B         DEC         HL
4E63: 30 29      JR           NC,$4E8E
4E65: 82         ADD         A,D
4E66: 31 AE 48   LD           SP,$48AE
4E69: AE         XOR         (HL)
4E6A: C6 13      ADD         $13
4E6C: 01 C6 15   LD           BC,$15C6
4E6F: 01 C6 17   LD           BC,$17C6
4E72: 01 83 14   LD           BC,$1483
4E75: 0D         DEC         C
4E76: 24         INC         H
4E77: AE         XOR         (HL)
4E78: 26 AE      LD           H,$AE
4E7A: 25         DEC         H
4E7B: AF         XOR         A
4E7C: 12         LD           (DE),A
4E7D: DC 22 DC   CALL       C,$DC22
4E80: 16 DC      LD           D,$DC
4E82: 82         ADD         A,D
4E83: 41         LD           B,C
4E84: DB                              
4E85: 52         LD           D,D
4E86: DC 62 DB   CALL       C,$DB62
4E89: C2 34 DB   JP           NZ,$DB34
4E8C: C2 54 DC   JP           NZ,$DC54
4E8F: 36 DC      LD           (HL),$DC
4E91: C2 46 DB   JP           NZ,$DB46
4E94: 66         LD           H,(HL)
4E95: DC 58 AA   CALL       C,$AA58
4E98: 03         INC         BC
4E99: 29         ADD         HL,HL
4E9A: 82         ADD         A,D
4E9B: 04         INC         B
4E9C: 0D         DEC         C
4E9D: 06 2A      LD           B,$2A
4E9F: FE 05      CP           $05
4EA1: 94         SUB         H
4EA2: 8A         ADC         A,D
4EA3: 00         NOP
4EA4: 6D         LD           L,L
4EA5: C7         RST         0X00
4EA6: 01 63 C3   LD           BC,$C363
4EA9: 10 6C      STOP       $6C
4EAB: 83         ADD         A,E
4EAC: 14         INC         D
4EAD: 6B         LD           L,E
4EAE: 15         DEC         D
4EAF: 69         LD           L,C
4EB0: 83         ADD         A,E
4EB1: 24         INC         H
4EB2: 69         LD           L,C
4EB3: 25         DEC         H
4EB4: 82         ADD         A,D
4EB5: 22         LD           (HLI),A
4EB6: 6D         LD           L,L
4EB7: 28 62      JR           Z,$4F1B
4EB9: 29         ADD         HL,HL
4EBA: 6D         LD           L,L
4EBB: 32         LD           (HLD),A
4EBC: 6C         LD           L,H
4EBD: C4 38 63   CALL       NZ,$6338
4EC0: 39         ADD         HL,SP
4EC1: 6C         LD           L,H
4EC2: 83         ADD         A,E
4EC3: 40         LD           B,B
4EC4: 6D         LD           L,L
4EC5: 41         LD           B,C
4EC6: 62         LD           H,D
4EC7: 85         ADD         A,L
4EC8: 45         LD           B,L
4EC9: 6D         LD           L,L
4ECA: 48         LD           C,B
4ECB: 62         LD           H,D
4ECC: C2 50 57   JP           NZ,$5750
4ECF: C2 55 6C   JP           NZ,$6C55
4ED2: 70         LD           (HL),B
4ED3: 54         LD           D,H
4ED4: 89         ADC         A,C
4ED5: 71         LD           (HL),C
4ED6: 5B         LD           E,E
4ED7: E1         POP         HL
4ED8: 01 2D 88   LD           BC,$882D
4EDB: 20 FE      JR           NZ,$4EDB
4EDD: 05         DEC         B
4EDE: 94         SUB         H
4EDF: 8A         ADC         A,D
4EE0: 00         NOP
4EE1: 6D         LD           L,L
4EE2: C4 08 63   CALL       NZ,$6308
4EE5: 83         ADD         A,E
4EE6: 14         INC         D
4EE7: 6B         LD           L,E
4EE8: 15         DEC         D
4EE9: 69         LD           L,C
4EEA: 83         ADD         A,E
4EEB: 24         INC         H
4EEC: 69         LD           L,C
4EED: 25         DEC         H
4EEE: 82         ADD         A,D
4EEF: C3 19 6C   JP           $6C19
4EF2: 83         ADD         A,E
4EF3: 20 6D      JR           NZ,$4F62
4EF5: 82         ADD         A,D
4EF6: 30 54      JR           NC,$4F4C
4EF8: 32         LD           (HLD),A
4EF9: 6C         LD           L,H
4EFA: 8A         ADC         A,D
4EFB: 40         LD           B,B
4EFC: 6D         LD           L,L
4EFD: 82         ADD         A,D
4EFE: 43         LD           B,E
4EFF: 04         INC         B
4F00: C2 58 51   JP           NZ,$5158
4F03: C2 59 54   JP           NZ,$5459
4F06: 88         ADC         A,B
4F07: 70         LD           (HL),B
4F08: 5B         LD           E,E
4F09: 82         ADD         A,D
4F0A: 78         LD           A,B
4F0B: 54         LD           D,H
4F0C: E1         POP         HL
4F0D: 01 25 88   LD           BC,$8825
4F10: 20 FE      JR           NZ,$4F10
4F12: 05         DEC         B
4F13: 94         SUB         H
4F14: 8A         ADC         A,D
4F15: 00         NOP
4F16: 54         LD           D,H
4F17: 84         ADD         A,H
4F18: 10 54      STOP       $54
4F1A: 83         ADD         A,E
4F1B: 20 54      JR           NZ,$4F71
4F1D: 14         INC         D
4F1E: 5E         LD           E,(HL)
4F1F: 23         INC         HL
4F20: 5E         LD           E,(HL)
4F21: C2 30 57   JP           NZ,$5730
4F24: C3 50 68   JP           $6850
4F27: C2 61 65   JP           NZ,$6561
4F2A: 61         LD           H,C
4F2B: 64         LD           H,H
4F2C: 88         ADC         A,B
4F2D: 62         LD           H,D
4F2E: 68         LD           L,B
4F2F: 88         ADC         A,B
4F30: 72         LD           (HL),D
4F31: 68         LD           L,B
4F32: C3 53 6C   JP           $6C53
4F35: C3 57 6C   JP           $6C57
4F38: 16 71      LD           D,$71
4F3A: 18 71      JR           $4FAD
4F3C: 41         LD           B,C
4F3D: 71         LD           (HL),C
4F3E: 32         LD           (HLD),A
4F3F: 71         LD           (HL),C
4F40: 25         DEC         H
4F41: 71         LD           (HL),C
4F42: 27         DAA
4F43: 71         LD           (HL),C
4F44: 29         ADD         HL,HL
4F45: 71         LD           (HL),C
4F46: 31 70 15   LD           SP,$1570
4F49: 70         LD           (HL),B
4F4A: 17         RLA
4F4B: 70         LD           (HL),B
4F4C: 19         ADD         HL,DE
4F4D: 70         LD           (HL),B
4F4E: 49         LD           C,C
4F4F: 68         LD           L,B
4F50: E1         POP         HL
4F51: 01 29 48   LD           BC,$4829
4F54: 50         LD           D,B
4F55: FE 05      CP           $05
4F57: 94         SUB         H
4F58: 8A         ADC         A,D
4F59: 00         NOP
4F5A: 54         LD           D,H
4F5B: 84         ADD         A,H
4F5C: 16 54      LD           D,$54
4F5E: 83         ADD         A,E
4F5F: 27         DAA
4F60: 54         LD           D,H
4F61: C2 39 51   JP           NZ,$5139
4F64: 15         DEC         D
4F65: 5A         LD           E,D
4F66: 26 5A      LD           H,$5A
4F68: C3 59 68   JP           $6859
4F6B: 82         ADD         A,D
4F6C: 40         LD           B,B
4F6D: 68         LD           L,B
4F6E: 46         LD           B,(HL)
4F6F: 68         LD           L,B
4F70: 47         LD           B,A
4F71: 64         LD           H,H
4F72: 57         LD           D,A
4F73: 65         LD           H,L
4F74: 60         LD           H,B
4F75: 68         LD           L,B
4F76: 67         LD           H,A
4F77: 68         LD           L,B
4F78: 88         ADC         A,B
4F79: 70         LD           (HL),B
4F7A: 68         LD           L,B
4F7B: C3 54 6C   JP           $6C54
4F7E: C2 68 65   JP           NZ,$6568
4F81: 68         LD           L,B
4F82: 64         LD           H,H
4F83: 11 71 13   LD           DE,$1371
4F86: 71         LD           (HL),C
4F87: 20 71      JR           NZ,$4FFA
4F89: 22         LD           (HLI),A
4F8A: 71         LD           (HL),C
4F8B: 24         INC         H
4F8C: 71         LD           (HL),C
4F8D: 48         LD           C,B
4F8E: 71         LD           (HL),C
4F8F: 10 70      STOP       $70
4F91: 12         LD           (DE),A
4F92: 70         LD           (HL),B
4F93: 14         INC         D
4F94: 70         LD           (HL),B
4F95: 38 70      JR           C,$5007
4F97: E1         POP         HL
4F98: 01 27 18   LD           BC,$1827
4F9B: 20 FE      JR           NZ,$4F9B
4F9D: 05         DEC         B
4F9E: 94         SUB         H
4F9F: 8A         ADC         A,D
4FA0: 00         NOP
4FA1: 6D         LD           L,L
4FA2: C2 10 57   JP           NZ,$5710
4FA5: C5         PUSH       BC
4FA6: 30 54      JR           NC,$4FFC
4FA8: 31 5B C4   LD           SP,$C45B
4FAB: 41         LD           B,C
4FAC: 54         LD           D,H
4FAD: 32         LD           (HLD),A
4FAE: 5D         LD           E,L
4FAF: C3 42 57   JP           $5742
4FB2: 88         ADC         A,B
4FB3: 72         LD           (HL),D
4FB4: 54         LD           D,H
4FB5: C3 01 63   JP           $6301
4FB8: 15         DEC         D
4FB9: 5A         LD           E,D
4FBA: 84         ADD         A,H
4FBB: 16 54      LD           D,$54
4FBD: 26 5A      LD           H,$5A
4FBF: 83         ADD         A,E
4FC0: 27         DAA
4FC1: 54         LD           D,H
4FC2: 82         ADD         A,D
4FC3: 63         LD           H,E
4FC4: 4C         LD           C,H
4FC5: 67         LD           H,A
4FC6: 4C         LD           C,H
4FC7: 37         SCF
4FC8: 71         LD           (HL),C
4FC9: 48         LD           C,B
4FCA: 71         LD           (HL),C
4FCB: 39         ADD         HL,SP
4FCC: 71         LD           (HL),C
4FCD: 38 70      JR           C,$503F
4FCF: 82         ADD         A,D
4FD0: 65         LD           H,L
4FD1: 5B         LD           E,E
4FD2: 82         ADD         A,D
4FD3: 68         LD           L,B
4FD4: 5B         LD           E,E
4FD5: E1         POP         HL
4FD6: 01 2C 78   LD           BC,$782C
4FD9: 70         LD           (HL),B
4FDA: FE 05      CP           $05
4FDC: 94         SUB         H
4FDD: 8A         ADC         A,D
4FDE: 00         NOP
4FDF: 6D         LD           L,L
4FE0: 86         ADD         A,(HL)
4FE1: 10 54      STOP       $54
4FE3: 85         ADD         A,L
4FE4: 20 54      JR           NZ,$503A
4FE6: 16 5E      LD           D,$5E
4FE8: 25         DEC         H
4FE9: 5E         LD           E,(HL)
4FEA: C5         PUSH       BC
4FEB: 08 63 30   LD           ($3063),SP
4FEE: 71         LD           (HL),C
4FEF: 32         LD           (HLD),A
4FF0: 71         LD           (HL),C
4FF1: 34         INC         (HL)
4FF2: 71         LD           (HL),C
4FF3: 41         LD           B,C
4FF4: 71         LD           (HL),C
4FF5: 43         LD           B,E
4FF6: 71         LD           (HL),C
4FF7: 31 70 33   LD           SP,$3370
4FFA: 70         LD           (HL),B
4FFB: C6 19      ADD         $19
4FFD: 51         LD           D,C
4FFE: 82         ADD         A,D
4FFF: 60         LD           H,B
5000: 5B         LD           E,E
5001: 86         ADD         A,(HL)
5002: 62         LD           H,D
5003: 4C         LD           C,H
5004: 68         LD           L,B
5005: 59         LD           E,C
5006: 8A         ADC         A,D
5007: 70         LD           (HL),B
5008: 54         LD           D,H
5009: E1         POP         HL
500A: 01 2F 88   LD           BC,$882F
500D: 20 FE      JR           NZ,$500D
500F: 04         INC         B
5010: 0D         DEC         C
5011: 69         LD           L,C
5012: F7         RST         0X30
5013: 74         LD           (HL),H
5014: FB         EI
5015: 78         LD           A,B
5016: F5         PUSH       AF
5017: 82         ADD         A,D
5018: 00         NOP
5019: 03         INC         BC
501A: 02         LD           (BC),A
501B: 25         DEC         H
501C: 07         RLCA
501D: 26 82      LD           H,$82
501F: 08 03 10   LD           ($1003),SP
5022: 03         INC         BC
5023: 11 25 12   LD           DE,$1225
5026: 29         ADD         HL,HL
5027: 17         RLA
5028: 2A         LD           A,(HLI)
5029: 18 26      JR           $5051
502B: 19         ADD         HL,DE
502C: 03         INC         BC
502D: 20 25      JR           NZ,$5054
502F: 21 29 28   LD           HL,$2829
5032: 2A         LD           A,(HLI)
5033: 29         ADD         HL,HL
5034: 26 56      LD           H,$56
5036: 2C         INC         L
5037: 57         LD           D,A
5038: 22         LD           (HLI),A
5039: 58         LD           E,B
503A: 98         SBC         B
503B: 59         LD           E,C
503C: 28 66      JR           Z,$50A4
503E: 24         INC         H
503F: C2 67 10   JP           NZ,$1067
5042: 69         LD           L,C
5043: 12         LD           (DE),A
5044: 76         HALT
5045: 28 78      JR           Z,$50BF
5047: 0D         DEC         C
5048: 79         LD           A,C
5049: 13         INC         DE
504A: 82         ADD         A,D
504B: 24         INC         H
504C: 20 33      JR           NZ,$5081
504E: 20 36      JR           NZ,$5086
5050: 20 82      JR           NZ,$4FD4
5052: 44         LD           B,H
5053: 20 03      JR           NZ,$5058
5055: C7         RST         0X00
5056: 06 C7      LD           B,$C7
5058: FE 04      CP           $04
505A: 0D         DEC         C
505B: 39         ADD         HL,SP
505C: 42         LD           B,D
505D: 60         LD           H,B
505E: F6 84      OR           $84
5060: 24         INC         H
5061: 13         INC         DE
5062: 82         ADD         A,D
5063: 34         INC         (HL)
5064: 20 82      JR           NZ,$4FE8
5066: 44         LD           B,H
5067: 20 50      JR           NZ,$50B9
5069: 27         DAA
506A: 88         ADC         A,B
506B: 51         LD           D,C
506C: 22         LD           (HLI),A
506D: 59         LD           E,C
506E: 28 8A      JR           Z,$4FFA
5070: 60         LD           H,B
5071: 12         LD           (DE),A
5072: 8A         ADC         A,D
5073: 70         LD           (HL),B
5074: 13         INC         DE
5075: 32         LD           (HLD),A
5076: 0F         RRCA
5077: 02         LD           (BC),A
5078: C7         RST         0X00
5079: 07         RLCA
507A: C7         RST         0X00
507B: FE 04      CP           $04
507D: 0D         DEC         C
507E: 29         ADD         HL,HL
507F: F7         RST         0X30
5080: 30 49      JR           NC,$50CB
5082: 50         LD           D,B
5083: 27         DAA
5084: 88         ADC         A,B
5085: 51         LD           D,C
5086: 22         LD           (HLI),A
5087: 59         LD           E,C
5088: 28 8A      JR           Z,$5014
508A: 60         LD           H,B
508B: 12         LD           (DE),A
508C: 8A         ADC         A,D
508D: 70         LD           (HL),B
508E: 13         INC         DE
508F: 83         ADD         A,E
5090: 13         INC         DE
5091: 0F         RRCA
5092: 83         ADD         A,E
5093: 23         INC         HL
5094: 0F         RRCA
5095: 83         ADD         A,E
5096: 33         INC         SP
5097: 0F         RRCA
5098: 24         INC         H
5099: A0         AND         B
509A: 02         LD           (BC),A
509B: C7         RST         0X00
509C: 07         RLCA
509D: C7         RST         0X00
509E: FE 04      CP           $04
50A0: 0D         DEC         C
50A1: 20 F2      JR           NZ,$5095
50A3: 74         LD           (HL),H
50A4: F1         POP         AF
50A5: 06 26      LD           B,$26
50A7: 83         ADD         A,E
50A8: 07         RLCA
50A9: 03         INC         BC
50AA: 16 2A      LD           D,$2A
50AC: 17         RLA
50AD: 21 18 26   LD           HL,$2618
50B0: 19         ADD         HL,DE
50B1: 03         INC         BC
50B2: 28 2A      JR           Z,$50DE
50B4: 29         ADD         HL,HL
50B5: 26 50      LD           H,$50
50B7: 27         DAA
50B8: 51         LD           D,C
50B9: 22         LD           (HLI),A
50BA: 52         LD           D,D
50BB: 2B         DEC         HL
50BC: 60         LD           H,B
50BD: 12         LD           (DE),A
50BE: 61         LD           H,C
50BF: 16 62      LD           D,$62
50C1: 23         INC         HL
50C2: 67         LD           H,A
50C3: 2C         INC         L
50C4: 68         LD           L,B
50C5: 22         LD           (HLI),A
50C6: 69         LD           L,C
50C7: 28 70      JR           Z,$5139
50C9: 13         INC         DE
50CA: 71         LD           (HL),C
50CB: 14         INC         D
50CC: 72         LD           (HL),D
50CD: 27         DAA
50CE: 77         LD           (HL),A
50CF: 28 78      JR           Z,$5149
50D1: 0F         RRCA
50D2: 79         LD           A,C
50D3: 2C         INC         L
50D4: 10 C9      STOP       $C9
50D6: 40         LD           B,B
50D7: C9         RET
50D8: FE 04      CP           $04
50DA: 0D         DEC         C
50DB: 04         INC         B
50DC: FA 74 FB   LD           A,($FB74)
50DF: 08 F4 78   LD           ($78F4),SP
50E2: F5         PUSH       AF
50E3: 06 26      LD           B,$26
50E5: C6 16      ADD         $16
50E7: 24         INC         H
50E8: 76         HALT
50E9: 28 07      JR           Z,$50F2
50EB: 14         INC         D
50EC: 08 0D 09   LD           ($090D),SP
50EF: 15         DEC         D
50F0: C6 17      ADD         $17
50F2: 11 C6 19   LD           DE,$19C6
50F5: 10 77      STOP       $77
50F7: 16 78      LD           D,$78
50F9: 0D         DEC         C
50FA: 79         LD           A,C
50FB: 17         RLA
50FC: 28 A1      JR           Z,$509F
50FE: 20 C9      JR           NZ,$50C9
5100: 50         LD           D,B
5101: C9         RET
5102: 26 CA      LD           H,$CA
5104: 56         LD           D,(HL)
5105: CA FE 04   JP           Z,$04FE
5108: 0D         DEC         C
5109: 29         ADD         HL,HL
510A: F3         DI
510B: 75         LD           (HL),L
510C: F1         POP         AF
510D: C3 47 A6   JP           $A647
5110: 48         LD           C,B
5111: A6         AND         (HL)
5112: 58         LD           E,B
5113: DE 59      SBC         $59
5115: 0D         DEC         C
5116: C2 68 0D   JP           NZ,$0D68
5119: 69         LD           L,C
511A: 2C         INC         L
511B: 79         LD           A,C
511C: 24         INC         H
511D: 49         LD           C,C
511E: 2A         LD           A,(HLI)
511F: 77         LD           (HL),A
5120: 2B         DEC         HL
5121: 00         NOP
5122: 0D         DEC         C
5123: 01 25 10   LD           BC,$1025
5126: 25         DEC         H
5127: 11 29 60   LD           DE,$6029
512A: 27         DAA
512B: 83         ADD         A,E
512C: 61         LD           H,C
512D: 22         LD           (HLI),A
512E: 63         LD           H,E
512F: 98         SBC         B
5130: 64         LD           H,H
5131: 2B         DEC         HL
5132: 82         ADD         A,D
5133: 70         LD           (HL),B
5134: 12         LD           (DE),A
5135: 72         LD           (HL),D
5136: 16 73      LD           D,$73
5138: 0D         DEC         C
5139: 74         LD           (HL),H
513A: 27         DAA
513B: 78         LD           A,B
513C: 0D         DEC         C
513D: 03         INC         BC
513E: C7         RST         0X00
513F: 07         RLCA
5140: C7         RST         0X00
5141: FE 04      CP           $04
5143: 0D         DEC         C
5144: 20 F6      JR           NZ,$513C
5146: 29         ADD         HL,HL
5147: F7         RST         0X30
5148: 73         LD           (HL),E
5149: F5         PUSH       AF
514A: 02         LD           (BC),A
514B: C7         RST         0X00
514C: 05         DEC         B
514D: C7         RST         0X00
514E: 07         RLCA
514F: 24         INC         H
5150: 17         RLA
5151: 2A         LD           A,(HLI)
5152: 82         ADD         A,D
5153: 18 21      JR           $5176
5155: 82         ADD         A,D
5156: 08 0D C5   LD           ($C50D),SP
5159: 29         ADD         HL,HL
515A: 0D         DEC         C
515B: 83         ADD         A,E
515C: 23         INC         HL
515D: A6         AND         (HL)
515E: 24         INC         H
515F: A0         AND         B
5160: C4 33 11   CALL       NZ,$1133
5163: 82         ADD         A,D
5164: 41         LD           B,C
5165: 13         INC         DE
5166: 82         ADD         A,D
5167: 50         LD           D,B
5168: 0D         DEC         C
5169: 60         LD           H,B
516A: 22         LD           (HLI),A
516B: 61         LD           H,C
516C: 2B         DEC         HL
516D: C2 62 0D   JP           NZ,$0D62
5170: 70         LD           (HL),B
5171: 03         INC         BC
5172: 71         LD           (HL),C
5173: 23         INC         HL
5174: C2 36 A7   JP           NZ,$A736
5177: C4 28 A6   CALL       NZ,$A628
517A: 83         ADD         A,E
517B: 55         LD           D,L
517C: A6         AND         (HL)
517D: 82         ADD         A,D
517E: 65         LD           H,L
517F: 4F         LD           C,A
5180: 67         LD           H,A
5181: A7         AND         A
5182: 73         LD           (HL),E
5183: 2C         INC         L
5184: 82         ADD         A,D
5185: 74         LD           (HL),H
5186: 22         LD           (HLI),A
5187: 76         HALT
5188: 2B         DEC         HL
5189: 79         LD           A,C
518A: 2C         INC         L
518B: 40         LD           B,B
518C: 29         ADD         HL,HL
518D: 78         LD           A,B
518E: 0D         DEC         C
518F: 52         LD           D,D
5190: DE 07      SBC         $07
5192: 26 77      LD           H,$77
5194: 0D         DEC         C
5195: FE 04      CP           $04
5197: 0D         DEC         C
5198: 04         INC         B
5199: F4                              
519A: 30 F6      JR           NC,$5192
519C: 73         LD           (HL),E
519D: 48         LD           C,B
519E: 07         RLCA
519F: 26 09      LD           H,$09
51A1: 24         INC         H
51A2: 10 29      STOP       $29
51A4: C6 17      ADD         $17
51A6: 24         INC         H
51A7: C8         RET         Z
51A8: 08 0F 70   LD           ($700F),SP
51AB: 22         LD           (HLI),A
51AC: 77         LD           (HL),A
51AD: 28 79      JR           Z,$5228
51AF: 24         INC         H
51B0: 48         LD           C,B
51B1: AF         XOR         A
51B2: 58         LD           E,B
51B3: B0         OR           B
51B4: 18 A0      JR           $5156
51B6: 27         DAA
51B7: CA 57 CA   JP           Z,$CA57
51BA: C3 13 0F   JP           $0F13
51BD: 85         ADD         A,L
51BE: 41         LD           B,C
51BF: 0F         RRCA
51C0: 83         ADD         A,E
51C1: 52         LD           D,D
51C2: 0F         RRCA
51C3: 63         LD           H,E
51C4: 0F         RRCA
51C5: C5         PUSH       BC
51C6: 20 0D      JR           NZ,$51D5
51C8: FE 04      CP           $04
51CA: 0D         DEC         C
51CB: 04         INC         B
51CC: FA 49 F7   LD           A,($F749)
51CF: 08 F4 06   LD           ($06F4),SP
51D2: 26 82      LD           H,$82
51D4: 16 24      LD           D,$24
51D6: 26 2A      LD           H,$2A
51D8: 82         ADD         A,D
51D9: 27         DAA
51DA: 21 29 26   LD           HL,$2629
51DD: 18 21      JR           $5200
51DF: 19         ADD         HL,DE
51E0: 0D         DEC         C
51E1: 50         LD           D,B
51E2: 27         DAA
51E3: 82         ADD         A,D
51E4: 51         LD           D,C
51E5: 22         LD           (HLI),A
51E6: 53         LD           D,E
51E7: 2B         DEC         HL
51E8: 83         ADD         A,E
51E9: 60         LD           H,B
51EA: 03         INC         BC
51EB: 63         LD           H,E
51EC: 23         INC         HL
51ED: 83         ADD         A,E
51EE: 70         LD           (HL),B
51EF: 03         INC         BC
51F0: 73         LD           (HL),E
51F1: 27         DAA
51F2: C2 07 10   JP           NZ,$1007
51F5: 09         ADD         HL,BC
51F6: 12         LD           (DE),A
51F7: C2 08 0D   JP           NZ,$0D08
51FA: 82         ADD         A,D
51FB: 18 13      JR           $5210
51FD: 32         LD           (HLD),A
51FE: 0F         RRCA
51FF: 17         RLA
5200: AC         XOR         H
5201: 62         LD           H,D
5202: AC         XOR         H
5203: FE 04      CP           $04
5205: 0D         DEC         C
5206: 05         DEC         B
5207: F0 40      LD           A,($40)
5209: F2                              
520A: 49         LD           C,C
520B: F7         RST         0X30
520C: 08 0D 09   LD           ($090D),SP
520F: 24         INC         H
5210: C2 17 10   JP           NZ,$1017
5213: 19         ADD         HL,DE
5214: 2A         LD           A,(HLI)
5215: 28 DE      JR           Z,$51F5
5217: 29         ADD         HL,HL
5218: A6         AND         (HL)
5219: C4 39 0D   CALL       NZ,$0D39
521C: 39         ADD         HL,SP
521D: 12         LD           (DE),A
521E: 79         LD           A,C
521F: 22         LD           (HLI),A
5220: 07         RLCA
5221: 29         ADD         HL,HL
5222: 20 25      JR           NZ,$5249
5224: 00         NOP
5225: 12         LD           (DE),A
5226: 01 16 02   LD           BC,$0216
5229: 25         DEC         H
522A: 12         LD           (DE),A
522B: 23         INC         HL
522C: 22         LD           (HLI),A
522D: 29         ADD         HL,HL
522E: 21 98 10   LD           HL,$1098
5231: 13         INC         DE
5232: 31 A7 30   LD           SP,$30A7
5235: C9         RET
5236: 60         LD           H,B
5237: C9         RET
5238: 73         LD           (HL),E
5239: C8         RET         Z
523A: 76         HALT
523B: C8         RET         Z
523C: 82         ADD         A,D
523D: 00         NOP
523E: 12         LD           (DE),A
523F: 02         LD           (BC),A
5240: A6         AND         (HL)
5241: 03         INC         BC
5242: 0D         DEC         C
5243: 04         INC         B
5244: 25         DEC         H
5245: 10 13      STOP       $13
5247: 11 0D 12   LD           DE,$120D
524A: 25         DEC         H
524B: 13         INC         DE
524C: 21 14 29   LD           HL,$2914
524F: 37         SCF
5250: 94         SUB         H
5251: FE 04      CP           $04
5253: 0D         DEC         C
5254: 29         ADD         HL,HL
5255: CA 49 CA   JP           Z,$CA49
5258: 03         INC         BC
5259: F4                              
525A: 39         ADD         HL,SP
525B: 4A         LD           C,D
525C: 40         LD           B,B
525D: F6 74      OR           $74
525F: F5         PUSH       AF
5260: 73         LD           (HL),E
5261: 2B         DEC         HL
5262: 82         ADD         A,D
5263: 74         LD           (HL),H
5264: 0D         DEC         C
5265: 76         HALT
5266: 2C         INC         L
5267: C5         PUSH       BC
5268: 20 0D      JR           NZ,$5277
526A: 02         LD           (BC),A
526B: 0D         DEC         C
526C: 00         NOP
526D: 03         INC         BC
526E: 01 23 10   LD           BC,$1023
5271: 21 11 29   LD           HL,$2911
5274: C2 13 11   JP           NZ,$1113
5277: 83         ADD         A,E
5278: 30 12      JR           NC,$528C
527A: 33         INC         SP
527B: 93         SUB         E
527C: 21 BE 22   LD           HL,$22BE
527F: DE 70      SBC         $70
5281: 22         LD           (HLI),A
5282: 04         INC         B
5283: 0D         DEC         C
5284: E2         LDFF00   (C),A
5285: 02         LD           (BC),A
5286: AA         XOR         D
5287: 18 10      JR           $5299
5289: 03         INC         BC
528A: 2A         LD           A,(HLI)
528B: 04         INC         B
528C: C7         RST         0X00
528D: 05         DEC         B
528E: C7         RST         0X00
528F: 06 29      LD           B,$29
5291: 82         ADD         A,D
5292: 07         RLCA
5293: 0D         DEC         C
5294: 09         ADD         HL,BC
5295: 24         INC         H
5296: 82         ADD         A,D
5297: 57         LD           D,A
5298: 20 82      JR           NZ,$521C
529A: 62         LD           H,D
529B: 20 82      JR           NZ,$521F
529D: 67         LD           H,A
529E: 20 20      JR           NZ,$52C0
52A0: A6         AND         (HL)
52A1: FE 04      CP           $04
52A3: 0D         DEC         C
52A4: 30 41      JR           NC,$52E7
52A6: 03         INC         BC
52A7: 3F         CCF
52A8: 07         RLCA
52A9: 26 C2      LD           H,$C2
52AB: 08 0F 09   LD           ($090F),SP
52AE: 24         INC         H
52AF: 17         RLA
52B0: 24         INC         H
52B1: 19         ADD         HL,DE
52B2: 2A         LD           A,(HLI)
52B3: 27         DAA
52B4: 2A         LD           A,(HLI)
52B5: 28 98      JR           Z,$524F
52B7: 29         ADD         HL,HL
52B8: 26 58      LD           H,$58
52BA: 2C         INC         L
52BB: 59         LD           E,C
52BC: 28 83      JR           Z,$5241
52BE: 24         INC         H
52BF: A6         AND         (HL)
52C0: 84         ADD         A,H
52C1: 54         LD           D,H
52C2: A6         AND         (HL)
52C3: 83         ADD         A,E
52C4: 34         INC         (HL)
52C5: AF         XOR         A
52C6: 83         ADD         A,E
52C7: 44         LD           B,H
52C8: B0         OR           B
52C9: 58         LD           E,B
52CA: 2C         INC         L
52CB: 59         LD           E,C
52CC: 28 82      JR           Z,$5250
52CE: 66         LD           H,(HL)
52CF: 20 68      JR           NZ,$5339
52D1: 24         INC         H
52D2: C2 69 03   JP           NZ,$0369
52D5: 78         LD           A,B
52D6: 28 FE      JR           Z,$52D6
52D8: 04         INC         B
52D9: 0D         DEC         C
52DA: 76         HALT
52DB: F5         PUSH       AF
52DC: 75         LD           (HL),L
52DD: 2B         DEC         HL
52DE: 82         ADD         A,D
52DF: 76         HALT
52E0: 0D         DEC         C
52E1: 78         LD           A,B
52E2: 2C         INC         L
52E3: 82         ADD         A,D
52E4: 00         NOP
52E5: 03         INC         BC
52E6: 82         ADD         A,D
52E7: 08 03 10   LD           ($1003),SP
52EA: 03         INC         BC
52EB: 19         ADD         HL,DE
52EC: 03         INC         BC
52ED: 02         LD           (BC),A
52EE: 25         DEC         H
52EF: 11 25 20   LD           DE,$2025
52F2: 25         DEC         H
52F3: 07         RLCA
52F4: 26 18      LD           H,$18
52F6: 26 29      LD           H,$29
52F8: 26 12      LD           H,$12
52FA: 29         ADD         HL,HL
52FB: 21 29 17   LD           HL,$1729
52FE: 2A         LD           A,(HLI)
52FF: 28 2A      JR           Z,$532B
5301: 83         ADD         A,E
5302: 25         DEC         H
5303: 0F         RRCA
5304: 83         ADD         A,E
5305: 35         DEC         (HL)
5306: 0F         RRCA
5307: 83         ADD         A,E
5308: 45         LD           B,L
5309: 0F         RRCA
530A: 70         LD           (HL),B
530B: 23         INC         HL
530C: 52         LD           D,D
530D: 2C         INC         L
530E: 53         LD           D,E
530F: 22         LD           (HLI),A
5310: 54         LD           D,H
5311: 2B         DEC         HL
5312: C2 62 24   JP           NZ,$2462
5315: C2 63 03   JP           NZ,$0363
5318: 64         LD           H,H
5319: 23         INC         HL
531A: 74         LD           (HL),H
531B: 27         DAA
531C: 71         LD           (HL),C
531D: 0D         DEC         C
531E: 82         ADD         A,D
531F: 22         LD           (HLI),A
5320: DB                              
5321: C2 32 DB   JP           NZ,$DB32
5324: 33         INC         SP
5325: A0         AND         B
5326: C3 24 DC   JP           $DC24
5329: 43         LD           B,E
532A: DC 15 A7   CALL       C,$A715
532D: 36 BE      LD           (HL),$BE
532F: E1         POP         HL
5330: 02         LD           (BC),A
5331: 56         LD           D,(HL)
5332: 68         LD           L,B
5333: 40         LD           B,B
5334: 03         INC         BC
5335: C7         RST         0X00
5336: 06 C7      LD           B,$C7
5338: FE 04      CP           $04
533A: 0D         DEC         C
533B: 04         INC         B
533C: F4                              
533D: 03         INC         BC
533E: 29         ADD         HL,HL
533F: 82         ADD         A,D
5340: 04         INC         B
5341: 0D         DEC         C
5342: 06 2A      LD           B,$2A
5344: 00         NOP
5345: 03         INC         BC
5346: 01 25 08   LD           BC,$0825
5349: 26 09      LD           H,$09
534B: 03         INC         BC
534C: 10 25      STOP       $25
534E: 11 29 13   LD           DE,$1329
5351: AC         XOR         H
5352: 16 AC      LD           D,$AC
5354: 18 2A      JR           $5380
5356: 19         ADD         HL,DE
5357: 26 31      LD           H,$31
5359: AC         XOR         H
535A: 38 AC      JR           C,$5308
535C: 33         INC         SP
535D: 2C         INC         L
535E: 82         ADD         A,D
535F: 34         INC         (HL)
5360: 22         LD           (HLI),A
5361: 35         DEC         (HL)
5362: 98         SBC         B
5363: 36 2B      LD           (HL),$2B
5365: 43         LD           B,E
5366: 24         INC         H
5367: 46         LD           B,(HL)
5368: 23         INC         HL
5369: 53         LD           D,E
536A: 2A         LD           A,(HLI)
536B: 82         ADD         A,D
536C: 54         LD           D,H
536D: 21 56 29   LD           HL,$2956
5370: 32         LD           (HLD),A
5371: 0F         RRCA
5372: 44         LD           B,H
5373: BE         CP           (HL)
5374: E1         POP         HL
5375: 02         LD           (BC),A
5376: 57         LD           D,A
5377: 48         LD           C,B
5378: 60         LD           H,B
5379: FE 04      CP           $04
537B: 0D         DEC         C
537C: 06 F4      LD           B,$F4
537E: 76         HALT
537F: F5         PUSH       AF
5380: 05         DEC         B
5381: 29         ADD         HL,HL
5382: 82         ADD         A,D
5383: 06 0D      LD           B,$0D
5385: 08 2A C8   LD           ($C82A),SP
5388: 00         NOP
5389: 23         INC         HL
538A: C8         RET         Z
538B: 01 0D C8   LD           BC,$C80D
538E: 02         LD           (BC),A
538F: 24         INC         H
5390: C8         RET         Z
5391: 03         INC         BC
5392: 03         INC         BC
5393: C8         RET         Z
5394: 04         INC         B
5395: 23         INC         HL
5396: 04         INC         B
5397: 25         DEC         H
5398: 74         LD           (HL),H
5399: 27         DAA
539A: 28 A1      JR           Z,$533D
539C: 82         ADD         A,D
539D: 17         RLA
539E: 0F         RRCA
539F: 27         DAA
53A0: 0F         RRCA
53A1: 82         ADD         A,D
53A2: 37         SCF
53A3: 0F         RRCA
53A4: FE 04      CP           $04
53A6: 0D         DEC         C
53A7: 06 F0      LD           B,$F0
53A9: 39         ADD         HL,SP
53AA: F3         DI
53AB: 76         HALT
53AC: F1         POP         AF
53AD: 05         DEC         B
53AE: C7         RST         0X00
53AF: 08 C7 C8   LD           ($C8C7),SP
53B2: 00         NOP
53B3: 23         INC         HL
53B4: C8         RET         Z
53B5: 01 0D C8   LD           BC,$C80D
53B8: 02         LD           (BC),A
53B9: 24         INC         H
53BA: C8         RET         Z
53BB: 03         INC         BC
53BC: 03         INC         BC
53BD: C8         RET         Z
53BE: 04         INC         B
53BF: 23         INC         HL
53C0: 04         INC         B
53C1: 25         DEC         H
53C2: 74         LD           (HL),H
53C3: 27         DAA
53C4: 31 4F 41   LD           SP,$414F
53C7: 4F         LD           C,A
53C8: 27         DAA
53C9: A0         AND         B
53CA: FE 04      CP           $04
53CC: 0D         DEC         C
53CD: 30 F6      JR           NC,$53C5
53CF: 86         ADD         A,(HL)
53D0: 13         INC         DE
53D1: DC C4 28   CALL       C,$28C4
53D4: DC 83 66   CALL       C,$6683
53D7: DC 23 2C   CALL       C,$2C23
53DA: 83         ADD         A,E
53DB: 24         INC         H
53DC: 22         LD           (HLI),A
53DD: 27         DAA
53DE: 2B         DEC         HL
53DF: C2 33 24   JP           NZ,$2433
53E2: 83         ADD         A,E
53E3: 34         INC         (HL)
53E4: 0F         RRCA
53E5: 83         ADD         A,E
53E6: 44         LD           B,H
53E7: 0F         RRCA
53E8: C2 37 23   JP           NZ,$2337
53EB: 53         LD           D,E
53EC: 2A         LD           A,(HLI)
53ED: 83         ADD         A,E
53EE: 54         LD           D,H
53EF: C7         RST         0X00
53F0: 55         LD           D,L
53F1: 98         SBC         B
53F2: 57         LD           D,A
53F3: 29         ADD         HL,HL
53F4: 62         LD           H,D
53F5: A7         AND         A
53F6: 35         DEC         (HL)
53F7: A0         AND         B
53F8: FE 04      CP           $04
53FA: 0D         DEC         C
53FB: 06 F4      LD           B,$F4
53FD: 74         LD           (HL),H
53FE: F5         PUSH       AF
53FF: 00         NOP
5400: 23         INC         HL
5401: 01 0D C3   LD           BC,$C30D
5404: 02         LD           (BC),A
5405: 24         INC         H
5406: C3 03 03   JP           $0303
5409: 04         INC         B
540A: 25         DEC         H
540B: C2 14 23   JP           NZ,$2314
540E: 32         LD           (HLD),A
540F: 2A         LD           A,(HLI)
5410: 33         INC         SP
5411: 21 34 29   LD           HL,$2934
5414: 60         LD           H,B
5415: 27         DAA
5416: 71         LD           (HL),C
5417: 27         DAA
5418: 69         LD           L,C
5419: 28 78      JR           Z,$5493
541B: 28 61      JR           Z,$547E
541D: 2B         DEC         HL
541E: 68         LD           L,B
541F: 2C         INC         L
5420: 70         LD           (HL),B
5421: 03         INC         BC
5422: 79         LD           A,C
5423: 03         INC         BC
5424: 72         LD           (HL),D
5425: C8         RET         Z
5426: 77         LD           (HL),A
5427: C8         RET         Z
5428: 28 A1      JR           Z,$53CB
542A: 82         ADD         A,D
542B: 17         RLA
542C: 0F         RRCA
542D: 27         DAA
542E: 0F         RRCA
542F: 82         ADD         A,D
5430: 37         SCF
5431: 0F         RRCA
5432: FE 04      CP           $04
5434: 0D         DEC         C
5435: 04         INC         B
5436: F0 39      LD           A,($39)
5438: F7         RST         0X30
5439: 83         ADD         A,E
543A: 00         NOP
543B: 03         INC         BC
543C: 03         INC         BC
543D: 25         DEC         H
543E: 06 26      LD           B,$26
5440: 83         ADD         A,E
5441: 07         RLCA
5442: 03         INC         BC
5443: 10 25      STOP       $25
5445: 82         ADD         A,D
5446: 11 21 12   LD           DE,$1221
5449: C7         RST         0X00
544A: 13         INC         DE
544B: 29         ADD         HL,HL
544C: 82         ADD         A,D
544D: 14         INC         D
544E: 0F         RRCA
544F: 16 2A      LD           D,$2A
5451: 17         RLA
5452: C7         RST         0X00
5453: 18 21      JR           $5476
5455: 19         ADD         HL,DE
5456: 26 86      LD           H,$86
5458: 22         LD           (HLI),A
5459: 0F         RRCA
545A: 86         ADD         A,(HL)
545B: 32         LD           (HLD),A
545C: 0F         RRCA
545D: 86         ADD         A,(HL)
545E: 42         LD           B,D
545F: 0F         RRCA
5460: C2 23 C0   JP           NZ,$C023
5463: C2 26 C0   JP           NZ,$C026
5466: 61         LD           H,C
5467: AC         XOR         H
5468: 68         LD           L,B
5469: AC         XOR         H
546A: 29         ADD         HL,HL
546B: 2A         LD           A,(HLI)
546C: C2 39 0D   JP           NZ,$0D39
546F: 59         LD           E,C
5470: 2C         INC         L
5471: 82         ADD         A,D
5472: 51         LD           D,C
5473: 20 82      JR           NZ,$53F7
5475: 57         LD           D,A
5476: 20 62      JR           NZ,$54DA
5478: 20 67      JR           NZ,$54E1
547A: 20 53      JR           NZ,$54CF
547C: FC                              
547D: E0 00      LDFF00   ($00),A
547F: B5         OR           L
5480: 68         LD           L,B
5481: 20 FE      JR           NZ,$5481
5483: 04         INC         B
5484: 0D         DEC         C
5485: 30 F2      JR           NC,$5479
5487: 86         ADD         A,(HL)
5488: 11 01 86   LD           DE,$8601
548B: 21 B0 86   LD           HL,$86B0
548E: 51         LD           D,C
548F: AF         XOR         A
5490: 86         ADD         A,(HL)
5491: 61         LD           H,C
5492: 01 82 17   LD           BC,$1782
5495: 0F         RRCA
5496: 82         ADD         A,D
5497: 27         DAA
5498: 0F         RRCA
5499: 82         ADD         A,D
549A: 37         SCF
549B: 0F         RRCA
549C: 28 A0      JR           Z,$543E
549E: 20 29      JR           NZ,$54C9
54A0: C2 30 0D   JP           NZ,$0D30
54A3: 50         LD           D,B
54A4: 2B         DEC         HL
54A5: FE 07      CP           $07
54A7: 0D         DEC         C
54A8: 03         INC         BC
54A9: C7         RST         0X00
54AA: 06 C7      LD           B,$C7
54AC: 74         LD           (HL),H
54AD: ED                              
54AE: 73         LD           (HL),E
54AF: C8         RET         Z
54B0: 76         HALT
54B1: C8         RET         Z
54B2: 00         NOP
54B3: 03         INC         BC
54B4: 09         ADD         HL,BC
54B5: 03         INC         BC
54B6: 01 25 10   LD           BC,$1025
54B9: 25         DEC         H
54BA: 11 29 08   LD           DE,$0829
54BD: 26 19      LD           H,$19
54BF: 26 18      LD           H,$18
54C1: 2A         LD           A,(HLI)
54C2: 22         LD           (HLI),A
54C3: 96         SUB         (HL)
54C4: 23         INC         HL
54C5: 0F         RRCA
54C6: 24         INC         H
54C7: 95         SUB         L
54C8: 25         DEC         H
54C9: 96         SUB         (HL)
54CA: 26 0F      LD           H,$0F
54CC: 27         DAA
54CD: 95         SUB         L
54CE: 86         ADD         A,(HL)
54CF: 32         LD           (HLD),A
54D0: 0F         RRCA
54D1: 42         LD           B,D
54D2: 94         SUB         H
54D3: 43         LD           B,E
54D4: 0F         RRCA
54D5: 44         LD           B,H
54D6: 93         SUB         E
54D7: 45         LD           B,L
54D8: 94         SUB         H
54D9: 46         LD           B,(HL)
54DA: 0F         RRCA
54DB: 47         LD           B,A
54DC: 93         SUB         E
54DD: 21 20 28   LD           HL,$2820
54E0: 20 FE      JR           NZ,$54E0
54E2: 07         RLCA
54E3: 0D         DEC         C
54E4: 39         ADD         HL,SP
54E5: EF         RST         0X28
54E6: 00         NOP
54E7: 03         INC         BC
54E8: 09         ADD         HL,BC
54E9: 03         INC         BC
54EA: 01 25 10   LD           BC,$1025
54ED: 25         DEC         H
54EE: 11 29 08   LD           DE,$0829
54F1: 26 19      LD           H,$19
54F3: 26 18      LD           H,$18
54F5: 2A         LD           A,(HLI)
54F6: 60         LD           H,B
54F7: 27         DAA
54F8: 71         LD           (HL),C
54F9: 27         DAA
54FA: 69         LD           L,C
54FB: 28 78      JR           Z,$5575
54FD: 28 61      JR           Z,$5560
54FF: 2B         DEC         HL
5500: 68         LD           L,B
5501: 2C         INC         L
5502: 70         LD           (HL),B
5503: 03         INC         BC
5504: 79         LD           A,C
5505: 03         INC         BC
5506: C6 13      ADD         $13
5508: D2 14 AF   JP           NC,$AF14
550B: C6 15      ADD         $15
550D: D1         POP         DE
550E: C5         PUSH       BC
550F: 24         INC         H
5510: 01 64 B0   LD           BC,$B064
5513: C2 32 D2   JP           NZ,$D232
5516: 20 C9      JR           NZ,$54E1
5518: 50         LD           D,B
5519: C9         RET
551A: FE 07      CP           $07
551C: 0D         DEC         C
551D: 04         INC         B
551E: D0         RET         NC
551F: 04         INC         B
5520: EC                              
5521: 39         ADD         HL,SP
5522: EF         RST         0X28
5523: 30 EE      JR           NC,$5513
5525: 74         LD           (HL),H
5526: ED                              
5527: 03         INC         BC
5528: C7         RST         0X00
5529: 06 C7      LD           B,$C7
552B: 73         LD           (HL),E
552C: C8         RET         Z
552D: 76         HALT
552E: C8         RET         Z
552F: 82         ADD         A,D
5530: 00         NOP
5531: 03         INC         BC
5532: 02         LD           (BC),A
5533: 25         DEC         H
5534: 07         RLCA
5535: 26 82      LD           H,$82
5537: 08 03 10   LD           ($1003),SP
553A: 25         DEC         H
553B: 11 21 12   LD           DE,$1221
553E: 29         ADD         HL,HL
553F: 17         RLA
5540: 2A         LD           A,(HLI)
5541: 18 21      JR           $5564
5543: 19         ADD         HL,DE
5544: 26 60      LD           H,$60
5546: 27         DAA
5547: 61         LD           H,C
5548: 22         LD           (HLI),A
5549: 62         LD           H,D
554A: 2B         DEC         HL
554B: 67         LD           H,A
554C: 2C         INC         L
554D: 68         LD           L,B
554E: 22         LD           (HLI),A
554F: 69         LD           L,C
5550: 28 82      JR           Z,$54D4
5552: 70         LD           (HL),B
5553: 03         INC         BC
5554: 82         ADD         A,D
5555: 78         LD           A,B
5556: 03         INC         BC
5557: 72         LD           (HL),D
5558: 27         DAA
5559: 77         LD           (HL),A
555A: 28 36      JR           Z,$5592
555C: CB E1      SET         1,E
555E: 02         LD           (BC),A
555F: 4C         LD           C,H
5560: 68         LD           L,B
5561: 40         LD           B,B
5562: FE 07      CP           $07
5564: 0D         DEC         C
5565: 30 EE      JR           NC,$5555
5567: 12         LD           (DE),A
5568: C7         RST         0X00
5569: 17         RLA
556A: C7         RST         0X00
556B: 8A         ADC         A,D
556C: 00         NOP
556D: 03         INC         BC
556E: 8A         ADC         A,D
556F: 70         LD           (HL),B
5570: 03         INC         BC
5571: 10 25      STOP       $25
5573: 88         ADC         A,B
5574: 11 21 19   LD           DE,$1921
5577: 26 60      LD           H,$60
5579: 27         DAA
557A: 88         ADC         A,B
557B: 61         LD           H,C
557C: 22         LD           (HLI),A
557D: 87         ADD         A,A
557E: 22         LD           (HLI),A
557F: D1         POP         DE
5580: C2 38 D0   JP           NZ,$D038
5583: 84         ADD         A,H
5584: 44         LD           B,H
5585: D2 86 32   JP           NC,$3286
5588: C0         RET         NZ
5589: C2 42 C0   JP           NZ,$C042
558C: 84         ADD         A,H
558D: 55         LD           D,L
558E: C0         RET         NZ
558F: 69         LD           L,C
5590: 28 12      JR           Z,$55A4
5592: C7         RST         0X00
5593: 17         RLA
5594: C7         RST         0X00
5595: 62         LD           H,D
5596: C8         RET         Z
5597: 67         LD           H,A
5598: C8         RET         Z
5599: 54         LD           D,H
559A: CB E1      SET         1,E
559C: 02         LD           (BC),A
559D: 4D         LD           C,L
559E: 48         LD           C,B
559F: 50         LD           D,B
55A0: FE 07      CP           $07
55A2: 0D         DEC         C
55A3: 04         INC         B
55A4: EC                              
55A5: 82         ADD         A,D
55A6: 00         NOP
55A7: 03         INC         BC
55A8: 02         LD           (BC),A
55A9: 25         DEC         H
55AA: 03         INC         BC
55AB: C7         RST         0X00
55AC: 06 C7      LD           B,$C7
55AE: 07         RLCA
55AF: 26 82      LD           H,$82
55B1: 08 03 10   LD           ($1003),SP
55B4: 25         DEC         H
55B5: 11 21 12   LD           DE,$1221
55B8: 29         ADD         HL,HL
55B9: 17         RLA
55BA: 2A         LD           A,(HLI)
55BB: 18 21      JR           $55DE
55BD: 19         ADD         HL,DE
55BE: 26 60      LD           H,$60
55C0: 27         DAA
55C1: 61         LD           H,C
55C2: 2B         DEC         HL
55C3: 63         LD           H,E
55C4: AE         XOR         (HL)
55C5: 68         LD           L,B
55C6: 2C         INC         L
55C7: 69         LD           L,C
55C8: 28 70      JR           Z,$563A
55CA: 03         INC         BC
55CB: 71         LD           (HL),C
55CC: 27         DAA
55CD: 73         LD           (HL),E
55CE: C8         RET         Z
55CF: 76         HALT
55D0: C8         RET         Z
55D1: 78         LD           A,B
55D2: 28 79      JR           Z,$564D
55D4: 03         INC         BC
55D5: C2 31 CF   JP           NZ,$CF31
55D8: 87         ADD         A,A
55D9: 32         LD           (HLD),A
55DA: D1         POP         DE
55DB: 33         INC         SP
55DC: CF         RST         0X08
55DD: 35         DEC         (HL)
55DE: CF         RST         0X08
55DF: 37         SCF
55E0: CF         RST         0X08
55E1: 42         LD           B,D
55E2: D0         RET         NC
55E3: 43         LD           B,E
55E4: D1         POP         DE
55E5: 82         ADD         A,D
55E6: 44         LD           B,H
55E7: AE         XOR         (HL)
55E8: 46         LD           B,(HL)
55E9: D0         RET         NC
55EA: 47         LD           B,A
55EB: D1         POP         DE
55EC: C2 48 D0   JP           NZ,$D048
55EF: 82         ADD         A,D
55F0: 51         LD           D,C
55F1: D2 53 CF   JP           NC,$CF53
55F4: 82         ADD         A,D
55F5: 54         LD           D,H
55F6: 20 82      JR           NZ,$557A
55F8: 56         LD           D,(HL)
55F9: D2 83 63   JP           NC,$6383
55FC: D2 66 D0   JP           NC,$D066
55FF: FE 07      CP           $07
5601: 0D         DEC         C
5602: 74         LD           (HL),H
5603: F1         POP         AF
5604: 84         ADD         A,H
5605: 13         INC         DE
5606: 0F         RRCA
5607: 84         ADD         A,H
5608: 23         INC         HL
5609: 0F         RRCA
560A: 84         ADD         A,H
560B: 33         INC         SP
560C: 0F         RRCA
560D: 82         ADD         A,D
560E: 54         LD           D,H
560F: 0F         RRCA
5610: 82         ADD         A,D
5611: 64         LD           H,H
5612: 0F         RRCA
5613: 02         LD           (BC),A
5614: 26 03      LD           H,$03
5616: 2A         LD           A,(HLI)
5617: 06 29      LD           B,$29
5619: 07         RLCA
561A: 25         DEC         H
561B: C3 12 24   JP           $2412
561E: 42         LD           B,D
561F: 2A         LD           A,(HLI)
5620: 84         ADD         A,H
5621: 43         LD           B,E
5622: 21 82 44   LD           HL,$4482
5625: 97         SUB         A
5626: 47         LD           B,A
5627: 29         ADD         HL,HL
5628: C3 17 23   JP           $2317
562B: 13         INC         DE
562C: C0         RET         NZ
562D: 16 C0      LD           D,$C0
562F: 33         INC         SP
5630: C0         RET         NZ
5631: 36 C0      LD           (HL),$C0
5633: 11 AC 18   LD           DE,$18AC
5636: AC         XOR         H
5637: 61         LD           H,C
5638: AC         XOR         H
5639: 68         LD           L,B
563A: AC         XOR         H
563B: 73         LD           (HL),E
563C: C8         RET         Z
563D: 76         HALT
563E: C8         RET         Z
563F: E0 00      LDFF00   ($00),A
5641: B5         OR           L
5642: 68         LD           L,B
5643: 22         LD           (HLI),A
5644: FE FE      CP           $FE
5646: 07         RLCA
5647: 0D         DEC         C
5648: 04         INC         B
5649: F0 74      LD           A,($74)
564B: F1         POP         AF
564C: 03         INC         BC
564D: C7         RST         0X00
564E: 06 C7      LD           B,$C7
5650: 11 AC 18   LD           DE,$18AC
5653: AC         XOR         H
5654: 61         LD           H,C
5655: AC         XOR         H
5656: 68         LD           L,B
5657: AC         XOR         H
5658: FE 07      CP           $07
565A: 0D         DEC         C
565B: 04         INC         B
565C: F8 39      LDHL       SP,$39
565E: F7         RST         0X30
565F: 03         INC         BC
5660: C7         RST         0X00
5661: 06 C7      LD           B,$C7
5663: 11 CF 12   LD           DE,$12CF
5666: D1         POP         DE
5667: 13         INC         DE
5668: C0         RET         NZ
5669: 84         ADD         A,H
566A: 14         INC         D
566B: D2 C3 18   JP           NC,$18C3
566E: CF         RST         0X08
566F: 83         ADD         A,E
5670: 21 D2 22   LD           HL,$22D2
5673: D0         RET         NC
5674: 24         INC         H
5675: D0         RET         NC
5676: 25         DEC         H
5677: C0         RET         NZ
5678: C2 26 D0   JP           NZ,$D026
567B: C2 27 C0   JP           NZ,$C027
567E: C3 31 D0   JP           $D031
5681: C2 32 C0   JP           NZ,$C032
5684: 33         INC         SP
5685: CF         RST         0X08
5686: 34         INC         (HL)
5687: C0         RET         NZ
5688: 35         DEC         (HL)
5689: D2 36 D0   JP           NC,$D036
568C: 82         ADD         A,D
568D: 43         LD           B,E
568E: D2 45 D0   JP           NC,$D045
5691: 46         LD           B,(HL)
5692: C0         RET         NZ
5693: 47         LD           B,A
5694: CF         RST         0X08
5695: 48         LD           C,B
5696: D1         POP         DE
5697: 52         LD           D,D
5698: D1         POP         DE
5699: C2 53 D0   JP           NZ,$D053
569C: 82         ADD         A,D
569D: 54         LD           D,H
569E: C0         RET         NZ
569F: 56         LD           D,(HL)
56A0: CF         RST         0X08
56A1: 57         LD           D,A
56A2: D1         POP         DE
56A3: 58         LD           E,B
56A4: C0         RET         NZ
56A5: 82         ADD         A,D
56A6: 61         LD           H,C
56A7: C0         RET         NZ
56A8: 63         LD           H,E
56A9: D0         RET         NC
56AA: 83         ADD         A,E
56AB: 64         LD           H,H
56AC: D1         POP         DE
56AD: 82         ADD         A,D
56AE: 67         LD           H,A
56AF: C0         RET         NZ
56B0: 31 D2 32   LD           SP,$32D2
56B3: D0         RET         NC
56B4: FE 07      CP           $07
56B6: 0D         DEC         C
56B7: 30 D1      JR           NC,$568A
56B9: 30 F2      JR           NC,$56AD
56BB: 20 C9      JR           NZ,$5686
56BD: 50         LD           D,B
56BE: C9         RET
56BF: 11 88 16   LD           DE,$1688
56C2: 88         ADC         A,B
56C3: 82         ADD         A,D
56C4: 21 88 82   LD           HL,$8288
56C7: 25         DEC         H
56C8: 88         ADC         A,B
56C9: 82         ADD         A,D
56CA: 33         INC         SP
56CB: 88         ADC         A,B
56CC: C2 38 88   JP           NZ,$8838
56CF: C2 51 88   JP           NZ,$8851
56D2: C2 53 88   JP           NZ,$8853
56D5: C2 56 88   JP           NZ,$8856
56D8: 54         LD           D,H
56D9: 88         ADC         A,B
56DA: 18 CB      JR           $56A7
56DC: E2         LDFF00   (C),A
56DD: 02         LD           (BC),A
56DE: AB         XOR         E
56DF: 88         ADC         A,B
56E0: 80         ADD         A,B
56E1: FE 04      CP           $04
56E3: 0D         DEC         C
56E4: FE 05      CP           $05
56E6: 94         SUB         H
56E7: 8A         ADC         A,D
56E8: 00         NOP
56E9: 6D         LD           L,L
56EA: C3 01 64   JP           $6401
56ED: C6 10      ADD         $10
56EF: 57         LD           D,A
56F0: 89         ADC         A,C
56F1: 31 80 89   LD           SP,$8980
56F4: 41         LD           B,C
56F5: 81         ADD         A,C
56F6: C3 14 6C   JP           $6C14
56F9: C3 15 6C   JP           $6C15
56FC: 89         ADC         A,C
56FD: 51         LD           D,C
56FE: 81         ADD         A,C
56FF: 89         ADC         A,C
5700: 61         LD           H,C
5701: 81         ADD         A,C
5702: 64         LD           H,H
5703: 50         LD           D,B
5704: 65         LD           H,L
5705: 56         LD           D,(HL)
5706: 70         LD           (HL),B
5707: 54         LD           D,H
5708: 89         ADC         A,C
5709: 71         LD           (HL),C
570A: 53         LD           D,E
570B: 82         ADD         A,D
570C: 74         LD           (HL),H
570D: 54         LD           D,H
570E: 82         ADD         A,D
570F: 44         LD           B,H
5710: 6D         LD           L,L
5711: E1         POP         HL
5712: 03         INC         BC
5713: 6D         LD           L,L
5714: 18 20      JR           $5736
5716: FE 05      CP           $05
5718: 94         SUB         H
5719: 8A         ADC         A,D
571A: 00         NOP
571B: 6D         LD           L,L
571C: C3 08 65   JP           $6508
571F: 89         ADC         A,C
5720: 30 80      JR           NC,$56A2
5722: 89         ADC         A,C
5723: 40         LD           B,B
5724: 81         ADD         A,C
5725: 87         ADD         A,A
5726: 50         LD           D,B
5727: 81         ADD         A,C
5728: 87         ADD         A,A
5729: 60         LD           H,B
572A: 81         ADD         A,C
572B: C4 12 6C   CALL       NZ,$6C12
572E: C4 19 51   CALL       NZ,$5119
5731: 52         LD           D,D
5732: 6D         LD           L,L
5733: 57         LD           D,A
5734: 50         LD           D,B
5735: 58         LD           E,B
5736: 53         LD           D,E
5737: C3 59 54   JP           $5459
573A: 67         LD           H,A
573B: 51         LD           D,C
573C: 68         LD           L,B
573D: 54         LD           D,H
573E: 87         ADD         A,A
573F: 70         LD           (HL),B
5740: 53         LD           D,E
5741: 83         ADD         A,E
5742: 77         LD           (HL),A
5743: 54         LD           D,H
5744: E1         POP         HL
5745: 03         INC         BC
5746: 6E         LD           L,(HL)
5747: 18 20      JR           $5769
5749: FE 0C      CP           $0C
574B: 0D         DEC         C
574C: 39         ADD         HL,SP
574D: F3         DI
574E: 74         LD           (HL),H
574F: F1         POP         AF
5750: 02         LD           (BC),A
5751: 26 83      LD           H,$83
5753: 03         INC         BC
5754: C0         RET         NZ
5755: 06 25      LD           B,$25
5757: 08 26 C2   LD           ($C226),SP
575A: 09         ADD         HL,BC
575B: 03         INC         BC
575C: 11 C0 C3   LD           DE,$C3C0
575F: 12         LD           (DE),A
5760: 24         INC         H
5761: C3 16 23   JP           $2316
5764: 13         INC         DE
5765: 17         RLA
5766: 14         INC         D
5767: 12         LD           (DE),A
5768: 15         DEC         D
5769: 16 23      LD           D,$23
576B: 11 25 10   LD           DE,$1025
576E: 33         INC         SP
576F: 15         DEC         D
5770: 35         DEC         (HL)
5771: 14         INC         D
5772: 17         RLA
5773: C0         RET         NZ
5774: 18 24      JR           $579A
5776: 42         LD           B,D
5777: 2A         LD           A,(HLI)
5778: 43         LD           B,E
5779: C7         RST         0X00
577A: 44         LD           B,H
577B: 98         SBC         B
577C: 45         LD           B,L
577D: C7         RST         0X00
577E: 46         LD           B,(HL)
577F: 29         ADD         HL,HL
5780: 29         ADD         HL,HL
5781: 26 28      LD           H,$28
5783: 2A         LD           A,(HLI)
5784: 58         LD           E,B
5785: 2C         INC         L
5786: 59         LD           E,C
5787: 28 68      JR           Z,$57F1
5789: 24         INC         H
578A: C2 69 03   JP           NZ,$0369
578D: 78         LD           A,B
578E: 28 24      JR           Z,$57B4
5790: A0         AND         B
5791: FE 0C      CP           $0C
5793: 0D         DEC         C
5794: 30 F6      JR           NC,$578C
5796: 74         LD           (HL),H
5797: F5         PUSH       AF
5798: C2 31 0F   JP           NZ,$0F31
579B: 82         ADD         A,D
579C: 64         LD           H,H
579D: 0F         RRCA
579E: 03         INC         BC
579F: C7         RST         0X00
57A0: 05         DEC         B
57A1: C7         RST         0X00
57A2: 22         LD           (HLI),A
57A3: A6         AND         (HL)
57A4: 24         INC         H
57A5: A6         AND         (HL)
57A6: 43         LD           B,E
57A7: A6         AND         (HL)
57A8: 45         LD           B,L
57A9: A6         AND         (HL)
57AA: C4 17 0F   CALL       NZ,$0F17
57AD: FE 04      CP           $04
57AF: 0D         DEC         C
57B0: 74         LD           (HL),H
57B1: F1         POP         AF
57B2: 84         ADD         A,H
57B3: 13         INC         DE
57B4: 0F         RRCA
57B5: 84         ADD         A,H
57B6: 23         INC         HL
57B7: 0F         RRCA
57B8: 84         ADD         A,H
57B9: 33         INC         SP
57BA: 0F         RRCA
57BB: 82         ADD         A,D
57BC: 54         LD           D,H
57BD: 0F         RRCA
57BE: 82         ADD         A,D
57BF: 64         LD           H,H
57C0: 0F         RRCA
57C1: 02         LD           (BC),A
57C2: 26 03      LD           H,$03
57C4: 2A         LD           A,(HLI)
57C5: 06 29      LD           B,$29
57C7: 07         RLCA
57C8: 25         DEC         H
57C9: C3 12 24   JP           $2412
57CC: 42         LD           B,D
57CD: 2A         LD           A,(HLI)
57CE: 84         ADD         A,H
57CF: 43         LD           B,E
57D0: 21 82 44   LD           HL,$4482
57D3: 97         SUB         A
57D4: 47         LD           B,A
57D5: 29         ADD         HL,HL
57D6: C3 17 23   JP           $2317
57D9: 13         INC         DE
57DA: C0         RET         NZ
57DB: 16 C0      LD           D,$C0
57DD: 33         INC         SP
57DE: C0         RET         NZ
57DF: 36 C0      LD           (HL),$C0
57E1: 11 AC 18   LD           DE,$18AC
57E4: AC         XOR         H
57E5: 61         LD           H,C
57E6: AC         XOR         H
57E7: 68         LD           L,B
57E8: AC         XOR         H
57E9: 73         LD           (HL),E
57EA: C8         RET         Z
57EB: 76         HALT
57EC: C8         RET         Z
57ED: E0 00      LDFF00   ($00),A
57EF: 2B         DEC         HL
57F0: 48         LD           C,B
57F1: 22         LD           (HLI),A
57F2: FE 0C      CP           $0C
57F4: 0D         DEC         C
57F5: 04         INC         B
57F6: F0 74      LD           A,($74)
57F8: F5         PUSH       AF
57F9: 02         LD           (BC),A
57FA: C7         RST         0X00
57FB: 07         RLCA
57FC: C7         RST         0X00
57FD: 20 C9      JR           NZ,$57C8
57FF: 82         ADD         A,D
5800: 61         LD           H,C
5801: 12         LD           (DE),A
5802: 63         LD           H,E
5803: 2C         INC         L
5804: 82         ADD         A,D
5805: 64         LD           H,H
5806: 22         LD           (HLI),A
5807: 66         LD           H,(HL)
5808: 2B         DEC         HL
5809: 73         LD           (HL),E
580A: 24         INC         H
580B: 82         ADD         A,D
580C: 74         LD           (HL),H
580D: 03         INC         BC
580E: 76         HALT
580F: 23         INC         HL
5810: 70         LD           (HL),B
5811: 23         INC         HL
5812: 82         ADD         A,D
5813: 71         LD           (HL),C
5814: 0D         DEC         C
5815: 82         ADD         A,D
5816: 77         LD           (HL),A
5817: 0D         DEC         C
5818: 79         LD           A,C
5819: 24         INC         H
581A: 22         LD           (HLI),A
581B: 8D         ADC         A,L
581C: 27         DAA
581D: 8D         ADC         A,L
581E: 42         LD           B,D
581F: 8D         ADC         A,L
5820: 47         LD           B,A
5821: 8D         ADC         A,L
5822: 35         DEC         (HL)
5823: 8D         ADC         A,L
5824: FE 0C      CP           $0C
5826: 0D         DEC         C
5827: 04         INC         B
5828: F0 74      LD           A,($74)
582A: F1         POP         AF
582B: 88         ADC         A,B
582C: 11 1B 88   LD           DE,$881B
582F: 21 1B 88   LD           HL,$881B
5832: 31 1B 88   LD           SP,$881B
5835: 41         LD           B,C
5836: 1B         DEC         DE
5837: 88         ADC         A,B
5838: 51         LD           D,C
5839: 1B         DEC         DE
583A: 88         ADC         A,B
583B: 61         LD           H,C
583C: 1B         DEC         DE
583D: 33         INC         SP
583E: 2C         INC         L
583F: 82         ADD         A,D
5840: 34         INC         (HL)
5841: 22         LD           (HLI),A
5842: 36 2B      LD           (HL),$2B
5844: 43         LD           B,E
5845: 2A         LD           A,(HLI)
5846: 82         ADD         A,D
5847: 44         LD           B,H
5848: 21 46 29   LD           HL,$2946
584B: FE 0C      CP           $0C
584D: 0E 74      LD           C,$74
584F: F5         PUSH       AF
5850: 03         INC         BC
5851: C7         RST         0X00
5852: 07         RLCA
5853: C7         RST         0X00
5854: C8         RET         Z
5855: 00         NOP
5856: 03         INC         BC
5857: 01 25 C6   LD           BC,$C625
585A: 11 23 71   LD           DE,$7123
585D: 27         DAA
585E: 83         ADD         A,E
585F: 14         INC         D
5860: 1B         DEC         DE
5861: 83         ADD         A,E
5862: 24         INC         H
5863: 1B         DEC         DE
5864: 83         ADD         A,E
5865: 34         INC         (HL)
5866: 1B         DEC         DE
5867: C4 45 1B   CALL       NZ,$1B45
586A: 25         DEC         H
586B: A0         AND         B
586C: 45         LD           B,L
586D: A9         XOR         C
586E: 74         LD           (HL),H
586F: 2B         DEC         HL
5870: 76         HALT
5871: 2C         INC         L
5872: 32         LD           (HLD),A
5873: 1B         DEC         DE
5874: FE 04      CP           $04
5876: 0D         DEC         C
5877: 04         INC         B
5878: F0 74      LD           A,($74)
587A: F5         PUSH       AF
587B: C8         RET         Z
587C: 00         NOP
587D: 03         INC         BC
587E: C8         RET         Z
587F: 01 03 C8   LD           BC,$C803
5882: 02         LD           (BC),A
5883: 03         INC         BC
5884: C8         RET         Z
5885: 07         RLCA
5886: 03         INC         BC
5887: C8         RET         Z
5888: 08 03 C8   LD           ($C803),SP
588B: 09         ADD         HL,BC
588C: 03         INC         BC
588D: 03         INC         BC
588E: 25         DEC         H
588F: 06 26      LD           B,$26
5891: 13         INC         DE
5892: 23         INC         HL
5893: 16 24      LD           D,$24
5895: 22         LD           (HLI),A
5896: 25         DEC         H
5897: 23         INC         HL
5898: 29         ADD         HL,HL
5899: 26 2A      LD           H,$2A
589B: 27         DAA
589C: 26 C3      LD           H,$C3
589E: 32         LD           (HLD),A
589F: 23         INC         HL
58A0: C3 37 24   JP           $2437
58A3: 62         LD           H,D
58A4: 27         DAA
58A5: 63         LD           H,E
58A6: 2B         DEC         HL
58A7: 66         LD           H,(HL)
58A8: 2C         INC         L
58A9: 67         LD           H,A
58AA: 28 73      JR           Z,$591F
58AC: 27         DAA
58AD: 76         HALT
58AE: 28 84      JR           Z,$5834
58B0: 33         INC         SP
58B1: 0F         RRCA
58B2: 84         ADD         A,H
58B3: 43         LD           B,E
58B4: 0F         RRCA
58B5: 84         ADD         A,H
58B6: 53         LD           D,E
58B7: 0F         RRCA
58B8: 33         INC         SP
58B9: AC         XOR         H
58BA: 36 AC      LD           (HL),$AC
58BC: 53         LD           D,E
58BD: AC         XOR         H
58BE: 56         LD           D,(HL)
58BF: AC         XOR         H
58C0: 44         LD           B,H
58C1: BE         CP           (HL)
58C2: E2         LDFF00   (C),A
58C3: 03         INC         BC
58C4: EF         RST         0X28
58C5: 18 10      JR           $58D7
58C7: FE 0C      CP           $0C
58C9: 0E 39      LD           C,$39
58CB: F7         RST         0X30
58CC: 76         HALT
58CD: F5         PUSH       AF
58CE: 02         LD           (BC),A
58CF: C7         RST         0X00
58D0: 07         RLCA
58D1: C7         RST         0X00
58D2: 83         ADD         A,E
58D3: 16 1B      LD           D,$1B
58D5: C2 27 1B   JP           NZ,$1B27
58D8: C2 28 1B   JP           NZ,$1B28
58DB: 83         ADD         A,E
58DC: 46         LD           B,(HL)
58DD: 1B         DEC         DE
58DE: 84         ADD         A,H
58DF: 54         LD           D,H
58E0: 1B         DEC         DE
58E1: 87         ADD         A,A
58E2: 61         LD           H,C
58E3: 1B         DEC         DE
58E4: C2 39 0D   JP           NZ,$0D39
58E7: C2 58 0D   JP           NZ,$0D58
58EA: 75         LD           (HL),L
58EB: 2B         DEC         HL
58EC: 76         HALT
58ED: 0D         DEC         C
58EE: 77         LD           (HL),A
58EF: 2C         INC         L
58F0: 29         ADD         HL,HL
58F1: 2A         LD           A,(HLI)
58F2: 59         LD           E,C
58F3: 2C         INC         L
58F4: 22         LD           (HLI),A
58F5: 8D         ADC         A,L
58F6: 27         DAA
58F7: 8D         ADC         A,L
58F8: 42         LD           B,D
58F9: 8D         ADC         A,L
58FA: 47         LD           B,A
58FB: 8D         ADC         A,L
58FC: 35         DEC         (HL)
58FD: 8D         ADC         A,L
58FE: 18 BF      JR           $58BF
5900: E2         LDFF00   (C),A
5901: 03         INC         BC
5902: 1F         RRA
5903: 88         ADC         A,B
5904: 10 FE      STOP       $FE
5906: 0C         INC         C
5907: 1D         DEC         E
5908: 04         INC         B
5909: F4                              
590A: 30 F6      JR           NC,$5902
590C: 59         LD           E,C
590D: F7         RST         0X30
590E: 10 C9      STOP       $C9
5910: 60         LD           H,B
5911: C9         RET
5912: 20 29      JR           NZ,$593D
5914: 50         LD           D,B
5915: 2B         DEC         HL
5916: C2 30 0D   JP           NZ,$0D30
5919: C4 03 24   CALL       NZ,$2403
591C: C5         PUSH       BC
591D: 06 23      LD           B,$23
591F: C4 04 03   CALL       NZ,$0304
5922: C5         PUSH       BC
5923: 05         DEC         B
5924: 03         INC         BC
5925: 43         LD           B,E
5926: 2A         LD           A,(HLI)
5927: 44         LD           B,H
5928: 26 54      LD           H,$54
592A: 2A         LD           A,(HLI)
592B: 55         LD           D,L
592C: 21 56 29   LD           HL,$2956
592F: 63         LD           H,E
5930: A7         AND         A
5931: 82         ADD         A,D
5932: 04         INC         B
5933: C0         RET         NZ
5934: 29         ADD         HL,HL
5935: CA 82 11   JP           Z,$1182
5938: 0F         RRCA
5939: 82         ADD         A,D
593A: 21 0F 82   LD           HL,$820F
593D: 31 0F 49   LD           SP,$490F
5940: 2A         LD           A,(HLI)
5941: 59         LD           E,C
5942: 0E 82      LD           C,$82
5944: 68         LD           L,B
5945: 0E 79      LD           C,$79
5947: 22         LD           (HLI),A
5948: 22         LD           (HLI),A
5949: A0         AND         B
594A: FE 0C      CP           $0C
594C: 8D         ADC         A,L
594D: 02         LD           (BC),A
594E: C7         RST         0X00
594F: 07         RLCA
5950: C7         RST         0X00
5951: 04         INC         B
5952: EC                              
5953: 74         LD           (HL),H
5954: F5         PUSH       AF
5955: 29         ADD         HL,HL
5956: F7         RST         0X30
5957: 50         LD           D,B
5958: F6 86      OR           $86
595A: 71         LD           (HL),C
595B: 0D         DEC         C
595C: C3 19 0D   JP           $0D19
595F: 22         LD           (HLI),A
5960: 13         INC         DE
5961: 27         DAA
5962: 13         INC         DE
5963: 42         LD           B,D
5964: 12         LD           (DE),A
5965: 47         LD           B,A
5966: 12         LD           (DE),A
5967: 31 10 36   LD           SP,$3610
596A: 10 33      STOP       $33
596C: 11 38 11   LD           DE,$1138
596F: 32         LD           (HLD),A
5970: 1C         INC         E
5971: 37         SCF
5972: 1C         INC         E
5973: 49         LD           C,C
5974: 2C         INC         L
5975: C2 59 24   JP           NZ,$2459
5978: 77         LD           (HL),A
5979: 2C         INC         L
597A: 78         LD           A,B
597B: 22         LD           (HLI),A
597C: 79         LD           A,C
597D: 28 20      JR           Z,$599F
597F: C9         RET
5980: 40         LD           B,B
5981: 29         ADD         HL,HL
5982: 82         ADD         A,D
5983: 50         LD           D,B
5984: 0E 82      LD           C,$82
5986: 60         LD           H,B
5987: 0E 70      LD           C,$70
5989: 2B         DEC         HL
598A: 58         LD           E,B
598B: 20 82      JR           NZ,$590F
598D: 67         LD           H,A
598E: 20 E2      JR           NZ,$5972
5990: 03         INC         BC
5991: 7C         LD           A,H
5992: 28 13      JR           Z,$59A7
5994: FE 0C      CP           $0C
5996: 7D         LD           A,L
5997: 40         LD           B,B
5998: F6 72      OR           $72
599A: F5         PUSH       AF
599B: 02         LD           (BC),A
599C: C7         RST         0X00
599D: 07         RLCA
599E: C7         RST         0X00
599F: 49         LD           C,C
59A0: CA C2 15   JP           Z,$15C2
59A3: A6         AND         (HL)
59A4: 83         ADD         A,E
59A5: 40         LD           B,B
59A6: 22         LD           (HLI),A
59A7: 43         LD           B,E
59A8: 2B         DEC         HL
59A9: C3 53 23   JP           $2353
59AC: 45         LD           B,L
59AD: A7         AND         A
59AE: 83         ADD         A,E
59AF: 46         LD           B,(HL)
59B0: A6         AND         (HL)
59B1: 50         LD           D,B
59B2: 17         RLA
59B3: 51         LD           D,C
59B4: A0         AND         B
59B5: 52         LD           D,D
59B6: 16 C3      LD           D,$C3
59B8: 53         LD           D,E
59B9: 23         INC         HL
59BA: 54         LD           D,H
59BB: A7         AND         A
59BC: 55         LD           D,L
59BD: DE 56      SBC         $56
59BF: A6         AND         (HL)
59C0: C2 60 11   JP           NZ,$1160
59C3: 71         LD           (HL),C
59C4: 0D         DEC         C
59C5: C2 62 10   JP           NZ,$1062
59C8: 83         ADD         A,E
59C9: 16 0F      LD           D,$0F
59CB: 83         ADD         A,E
59CC: 26 0F      LD           H,$0F
59CE: 83         ADD         A,E
59CF: 36 0F      LD           (HL),$0F
59D1: 27         DAA
59D2: BE         CP           (HL)
59D3: E2         LDFF00   (C),A
59D4: 03         INC         BC
59D5: 7D         LD           A,L
59D6: 88         ADC         A,B
59D7: 10 FE      STOP       $FE
59D9: 0C         INC         C
59DA: 3E 04      LD           A,$04
59DC: F4                              
59DD: 74         LD           (HL),H
59DE: F5         PUSH       AF
59DF: C4 00 03   CALL       NZ,$0300
59E2: 88         ADC         A,B
59E3: 71         LD           (HL),C
59E4: 0D         DEC         C
59E5: 01 25 03   LD           BC,$0325
59E8: C7         RST         0X00
59E9: 07         RLCA
59EA: C7         RST         0X00
59EB: 04         INC         B
59EC: 29         ADD         HL,HL
59ED: 06 2A      LD           B,$2A
59EF: C3 11 23   JP           $2311
59F2: 40         LD           B,B
59F3: 25         DEC         H
59F4: 41         LD           B,C
59F5: 29         ADD         HL,HL
59F6: 05         DEC         B
59F7: 1B         DEC         DE
59F8: 84         ADD         A,H
59F9: 15         DEC         D
59FA: 1B         DEC         DE
59FB: C2 27 1B   JP           NZ,$1B27
59FE: C2 28 1B   JP           NZ,$1B28
5A01: 83         ADD         A,E
5A02: 46         LD           B,(HL)
5A03: 1B         DEC         DE
5A04: 84         ADD         A,H
5A05: 54         LD           D,H
5A06: 1B         DEC         DE
5A07: 87         ADD         A,A
5A08: 61         LD           H,C
5A09: 1B         DEC         DE
5A0A: 87         ADD         A,A
5A0B: 71         LD           (HL),C
5A0C: 1B         DEC         DE
5A0D: C2 58 0D   JP           NZ,$0D58
5A10: C2 58 20   JP           NZ,$2058
5A13: FE 04      CP           $04
5A15: 0D         DEC         C
5A16: 02         LD           (BC),A
5A17: C7         RST         0X00
5A18: 04         INC         B
5A19: F8 07      LDHL       SP,$07
5A1B: C7         RST         0X00
5A1C: 29         ADD         HL,HL
5A1D: F7         RST         0X30
5A1E: 87         ADD         A,A
5A1F: 12         LD           (DE),A
5A20: B0         OR           B
5A21: 82         ADD         A,D
5A22: 14         INC         D
5A23: 0D         DEC         C
5A24: C6 11      ADD         $11
5A26: 01 86 62   LD           BC,$6286
5A29: AF         XOR         A
5A2A: 38 AF      JR           C,$59DB
5A2C: C2 48 01   JP           NZ,$0148
5A2F: 68         LD           L,B
5A30: B0         OR           B
5A31: 19         ADD         HL,DE
5A32: 2A         LD           A,(HLI)
5A33: 29         ADD         HL,HL
5A34: 0D         DEC         C
5A35: 39         ADD         HL,SP
5A36: 2C         INC         L
5A37: 49         LD           C,C
5A38: 24         INC         H
5A39: 59         LD           E,C
5A3A: 2A         LD           A,(HLI)
5A3B: 69         LD           L,C
5A3C: 0D         DEC         C
5A3D: 79         LD           A,C
5A3E: 22         LD           (HLI),A
5A3F: 22         LD           (HLI),A
5A40: A6         AND         (HL)
5A41: 27         DAA
5A42: A7         AND         A
5A43: 52         LD           D,D
5A44: A6         AND         (HL)
5A45: 57         LD           D,A
5A46: A6         AND         (HL)
5A47: 82         ADD         A,D
5A48: 54         LD           D,H
5A49: 20 FE      JR           NZ,$5A49
5A4B: 0C         INC         C
5A4C: 9D         SBC         L
5A4D: 05         DEC         B
5A4E: F4                              
5A4F: 30 F6      JR           NC,$5A47
5A51: 75         LD           (HL),L
5A52: F5         PUSH       AF
5A53: 84         ADD         A,H
5A54: 05         DEC         B
5A55: 21 88 71   LD           HL,$7188
5A58: 0D         DEC         C
5A59: C8         RET         Z
5A5A: 09         ADD         HL,BC
5A5B: 24         INC         H
5A5C: 00         NOP
5A5D: 25         DEC         H
5A5E: 01 21 02   LD           BC,$0221
5A61: 26 C4      LD           H,$C4
5A63: 03         INC         BC
5A64: 03         INC         BC
5A65: C5         PUSH       BC
5A66: 04         INC         B
5A67: 23         INC         HL
5A68: 10 29      STOP       $29
5A6A: C2 12 24   JP           NZ,$2412
5A6D: 82         ADD         A,D
5A6E: 30 22      JR           NC,$5A92
5A70: 32         LD           (HLD),A
5A71: 28 84      JR           Z,$59F7
5A73: 40         LD           B,B
5A74: 03         INC         BC
5A75: 84         ADD         A,H
5A76: 50         LD           D,B
5A77: 21 54 29   LD           HL,$2954
5A7A: 70         LD           (HL),B
5A7B: 2B         DEC         HL
5A7C: 04         INC         B
5A7D: 25         DEC         H
5A7E: 09         ADD         HL,BC
5A7F: 26 29      LD           H,$29
5A81: CA 59 CA   JP           Z,$CA59
5A84: 52         LD           D,D
5A85: C7         RST         0X00
5A86: 05         DEC         B
5A87: 29         ADD         HL,HL
5A88: 06 0D      LD           B,$0D
5A8A: 07         RLCA
5A8B: 2A         LD           A,(HLI)
5A8C: 83         ADD         A,E
5A8D: 25         DEC         H
5A8E: 0F         RRCA
5A8F: 83         ADD         A,E
5A90: 35         DEC         (HL)
5A91: 0F         RRCA
5A92: 83         ADD         A,E
5A93: 45         LD           B,L
5A94: 0F         RRCA
5A95: 36 A0      LD           (HL),$A0
5A97: 11 BE E2   LD           DE,$E2BE
5A9A: 03         INC         BC
5A9B: 5E         LD           E,(HL)
5A9C: 18 13      JR           $5AB1
5A9E: 15         DEC         D
5A9F: 20 82      JR           NZ,$5A23
5AA1: 17         RLA
5AA2: 20 FE      JR           NZ,$5AA2
5AA4: 0C         INC         C
5AA5: 2D         DEC         L
5AA6: 02         LD           (BC),A
5AA7: C7         RST         0X00
5AA8: 07         RLCA
5AA9: C7         RST         0X00
5AAA: 20 C9      JR           NZ,$5A75
5AAC: 50         LD           D,B
5AAD: C9         RET
5AAE: 71         LD           (HL),C
5AAF: F5         PUSH       AF
5AB0: 19         ADD         HL,DE
5AB1: F7         RST         0X30
5AB2: 14         INC         D
5AB3: A6         AND         (HL)
5AB4: 15         DEC         D
5AB5: 1B         DEC         DE
5AB6: 83         ADD         A,E
5AB7: 16 0E      LD           D,$0E
5AB9: C2 19 1B   JP           NZ,$1B19
5ABC: 21 A6 22   LD           HL,$22A6
5ABF: DE 23      SBC         $23
5AC1: A7         AND         A
5AC2: 82         ADD         A,D
5AC3: 24         INC         H
5AC4: 1B         DEC         DE
5AC5: 83         ADD         A,E
5AC6: 26 0E      LD           H,$0E
5AC8: 33         INC         SP
5AC9: 2C         INC         L
5ACA: 34         INC         (HL)
5ACB: 22         LD           (HLI),A
5ACC: 35         DEC         (HL)
5ACD: 2B         DEC         HL
5ACE: 36 A0      LD           (HL),$A0
5AD0: 83         ADD         A,E
5AD1: 37         SCF
5AD2: 0E C3      LD           C,$C3
5AD4: 43         LD           B,E
5AD5: 24         INC         H
5AD6: C4 44 03   CALL       NZ,$0344
5AD9: C4 45 23   CALL       NZ,$2345
5ADC: C2 46 1B   JP           NZ,$1B46
5ADF: 83         ADD         A,E
5AE0: 47         LD           B,A
5AE1: 0E 53      LD           C,$53
5AE3: CA 55 C9   JP           Z,$C955
5AE6: 83         ADD         A,E
5AE7: 57         LD           D,A
5AE8: 0E 84      LD           C,$84
5AEA: 66         LD           H,(HL)
5AEB: 0E 73      LD           C,$73
5AED: 28 84      JR           Z,$5A73
5AEF: 76         HALT
5AF0: 0E 79      LD           C,$79
5AF2: 0D         DEC         C
5AF3: 11 BE E2   LD           DE,$E2BE
5AF6: 03         INC         BC
5AF7: 5F         LD           E,A
5AF8: 88         ADC         A,B
5AF9: 10 FE      STOP       $FE
5AFB: 0C         INC         C
5AFC: 9D         SBC         L
5AFD: 07         RLCA
5AFE: F4                              
5AFF: 10 F6      STOP       $F6
5B01: 29         ADD         HL,HL
5B02: F7         RST         0X30
5B03: 75         LD           (HL),L
5B04: F5         PUSH       AF
5B05: 00         NOP
5B06: 29         ADD         HL,HL
5B07: C8         RET         Z
5B08: 07         RLCA
5B09: 24         INC         H
5B0A: 08 17 C7   LD           ($C717),SP
5B0D: 18 11      JR           $5B20
5B0F: 09         ADD         HL,BC
5B10: 12         LD           (DE),A
5B11: 19         ADD         HL,DE
5B12: 96         SUB         (HL)
5B13: C6 29      ADD         $29
5B15: 10 10      STOP       $10
5B17: 1B         DEC         DE
5B18: 87         ADD         A,A
5B19: 20 1B      JR           NZ,$5B36
5B1B: C4 30 0E   CALL       NZ,$0E30
5B1E: 31 0E C2   LD           SP,$C20E
5B21: 32         LD           (HLD),A
5B22: 1B         DEC         DE
5B23: C4 36 1B   CALL       NZ,$1B36
5B26: C4 41 1B   CALL       NZ,$1B41
5B29: C2 55 0E   JP           NZ,$0E55
5B2C: 82         ADD         A,D
5B2D: 75         LD           (HL),L
5B2E: 0E 27      LD           C,$27
5B30: CA 57 CA   JP           Z,$CA57
5B33: 84         ADD         A,H
5B34: 13         INC         DE
5B35: 1B         DEC         DE
5B36: 82         ADD         A,D
5B37: 24         INC         H
5B38: 0D         DEC         C
5B39: 82         ADD         A,D
5B3A: 33         INC         SP
5B3B: 1B         DEC         DE
5B3C: 35         DEC         (HL)
5B3D: 0D         DEC         C
5B3E: 82         ADD         A,D
5B3F: 44         LD           B,H
5B40: 1B         DEC         DE
5B41: 25         DEC         H
5B42: C0         RET         NZ
5B43: FE 0C      CP           $0C
5B45: 1D         DEC         E
5B46: 02         LD           (BC),A
5B47: F4                              
5B48: 10 F6      STOP       $F6
5B4A: 29         ADD         HL,HL
5B4B: F7         RST         0X30
5B4C: 73         LD           (HL),E
5B4D: F5         PUSH       AF
5B4E: 00         NOP
5B4F: 93         SUB         E
5B50: 02         LD           (BC),A
5B51: 10 C2      STOP       $C2
5B53: 03         INC         BC
5B54: 23         INC         HL
5B55: C2 09 24   JP           NZ,$2409
5B58: 10 13      STOP       $13
5B5A: 12         LD           (DE),A
5B5B: 14         INC         D
5B5C: 20 25      JR           NZ,$5B83
5B5E: 21 98 22   LD           HL,$2298
5B61: 21 23 29   LD           HL,$2923
5B64: 29         ADD         HL,HL
5B65: 2A         LD           A,(HLI)
5B66: 39         ADD         HL,SP
5B67: 0D         DEC         C
5B68: 49         LD           C,C
5B69: 2C         INC         L
5B6A: 50         LD           D,B
5B6B: C9         RET
5B6C: 59         LD           E,C
5B6D: CA 73 2B   JP           Z,$2B73
5B70: 85         ADD         A,L
5B71: 74         LD           (HL),H
5B72: 0D         DEC         C
5B73: 79         LD           A,C
5B74: 24         INC         H
5B75: 85         ADD         A,L
5B76: 24         INC         H
5B77: A6         AND         (HL)
5B78: 86         ADD         A,(HL)
5B79: 43         LD           B,E
5B7A: A6         AND         (HL)
5B7B: 25         DEC         H
5B7C: AF         XOR         A
5B7D: 35         DEC         (HL)
5B7E: 01 45 B0   LD           BC,$B045
5B81: 34         INC         (HL)
5B82: AE         XOR         (HL)
5B83: 36 AE      LD           (HL),$AE
5B85: 82         ADD         A,D
5B86: 41         LD           B,C
5B87: AF         XOR         A
5B88: 82         ADD         A,D
5B89: 51         LD           D,C
5B8A: 01 53 AF   LD           BC,$AF53
5B8D: 83         ADD         A,E
5B8E: 61         LD           H,C
5B8F: B0         OR           B
5B90: FE 0C      CP           $0C
5B92: 1E 04      LD           E,$04
5B94: F4                              
5B95: 30 F6      JR           NC,$5B8D
5B97: 10 C9      STOP       $C9
5B99: 50         LD           D,B
5B9A: C9         RET
5B9B: 20 29      JR           NZ,$5BC6
5B9D: 88         ADC         A,B
5B9E: 01 1B 86   LD           BC,$861B
5BA1: 11 1B 84   LD           DE,$841B
5BA4: 23         INC         HL
5BA5: 1B         DEC         DE
5BA6: 83         ADD         A,E
5BA7: 33         INC         SP
5BA8: 1B         DEC         DE
5BA9: 83         ADD         A,E
5BAA: 43         LD           B,E
5BAB: 1B         DEC         DE
5BAC: 82         ADD         A,D
5BAD: 52         LD           D,D
5BAE: 1B         DEC         DE
5BAF: 83         ADD         A,E
5BB0: 61         LD           H,C
5BB1: 1B         DEC         DE
5BB2: 37         SCF
5BB3: A0         AND         B
5BB4: 47         LD           B,A
5BB5: A7         AND         A
5BB6: 46         LD           B,(HL)
5BB7: A9         XOR         C
5BB8: 28 0E      JR           Z,$5BC8
5BBA: 57         LD           D,A
5BBB: 0E 82      LD           C,$82
5BBD: 65         LD           H,L
5BBE: 0E C2      LD           C,$C2
5BC0: 30 0D      JR           NC,$5BCF
5BC2: C4 21 0D   CALL       NZ,$0D21
5BC5: C4 12 0D   CALL       NZ,$0D12
5BC8: 40         LD           B,B
5BC9: 2B         DEC         HL
5BCA: C2 51 20   JP           NZ,$2051
5BCD: FE 0C      CP           $0C
5BCF: 9E         SBC         (HL)
5BD0: 04         INC         B
5BD1: F4                              
5BD2: 19         ADD         HL,DE
5BD3: F7         RST         0X30
5BD4: 73         LD           (HL),E
5BD5: F5         PUSH       AF
5BD6: C3 00 23   JP           $2300
5BD9: 88         ADC         A,B
5BDA: 01 0D C2   LD           BC,$C20D
5BDD: 09         ADD         HL,BC
5BDE: 24         INC         H
5BDF: 29         ADD         HL,HL
5BE0: 2A         LD           A,(HLI)
5BE1: C2 39 0D   JP           NZ,$0D39
5BE4: 30 27      JR           NC,$5C0D
5BE6: 84         ADD         A,H
5BE7: 31 22 35   LD           SP,$3522
5BEA: 2B         DEC         HL
5BEB: C3 45 23   JP           $2345
5BEE: 10 C9      STOP       $C9
5BF0: 32         LD           (HLD),A
5BF1: C8         RET         Z
5BF2: 40         LD           B,B
5BF3: 17         RLA
5BF4: 82         ADD         A,D
5BF5: 41         LD           B,C
5BF6: 12         LD           (DE),A
5BF7: C3 50 11   JP           $1150
5BFA: C4 44 10   CALL       NZ,$1044
5BFD: 83         ADD         A,E
5BFE: 51         LD           D,C
5BFF: 0F         RRCA
5C00: 83         ADD         A,E
5C01: 61         LD           H,C
5C02: 0F         RRCA
5C03: 83         ADD         A,E
5C04: 71         LD           (HL),C
5C05: 0F         RRCA
5C06: 75         LD           (HL),L
5C07: 27         DAA
5C08: 84         ADD         A,H
5C09: 76         HALT
5C0A: 22         LD           (HLI),A
5C0B: 77         LD           (HL),A
5C0C: C8         RET         Z
5C0D: C2 09 24   JP           NZ,$2409
5C10: 88         ADC         A,B
5C11: 11 1B 86   LD           DE,$861B
5C14: 21 1B 82   LD           HL,$821B
5C17: 27         DAA
5C18: 0E 29      LD           C,$29
5C1A: 2A         LD           A,(HLI)
5C1B: C4 36 1B   CALL       NZ,$1B36
5C1E: 83         ADD         A,E
5C1F: 37         SCF
5C20: 0E 83      LD           C,$83
5C22: 47         LD           B,A
5C23: 0E 83      LD           C,$83
5C25: 57         LD           D,A
5C26: 0E 83      LD           C,$83
5C28: 67         LD           H,A
5C29: 1B         DEC         DE
5C2A: 82         ADD         A,D
5C2B: 11 0D 82   LD           DE,$820D
5C2E: 21 0D 43   LD           HL,$430D
5C31: 0D         DEC         C
5C32: 62         LD           H,D
5C33: BE         CP           (HL)
5C34: E2         LDFF00   (C),A
5C35: 03         INC         BC
5C36: 1E 18      LD           E,$18
5C38: 10 C2      STOP       $C2
5C3A: 11 20 FE   LD           DE,$FE20
5C3D: 0C         INC         C
5C3E: 9E         SBC         (HL)
5C3F: 01 F0 10   LD           BC,$10F0
5C42: F6 59      OR           $59
5C44: F7         RST         0X30
5C45: 75         LD           (HL),L
5C46: F5         PUSH       AF
5C47: 00         NOP
5C48: 25         DEC         H
5C49: 03         INC         BC
5C4A: 26 C2      LD           H,$C2
5C4C: 04         INC         B
5C4D: 03         INC         BC
5C4E: C2 05 23   JP           NZ,$2305
5C51: 09         ADD         HL,BC
5C52: 0D         DEC         C
5C53: 10 23      STOP       $23
5C55: 82         ADD         A,D
5C56: 11 0D 13   LD           DE,$130D
5C59: 24         INC         H
5C5A: 20 29      JR           NZ,$5C85
5C5C: 23         INC         HL
5C5D: 2A         LD           A,(HLI)
5C5E: 24         INC         H
5C5F: 21 25 29   LD           HL,$2925
5C62: 26 1B      LD           H,$1B
5C64: 84         ADD         A,H
5C65: 34         INC         (HL)
5C66: 1B         DEC         DE
5C67: 86         ADD         A,(HL)
5C68: 44         LD           B,H
5C69: 1B         DEC         DE
5C6A: 82         ADD         A,D
5C6B: 53         LD           D,E
5C6C: 1B         DEC         DE
5C6D: 55         LD           D,L
5C6E: 2C         INC         L
5C6F: 84         ADD         A,H
5C70: 56         LD           D,(HL)
5C71: 22         LD           (HLI),A
5C72: 57         LD           D,A
5C73: C8         RET         Z
5C74: 85         ADD         A,L
5C75: 60         LD           H,B
5C76: 1B         DEC         DE
5C77: 65         LD           H,L
5C78: 24         INC         H
5C79: 66         LD           H,(HL)
5C7A: 17         RLA
5C7B: 83         ADD         A,E
5C7C: 67         LD           H,A
5C7D: 12         LD           (DE),A
5C7E: 85         ADD         A,L
5C7F: 70         LD           (HL),B
5C80: 22         LD           (HLI),A
5C81: 75         LD           (HL),L
5C82: 28 76      JR           Z,$5CFA
5C84: 11 83 77   LD           DE,$7783
5C87: 0D         DEC         C
5C88: 12         LD           (DE),A
5C89: AA         XOR         D
5C8A: FE 0C      CP           $0C
5C8C: 9D         SBC         L
5C8D: 05         DEC         B
5C8E: F4                              
5C8F: 10 F6      STOP       $F6
5C91: 74         LD           (HL),H
5C92: F5         PUSH       AF
5C93: 82         ADD         A,D
5C94: 05         DEC         B
5C95: 0E C5      LD           C,$C5
5C97: 07         RLCA
5C98: 24         INC         H
5C99: C6 08      ADD         $08
5C9B: 11 C8 09   LD           DE,$09C8
5C9E: 10 83      STOP       $83
5CA0: 10 0E      STOP       $0E
5CA2: 16 0E      LD           D,$0E
5CA4: 87         ADD         A,A
5CA5: 20 0E      JR           NZ,$5CB5
5CA7: 85         ADD         A,L
5CA8: 30 0E      JR           NC,$5CB8
5CAA: 82         ADD         A,D
5CAB: 35         DEC         (HL)
5CAC: 1B         DEC         DE
5CAD: 87         ADD         A,A
5CAE: 40         LD           B,B
5CAF: 1B         DEC         DE
5CB0: 42         LD           B,D
5CB1: 0E 27      LD           C,$27
5CB3: CA 87 50   JP           Z,$5087
5CB6: 22         LD           (HLI),A
5CB7: 52         LD           D,D
5CB8: C8         RET         Z
5CB9: 57         LD           D,A
5CBA: 28 88      JR           Z,$5C44
5CBC: 60         LD           H,B
5CBD: 12         LD           (DE),A
5CBE: 68         LD           L,B
5CBF: 93         SUB         E
5CC0: 89         ADC         A,C
5CC1: 70         LD           (HL),B
5CC2: 0D         DEC         C
5CC3: FE 0C      CP           $0C
5CC5: 0D         DEC         C
5CC6: 04         INC         B
5CC7: F4                              
5CC8: 76         HALT
5CC9: ED                              
5CCA: 20 C9      JR           NZ,$5C95
5CCC: 50         LD           D,B
5CCD: C9         RET
5CCE: 29         ADD         HL,HL
5CCF: CA 59 CA   JP           Z,$CA59
5CD2: 03         INC         BC
5CD3: 29         ADD         HL,HL
5CD4: 04         INC         B
5CD5: 0D         DEC         C
5CD6: 05         DEC         B
5CD7: 2A         LD           A,(HLI)
5CD8: 09         ADD         HL,BC
5CD9: 24         INC         H
5CDA: 85         ADD         A,L
5CDB: 11 0E C2   LD           DE,$C20E
5CDE: 18 1B      JR           $5CFB
5CE0: C3 21 0F   JP           $0F21
5CE3: 85         ADD         A,L
5CE4: 22         LD           (HLI),A
5CE5: 0E 32      LD           C,$32
5CE7: A0         AND         B
5CE8: 84         ADD         A,H
5CE9: 33         INC         SP
5CEA: 0E 82      LD           C,$82
5CEC: 37         SCF
5CED: 1B         DEC         DE
5CEE: 42         LD           B,D
5CEF: 0F         RRCA
5CF0: 84         ADD         A,H
5CF1: 43         LD           B,E
5CF2: 0E 82      LD           C,$82
5CF4: 47         LD           B,A
5CF5: 1B         DEC         DE
5CF6: 85         ADD         A,L
5CF7: 51         LD           D,C
5CF8: 0E 83      LD           C,$83
5CFA: 56         LD           D,(HL)
5CFB: 1B         DEC         DE
5CFC: 84         ADD         A,H
5CFD: 61         LD           H,C
5CFE: 0E 84      LD           C,$84
5D00: 65         LD           H,L
5D01: 1B         DEC         DE
5D02: 09         ADD         HL,BC
5D03: 26 82      LD           H,$82
5D05: 14         INC         D
5D06: 0D         DEC         C
5D07: 84         ADD         A,H
5D08: 05         DEC         B
5D09: 0D         DEC         C
5D0A: 09         ADD         HL,BC
5D0B: 24         INC         H
5D0C: 21 20 FE   LD           HL,$FE20
5D0F: 0C         INC         C
5D10: 2D         DEC         L
5D11: 03         INC         BC
5D12: F4                              
5D13: 10 F7      STOP       $F7
5D15: C3 00 11   JP           $1100
5D18: 83         ADD         A,E
5D19: 01 0F 83   LD           BC,$830F
5D1C: 11 0F 83   LD           DE,$830F
5D1F: 21 0F C3   LD           HL,$C30F
5D22: 04         INC         B
5D23: 10 85      STOP       $85
5D25: 05         DEC         B
5D26: 12         LD           (DE),A
5D27: 30 15      JR           NC,$5D3E
5D29: 83         ADD         A,E
5D2A: 31 13 34   LD           SP,$3413
5D2D: 14         INC         D
5D2E: 85         ADD         A,L
5D2F: 15         DEC         D
5D30: 13         INC         DE
5D31: 40         LD           B,B
5D32: 25         DEC         H
5D33: 84         ADD         A,H
5D34: 41         LD           B,C
5D35: 21 45 29   LD           HL,$2945
5D38: 25         DEC         H
5D39: 25         DEC         H
5D3A: 84         ADD         A,H
5D3B: 26 21      LD           H,$21
5D3D: 35         DEC         (HL)
5D3E: 23         INC         HL
5D3F: 27         DAA
5D40: C7         RST         0X00
5D41: 42         LD           B,D
5D42: C7         RST         0X00
5D43: 84         ADD         A,H
5D44: 36 1B      LD           (HL),$1B
5D46: 85         ADD         A,L
5D47: 51         LD           D,C
5D48: 1B         DEC         DE
5D49: 84         ADD         A,H
5D4A: 46         LD           B,(HL)
5D4B: 1B         DEC         DE
5D4C: 84         ADD         A,H
5D4D: 56         LD           D,(HL)
5D4E: 1B         DEC         DE
5D4F: 89         ADC         A,C
5D50: 61         LD           H,C
5D51: 1B         DEC         DE
5D52: 12         LD           (DE),A
5D53: A0         AND         B
5D54: 48         LD           C,B
5D55: A6         AND         (HL)
5D56: 82         ADD         A,D
5D57: 46         LD           B,(HL)
5D58: 0E 86      LD           C,$86
5D5A: 52         LD           D,D
5D5B: 0E 83      LD           C,$83
5D5D: 63         LD           H,E
5D5E: 0E C2      LD           C,$C2
5D60: 51         LD           D,C
5D61: 20 FE      JR           NZ,$5D61
5D63: 0C         INC         C
5D64: 0D         DEC         C
5D65: 04         INC         B
5D66: F4                              
5D67: 30 F6      JR           NC,$5D5F
5D69: 74         LD           (HL),H
5D6A: F5         PUSH       AF
5D6B: 8A         ADC         A,D
5D6C: 00         NOP
5D6D: 0D         DEC         C
5D6E: 86         ADD         A,(HL)
5D6F: 00         NOP
5D70: 12         LD           (DE),A
5D71: 06 93      LD           B,$93
5D73: 83         ADD         A,E
5D74: 07         RLCA
5D75: 0D         DEC         C
5D76: 8A         ADC         A,D
5D77: 10 13      STOP       $13
5D79: 15         DEC         D
5D7A: 0D         DEC         C
5D7B: 89         ADC         A,C
5D7C: 20 21      JR           NZ,$5D9F
5D7E: 22         LD           (HLI),A
5D7F: C7         RST         0X00
5D80: 27         DAA
5D81: C7         RST         0X00
5D82: 25         DEC         H
5D83: 98         SBC         B
5D84: 29         ADD         HL,HL
5D85: 26 89      LD           H,$89
5D87: 30 1B      JR           NC,$5DA4
5D89: 35         DEC         (HL)
5D8A: 1B         DEC         DE
5D8B: C4 39 24   CALL       NZ,$2439
5D8E: 89         ADC         A,C
5D8F: 40         LD           B,B
5D90: 1B         DEC         DE
5D91: 89         ADC         A,C
5D92: 50         LD           D,B
5D93: 1B         DEC         DE
5D94: 89         ADC         A,C
5D95: 60         LD           H,B
5D96: 1B         DEC         DE
5D97: 41         LD           B,C
5D98: A6         AND         (HL)
5D99: 44         LD           B,H
5D9A: A6         AND         (HL)
5D9B: 47         LD           B,A
5D9C: A6         AND         (HL)
5D9D: 89         ADC         A,C
5D9E: 70         LD           (HL),B
5D9F: 22         LD           (HLI),A
5DA0: 73         LD           (HL),E
5DA1: 2B         DEC         HL
5DA2: 82         ADD         A,D
5DA3: 74         LD           (HL),H
5DA4: 1B         DEC         DE
5DA5: 76         HALT
5DA6: 2C         INC         L
5DA7: 79         LD           A,C
5DA8: 28 49      JR           Z,$5DF3
5DAA: F3         DI
5DAB: FE 0C      CP           $0C
5DAD: 0D         DEC         C
5DAE: 04         INC         B
5DAF: F4                              
5DB0: 40         LD           B,B
5DB1: F2                              
5DB2: 59         LD           E,C
5DB3: EF         RST         0X28
5DB4: 74         LD           (HL),H
5DB5: F1         POP         AF
5DB6: 8A         ADC         A,D
5DB7: 00         NOP
5DB8: 0D         DEC         C
5DB9: 09         ADD         HL,BC
5DBA: 94         SUB         H
5DBB: 8A         ADC         A,D
5DBC: 10 13      STOP       $13
5DBE: 20 25      JR           NZ,$5DE5
5DC0: 88         ADC         A,B
5DC1: 21 21 29   LD           HL,$2921
5DC4: 26 22      LD           H,$22
5DC6: C7         RST         0X00
5DC7: 27         DAA
5DC8: C7         RST         0X00
5DC9: 84         ADD         A,H
5DCA: 31 1B 83   LD           SP,$831B
5DCD: 35         DEC         (HL)
5DCE: 0F         RRCA
5DCF: 85         ADD         A,L
5DD0: 41         LD           B,C
5DD1: 1B         DEC         DE
5DD2: 86         ADD         A,(HL)
5DD3: 51         LD           D,C
5DD4: 1B         DEC         DE
5DD5: 88         ADC         A,B
5DD6: 61         LD           H,C
5DD7: 1B         DEC         DE
5DD8: C2 47 0F   JP           NZ,$0F47
5DDB: 55         LD           D,L
5DDC: 0F         RRCA
5DDD: 43         LD           B,E
5DDE: A6         AND         (HL)
5DDF: 46         LD           B,(HL)
5DE0: A0         AND         B
5DE1: FE 0C      CP           $0C
5DE3: 0D         DEC         C
5DE4: 05         DEC         B
5DE5: C7         RST         0X00
5DE6: 06 EC      LD           B,$EC
5DE8: 08 C7 49   LD           ($49C7),SP
5DEB: CA 50 EE   JP           Z,$EE50
5DEE: 82         ADD         A,D
5DEF: 00         NOP
5DF0: 12         LD           (DE),A
5DF1: 02         LD           (BC),A
5DF2: 16 03      LD           D,$03
5DF4: 25         DEC         H
5DF5: 10 13      STOP       $13
5DF7: 12         LD           (DE),A
5DF8: 14         INC         D
5DF9: 13         INC         DE
5DFA: 23         INC         HL
5DFB: C3 14 0F   JP           $0F14
5DFE: C3 15 C0   JP           $C015
5E01: 83         ADD         A,E
5E02: 16 1B      LD           D,$1B
5E04: 20 25      JR           NZ,$5E2B
5E06: 21 98 22   LD           HL,$2298
5E09: 21 23 29   LD           HL,$2923
5E0C: 24         INC         H
5E0D: A0         AND         B
5E0E: 83         ADD         A,E
5E0F: 26 1B      LD           H,$1B
5E11: 33         INC         SP
5E12: 0E 83      LD           C,$83
5E14: 36 0E      LD           (HL),$0E
5E16: 84         ADD         A,H
5E17: 41         LD           B,C
5E18: C0         RET         NZ
5E19: 83         ADD         A,E
5E1A: 45         LD           B,L
5E1B: 0E C2      LD           C,$C2
5E1D: 48         LD           C,B
5E1E: 1B         DEC         DE
5E1F: 52         LD           D,D
5E20: 1B         DEC         DE
5E21: 85         ADD         A,L
5E22: 53         LD           D,E
5E23: 0E 87      LD           C,$87
5E25: 62         LD           H,D
5E26: 1B         DEC         DE
5E27: 64         LD           H,H
5E28: 0E 84      LD           C,$84
5E2A: 31 0F FE   LD           SP,$FE0F
5E2D: 0C         INC         C
5E2E: 0D         DEC         C
5E2F: 04         INC         B
5E30: F4                              
5E31: 02         LD           (BC),A
5E32: C7         RST         0X00
5E33: 07         RLCA
5E34: C7         RST         0X00
5E35: 03         INC         BC
5E36: 29         ADD         HL,HL
5E37: 82         ADD         A,D
5E38: 04         INC         B
5E39: 1B         DEC         DE
5E3A: 06 2A      LD           B,$2A
5E3C: 88         ADC         A,B
5E3D: 11 1B 82   LD           DE,$821B
5E40: 14         INC         D
5E41: 1B         DEC         DE
5E42: 88         ADC         A,B
5E43: 21 1B 88   LD           HL,$881B
5E46: 31 1B 88   LD           SP,$881B
5E49: 41         LD           B,C
5E4A: 1B         DEC         DE
5E4B: 88         ADC         A,B
5E4C: 51         LD           D,C
5E4D: 1B         DEC         DE
5E4E: 88         ADC         A,B
5E4F: 61         LD           H,C
5E50: 1B         DEC         DE
5E51: C2 23 C0   JP           NZ,$C023
5E54: C2 26 C0   JP           NZ,$C026
5E57: 84         ADD         A,H
5E58: 43         LD           B,E
5E59: 0D         DEC         C
5E5A: 86         ADD         A,(HL)
5E5B: 52         LD           D,D
5E5C: 0D         DEC         C
5E5D: 86         ADD         A,(HL)
5E5E: 62         LD           H,D
5E5F: 0D         DEC         C
5E60: 53         LD           D,E
5E61: FC                              
5E62: E0 00      LDFF00   ($00),A
5E64: 2B         DEC         HL
5E65: 48         LD           C,B
5E66: 22         LD           (HLI),A
5E67: FE 0C      CP           $0C
5E69: 0D         DEC         C
5E6A: 04         INC         B
5E6B: F0 03      LD           A,($03)
5E6D: C7         RST         0X00
5E6E: 06 C7      LD           B,$C7
5E70: 88         ADC         A,B
5E71: 11 1B 88   LD           DE,$881B
5E74: 21 1B 88   LD           HL,$881B
5E77: 31 1B 88   LD           SP,$881B
5E7A: 41         LD           B,C
5E7B: 1B         DEC         DE
5E7C: 88         ADC         A,B
5E7D: 51         LD           D,C
5E7E: 1B         DEC         DE
5E7F: 88         ADC         A,B
5E80: 61         LD           H,C
5E81: 1B         DEC         DE
5E82: 84         ADD         A,H
5E83: 23         INC         HL
5E84: 0E C2      LD           C,$C2
5E86: 33         INC         SP
5E87: C0         RET         NZ
5E88: 82         ADD         A,D
5E89: 34         INC         (HL)
5E8A: DD                              
5E8B: C2 36 C0   JP           NZ,$C036
5E8E: C3 37 DD   JP           $DD37
5E91: C2 38 0E   JP           NZ,$0E38
5E94: C3 42 0E   JP           $0E42
5E97: 85         ADD         A,L
5E98: 53         LD           D,E
5E99: DD                              
5E9A: 84         ADD         A,H
5E9B: 64         LD           H,H
5E9C: 0E 45      LD           C,$45
5E9E: 0D         DEC         C
5E9F: 44         LD           B,H
5EA0: A0         AND         B
5EA1: FE 05      CP           $05
5EA3: 94         SUB         H
5EA4: 83         ADD         A,E
5EA5: 02         LD           (BC),A
5EA6: 6B         LD           L,E
5EA7: 03         INC         BC
5EA8: 69         LD           L,C
5EA9: 83         ADD         A,E
5EAA: 12         LD           (DE),A
5EAB: 69         LD           L,C
5EAC: 13         INC         DE
5EAD: 82         ADD         A,D
5EAE: 83         ADD         A,E
5EAF: 06 6B      LD           B,$6B
5EB1: 07         RLCA
5EB2: 69         LD           L,C
5EB3: 83         ADD         A,E
5EB4: 16 69      LD           D,$69
5EB6: 17         RLA
5EB7: 82         ADD         A,D
5EB8: C3 00 6C   JP           $6C00
5EBB: 8A         ADC         A,D
5EBC: 30 6D      JR           NC,$5F2B
5EBE: 82         ADD         A,D
5EBF: 33         INC         SP
5EC0: 04         INC         B
5EC1: 37         SCF
5EC2: 62         LD           H,D
5EC3: 47         LD           B,A
5EC4: 63         LD           H,E
5EC5: C4 40 57   CALL       NZ,$5740
5EC8: 87         ADD         A,A
5EC9: 51         LD           D,C
5ECA: 80         ADD         A,B
5ECB: 87         ADD         A,A
5ECC: 61         LD           H,C
5ECD: 81         ADD         A,C
5ECE: 87         ADD         A,A
5ECF: 71         LD           (HL),C
5ED0: 53         LD           D,E
5ED1: C2 57 67   JP           NZ,$6757
5ED4: C3 48 51   JP           $5148
5ED7: C3 49 54   JP           $5449
5EDA: 82         ADD         A,D
5EDB: 78         LD           A,B
5EDC: 54         LD           D,H
5EDD: FE 05      CP           $05
5EDF: 94         SUB         H
5EE0: 83         ADD         A,E
5EE1: 03         INC         BC
5EE2: 6B         LD           L,E
5EE3: 04         INC         B
5EE4: 69         LD           L,C
5EE5: 83         ADD         A,E
5EE6: 13         INC         DE
5EE7: 69         LD           L,C
5EE8: 14         INC         D
5EE9: 82         ADD         A,D
5EEA: C3 08 65   JP           $6508
5EED: C3 09 6C   JP           $6C09
5EF0: 30 6D      JR           NC,$5F5F
5EF2: 31 64 C2   LD           SP,$C264
5EF5: 41         LD           B,C
5EF6: 65         LD           H,L
5EF7: 83         ADD         A,E
5EF8: 37         SCF
5EF9: 6D         LD           L,L
5EFA: C3 40 57   JP           $5740
5EFD: 83         ADD         A,E
5EFE: 61         LD           H,C
5EFF: 5B         LD           E,E
5F00: 84         ADD         A,H
5F01: 64         LD           H,H
5F02: 4C         LD           C,H
5F03: C3 48 51   JP           $5148
5F06: C3 49 54   JP           $5449
5F09: 8A         ADC         A,D
5F0A: 70         LD           (HL),B
5F0B: 54         LD           D,H
5F0C: E1         POP         HL
5F0D: 03         INC         BC
5F0E: 6A         LD           L,D
5F0F: 78         LD           A,B
5F10: 30 FE      JR           NC,$5F10
5F12: 0C         INC         C
5F13: 0D         DEC         C
5F14: FE 0C      CP           $0C
5F16: 0D         DEC         C
5F17: 39         ADD         HL,SP
5F18: F3         DI
5F19: 86         ADD         A,(HL)
5F1A: 22         LD           (HLI),A
5F1B: 0F         RRCA
5F1C: 86         ADD         A,(HL)
5F1D: 32         LD           (HLD),A
5F1E: 0F         RRCA
5F1F: 86         ADD         A,(HL)
5F20: 42         LD           B,D
5F21: 0F         RRCA
5F22: 33         INC         SP
5F23: 0D         DEC         C
5F24: 36 0D      LD           (HL),$0D
5F26: 53         LD           D,E
5F27: 0F         RRCA
5F28: 56         LD           D,(HL)
5F29: 0F         RRCA
5F2A: 11 A6 18   LD           DE,$18A6
5F2D: A6         AND         (HL)
5F2E: 61         LD           H,C
5F2F: A6         AND         (HL)
5F30: 68         LD           L,B
5F31: A6         AND         (HL)
5F32: FE 0C      CP           $0C
5F34: 0D         DEC         C
5F35: 30 F6      JR           NC,$5F2D
5F37: 84         ADD         A,H
5F38: 23         INC         HL
5F39: DD                              
5F3A: 86         ADD         A,(HL)
5F3B: 32         LD           (HLD),A
5F3C: DD                              
5F3D: 86         ADD         A,(HL)
5F3E: 42         LD           B,D
5F3F: DD                              
5F40: 84         ADD         A,H
5F41: 53         LD           D,E
5F42: DD                              
5F43: 33         INC         SP
5F44: A7         AND         A
5F45: 36 A7      LD           (HL),$A7
5F47: 44         LD           B,H
5F48: A6         AND         (HL)
5F49: 45         LD           B,L
5F4A: A6         AND         (HL)
5F4B: 48         LD           C,B
5F4C: DD                              
5F4D: 66         LD           H,(HL)
5F4E: DD                              
5F4F: 68         LD           L,B
5F50: BE         CP           (HL)
5F51: E2         LDFF00   (C),A
5F52: 04         INC         B
5F53: A8         XOR         B
5F54: 18 13      JR           $5F69
5F56: FE 0C      CP           $0C
5F58: 0D         DEC         C
5F59: 74         LD           (HL),H
5F5A: F1         POP         AF
5F5B: 84         ADD         A,H
5F5C: 13         INC         DE
5F5D: 0F         RRCA
5F5E: 84         ADD         A,H
5F5F: 23         INC         HL
5F60: 0F         RRCA
5F61: 84         ADD         A,H
5F62: 33         INC         SP
5F63: 0F         RRCA
5F64: 82         ADD         A,D
5F65: 54         LD           D,H
5F66: 0F         RRCA
5F67: 82         ADD         A,D
5F68: 64         LD           H,H
5F69: 0F         RRCA
5F6A: 02         LD           (BC),A
5F6B: 26 03      LD           H,$03
5F6D: 2A         LD           A,(HLI)
5F6E: 06 29      LD           B,$29
5F70: 07         RLCA
5F71: 25         DEC         H
5F72: C3 12 24   JP           $2412
5F75: 42         LD           B,D
5F76: 2A         LD           A,(HLI)
5F77: 84         ADD         A,H
5F78: 43         LD           B,E
5F79: 21 82 44   LD           HL,$4482
5F7C: 97         SUB         A
5F7D: 47         LD           B,A
5F7E: 29         ADD         HL,HL
5F7F: C3 17 23   JP           $2317
5F82: 13         INC         DE
5F83: C0         RET         NZ
5F84: 16 C0      LD           D,$C0
5F86: 33         INC         SP
5F87: C0         RET         NZ
5F88: 36 C0      LD           (HL),$C0
5F8A: E0 00      LDFF00   ($00),A
5F8C: D9         RETI
5F8D: 58         LD           E,B
5F8E: 40         LD           B,B
5F8F: FE 0C      CP           $0C
5F91: 0D         DEC         C
5F92: 59         LD           E,C
5F93: F3         DI
5F94: C8         RET         Z
5F95: 00         NOP
5F96: 03         INC         BC
5F97: C8         RET         Z
5F98: 01 03 83   LD           BC,$8303
5F9B: 07         RLCA
5F9C: 03         INC         BC
5F9D: 83         ADD         A,E
5F9E: 17         RLA
5F9F: 03         INC         BC
5FA0: 83         ADD         A,E
5FA1: 27         DAA
5FA2: 03         INC         BC
5FA3: 83         ADD         A,E
5FA4: 37         SCF
5FA5: 03         INC         BC
5FA6: 02         LD           (BC),A
5FA7: 25         DEC         H
5FA8: 83         ADD         A,E
5FA9: 03         INC         BC
5FAA: 21 06 26   LD           HL,$2606
5FAD: C6 12      ADD         $12
5FAF: 23         INC         HL
5FB0: C3 16 24   JP           $2416
5FB3: 46         LD           B,(HL)
5FB4: 2A         LD           A,(HLI)
5FB5: 82         ADD         A,D
5FB6: 47         LD           B,A
5FB7: 21 49 26   LD           HL,$2649
5FBA: 72         LD           (HL),D
5FBB: 27         DAA
5FBC: 83         ADD         A,E
5FBD: 13         INC         DE
5FBE: 0F         RRCA
5FBF: 83         ADD         A,E
5FC0: 23         INC         HL
5FC1: 0F         RRCA
5FC2: 83         ADD         A,E
5FC3: 33         INC         SP
5FC4: 0F         RRCA
5FC5: 24         INC         H
5FC6: A0         AND         B
5FC7: C2 56 20   JP           NZ,$2056
5FCA: FE 0C      CP           $0C
5FCC: 0D         DEC         C
5FCD: 50         LD           D,B
5FCE: F2                              
5FCF: 74         LD           (HL),H
5FD0: F1         POP         AF
5FD1: 86         ADD         A,(HL)
5FD2: 22         LD           (HLI),A
5FD3: 0F         RRCA
5FD4: 86         ADD         A,(HL)
5FD5: 32         LD           (HLD),A
5FD6: 0F         RRCA
5FD7: 86         ADD         A,(HL)
5FD8: 42         LD           B,D
5FD9: 0F         RRCA
5FDA: 33         INC         SP
5FDB: 0D         DEC         C
5FDC: 36 0D      LD           (HL),$0D
5FDE: 53         LD           D,E
5FDF: 0F         RRCA
5FE0: 56         LD           D,(HL)
5FE1: 0F         RRCA
5FE2: 11 A6 18   LD           DE,$18A6
5FE5: A6         AND         (HL)
5FE6: 68         LD           L,B
5FE7: A6         AND         (HL)
5FE8: FE 0C      CP           $0C
5FEA: 0D         DEC         C
5FEB: 04         INC         B
5FEC: F0 74      LD           A,($74)
5FEE: F1         POP         AF
5FEF: 86         ADD         A,(HL)
5FF0: 22         LD           (HLI),A
5FF1: 0F         RRCA
5FF2: 86         ADD         A,(HL)
5FF3: 52         LD           D,D
5FF4: 0F         RRCA
5FF5: C2 32 0F   JP           NZ,$0F32
5FF8: C2 37 0F   JP           NZ,$0F37
5FFB: FE 0C      CP           $0C
5FFD: 0D         DEC         C
5FFE: 83         ADD         A,E
5FFF: 11 0F 83   LD           DE,$830F
6002: 21 0F 83   LD           HL,$830F
6005: 31 0F 22   LD           SP,$220F
6008: A0         AND         B
6009: 04         INC         B
600A: 26 05      LD           H,$05
600C: 25         DEC         H
600D: C2 14 24   JP           NZ,$2414
6010: C2 15 23   JP           NZ,$2315
6013: 34         INC         (HL)
6014: 2A         LD           A,(HLI)
6015: 35         DEC         (HL)
6016: 29         ADD         HL,HL
6017: 83         ADD         A,E
6018: 26 AF      LD           H,$AF
601A: 83         ADD         A,E
601B: 36 01      LD           (HL),$01
601D: 41         LD           B,C
601E: AF         XOR         A
601F: 43         LD           B,E
6020: AF         XOR         A
6021: 85         ADD         A,L
6022: 44         LD           B,H
6023: 01 C2 51   LD           BC,$51C2
6026: 01 86 53   LD           BC,$5386
6029: B0         OR           B
602A: 82         ADD         A,D
602B: 57         LD           D,A
602C: 01 67 9F   LD           BC,$9F67
602F: 68         LD           L,B
6030: B0         OR           B
6031: 18 BE      JR           $5FF1
6033: E2         LDFF00   (C),A
6034: 04         INC         B
6035: A2         AND         D
6036: 18 10      JR           $6048
6038: FE 0C      CP           $0C
603A: 0D         DEC         C
603B: 04         INC         B
603C: F0 39      LD           A,($39)
603E: F7         RST         0X30
603F: 71         LD           (HL),C
6040: F5         PUSH       AF
6041: 29         ADD         HL,HL
6042: 2A         LD           A,(HLI)
6043: 39         ADD         HL,SP
6044: 0D         DEC         C
6045: 49         LD           C,C
6046: 2C         INC         L
6047: 71         LD           (HL),C
6048: 2B         DEC         HL
6049: 72         LD           (HL),D
604A: 0D         DEC         C
604B: 73         LD           (HL),E
604C: 2C         INC         L
604D: 82         ADD         A,D
604E: 11 A6 82   LD           DE,$82A6
6051: 22         LD           (HLI),A
6052: A6         AND         (HL)
6053: 33         INC         SP
6054: A7         AND         A
6055: 82         ADD         A,D
6056: 44         LD           B,H
6057: A6         AND         (HL)
6058: 55         LD           D,L
6059: A7         AND         A
605A: 82         ADD         A,D
605B: 66         LD           H,(HL)
605C: A6         AND         (HL)
605D: 18 20      JR           $607F
605F: 21 20 34   LD           HL,$3420
6062: 20 56      JR           NZ,$60BA
6064: 20 61      JR           NZ,$60C7
6066: 20 68      JR           NZ,$60D0
6068: 20 FE      JR           NZ,$6068
606A: 0C         INC         C
606B: 3D         DEC         A
606C: 20 F6      JR           NZ,$6064
606E: 77         LD           (HL),A
606F: F5         PUSH       AF
6070: 82         ADD         A,D
6071: 77         LD           (HL),A
6072: 0D         DEC         C
6073: 30 0D      JR           NC,$6082
6075: 74         LD           (HL),H
6076: 0D         DEC         C
6077: 20 29      JR           NZ,$60A2
6079: 30 0D      JR           NC,$6088
607B: 40         LD           B,B
607C: 2B         DEC         HL
607D: 11 A6 84   LD           DE,$84A6
6080: 13         INC         DE
6081: B0         OR           B
6082: 82         ADD         A,D
6083: 17         RLA
6084: 0F         RRCA
6085: 84         ADD         A,H
6086: 23         INC         HL
6087: A6         AND         (HL)
6088: 27         DAA
6089: 0F         RRCA
608A: 37         SCF
608B: AF         XOR         A
608C: C5         PUSH       BC
608D: 36 A6      LD           (HL),$A6
608F: 38 01      JR           C,$6092
6091: 82         ADD         A,D
6092: 47         LD           B,A
6093: 01 82 57   LD           BC,$5782
6096: 01 82 67   LD           BC,$6782
6099: B0         OR           B
609A: 28 9E      JR           Z,$603A
609C: 82         ADD         A,D
609D: 74         LD           (HL),H
609E: 0D         DEC         C
609F: 18 A0      JR           $6041
60A1: 83         ADD         A,E
60A2: 62         LD           H,D
60A3: 20 FE      JR           NZ,$60A3
60A5: 04         INC         B
60A6: 0D         DEC         C
60A7: 59         LD           E,C
60A8: F3         DI
60A9: 82         ADD         A,D
60AA: 24         INC         H
60AB: C0         RET         NZ
60AC: 82         ADD         A,D
60AD: 54         LD           D,H
60AE: C0         RET         NZ
60AF: 41         LD           B,C
60B0: AC         XOR         H
60B1: 48         LD           C,B
60B2: AC         XOR         H
60B3: 11 BE E2   LD           DE,$E2BE
60B6: 04         INC         B
60B7: A6         AND         (HL)
60B8: 18 13      JR           $60CD
60BA: 82         ADD         A,D
60BB: 17         RLA
60BC: 20 28      JR           NZ,$60E6
60BE: 20 82      JR           NZ,$6042
60C0: 61         LD           H,C
60C1: 20 FE      JR           NZ,$60C1
60C3: 04         INC         B
60C4: 0D         DEC         C
60C5: 50         LD           D,B
60C6: F2                              
60C7: 59         LD           E,C
60C8: F3         DI
60C9: C4 00 03   CALL       NZ,$0300
60CC: C4 01 03   CALL       NZ,$0301
60CF: C4 09 03   CALL       NZ,$0309
60D2: 02         LD           (BC),A
60D3: 25         DEC         H
60D4: 08 26 40   LD           ($4026),SP
60D7: 25         DEC         H
60D8: 41         LD           B,C
60D9: 21 42 29   LD           HL,$2942
60DC: C3 12 23   JP           $2312
60DF: C3 18 24   JP           $2418
60E2: 48         LD           C,B
60E3: 2A         LD           A,(HLI)
60E4: 49         LD           C,C
60E5: 26 FE      LD           H,$FE
60E7: 0C         INC         C
60E8: 2D         DEC         L
60E9: 39         ADD         HL,SP
60EA: F7         RST         0X30
60EB: 04         INC         B
60EC: F8 50      LDHL       SP,$50
60EE: F6 82      OR           $82
60F0: 14         INC         D
60F1: 0F         RRCA
60F2: 20 27      JR           NZ,$611B
60F4: 87         ADD         A,A
60F5: 21 22 28   LD           HL,$2822
60F8: 2B         DEC         HL
60F9: 29         ADD         HL,HL
60FA: A6         AND         (HL)
60FB: 38 27      JR           C,$6124
60FD: 39         ADD         HL,SP
60FE: 22         LD           (HLI),A
60FF: 40         LD           B,B
6100: 25         DEC         H
6101: 85         ADD         A,L
6102: 41         LD           B,C
6103: 21 46 26   LD           HL,$2646
6106: 56         LD           D,(HL)
6107: 2A         LD           A,(HLI)
6108: 83         ADD         A,E
6109: 57         LD           D,A
610A: 21 88 30   LD           HL,$3088
610D: 03         INC         BC
610E: 83         ADD         A,E
610F: 47         LD           B,A
6110: 03         INC         BC
6111: FE 0C      CP           $0C
6113: 4D         LD           C,L
6114: 30 F6      JR           NC,$610C
6116: 20 A6      JR           NZ,$60BE
6118: 30 22      JR           NC,$613C
611A: 31 2B 40   LD           SP,$402B
611D: 03         INC         BC
611E: 41         LD           B,C
611F: 23         INC         HL
6120: 50         LD           D,B
6121: 21 51 29   LD           HL,$2951
6124: 84         ADD         A,H
6125: 12         LD           (DE),A
6126: 01 84 22   LD           BC,$2284
6129: 01 84 32   LD           BC,$3284
612C: 01 84 42   LD           BC,$4284
612F: 01 84 52   LD           BC,$5284
6132: B0         OR           B
6133: C2 27 A6   JP           NZ,$A627
6136: 82         ADD         A,D
6137: 46         LD           B,(HL)
6138: A6         AND         (HL)
6139: 48         LD           C,B
613A: DE 56      SBC         $56
613C: A6         AND         (HL)
613D: 57         LD           D,A
613E: BE         CP           (HL)
613F: E2         LDFF00   (C),A
6140: 04         INC         B
6141: A4         AND         H
6142: 18 10      JR           $6154
6144: 67         LD           H,A
6145: A7         AND         A
6146: FE 0C      CP           $0C
6148: 0D         DEC         C
6149: 01 F4 71   LD           BC,$71F4
614C: F5         PUSH       AF
614D: 01 29 02   LD           BC,$0229
6150: 0D         DEC         C
6151: 03         INC         BC
6152: 2A         LD           A,(HLI)
6153: 71         LD           (HL),C
6154: 2B         DEC         HL
6155: 72         LD           (HL),D
6156: 1B         DEC         DE
6157: 73         LD           (HL),E
6158: 2C         INC         L
6159: 05         DEC         B
615A: C7         RST         0X00
615B: 75         LD           (HL),L
615C: C8         RET         Z
615D: 40         LD           B,B
615E: C9         RET
615F: 49         LD           C,C
6160: CA 88 11   JP           Z,$1188
6163: 1B         DEC         DE
6164: 88         ADC         A,B
6165: 21 1B 88   LD           HL,$881B
6168: 31 1B 88   LD           SP,$881B
616B: 41         LD           B,C
616C: 1B         DEC         DE
616D: 88         ADC         A,B
616E: 51         LD           D,C
616F: 1B         DEC         DE
6170: 88         ADC         A,B
6171: 61         LD           H,C
6172: 1B         DEC         DE
6173: 83         ADD         A,E
6174: 34         INC         (HL)
6175: 0E 83      LD           C,$83
6177: 44         LD           B,H
6178: 0E 83      LD           C,$83
617A: 54         LD           D,H
617B: 0E E2      LD           C,$E2
617D: 04         INC         B
617E: A3         AND         E
617F: 48         LD           C,B
6180: 10 FE      STOP       $FE
6182: 0C         INC         C
6183: 1D         DEC         E
6184: 07         RLCA
6185: F4                              
6186: 19         ADD         HL,DE
6187: F7         RST         0X30
6188: 73         LD           (HL),E
6189: F5         PUSH       AF
618A: C5         PUSH       BC
618B: 06 A6      LD           B,$A6
618D: 82         ADD         A,D
618E: 07         RLCA
618F: 0F         RRCA
6190: 82         ADD         A,D
6191: 17         RLA
6192: 0F         RRCA
6193: 82         ADD         A,D
6194: 27         DAA
6195: 0F         RRCA
6196: 09         ADD         HL,BC
6197: 2A         LD           A,(HLI)
6198: 19         ADD         HL,DE
6199: 0D         DEC         C
619A: 29         ADD         HL,HL
619B: A6         AND         (HL)
619C: 17         RLA
619D: A0         AND         B
619E: 29         ADD         HL,HL
619F: A6         AND         (HL)
61A0: 38 2C      JR           C,$61CE
61A2: 48         LD           C,B
61A3: 2A         LD           A,(HLI)
61A4: 39         ADD         HL,SP
61A5: 22         LD           (HLI),A
61A6: 49         LD           C,C
61A7: 21 59 0D   LD           HL,$0D59
61AA: 37         SCF
61AB: AF         XOR         A
61AC: 47         LD           B,A
61AD: 01 57 B0   LD           BC,$B057
61B0: 82         ADD         A,D
61B1: 52         LD           D,D
61B2: A6         AND         (HL)
61B3: 63         LD           H,E
61B4: AF         XOR         A
61B5: 82         ADD         A,D
61B6: 64         LD           H,H
61B7: AE         XOR         (HL)
61B8: 66         LD           H,(HL)
61B9: AF         XOR         A
61BA: 68         LD           L,B
61BB: A6         AND         (HL)
61BC: 69         LD           L,C
61BD: 2C         INC         L
61BE: C2 21 DF   JP           NZ,$DF21
61C1: 35         DEC         (HL)
61C2: DF         RST         0X18
61C3: 73         LD           (HL),E
61C4: 2B         DEC         HL
61C5: 82         ADD         A,D
61C6: 74         LD           (HL),H
61C7: 0D         DEC         C
61C8: 76         HALT
61C9: 2C         INC         L
61CA: C2 13 20   JP           NZ,$2013
61CD: FE 0C      CP           $0C
61CF: 0D         DEC         C
61D0: 40         LD           B,B
61D1: F6 00      OR           $00
61D3: 21 10 0D   LD           HL,$0D10
61D6: 20 A6      JR           NZ,$617E
61D8: 30 2B      JR           NC,$6205
61DA: 40         LD           B,B
61DB: 29         ADD         HL,HL
61DC: 50         LD           D,B
61DD: 0D         DEC         C
61DE: 60         LD           H,B
61DF: 2B         DEC         HL
61E0: 84         ADD         A,H
61E1: 12         LD           (DE),A
61E2: 01 84 22   LD           BC,$2284
61E5: B0         OR           B
61E6: 82         ADD         A,D
61E7: 17         RLA
61E8: A6         AND         (HL)
61E9: 82         ADD         A,D
61EA: 27         DAA
61EB: 0F         RRCA
61EC: 82         ADD         A,D
61ED: 37         SCF
61EE: 0F         RRCA
61EF: 82         ADD         A,D
61F0: 47         LD           B,A
61F1: 0F         RRCA
61F2: 38 A0      JR           C,$6194
61F4: 86         ADD         A,(HL)
61F5: 31 A6 46   LD           SP,$46A6
61F8: A6         AND         (HL)
61F9: 83         ADD         A,E
61FA: 56         LD           D,(HL)
61FB: A6         AND         (HL)
61FC: 44         LD           B,H
61FD: DF         RST         0X18
61FE: 61         LD           H,C
61FF: DF         RST         0X18
6200: 67         LD           H,A
6201: DF         RST         0X18
6202: FE 0C      CP           $0C
6204: 0D         DEC         C
6205: 01 F4 39   LD           BC,$39F4
6208: F7         RST         0X30
6209: 22         LD           (HLI),A
620A: 4F         LD           C,A
620B: 27         DAA
620C: 4F         LD           C,A
620D: 52         LD           D,D
620E: 4F         LD           C,A
620F: 57         LD           D,A
6210: 4F         LD           C,A
6211: 34         INC         (HL)
6212: 4F         LD           C,A
6213: 45         LD           B,L
6214: 4F         LD           C,A
6215: 01 29 02   LD           BC,$0229
6218: 1B         DEC         DE
6219: 03         INC         BC
621A: 2A         LD           A,(HLI)
621B: 29         ADD         HL,HL
621C: 2A         LD           A,(HLI)
621D: C2 39 0D   JP           NZ,$0D39
6220: 59         LD           E,C
6221: 2C         INC         L
6222: 82         ADD         A,D
6223: 12         LD           (DE),A
6224: 1B         DEC         DE
6225: C4 23 1B   CALL       NZ,$1B23
6228: FE 0C      CP           $0C
622A: 93         SUB         E
622B: 04         INC         B
622C: F4                              
622D: 30 F6      JR           NC,$6225
622F: 49         LD           C,C
6230: F3         DI
6231: 73         LD           (HL),E
6232: F5         PUSH       AF
6233: C8         RET         Z
6234: 04         INC         B
6235: 0D         DEC         C
6236: C6 05      ADD         $05
6238: 0D         DEC         C
6239: 84         ADD         A,H
623A: 30 0D      JR           NC,$6249
623C: 89         ADC         A,C
623D: 40         LD           B,B
623E: 0D         DEC         C
623F: 84         ADD         A,H
6240: 55         LD           D,L
6241: 0D         DEC         C
6242: C3 53 0D   JP           $0D53
6245: 83         ADD         A,E
6246: 20 21      JR           NZ,$6269
6248: 23         INC         HL
6249: 29         ADD         HL,HL
624A: C2 03 23   JP           NZ,$2303
624D: C3 06 24   JP           $2406
6250: 36 2A      LD           (HL),$2A
6252: 83         ADD         A,E
6253: 37         SCF
6254: 21 82 50   LD           HL,$5082
6257: 22         LD           (HLI),A
6258: 52         LD           D,D
6259: 2B         DEC         HL
625A: C2 62 23   JP           NZ,$2362
625D: 65         LD           H,L
625E: 2C         INC         L
625F: 75         LD           (HL),L
6260: 24         INC         H
6261: 83         ADD         A,E
6262: 66         LD           H,(HL)
6263: 22         LD           (HLI),A
6264: 69         LD           L,C
6265: 28 39      JR           Z,$62A0
6267: 26 83      LD           H,$83
6269: 33         INC         SP
626A: 0F         RRCA
626B: 83         ADD         A,E
626C: 43         LD           B,E
626D: 0F         RRCA
626E: 83         ADD         A,E
626F: 53         LD           D,E
6270: 0F         RRCA
6271: 33         INC         SP
6272: A6         AND         (HL)
6273: 35         DEC         (HL)
6274: A6         AND         (HL)
6275: 53         LD           D,E
6276: A6         AND         (HL)
6277: 55         LD           D,L
6278: A6         AND         (HL)
6279: 44         LD           B,H
627A: A7         AND         A
627B: 25         DEC         H
627C: AA         XOR         D
627D: FE 0C      CP           $0C
627F: 0D         DEC         C
6280: 40         LD           B,B
6281: F2                              
6282: 86         ADD         A,(HL)
6283: 22         LD           (HLI),A
6284: 0F         RRCA
6285: 86         ADD         A,(HL)
6286: 32         LD           (HLD),A
6287: 0F         RRCA
6288: 86         ADD         A,(HL)
6289: 42         LD           B,D
628A: 0F         RRCA
628B: 33         INC         SP
628C: 0D         DEC         C
628D: 36 0D      LD           (HL),$0D
628F: 53         LD           D,E
6290: 0F         RRCA
6291: 56         LD           D,(HL)
6292: 0F         RRCA
6293: 11 A6 18   LD           DE,$18A6
6296: A6         AND         (HL)
6297: FE 0C      CP           $0C
6299: 0D         DEC         C
629A: 19         ADD         HL,DE
629B: F3         DI
629C: 59         LD           E,C
629D: F7         RST         0X30
629E: 86         ADD         A,(HL)
629F: 22         LD           (HLI),A
62A0: 0F         RRCA
62A1: 86         ADD         A,(HL)
62A2: 32         LD           (HLD),A
62A3: 0F         RRCA
62A4: 86         ADD         A,(HL)
62A5: 42         LD           B,D
62A6: 0F         RRCA
62A7: 33         INC         SP
62A8: 0D         DEC         C
62A9: 36 0D      LD           (HL),$0D
62AB: 53         LD           D,E
62AC: 0F         RRCA
62AD: 56         LD           D,(HL)
62AE: 0F         RRCA
62AF: 59         LD           E,C
62B0: 2A         LD           A,(HLI)
62B1: 69         LD           L,C
62B2: 0D         DEC         C
62B3: 79         LD           A,C
62B4: 22         LD           (HLI),A
62B5: FE 0C      CP           $0C
62B7: 0D         DEC         C
62B8: 10 F2      STOP       $F2
62BA: 72         LD           (HL),D
62BB: F5         PUSH       AF
62BC: 83         ADD         A,E
62BD: 16 0F      LD           D,$0F
62BF: 83         ADD         A,E
62C0: 26 0F      LD           H,$0F
62C2: 83         ADD         A,E
62C3: 36 0F      LD           (HL),$0F
62C5: 87         ADD         A,A
62C6: 32         LD           (HLD),A
62C7: A6         AND         (HL)
62C8: 30 27      JR           NC,$62F1
62CA: 31 2B 82   LD           SP,$822B
62CD: 34         INC         (HL)
62CE: 0D         DEC         C
62CF: 40         LD           B,B
62D0: 03         INC         BC
62D1: 41         LD           B,C
62D2: 23         INC         HL
62D3: 44         LD           B,H
62D4: A7         AND         A
62D5: 45         LD           B,L
62D6: A6         AND         (HL)
62D7: 50         LD           D,B
62D8: 21 51 29   LD           HL,$2951
62DB: 60         LD           H,B
62DC: 0D         DEC         C
62DD: 61         LD           H,C
62DE: DE 70      SBC         $70
62E0: 22         LD           (HLI),A
62E1: 76         HALT
62E2: 2B         DEC         HL
62E3: 82         ADD         A,D
62E4: 77         LD           (HL),A
62E5: 0D         DEC         C
62E6: 79         LD           A,C
62E7: 24         INC         H
62E8: 17         RLA
62E9: BE         CP           (HL)
62EA: E2         LDFF00   (C),A
62EB: 04         INC         B
62EC: A5         AND         L
62ED: 88         ADC         A,B
62EE: 10 82      STOP       $82
62F0: 34         INC         (HL)
62F1: 20 FE      JR           NZ,$62F1
62F3: 0C         INC         C
62F4: 0D         DEC         C
62F5: 49         LD           C,C
62F6: F3         DI
62F7: 74         LD           (HL),H
62F8: F1         POP         AF
62F9: 86         ADD         A,(HL)
62FA: 22         LD           (HLI),A
62FB: 0F         RRCA
62FC: 86         ADD         A,(HL)
62FD: 32         LD           (HLD),A
62FE: 0F         RRCA
62FF: 86         ADD         A,(HL)
6300: 42         LD           B,D
6301: 0F         RRCA
6302: 33         INC         SP
6303: 0D         DEC         C
6304: 36 0D      LD           (HL),$0D
6306: 53         LD           D,E
6307: 0F         RRCA
6308: 56         LD           D,(HL)
6309: 0F         RRCA
630A: 11 A6 FE   LD           DE,$FEA6
630D: 0C         INC         C
630E: 0D         DEC         C
630F: 03         INC         BC
6310: F4                              
6311: 40         LD           B,B
6312: F6 84      OR           $84
6314: 06 03      LD           B,$03
6316: 84         ADD         A,H
6317: 16 03      LD           D,$03
6319: 84         ADD         A,H
631A: 26 03      LD           H,$03
631C: 82         ADD         A,D
631D: 03         INC         BC
631E: 0D         DEC         C
631F: 02         LD           (BC),A
6320: 29         ADD         HL,HL
6321: C3 05 24   JP           $2405
6324: 35         DEC         (HL)
6325: 2A         LD           A,(HLI)
6326: 83         ADD         A,E
6327: 36 21      LD           (HL),$21
6329: 39         ADD         HL,SP
632A: 26 60      LD           H,$60
632C: 27         DAA
632D: 88         ADC         A,B
632E: 61         LD           H,C
632F: 22         LD           (HLI),A
6330: 69         LD           L,C
6331: 28 8A      JR           Z,$62BD
6333: 70         LD           (HL),B
6334: 03         INC         BC
6335: 14         INC         D
6336: DF         RST         0X18
6337: 52         LD           D,D
6338: DF         RST         0X18
6339: 82         ADD         A,D
633A: 47         LD           B,A
633B: 0F         RRCA
633C: 82         ADD         A,D
633D: 57         LD           D,A
633E: 0F         RRCA
633F: 83         ADD         A,E
6340: 11 0F 83   LD           DE,$830F
6343: 21 0F 83   LD           HL,$830F
6346: 31 0F 22   LD           SP,$220F
6349: A0         AND         B
634A: 48         LD           C,B
634B: BE         CP           (HL)
634C: E2         LDFF00   (C),A
634D: 04         INC         B
634E: A7         AND         A
634F: 88         ADC         A,B
6350: 10 15      STOP       $15
6352: 2A         LD           A,(HLI)
6353: 16 21      LD           D,$21
6355: 17         RLA
6356: 26 27      LD           H,$27
6358: 24         INC         H
6359: 37         SCF
635A: 2A         LD           A,(HLI)
635B: 38 21      JR           C,$637E
635D: 39         ADD         HL,SP
635E: 26 82      LD           H,$82
6360: 25         DEC         H
6361: 20 82      JR           NZ,$62E5
6363: 35         DEC         (HL)
6364: 20 FE      JR           NZ,$6364
6366: 0C         INC         C
6367: 0D         DEC         C
6368: 59         LD           E,C
6369: F7         RST         0X30
636A: 83         ADD         A,E
636B: 12         LD           (DE),A
636C: 0F         RRCA
636D: 83         ADD         A,E
636E: 22         LD           (HLI),A
636F: 0F         RRCA
6370: 83         ADD         A,E
6371: 32         LD           (HLD),A
6372: 0F         RRCA
6373: 84         ADD         A,H
6374: 15         DEC         D
6375: 01 84 25   LD           BC,$2584
6378: 01 84 35   LD           BC,$3584
637B: 01 84 45   LD           BC,$4584
637E: B0         OR           B
637F: 19         ADD         HL,DE
6380: 2A         LD           A,(HLI)
6381: 29         ADD         HL,HL
6382: 0D         DEC         C
6383: 39         ADD         HL,SP
6384: 2C         INC         L
6385: 23         INC         HL
6386: A0         AND         B
6387: C6 11      ADD         $11
6389: 20 FE      JR           NZ,$6389
638B: 0C         INC         C
638C: 0D         DEC         C
638D: 29         ADD         HL,HL
638E: F7         RST         0X30
638F: 50         LD           D,B
6390: F2                              
6391: 07         RLCA
6392: 26 82      LD           H,$82
6394: 08 03 10   LD           ($1003),SP
6397: 29         ADD         HL,HL
6398: C6 13      ADD         $13
639A: A6         AND         (HL)
639B: C6 15      ADD         $15
639D: A6         AND         (HL)
639E: 17         RLA
639F: 24         INC         H
63A0: 18 C0      JR           $6362
63A2: 19         ADD         HL,DE
63A3: 03         INC         BC
63A4: 20 0D      JR           NZ,$63B3
63A6: 27         DAA
63A7: 2A         LD           A,(HLI)
63A8: 82         ADD         A,D
63A9: 28 21      JR           Z,$63CC
63AB: 30 2B      JR           NC,$63D8
63AD: 31 AE 33   LD           SP,$33AE
63B0: AF         XOR         A
63B1: 35         DEC         (HL)
63B2: AF         XOR         A
63B3: 37         SCF
63B4: AF         XOR         A
63B5: 39         ADD         HL,SP
63B6: A6         AND         (HL)
63B7: 41         LD           B,C
63B8: A6         AND         (HL)
63B9: 43         LD           B,E
63BA: B0         OR           B
63BB: 45         LD           B,L
63BC: B0         OR           B
63BD: 47         LD           B,A
63BE: B0         OR           B
63BF: 49         LD           C,C
63C0: 0D         DEC         C
63C1: 57         LD           D,A
63C2: 2C         INC         L
63C3: 82         ADD         A,D
63C4: 58         LD           E,B
63C5: 22         LD           (HLI),A
63C6: 67         LD           H,A
63C7: 24         INC         H
63C8: 68         LD           L,B
63C9: C0         RET         NZ
63CA: 69         LD           L,C
63CB: 03         INC         BC
63CC: 77         LD           (HL),A
63CD: 28 82      JR           Z,$6351
63CF: 78         LD           A,B
63D0: 03         INC         BC
63D1: FE 0C      CP           $0C
63D3: 0D         DEC         C
63D4: 02         LD           (BC),A
63D5: F0 74      LD           A,($74)
63D7: F5         PUSH       AF
63D8: 30 F6      JR           NC,$63D0
63DA: 06 29      LD           B,$29
63DC: 82         ADD         A,D
63DD: 07         RLCA
63DE: 0D         DEC         C
63DF: 09         ADD         HL,BC
63E0: 24         INC         H
63E1: 20 29      JR           NZ,$640C
63E3: C2 30 0D   JP           NZ,$0D30
63E6: 30 A6      JR           NC,$638E
63E8: 50         LD           D,B
63E9: 2B         DEC         HL
63EA: C5         PUSH       BC
63EB: 16 A6      LD           D,$A6
63ED: 82         ADD         A,D
63EE: 17         RLA
63EF: AF         XOR         A
63F0: 82         ADD         A,D
63F1: 27         DAA
63F2: 01 82 37   LD           BC,$3782
63F5: 01 82 47   LD           BC,$4782
63F8: 01 82 57   LD           BC,$5782
63FB: B0         OR           B
63FC: 18 9E      JR           $639C
63FE: 15         DEC         D
63FF: C0         RET         NZ
6400: 51         LD           D,C
6401: 20 82      JR           NZ,$6385
6403: 61         LD           H,C
6404: 20 27      JR           NZ,$642D
6406: B0         OR           B
6407: 37         SCF
6408: 20 47      JR           NZ,$6451
640A: AF         XOR         A
640B: FE 0C      CP           $0C
640D: 3D         DEC         A
640E: 04         INC         B
640F: F0 74      LD           A,($74)
6411: F5         PUSH       AF
6412: 21 DD 28   LD           HL,$28DD
6415: DD                              
6416: 82         ADD         A,D
6417: 44         LD           B,H
6418: DD                              
6419: 82         ADD         A,D
641A: 54         LD           D,H
641B: DD                              
641C: 51         LD           D,C
641D: DD                              
641E: 58         LD           E,B
641F: DD                              
6420: 82         ADD         A,D
6421: 61         LD           H,C
6422: DD                              
6423: 82         ADD         A,D
6424: 67         LD           H,A
6425: DD                              
6426: 32         LD           (HLD),A
6427: A6         AND         (HL)
6428: 37         SCF
6429: A6         AND         (HL)
642A: 82         ADD         A,D
642B: 71         LD           (HL),C
642C: A6         AND         (HL)
642D: 82         ADD         A,D
642E: 77         LD           (HL),A
642F: A6         AND         (HL)
6430: C3 55 1B   JP           $1B55
6433: C7         RST         0X00
6434: 16 1B      LD           D,$1B
6436: 82         ADD         A,D
6437: 73         LD           (HL),E
6438: 0D         DEC         C
6439: C2 16 0D   JP           NZ,$0D16
643C: FE 0C      CP           $0C
643E: 0D         DEC         C
643F: 39         ADD         HL,SP
6440: F7         RST         0X30
6441: 22         LD           (HLI),A
6442: A6         AND         (HL)
6443: 27         DAA
6444: A6         AND         (HL)
6445: 52         LD           D,D
6446: A6         AND         (HL)
6447: 57         LD           D,A
6448: A6         AND         (HL)
6449: 23         INC         HL
644A: 20 36      JR           NZ,$6482
644C: 20 43      JR           NZ,$6491
644E: 20 56      JR           NZ,$64A6
6450: 20 34      JR           NZ,$6486
6452: A6         AND         (HL)
6453: 45         LD           B,L
6454: A6         AND         (HL)
6455: FE 0C      CP           $0C
6457: 2D         DEC         L
6458: 04         INC         B
6459: F0 30      LD           A,($30)
645B: F2                              
645C: 39         ADD         HL,SP
645D: F7         RST         0X30
645E: C2 39 0D   JP           NZ,$0D39
6461: 19         ADD         HL,DE
6462: A6         AND         (HL)
6463: 22         LD           (HLI),A
6464: A6         AND         (HL)
6465: 35         DEC         (HL)
6466: A6         AND         (HL)
6467: 46         LD           B,(HL)
6468: A6         AND         (HL)
6469: 53         LD           D,E
646A: A6         AND         (HL)
646B: 69         LD           L,C
646C: A6         AND         (HL)
646D: FE 0C      CP           $0C
646F: 6D         LD           L,L
6470: 04         INC         B
6471: F4                              
6472: 30 F6      JR           NC,$646A
6474: 74         LD           (HL),H
6475: ED                              
6476: 82         ADD         A,D
6477: 04         INC         B
6478: 0D         DEC         C
6479: C2 30 0D   JP           NZ,$0D30
647C: 00         NOP
647D: 29         ADD         HL,HL
647E: 82         ADD         A,D
647F: 01 A6 82   LD           BC,$82A6
6482: 07         RLCA
6483: A6         AND         (HL)
6484: 10 A6      STOP       $A6
6486: 60         LD           H,B
6487: A6         AND         (HL)
6488: 84         ADD         A,H
6489: 13         INC         DE
648A: DD                              
648B: 21 DD 28   LD           HL,$28DD
648E: DD                              
648F: 35         DEC         (HL)
6490: DD                              
6491: 44         LD           B,H
6492: DD                              
6493: 52         LD           D,D
6494: DD                              
6495: 57         LD           D,A
6496: DD                              
6497: 61         LD           H,C
6498: DD                              
6499: 68         LD           L,B
649A: DD                              
649B: C6 05      ADD         $05
649D: 1B         DEC         DE
649E: 06 1B      LD           B,$1B
64A0: 82         ADD         A,D
64A1: 53         LD           D,E
64A2: 1B         DEC         DE
64A3: 63         LD           H,E
64A4: 1B         DEC         DE
64A5: FE 0C      CP           $0C
64A7: 0D         DEC         C
64A8: 39         ADD         HL,SP
64A9: F3         DI
64AA: 88         ADC         A,B
64AB: 11 0F 88   LD           DE,$880F
64AE: 21 0F 88   LD           HL,$880F
64B1: 31 0F 82   LD           SP,$820F
64B4: 34         INC         (HL)
64B5: 0D         DEC         C
64B6: 04         INC         B
64B7: 26 05      LD           H,$05
64B9: 25         DEC         H
64BA: 14         INC         D
64BB: 24         INC         H
64BC: 15         DEC         D
64BD: 23         INC         HL
64BE: 24         INC         H
64BF: 2A         LD           A,(HLI)
64C0: 25         DEC         H
64C1: 29         ADD         HL,HL
64C2: 74         LD           (HL),H
64C3: 28 75      JR           Z,$653A
64C5: 27         DAA
64C6: 64         LD           H,H
64C7: 24         INC         H
64C8: 65         LD           H,L
64C9: 23         INC         HL
64CA: 54         LD           D,H
64CB: 2C         INC         L
64CC: 55         LD           D,L
64CD: 2B         DEC         HL
64CE: 52         LD           D,D
64CF: C0         RET         NZ
64D0: 57         LD           D,A
64D1: C0         RET         NZ
64D2: 27         DAA
64D3: A0         AND         B
64D4: 22         LD           (HLI),A
64D5: BE         CP           (HL)
64D6: E2         LDFF00   (C),A
64D7: 04         INC         B
64D8: A9         XOR         C
64D9: 88         ADC         A,B
64DA: 10 FE      STOP       $FE
64DC: 0C         INC         C
64DD: 0D         DEC         C
64DE: 04         INC         B
64DF: EC                              
64E0: 30 F2      JR           NC,$64D4
64E2: 49         LD           C,C
64E3: F7         RST         0X30
64E4: 87         ADD         A,A
64E5: 31 0F 41   LD           SP,$410F
64E8: 0F         RRCA
64E9: 27         DAA
64EA: 0F         RRCA
64EB: 83         ADD         A,E
64EC: 17         RLA
64ED: 0F         RRCA
64EE: 28 A6      JR           Z,$6496
64F0: 13         INC         DE
64F1: 1B         DEC         DE
64F2: C4 14 1B   CALL       NZ,$1B14
64F5: C3 45 1B   JP           $1B45
64F8: 09         ADD         HL,BC
64F9: 21 C2 29   LD           HL,$29C2
64FC: A6         AND         (HL)
64FD: 49         LD           C,C
64FE: 0D         DEC         C
64FF: 59         LD           E,C
6500: 2C         INC         L
6501: 23         INC         HL
6502: C0         RET         NZ
6503: 26 C0      LD           H,$C0
6505: 43         LD           B,E
6506: C0         RET         NZ
6507: 46         LD           B,(HL)
6508: C0         RET         NZ
6509: 14         INC         D
650A: 0D         DEC         C
650B: FE 0C      CP           $0C
650D: 0D         DEC         C
650E: 40         LD           B,B
650F: F6 59      OR           $59
6511: F7         RST         0X30
6512: 00         NOP
6513: 21 10 0D   LD           HL,$0D10
6516: 20 A6      JR           NZ,$64BE
6518: 89         ADC         A,C
6519: 30 A6      JR           NC,$64C1
651B: 40         LD           B,B
651C: 0D         DEC         C
651D: 50         LD           D,B
651E: 2B         DEC         HL
651F: 83         ADD         A,E
6520: 16 0F      LD           D,$0F
6522: 83         ADD         A,E
6523: 26 0F      LD           H,$0F
6525: 17         RLA
6526: A0         AND         B
6527: 59         LD           E,C
6528: 2A         LD           A,(HLI)
6529: 69         LD           L,C
652A: 0D         DEC         C
652B: 84         ADD         A,H
652C: 12         LD           (DE),A
652D: 01 84 22   LD           BC,$2284
6530: B0         OR           B
6531: 79         LD           A,C
6532: 22         LD           (HLI),A
6533: 53         LD           D,E
6534: C0         RET         NZ
6535: 56         LD           D,(HL)
6536: C0         RET         NZ
6537: 82         ADD         A,D
6538: 10 0F      STOP       $0F
653A: 21 0F FE   LD           HL,$FE0F
653D: 0C         INC         C
653E: 0D         DEC         C
653F: 50         LD           D,B
6540: F6 50      OR           $50
6542: 29         ADD         HL,HL
6543: 88         ADC         A,B
6544: 11 0F 88   LD           DE,$880F
6547: 21 0F 88   LD           HL,$880F
654A: 31 0F 04   LD           SP,$040F
654D: 26 05      LD           H,$05
654F: 25         DEC         H
6550: 14         INC         D
6551: 24         INC         H
6552: 15         DEC         D
6553: 23         INC         HL
6554: 24         INC         H
6555: 2A         LD           A,(HLI)
6556: 25         DEC         H
6557: 29         ADD         HL,HL
6558: 82         ADD         A,D
6559: 34         INC         (HL)
655A: 0D         DEC         C
655B: 22         LD           (HLI),A
655C: C0         RET         NZ
655D: 27         DAA
655E: C0         RET         NZ
655F: 60         LD           H,B
6560: 0D         DEC         C
6561: 70         LD           (HL),B
6562: 22         LD           (HLI),A
6563: 53         LD           D,E
6564: FC                              
6565: E0 00      LDFF00   ($00),A
6567: D9         RETI
6568: 58         LD           E,B
6569: 40         LD           B,B
656A: FE 05      CP           $05
656C: 94         SUB         H
656D: 11 83 C5   LD           DE,$C583
6570: 21 84 88   LD           HL,$8884
6573: 51         LD           D,C
6574: 84         ADD         A,H
6575: 88         ADC         A,B
6576: 61         LD           H,C
6577: 84         ADD         A,H
6578: 83         ADD         A,E
6579: 33         INC         SP
657A: 83         ADD         A,E
657B: 8A         ADC         A,D
657C: 00         NOP
657D: 6D         LD           L,L
657E: 01 65 8A   LD           BC,$8A65
6581: 70         LD           (HL),B
6582: 6D         LD           L,L
6583: C3 10 6C   JP           $6C10
6586: C3 12 6C   JP           $6C12
6589: 8A         ADC         A,D
658A: 40         LD           B,B
658B: 6D         LD           L,L
658C: 41         LD           B,C
658D: 84         ADD         A,H
658E: 83         ADD         A,E
658F: 43         LD           B,E
6590: 84         ADD         A,H
6591: 8A         ADC         A,D
6592: 70         LD           (HL),B
6593: 6D         LD           L,L
6594: 82         ADD         A,D
6595: 61         LD           H,C
6596: 72         LD           (HL),D
6597: 63         LD           H,E
6598: 73         LD           (HL),E
6599: C2 50 6C   JP           NZ,$6C50
659C: C2 59 4B   JP           NZ,$4B59
659F: 11 83 36   LD           DE,$3683
65A2: 6D         LD           L,L
65A3: 86         ADD         A,(HL)
65A4: 13         INC         DE
65A5: 5C         LD           E,H
65A6: 84         ADD         A,H
65A7: 24         INC         H
65A8: 04         INC         B
65A9: C3 19 6C   JP           $6C19
65AC: E1         POP         HL
65AD: 04         INC         B
65AE: 86         ADD         A,(HL)
65AF: 88         ADC         A,B
65B0: 20 FE      JR           NZ,$65B0
65B2: 05         DEC         B
65B3: 94         SUB         H
65B4: 82         ADD         A,D
65B5: 00         NOP
65B6: 6D         LD           L,L
65B7: 82         ADD         A,D
65B8: 08 6D C3   LD           ($C36D),SP
65BB: 11 6C C6   LD           DE,$C66C
65BE: 18 6C      JR           $662C
65C0: 10 54      STOP       $54
65C2: 19         ADD         HL,DE
65C3: 54         LD           D,H
65C4: 20 54      JR           NZ,$661A
65C6: 29         ADD         HL,HL
65C7: 54         LD           D,H
65C8: 30 54      JR           NC,$661E
65CA: 39         ADD         HL,SP
65CB: 54         LD           D,H
65CC: C4 49 54   CALL       NZ,$5449
65CF: 82         ADD         A,D
65D0: 40         LD           B,B
65D1: 6D         LD           L,L
65D2: C2 58 6C   JP           NZ,$6C58
65D5: 89         ADC         A,C
65D6: 70         LD           (HL),B
65D7: 6D         LD           L,L
65D8: 86         ADD         A,(HL)
65D9: 02         LD           (BC),A
65DA: 80         ADD         A,B
65DB: 86         ADD         A,(HL)
65DC: 12         LD           (DE),A
65DD: 81         ADD         A,C
65DE: 86         ADD         A,(HL)
65DF: 22         LD           (HLI),A
65E0: 81         ADD         A,C
65E1: 86         ADD         A,(HL)
65E2: 32         LD           (HLD),A
65E3: 81         ADD         A,C
65E4: 86         ADD         A,(HL)
65E5: 42         LD           B,D
65E6: 81         ADD         A,C
65E7: 86         ADD         A,(HL)
65E8: 52         LD           D,D
65E9: 81         ADD         A,C
65EA: 86         ADD         A,(HL)
65EB: 62         LD           H,D
65EC: 81         ADD         A,C
65ED: 82         ADD         A,D
65EE: 50         LD           D,B
65EF: 4B         LD           C,E
65F0: 82         ADD         A,D
65F1: 60         LD           H,B
65F2: 4B         LD           C,E
65F3: C2 24 6C   JP           NZ,$6C24
65F6: 82         ADD         A,D
65F7: 44         LD           B,H
65F8: 6D         LD           L,L
65F9: E1         POP         HL
65FA: 04         INC         B
65FB: 8D         ADC         A,L
65FC: 50         LD           D,B
65FD: 48         LD           C,B
65FE: FE 05      CP           $05
6600: 94         SUB         H
6601: 8A         ADC         A,D
6602: 00         NOP
6603: 6D         LD           L,L
6604: C5         PUSH       BC
6605: 10 6C      STOP       $6C
6607: 85         ADD         A,L
6608: 30 6D      JR           NC,$6677
660A: C3 17 6C   JP           $6C17
660D: 47         LD           B,A
660E: 6D         LD           L,L
660F: 82         ADD         A,D
6610: 35         DEC         (HL)
6611: 64         LD           H,H
6612: C3 01 65   JP           $6501
6615: 16 8F      LD           D,$8F
6617: 82         ADD         A,D
6618: 60         LD           H,B
6619: 6D         LD           L,L
661A: 82         ADD         A,D
661B: 70         LD           (HL),B
661C: 54         LD           D,H
661D: 88         ADC         A,B
661E: 72         LD           (HL),D
661F: 6D         LD           L,L
6620: 83         ADD         A,E
6621: 43         LD           B,E
6622: 6B         LD           L,E
6623: 44         LD           B,H
6624: 69         LD           L,C
6625: 83         ADD         A,E
6626: 53         LD           D,E
6627: 69         LD           L,C
6628: 54         LD           D,H
6629: 82         ADD         A,D
662A: 51         LD           D,C
662B: 75         LD           (HL),L
662C: C3 29 6D   JP           $6D29
662F: 39         ADD         HL,SP
6630: 6C         LD           L,H
6631: 69         LD           L,C
6632: 6D         LD           L,L
6633: E1         POP         HL
6634: 04         INC         B
6635: 8C         ADC         A,H
6636: 78         LD           A,B
6637: 60         LD           H,B
6638: FE 05      CP           $05
663A: 94         SUB         H
663B: 83         ADD         A,E
663C: 12         LD           (DE),A
663D: 6B         LD           L,E
663E: 13         INC         DE
663F: 69         LD           L,C
6640: 83         ADD         A,E
6641: 22         LD           (HLI),A
6642: 69         LD           L,C
6643: 23         INC         HL
6644: 82         ADD         A,D
6645: 8A         ADC         A,D
6646: 00         NOP
6647: 6D         LD           L,L
6648: C6 08      ADD         $08
664A: 63         LD           H,E
664B: 16 8F      LD           D,$8F
664D: C2 17 6C   JP           NZ,$6C17
6650: C5         PUSH       BC
6651: 19         ADD         HL,DE
6652: 6C         LD           L,H
6653: 20 6D      JR           NZ,$66C2
6655: 30 6C      JR           NC,$66C3
6657: 31 6D 35   LD           SP,$356D
665A: 6D         LD           L,L
665B: 36 64      LD           (HL),$64
665D: 37         SCF
665E: 6D         LD           L,L
665F: 38 62      JR           C,$66C3
6661: 39         ADD         HL,SP
6662: 6D         LD           L,L
6663: 86         ADD         A,(HL)
6664: 40         LD           B,B
6665: 6D         LD           L,L
6666: 60         LD           H,B
6667: 6D         LD           L,L
6668: 69         LD           L,C
6669: 6D         LD           L,L
666A: 8A         ADC         A,D
666B: 70         LD           (HL),B
666C: 6D         LD           L,L
666D: E1         POP         HL
666E: 04         INC         B
666F: 94         SUB         H
6670: 78         LD           A,B
6671: 20 FE      JR           NZ,$6671
6673: 05         DEC         B
6674: 94         SUB         H
6675: 8A         ADC         A,D
6676: 00         NOP
6677: 68         LD           L,B
6678: C3 01 65   JP           $6501
667B: C3 10 6C   JP           $6C10
667E: 89         ADC         A,C
667F: 31 7B C2   LD           SP,$C27B
6682: 13         INC         DE
6683: 4D         LD           C,L
6684: 83         ADD         A,E
6685: 14         INC         D
6686: 6B         LD           L,E
6687: 15         DEC         D
6688: 69         LD           L,C
6689: 83         ADD         A,E
668A: 24         INC         H
668B: 69         LD           L,C
668C: 25         DEC         H
668D: 82         ADD         A,D
668E: C2 16 4D   JP           NZ,$4D16
6691: C2 40 57   JP           NZ,$5740
6694: 89         ADC         A,C
6695: 51         LD           D,C
6696: 80         ADD         A,B
6697: 88         ADC         A,B
6698: 62         LD           H,D
6699: 81         ADD         A,C
669A: 88         ADC         A,B
669B: 72         LD           (HL),D
669C: 81         ADD         A,C
669D: 82         ADD         A,D
669E: 78         LD           A,B
669F: 53         LD           D,E
66A0: C2 60 54   JP           NZ,$5460
66A3: 61         LD           H,C
66A4: 56         LD           D,(HL)
66A5: 71         LD           (HL),C
66A6: 54         LD           D,H
66A7: 88         ADC         A,B
66A8: 72         LD           (HL),D
66A9: 53         LD           D,E
66AA: 34         INC         (HL)
66AB: 04         INC         B
66AC: 82         ADD         A,D
66AD: 37         SCF
66AE: 04         INC         B
66AF: 48         LD           C,B
66B0: 64         LD           H,H
66B1: E1         POP         HL
66B2: 04         INC         B
66B3: 89         ADC         A,C
66B4: 18 20      JR           $66D6
66B6: FE 05      CP           $05
66B8: 94         SUB         H
66B9: 8A         ADC         A,D
66BA: 00         NOP
66BB: 68         LD           L,B
66BC: C3 08 65   JP           $6508
66BF: C3 19 6C   JP           $6C19
66C2: 89         ADC         A,C
66C3: 30 7B      JR           NC,$6740
66C5: C2 11 4D   JP           NZ,$4D11
66C8: C2 16 4D   JP           NZ,$4D16
66CB: 83         ADD         A,E
66CC: 13         INC         DE
66CD: 6B         LD           L,E
66CE: 14         INC         D
66CF: 69         LD           L,C
66D0: 83         ADD         A,E
66D1: 23         INC         HL
66D2: 69         LD           L,C
66D3: 24         INC         H
66D4: 82         ADD         A,D
66D5: C2 49 51   JP           NZ,$5149
66D8: 89         ADC         A,C
66D9: 50         LD           D,B
66DA: 80         ADD         A,B
66DB: 89         ADC         A,C
66DC: 60         LD           H,B
66DD: 81         ADD         A,C
66DE: 82         ADD         A,D
66DF: 63         LD           H,E
66E0: 53         LD           D,E
66E1: 88         ADC         A,B
66E2: 70         LD           (HL),B
66E3: 53         LD           D,E
66E4: 82         ADD         A,D
66E5: 73         LD           (HL),E
66E6: 54         LD           D,H
66E7: C2 69 54   JP           NZ,$5469
66EA: 68         LD           L,B
66EB: 56         LD           D,(HL)
66EC: 78         LD           A,B
66ED: 54         LD           D,H
66EE: 82         ADD         A,D
66EF: 33         INC         SP
66F0: 04         INC         B
66F1: E1         POP         HL
66F2: 04         INC         B
66F3: 96         SUB         (HL)
66F4: 88         ADC         A,B
66F5: 50         LD           D,B
66F6: FE 05      CP           $05
66F8: 94         SUB         H
66F9: 8A         ADC         A,D
66FA: 00         NOP
66FB: 6D         LD           L,L
66FC: C6 10      ADD         $10
66FE: 6C         LD           L,H
66FF: 82         ADD         A,D
6700: 30 6D      JR           NC,$676F
6702: 8A         ADC         A,D
6703: 70         LD           (HL),B
6704: 6D         LD           L,L
6705: 39         ADD         HL,SP
6706: 6D         LD           L,L
6707: 49         LD           C,C
6708: 6C         LD           L,H
6709: 59         LD           E,C
670A: 6D         LD           L,L
670B: C3 01 65   JP           $6501
670E: C4 12 4D   CALL       NZ,$4D12
6711: C4 14 4D   CALL       NZ,$4D14
6714: C2 16 4D   JP           NZ,$4D16
6717: C2 18 4D   JP           NZ,$4D18
671A: E1         POP         HL
671B: 04         INC         B
671C: 81         ADD         A,C
671D: 88         ADC         A,B
671E: 70         LD           (HL),B
671F: FE 05      CP           $05
6721: 94         SUB         H
6722: 8A         ADC         A,D
6723: 00         NOP
6724: 6D         LD           L,L
6725: C6 19      ADD         $19
6727: 6C         LD           L,H
6728: 8A         ADC         A,D
6729: 70         LD           (HL),B
672A: 6D         LD           L,L
672B: 83         ADD         A,E
672C: 30 6D      JR           NC,$679B
672E: 83         ADD         A,E
672F: 37         SCF
6730: 6D         LD           L,L
6731: C4 31 65   CALL       NZ,$6531
6734: C6 08      ADD         $08
6736: 65         LD           H,L
6737: 40         LD           B,B
6738: 6C         LD           L,H
6739: C3 42 6C   JP           $6C42
673C: 50         LD           D,B
673D: 6D         LD           L,L
673E: C4 14 4D   CALL       NZ,$4D14
6741: C2 16 4D   JP           NZ,$4D16
6744: 31 64 38   LD           SP,$3864
6747: 64         LD           H,H
6748: E1         POP         HL
6749: 04         INC         B
674A: 9E         SBC         (HL)
674B: 28 30      JR           Z,$677D
674D: FE 05      CP           $05
674F: 94         SUB         H
6750: C6 00      ADD         $00
6752: 68         LD           L,B
6753: C6 01      ADD         $01
6755: 65         LD           H,L
6756: 88         ADC         A,B
6757: 02         LD           (BC),A
6758: 68         LD           L,B
6759: 19         ADD         HL,DE
675A: 68         LD           L,B
675B: 83         ADD         A,E
675C: 22         LD           (HLI),A
675D: 68         LD           L,B
675E: 27         DAA
675F: 68         LD           L,B
6760: 28 64      JR           Z,$67C6
6762: 29         ADD         HL,HL
6763: 68         LD           L,B
6764: 83         ADD         A,E
6765: 33         INC         SP
6766: 6B         LD           L,E
6767: 34         INC         (HL)
6768: 69         LD           L,C
6769: 83         ADD         A,E
676A: 43         LD           B,E
676B: 69         LD           L,C
676C: 44         LD           B,H
676D: 82         ADD         A,D
676E: C2 38 65   JP           NZ,$6538
6771: 83         ADD         A,E
6772: 57         LD           D,A
6773: 68         LD           L,B
6774: 83         ADD         A,E
6775: 60         LD           H,B
6776: 68         LD           L,B
6777: 84         ADD         A,H
6778: 63         LD           H,E
6779: 4C         LD           C,H
677A: 67         LD           H,A
677B: 68         LD           L,B
677C: 82         ADD         A,D
677D: 68         LD           L,B
677E: 60         LD           H,B
677F: 82         ADD         A,D
6780: 70         LD           (HL),B
6781: 60         LD           H,B
6782: 86         ADD         A,(HL)
6783: 72         LD           (HL),D
6784: 68         LD           L,B
6785: 82         ADD         A,D
6786: 78         LD           A,B
6787: 60         LD           H,B
6788: E1         POP         HL
6789: 02         LD           (BC),A
678A: 4A         LD           C,D
678B: 18 30      JR           $67BD
678D: FE 05      CP           $05
678F: 94         SUB         H
6790: C2 00 60   JP           NZ,$6000
6793: 89         ADC         A,C
6794: 01 68 11   LD           BC,$1168
6797: 68         LD           L,B
6798: C7         RST         0X00
6799: 19         ADD         HL,DE
679A: 68         LD           L,B
679B: 82         ADD         A,D
679C: 20 68      JR           NZ,$6806
679E: 83         ADD         A,E
679F: 33         INC         SP
67A0: 6B         LD           L,E
67A1: 34         INC         (HL)
67A2: 69         LD           L,C
67A3: 83         ADD         A,E
67A4: 43         LD           B,E
67A5: 69         LD           L,C
67A6: 44         LD           B,H
67A7: 82         ADD         A,D
67A8: 36 64      LD           (HL),$64
67AA: C4 37 6C   CALL       NZ,$6C37
67AD: 38 64      JR           C,$6813
67AF: 83         ADD         A,E
67B0: 50         LD           D,B
67B1: 68         LD           L,B
67B2: C2 46 65   JP           NZ,$6546
67B5: C4 48 65   CALL       NZ,$6548
67B8: 83         ADD         A,E
67B9: 50         LD           D,B
67BA: 68         LD           L,B
67BB: 82         ADD         A,D
67BC: 60         LD           H,B
67BD: 60         LD           H,B
67BE: 62         LD           H,D
67BF: 68         LD           L,B
67C0: 84         ADD         A,H
67C1: 63         LD           H,E
67C2: 4C         LD           C,H
67C3: 82         ADD         A,D
67C4: 70         LD           (HL),B
67C5: 60         LD           H,B
67C6: 86         ADD         A,(HL)
67C7: 72         LD           (HL),D
67C8: 68         LD           L,B
67C9: E1         POP         HL
67CA: 02         LD           (BC),A
67CB: 5C         LD           E,H
67CC: 88         ADC         A,B
67CD: 20 FE      JR           NZ,$67CD
67CF: 0C         INC         C
67D0: 0D         DEC         C
67D1: 00         NOP
67D2: 0D         DEC         C
67D3: 01 25 08   LD           BC,$0825
67D6: 26 09      LD           H,$09
67D8: DF         RST         0X18
67D9: 10 25      STOP       $25
67DB: 11 29 C3   LD           DE,$C329
67DE: 12         LD           (DE),A
67DF: 10 13      STOP       $13
67E1: 25         DEC         H
67E2: 82         ADD         A,D
67E3: 14         INC         D
67E4: 21 16 26   LD           HL,$2616
67E7: C3 17 11   JP           $1117
67EA: 18 2A      JR           $6816
67EC: 19         ADD         HL,DE
67ED: 26 23      LD           H,$23
67EF: 23         INC         HL
67F0: 82         ADD         A,D
67F1: 24         INC         H
67F2: 1B         DEC         DE
67F3: 26 24      LD           H,$24
67F5: 33         INC         SP
67F6: 27         DAA
67F7: 82         ADD         A,D
67F8: 34         INC         (HL)
67F9: 22         LD           (HLI),A
67FA: 36 28      LD           (HL),$28
67FC: 42         LD           B,D
67FD: 87         ADD         A,A
67FE: 52         LD           D,D
67FF: CE 84      ADC         $84
6801: 43         LD           B,E
6802: 12         LD           (DE),A
6803: 47         LD           B,A
6804: 87         ADD         A,A
6805: 57         LD           D,A
6806: CE 60      ADC         $60
6808: 27         DAA
6809: 61         LD           H,C
680A: 2B         DEC         HL
680B: 68         LD           L,B
680C: 2C         INC         L
680D: 69         LD           L,C
680E: 28 70      JR           Z,$6880
6810: DF         RST         0X18
6811: 71         LD           (HL),C
6812: 27         DAA
6813: 78         LD           A,B
6814: 28 79      JR           Z,$688F
6816: 0D         DEC         C
6817: 74         LD           (HL),H
6818: FD                              
6819: E0 00      LDFF00   ($00),A
681B: 8D         ADC         A,L
681C: 38 20      JR           C,$683E
681E: FE 0C      CP           $0C
6820: 0D         DEC         C
6821: FE 0C      CP           $0C
6823: 0D         DEC         C
6824: FE 0C      CP           $0C
6826: 0D         DEC         C
6827: FE 04      CP           $04
6829: 0D         DEC         C
682A: 73         LD           (HL),E
682B: F1         POP         AF
682C: 02         LD           (BC),A
682D: C7         RST         0X00
682E: 02         LD           (BC),A
682F: C7         RST         0X00
6830: 05         DEC         B
6831: 26 06      LD           H,$06
6833: 2A         LD           A,(HLI)
6834: 88         ADC         A,B
6835: 11 0F 88   LD           DE,$880F
6838: 21 0F 88   LD           HL,$880F
683B: 31 0F C3   LD           SP,$C30F
683E: 14         INC         D
683F: DC C3 15   CALL       C,$15C3
6842: 24         INC         H
6843: 27         DAA
6844: A0         AND         B
6845: 37         SCF
6846: DB                              
6847: 39         ADD         HL,SP
6848: 2A         LD           A,(HLI)
6849: 84         ADD         A,H
684A: 41         LD           B,C
684B: DC 45 2A   CALL       C,$2A45
684E: 83         ADD         A,E
684F: 46         LD           B,(HL)
6850: 21 47 98   LD           HL,$9847
6853: 49         LD           C,C
6854: 26 07      LD           H,$07
6856: A3         AND         E
6857: E0 00      LDFF00   ($00),A
6859: 6C         LD           L,H
685A: 48         LD           C,B
685B: 40         LD           B,B
685C: FE 04      CP           $04
685E: 0D         DEC         C
685F: 75         LD           (HL),L
6860: F1         POP         AF
6861: 02         LD           (BC),A
6862: C7         RST         0X00
6863: 03         INC         BC
6864: 29         ADD         HL,HL
6865: 04         INC         B
6866: 25         DEC         H
6867: 07         RLCA
6868: C7         RST         0X00
6869: 88         ADC         A,B
686A: 11 0F 88   LD           DE,$880F
686D: 21 0F 88   LD           HL,$880F
6870: 31 0F C3   LD           SP,$C30F
6873: 14         INC         D
6874: 23         INC         HL
6875: C3 15 DC   JP           $DC15
6878: 22         LD           (HLI),A
6879: A0         AND         B
687A: 30 29      JR           NC,$68A5
687C: 32         LD           (HLD),A
687D: DB                              
687E: 40         LD           B,B
687F: 25         DEC         H
6880: 83         ADD         A,E
6881: 41         LD           B,C
6882: 21 42 98   LD           HL,$9842
6885: 44         LD           B,H
6886: 29         ADD         HL,HL
6887: 84         ADD         A,H
6888: 45         LD           B,L
6889: DC 32 DB   CALL       C,$DB32
688C: FE 04      CP           $04
688E: 0D         DEC         C
688F: 03         INC         BC
6890: F0 49      LD           A,($49)
6892: F7         RST         0X30
6893: 74         LD           (HL),H
6894: F5         PUSH       AF
6895: 02         LD           (BC),A
6896: C7         RST         0X00
6897: 05         DEC         B
6898: C7         RST         0X00
6899: C5         PUSH       BC
689A: 16 DC      LD           D,$DC
689C: 86         ADD         A,(HL)
689D: 23         INC         HL
689E: DB                              
689F: C2 33 DB   JP           NZ,$DB33
68A2: 50         LD           D,B
68A3: 27         DAA
68A4: 82         ADD         A,D
68A5: 51         LD           D,C
68A6: 22         LD           (HLI),A
68A7: 53         LD           D,E
68A8: 2B         DEC         HL
68A9: 63         LD           H,E
68AA: 23         INC         HL
68AB: 73         LD           (HL),E
68AC: 27         DAA
68AD: 83         ADD         A,E
68AE: 60         LD           H,B
68AF: 03         INC         BC
68B0: 83         ADD         A,E
68B1: 70         LD           (HL),B
68B2: 03         INC         BC
68B3: 66         LD           H,(HL)
68B4: 2C         INC         L
68B5: 83         ADD         A,E
68B6: 67         LD           H,A
68B7: 22         LD           (HLI),A
68B8: 76         HALT
68B9: 28 49      JR           Z,$6904
68BB: 2A         LD           A,(HLI)
68BC: 59         LD           E,C
68BD: 0D         DEC         C
68BE: 83         ADD         A,E
68BF: 77         LD           (HL),A
68C0: 03         INC         BC
68C1: 60         LD           H,B
68C2: C0         RET         NZ
68C3: 83         ADD         A,E
68C4: 70         LD           (HL),B
68C5: C0         RET         NZ
68C6: 51         LD           D,C
68C7: 98         SBC         B
68C8: FE 04      CP           $04
68CA: 9D         SBC         L
68CB: 40         LD           B,B
68CC: DB                              
68CD: 40         LD           B,B
68CE: F6 76      OR           $76
68D0: F5         PUSH       AF
68D1: 88         ADC         A,B
68D2: 01 12 09   LD           BC,$0912
68D5: 16 C7      LD           D,$C7
68D7: 19         ADD         HL,DE
68D8: 10 10      STOP       $10
68DA: 15         DEC         D
68DB: 87         ADD         A,A
68DC: 11 13 17   LD           DE,$1713
68DF: 95         SUB         L
68E0: 13         INC         DE
68E1: 0D         DEC         C
68E2: C6 27      ADD         $27
68E4: 11 C6 20   LD           DE,$20C6
68E7: 23         INC         HL
68E8: 86         ADD         A,(HL)
68E9: 21 21 C5   LD           HL,$C521
68EC: 36 24      LD           (HL),$24
68EE: 20 25      JR           NZ,$6915
68F0: 22         LD           (HLI),A
68F1: C7         RST         0X00
68F2: 23         INC         HL
68F3: 98         SBC         B
68F4: 24         INC         H
68F5: C7         RST         0X00
68F6: 26 26      LD           H,$26
68F8: 40         LD           B,B
68F9: 29         ADD         HL,HL
68FA: 50         LD           D,B
68FB: 0D         DEC         C
68FC: 60         LD           H,B
68FD: 2B         DEC         HL
68FE: 83         ADD         A,E
68FF: 32         LD           (HLD),A
6900: 0F         RRCA
6901: 83         ADD         A,E
6902: 42         LD           B,D
6903: 0F         RRCA
6904: 83         ADD         A,E
6905: 52         LD           D,D
6906: 0F         RRCA
6907: 85         ADD         A,L
6908: 61         LD           H,C
6909: C0         RET         NZ
690A: 43         LD           B,E
690B: A0         AND         B
690C: FE 04      CP           $04
690E: 9D         SBC         L
690F: 72         LD           (HL),D
6910: F5         PUSH       AF
6911: 88         ADC         A,B
6912: 11 DB 88   LD           DE,$88DB
6915: 21 DB 88   LD           HL,$88DB
6918: 31 DB 88   LD           SP,$88DB
691B: 41         LD           B,C
691C: DB                              
691D: 88         ADC         A,B
691E: 51         LD           D,C
691F: DB                              
6920: 88         ADC         A,B
6921: 61         LD           H,C
6922: DB                              
6923: 8A         ADC         A,D
6924: 00         NOP
6925: A6         AND         (HL)
6926: C6 10      ADD         $10
6928: A6         AND         (HL)
6929: C7         RST         0X00
692A: 19         ADD         HL,DE
692B: A6         AND         (HL)
692C: 70         LD           (HL),B
692D: 11 71 0D   LD           DE,$0D71
6930: 72         LD           (HL),D
6931: 10 86      STOP       $86
6933: 73         LD           (HL),E
6934: A6         AND         (HL)
6935: 82         ADD         A,D
6936: 14         INC         D
6937: 0D         DEC         C
6938: 33         INC         SP
6939: 0D         DEC         C
693A: 36 0D      LD           (HL),$0D
693C: FE 04      CP           $04
693E: 0D         DEC         C
693F: 74         LD           (HL),H
6940: F1         POP         AF
6941: 73         LD           (HL),E
6942: C8         RET         Z
6943: 76         HALT
6944: C8         RET         Z
6945: 20 C9      JR           NZ,$6910
6947: 50         LD           D,B
6948: C9         RET
6949: 29         ADD         HL,HL
694A: CA 59 CA   JP           Z,$CA59
694D: 84         ADD         A,H
694E: 13         INC         DE
694F: 0F         RRCA
6950: 84         ADD         A,H
6951: 23         INC         HL
6952: 0F         RRCA
6953: 84         ADD         A,H
6954: 33         INC         SP
6955: 0F         RRCA
6956: 02         LD           (BC),A
6957: 26 03      LD           H,$03
6959: 2A         LD           A,(HLI)
695A: 06 29      LD           B,$29
695C: 07         RLCA
695D: 25         DEC         H
695E: C3 12 24   JP           $2412
6961: 42         LD           B,D
6962: 2A         LD           A,(HLI)
6963: 84         ADD         A,H
6964: 43         LD           B,E
6965: 21 82 44   LD           HL,$4482
6968: 97         SUB         A
6969: 82         ADD         A,D
696A: 54         LD           D,H
696B: 0F         RRCA
696C: 82         ADD         A,D
696D: 64         LD           H,H
696E: 0F         RRCA
696F: 47         LD           B,A
6970: 29         ADD         HL,HL
6971: C3 17 23   JP           $2317
6974: 13         INC         DE
6975: C0         RET         NZ
6976: 16 C0      LD           D,$C0
6978: 33         INC         SP
6979: C0         RET         NZ
697A: 36 C0      LD           (HL),$C0
697C: 11 AC 18   LD           DE,$18AC
697F: AC         XOR         H
6980: 61         LD           H,C
6981: AC         XOR         H
6982: 68         LD           L,B
6983: AC         XOR         H
6984: E0 00      LDFF00   ($00),A
6986: 8C         ADC         A,H
6987: 38 40      JR           C,$69C9
6989: FE FE      CP           $FE
698B: 0C         INC         C
698C: 3D         DEC         A
698D: 74         LD           (HL),H
698E: F5         PUSH       AF
698F: 02         LD           (BC),A
6990: C7         RST         0X00
6991: 07         RLCA
6992: C7         RST         0X00
6993: 11 20 18   LD           DE,$1820
6996: 20 86      JR           NZ,$691E
6998: 12         LD           (DE),A
6999: 0F         RRCA
699A: 86         ADD         A,(HL)
699B: 22         LD           (HLI),A
699C: 0F         RRCA
699D: 86         ADD         A,(HL)
699E: 32         LD           (HLD),A
699F: 0F         RRCA
69A0: C2 62 10   JP           NZ,$1062
69A3: 86         ADD         A,(HL)
69A4: 53         LD           D,E
69A5: 13         INC         DE
69A6: 52         LD           D,D
69A7: 96         SUB         (HL)
69A8: 63         LD           H,E
69A9: 25         DEC         H
69AA: 84         ADD         A,H
69AB: 64         LD           H,H
69AC: 21 68 26   LD           HL,$2668
69AF: 73         LD           (HL),E
69B0: 23         INC         HL
69B1: 78         LD           A,B
69B2: 24         INC         H
69B3: 84         ADD         A,H
69B4: 74         LD           (HL),H
69B5: 1B         DEC         DE
69B6: 86         ADD         A,(HL)
69B7: 12         LD           (DE),A
69B8: 20 C2      JR           NZ,$697C
69BA: 21 20 C2   LD           HL,$C220
69BD: 28 20      JR           Z,$69DF
69BF: 88         ADC         A,B
69C0: 41         LD           B,C
69C1: 20 23      JR           NZ,$69E6
69C3: A0         AND         B
69C4: FE 04      CP           $04
69C6: 0D         DEC         C
69C7: 05         DEC         B
69C8: F4                              
69C9: 72         LD           (HL),D
69CA: F5         PUSH       AF
69CB: 83         ADD         A,E
69CC: 00         NOP
69CD: 03         INC         BC
69CE: 03         INC         BC
69CF: 25         DEC         H
69D0: 04         INC         B
69D1: C7         RST         0X00
69D2: 07         RLCA
69D3: C7         RST         0X00
69D4: 08 26 09   LD           ($0926),SP
69D7: 03         INC         BC
69D8: 10 25      STOP       $25
69DA: 82         ADD         A,D
69DB: 11 21 13   LD           DE,$1321
69DE: 29         ADD         HL,HL
69DF: 18 2A      JR           $6A0B
69E1: 19         ADD         HL,DE
69E2: 26 23      LD           H,$23
69E4: 20 28      JR           NZ,$6A0E
69E6: 20 87      JR           NZ,$696F
69E8: 32         LD           (HLD),A
69E9: A6         AND         (HL)
69EA: 41         LD           B,C
69EB: 20 47      JR           NZ,$6A34
69ED: 20 87      JR           NZ,$6976
69EF: 51         LD           D,C
69F0: A6         AND         (HL)
69F1: 65         LD           H,L
69F2: 20 34      JR           NZ,$6A28
69F4: A7         AND         A
69F5: 44         LD           B,H
69F6: 20 FE      JR           NZ,$69F6
69F8: 04         INC         B
69F9: 0D         DEC         C
69FA: 04         INC         B
69FB: F0 29      LD           A,($29)
69FD: F7         RST         0X30
69FE: 74         LD           (HL),H
69FF: F5         PUSH       AF
6A00: 06 26      LD           B,$26
6A02: 16 2A      LD           D,$2A
6A04: 83         ADD         A,E
6A05: 17         RLA
6A06: 21 83 07   LD           HL,$0783
6A09: 03         INC         BC
6A0A: 20 C9      JR           NZ,$69D5
6A0C: 50         LD           D,B
6A0D: C9         RET
6A0E: 29         ADD         HL,HL
6A0F: 0D         DEC         C
6A10: C4 13 DB   CALL       NZ,$DB13
6A13: C4 36 DC   CALL       NZ,$DC36
6A16: 82         ADD         A,D
6A17: 37         SCF
6A18: DC 39 2C   CALL       C,$2C39
6A1B: C3 47 20   JP           $2047
6A1E: C3 48 20   JP           $2048
6A21: 73         LD           (HL),E
6A22: 2B         DEC         HL
6A23: 82         ADD         A,D
6A24: 74         LD           (HL),H
6A25: 0D         DEC         C
6A26: 76         HALT
6A27: 2C         INC         L
6A28: FE 04      CP           $04
6A2A: 1D         DEC         E
6A2B: 02         LD           (BC),A
6A2C: F4                              
6A2D: 20 F6      JR           NZ,$6A25
6A2F: 39         ADD         HL,SP
6A30: F7         RST         0X30
6A31: 76         HALT
6A32: F5         PUSH       AF
6A33: 10 29      STOP       $29
6A35: 20 0D      JR           NZ,$6A44
6A37: 30 2B      JR           NC,$6A64
6A39: C7         RST         0X00
6A3A: 02         LD           (BC),A
6A3B: 0F         RRCA
6A3C: C7         RST         0X00
6A3D: 03         INC         BC
6A3E: 0F         RRCA
6A3F: C7         RST         0X00
6A40: 04         INC         B
6A41: 0F         RRCA
6A42: 86         ADD         A,(HL)
6A43: 31 C0 33   LD           SP,$33C0
6A46: AC         XOR         H
6A47: C2 06 24   JP           NZ,$2406
6A4A: 56         LD           D,(HL)
6A4B: 2C         INC         L
6A4C: 82         ADD         A,D
6A4D: 57         LD           D,A
6A4E: 22         LD           (HLI),A
6A4F: 59         LD           E,C
6A50: 28 76      JR           Z,$6AC8
6A52: 28 67      JR           Z,$6ABB
6A54: 17         RLA
6A55: 82         ADD         A,D
6A56: 68         LD           L,B
6A57: 12         LD           (DE),A
6A58: 77         LD           (HL),A
6A59: 11 78 0D   LD           DE,$0D78
6A5C: 79         LD           A,C
6A5D: 96         SUB         (HL)
6A5E: 26 2A      LD           H,$2A
6A60: 82         ADD         A,D
6A61: 27         DAA
6A62: 21 29 26   LD           HL,$2629
6A65: 09         ADD         HL,BC
6A66: 94         SUB         H
6A67: 07         RLCA
6A68: 11 17 15   LD           DE,$1517
6A6B: 82         ADD         A,D
6A6C: 18 13      JR           $6A81
6A6E: 66         LD           H,(HL)
6A6F: 24         INC         H
6A70: 17         RLA
6A71: AC         XOR         H
6A72: 13         INC         DE
6A73: A0         AND         B
6A74: 53         LD           D,E
6A75: BE         CP           (HL)
6A76: E2         LDFF00   (C),A
6A77: 05         DEC         B
6A78: DC 18 13   CALL       C,$1318
6A7B: FE 04      CP           $04
6A7D: 9D         SBC         L
6A7E: 30 DC      JR           NC,$6A5C
6A80: 30 F2      JR           NC,$6A74
6A82: 39         ADD         HL,SP
6A83: F3         DI
6A84: 8A         ADC         A,D
6A85: 00         NOP
6A86: 12         LD           (DE),A
6A87: 8A         ADC         A,D
6A88: 60         LD           H,B
6A89: 12         LD           (DE),A
6A8A: 8A         ADC         A,D
6A8B: 10 13      STOP       $13
6A8D: 8A         ADC         A,D
6A8E: 70         LD           (HL),B
6A8F: 13         INC         DE
6A90: 20 25      JR           NZ,$6AB7
6A92: 88         ADC         A,B
6A93: 21 21 29   LD           HL,$2921
6A96: 26 50      LD           H,$50
6A98: 27         DAA
6A99: 88         ADC         A,B
6A9A: 51         LD           D,C
6A9B: 22         LD           (HLI),A
6A9C: 59         LD           E,C
6A9D: 28 23      JR           Z,$6AC2
6A9F: C7         RST         0X00
6AA0: 26 C7      LD           H,$C7
6AA2: 53         LD           D,E
6AA3: C8         RET         Z
6AA4: 56         LD           D,(HL)
6AA5: C8         RET         Z
6AA6: 33         INC         SP
6AA7: 20 36      JR           NZ,$6ADF
6AA9: 20 43      JR           NZ,$6AEE
6AAB: 20 46      JR           NZ,$6AF3
6AAD: 20 FE      JR           NZ,$6AAD
6AAF: 04         INC         B
6AB0: 0D         DEC         C
6AB1: 02         LD           (BC),A
6AB2: F4                              
6AB3: 30 F2      JR           NC,$6AA7
6AB5: 76         HALT
6AB6: F5         PUSH       AF
6AB7: 00         NOP
6AB8: 93         SUB         E
6AB9: 01 0D 02   LD           BC,$020D
6ABC: 10 03      STOP       $03
6ABE: 25         DEC         H
6ABF: 82         ADD         A,D
6AC0: 10 13      STOP       $13
6AC2: 12         LD           (DE),A
6AC3: 14         INC         D
6AC4: 20 25      JR           NZ,$6AEB
6AC6: 82         ADD         A,D
6AC7: 21 21 23   LD           HL,$2321
6ACA: 29         ADD         HL,HL
6ACB: 50         LD           D,B
6ACC: 27         DAA
6ACD: 82         ADD         A,D
6ACE: 51         LD           D,C
6ACF: 22         LD           (HLI),A
6AD0: 53         LD           D,E
6AD1: 28 43      JR           Z,$6B16
6AD3: 2C         INC         L
6AD4: 83         ADD         A,E
6AD5: 44         LD           B,H
6AD6: 22         LD           (HLI),A
6AD7: 47         LD           B,A
6AD8: 2B         DEC         HL
6AD9: C3 57 23   JP           $2357
6ADC: 84         ADD         A,H
6ADD: 60         LD           H,B
6ADE: 12         LD           (DE),A
6ADF: 64         LD           H,H
6AE0: 93         SUB         E
6AE1: 54         LD           D,H
6AE2: AC         XOR         H
6AE3: 56         LD           D,(HL)
6AE4: AC         XOR         H
6AE5: 86         ADD         A,(HL)
6AE6: 70         LD           (HL),B
6AE7: 13         INC         DE
6AE8: 76         HALT
6AE9: 14         INC         D
6AEA: 66         LD           H,(HL)
6AEB: 10 78      STOP       $78
6AED: 0D         DEC         C
6AEE: 13         INC         DE
6AEF: 23         INC         HL
6AF0: 79         LD           A,C
6AF1: 24         INC         H
6AF2: FE 04      CP           $04
6AF4: 0D         DEC         C
6AF5: 04         INC         B
6AF6: F0 74      LD           A,($74)
6AF8: F1         POP         AF
6AF9: 03         INC         BC
6AFA: C7         RST         0X00
6AFB: 06 C7      LD           B,$C7
6AFD: 88         ADC         A,B
6AFE: 11 0F C4   LD           DE,$C40F
6B01: 21 0F C4   LD           HL,$C40F
6B04: 28 0F      JR           Z,$6B15
6B06: 88         ADC         A,B
6B07: 61         LD           H,C
6B08: 0F         RRCA
6B09: 11 20 18   LD           DE,$1820
6B0C: 20 61      JR           NZ,$6B6F
6B0E: 20 68      JR           NZ,$6B78
6B10: 20 FE      JR           NZ,$6B10
6B12: 04         INC         B
6B13: 0D         DEC         C
6B14: 04         INC         B
6B15: F4                              
6B16: 74         LD           (HL),H
6B17: F1         POP         AF
6B18: 88         ADC         A,B
6B19: 21 0F 88   LD           HL,$880F
6B1C: 31 0F 88   LD           SP,$880F
6B1F: 41         LD           B,C
6B20: 0F         RRCA
6B21: C3 24 0D   JP           $0D24
6B24: C3 25 0D   JP           $0D25
6B27: 61         LD           H,C
6B28: AC         XOR         H
6B29: 68         LD           L,B
6B2A: AC         XOR         H
6B2B: 32         LD           (HLD),A
6B2C: BE         CP           (HL)
6B2D: E2         LDFF00   (C),A
6B2E: 05         DEC         B
6B2F: DB                              
6B30: 88         ADC         A,B
6B31: 10 FE      STOP       $FE
6B33: 0C         INC         C
6B34: 9D         SBC         L
6B35: 03         INC         BC
6B36: F4                              
6B37: 75         LD           (HL),L
6B38: F5         PUSH       AF
6B39: C8         RET         Z
6B3A: 00         NOP
6B3B: 23         INC         HL
6B3C: C5         PUSH       BC
6B3D: 02         LD           (BC),A
6B3E: 10 C4      STOP       $C4
6B40: 03         INC         BC
6B41: 23         INC         HL
6B42: 84         ADD         A,H
6B43: 04         INC         B
6B44: 1B         DEC         DE
6B45: 84         ADD         A,H
6B46: 14         INC         D
6B47: 1B         DEC         DE
6B48: 84         ADD         A,H
6B49: 24         INC         H
6B4A: 1B         DEC         DE
6B4B: 84         ADD         A,H
6B4C: 34         INC         (HL)
6B4D: 1B         DEC         DE
6B4E: C4 08 24   CALL       NZ,$2408
6B51: C5         PUSH       BC
6B52: 09         ADD         HL,BC
6B53: 24         INC         H
6B54: 52         LD           D,D
6B55: 94         SUB         H
6B56: 53         LD           D,E
6B57: 12         LD           (DE),A
6B58: 54         LD           D,H
6B59: 16 64      LD           D,$64
6B5B: 10 43      STOP       $43
6B5D: 27         DAA
6B5E: 44         LD           B,H
6B5F: 22         LD           (HLI),A
6B60: 45         LD           B,L
6B61: 2B         DEC         HL
6B62: C4 46 1B   CALL       NZ,$1B46
6B65: 47         LD           B,A
6B66: 2C         INC         L
6B67: 48         LD           C,B
6B68: 28 C3      JR           Z,$6B2D
6B6A: 55         LD           D,L
6B6B: 23         INC         HL
6B6C: C3 57 24   JP           $2457
6B6F: 58         LD           E,B
6B70: 2C         INC         L
6B71: 59         LD           E,C
6B72: 28 C2      JR           Z,$6B36
6B74: 68         LD           L,B
6B75: 24         INC         H
6B76: C2 69 03   JP           NZ,$0369
6B79: 71         LD           (HL),C
6B7A: 0D         DEC         C
6B7B: 72         LD           (HL),D
6B7C: 2C         INC         L
6B7D: 73         LD           (HL),E
6B7E: 22         LD           (HLI),A
6B7F: 74         LD           (HL),H
6B80: 2B         DEC         HL
6B81: 10 C9      STOP       $C9
6B83: 40         LD           B,B
6B84: C9         RET
6B85: 19         ADD         HL,DE
6B86: CA 49 CA   JP           Z,$CA49
6B89: 16 A0      LD           D,$A0
6B8B: 82         ADD         A,D
6B8C: 62         LD           H,D
6B8D: 20 FE      JR           NZ,$6B8D
6B8F: 04         INC         B
6B90: 0D         DEC         C
6B91: 02         LD           (BC),A
6B92: F0 72      LD           A,($72)
6B94: F1         POP         AF
6B95: 05         DEC         B
6B96: 26 06      LD           H,$06
6B98: 2A         LD           A,(HLI)
6B99: C3 15 24   JP           $2415
6B9C: 45         LD           B,L
6B9D: 2A         LD           A,(HLI)
6B9E: 83         ADD         A,E
6B9F: 46         LD           B,(HL)
6BA0: 21 47 98   LD           HL,$9847
6BA3: 49         LD           C,C
6BA4: 26 39      LD           H,$39
6BA6: 2A         LD           A,(HLI)
6BA7: 11 20 14   LD           DE,$1420
6BAA: 20 16      JR           NZ,$6BC2
6BAC: 11 36 15   LD           DE,$1536
6BAF: 38 13      JR           C,$6BC4
6BB1: 67         LD           H,A
6BB2: 2C         INC         L
6BB3: 68         LD           L,B
6BB4: 22         LD           (HLI),A
6BB5: 69         LD           L,C
6BB6: 28 77      JR           Z,$6C2F
6BB8: 28 78      JR           Z,$6C32
6BBA: 0D         DEC         C
6BBB: 79         LD           A,C
6BBC: 2C         INC         L
6BBD: 18 BE      JR           $6B7D
6BBF: E2         LDFF00   (C),A
6BC0: 05         DEC         B
6BC1: DD                              
6BC2: 88         ADC         A,B
6BC3: 10 FE      STOP       $FE
6BC5: 04         INC         B
6BC6: 0D         DEC         C
6BC7: 04         INC         B
6BC8: F4                              
6BC9: 49         LD           C,C
6BCA: F7         RST         0X30
6BCB: 03         INC         BC
6BCC: 29         ADD         HL,HL
6BCD: 82         ADD         A,D
6BCE: 04         INC         B
6BCF: 0D         DEC         C
6BD0: 06 2A      LD           B,$2A
6BD2: 02         LD           (BC),A
6BD3: C7         RST         0X00
6BD4: 07         RLCA
6BD5: C7         RST         0X00
6BD6: C3 16 DC   JP           $DC16
6BD9: 82         ADD         A,D
6BDA: 57         LD           D,A
6BDB: DC 86 41   CALL       C,$4186
6BDE: DB                              
6BDF: C2 56 DB   JP           NZ,$DB56
6BE2: 46         LD           B,(HL)
6BE3: DC 28 A1   CALL       C,$A128
6BE6: FE 07      CP           $07
6BE8: 0D         DEC         C
6BE9: 11 8E 06   LD           DE,$068E
6BEC: F4                              
6BED: 40         LD           B,B
6BEE: F2                              
6BEF: 49         LD           C,C
6BF0: 4A         LD           C,D
6BF1: 75         LD           (HL),L
6BF2: F5         PUSH       AF
6BF3: 06 26      LD           B,$26
6BF5: 16 24      LD           D,$24
6BF7: 26 2A      LD           H,$2A
6BF9: 27         DAA
6BFA: 21 28 98   LD           HL,$9828
6BFD: 29         ADD         HL,HL
6BFE: 26 07      LD           H,$07
6C00: 11 08 0D   LD           DE,$0D08
6C03: 09         ADD         HL,BC
6C04: 10 19      STOP       $19
6C06: 14         INC         D
6C07: 02         LD           (BC),A
6C08: C7         RST         0X00
6C09: 05         DEC         B
6C0A: C7         RST         0X00
6C0B: C4 34 DB   CALL       NZ,$DB34
6C0E: 83         ADD         A,E
6C0F: 41         LD           B,C
6C10: DC 35 DB   CALL       C,$DB35
6C13: 71         LD           (HL),C
6C14: 2B         DEC         HL
6C15: 77         LD           (HL),A
6C16: 2B         DEC         HL
6C17: 72         LD           (HL),D
6C18: 0D         DEC         C
6C19: 76         HALT
6C1A: 0D         DEC         C
6C1B: 73         LD           (HL),E
6C1C: 2C         INC         L
6C1D: 77         LD           (HL),A
6C1E: 2C         INC         L
6C1F: 75         LD           (HL),L
6C20: 2B         DEC         HL
6C21: 82         ADD         A,D
6C22: 12         LD           (DE),A
6C23: 20 23      JR           NZ,$6C48
6C25: 20 25      JR           NZ,$6C4C
6C27: 20 61      JR           NZ,$6C8A
6C29: 20 39      JR           NZ,$6C64
6C2B: CA 59 CA   JP           Z,$CA59
6C2E: 83         ADD         A,E
6C2F: 46         LD           B,(HL)
6C30: 0F         RRCA
6C31: C3 56 0F   JP           $0F56
6C34: FE 07      CP           $07
6C36: 07         RLCA
6C37: 40         LD           B,B
6C38: DC 40 41   CALL       C,$4140
6C3B: 22         LD           (HLI),A
6C3C: AB         XOR         E
6C3D: 26 AB      LD           H,$AB
6C3F: 85         ADD         A,L
6C40: 32         LD           (HLD),A
6C41: A6         AND         (HL)
6C42: 44         LD           B,H
6C43: A6         AND         (HL)
6C44: 83         ADD         A,E
6C45: 54         LD           D,H
6C46: A6         AND         (HL)
6C47: 83         ADD         A,E
6C48: 62         LD           H,D
6C49: A6         AND         (HL)
6C4A: 66         LD           H,(HL)
6C4B: A6         AND         (HL)
6C4C: 18 BF      JR           $6C0D
6C4E: E2         LDFF00   (C),A
6C4F: 05         DEC         B
6C50: D9         RETI
6C51: 88         ADC         A,B
6C52: 10 FE      STOP       $FE
6C54: 04         INC         B
6C55: 0D         DEC         C
6C56: 03         INC         BC
6C57: C7         RST         0X00
6C58: 06 C7      LD           B,$C7
6C5A: 07         RLCA
6C5B: F4                              
6C5C: 76         HALT
6C5D: F5         PUSH       AF
6C5E: 07         RLCA
6C5F: 29         ADD         HL,HL
6C60: 08 0D 09   LD           ($090D),SP
6C63: 24         INC         H
6C64: 18 DE      JR           $6C44
6C66: 13         INC         DE
6C67: DA 16 DA   JP           C,$DA16
6C6A: 22         LD           (HLI),A
6C6B: DA 27 DA   JP           C,$DA27
6C6E: 31 DA 33   LD           SP,$33DA
6C71: DA 36 DA   JP           C,$DA36
6C74: 38 DA      JR           C,$6C50
6C76: 42         LD           B,D
6C77: DA 82 44   JP           C,$4482
6C7A: DA 47 DA   JP           C,$DA47
6C7D: 53         LD           D,E
6C7E: DA 56 DA   JP           C,$DA56
6C81: 82         ADD         A,D
6C82: 64         LD           H,H
6C83: DA 11 BE   JP           C,$BE11
6C86: E2         LDFF00   (C),A
6C87: 05         DEC         B
6C88: DA 18 13   JP           C,$1318
6C8B: 32         LD           (HLD),A
6C8C: 0F         RRCA
6C8D: FE 04      CP           $04
6C8F: 0D         DEC         C
6C90: 03         INC         BC
6C91: C7         RST         0X00
6C92: 04         INC         B
6C93: F8 06      LDHL       SP,$06
6C95: C7         RST         0X00
6C96: 74         LD           (HL),H
6C97: F1         POP         AF
6C98: 82         ADD         A,D
6C99: 32         LD           (HLD),A
6C9A: AC         XOR         H
6C9B: 82         ADD         A,D
6C9C: 36 AC      LD           (HL),$AC
6C9E: 82         ADD         A,D
6C9F: 42         LD           B,D
6CA0: AC         XOR         H
6CA1: 82         ADD         A,D
6CA2: 46         LD           B,(HL)
6CA3: AC         XOR         H
6CA4: 42         LD           B,D
6CA5: AB         XOR         E
6CA6: 47         LD           B,A
6CA7: AB         XOR         E
6CA8: FE 04      CP           $04
6CAA: 0D         DEC         C
6CAB: 04         INC         B
6CAC: F0 74      LD           A,($74)
6CAE: 40         LD           B,B
6CAF: 03         INC         BC
6CB0: C7         RST         0X00
6CB1: 06 C7      LD           B,$C7
6CB3: 84         ADD         A,H
6CB4: 13         INC         DE
6CB5: 0F         RRCA
6CB6: 22         LD           (HLI),A
6CB7: 0F         RRCA
6CB8: 27         DAA
6CB9: 0F         RRCA
6CBA: 31 0F 82   LD           SP,$820F
6CBD: 34         INC         (HL)
6CBE: 0F         RRCA
6CBF: 38 0F      JR           C,$6CD0
6CC1: 42         LD           B,D
6CC2: 0F         RRCA
6CC3: 82         ADD         A,D
6CC4: 44         LD           B,H
6CC5: 0F         RRCA
6CC6: 47         LD           B,A
6CC7: 0F         RRCA
6CC8: 84         ADD         A,H
6CC9: 53         LD           D,E
6CCA: 0F         RRCA
6CCB: FE 0C      CP           $0C
6CCD: 0D         DEC         C
6CCE: 05         DEC         B
6CCF: F4                              
6CD0: 49         LD           C,C
6CD1: F7         RST         0X30
6CD2: 71         LD           (HL),C
6CD3: F5         PUSH       AF
6CD4: 00         NOP
6CD5: 23         INC         HL
6CD6: 01 0D 02   LD           BC,$020D
6CD9: 2A         LD           A,(HLI)
6CDA: 04         INC         B
6CDB: 29         ADD         HL,HL
6CDC: 05         DEC         B
6CDD: 23         INC         HL
6CDE: C2 06 1B   JP           NZ,$1B06
6CE1: C6 07      ADD         $07
6CE3: 24         INC         H
6CE4: 08 2A C2   LD           ($C22A),SP
6CE7: 13         INC         DE
6CE8: 10 04      STOP       $04
6CEA: 29         ADD         HL,HL
6CEB: 05         DEC         B
6CEC: 23         INC         HL
6CED: 15         DEC         D
6CEE: 29         ADD         HL,HL
6CEF: 14         INC         D
6CF0: 25         DEC         H
6CF1: C6 18      ADD         $18
6CF3: 11 22 A6   LD           DE,$A622
6CF6: C2 24 23   JP           NZ,$2324
6CF9: C3 25 1B   JP           $1B25
6CFC: C3 26 1B   JP           $1B26
6CFF: 82         ADD         A,D
6D00: 31 13 33   LD           SP,$3313
6D03: 14         INC         D
6D04: 41         LD           B,C
6D05: 25         DEC         H
6D06: 82         ADD         A,D
6D07: 42         LD           B,D
6D08: 21 44 29   LD           HL,$2944
6D0B: C3 51 23   JP           $2351
6D0E: 85         ADD         A,L
6D0F: 52         LD           D,D
6D10: 1B         DEC         DE
6D11: C2 62 1B   JP           NZ,$1B62
6D14: 63         LD           H,E
6D15: 2C         INC         L
6D16: 83         ADD         A,E
6D17: 64         LD           H,H
6D18: 22         LD           (HLI),A
6D19: 67         LD           H,A
6D1A: 28 70      JR           Z,$6D8C
6D1C: 23         INC         HL
6D1D: 71         LD           (HL),C
6D1E: 23         INC         HL
6D1F: 73         LD           (HL),E
6D20: 24         INC         H
6D21: 74         LD           (HL),H
6D22: 2C         INC         L
6D23: 23         INC         HL
6D24: 0D         DEC         C
6D25: 28 0D      JR           Z,$6D34
6D27: 11 DE 40   LD           DE,$40DE
6D2A: C9         RET
6D2B: FE 0C      CP           $0C
6D2D: 0D         DEC         C
6D2E: 02         LD           (BC),A
6D2F: F0 40      LD           A,($40)
6D31: F2                              
6D32: 11 AE 61   LD           DE,$61AE
6D35: AE         XOR         (HL)
6D36: 68         LD           L,B
6D37: AE         XOR         (HL)
6D38: 33         INC         SP
6D39: AF         XOR         A
6D3A: 35         DEC         (HL)
6D3B: AF         XOR         A
6D3C: 43         LD           B,E
6D3D: B0         OR           B
6D3E: 45         LD           B,L
6D3F: B0         OR           B
6D40: 07         RLCA
6D41: 26 08      LD           H,$08
6D43: 0D         DEC         C
6D44: 09         ADD         HL,BC
6D45: 2A         LD           A,(HLI)
6D46: 17         RLA
6D47: 2A         LD           A,(HLI)
6D48: 18 98      JR           $6CE2
6D4A: 19         ADD         HL,DE
6D4B: 26 27      LD           H,$27
6D4D: AF         XOR         A
6D4E: 37         SCF
6D4F: B0         OR           B
6D50: 38 AE      JR           C,$6D00
6D52: FE 04      CP           $04
6D54: 0D         DEC         C
6D55: 02         LD           (BC),A
6D56: F4                              
6D57: 19         ADD         HL,DE
6D58: F3         DI
6D59: 74         LD           (HL),H
6D5A: FB         EI
6D5B: C7         RST         0X00
6D5C: 06 0F      LD           B,$0F
6D5E: 84         ADD         A,H
6D5F: 66         LD           H,(HL)
6D60: 0F         RRCA
6D61: 01 29 02   LD           BC,$0229
6D64: 0D         DEC         C
6D65: 03         INC         BC
6D66: 24         INC         H
6D67: 04         INC         B
6D68: 03         INC         BC
6D69: 05         DEC         B
6D6A: 23         INC         HL
6D6B: 07         RLCA
6D6C: 2A         LD           A,(HLI)
6D6D: 12         LD           (DE),A
6D6E: DB                              
6D6F: 13         INC         DE
6D70: 2A         LD           A,(HLI)
6D71: 14         INC         D
6D72: C7         RST         0X00
6D73: 15         DEC         D
6D74: 29         ADD         HL,HL
6D75: 16 DB      LD           D,$DB
6D77: 52         LD           D,D
6D78: DB                              
6D79: 56         LD           D,(HL)
6D7A: DB                              
6D7B: 83         ADD         A,E
6D7C: 23         INC         HL
6D7D: 0F         RRCA
6D7E: 83         ADD         A,E
6D7F: 33         INC         SP
6D80: 0F         RRCA
6D81: 83         ADD         A,E
6D82: 43         LD           B,E
6D83: 0F         RRCA
6D84: 59         LD           E,C
6D85: 2A         LD           A,(HLI)
6D86: 79         LD           A,C
6D87: 22         LD           (HLI),A
6D88: 30 C9      JR           NC,$6D53
6D8A: 39         ADD         HL,SP
6D8B: CA FE 04   JP           Z,$04FE
6D8E: 0D         DEC         C
6D8F: 10 DB      STOP       $DB
6D91: 10 F6      STOP       $F6
6D93: 77         LD           (HL),A
6D94: F1         POP         AF
6D95: 02         LD           (BC),A
6D96: C7         RST         0X00
6D97: 07         RLCA
6D98: C7         RST         0X00
6D99: C3 16 0F   JP           $0F16
6D9C: 30 27      JR           NC,$6DC5
6D9E: 85         ADD         A,L
6D9F: 31 22 C3   LD           SP,$C322
6DA2: 46         LD           B,(HL)
6DA3: 23         INC         HL
6DA4: 76         HALT
6DA5: 27         DAA
6DA6: 84         ADD         A,H
6DA7: 50         LD           D,B
6DA8: 21 54 26   LD           HL,$2654
6DAB: C2 64 24   JP           NZ,$2464
6DAE: 86         ADD         A,(HL)
6DAF: 40         LD           B,B
6DB0: 03         INC         BC
6DB1: C3 55 03   JP           $0355
6DB4: 60         LD           H,B
6DB5: 0D         DEC         C
6DB6: 70         LD           (HL),B
6DB7: 2B         DEC         HL
6DB8: 83         ADD         A,E
6DB9: 71         LD           (HL),C
6DBA: 0D         DEC         C
6DBB: 82         ADD         A,D
6DBC: 17         RLA
6DBD: 0F         RRCA
6DBE: 82         ADD         A,D
6DBF: 27         DAA
6DC0: 0F         RRCA
6DC1: 82         ADD         A,D
6DC2: 37         SCF
6DC3: 0F         RRCA
6DC4: 52         LD           D,D
6DC5: C7         RST         0X00
6DC6: 27         DAA
6DC7: A0         AND         B
6DC8: 35         DEC         (HL)
6DC9: 2B         DEC         HL
6DCA: 45         LD           B,L
6DCB: 27         DAA
6DCC: 46         LD           B,(HL)
6DCD: 2B         DEC         HL
6DCE: 83         ADD         A,E
6DCF: 60         LD           H,B
6DD0: 0F         RRCA
6DD1: 72         LD           (HL),D
6DD2: 0F         RRCA
6DD3: FE 04      CP           $04
6DD5: 0D         DEC         C
6DD6: 06 F0      LD           B,$F0
6DD8: 59         LD           E,C
6DD9: F3         DI
6DDA: 21 AC 27   LD           HL,$27AC
6DDD: AC         XOR         H
6DDE: 61         LD           H,C
6DDF: AC         XOR         H
6DE0: 67         LD           H,A
6DE1: AC         XOR         H
6DE2: 33         INC         SP
6DE3: AF         XOR         A
6DE4: 34         INC         (HL)
6DE5: AE         XOR         (HL)
6DE6: 35         DEC         (HL)
6DE7: AF         XOR         A
6DE8: 43         LD           B,E
6DE9: 01 45 01   LD           BC,$0145
6DEC: 53         LD           D,E
6DED: B0         OR           B
6DEE: 54         LD           D,H
6DEF: AE         XOR         (HL)
6DF0: 55         LD           D,L
6DF1: B0         OR           B
6DF2: 85         ADD         A,L
6DF3: 00         NOP
6DF4: 03         INC         BC
6DF5: 05         DEC         B
6DF6: 25         DEC         H
6DF7: 08 26 09   LD           ($0926),SP
6DFA: 03         INC         BC
6DFB: 10 25      STOP       $25
6DFD: 84         ADD         A,H
6DFE: 11 21 15   LD           DE,$1521
6E01: 29         ADD         HL,HL
6E02: 18 2A      JR           $6E2E
6E04: 19         ADD         HL,DE
6E05: 26 E1      LD           H,$E1
6E07: 05         DEC         B
6E08: D4 50 7C   CALL       NC,$7C50
6E0B: FE 04      CP           $04
6E0D: 0D         DEC         C
6E0E: 04         INC         B
6E0F: F0 50      LD           A,($50)
6E11: F2                              
6E12: 11 AC 18   LD           DE,$18AC
6E15: AC         XOR         H
6E16: 21 AF 22   LD           HL,$22AF
6E19: A7         AND         A
6E1A: 84         ADD         A,H
6E1B: 23         INC         HL
6E1C: 13         INC         DE
6E1D: 37         SCF
6E1E: A7         AND         A
6E1F: 28 AF      JR           Z,$6DD0
6E21: 31 B0 38   LD           SP,$38B0
6E24: B0         OR           B
6E25: 86         ADD         A,(HL)
6E26: 42         LD           B,D
6E27: AE         XOR         (HL)
6E28: 54         LD           D,H
6E29: A7         AND         A
6E2A: 65         LD           H,L
6E2B: A7         AND         A
6E2C: FE 04      CP           $04
6E2E: 0D         DEC         C
6E2F: 04         INC         B
6E30: 3F         CCF
6E31: 74         LD           (HL),H
6E32: ED                              
6E33: 11 AC 18   LD           DE,$18AC
6E36: AC         XOR         H
6E37: 61         LD           H,C
6E38: AC         XOR         H
6E39: 68         LD           L,B
6E3A: AC         XOR         H
6E3B: 04         INC         B
6E3C: 47         LD           B,A
6E3D: C2 32 20   JP           NZ,$2032
6E40: C2 37 20   JP           NZ,$2037
6E43: FE 0C      CP           $0C
6E45: 0D         DEC         C
6E46: 00         NOP
6E47: 23         INC         HL
6E48: 01 F4 77   LD           BC,$77F4
6E4B: F5         PUSH       AF
6E4C: C6 01      ADD         $01
6E4E: 23         INC         HL
6E4F: C5         PUSH       BC
6E50: 02         LD           (BC),A
6E51: 1B         DEC         DE
6E52: C4 03 24   CALL       NZ,$2403
6E55: 04         INC         B
6E56: 2A         LD           A,(HLI)
6E57: 07         RLCA
6E58: C7         RST         0X00
6E59: C2 14 11   JP           NZ,$1114
6E5C: 34         INC         (HL)
6E5D: 15         DEC         D
6E5E: 36 13      LD           (HL),$13
6E60: 37         SCF
6E61: 95         SUB         L
6E62: 43         LD           B,E
6E63: 2A         LD           A,(HLI)
6E64: 44         LD           B,H
6E65: 21 45 98   LD           HL,$9845
6E68: 46         LD           B,(HL)
6E69: 26 C3      LD           H,$C3
6E6B: 47         LD           B,A
6E6C: 11 84 52   LD           DE,$5284
6E6F: 1B         DEC         DE
6E70: 56         LD           D,(HL)
6E71: 24         INC         H
6E72: 61         LD           H,C
6E73: 27         DAA
6E74: 84         ADD         A,H
6E75: 62         LD           H,D
6E76: 22         LD           (HLI),A
6E77: 66         LD           H,(HL)
6E78: 28 73      JR           Z,$6EED
6E7A: C8         RET         Z
6E7B: 76         HALT
6E7C: C8         RET         Z
6E7D: 83         ADD         A,E
6E7E: 16 20      LD           D,$20
6E80: FE 04      CP           $04
6E82: 0D         DEC         C
6E83: 04         INC         B
6E84: FA 74 F5   LD           A,($F574)
6E87: 00         NOP
6E88: 17         RLA
6E89: 01 12 02   LD           BC,$0212
6E8C: 16 03      LD           D,$03
6E8E: 25         DEC         H
6E8F: 06 26      LD           B,$26
6E91: 07         RLCA
6E92: 17         RLA
6E93: 08 12 09   LD           ($0912),SP
6E96: 16 C2      LD           D,$C2
6E98: 10 11      STOP       $11
6E9A: C2 12 10   JP           NZ,$1012
6E9D: C3 13 23   JP           $2313
6EA0: C3 16 24   JP           $2416
6EA3: C2 17 11   JP           NZ,$1117
6EA6: 18 20      JR           $6EC8
6EA8: C2 19 10   JP           NZ,$1019
6EAB: 30 AC      JR           NC,$6E59
6EAD: 32         LD           (HLD),A
6EAE: AC         XOR         H
6EAF: 37         SCF
6EB0: AC         XOR         H
6EB1: 39         ADD         HL,SP
6EB2: AC         XOR         H
6EB3: 40         LD           B,B
6EB4: 25         DEC         H
6EB5: 41         LD           B,C
6EB6: 98         SBC         B
6EB7: 42         LD           B,D
6EB8: 21 43 29   LD           HL,$2943
6EBB: 46         LD           B,(HL)
6EBC: 2A         LD           A,(HLI)
6EBD: 47         LD           B,A
6EBE: 21 48 98   LD           HL,$9848
6EC1: 49         LD           C,C
6EC2: 26 11      LD           H,$11
6EC4: A0         AND         B
6EC5: FE 04      CP           $04
6EC7: 1D         DEC         E
6EC8: 07         RLCA
6EC9: F4                              
6ECA: 20 C9      JR           NZ,$6E95
6ECC: 50         LD           D,B
6ECD: C9         RET
6ECE: 77         LD           (HL),A
6ECF: F5         PUSH       AF
6ED0: C7         RST         0X00
6ED1: 04         INC         B
6ED2: 24         INC         H
6ED3: C8         RET         Z
6ED4: 05         DEC         B
6ED5: 03         INC         BC
6ED6: C7         RST         0X00
6ED7: 06 23      LD           B,$23
6ED9: 06 25      LD           B,$25
6EDB: 09         ADD         HL,BC
6EDC: 26 71      LD           H,$71
6EDE: 2B         DEC         HL
6EDF: 72         LD           (HL),D
6EE0: 0D         DEC         C
6EE1: 73         LD           (HL),E
6EE2: 2C         INC         L
6EE3: 74         LD           (HL),H
6EE4: 28 76      JR           Z,$6F5C
6EE6: 27         DAA
6EE7: 82         ADD         A,D
6EE8: 27         DAA
6EE9: 0F         RRCA
6EEA: 82         ADD         A,D
6EEB: 37         SCF
6EEC: 0F         RRCA
6EED: 82         ADD         A,D
6EEE: 47         LD           B,A
6EEF: 0F         RRCA
6EF0: 24         INC         H
6EF1: CA 54 CA   JP           Z,$CA54
6EF4: 37         SCF
6EF5: A0         AND         B
6EF6: C8         RET         Z
6EF7: 02         LD           (BC),A
6EF8: 0F         RRCA
6EF9: FE 04      CP           $04
6EFB: 0D         DEC         C
6EFC: 04         INC         B
6EFD: EC                              
6EFE: 49         LD           C,C
6EFF: F3         DI
6F00: 74         LD           (HL),H
6F01: F5         PUSH       AF
6F02: 13         INC         DE
6F03: C0         RET         NZ
6F04: 16 C0      LD           D,$C0
6F06: 82         ADD         A,D
6F07: 00         NOP
6F08: 03         INC         BC
6F09: 82         ADD         A,D
6F0A: 08 03 02   LD           ($0203),SP
6F0D: 25         DEC         H
6F0E: 07         RLCA
6F0F: 26 10      LD           H,$10
6F11: 25         DEC         H
6F12: 11 21 12   LD           DE,$1221
6F15: 29         ADD         HL,HL
6F16: 17         RLA
6F17: 2A         LD           A,(HLI)
6F18: 18 21      JR           $6F3B
6F1A: 19         ADD         HL,DE
6F1B: 26 FE      LD           H,$FE
6F1D: 0C         INC         C
6F1E: 0D         DEC         C
6F1F: 07         RLCA
6F20: DB                              
6F21: 07         RLCA
6F22: F0 40      LD           A,($40)
6F24: F2                              
6F25: 73         LD           (HL),E
6F26: F1         POP         AF
6F27: 47         LD           B,A
6F28: 2C         INC         L
6F29: 48         LD           C,B
6F2A: 22         LD           (HLI),A
6F2B: 49         LD           C,C
6F2C: 28 C2      JR           Z,$6EF0
6F2E: 57         LD           D,A
6F2F: 24         INC         H
6F30: 77         LD           (HL),A
6F31: 28 59      JR           Z,$6F8C
6F33: 2C         INC         L
6F34: 78         LD           A,B
6F35: 0D         DEC         C
6F36: 79         LD           A,C
6F37: 24         INC         H
6F38: 02         LD           (BC),A
6F39: C7         RST         0X00
6F3A: C3 58 0F   JP           $0F58
6F3D: 58         LD           E,B
6F3E: A0         AND         B
6F3F: 82         ADD         A,D
6F40: 00         NOP
6F41: 03         INC         BC
6F42: 02         LD           (BC),A
6F43: 25         DEC         H
6F44: 10 25      STOP       $25
6F46: 11 21 12   LD           DE,$1221
6F49: 29         ADD         HL,HL
6F4A: 82         ADD         A,D
6F4B: 17         RLA
6F4C: 0F         RRCA
6F4D: 82         ADD         A,D
6F4E: 61         LD           H,C
6F4F: 0F         RRCA
6F50: FE 04      CP           $04
6F52: 0D         DEC         C
6F53: 04         INC         B
6F54: F0 03      LD           A,($03)
6F56: C7         RST         0X00
6F57: 06 C7      LD           B,$C7
6F59: 83         ADD         A,E
6F5A: 32         LD           (HLD),A
6F5B: 0F         RRCA
6F5C: 83         ADD         A,E
6F5D: 42         LD           B,D
6F5E: 0F         RRCA
6F5F: 83         ADD         A,E
6F60: 52         LD           D,D
6F61: 0F         RRCA
6F62: 85         ADD         A,L
6F63: 21 DC C3   LD           HL,$C3DC
6F66: 35         DEC         (HL)
6F67: DC C3 31   CALL       C,$31C3
6F6A: DC 85 61   CALL       C,$6185
6F6D: DC 43 BE   CALL       C,$BE43
6F70: E2         LDFF00   (C),A
6F71: 05         DEC         B
6F72: D8         RET         C
6F73: 18 10      JR           $6F85
6F75: FE 04      CP           $04
6F77: 0D         DEC         C
6F78: 07         RLCA
6F79: F0 39      LD           A,($39)
6F7B: F7         RST         0X30
6F7C: 01 29 02   LD           BC,$0229
6F7F: 0D         DEC         C
6F80: 03         INC         BC
6F81: 2A         LD           A,(HLI)
6F82: 29         ADD         HL,HL
6F83: 2A         LD           A,(HLI)
6F84: C2 39 0D   JP           NZ,$0D39
6F87: 59         LD           E,C
6F88: 2C         INC         L
6F89: 22         LD           (HLI),A
6F8A: AC         XOR         H
6F8B: 83         ADD         A,E
6F8C: 23         INC         HL
6F8D: 0F         RRCA
6F8E: 26 AC      LD           H,$AC
6F90: C2 32 0F   JP           NZ,$0F32
6F93: C2 36 0F   JP           NZ,$0F36
6F96: 52         LD           D,D
6F97: AC         XOR         H
6F98: 83         ADD         A,E
6F99: 53         LD           D,E
6F9A: 0F         RRCA
6F9B: 56         LD           D,(HL)
6F9C: AC         XOR         H
6F9D: C2 02 0F   JP           NZ,$0F02
6FA0: FE 07      CP           $07
6FA2: 0D         DEC         C
6FA3: 30 D0      JR           NC,$6F75
6FA5: 30 F6      JR           NC,$6F9D
6FA7: 39         ADD         HL,SP
6FA8: F7         RST         0X30
6FA9: 11 AC 18   LD           DE,$18AC
6FAC: AC         XOR         H
6FAD: 61         LD           H,C
6FAE: AC         XOR         H
6FAF: 68         LD           L,B
6FB0: AC         XOR         H
6FB1: 20 29      JR           NZ,$6FDC
6FB3: 29         ADD         HL,HL
6FB4: 2A         LD           A,(HLI)
6FB5: C2 30 0D   JP           NZ,$0D30
6FB8: C2 39 0D   JP           NZ,$0D39
6FBB: 50         LD           D,B
6FBC: 2B         DEC         HL
6FBD: 59         LD           E,C
6FBE: 2C         INC         L
6FBF: C3 32 C0   JP           $C032
6FC2: C3 37 C0   JP           $C037
6FC5: 53         LD           D,E
6FC6: FC                              
6FC7: E0 00      LDFF00   ($00),A
6FC9: 8C         ADC         A,H
6FCA: 38 40      JR           C,$700C
6FCC: FE 07      CP           $07
6FCE: 0D         DEC         C
6FCF: 30 F6      JR           NC,$6FC7
6FD1: 39         ADD         HL,SP
6FD2: F7         RST         0X30
6FD3: 82         ADD         A,D
6FD4: 00         NOP
6FD5: 03         INC         BC
6FD6: 02         LD           (BC),A
6FD7: 25         DEC         H
6FD8: 04         INC         B
6FD9: 26 05      LD           H,$05
6FDB: 25         DEC         H
6FDC: 07         RLCA
6FDD: 26 82      LD           H,$82
6FDF: 08 03 82   LD           ($8203),SP
6FE2: 10 03      STOP       $03
6FE4: 12         LD           (DE),A
6FE5: 23         INC         HL
6FE6: 14         INC         D
6FE7: 24         INC         H
6FE8: 15         DEC         D
6FE9: 23         INC         HL
6FEA: 17         RLA
6FEB: 24         INC         H
6FEC: 82         ADD         A,D
6FED: 18 03      JR           $6FF2
6FEF: 82         ADD         A,D
6FF0: 20 21      JR           NZ,$7013
6FF2: 22         LD           (HLI),A
6FF3: 29         ADD         HL,HL
6FF4: 24         INC         H
6FF5: 2A         LD           A,(HLI)
6FF6: 25         DEC         H
6FF7: 29         ADD         HL,HL
6FF8: 27         DAA
6FF9: 2A         LD           A,(HLI)
6FFA: 82         ADD         A,D
6FFB: 28 21      JR           Z,$701E
6FFD: C2 30 0D   JP           NZ,$0D30
7000: C2 39 0D   JP           NZ,$0D39
7003: 82         ADD         A,D
7004: 50         LD           D,B
7005: 22         LD           (HLI),A
7006: 52         LD           D,D
7007: 2B         DEC         HL
7008: 57         LD           D,A
7009: 2C         INC         L
700A: 82         ADD         A,D
700B: 58         LD           E,B
700C: 22         LD           (HLI),A
700D: 8A         ADC         A,D
700E: 60         LD           H,B
700F: 03         INC         BC
7010: 62         LD           H,D
7011: 23         INC         HL
7012: 67         LD           H,A
7013: 24         INC         H
7014: 82         ADD         A,D
7015: 70         LD           (HL),B
7016: 03         INC         BC
7017: 72         LD           (HL),D
7018: 27         DAA
7019: 77         LD           (HL),A
701A: 28 82      JR           Z,$6F9E
701C: 78         LD           A,B
701D: 03         INC         BC
701E: 83         ADD         A,E
701F: 33         INC         SP
7020: D2 C3 34   JP           NC,$34C3
7023: CF         RST         0X08
7024: C2 36 CF   JP           NZ,$CF36
7027: C3 43 D0   JP           $D043
702A: C2 45 D0   JP           NZ,$D045
702D: 56         LD           D,(HL)
702E: D1         POP         DE
702F: 64         LD           H,H
7030: D1         POP         DE
7031: 82         ADD         A,D
7032: 65         LD           H,L
7033: AE         XOR         (HL)
7034: FE 07      CP           $07
7036: 0D         DEC         C
7037: 04         INC         B
7038: D0         RET         NC
7039: 04         INC         B
703A: AA         XOR         D
703B: 04         INC         B
703C: F0 30      LD           A,($30)
703E: F6 03      OR           $03
7040: C7         RST         0X00
7041: 06 C7      LD           B,$C7
7043: 20 29      JR           NZ,$706E
7045: C2 30 0D   JP           NZ,$0D30
7048: 50         LD           D,B
7049: 2B         DEC         HL
704A: 61         LD           H,C
704B: 20 68      JR           NZ,$70B5
704D: 20 84      JR           NZ,$6FD3
704F: 23         INC         HL
7050: DA 82 32   JP           C,$3282
7053: DA 82 36   JP           C,$3682
7056: DA 82 42   JP           C,$4282
7059: DA 82 46   JP           C,$4682
705C: DA 84 53   JP           C,$5384
705F: DA FE 04   JP           C,$04FE
7062: 0D         DEC         C
7063: 03         INC         BC
7064: F0 02      LD           A,($02)
7066: C7         RST         0X00
7067: 05         DEC         B
7068: C7         RST         0X00
7069: 07         RLCA
706A: 26 C6      LD           H,$C6
706C: 08 0F 09   LD           ($090F),SP
706F: 24         INC         H
7070: C4 17 24   CALL       NZ,$2417
7073: 22         LD           (HLI),A
7074: DC 26 DC   CALL       C,$DC26
7077: 31 DC 83   LD           SP,$83DC
707A: 33         INC         SP
707B: DC 40 27   CALL       C,$2740
707E: 41         LD           B,C
707F: 98         SBC         B
7080: 42         LD           B,D
7081: 2B         DEC         HL
7082: 83         ADD         A,E
7083: 43         LD           B,E
7084: DB                              
7085: 44         LD           B,H
7086: DC 50 2B   CALL       C,$2B50
7089: 51         LD           D,C
708A: 0F         RRCA
708B: 52         LD           D,D
708C: 23         INC         HL
708D: 53         LD           D,E
708E: DB                              
708F: 54         LD           D,H
7090: 2C         INC         L
7091: 55         LD           D,L
7092: 98         SBC         B
7093: 56         LD           D,(HL)
7094: 22         LD           (HLI),A
7095: 57         LD           D,A
7096: 28 61      JR           Z,$70F9
7098: C0         RET         NZ
7099: 62         LD           H,D
709A: 27         DAA
709B: 63         LD           H,E
709C: 22         LD           (HLI),A
709D: 64         LD           H,H
709E: 28 84      JR           Z,$7024
70A0: 65         LD           H,L
70A1: 0F         RRCA
70A2: C2 50 C0   JP           NZ,$C050
70A5: 70         LD           (HL),B
70A6: 2C         INC         L
70A7: 11 20 FE   LD           DE,$FE20
70AA: 05         DEC         B
70AB: 94         SUB         H
70AC: 8A         ADC         A,D
70AD: 00         NOP
70AE: 68         LD           L,B
70AF: C3 01 65   JP           $6501
70B2: C6 10      ADD         $10
70B4: 68         LD           L,B
70B5: 83         ADD         A,E
70B6: 14         INC         D
70B7: 6B         LD           L,E
70B8: 15         DEC         D
70B9: 69         LD           L,C
70BA: 83         ADD         A,E
70BB: 24         INC         H
70BC: 69         LD           L,C
70BD: 25         DEC         H
70BE: 82         ADD         A,D
70BF: 38 64      JR           C,$7125
70C1: 82         ADD         A,D
70C2: 45         LD           B,L
70C3: 64         LD           H,H
70C4: C3 48 65   JP           $6548
70C7: C3 39 68   JP           $6839
70CA: 69         LD           L,C
70CB: 68         LD           L,B
70CC: 89         ADC         A,C
70CD: 70         LD           (HL),B
70CE: 68         LD           L,B
70CF: 79         LD           A,C
70D0: 68         LD           L,B
70D1: 82         ADD         A,D
70D2: 31 68 33   LD           SP,$3368
70D5: 64         LD           H,H
70D6: 83         ADD         A,E
70D7: 41         LD           B,C
70D8: 64         LD           H,H
70D9: C2 51 65   JP           NZ,$6551
70DC: E1         POP         HL
70DD: 05         DEC         B
70DE: D2 38 50   JP           NC,$5038
70E1: FE 05      CP           $05
70E3: 94         SUB         H
70E4: 8A         ADC         A,D
70E5: 00         NOP
70E6: 68         LD           L,B
70E7: C6 08      ADD         $08
70E9: 65         LD           H,L
70EA: 83         ADD         A,E
70EB: 11 6B 12   LD           DE,$126B
70EE: 69         LD           L,C
70EF: 83         ADD         A,E
70F0: 21 69 22   LD           HL,$2269
70F3: 82         ADD         A,D
70F4: 14         INC         D
70F5: 68         LD           L,B
70F6: 15         DEC         D
70F7: 68         LD           L,B
70F8: C5         PUSH       BC
70F9: 19         ADD         HL,DE
70FA: 68         LD           L,B
70FB: 30 68      JR           NC,$7165
70FD: 31 64 C2   LD           SP,$C264
7100: 41         LD           B,C
7101: 65         LD           H,L
7102: 82         ADD         A,D
7103: 24         INC         H
7104: 68         LD           L,B
7105: 82         ADD         A,D
7106: 44         LD           B,H
7107: 64         LD           H,H
7108: C2 40 68   JP           NZ,$6840
710B: 8A         ADC         A,D
710C: 60         LD           H,B
710D: 68         LD           L,B
710E: 84         ADD         A,H
710F: 63         LD           H,E
7110: 04         INC         B
7111: 63         LD           H,E
7112: 75         LD           (HL),L
7113: 8A         ADC         A,D
7114: 70         LD           (HL),B
7115: 68         LD           L,B
7116: 84         ADD         A,H
7117: 73         LD           (HL),E
7118: 68         LD           L,B
7119: 82         ADD         A,D
711A: 70         LD           (HL),B
711B: 60         LD           H,B
711C: 82         ADD         A,D
711D: 78         LD           A,B
711E: 60         LD           H,B
711F: E1         POP         HL
7120: 05         DEC         B
7121: C2 88 20   JP           NZ,$2088
7124: FE 05      CP           $05
7126: 94         SUB         H
7127: 12         LD           (DE),A
7128: 69         LD           L,C
7129: 22         LD           (HLI),A
712A: 82         ADD         A,D
712B: 14         INC         D
712C: 69         LD           L,C
712D: 24         INC         H
712E: 82         ADD         A,D
712F: 16 69      LD           D,$69
7131: 26 82      LD           H,$82
7133: 8A         ADC         A,D
7134: 00         NOP
7135: 68         LD           L,B
7136: C5         PUSH       BC
7137: 01 63 C6   LD           BC,$C663
713A: 10 68      STOP       $68
713C: C4 13 65   CALL       NZ,$6513
713F: C4 15 65   CALL       NZ,$6515
7142: C5         PUSH       BC
7143: 17         RLA
7144: 65         LD           H,L
7145: 82         ADD         A,D
7146: 38 68      JR           C,$71B0
7148: C3 48 68   JP           $6848
714B: C3 49 54   JP           $5449
714E: 87         ADD         A,A
714F: 61         LD           H,C
7150: 4C         LD           C,H
7151: 8A         ADC         A,D
7152: 70         LD           (HL),B
7153: 68         LD           L,B
7154: 37         SCF
7155: 64         LD           H,H
7156: 65         LD           H,L
7157: 68         LD           L,B
7158: C4 49 60   CALL       NZ,$6049
715B: E1         POP         HL
715C: 05         DEC         B
715D: C3 18 20   JP           $2018
7160: FE 05      CP           $05
7162: 94         SUB         H
7163: 8A         ADC         A,D
7164: 00         NOP
7165: 68         LD           L,B
7166: C2 08 63   JP           NZ,$6308
7169: 13         INC         DE
716A: 64         LD           H,H
716B: C6 19      ADD         $19
716D: 68         LD           L,B
716E: 82         ADD         A,D
716F: 30 68      JR           NC,$71D9
7171: 33         INC         SP
7172: 68         LD           L,B
7173: 82         ADD         A,D
7174: 35         DEC         (HL)
7175: 68         LD           L,B
7176: C3 38 65   JP           $6538
7179: 38 64      JR           C,$71DF
717B: C4 40 68   CALL       NZ,$6840
717E: C3 41 68   JP           $6841
7181: 43         LD           B,E
7182: 68         LD           L,B
7183: 82         ADD         A,D
7184: 45         LD           B,L
7185: 68         LD           L,B
7186: 82         ADD         A,D
7187: 62         LD           H,D
7188: 4C         LD           C,H
7189: 64         LD           H,H
718A: 68         LD           L,B
718B: 68         LD           L,B
718C: 4C         LD           C,H
718D: 89         ADC         A,C
718E: 71         LD           (HL),C
718F: 68         LD           L,B
7190: C4 40 60   CALL       NZ,$6040
7193: E1         POP         HL
7194: 05         DEC         B
7195: BD         CP           L
7196: 28 50      JR           Z,$71E8
7198: FE 05      CP           $05
719A: 94         SUB         H
719B: C6 01      ADD         $01
719D: 65         LD           H,L
719E: C6 00      ADD         $00
71A0: 68         LD           L,B
71A1: C3 02 68   JP           $6802
71A4: 87         ADD         A,A
71A5: 03         INC         BC
71A6: 60         LD           H,B
71A7: 86         ADD         A,(HL)
71A8: 13         INC         DE
71A9: 68         LD           L,B
71AA: 19         ADD         HL,DE
71AB: 60         LD           H,B
71AC: 23         INC         HL
71AD: 68         LD           L,B
71AE: 82         ADD         A,D
71AF: 28 68      JR           Z,$7219
71B1: 83         ADD         A,E
71B2: 32         LD           (HLD),A
71B3: 6B         LD           L,E
71B4: 33         INC         SP
71B5: 69         LD           L,C
71B6: 83         ADD         A,E
71B7: 42         LD           B,D
71B8: 69         LD           L,C
71B9: 43         LD           B,E
71BA: 82         ADD         A,D
71BB: 83         ADD         A,E
71BC: 37         SCF
71BD: 6B         LD           L,E
71BE: 38 69      JR           C,$7229
71C0: 83         ADD         A,E
71C1: 47         LD           B,A
71C2: 69         LD           L,C
71C3: 48         LD           C,B
71C4: 82         ADD         A,D
71C5: 8A         ADC         A,D
71C6: 60         LD           H,B
71C7: 68         LD           L,B
71C8: 8A         ADC         A,D
71C9: 70         LD           (HL),B
71CA: 60         LD           H,B
71CB: E1         POP         HL
71CC: 05         DEC         B
71CD: B9         CP           C
71CE: 38 60      JR           C,$7230
71D0: FE 05      CP           $05
71D2: 94         SUB         H
71D3: 87         ADD         A,A
71D4: 00         NOP
71D5: 60         LD           H,B
71D6: C3 07 68   JP           $6807
71D9: C6 08      ADD         $08
71DB: 65         LD           H,L
71DC: C7         RST         0X00
71DD: 09         ADD         HL,BC
71DE: 68         LD           L,B
71DF: 87         ADD         A,A
71E0: 10 68      STOP       $68
71E2: 10 60      STOP       $60
71E4: 16 60      LD           D,$60
71E6: 87         ADD         A,A
71E7: 20 68      JR           NZ,$7251
71E9: 22         LD           (HLI),A
71EA: 04         INC         B
71EB: 24         INC         H
71EC: 04         INC         B
71ED: 83         ADD         A,E
71EE: 30 6B      JR           NC,$725B
71F0: 31 69 83   LD           SP,$8369
71F3: 40         LD           B,B
71F4: 69         LD           L,C
71F5: 41         LD           B,C
71F6: 82         ADD         A,D
71F7: 83         ADD         A,E
71F8: 35         DEC         (HL)
71F9: 6B         LD           L,E
71FA: 36 69      LD           (HL),$69
71FC: 83         ADD         A,E
71FD: 45         LD           B,L
71FE: 69         LD           L,C
71FF: 46         LD           B,(HL)
7200: 82         ADD         A,D
7201: 8A         ADC         A,D
7202: 60         LD           H,B
7203: 68         LD           L,B
7204: 8A         ADC         A,D
7205: 70         LD           (HL),B
7206: 60         LD           H,B
7207: E1         POP         HL
7208: 05         DEC         B
7209: BF         CP           A
720A: 88         ADC         A,B
720B: 20 FE      JR           NZ,$720B
720D: 04         INC         B
720E: 0D         DEC         C
720F: FE 04      CP           $04
7211: 0D         DEC         C
7212: FE 0C      CP           $0C
7214: 0D         DEC         C
7215: 00         NOP
7216: DF         RST         0X18
7217: 01 25 02   LD           BC,$0225
721A: C7         RST         0X00
721B: 06 C7      LD           B,$C7
721D: 08 26 09   LD           ($0926),SP
7220: DF         RST         0X18
7221: 10 25      STOP       $25
7223: 11 29 18   LD           DE,$1829
7226: 2A         LD           A,(HLI)
7227: 19         ADD         HL,DE
7228: 26 20      LD           H,$20
722A: 29         ADD         HL,HL
722B: 21 0F 23   LD           HL,$230F
722E: 87         ADD         A,A
722F: 25         DEC         H
7230: 87         ADD         A,A
7231: 29         ADD         HL,HL
7232: 24         INC         H
7233: 30 25      JR           NC,$725A
7235: 31 21 32   LD           SP,$3221
7238: 26 33      LD           H,$33
723A: CE 34      ADC         $34
723C: 86         ADD         A,(HL)
723D: 35         DEC         (HL)
723E: CE 36      ADC         $36
7240: 25         DEC         H
7241: 37         SCF
7242: 21 38 26   LD           HL,$2638
7245: 39         ADD         HL,SP
7246: 2A         LD           A,(HLI)
7247: C2 41 1B   JP           NZ,$1B41
724A: 42         LD           B,D
724B: 24         INC         H
724C: 46         LD           B,(HL)
724D: 23         INC         HL
724E: 47         LD           B,A
724F: 0F         RRCA
7250: 48         LD           C,B
7251: 24         INC         H
7252: 49         LD           C,C
7253: 0D         DEC         C
7254: 52         LD           D,D
7255: 2A         LD           A,(HLI)
7256: 83         ADD         A,E
7257: 53         LD           D,E
7258: 21 54 98   LD           HL,$9854
725B: 56         LD           D,(HL)
725C: 29         ADD         HL,HL
725D: 58         LD           E,B
725E: 2A         LD           A,(HLI)
725F: 59         LD           E,C
7260: 26 85      LD           H,$85
7262: 61         LD           H,C
7263: 1B         DEC         DE
7264: 68         LD           L,B
7265: CB E0      SET         1,E
7267: 00         NOP
7268: E6 48      AND         $48
726A: 40         LD           B,B
726B: FE 0C      CP           $0C
726D: 0D         DEC         C
726E: 02         LD           (BC),A
726F: C7         RST         0X00
7270: 06 C7      LD           B,$C7
7272: 10 29      STOP       $29
7274: 12         LD           (DE),A
7275: 0F         RRCA
7276: 16 25      LD           D,$25
7278: 17         RLA
7279: 21 18 26   LD           HL,$2618
727C: 19         ADD         HL,DE
727D: 2A         LD           A,(HLI)
727E: 20 25      JR           NZ,$72A5
7280: 21 21 22   LD           HL,$2221
7283: 26 23      LD           H,$23
7285: 87         ADD         A,A
7286: 25         DEC         H
7287: 87         ADD         A,A
7288: C4 26 23   CALL       NZ,$2326
728B: C2 27 20   JP           NZ,$2027
728E: 38 20      JR           C,$72B0
7290: 28 2A      JR           Z,$72BC
7292: 29         ADD         HL,HL
7293: 26 C2      LD           H,$C2
7295: 32         LD           (HLD),A
7296: 24         INC         H
7297: 33         INC         SP
7298: CE 34      ADC         $34
729A: 86         ADD         A,(HL)
729B: 35         DEC         (HL)
729C: CE 52      ADC         $52
729E: 2A         LD           A,(HLI)
729F: 83         ADD         A,E
72A0: 53         LD           D,E
72A1: 21 56 29   LD           HL,$2956
72A4: 57         LD           D,A
72A5: 0F         RRCA
72A6: 87         ADD         A,A
72A7: 61         LD           H,C
72A8: 1B         DEC         DE
72A9: 68         LD           L,B
72AA: 2C         INC         L
72AB: 69         LD           L,C
72AC: 28 72      JR           Z,$7320
72AE: C8         RET         Z
72AF: 76         HALT
72B0: C8         RET         Z
72B1: 78         LD           A,B
72B2: 28 79      JR           Z,$732D
72B4: 0D         DEC         C
72B5: 54         LD           D,H
72B6: 98         SBC         B
72B7: 48         LD           C,B
72B8: CB E0      SET         1,E
72BA: 00         NOP
72BB: 52         LD           D,D
72BC: 68         LD           L,B
72BD: 30 FE      JR           NC,$72BD
72BF: 0C         INC         C
72C0: 0D         DEC         C
72C1: 02         LD           (BC),A
72C2: C7         RST         0X00
72C3: 06 C7      LD           B,$C7
72C5: 10 29      STOP       $29
72C7: 12         LD           (DE),A
72C8: 0F         RRCA
72C9: 16 25      LD           D,$25
72CB: 17         RLA
72CC: 21 18 26   LD           HL,$2618
72CF: 19         ADD         HL,DE
72D0: 2A         LD           A,(HLI)
72D1: 20 25      JR           NZ,$72F8
72D3: 21 21 22   LD           HL,$2221
72D6: 26 23      LD           H,$23
72D8: 87         ADD         A,A
72D9: 25         DEC         H
72DA: 87         ADD         A,A
72DB: C4 26 23   CALL       NZ,$2326
72DE: C2 27 20   JP           NZ,$2027
72E1: 38 20      JR           C,$7303
72E3: 28 2A      JR           Z,$730F
72E5: 29         ADD         HL,HL
72E6: 26 C2      LD           H,$C2
72E8: 32         LD           (HLD),A
72E9: 24         INC         H
72EA: 33         INC         SP
72EB: CE 34      ADC         $34
72ED: 86         ADD         A,(HL)
72EE: 35         DEC         (HL)
72EF: CE 52      ADC         $52
72F1: 2A         LD           A,(HLI)
72F2: 83         ADD         A,E
72F3: 53         LD           D,E
72F4: 21 56 29   LD           HL,$2956
72F7: 57         LD           D,A
72F8: 0F         RRCA
72F9: 87         ADD         A,A
72FA: 61         LD           H,C
72FB: 1B         DEC         DE
72FC: 68         LD           L,B
72FD: 2C         INC         L
72FE: 69         LD           L,C
72FF: 28 72      JR           Z,$7373
7301: C8         RET         Z
7302: 76         HALT
7303: C8         RET         Z
7304: 78         LD           A,B
7305: 28 79      JR           Z,$7380
7307: 0D         DEC         C
7308: 54         LD           D,H
7309: 98         SBC         B
730A: 48         LD           C,B
730B: CB E0      SET         1,E
730D: 00         NOP
730E: 04         INC         B
730F: 78         LD           A,B
7310: 70         LD           (HL),B
7311: FE 04      CP           $04
7313: 0D         DEC         C
7314: 02         LD           (BC),A
7315: 99         SBC         C
7316: C2 11 DF   JP           NZ,$DF11
7319: 12         LD           (DE),A
731A: 9A         SBC         D
731B: 83         ADD         A,E
731C: 15         DEC         D
731D: DF         RST         0X18
731E: 22         LD           (HLI),A
731F: C5         PUSH       BC
7320: 26 A6      LD           H,$A6
7322: 27         DAA
7323: CE 28      ADC         $28
7325: A6         AND         (HL)
7326: 32         LD           (HLD),A
7327: C6 38      ADD         $38
7329: 20 43      JR           NZ,$736E
732B: DF         RST         0X18
732C: 48         LD           C,B
732D: DF         RST         0X18
732E: 83         ADD         A,E
732F: 52         LD           D,D
7330: DF         RST         0X18
7331: 82         ADD         A,D
7332: 57         LD           D,A
7333: 20 82      JR           NZ,$72B7
7335: 61         LD           H,C
7336: DF         RST         0X18
7337: 82         ADD         A,D
7338: 67         LD           H,A
7339: 20 18      JR           NZ,$7353
733B: AB         XOR         E
733C: 74         LD           (HL),H
733D: FD                              
733E: E0 00      LDFF00   ($00),A
7340: F6 58      OR           $58
7342: 42         LD           B,D
7343: FE 0C      CP           $0C
7345: 05         DEC         B
7346: 00         NOP
7347: DF         RST         0X18
7348: 01 25 08   LD           BC,$0825
734B: 26 09      LD           H,$09
734D: DF         RST         0X18
734E: 10 25      STOP       $25
7350: 11 29 86   LD           DE,$8629
7353: 12         LD           (DE),A
7354: 1B         DEC         DE
7355: 18 2A      JR           $7381
7357: 19         ADD         HL,DE
7358: 26 C4      LD           H,$C4
735A: 21 1B C4   LD           HL,$C41B
735D: 22         LD           (HLI),A
735E: 1B         DEC         DE
735F: 23         INC         HL
7360: 2C         INC         L
7361: 82         ADD         A,D
7362: 24         INC         H
7363: 22         LD           (HLI),A
7364: 26 2B      LD           H,$2B
7366: C4 27 1B   CALL       NZ,$1B27
7369: C4 28 1B   CALL       NZ,$1B28
736C: 60         LD           H,B
736D: 27         DAA
736E: 61         LD           H,C
736F: 2B         DEC         HL
7370: 86         ADD         A,(HL)
7371: 62         LD           H,D
7372: 1B         DEC         DE
7373: 68         LD           L,B
7374: 2C         INC         L
7375: 69         LD           L,C
7376: 28 70      JR           Z,$73E8
7378: DF         RST         0X18
7379: 71         LD           (HL),C
737A: 27         DAA
737B: 73         LD           (HL),E
737C: 2B         DEC         HL
737D: 82         ADD         A,D
737E: 74         LD           (HL),H
737F: 0D         DEC         C
7380: 76         HALT
7381: 2C         INC         L
7382: 78         LD           A,B
7383: 28 79      JR           Z,$73FE
7385: DF         RST         0X18
7386: C2 33 24   JP           NZ,$2433
7389: C2 36 23   JP           NZ,$2336
738C: 53         LD           D,E
738D: 2A         LD           A,(HLI)
738E: 82         ADD         A,D
738F: 54         LD           D,H
7390: 97         SUB         A
7391: 56         LD           D,(HL)
7392: 29         ADD         HL,HL
7393: FE 0C      CP           $0C
7395: 95         SUB         L
7396: 00         NOP
7397: DF         RST         0X18
7398: 01 25 82   LD           BC,$8225
739B: 02         LD           (BC),A
739C: 21 04 26   LD           HL,$2604
739F: 05         DEC         B
73A0: DF         RST         0X18
73A1: 82         ADD         A,D
73A2: 06 0D      LD           B,$0D
73A4: 08 DF 10   LD           ($10DF),SP
73A7: 25         DEC         H
73A8: 11 29 14   LD           DE,$1429
73AB: 24         INC         H
73AC: 82         ADD         A,D
73AD: 15         DEC         D
73AE: DF         RST         0X18
73AF: 83         ADD         A,E
73B0: 17         RLA
73B1: 0D         DEC         C
73B2: C2 20 23   JP           NZ,$2320
73B5: 24         INC         H
73B6: 2A         LD           A,(HLI)
73B7: 25         DEC         H
73B8: 26 84      LD           H,$84
73BA: 26 DF      LD           H,$DF
73BC: 18 0D      JR           $73CB
73BE: 35         DEC         (HL)
73BF: 2A         LD           A,(HLI)
73C0: 36 26      LD           (HL),$26
73C2: 83         ADD         A,E
73C3: 37         SCF
73C4: DF         RST         0X18
73C5: 40         LD           B,B
73C6: 27         DAA
73C7: 41         LD           B,C
73C8: 2B         DEC         HL
73C9: 45         LD           B,L
73CA: 1B         DEC         DE
73CB: 46         LD           B,(HL)
73CC: 2A         LD           A,(HLI)
73CD: 83         ADD         A,E
73CE: 47         LD           B,A
73CF: 21 50 DF   LD           HL,$DF50
73D2: 51         LD           D,C
73D3: 27         DAA
73D4: 52         LD           D,D
73D5: 2B         DEC         HL
73D6: 84         ADD         A,H
73D7: 54         LD           D,H
73D8: 1B         DEC         DE
73D9: 82         ADD         A,D
73DA: 58         LD           E,B
73DB: 0E 60      LD           C,$60
73DD: 0D         DEC         C
73DE: 61         LD           H,C
73DF: DF         RST         0X18
73E0: 62         LD           H,D
73E1: 27         DAA
73E2: 63         LD           H,E
73E3: 22         LD           (HLI),A
73E4: 64         LD           H,H
73E5: 2B         DEC         HL
73E6: 82         ADD         A,D
73E7: 65         LD           H,L
73E8: 1B         DEC         DE
73E9: 83         ADD         A,E
73EA: 67         LD           H,A
73EB: 0E 82      LD           C,$82
73ED: 70         LD           (HL),B
73EE: 0D         DEC         C
73EF: 82         ADD         A,D
73F0: 72         LD           (HL),D
73F1: DF         RST         0X18
73F2: 74         LD           (HL),H
73F3: 27         DAA
73F4: 85         ADD         A,L
73F5: 75         LD           (HL),L
73F6: 22         LD           (HLI),A
73F7: 22         LD           (HLI),A
73F8: CB E0      SET         1,E
73FA: 00         NOP
73FB: E7         RST         0X20
73FC: 68         LD           L,B
73FD: 20 FE      JR           NZ,$73FD
73FF: 0C         INC         C
7400: 95         SUB         L
7401: 02         LD           (BC),A
7402: 0D         DEC         C
7403: 82         ADD         A,D
7404: 04         INC         B
7405: DF         RST         0X18
7406: C3 09 DF   JP           $DF09
7409: 82         ADD         A,D
740A: 10 0D      STOP       $0D
740C: 13         INC         DE
740D: DF         RST         0X18
740E: 16 DF      LD           D,$DF
7410: 18 DF      JR           $73F1
7412: 20 DF      JR           NZ,$73F3
7414: 85         ADD         A,L
7415: 21 0D 85   LD           HL,$850D
7418: 30 DF      JR           NC,$73F9
741A: 82         ADD         A,D
741B: 35         DEC         (HL)
741C: 0D         DEC         C
741D: 37         SCF
741E: DF         RST         0X18
741F: 39         ADD         HL,SP
7420: 0D         DEC         C
7421: 84         ADD         A,H
7422: 40         LD           B,B
7423: 21 44 26   LD           HL,$2644
7426: 45         LD           B,L
7427: DF         RST         0X18
7428: 82         ADD         A,D
7429: 46         LD           B,(HL)
742A: 0D         DEC         C
742B: C2 48 DF   JP           NZ,$DF48
742E: 84         ADD         A,H
742F: 50         LD           D,B
7430: 0E 54      LD           C,$54
7432: 2A         LD           A,(HLI)
7433: 55         LD           D,L
7434: 26 56      LD           H,$56
7436: DF         RST         0X18
7437: 85         ADD         A,L
7438: 60         LD           H,B
7439: 0E 65      LD           C,$65
743B: 2A         LD           A,(HLI)
743C: 66         LD           H,(HL)
743D: 26 C2      LD           H,$C2
743F: 67         LD           H,A
7440: DF         RST         0X18
7441: C2 68 0D   JP           NZ,$0D68
7444: 69         LD           L,C
7445: 0D         DEC         C
7446: 82         ADD         A,D
7447: 70         LD           (HL),B
7448: 22         LD           (HLI),A
7449: 72         LD           (HL),D
744A: 2B         DEC         HL
744B: 83         ADD         A,E
744C: 73         LD           (HL),E
744D: 0E 76      LD           C,$76
744F: 24         INC         H
7450: 79         LD           A,C
7451: DF         RST         0X18
7452: FE 0C      CP           $0C
7454: 3D         DEC         A
7455: 00         NOP
7456: DF         RST         0X18
7457: 01 25 02   LD           BC,$0225
745A: 29         ADD         HL,HL
745B: 03         INC         BC
745C: 25         DEC         H
745D: 05         DEC         B
745E: 21 06 26   LD           HL,$2606
7461: 07         RLCA
7462: 2A         LD           A,(HLI)
7463: 08 26 C8   LD           ($C826),SP
7466: 09         ADD         HL,BC
7467: DF         RST         0X18
7468: 10 25      STOP       $25
746A: 11 29 12   LD           DE,$1229
746D: 25         DEC         H
746E: 13         INC         DE
746F: 29         ADD         HL,HL
7470: 16 2A      LD           D,$2A
7472: 17         RLA
7473: 26 C3      LD           H,$C3
7475: 18 24      JR           $749B
7477: 21 25 22   LD           HL,$2225
747A: 29         ADD         HL,HL
747B: 27         DAA
747C: 24         INC         H
747D: C2 31 23   JP           NZ,$2331
7480: 35         DEC         (HL)
7481: 2C         INC         L
7482: 36 22      LD           (HL),$22
7484: 37         SCF
7485: 28 44      JR           Z,$74CB
7487: 2C         INC         L
7488: 45         LD           B,L
7489: 28 46      JR           Z,$74D1
748B: 2C         INC         L
748C: 47         LD           B,A
748D: 22         LD           (HLI),A
748E: 48         LD           C,B
748F: 28 51      JR           Z,$74E2
7491: 27         DAA
7492: 82         ADD         A,D
7493: 52         LD           D,D
7494: 22         LD           (HLI),A
7495: 54         LD           D,H
7496: 28 55      JR           Z,$74ED
7498: 2C         INC         L
7499: 56         LD           D,(HL)
749A: 28 82      JR           Z,$741E
749C: 57         LD           D,A
749D: DF         RST         0X18
749E: 63         LD           H,E
749F: 1B         DEC         DE
74A0: 64         LD           H,H
74A1: 2C         INC         L
74A2: 65         LD           H,L
74A3: 28 66      JR           Z,$750B
74A5: DF         RST         0X18
74A6: 82         ADD         A,D
74A7: 72         LD           (HL),D
74A8: 1B         DEC         DE
74A9: 74         LD           (HL),H
74AA: 24         INC         H
74AB: 75         LD           (HL),L
74AC: DF         RST         0X18
74AD: 78         LD           A,B
74AE: DF         RST         0X18
74AF: 04         INC         B
74B0: A3         AND         E
74B1: E0 00      LDFF00   ($00),A
74B3: 2F         CPL
74B4: 18 70      JR           $7526
74B6: FE 0C      CP           $0C
74B8: 05         DEC         B
74B9: 74         LD           (HL),H
74BA: 3D         DEC         A
74BB: 00         NOP
74BC: DF         RST         0X18
74BD: 01 25 08   LD           BC,$0825
74C0: 26 09      LD           H,$09
74C2: DF         RST         0X18
74C3: 10 25      STOP       $25
74C5: 11 29 18   LD           DE,$1829
74C8: 2A         LD           A,(HLI)
74C9: 19         ADD         HL,DE
74CA: 26 60      LD           H,$60
74CC: 27         DAA
74CD: 61         LD           H,C
74CE: 2B         DEC         HL
74CF: 68         LD           L,B
74D0: 2C         INC         L
74D1: 69         LD           L,C
74D2: 28 70      JR           Z,$7544
74D4: DF         RST         0X18
74D5: 71         LD           (HL),C
74D6: 27         DAA
74D7: 78         LD           A,B
74D8: 28 79      JR           Z,$7553
74DA: DF         RST         0X18
74DB: 22         LD           (HLI),A
74DC: 0F         RRCA
74DD: 36 0F      LD           (HL),$0F
74DF: 31 0F 44   LD           SP,$440F
74E2: 0F         RRCA
74E3: 67         LD           H,A
74E4: 0F         RRCA
74E5: 82         ADD         A,D
74E6: 25         DEC         H
74E7: 0F         RRCA
74E8: FE 0C      CP           $0C
74EA: 9D         SBC         L
74EB: 00         NOP
74EC: 25         DEC         H
74ED: 82         ADD         A,D
74EE: 01 21 03   LD           BC,$0321
74F1: 26 82      LD           H,$82
74F3: 05         DEC         B
74F4: DF         RST         0X18
74F5: C2 13 24   JP           NZ,$2413
74F8: 82         ADD         A,D
74F9: 15         DEC         D
74FA: 05         DEC         B
74FB: 82         ADD         A,D
74FC: 17         RLA
74FD: DF         RST         0X18
74FE: 86         ADD         A,(HL)
74FF: 24         INC         H
7500: DF         RST         0X18
7501: 27         DAA
7502: 05         DEC         B
7503: 82         ADD         A,D
7504: 31 1B 33   LD           SP,$331B
7507: 2A         LD           A,(HLI)
7508: 86         ADD         A,(HL)
7509: 34         INC         (HL)
750A: 21 40 27   LD           HL,$2740
750D: 41         LD           B,C
750E: 2B         DEC         HL
750F: 88         ADC         A,B
7510: 42         LD           B,D
7511: 1B         DEC         DE
7512: 51         LD           D,C
7513: 27         DAA
7514: 88         ADC         A,B
7515: 52         LD           D,D
7516: 22         LD           (HLI),A
7517: 82         ADD         A,D
7518: 60         LD           H,B
7519: 05         DEC         B
751A: 88         ADC         A,B
751B: 62         LD           H,D
751C: DF         RST         0X18
751D: 64         LD           H,H
751E: 0D         DEC         C
751F: 82         ADD         A,D
7520: 66         LD           H,(HL)
7521: 0D         DEC         C
7522: 89         ADC         A,C
7523: 70         LD           (HL),B
7524: DF         RST         0X18
7525: 72         LD           (HL),D
7526: 05         DEC         B
7527: 73         LD           (HL),E
7528: 0D         DEC         C
7529: C3 10 23   JP           $2310
752C: 21 1B 12   LD           HL,$121B
752F: CB E0      SET         1,E
7531: 00         NOP
7532: 2B         DEC         HL
7533: 68         LD           L,B
7534: 30 FE      JR           NC,$7534
7536: 0C         INC         C
7537: 9D         SBC         L
7538: 8A         ADC         A,D
7539: 00         NOP
753A: DF         RST         0X18
753B: 83         ADD         A,E
753C: 06 05      LD           B,$05
753E: 82         ADD         A,D
753F: 11 DF 83   LD           DE,$83DF
7542: 15         DEC         D
7543: DF         RST         0X18
7544: 8A         ADC         A,D
7545: 20 DF      JR           NZ,$7526
7547: 82         ADD         A,D
7548: 25         DEC         H
7549: 0D         DEC         C
754A: 88         ADC         A,B
754B: 30 21      JR           NC,$756E
754D: 38 26      JR           C,$7575
754F: 39         ADD         HL,SP
7550: DF         RST         0X18
7551: 84         ADD         A,H
7552: 40         LD           B,B
7553: 1B         DEC         DE
7554: 44         LD           B,H
7555: A7         AND         A
7556: 45         LD           B,L
7557: AE         XOR         (HL)
7558: 48         LD           C,B
7559: 2A         LD           A,(HLI)
755A: 49         LD           C,C
755B: 26 86      LD           H,$86
755D: 50         LD           D,B
755E: 22         LD           (HLI),A
755F: 56         LD           D,(HL)
7560: 2B         DEC         HL
7561: C2 59 24   JP           NZ,$2459
7564: 86         ADD         A,(HL)
7565: 60         LD           H,B
7566: DF         RST         0X18
7567: 62         LD           H,D
7568: 05         DEC         B
7569: 63         LD           H,E
756A: 0D         DEC         C
756B: 66         LD           H,(HL)
756C: 23         INC         HL
756D: 82         ADD         A,D
756E: 71         LD           (HL),C
756F: DF         RST         0X18
7570: 83         ADD         A,E
7571: 73         LD           (HL),E
7572: 05         DEC         B
7573: 76         HALT
7574: 27         DAA
7575: 82         ADD         A,D
7576: 77         LD           (HL),A
7577: 22         LD           (HLI),A
7578: 79         LD           A,C
7579: 28 68      JR           Z,$75E3
757B: CB E0      SET         1,E
757D: 00         NOP
757E: 2D         DEC         L
757F: 58         LD           E,B
7580: 50         LD           D,B
7581: FE 05      CP           $05
7583: 94         SUB         H
7584: 88         ADC         A,B
7585: 00         NOP
7586: 69         LD           L,C
7587: C2 08 6C   JP           NZ,$6C08
758A: C2 09 68   JP           NZ,$6809
758D: 88         ADC         A,B
758E: 10 69      STOP       $69
7590: 20 61      JR           NZ,$75F3
7592: 21 64 22   LD           HL,$2264
7595: 5F         LD           E,A
7596: 87         ADD         A,A
7597: 23         INC         HL
7598: 60         LD           H,B
7599: C3 30 57   JP           $5730
759C: C2 31 65   JP           NZ,$6531
759F: 32         LD           (HLD),A
75A0: 5A         LD           E,D
75A1: 87         ADD         A,A
75A2: 33         INC         SP
75A3: 5C         LD           E,H
75A4: 53         LD           D,E
75A5: 82         ADD         A,D
75A6: 57         LD           D,A
75A7: 82         ADD         A,D
75A8: 60         LD           H,B
75A9: 54         LD           D,H
75AA: 61         LD           H,C
75AB: 5B         LD           E,E
75AC: 62         LD           H,D
75AD: 5D         LD           E,L
75AE: 63         LD           H,E
75AF: 4C         LD           C,H
75B0: 64         LD           H,H
75B1: 59         LD           E,C
75B2: 65         LD           H,L
75B3: 5D         LD           E,L
75B4: 82         ADD         A,D
75B5: 66         LD           H,(HL)
75B6: 4C         LD           C,H
75B7: 68         LD           L,B
75B8: 59         LD           E,C
75B9: 69         LD           L,C
75BA: 5B         LD           E,E
75BB: 8A         ADC         A,D
75BC: 70         LD           (HL),B
75BD: 54         LD           D,H
75BE: E0 00      LDFF00   ($00),A
75C0: 49         LD           C,C
75C1: 68         LD           L,B
75C2: 50         LD           D,B
75C3: FE 05      CP           $05
75C5: 94         SUB         H
75C6: C2 00 68   JP           NZ,$6800
75C9: C2 01 6D   JP           NZ,$6D01
75CC: 02         LD           (BC),A
75CD: 79         LD           A,C
75CE: 03         INC         BC
75CF: E3                              
75D0: 82         ADD         A,D
75D1: 04         INC         B
75D2: E4                              
75D3: 06 E5      LD           B,$E5
75D5: 12         LD           (DE),A
75D6: 03         INC         BC
75D7: 13         INC         DE
75D8: 7F         LD           A,A
75D9: 82         ADD         A,D
75DA: 14         INC         D
75DB: 4D         LD           C,L
75DC: 16 E6      LD           D,$E6
75DE: 07         RLCA
75DF: E3                              
75E0: 82         ADD         A,D
75E1: 08 E4 17   LD           ($17E4),SP
75E4: 7F         LD           A,A
75E5: 82         ADD         A,D
75E6: 18 4D      JR           $7635
75E8: 8A         ADC         A,D
75E9: 20 60      JR           NZ,$764B
75EB: 25         DEC         H
75EC: 61         LD           H,C
75ED: 26 64      LD           H,$64
75EF: 27         DAA
75F0: 5F         LD           E,A
75F1: 85         ADD         A,L
75F2: 30 5C      JR           NC,$7650
75F4: 35         DEC         (HL)
75F5: 5E         LD           E,(HL)
75F6: C2 36 65   JP           NZ,$6536
75F9: C2 37 51   JP           NZ,$5137
75FC: C5         PUSH       BC
75FD: 38 54      JR           C,$7653
75FF: C5         PUSH       BC
7600: 39         ADD         HL,SP
7601: 54         LD           D,H
7602: 53         LD           D,E
7603: 82         ADD         A,D
7604: 55         LD           D,L
7605: 64         LD           H,H
7606: 56         LD           D,(HL)
7607: 59         LD           E,C
7608: 83         ADD         A,E
7609: 57         LD           D,A
760A: 54         LD           D,H
760B: 60         LD           H,B
760C: 5B         LD           E,E
760D: 61         LD           H,C
760E: 5D         LD           E,L
760F: 65         LD           H,L
7610: 65         LD           H,L
7611: 66         LD           H,(HL)
7612: 51         LD           D,C
7613: 83         ADD         A,E
7614: 67         LD           H,A
7615: 54         LD           D,H
7616: 8A         ADC         A,D
7617: 70         LD           (HL),B
7618: 54         LD           D,H
7619: 84         ADD         A,H
761A: 72         LD           (HL),D
761B: 5B         LD           E,E
761C: E0 00      LDFF00   ($00),A
761E: 4A         LD           C,D
761F: 88         ADC         A,B
7620: 30 FE      JR           NC,$7620
7622: 0C         INC         C
7623: 9D         SBC         L
7624: 02         LD           (BC),A
7625: 05         DEC         B
7626: 03         INC         BC
7627: DF         RST         0X18
7628: 04         INC         B
7629: 25         DEC         H
762A: 84         ADD         A,H
762B: 05         DEC         B
762C: 21 09 26   LD           HL,$2609
762F: 10 05      STOP       $05
7631: 82         ADD         A,D
7632: 11 DF 13   LD           DE,$13DF
7635: 25         DEC         H
7636: 14         INC         D
7637: 29         ADD         HL,HL
7638: C7         RST         0X00
7639: 19         ADD         HL,DE
763A: 24         INC         H
763B: 20 25      JR           NZ,$7662
763D: 82         ADD         A,D
763E: 21 21 23   LD           HL,$2321
7641: 29         ADD         HL,HL
7642: C3 30 23   JP           $2330
7645: 35         DEC         (HL)
7646: 2C         INC         L
7647: 36 22      LD           (HL),$22
7649: 37         SCF
764A: 2B         DEC         HL
764B: 45         LD           B,L
764C: 24         INC         H
764D: C4 46 DF   CALL       NZ,$DF46
7650: C4 47 23   CALL       NZ,$2347
7653: 54         LD           D,H
7654: 2C         INC         L
7655: 55         LD           D,L
7656: 28 60      JR           Z,$76B8
7658: 27         DAA
7659: 84         ADD         A,H
765A: 61         LD           H,C
765B: 22         LD           (HLI),A
765C: 64         LD           H,H
765D: 28 65      JR           Z,$76C4
765F: DF         RST         0X18
7660: 66         LD           H,(HL)
7661: 0D         DEC         C
7662: 84         ADD         A,H
7663: 70         LD           (HL),B
7664: DF         RST         0X18
7665: 31 CB E0   LD           SP,$E0CB
7668: 00         NOP
7669: 03         INC         BC
766A: 48         LD           C,B
766B: 50         LD           D,B
766C: FE 05      CP           $05
766E: 94         SUB         H
766F: 83         ADD         A,E
7670: 12         LD           (DE),A
7671: 6B         LD           L,E
7672: 13         INC         DE
7673: 69         LD           L,C
7674: 83         ADD         A,E
7675: 22         LD           (HLI),A
7676: 69         LD           L,C
7677: 23         INC         HL
7678: 82         ADD         A,D
7679: 83         ADD         A,E
767A: 16 6B      LD           D,$6B
767C: 17         RLA
767D: 69         LD           L,C
767E: 83         ADD         A,E
767F: 26 69      LD           H,$69
7681: 27         DAA
7682: 82         ADD         A,D
7683: 8A         ADC         A,D
7684: 00         NOP
7685: 6D         LD           L,L
7686: 8A         ADC         A,D
7687: 40         LD           B,B
7688: 6D         LD           L,L
7689: C3 10 6C   JP           $6C10
768C: C3 19 6C   JP           $6C19
768F: C4 01 65   CALL       NZ,$6501
7692: 8A         ADC         A,D
7693: 50         LD           D,B
7694: 83         ADD         A,E
7695: 8A         ADC         A,D
7696: 60         LD           H,B
7697: 84         ADD         A,H
7698: 8A         ADC         A,D
7699: 70         LD           (HL),B
769A: 84         ADD         A,H
769B: 43         LD           B,E
769C: 64         LD           H,H
769D: 83         ADD         A,E
769E: 44         LD           B,H
769F: 04         INC         B
76A0: 82         ADD         A,D
76A1: 60         LD           H,B
76A2: 4B         LD           C,E
76A3: 82         ADD         A,D
76A4: 70         LD           (HL),B
76A5: 4B         LD           C,E
76A6: 82         ADD         A,D
76A7: 68         LD           L,B
76A8: 4B         LD           C,E
76A9: 82         ADD         A,D
76AA: 78         LD           A,B
76AB: 4B         LD           C,E
76AC: E1         POP         HL
76AD: 03         INC         BC
76AE: 66         LD           H,(HL)
76AF: 48         LD           C,B
76B0: 50         LD           D,B
76B1: FE 0C      CP           $0C
76B3: 9D         SBC         L
76B4: 00         NOP
76B5: DF         RST         0X18
76B6: 01 25 83   LD           BC,$8325
76B9: 02         LD           (BC),A
76BA: 21 05 26   LD           HL,$2605
76BD: 06 DF      LD           B,$DF
76BF: 09         ADD         HL,BC
76C0: DF         RST         0X18
76C1: 10 25      STOP       $25
76C3: 11 29 15   LD           DE,$1529
76C6: 2A         LD           A,(HLI)
76C7: 16 26      LD           D,$26
76C9: 17         RLA
76CA: DF         RST         0X18
76CB: C3 20 23   JP           $2320
76CE: 26 2A      LD           H,$2A
76D0: 27         DAA
76D1: 26 82      LD           H,$82
76D3: 28 DF      JR           Z,$76B4
76D5: 83         ADD         A,E
76D6: 34         INC         (HL)
76D7: AF         XOR         A
76D8: 37         SCF
76D9: 2A         LD           A,(HLI)
76DA: 82         ADD         A,D
76DB: 38 21      JR           C,$76FE
76DD: 41         LD           B,C
76DE: A6         AND         (HL)
76DF: 43         LD           B,E
76E0: AF         XOR         A
76E1: 83         ADD         A,E
76E2: 44         LD           B,H
76E3: 01 47 AE   LD           BC,$AE47
76E6: 50         LD           D,B
76E7: 27         DAA
76E8: 51         LD           D,C
76E9: 2B         DEC         HL
76EA: 84         ADD         A,H
76EB: 53         LD           D,E
76EC: B0         OR           B
76ED: 58         LD           E,B
76EE: A7         AND         A
76EF: 60         LD           H,B
76F0: DF         RST         0X18
76F1: 61         LD           H,C
76F2: 27         DAA
76F3: 84         ADD         A,H
76F4: 62         LD           H,D
76F5: 22         LD           (HLI),A
76F6: 66         LD           H,(HL)
76F7: 2B         DEC         HL
76F8: 68         LD           L,B
76F9: AE         XOR         (HL)
76FA: 85         ADD         A,L
76FB: 71         LD           (HL),C
76FC: DF         RST         0X18
76FD: 76         HALT
76FE: 27         DAA
76FF: 83         ADD         A,E
7700: 77         LD           (HL),A
7701: 22         LD           (HLI),A
7702: 03         INC         BC
7703: A3         AND         E
7704: E0 00      LDFF00   ($00),A
7706: 9C         SBC         H
7707: 58         LD           E,B
7708: 10 FE      STOP       $FE
770A: 0C         INC         C
770B: 9D         SBC         L
770C: 83         ADD         A,E
770D: 00         NOP
770E: DF         RST         0X18
770F: 05         DEC         B
7710: DF         RST         0X18
7711: C2 10 DF   JP           NZ,$DF10
7714: 83         ADD         A,E
7715: 16 DF      LD           D,$DF
7717: 84         ADD         A,H
7718: 21 DF 29   LD           HL,$29DF
771B: DF         RST         0X18
771C: 84         ADD         A,H
771D: 30 21      JR           NC,$7740
771F: 34         INC         (HL)
7720: 26 83      LD           H,$83
7722: 35         DEC         (HL)
7723: DF         RST         0X18
7724: 82         ADD         A,D
7725: 42         LD           B,D
7726: 0E 44      LD           C,$44
7728: 2A         LD           A,(HLI)
7729: 82         ADD         A,D
772A: 45         LD           B,L
772B: 21 47 26   LD           HL,$2647
772E: 48         LD           C,B
772F: DF         RST         0X18
7730: 84         ADD         A,H
7731: 51         LD           D,C
7732: 0E 82      LD           C,$82
7734: 55         LD           D,L
7735: 1B         DEC         DE
7736: 57         LD           D,A
7737: 2A         LD           A,(HLI)
7738: 58         LD           E,B
7739: 21 59 26   LD           HL,$2659
773C: 83         ADD         A,E
773D: 61         LD           H,C
773E: 0E 82      LD           C,$82
7740: 64         LD           H,H
7741: 1B         DEC         DE
7742: 69         LD           L,C
7743: 24         INC         H
7744: 89         ADC         A,C
7745: 70         LD           (HL),B
7746: 22         LD           (HLI),A
7747: 79         LD           A,C
7748: 28 58      JR           Z,$77A2
774A: A3         AND         E
774B: E0 00      LDFF00   ($00),A
774D: 9D         SBC         L
774E: 38 30      JR           C,$7780
7750: FE 0C      CP           $0C
7752: 0E 00      LD           C,$00
7754: DF         RST         0X18
7755: 01 25 08   LD           BC,$0825
7758: 26 09      LD           H,$09
775A: DF         RST         0X18
775B: 10 25      STOP       $25
775D: 11 29 18   LD           DE,$1829
7760: 2A         LD           A,(HLI)
7761: 19         ADD         HL,DE
7762: 26 60      LD           H,$60
7764: 27         DAA
7765: 61         LD           H,C
7766: 2B         DEC         HL
7767: 68         LD           L,B
7768: 2C         INC         L
7769: 69         LD           L,C
776A: 28 70      JR           Z,$77DC
776C: DF         RST         0X18
776D: 71         LD           (HL),C
776E: 27         DAA
776F: 73         LD           (HL),E
7770: 2B         DEC         HL
7771: 74         LD           (HL),H
7772: 0E 75      LD           C,$75
7774: 2C         INC         L
7775: 78         LD           A,B
7776: 28 79      JR           Z,$77F1
7778: DF         RST         0X18
7779: E0 00      LDFF00   ($00),A
777B: 2E 58      LD           L,$58
777D: 20 FE      JR           NZ,$777D
777F: 0C         INC         C
7780: 0D         DEC         C
7781: 00         NOP
7782: 0D         DEC         C
7783: 01 25 08   LD           BC,$0825
7786: 26 09      LD           H,$09
7788: DF         RST         0X18
7789: 10 25      STOP       $25
778B: 11 29 C3   LD           DE,$C329
778E: 12         LD           (DE),A
778F: 10 13      STOP       $13
7791: 25         DEC         H
7792: 82         ADD         A,D
7793: 14         INC         D
7794: 21 16 26   LD           HL,$2616
7797: C3 17 11   JP           $1117
779A: 18 2A      JR           $77C6
779C: 19         ADD         HL,DE
779D: 26 23      LD           H,$23
779F: 23         INC         HL
77A0: 82         ADD         A,D
77A1: 24         INC         H
77A2: 1B         DEC         DE
77A3: 26 24      LD           H,$24
77A5: 33         INC         SP
77A6: 27         DAA
77A7: 82         ADD         A,D
77A8: 34         INC         (HL)
77A9: 22         LD           (HLI),A
77AA: 36 28      LD           (HL),$28
77AC: 42         LD           B,D
77AD: 87         ADD         A,A
77AE: 52         LD           D,D
77AF: CE 84      ADC         $84
77B1: 43         LD           B,E
77B2: 12         LD           (DE),A
77B3: 47         LD           B,A
77B4: 87         ADD         A,A
77B5: 57         LD           D,A
77B6: CE 60      ADC         $60
77B8: 27         DAA
77B9: 61         LD           H,C
77BA: 2B         DEC         HL
77BB: 68         LD           L,B
77BC: 2C         INC         L
77BD: 69         LD           L,C
77BE: 28 70      JR           Z,$7830
77C0: DF         RST         0X18
77C1: 71         LD           (HL),C
77C2: 27         DAA
77C3: 78         LD           A,B
77C4: 28 79      JR           Z,$783F
77C6: 0D         DEC         C
77C7: 74         LD           (HL),H
77C8: FD                              
77C9: E0 00      LDFF00   ($00),A
77CB: 87         ADD         A,A
77CC: 28 10      JR           Z,$77DE
77CE: FE 0C      CP           $0C
77D0: 9D         SBC         L
77D1: C4 00 DF   CALL       NZ,$DF00
77D4: C4 21 DF   CALL       NZ,$DF21
77D7: 02         LD           (BC),A
77D8: 00         NOP
77D9: C7         RST         0X00
77DA: 03         INC         BC
77DB: 23         INC         HL
77DC: C7         RST         0X00
77DD: 06 24      LD           B,$24
77DF: C3 07 DF   JP           $DF07
77E2: 09         ADD         HL,BC
77E3: 00         NOP
77E4: 12         LD           (DE),A
77E5: DF         RST         0X18
77E6: C3 18 DF   JP           $DF18
77E9: 19         ADD         HL,DE
77EA: DF         RST         0X18
77EB: 22         LD           (HLI),A
77EC: 00         NOP
77ED: 29         ADD         HL,HL
77EE: 00         NOP
77EF: 37         SCF
77F0: 00         NOP
77F1: 40         LD           B,B
77F2: 00         NOP
77F3: 42         LD           B,D
77F4: DF         RST         0X18
77F5: 47         LD           B,A
77F6: DF         RST         0X18
77F7: C2 48 00   JP           NZ,$0048
77FA: C2 52 00   JP           NZ,$0052
77FD: 57         LD           D,A
77FE: 00         NOP
77FF: C3 59 DF   JP           $DF59
7802: C2 60 DF   JP           NZ,$DF60
7805: C2 68 DF   JP           NZ,$DF68
7808: 71         LD           (HL),C
7809: DF         RST         0X18
780A: 73         LD           (HL),E
780B: 27         DAA
780C: 82         ADD         A,D
780D: 74         LD           (HL),H
780E: 22         LD           (HLI),A
780F: 76         HALT
7810: 28 65      JR           Z,$7877
7812: CB E0      SET         1,E
7814: 00         NOP
7815: 92         SUB         D
7816: 58         LD           E,B
7817: 52         LD           D,D
7818: FE 0C      CP           $0C
781A: 0D         DEC         C
781B: 00         NOP
781C: DF         RST         0X18
781D: 01 25 08   LD           BC,$0825
7820: 26 09      LD           H,$09
7822: DF         RST         0X18
7823: 10 25      STOP       $25
7825: 11 29 18   LD           DE,$1829
7828: 2A         LD           A,(HLI)
7829: 19         ADD         HL,DE
782A: 26 60      LD           H,$60
782C: 27         DAA
782D: 61         LD           H,C
782E: 2B         DEC         HL
782F: 68         LD           L,B
7830: 2C         INC         L
7831: 69         LD           L,C
7832: 28 70      JR           Z,$78A4
7834: DF         RST         0X18
7835: 71         LD           (HL),C
7836: 27         DAA
7837: 78         LD           A,B
7838: 28 79      JR           Z,$78B3
783A: DF         RST         0X18
783B: 03         INC         BC
783C: C7         RST         0X00
783D: 06 C7      LD           B,$C7
783F: 82         ADD         A,D
7840: 14         INC         D
7841: 1B         DEC         DE
7842: 84         ADD         A,H
7843: 23         INC         HL
7844: 1B         DEC         DE
7845: 84         ADD         A,H
7846: 33         INC         SP
7847: 1B         DEC         DE
7848: 82         ADD         A,D
7849: 44         LD           B,H
784A: 1B         DEC         DE
784B: 74         LD           (HL),H
784C: 3D         DEC         A
784D: E0 00      LDFF00   ($00),A
784F: F4                              
7850: 18 20      JR           $7872
7852: FE 0C      CP           $0C
7854: 0D         DEC         C
7855: 00         NOP
7856: DF         RST         0X18
7857: 01 25 08   LD           BC,$0825
785A: 26 09      LD           H,$09
785C: DF         RST         0X18
785D: 10 25      STOP       $25
785F: 11 29 18   LD           DE,$1829
7862: 2A         LD           A,(HLI)
7863: 19         ADD         HL,DE
7864: 26 60      LD           H,$60
7866: 27         DAA
7867: 61         LD           H,C
7868: 2B         DEC         HL
7869: 68         LD           L,B
786A: 2C         INC         L
786B: 69         LD           L,C
786C: 28 70      JR           Z,$78DE
786E: DF         RST         0X18
786F: 71         LD           (HL),C
7870: 27         DAA
7871: 78         LD           A,B
7872: 28 79      JR           Z,$78ED
7874: DF         RST         0X18
7875: 03         INC         BC
7876: C7         RST         0X00
7877: 06 C7      LD           B,$C7
7879: 82         ADD         A,D
787A: 14         INC         D
787B: 1B         DEC         DE
787C: 84         ADD         A,H
787D: 23         INC         HL
787E: 1B         DEC         DE
787F: 84         ADD         A,H
7880: 33         INC         SP
7881: 1B         DEC         DE
7882: 82         ADD         A,D
7883: 44         LD           B,H
7884: 1B         DEC         DE
7885: 21 C5 31   LD           HL,$31C5
7888: C6 24      ADD         $24
788A: 9B         SBC         E
788B: 25         DEC         H
788C: 9C         SBC         H
788D: 74         LD           (HL),H
788E: 3D         DEC         A
788F: E0 00      LDFF00   ($00),A
7891: F4                              
7892: 18 20      JR           $78B4
7894: FE 0C      CP           $0C
7896: 95         SUB         L
7897: 82         ADD         A,D
7898: 00         NOP
7899: DF         RST         0X18
789A: 02         LD           (BC),A
789B: 23         INC         HL
789C: 84         ADD         A,H
789D: 03         INC         BC
789E: 0E 06      LD           C,$06
78A0: 2A         LD           A,(HLI)
78A1: 07         RLCA
78A2: 26 C2      LD           H,$C2
78A4: 08 DF C2   LD           ($C2DF),SP
78A7: 09         ADD         HL,BC
78A8: 0D         DEC         C
78A9: C2 10 0D   JP           NZ,$0D10
78AC: 11 DF 12   LD           DE,$12DF
78AF: 27         DAA
78B0: 13         INC         DE
78B1: 2B         DEC         HL
78B2: 83         ADD         A,E
78B3: 14         INC         D
78B4: 0E 17      LD           C,$17
78B6: 24         INC         H
78B7: C2 21 0D   JP           NZ,$0D21
78BA: 22         LD           (HLI),A
78BB: DF         RST         0X18
78BC: 23         INC         HL
78BD: 27         DAA
78BE: 24         INC         H
78BF: 2B         DEC         HL
78C0: 82         ADD         A,D
78C1: 25         DEC         H
78C2: 1B         DEC         DE
78C3: 27         DAA
78C4: 2A         LD           A,(HLI)
78C5: 28 26      JR           Z,$78ED
78C7: 29         ADD         HL,HL
78C8: DF         RST         0X18
78C9: C2 32 0D   JP           NZ,$0D32
78CC: 33         INC         SP
78CD: DF         RST         0X18
78CE: 34         INC         (HL)
78CF: 27         DAA
78D0: 35         DEC         (HL)
78D1: 2B         DEC         HL
78D2: 82         ADD         A,D
78D3: 36 1B      LD           (HL),$1B
78D5: 38 2A      JR           C,$7901
78D7: 39         ADD         HL,SP
78D8: 26 40      LD           H,$40
78DA: 0D         DEC         C
78DB: 82         ADD         A,D
78DC: 42         LD           B,D
78DD: 0D         DEC         C
78DE: C2 44 DF   JP           NZ,$DF44
78E1: 45         LD           B,L
78E2: 23         INC         HL
78E3: 46         LD           B,(HL)
78E4: 1B         DEC         DE
78E5: C3 49 24   JP           $2449
78E8: 51         LD           D,C
78E9: 0D         DEC         C
78EA: 52         LD           D,D
78EB: DF         RST         0X18
78EC: 55         LD           D,L
78ED: 27         DAA
78EE: 56         LD           D,(HL)
78EF: 2B         DEC         HL
78F0: C2 63 DF   JP           NZ,$DF63
78F3: C2 64 0D   JP           NZ,$0D64
78F6: C2 65 DF   JP           NZ,$DF65
78F9: 66         LD           H,(HL)
78FA: 23         INC         HL
78FB: 70         LD           (HL),B
78FC: DF         RST         0X18
78FD: 76         HALT
78FE: 27         DAA
78FF: 82         ADD         A,D
7900: 77         LD           (HL),A
7901: 22         LD           (HLI),A
7902: 79         LD           A,C
7903: 28 68      JR           Z,$796D
7905: CB E0      SET         1,E
7907: 00         NOP
7908: F9         LD           SP,HL
7909: 78         LD           A,B
790A: 50         LD           D,B
790B: FE 0C      CP           $0C
790D: 90         SUB         B
790E: C2 00 23   JP           NZ,$2300
7911: 82         ADD         A,D
7912: 02         LD           (BC),A
7913: 1B         DEC         DE
7914: C2 04 24   JP           NZ,$2404
7917: 83         ADD         A,E
7918: 05         DEC         B
7919: DF         RST         0X18
791A: 83         ADD         A,E
791B: 11 1B 15   LD           DE,$151B
791E: DF         RST         0X18
791F: 18 DF      JR           $7900
7921: 20 27      JR           NZ,$794A
7923: 21 2B 22   LD           HL,$222B
7926: 1B         DEC         DE
7927: 23         INC         HL
7928: 0E 24      LD           C,$24
792A: 2A         LD           A,(HLI)
792B: 25         DEC         H
792C: 26 82      LD           H,$82
792E: 26 0D      LD           H,$0D
7930: C3 29 DF   JP           $DF29
7933: C2 30 DF   JP           NZ,$DF30
7936: 31 23 83   LD           SP,$8323
7939: 32         LD           (HLD),A
793A: 0E 35      LD           C,$35
793C: 2A         LD           A,(HLI)
793D: 36 26      LD           (HL),$26
793F: 37         SCF
7940: DF         RST         0X18
7941: 38 0D      JR           C,$7950
7943: 41         LD           B,C
7944: 27         DAA
7945: 42         LD           B,D
7946: 2B         DEC         HL
7947: 83         ADD         A,E
7948: 43         LD           B,E
7949: 0E 46      LD           C,$46
794B: 2A         LD           A,(HLI)
794C: 47         LD           B,A
794D: 26 48      LD           H,$48
794F: DF         RST         0X18
7950: 50         LD           D,B
7951: 0D         DEC         C
7952: 51         LD           D,C
7953: DF         RST         0X18
7954: 52         LD           D,D
7955: 27         DAA
7956: 53         LD           D,E
7957: 2B         DEC         HL
7958: 83         ADD         A,E
7959: 54         LD           D,H
795A: 0E 57      LD           C,$57
795C: 2A         LD           A,(HLI)
795D: 59         LD           E,C
795E: 26 61      LD           H,$61
7960: 0D         DEC         C
7961: 62         LD           H,D
7962: DF         RST         0X18
7963: 63         LD           H,E
7964: 27         DAA
7965: 64         LD           H,H
7966: 22         LD           (HLI),A
7967: 65         LD           H,L
7968: 2B         DEC         HL
7969: 83         ADD         A,E
796A: 66         LD           H,(HL)
796B: 0E 69      LD           C,$69
796D: 24         INC         H
796E: 72         LD           (HL),D
796F: 0D         DEC         C
7970: 82         ADD         A,D
7971: 73         LD           (HL),E
7972: DF         RST         0X18
7973: 75         LD           (HL),L
7974: 27         DAA
7975: 83         ADD         A,E
7976: 76         HALT
7977: 22         LD           (HLI),A
7978: 79         LD           A,C
7979: 28 68      JR           Z,$79E3
797B: 1B         DEC         DE
797C: 01 0D 58   LD           BC,$580D
797F: A3         AND         E
7980: E0 00      LDFF00   ($00),A
7982: 8F         ADC         A,A
7983: 08 20 FE   LD           ($FE20),SP
7986: 0C         INC         C
7987: 05         DEC         B
7988: 04         INC         B
7989: 47         LD           B,A
798A: 00         NOP
798B: DF         RST         0X18
798C: 01 25 08   LD           BC,$0825
798F: 26 09      LD           H,$09
7991: DF         RST         0X18
7992: 10 25      STOP       $25
7994: 11 29 18   LD           DE,$1829
7997: 2A         LD           A,(HLI)
7998: 19         ADD         HL,DE
7999: 26 60      LD           H,$60
799B: 27         DAA
799C: 61         LD           H,C
799D: 2B         DEC         HL
799E: 68         LD           L,B
799F: 2C         INC         L
79A0: 69         LD           L,C
79A1: 28 70      JR           Z,$7A13
79A3: DF         RST         0X18
79A4: 71         LD           (HL),C
79A5: 27         DAA
79A6: 78         LD           A,B
79A7: 28 79      JR           Z,$7A22
79A9: DF         RST         0X18
79AA: 22         LD           (HLI),A
79AB: 0F         RRCA
79AC: 36 0F      LD           (HL),$0F
79AE: 31 0F 44   LD           SP,$440F
79B1: 0F         RRCA
79B2: 67         LD           H,A
79B3: 0F         RRCA
79B4: 82         ADD         A,D
79B5: 25         DEC         H
79B6: 0F         RRCA
79B7: 39         ADD         HL,SP
79B8: 2A         LD           A,(HLI)
79B9: 49         LD           C,C
79BA: 05         DEC         B
79BB: 59         LD           E,C
79BC: 2C         INC         L
79BD: 38 AE      JR           C,$796D
79BF: 42         LD           B,D
79C0: AE         XOR         (HL)
79C1: 62         LD           H,D
79C2: AE         XOR         (HL)
79C3: FE 0C      CP           $0C
79C5: 0D         DEC         C
79C6: 00         NOP
79C7: DF         RST         0X18
79C8: 01 25 08   LD           BC,$0825
79CB: 26 09      LD           H,$09
79CD: DF         RST         0X18
79CE: 10 25      STOP       $25
79D0: 11 29 18   LD           DE,$1829
79D3: 2A         LD           A,(HLI)
79D4: 19         ADD         HL,DE
79D5: 26 60      LD           H,$60
79D7: 27         DAA
79D8: 61         LD           H,C
79D9: 2B         DEC         HL
79DA: 68         LD           L,B
79DB: 2C         INC         L
79DC: 69         LD           L,C
79DD: 28 70      JR           Z,$7A4F
79DF: DF         RST         0X18
79E0: 71         LD           (HL),C
79E1: 27         DAA
79E2: 78         LD           A,B
79E3: 28 79      JR           Z,$7A5E
79E5: DF         RST         0X18
79E6: 22         LD           (HLI),A
79E7: 05         DEC         B
79E8: 36 05      LD           (HL),$05
79EA: 31 05 44   LD           SP,$4405
79ED: 05         DEC         B
79EE: 67         LD           H,A
79EF: 05         DEC         B
79F0: 82         ADD         A,D
79F1: 25         DEC         H
79F2: 05         DEC         B
79F3: 30 29      JR           NC,$7A1E
79F5: 40         LD           B,B
79F6: 05         DEC         B
79F7: 50         LD           D,B
79F8: 2B         DEC         HL
79F9: 57         LD           D,A
79FA: CB E0      SET         1,E
79FC: 00         NOP
79FD: CF         RST         0X08
79FE: 58         LD           E,B
79FF: 10 FE      STOP       $FE
7A01: 04         INC         B
7A02: 0D         DEC         C
7A03: 88         ADC         A,B
7A04: 01 99 88   LD           BC,$8899
7A07: 11 9A 21   LD           DE,$219A
7A0A: CE 23      ADC         $23
7A0C: CE 26      ADC         $26
7A0E: CE 28      ADC         $28
7A10: CE 51      ADC         $51
7A12: CE 53      ADC         $53
7A14: CE 56      ADC         $56
7A16: CE 58      ADC         $58
7A18: CE 74      ADC         $74
7A1A: FD                              
7A1B: E0 00      LDFF00   ($00),A
7A1D: B0         OR           B
7A1E: 38 32      JR           C,$7A52
7A20: FE 0C      CP           $0C
7A22: 0D         DEC         C
7A23: 00         NOP
7A24: 0D         DEC         C
7A25: 01 25 08   LD           BC,$0825
7A28: 26 09      LD           H,$09
7A2A: DF         RST         0X18
7A2B: 10 25      STOP       $25
7A2D: 11 29 C3   LD           DE,$C329
7A30: 12         LD           (DE),A
7A31: 10 13      STOP       $13
7A33: 25         DEC         H
7A34: 82         ADD         A,D
7A35: 14         INC         D
7A36: 21 16 26   LD           HL,$2616
7A39: C3 17 11   JP           $1117
7A3C: 18 2A      JR           $7A68
7A3E: 19         ADD         HL,DE
7A3F: 26 23      LD           H,$23
7A41: 23         INC         HL
7A42: 82         ADD         A,D
7A43: 24         INC         H
7A44: 1B         DEC         DE
7A45: 26 24      LD           H,$24
7A47: 33         INC         SP
7A48: 27         DAA
7A49: 82         ADD         A,D
7A4A: 34         INC         (HL)
7A4B: 22         LD           (HLI),A
7A4C: 36 28      LD           (HL),$28
7A4E: 42         LD           B,D
7A4F: 87         ADD         A,A
7A50: 52         LD           D,D
7A51: CE 84      ADC         $84
7A53: 43         LD           B,E
7A54: 12         LD           (DE),A
7A55: 47         LD           B,A
7A56: 87         ADD         A,A
7A57: 57         LD           D,A
7A58: CE 60      ADC         $60
7A5A: 27         DAA
7A5B: 61         LD           H,C
7A5C: 2B         DEC         HL
7A5D: 68         LD           L,B
7A5E: 2C         INC         L
7A5F: 69         LD           L,C
7A60: 28 70      JR           Z,$7AD2
7A62: DF         RST         0X18
7A63: 71         LD           (HL),C
7A64: 27         DAA
7A65: 78         LD           A,B
7A66: 28 79      JR           Z,$7AE1
7A68: 0D         DEC         C
7A69: 74         LD           (HL),H
7A6A: FD                              
7A6B: E0 00      LDFF00   ($00),A
7A6D: 1F         RRA
7A6E: 38 50      JR           C,$7AC0
7A70: FE 0C      CP           $0C
7A72: 0D         DEC         C
7A73: 84         ADD         A,H
7A74: 11 1B 85   LD           DE,$851B
7A77: 21 1B 86   LD           HL,$861B
7A7A: 31 1B 86   LD           SP,$861B
7A7D: 41         LD           B,C
7A7E: 1B         DEC         DE
7A7F: 87         ADD         A,A
7A80: 51         LD           D,C
7A81: 1B         DEC         DE
7A82: 88         ADC         A,B
7A83: 61         LD           H,C
7A84: 1B         DEC         DE
7A85: 25         DEC         H
7A86: 0F         RRCA
7A87: 51         LD           D,C
7A88: 0E 83      LD           C,$83
7A8A: 61         LD           H,C
7A8B: 0E 15      LD           C,$15
7A8D: A0         AND         B
7A8E: 74         LD           (HL),H
7A8F: FD                              
7A90: E0 00      LDFF00   ($00),A
7A92: 38 58      JR           C,$7AEC
7A94: 30 FE      JR           NC,$7A94
7A96: 04         INC         B
7A97: 9D         SBC         L
7A98: 8A         ADC         A,D
7A99: 00         NOP
7A9A: DF         RST         0X18
7A9B: 82         ADD         A,D
7A9C: 10 DF      STOP       $DF
7A9E: 82         ADD         A,D
7A9F: 18 DF      JR           $7A80
7AA1: 82         ADD         A,D
7AA2: 20 DF      JR           NZ,$7A83
7AA4: 82         ADD         A,D
7AA5: 27         DAA
7AA6: DF         RST         0X18
7AA7: 85         ADD         A,L
7AA8: 34         INC         (HL)
7AA9: DF         RST         0X18
7AAA: C2 29 DF   JP           NZ,$DF29
7AAD: 82         ADD         A,D
7AAE: 44         LD           B,H
7AAF: DF         RST         0X18
7AB0: 82         ADD         A,D
7AB1: 54         LD           D,H
7AB2: DF         RST         0X18
7AB3: 82         ADD         A,D
7AB4: 74         LD           (HL),H
7AB5: DF         RST         0X18
7AB6: 13         INC         DE
7AB7: 25         DEC         H
7AB8: 82         ADD         A,D
7AB9: 14         INC         D
7ABA: 21 16 26   LD           HL,$2616
7ABD: 22         LD           (HLI),A
7ABE: 25         DEC         H
7ABF: 23         INC         HL
7AC0: 29         ADD         HL,HL
7AC1: 82         ADD         A,D
7AC2: 24         INC         H
7AC3: 05         DEC         B
7AC4: 26 2A      LD           H,$2A
7AC6: 27         DAA
7AC7: 26 32      LD           H,$32
7AC9: 23         INC         HL
7ACA: 84         ADD         A,H
7ACB: 33         INC         SP
7ACC: 05         DEC         B
7ACD: 37         SCF
7ACE: 24         INC         H
7ACF: 42         LD           B,D
7AD0: 27         DAA
7AD1: 43         LD           B,E
7AD2: 2B         DEC         HL
7AD3: 82         ADD         A,D
7AD4: 44         LD           B,H
7AD5: 05         DEC         B
7AD6: 46         LD           B,(HL)
7AD7: 2C         INC         L
7AD8: 47         LD           B,A
7AD9: 28 53      JR           Z,$7B2E
7ADB: 27         DAA
7ADC: 82         ADD         A,D
7ADD: 54         LD           D,H
7ADE: 22         LD           (HLI),A
7ADF: 56         LD           D,(HL)
7AE0: 28 24      JR           Z,$7B06
7AE2: A0         AND         B
7AE3: 45         LD           B,L
7AE4: CB E0      SET         1,E
7AE6: 00         NOP
7AE7: 78         LD           A,B
7AE8: 28 70      JR           Z,$7B5A
7AEA: FE 00      CP           $00
7AEC: 9D         SBC         L
7AED: 87         ADD         A,A
7AEE: 00         NOP
7AEF: DF         RST         0X18
7AF0: 05         DEC         B
7AF1: 0D         DEC         C
7AF2: C4 07 23   CALL       NZ,$2307
7AF5: C6 09      ADD         $09
7AF7: 24         INC         H
7AF8: 82         ADD         A,D
7AF9: 11 DF C3   LD           DE,$C3DF
7AFC: 14         INC         D
7AFD: 05         DEC         B
7AFE: 20 05      JR           NZ,$7B05
7B00: 25         DEC         H
7B01: DF         RST         0X18
7B02: C3 28 DF   JP           $DF28
7B05: 30 DF      JR           NC,$7AE6
7B07: 83         ADD         A,E
7B08: 40         LD           B,B
7B09: DF         RST         0X18
7B0A: 44         LD           B,H
7B0B: DF         RST         0X18
7B0C: 45         LD           B,L
7B0D: 25         DEC         H
7B0E: 46         LD           B,(HL)
7B0F: 21 47 29   LD           HL,$2947
7B12: 52         LD           D,D
7B13: 05         DEC         B
7B14: 53         LD           D,E
7B15: DF         RST         0X18
7B16: C2 55 23   JP           NZ,$2355
7B19: 82         ADD         A,D
7B1A: 57         LD           D,A
7B1B: DF         RST         0X18
7B1C: 60         LD           H,B
7B1D: DF         RST         0X18
7B1E: 64         LD           H,H
7B1F: DF         RST         0X18
7B20: 68         LD           L,B
7B21: 2C         INC         L
7B22: 69         LD           L,C
7B23: 28 83      JR           Z,$7AA8
7B25: 72         LD           (HL),D
7B26: DF         RST         0X18
7B27: 75         LD           (HL),L
7B28: 27         DAA
7B29: 78         LD           A,B
7B2A: 28 79      JR           Z,$7BA5
7B2C: DF         RST         0X18
7B2D: 76         HALT
7B2E: FD                              
7B2F: E0 00      LDFF00   ($00),A
7B31: 13         INC         DE
7B32: 58         LD           E,B
7B33: 10 FE      STOP       $FE
7B35: 05         DEC         B
7B36: 94         SUB         H
7B37: 8A         ADC         A,D
7B38: 00         NOP
7B39: 84         ADD         A,H
7B3A: 8A         ADC         A,D
7B3B: 10 84      STOP       $84
7B3D: 8A         ADC         A,D
7B3E: 20 84      JR           NZ,$7AC4
7B40: 8A         ADC         A,D
7B41: 30 84      JR           NC,$7AC7
7B43: 8A         ADC         A,D
7B44: 40         LD           B,B
7B45: 84         ADD         A,H
7B46: 8A         ADC         A,D
7B47: 50         LD           D,B
7B48: 84         ADD         A,H
7B49: 8A         ADC         A,D
7B4A: 60         LD           H,B
7B4B: 84         ADD         A,H
7B4C: 8A         ADC         A,D
7B4D: 70         LD           (HL),B
7B4E: 84         ADD         A,H
7B4F: 82         ADD         A,D
7B50: 00         NOP
7B51: 4B         LD           C,E
7B52: 82         ADD         A,D
7B53: 08 4B 10   LD           ($104B),SP
7B56: 4B         LD           C,E
7B57: 19         ADD         HL,DE
7B58: 4B         LD           C,E
7B59: 60         LD           H,B
7B5A: 72         LD           (HL),D
7B5B: 61         LD           H,C
7B5C: 73         LD           (HL),E
7B5D: 68         LD           L,B
7B5E: 74         LD           (HL),H
7B5F: 69         LD           L,C
7B60: 72         LD           (HL),D
7B61: 83         ADD         A,E
7B62: 70         LD           (HL),B
7B63: 72         LD           (HL),D
7B64: 73         LD           (HL),E
7B65: 73         LD           (HL),E
7B66: 74         LD           (HL),H
7B67: 74         LD           (HL),H
7B68: 75         LD           (HL),L
7B69: 72         LD           (HL),D
7B6A: 76         HALT
7B6B: 7E         LD           A,(HL)
7B6C: 83         ADD         A,E
7B6D: 77         LD           (HL),A
7B6E: 72         LD           (HL),D
7B6F: E1         POP         HL
7B70: 03         INC         BC
7B71: 66         LD           H,(HL)
7B72: 48         LD           C,B
7B73: 50         LD           D,B
7B74: FE FF      CP           $FF
7B76: FF         RST         0X38
7B77: FF         RST         0X38
7B78: FF         RST         0X38
7B79: FF         RST         0X38
7B7A: FF         RST         0X38
7B7B: FF         RST         0X38
7B7C: FF         RST         0X38
7B7D: FF         RST         0X38
7B7E: FF         RST         0X38
7B7F: FF         RST         0X38
7B80: FF         RST         0X38
7B81: FF         RST         0X38
7B82: FF         RST         0X38
7B83: FF         RST         0X38
7B84: FF         RST         0X38
7B85: FF         RST         0X38
7B86: FF         RST         0X38
7B87: FF         RST         0X38
7B88: FF         RST         0X38
7B89: FF         RST         0X38
7B8A: FF         RST         0X38
7B8B: FF         RST         0X38
7B8C: FF         RST         0X38
7B8D: FF         RST         0X38
7B8E: FF         RST         0X38
7B8F: FF         RST         0X38
7B90: FF         RST         0X38
7B91: FF         RST         0X38
7B92: FF         RST         0X38
7B93: FF         RST         0X38
7B94: FF         RST         0X38
7B95: FF         RST         0X38
7B96: FF         RST         0X38
7B97: FF         RST         0X38
7B98: FF         RST         0X38
7B99: FF         RST         0X38
7B9A: FF         RST         0X38
7B9B: FF         RST         0X38
7B9C: FF         RST         0X38
7B9D: FF         RST         0X38
7B9E: FF         RST         0X38
7B9F: FF         RST         0X38
7BA0: FF         RST         0X38
7BA1: FF         RST         0X38
7BA2: FF         RST         0X38
7BA3: FF         RST         0X38
7BA4: FF         RST         0X38
7BA5: FF         RST         0X38
7BA6: FF         RST         0X38
7BA7: FF         RST         0X38
7BA8: FF         RST         0X38
7BA9: FF         RST         0X38
7BAA: FF         RST         0X38
7BAB: FF         RST         0X38
7BAC: FF         RST         0X38
7BAD: FF         RST         0X38
7BAE: FF         RST         0X38
7BAF: FF         RST         0X38
7BB0: FF         RST         0X38
7BB1: FF         RST         0X38
7BB2: FF         RST         0X38
7BB3: FF         RST         0X38
7BB4: FF         RST         0X38
7BB5: FF         RST         0X38
7BB6: FF         RST         0X38
7BB7: FF         RST         0X38
7BB8: FF         RST         0X38
7BB9: FF         RST         0X38
7BBA: FF         RST         0X38
7BBB: FF         RST         0X38
7BBC: FF         RST         0X38
7BBD: FF         RST         0X38
7BBE: FF         RST         0X38
7BBF: FF         RST         0X38
7BC0: FF         RST         0X38
7BC1: FF         RST         0X38
7BC2: FF         RST         0X38
7BC3: FF         RST         0X38
7BC4: FF         RST         0X38
7BC5: FF         RST         0X38
7BC6: FF         RST         0X38
7BC7: FF         RST         0X38
7BC8: FF         RST         0X38
7BC9: FF         RST         0X38
7BCA: FF         RST         0X38
7BCB: FF         RST         0X38
7BCC: FF         RST         0X38
7BCD: FF         RST         0X38
7BCE: FF         RST         0X38
7BCF: FF         RST         0X38
7BD0: FF         RST         0X38
7BD1: FF         RST         0X38
7BD2: FF         RST         0X38
7BD3: FF         RST         0X38
7BD4: FF         RST         0X38
7BD5: FF         RST         0X38
7BD6: FF         RST         0X38
7BD7: FF         RST         0X38
7BD8: FF         RST         0X38
7BD9: FF         RST         0X38
7BDA: FF         RST         0X38
7BDB: FF         RST         0X38
7BDC: FF         RST         0X38
7BDD: FF         RST         0X38
7BDE: FF         RST         0X38
7BDF: FF         RST         0X38
7BE0: FF         RST         0X38
7BE1: FF         RST         0X38
7BE2: FF         RST         0X38
7BE3: FF         RST         0X38
7BE4: FF         RST         0X38
7BE5: FF         RST         0X38
7BE6: FF         RST         0X38
7BE7: FF         RST         0X38
7BE8: FF         RST         0X38
7BE9: FF         RST         0X38
7BEA: FF         RST         0X38
7BEB: FF         RST         0X38
7BEC: FF         RST         0X38
7BED: FF         RST         0X38
7BEE: FF         RST         0X38
7BEF: FF         RST         0X38
7BF0: FF         RST         0X38
7BF1: FF         RST         0X38
7BF2: FF         RST         0X38
7BF3: FF         RST         0X38
7BF4: FF         RST         0X38
7BF5: FF         RST         0X38
7BF6: FF         RST         0X38
7BF7: FF         RST         0X38
7BF8: FF         RST         0X38
7BF9: FF         RST         0X38
7BFA: FF         RST         0X38
7BFB: FF         RST         0X38
7BFC: FF         RST         0X38
7BFD: FF         RST         0X38
7BFE: FF         RST         0X38
7BFF: FF         RST         0X38
7C00: FF         RST         0X38
7C01: FF         RST         0X38
7C02: FF         RST         0X38
7C03: FF         RST         0X38
7C04: FF         RST         0X38
7C05: FF         RST         0X38
7C06: FF         RST         0X38
7C07: FF         RST         0X38
7C08: FF         RST         0X38
7C09: FF         RST         0X38
7C0A: FF         RST         0X38
7C0B: FF         RST         0X38
7C0C: FF         RST         0X38
7C0D: FF         RST         0X38
7C0E: FF         RST         0X38
7C0F: FF         RST         0X38
7C10: FF         RST         0X38
7C11: FF         RST         0X38
7C12: FF         RST         0X38
7C13: FF         RST         0X38
7C14: FF         RST         0X38
7C15: FF         RST         0X38
7C16: FF         RST         0X38
7C17: FF         RST         0X38
7C18: FF         RST         0X38
7C19: FF         RST         0X38
7C1A: FF         RST         0X38
7C1B: FF         RST         0X38
7C1C: FF         RST         0X38
7C1D: FF         RST         0X38
7C1E: FF         RST         0X38
7C1F: FF         RST         0X38
7C20: FF         RST         0X38
7C21: FF         RST         0X38
7C22: FF         RST         0X38
7C23: FF         RST         0X38
7C24: FF         RST         0X38
7C25: FF         RST         0X38
7C26: FF         RST         0X38
7C27: FF         RST         0X38
7C28: FF         RST         0X38
7C29: FF         RST         0X38
7C2A: FF         RST         0X38
7C2B: FF         RST         0X38
7C2C: FF         RST         0X38
7C2D: FF         RST         0X38
7C2E: FF         RST         0X38
7C2F: FF         RST         0X38
7C30: FF         RST         0X38
7C31: FF         RST         0X38
7C32: FF         RST         0X38
7C33: FF         RST         0X38
7C34: FF         RST         0X38
7C35: FF         RST         0X38
7C36: FF         RST         0X38
7C37: FF         RST         0X38
7C38: FF         RST         0X38
7C39: FF         RST         0X38
7C3A: FF         RST         0X38
7C3B: FF         RST         0X38
7C3C: FF         RST         0X38
7C3D: FF         RST         0X38
7C3E: FF         RST         0X38
7C3F: FF         RST         0X38
7C40: FF         RST         0X38
7C41: FF         RST         0X38
7C42: FF         RST         0X38
7C43: FF         RST         0X38
7C44: FF         RST         0X38
7C45: FF         RST         0X38
7C46: FF         RST         0X38
7C47: FF         RST         0X38
7C48: FF         RST         0X38
7C49: FF         RST         0X38
7C4A: FF         RST         0X38
7C4B: FF         RST         0X38
7C4C: FF         RST         0X38
7C4D: FF         RST         0X38
7C4E: FF         RST         0X38
7C4F: FF         RST         0X38
7C50: FF         RST         0X38
7C51: FF         RST         0X38
7C52: FF         RST         0X38
7C53: FF         RST         0X38
7C54: FF         RST         0X38
7C55: FF         RST         0X38
7C56: FF         RST         0X38
7C57: FF         RST         0X38
7C58: FF         RST         0X38
7C59: FF         RST         0X38
7C5A: FF         RST         0X38
7C5B: FF         RST         0X38
7C5C: FF         RST         0X38
7C5D: FF         RST         0X38
7C5E: FF         RST         0X38
7C5F: FF         RST         0X38
7C60: FF         RST         0X38
7C61: FF         RST         0X38
7C62: FF         RST         0X38
7C63: FF         RST         0X38
7C64: FF         RST         0X38
7C65: FF         RST         0X38
7C66: FF         RST         0X38
7C67: FF         RST         0X38
7C68: FF         RST         0X38
7C69: FF         RST         0X38
7C6A: FF         RST         0X38
7C6B: FF         RST         0X38
7C6C: FF         RST         0X38
7C6D: FF         RST         0X38
7C6E: FF         RST         0X38
7C6F: FF         RST         0X38
7C70: FF         RST         0X38
7C71: FF         RST         0X38
7C72: FF         RST         0X38
7C73: FF         RST         0X38
7C74: FF         RST         0X38
7C75: FF         RST         0X38
7C76: FF         RST         0X38
7C77: FF         RST         0X38
7C78: FF         RST         0X38
7C79: FF         RST         0X38
7C7A: FF         RST         0X38
7C7B: FF         RST         0X38
7C7C: FF         RST         0X38
7C7D: FF         RST         0X38
7C7E: FF         RST         0X38
7C7F: FF         RST         0X38
7C80: FF         RST         0X38
7C81: FF         RST         0X38
7C82: FF         RST         0X38
7C83: FF         RST         0X38
7C84: FF         RST         0X38
7C85: FF         RST         0X38
7C86: FF         RST         0X38
7C87: FF         RST         0X38
7C88: FF         RST         0X38
7C89: FF         RST         0X38
7C8A: FF         RST         0X38
7C8B: FF         RST         0X38
7C8C: FF         RST         0X38
7C8D: FF         RST         0X38
7C8E: FF         RST         0X38
7C8F: FF         RST         0X38
7C90: FF         RST         0X38
7C91: FF         RST         0X38
7C92: FF         RST         0X38
7C93: FF         RST         0X38
7C94: FF         RST         0X38
7C95: FF         RST         0X38
7C96: FF         RST         0X38
7C97: FF         RST         0X38
7C98: FF         RST         0X38
7C99: FF         RST         0X38
7C9A: FF         RST         0X38
7C9B: FF         RST         0X38
7C9C: FF         RST         0X38
7C9D: FF         RST         0X38
7C9E: FF         RST         0X38
7C9F: FF         RST         0X38
7CA0: FF         RST         0X38
7CA1: FF         RST         0X38
7CA2: FF         RST         0X38
7CA3: FF         RST         0X38
7CA4: FF         RST         0X38
7CA5: FF         RST         0X38
7CA6: FF         RST         0X38
7CA7: FF         RST         0X38
7CA8: FF         RST         0X38
7CA9: FF         RST         0X38
7CAA: FF         RST         0X38
7CAB: FF         RST         0X38
7CAC: FF         RST         0X38
7CAD: FF         RST         0X38
7CAE: FF         RST         0X38
7CAF: FF         RST         0X38
7CB0: FF         RST         0X38
7CB1: FF         RST         0X38
7CB2: FF         RST         0X38
7CB3: FF         RST         0X38
7CB4: FF         RST         0X38
7CB5: FF         RST         0X38
7CB6: FF         RST         0X38
7CB7: FF         RST         0X38
7CB8: FF         RST         0X38
7CB9: FF         RST         0X38
7CBA: FF         RST         0X38
7CBB: FF         RST         0X38
7CBC: FF         RST         0X38
7CBD: FF         RST         0X38
7CBE: FF         RST         0X38
7CBF: FF         RST         0X38
7CC0: FF         RST         0X38
7CC1: FF         RST         0X38
7CC2: FF         RST         0X38
7CC3: FF         RST         0X38
7CC4: FF         RST         0X38
7CC5: FF         RST         0X38
7CC6: FF         RST         0X38
7CC7: FF         RST         0X38
7CC8: FF         RST         0X38
7CC9: FF         RST         0X38
7CCA: FF         RST         0X38
7CCB: FF         RST         0X38
7CCC: FF         RST         0X38
7CCD: FF         RST         0X38
7CCE: FF         RST         0X38
7CCF: FF         RST         0X38
7CD0: FF         RST         0X38
7CD1: FF         RST         0X38
7CD2: FF         RST         0X38
7CD3: FF         RST         0X38
7CD4: FF         RST         0X38
7CD5: FF         RST         0X38
7CD6: FF         RST         0X38
7CD7: FF         RST         0X38
7CD8: FF         RST         0X38
7CD9: FF         RST         0X38
7CDA: FF         RST         0X38
7CDB: FF         RST         0X38
7CDC: FF         RST         0X38
7CDD: FF         RST         0X38
7CDE: FF         RST         0X38
7CDF: FF         RST         0X38
7CE0: FF         RST         0X38
7CE1: FF         RST         0X38
7CE2: FF         RST         0X38
7CE3: FF         RST         0X38
7CE4: FF         RST         0X38
7CE5: FF         RST         0X38
7CE6: FF         RST         0X38
7CE7: FF         RST         0X38
7CE8: FF         RST         0X38
7CE9: FF         RST         0X38
7CEA: FF         RST         0X38
7CEB: FF         RST         0X38
7CEC: FF         RST         0X38
7CED: FF         RST         0X38
7CEE: FF         RST         0X38
7CEF: FF         RST         0X38
7CF0: FF         RST         0X38
7CF1: FF         RST         0X38
7CF2: FF         RST         0X38
7CF3: FF         RST         0X38
7CF4: FF         RST         0X38
7CF5: FF         RST         0X38
7CF6: FF         RST         0X38
7CF7: FF         RST         0X38
7CF8: FF         RST         0X38
7CF9: FF         RST         0X38
7CFA: FF         RST         0X38
7CFB: FF         RST         0X38
7CFC: FF         RST         0X38
7CFD: FF         RST         0X38
7CFE: FF         RST         0X38
7CFF: FF         RST         0X38
7D00: FF         RST         0X38
7D01: FF         RST         0X38
7D02: FF         RST         0X38
7D03: FF         RST         0X38
7D04: FF         RST         0X38
7D05: FF         RST         0X38
7D06: FF         RST         0X38
7D07: FF         RST         0X38
7D08: FF         RST         0X38
7D09: FF         RST         0X38
7D0A: FF         RST         0X38
7D0B: FF         RST         0X38
7D0C: FF         RST         0X38
7D0D: FF         RST         0X38
7D0E: FF         RST         0X38
7D0F: FF         RST         0X38
7D10: FF         RST         0X38
7D11: FF         RST         0X38
7D12: FF         RST         0X38
7D13: FF         RST         0X38
7D14: FF         RST         0X38
7D15: FF         RST         0X38
7D16: FF         RST         0X38
7D17: FF         RST         0X38
7D18: FF         RST         0X38
7D19: FF         RST         0X38
7D1A: FF         RST         0X38
7D1B: FF         RST         0X38
7D1C: FF         RST         0X38
7D1D: FF         RST         0X38
7D1E: FF         RST         0X38
7D1F: FF         RST         0X38
7D20: FF         RST         0X38
7D21: FF         RST         0X38
7D22: FF         RST         0X38
7D23: FF         RST         0X38
7D24: FF         RST         0X38
7D25: FF         RST         0X38
7D26: FF         RST         0X38
7D27: FF         RST         0X38
7D28: FF         RST         0X38
7D29: FF         RST         0X38
7D2A: FF         RST         0X38
7D2B: FF         RST         0X38
7D2C: FF         RST         0X38
7D2D: FF         RST         0X38
7D2E: FF         RST         0X38
7D2F: FF         RST         0X38
7D30: FF         RST         0X38
7D31: FF         RST         0X38
7D32: FF         RST         0X38
7D33: FF         RST         0X38
7D34: FF         RST         0X38
7D35: FF         RST         0X38
7D36: FF         RST         0X38
7D37: FF         RST         0X38
7D38: FF         RST         0X38
7D39: FF         RST         0X38
7D3A: FF         RST         0X38
7D3B: FF         RST         0X38
7D3C: FF         RST         0X38
7D3D: FF         RST         0X38
7D3E: FF         RST         0X38
7D3F: FF         RST         0X38
7D40: FF         RST         0X38
7D41: FF         RST         0X38
7D42: FF         RST         0X38
7D43: FF         RST         0X38
7D44: FF         RST         0X38
7D45: FF         RST         0X38
7D46: FF         RST         0X38
7D47: FF         RST         0X38
7D48: FF         RST         0X38
7D49: FF         RST         0X38
7D4A: FF         RST         0X38
7D4B: FF         RST         0X38
7D4C: FF         RST         0X38
7D4D: FF         RST         0X38
7D4E: FF         RST         0X38
7D4F: FF         RST         0X38
7D50: FF         RST         0X38
7D51: FF         RST         0X38
7D52: FF         RST         0X38
7D53: FF         RST         0X38
7D54: FF         RST         0X38
7D55: FF         RST         0X38
7D56: FF         RST         0X38
7D57: FF         RST         0X38
7D58: FF         RST         0X38
7D59: FF         RST         0X38
7D5A: FF         RST         0X38
7D5B: FF         RST         0X38
7D5C: FF         RST         0X38
7D5D: FF         RST         0X38
7D5E: FF         RST         0X38
7D5F: FF         RST         0X38
7D60: FF         RST         0X38
7D61: FF         RST         0X38
7D62: FF         RST         0X38
7D63: FF         RST         0X38
7D64: FF         RST         0X38
7D65: FF         RST         0X38
7D66: FF         RST         0X38
7D67: FF         RST         0X38
7D68: FF         RST         0X38
7D69: FF         RST         0X38
7D6A: FF         RST         0X38
7D6B: FF         RST         0X38
7D6C: FF         RST         0X38
7D6D: FF         RST         0X38
7D6E: FF         RST         0X38
7D6F: FF         RST         0X38
7D70: FF         RST         0X38
7D71: FF         RST         0X38
7D72: FF         RST         0X38
7D73: FF         RST         0X38
7D74: FF         RST         0X38
7D75: FF         RST         0X38
7D76: FF         RST         0X38
7D77: FF         RST         0X38
7D78: FF         RST         0X38
7D79: FF         RST         0X38
7D7A: FF         RST         0X38
7D7B: FF         RST         0X38
7D7C: FF         RST         0X38
7D7D: FF         RST         0X38
7D7E: FF         RST         0X38
7D7F: FF         RST         0X38
7D80: FF         RST         0X38
7D81: FF         RST         0X38
7D82: FF         RST         0X38
7D83: FF         RST         0X38
7D84: FF         RST         0X38
7D85: FF         RST         0X38
7D86: FF         RST         0X38
7D87: FF         RST         0X38
7D88: FF         RST         0X38
7D89: FF         RST         0X38
7D8A: FF         RST         0X38
7D8B: FF         RST         0X38
7D8C: FF         RST         0X38
7D8D: FF         RST         0X38
7D8E: FF         RST         0X38
7D8F: FF         RST         0X38
7D90: FF         RST         0X38
7D91: FF         RST         0X38
7D92: FF         RST         0X38
7D93: FF         RST         0X38
7D94: FF         RST         0X38
7D95: FF         RST         0X38
7D96: FF         RST         0X38
7D97: FF         RST         0X38
7D98: FF         RST         0X38
7D99: FF         RST         0X38
7D9A: FF         RST         0X38
7D9B: FF         RST         0X38
7D9C: FF         RST         0X38
7D9D: FF         RST         0X38
7D9E: FF         RST         0X38
7D9F: FF         RST         0X38
7DA0: FF         RST         0X38
7DA1: FF         RST         0X38
7DA2: FF         RST         0X38
7DA3: FF         RST         0X38
7DA4: FF         RST         0X38
7DA5: FF         RST         0X38
7DA6: FF         RST         0X38
7DA7: FF         RST         0X38
7DA8: FF         RST         0X38
7DA9: FF         RST         0X38
7DAA: FF         RST         0X38
7DAB: FF         RST         0X38
7DAC: FF         RST         0X38
7DAD: FF         RST         0X38
7DAE: FF         RST         0X38
7DAF: FF         RST         0X38
7DB0: FF         RST         0X38
7DB1: FF         RST         0X38
7DB2: FF         RST         0X38
7DB3: FF         RST         0X38
7DB4: FF         RST         0X38
7DB5: FF         RST         0X38
7DB6: FF         RST         0X38
7DB7: FF         RST         0X38
7DB8: FF         RST         0X38
7DB9: FF         RST         0X38
7DBA: FF         RST         0X38
7DBB: FF         RST         0X38
7DBC: FF         RST         0X38
7DBD: FF         RST         0X38
7DBE: FF         RST         0X38
7DBF: FF         RST         0X38
7DC0: FF         RST         0X38
7DC1: FF         RST         0X38
7DC2: FF         RST         0X38
7DC3: FF         RST         0X38
7DC4: FF         RST         0X38
7DC5: FF         RST         0X38
7DC6: FF         RST         0X38
7DC7: FF         RST         0X38
7DC8: FF         RST         0X38
7DC9: FF         RST         0X38
7DCA: FF         RST         0X38
7DCB: FF         RST         0X38
7DCC: FF         RST         0X38
7DCD: FF         RST         0X38
7DCE: FF         RST         0X38
7DCF: FF         RST         0X38
7DD0: FF         RST         0X38
7DD1: FF         RST         0X38
7DD2: FF         RST         0X38
7DD3: FF         RST         0X38
7DD4: FF         RST         0X38
7DD5: FF         RST         0X38
7DD6: FF         RST         0X38
7DD7: FF         RST         0X38
7DD8: FF         RST         0X38
7DD9: FF         RST         0X38
7DDA: FF         RST         0X38
7DDB: FF         RST         0X38
7DDC: FF         RST         0X38
7DDD: FF         RST         0X38
7DDE: FF         RST         0X38
7DDF: FF         RST         0X38
7DE0: FF         RST         0X38
7DE1: FF         RST         0X38
7DE2: FF         RST         0X38
7DE3: FF         RST         0X38
7DE4: FF         RST         0X38
7DE5: FF         RST         0X38
7DE6: FF         RST         0X38
7DE7: FF         RST         0X38
7DE8: FF         RST         0X38
7DE9: FF         RST         0X38
7DEA: FF         RST         0X38
7DEB: FF         RST         0X38
7DEC: FF         RST         0X38
7DED: FF         RST         0X38
7DEE: FF         RST         0X38
7DEF: FF         RST         0X38
7DF0: FF         RST         0X38
7DF1: FF         RST         0X38
7DF2: FF         RST         0X38
7DF3: FF         RST         0X38
7DF4: FF         RST         0X38
7DF5: FF         RST         0X38
7DF6: FF         RST         0X38
7DF7: FF         RST         0X38
7DF8: FF         RST         0X38
7DF9: FF         RST         0X38
7DFA: FF         RST         0X38
7DFB: FF         RST         0X38
7DFC: FF         RST         0X38
7DFD: FF         RST         0X38
7DFE: FF         RST         0X38
7DFF: FF         RST         0X38
7E00: FF         RST         0X38
7E01: FF         RST         0X38
7E02: FF         RST         0X38
7E03: FF         RST         0X38
7E04: FF         RST         0X38
7E05: FF         RST         0X38
7E06: FF         RST         0X38
7E07: FF         RST         0X38
7E08: FF         RST         0X38
7E09: FF         RST         0X38
7E0A: FF         RST         0X38
7E0B: FF         RST         0X38
7E0C: FF         RST         0X38
7E0D: FF         RST         0X38
7E0E: FF         RST         0X38
7E0F: FF         RST         0X38
7E10: FF         RST         0X38
7E11: FF         RST         0X38
7E12: FF         RST         0X38
7E13: FF         RST         0X38
7E14: FF         RST         0X38
7E15: FF         RST         0X38
7E16: FF         RST         0X38
7E17: FF         RST         0X38
7E18: FF         RST         0X38
7E19: FF         RST         0X38
7E1A: FF         RST         0X38
7E1B: FF         RST         0X38
7E1C: FF         RST         0X38
7E1D: FF         RST         0X38
7E1E: FF         RST         0X38
7E1F: FF         RST         0X38
7E20: FF         RST         0X38
7E21: FF         RST         0X38
7E22: FF         RST         0X38
7E23: FF         RST         0X38
7E24: FF         RST         0X38
7E25: FF         RST         0X38
7E26: FF         RST         0X38
7E27: FF         RST         0X38
7E28: FF         RST         0X38
7E29: FF         RST         0X38
7E2A: FF         RST         0X38
7E2B: FF         RST         0X38
7E2C: FF         RST         0X38
7E2D: FF         RST         0X38
7E2E: FF         RST         0X38
7E2F: FF         RST         0X38
7E30: FF         RST         0X38
7E31: FF         RST         0X38
7E32: FF         RST         0X38
7E33: FF         RST         0X38
7E34: FF         RST         0X38
7E35: FF         RST         0X38
7E36: FF         RST         0X38
7E37: FF         RST         0X38
7E38: FF         RST         0X38
7E39: FF         RST         0X38
7E3A: FF         RST         0X38
7E3B: FF         RST         0X38
7E3C: FF         RST         0X38
7E3D: FF         RST         0X38
7E3E: FF         RST         0X38
7E3F: FF         RST         0X38
7E40: FF         RST         0X38
7E41: FF         RST         0X38
7E42: FF         RST         0X38
7E43: FF         RST         0X38
7E44: FF         RST         0X38
7E45: FF         RST         0X38
7E46: FF         RST         0X38
7E47: FF         RST         0X38
7E48: FF         RST         0X38
7E49: FF         RST         0X38
7E4A: FF         RST         0X38
7E4B: FF         RST         0X38
7E4C: FF         RST         0X38
7E4D: FF         RST         0X38
7E4E: FF         RST         0X38
7E4F: FF         RST         0X38
7E50: FF         RST         0X38
7E51: FF         RST         0X38
7E52: FF         RST         0X38
7E53: FF         RST         0X38
7E54: FF         RST         0X38
7E55: FF         RST         0X38
7E56: FF         RST         0X38
7E57: FF         RST         0X38
7E58: FF         RST         0X38
7E59: FF         RST         0X38
7E5A: FF         RST         0X38
7E5B: FF         RST         0X38
7E5C: FF         RST         0X38
7E5D: FF         RST         0X38
7E5E: FF         RST         0X38
7E5F: FF         RST         0X38
7E60: FF         RST         0X38
7E61: FF         RST         0X38
7E62: FF         RST         0X38
7E63: FF         RST         0X38
7E64: FF         RST         0X38
7E65: FF         RST         0X38
7E66: FF         RST         0X38
7E67: FF         RST         0X38
7E68: FF         RST         0X38
7E69: FF         RST         0X38
7E6A: FF         RST         0X38
7E6B: FF         RST         0X38
7E6C: FF         RST         0X38
7E6D: FF         RST         0X38
7E6E: FF         RST         0X38
7E6F: FF         RST         0X38
7E70: FF         RST         0X38
7E71: FF         RST         0X38
7E72: FF         RST         0X38
7E73: FF         RST         0X38
7E74: FF         RST         0X38
7E75: FF         RST         0X38
7E76: FF         RST         0X38
7E77: FF         RST         0X38
7E78: FF         RST         0X38
7E79: FF         RST         0X38
7E7A: FF         RST         0X38
7E7B: FF         RST         0X38
7E7C: FF         RST         0X38
7E7D: FF         RST         0X38
7E7E: FF         RST         0X38
7E7F: FF         RST         0X38
7E80: FF         RST         0X38
7E81: FF         RST         0X38
7E82: FF         RST         0X38
7E83: FF         RST         0X38
7E84: FF         RST         0X38
7E85: FF         RST         0X38
7E86: FF         RST         0X38
7E87: FF         RST         0X38
7E88: FF         RST         0X38
7E89: FF         RST         0X38
7E8A: FF         RST         0X38
7E8B: FF         RST         0X38
7E8C: FF         RST         0X38
7E8D: FF         RST         0X38
7E8E: FF         RST         0X38
7E8F: FF         RST         0X38
7E90: FF         RST         0X38
7E91: FF         RST         0X38
7E92: FF         RST         0X38
7E93: FF         RST         0X38
7E94: FF         RST         0X38
7E95: FF         RST         0X38
7E96: FF         RST         0X38
7E97: FF         RST         0X38
7E98: FF         RST         0X38
7E99: FF         RST         0X38
7E9A: FF         RST         0X38
7E9B: FF         RST         0X38
7E9C: FF         RST         0X38
7E9D: FF         RST         0X38
7E9E: FF         RST         0X38
7E9F: FF         RST         0X38
7EA0: FF         RST         0X38
7EA1: FF         RST         0X38
7EA2: FF         RST         0X38
7EA3: FF         RST         0X38
7EA4: FF         RST         0X38
7EA5: FF         RST         0X38
7EA6: FF         RST         0X38
7EA7: FF         RST         0X38
7EA8: FF         RST         0X38
7EA9: FF         RST         0X38
7EAA: FF         RST         0X38
7EAB: FF         RST         0X38
7EAC: FF         RST         0X38
7EAD: FF         RST         0X38
7EAE: FF         RST         0X38
7EAF: FF         RST         0X38
7EB0: FF         RST         0X38
7EB1: FF         RST         0X38
7EB2: FF         RST         0X38
7EB3: FF         RST         0X38
7EB4: FF         RST         0X38
7EB5: FF         RST         0X38
7EB6: FF         RST         0X38
7EB7: FF         RST         0X38
7EB8: FF         RST         0X38
7EB9: FF         RST         0X38
7EBA: FF         RST         0X38
7EBB: FF         RST         0X38
7EBC: FF         RST         0X38
7EBD: FF         RST         0X38
7EBE: FF         RST         0X38
7EBF: FF         RST         0X38
7EC0: FF         RST         0X38
7EC1: FF         RST         0X38
7EC2: FF         RST         0X38
7EC3: FF         RST         0X38
7EC4: FF         RST         0X38
7EC5: FF         RST         0X38
7EC6: FF         RST         0X38
7EC7: FF         RST         0X38
7EC8: FF         RST         0X38
7EC9: FF         RST         0X38
7ECA: FF         RST         0X38
7ECB: FF         RST         0X38
7ECC: FF         RST         0X38
7ECD: FF         RST         0X38
7ECE: FF         RST         0X38
7ECF: FF         RST         0X38
7ED0: FF         RST         0X38
7ED1: FF         RST         0X38
7ED2: FF         RST         0X38
7ED3: FF         RST         0X38
7ED4: FF         RST         0X38
7ED5: FF         RST         0X38
7ED6: FF         RST         0X38
7ED7: FF         RST         0X38
7ED8: FF         RST         0X38
7ED9: FF         RST         0X38
7EDA: FF         RST         0X38
7EDB: FF         RST         0X38
7EDC: FF         RST         0X38
7EDD: FF         RST         0X38
7EDE: FF         RST         0X38
7EDF: FF         RST         0X38
7EE0: FF         RST         0X38
7EE1: FF         RST         0X38
7EE2: FF         RST         0X38
7EE3: FF         RST         0X38
7EE4: FF         RST         0X38
7EE5: FF         RST         0X38
7EE6: FF         RST         0X38
7EE7: FF         RST         0X38
7EE8: FF         RST         0X38
7EE9: FF         RST         0X38
7EEA: FF         RST         0X38
7EEB: FF         RST         0X38
7EEC: FF         RST         0X38
7EED: FF         RST         0X38
7EEE: FF         RST         0X38
7EEF: FF         RST         0X38
7EF0: FF         RST         0X38
7EF1: FF         RST         0X38
7EF2: FF         RST         0X38
7EF3: FF         RST         0X38
7EF4: FF         RST         0X38
7EF5: FF         RST         0X38
7EF6: FF         RST         0X38
7EF7: FF         RST         0X38
7EF8: FF         RST         0X38
7EF9: FF         RST         0X38
7EFA: FF         RST         0X38
7EFB: FF         RST         0X38
7EFC: FF         RST         0X38
7EFD: FF         RST         0X38
7EFE: FF         RST         0X38
7EFF: FF         RST         0X38
7F00: FF         RST         0X38
7F01: FF         RST         0X38
7F02: FF         RST         0X38
7F03: FF         RST         0X38
7F04: FF         RST         0X38
7F05: FF         RST         0X38
7F06: FF         RST         0X38
7F07: FF         RST         0X38
7F08: FF         RST         0X38
7F09: FF         RST         0X38
7F0A: FF         RST         0X38
7F0B: FF         RST         0X38
7F0C: FF         RST         0X38
7F0D: FF         RST         0X38
7F0E: FF         RST         0X38
7F0F: FF         RST         0X38
7F10: FF         RST         0X38
7F11: FF         RST         0X38
7F12: FF         RST         0X38
7F13: FF         RST         0X38
7F14: FF         RST         0X38
7F15: FF         RST         0X38
7F16: FF         RST         0X38
7F17: FF         RST         0X38
7F18: FF         RST         0X38
7F19: FF         RST         0X38
7F1A: FF         RST         0X38
7F1B: FF         RST         0X38
7F1C: FF         RST         0X38
7F1D: FF         RST         0X38
7F1E: FF         RST         0X38
7F1F: FF         RST         0X38
7F20: FF         RST         0X38
7F21: FF         RST         0X38
7F22: FF         RST         0X38
7F23: FF         RST         0X38
7F24: FF         RST         0X38
7F25: FF         RST         0X38
7F26: FF         RST         0X38
7F27: FF         RST         0X38
7F28: FF         RST         0X38
7F29: FF         RST         0X38
7F2A: FF         RST         0X38
7F2B: FF         RST         0X38
7F2C: FF         RST         0X38
7F2D: FF         RST         0X38
7F2E: FF         RST         0X38
7F2F: FF         RST         0X38
7F30: FF         RST         0X38
7F31: FF         RST         0X38
7F32: FF         RST         0X38
7F33: FF         RST         0X38
7F34: FF         RST         0X38
7F35: FF         RST         0X38
7F36: FF         RST         0X38
7F37: FF         RST         0X38
7F38: FF         RST         0X38
7F39: FF         RST         0X38
7F3A: FF         RST         0X38
7F3B: FF         RST         0X38
7F3C: FF         RST         0X38
7F3D: FF         RST         0X38
7F3E: FF         RST         0X38
7F3F: FF         RST         0X38
7F40: FF         RST         0X38
7F41: FF         RST         0X38
7F42: FF         RST         0X38
7F43: FF         RST         0X38
7F44: FF         RST         0X38
7F45: FF         RST         0X38
7F46: FF         RST         0X38
7F47: FF         RST         0X38
7F48: FF         RST         0X38
7F49: FF         RST         0X38
7F4A: FF         RST         0X38
7F4B: FF         RST         0X38
7F4C: FF         RST         0X38
7F4D: FF         RST         0X38
7F4E: FF         RST         0X38
7F4F: FF         RST         0X38
7F50: FF         RST         0X38
7F51: FF         RST         0X38
7F52: FF         RST         0X38
7F53: FF         RST         0X38
7F54: FF         RST         0X38
7F55: FF         RST         0X38
7F56: FF         RST         0X38
7F57: FF         RST         0X38
7F58: FF         RST         0X38
7F59: FF         RST         0X38
7F5A: FF         RST         0X38
7F5B: FF         RST         0X38
7F5C: FF         RST         0X38
7F5D: FF         RST         0X38
7F5E: FF         RST         0X38
7F5F: FF         RST         0X38
7F60: FF         RST         0X38
7F61: FF         RST         0X38
7F62: FF         RST         0X38
7F63: FF         RST         0X38
7F64: FF         RST         0X38
7F65: FF         RST         0X38
7F66: FF         RST         0X38
7F67: FF         RST         0X38
7F68: FF         RST         0X38
7F69: FF         RST         0X38
7F6A: FF         RST         0X38
7F6B: FF         RST         0X38
7F6C: FF         RST         0X38
7F6D: FF         RST         0X38
7F6E: FF         RST         0X38
7F6F: FF         RST         0X38
7F70: FF         RST         0X38
7F71: FF         RST         0X38
7F72: FF         RST         0X38
7F73: FF         RST         0X38
7F74: FF         RST         0X38
7F75: FF         RST         0X38
7F76: FF         RST         0X38
7F77: FF         RST         0X38
7F78: FF         RST         0X38
7F79: FF         RST         0X38
7F7A: FF         RST         0X38
7F7B: FF         RST         0X38
7F7C: FF         RST         0X38
7F7D: FF         RST         0X38
7F7E: FF         RST         0X38
7F7F: FF         RST         0X38
7F80: FF         RST         0X38
7F81: FF         RST         0X38
7F82: FF         RST         0X38
7F83: FF         RST         0X38
7F84: FF         RST         0X38
7F85: FF         RST         0X38
7F86: FF         RST         0X38
7F87: FF         RST         0X38
7F88: FF         RST         0X38
7F89: FF         RST         0X38
7F8A: FF         RST         0X38
7F8B: FF         RST         0X38
7F8C: FF         RST         0X38
7F8D: FF         RST         0X38
7F8E: FF         RST         0X38
7F8F: FF         RST         0X38
7F90: FF         RST         0X38
7F91: FF         RST         0X38
7F92: FF         RST         0X38
7F93: FF         RST         0X38
7F94: FF         RST         0X38
7F95: FF         RST         0X38
7F96: FF         RST         0X38
7F97: FF         RST         0X38
7F98: FF         RST         0X38
7F99: FF         RST         0X38
7F9A: FF         RST         0X38
7F9B: FF         RST         0X38
7F9C: FF         RST         0X38
7F9D: FF         RST         0X38
7F9E: FF         RST         0X38
7F9F: FF         RST         0X38
7FA0: FF         RST         0X38
7FA1: FF         RST         0X38
7FA2: FF         RST         0X38
7FA3: FF         RST         0X38
7FA4: FF         RST         0X38
7FA5: FF         RST         0X38
7FA6: FF         RST         0X38
7FA7: FF         RST         0X38
7FA8: FF         RST         0X38
7FA9: FF         RST         0X38
7FAA: FF         RST         0X38
7FAB: FF         RST         0X38
7FAC: FF         RST         0X38
7FAD: FF         RST         0X38
7FAE: FF         RST         0X38
7FAF: FF         RST         0X38
7FB0: FF         RST         0X38
7FB1: FF         RST         0X38
7FB2: FF         RST         0X38
7FB3: FF         RST         0X38
7FB4: FF         RST         0X38
7FB5: FF         RST         0X38
7FB6: FF         RST         0X38
7FB7: FF         RST         0X38
7FB8: FF         RST         0X38
7FB9: FF         RST         0X38
7FBA: FF         RST         0X38
7FBB: FF         RST         0X38
7FBC: FF         RST         0X38
7FBD: FF         RST         0X38
7FBE: FF         RST         0X38
7FBF: FF         RST         0X38
7FC0: FF         RST         0X38
7FC1: FF         RST         0X38
7FC2: FF         RST         0X38
7FC3: FF         RST         0X38
7FC4: FF         RST         0X38
7FC5: FF         RST         0X38
7FC6: FF         RST         0X38
7FC7: FF         RST         0X38
7FC8: FF         RST         0X38
7FC9: FF         RST         0X38
7FCA: FF         RST         0X38
7FCB: FF         RST         0X38
7FCC: FF         RST         0X38
7FCD: FF         RST         0X38
7FCE: FF         RST         0X38
7FCF: FF         RST         0X38
7FD0: FF         RST         0X38
7FD1: FF         RST         0X38
7FD2: FF         RST         0X38
7FD3: FF         RST         0X38
7FD4: FF         RST         0X38
7FD5: FF         RST         0X38
7FD6: FF         RST         0X38
7FD7: FF         RST         0X38
7FD8: FF         RST         0X38
7FD9: FF         RST         0X38
7FDA: FF         RST         0X38
7FDB: FF         RST         0X38
7FDC: FF         RST         0X38
7FDD: FF         RST         0X38
7FDE: FF         RST         0X38
7FDF: FF         RST         0X38
7FE0: FF         RST         0X38
7FE1: FF         RST         0X38
7FE2: FF         RST         0X38
7FE3: FF         RST         0X38
7FE4: FF         RST         0X38
7FE5: FF         RST         0X38
7FE6: FF         RST         0X38
7FE7: FF         RST         0X38
7FE8: FF         RST         0X38
7FE9: FF         RST         0X38
7FEA: FF         RST         0X38
7FEB: FF         RST         0X38
7FEC: FF         RST         0X38
7FED: FF         RST         0X38
7FEE: FF         RST         0X38
7FEF: FF         RST         0X38
7FF0: FF         RST         0X38
7FF1: FF         RST         0X38
7FF2: FF         RST         0X38
7FF3: FF         RST         0X38
7FF4: FF         RST         0X38
7FF5: FF         RST         0X38
7FF6: FF         RST         0X38
7FF7: FF         RST         0X38
7FF8: FF         RST         0X38
7FF9: FF         RST         0X38
7FFA: FF         RST         0X38
7FFB: FF         RST         0X38
7FFC: FF         RST         0X38
7FFD: FF         RST         0X38
7FFE: FF         RST         0X38
7FFF: FF         RST         0X38
```
